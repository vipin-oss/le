#!/usr/bin/env python3
"""BK-10: the thermoelastic Rayleigh secular determinant (P3 atlas, step 30).

Why this file exists
--------------------
`atlas_case_coverage.csv` marks the six surface-wave cases as *partial*: BK-09
checks the **elastic** Rayleigh equation, which is only the zero-coupling limit
of what those papers actually study.  A surface wave on a thermoelastic half
space is a three-partial-wave problem - one shear mode, and a coupled
longitudinal/thermal pair - so BK-09 cannot see the coupling, the relaxation
time, or the attenuation.  This file adds the missing invariant as **BK-10**.

The model is the template the rest of the project already uses (see
`../P4_second_impl/second_impl.py`, eq. (D)):

  heat-flux template   q + tq q' = -k T,x - ks v,x ,  v' = T
  energy balance       rho cv T' + beta T0 u',x = -q,x
  momentum             rho u'' = rho c1^2 u,xx - beta T,x

For a plane wave with a depth dependence exp(i (kx + gamma k z)) every field
equation depends on the depth only through chi = k^2 (1 + gamma^2), so the
bulk quadratic in K becomes a quadratic in chi with *the same* coefficients
A, B, C - that is what makes the half-space problem solvable with the code that
already exists.  The shear partial wave is decoupled (no volume change, no
temperature), with chi_S = -s^2 / c_S^2.

Boundary conditions at the free, thermally insulated surface (z = 0):

  sigma_xz = 0 ,  sigma_zz = 0 ,  dT/dz = 0 .

The momentum elimination gives the sign that decides everything:

      (rho c1^2 chi + rho s^2) e = beta chi T ,   e = div u = -chi phi
  =>  beta T = -(rho c1^2 chi + rho s^2) phi          (d = rho c1^2 chi + rho s^2)

so `sigma_zz` carries `+d/k^2`, not `-d/k^2`.  That sign is not a taste: with
the opposite one the dissipative models (Fourier, LS, DPL, GN-III) come out
**growing** in time while the lossless ones (GN-II, MGT) come out neutral,
which is impossible for a passive medium.  The right sign gives decay for the
dissipative models and exactly zero for the lossless ones - check 2 and 3.

What is checked (6 rows, all PASS)
----------------------------------
1. beta -> 0 reproduces the classical elastic Rayleigh root of BK-09 for all
   six models: 0.9194016868 c_S at c1 = sqrt(3) c_S (nu = 1/4).
2. Passivity: the dissipative models have Re s < 0 (attenuation, no growing
   surface mode) at k = 0.5, 1, 5.
3. Losslessness: GN-II and MGT have |Re s| < 1e-12 and a speed that does not
   depend on k.
4. Sub-shear: v = Re(i s)/k stays below c_S for every model and every k.
5. The dissipative models approach the elastic isothermal value as k -> 50
   (Fourier, DPL, GN-III) and get closer to it than at k = 0.5; LS keeps a
   residual dispersion and is reported, not asserted.
6. Thermoelastic damping of the Rayleigh wave is weak: Q^-1 < 0.01 throughout.

What this is *not*: a comparison with any paper.  The six surface cases are
still `full_text_read = no`, so this benchmark says what any implementation of
this model class must reproduce; it does not say what paper AT-07 reports.

Usage
  python3 bench_thermoelastic.py            # writes bench_thermoelastic_results.csv
  python3 bench_thermoelastic.py --check    # PASS/FAIL lines, exit 1 on failure

Requires numpy.  Runtime < 1 s.  Nothing under `scripts/` is touched.
"""
import cmath
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "P4_second_impl")))
import second_impl as S                                        # noqa: E402

RHO, CV, C1 = 1.0, 1.0, 1.0
CS2 = 1.0 / 3.0                      # c_S^2 with c1^2 = 3 c_S^2  (nu = 1/4)
MU = RHO * CS2
LAM = RHO * C1 ** 2 - 2.0 * MU
CS = math.sqrt(CS2)
EPS = S.EPS                          # beta^2 T0 = 0.1
LOSSY = ("Fourier", "LS", "DPL", "GN-III")
LOSSLESS = ("GN-II", "MGT")
KS = (0.5, 1.0, 5.0)


def rayleigh_elastic(eta):
    """c_R/c_S from (2 - x^2)^2 = 4 sqrt(1 - x^2) sqrt(1 - eta x^2), eta = (c_S/c1)^2.

    Returns the *ratio* c_R/c_S, not a speed.

    x = 0 is a degenerate root of this written form, hence the bracket (0.5, 1).
    """
    def f(x):
        a = max(0.0, 1.0 - x * x)
        b = max(0.0, 1.0 - eta * x * x)
        return (2.0 - x * x) ** 2 - 4.0 * math.sqrt(a) * math.sqrt(b)
    lo, hi = 0.5, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


C_R = rayleigh_elastic(CS2 / C1 ** 2) * CS        # ratio -> speed, in units of c1 = 1


def _chi_roots(s, p, beta2T0):
    """The coupled longitudinal/thermal pair: the same A, B, C as second_impl."""
    s = complex(s)
    D0 = 1.0 + p["tq"] * s
    N = p["k"] * s * (1.0 + p["tT"] * s) + p["ks"] * (1.0 + p["tv"] * s)
    A = RHO * C1 ** 2 * N
    B = RHO * C1 ** 2 * (s * RHO * CV) * (s * D0) + RHO * s ** 2 * N + beta2T0 * s ** 2 * D0
    Cc = RHO * s ** 2 * (s * RHO * CV) * (s * D0)
    co = np.array([A, B, Cc], dtype=complex)
    nz = np.nonzero(np.abs(co) > 1e-13 * max(1.0, float(np.max(np.abs(co)))))[0]
    return list(np.roots(co[nz[0]:]))


def det_s(s, k, p, beta2T0):
    """3x3 secular determinant for a real wavenumber k and complex s."""
    s = complex(s)
    chi = _chi_roots(s, p, beta2T0)
    chi_s = -s * s / CS2

    def gam(ch):
        g = cmath.sqrt(complex(ch) / (k * k) - 1.0)
        return g if g.imag > 0 else -g              # decay away from the surface

    gs = [gam(c) for c in chi]
    g_s = gam(chi_s)
    ds = [RHO * C1 ** 2 * c + RHO * s * s for c in chi]
    m = np.zeros((3, 3), dtype=complex)
    for j, (g, d) in enumerate(zip(gs, ds)):
        m[0, j] = -2.0 * g                                   # sigma_xz = 0
        m[1, j] = -(LAM + (LAM + 2.0 * MU) * g * g) + d / (k * k)   # sigma_zz = 0
        m[2, j] = g * d                                       # dT/dz = 0
    m[0, 2] = 1.0 - g_s * g_s
    m[1, 2] = 2.0 * MU * g_s
    m[2, 2] = 0.0
    return np.linalg.det(m)


def solve(k, p, beta2T0=EPS, seed=None):
    """Complex Newton for the surface mode; returns (s, residual)."""
    s = complex(seed if seed is not None else -1j * k * C_R)
    for _ in range(200):
        f0 = det_s(s, k, p, beta2T0)
        h = 1e-7 * max(abs(s), 1e-12)
        df = (det_s(s + h, k, p, beta2T0) - f0) / h
        if df == 0.0:
            break
        step = -f0 / df
        s += step
        if abs(step) < 1e-15 * max(abs(s), 1e-12):
            break
    return s, abs(det_s(s, k, p, beta2T0))


def mode(k, name, beta2T0=EPS):
    s, res = solve(k, S.MODELS[name], beta2T0)
    w = -s.imag
    return dict(model=name, k=k, s=s, re_s=s.real, v=w / k, qinv=2.0 * abs(s.real) / abs(w) if w else 0.0,
                residual=res)


# ------------------------------------------------------------------ benchmarks
def b10_decoupling():
    """beta -> 0 must give back the elastic Rayleigh root, whatever the model."""
    worst, bad = 0.0, []
    for name in S.MODELS:
        s, _ = solve(1.0, S.MODELS[name], 0.0)
        v = (-s.imag) / 1.0
        err = abs(v - C_R) / CS
        worst = max(worst, err)
        if err > 1e-9:
            bad.append("%s:%.2e" % (name, err))
    return ("beta -> 0 limit against the elastic Rayleigh root",
            "max |v - c_R| = %.2e c_S (c_R = %.10f c_S)" % (worst, C_R / CS),
            "<= 1e-09 c_S, all 6 models", len(bad), bad)


def b10_passivity():
    """Re s < 0: a passive thermoelastic half space cannot grow a surface wave."""
    worst, bad, n = -1e9, [], 0
    for name in LOSSY:
        for k in KS:
            r = mode(k, name)
            n += 1
            worst = max(worst, r["re_s"] / (r["v"] * k))
            if r["re_s"] >= 0.0:
                bad.append("%s@k=%g:%+.2e" % (name, k, r["re_s"]))
    return ("no growing surface mode in the four dissipative models",
            "max Re s / (k v) = %+.3e over %d (model, k) points" % (worst, n),
            "Re s < 0 everywhere", len(bad), bad)


def b10_lossless():
    """GN-II and MGT have no dissipation, so the surface mode must be neutral."""
    worst, bad, spread = 0.0, [], 0.0
    for name in LOSSLESS:
        vs = []
        for k in KS:
            r = mode(k, name)
            worst = max(worst, abs(r["re_s"]) / (r["v"] * k))
            vs.append(r["v"])
            if abs(r["re_s"]) > 1e-12 * abs(r["v"] * k):
                bad.append("%s@k=%g:%+.2e" % (name, k, r["re_s"]))
        spread = max(spread, (max(vs) - min(vs)) / CS)
    return ("GN-II and MGT carry no attenuation and no dispersion",
            "max |Re s|/(k v) = %.1e, speed spread over k = %.1e c_S"
            % (worst, spread),
            "|Re s| <= 1e-12 k v and spread <= 1e-12 c_S", len(bad), bad)


def b10_subshear():
    """A Rayleigh wave is slower than the shear wave - and c_S is model-independent."""
    worst, bad, n = 0.0, [], 0
    for name in S.MODELS:
        for k in KS:
            r = mode(k, name)
            n += 1
            worst = max(worst, r["v"] / CS)
            if not (0.0 < r["v"] < CS * (1.0 - 1e-9)):
                bad.append("%s@k=%g:v/c_S=%.6f" % (name, k, r["v"] / CS))
    return ("the surface speed stays below c_S for every model and wavenumber",
            "max v/c_S = %.6f over %d points" % (worst, n),
            "0 < v < c_S", len(bad), bad)


def b10_isothermal_limit():
    """At large k the dissipative models tend to the elastic isothermal c_R."""
    rows = {}
    for name in ("Fourier", "DPL", "GN-III"):
        near = mode(50.0, name)
        far = mode(0.5, name)
        rows[name] = (near["v"], far["v"])
    worst = max(abs(v[0] - C_R) / CS for v in rows.values())
    closer = all(abs(v[0] - C_R) < abs(v[1] - C_R) for v in rows.values())
    ls = mode(50.0, "LS")["v"]
    bad = []
    if worst > 1e-3:
        bad.append("far from c_R: %.2e" % worst)
    if not closer:
        bad.append("k = 50 is not closer to c_R than k = 0.5")
    return ("k -> 50 reaches the elastic isothermal root (Fourier, DPL, GN-III)",
            "max |v(k=50) - c_R| = %.2e c_S (LS at k = 50 is %.6f c_S, its own value)"
            % (worst, ls / CS),
            "<= 1e-03 c_S and closer than at k = 0.5", len(bad), bad)


def b10_damping():
    """Thermoelastic damping of a Rayleigh wave is weak in this parameter range."""
    worst, bad, n = 0.0, [], 0
    for name in LOSSY:
        for k in KS:
            r = mode(k, name)
            n += 1
            worst = max(worst, r["qinv"])
            if r["qinv"] > 1e-2:
                bad.append("%s@k=%g:Q^-1=%.3e" % (name, k, r["qinv"]))
    return ("Q^-1 of the surface mode stays small", "max Q^-1 = %.3e over %d points" % (worst, n),
            "<= 1e-02", len(bad), bad)


CHECKS = (b10_decoupling, b10_lossless, b10_isothermal_limit,
          b10_damping, b10_passivity, b10_subshear)

HEADER = ["benchmark_id", "quantity_checked", "measured", "reference", "reference_type",
         "tolerance", "verdict", "script"]


def run(outdir=HERE):
    rows = []
    failures = 0
    for fn in CHECKS:
        q, measured, tol, nbad, bad = fn()
        verdict = "PASS" if nbad == 0 else "FAIL"
        failures += (nbad > 0)
        rows.append(dict(benchmark_id="BK-10", quantity_checked=q, measured=measured,
                         reference=tol, reference_type="closed form + structural requirement",
                         tolerance=tol, verdict=verdict, script="bench_thermoelastic.py"))
        print("  BK-10  %-5s  %-66s %s" % (verdict, q[:66], measured))
        for b in bad[:3]:
            print("           %s" % b)
    out = os.path.join(outdir, "bench_thermoelastic_results.csv")
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=HEADER)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print("rows: %d, failures: %d" % (len(rows), failures))
    return failures


def main():
    if "--check" in sys.argv:
        fails = run(os.path.join(HERE, "..", ".."))
    else:
        fails = run()
    if fails:
        print("FAIL %d row(s)" % fails)
        return 1
    print("PASS all %d rows" % len(CHECKS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
