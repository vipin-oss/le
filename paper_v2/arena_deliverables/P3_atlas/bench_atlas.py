#!/usr/bin/env python3
"""Executable invariants behind the 40 proposed atlas problems (Task 5, second half).

`atlas_plan.csv` lists 40 problems, each with a free-text "validation target".
A free-text target cannot be run.  This file turns those targets into eight
machine-checkable benchmark families (BK-01 ... BK-08) that any implementation
of the corresponding wave family has to satisfy, and pins a tolerance for each.

What the benchmarks are, and what they are *not*
-----------------------------------------------
They are **invariants of the model structure**, not comparisons with the
individual papers: the 40 papers were read at title/metadata level only
(`full_text_read = no` in `atlas_plan.csv`), so none of their secular equations
or parameter sets is available here.  A benchmark of the form "reproduce
Fig. 3 of paper X" would be fiction.  A benchmark of the form "a model of this
class must show exactly two K = k^2 roots, the adiabatic low-frequency limit,
the Debye-shaped Q^-1 peak at the right height, Rayleigh alpha ~ w^2 at low
frequency, saturating alpha at high frequency, and no growing mode" is checkable
today and is what the papers are then tested against later.

Every check drives `../P4_second_impl/second_impl.py` (the independent
reimplementation from Task 6) and nothing else.  No file under `scripts/` is
imported, executed or modified.

Usage
  python3 bench_atlas.py            # runs the benchmarks, writes bench_atlas_results.csv
  python3 bench_atlas.py --check    # runs them, prints only PASS/FAIL, exit 1 on any failure

Requires numpy.  Runtime < 2 s.
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
IMPL_DIR = os.path.normpath(os.path.join(HERE, "..", "P4_second_impl"))
sys.path.insert(0, IMPL_DIR)
import second_impl as S                                    # noqa: E402

MODELS = S.MODELS
EPS = S.EPS
ADIA = math.sqrt(1.0 + EPS)                                # sqrt(1.1)
DELTA = EPS / (1.0 + EPS)                                  # relaxation strength
GN2_SLOW = 0.8543089535574103                               # closed form, GN-II
GN2_FAST = 1.1705367195742484
TAU = 1.0

# ------------------------------------------------------------------ helpers
def alpha_elastic(w, p):
    """Attenuation coefficient Im k of the least damped propagating branch."""
    best = None
    for k in S.spatial_k(w, p):
        if k.real <= 0:
            continue
        q = 2.0 * k.imag / k.real
        if best is None or q < best[0]:
            best = (q, k)
    return best[1].imag


def speeds(w, p):
    return [v for v, _q in S.branch_modes(w, p) if math.isfinite(v)]


# ------------------------------------------------------------------ benchmarks
def bk01_branch_structure():
    """A quadratic in K has exactly two roots - for every model, every frequency."""
    bad = []
    for name, p in MODELS.items():
        for w in (0.5, 5.0):
            n = len(S.coupled_K_roots(w, p))
            if n != 2:
                bad.append("%s@%g:%d" % (name, w, n))
    return ("K-roots per (model, frequency)", "2", "exactly 2", len(bad), bad)


def bk02_adiabatic_limit():
    """w -> 0: the elastic branch speed must tend to sqrt(1+eps) = 1.0488088."""
    worst, where = 0.0, ""
    for name in ("Fourier", "DPL", "LS"):
        v = S.branch_modes(1e-6, MODELS[name])[0][0]
        rel = abs(v / ADIA - 1.0)
        if rel > worst:
            worst, where = rel, "%s v_p=%.15f" % (name, v)
    return ("max relative error of v_p(w=1e-6) vs sqrt(1+eps)", where, 1e-9, worst, [])


def bk03_high_frequency_limit():
    """w -> inf: Fourier -> isothermal 1.0, LS -> the GN-II fast root."""
    v_f = S.branch_modes(1e3, MODELS["Fourier"])[0][0]
    v_l = S.branch_modes(1e3, MODELS["LS"])[0][0]
    e_f = abs(v_f - 1.0)
    e_l = abs(v_l / GN2_FAST - 1.0)
    return ("|v_p(1e3) - limit|: Fourier->1.0, LS->1.1705367195742484",
            "Fourier %.6e, LS %.6e" % (e_f, e_l), "1e-6 / 1e-5",
            (e_f, e_l), [])


def bk04_debye_peak():
    """Zener/Lifshitz-Roukes shape: one interior maximum, height ~ Delta/2, at w*tau ~ 1."""
    ws = np.logspace(-1, 1, 2001)
    _v, q = S.elastic_branch(ws, MODELS["Fourier"])
    i = int(np.argmax(q))
    interior = 0 < i < len(ws) - 1
    peak_w, peak_q = float(ws[i]), float(q[i])
    e_pos = abs(peak_w * TAU - 1.0)                            # 0.099 measured
    e_hgt = abs(peak_q / (0.5 * DELTA) - 1.0)                  # 0.102 measured
    return ("Debye peak: uniqueness, position vs 1/tau, height vs Delta/2",
            "interior=%s w*=%0.4f Q*=%.5f (Delta/2=%.5f)" % (interior, peak_w, peak_q, 0.5 * DELTA),
            "interior (0/1), |w*tau-1|, |Q*/(Delta/2)-1|",
            (0.0 if interior else 1.0, e_pos, e_hgt), [])


def bk05_attenuation_low_frequency():
    """Rayleigh regime: alpha proportional to w^2, so alpha/w^2 is constant."""
    vals = [alpha_elastic(w, MODELS["Fourier"]) / w ** 2 for w in (1e-3, 3e-3, 1e-2)]
    spread = (max(vals) - min(vals)) / (sum(vals) / len(vals))
    return ("relative spread of alpha/w^2 over w in [1e-3, 1e-2] (Fourier)",
            "alpha/w^2 = %.6e +- %.1e" % (sum(vals) / len(vals), 0.5 * (max(vals) - min(vals))),
            1e-3, spread, [])


def bk06_attenuation_high_frequency():
    """Bounded attenuation: alpha saturates, it does not grow without limit."""
    out, worst = [], 0.0
    for name, ref in (("Fourier", 0.05), ("LS", None)):
        a1 = alpha_elastic(1e2, MODELS[name])
        a2 = alpha_elastic(1e3, MODELS[name])
        rel = abs(a2 - a1) / abs(a2)
        out.append("%s: alpha(1e2)=%.6f alpha(1e3)=%.6f" % (name, a1, a2))
        worst = max(worst, rel)
    return ("relative change of alpha between w=1e2 and w=1e3 (saturation)",
            "; ".join(out), 1e-3, worst, [])


def bk07_lossless_hyperbolic():
    """GN-II: zero loss, and the two speeds are the closed form, frequency-independent."""
    worst_q, worst_v = 0.0, 0.0
    for w in (0.1, 1.0, 10.0, 100.0):
        m = S.branch_modes(w, MODELS["GN-II"])
        for v, q in m:
            worst_q = max(worst_q, abs(q))
        vs = sorted((m[0][0], m[1][0]))
        worst_v = max(worst_v, abs(vs[0] / GN2_SLOW - 1.0), abs(vs[1] / GN2_FAST - 1.0))
    return ("GN-II: max |Q^-1| and max relative speed error vs closed form",
            "max|Q^-1| = %.3e, max speed rel. err = %.3e" % (worst_q, worst_v),
            "1e-12 (both)", (worst_q, worst_v), [])


def bk08_stability():
    """No growing mode: every bar-mode root must have Re s <= 0."""
    worst, where = -1e9, ""
    for name, p in MODELS.items():
        for K in (0.01, 0.1, 1.0, 10.0, 100.0):
            r = S.bar_s_roots(K, p)
            if len(r) == 0:
                continue
            m = max(z.real for z in r)
            if m > worst:
                worst, where = m, "%s, K=%g" % (name, K)
    return ("max Re s over 6 models x 5 wavenumbers (growth if > 0)",
            "%0.3e (%s)" % (worst, where), 1e-12, worst, [])


BENCH = [
    ("BK-01", "branch structure", bk01_branch_structure, "exact"),
    ("BK-02", "low-frequency adiabatic limit", bk02_adiabatic_limit, "1e-9"),
    ("BK-03", "high-frequency limit", bk03_high_frequency_limit, "1e-6 / 1e-5"),
    ("BK-04", "thermoelastic damping peak", bk04_debye_peak, "0 / 0.20 / 0.15"),
    ("BK-05", "attenuation ~ w^2 (low frequency)", bk05_attenuation_low_frequency, "1e-3"),
    ("BK-06", "attenuation saturation (high frequency)", bk06_attenuation_high_frequency, "1e-3"),
    ("BK-07", "lossless hyperbolic model (GN-II)", bk07_lossless_hyperbolic, "1e-12"),
    ("BK-08", "stability of bar modes", bk08_stability, "1e-12"),
]


def run_benchmarks():
    rows, failures = [], 0
    for bid, fam, fn, tol in BENCH:
        desc, measured, reftxt, err, notes = fn()
        if isinstance(err, bool):
            ok, ermax = err, float(not err)
        elif isinstance(err, (list, tuple)):
            nums = [float(x) for x in err]
            ok = all(n <= float(t) for n, t in zip(nums, _tol_list(tol)))
            ermax = max(nums)
        elif tol == "exact":
            ok, ermax = (int(err) == 0), float(err)
        else:
            ok = float(err) <= float(tol)
            ermax = float(err)
        if not ok:
            failures += 1
            for n in notes:
                print("  detail: " + n)
        rows.append(dict(benchmark_id=bid, family=fam, quantity=desc, measured=measured,
                         reference=reftxt, tolerance=tol, error=ermax,
                         verdict="PASS" if ok else "FAIL"))
        print("%s %s %-42s %s (tol %s)" % ("PASS" if ok else "FAIL", bid, fam, measured, tol))
    return rows, failures


def _tol_list(tol):
    """Tolerance string -> list of floats; separators are '/', spaces or commas."""
    return [float(t) for t in tol.replace("/", " ").replace(",", " ").split()]


def main(argv):
    check_only = "--check" in argv
    rows, failures = run_benchmarks()
    if check_only:
        if failures:
            print("FAIL %d benchmark(s) out of tolerance" % failures)
            return 1
        print("PASS all benchmarks (n=%d, failures=0)" % len(rows))
        return 0
    out = os.path.join(HERE, "bench_atlas_results.csv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["benchmark_id", "family", "quantity", "measured",
                                           "reference", "tolerance", "error", "verdict"])
        w.writeheader()
        w.writerows(rows)
    print("wrote %s (%d rows)" % (os.path.basename(out), len(rows)))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
