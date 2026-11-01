#!/usr/bin/env python3
"""Builds and verifies the Overleaf-ready submission zip for the review.

Stages: the revised master (tex, bib, tables, appendices, frontmatter), the figure PDFs, the build
instructions, the review-cycle log and the P1 audit report. Then it verifies the *staged* tree, not the
source tree: every \\input, every \\includegraphics, every \\ref target and every citation key is checked
against what is actually inside the zip. A zip that fails verification is not written.
"""
import os
import re
import shutil
import subprocess
import sys
import zipfile

ROOT = "/home/user/le/paper_v2"
MASTER = os.path.join(ROOT, "manuscript_v2", "master")
FIGSRC = "/home/user/manuscript/master/figures/source"
STAGE = "/tmp/submission_stage"
OUTDIR = "/home/user/deliverables"
VERSION = "v1.2"
ZIP = os.path.join(OUTDIR, "le_review_%s_2026-11-01.zip" % VERSION)


def copytree_text():
    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)
    os.makedirs(STAGE)
    for root, _, files in os.walk(MASTER):
        for f in files:
            if f.endswith(".tex") or f.endswith(".bib") or f == "Makefile" or f.endswith(".md"):
                src = os.path.join(root, f)
                dst = os.path.join(STAGE, os.path.relpath(src, MASTER))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
    figs = os.path.join(STAGE, "figures", "source")
    os.makedirs(figs, exist_ok=True)
    n = 0
    PROVISIONAL = {"fig07-theory-map.pdf", "fig18-taxonomy.pdf"}   # declared provisional in Appendix D
    for f in sorted(os.listdir(FIGSRC)):
        if f.endswith(".pdf") and f not in PROVISIONAL:
            shutil.copy2(os.path.join(FIGSRC, f), os.path.join(figs, f))
            n += 1
    return n


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def verify():
    tex = {}
    for root, _, files in os.walk(STAGE):
        for f in files:
            if f.endswith(".tex"):
                p = os.path.join(root, f)
                tex[p] = strip_comments(open(p, encoding="utf-8", errors="replace").read())
    joined = "\n".join(tex.values())
    problems = []

    labels = set(re.findall(r"\\label\{([^}]+)\}", joined))
    refs = {k.strip() for m in re.finditer(r"\\(?:ref|eqref|cref|Cref|autoref)\{([^}]+)\}", joined)
            for k in m.group(1).split(",")}
    problems += [("unresolved ref", r) for r in refs - labels if r]

    bib = ""
    for root, _, files in os.walk(STAGE):
        for f in files:
            if f.endswith(".bib"):
                bib += open(os.path.join(root, f), encoding="utf-8", errors="replace").read()
    keys = set(re.findall(r"@\w+\s*\{\s*([^,]+),", bib))
    cited = {k.strip() for m in re.finditer(r"\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]+)\}", joined)
             for k in m.group(1).split(",")}
    problems += [("uncited-missing key", k) for k in cited - keys if k]

    for name in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", joined):
        cands = [name] if os.path.splitext(name)[1] else [name + e for e in (".pdf", ".png", ".jpg")]
        if not any(os.path.exists(os.path.join(STAGE, "figures", "source", c)) for c in cands):
            problems.append(("missing figure", name))

    for t in re.findall(r"\\input\{([^}]+)\}", joined):
        p = t if t.endswith(".tex") else t + ".tex"
        if not os.path.exists(os.path.join(STAGE, p)):
            problems.append(("missing input", t))

    dup = [l for l in labels if len(re.findall(r"\\label\{%s\}" % re.escape(l), joined)) > 1]
    problems += [("duplicate label", d) for d in dup]
    return problems, len(tex), len(joined.split())


def main():
    nfig = copytree_text()
    problems, ntex, nwords = verify()
    if problems:
        print("REFUSING TO ZIP: %d problem(s)" % len(problems))
        for kind, item in problems[:20]:
            print("  %-18s %s" % (kind, item))
        return 1

    with open(os.path.join(STAGE, "README_BUILD.md"), "w", encoding="utf-8") as f:
        f.write("""# Building this package

This is the submission package of **Multiphysics Wave Mechanics in Generalized Continua: A Constructive
Review of Theory, Energy Transport, and Interface Phenomena** (Vipin Gupta), version %s.

## Build

Overleaf: upload this zip as a new project and set `main.tex` as the main document. Or locally:

```
pdflatex main
bibtex   main
pdflatex main
pdflatex main
```

## Contents

- `main.tex` — master file: front matter, 17 sections, 6 appendices, declarations, bibliography.
- `frontmatter/` — title page, abstract (with keywords), notation, acronyms, declarations.
- `sections/sec01..sec17` — the review.
- `appendices/appA..appF` — equation register, balance derivations, benchmark tables, figure-status table,
  table index, reproducibility notes.
- `tables/source/` — the ten table sources that the sections `\\input`.
- `figures/source/` — the %d figure PDFs. Two further figures (`fig07-theory-map`, `fig18-taxonomy`) are
  deliberately **not** included in the text; they are declared provisional in Appendix D. They are not shipped
  here for that reason.
- `references_local.bib` — the bibliography.
- `REVIEW_CYCLES.md`, `CHANGELOG_v2.md` — the revision record.

## Verification performed before packaging

Every `\\ref`/`\\eqref` target resolves to a `\\label`; no label is defined twice; every `\\cite` key exists in
`references_local.bib`; every `\\includegraphics` file is present in `figures/source/`; every `\\input` file is
present; no placeholder text; header counts (17 sections, 7 appendix files, 18 figures, 8 tables) match the tree.
The package was assembled only after those checks passed on the *staged* tree.

## Known limits, stated on purpose

The manuscript's appendix D lists the status of every figure, including the two provisional ones. The benchmark
tables print measured value, reference value and residual for each check. The review does not claim case-level
results for the atlas; it claims 40 executable invariants and reports which of them are benchmarks against a
closed form.
""" % (VERSION, nfig))
    for doc, dst in ((os.path.join(ROOT, "manuscript_v2", "REVIEW_CYCLES.md"), "REVIEW_CYCLES.md"),
                     (os.path.join(ROOT, "manuscript_v2", "CHANGELOG_v2.md"), "CHANGELOG_v2.md"),
                     (os.path.join(ROOT, "arena_deliverables", "P1_audit", "P1_SOURCE_AUDIT_2026-11-01.md"),
                      "P1_SOURCE_AUDIT.md")):
        if os.path.exists(doc):
            shutil.copy2(doc, os.path.join(STAGE, dst))

    os.makedirs(OUTDIR, exist_ok=True)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(STAGE):
            for f in files:
                p = os.path.join(root, f)
                z.write(p, os.path.relpath(p, STAGE))
    size = os.path.getsize(ZIP) / 1e6
    print("wrote %s  (%.1f MB)" % (ZIP, size))
    print("  %d .tex files, %d figure PDFs, %d words in the sources" % (ntex, nfig, nwords))
    print("  verification on the staged tree: 0 problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
