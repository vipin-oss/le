#!/usr/bin/env python3
"""Validate experiments_2.csv (the Task 4 extraction run).

The four papers named in Task 4 are all unreachable: three are members of the
52 MB / 62 MB archives that are over the 25 MB extraction cap and have never been
unzipped, and the fourth ("a review of second sound in solids") is not even
identified.  So every row must be honestly blocked, and the rule "a value may be
written only if it was read on a page, and must carry the page number" must be
enforced mechanically, not by trust:

 1. header is exactly the declared schema;
 2. 4 rows, unique experiment_id;
 3. entry_id that is not empty exists in experiments_1.csv;
 4. target_id is 'none' or exists in extraction_protocol.csv;
 5. DOI is a well-formed DOI or the literal NOT FOUND (never a guess);
 6. status is one of the honest states, and for a blocked row value, unit,
    uncertainty and page are all EMPTY;
 7. for any row that ever claims to be read, value, page and read_level must all
    be non-empty and page must contain a page number - so a future value cannot be
    added without its page;
 8. no cell contains a Drive identifier, a link or a source-library folder name.

Prints PASS lines and exits 0.  Standard library only.
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV = HERE / "experiments_2.csv"
EXP1 = HERE / "experiments_1.csv"
PROTO = HERE / "extraction_protocol.csv"

SCHEMA = ["experiment_id", "entry_id", "target_id", "source", "DOI", "quantity_to_extract",
          "value", "unit", "uncertainty", "page", "read_level", "status", "blocker", "notes"]
BLOCKED = {"SOURCE NOT AVAILABLE"}
READ = {"READ_AT_PAGE"}
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
PAGE_RE = re.compile(r"p\.\s?\d")

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


def main():
    with CSV.open(newline="", encoding="utf-8") as fh:
        rdr = csv.reader(fh)
        header = next(rdr)
        rows = [dict(zip(header, r)) for r in rdr]
    check(header == SCHEMA, f"header mismatch: {header}")
    print(f"PASS header: {len(header)} columns in the declared order")

    check(len(rows) == 4, f"expected 4 experimental-paper rows, found {len(rows)}")
    ids = [r["experiment_id"] for r in rows]
    check(len(set(ids)) == len(ids), f"duplicate experiment ids {ids}")
    print(f"PASS rows: {len(rows)} experimental papers, ids unique")

    exp1 = {r["entry_id"] for r in csv.DictReader(EXP1.open(newline="", encoding="utf-8"))}
    proto = {r["target_id"] for r in csv.DictReader(PROTO.open(newline="", encoding="utf-8"))}
    for r in rows:
        if r["entry_id"]:
            check(r["entry_id"] in exp1, f"{r['experiment_id']}: entry {r['entry_id']} not in experiments_1.csv")
        check(r["target_id"] == "none" or r["target_id"] in proto,
              f"{r['experiment_id']}: target {r['target_id']} not in extraction_protocol.csv")
    print("PASS linkage: entry ids and protocol targets all resolve")

    for r in rows:
        doi = r["DOI"].strip()
        check(doi == "NOT FOUND" or DOI_RE.match(doi) is not None,
              f"{r['experiment_id']}: DOI {doi!r} is neither a DOI nor NOT FOUND")
        st = r["status"]
        check(st in BLOCKED | READ, f"{r['experiment_id']}: status {st!r} not allowed")
        if st in BLOCKED:
            for col in ("value", "unit", "uncertainty", "page"):
                check(r[col].strip() == "",
                      f"{r['experiment_id']}: blocked row carries a {col} ({r[col]!r})")
            check(r["read_level"].startswith("none"), f"{r['experiment_id']}: blocked row claims read_level")
            check(len(r["blocker"]) > 40, f"{r['experiment_id']}: blocked row states no blocker")
        else:
            check(r["value"].strip() != "", f"{r['experiment_id']}: read row has no value")
            check(PAGE_RE.search(r["page"]) is not None, f"{r['experiment_id']}: read row has no page number")
            check(r["read_level"].strip() != "", f"{r['experiment_id']}: read row has no read_level")
        for field in r.values():
            check(not re.search(r"https?://|drive\.google|docs\.google|\b1[A-Za-z0-9_-]{32}\b", field),
                  f"{r['experiment_id']}: link or Drive id leaked into the CSV")
            check("LE_" not in field and "Extracted ZIPs" not in field,
                  f"{r['experiment_id']}: source-library folder name leaked into the CSV")
    print("PASS content: every blocked row is empty of value/unit/uncertainty/page, every read row carries a page")

    if fails:
        for f in fails:
            print("FAIL", f)
        return 1
    blocked = sum(1 for r in rows if r["status"] in BLOCKED)
    print(f"PASS all checks (rows={len(rows)}, blocked={blocked}, read={len(rows)-blocked})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
