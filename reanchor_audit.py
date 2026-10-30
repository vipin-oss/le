#!/usr/bin/env python3
"""Re-anchor EQUATION_AUDIT.csv 'line' column to current source locations.

Scans each audited .tex file for \\begin{equation}...\\end{equation} blocks,
takes the \\label{eq:X} inside each, records the line of \\begin{equation},
and rewrites EQUATION_AUDIT.csv 'line' values accordingly. Only the 'line'
column is touched; all other fields are preserved verbatim.
"""
import csv, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "phase5/reports/EQUATION_AUDIT.csv"

SECTION_FILES = {
    "3": "phase5/master/sections/sec03_foundations.tex",
    "4": "phase5/master/sections/sec04_thermoelastic.tex",
    "5": "phase5/master/sections/sec05_multiphysics.tex",
    "6": "phase5/master/sections/sec06_transport.tex",
    "7": "phase5/master/sections/sec07_nonlocal.tex",
    "8": "phase5/master/sections/sec08_mathematical_methods.tex",
    "9": "phase5/master/sections/sec09_interfaces.tex",
    "10": "phase5/master/sections/sec10_energy.tex",
    "11": "phase5/master/sections/sec11_advanced.tex",
    "14": "phase5/master/sections/sec14_taxonomy.tex",
    "B": "phase5/master/appendices/appB_balance_derivations.tex",
}

ENV = re.compile(r"\\begin\{(equation\*?)\}(.*?)\\end\{\1\}", re.S)
LABEL = re.compile(r"\\label\{eq:([^}]+)\}")


def strip_comments(text):
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


def build_index(text):
    """label -> line of \\begin{equation} for labeled displays."""
    idx = {}
    for match in ENV.finditer(text):
        line = text.count("\n", 0, match.start()) + 1
        lm = LABEL.search(match.group(2))
        if lm:
            idx[lm.group(1)] = line
    return idx


indices = {}
for section, rel in SECTION_FILES.items():
    p = ROOT / rel
    if p.exists():
        indices[section] = build_index(strip_comments(p.read_text(encoding="utf-8")))
    else:
        indices[section] = {}

rows = list(csv.DictReader(REPORT.open(newline="", encoding="utf-8")))
fieldnames = rows[0].keys()
changed = 0
not_found = []
for row in rows:
    sec = row["section"]
    label = row["label"]
    m = re.match(r"eq:(.+)", label)
    key = m.group(1) if m else label
    new_line = indices.get(sec, {}).get(key)
    old_line = int(row["line"])
    if new_line is None:
        not_found.append((sec, rel if False else row["source_file"], label, old_line))
        continue
    if new_line != old_line:
        row["line"] = str(new_line)
        changed += 1

with REPORT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)

print("updated lines:", changed)
print("labels not found in source (check these):")
for t in not_found:
    print("  ", t)
