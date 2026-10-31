#!/usr/bin/env python3
"""Validator for the claim_check_B_batch_NNN.csv deliverables (Task 1, sections 16-36).

Run from this directory:  python3 check_claim_check_B.py
Every check prints a line starting with PASS (or FAIL) and the exit code is 0 only if all pass.
"""
import csv, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

COLS = ["claim_id","manuscript_location","manuscript_statement","cited_source","source_doi",
        "found_in_library","verdict","source_page_or_equation","source_wording_max25words",
        "what_source_actually_states","verification_level","notes"]
VERDICTS = {"SUPPORTED","PARTLY SUPPORTED","NOT SUPPORTED","SOURCE NOT AVAILABLE"}
LIB = {"yes","no","not confirmed"}
LEVELS = {"R0","R1","R2","R3"}
EXPECTED_ROWS = 667          # 283 for sections 16-36 (batches 001-008) + 384 for the appendices

fails = []
def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else " :: " + detail))
    if not ok: fails.append(name)

files = sorted(glob.glob("claim_check_B_batch_*.csv"))
check("eighteen batch files present", len(files) == 18, "found %d" % len(files))

rows = []
for f in files:
    with open(f, newline="") as fh:
        rdr = csv.DictReader(fh)
        hdr = rdr.fieldnames
        check("header matches Task 1 schema in %s" % f, hdr == COLS, str(hdr))
        rows += list(rdr)

check("total rows == %d" % EXPECTED_ROWS, len(rows) == EXPECTED_ROWS, "found %d" % len(rows))
check("batch sizes 20-40", all(20 <= sum(1 for _ in csv.DictReader(open(f))) <= 40 for f in files))

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

def _loc_ok(loc):
    m = re.match(r"^Section (\d+)", loc)
    if m:
        return 16 <= int(m.group(1)) <= 36
    return loc.startswith("Appendix ") and re.search(r"^Appendix [A-H]", loc) is not None

check("every row states a section 16-36 or an appendix A-H",
      all(_loc_ok(r["manuscript_location"]) for r in rows),
      str([r["claim_id"] for r in rows if not _loc_ok(r["manuscript_location"])][:5]))
check("every row states a page number",
      all(re.search(r"p\. \d+", r["manuscript_location"]) for r in rows))

# Long tokens are allowed only when they are bibliography keys (a citation key such as
# MarchandMcDevittTriggiani2012 is 28+ characters and legitimate); Drive ids are not.
BIBKEYS = set()
try:
    import zipfile
    z = zipfile.ZipFile(os.path.join(HERE, "..", "..", "paper_sources.zip"))
    for n in z.namelist():
        if n.startswith("refs") and n.endswith(".bib"):
            BIBKEYS |= set(re.findall(r"@\w+\{([^,]+),", z.read(n).decode("utf-8", "replace")))
except Exception:
    pass
leak = re.compile(r"(drive\.google|docs\.google|https?://|/folders/)")
longtok = re.compile(r"\b[A-Za-z0-9]{28,}\b")
def _leaky(r):
    txt = " ".join(r.values())
    if leak.search(txt):
        return True
    return any(t not in BIBKEYS for t in longtok.findall(txt))
bad = [r["claim_id"] for r in rows if _leaky(r)]
check("no Drive links, URLs or unknown long ids in any field", not bad, str(bad[:5]))

# A metadata row (catalogue entry vs the project's own bibliography record) is fully
# supported by the record itself, so R1 is allowed there - and only there.
def _is_metadata_row(r):
    return r["cited_source"].startswith("bibliography record")

bad = [r["claim_id"] for r in rows if r["verification_level"] == "R0" and r["verdict"] == "SUPPORTED"]
check("no SUPPORTED row below R2 unless it is a bibliography-metadata row", not bad, str(bad[:5]))
bad = [r["claim_id"] for r in rows if r["verification_level"] == "R1"
       and r["verdict"] == "SUPPORTED" and not _is_metadata_row(r)]
check("R1 SUPPORTED rows are all bibliography-metadata rows", not bad, str(bad[:5]))

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
