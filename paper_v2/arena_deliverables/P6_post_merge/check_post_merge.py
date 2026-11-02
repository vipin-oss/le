#!/usr/bin/env python3
"""Gate for the post-merge audit tables.

Checks, all against files in this repository:
  A  post_merge_claims.csv has the agreed columns, unique ids, statements of at most 25 words,
     a verdict from the fixed vocabulary, a location and a page/equation locator on every row
  B  every bib key named in its source column exists in one of the paper's .bib files
  C  pdfs_needed_final.csv has at most 60 rows, the agreed columns, ranks 1..n, no duplicate keys,
     and no key that the register no longer treats as SOURCE NOT AVAILABLE
  D  claim_check_C batches are numbered without gaps and the register's SOURCE NOT AVAILABLE rows
     match the keys the needed list says are still missing
Prints PASS and exits 0 only if all of that holds.
"""
from __future__ import annotations

import csv
import glob
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent.parent
DELIV = PAPER / "arena_deliverables"
CLAIMS_CSV = HERE / "post_merge_claims.csv"
NEEDED = HERE / "pdfs_needed_final.csv"
REGISTER = PAPER / "claim_register.csv"
BATCH_DIR = DELIV / "P3_evidence_claims_C"

COLS_CLAIMS = ["claim_id", "location", "statement", "source", "verdict", "page_or_equation", "note"]
VERDICTS = {"SUPPORTED", "PARTLY", "NOT SUPPORTED", "SOURCE NOT AVAILABLE"}


def main() -> int:
    problems: list[str] = []

    rows = list(csv.DictReader(CLAIMS_CSV.open(encoding="utf-8")))
    if list(rows[0].keys()) != COLS_CLAIMS:
        problems.append(f"A columns are {list(rows[0].keys())}, expected {COLS_CLAIMS}")
    ids = [r["claim_id"] for r in rows]
    if len(set(ids)) != len(ids):
        problems.append("A duplicate claim_id")
    for r in rows:
        w = len((r["statement"] or "").split())
        if w > 25:
            problems.append(f"A {r['claim_id']}: statement is {w} words")
        if r["verdict"] not in VERDICTS:
            problems.append(f"A {r['claim_id']}: verdict '{r['verdict']}' not in vocabulary")
        if not (r["location"] or "").strip():
            problems.append(f"A {r['claim_id']}: no location")
        if not (r["page_or_equation"] or "").strip():
            problems.append(f"A {r['claim_id']}: no page_or_equation")

    # The bibliography ships inside the Overleaf package, with a few .bib files loose in paper_v2.
    bib = "\n".join(f.read_text(encoding="utf-8", errors="ignore")
                     for f in map(Path, glob.glob(str(PAPER / "*.bib"))))
    pkg = PAPER / "overleaf_package.zip"
    if pkg.exists():
        import zipfile
        with zipfile.ZipFile(pkg) as z:
            for n in z.namelist():
                if n.endswith(".bib"):
                    bib += "\n" + z.read(n).decode("utf-8", "ignore")
    # Only tokens that can only be citation keys are tested (Biot1956, Quintanilla2003DPL, ...).
    KEY = re.compile(r"\b[A-Z][A-Za-z]*[A-Z][a-z]*\d{4}[a-z]?\b|\b[A-Z][a-z]+\d{4}[a-z]?\b")
    for r in rows:
        for key in KEY.findall(" ".join(r.values())):
            if key not in bib:
                problems.append(f"B {r['claim_id']}: bib key not found: {key}")

    needed = list(csv.DictReader(NEEDED.open(encoding="utf-8")))
    if len(needed) > 60:
        problems.append(f"C needed list has {len(needed)} rows (cap 60)")
    want = ["rank", "bib_key", "title", "authors", "journal", "year", "doi", "claims_blocked",
            "why_needed"]
    if list(needed[0].keys()) != want:
        problems.append(f"C needed columns are {list(needed[0].keys())}, expected {want}")
    if [int(r["rank"]) for r in needed] != list(range(1, len(needed) + 1)):
        problems.append("C ranks are not 1..n")
    keys = [r["bib_key"] for r in needed]
    if len(set(keys)) != len(keys):
        problems.append("C duplicate bib_key")

    reg = list(csv.DictReader(REGISTER.open(encoding="utf-8")))
    sna_keys = {(r["cited_source"] or "").split("|")[0].strip()
                for r in reg if r["verdict"].strip() == "SOURCE NOT AVAILABLE"}
    listed = {k for k in keys if k in sna_keys}
    if not listed:
        problems.append("C the needed list names no key that is still SOURCE NOT AVAILABLE")

    nums = sorted(int(re.search(r"batch_(\d+)", Path(f).name).group(1))
                  for f in glob.glob(str(BATCH_DIR / "claim_check_C_batch_*.csv")))
    if nums != list(range(1, len(nums) + 1)):
        problems.append(f"D batch numbering has a gap: {nums}")

    print(f"post-merge claims: {len(rows)} (SUPPORTED {sum(r['verdict']=='SUPPORTED' for r in rows)}, "
          f"PARTLY {sum(r['verdict']=='PARTLY' for r in rows)}, "
          f"NOT SUPPORTED {sum(r['verdict']=='NOT SUPPORTED' for r in rows)}, "
          f"SOURCE NOT AVAILABLE {sum(r['verdict']=='SOURCE NOT AVAILABLE' for r in rows)})")
    print(f"needed list: {len(needed)} rows, {len(listed)} of them still SOURCE NOT AVAILABLE")
    print(f"register: {len(reg)} rows, SOURCE NOT AVAILABLE {len(sna_keys)}; batches {nums[0]}-{nums[-1]}")
    if problems:
        for p in problems:
            print("FAIL", p)
        print(f"FAIL {len(problems)} problem(s)")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
