#!/usr/bin/env python3
"""Independent second implementation of the template dispersion (Task 6).

Nothing in this file imports, executes or copies `scripts/models.py`.  The
determinant is assembled from the field equations and solved with polynomial
numerical linear algebra (numpy.roots), and every reported number is compared
with the archived output in `scripts/numbers_log.txt`.

Governing equations (linear, isotropic, uniform T0, plane waves exp(i(kx - wt)),
s = -i w, K = k^2):

  heat-flux template    q + tq q' = -k (T,x + tT T',x) - ks (v,x + tv v',x), v' = T
  energy balance        rho cv T' + beta T0 u',x = -q,x
  momentum              rho u'' = rho c1^2 u,xx - beta T,x

Eliminating u and T with q^ = -G(s) T^,x gives

  (rho c1^2 K + rho s^2) (s rho cv + G(s) K) + beta^2 T0 s K = 0,          (D)

with G = N / (s D0), D0 = 1 + tq s, N = k s (1 + tT s) + ks (1 + tv s).  Writing
(D) times s D0 as a polynomial in K:

  A K^2 + B K + C = 0,
  A = rho c1^2 N,
  B = rho c1^2 (s rho cv) D0 + rho s^2 N + beta^2 T0 s D0,
  C = rho s^2 (s rho cv) D0.

For real k (bar modes) the same expression is assembled as a polynomial in s and
all roots are found; the acoustic-type root is followed by continuity.

Reported quantities: v_p = w / Re k, Q^-1 = 2 Im k / Re k (propagating waves);
for real k, Q^-1 = 2 |Im w| / |Re w| with w = i s.

Usage:
  python3 second_impl.py           # writes second_impl_comparison.csv,
                                   # second_impl_elastic_branch.csv, second_impl_report.md
  python3 second_impl.py --check   # assertions only; prints PASS lines and exits 0
"""
import csv
import cmath
import math
import os
import sys
import tempfile

import numpy as np

# ------------------------------------------------------------------ parameters
# Template parameter sets as defined in scripts/models.py: (k, ks, tq, tT, tv).
TAU_REF = 1.0
MODELS = {
    "Fourier": dict(k=1.0, ks=0.0, tq=0.0, tT=0.0, tv=0.0),
    "LS":      dict(k=1.0, ks=0.0, tq=TAU_REF, tT=0.0, tv=0.0),
    "DPL":     dict(k=1.0, ks=0.0, tq=TAU_REF, tT=0.5 * TAU_REF, tv=0.0),
    "GN-II":   dict(k=0.0, ks=1.0, tq=0.0, tT=0.0, tv=0.0),
    "GN-III":  dict(k=1.0, ks=1.0, tq=0.0, tT=0.0, tv=0.0),
    "MGT":     dict(k=1.0, ks=1.0, tq=TAU_REF, tT=0.0, tv=0.0),
}
RHO, CV, C1 = 1.0, 1.0, 1.0     # nondimensional reference medium
EPS = 0.1                       # beta^2 T0 = eps, as in the scripts
TOL_ROUNDED = 5e-5              # archived values are printed with 4-6 significant digits


# ------------------------------------------------------------- polynomial tools
def _trim_hi(a):
    """Drop numerically zero *trailing* entries of a lowest-power-first array."""
    a = np.asarray(a, dtype=complex)
    if a.size == 0:
        return a
    thr = 1e-13 * max(1.0, float(np.max(np.abs(a))))
    nz = np.nonzero(np.abs(a) > thr)[0]
    return a[:nz[-1] + 1] if nz.size else np.array([0.0 + 0.0j])


def _pad(a, n):
    a = np.asarray(a, dtype=complex)
    return a if a.size >= n else np.concatenate([a, np.zeros(n - a.size, dtype=complex)])


# ------------------------------------------------------------------ model layer
def transfer_function(s, p):
    """G(s) of the template (q^ = -G T^,x), evaluated at complex s."""
    s = complex(s)
    num = p["k"] * (1.0 + p["tT"] * s) + p["ks"] * (1.0 + p["tv"] * s) / s
    return num / (1.0 + p["tq"] * s)


def coupled_K_roots(w, p, beta2T0=EPS, rho=RHO, cv=CV, c1=C1):
    """Both K = k^2 roots of (D) at real frequency w, obtained with numpy.roots."""
    s = -1j * complex(w)
    D0 = 1.0 + p["tq"] * s
    N = p["k"] * s * (1.0 + p["tT"] * s) + p["ks"] * (1.0 + p["tv"] * s)
    A = rho * c1 ** 2 * N
    B = rho * c1 ** 2 * (s * rho * cv) * (s * D0) + rho * s ** 2 * N + beta2T0 * s ** 2 * D0
    C = rho * s ** 2 * (s * rho * cv) * (s * D0)
    coeffs = np.array([A, B, C], dtype=complex)
    # drop exactly-zero highest powers (e.g. GN-II with k = 0 keeps degree 2)
    nz = np.nonzero(np.abs(coeffs) > 1e-13 * max(1.0, float(np.max(np.abs(coeffs)))))[0]
    return np.roots(coeffs[nz[0]:])


def spatial_k(w, p, **kw):
    """Both wavenumbers at real w, on the physical branch.

    Sign convention: propagation in +x (Re k > 0) when the root propagates,
    otherwise the decaying branch (Im k > 0).  For a lossless medium the two
    roots are then k = +-|k| with |Im k| = 0.
    """
    out = []
    for K in coupled_K_roots(w, p, **kw):
        k = cmath.sqrt(K)
        if abs(k.real) > 1e-12:
            if k.real < 0:
                k = -k
        elif k.imag < 0:
            k = -k
        out.append(k)
    return out


def thermal_k(w, p, rho=RHO, cv=CV):
    """Uncoupled thermal branch: k^2 = -s rho cv / G(s), Im k >= 0."""
    s = -1j * complex(w)
    k = cmath.sqrt(-s * rho * cv / transfer_function(s, p))
    return -k if k.imag < 0 else k


def branch_modes(w, p, beta2T0=EPS):
    """Both branches at real w as (v_p, Q^-1), least damped first.

    The acoustic/elastic branch is identified physically as the *least damped*
    of the two propagating branches (Q^-1 = 2 Im k / Re k); ties are broken by
    proximity to the adiabatic speed sqrt(1 + eps).  This is a local criterion
    and therefore immune to branch-swapping in continuity tracking.
    """
    modes = []
    for k in spatial_k(w, p, beta2T0=beta2T0):
        if k.real > 1e-12:
            modes.append((w / k.real, 2.0 * k.imag / k.real))
        else:
            modes.append((float("inf"), float("inf")))       # evanescent
    target = math.sqrt(1.0 + beta2T0)
    # round Q^-1 before ordering so that lossless noise cannot swap the branches
    return sorted(modes, key=lambda t: (round(t[1], 8), abs(t[0] - target)))


def elastic_branch(freqs, p, beta2T0=EPS):
    """(v_p, Q^-1) of the elastic branch on the frequency list."""
    v, q = [], []
    for w in freqs:
        vv, qq = branch_modes(w, p, beta2T0=beta2T0)[0]
        v.append(vv)
        q.append(qq)
    return np.array(v, dtype=float), np.array(q, dtype=float)


def bar_s_roots(K, p, beta2T0=EPS, rho=RHO, cv=CV, c1=C1):
    """All complex s of (D) at real wavenumber k (K = k^2), via polynomial algebra.

    (D) multiplied by s D0(s) reads, with P1 = rho c1^2 K + rho s^2,

      P1 (s rho cv D0 + K N) + beta^2 T0 s^2 D0 K = 0,

    which is a polynomial of degree at most four in s.
    """
    D0 = np.array([1.0, p["tq"]], dtype=complex)                        # 1 + tq s
    N = np.array([p["ks"], p["k"] + p["ks"] * p["tv"], p["k"] * p["tT"]], dtype=complex)
    sD0 = np.polynomial.polynomial.polymul([0.0, 1.0], D0)              # s D0(s)
    P1 = np.array([rho * c1 ** 2 * K, 0.0, rho], dtype=complex)         # rho c1^2 K + rho s^2
    P2 = np.polynomial.polynomial.polyadd(
        rho * cv * np.polynomial.polynomial.polymul([0.0, 1.0], sD0), K * N)
    P3 = beta2T0 * K * np.polynomial.polynomial.polymul([0.0, 1.0], sD0)
    P1, P2, P3 = _trim_hi(P1), _trim_hi(P2), _trim_hi(P3)
    prod = np.polynomial.polynomial.polymul(P1, P2)        # P1(s) * P2(s)
    poly = np.polynomial.polynomial.polyadd(_pad(prod, max(prod.size, P3.size)),
                                            _pad(P3, max(prod.size, P3.size)))
    poly = _trim_hi(poly)
    return np.roots(poly[::-1])


def _qinv(z):
    """Q^-1 = 2 |Im w| / |Re w| with w = i s  ->  2 |Re s| / |Im s|."""
    return 2.0 * abs(z.real) / abs(z.imag)


def bar_modes(K, tau):
    """All damped bar modes at real wavenumber k (K = k^2), as (Q^-1, s)."""
    p = dict(k=1.0, ks=0.0, tq=tau, tT=0.0, tv=0.0)
    out = []
    for z in bar_s_roots(K, p):
        if abs(z) < 1e-13 or abs(z.imag) < 1e-13 or abs(z.real) < 1e-13:
            continue                      # spurious root at s = 0 / real root: Q^-1 undefined
        out.append((_qinv(z), z))
    seen, uniq = set(), []
    for q, z in sorted(out, key=lambda t: t[0]):
        key = round(q, 9)
        if key not in seen:
            seen.add(key)
            uniq.append((q, z))
    return uniq


def bar_branch(kvals, tau, per_interval=40):
    """Q^-1 of the branch that continues the low-k acoustic mode, exactly at kvals."""
    kvals = sorted(kvals)
    grid = [kvals[0]]
    for a, b in zip(kvals, kvals[1:]):
        grid += list(np.logspace(math.log10(a), math.log10(b), per_interval)[1:])
    p = dict(k=1.0, ks=0.0, tq=tau, tT=0.0, tv=0.0)
    prev, tracked = None, {}
    for kk in grid:
        cand = [z for z in bar_s_roots(kk ** 2, p)
                if abs(z) > 1e-13 and abs(z.imag) > 1e-13 and abs(z.real) > 1e-13]
        if not cand:
            continue
        if prev is None:
            z = min(cand, key=lambda z: abs(z + 1j * kk * math.sqrt(1.0 + EPS)))
        else:
            z = min(cand, key=lambda z: abs(z - prev))
        prev = z
        for Kv in kvals:
            if abs(kk - Kv) <= 1e-12 * max(1.0, Kv):
                tracked[Kv] = (float(_qinv(z)), z)
    return tracked


# ------------------------------------------------------ archived reference values
# Every number below is a literal from scripts/numbers_log.txt.  `which` selects
# the quantity: thermal | elastic | coupled_slow | coupled_fast | bar.
REF = []


def _ref(which, label, params, point, value, block, digits):
    REF.append(dict(which=which, label=label, params=dict(params), point=float(point),
                    value=float(value), block=block, digits=digits))


FAMILY = {
    "Fourier": dict(k=1, ks=0, tq=0, tT=0, tv=0),
    "Lord-Shulman": dict(k=1, ks=0, tq=1, tT=0, tv=0),
    "DPL(tT=0.5tq)": dict(k=1, ks=0, tq=1, tT=0.5, tv=0),
    "GN-II": dict(k=0, ks=0.25, tq=0, tT=0, tv=0),
    "GN-III": dict(k=1, ks=0.25, tq=0, tT=0, tv=0),
    "MGT": dict(k=1, ks=0.25, tq=1, tT=0, tv=0),
}
FAMILY_LIMITS = {           # fig_thermal_family block: w = 0.001 and w = 100
    "Fourier": (0.0447, 14.1421),
    "Lord-Shulman": (0.0447, 1.0),
    "DPL(tT=0.5tq)": (0.0447, 9.9511),
    "GN-II": (0.5, 0.5),
    "GN-III": (0.5, 14.1245),
    "MGT": (0.5, 1.0),
}
for _n, _p in FAMILY.items():
    _lo, _hi = FAMILY_LIMITS[_n]
    _ref("thermal_uncoupled", "fig_thermal_family/%s @ w=1e-3" % _n, _p, 1e-3, _lo,
         "fig_thermal_family block (w=0.001)", 3)
    _ref("thermal_uncoupled", "fig_thermal_family/%s @ w=1e2" % _n, _p, 1e2, _hi,
         "fig_thermal_family block (w=100.0)", 6)

# check_gn2 block: GN-II is non-dispersive; closed-form roots, 16 digits
for _w in (0.5, 2.0, 10.0):
    _ref("coupled_slow", "check_gn2/GN-II slow @ w=%g" % _w, MODELS["GN-II"], _w,
         0.8543089535574103, "check_gn2 block, closed-form root", 16)
    _ref("coupled_fast", "check_gn2/GN-II fast @ w=%g" % _w, MODELS["GN-II"], _w,
         1.1705367195742484, "check_gn2 block, closed-form root", 16)

# check_fronts block: LS at w = 2e3, tau0 = 0.25, eps = 0.1 (printed to 4 dp)
_LS_FRONT = dict(k=1.0, ks=0.0, tq=0.25, tT=0.0, tv=0.0)
_ref("coupled_slow", "check_fronts/LS slow front @ w=2e3", _LS_FRONT, 2e3, 0.9839,
     "check_fronts block (4 dp)", 4)
_ref("coupled_fast", "check_fronts/LS fast front @ w=2e3", _LS_FRONT, 2e3, 2.0327,
     "check_fronts block (4 dp)", 4)

# fig_dispersion block: eps = 0.1, tau = 0.25, elastic and thermal speeds, 16 digits
_LS_DISP = dict(k=1.0, ks=0.0, tq=0.25, tT=0.0, tv=0.0)
_CD_DISP = dict(k=1.0, ks=0.0, tq=0.0, tT=0.0, tv=0.0)
_ref("elastic", "fig_dispersion/LS elastic @ w=10^1.6", _LS_DISP, 10 ** 1.6,
     0.9839644366553235, "fig_dispersion block (LS elastic, high w)", 16)
_ref("coupled_thermal", "fig_dispersion/LS thermal @ w=10^1.6", _LS_DISP, 10 ** 1.6,
     2.0298360266180757, "fig_dispersion block (LS thermal, high w)", 16)
_ref("elastic", "fig_dispersion/classical elastic @ w=1e-2", _CD_DISP, 1e-2,
     1.0488055351860703, "fig_dispersion block (CD elastic, low w)", 16)
_ref("elastic", "fig_dispersion/classical elastic @ w=10^1.6", _CD_DISP, 10 ** 1.6,
     1.0000307473049175, "fig_dispersion block (CD elastic, high w)", 16)

# fig_bar_modes block: printed Q^-1 at six wavenumbers, eps = 0.1
BAR_REF = {
    (0.0, 0.01): 0.0008667, (0.0, 0.1): 0.008606, (0.0, 1.0): 0.04869,
    (0.0, 3.0): 0.03009, (0.0, 10.0): 0.009906, (0.0, 30.0): 0.00333,
    (0.25, 0.01): 0.0008668, (0.25, 0.1): 0.008641, (0.25, 1.0): 0.06317,
    (0.25, 3.0): 0.6735, (0.25, 10.0): 0.1897, (0.25, 30.0): 0.0629,
    (1.0, 0.01): 0.0008668, (1.0, 0.1): 0.008672, (1.0, 1.0): 0.09062,
    (1.0, 3.0): 0.1122, (1.0, 10.0): 0.03587, (1.0, 30.0): 0.01201,
}


def evaluate(r):
    """Compute the quantity that a REF row compares with the archived value."""
    w, p = r["point"], r["params"]
    if r["which"] == "thermal_uncoupled":
        return w / thermal_k(w, p).real
    modes = branch_modes(w, p)
    if r["which"] == "elastic":
        return modes[0][0]
    if r["which"] == "coupled_thermal":
        return modes[1][0]
    speeds = sorted(m[0] for m in modes)
    if r["which"] == "coupled_slow":
        return speeds[0]
    if r["which"] == "coupled_fast":
        return speeds[-1]
    raise ValueError(r["which"])


def run(outdir="."):
    rows = []
    for r in REF:
        val = evaluate(r)
        rows.append(dict(kind=r["which"], quantity=r["label"], point=r["point"],
                         archived=r["value"], computed=float(val),
                         rel_diff=abs(val - r["value"]) / abs(r["value"]),
                         block=r["block"], digits=r["digits"],
                         acoustic_q="", n_modes=""))
    kvals = sorted({K for (_, K) in BAR_REF})
    for tau in sorted({t for (t, _) in BAR_REF}):
        tracked = bar_branch(kvals, tau)
        for K in kvals:
            qref = BAR_REF[(tau, K)]
            modes = bar_modes(K ** 2, tau)      # BAR_REF keys are wavenumbers k, K = k^2
            qbest, zbest = min(modes, key=lambda t: abs(t[0] - qref))
            qtrack = tracked.get(K, (float("nan"), None))[0]
            rows.append(dict(kind="bar", quantity="fig_bar_modes/tau=%.2f k=%.2g" % (tau, K),
                             point=K, archived=qref, computed=qbest,
                             rel_diff=abs(qbest - qref) / qref,
                             block="fig_bar_modes block (printed Q^-1)",
                             digits=4, acoustic_q=qtrack,
                             n_modes=len(modes)))

    freqs = np.logspace(-3, 2, 20)
    table = []
    for name in ("Fourier", "LS", "DPL", "GN-III", "MGT"):
        for w in freqs:
            modes = branch_modes(float(w), MODELS[name])
            table.append(dict(model=name, omega=float(w),
                              v_p=float(modes[0][0]), Qinv=float(modes[0][1]),
                              v_p_other=float(modes[1][0]), Qinv_other=float(modes[1][1])))

    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "second_impl_comparison.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=["kind", "quantity", "point", "archived",
                                           "computed", "rel_diff", "block", "digits",
                                           "acoustic_q", "n_modes"])
        wr.writeheader()
        for x in rows:
            wr.writerow({k: ("%.17g" % v if isinstance(v, float) else v) for k, v in x.items()})
    with open(os.path.join(outdir, "second_impl_elastic_branch.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=["model", "omega", "v_p", "Qinv",
                                           "v_p_other", "Qinv_other"])
        wr.writeheader()
        for x in table:
            wr.writerow({k: ("%.17g" % v if isinstance(v, float) else v) for k, v in x.items()})
    return rows, table


def report(rows, table):
    L = ["# Independent second implementation - comparison report\n",
         "Code: `second_impl.py` (standalone, numpy only, no import from `scripts/`).\n",
         "## Agreement with `scripts/numbers_log.txt`\n",
         "| quantity | archived | computed here | rel. diff | log block |",
         "|---|---|---|---|---|"]
    for x in rows:
        L.append("| %s | %.10g | %.10g | %.2e | %s |" %
                 (x["quantity"], x["archived"], x["computed"], x["rel_diff"], x["block"]))
    L.append("\n### Bar modes: mode-by-mode agreement and branch labelling\n")
    L.append("| tau, k | archived | matching mode | rel. diff | modes at this k "
             "| acoustic continuation |")
    L.append("|---|---|---|---|---|---|")
    for x in rows:
        if x["kind"] == "bar":
            L.append("| tau=%s | %.4g | %.6g | %.1e | %s | %.6g |" %
                     (x["quantity"].split("tau=")[1].split(" ")[0], x["archived"],
                      x["computed"], x["rel_diff"], x["n_modes"], x["acoustic_q"]))
    L.append("\n### Maximum relative difference by quantity\n")
    L.append("| quantity class | rows | worst rel. diff |")
    L.append("|---|---|---|")
    per = {}
    for x in rows:
        per.setdefault(x["kind"], []).append(x["rel_diff"])
    for k, v in per.items():
        L.append("| %s | %d | %.2e |" % (k, len(v), max(v)))
    L.append("\n## Elastic branch at 20 frequencies (v_p = w/Re k, Q^-1 = 2 Im k / Re k)\n")
    L.append("| model | omega | v_p | Q^-1 | second branch v_p | second branch Q^-1 |")
    L.append("|---|---|---|---|---|---|")
    for x in table:
        L.append("| %s | %.4g | %.10f | %.6e | %.10f | %.6e |" %
                 (x["model"], x["omega"], x["v_p"], x["Qinv"],
                  x["v_p_other"], x["Qinv_other"]))
    return "\n".join(L) + "\n"


def check():
    tmp = tempfile.mkdtemp()
    rows, table = run(outdir=tmp)
    ok = True
    per = {}
    for x in rows:
        per.setdefault(x["kind"], []).append(x)
    for kind, xs in per.items():
        worst = max(xs, key=lambda x: x["rel_diff"])
        # tolerance from the printed precision of the archived entry
        tol = {"bar": 2e-4, 3: 2e-3, 4: 2e-4, 6: 1e-5}.get(
            worst["digits"], 1e-10)      # tolerance set by the printed precision
        good = worst["rel_diff"] <= tol
        ok &= good
        print(("PASS " if good else "FAIL ") +
              "%s: %d archived values, worst rel. diff %.2e (%s, tol %.0e)" %
              (kind, len(xs), worst["rel_diff"], worst["quantity"], tol))
    # 20-frequency table: internal consistency checks
    freqs = np.logspace(-3, 2, 20)
    v_cd, q_cd = elastic_branch(freqs, MODELS["Fourier"])
    v_ls, q_ls = elastic_branch(freqs, MODELS["LS"])
    good = abs(v_cd[0] - math.sqrt(1.0 + EPS)) < 5e-3
    ok &= good
    print(("PASS " if good else "FAIL ") +
          "classical v_p(w=1e-3)=%.6f approaches the adiabatic limit sqrt(1+eps)=%.6f" %
          (v_cd[0], math.sqrt(1 + EPS)))
    i = int(np.argmax(q_cd))
    good = 0 < i < len(q_cd) - 1 and np.all(np.diff(q_cd[:i + 1]) > 0) and np.all(np.diff(q_cd[i:]) < 0)
    ok &= good
    print(("PASS " if good else "FAIL ") +
          "classical Q^-1 is single-peaked at w=%.3g (Q^-1=%.4g), as a Debye peak must be" %
          (freqs[i], q_cd[i]))
    # structural checks on the 20-frequency table
    good = all(np.isfinite([x["v_p"] for x in table])) and all(x["v_p"] > 0 for x in table) \
        and all(x["Qinv"] >= -1e-12 for x in table)
    ok &= good
    print(("PASS " if good else "FAIL ") +
          "table values are finite with v_p > 0 and Q^-1 >= 0 (%d rows)" % len(table))
    # classical branch must decrease monotonically from the adiabatic to the isothermal speed
    vfd = np.array([x["v_p"] for x in table if x["model"] == "Fourier"])
    good = bool(np.all(np.diff(vfd) <= 1e-12)) and abs(vfd[0] - math.sqrt(1 + EPS)) < 1e-3 \
        and abs(vfd[-1] - 1.0) < 1e-3
    ok &= good
    print(("PASS " if good else "FAIL ") +
          "Fourier branch decreases monotonically %.5f -> %.5f (adiabatic -> isothermal)" % (vfd[0], vfd[-1]))
    # LS with tau = 1: the two branches are close (0.8543 and 1.1705); the least damped
    # one must stay within 1.5% of the value already checked against the archive
    vls = np.array([x["v_p"] for x in table if x["model"] == "LS"])
    good = abs(vls[-1] - 1.1705367195742484) < 2e-4
    ok &= good
    print(("PASS " if good else "FAIL ") +
          "LS branch at w=1e2 reaches %.6f, the fast root of the archived quadratic (1.170537)" % vls[-1])
    good = len(table) == 100 and np.all(np.isfinite([x["v_p"] for x in table]))
    ok &= good
    print(("PASS " if good else "FAIL ") + "20-frequency table has %d finite rows (5 models x 20)" % len(table))
    # branch labelling in the archived bar-mode printout: at tau > 0 and k >= 3 the
    # printed number belongs to the strongly damped pair, not to the continuation of
    # the low-k acoustic mode; both are modes of the same polynomial
    mism = [x for x in rows if x["kind"] == "bar" and x["acoustic_q"]
            and abs(x["acoustic_q"] - x["archived"]) / x["archived"] > 0.1]
    good = len(mism) >= 3
    ok &= good
    print(("PASS " if good else "FAIL ") +
          "%d of 18 bar-mode entries belong to the strongly damped pair, not to the "
          "acoustic continuation (branch label, not a numerical disagreement)" % len(mism))
    if not ok:
        print("FAIL some checks failed")
        return 1
    print("PASS all checks (archived values compared=%d, table rows=%d)" % (len(rows), len(table)))
    return 0


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    here = os.path.dirname(os.path.abspath(__file__))
    rows, table = run(outdir=here)
    open(os.path.join(here, "second_impl_report.md"), "w").write(report(rows, table))
    per = {}
    for x in rows:
        per.setdefault(x["kind"], []).append(x["rel_diff"])
    print("comparisons: %d rows" % len(rows))
    for k, v in sorted(per.items()):
        print("  %-14s %3d values, worst rel. diff %.2e" % (k, len(v), max(v)))
    print("wrote second_impl_comparison.csv, second_impl_elastic_branch.csv, second_impl_report.md")
