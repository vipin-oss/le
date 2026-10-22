# Phase5 v1.1 scientific-review audit workspace

Versioned working copy of the manuscript. This is **not** a release or submission package. The phase4 source and tracked baseline PDF remain preserved; provenance and the 161-page vs reported 170-page artifact discrepancy are documented in `reports/version-provenance.md`.

## Contents

- `master/` — revised LaTeX source, v1.0 baseline PDF, local bibliography, build configuration, figures, and portable table inputs.
- `tables/source/` — editable table sources mirrored into the master package.
- `figures/source/` — 18 editable SVG figures and 18 generated vector PDFs.
- `journal/` — generic article/supplement wrappers; not tied to a named journal and not compiled.
- `references/`, `literature/` — inherited provenance/verification records, 95-item inventory, and search/extraction notes; not a new systematic search.
- `scripts/` — conversion, inventory, figure validation, build and log-check scripts.
- `reports/` — provenance, audit, literature/equation/figure registers, PDF thumbnails, and separate quality gates.

## Status summary

**Not built; not scientifically verified as a whole; not submission-ready.** The 18 SVG-to-PDF conversions and static source scans passed. The available 161-page v1.0 PDF was surveyed at thumbnail scale; it is not the separately described 170-page artifact and is not a rendering of v1.1. Local `pdflatex`/`latexmk` are unavailable, so there is no phase5 PDF, final TeX log, page count, or final visual proof. The classical local energy density and outward-positive flux were re-derived under stated assumptions. Other model-family claims are explicitly conditional, unverified, or open; see `reports/scientific-audit.md` and `reports/equation-audit.csv`.

See `reports/build-status.md`, `reports/quality-gates.md`, and `reports/version-provenance.md` before using or packaging any artifact. Do not describe this workspace as a completed audit or final review.
