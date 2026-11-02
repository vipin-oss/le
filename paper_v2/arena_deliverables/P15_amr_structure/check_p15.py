#!/usr/bin/env python3
"""Gate for the P15 deliverable (AMR structure study).

Checks
  1  the four files exist and are non-trivial;
  2  amr_papers.csv has exactly 28 columns in the header and in every row (the column-shift bug that
     broke check_p13 would fail here), 3 AMR articles, known keys, numeric fields parse, no empty cells;
  3  the article facts are the ones measured: page counts, reference counts, figure/table/equation
     counts, section counts and the two citation styles;
  4  report.md covers the three articles, the missing-source list, our 173-page baseline and the
     reference-style findings;
  5  restructure_plan.md maps every old body section 1-39 and every old appendix A-J exactly once, and
     proposes 10 numbered sections and 12 appendices;
  6  hygiene: nothing binary in this folder, no library location, no link, no .zip, no long opaque id.

Exit 0 with one PASS line, or 1 with the failing checks listed.
"""
from __future__ import annotations

import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent

CSV = HERE / "amr_papers.csv"
REPORT = HERE / "report.md"
PLAN = HERE / "restructure_plan.md"

COLUMNS = ["key", "title", "journal", "volume_issue_year", "article_or_pages",
           "doi_printed_on_pdf", "pages_in_pdf", "references", "figures", "tables",
           "equations", "eq_numbering", "abstract_words", "keywords", "n_top_sections",
           "section_titles_in_order", "subsections_of_two_sections", "nomenclature",
           "appendix", "acknowledgment", "conclusions_or_outlook_title", "citation_in_text",
           "reference_list_order", "reference_list_format", "historical_section_first",
           "summary_table_or_box", "figure_style", "figure_caption_style"]

EXPECTED = {
    # key: (pages, figures, tables, equations, n_sections)
    "Chandrasekharaiah1986": (22, 0, 2, 142, 6),
    "Chandrasekharaiah1998": (25, 0, 0, 141, 8),
    "Hussein2014": (38, 43, 0, 86, 6),
}

fails: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    if not ok:
        fails.append(f"{name}: {detail}" if detail else name)


# 1 ------------------------------------------------------------------------------------------
for path in (CSV, REPORT, PLAN):
    check(f"file {path.name}", path.is_file(), "missing")
if fails:
    print("FAIL " + " | ".join(fails))
    sys.exit(1)
check("report non-trivial", REPORT.stat().st_size > 6000, f"{REPORT.stat().st_size} bytes")
check("plan non-trivial", PLAN.stat().st_size > 6000, f"{PLAN.stat().st_size} bytes")

# 2 ------------------------------------------------------------------------------------------
with CSV.open(newline="", encoding="utf8") as fh:
    raw = list(csv.reader(fh))
check("csv header", raw[0] == COLUMNS, f"{len(raw[0])} columns")
rows = raw[1:]
check("csv row count", len(rows) == 3, f"{len(rows)} rows")
by_key: dict[str, dict[str, str]] = {}
for i, row in enumerate(rows, start=2):
    if len(row) != len(COLUMNS):
        fails.append(f"csv line {i}: {len(row)} columns, expected {len(COLUMNS)}")
        continue
    rec = dict(zip(COLUMNS, row))
    key = rec["key"]
    if key not in EXPECTED:
        fails.append(f"csv line {i}: unknown key {key!r}")
        continue
    by_key[key] = rec
    for field, value in rec.items():
        if not value.strip():
            fails.append(f"csv {key}.{field}: empty")
check("csv keys", set(by_key) == set(EXPECTED), f"missing {set(EXPECTED) - set(by_key)}")

for key, (pages, figs, tabs, eqs, secs) in EXPECTED.items():
    rec = by_key.get(key, {})
    if not rec:
        continue
    check(f"{key} pages", rec["pages_in_pdf"] == str(pages), rec["pages_in_pdf"])
    check(f"{key} figures", rec["figures"] == str(figs), rec["figures"])
    check(f"{key} tables", rec["tables"].startswith(str(tabs)), rec["tables"])
    check(f"{key} equations", rec["equations"] == str(eqs), rec["equations"])
    check(f"{key} sections", rec["n_top_sections"] == str(secs), rec["n_top_sections"])
    check(f"{key} equation numbering stated",
          ("per section" in rec["eq_numbering"]) or ("sequential" in rec["eq_numbering"]),
          rec["eq_numbering"])
    check(f"{key} references stated", re.search(r"\d", rec["references"]) is not None,
          rec["references"])
    check(f"{key} abstract words", rec["abstract_words"].isdigit(), rec["abstract_words"])

check("1986/1998 are author-year",
      "author-year" in by_key.get("Chandrasekharaiah1986", {}).get("citation_in_text", "")
      and "author-year" in by_key.get("Chandrasekharaiah1998", {}).get("citation_in_text", ""))
check("2014 is numeric", "numeric" in by_key.get("Hussein2014", {}).get("citation_in_text", ""))
check("2014 reference order", "order of appearance" in by_key.get("Hussein2014", {}).get("reference_list_order", ""))
check("1998 reference order", "alphabetical" in by_key.get("Chandrasekharaiah1998", {}).get("reference_list_order", ""))

# 3 ------------------------------------------------------------------------------------------
report = REPORT.read_text(encoding="utf8")
must = {
    "article 1986": r"Chandrasekharaiah 1986",
    "article 1998": r"Chandrasekharaiah 1998",
    "article 2014": r"Hussein",
    "1986 pages": r"355–376",
    "1998 pages": r"705–729",
    "2014 doi": r"10\.1115/1\.4026911",
    "2014 pages": r"040802",
    "three AMR": r"three",
    "missing source list": r"NOT READ",
    "noda listed": r"Noda",
    "our baseline 173": r"173",
    "our sections 39": r"39",
    "our refs 414": r"414",
    "our tables 26": r"26",
    "keywords finding": r"keywords",
    "nomenclature finding": r"Nomenclature",
    "citation scheme correction": r"sort&compress",
    "unsrtnat": r"unsrtnat",
    "asme bst": r"asme2e",
    "outlook": r"[Oo]utlook",
    "summary table": r"summary table",
}
for label, pattern in must.items():
    check(f"report: {label}", re.search(pattern, report) is not None, f"pattern {pattern!r}")

check("plan: ten sections", "10 numbered sections" in PLAN.read_text(encoding="utf8"))
check("plan: twelve appendices", "Appendices (12" in PLAN.read_text(encoding="utf8"))

# 4/5 ----------------------------------------------------------------------------------------
plan = PLAN.read_text(encoding="utf8")
old_map = re.findall(r"^old=(\d{2}) -> new=(.+)$", plan, re.M)
check("plan: 39 old sections mapped", len(old_map) == 39, f"{len(old_map)} lines")
check("plan: old sections 1..39 each once",
      sorted(int(a) for a, _ in old_map) == list(range(1, 40)),
      f"{sorted(int(a) for a, _ in old_map)}")
check("plan: every old section has a destination",
      all(dest.strip() for _, dest in old_map), "empty destination")
app_map = re.findall(r"^old=App\.([A-J]) -> new=App\.([A-J])$", plan, re.M)
check("plan: appendices A..J mapped once", [a for a, _ in app_map] == list("ABCDEFGHIJ"),
      f"{[a for a, _ in app_map]}")
for label in ("Table 1", "Appendix K", "Appendix L", "Conclusions and outlook"):
    check(f"plan: {label}", label in plan, "not stated")
check("plan: notation list", "notation list" in plan.lower(), "not stated")

# 6 ------------------------------------------------------------------------------------------
binaries = [p.name for p in HERE.iterdir() if p.is_file() and p.suffix.lower() in
            {".pdf", ".zip", ".png", ".jpg", ".jpeg", ".docx", ".xlsx"}]
check("folder has no binary artefacts", not binaries, f"{binaries}")
files = sorted(p.name for p in HERE.iterdir() if p.is_file())
check("folder contents", set(files) == {"report.md", "amr_papers.csv", "restructure_plan.md", "check_p15.py"},
      f"{files}")

def hygiene(name: str, text: str) -> None:
    stripped = (text.replace("`.tex`", "TEXTFILE").replace("main.pdf", "BUILDPDF")
                .replace("main.tex", "MAINTEX").replace("`main.tex`", "MAINTEX"))
    for pattern, label in (
        (r"[\w/\\-]+\.pdf\b", "pdf file name"),
        (r"[\w/\\-]+\.zip\b", "zip file name"),
        (r"[\w/\\-]+\.tex\b", "tex file name"),
        (r"https?://", "link"),
        (r"\bwww\.", "link"),
        (r"drive\.google|docs\.google|/gdrive/|/My Drive/|LE_SOURCES|0AGrjo", "drive reference"),
        (r"[A-Za-z0-9_\-]{33,}", "long opaque identifier"),
        (r"\\documentclass|\\begin\{|\\end\{", "latex source"),
    ):
        hit = re.search(pattern, stripped)
        check(f"hygiene {name}: {label}", hit is None,
              f"found {hit.group(0)[:60] if hit else ''}")

hygiene("report.md", report)
hygiene("restructure_plan.md", plan)
hygiene("amr_papers.csv", CSV.read_text(encoding="utf8"))

if fails:
    print(f"FAIL {len(fails)} check(s)")
    for f in fails:
        print("  -", f)
    sys.exit(1)

print(f"PASS P15: {len(by_key)} AMR articles (1986/1998/2014) with {len(COLUMNS)} fields each; "
      f"39 old body sections and 10 old appendices each mapped once to 10 sections + 12 appendices; "
      f"report states the three-article pattern, the missing Noda entry and the 173-page baseline; "
      f"no binary, link or library location in this folder")
sys.exit(0)
