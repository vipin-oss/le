#!/usr/bin/env python3
"""Check structural coverage and ledger links in the Q3 theory-status matrix.

This validates family coverage and evidence-class references only. It does not
independently verify any source claim or settle any model-specific dispute.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "reports/Q3_THEORY_STATUS.csv"
LEDGER = ROOT / "reports/OPEN_CLAIMS_LEDGER.csv"
EXPECTED = {
    "Classical local Cauchy/Fourier",
    "Lord–Shulman (LS)",
    "Green–Lindsay (GL)",
    "Green–Naghdi I (GN-I)",
    "Green–Naghdi II (GN-II)",
    "Green–Naghdi III (GN-III)",
    "Dual-phase-lag (DPL)",
    "Triple-phase-lag (TPL)",
    "Moore–Gibson–Thompson (MGT)",
    "Memory-dependent derivative (MDD)",
    "Fractional scalar / thermoelastic",
    "Spatially nonlocal elasticity",
    "Positive-gradient models",
    "Coupled multiphysics / piezothermoelastic",
}
REQUIRED_COLUMNS = {
    "family",
    "established_status",
    "established_anchor",
    "established_ledger_rows",
    "disputed_or_variant_status",
    "counterexample_or_ill_posedness_status",
    "disputed_anchor",
    "disputed_ledger_rows",
    "open_question",
    "open_ledger_rows",
}

with MATRIX.open(newline="", encoding="utf-8") as stream:
    reader = csv.DictReader(stream)
    assert set(reader.fieldnames or ()) == REQUIRED_COLUMNS
    rows = list(reader)
assert len(rows) == len(EXPECTED)
assert {row["family"] for row in rows} == EXPECTED

with LEDGER.open(newline="", encoding="utf-8-sig") as stream:
    ledger_rows = {row["ledger_row_id"]: row for row in csv.DictReader(stream)}

for row in rows:
    for column in REQUIRED_COLUMNS - {"family"}:
        assert row[column].strip(), f"{row['family']}: empty {column}"
    for column in ("established_ledger_rows", "disputed_ledger_rows", "open_ledger_rows"):
        ids = [item.strip() for item in row[column].split(";")]
        assert ids and all(re.fullmatch(r"OCL-\d{3}", item) for item in ids)
        assert all(item in ledger_rows for item in ids), f"{row['family']}: unknown ledger id in {column}"
    established_ids = [item.strip() for item in row["established_ledger_rows"].split(";")]
    if row["established_status"].startswith(("No ", "None ")):
        assert any(ledger_rows[item]["class"] in {"B", "C"} for item in established_ids), row["family"]
    else:
        assert all(ledger_rows[item]["class"] in {"A", "V"} for item in established_ids), row["family"]

content = MATRIX.read_text(encoding="utf-8")
by_family = {row["family"]: row for row in rows}
for row in rows:
    if row["established_status"].startswith(("No ", "None ")):
        continue
    for item in (value.strip() for value in row["established_ledger_rows"].split(";")):
        entry = ledger_rows[item]
        if entry["class"] == "A":
            assert entry["resolved_by"].strip() and entry["evidence_mode"].strip(), item
        elif entry["class"] == "V":
            script = entry["resolved_by"].split(";")[0].strip()
            assert script and (ROOT.parent / script).is_file(), f"{item}: missing reproducible script {script}"

# Keep the principal unresolved source/variant issues visible in their family rows.
for family, column, required in (
    ("Dual-phase-lag (DPL)", "disputed_ledger_rows", {"OCL-445", "OCL-488"}),
    ("Dual-phase-lag (DPL)", "open_ledger_rows", {"OCL-488"}),
    ("Green–Naghdi II (GN-II)", "established_ledger_rows", {"OCL-493"}),
    ("Green–Naghdi II (GN-II)", "open_ledger_rows", {"OCL-491"}),
    ("Green–Naghdi III (GN-III)", "established_ledger_rows", {"OCL-494"}),
    ("Green–Naghdi III (GN-III)", "open_ledger_rows", {"OCL-492"}),
    ("Moore–Gibson–Thompson (MGT)", "open_ledger_rows", {"OCL-174", "OCL-175"}),
    ("Memory-dependent derivative (MDD)", "open_ledger_rows", {"OCL-402"}),
    ("Fractional scalar / thermoelastic", "open_ledger_rows", {"OCL-403"}),
    ("Lord–Shulman (LS)", "open_ledger_rows", {"OCL-011"}),
):
    actual = {item.strip() for item in by_family[family][column].split(";")}
    assert required <= actual, f"{family}: unresolved issue missing from {column}"
assert "unstable solutions" in by_family["Dual-phase-lag (DPL)"]["disputed_or_variant_status"]
assert "equality is unclassified" in by_family["Dual-phase-lag (DPL)"]["disputed_or_variant_status"]
dpl_counterexample = by_family["Dual-phase-lag (DPL)"]["counterexample_or_ill_posedness_status"]
assert "one-dimensional problem" in dpl_counterexample and "not a universal ill-posedness result" in dpl_counterexample
mgt_counterexample = by_family["Moore–Gibson–Thompson (MGT)"]["counterexample_or_ill_posedness_status"]
assert "OCL-175" in mgt_counterexample and "pending source verification" in mgt_counterexample
gn3_status = by_family["Green–Naghdi III (GN-III)"]["established_status"]
assert "Fourier-conductivity-dominant" in gn3_status and "negligible-conductivity" in gn3_status
assert all(row["counterexample_or_ill_posedness_status"].strip() for row in rows)

assert not re.search(r"drive\.google\.com|docs\.google\.com|open\?id=|drive/(?:file|folders)/[A-Za-z0-9_-]{25,}", content, re.I)
print("PASS: Q3 matrix covers all 14 requested theory families with established, variant/dispute, and open fields")
print("PASS: established A/V rows have provenance or an existing derivation script; family-specific unresolved rows remain linked")
print("PASS: Quintanilla instability counterexample, critical equality, and DOI conflict remain visible under DPL")
print("Scope: structural/source-map consistency only; this check does not independently re-read primary sources or adjudicate conflicts")
