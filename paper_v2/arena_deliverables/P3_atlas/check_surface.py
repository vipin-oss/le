#!/usr/bin/env python3
"""Check BK-09 and the atlas coverage map.

    cd paper_v2/arena_deliverables/P3_atlas && python3 check_surface.py

Exit 0 and a line starting with PASS only if the surface-wave invariant still passes
and the coverage map still says the same thing about the same 40 cases.
"""
import collections
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "bench_surface_results.csv")
COV = os.path.join(HERE, "atlas_case_coverage.csv")
PLAN = os.path.join(HERE, "atlas_plan.csv")
MAIN = os.path.join(HERE, "bench_atlas_results.csv")
FAM = os.path.join(HERE, "bench_families_results.csv")

fails = []


def check(label, ok, detail=""):
    if ok:
        print("  ok   %s%s" % (label, ("  [%s]" % detail) if detail else ""))
    else:
        print("  FAIL %s%s" % (label, ("  [%s]" % detail) if detail else ""))
        fails.append(label)


def rows(p):
    with open(p, encoding="utf-8") as f:
        return list(csv.DictReader(f))


res = rows(RES)
cov = rows(COV)
plan = rows(PLAN)
main = rows(MAIN)
fam = rows(FAM)

print("== BK-09, the surface-wave invariant ==")
check("it has six rows", len(res) == 6, str(len(res)))
check("every row passes", all(r["verdict"] == "PASS" for r in res),
      ", ".join(r["quantity"] for r in res if r["verdict"] != "PASS"))
check("every row is BK-09", all(r["benchmark_id"] == "BK-09" for r in res))
check("the classical incompressible value is printed", any("0.9553" in r["measured"] for r in res))
check("the quarter-ratio anchor is printed", any(r["measured"].startswith("0.9194") for r in res))
check("the residual is below its tolerance",
      any(float(r["measured"]) < 1e-10 for r in res if "residual" in r["quantity"]))

print("== the coverage map ==")
check("it has one row per planned case", len(cov) == len(plan) == 40, "%d / %d" % (len(cov), len(plan)))
check("the problem ids match the plan exactly",
      [c["problem_id"] for c in cov] == [p["problem_id"] for p in plan])
check("the bibkeys match the plan exactly",
      [c["bibkey"] for c in cov] == [p["bibkey"] for p in plan])
cnt = collections.Counter(c["coverage"] for c in cov)
check("the coverage split is 29 full / 5 partial / 6 none",
      cnt == {"yes": 29, "partial": 5, "no": 6}, str(dict(cnt)))
check("no case claims a case-level result",
      all(c["case_level_result"] == "no" for c in cov))
check("every case says why there is no case-level result",
      all("full_text_read = no" in c["why_no_case_result"] for c in cov))
check("every uncovered case names the invariant that is missing",
      all(c["missing_invariant"].startswith("no ") and re.search(r"BK-1\d", c["missing_invariant"])
          for c in cov if c["coverage"] == "no"))
check("the partial cases say what they are missing",
      all(c["missing_invariant"] for c in cov if c["coverage"] == "partial"))
check("the fully covered cases name only benchmarks that exist",
      all(all(b in {"BK-01", "BK-02", "BK-03", "BK-04", "BK-05", "BK-06", "BK-07",
                    "BK-08", "BK-09", "BK-10", "BK-12", "BK-13", "BK-14"}
              for b in c["applicable_benchmarks"].split())
          for c in cov if c["coverage"] == "yes"))
check("the fully covered families are the six that have an executable invariant",
      {c["wave_family"] for c in cov if c["coverage"] == "yes"}
      == {"bulk", "TED / damping", "surface (Rayleigh)", "Lamb / plate", "shear / SH",
          "interface / layered"},
      ", ".join(sorted({c["wave_family"] for c in cov if c["coverage"] == "yes"})))
check("the three result files together hold %d benchmark rows" % (len(main) + len(res) + len(fam)),
      len(main) == 8 and len(res) == 6 and len(fam) == 14,
      "%d + %d + %d" % (len(main), len(res), len(fam)))
check("every BK-12/13/14 row passes", all(r["verdict"] == "PASS" for r in fam),
      ", ".join(r["quantity"] for r in fam if r["verdict"] != "PASS"))
bks = sorted({r["benchmark_id"] for r in fam})
check("the new families are BK-12, BK-13 and BK-14", bks == ["BK-12", "BK-13", "BK-14"], str(bks))
check("the surface file names no link or drive id",
      not re.search(r"https?://|drive\.google", open(RES, encoding="utf-8").read()))

print()
print("     BK-09: %d rows, all PASS | coverage: full %d, partial %d, none %d of %d"
      % (len(res), cnt["yes"], cnt["partial"], cnt["no"], len(cov)))
if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (BK-09=%d rows, BK-12/13/14=%d rows, coverage=%d/%d/%d of %d)"
      % (len(res), len(fam), cnt["yes"], cnt["partial"], cnt["no"], len(cov)))
