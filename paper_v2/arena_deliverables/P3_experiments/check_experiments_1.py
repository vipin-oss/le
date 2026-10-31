#!/usr/bin/env python3
"""Validator for P3_experiments/experiments_1.csv (Task 4)."""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "experiments_1.csv")
REQUIRED = ["entry_id", "material_system", "temperature", "method",
            "quoted_number_with_units", "quote_location", "model_used_to_extract",
            "uncertainty_or_identifiability_stated", "DOI", "doi_source",
            "read_level", "relevance_to_paper", "notes"]
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
READ_LEVELS = {"abstract only", "metadata only",
               "abstract plus excerpted article text (publisher page)", "full text"}
FORBIDDEN = [r"drive\.google", r"docs\.google", r"folders/", r"\[DRIVE",
             r"\b1[A-Za-z0-9_-]{32}\b"]
NUMBERISH = re.compile(r"\d")


def main():
    ok = True
    rows = list(csv.DictReader(open(CSV, newline="")))
    header = list(rows[0].keys()) if rows else []
    if header != REQUIRED:
        print("FAIL header mismatch: %s" % header)
        return 1
    ids = set()
    for i, r in enumerate(rows, 2):
        tag = "row %d (%s)" % (i, r["entry_id"])
        for col in REQUIRED:
            if not r[col].strip():
                print("FAIL %s: empty %s" % (tag, col))
                ok = False
        if r["entry_id"] in ids:
            print("FAIL %s: duplicate entry_id" % tag)
            ok = False
        ids.add(r["entry_id"])
        if not (DOI_RE.match(r["DOI"]) or r["DOI"] == "NOT FOUND"):
            print("FAIL %s: bad DOI %r" % (tag, r["DOI"]))
            ok = False
        if r["read_level"] not in READ_LEVELS:
            print("FAIL %s: unexpected read_level %r" % (tag, r["read_level"]))
            ok = False
        q = r["quoted_number_with_units"].lower()
        if r["read_level"] == "metadata only" and not q.startswith(("not read", "no number", "unknown")):
            print("FAIL %s: metadata-only entry quotes a number: %r" % (tag, q[:40]))
            ok = False
        if r["read_level"] == "abstract only" and NUMBERISH.search(q) and "abstract" not in r["quote_location"].lower():
            print("FAIL %s: number quoted but the quote location is not the abstract" % tag)
            ok = False
        if r["uncertainty_or_identifiability_stated"].lower() not in (
                "yes", "no", "not applicable", "unknown") and not r["uncertainty_or_identifiability_stated"].lower().startswith(("yes -", "qualitative")):
            print("FAIL %s: uncertainty field not in the controlled vocabulary: %r" %
                  (tag, r["uncertainty_or_identifiability_stated"][:40]))
            ok = False
    blob = open(CSV, encoding="utf8").read()
    for pat in FORBIDDEN:
        if re.search(pat, blob, re.I):
            print("FAIL forbidden pattern in file: %s" % pat)
            ok = False
    if not ok:
        print("FAIL some checks failed")
        return 1
    print("PASS all checks (rows=%d, columns=%d)" % (len(rows), len(REQUIRED)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
