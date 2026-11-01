#!/usr/bin/env python3
"""Checker for BK-10 (`bench_thermoelastic.py`).

It re-runs the benchmark and then asserts the things a reader would otherwise
have to take on trust:

  1. every row in the CSV is PASS, and the CSV agrees with a fresh run;
  2. the decoupling row is anchored on the *classical* Rayleigh value
     0.9194016868 c_S, not on a number this file produced earlier;
  3. the sign that decides the physics (beta T = -d phi) is the one that makes
     dissipative models decay and lossless models neutral - i.e. the two rows
     "no growing surface mode" and "GN-II and MGT carry no attenuation" are both
     present, which is only possible with that sign;
  4. the surface family is no longer marked partial in the coverage map, and the
     BK-10 id used there is the one this file writes;
  5. nothing in the file names a link, a drive id or a library folder.

Exit 0 with a line starting with PASS.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "bench_thermoelastic_results.csv")
sys.path.insert(0, HERE)
import bench_thermoelastic as B                                    # noqa: E402

fails = []


def check(name, ok, detail=""):
    print(("  ok   " if ok else "  FAIL ") + name + ("  [" + detail + "]" if detail else ""))
    if not ok:
        fails.append(name)


def rows(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


check("the benchmark writes a CSV", os.path.exists(CSV), CSV)
res = rows(CSV)
check("it holds the six BK-10 rows", len(res) == 6, str(len(res)))
check("every row passes", all(r["verdict"] == "PASS" for r in res),
      ", ".join(r["quantity_checked"] for r in res if r["verdict"] != "PASS"))
check("every row is BK-10", {r["benchmark_id"] for r in res} == {"BK-10"},
      str({r["benchmark_id"] for r in res}))

# 1. a fresh run reproduces the file
before = {r["quantity_checked"]: r["measured"] for r in res}
fails_now = B.run(HERE)
check("a fresh run still fails nothing", fails_now == 0, str(fails_now))
after = {r["quantity_checked"]: r["measured"] for r in rows(CSV)}
check("the CSV is reproducible", before == after,
      ", ".join(k for k in before if before[k] != after.get(k)))

# 2. the decoupling anchor is the classical value
check("the elastic anchor is the classical Rayleigh ratio",
      abs(B.C_R / B.CS - 0.9194016868) < 1e-9, "%.10f" % (B.C_R / B.CS))
dec = [r for r in res if "beta -> 0" in r["quantity_checked"]]
check("the decoupling row is anchored on it, not on itself",
      len(dec) == 1 and "0.9194016868" in dec[0]["measured"], dec[0]["measured"] if dec else "")

# 3. both halves of the sign test are present and passing
grow = [r for r in res if "growing surface mode" in r["quantity_checked"]]
neut = [r for r in res if "no attenuation" in r["quantity_checked"]]
check("the sign test is present in both directions",
      len(grow) == 1 and len(neut) == 1 and grow[0]["verdict"] == "PASS" and neut[0]["verdict"] == "PASS",
      (grow[0]["measured"] if grow else "-") + " | " + (neut[0]["measured"] if neut else "-"))

# 4. the coverage map
cov = rows(os.path.join(HERE, "atlas_case_coverage.csv"))
surf = [c for c in cov if c["wave_family"] == "surface (Rayleigh)"]
check("the surface family is covered", surf and all(c["coverage"] == "yes" for c in surf),
      "%d rows" % len(surf))
check("its cases name BK-10", surf and all("BK-10" in c["applicable_benchmarks"] for c in surf),
      surf[0]["applicable_benchmarks"] if surf else "")
cnt = {}
for c in cov:
    cnt[c["coverage"]] = cnt.get(c["coverage"], 0) + 1
check("the coverage split is 34 full / 0 partial / 6 none",
      cnt == {"yes": 34, "no": 6}, str(dict(cnt)))

# 5. hygiene
for path in (os.path.join(HERE, "bench_thermoelastic.py"), CSV):
    text = open(path, encoding="utf-8").read()
    check("%s names no link or drive id" % os.path.basename(path),
          not re.search(r"https?://|drive\.google|1[A-Za-z0-9_-]{20,}", text))

if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (BK-10=%d rows, all PASS, coverage=%d/%d of %d)"
      % (len(res), cnt["yes"], cnt["no"], len(cov)))
