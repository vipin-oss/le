#!/usr/bin/env python3
"""Apply only Crossref-VERIFIED, mapped R3e claims to Section 8."""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

from r3c_apply import merge_bib


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def insert_block(text: str, marker: str, content: str, anchor: str) -> str:
    begin = f"% R3E-BEGIN:{marker}"
    end = f"% R3E-END:{marker}"
    pattern = re.compile(rf"(?ms)^{re.escape(begin)}\n.*?^{re.escape(end)}\n?")
    text = pattern.sub("", text)
    if text.count(anchor) != 1:
        raise RuntimeError(f"Expected one Section 8 insertion anchor for R3e, found {text.count(anchor)}")
    block = f"{begin}\n{content.rstrip()}\n{end}\n\n"
    return text.replace(anchor, block + anchor, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-csv", type=Path, required=True)
    parser.add_argument("--map-csv", type=Path, required=True)
    parser.add_argument("--reports-dir", type=Path, required=True)
    parser.add_argument("--local-bib", type=Path, required=True)
    parser.add_argument("--sections-dir", type=Path, required=True)
    parser.add_argument("--status-report", type=Path, required=True)
    args = parser.parse_args()

    verified_rows = read_csv(args.verify_csv)
    mappings = read_csv(args.map_csv)
    if len(mappings) != 2:
        raise RuntimeError("R3e apply expects exactly the two requested source mappings")
    verify_by_key = {row.get("citekey", "").strip(): row for row in verified_rows}
    selected: dict[str, dict[str, str]] = {}
    for mapping in mappings:
        key = mapping.get("citekey", "").strip()
        check = verify_by_key.get(key, {})
        if (mapping.get("include", "").strip().upper() == "YES"
                and mapping.get("claim_status", "") == "PRIMARY-SOURCE-CHECKED"
                and check.get("DOI", "").strip().lower() == mapping.get("doi", "").strip().lower()
                and check.get("status") == "VERIFIED"
                and check.get("bib_ready") == "YES"):
            selected[key] = {**mapping, **check}

    added_keys = merge_bib(args.local_bib, args.reports_dir / "R3E_VERIFIED_REFERENCES.bib")
    local_keys = {row["key"] for row in __import__("crossref_enrich").parse_bib(args.local_bib)}
    missing_bib = sorted({row.get("resolved_citekey", "") for row in selected.values()} - local_keys)
    missing_bib = [key for key in missing_bib if key]
    if missing_bib:
        raise RuntimeError("R3e citations lack verified BibTeX entries: " + ", ".join(missing_bib))

    dubner_key = selected.get("DubnerAbate1968", {}).get("resolved_citekey")
    stehfest_key = selected.get("Stehfest1970", {}).get("resolved_citekey")
    blocks = []
    if dubner_key:
        blocks.append(
            r"\paragraph{Dubner--Abate cosine-series inversion.} For real causal $f$ with $f(t)=0$ for $t<0$, write $F(s)=\mathcal{L}\{f\}(s)$. Their Eq.~(15) obtains the following cosine series by applying the trapezoidal rule to the cosine inversion integral:"
            "\n\n"
            r"\begin{equation}"
            "\n"
            r"\begin{aligned}"
            "\n"
            r"f(t)&\simeq\frac{e^{at}}{T}\left[\frac{\operatorname{Re}F(a)}{2}+\right."
            r"\\"
            r"&\qquad\left.\sum_{k=1}^{\infty}\operatorname{Re}F\!\left(a+\frac{ik\pi}{T}\right)\cos\!\left(\frac{k\pi t}{T}\right)\right]."
            "\n"
            r"\end{aligned}"
            "\n"
            r"\end{equation}"
            "\n\n"
            rf"The formula is valid for $0<t<T/2$; choosing $T=2t_{{\max}}$ gives the source's stated window. Under its bounded-function assumption $|f|\leq C$, the periodization error is of order $C e^{{-aT}}$; finite-series truncation error is controlled separately by the last retained term (PRIMARY-SOURCE-CHECKED) \cite{{{dubner_key}}}."
        )
    if stehfest_key:
        blocks.append(
            r"\paragraph{Stehfest real-axis inversion.} For even $N$, Stehfest's algorithm writes the inversion as"
            "\n\n"
            r"\begin{equation}"
            "\n"
            r"F_a=\frac{\ln 2}{T}\sum_{i=1}^{N}V_i\,P\!\left(\frac{i\ln 2}{T}\right),\qquad N\ \text{even},"
            "\n"
            r"\end{equation}"
            "\n\n"
            r"where $P(s)=\mathcal{L}\{f\}(s)$ and"
            "\n\n"
            r"\begin{equation}"
            "\n"
            r"\begin{aligned}"
            "\n"
            r"V_i&=(-1)^{N/2+i}\sum_{k=\lfloor(i+1)/2\rfloor}^{\min(i,N/2)}"
            r"\\"
            r"&\quad\left[\begin{gathered}"
            r"\frac{k^{N/2}(2k)!}{(N/2-k)!\,k!\,(k-1)!}"
            r"\\"
            r"{}\times\frac{1}{(i-k)!(2k-i)!}"
            r"\end{gathered}\right]."
            "\n"
            r"\end{aligned}"
            "\n"
            r"\end{equation}"
            "\n\n"
            rf"The weights depend only on $N$ and grow as $N$ increases: accuracy can improve until rounding error dominates, so the choice of even $N$ trades approximation error against available precision (PRIMARY-SOURCE-CHECKED) \cite{{{stehfest_key}}}."
        )

    if blocks:
        blocks.append(
            r"\paragraph{Evidence scope.} These source-specific procedures do not establish a general method ranking. Limited primary sources are available for numerical Laplace inversion in this section."
        )
    else:
        blocks.append(
            r"\paragraph{Evidence scope.} The two requested Laplace-inversion records did not pass all Crossref/BibTeX gates; their source-specific formulas are not asserted here. Limited primary sources are available for numerical Laplace inversion in this section."
        )

    section_path = args.sections_dir / "sec08_mathematical_methods.tex"
    section = section_path.read_text(encoding="utf-8")
    section = insert_block(section, "LAPLACE-INVERSION", "\n\n".join(blocks),
                           r"\subsection{Green's functions and fundamental solutions}")
    section_path.write_text(section, encoding="utf-8")

    counts = Counter(row.get("status", "") for row in verified_rows)
    ready = sum(row.get("bib_ready") == "YES" for row in verified_rows)
    unresolved = [row for row in verified_rows if row.get("status") in {"MISMATCH", "NOT-FOUND"}
                  or (row.get("status") == "VERIFIED" and row.get("bib_ready") != "YES")]
    report = args.status_report.read_text(encoding="utf-8")
    begin = report.find("## R3e verification and Section 8 update")
    end = report.find("## Final strict build")
    if end < 0:
        raise RuntimeError("R3_STATUS.md must have the final-build heading")
    if begin < 0:
        begin = end
    elif begin >= end:
        raise RuntimeError("R3e status section must precede the final-build section")
    output = [
        "## R3e verification and Section 8 update", "",
        "- Scope: only the two requested DOIs were queried; no other Crossref records were requested.",
        f"- R3e Crossref: {len(verified_rows)} requested DOI rows; {counts['VERIFIED']} VERIFIED, {counts['MISMATCH']} MISMATCH, {counts['NOT-FOUND']} NOT-FOUND, {counts['NO-DOI']} NO-DOI; bibliography-ready: {ready}; mapped citations used: {len(selected)}; new BibTeX keys: {len(added_keys)}.",
        "- Section 8 uses the checked Dubner--Abate Eq. (15) cosine/trapezoidal formula and/or Stehfest's even-N weights only when that row is Crossref-VERIFIED and bibliography-ready. Stehfest is restricted to the paper's stated rounding-error/N trade-off; no behavior inference is attributed to him.",
        "- These two source-specific methods do not establish a broader comparison or ranking. Limited primary sources remain the stated scope for numerical Laplace inversion in Section 8.",
        "- R3e unresolved rows (not cited):",
    ]
    if unresolved:
        output.extend(f"  - `{row.get('citekey')}` / {row.get('DOI')} — {row.get('status')}: {row.get('reason', '')}" for row in unresolved)
    else:
        output.append("  - None.")
    output += ["", ""]
    report = report[:begin] + "\n".join(output) + report[end:]

    final_start = report.find("## Final strict build")
    final_block = report[final_start:]
    for label, marker in (("Content/source commit", "__R3_SOURCE_COMMIT__"),
                          ("Strict CI run ID", "__R3_CI_RUN_ID__"),
                          ("Strict build-step time", "__R3_BUILD_SECONDS__"),
                          ("PDF pages", "__R3_PDF_PAGES__"),
                          ("Undefined references/citations", "__R3_UNRESOLVED_REFS__")):
        final_block, count = re.subn(rf"(?m)^- {re.escape(label)}:.*$", f"- {label}: `{marker}`", final_block, count=1)
        if count != 1:
            raise RuntimeError(f"R3_STATUS.md final-build field missing: {label}")
    report = report[:final_start] + final_block
    args.status_report.write_text(report, encoding="utf-8")
    print(f"R3e selected {len(selected)} verified mapped rows; new BibTeX keys={len(added_keys)}; unresolved={len(unresolved)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
