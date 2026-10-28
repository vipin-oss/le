#!/usr/bin/env python3
"""Check the split between two distinct 2017 Kumar bibliography records."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BIB = ROOT / "phase5/master/references_local.bib"
CROSSREF = ROOT / "phase5/reports/crossref_raw_r3b/10.12921_cmst.2016.0000036.json"
LEDGER = ROOT / "phase5/reports/OPEN_CLAIMS_LEDGER.csv"
ACTIVE_TEX = [
    ROOT / "phase5/master/sections/sec09_interfaces.tex",
    ROOT / "phase5/master/sections/sec10_energy.tex",
]


def entry_for(text: str, key: str) -> str:
    match = re.search(
        rf"@\w+\{{{re.escape(key)},(.*?)(?=\n@\w+\{{|\Z)", text, re.DOTALL
    )
    if not match:
        raise AssertionError(f"missing bibliography entry {key}")
    return match.group(1)


def field(entry: str, name: str) -> str | None:
    match = re.search(rf"^\s*{re.escape(name)}\s*=\s*\{{(.*?)\}}\s*,?\s*$", entry, re.M)
    return match.group(1) if match else None


bib = BIB.read_text(encoding="utf-8")
kumar = entry_for(bib, "Kumar2017")
kansal = entry_for(bib, "KumarKansal2017")

assert field(kumar, "title") == (
    "Damping in Microscale Modified Couple Stress Thermoelastic Circular Kirchhoff Plate Resonators"
)
assert field(kumar, "author") == "Kumar, Rajneesh and Devi, Shaloo and Sharma, Veena"
assert field(kumar, "doi") is None, "unverified DOI must not be assigned to Kumar2017"
assert field(kumar, "verified") == "NO"

crossref = json.loads(CROSSREF.read_text(encoding="utf-8"))
message = crossref["message"]
assert crossref["http_status"] == 200
assert message["DOI"].lower() == "10.12921/cmst.2016.0000036"
assert message["title"][0] == field(kansal, "title")
assert [(a["given"], a["family"]) for a in message["author"]] == [
    ("Rajneesh", "Kumar"),
    ("Tarun", "Kansal"),
]
assert field(kansal, "doi") == "10.12921/cmst.2016.0000036"
assert field(kansal, "verified") == "YES"

active = "\n".join(path.read_text(encoding="utf-8") for path in ACTIVE_TEX)
assert r"\cite{KumarKansal2017}" in active
assert r"\cite{Kumar2017}" not in active

with LEDGER.open(newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
dependent_ids = {
    "OCL-076", "OCL-278", "OCL-279", "OCL-285", "OCL-288",
    "OCL-292", "OCL-293", "OCL-294",
}
dependent = [row for row in rows if row["ledger_row_id"] in dependent_ids]
assert len(dependent) == len(dependent_ids), "expected all eight directly linked ledger rows"
assert all(row["class"] in {"B", "C"} for row in dependent), (
    "bibliographic verification must not promote the directly linked technical claims"
)
# OCL-286, -287, and -291 are separate, page-read source claims in the same
# numerical interval, not Kumar-dependent rows; retain their existing Class A.
unrelated_source_rows = [row for row in rows if row["ledger_row_id"] in {"OCL-286", "OCL-287", "OCL-291"}]
assert len(unrelated_source_rows) == 3
assert all(row["class"] == "A" for row in unrelated_source_rows)
assert all(
    "KumarKansal2017" not in " ".join(row.values())
    and "Kumar & Kansal (2017)" not in " ".join(row.values())
    for row in unrelated_source_rows
)

print(
    "Kumar reference split verified: Crossref DOI belongs to Kumar & Kansal; "
    "the library Kumar/Devi/Sharma record remains unverified; eight directly linked claims stay B/C; "
    "three separate page-read claims remain A."
)
