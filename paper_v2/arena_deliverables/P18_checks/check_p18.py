#!/usr/bin/env python3
"""Gate for the P18 source checks (Green-Lindsay inequality, Nowacki, Chen/Dreyer-Struchtrup).

  P01  the folder holds exactly the four required files plus this gate
  P02  evidence.csv: >= 40 rows, unique ids, statuses in vocabulary, no empty
       provenance/location/consequence, and the seven source groups are all present
  P03  every source named in the task has a row, including the two with no equation-level
       read (Hetnarski-Ignaczak 1999/2000, Chandrasekharaiah 1998)
  P04  the two inequalities that were never recorded are marked NOT-RECORDED (ids G06, I06)
  P05  gl_inequality.md carries the mapping (alpha/h, t1/t0, tau_1/tau_0), the conversion
       rule both ways, the correction that GL is Section 4.2.3, and the two page pointers
  P06  nowacki.md carries both ISBNs, the 1986 Pergamon record, the author initial, and the
       no-copy / zero-record statements
  P07  extra_lit.md refuses a content summary and prints both bibliographic records
  P08  every DOI printed anywhere in the folder is one of the four verified here
  P09  repository hygiene: no binaries, no URLs, no cloud-drive references, no absolute paths
  P10  no file claims a primary-source read in this environment

Prints `PASS ...` and exits 0 only if every check holds.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

REQUIRED = ["gl_inequality.md", "nowacki.md", "extra_lit.md", "evidence.csv"]
STATUS = {"RECORDED-READ", "NOT-RECORDED", "NOT-IN-LIBRARY", "VERIFIED-EXTERNALLY",
          "DERIVED", "MANUSCRIPT-STATEMENT", "REPO-RECORD"}
VERIFIED_DOIS = {
    "10.1103/physrevlett.86.2297",
    "10.1007/bf01135371",
    "10.1080/01495737808926940",
    "10.1016/b978-0-08-024767-0",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=".")
    a = ap.parse_args()
    d = Path(a.dir).resolve()
    problems: list[str] = []
    notes: list[str] = []

    def bad(code, msg):
        problems.append(f"{code} {msg}")

    # P01 -------------------------------------------------------------------
    present = sorted(p.name for p in d.iterdir() if p.is_file())
    for name in REQUIRED:
        if name not in present:
            bad("P01", f"missing required file {name}")
    for name in present:
        if name not in REQUIRED and name != "check_p18.py":
            bad("P01", f"unexpected file: {name}")

    # P02 -------------------------------------------------------------------
    rows = []
    p = d / "evidence.csv"
    if p.exists():
        rows = list(csv.DictReader(p.open(encoding="utf-8")))
        if len(rows) < 40:
            bad("P02", f"only {len(rows)} evidence rows (expected at least 40)")
        ids = [r["id"] for r in rows]
        if len(ids) != len(set(ids)):
            bad("P02", "duplicate ids in evidence.csv")
        for r in rows:
            if r["status"] not in STATUS:
                bad("P02", f"{r['id']}: status {r['status']!r}")
            for f in ("provenance", "location_in_source", "consequence_for_review",
                      "finding", "item_sought", "source"):
                if not r.get(f, "").strip():
                    bad("P02", f"{r['id']}: empty {f}")
        notes.append(f"evidence rows={len(rows)}")

    blob = " ".join(" ".join(r.values()) for r in rows).lower()

    # P03 -------------------------------------------------------------------
    for probe, label in [
        ("green & lindsay 1972", "Green & Lindsay 1972"),
        ("ignaczak & ostoja-starzewski 2010", "Ignaczak & Ostoja-Starzewski 2010"),
        ("1999", "Hetnarski & Ignaczak 1999"),
        ("2000", "Hetnarski & Ignaczak 2000"),
        ("chandrasekharaiah 1998", "Chandrasekharaiah 1998"),
        ("chen 2001", "Chen 2001"),
        ("dreyer", "Dreyer & Struchtrup 1993"),
        ("nowacki", "Nowacki"),
    ]:
        if probe not in blob:
            bad("P03", f"no evidence row mentions {label}")

    # P04 -------------------------------------------------------------------
    by_id = {r["id"]: r for r in rows}
    for rid, label in [("G06", "Green-Lindsay inequality"),
                       ("I06", "Ignaczak-Ostoja-Starzewski inequality")]:
        r = by_id.get(rid)
        if not r:
            bad("P04", f"missing row {rid} ({label})")
        elif r["status"] != "NOT-RECORDED":
            bad("P04", f"{rid}: {label} is marked {r['status']}, must be NOT-RECORDED")

    # P05 -------------------------------------------------------------------
    p = d / "gl_inequality.md"
    if p.exists():
        t = p.read_text(encoding="utf-8")
        for probe, label in [
            ("α in the stress", "GL alpha in the stress"),
            ("h in the energy equation", "GL h in the energy equation"),
            ("t1", "I&O t1"),
            ("t0", "I&O t0"),
            ("τ1 ≥ τ0 ≥ 0", "conversion to tau_1 >= tau_0"),
            ("τ0 ≥ τ1 ≥ 0", "conversion to tau_0 >= tau_1"),
            ("4.2.3", "correction that GL is Section 4.2.3"),
            ("(4.8)–(4.10)", "GL page pointer to the restrictions"),
            ("printed p. 21", "I&O page pointer"),
            ("least one of these three printed statements is wrong", "the certainty statement"),
            ("No copy of any of the four sources exists in this working environment",
             "the environment statement"),
            ("NOT RECORDED", "the not-recorded marking"),
        ]:
            if probe not in t:
                bad("P05", f"gl_inequality.md lacks {label} ({probe!r})")
        if not re.search(r"p\.\s?5[,\s]", t) or not re.search(r"p\.\s?6", t):
            bad("P05", "gl_inequality.md does not cite printed pp. 5 and 6")

    # P06 -------------------------------------------------------------------
    p = d / "nowacki.md"
    if p.exists():
        t = p.read_text(encoding="utf-8")
        for probe, label in [
            ("9780080175238", "the bib ISBN"),
            ("9780080247670", "the 1986 ISBN"),
            ("Witold", "the author's given name"),
            ("1986", "the print year"),
            ("0 results", "the zero-record finding"),
            ("NOT SUPPLIED", "the library finding"),
            ("Nowacki, W.", "the corrected initial"),
        ]:
            if probe not in t:
                bad("P06", f"nowacki.md lacks {label} ({probe!r})")

    # P07 -------------------------------------------------------------------
    p = d / "extra_lit.md"
    if p.exists():
        t = p.read_text(encoding="utf-8")
        for probe, label in [
            ("10.1103/PhysRevLett.86.2297", "the Chen DOI"),
            ("10.1007/BF01135371", "the Dreyer-Struchtrup DOI"),
            ("2297–2300", "the Chen pages"),
            ("3–50", "the Dreyer-Struchtrup pages"),
            ("NOT IN LIBRARY", "the absence marking"),
            ("no sentence about either paper's content", "the refusal to summarise"),
        ]:
            if probe not in t:
                bad("P07", f"extra_lit.md lacks {label} ({probe!r})")
        if "the paper shows" in t.lower():
            bad("P07", "extra_lit.md appears to assert content of an unread paper")

    # P08 -------------------------------------------------------------------
    for p in d.iterdir():
        if p.suffix.lower() not in {".md", ".csv"}:
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"10\.\d{4,9}/[^\s,;)\]]+", t):
            doi = m.group(0).rstrip(".").lower()
            if not any(doi.startswith(v) for v in VERIFIED_DOIS):
                bad("P08", f"{p.name}: DOI not verified in this session: {m.group(0)}")

    # P09 -------------------------------------------------------------------
    for p in d.iterdir():
        if p.suffix.lower() in {".pdf", ".zip", ".png", ".jpg", ".jpeg"}:
            bad("P09", f"binary artefact: {p.name}")
        if p.name == "check_p18.py" or p.suffix.lower() not in {".md", ".csv"}:
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        for s, label in [("http://", "URL"), ("https://", "URL"),
                         ("drive.google", "cloud-drive reference"),
                         ("docs.google", "cloud-drive reference"),
                         ("/Users/", "absolute local path"),
                         ("C:\\", "absolute local path"),
                         ("Overleaf", "external service name")]:
            if s in t:
                bad("P09", f"{p.name}: contains {label} ('{s}')")
        if re.search(r"\b1[A-Za-z0-9_-]{25,}\b", t):
            bad("P09", f"{p.name}: looks like a cloud-drive identifier")

    # P10 -------------------------------------------------------------------
    forbidden = ["was read here", "read in this environment", "I read the",
                 "was read for this task", "reading the copy"]
    for p in d.iterdir():
        if p.suffix.lower() not in {".md", ".csv"}:
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        low = t.lower()
        for f in forbidden:
            if f.lower() in low:
                bad("P10", f"{p.name}: claims a fresh read ('{f}')")

    for n in notes:
        print(f"  note: {n}")
    if problems:
        for pr in problems:
            print(f"FAIL {pr}")
        print(f"FAIL {len(problems)} problem(s)")
        return 1
    print(f"PASS all P18 checks ({len(REQUIRED)} files, {len(notes)} notes, 0 problems)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
