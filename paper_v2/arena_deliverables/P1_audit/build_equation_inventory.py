#!/usr/bin/env python3
"""Build a complete inventory of the numbered equations, and measure how far the
Appendix-A register can be tied back to them.

Two questions, both factual:

1. *Inventory.* Every numbered equation the manuscript prints, in print order, with
   its label, its section and the file it lives in. If the count of `equation`
   environments in `\\input` order does not equal the highest printed equation number
   in the compiled PDF, something is wrong and this script says so.

2. *Linkage.* Each Appendix-A register row is matched to the printed equation(s) whose
   content contains the row's own mathematics. The result is reported as
   `unique` / `multiple` / `none` — the register is **not** edited here, because which
   row means which printed equation is the author's call, and a wrong pointer is worse
   than an absent one.

Outputs (in --out):
    equation_inventory.csv   printed,label,section,subsection,file
    register_linkage.csv     eq_id,status,candidates,pointer_status,register_math

Usage:  python3 P1_audit/build_equation_inventory.py [--master ../manuscript_v2/master]
        [--pdf /path/to/compiled.pdf] [--out P1_audit]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

STATUS_RE = re.compile(r"\s*(EQ-\d{3})\s*&(.*?)&\s*([A-Z][A-Z-]+)\s*&(.*)$")


def strip_comments(src: str) -> str:
    return "\n".join(l for l in src.splitlines() if not l.lstrip().startswith("%"))


def tex_to_text(s: str) -> str:
    s = re.sub(r"\\[a-zA-Z]+\*?", "", s)
    return re.sub(r"\s+", " ", s.replace("{", "").replace("}", "")).strip()


def norm_math(s: str) -> str:
    s = s.replace("\\left", "").replace("\\right", "")
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\\(displaystyle|textstyle|big|Big|bigg|Bigg|,|;|:|!|quad|qquad)", "", s)
    return re.sub(r"[\s{}]", "", s)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--master", default="../manuscript_v2/master")
    ap.add_argument("--pdf", default="")
    ap.add_argument("--out", default="P1_audit")
    a = ap.parse_args()
    master, out = Path(a.master), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    main_tex = (master / "main.tex").read_text(encoding="utf-8")
    order = [f if f.endswith(".tex") else f + ".tex"
             for f in re.findall(r"\\input\{([^}]+)\}", main_tex)]

    inventory, n = [], 0
    bodies: list[tuple[str, str]] = []  # (label, normalised math)
    for f in order:
        p = master / f
        if not p.exists():
            continue
        src = strip_comments(p.read_text(encoding="utf-8", errors="replace"))
        sec = re.search(r"\\section\*?\{", src)
        cur_sec = tex_to_text(src[sec.end():src.index("}", sec.end())]) if sec else ""
        for m in re.finditer(r"\\begin\{equation\}(.*?)\\end\{equation\}", src, re.S):
            body = m.group(1)
            labels = re.findall(r"\\label\{([^}]+)\}", body)
            label = labels[0] if labels else ""
            before = src[:m.start()]
            subs = list(re.finditer(r"\\subsection\*?\{([^}]*)\}", before))
            n += 1
            inventory.append({"printed": n, "label": label, "section": cur_sec,
                              "subsection": tex_to_text(subs[-1].group(1)) if subs else "",
                              "file": f})
            bodies.append((label, norm_math(body)))

    with (out / "equation_inventory.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["printed", "label", "section", "subsection", "file"])
        w.writeheader()
        w.writerows(inventory)

    # ---- cross-check against the compiled PDF --------------------------------
    pdf_max = pdf_distinct = None
    if a.pdf:
        try:
            import pymupdf
            doc = pymupdf.open(a.pdf)
            nums = set()
            for i in range(doc.page_count):
                for mm in re.finditer(r"\((\d{1,3})\)\s*$", doc[i].get_text(), re.M):
                    nums.add(int(mm.group(1)))
            pdf_max, pdf_distinct = (max(nums) if nums else 0), len(nums)
        except Exception as exc:  # noqa: BLE001
            print(f"warning: PDF not read ({exc})")

    mismatch = [r for r in inventory if not r["label"]]
    print(f"numbered equations in sources: {len(inventory)}; without a \\label: {len(mismatch)}")
    if pdf_max is not None:
        ok = pdf_max == len(inventory) == pdf_distinct
        print(f"compiled PDF: highest number {pdf_max}, distinct numbers {pdf_distinct} "
              f"-> {'MATCH' if ok else 'MISMATCH'}")
        if not ok:
            print("MISMATCH: the source inventory and the printed numbering disagree", file=sys.stderr)

    # ---- register linkage ----------------------------------------------------
    reg = (master / "appendices" / "appA_equation_register.tex").read_text(encoding="utf-8")
    links = []
    for line in reg.splitlines():
        m = STATUS_RE.match(line)
        if not m:
            continue
        eq_id, cell, status = m.group(1), m.group(2), m.group(3)
        maths = [x for x in re.findall(r"\$([^$]+)\$", cell) if len(norm_math(x)) > 10]
        hits: set[str] = set()
        for snippet in maths:
            k = norm_math(snippet)
            for label, txt in bodies:
                if k and k in txt:
                    hits.add(label or "?")
        main_text_hits = {h for h in hits if not h.startswith("appB")}
        if len(hits) == 1:
            pointer = "unique"
        elif len(main_text_hits) == 1:
            pointer = "unique-in-main-text"
        elif hits:
            pointer = "multiple"
        else:
            pointer = "none"
        ptr = re.search(r"\\eqref\{([^}]+)\}", cell)
        links.append({"eq_id": eq_id, "status": status, "pointer": ptr.group(1) if ptr else "",
                      "candidates": ";".join(sorted(hits)),
                      "pointer_status": pointer,
                      "register_math": "; ".join(maths)[:120]})

    with (out / "register_linkage.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["eq_id", "status", "pointer", "candidates",
                                           "pointer_status", "register_math"])
        w.writeheader()
        w.writerows(links)

    tally: dict[str, int] = {}
    for r in links:
        tally[r["pointer_status"]] = tally.get(r["pointer_status"], 0) + 1
    pointed = [r for r in links if r["pointer"]]
    print(f"register rows carrying an \\eqref pointer: {len(pointed)}")
    print(f"register rows: {len(links)}; linkage: "
          + ", ".join(f"{k}={v}" for k, v in sorted(tally.items())))
    print(f"wrote {out/'equation_inventory.csv'} and {out/'register_linkage.csv'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
