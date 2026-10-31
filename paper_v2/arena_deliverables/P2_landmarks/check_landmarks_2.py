#!/usr/bin/env python3
"""Validator for P2_landmarks/landmarks_2.csv (Task 3)."""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "landmarks_2.csv")
REQUIRED = ["landmark_id", "Authors", "Title", "Journal_or_publisher", "Volume",
            "Pages", "Year", "DOI", "doi_status", "relevance_one_line",
            "belongs_in_section", "in_paper_status", "verified_from"]
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
FORBIDDEN = [r"drive\.google", r"docs\.google", r"folders/", r"\[DRIVE",
             r"\b1[A-Za-z0-9_-]{32}\b"]
ALLOWED_STATUS = {"verified on publisher page", "book with no DOI"}
ALLOWED_PAPER = {"missing from bibliography", "in bibliography but never cited"}


def main():
    ok = True
    with open(CSV, newline="") as f:
        rows = list(csv.DictReader(f))
        header = rows[0].keys() if rows else []
    if list(header) != REQUIRED:
        print("FAIL header mismatch: %s" % list(header))
        return 1
    if not rows:
        print("FAIL no rows")
        return 1
    ids = set()
    for i, r in enumerate(rows, 2):
        tag = "row %d (%s)" % (i, r.get("landmark_id", "?"))
        book = r["doi_status"] == "book with no DOI" or bool(
            re.search(r"press|springer|wiley|elsevier|academic|university",
                      r["Journal_or_publisher"], re.I))
        for col in REQUIRED:
            if not r[col].strip():
                # a monograph has no volume/pages of its own
                if book and col in ("Volume", "Pages"):
                    continue
                print("FAIL %s: empty %s" % (tag, col))
                ok = False
        if r["landmark_id"] in ids:
            print("FAIL %s: duplicate landmark_id" % tag)
            ok = False
        ids.add(r["landmark_id"])
        if not (DOI_RE.match(r["DOI"]) or r["DOI"] == "NOT FOUND"):
            print("FAIL %s: DOI is neither a DOI nor NOT FOUND: %r" % (tag, r["DOI"]))
            ok = False
        if r["doi_status"] not in ALLOWED_STATUS:
            print("FAIL %s: unexpected doi_status %r" % (tag, r["doi_status"]))
            ok = False
        if r["DOI"] == "NOT FOUND" and r["doi_status"] != "book with no DOI":
            print("FAIL %s: NOT FOUND DOI must be labelled 'book with no DOI'" % tag)
            ok = False
        if r["DOI"] != "NOT FOUND" and r["doi_status"] != "verified on publisher page":
            print("FAIL %s: DOI given but not marked verified" % tag)
            ok = False
        if r["in_paper_status"] not in ALLOWED_PAPER:
            print("FAIL %s: unexpected in_paper_status %r" % (tag, r["in_paper_status"]))
            ok = False
        if not r["Year"].isdigit() or not (1900 <= int(r["Year"]) <= 2026):
            print("FAIL %s: implausible year %r" % (tag, r["Year"]))
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
