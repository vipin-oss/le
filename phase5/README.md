# Phase 5 — active review manuscript

`phase5/` is the current working copy for **“Multiphysics Wave Mechanics in Generalized Continua.”** It is a review-manuscript draft, not a published or fully scientifically certified review.

## Status

- Manuscript/source build validation: [CI run 40435990048](https://github.com/vipin-oss/le/actions/runs/40435990048), successful; 130 PDF pages for source commit `893c46f` (2026-10-27). The workflow-published PDF/contact sheets are in output commit `b4257e0`.
- Engineering gates: zero undefined references/citations, zero overfull boxes above 1 pt, zero near-overfull boxes above 0.5 pt, and zero forbidden process-tag or privacy-token matches. The font and build checks also passed.
- Build output: [`build_outputs/phase5-v1.1-master.pdf`](build_outputs/phase5-v1.1-master.pdf); overview contact sheets are in [`build_outputs/contact-sheets/`](build_outputs/contact-sheets/).
- Scientific status: the classical local energy density and outward-positive flux have been derived and symbolically checked under stated assumptions. Sections 5 and 7 received targeted source passes; Section 7 OCL-256/-257/-258/-260/-261 are Class A and OCL-259 remains title-level only. Section 5 void, micropolar, and interface-study claims remain open. See the open-claim ledger, `R4B_SOURCE_FINDINGS.md`, `MISSING_SOURCES.csv`, and [reports README](reports/README.md).
- Submission readiness: **not passed**. Claim-level primary-source review, some model-specific derivations, figure source/licensing checks, and final-size proofreading remain open.

The 130-page count is an engineering build result, not a measure of scientific completeness.

## Contents

| Path | Purpose |
|---|---|
| `master/` | Active LaTeX source, section files, editable tables, local bibliography, and current figure assets. Entry point: `master/main.tex`. |
| `figures/source/` | Phase5 SVG figure sources and their generated vector PDFs. |
| `tables/source/` | Editable table sources used by the master. |
| `scripts/` | Inventory, figure validation, build, PDF/font, and strict log-gate scripts. |
| `tools/` | Pinned Node renderer dependencies and Python audit requirements. |
| `reports/` | Current authoritative claim/deletion ledgers, build status, and historical evidence reports. Start with `reports/README.md`. |
| `literature/` | Literature inventory and authored review summaries; not publisher full text. |
| `journal/` | Generic, uncompiled journal/supplement wrappers. |
| `exports/` | Notes about archived source-only packages; current generated build outputs are under `build_outputs/`. |
| `build_outputs/` | CI-published manuscript PDF and contact sheets. |

`phase4/` remains as a read-only v1.0 baseline and literature inventory used by phase5 audit/reconciliation scripts. It is not the active manuscript. Third-party full-text extraction files have been removed; their path-only exclusion record is `archive/EXCLUDED_SOURCE_TEXTS.csv`.

## Build

CI is defined by [`.github/workflows/latex-build.yml`](../.github/workflows/latex-build.yml). It uses a prebuilt TeX Live container; pushes to `arena/**`, pull requests targeting `main`, and manual workflow dispatches run the strict build.

For a local Linux build, install complete TeX Live (`latexmk`, `pdflatex`, `bibtex`, `pdffonts`), Python 3 with `venv`, Node.js 20/npm, Poppler utilities, and DejaVu fonts. From the repository root:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r phase5/tools/requirements-audit.txt
npm ci --prefix phase5/tools
bash phase5/scripts/build_master.sh
```

The output and logs are written under `phase5/master/build/`. A green engineering build does not verify every scientific claim.

## Which records are authoritative

- [`reports/OPEN_CLAIMS_LEDGER.csv`](reports/OPEN_CLAIMS_LEDGER.csv) — authoritative current register of open claims (445 rows: A=25, B=124, C=296).
- [`reports/R4A_DELETION_AUDIT.csv`](reports/R4A_DELETION_AUDIT.csv) — authoritative current record of removed text (593 rows, zero `NONE` identifiers).
- [`reports/build-status.md`](reports/build-status.md) — current engineering-build status. Older status, page-reconciliation, and Crossref files are historical snapshots; see [`reports/README.md`](reports/README.md).
