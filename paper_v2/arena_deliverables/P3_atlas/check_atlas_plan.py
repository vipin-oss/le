#!/usr/bin/env python3
"""Validator for P3_atlas/atlas_plan.csv (Task 5)."""
import csv
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "atlas_plan.csv")
REQUIRED = ["problem_id", "wave_family", "bibkey", "DOI", "title", "year",
            "model_as_titled", "geometry_as_titled", "validation_target_proposed",
            "evidence_basis", "full_text_read", "in_current_atlas", "gap_note", "priority"]
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
FAMILIES = {"bulk", "surface (Rayleigh)", "Lamb / plate", "interface / layered",
            "shear / SH", "porous / voids", "multifield", "TED / damping"}
FORBIDDEN = [r"drive\.google", r"docs\.google", r"folders/", r"\[DRIVE",
             r"\b1[A-Za-z0-9_-]{32}\b"]


def main():
    ok = True
    rows = list(csv.DictReader(open(CSV, newline="")))
    header = list(rows[0].keys()) if rows else []
    if header != REQUIRED:
        print("FAIL header mismatch")
        return 1
    if len(rows) != 40:
        print("FAIL expected 40 proposed problems, found %d" % len(rows))
        ok = False
    ids, dois = set(), set()
    for i, r in enumerate(rows, 2):
        tag = "row %d (%s)" % (i, r.get("problem_id"))
        for col in REQUIRED:
            if not r[col].strip():
                print("FAIL %s: empty %s" % (tag, col))
                ok = False
        if r["problem_id"] in ids:
            print("FAIL %s: duplicate problem_id" % tag)
            ok = False
        ids.add(r["problem_id"])
        if not DOI_RE.match(r["DOI"]):
            print("FAIL %s: DOI is not a DOI: %r" % (tag, r["DOI"]))
            ok = False
        if r["DOI"] in dois:
            print("FAIL %s: duplicate DOI %s" % (tag, r["DOI"]))
            ok = False
        dois.add(r["DOI"])
        if r["wave_family"] not in FAMILIES:
            print("FAIL %s: unknown wave family %r" % (tag, r["wave_family"]))
            ok = False
        if not (r["year"].isdigit() and 2000 <= int(r["year"]) <= 2026):
            print("FAIL %s: year outside 2000-2026: %r" % (tag, r["year"]))
            ok = False
        if r["full_text_read"] != "no":
            print("FAIL %s: full_text_read must be 'no' for a proposal" % tag)
            ok = False
        if "title" not in r["evidence_basis"].lower():
            print("FAIL %s: evidence_basis must say the inference is from the title" % tag)
            ok = False
    counts = Counter(r["wave_family"] for r in rows)
    for fam in FAMILIES:
        if counts[fam] < 2:
            print("FAIL stratification: family %r has %d entries" % (fam, counts[fam]))
            ok = False
    blob = open(CSV, encoding="utf8").read()
    for pat in FORBIDDEN:
        if re.search(pat, blob, re.I):
            print("FAIL forbidden pattern in file: %s" % pat)
            ok = False
    if not ok:
        print("FAIL some checks failed")
        return 1
    print("PASS all checks (rows=%d, families=%d, min family size=%d)" %
          (len(rows), len(counts), min(counts.values())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
