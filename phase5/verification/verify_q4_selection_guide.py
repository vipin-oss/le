#!/usr/bin/env python3
"""Check that the conditional Q4 guide remains mapped to evidence and open gaps.

This is a structural/provenance check. It does not independently validate
primary-source claims, prove model admissibility, or validate a numerical
benchmark solution.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

# Note: manuscript uses "Symbolically verified" (not "Script-verified")
# terminology; this gate checks for the current prose labels.
ROOT = Path(__file__).resolve().parents[1]
SECTION = ROOT / "master/sections/sec16_future.tex"
BIB = ROOT / "master/references_local.bib"
LEDGER = ROOT / "reports/OPEN_CLAIMS_LEDGER.csv"
APP_C = ROOT / "master/appendices/appC_benchmarks.tex"

text = SECTION.read_text(encoding="utf-8")
start = text.index(r"\subsection{Conditional theory-selection guide and evidence checkpoints}")
end = text.index(r"\subsection{Coupled-field modeling in emerging materials}", start)
guide = text[start:end]

required_phrases = (
    "not a ranking of theories",
    "Local thermoelastic baseline",
    "One-time heat-flux relaxation",
    "Green--Naghdi models",
    "Lag-based transport",
    "Spatial, fractional, or hereditary operators",
    "Additional coupled fields",
    "Benchmark evidence: derivations versus source checkpoints",
    "Research roadmap from the Q3 evidence gaps",
    "The GN-III type-II/type-III scope distinction is image-checked",
    "the zero-source map from source Eqs. (3.19)–(3.20) to manuscript Eqs. (4.1) and (4.14) is verified",
    "specifications rather than numerically validated reference solutions",
    "two-wave cross-term is shown before time averaging",
    "equality case is not classified",
)
for phrase in required_phrases:
    assert phrase in guide, f"Q4 guide missing required bounded statement: {phrase}"

required_citations = {
    "Biot1956",
    "Lord1967",
    "Green1993",
    "GreenGN1992",
    "Quintanilla2003DPL",
    "RoyChoudhuri2007",
    "Eringen1983",
}
bib = BIB.read_text(encoding="utf-8")
for key in required_citations:
    assert re.search(r"@\w+\s*\{" + re.escape(key) + r"\s*,", bib), f"Missing bibliography key {key}"
    assert re.search(r"\\cite(?:\[[^\]]*\])?\{[^}]*\b" + re.escape(key) + r"\b[^}]*\}", guide), f"Missing guide citation {key}"

with LEDGER.open(newline="", encoding="utf-8-sig") as stream:
    ledger = {row["ledger_row_id"]: row for row in csv.DictReader(stream)}

required_classes = {
    "OCL-011": "C",
    "OCL-123": "C",
    "OCL-169": "A",
    "OCL-174": "A",
    "OCL-175": "A",
    "OCL-195": "A",
    "OCL-258": "A",
    "OCL-321": "A",
    "OCL-402": "B",
    "OCL-403": "B",
    "OCL-445": "A",
    "OCL-466": "V",
    "OCL-467": "V",
    "OCL-468": "V",
    "OCL-470": "V",
    "OCL-471": "V",
    "OCL-472": "V",
    "OCL-473": "V",
    "OCL-480": "V",
    "OCL-483": "B",
    "OCL-485": "B",
    "OCL-491": "B",
    "OCL-492": "B",
    "OCL-493": "A",
    "OCL-494": "A",
    "OCL-495": "A",
    "OCL-496": "A",
    "OCL-498": "V",
}
for row_id, expected_class in required_classes.items():
    assert row_id in ledger, f"Missing evidence row {row_id}"
    assert ledger[row_id]["class"] == expected_class, f"{row_id}: expected {expected_class}, got {ledger[row_id]['class']}"
    if expected_class in {"A", "V"}:
        assert ledger[row_id]["resolved_by"].strip(), f"{row_id}: missing source or derivation"
        assert ledger[row_id]["evidence_mode"].strip(), f"{row_id}: missing evidence mode"

# Keep each displayed guide decision tied to its own source/script and open rows.
section_mappings = {
    "Local thermoelastic baseline": ("OCL-480",),
    "One-time heat-flux relaxation": ("OCL-495", "OCL-011"),
    "Green--Naghdi models": ("OCL-493", "OCL-494", "OCL-498", "OCL-491", "OCL-492"),
    "Lag-based transport": ("OCL-445", "OCL-169", "OCL-488", "OCL-123"),
    "Spatial, fractional, or hereditary operators": ("OCL-258", "OCL-321", "OCL-402", "OCL-403"),
    "Additional coupled fields": ("OCL-195", "OCL-483", "OCL-485"),
}
for phrase, row_ids in section_mappings.items():
    assert phrase in guide, f"Missing mapped guide decision {phrase}"
    assert all(row_id in ledger for row_id in row_ids), f"{phrase}: missing mapped evidence row"

benchmark_mappings = {
    "Symbolically verified identity": ("OCL-480",),
    "Symbolically verified interface check": ("OCL-466", "OCL-467", "OCL-468"),
    "Symbolically verified algebra": ("OCL-470", "OCL-471", "OCL-472", "OCL-473"),
    "Primary-source checkpoint": ("OCL-493", "OCL-494", "OCL-495", "OCL-496"),
}
for phrase, row_ids in benchmark_mappings.items():
    assert phrase in guide, f"Missing benchmark evidence category {phrase}"
    assert all(row_id in ledger for row_id in row_ids), f"{phrase}: missing mapped evidence row"

script_rows = ("OCL-466", "OCL-467", "OCL-468", "OCL-470", "OCL-471", "OCL-472", "OCL-473", "OCL-480", "OCL-498")
for row_id in script_rows:
    script = ledger[row_id]["resolved_by"].split(";")[0].strip()
    assert script and (ROOT.parent / script).is_file(), f"{row_id}: missing verifier {script}"

assert r"\subsection{Benchmark evidence: derivations versus source checkpoints}" in guide
assert "Primary-source checkpoint" in guide and "Symbolically verified identity" in guide
assert "BM-1--BM-5" in guide and "BM-1: Classical elastic interface" in APP_C.read_text(encoding="utf-8")
assert "not a general interface theorem" in guide
assert not re.search(r"drive\.google\.com|docs\.google\.com|open\?id=|drive/(?:file|folders)/[A-Za-z0-9_-]{25,}", guide, re.I)
assert not re.search(r"phase5/|phase4/|\.csv", guide, re.I), "Repository-internal path leaked into rendered guide"
assert not re.search(r"\bOCL-\d{3}\b", guide), "Internal ledger ID leaked into rendered guide"

row = ledger.get("OCL-497")
assert row and row["class"] == "V"
assert row["resolved_by"].split(";")[0].strip() == "phase5/verification/verify_q4_selection_guide.py"
assert "STRUCTURAL COVERAGE" in row["evidence_mode"]

print("PASS: conditional theory guide covers scoped model choices, source limits, script checks, and Q3 gaps")
print("PASS: cited A/V and unresolved B/C ledger records remain present with source/script provenance")
print("PASS: BM-1--BM-5 are identified as specifications, not misreported as validated numerical outcomes")
print("Scope: structural/provenance consistency only; no source re-review or independent numerical proof")
