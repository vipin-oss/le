#!/usr/bin/env python3
"""Validate library_inventory_v3.csv, the consolidated re-scan of the whole library.

The 2026-10-31 re-scan merged the two earlier file-level passes and added, for every
file, an explicit status drawn from a closed set, so that a reader can tell at a glance
whether a row is usable:

    match    - a bibliography key was matched from the page (title and/or printed DOI)
    no key   - the first page was read but no bibliography key corresponds to it
    mismatch - the file holds a different work from the one its name suggests
    NOT READ - not even the first page has been seen (the file is over the read cap)

Checks: header and order; unique file names; every status in the allowed set; a match
carries a key, a non-match does not; a mismatch and a NOT READ row state a reason; the
counts are the audited ones; no Drive id, link or source-library folder name anywhere.
Prints PASS lines and exits 0.  Standard library only.
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV = HERE / "library_inventory_v3.csv"

HEADER = ["file_name", "first_page_title", "first_page_doi", "matched_bib_key",
          "status", "status_reason", "source_pass"]
STATUSES = {"match", "no key", "mismatch", "NOT READ"}
N_ROWS = 117
N_MATCH, N_NOKEY, N_MISMATCH, N_NOTREAD = 63, 33, 20, 1

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


def main():
    with CSV.open(newline="", encoding="utf-8") as fh:
        rdr = csv.reader(fh)
        header = next(rdr)
        rows = [dict(zip(header, r)) for r in rdr]
    check(header == HEADER, f"header mismatch: {header}")
    print(f"PASS header: {len(header)} columns in the declared order")

    check(len(rows) == N_ROWS, f"rows {len(rows)} != {N_ROWS}")
    names = [r["file_name"] for r in rows]
    check(len(set(names)) == len(names), f"duplicate file names: {len(names)-len(set(names))}")
    print(f"PASS rows: {len(rows)} files, names unique")

    counts = {}
    for r in rows:
        st = r["status"]
        check(st in STATUSES, f"{r['file_name']}: status {st!r} not in the closed set")
        counts[st] = counts.get(st, 0) + 1
        if st == "match":
            check(r["matched_bib_key"].strip() != "", f"{r['file_name']}: match without a key")
            check(not r["matched_bib_key"].upper().startswith("MISMATCH"),
                  f"{r['file_name']}: match row carries a MISMATCH token as its key")
        else:
            check(r["matched_bib_key"].strip() == "", f"{r['file_name']}: non-match rows carry no key")
        if st in ("mismatch", "NOT READ", "no key"):
            check(len(r["status_reason"]) > 20, f"{r['file_name']}: {st} row states no reason")
    check(counts.get("match") == N_MATCH, f"match {counts.get('match')} != {N_MATCH}")
    check(counts.get("no key") == N_NOKEY, f"no key {counts.get('no key')} != {N_NOKEY}")
    check(counts.get("mismatch") == N_MISMATCH, f"mismatch {counts.get('mismatch')} != {N_MISMATCH}")
    check(counts.get("NOT READ") == N_NOTREAD, f"NOT READ {counts.get('NOT READ')} != {N_NOTREAD}")
    print("PASS statuses: match=%d no-key=%d mismatch=%d NOT-READ=%d" %
          (counts.get("match", 0), counts.get("no key", 0), counts.get("mismatch", 0), counts.get("NOT READ", 0)))

    by = {r["file_name"]: r for r in rows}
    check("2ndSoundSolids.pdf" in by and by["2ndSoundSolids.pdf"]["matched_bib_key"] == "Chester1963",
          "2ndSoundSolids.pdf is not recorded as Chester1963")
    check("ezzat2011.pdf" in by and by["ezzat2011.pdf"]["status"] == "mismatch",
          "ezzat2011.pdf is not flagged as a mismatch")
    check("nonlocal-continuum-field-theories-2004.pdf" in by and
          by["nonlocal-continuum-field-theories-2004.pdf"]["status"] == "NOT READ",
          "the 29.7 MB book is not flagged NOT READ")
    print("PASS traps: ezzat2011 mismatched, 2ndSoundSolids = Chester1963, the over-cap book NOT READ")

    for r in rows:
        for field in r.values():
            check(not re.search(r"https?://|drive\.google|docs\.google|\b1[A-Za-z0-9_-]{32}\b", field),
                  f"{r['file_name']}: link or Drive id leaked into the inventory")
            check("LE_" not in field and "Extracted ZIPs" not in field,
                  f"{r['file_name']}: source-library folder name leaked into the inventory")
    print("PASS hygiene: no link, no Drive id, no source-library folder name")

    if fails:
        for f in fails:
            print("FAIL", f)
        return 1
    print("PASS all checks (rows=%d, match=%d, no-key=%d, mismatch=%d, NOT READ=%d)" %
          (len(rows), N_MATCH, N_NOKEY, N_MISMATCH, N_NOTREAD))
    return 0


if __name__ == "__main__":
    sys.exit(main())
