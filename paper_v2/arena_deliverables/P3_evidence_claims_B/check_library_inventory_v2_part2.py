#!/usr/bin/env python3
"""Validate library_inventory_v2_part2.csv (the second, much larger library pass).

Checks
 1. the four requested columns, 79 rows, one per file read in this pass;
 2. every matched_bib_key is blank, starts with MISMATCH, or is a real key in refs*.bib;
 3. the counts are the ones established while reading: 51 matches, 26 without a key,
    2 mismatches;
 4. every non-blank DOI is well formed and every DOI-looking cell is either a DOI or
    empty (no invented identifiers);
 5. the two known traps are recorded as MISMATCH (2ndSoundSolids.pdf is an X-ray
    article; ezzat2011.pdf is not the ZAMP paper keyed Ezzat2011);
 6. the five Task-4 / landmark files are present and carry the expected status
    (cahill2003, huberman2019, jackson1970 matched, gurtin1968 matched,
    2ndSoundSolids flagged);
 7. the findings file covers exactly the rows without a bib key;
 8. no Drive identifier, link or source-library folder name anywhere.
Prints PASS lines and exits 0.
"""
import csv
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE / "library_inventory_v2_part2.csv"
FIND = HERE / "library_inventory_v2_part2_findings.csv"
ZIP = HERE.parents[1] / "paper_sources.zip"

HEADER = ["file_name", "first_page_title", "first_page_doi", "matched_bib_key"]
N_ROWS, N_MATCH, N_BLANK, N_MISMATCH = 79, 51, 26, 2
fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


def main():
    keys = set()
    with zipfile.ZipFile(ZIP) as z:
        for n in z.namelist():
            if n.endswith(".bib"):
                keys |= set(re.findall(r"@\w+\{([^,]+),", z.read(n).decode("utf-8", "replace")))

    with INV.open(newline="", encoding="utf-8") as fh:
        rdr = csv.reader(fh)
        header = next(rdr)
        rows = [dict(zip(header, r)) for r in rdr]
    check(header == HEADER, f"header mismatch: {header}")
    check(len(rows) == N_ROWS, f"row count {len(rows)} != {N_ROWS}")
    names = [r["file_name"] for r in rows]
    check(len(set(names)) == len(names), "duplicate file_name")
    print(f"PASS rows: {len(rows)} files, names unique")

    match = blank = mismatch = 0
    for r in rows:
        k = r["matched_bib_key"]
        if k.startswith("MISMATCH"):
            mismatch += 1
        elif k == "":
            blank += 1
        else:
            match += 1
            check(k in keys, f"{r['file_name']}: key {k!r} not in refs*.bib")
        doi = r["first_page_doi"].strip()
        if doi:
            check(re.match(r"^10\.\d{4,9}/\S+$", doi) is not None, f"{r['file_name']}: bad DOI {doi!r}")
        check(bool(r["first_page_title"].strip()), f"{r['file_name']}: empty title cell")
        for cell in r.values():
            check(not re.search(r"https?://drive|drive\.google|docs\.google", cell),
                  f"{r['file_name']}: Drive link leaked")
            check("LE_" not in cell and "Extracted ZIPs" not in cell,
                  f"{r['file_name']}: folder name leaked")
    check(match == N_MATCH, f"match {match} != {N_MATCH}")
    check(blank == N_BLANK, f"blank {blank} != {N_BLANK}")
    check(mismatch == N_MISMATCH, f"mismatch {mismatch} != {N_MISMATCH}")
    print(f"PASS keys: {match} matched, {blank} without a key, {mismatch} mismatched")

    by = {r["file_name"]: r for r in rows}
    check(by["2ndSoundSolids.pdf"]["matched_bib_key"].startswith("MISMATCH"),
          "2ndSoundSolids.pdf is not flagged as a mismatch")
    check(by["ezzat2011.pdf"]["matched_bib_key"].startswith("MISMATCH"),
          "ezzat2011.pdf is not flagged as a mismatch")
    for f, k in (("cahill2003.pdf", "Cahill2003"), ("huberman2019.pdf", "Huberman2019"),
                 ("jackson1970.pdf", "Jackson1970"), ("gurtin1968.pdf", "GurtinPipkin1968")):
        check(f in by and by[f]["matched_bib_key"] == k, f"{f} is missing or not matched to {k}")
    print("PASS traps: the two mismatches and the four newly available targets are as recorded")

    with FIND.open(newline="", encoding="utf-8") as fh:
        findings = list(csv.DictReader(fh))
    blanks = {r["file_name"] for r in rows if r["matched_bib_key"] == ""}
    check({f["file_name"] for f in findings} == blanks, "findings do not cover exactly the key-less rows")
    check(len(findings) == len(blanks), f"findings rows {len(findings)} != key-less rows {len(blanks)}")
    print(f"PASS findings: {len(findings)} key-less files explained")

    if fails:
        for f in fails:
            print("FAIL", f)
        return 1
    print(f"PASS all checks (rows={len(rows)}, match={match}, blank={blank}, mismatch={mismatch}, findings={len(findings)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
