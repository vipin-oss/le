#!/usr/bin/env python3
"""Verify active citation-key coverage and bounded B22 Crossref dispositions.

This is a bibliography/record-integrity check, not claim-level source verification.
Uncited working-bibliography entries are reported but are not automatically removed.
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MASTER = ROOT / "phase5/master"
MAIN = MASTER / "main.tex"
BIB = MASTER / "references_local.bib"
FINAL_CSV = ROOT / "phase5/reports/CROSSREF_FINAL.csv"
FINAL_NOTES = ROOT / "phase5/reports/CROSSREF_FINAL_NOTES.md"
CROSSREF_DIR = ROOT / "phase5/reports/crossref_final"


def uncomment(text: str) -> str:
    """Remove TeX comments, preserving escaped percent signs."""
    output: list[str] = []
    for line in text.splitlines():
        kept: list[str] = []
        i = 0
        while i < len(line):
            if line[i] == "%":
                backslashes = 0
                j = i - 1
                while j >= 0 and line[j] == "\\":
                    backslashes += 1
                    j -= 1
                if backslashes % 2 == 0:
                    break
            kept.append(line[i])
            i += 1
        output.append("".join(kept))
    return "\n".join(output)


def active_tex_files(path: Path, seen: set[Path] | None = None) -> list[Path]:
    seen = seen or set()
    path = path.resolve()
    if path in seen:
        return []
    if not path.is_file():
        raise AssertionError(f"missing active TeX input: {path}")
    seen.add(path)
    text = uncomment(path.read_text(encoding="utf-8"))
    result = [path]
    for match in re.finditer(r"\\(?:input|include)\s*\{([^}]+)\}", text):
        name = match.group(1).strip()
        child = (MASTER / name) if not name.startswith("/") else Path(name)
        if child.suffix != ".tex":
            child = child.with_suffix(".tex")
        result.extend(active_tex_files(child, seen))
    return result


def bib_keys(text: str) -> list[str]:
    return re.findall(r"@(?!string\b|preamble\b|comment\b)\w+\s*\{\s*([^,\s]+)\s*,", text, re.I)


def bib_entry(text: str, key: str) -> str:
    match = re.search(rf"@\w+\s*\{{\s*{re.escape(key)}\s*,", text, re.I)
    if not match:
        raise AssertionError(f"bibliography entry missing: {key}")
    start = match.start()
    depth = 0
    in_quote = False
    escaped = False
    opened = False
    for i in range(match.start(), len(text)):
        char = text[i]
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"':
            in_quote = not in_quote
        if in_quote:
            continue
        if char == "{":
            opened = True
            depth += 1
        elif char == "}" and opened:
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    raise AssertionError(f"unterminated bibliography entry: {key}")


def field(entry: str, name: str) -> str | None:
    match = re.search(rf"^\s*{re.escape(name)}\s*=\s*\{{(.*?)\}}\s*,?\s*$", entry, re.I | re.M)
    if match:
        return match.group(1).strip()
    match = re.search(rf"^\s*{re.escape(name)}\s*=\s*([^,\n]+)", entry, re.I | re.M)
    return match.group(1).strip().strip("{}") if match else None


bib_text = BIB.read_text(encoding="utf-8")
keys_list = bib_keys(bib_text)
key_counts = Counter(keys_list)
duplicates = sorted(key for key, count in key_counts.items() if count > 1)
assert not duplicates, f"duplicate bibliography keys: {duplicates}"
keys = set(keys_list)

files = active_tex_files(MAIN)
used: set[str] = set()
for path in files:
    text = uncomment(path.read_text(encoding="utf-8"))
    for match in re.finditer(
        r"\\(?:cite[a-zA-Z]*|[a-zA-Z]*cite[a-zA-Z]*)"
        r"(?:\[[^\]]*\]){0,2}\s*\{([^}]*)\}",
        text,
    ):
        used.update(key.strip() for key in match.group(1).split(",") if key.strip() and key.strip() != "*")
missing = sorted(used - keys)
assert not missing, f"active citation keys have no bibliography entry: {missing}"
uncited = sorted(keys - used)

with FINAL_CSV.open(newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
assert len(rows) == 14, f"expected 14 itemized Crossref/source-page comparisons, found {len(rows)}"
by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
for row in rows:
    by_key[row["bib_key"]].append(row)
assert {key: len(value) for key, value in by_key.items()} == {
    "Quintanilla2003DPL": 8,
    "DellOroPata2016Viscoelasticity": 6,
}

quint_doi = next(row for row in by_key["Quintanilla2003DPL"] if row["field"] == "doi")
assert quint_doi["comparison"] == "CONFLICT-UNRESOLVED"
assert quint_doi["status"] == "VERIFIED-NO"
assert "10.1080/01495730390203518" in quint_doi["source_page_assertion"]
assert "10.1080/713855996" in quint_doi["source_page_assertion"]
response_match = json.loads((CROSSREF_DIR / "10.1080_713855996.json").read_text(encoding="utf-8"))
response_404 = json.loads((CROSSREF_DIR / "10.1080_01495730390203518.json").read_text(encoding="utf-8"))
assert response_match["message"]["DOI"].lower() == "10.1080/713855996"
assert response_404["http_status"] == 404
notes = FINAL_NOTES.read_text(encoding="utf-8")
normalized_notes = " ".join(notes.split())
assert "Both source-page reports are preserved" in normalized_notes
assert "conflict is unresolved" in normalized_notes
quint_entry = bib_entry(bib_text, "Quintanilla2003DPL")
assert field(quint_entry, "doi") == "10.1080/713855996"
assert field(quint_entry, "verified") == "NO"

pata_rows = by_key["DellOroPata2016Viscoelasticity"]
assert sum(row["status"] == "NOT-INDEPENDENTLY-RECHECKED" for row in pata_rows) == 3
assert sum(row["status"] == "B22-SPOTCHECK-ONLY; RAW RESPONSE UNAVAILABLE" for row in pata_rows) == 2
pata_entry = bib_entry(bib_text, "DellOroPata2016Viscoelasticity")
assert field(pata_entry, "volume") == "76"
assert field(pata_entry, "pages") == "641--655"
assert field(pata_entry, "verified") == "NO"

print(f"PASS: {len(used)} active cited keys resolve to {len(keys)} unique bibliography entries across {len(files)} TeX inputs")
print(f"INFO: {len(uncited)} uncited working-bibliography entries retained for disposition; none removed")
print("PASS: 14 Crossref/source-page comparisons cover the two required entries")
print("PASS: Quintanilla DOI conflict remains explicit and verified=NO; Dell'Oro–Pata raw-response limits remain explicit and verified=NO")
