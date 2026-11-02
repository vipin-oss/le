#!/usr/bin/env python3
"""Gate for the P17 submission-support deliverables.

Checks the eight files in this directory against the rules of task P17 (request BA):

  G01  the directory holds exactly the eight required files plus this gate
  G02  pages_fix.csv: the seven keys, all fields filled, a DOI in the evidence column,
       the match columns in {yes,no}, and no NOT FOUND unless the evidence says why
  G03  abstract_claims.csv: 12 claims, statuses in {yes,partly,no}, every claim carries
       the place in the body that supports it, excerpts stay at 15 words or fewer
  G04  figure_table_list.csv: figures 1-41 and tables 1-25 all present, source and units
       columns filled, severities in vocabulary, an action wherever a finding is recorded
  G05  referee_report.md: the three severity labels are used, at least 15 numbered
       findings, and every finding carries a page or section reference
  G06  supplement_plan.md: all twelve appendices A-L appear with a page count, the
       self-containment requirement is stated, and the reference-renumbering cost is
       stated as a number
  G07  presubmission_email.md: the quoted abstract is 150 words or fewer, the length
       statement is present, and no reviewer is named
  G08  cover_letter.md: originality/simultaneous submission, generative-tool
       disclosure, code availability, permissions and the self-citation proportion
  G09  new_vs_existing.md: the quotable block is 120 words or fewer and cites sections
  G10  every word count that a file claims about itself is the true count
  G11  repository hygiene: no PDFs, archives or images here, no URLs, no cloud-drive
       references or identifiers, no absolute local paths, no folder names
  G12  no first person in the paper-facing statement

Prints `PASS ...` and exits 0 only if every check holds.

Usage:  python3 check_p17.py [--dir .]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

REQUIRED = [
    "pages_fix.csv",
    "referee_report.md",
    "abstract_claims.csv",
    "supplement_plan.md",
    "presubmission_email.md",
    "cover_letter.md",
    "new_vs_existing.md",
    "figure_table_list.csv",
]
KEYS = ["Maranganti2006", "Julius2017", "Ezzat2016", "Das2026",
        "Singh2020d", "Tiwari2022", "Singh2023"]
SEV = {"critical", "major", "minor", "none"}
STATUS = {"yes", "partly", "no"}
APPX = list("ABCDEFGHIJKL")


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", text)


def blockquoted_after(txt: str, marker: str) -> str:
    """Return the blockquote that follows the first line containing `marker`."""
    lines = txt.splitlines()
    start = None
    for i, ln in enumerate(lines):
        if marker in ln:
            start = i + 1
            break
    if start is None:
        return ""
    out = []
    for ln in lines[start:]:
        if ln.startswith(">"):
            out.append(re.sub(r"^>\s?", "", ln))
        elif out:
            break
        elif ln.strip():
            break
    return " ".join(out).strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=".")
    a = ap.parse_args()
    d = Path(a.dir).resolve()
    problems: list[str] = []
    notes: list[str] = []

    def fail(code, msg):
        problems.append(f"{code} {msg}")

    # ---- G01 file set -------------------------------------------------------
    present = sorted(p.name for p in d.iterdir() if p.is_file())
    for name in REQUIRED:
        if name not in present:
            fail("G01", f"missing required file {name}")
    for name in present:
        if name not in REQUIRED and name != "check_p17.py":
            fail("G01", f"unexpected file in the deliverable directory: {name}")
    notes.append(f"files={len(present)}")

    # ---- G02 pages_fix.csv --------------------------------------------------
    p = d / "pages_fix.csv"
    if p.exists():
        rows = list(csv.DictReader(p.open(encoding="utf-8")))
        if [r["key"] for r in rows] != KEYS:
            fail("G02", f"keys are {[r['key'] for r in rows]} (expected the seven of the task)")
        for r in rows:
            for f in ("volume", "issue", "pages_or_article_no", "evidence"):
                if not r.get(f, "").strip():
                    fail("G02", f"{r['key']}: empty field {f}")
            if "10." not in r.get("evidence", ""):
                fail("G02", f"{r['key']}: evidence carries no DOI")
            for f in ("title_match", "authors_match", "year_match", "journal_match"):
                if r.get(f) not in {"yes", "no"}:
                    fail("G02", f"{r['key']}: {f} = {r.get(f)!r}")
            if "NOT FOUND" in str(r) and "NOT FOUND" not in r.get("evidence", ""):
                fail("G02", f"{r['key']}: NOT FOUND without evidence")
        notes.append(f"pages_fix keys={len(rows)}")

    # ---- G03 abstract_claims.csv -------------------------------------------
    p = d / "abstract_claims.csv"
    if p.exists():
        rows = list(csv.DictReader(p.open(encoding="utf-8")))
        if len(rows) != 12:
            fail("G03", f"{len(rows)} claims (expected 12)")
        for r in rows:
            if r.get("status") not in STATUS:
                fail("G03", f"{r.get('claim_id')}: status {r.get('status')!r}")
            if not r.get("supported_where", "").strip():
                fail("G03", f"{r.get('claim_id')}: no body reference")
            if len(words(r.get("claim_excerpt", ""))) > 15:
                fail("G03", f"{r.get('claim_id')}: excerpt longer than 15 words")
            if not re.search(r"Sec\.|Table|Fig\.|Eq\.", r.get("supported_where", "")):
                fail("G03", f"{r.get('claim_id')}: body reference is not a location")
        notes.append("claims=" + str(len(rows)))

    # ---- G04 figure_table_list.csv -----------------------------------------
    p = d / "figure_table_list.csv"
    if p.exists():
        rows = list(csv.DictReader(p.open(encoding="utf-8")))
        figs = sorted(int(r["number"]) for r in rows if r["kind"] == "figure")
        tabs = sorted(int(r["number"]) for r in rows if r["kind"] == "table")
        if figs != list(range(1, 42)):
            fail("G04", f"figures present: {figs}")
        if tabs != list(range(1, 26)):
            fail("G04", f"tables present: {tabs}")
        for r in rows:
            if r["severity"] not in SEV:
                fail("G04", f"{r['item_id']}: severity {r['severity']!r}")
            if not r["source_or_script"].strip():
                fail("G04", f"{r['item_id']}: no source or script")
            if not r["units_or_parameters"].strip():
                fail("G04", f"{r['item_id']}: no units or parameters")
            if r["severity"] != "none" and not r["finding"].strip():
                fail("G04", f"{r['item_id']}: severity without a finding")
            if r["severity"] != "none" and not r["action"].strip():
                fail("G04", f"{r['item_id']}: finding without an action")
            if not r["printed_page"].isdigit():
                fail("G04", f"{r['item_id']}: page {r['printed_page']!r}")
        notes.append(f"figures={len(figs)}, tables={len(tabs)}")

    # ---- G05 referee_report.md ---------------------------------------------
    p = d / "referee_report.md"
    if p.exists():
        t = p.read_text(encoding="utf-8")
        for sev in ("critical", "major", "minor"):
            if sev not in t:
                fail("G05", f"severity {sev} never used")
        ids = sorted(set(re.findall(r"^### (R\d+)", t, re.M)),
                     key=lambda s: int(s[1:]))
        if len(ids) < 15:
            fail("G05", f"only {len(ids)} numbered findings")
        for m in re.finditer(r"^### (R\d+)[^\n]*", t, re.M):
            head = m.group(0)
            if "**" not in head:
                fail("G05", f"{m.group(1)}: no severity label on the finding")
        if not re.search(r"p\.\s?\d", t):
            fail("G05", "no page references")
        if "UNVERIFIED" not in t:
            fail("G05", "no UNVERIFIED marking for an unchecked reference")
        if not re.search(r"DOI 10\.", t):
            fail("G05", "no verified DOI for the suggested literature")
        notes.append(f"findings={len(ids)}")

    # ---- G06 supplement_plan.md -------------------------------------------
    p = d / "supplement_plan.md"
    if p.exists():
        t = p.read_text(encoding="utf-8")
        for L in APPX:
            if not re.search(rf"^\|\s*{L}\s*\|\s*p\.\s*\d+\s*\|", t, re.M):
                fail("G06", f"appendix {L} not listed with its opening page")
        if "self-contained" not in t:
            fail("G06", "the self-containment requirement is not stated")
        if not re.search(r"\b(66|72|75)\b\s*(of the|references|of them)", t):
            fail("G06", "the reference-renumbering cost is not stated as a number")
        if len(re.findall(r"\|\s*\d+\s*\|", t)) < 10:
            fail("G06", "fewer than ten page-count cells")
        notes.append("appendices A-L listed with pages")

    # ---- G07 presubmission_email.md ---------------------------------------
    p = d / "presubmission_email.md"
    if p.exists():
        t = p.read_text(encoding="utf-8")
        abstract = blockquoted_after(t, "Abstract (150 words)")
        n = len(words(abstract))
        if not abstract:
            fail("G07", "no quoted abstract found")
        elif n > 150:
            fail("G07", f"abstract is {n} words (limit 150)")
        else:
            notes.append(f"abstract words={n}")
        if "supplementary material" not in t:
            fail("G07", "no supplementary-material statement")
        if "157 pages" not in t:
            fail("G07", "no length statement in pages")
        if not re.search(r"[Ss]uggested reviewers", t):
            fail("G07", "the no-reviewers position is not stated")
        m = re.search(r"\*\*Suggested reviewers\.\*\*\s*(.+)", t)
        if m and "none proposed" not in m.group(1).lower():
            fail("G07", f"a reviewer may be named: {m.group(1)[:40]!r}")

    # ---- G08 cover_letter.md ----------------------------------------------
    p = d / "cover_letter.md"
    if p.exists():
        low = p.read_text(encoding="utf-8").lower()
        for needle, label in [
            ("simultaneous", "no-simultaneous-submission statement"),
            ("not been published", "prior-publication statement"),
            ("generative", "generative-tool disclosure"),
            ("availability", "data/code availability"),
            ("permission", "figure permissions"),
            ("9.2", "self-citation proportion"),
        ]:
            if needle not in low:
                fail("G08", f"missing {label}")

    # ---- G09 new_vs_existing.md -------------------------------------------
    p = d / "new_vs_existing.md"
    if p.exists():
        t = p.read_text(encoding="utf-8")
        block = blockquoted_after(t, "The statement (")
        n = len(words(block))
        if not block:
            fail("G09", "no quoted statement found")
        elif n > 120:
            fail("G09", f"statement is {n} words (limit 120)")
        else:
            notes.append(f"new-vs-existing words={n}")
        if len(re.findall(r"Sec\.\s*\d", block)) < 3:
            fail("G09", "the statement does not trace its items to sections")

    # ---- G10 self-reported word counts are true ---------------------------
    for name, pattern in [("presubmission_email.md", r"the draft is (\d+)"),
                          ("new_vs_existing.md", r"\((\d+) words, within")]:
        p = d / name
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8")
        m = re.search(pattern, t)
        if not m:
            continue
        claimed = int(m.group(1))
        marker = "Abstract (150 words)" if name.startswith("presub") else "The statement ("
        actual = len(words(blockquoted_after(t, marker)))
        if claimed != actual:
            fail("G10", f"{name} claims {claimed} words, the block has {actual}")

    # ---- G11 repository hygiene -------------------------------------------
    for p in d.iterdir():
        if p.name == "check_p17.py":
            continue
        if p.suffix.lower() in {".pdf", ".zip", ".png", ".jpg", ".jpeg", ".docx", ".xlsx"}:
            fail("G11", f"binary artefact in the repository: {p.name}")
        if p.suffix.lower() not in {".md", ".csv", ".py"}:
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        for bad, label in [("http://", "URL"), ("https://", "URL"),
                           ("drive.google", "cloud-drive reference"),
                           ("docs.google", "cloud-drive reference"),
                           ("/Users/", "absolute local path"),
                           ("C:\\", "absolute local path"),
                           ("Overleaf", "external folder or service name"),
                           ("Dropbox", "external folder or service name")]:
            if bad in t:
                fail("G11", f"{p.name}: contains {label} ('{bad}')")
        if re.search(r"\b1[A-Za-z0-9_-]{25,}\b", t):
            fail("G11", f"{p.name}: looks like a cloud-drive file identifier")

    # ---- G12 no first person in the paper-facing statement -----------------
    p = d / "new_vs_existing.md"
    if p.exists():
        block = blockquoted_after(p.read_text(encoding="utf-8"), "The statement (")
        if re.search(r"\b(I|we|our|us|my)\b", block):
            fail("G12", "first person in the paper-facing statement")

    for n in notes:
        print(f"  note: {n}")
    if problems:
        for pr in problems:
            print(f"FAIL {pr}")
        print(f"FAIL {len(problems)} problem(s)")
        return 1
    print(f"PASS all P17 deliverable checks ({len(REQUIRED)} files, "
          f"{len(notes)} notes, 0 problems)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
