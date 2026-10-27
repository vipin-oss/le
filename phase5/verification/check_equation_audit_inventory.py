#!/usr/bin/env python3
"""Check that the Section 4--10 equation audit covers every display group.

This is an inventory/coverage gate only. It verifies source locations, labels,
allowed statuses, and non-empty scope/evidence/action fields; it does not
validate any equation, source transcription, derivation, or physical claim.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports/EQUATION_AUDIT.csv"
SECTIONS = {
    4: "thermoelastic",
    5: "multiphysics",
    6: "transport",
    7: "nonlocal",
    8: "mathematical_methods",
    9: "interfaces",
    10: "energy",
}
ALLOWED = {"VERIFIED-SOURCE", "VERIFIED-SYMBOLIC", "CONDITIONAL", "OPEN"}
ENV = re.compile(r"\\begin\{(equation\*?)\}(.*?)\\end\{\1\}", re.S)
LABEL = re.compile(r"\\label\{([^}]+)\}")


def strip_comments(text: str) -> str:
    """Remove TeX comments while preserving line count and escaped percent signs."""
    result = []
    for line in text.splitlines(keepends=True):
        backslashes = 0
        cut = None
        for index, char in enumerate(line):
            if char == "%" and backslashes % 2 == 0:
                cut = index
                break
            backslashes = backslashes + 1 if char == "\\" else 0
        if cut is None:
            result.append(line)
        else:
            ending = line[len(line.rstrip("\r\n")):]
            result.append(line[:cut] + ending)
    return "".join(result)


def source_inventory() -> list[tuple[int, str, int, str]]:
    displays = []
    for section, stem in SECTIONS.items():
        relative = f"master/sections/sec{section:02d}_{stem}.tex"
        text = strip_comments((ROOT / relative).read_text(encoding="utf-8"))
        for ordinal, match in enumerate(ENV.finditer(text), 1):
            line = text.count("\n", 0, match.start()) + 1
            label_match = LABEL.search(match.group(2))
            label = label_match.group(1) if label_match else f"UNNUMBERED-DISPLAY-{ordinal}"
            displays.append((section, relative, line, label))
    return displays


def main() -> None:
    expected = source_inventory()
    with REPORT.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    required = {
        "audit_id", "section", "source_file", "line", "label", "display_tex",
        "status", "source_anchor_or_script", "scope_and_assumptions",
        "negative_test", "ledger_rows", "next_action",
    }
    if not rows or not required.issubset(rows[0]):
        raise SystemExit(f"FAIL: audit CSV missing required columns: {sorted(required)}")
    actual = []
    for row in rows:
        try:
            actual.append((int(row["section"]), row["source_file"], int(row["line"]), row["label"]))
        except (TypeError, ValueError) as exc:
            raise SystemExit(f"FAIL: malformed source location in {row.get('audit_id')}: {exc}")
        if row["status"] not in ALLOWED:
            raise SystemExit(f"FAIL: invalid status for {row['audit_id']}: {row['status']}")
        for field in ("display_tex", "source_anchor_or_script", "scope_and_assumptions", "negative_test", "ledger_rows", "next_action"):
            if not row[field].strip():
                raise SystemExit(f"FAIL: empty {field} for {row['audit_id']}")
    if len(actual) != len(set(actual)):
        raise SystemExit("FAIL: duplicate equation display row in audit CSV")
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    if missing or extra:
        raise SystemExit(f"FAIL: equation inventory mismatch; missing={missing}; extra={extra}")
    if len(rows) != len(expected):
        raise SystemExit(f"FAIL: row count {len(rows)} != display count {len(expected)}")
    print(f"PASS: all {len(expected)} displayed equation groups in Sections 4--10 have one audit row")
    print("Scope: inventory coverage only; no formula/source/derivation validation")


if __name__ == "__main__":
    main()
