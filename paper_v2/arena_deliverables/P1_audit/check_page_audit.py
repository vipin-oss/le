#!/usr/bin/env python3
"""Gate for the page-level audit artifacts.

Reads what `audit_pages.py` produced and refuses the state if anything is
missing, contradictory, or failing.  Prints a line starting with PASS and
exits 0 only when every assertion holds.

Usage:  python3 P1_audit/check_page_audit.py [--dir P1_audit]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

REQUIRED_PASS = [
    "P01",  # identity
    "P03",  # no ??
    "P04",  # no [?]
    "P05",  # no leaked LaTeX
    "P06",  # all titles rendered
    "P08",  # keywords
    "P09",  # declarations
    "P10",  # abstract length
    "P12",  # captions
    "P14",  # register vocabulary
    "P17",  # citations resolve
    "P19",  # fonts embedded
    "P23",  # no orphan sources
    "P24",  # float numbering
    "P26",  # section order
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="P1_audit")
    a = ap.parse_args()
    d = Path(a.dir)
    csv_path = d / "page_audit_results.csv"
    sum_path = d / "PAGE_AUDIT_SUMMARY.md"
    map_path = d / "section_pagemap.csv"

    problems: list[str] = []
    notes: list[str] = []

    for f in (csv_path, sum_path, map_path):
        if not f.exists():
            print(f"FAIL (missing artifact: {f})")
            return 1

    rows = list(csv.DictReader(csv_path.open(encoding="utf-8")))
    by_id = {r["check_id"]: r for r in rows}

    if len(rows) != len(by_id):
        problems.append("duplicate check ids in results table")
    for i in range(1, 27):
        cid = f"P{i:02d}"
        if cid not in by_id:
            problems.append(f"missing check {cid}")

    fails = [r for r in rows if r["verdict"] == "FAIL"]
    if fails:
        problems.append("failing checks: " + ", ".join(f"{r['check_id']}" for r in fails))
    for cid in REQUIRED_PASS:
        if cid in by_id and by_id[cid]["verdict"] != "PASS":
            problems.append(f"{cid} expected PASS, got {by_id[cid]['verdict']}")

    # extent
    pages = words = 0
    m = re.search(r"pages=(\d+)", by_id.get("P02", {}).get("observed", ""))
    if not m:
        m = re.search(r"(\d+) pages", by_id.get("P02", {}).get("observed", ""))
    if m:
        pages = int(m.group(1))
    mw = re.search(r"([\d,]+) words", by_id.get("P02", {}).get("observed", ""))
    if mw:
        words = int(mw.group(1).replace(",", ""))
    if pages < 100:
        problems.append(f"page count implausibly small ({pages})")
    if words < 40_000:
        problems.append(f"word count implausibly small ({words})")
    notes.append(f"pages={pages} words={words}")

    # register statuses must all be defined labels
    obs = by_id.get("P14", {}).get("observed", "")
    labels = dict(re.findall(r"([A-Z][A-Z-]+)=(\d+)", obs))
    total = sum(int(v) for v in labels.values())
    if total == 0:
        problems.append("register statuses not parsed")
    notes.append(f"register rows={total} labels={len(labels)}")

    # section map completeness and monotonicity
    pmap = list(csv.DictReader(map_path.open(encoding="utf-8")))
    if len(pmap) < 20:
        problems.append(f"section map too small ({len(pmap)} rows)")
    if any(not r["first_page"] for r in pmap):
        problems.append("section map has unmapped sections")
    seq = [int(r["first_page"]) for r in pmap if r["first_page"]]
    if seq != sorted(seq):
        problems.append("section map page order not monotonic")
    notes.append(f"sections={len(pmap)}")

    # summary file must agree with the results table
    summary = sum_path.read_text(encoding="utf-8")
    m = re.search(r"checks: (\d+)\s+\((\d+) PASS, (\d+) REPORT, (\d+) FAIL\)", summary)
    if not m:
        problems.append("summary line missing or malformed")
    else:
        if int(m.group(1)) != len(rows):
            problems.append("summary check count disagrees with results table")
        if int(m.group(4)) != len(fails):
            problems.append("summary FAIL count disagrees with results table")
        notes.append(f"summary says {m.group(2)} PASS / {m.group(3)} REPORT / {m.group(4)} FAIL")

    if problems:
        print("FAIL (" + "; ".join(problems) + ")")
        return 1

    print(f"PASS (checks={len(rows)}, fail=0, {', '.join(notes)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
