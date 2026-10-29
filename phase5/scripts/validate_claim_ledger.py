#!/usr/bin/env python3
"""Validate claim-ledger classes and the provenance required for A/V entries."""
from __future__ import annotations

import csv
import sys
import traceback
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports" / "OPEN_CLAIMS_LEDGER.csv"
EXPECTED = {
    "ledger_row_id",
    "section",
    "tex_file:line",
    "old_text_short",
    "class",
    "what_was_changed",
    "needed_source",
    "resolved_by",
    "evidence_mode",
}

try:
    with LEDGER.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if set(reader.fieldnames or ()) != EXPECTED:
            raise SystemExit(f"Unexpected ledger columns: {reader.fieldnames}")
        rows = list(reader)
except SystemExit:
    raise
except Exception as exc:
    print(f"FATAL: cannot read ledger: {exc}")
    traceback.print_exc()
    sys.exit(1)

errors: list[str] = []
ids = [row["ledger_row_id"].strip() for row in rows]
if len(ids) != len(set(ids)):
    errors.append("duplicate ledger_row_id")

allowed = {"A", "B", "C", "V"}
counts = Counter(row["class"].strip() for row in rows)
for row in rows:
    row_id = row["ledger_row_id"].strip()
    cls = row["class"].strip()
    resolved = row["resolved_by"].strip()
    if cls not in allowed:
        errors.append(f"{row_id}: unsupported class {cls!r}")
        continue
    if cls == "A" and not resolved:
        errors.append(f"{row_id}: Class A row lacks resolved_by source anchor")
    if cls == "V":
        if not resolved:
            errors.append(f"{row_id}: Class V row lacks resolved_by script/derivation")
            continue
        script = resolved.split(":", 1)[0]
        if not (ROOT.parent / script).is_file():
            errors.append(f"{row_id}: Class V verification path does not exist: {script}")
        if not row["evidence_mode"].strip():
            errors.append(f"{row_id}: Class V row lacks evidence_mode")

print(f"Claim ledger rows: {len(rows)}; classes: {dict(sorted(counts.items()))}")
for error in errors:
    print("ERROR:", error)
sys.exit(bool(errors))
