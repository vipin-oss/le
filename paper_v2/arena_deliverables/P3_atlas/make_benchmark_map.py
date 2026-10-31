#!/usr/bin/env python3
"""Map the 40 proposed atlas problems onto the eight executable benchmarks.

Reads `atlas_plan.csv` (produced by `make_atlas_plan.py`), assigns every problem
the benchmark families that its wave family must satisfy, and writes
`benchmark_map.csv`.  The assignment is by wave family, not by paper: the papers
are known only at title/metadata level (`full_text_read = no`), so no
paper-specific secular equation, parameter set or figure is claimed.

Usage:  python3 make_benchmark_map.py [--check]
`--check` writes to a temporary file and verifies the output is stable.
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# wave family -> benchmark ids that an implementation of that family must pass
FAMILY_BENCH = {
    "bulk":                ["BK-01", "BK-02", "BK-03", "BK-05", "BK-06", "BK-07", "BK-08"],
    "porous / voids":      ["BK-01", "BK-05", "BK-08"],
    "multifield":          ["BK-01", "BK-03", "BK-08"],
    "surface (Rayleigh)":  ["BK-01", "BK-02", "BK-08"],
    "Lamb / plate":        ["BK-01", "BK-02", "BK-04", "BK-08"],
    "interface / layered": ["BK-01", "BK-03", "BK-08"],
    "shear / SH":          ["BK-01", "BK-03", "BK-07", "BK-08"],
    "TED / damping":       ["BK-04", "BK-08"],
}
FIELDS = ["problem_id", "wave_family", "bibkey", "DOI", "validation_target_proposed",
          "benchmark_ids", "n_benchmarks", "tolerance_ref", "paper_equation_read",
          "paper_parameters_read", "benchmark_status", "what_is_still_missing"]


def build():
    with open(os.path.join(HERE, "atlas_plan.csv"), newline="") as fh:
        plan = list(csv.DictReader(fh))
    out = []
    for r in plan:
        fam = r["wave_family"]
        if fam not in FAMILY_BENCH:
            raise SystemExit("unmapped wave family: %r" % fam)
        bids = FAMILY_BENCH[fam]
        out.append(dict(
            problem_id=r["problem_id"],
            wave_family=fam,
            bibkey=r["bibkey"],
            DOI=r["DOI"],
            validation_target_proposed=r["validation_target_proposed"],
            benchmark_ids=";".join(bids),
            n_benchmarks=len(bids),
            tolerance_ref=";".join(bids) + " (bench_tolerances.csv)",
            paper_equation_read="no",
            paper_parameters_read="no",
            benchmark_status="invariant-only: the executable checks test the model class, "
                             "not this paper's own secular equation",
            what_is_still_missing="read the paper's dispersion relation and parameter table, "
                                  "then add a paper-specific reference value at the same tolerance",
        ))
    return out


def main(argv):
    rows = build()
    dest = os.path.join(HERE, "benchmark_map.csv")
    if "--check" in argv:
        dest = os.path.join(HERE, ".benchmark_map_check.csv")
    with open(dest, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    fams = sorted({r["wave_family"] for r in rows})
    print("wrote %s (%d problems, %d families)" % (os.path.basename(dest), len(rows), len(fams)))
    if "--check" in argv:
        a = open(os.path.join(HERE, "benchmark_map.csv")).read()
        b = open(dest).read()
        os.remove(dest)
        ok = a == b
        print("%s --check: output matches the committed file" % ("PASS" if ok else "FAIL"))
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
