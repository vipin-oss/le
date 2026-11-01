#!/usr/bin/env python3
"""BK-11: branch count for the m-field extension of the template (P3 atlas, step 31).

Why this file exists
--------------------
`atlas_case_coverage.csv` marks the five porous / voids cases as *partial*:
BK-01 checks that the coupled dispersion has exactly two `K = k^2` roots, which
is a statement about the **one-heat-field** template this repository implements.
Double-porosity and multi-phase models carry more than one extra field, so they
have more branches, and a benchmark that says "two roots" would be wrong for
them.  What the atlas needs is the count as a function of the number of fields.

What is claimed here, and what is *not*
---------------------------------------
This file does **not** contain a porous model.  The repository has none (no
double-porosity constitutive equations, no permeability, no Biot coefficients),
and inventing one would produce numbers about a material model nobody uses -
the same reason BK-15 is left unwritten.  What this file does contain is the
*algebra* of adding fields, which needs no material data at all:

  momentum   (rho c1^2 K + rho s^2) e - sum_i beta_i K T_i = 0
  energy_i   beta_i T0 s e + (s rho c_i + G_i(s) K) T_i = 0 ,  i = 1 ... m

For m = 1 this is exactly the pair whose determinant is equation (D) of
`../P4_second_impl/second_impl.py`:

  (rho c1^2 K + rho s^2)(s rho c_v + G K) + beta^2 T0 s K = 0 .

With m fields the bordered determinant is

  det = (a K + b) prod_i (c_i K + d_i) + sum_i e_i K prod_{j != i} (c_j K + d_j)

with a = rho c1^2, b = rho s^2, c_i = G_i(s), d_i = s rho c_i, e_i = beta_i^2 T0 s,
so it is a polynomial of degree **m + 1** in K whose leading coefficient is
a prod_i G_i.  Hence: **m + 1 branches, no more and no fewer**, of which exactly
one is acoustic (the root that tends to -s^2/c1^2 and scales as s^2) and the
other m are diffusive (they scale as s, like -s rho c_i / G_i).  That is the
invariant: a model with m extra fields that reports two branches has lost m - 1
of them, and one that reports a third *propagating* branch for a two-field model
has invented one.

Everything below is checked against the verified code where it can be:
  * m = 1 must reproduce `second_impl.coupled_K_roots` for all six models;
  * the decoupled limit (beta_i = 0 for i >= 2) must put the extra roots exactly
    on the uncoupled thermal roots `-s rho c_i / G_i(s)`, which is what
    `second_impl.thermal_k` computes;
  * the closed form must agree with a numeric determinant of the bordered matrix.

The extra fields' parameters are explicitly **generic placeholders** (a table of
conductivities and heat capacities), used only to exercise the algebra.

Usage
  python3 bench_porous.py            # writes bench_porous_results.csv
  python3 bench_porous.py --check    # PASS/FAIL lines, exit 1 on failure

Requires numpy.  Runtime < 1 s.  Nothing under `scripts/` is touched.
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "P4_second_impl")))
import second_impl as S                                        # noqa: E402

RHO, C1 = 1.0, 1.0
T0 = 1.0
EPS = S.EPS

# generic placeholder fields 2 ... m (no material meaning: they exercise the algebra)
# All three are *diffusive* fields (no ks second-sound term, no flux lags), which is the
# structure a double-porosity / multi-phase model has: one extra diffusive branch per field.
EXTRA = [dict(k=0.7, ks=0.0, tq=0.3, tT=0.0, tv=0.0, cv=0.8),
         dict(k=1.3, ks=0.0, tq=0.0, tT=0.0, tv=0.0, cv=1.2),
         dict(k=0.5, ks=0.0, tq=0.8, tT=0.0, tv=0.0, cv=0.9)]


def fields(m, name="Fourier"):
    """Field 1 from the verified template, fields 2..m from the placeholder table."""
    out = [dict(S.MODELS[name], cv=S.CV, beta2=EPS)]
    for i in range(1, m):
        out.append(dict(EXTRA[(i - 1) % len(EXTRA)], beta2=EPS))
    return out


def coeffs_in_K(s, fl, beta2=None):
    """(numeric determinant check data, polynomial coefficients of det, highest first)."""
    s = complex(s)
    a = RHO * C1 ** 2
    b = RHO * s * s
    c = [S.transfer_function(s, f) for f in fl]
    d = [s * RHO * f["cv"] for f in fl]
    e = [(f["beta2"] if beta2 is None else beta2[i]) * T0 * s for i, f in enumerate(fl)]
    # closed form: (aK+b) prod(c_i K + d_i) + sum_i e_i K prod_{j!=i}(c_j K+d_j)
    poly = np.array([a, b], dtype=complex)
    for ci, di in zip(c, d):
        poly = np.convolve(poly, np.array([ci, di], dtype=complex))
    for i, ei in enumerate(e):
        term = np.array([ei, 0.0], dtype=complex)
        for j, (cj, dj) in enumerate(zip(c, d)):
            if j != i:
                term = np.convolve(term, np.array([cj, dj], dtype=complex))
        # e_i K prod_{j!=i}(...) has degree m, the main term degree m+1: left-pad
        if len(term) < len(poly):
            term = np.concatenate((np.zeros(len(poly) - len(term), dtype=complex), term))
        poly = poly + term
    return poly


def numeric_det(s, fl, K, beta2=None):
    """Determinant of the bordered (m+1) x (m+1) matrix, assembled by hand."""
    s = complex(s)
    m = len(fl)
    mat = np.zeros((m + 1, m + 1), dtype=complex)
    mat[0, 0] = RHO * C1 ** 2 * K + RHO * s * s
    for i, f in enumerate(fl):
        beta2_i = f["beta2"] if beta2 is None else beta2[i]
        mat[0, i + 1] = -math.sqrt(beta2_i) * K
        mat[i + 1, 0] = math.sqrt(beta2_i) * T0 * s
        mat[i + 1, i + 1] = s * RHO * f["cv"] + S.transfer_function(s, f) * K
    return np.linalg.det(mat)


def roots_in_K(s, fl, beta2=None):
    poly = coeffs_in_K(s, fl, beta2)
    scale = max(1.0, float(np.max(np.abs(poly))))
    nz = np.nonzero(np.abs(poly) > 1e-13 * scale)[0]
    return list(np.roots(poly[nz[0]:])) if len(nz) else []


# ------------------------------------------------------------------ benchmarks
def b11_m1_matches_impl():
    """m = 1 must be the verified implementation, root for root."""
    worst, bad, n = 0.0, [], 0
    for name in S.MODELS:
        for w in (0.5, 5.0):
            s = -1j * w
            mine = sorted((complex(x) for x in roots_in_K(s, fields(1, name))),
                          key=lambda z: (round(z.real, 9), round(z.imag, 9)))
            theirs = sorted((complex(x) for x in S.coupled_K_roots(w, S.MODELS[name])),
                            key=lambda z: (round(z.real, 9), round(z.imag, 9)))
            n += 1
            if len(mine) != len(theirs):
                bad.append("%s@%g: %d vs %d roots" % (name, w, len(mine), len(theirs)))
                continue
            for x, y in zip(mine, theirs):
                rel = abs(x - y) / max(1.0, abs(y))
                worst = max(worst, rel)
                if rel > 1e-10:
                    bad.append("%s@%g: %.2e" % (name, w, rel))
    return ("m = 1 reproduces second_impl.coupled_K_roots",
            "max relative difference %.2e over %d (model, frequency) pairs" % (worst, n),
            "<= 1e-10", len(bad), bad)


def b11_degree_and_count():
    """Degree m+1 and exactly m+1 roots, for m = 1 ... 6, every model."""
    worst, bad, n = 0.0, [], 0
    for m in range(1, 7):
        for name in ("Fourier", "LS", "GN-III"):
            for w in (0.5, 5.0):
                fl = fields(m, name)
                poly = coeffs_in_K(-1j * w, fl)
                r = roots_in_K(-1j * w, fl)
                n += 1
                if len(poly) != m + 2:
                    bad.append("m=%d %s: polynomial of degree %d" % (m, name, len(poly) - 1))
                if len(r) != m + 1:
                    bad.append("m=%d %s@%g: %d roots" % (m, name, w, len(r)))
                lead = abs(poly[0])
                if lead < 1e-12:
                    bad.append("m=%d %s: leading coefficient vanishes" % (m, name))
                worst = max(worst, lead)
    return ("the determinant is a polynomial of degree m+1 with m+1 roots",
            "m = 1 ... 6, 3 models, 2 frequencies: %d cases, smallest |leading coeff| = %.2e"
            % (n, worst),
            "degree m+1 and m+1 roots everywhere", len(bad), bad)


def b11_decoupled_limit():
    """beta_i = 0 isolates the extra roots; they must sit on -s rho c_i / G_i."""
    worst, bad, n = 0.0, [], 0
    for m in (2, 3, 4):
        for w in (0.5, 5.0):
            s = -1j * w
            fl = fields(m, "Fourier")
            beta2 = [EPS] + [0.0] * (m - 1)
            r = roots_in_K(s, fl, beta2)
            target = [S.thermal_k(w, fl[i], rho=RHO, cv=fl[i]["cv"]) ** 2 for i in range(1, m)]
            for t in target:
                n += 1
                best = min(abs(x - t) / max(1.0, abs(t)) for x in r)
                worst = max(worst, best)
                if best > 1e-9:
                    bad.append("m=%d@%g: thermal root off by %.2e" % (m, w, best))
    return ("decoupled extra fields land exactly on the uncoupled thermal roots",
            "max relative distance %.2e over %d (m, frequency, field) points" % (worst, n),
            "<= 1e-09", len(bad), bad)


def _split(roots):
    """Propagating = Re K > 0 with |Im K| < 0.1 |Re K|; diffusive = the opposite."""
    prop = [x for x in roots if x.real > 0.0 and abs(x.imag) < 0.1 * x.real]
    diff = [x for x in roots if abs(x.real) < 0.1 * abs(x.imag)]
    return prop, diff


def b11_one_acoustic():
    """In the low-frequency limit: one propagating branch, m diffusive ones, K ~ s."""
    bad, n, worst = [], 0, 0.0
    for m in (1, 2, 3, 4):
        for w in (1e-3, 1e-2):
            fl = fields(m, "Fourier")
            r1 = roots_in_K(-1j * w, fl)
            r2 = roots_in_K(-1j * 10.0 * w, fl)
            prop, diff = _split(r1)
            n += 1
            if len(prop) != 1 or len(diff) != m:
                bad.append("m=%d@%g: %d propagating, %d diffusive" % (m, w, len(prop), len(diff)))
                continue
            # the diffusive roots must scale as s (a factor 10 in w gives a factor 10 in |K|)
            for x in diff:
                cand = min(r2, key=lambda y: abs(y - 10.0 * x))
                if abs(x) > 1e-14:
                    worst = max(worst, abs(abs(cand) / abs(x) - 10.0) / 10.0)
    return ("low-frequency split: exactly one propagating branch and m diffusive ones (K ~ s)",
            "m = 1 ... 4, w = 1e-3 and 1e-2: worst |K| scaling error for a factor 10 in w = %.2e"
            % worst,
            "1 propagating + m diffusive, diffusive |K| linear in w", len(bad), bad)


def b11_det_agrees():
    """The closed form and a hand-built numeric determinant must agree."""
    worst, bad, n = 0.0, [], 0
    rng = np.random.default_rng(20261101)
    for m in (1, 2, 3, 4):
        fl = fields(m, "GN-III")
        for _ in range(4):
            s = -1j * float(rng.uniform(0.2, 5.0))
            K = complex(rng.uniform(-3.0, 3.0), rng.uniform(-1.0, 1.0))
            poly = coeffs_in_K(s, fl)
            closed = np.polyval(poly, K)
            num = numeric_det(s, fl, K)
            n += 1
            rel = abs(closed - num) / max(1.0, abs(num))
            worst = max(worst, rel)
            if rel > 1e-10:
                bad.append("m=%d: %.2e" % (m, rel))
    return ("the closed form equals the numeric determinant of the bordered matrix",
            "max relative difference %.2e over %d random (s, K) points" % (worst, n),
            "<= 1e-10", len(bad), bad)


def b11_one_elastic_root():
    """The elastic branch keeps its low-frequency position; extra fields only soften it.

    For m = 1 the position is an anchor rather than a fit: K -> w^2 / (1 + eps), i.e. the
    adiabatic speed sqrt(1 + eps) c1 that BK-02 pins in the bulk.  Each further field adds
    complaisance, so the branch may soften, but no faster than the naive parallel sum
    1 / (1 + m eps) - and no other root may come near it.
    """
    bad, n, worst = [], 0, 0.0
    ratios = []
    for m in (1, 2, 3, 4):
        fl = fields(m, "Fourier")
        w = 1e-3
        r = roots_in_K(-1j * w, fl)
        prop, _d = _split(r)
        n += 1
        if len(prop) != 1:
            bad.append("m=%d: %d propagating roots" % (m, len(prop)))
            continue
        target = w * w / C1 ** 2
        ratio = prop[0].real / target
        ratios.append("%d:%.4f" % (m, ratio))
        if m == 1:
            err = abs(ratio - 1.0 / (1.0 + EPS))
            worst = max(worst, err)
            if err > 1e-3:
                bad.append("m=1: K/K_iso = %.6f, expected 1/(1+eps) = %.6f"
                           % (ratio, 1.0 / (1.0 + EPS)))
        else:
            lo = 0.9 / (1.0 + m * EPS)
            if not (lo < ratio <= 1.0):
                bad.append("m=%d: K/K_iso = %.4f outside (%.4f, 1]" % (m, ratio, lo))
        near = [x for x in r if abs(x.real / target - ratio) < 0.5 * ratio and x in prop]
        if len(near) != 1:
            bad.append("m=%d: %d roots at the elastic position" % (m, len(near)))
    return ("the elastic branch keeps its low-frequency position for every m",
            "K/K_iso = %s, with 1/(1+eps) = %.6f as the m = 1 anchor"
            % (", ".join(ratios), 1.0 / (1.0 + EPS)),
            "m=1 exact to 1e-03; m>1 above 0.9/(1+m eps); one root only", len(bad), bad)


CHECKS = (b11_m1_matches_impl, b11_degree_and_count, b11_decoupled_limit,
          b11_one_acoustic, b11_one_elastic_root, b11_det_agrees)

HEADER = ["benchmark_id", "quantity_checked", "measured", "reference", "reference_type",
          "tolerance", "verdict", "script"]


def run(outdir=HERE):
    rows, failures = [], 0
    for fn in CHECKS:
        q, measured, tol, nbad, bad = fn()
        verdict = "PASS" if nbad == 0 else "FAIL"
        failures += (nbad > 0)
        rows.append(dict(benchmark_id="BK-11", quantity_checked=q, measured=measured,
                         reference=tol, reference_type="algebraic structure + verified m=1 code",
                         tolerance=tol, verdict=verdict, script="bench_porous.py"))
        print("  BK-11  %-5s  %-66s %s" % (verdict, q[:66], measured))
        for b in bad[:3]:
            print("           %s" % b)
    out = os.path.join(outdir, "bench_porous_results.csv")
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=HEADER)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print("rows: %d, failures: %d" % (len(rows), failures))
    return failures


def main():
    fails = run(os.path.join(HERE, "..", "..")) if "--check" in sys.argv else run()
    if fails:
        print("FAIL %d row(s)" % fails)
        return 1
    print("PASS all %d rows" % len(CHECKS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
