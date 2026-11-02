#!/usr/bin/env python3
"""Gate for the P16 deliverable (ASME compliance support).

1  the six files exist and are non-trivial;
2  firstperson_fixes.csv: 77 rows, every row is a real sentence with a pronoun, the replacement has
   none, and the numbers / citation keys / cross-reference targets are unchanged;
3  dois_found.csv: exactly the 31 requested keys, match in {yes,no}, a DOI exactly when match is yes;
4  journal_abbrev.csv: 155 journals, four ASME-sourced rows and they are the four ASME titles;
5  style_check.csv: 439 entries, 15 typed given-name-first, one without an author, none with the year
   field before the title field;
6  report.md states the findings and the ASME source;
7  hygiene: no binary artefacts, no LaTeX source, no library location in this folder.
"""
from __future__ import annotations

import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
fails: list[str] = []


def check(name, ok, detail=""):
    if not ok:
        fails.append(f"{name}: {detail}" if detail else name)


FP = HERE / "firstperson_fixes.csv"
DO = HERE / "dois_found.csv"
JA = HERE / "journal_abbrev.csv"
SC = HERE / "style_check.csv"
RP = HERE / "report.md"

for p in (FP, DO, JA, SC, RP):
    check(f"file {p.name}", p.is_file(), "missing")
if fails:
    print("FAIL " + " | ".join(fails))
    sys.exit(1)
check("report size", RP.stat().st_size > 8000, f"{RP.stat().st_size} B")

# ---------------------------------------------------------------- 1. first person
rows = list(csv.DictReader(FP.open(encoding="utf8")))
check("fp header", list(rows[0].keys()) == ["file", "line", "original", "replacement", "pronoun"],
      str(list(rows[0].keys())))
check("fp rows", len(rows) == 77, f"{len(rows)}")

FIRST = re.compile(r"(?<![\w\\])(we|We|our|Our|us|Us|I|my|My)(?![\w])")
NUM = re.compile(r"\d+(?:\.\d+)?")
CITE = re.compile(r"\\[cC]ite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}")
REF = re.compile(r"\\[cC]?[rR]ef\{([^}]*)\}|\\eqref\{([^}]*)\}")

for i, r in enumerate(rows, start=2):
    if not re.match(r"^(main\.tex|sections/[A-Za-z0-9_.\-]+\.tex)$", r["file"]):
        fails.append(f"fp line {i}: bad file path {r['file']!r}")
    if not r["line"].isdigit():
        fails.append(f"fp line {i}: line {r['line']!r}")
    if not FIRST.search(r["original"]):
        fails.append(f"fp line {i}: original has no first-person pronoun")
    if FIRST.search(r["replacement"]):
        fails.append(f"fp line {i}: replacement still has {FIRST.search(r['replacement']).group(0)!r}")
    if sorted(NUM.findall(r["original"])) != sorted(NUM.findall(r["replacement"])):
        fails.append(f"fp line {i}: numbers changed")
    if sorted(CITE.findall(r["original"])) != sorted(CITE.findall(r["replacement"])):
        fails.append(f"fp line {i}: citation keys changed")
    o_ref = sorted(m for t in REF.findall(r["original"]) for m in t)
    n_ref = sorted(m for t in REF.findall(r["replacement"]) for m in t)
    if o_ref != n_ref:
        fails.append(f"fp line {i}: ref targets changed")
    if len(r["replacement"]) < 0.6 * len(r["original"]):
        fails.append(f"fp line {i}: replacement much shorter than the original")

files = {r["file"] for r in rows}
check("fp distinct files", len(files) == 38, f"{len(files)}")
check("fp main.tex covered", "main.tex" in files)

# ---------------------------------------------------------------- 2. DOIs
REQ = """Achenbach1973 Ackerman1966 Auld1973 Boley1960 BornKarman1912 Carlson1972 Cattaneo1948
Chadwick1960 Chester1963 Cohen2007 Danilovskaya1950 Duhamel1837 Eringen2002 Gulyaev1969
IgnaczakOstoja2010 Jackson1970 Jou2010 Kaminski1990 Kumar2017 Laude2015 Love1911 Mitra1995
Nowacki1975 Pennes1948 Podlubny1999 Rayleigh1885 Scholte1947 Scruby1990 Tzou1997 Tzou2015
Vernotte1958""".split()
drows = list(csv.DictReader(DO.open(encoding="utf8")))
check("doi header", list(drows[0].keys()) == ["key", "doi", "evidence", "match"], str(list(drows[0].keys())))
check("doi rows", len(drows) == len(REQ) == 31, f"{len(drows)} vs {len(REQ)}")
check("doi keys", {r["key"] for r in drows} == set(REQ), "key set differs")
yes = no = 0
for r in drows:
    if r["match"] not in ("yes", "no"):
        fails.append(f"doi {r['key']}: match={r['match']!r}")
        continue
    if r["match"] == "yes":
        yes += 1
        if not re.match(r"^10\.\d{4,9}/\S+$", r["doi"]):
            fails.append(f"doi {r['key']}: malformed DOI {r['doi']!r}")
        if "Crossref" not in r["evidence"]:
            fails.append(f"doi {r['key']}: no Crossref evidence")
    else:
        no += 1
        if r["doi"].strip():
            fails.append(f"doi {r['key']}: match=no but a DOI is given")
        if "NO DOI EXISTS" not in r["evidence"]:
            fails.append(f"doi {r['key']}: match=no without an explicit reason")
    if len(r["evidence"]) < 40:
        fails.append(f"doi {r['key']}: evidence too short")
check("doi split", (yes, no) == (18, 13), f"yes={yes} no={no}")

# ---------------------------------------------------------------- 3. abbreviations
jrows = list(csv.DictReader(JA.open(encoding="utf8")))
check("ja header", list(jrows[0].keys()) == ["full_name", "abbreviation", "source"], str(list(jrows[0].keys())))
check("ja rows", len(jrows) == 155, f"{len(jrows)}")
check("ja unique", len({r["full_name"] for r in jrows}) == 155, "duplicate full names")
asme = [r for r in jrows if r["source"].startswith("ASME")]
iso = [r for r in jrows if r["source"].startswith("ISO 4")]
check("ja source values", len(asme) + len(iso) == 155, f"other source values present")
check("ja asme count", len(asme) == 4, f"{len(asme)}")
check("ja asme titles",
      {r["full_name"] for r in asme} == {"Applied Mechanics Reviews", "Journal of Applied Mechanics",
                                         "Journal of Heat Transfer", "Journal of Biomechanical Engineering"},
      str(sorted(r["full_name"] for r in asme)))
for r in jrows:
    if not r["full_name"].strip() or not r["abbreviation"].strip():
        fails.append(f"ja empty row: {r}")
    if len(r["abbreviation"]) > len(r["full_name"]):
        fails.append(f"ja {r['full_name']}: abbreviation longer than the name")

# ---------------------------------------------------------------- 4. style check
srows = list(csv.DictReader(SC.open(encoding="utf8")))
check("sc header", list(srows[0].keys()) == ["key", "bib_file", "type", "first_author_as_in_bib",
                                             "name_form_in_bib", "year_field_before_title_field", "note"],
      str(list(srows[0].keys())))
check("sc rows", len(srows) == 439, f"{len(srows)}")
check("sc initials-first", sum(1 for r in srows if r["name_form_in_bib"] == "initials/given-first") == 15,
      str(sum(1 for r in srows if r["name_form_in_bib"] == "initials/given-first")))
check("sc no author", sum(1 for r in srows if r["name_form_in_bib"] == "no author field") == 1,
      str(sum(1 for r in srows if r["name_form_in_bib"] == "no author field")))
check("sc year-before-title", sum(1 for r in srows if r["year_field_before_title_field"] == "yes") == 0,
      str(sum(1 for r in srows if r["year_field_before_title_field"] == "yes")))
check("sc bib files", len({r["bib_file"] for r in srows}) >= 5, str(sorted({r['bib_file'] for r in srows})))

# ---------------------------------------------------------------- 5. report
txt = RP.read_text(encoding="utf8")
for label, pat in {
    "77 rewrites": r"\b77\b", "38 files": r"\b38\b", "155 journals": r"\b155\b",
    "18 with doi": r"\b18\b", "13 without": r"\b13\b", "31 keys": r"\b31\b",
    "asme page cited": r"asme\.org/publications-submissions/journals",
    "asme bst": r"asme2e", "initials first": r"initials first",
    "year position": r"year.*(last|after the authors)|after the authors.*year",
    "false positives": r"false positive", "editorial note on Scruby": r"[Rr]eissue",
    "NOT READ style limits": r"[Ll]imits",
}.items():
    check(f"report: {label}", re.search(pat, txt, re.S) is not None, "not found")

# ---------------------------------------------------------------- 6. hygiene
binaries = [p.name for p in HERE.iterdir() if p.is_file() and p.suffix.lower() in
            {".pdf", ".zip", ".png", ".jpg", ".jpeg", ".tex", ".bib", ".bbl", ".docx"}]
check("no binaries or manuscript files", not binaries, f"{binaries}")
check("folder contents",
      {p.name for p in HERE.iterdir() if p.is_file()} ==
      {"firstperson_fixes.csv", "dois_found.csv", "journal_abbrev.csv", "style_check.csv",
       "report.md", "check_p16.py"},
      str(sorted(p.name for p in HERE.iterdir() if p.is_file())))
for name in (FP, DO, JA, SC, RP):
    body = name.read_text(encoding="utf8")
    for pat, label in ((r"drive\.google|docs\.google|/gdrive/|/My Drive/", "drive reference"),
                       (r"\b[0-9a-f]{32}\b", "32-hex identifier")):
        hit = re.search(pat, body)
        check(f"hygiene {name.name}: {label}", hit is None, hit.group(0) if hit else "")

if fails:
    print(f"FAIL {len(fails)} check(s)")
    for f in fails:
        print("  -", f)
    sys.exit(1)

print(f"PASS P16: {len(rows)} first-person rewrites over {len(files)} files with numbers, citations and "
      f"cross-references preserved; {len(drows)} DOI lookups ({yes} found, {no} none); "
      f"{len(jrows)} journal names ({len(asme)} ASME, {len(iso)} ISO 4); {len(srows)} bib entries "
      f"style-checked (15 given-name-first, 1 authorless); no manuscript file in this folder")
sys.exit(0)
