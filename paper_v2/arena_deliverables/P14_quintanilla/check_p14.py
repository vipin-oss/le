#!/usr/bin/env python3
"""Gate for the P14 deliverable (Quintanilla 2003 and the DPL stability sentence).

Checks
  1  the four files exist and are non-trivial;
  2  evidence.csv has exactly 8 columns in every row (guards the column-shift bug that broke
     check_p13), only known keys, >= 3 rows per key, quotes <= 15 words, eq/theorem and page present;
  3  no key collides with P8_coverage (csv/bib), P10 or P13;
  4  refs_P14.bib has one well-formed entry per evidence key and nothing else;
  5  report.md states the verdict for the s06_lags sentence, the re-judged S5 both ways, the three
     thresholds and their three papers, and one line per secondary source;
  6  hygiene: no .pdf/.zip file names, no links, no .tex files, no long opaque identifiers.

Exit 0 with a single PASS line when everything holds, exit 1 with the failing checks listed.
"""
from __future__ import annotations   # P14 report is plain text, gate is plain python

import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent          # repository root

EVIDENCE = HERE / "evidence.csv"
REPORT = HERE / "report.md"
BIB = HERE / "refs_P14.bib"

EXPECTED_KEYS = {
    "Quintanilla2003JTS",
    "Quintanilla2002JNET",
    "QuintanillaRacke2006IJHMT",
    "FabrizioLazzari2014",
    "ChiritaDApiceZampoli2016",
    "ChiritaCiarlettaTibullo2017",
    "QuintanillaRacke2003DCDS",
}
SECONDARY = [
    "Quintanilla2002JNET",
    "QuintanillaRacke2006IJHMT",
    "FabrizioLazzari2014",
    "ChiritaDApiceZampoli2016",
    "ChiritaCiarlettaTibullo2017",
]
COLUMNS = ["key", "claim", "quote", "eq_theorem", "page", "sentence", "kind", "verbatim"]
SENTENCES = {"S4", "S5", "-"}
KINDS = {"quote", "absence", "na"}
VERBATIM = {"yes", "eq", "na"}

fails: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    if not ok:
        fails.append(f"{name}: {detail}" if detail else name)


# 1 ------------------------------------------------------------------------------------------
for path in (EVIDENCE, REPORT, BIB):
    check(f"file {path.name}", path.is_file(), "missing")
if fails:
    print("FAIL " + " | ".join(fails))
    sys.exit(1)
check("report non-trivial", REPORT.stat().st_size > 4000, f"{REPORT.stat().st_size} bytes")

# 2 ------------------------------------------------------------------------------------------
with EVIDENCE.open(newline="", encoding="utf8") as fh:
    raw = list(csv.reader(fh))
check("evidence has header+rows", len(raw) >= 20, f"{len(raw)} lines")
check("evidence header", raw[0] == COLUMNS, str(raw[0]))
rows = raw[1:]
by_key: dict[str, list[list[str]]] = {}
for i, row in enumerate(rows, start=2):
    if len(row) != len(COLUMNS):
        fails.append(f"evidence line {i}: {len(row)} columns, expected {len(COLUMNS)}")
        continue
    rec = dict(zip(COLUMNS, row))
    key = rec["key"]
    if key not in EXPECTED_KEYS:
        fails.append(f"evidence line {i}: unknown key {key!r}")
    by_key.setdefault(key, []).append(row)
    words = rec["quote"].split()
    if rec["kind"] == "quote" and len(words) > 15:
        fails.append(f"evidence line {i}: quote has {len(words)} words")
    if len(words) < 3 and rec["kind"] == "quote":
        fails.append(f"evidence line {i}: quote too short to be evidence")
    if not rec["eq_theorem"] or rec["eq_theorem"].upper() == "NA":
        fails.append(f"evidence line {i}: no equation/theorem number")
    if not re.fullmatch(r"\d{3,4}", rec["page"]):
        fails.append(f"evidence line {i}: page {rec['page']!r} is not a printed page number")
    if rec["sentence"] not in SENTENCES:
        fails.append(f"evidence line {i}: sentence {rec['sentence']!r}")
    if rec["kind"] not in KINDS:
        fails.append(f"evidence line {i}: kind {rec['kind']!r}")
    if rec["verbatim"] not in VERBATIM:
        fails.append(f"evidence line {i}: verbatim {rec['verbatim']!r}")
    if not rec["claim"]:
        fails.append(f"evidence line {i}: empty claim")
check("keys covered", set(by_key) == EXPECTED_KEYS, f"missing {EXPECTED_KEYS - set(by_key)}")
for key in sorted(EXPECTED_KEYS & set(by_key)):
    check(f"rows for {key}", len(by_key[key]) >= 3, f"only {len(by_key[key])}")

# 3 ------------------------------------------------------------------------------------------
other_keys: set[str] = set()
p8csv = ROOT / "paper_v2/arena_deliverables/P8_coverage/refs_P8.csv"
if p8csv.is_file():
    with p8csv.open(newline="", encoding="utf8") as fh:
        for row in csv.DictReader(fh):
            for field in ("key", "bibkey", "cite_key"):
                if row.get(field):
                    other_keys.add(row[field].strip())
for bib in ("P8_coverage/refs_P8.bib", "P10_verification/refs_P10.bib",
            "P13_books/refs_P13.bib"):
    path = ROOT / "paper_v2/arena_deliverables" / bib
    if path.is_file():
        other_keys |= set(re.findall(r"@\w+\{([^,]+),", path.read_text(encoding="utf8")))
clash = EXPECTED_KEYS & other_keys
check("no key clash", not clash, f"collides with {sorted(clash)}")

# 4 ------------------------------------------------------------------------------------------
bib_text = BIB.read_text(encoding="utf8")
bib_entries = re.findall(r"@(\w+)\{([^,]+),(.*?)\n\}", bib_text, re.S)
bib_keys = [e[1].strip() for e in bib_entries]
check("bib keys", set(bib_keys) == EXPECTED_KEYS,
      f"extra {set(bib_keys) - EXPECTED_KEYS}, missing {EXPECTED_KEYS - set(bib_keys)}")
check("bib no duplicate keys", len(bib_keys) == len(set(bib_keys)))
check("bib brace balance", bib_text.count("{") == bib_text.count("}"),
      f"{bib_text.count('{')} vs {bib_text.count('}')}")
for kind, key, body in bib_entries:
    for field in ("author", "title", "journal", "year", "pages"):
        check(f"bib {key}.{field}", re.search(rf"{field}\s*=", body) is not None, "field missing")

# 5 ------------------------------------------------------------------------------------------
report = REPORT.read_text(encoding="utf8")
must_have = {
    "s06_lags verdict": r"\*\*Verdict \(s06_lags sentence\): SUPPORTED",
    "S5 unqualified verdict": r"\*\*NOT SUPPORTED\*\*",
    "S5 qualified verdict": r"\*\*SUPPORTED\*\*",
    "condition": r"τ_T > τ_q/2",
    "half threshold": r"τ_q/2|½",
    "third threshold": r"2 − √3|2 − sqrt\(3\)",
    "character threshold": r"τ_T = τ_q",
    "Theorem 1": r"Theorem 1",
    "Hurwitz": r"Hurwitz",
    "file-identity correction": r"not Quintanilla|is not",
    "printed page 716": r"716",
    "printed page 718": r"718",
    "printed page 720": r"720",
    "printed page 717": r"717",
    "missing-list statement": r"missing",
    "gates statement": r"check_p14",
}
for label, pattern in must_have.items():
    check(f"report: {label}", re.search(pattern, report) is not None, f"pattern {pattern!r}")
for key in SECONDARY:
    check(f"report: one-line verdict for {key}", key in report, "key not mentioned")
check("report: ≤15-word rule stated", "15 words" in report)

# 6 ------------------------------------------------------------------------------------------
def hygiene(name: str, text: str) -> None:
    stripped = text.replace("`.tex`", "TEXTFILE")
    for pattern, label in (
        (r"[\w/\\-]+\.pdf\b", "pdf file name"),
        (r"[\w/\\-]+\.zip\b", "zip file name"),
        (r"[\w/\\-]+\.tex\b", "tex file name"),
        (r"https?://", "link"),
        (r"\bwww\.", "link"),
        (r"drive\.google|docs\.google|/gdrive/|/My Drive/", "drive reference"),
        (r"[A-Za-z0-9_\-]{33,}", "long opaque identifier"),
        (r"\\documentclass|\\begin\{|\\end\{", "latex source"),
    ):
        hit = re.search(pattern, stripped)
        check(f"hygiene {name}: {label}", hit is None,
              f"found {hit.group(0)[:60] if hit else ''}")

hygiene("report.md", report)
hygiene("evidence.csv", EVIDENCE.read_text(encoding="utf8"))
hygiene("refs_P14.bib", bib_text)

files = sorted(p.name for p in HERE.iterdir() if p.is_file())
check("folder contents", set(files) == {"report.md", "evidence.csv", "refs_P14.bib", "check_p14.py"},
      f"unexpected {files}")

if fails:
    print(f"FAIL {len(fails)} check(s)")
    for f in fails:
        print("  -", f)
    sys.exit(1)

print(f"PASS P14: evidence rows={len(rows)} keys={len(by_key)} quotes/all<=15 words "
      f"secondary verdicts={len(SECONDARY)} bib entries={len(bib_entries)} "
      f"no key clash ({len(other_keys)} other keys), no pdf/zip/tex/links in this folder")
sys.exit(0)
