#!/usr/bin/env python3
"""Checker for BK-11 (`bench_porous.py`).

Asserts what a reader should not have to take on trust:

  1. the CSV exists, holds six BK-11 rows and every one is PASS, and a fresh run
     reproduces it;
  2. m = 1 is anchored on the *verified* implementation, not on this file's own
     algebra: `second_impl.coupled_K_roots` must agree to 1e-10;
  3. the branch count is m+1 for m = 1 ... 6 - i.e. the file is not quietly
     dropping the polynomial's degree when the leading coefficient is small;
  4. the decoupled limit lands on `second_impl.thermal_k`, so the extra roots are
     the thermal roots of the extra fields and not some artifact;
  5. the coverage map no longer calls the porous family partial, and its cases
     name BK-11;
  6. the file states plainly that it contains no porous model (it is algebra,
     not invented constitutive data) and names no link or drive id.

Exit 0 with a line starting with PASS.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "bench_porous_results.csv")
sys.path.insert(0, HERE)
import bench_porous as B                                            # noqa: E402
import second_impl as S                                             # noqa: E402

fails = []


def check(name, ok, detail=""):
    print(("  ok   " if ok else "  FAIL ") + name + ("  [" + detail + "]" if detail else ""))
    if not ok:
        fails.append(name)


def rows(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


res = rows(CSV)
check("the benchmark writes a CSV", os.path.exists(CSV), CSV)
check("it holds the six BK-11 rows", len(res) == 6, str(len(res)))
check("every row passes", all(r["verdict"] == "PASS" for r in res),
      ", ".join(r["quantity_checked"] for r in res if r["verdict"] != "PASS"))
check("every row is BK-11", {r["benchmark_id"] for r in res} == {"BK-11"},
      str({r["benchmark_id"] for r in res}))

before = {r["quantity_checked"]: r["measured"] for r in res}
check("a fresh run still fails nothing", B.run(HERE) == 0)
check("the CSV is reproducible", before == {r["quantity_checked"]: r["measured"] for r in rows(CSV)})

# 2. the m = 1 anchor really is the verified implementation
same, worst = True, 0.0
for name in S.MODELS:
    for w in (0.5, 5.0):
        mine = sorted((complex(x) for x in B.roots_in_K(-1j * w, B.fields(1, name))),
                      key=lambda z: (round(z.real, 9), round(z.imag, 9)))
        theirs = sorted((complex(x) for x in S.coupled_K_roots(w, S.MODELS[name])),
                        key=lambda z: (round(z.real, 9), round(z.imag, 9)))
        if len(mine) != len(theirs):
            same = False
            continue
        for x, y in zip(mine, theirs):
            rel = abs(x - y) / max(1.0, abs(y))
            worst = max(worst, rel)
            same = same and rel <= 1e-10
check("m = 1 matches second_impl.coupled_K_roots", same, "max rel %.2e" % worst)

# 3. degree and count
ok, seen = True, []
for m in range(1, 7):
    seen.append(len(B.roots_in_K(-1j * 1.0, B.fields(m, "Fourier"))))
    ok = ok and seen[-1] == m + 1
check("the branch count is m+1 for m = 1 ... 6", ok, str(seen))

# 4. decoupled limit against thermal_k
worst, ok = 0.0, True
for m in (2, 3):
    s = -1j * 1.0
    fl = B.fields(m, "Fourier")
    r = B.roots_in_K(s, fl, [B.EPS] + [0.0] * (m - 1))
    for i in range(1, m):
        t = S.thermal_k(1.0, fl[i], rho=B.RHO, cv=fl[i]["cv"]) ** 2
        d = min(abs(x - t) / max(1.0, abs(t)) for x in r)
        worst = max(worst, d)
        ok = ok and d <= 1e-9
check("the decoupled extra roots are thermal_k roots", ok, "max rel %.2e" % worst)

# 5. coverage map
cov = rows(os.path.join(HERE, "atlas_case_coverage.csv"))
por = [c for c in cov if c["wave_family"] == "porous / voids"]
check("the porous family is covered", por and all(c["coverage"] == "yes" for c in por),
      "%d rows" % len(por))
check("its cases name BK-11", por and all("BK-11" in c["applicable_benchmarks"] for c in por),
      por[0]["applicable_benchmarks"] if por else "")
cnt = {}
for c in cov:
    cnt[c["coverage"]] = cnt.get(c["coverage"], 0) + 1
check("the coverage split is 34 full / 0 partial / 6 none",
      cnt == {"yes": 34, "no": 6}, str(dict(cnt)))

# 6. honesty and hygiene
text = open(os.path.join(HERE, "bench_porous.py"), encoding="utf-8").read()
check("the file says it contains no porous model",
      "does **not** contain a porous model" in text)
check("it names no link or drive id",
      not re.search(r"https?://|drive\.google|1[A-Za-z0-9_-]{20,}", text + open(CSV, encoding="utf-8").read()))

if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (BK-11=%d rows, all PASS, branch count m+1 up to m=6, coverage=%d/%d of %d)"
      % (len(res), cnt["yes"], cnt["no"], len(cov)))
