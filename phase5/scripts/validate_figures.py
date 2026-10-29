#!/usr/bin/env python3
"""Structural figure checks only; does not render or visually validate artwork."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "master"
SOURCE = MASTER / "figures" / "source"
expected = set()
for tex in (MASTER / "sections").glob("*.tex"):
    expected.update(re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", tex.read_text(encoding="utf-8")))
errors = []
for name in sorted(expected):
    if not name.lower().endswith(".pdf"):
        errors.append(f"included asset is not an explicit PDF: {name}")
        continue
    pdf = SOURCE / name
    svg = SOURCE / (Path(name).stem + ".svg")
    if not pdf.is_file():
        errors.append(f"missing rendered PDF: {pdf.relative_to(ROOT)}")
    elif pdf.read_bytes()[:5] != b"%PDF-":
        errors.append(f"invalid PDF header: {pdf.relative_to(ROOT)}")
    if not svg.is_file():
        errors.append(f"missing editable SVG source: {svg.relative_to(ROOT)}")
    else:
        try:
            ET.parse(svg)
        except ET.ParseError as exc:
            errors.append(f"malformed SVG {svg.relative_to(ROOT)}: {exc}")

actual_svg = {p.stem for p in SOURCE.glob("*.svg")}
expected_stems = {Path(name).stem for name in expected}
if expected_stems != actual_svg:
    errors.append(f"figure inventory mismatch; included={len(expected_stems)}, source SVGs={len(actual_svg)}")

print(f"Unique included PDF figures: {len(expected_stems)}")
print(f"Editable SVG sources present and parseable: {len(expected_stems) - sum('malformed SVG' in e or 'missing editable SVG' in e for e in errors)}/{len(expected_stems)}")
print(f"Included PDF files present: {len(expected_stems) - sum('missing rendered PDF' in e or 'invalid PDF header' in e for e in errors)}/{len(expected_stems)}")
print("NOTE: this script checks file presence/header/XML only; it does not inspect PDF vectors, typography, captions, or scientific content.")
for error in errors:
    print("ERROR:", error)
sys.exit(bool(errors))
