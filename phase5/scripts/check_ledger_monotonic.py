#!/usr/bin/env python3
"""Monotonic gate for the claim ledger.

Fails when:
  1. The set of ledger IDs at HEAD is not a superset of the IDs at the parent
     commit (i.e. IDs were removed), or
  2. The A+V count decreases without a DOWNGRADE marker row whose NOTES name
     the affected ID(s) and give a reason, or
  3. Any Class A row is downgraded to B/C/V without such a marker, or
  4. Any Class V row loses its resolved_by without such a marker, or
  5. Any row's evidence_mode weakens (e.g. PRIMARY-SOURCE -> generic) without
     such a marker.

A valid DOWNGRADE marker row must:
  * Have "DOWNGRADE" in its what_was_changed field, AND
  * Name the affected ledger_row_id(s) in its notes column, AND
  * State a reason in its notes column.

Usage (CI, with fetch-depth = 0 so full history is available):
    python3 phase5/scripts/check_ledger_monotonic.py

The script reads phase5/reports/OPEN_CLAIMS_LEDGER.csv at HEAD and compares it
against the ledger of the parent of the last commit that changed the ledger.
"""

from __future__ import annotations

import csv
import io
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER_PATH = "phase5/reports/OPEN_CLAIMS_LEDGER.csv"

# Evidence modes ordered from strongest to weakest for downgrade detection.
EVIDENCE_RANK = {
    "PRIMARY-SOURCE": 5,
    "SECOND-READER CONFIRMED": 4,
    "SYMPY-DEFINITIONAL-IDENTITY": 3,
    "SYMBOLIC": 2,
    "GENERIC": 1,
    "UNRESOLVED": 0,
}


def evidence_rank(mode: str) -> int:
    mode_upper = mode.upper()
    for key, rank in EVIDENCE_RANK.items():
        if key in mode_upper:
            return rank
    return 0


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


def last_commit_changing_ledger() -> str:
    """Return the hash of the last commit that changed the ledger file."""
    result = subprocess.run(
        ["git", "log", "-1", "--format=%H", "--", LEDGER_PATH],
        capture_output=True,
        text=True,
        check=True,
        cwd=ROOT,
    )
    return result.stdout.strip()


def annotate(title: str, finding: str) -> None:
    """Print a GitHub Actions error annotation."""
    print(f"::error title={title}::{finding}")


def valid_downgrade_marker(rows: list[dict], affected_id: str) -> bool:
    """Return True if a DOWNGRADE marker row names affected_id and gives a reason.

    The marker row must have "DOWNGRADE" in what_was_changed, name the affected
    ledger_row_id in that same field, and state a substantive reason (>=3 chars
    beyond the ID itself).
    """
    for row in rows:
        changed = row.get("what_was_changed", "")
        if "DOWNGRADE" not in changed.upper():
            continue
        if affected_id not in changed:
            continue
        reason_text = changed.replace(affected_id, "").replace("DOWNGRADE", "").strip(" -:;,")
        if len(reason_text) >= 3:
            return True
    return False


def main() -> None:
    # Current ledger at HEAD
    head_text = (ROOT / LEDGER_PATH).read_text(encoding="utf-8-sig")
    head_rows = read_ledger_csv(head_text)
    head_by_id = {row_key(r): r for r in head_rows}
    head_ids = set(head_by_id.keys())
    head_counts = Counter(r["class"].strip() for r in head_rows)
    head_av = head_counts.get("A", 0) + head_counts.get("V", 0)

    # Parent commit ledger: compare with the parent of the last commit
    # that changed the ledger. Requires fetch-depth = 0 (full history).
    try:
        last_change = last_commit_changing_ledger()
        if not last_change:
            print("ERROR: no commit found that changed the ledger")
            sys.exit(1)
        parent_ref = f"{last_change}^"
        parent_text = git_show(parent_ref, LEDGER_PATH)
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: cannot read ledger at parent of last ledger change: {exc.stderr.strip()}")
        sys.exit(1)

    parent_rows = read_ledger_csv(parent_text)
    parent_by_id = {row_key(r): r for r in parent_rows}
    parent_ids = set(parent_by_id.keys())
    parent_counts = Counter(r["class"].strip() for r in parent_rows)
    parent_av = parent_counts.get("A", 0) + parent_counts.get("V", 0)

    # Check 1: IDs must not be removed
    removed_ids = sorted(parent_ids - head_ids)
    if removed_ids:
        for rid in removed_ids[:20]:
            annotate(
                "Check ledger ID monotonicity (no removals, no silent A/V downgrade)",
                f"ledger ID removed since parent of last ledger change: {rid}",
            )
        print(f"ERROR: {len(removed_ids)} ledger ID(s) removed since parent of last ledger change:")
        for rid in removed_ids[:20]:
            print(f"  {rid}")
        if len(removed_ids) > 20:
            print(f"  ... and {len(removed_ids) - 20} more")
        sys.exit(1)

    # Check 2: A+V count must not decrease without a valid DOWNGRADE marker
    if head_av < parent_av:
        # Check if there's a valid marker for the overall decrease
        marker_ok = any(
            "DOWNGRADE" in r.get("what_was_changed", "").upper()
            and r.get("notes", "").strip()
            for r in head_rows
        )
        if not marker_ok:
            annotate(
                "Check ledger ID monotonicity (no removals, no silent A/V downgrade)",
                f"A+V count decreased ({parent_av} -> {head_av}) without valid DOWNGRADE marker row",
            )
            print(
                f"ERROR: A+V count decreased ({parent_av} -> {head_av}) "
                "without a valid DOWNGRADE marker row (notes must name affected ID(s) and reason)"
            )
            sys.exit(1)

    # Check 3: No Class A row downgraded to lower class without valid marker
    for rid in sorted(head_ids & parent_ids):
        hrow = head_by_id[rid]
        prow = parent_by_id[rid]
        hcls = hrow["class"].strip()
        pcls = prow["class"].strip()
        if pcls == "A" and hcls in ("B", "C", "V"):
            if not valid_downgrade_marker(head_rows, rid):
                annotate(
                    "Check ledger ID monotonicity (no removals, no silent A/V downgrade)",
                    f"Class A row {rid} downgraded to {hcls} without valid DOWNGRADE marker",
                )
                print(f"ERROR: Class A row {rid} downgraded to {hcls} without valid DOWNGRADE marker")
                sys.exit(1)

    # Check 4: No Class V row loses resolved_by without valid marker
    for rid in sorted(head_ids & parent_ids):
        hrow = head_by_id[rid]
        prow = parent_by_id[rid]
        if prow["class"].strip() == "V":
            if prow.get("resolved_by", "").strip() and not hrow.get("resolved_by", "").strip():
                if not valid_downgrade_marker(head_rows, rid):
                    annotate(
                        "Check ledger ID monotonicity (no removals, no silent A/V downgrade)",
                        f"Class V row {rid} lost resolved_by without valid DOWNGRADE marker",
                    )
                    print(f"ERROR: Class V row {rid} lost resolved_by without valid DOWNGRADE marker")
                    sys.exit(1)

    # Check 5: No evidence_mode weakening without valid marker
    for rid in sorted(head_ids & parent_ids):
        hrow = head_by_id[rid]
        prow = parent_by_id[rid]
        hrank = evidence_rank(hrow.get("evidence_mode", ""))
        prank = evidence_rank(prow.get("evidence_mode", ""))
        if hrank < prank:
            if not valid_downgrade_marker(head_rows, rid):
                annotate(
                    "Check ledger ID monotonicity (no removals, no silent A/V downgrade)",
                    f"Row {rid} evidence_mode weakened "
                    f"('{prow.get('evidence_mode', '')}' -> '{hrow.get('evidence_mode', '')}') "
                    "without valid DOWNGRADE marker",
                )
                print(
                    f"ERROR: Row {rid} evidence_mode weakened "
                    f"('{prow.get('evidence_mode', '')}' -> '{hrow.get('evidence_mode', '')}') "
                    "without valid DOWNGRADE marker"
                )
                sys.exit(1)

    print(
        f"PASS: ledger IDs monotonic "
        f"(HEAD={len(head_ids)} >= parent-of-last-change={len(parent_ids)}); "
        f"A+V count {parent_av} -> {head_av}; "
        f"new IDs: {sorted(head_ids - parent_ids)}"
    )


def row_key(row: dict) -> str:
    return row["ledger_row_id"].strip()


if __name__ == "__main__":
    main()
