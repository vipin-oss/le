#!/usr/bin/env python3
"""Validate library_inventory_v2.csv and library_inventory_v2_findings.csv.

Checks
  1. header is exactly the four requested columns
  2. 37 rows, one per PDF in the unzipped library folder, file_name unique
  3. matched_bib_key is blank, starts with MISMATCH, or is a real key in refs*.bib
  4. no Drive identifier, link or library folder name leaks into the CSV
  5. every non-blank first_page_doi looks like a DOI
  6. findings file has 7 rows, all of them blank-key rows of the inventory
Prints PASS... and exits 0 when everything holds.
"""
import csv
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE / "library_inventory_v2.csv"
FIND = HERE / "library_inventory_v2_findings.csv"
ZIP = HERE.parents[1] / "paper_sources.zip"

EXPECTED_HEADER = ["file_name", "first_page_title", "first_page_doi", "matched_bib_key"]
N_ROWS = 37
N_MATCH, N_BLANK, N_MISMATCH = 11, 7, 19

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


def bib_keys():
    keys = set()
    with zipfile.ZipFile(ZIP) as z:
        for name in z.namelist():
            if name.endswith(".bib"):
                keys |= set(re.findall(r"@\w+\{([^,]+),", z.read(name).decode("utf-8", "replace")))
    return keys


def main():
    keys = bib_keys()
    check(keys, "no bib keys read from paper_sources.zip")

    with INV.open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        header = next(reader)
        rows = list(reader)
    check(header == EXPECTED_HEADER, f"header is {header}")

    names = [r[0] for r in rows]
    check(len(rows) == N_ROWS, f"row count {len(rows)} != {N_ROWS}")
    check(len(set(names)) == len(names), "duplicate file_name")
    check(all(len(r) == 4 for r in rows), "a row does not have 4 fields")

    match = blank = mismatch = 0
    for name, title, doi, key in rows:
        check(bool(title.strip()), f"{name}: empty first_page_title")
        if key.startswith("MISMATCH"):
            mismatch += 1
        elif key == "":
            blank += 1
        else:
            match += 1
            check(key in keys, f"{name}: matched_bib_key {key!r} not in refs*.bib")
        if doi:
            check(re.match(r"^10\.\d{4,9}/[^\s]+$", doi) is not None, f"{name}: bad DOI {doi!r}")
        for field in (name, title, doi, key):
            check(not re.search(r"https?://|drive\.google|docs\.google|\b1[A-Za-z0-9_-]{32}\b", field),
                  f"{name}: link or Drive id leaked into the CSV")
            check("LE_" not in field and "Extracted ZIPs" not in field,
                  f"{name}: source-library folder name leaked into the CSV")
    check(match == N_MATCH, f"matched rows {match} != {N_MATCH}")
    check(blank == N_BLANK, f"blank-key rows {blank} != {N_BLANK}")
    check(mismatch == N_MISMATCH, f"mismatch rows {mismatch} != {N_MISMATCH}")
    check(any(k.startswith("MISMATCH") and "Quintanilla2008a" in k for _, _, _, k in rows),
          "the Quintanilla2008-vs-2008a mismatch is not recorded")
    check(any(n == "tzou1995.pdf" and k.startswith("MISMATCH") for n, _, _, k in rows),
          "the tzou1995 mismatch is not recorded")

    with FIND.open(newline="", encoding="utf-8") as fh:
        find = list(csv.DictReader(fh))
    check(len(find) == 7, f"findings rows {len(find)} != 7")
    blanks = {n for n, _, _, k in rows if k == ""}
    for r in find:
        check(r["file_name"] in blanks, f"findings row {r['file_name']} is not a blank-key inventory row")
    check({r["file_name"] for r in find} == blanks, "findings file does not cover exactly the blank-key files")

    if fails:
        for f in fails:
            print("FAIL", f)
        return 1
    print(f"PASS all checks (inventory rows={len(rows)}, match={match}, blank={blank}, mismatch={mismatch}, findings={len(find)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
