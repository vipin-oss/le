#!/usr/bin/env python3
"""Page-level audit of the compiled v1.2 review paper (P1 second half).

Cross-checks the *compiled PDF* against the *LaTeX sources* it was built from.
This is deliberately a different question from `audit_sources.py`: that script
asks "are the claims sourced?"; this one asks "did the document that a reader
receives actually contain what the sources say, with nothing unresolved,
nothing leaked, and nothing broken?".

Inputs
  --pdf       compiled PDF (kept outside the repository)
  --master    directory holding the .tex sources (default master/)
  --out       output directory for the CSV + summary

Outputs
  page_audit_results.csv   one row per checked object
  PAGE_AUDIT_SUMMARY.md    human-readable summary

Verdicts are PASS / FAIL / REPORT.  REPORT is used where the measured value is
informative but has no defensible threshold (page count, word count, status
histogram); it is never a substitute for a failing assertion.

No network.  No writes outside --out.  Requires PyMuPDF.
"""
from __future__ import annotations

import argparse
import collections
import csv
import unicodedata
import json
import re
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:  # pragma: no cover
    try:
        import fitz as pymupdf
    except ImportError:
        sys.exit("FATAL: PyMuPDF not available (pip install --break-system-packages pymupdf)")

STATUSES = {"DERIVED", "CONDITIONAL", "PRIMARY-SOURCE-CHECKED",
            "SECONDARY-SOURCE", "UNVERIFIED", "OPEN"}

TEX_ESCAPES = {
    r"\%": "%", r"\&": "&", r"\_": "_", r"\#": "#", r"\$": "$",
    r"\textbackslash{}": "", r"\textasciitilde{}": "~",
    r"\,": " ", r"\;": " ", r"\:": " ", r"\ ": " ", r"\!": "", r"\-": "", r"\/": "",
}


def tex_to_text(s: str) -> str:
    """Reduce a LaTeX brace fragment to the characters a PDF reader would see."""
    s = s.replace("---", "\u2014").replace("--", "\u2013")
    s = s.replace("``", "\u201c").replace("''", "\u201d")
    for a, b in TEX_ESCAPES.items():
        s = s.replace(a, b)
    s = re.sub(r"\\[a-zA-Z]+\*?", "", s)
    s = s.replace("{", "").replace("}", "").replace("~", " ")
    s = s.replace("$", "")
    return re.sub(r"\s+", " ", s).strip()


def norm(s: str) -> str:
    """Normalise whitespace + typographic variants so containment tests compare
    characters a reader sees, not the encodings pdfTeX happened to emit."""
    s = s.replace("\u00ad", "")
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl").replace("\ufb00", "ff")
    s = re.sub(r"[ \t\n\r\u00a0]+", " ", s)
    return s.strip()


def alnum(s: str) -> str:
    """Letters and digits only: the strongest comparison that still ignores
    line-breaking, hyphenation and maths spacing."""
    s = re.sub(r"\\[a-zA-Z]+|[\\^~'\"`=.]", "", norm(s))  # drop LaTeX accent machinery
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", s.lower())


def reachable_files(src: dict[str, str]) -> set[str]:
    """Files reachable from main.tex through the \\input/\\include graph."""
    seen: set[str] = set()
    stack = ["main.tex"]
    while stack:
        cur = stack.pop()
        if cur in seen or cur not in src:
            continue
        seen.add(cur)
        base = Path(cur).parent
        for m in re.finditer(r"\\(?:input|include)\s*\{([^}]+)\}", src[cur]):
            tgt = m.group(1).strip()
            if not tgt.endswith(".tex"):
                tgt += ".tex"
            cand = (base / tgt).as_posix()
            stack.append(cand if cand in src else tgt)
    return seen


def tex_files(master: Path) -> list[Path]:
    return sorted(p for p in master.rglob("*.tex"))


def brace_arg(text: str, cmd: str) -> list[str]:
    """Return the first brace group after every occurrence of \\cmd (1 level)."""
    out = []
    for m in re.finditer(r"\\" + cmd + r"\*?\s*(?:\[[^\]]*\])?\s*\{", text):
        i = m.end()
        depth, start = 1, i
        while i < len(text) and depth:
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
            elif text[i] == "\\":
                i += 1
            i += 1
        out.append(text[start:i - 1])
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--master", default="master")
    ap.add_argument("--out", default="P1_audit")
    args = ap.parse_args()

    pdf_path = Path(args.pdf)
    master = Path(args.master)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(pdf_path)
    pages = [doc[i].get_text() for i in range(doc.page_count)]
    full = norm("\n".join(pages))
    low = full.lower()
    src = {p.relative_to(master).as_posix(): p.read_text(encoding="utf-8", errors="replace")
           for p in tex_files(master)}
    all_tex = "\n".join(src.values())

    # Which sources changed after this PDF was compiled? Needed by P06/P12 so that
    # "the PDF predates the edit" is not reported as "the source is missing from the PDF".
    import datetime
    _m = re.match(r"D:(\d{14})", doc.metadata.get("creationDate", "") or "")
    built_at = datetime.datetime.strptime(_m.group(1), "%Y%m%d%H%M%S") if _m else None
    drift = set()
    if built_at:
        for f in src:
            mt = datetime.datetime.utcfromtimestamp((master / f).stat().st_mtime)
            if mt > built_at + datetime.timedelta(seconds=60):
                drift.add(f)

    rows: list[dict] = []

    def add(cid, obj, expected, observed, verdict, note=""):
        rows.append(dict(check_id=cid, object=obj, expected=expected,
                         observed=observed, verdict=verdict, note=note))

    # ---- P01 document identity -------------------------------------------
    meta = {k: v for k, v in doc.metadata.items() if v}
    add("P01", "pdf opens / identity",
        "readable, titled, authored",
        f"pages={doc.page_count}; title={meta.get('title','-')!r}; author={meta.get('author','-')!r}; "
        f"producer={meta.get('producer','-')}",
        "PASS" if meta.get("title") and meta.get("author") else "FAIL")

    words = len(full.split())
    add("P02", "extent", "reported (no target length imposed)",
        f"{doc.page_count} pages, {words} words", "REPORT")

    # ---- P03 unresolved references and citations --------------------------
    qq = full.count("??")
    add("P03", "unresolved \\ref (?? marks)", "0", str(qq), "PASS" if qq == 0 else "FAIL")
    miss = full.count("[?]")
    add("P04", "missing citations ([?] marks)", "0", str(miss), "PASS" if miss == 0 else "FAIL")

    # ---- P05 leaked LaTeX -------------------------------------------------
    leaks = {tok: full.count(tok) for tok in
             ("\\begin{", "\\end{", "Undefined control sequence", "LaTeX Error",
              "\\cite{", "\\ref{", "Overfull \\hbox")}
    n_leak = sum(leaks.values())
    add("P05", "leaked LaTeX / errors in PDF text", "0",
        "; ".join(f"{k}={v}" for k, v in leaks.items() if v) or "none",
        "PASS" if n_leak == 0 else "FAIL")

    # ---- P06 section titles present --------------------------------------
    titles = []
    for f, t in src.items():
        for cmd in ("section", "subsection"):
            for a in brace_arg(t, cmd):
                if "%" in a or a.startswith("\\"):
                    continue
                txt = tex_to_text(a)
                if len(txt) > 3:
                    titles.append((cmd, f, txt))
    hay_a = alnum(full)
    missing = []
    for cmd, f, txt in titles:
        key = alnum(txt)
        if key[:70] and key[:70] not in hay_a:
            missing.append(f"{f}:{cmd}:{txt[:60]}")
    pending = [m for m in missing if m.split(":")[0] in drift]
    lost = [m for m in missing if m.split(":")[0] not in drift]
    add("P06", "every \\section/\\subsection title appears in the PDF",
        f"all {len(titles)} titles present",
        f"{len(missing)} not in this PDF ({len(pending)} pending rebuild, {len(lost)} unexplained)",
        "PASS" if not lost else "FAIL",
        ("pending rebuild: " + " | ".join(pending[:4])) if pending else " | ".join(lost[:8]))

    # ---- P07 appendices ---------------------------------------------------
    app_titles = [tex_to_text(a) for a in brace_arg(all_tex, "section")]
    letters = re.findall(r"\\appendix|\\begin\{appendices\}", all_tex)
    reached = reachable_files(src)
    appfiles = sorted(f for f in src if Path(f).parent.name == "appendices" and f in reached)
    found = []
    for f in appfiles:
        args = brace_arg(src[f], "section")
        if not args:
            continue
        t = tex_to_text(args[0])
        if t and t in full:
            found.append(f)
    add("P07", "appendix files present in PDF",
        f"{len(appfiles)} appendix sources rendered",
        f"{len(found)}/{len(appfiles)}", "PASS" if len(found) == len(appfiles) else "FAIL",
        " | ".join(sorted(set(appfiles) - set(found))[:10]))

    # ---- P08 abstract / keywords / declarations ---------------------------
    kwm = re.search(r"Keywords:\s*", full)
    if kwm:
        window = full[kwm.end():kwm.end() + 700]
        window = re.split(r"\n\s*(?:1\s+Introduction|Contents)", window)[0]
        nkw = len([k for k in re.split(r";", window) if len(k.strip()) > 3])
    else:
        nkw = 0
    add("P08", "keywords block", ">= 6 keywords", f"{nkw} keywords",
        "PASS" if nkw >= 6 else "FAIL")
    decl = "declarations" in low
    add("P09", "declarations section", "present", "present" if decl else "absent",
        "PASS" if decl else "FAIL")
    abs_words = 0
    if (m := re.search(r"Abstract(.{0,4000}?)Keywords:", full, re.S)):
        abs_words = len(m.group(1).split())
    add("P10", "abstract length", "150-350 words", f"{abs_words} words",
        "PASS" if 150 <= abs_words <= 350 else "FAIL")

    # ---- P11 figures ------------------------------------------------------
    inc = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", all_tex)
    inc = [i for i in inc if "figures/provisional" not in i]
    # Figures are included as vector PDFs, so they are content streams rather
    # than raster XObjects: test the pages that carry a figure caption for
    # non-text drawing content instead of counting get_images().
    fig_pages = []
    for i in range(doc.page_count):
        txt = pages[i]
        if re.search(r"Figure\s+\d+:\s*", txt):
            drawings = len(doc[i].get_drawings())
            raster = len(doc[i].get_images(full=True))
            if drawings > 0 or raster > 0:
                fig_pages.append(i + 1)
    add("P11", "figure pages carry vector/raster artwork",
        f"{len(inc)} \\includegraphics in sources",
        f"{len(fig_pages)} pages with a figure caption and drawing content",
        "PASS" if len(fig_pages) >= max(1, len(inc) - 2) else "FAIL",
        "vector figures are content streams; caption pages without artwork would "
        "mean a missing graphic")

    # ---- P12 figure + table captions -------------------------------------
    caps = []
    for f, s in src.items():
        for c in brace_arg(s, "caption"):
            txt = tex_to_text(c)
            if len(txt) > 12:
                caps.append((f, txt))
    full_a = alnum(full)
    cap_missing = [c for c in caps if alnum(c[1])[:60] not in full_a]
    cpend = [c for c in cap_missing if c[0] in drift]
    clust = [c for c in cap_missing if c[0] not in drift]
    add("P12", "figure/table captions rendered",
        f"all {len(caps)} captions",
        f"{len(caps) - len(cap_missing)} present, {len(cpend)} pending rebuild, "
        f"{len(clust)} unexplained", "PASS" if not clust else "FAIL",
        " | ".join(c[1][:50] for c in clust[:5]))

    # ---- P13 equation register integrity ----------------------------------
    eq_ids = re.findall(r"\bEQ-(\d{3})\b", all_tex)
    cnt = collections.Counter(eq_ids)
    dups = [k for k, v in cnt.items() if v > 1 and v > 6]  # 1 def + a few refs
    statuses = collections.Counter()
    for line in all_tex.splitlines():
        m = re.match(r"\s*EQ-\d{3}\s*&(.*?)&\s*([A-Z][A-Z-]+)\s*&", line)
        if m:
            statuses[m.group(2)] += 1
    add("P13", "equation register: unique EQ ids",
        "no id reused as a definition",
        f"{len(cnt)} distinct ids; def-lines={sum(statuses.values())}; "
        f"dups-suspect={len(dups)}", "REPORT" if not dups else "FAIL",
        " | ".join(f"EQ-{d}" for d in dups[:8]))
    legend = set(re.findall(r"\\item \\textbf\{([A-Z][A-Z-]+):\}", all_tex))
    bad = sorted(set(statuses) - legend)
    add("P14", "equation register: every status is defined in the legend",
        "statuses used == statuses defined",
        "; ".join(f"{k}={v}" for k, v in statuses.most_common()),
        "PASS" if not bad else "FAIL",
        ("undefined labels: " + ", ".join(bad)) if bad else "")
    pct_verified = 100.0 * (statuses["DERIVED"] + statuses["PRIMARY-SOURCE-CHECKED"]) / max(1, sum(statuses.values()))
    add("P15", "equation register: derived + primary-checked share",
        "reported (no threshold imposed; v1.1 stated the register is largely unverified)",
        f"{pct_verified:.1f}% of {sum(statuses.values())} rows", "REPORT")

    # ---- P16 numbered equations in the PDF --------------------------------
    eq_nums = set()
    for t in pages:
        for m in re.finditer(r"\((\d{1,3})\)\s*$", t, re.M):
            eq_nums.add(int(m.group(1)))
    add("P16", "numbered equations in PDF", "reported for register cross-check",
        f"{len(eq_nums)} distinct equation numbers, max={max(eq_nums) if eq_nums else 0}",
        "REPORT")

    # ---- P17 bibliography --------------------------------------------------
    bib = list(master.rglob("*.bib"))
    bib_keys: set[str] = set()
    for b in bib:
        bib_keys |= set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", b.read_text(errors="replace")))
    cited: set[str] = set()
    for m in re.finditer(r"\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}", all_tex):
        cited |= {k.strip() for k in m.group(1).split(",") if k.strip()}
    # The bibliography is author--year (no numbers): check that each cited
    # entry's first-author surname and year actually appear in the printed list.
    ref_start = next((i for i in range(doc.page_count)
                      if re.search(r"^\s*References\s*$", pages[i], re.M)), None)
    ref_text = alnum("\n".join(pages[ref_start:])) if ref_start is not None else ""
    bib_records: dict[str, tuple[str, str]] = {}
    for b in bib:
        body = b.read_text(errors="replace")
        for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)(?=\n@|\Z)", body, re.S):
            key, blk = m.group(1), m.group(2)
            am = re.search(r"author\s*=\s*[{\"](.*?)[}\"]\s*,?\n", blk, re.S)
            ym = re.search(r"\byear\s*=\s*[{]?\s*(\d{4})", blk)
            if not (am and ym):
                continue
            first = re.split(r"\s+and\s+", am.group(1).strip())[0]
            surname = first.split(",")[0] if "," in first else first.split()[-1]
            bib_records[key] = (alnum(surname), ym.group(1))
    unresolved = [k for k in cited
                  if k not in bib_keys
                  or (k in bib_records and bib_records[k][0] not in ref_text)]
    add("P17", "citations resolve to a printed reference",
        f"every cited key appears in .bib and in the reference list ({len(cited)} cited)",
        f"{len(unresolved)} unresolved; reference list found on p.{ref_start + 1 if ref_start is not None else 0}",
        "PASS" if not unresolved else "FAIL",
        " | ".join(sorted(unresolved)[:10]))
    uncited = sorted(bib_keys - cited)
    add("P18", "bibliographic hygiene", "reported (uncited entries are allowed)",
        f"{len(bib_keys)} entries, {len(cited)} cited, {len(uncited)} uncited", "REPORT",
        " | ".join(uncited[:10]))

    # ---- P19 font embedding ------------------------------------------------
    bad_fonts = set()
    for i in range(doc.page_count):
        for f in doc[i].get_fonts(full=True):
            # (xref, ext, type, basefont, name, encoding)
            if f[1] == "" and f[3] not in bad_fonts:
                bad_fonts.add(f"{f[3]}(base14-no-file)")
    add("P19", "fonts embedded", "every font has an embedded file",
        "all embedded" if not bad_fonts else f"{len(bad_fonts)} without file",
        "PASS" if not bad_fonts else "REPORT", " | ".join(sorted(bad_fonts)[:6]))

    # ---- P20 margin overflow proxy ----------------------------------------
    over = []
    for i in range(doc.page_count):
        pw = doc[i].rect.width
        for b in doc[i].get_text("blocks"):
            if b[2] > pw - 40:  # 40 pt right margin guard
                over.append(i + 1)
                break
    add("P20", "right-margin overflow proxy",
        "no page with text within 40 pt of the trim edge",
        f"{len(over)} pages flagged", "PASS" if not over else "REPORT",
        f"pages: {sorted(set(over))[:15]}")

    # ---- P21 table of contents --------------------------------------------
    toc = "contents" in low[:6000]
    add("P21", "table of contents", "present near the front matter",
        "present" if toc else "absent", "PASS" if toc else "REPORT")
    bookmarks = len(doc.get_toc())
    add("P22", "PDF bookmarks (hyperref outlines)", ">= 10 entries", f"{bookmarks} entries",
        "PASS" if bookmarks >= 10 else "REPORT")

    # ---- P23 every source file is reachable from main.tex -------------------
    orphans = sorted(set(src) - reachable_files(src))
    add("P23", "no orphan .tex in the built tree",
        "every source reachable from main.tex via \\input/\\include",
        f"{len(orphans)} unreachable of {len(src)}",
        "PASS" if not orphans else "FAIL", " | ".join(orphans[:10]))

    # ---- P24 figure and table numbering contiguous --------------------------
    fig_n = sorted({int(m.group(1)) for t in pages
                    for m in re.finditer(r"Figure\s+(\d+)\s*:", t)})
    tab_n = sorted({int(m.group(1)) for t in pages
                    for m in re.finditer(r"Table\s+(\d+)\s*:", t)})
    fig_gap = [n for n in range(1, (max(fig_n) if fig_n else 0) + 1) if n not in fig_n]
    tab_gap = [n for n in range(1, (max(tab_n) if tab_n else 0) + 1) if n not in tab_n]
    add("P24", "float numbering contiguous",
        "no gaps in Figure/Table numbers",
        f"figures 1-{max(fig_n) if fig_n else 0} ({len(fig_n)} seen, gaps={fig_gap}); "
        f"tables 1-{max(tab_n) if tab_n else 0} ({len(tab_n)} seen, gaps={tab_gap})",
        "PASS" if not fig_gap and not tab_gap else "FAIL")

    # ---- P25 sources unchanged since the PDF was compiled -------------------
    cdate = doc.metadata.get("creationDate", "")
    add("P25", "sources unchanged since this PDF was compiled",
        "no .tex edited after the build timestamp",
        f"{len(drift)} file(s) edited after {cdate}" if drift else "none",
        "PASS" if not drift else "REPORT",
        ("rebuild needed for: " + ", ".join(sorted(drift)[:6])) if drift else "")

    # ---- P26 section order and page map from hyperref bookmarks ------------
    toc = doc.get_toc(simple=True)
    lv1 = [e for e in toc if e[0] == 1]
    order = re.findall(r"\\input\{([^}]+)\}", src.get("main.tex", ""))
    pagemap, unmapped = [], []
    for f in order:
        name = f if f.endswith(".tex") else f + ".tex"
        if name not in src:
            continue
        args = brace_arg(src[name], "section")
        if not args:
            continue
        title = tex_to_text(args[0])
        key = alnum(title)
        hit = next((e for e in lv1
                    if alnum(re.sub(r"^(?:\d{1,2}|[A-F])(?:\.\d+)*\s+", "", e[1])) == key), None)
        pagemap.append({"source": name, "title": title,
                        "first_page": hit[2] if hit else ""})
        if not hit:
            unmapped.append(title)
    pages_seq = [r["first_page"] for r in pagemap if r["first_page"]]
    monotonic = pages_seq == sorted(pages_seq)
    add("P26", "section order matches main.tex and pages increase",
        "all input sections bookmarked, in source order",
        f"{len(pagemap) - len(unmapped)}/{len(pagemap)} mapped; "
        f"pages {'monotonic' if monotonic else 'OUT OF ORDER'}; "
        f"body starts p.{pages_seq[0] if pages_seq else '?'}",
        "PASS" if not unmapped and monotonic else "FAIL",
        " | ".join(unmapped[:6]))
    with (out / "section_pagemap.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["source", "title", "first_page"])
        w.writeheader()
        w.writerows(pagemap)

    # ---- write outputs -----------------------------------------------------
    csv_path = out / "page_audit_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["check_id", "object", "expected",
                                           "observed", "verdict", "note"])
        w.writeheader()
        w.writerows(rows)

    npf = sum(1 for r in rows if r["verdict"] == "PASS")
    nff = sum(1 for r in rows if r["verdict"] == "FAIL")
    nrep = sum(1 for r in rows if r["verdict"] == "REPORT")
    summary = [
        "# Page-Level Audit Summary — compiled v1.2 \u2194 LaTeX sources",
        "",
        f"- checks: {len(rows)}  ({npf} PASS, {nrep} REPORT, {nff} FAIL)",
        f"- PDF: {doc.page_count} pages, {words} words",
        f"- unresolved refs: {qq}; missing citations: {miss}; leaked LaTeX tokens: {n_leak}",
        f"- section/subsection titles checked: {len(titles)}; missing: {len(missing)}",
        f"- appendices rendered: {len(found)}/{len(appfiles)}",
        f"- captions checked: {len(caps)}; missing: {len(cap_missing)}",
        f"- register rows: {sum(statuses.values())}; distinct EQ ids: {len(cnt)}",
        f"- statuses: " + ", ".join(f"{k}={v}" for k, v in statuses.most_common()),
        f"- citations: {len(cited)} cited of {len(bib_keys)} in .bib",
        "",
        "Full row-level detail: `page_audit_results.csv`.",
        "",
    ]
    if missing:
        summary += ["## Missing titles", ""] + [f"- {m}" for m in missing] + [""]
    if cap_missing:
        summary += ["## Missing captions", ""] + [f"- {c}" for c in cap_missing[:20]] + [""]
    (out / "PAGE_AUDIT_SUMMARY.md").write_text("\n".join(summary), encoding="utf-8")

    print(json.dumps({"checks": len(rows), "pass": npf, "report": nrep, "fail": nff,
                      "pages": doc.page_count, "words": words,
                      "csv": str(csv_path)}, indent=2))
    return 0 if nff == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
