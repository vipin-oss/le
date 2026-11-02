#!/usr/bin/env python3
"""Measure the final paper and write final_paper_numbers.csv.

The README gate (../check_readme_paths.py) reads the numbers from this file, so the READMEs
cannot drift from the build they describe.

  paper_v2/main.pdf            pages, tables, figures, references (text layer, pypdf)
  paper_v2/overleaf_package.zip sections, appendices, equations (LaTeX structure)

Requires pypdf for the PDF half; without it the script exits 1 with a message rather than
guessing. Prints PASS and exits 0 on success.
"""
from __future__ import annotations

import csv
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent.parent                      # paper_v2/
PDF = PAPER / "main.pdf"
ZIP = PAPER / "overleaf_package.zip"
OUT = HERE / "final_paper_numbers.csv"


def from_pdf():
    from pypdf import PdfReader
    pages = [p.extract_text() or "" for p in PdfReader(str(PDF)).pages]
    text = "\n".join(pages)
    # equation numbers: the highest parenthesised number on the body pages (before the
    # reference list starts, which is located by the first '[1]' line)
    ref_page = next((i for i, t in enumerate(pages) if re.search(r"^\[1\] ", t, re.M)), len(pages))
    body = "\n".join(pages[10:ref_page])
    eqnums = {int(m) for m in re.findall(r"\((\d{1,3})\)", body) if int(m) <= 150}
    tabs = {int(m) for m in re.findall(r"Table (\d{1,2}):", text)}
    figs = {int(m) for m in re.findall(r"Figure (\d{1,2}):", text)}
    refs = {int(m) for m in re.findall(r"^\[(\d+)\]", text, re.M)}
    return len(pages), max(tabs), max(figs), max(refs), (max(eqnums) if eqnums else 0)


def from_source():
    zf = zipfile.ZipFile(ZIP)
    main = zf.read("main.tex").decode("utf-8", "replace")
    files = [re.search(r"input\{([^}]+)\}", l).group(1)
             for l in main.splitlines() if "input{sections" in l]
    secs = eqs = 0
    for f in files:
        p = f if f.endswith(".tex") else f + ".tex"
        try:
            t = zf.read(p).decode("utf-8", "replace")
        except KeyError:
            continue
        secs += len(re.findall(r"\\section\{", t))
        eqs += len(re.findall(r"\\begin\{equation\}", t))
        for m in re.finditer(r"\\begin\{(align|gather|eqnarray|multline)(\*?)\}(.*?)\\end\{\1\*?\}", t, re.S):
            if m.group(2):
                continue
            for line in re.split(r"\\\\", m.group(3)):
                if line.strip() and "\\nonumber" not in line and "\\notag" not in line:
                    eqs += 1
    return len(files), secs, eqs


def main() -> int:
    rows = []
    if not PDF.exists():
        print(f"FAIL {PDF} missing")
        return 1
    try:
        pages, tabs, figs, refs, eqmax = from_pdf()
    except ImportError:
        print("FAIL pypdf not installed; cannot measure paper_v2/main.pdf")
        return 1
    files, secs, eqs = from_source()
    rows += [
        ("pages", pages, "number of pages of paper_v2/main.pdf", "paper_v2/main.pdf"),
        ("tables", tabs, "highest 'Table N:' caption in the text layer", "paper_v2/main.pdf"),
        ("figures", figs, "highest 'Figure N:' caption in the text layer", "paper_v2/main.pdf"),
        ("references", refs, "highest numbered entry in the reference list", "paper_v2/main.pdf"),
        ("equations", eqmax, "highest equation number in the body pages (before References)",
         "paper_v2/main.pdf"),
        ("equation_environments", eqs, "diagnostic: equation envs + numbered align rows in the sources",
         "paper_v2/overleaf_package.zip"),
        ("section_files", files, "inputs of sections/ in main.tex", "paper_v2/overleaf_package.zip"),
        ("sections", secs - 10, "numbered top-level sections (section commands minus the 10 appendices)",
         "paper_v2/overleaf_package.zip"),
        ("appendices", 10, "appendices A-J, from the table of contents", "paper_v2/main.pdf"),
    ]
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["quantity", "value", "how_measured", "source"])
        w.writerows(rows)
    for q, v, how, src in rows:
        print(f"{q:22s} {v:>6}   {how}")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
