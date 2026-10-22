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
check_counts: dict[str, int] = {}
layout_warning_checks = {
    "duplicate page.1 destinations": r"(?i)destination with the same identifier \(name\{page\.1\}\) has been already used",
    "PDF-string token warnings": r"Token not allowed in a PDF string",
    "h-float specifier warnings": r"`h' float specifier changed to `ht'",
    "underfull hboxes": r"Underfull \\hbox",
    "underfull vboxes": r"Underfull \\vbox",
}
for name, pattern in checks.items():
    hits = re.findall(pattern, text)
    check_counts[name] = len(hits)
    print(f"{name}: {len(hits)}")
    if hits:
        failed = True
        for hit in hits[:12]:
            print("  ", hit.strip() if isinstance(hit, str) else hit)

print("nonfatal layout warning inventory:")
for name, pattern in layout_warning_checks.items():
    print(f"  {name}: {len(re.findall(pattern, text))}")

# Treat material horizontal or vertical overflow above 1 pt as a proofing failure.
boxes: list[tuple[str, float, int, str, str, str]] = []
log_lines = text.splitlines()
for kind, pattern in (
    ("hbox", r"Overfull \\hbox \(([-+0-9.]+)pt too wide\)"),
    ("vbox", r"Overfull \\vbox \(([-+0-9.]+)pt too high\)"),
):
    for match in re.finditer(pattern, text):
        size = float(match.group(1))
        if size > 1.0:
            line = text.count("\n", 0, match.start()) + 1
            index = line - 1
            nearby = log_lines[max(0, index - 500):index + 3]
            source = "unknown source"
            for nearby_line in reversed(nearby):
                source_match = re.search(r"(?:\./|/)[^()\s]+\.tex", nearby_line)
                if source_match:
                    source = source_match.group(0)
                    break
            warning = log_lines[index]
            nearby_text = "\n".join(log_lines[max(0, index - 3):min(len(log_lines), index + 12)])
            source_lines = re.search(r"at lines ([0-9]+--[0-9]+)", nearby_text)
            source_range = source_lines.group(1) if source_lines else "?"
            context = " / ".join(
                item.strip() for item in log_lines[max(0, index - 2):min(len(log_lines), index + 10)] if item.strip()
            )
            boxes.append((kind, size, line, source, source_range, context[:220]))
print(f"overfull hboxes/vboxes > 1 pt: {len(boxes)}")
by_source: dict[str, list[tuple[str, float, int, str, str, str]]] = {}
for box in boxes:
    by_source.setdefault(Path(box[3]).name, []).append(box)
source_details = []
for source, entries in sorted(by_source.items(), key=lambda item: (-len(item[1]), item[0]))[:30]:
    worst = max(entries, key=lambda entry: entry[1])
    source_details.append(
        f"{source}={len(entries)} (max {worst[1]:.1f}pt at {worst[4]}; {worst[5][:100]})"
    )
if source_details:
    print("overfull by source: " + " | ".join(source_details))
if len(boxes) <= 50:
    details = [
        f"{Path(source).name}:{source_range} +{size:.1f}pt {excerpt[:220]}"
        for _kind, size, _line, source, source_range, excerpt in boxes
    ]
    print("all overfull details: " + " | ".join(details))
worst_overall = sorted(boxes, key=lambda entry: entry[1], reverse=True)[:8]
if worst_overall:
    print("largest overfull boxes: " + " | ".join(
        f"{Path(source).name}:{source_range} +{size:.1f}pt {excerpt[:220]}"
        for _kind, size, _line, source, source_range, excerpt in worst_overall
    ))
if boxes:
    failed = True

# Verify that BibTeX actually produced and resolved the manuscript bibliography.
bibitems = 0
bibcites = 0
missing: list[str] = []
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

print("gate summary: " + "; ".join(f"{name}={count}" for name, count in check_counts.items()) + f"; overfull_boxes={len(boxes)}; bibitems={bibitems}; bibcites={bibcites}; missing_bib_keys={len(missing)}")
print("BUILD LOG CHECK: FAIL" if failed else "BUILD LOG CHECK: PASS")
sys.exit(1 if failed else 0)
