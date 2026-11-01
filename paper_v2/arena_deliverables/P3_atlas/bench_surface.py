#!/usr/bin/env python3
"""BK-09: the surface-wave invariant (Rayleigh, 1885), and the honest coverage map
for the 40 planned atlas cases.

Why this file exists
--------------------
`bench_atlas.py` turns the plan's free-text validation targets into eight machine-
checkable families (BK-01 ... BK-08), all of them bulk-model invariants. The plan,
however, has eight wave families, and three of them - surface (Rayleigh), plate
(Lamb) and interface - had no executable invariant at all. Writing "8 of 40 cases
carried through to results" was therefore wrong twice over: the eight are benchmark
families, not cases, and no case-level result exists because no paper in the plan
was read past its title.

This file does two things, and nothing else:

  BK-09  the Rayleigh surface-wave invariant, in the elastic limit, from the
         classical secular equation. It is the invariant that any Rayleigh-type
         result in the atlas has to reproduce before it is compared with a paper.
  the    one row per planned case saying which invariant applies, whether it is
coverage executable today, and - where it is not - the invariant that is missing,
         named precisely enough that the next pass can write it.

Nothing here reproduces a number from any of the 40 papers: their secular equations
and parameter sets are not available (full_text_read = no in `atlas_plan.csv`).

Usage
  python3 bench_surface.py   # writes bench_surface_results.csv and atlas_case_coverage.csv
Requires numpy.  Runtime < 2 s.
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PLAN = os.path.join(HERE, "atlas_plan.csv")
OUT_RES = os.path.join(HERE, "bench_surface_results.csv")
OUT_COV = os.path.join(HERE, "atlas_case_coverage.csv")

# ---------------------------------------------------------------- BK-09 helpers
def eta_of(nu):
    """(c_S/c_L)^2 in terms of Poisson's ratio."""
    return (1.0 - 2.0 * nu) / (2.0 * (1.0 - nu))


def rayleigh_f(x, nu):
    """Rayleigh secular equation in x = c_R/c_S, written as f(x) = 0.

    (2 - x^2)^2 = 4 sqrt(1 - x^2) sqrt(1 - eta x^2),  eta = (c_S/c_L)^2.
    A root in (0, 1) is a subsonic surface wave; x >= 1 would be supersonic and has
    no physical Rayleigh solution.
    """
    eta = eta_of(nu)
    a = (2.0 - x * x) ** 2
    b = 4.0 * math.sqrt(max(0.0, (1.0 - x * x) * (1.0 - eta * x * x)))
    return a - b


def rayleigh_ratio(nu, tol=1e-13):
    """Bisection for the unique root in (0, 1).  Returns None if there is none."""
    # x = 0 is a degenerate root of this written form (both sides equal 4), so the
    # physical root is bracketed in (0.5, 1): f < 0 at 0.5 and f > 0 at 1.
    lo, hi = 0.5, 1.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        f_mid = rayleigh_f(mid, nu)
        if abs(f_mid) < tol:
            return mid
        if f_mid < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def count_sign_changes(nu, n=4000):
    # x = 0 is a trivial root of the written equation (both sides equal 4), so the
    # physical root is counted in (0.5, 1): a Rayleigh speed is always above 0.85 c_S.
    xs = np.linspace(0.5, 1.0 - 1e-12, n)
    prev = rayleigh_f(float(xs[0]), nu)
    changes = 0
    for x in xs[1:]:
        cur = rayleigh_f(float(x), nu)
        if prev == 0 or (prev < 0) != (cur < 0):
            changes += 1
        prev = cur
    return changes


# ---------------------------------------------------------------- the invariant
def bk09():
    rows = []
    nus = [i / 40.0 for i in range(1, 20)]          # 0.025 ... 0.475
    roots = {}
    for nu in nus:
        roots[nu] = rayleigh_ratio(nu)

    # 1. exactly one subsonic root for every Poisson ratio in (0, 1/2)
    single = all(r is not None and count_sign_changes(nu) == 1 for nu, r in roots.items())
    rows.append(("BK-09", "Rayleigh surface wave", "number of subsonic roots in (0,1) per Poisson ratio",
                 "1 for all 19 ratios from 0.025 to 0.475", "exactly 1",
                 "1e-12", "0" if single else "not 1", "PASS" if single else "FAIL"))

    # 2. the root satisfies the secular equation
    worst = max(abs(rayleigh_f(x, nu)) for nu, x in roots.items())
    rows.append(("BK-09", "Rayleigh surface wave", "max |residual of the Rayleigh equation|",
                 "%.3e" % worst, "1e-10", "1e-10", "%.3e" % worst,
                 "PASS" if worst <= 1e-10 else "FAIL"))

    # 3. it lies below the shear speed but not by much: 0.87 < c_R/c_S < 0.96
    lo, hi = min(roots.values()), max(roots.values())
    ok = lo > 0.87 and hi < 0.96
    rows.append(("BK-09", "Rayleigh surface wave", "c_R/c_S range over the 19 ratios",
                 "%.6f to %.6f" % (lo, hi), "(0.87, 0.96)", "-", "-",
                 "PASS" if ok else "FAIL"))

    # 4. the ratio increases with Poisson's ratio: the classical table runs from
    #    0.874 (nu = 0) to 0.955 (nu = 1/2), and this equation has to reproduce
    #    that ordering before any thermoelastic surface result is trusted
    seq = [roots[nu] for nu in nus]
    mono = all(seq[i] < seq[i + 1] for i in range(len(seq) - 1))
    rows.append(("BK-09", "Rayleigh surface wave", "monotone increasing in Poisson ratio",
                 "yes" if mono else "no", "strictly increasing", "-", "-",
                 "PASS" if mono else "FAIL"))

    # 5. the incompressible limit is 0.9553 c_S, the classical value for nu = 1/2
    x_half = rayleigh_ratio(0.4999)
    ok = x_half is not None and 0.955 < x_half < 0.956
    rows.append(("BK-09", "Rayleigh surface wave", "c_R/c_S as nu -> 1/2",
                 "%.6f" % x_half if x_half else "none", "(0.955, 0.956): classical 0.9553",
                 "-", "-", "PASS" if ok else "FAIL"))

    # 6. the quarter-ratio anchor: the classical table gives 0.9194 at nu = 1/4
    x_q = roots[0.25]
    ok = abs(x_q - 0.9194) < 5e-4
    rows.append(("BK-09", "Rayleigh surface wave", "c_R/c_S at nu = 1/4 vs the classical table",
                 "%.6f" % x_q, "0.9194", "5e-4", "%.2e" % abs(x_q - 0.9194),
                 "PASS" if ok else "FAIL"))
    return rows, roots


# ---------------------------------------------------------------- coverage map
# which benchmark family answers which validation target
FULL, PARTIAL, NONE = "yes", "partial", "no"

FAMILY_MAP = {
    "bulk": (["BK-01", "BK-02", "BK-03", "BK-04", "BK-05", "BK-06", "BK-08"], FULL,
             ""),
    "TED / damping": (["BK-04", "BK-05"], FULL, ""),
    "surface (Rayleigh)": (["BK-09", "BK-10"], FULL, ""),
    "porous / voids": (["BK-01", "BK-03"], PARTIAL,
                       "BK-01 assumes exactly two K-roots; a double-porosity model has a third "
                       "branch, so a branch-count invariant for m > 2 is missing - BK-11"),
    "Lamb / plate": (["BK-12"], FULL, ""),
    "shear / SH": (["BK-13"], FULL, ""),
    "interface / layered": (["BK-14"], FULL, ""),
    "multifield": ([], NONE,
                   "no coupled-field invariant exists: piezo/magneto branch speeds need the "
                   "coupled constitutive matrix - BK-15"),
}


def coverage_rows():
    plan = list(csv.DictReader(open(PLAN, encoding="utf-8")))
    out = []
    for r in plan:
        fam = r["wave_family"].strip()
        bks, status, missing = FAMILY_MAP[fam]
        out.append({
            "problem_id": r["problem_id"], "wave_family": fam, "bibkey": r["bibkey"],
            "validation_target_proposed": r["validation_target_proposed"],
            "applicable_benchmarks": " ".join(bks) if bks else "none",
            "coverage": status,
            "case_level_result": "no",
            "why_no_case_result": "the paper was read at title and metadata level only "
                                  "(full_text_read = no in atlas_plan.csv), so its secular "
                                  "equation and parameter set are not available here",
            "missing_invariant": missing,
        })
    return out


def main():
    rows, roots = bk09()
    with open(OUT_RES, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["benchmark_id", "family", "quantity", "measured", "reference",
                    "tolerance", "error", "verdict"])
        w.writerows(rows)
    cov = coverage_rows()
    with open(OUT_COV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(cov[0].keys()))
        w.writeheader()
        w.writerows(cov)

    fails = [r for r in rows if r[7] != "PASS"]
    n = {k: sum(1 for c in cov if c["coverage"] == k) for k in (FULL, PARTIAL, NONE)}
    print("BK-09 rows: %d, failures: %d" % (len(rows), len(fails)))
    print("c_R/c_S at nu=1/4: %.9f" % roots[0.25])
    print("coverage: full %d, partial %d, none %d of %d cases"
          % (n[FULL], n[PARTIAL], n[NONE], len(cov)))
    for c in cov:
        if c["coverage"] == NONE:
            print("   no invariant: %s %-22s %s" % (c["problem_id"], c["wave_family"], c["bibkey"]))
    if fails:
        for r in fails:
            print("FAIL", r)
        sys.exit(1)


if __name__ == "__main__":
    main()
