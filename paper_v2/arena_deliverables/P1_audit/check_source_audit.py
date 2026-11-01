#!/usr/bin/env python3
"""Checks the P1 source audit: the report exists, its numbers are re-derivable, and it is honest.

Re-derives the three findings that matter (a dangling citation, duplicate source copies, figure files
nobody includes) straight from the sources, then checks that the CSV says the same thing, that the MD
lists every FAIL, and that the audit itself did not edit a single .tex.
"""
import csv
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("AUDIT_SRC") or os.path.normpath(os.path.join(HERE, "..", "..", "manuscript_v2"))
CSV = os.path.join(HERE, "source_audit_2026-11-01.csv")
MD = os.path.join(HERE, "P1_SOURCE_AUDIT_2026-11-01.md")
fails = []


def check(what, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + what + ((" [%s]" % detail) if detail and not ok else ""))
    if not ok:
        fails.append(what)


def tex():
    out = {}
    for root, _, fs in os.walk(SRC):
        for f in fs:
            if f.endswith(".tex"):
                p = os.path.join(root, f)
                out[p] = re.sub(r"(?<!\\)%.*", "", open(p, encoding="utf-8", errors="replace").read())
    return out


rows = {r["check_id"]: r for r in csv.DictReader(open(CSV, encoding="utf-8"))} if os.path.exists(CSV) else {}
md = open(MD, encoding="utf-8").read() if os.path.exists(MD) else ""

check("the audit ran over the landed sources", os.path.isdir(SRC) and len(tex()) > 40, str(len(tex())))
check("the csv carries checks A1-A11", {"A%d" % i for i in range(1, 12)} <= set(rows), str(sorted(rows)))
check("the md reports every FAIL as a finding",
      all(("### %s " % cid) in md for cid, r in rows.items() if r["status"] == "FAIL"),
      str([cid for cid, r in rows.items() if r["status"] == "FAIL" and ("### %s " % cid) not in md]))
check("the md says what the audit does not cover", "What this audit does not cover" in md
      and "signs" in md and "45 scripts" not in md.replace("the 45 scripts", ""))

T = tex()
joined = "\n".join(T.values())
labels = set(re.findall(r"\\label\{([^}]+)\}", joined))
refs = set(re.findall(r"\\(?:ref|eqref|cref|Cref|autoref)\{([^}]+)\}", joined))
unres = {k for r in refs for k in r.split(",") if k.strip() not in labels}
check("A1 holds: every reference target is a label (%d refs, %d labels)" % (len(refs), len(labels)),
      not unres and rows.get("A1", {}).get("status") == "PASS", str(sorted(unres)[:5]))

bib = ""
for root, _, fs in os.walk(SRC):
    for f in fs:
        if f.endswith(".bib"):
            bib += open(os.path.join(root, f), encoding="utf-8", errors="replace").read()
keys = set(re.findall(r"@\w+\s*\{\s*([^,]+),", bib))
cited = {k.strip() for m in re.finditer(r"\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]+)\}", joined)
         for k in m.group(1).split(",")}
missing = {k for k in cited if k and k not in keys}
check("A3 is a real finding, not a parse error: %d cited key(s) absent from %d bib entries"
      % (len(missing), len(keys)),
      missing and rows.get("A3", {}).get("status") == "FAIL" and str(rows["A3"]["n"]) == str(len(missing)),
      str(sorted(missing)))

dups = {}
for root, _, fs in os.walk(SRC):
    for f in fs:
        if f.endswith(".tex"):
            p = os.path.join(root, f)
            r = os.path.relpath(p, SRC)
            dups.setdefault(os.path.basename(p), set()).add(r.split(os.sep)[0])
same_file_twice = {b: d for b, d in dups.items() if len(d) > 1}
check("A2b is a real finding: %d files exist under two different roots" % len(same_file_twice),
      same_file_twice and rows.get("A2b", {}).get("status") == "FAIL",
      str(sorted(same_file_twice)[:5]))

figdir = "/home/user/manuscript/master/figures/source"
used = {os.path.basename(m) for m in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", joined)}
allf = [f for f in os.listdir(figdir) if f.endswith(".pdf")]
unused = [f for f in allf if f not in used]
check("A11 is a real finding: %d of %d figure files are never included" % (len(unused), len(allf)),
      len(unused) == int(rows["A11"]["n"]) and rows["A11"]["status"] == "FAIL", str(unused))

check("the audit claims no result for signs, notation or derivations",
      "not about signs" in md or "signs, dimensions and derivation steps" in md)
dirty = subprocess.run(["git", "-C", SRC, "status", "--porcelain", "--", "."],
                       capture_output=True, text=True).stdout.strip()
check("the audit did not edit a single source file", dirty == "", dirty[:200])

print()
if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (P1 source audit: %d checks in the report, %d FAIL findings, sources untouched)"
      % (len(rows), sum(1 for r in rows.values() if r["status"] == "FAIL")))
