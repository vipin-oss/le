#!/usr/bin/env python3
"""Emit a concise list of unique TeX overfull boxes above 0.5 pt."""
from __future__ import annotations

from pathlib import Path
import re
import sys

log = Path(sys.argv[1] if len(sys.argv) > 1 else "phase5/master/build/main.log")
if not log.is_file():
    raise SystemExit(f"ERROR: build log missing: {log}")
text = log.read_text(errors="replace")
lines = text.splitlines()
pattern = re.compile(r"Overfull \\\\([hv])box \(([-+0-9.]+)pt too (?:wide|high)\)")
found: list[str] = []
seen: set[tuple[str, str, float]] = set()
for match in pattern.finditer(text):
    size = float(match.group(2))
    if size <= 0.5:
        continue
    index = text.count("\n", 0, match.start())
    context = "\n".join(lines[index:min(len(lines), index + 12)])
    source_range_match = re.search(r"at lines ([0-9]+--[0-9]+)", context)
    source_range = source_range_match.group(1) if source_range_match else "line ?"
    candidates = re.findall(r"(?:\./|/)[^()\s]+\.tex", "\n".join(lines[max(0, index - 1000):index + 1]))
    source = "unknown source"
    line_end = int(source_range.split("--")[-1]) if "--" in source_range else None
    for candidate in reversed(candidates):
        path = Path(candidate)
        if line_end is not None and path.is_file():
            if line_end > len(path.read_text(errors="replace").splitlines()):
                continue
        source = path.name
        break
    kind = match.group(1) + "box"
    key = (source, source_range, round(size, 2))
    if key in seen:
        continue
    seen.add(key)
    found.append(f"{source}:{source_range} +{size:.2f}pt {kind}")
print("; ".join(found) if found else "none")
