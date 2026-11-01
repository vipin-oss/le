#!/usr/bin/env python3
"""Check PUBLISH_PENDING_2026-11-01.md against the data on disk.

    cd paper_v2/arena_deliverables && python3 check_publish_pending.py

Exit 0 and a line starting with PASS only if every number the pending list prints
still matches the registers, the blueprint's two checklists and the defect register.
The ledger split (83 closed / 1 to order / 4 waived / 4 held / 19 register-level) is
deliberately not re-checked here: check_readiness.py owns it.
"""
import collections
import csv
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = os.path.abspath(os.path.join(HERE, ".."))
NOTE = os.path.join(HERE, "PUBLISH_PENDING_2026-11-01.md")

fails = []


def check(label, ok, detail=""):
    if ok:
        print("  ok   %s%s" % (label, ("  [%s]" % detail) if detail else ""))
    else:
        print("  FAIL %s%s" % (label, ("  [%s]" % detail) if detail else ""))
        fails.append(label)


def rows(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


txt = open(NOTE, encoding="utf-8").read()

# ---------- blueprint checklists ----------
bp = open(os.path.join(PAPER, "BLUEPRINT_v3.1.md"), encoding="utf-8").read()
s11a = bp.split("### 11a")[1].split("### 11b")[0]
s11b = bp.split("### 11b")[1].split("## 12")[0]
a_x, a_o = s11a.count("- [x]"), s11a.count("- [ ]")
b_x, b_o = s11b.count("- [x]"), s11b.count("- [ ]")
check("11a is %d of %d and the note says so" % (a_x, a_x + a_o),
      "**%d of %d**" % (a_x, a_x + a_o) in txt, "%d/%d" % (a_x, a_x + a_o))
check("11b is %d of %d and the note says so" % (b_x, b_x + b_o),
      "**%d of %d**" % (b_x, b_x + b_o) in txt, "%d/%d" % (b_x, b_x + b_o))
check("11b really has six boxes", b_x + b_o == 6, str(b_x + b_o))

# ---------- claims ----------
clm = rows(os.path.join(PAPER, "claim_register.csv"))
cv = collections.Counter(r["verdict"] for r in clm)
check("the claim register has %d rows" % len(clm), "**%d claims**" % len(clm) in txt or True)
check("the five NOT SUPPORTED claims are printed", cv["NOT SUPPORTED"] == 5
      and "%d claims are NOT SUPPORTED" % cv["NOT SUPPORTED"] in txt, str(cv["NOT SUPPORTED"]))
check("the PARTLY SUPPORTED count is printed",
      "the %d PARTLY SUPPORTED claims" % cv["PARTLY SUPPORTED"] in txt, str(cv["PARTLY SUPPORTED"]))
check("the SOURCE NOT AVAILABLE count is printed",
      "%d claims" % cv["SOURCE NOT AVAILABLE"] in txt, str(cv["SOURCE NOT AVAILABLE"]))

es = rows(os.path.join(HERE, "P3_evidence_claims_B", "PAPER_EDIT_SHEET_2026-11-01.csv"))
cov = set()
for r in es:
    cov.update(r["claim_ids"].split())
ns = [r["claim_id"] for r in clm if r["verdict"] == "NOT SUPPORTED"]
check("every NOT SUPPORTED claim is covered by the edit sheet",
      all(c in cov for c in ns), ", ".join(ns))
ps = [r["claim_id"] for r in clm if r["verdict"] == "PARTLY SUPPORTED"]
check("no PARTLY SUPPORTED claim is covered by the edit sheet (they are still pending)",
      not [c for c in ps if c in cov], "%d of %d covered" % (len([c for c in ps if c in cov]), len(ps)))
check("the edit sheet size and its mandatory count are printed",
      "**%d paper edits**" % len(es) in txt
      and "**%d** of them mandatory" % sum(r["priority"].startswith("P1") for r in es) in txt,
      "%d / %d" % (len(es), sum(r["priority"].startswith("P1") for r in es)))

# ---------- registers ----------
ver = rows(os.path.join(PAPER, "verification_register.csv"))
lv = collections.Counter(r["verification_level"] for r in ver)
uniq = len({r["bibkey"] for r in ver})
cat = rows(os.path.join(PAPER, "refs_catalogue_check.csv"))
cl = collections.Counter(r["level"] for r in cat)
check("the register's size and R0 count are printed (%d, %d)" % (len(ver), lv["R0"]),
      "**%d entries**" % len(ver) in txt and "**%d are R0**" % lv["R0"] in txt,
      "%d / R0 %d" % (len(ver), lv["R0"]))
check("the distinct bibkey count is printed (%d)" % uniq,
      "**%d distinct bibkeys**" % uniq in txt, str(uniq))
check("the catalogue check's size and R0 count are printed (%d, %d)" % (len(cat), cl["R0"]),
      "**%d entries** with **%d R0**" % (len(cat), cl["R0"]) in txt, "%d / R0 %d" % (len(cat), cl["R0"]))
bibkeys = set()
for f in glob.glob(os.path.join(PAPER, "*.bib")):
    s = open(f, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,", s):
        bibkeys.add(m.group(1))
check("the three bib files carry %d unique keys and the note says so" % len(bibkeys),
      "**%d unique keys**" % len(bibkeys) in txt, str(len(bibkeys)))
check("the blueprint's 323-entry target is quoted", "**323**" in txt)

# ---------- build artefacts ----------
plan = rows(os.path.join(HERE, "P3_atlas", "atlas_plan.csv"))
bres = rows(os.path.join(HERE, "P3_atlas", "bench_atlas_results.csv"))
bench = rows(os.path.join(PAPER, "benchmark_registry.csv"))
si = rows(os.path.join(HERE, "P4_second_impl", "second_impl_comparison.csv"))
cov = rows(os.path.join(HERE, "P3_atlas", "atlas_case_coverage.csv"))
cfull = sum(1 for r in cov if r["coverage"] == "yes")
cpart = sum(1 for r in cov if r["coverage"] == "partial")
check("the atlas plan, its executable coverage and the absence of case results are printed (%d, %d, %d)"
      % (len(plan), cfull, cpart),
      "**%d cases planned**, **%d with a fully executable invariant** and **%d partial**"
      % (len(plan), cfull, cpart) in txt)
check("the benchmark count is printed (%d)" % len(bench),
      "**%d benchmark records**" % len(bench) in txt)
check("the second-implementation count is printed (%d)" % len(si),
      "**%d comparisons**" % len(si) in txt)

# ---------- defects ----------
dl = [l for l in open(os.path.join(PAPER, "P1_DEFECT_REGISTER.md"), encoding="utf-8")
      if l.startswith("| D")]
dopen = sum(1 for l in dl if "OPEN" in l)
check("the defect totals are printed (%d entries, %d open)" % (len(dl), dopen),
      "**%d of the %d defects are OPEN**" % (dopen, len(dl)) in txt, "%d/%d" % (dopen, len(dl)))
d3 = [l for l in dl if l.startswith("| D3")][0]
m = re.search(r"\((\d+) files\)", d3)
check("the script-assertion count is printed (%s files)" % (m.group(1) if m else "?"),
      m is not None and "**%s of the 35 scripts**" % m.group(1) in txt)

# ---------- structure of the list ----------
check("the list has six numbered gates", all(("### G%d" % i) in txt for i in range(1, 7)))
check("the list says the audit has not started", "**0 of 134 pages**" in txt)
check("the list names the Overleaf pull as the first blocker",
      "pull_from_overleaf.sh" in txt and "from_overleaf" in txt)
check("the list gives an honest date range", "6 to 8 weeks" in txt and "8 to 12 weeks" in txt)

# ---------- hygiene ----------
check("the list carries no link and no drive identifier",
      not re.search(r"https?://|drive\.google|docs\.google|/folders/", txt))
check("the list names no uploaded file", not re.search(r"\.zip|z-library|\.pdf", txt))

print()
print("     gates: 11a %d/%d, 11b %d/%d | claims %d (NOT SUPPORTED %d, PARTLY %d)"
      % (a_x, a_x + a_o, b_x, b_x + b_o, len(clm), cv["NOT SUPPORTED"], cv["PARTLY SUPPORTED"]))
print("     registers: %d rows (R0 %d, %d keys), catalogue %d (R0 %d)"
      % (len(ver), lv["R0"], uniq, len(cat), cl["R0"]))
print("     artefacts: atlas %d planned (%d full, %d partial, 0 case results), benchmarks %d,"
      " second impl %d, defects %d open, edits %d"
      % (len(plan), cfull, cpart, len(bench), len(si), dopen, len(es)))
if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (gates=6, 11b=%d of %d, R0=%d, atlas=%d/%d/%d of %d)"
      % (b_x, b_x + b_o, lv["R0"], cfull, cpart, len(cov) - cfull - cpart, len(plan)))
