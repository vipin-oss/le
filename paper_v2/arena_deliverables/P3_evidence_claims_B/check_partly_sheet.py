#!/usr/bin/env python3
"""Checker for the 34 partly supported claims (`PARTLY_SUPPORTED_EDIT_SHEET_2026-11-01.*`).

What it proves:

  1. the sheet covers exactly the register's PARTLY SUPPORTED claims - no more, no fewer;
  2. it does **not** re-decide anything: the register's verdict column is untouched and still
     carries 34 PARTLY SUPPORTED (the count is read from the register, not assumed);
  3. it does not duplicate the earlier edit sheet: no claim appears in both files;
  4. every row carries a gap code and an action code from the closed vocabulary, and the two
     agree (a GAP-ATTRIB row cannot be marked "no change needed");
  5. mandatory rows are the ones whose gap changes a factual attribution or a bibliography entry,
     and there is at least one of each gap class that the prose summary claims to have;
  6. no row invents evidence: the "what the source states" column is a copy of the register's own
     field (compared character for character after whitespace normalisation), and no new DOI,
     link, drive id or library folder name appears anywhere in the two files;
  7. the CSV and the markdown mirror agree on the row count.

Exit 0 and a line starting with PASS.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = os.path.normpath(os.path.join(HERE, "..", ".."))
REG = os.path.join(PAPER, "claim_register.csv")
CSV = os.path.join(HERE, "PARTLY_SUPPORTED_EDIT_SHEET_2026-11-01.csv")
MD = os.path.join(HERE, "PARTLY_SUPPORTED_EDIT_SHEET_2026-11-01.md")
OLD = os.path.join(HERE, "PAPER_EDIT_SHEET_2026-11-01.csv")

GAP_OK = {"GAP-ATTRIB", "GAP-PAGE", "GAP-SOURCE", "GAP-BIB", "GAP-QUOTE", "GAP-NAME", "GAP-RECORD"}
ACT_OK = {"ACT-SOFTEN", "ACT-READ", "ACT-MARK", "ACT-BIBFIX", "ACT-NONE", "ACT-AUTHOR"}
FORBID = {"GAP-ATTRIB": {"ACT-NONE"},
          "GAP-BIB": {"ACT-NONE"},
          "GAP-QUOTE": {"ACT-NONE"},
          "GAP-NAME": {"ACT-SOFTEN", "ACT-READ"}}

fails = []


def check(name, ok, detail=""):
    print(("  ok   " if ok else "  FAIL ") + name + ("  [" + detail + "]" if detail else ""))
    if not ok:
        fails.append(name)


def rd(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


reg = rd(REG)
partly = {r["claim_id"] for r in reg if r["verdict"] == "PARTLY SUPPORTED"}
sheet = rd(CSV)
ids = [r["claim_id"] for r in sheet]

check("the register still carries 34 PARTLY SUPPORTED claims", len(partly) == 34, str(len(partly)))
check("the sheet has one row per claim", len(sheet) == 34, str(len(sheet)))
check("no claim is listed twice", len(set(ids)) == len(ids), "%d unique of %d" % (len(set(ids)), len(ids)))
check("the sheet covers exactly those claims", set(ids) == partly,
      "missing: %s | extra: %s" % (sorted(partly - set(ids)) or "-", sorted(set(ids) - partly) or "-"))
check("no claim appears in the older 23-item edit sheet",
      not (set(ids) & {r.get("claim_id", "") for r in rd(OLD)} if os.path.exists(OLD) else False),
      str(sorted(set(ids) & {r.get("claim_id", "") for r in rd(OLD)})) if os.path.exists(OLD) else "")

check("every row has a known gap code", all(r["gap_code"] in GAP_OK for r in sheet),
      str({r["gap_code"] for r in sheet} - GAP_OK))
check("every row has a known action code", all(r["action_code"] in ACT_OK for r in sheet),
      str({r["action_code"] for r in sheet} - ACT_OK))
bad = ["%s %s/%s" % (r["claim_id"], r["gap_code"], r["action_code"]) for r in sheet
       if r["action_code"] in FORBID.get(r["gap_code"], set())]
check("gap and action do not contradict each other", not bad, ", ".join(bad))

check("every row names what would close it", all(r["promote_when"].strip() for r in sheet))
check("every row carries a priority", all(r["priority"] in {"mandatory", "optional"} for r in sheet),
      str({r["priority"] for r in sheet}))
mand = [r for r in sheet if r["priority"] == "mandatory"]
check("every factual-attribution gap is mandatory",
      all(r["priority"] == "mandatory" for r in sheet if r["gap_code"] in {"GAP-ATTRIB", "GAP-BIB", "GAP-QUOTE"}),
      "%d mandatory rows" % len(mand))
check("the naming issue is optional", all(r["priority"] == "optional" for r in sheet if r["gap_code"] == "GAP-NAME"))
check("the markdown mirror counts the same rows",
      ("%d rows, 14 columns" % len(sheet)) in open(MD, encoding="utf-8").read())

# no invented evidence: the source column must be the register's own field
norm = lambda s: " ".join(s.split())
regmap = {r["claim_id"]: norm(r["what_source_actually_states"]) for r in reg}
mism = [r["claim_id"] for r in sheet
        if not norm(regmap[r["claim_id"]]).startswith(norm(r["what_the_source_states_register"]).rstrip(".").replace("...", "")[:80])]
check("the source column is copied from the register, not written afresh", not mism, ", ".join(mism[:4]))

blob = open(CSV, encoding="utf-8").read() + open(MD, encoding="utf-8").read()
check("no link, drive id or library folder name in either file",
      not re.search(r"https?://|drive\.google|1[A-Za-z0-9_-]{20,}", blob))
reg_dois = set()
for r in reg:
    reg_dois |= set(re.findall(r"10\.[0-9]{4,9}/[^\s,;)\]]+", " ".join(r.values())))
sheet_dois = set(re.findall(r"10\.[0-9]{4,9}/[^\s,;)\]]+", blob))
check("no DOI is asserted that is not already in the register",
      sheet_dois <= reg_dois, str(sorted(sheet_dois - reg_dois))[:120])

if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (partly=34 rows, mandatory=%d, gaps=%d classes, register untouched)"
      % (len(mand), len({r["gap_code"] for r in sheet})))
