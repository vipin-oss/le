#!/usr/bin/env python3
"""Validator for the claim_check_B_batch_NNN.csv deliverables (Task 1, sections 16-36).

Run from this directory:  python3 check_claim_check_B.py
Every check prints a line starting with PASS (or FAIL) and the exit code is 0 only if all pass.
"""
import csv, glob, re, sys

COLS = ["claim_id","manuscript_location","manuscript_statement","cited_source","source_doi",
        "found_in_library","verdict","source_page_or_equation","source_wording_max25words",
        "what_source_actually_states","verification_level","notes"]
VERDICTS = {"SUPPORTED","PARTLY SUPPORTED","NOT SUPPORTED","SOURCE NOT AVAILABLE"}
LIB = {"yes","no","not confirmed"}
LEVELS = {"R0","R1","R2","R3"}
EXPECTED_ROWS = 283

fails = []
def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else " :: " + detail))
    if not ok: fails.append(name)

files = sorted(glob.glob("claim_check_B_batch_*.csv"))
check("eight batch files present", len(files) == 8, "found %d" % len(files))

rows = []
for f in files:
    with open(f, newline="") as fh:
        rdr = csv.DictReader(fh)
        hdr = rdr.fieldnames
        check("header matches Task 1 schema in %s" % f, hdr == COLS, str(hdr))
        rows += list(rdr)

check("total rows == %d" % EXPECTED_ROWS, len(rows) == EXPECTED_ROWS, "found %d" % len(rows))
check("batch sizes 31-36", all(31 <= sum(1 for _ in csv.DictReader(open(f))) <= 36 for f in files))

ids = [r["claim_id"] for r in rows]
check("claim ids unique", len(set(ids)) == len(ids))
check("claim ids contiguous CB-0001..CB-%04d" % EXPECTED_ROWS,
      ids == ["CB-%04d" % i for i in range(1, EXPECTED_ROWS + 1)])
check("no empty required fields",
      all(all(r[c].strip() for c in COLS) for r in rows))
check("verdict values allowed", all(r["verdict"] in VERDICTS for r in rows),
      str({r["verdict"] for r in rows} - VERDICTS))
check("found_in_library values allowed", all(r["found_in_library"] in LIB for r in rows),
      str({r["found_in_library"] for r in rows} - LIB))
check("verification levels R0-R3", all(r["verification_level"] in LEVELS for r in rows))

def nwords(s):
    return len([w for w in s.split() if w != "[...]"])
bad = [r["claim_id"] for r in rows if nwords(r["manuscript_statement"]) > 25]
check("manuscript_statement <= 25 words", not bad, str(bad[:5]))
bad = [r["claim_id"] for r in rows
       if r["source_wording_max25words"] != "-" and nwords(r["source_wording_max25words"]) > 25]
check("source_wording_max25words <= 25 words", not bad, str(bad[:5]))

check("every row states a section number 16-36",
      all(re.match(r"^Section (\d+)", r["manuscript_location"]) and
          16 <= int(r["manuscript_location"].split()[1].split(".")[0]) <= 36 for r in rows))
check("every row states a page number",
      all(re.search(r"p\. \d+", r["manuscript_location"]) for r in rows))

leak = re.compile(r"(drive\.google|docs\.google|https?://|/folders/|\b[A-Za-z0-9]{28,}\b)")
bad = [r["claim_id"] for r in rows if leak.search(" ".join(r.values()))]
check("no Drive links, URLs or long ids in any field", not bad, str(bad[:5]))

bad = [r["claim_id"] for r in rows if r["verification_level"] == "R0" and r["verdict"] == "SUPPORTED"]
check("no SUPPORTED row below R2", not bad, str(bad[:5]))

per = {}
for r in rows:
    per[r["verdict"]] = per.get(r["verdict"], 0) + 1
print("     verdict counts: " + ", ".join("%s=%d" % kv for kv in sorted(per.items())))
print("     found_in_library counts: " + ", ".join(
    "%s=%d" % (k, sum(1 for r in rows if r["found_in_library"] == k)) for k in sorted(LIB)))

if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (rows=%d, batches=%d)" % (len(rows), len(files)))
sys.exit(0)
