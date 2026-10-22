# Phase5 v1.1 source build and audit

## Source-of-truth and version provenance

- `phase4/manuscript/` is the inherited v1.0 source tree; it is preserved unchanged.
- `phase4/manuscript/main.pdf` and `phase5/master/v1.0-baseline.pdf` are byte-identical repository artifacts. Their embedded metadata reports **161 pages**, producer `pdfTeX-1.40.25`, and creation date 2023-11-14. This does not match the separately described 170-page/pdfTeX-1.40.29 attachment; no such attachment is present in this workspace, so its provenance and page-specific observations cannot be confirmed from the available files.
- `phase5/master/` is the editable v1.1 working copy. Its figures and tables are self-contained beneath that directory. `phase5/figures/source/` and `phase5/tables/source/` remain phase-level mirrors used by audits and scripts.
- `phase5/master/figures/rendered/` retains v1.0 SVG snapshots for comparison; despite the folder name these are SVG sources, not PDFs.

## Build figures

The manuscript includes PDF figures directly; there is no shell-escape conversion inside LaTeX.

```sh
cd phase5
npm ci --prefix tools --ignore-scripts
./scripts/build_figures.sh
```

This converts each `figures/source/*.svg` to a vector PDF in `master/figures/source/`, then mirrors the PDFs for workspace-level static checks. Conversion uses the pinned `pdfkit` and `svg-to-pdfkit` dependencies in `tools/package-lock.json`. The SVGs use DejaVu Sans; the script expects its TTF files at `/usr/share/fonts/truetype/dejavu/`.

The renderer currently reports zero unsupported-SVG warnings for the 18 source images. Every PDF has vector drawing operators and extracted text, and zero embedded raster images in the generated page objects. This is not a substitute for inspection at final manuscript size.

## Compile the master

From the repository root, install the pinned converter and symbolic-audit dependencies, then run the strict build:

```sh
npm ci --prefix phase5/tools --ignore-scripts
python3 -m pip install -r phase5/tools/requirements-audit.txt
bash phase5/scripts/build_master.sh
```

The script validates source paths and figures, rebuilds figure PDFs, cleans generated outputs, performs four fail-fast pdfLaTeX passes with an explicit BibTeX pass, checks the final log for errors/unresolved references/missing graphics and material overfull boxes, and records PDF metadata/fonts. It uses no suppressed errors. The project requires standard TeX Live packages for `article`, `natbib`, `hyperref`, `cleveref`, AMS math, `booktabs`, `tabularx`, `longtable`, `graphicx`, `caption`, `subcaption`, `enumitem`, `titlesec`, `setspace`, `xcolor`, `array`, `geometry`, and dependencies. No `draft` option is intentionally enabled.

Seven strict CI attempts (`39728213927`, `39728597464`, `39728900152`, `39729338751`, `39729569948`, `39729834892`, and `39730189442`) failed in the build step. The latest explicit pdfLaTeX/BibTeX run returned exit 1; annotations exposed unresolved citations/references in the final log check, but signed logs and its uploaded log artifact could not be downloaded to establish the bibliography/aux cause. Running BibTeX from the output directory was tried in the latest run and did not clear the warnings. Local TeX tools are absent, so no successful v1.1 compile is claimed. See `reports/build-status.md` for the current state.

## Static checks

```sh
python3 phase5/scripts/audit_inventory.py
python3 phase5/scripts/validate_figures.py
python3 -m pip install -r phase5/tools/requirements-audit.txt
python3 phase5/scripts/verify_classical_flux.py
```

These scans cover input/include paths, labels, cross-reference targets, bibliography keys/files, expected figure files, and SVG/PDF file-level properties. The SymPy script checks only the displayed classical symmetric-Cauchy power identity and stated units. None compiles TeX, establishes generalized-theory validity, or replaces visual proofing. See `phase5/reports/build-status.md`, `quality-gates.md`, and `scientific-audit.md` for limitations/open work.

## Journal wrapper

`journal/main.tex` and `journal/supplement.tex` are generic, non-journal-specific wrappers. They share the master sections; they are not certified as a submission package until the main build, cross-reference flow, scope/format choice, and supplement review are complete.
