#!/usr/bin/env python3
"""Monotonic gate for the claim ledger.

Fails when the set of ledger IDs at HEAD is not a superset of the IDs at the
parent commit (i.e. IDs were removed), or when the A+V count decreases without
an explicit DOWNGRADE marker row.

Usage (CI, with fetch-depth >= 2):
    python3 phase5/scripts/check_ledger_monotonic.py

The script reads phase5/reports/OPEN_CLAIMS_LEDGER.csv at HEAD and compares it
against `git show HEAD~1:phase5/reports/OPEN_CLAIMS_LEDGER.csv`.
"""

from __future__ import annotations

import csv
import io
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER_PATH = "phase5/reports/OPEN_CLAIMS_LEDGER.csv"


def read_ledger_csv(text: str) -> list[dict]:
    # Strip BOM, normalize CRLF -> LF before parsing
    text = text.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    reader = csv.DictReader(io.StringIO(text, newline=""))
    return list(reader)


def git_show(ref: str, path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        capture_output=True,
        text=True,
        check=True,
        cwd=ROOT,
    )
    return result.stdout


def main() -> None:
    # Current ledger at HEAD
    head_text = (ROOT / LEDGER_PATH).read_text(encoding="utf-8-sig")
    head_rows = read_ledger_csv(head_text)
    head_ids = {row["ledger_row_id"].strip() for row in head_rows}
    head_counts = Counter(row["class"].strip() for row in head_rows)
    head_av = head_counts.get("A", 0) + head_counts.get("V", 0)

    # Parent commit ledger
    try:
        parent_text = git_show("HEAD~1", LEDGER_PATH)
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: cannot read ledger at HEAD~1: {exc.stderr.strip()}")
        sys.exit(1)

    parent_rows = read_ledger_csv(parent_text)
    parent_ids = {row["ledger_row_id"].strip() for row in parent_rows}
    parent_counts = Counter(row["class"].strip() for row in parent_rows)
    parent_av = parent_counts.get("A", 0) + parent_counts.get("V", 0)

    # Check 1: IDs must not be removed
    removed_ids = sorted(parent_ids - head_ids)
    if removed_ids:
        print(f"ERROR: {len(removed_ids)} ledger ID(s) removed since HEAD~1:")
        for rid in removed_ids[:20]:
            print(f"  {rid}")
        if len(removed_ids) > 20:
            print(f"  ... and {len(removed_ids) - 20} more")
        sys.exit(1)

    # Check 2: A+V count must not decrease without a DOWNGRADE marker row
    downgrade_rows = [
        row for row in head_rows if "DOWNGRADE" in row.get("what_was_changed", "").upper()
    ]
    if head_av < parent_av and not downgrade_rows:
        print(
            f"ERROR: A+V count decreased ({parent_av} -> {head_av}) "
            "without a DOWNGRADE marker row"
        )
        sys.exit(1)

    print(
        f"PASS: ledger IDs monotonic (HEAD={len(head_ids)} >= HEAD~1={len(parent_ids)}); "
        f"A+V count {parent_av} -> {head_av}; new IDs: {sorted(head_ids - parent_ids)}"
    )


if __name__ == "__main__":
    main()

# End of script
