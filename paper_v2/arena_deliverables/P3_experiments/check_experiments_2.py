#!/usr/bin/env python3
"""Validate the Task 4 second-pass deliverable (`extraction_protocol.csv`).

The second pass could not be executed: the six blocking papers plus the Zener
source are present only inside archive bundles that exceed the extraction cap,
and this environment has no network route to fetch them.  What is delivered
instead is the *protocol* - for every blocking entry, the exact quantity to pull
out of the paper, the conversion to a relaxation time, how the uncertainty is to
be handled, and where in the paper to look.  This validator makes sure that
protocol is complete and, more importantly, that it contains **no measured value**:
a protocol cannot smuggle in a number that was never read.

Checks:
 1. header is exactly the declared schema (11 columns, fixed order);
 2. 9 target rows, unique target ids;
 3. every entry_id that is not an ATT* target exists in experiments_1.csv;
 4. DOI column is either '-' or a well-formed DOI;
 5. status is one of the three honest states, i.e. nothing is marked READ;
 6. the free-text columns are non-empty, and the two columns that would carry a
    reading (value, page) do not exist at all;
 7. no cell in the file looks like a measured relaxation time (a number followed
    by 's', 'ps', 'ns' or 'fs') - that pattern would mean a value was invented.

Prints PASS lines and exits 0.  Standard library only.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROTO = os.path.join(HERE, "extraction_protocol.csv")
EXP1 = os.path.join(HERE, "experiments_1.csv")

SCHEMA = ["target_id", "entry_id", "source", "DOI", "quantity_to_extract", "paper_symbol",
          "conversion_to_relaxation_time", "uncertainty_handling", "where_to_look",
          "status", "blocker"]
STATUS_OK = {"BLOCKED_ARCHIVE_OVER_CAP", "BLOCKED_SOURCE_NOT_IDENTIFIED",
             "READY_WHEN_PDF_AVAILABLE"}
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
# a value with a time unit, e.g. "1.4 ps", "3e-12 s" - must not appear anywhere
TIME_VALUE_RE = re.compile(r"\b\d+(?:\.\d+)?(?:[eE][-+]?\d+)?\s*(?:fs|ps|ns|us|s)\b")

errors = []


def fail(m):
    errors.append(m)


def main():
    with open(PROTO, newline="") as fh:
        rdr = csv.reader(fh)
        header = next(rdr)
        rows = [dict(zip(header, r)) for r in rdr]
    if header != SCHEMA:
        fail("header is %s, expected %s" % (header, SCHEMA))
    print("PASS header: %d columns in the declared order" % len(header))

    if len(rows) != 9:
        fail("expected 9 target rows, found %d" % len(rows))
    ids = [r["target_id"] for r in rows]
    if len(set(ids)) != len(ids):
        fail("duplicate target ids: %s" % ids)
    print("PASS rows: %d targets, ids unique" % len(rows))

    with open(EXP1, newline="") as fh:
        exp1_ids = {r["entry_id"] for r in csv.DictReader(fh)}
    for r in rows:
        if not r["entry_id"].startswith("ATT") and r["entry_id"] not in exp1_ids:
            fail("%s: entry_id %r is not in experiments_1.csv" % (r["target_id"], r["entry_id"]))
    print("PASS linkage: every blocked entry id exists in experiments_1.csv")

    for r in rows:
        doi = r["DOI"].strip()
        if doi != "-" and not DOI_RE.match(doi):
            fail("%s: malformed DOI %r" % (r["target_id"], doi))
        if r["status"] not in STATUS_OK:
            fail("%s: status %r is not an honest blocked/ready state"
                 % (r["target_id"], r["status"]))
        for col in ("quantity_to_extract", "conversion_to_relaxation_time",
                    "uncertainty_handling", "where_to_look", "blocker"):
            if not r[col].strip():
                fail("%s: empty %s" % (r["target_id"], col))
    print("PASS content: DOI syntax, status vocabulary and all instruction columns filled")

    text = open(PROTO).read()
    hits = [m.group(0) for m in TIME_VALUE_RE.finditer(text)]
    if hits:
        fail("the protocol contains time values, which would mean a measurement was "
             "recorded: %s" % hits[:5])
    print("PASS no measured value: no time-unit number appears anywhere in the file")

    if errors:
        for e in errors:
            print("FAIL " + e)
        print("FAIL %d check(s) failed" % len(errors))
        return 1
    blocked = sum(1 for r in rows if r["status"].startswith("BLOCKED"))
    print("PASS all checks (rows=%d, columns=%d, blocked=%d, read=0)"
          % (len(rows), len(header), blocked))
    return 0


if __name__ == "__main__":
    sys.exit(main())
