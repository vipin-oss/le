#!/usr/bin/env python3
"""Fail-fast checks for a completed phase5 pdfLaTeX/BibTeX build log."""
from __future__ import annotations

from pathlib import Path
import re
import sys

log = Path(sys.argv[1] if len(sys.argv) > 1 else "main.log")
if not log.is_file():
    print(f"ERROR: build log missing: {log}")
    sys.exit(2)
text = log.read_text(errors="replace")
checks = {
    "fatal TeX errors": r"(?m)^! ",
    "undefined references/citations": r"(?i)(?:reference|eqref|cref|citation)[^\n]*undefined",
    "missing figure/file errors": r"(?i)(?:file .* not found|not found.*\.pdf|cannot determine size of graphic|no bounding box)",
    "LaTeX unresolved-reference summary": r"(?i)there were undefined (?:references|citations)",
}
failed = False
for name, pattern in checks.items():
    hits = re.findall(pattern, text)
    print(f"{name}: {len(hits)}")
    if hits:
        failed = True
        for hit in hits[:12]:
            print("  ", hit.strip() if isinstance(hit, str) else hit)

# Treat material horizontal or vertical overflow above 1 pt as a proofing failure.
boxes: list[tuple[str, float, int]] = []
for kind, pattern in (
    ("hbox", r"Overfull \\hbox \(([-+0-9.]+)pt too wide\)"),
    ("vbox", r"Overfull \\vbox \(([-+0-9.]+)pt too high\)"),
):
    for match in re.finditer(pattern, text):
        size = float(match.group(1))
        if size > 1.0:
            line = text.count("\n", 0, match.start()) + 1
            boxes.append((kind, size, line))
print(f"overfull hboxes/vboxes > 1 pt: {len(boxes)}")
for kind, size, line in boxes[:100]:
    print(f"  {kind}, log line {line}: {size:.3f} pt")
if boxes:
    failed = True

# Verify that BibTeX actually produced and resolved the manuscript bibliography.
bbl = log.with_suffix(".bbl")
aux = log.with_suffix(".aux")
blg = log.with_suffix(".blg")
if not bbl.is_file():
    print(f"ERROR: bibliography output missing: {bbl}")
    failed = True
else:
    bibitems = len(re.findall(r"\\bibitem\b", bbl.read_text(errors="replace")))
    print(f"bibliography items: {bibitems}")
    if bibitems == 0:
        print("ERROR: bibliography file has no \\bibitem entries")
        failed = True
if not aux.is_file():
    print(f"ERROR: auxiliary file missing: {aux}")
    failed = True
else:
    bibcites = len(re.findall(r"\\bibcite\b", aux.read_text(errors="replace")))
    print(f"resolved bibliography citations in aux: {bibcites}")
    if bibcites == 0:
        print("ERROR: auxiliary file has no \\bibcite entries")
        failed = True
if blg.is_file():
    blg_text = blg.read_text(errors="replace")
    missing = re.findall(r"(?im)^Warning--I didn't find a database entry for ['\"]?([^'\"\n]+)", blg_text)
    print(f"BibTeX missing database entries: {len(missing)}")
    for key in missing[:40]:
        print(f"  {key.strip()}")
    if missing:
        failed = True
else:
    print(f"ERROR: BibTeX log missing: {blg}")
    failed = True

print("BUILD LOG CHECK: FAIL" if failed else "BUILD LOG CHECK: PASS")
sys.exit(1 if failed else 0)
