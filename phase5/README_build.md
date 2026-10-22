# Phase5 v1.1 source build and audit

## Source-of-truth and version provenance

- `phase4/manuscript/` is the inherited v1.0 source tree; it is preserved unchanged.
- `phase4/manuscript/main.pdf` and `phase5/master/v1.0-baseline.pdf` are byte-identical repository artifacts. Their embedded metadata reports **161 pages**, producer `pdfTeX-1.40.25`, and creation date 2023-11-14. This does not match the separately described 170-page/pdfTeX-1.40.29 attachment; no such attachment is present in this workspace, so its provenance and page-specific observations cannot be confirmed from the available files.
- `phase5/master/` is the editable v1.1 working copy. Its figures and tables are self-contained beneath that directory. `phase5/figures/source/` and `phase5/tables/source/` remain phase-level mirrors used by audits and scripts.

## Build figures

The manuscript includes PDF figures directly; there is no shell-escape conversion inside LaTeX.

```sh
cd phase5
npm ci --prefix tools
./scripts/build_figures.sh
```

This converts each `figures/source/*.svg` to a vector PDF in `master/figures/source/`, then mirrors the PDFs for workspace-level static checks. Conversion uses the pinned `pdfkit` and `svg-to-pdfkit` dependencies in `tools/package-lock.json`. The SVGs use DejaVu Sans; the script currently expects its TTF files at `/usr/share/fonts/truetype/dejavu/`. If absent, install a compatible DejaVu Sans font and update the script's `fontDir`.

The renderer currently reports zero unsupported-SVG warnings for the 18 source images. Every PDF has vector drawing operators and extracted text, and zero embedded raster images in the generated page objects. This is not a substitute for inspection at final manuscript size.

## Compile the master

With TeX Live (pdfLaTeX, BibTeX, `latexmk`) installed:

```sh
cd phase5/master
latexmk -pdf -interaction=nonstopmode -file-line-error -halt-on-error -recorder main.tex
```

The project requires a standard TeX Live installation containing `article`, `natbib`, `hyperref`, `cleveref`, AMS math, `booktabs`, `tabularx`, `longtable`, `graphicx`, `caption`, `subcaption`, `enumitem`, `titlesec`, `setspace`, `xcolor`, `array`, `geometry`, and their dependencies. No `draft` option is intentionally enabled. Exact package versions must be recorded from the build host; the current sandbox has no TeX engine or `latexmk`, so no v1.1 compile result is claimed.

## Static checks performed

```sh
python3 scripts/audit_inventory.py
python3 scripts/validate_figures.py
python3 scripts/verify_classical_flux.py  # after installing tools/requirements-audit.txt
```

The inventory and figure scripts check labels, cross-reference targets, bibliography keys, expected figure files, and SVG/PDF file-level properties. The SymPy script checks only the displayed classical symmetric-Cauchy power identity and its stated units; install its pinned dependency with `python3 -m pip install -r tools/requirements-audit.txt`. None of these checks compiles TeX, establishes generalized-theory validity, or replaces visual proofing. See `reports/build-status.md`, `reports/quality-gates.md`, and `reports/scientific-audit.md` for executed checks, limitations, and open work.

## Journal wrapper

`journal/main.tex` and `journal/supplement.tex` are generic, non-journal-specific wrappers. They share the master sections; they are not certified as a submission package until the main build, cross-reference flow, scope/format choice, and supplement review are complete.
