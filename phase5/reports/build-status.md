# Build forensics and engineering status — phase5 v1.1

## Source inventory and PDF provenance

- The inherited source is `phase4/manuscript/main.tex`; it includes section files from `phase4/manuscript/` and table inputs at `../tables/source/`. It was not self-contained for upload as a manuscript folder.
- The editable, versioned repair is `phase5/master/main.tex`. Figure PDFs and editable SVGs now live inside `phase5/master/figures/source/`; eight editable table files are mirrored inside `phase5/master/tables/source/`, and section inputs use `tables/source/...`.
- `phase4/manuscript/main.pdf` and `phase5/master/v1.0-baseline.pdf` are byte-identical (SHA-256 `b03dc426046a1473d3d6cf1088f9fc115c7103b4786c4eb2389ab968f640c636`). PyMuPDF reports 161 pages, producer `pdfTeX-1.40.25`, and timestamp `2023-11-14T22:13:20Z`. The fixed timestamp in the repository CI workflow is `SOURCE_DATE_EPOCH=1700000000`, so the embedded creation date is not the actual CI build date. The tracked PDF was published in commit `00908ce` (“build 32”).
- CI run `39654760555` is associated by the committed diagnostics with TeX Live 2023; the GitHub API reports its source commit as `d4a9dafc79149455e7008845dc2a5a759dca3e10`. The latest diagnostics commit references successful CI run `39716768990`. The tracked baseline copy in this workspace is **161 pages and contains rendered figures** in the page-thumbnail survey; it is not the separately described 170-page/pdfTeX-1.40.29 attachment. That attachment was not available locally, so its build root, missing-file boxes, and exact page symptoms cannot be directly reproduced or disputed against the attached file.
- A 161-page thumbnail survey was rendered from the tracked baseline PDF into `reports/v1.0-thumbnails/`; all sheets were reviewed. No blank/near-blank page was identified at thumbnail scale. Tables near pages 145–161 show visibly narrow, fragmented, or overlong content and require source/layout remediation. This is review of the repository baseline, not a proof of v1.1.

## Phase5 figure build executed

- Installed the pinned `pdfkit@0.20.2` and `svg-to-pdfkit@0.1.8` packages from npm for the local conversion.
- Ran `./phase5/scripts/build_figures.sh`: **18 SVGs converted to PDFs, zero renderer warnings**. The generated single-page PDFs are in `master/figures/source/`; mirrored assets are in `figures/source/`.
- `python3 phase5/scripts/validate_figures.py`: **18/18 included PDFs present; 18/18 corresponding SVGs parse as XML**.
- PyMuPDF structural inspection: all 18 PDFs have extractable text and vector drawing operators; the PDF pages report zero raster image XObjects. A contact sheet is at `reports/figure-contact-sheet.png`, with inspection details in `reports/figure-render-inspection.txt`. This does not prove text legibility at the final manuscript scale or scientific correctness.

## Static source checks executed

Latest `python3 phase5/scripts/audit_inventory.py` result: **37 TeX files; 430 labels; 297 reference commands; 56 bibliography keys; 222 citation calls; 0 malformed truncated ref commands; 0 unescaped underscores in `\\texttt` paths; 0 duplicate labels; 0 duplicate bibliography keys; 0 missing reference labels; 0 missing citation keys; 0 missing input/include files; 0 missing bibliography files; 0 missing PDF figure assets.** This is a source scan, not a TeX/BibTeX build. The inherited literature inventory contains 95 rows, including 47 blank DOI cells; no claim-level literature audit is implied.

## Compile status and blocker

**No successful phase5 LaTeX build or final PDF exists.** Locally, `bash phase5/scripts/build_master.sh` exits 127 at its prerequisite check because `latexmk` is absent; `pdflatex`, `bibtex`, `tectonic`, `rsvg-convert`, and Inkscape are also absent. A Tectonic release download redirected to `objects.githubusercontent.com`, outside the sandbox's permitted outbound hosts.

Nine strict phase5 GitHub attempts—runs `39728213927` (`f8d41ea`), `39728597464` (`97c108c`), `39728900152` (`0af5998`), `39729338751` (`cfe3ab6`), `39729569948` (`c185ce8`), `39729834892` (`88e5b2d`), `39730189442` (`5f7943a`), `39730441139` (`55fd121`), and `39730774923` (`de4b1da`)—**failed** (first three exit 12; last six exit 1). Earlier runs emitted undefined citation/reference warnings, but those were not from a confirmed final pass. The latest run's consolidated log annotation shows pdfLaTeX pass 1 stopped at `phase5/master/sections/sec04_thermoelastic.tex:17` with `Missing $ inserted`; the source line had a truncated `ef{fig:theory_evolution}` instead of `\ref{...}`. Static scanning then found three more truncated references in `sec17_conclusions.tex:49`, `sec15_challenges.tex:360`, and `sec16_future.tex:325`. Because pass 1 halted, BibTeX, later TeX passes, and the final log gate did not run. All four references have been repaired, and the static inventory now detects this fragment; the repairs have not yet been built. The latest failed job uploaded a build-log artifact, but signed logs/artifact downloads returned EOF. PDF upload was skipped; no successful v1.1 PDF exists. A local smoke test exercised the EXIT diagnostic on missing `latexmk` (expected exit 127). No final log, page count, verified font-embedding report, overfull-box report, or Overleaf-default result is available.

The inherited GitHub workflow used `|| true` around conversion and LaTeX steps and built `phase4/manuscript`; its earlier green status is not evidence for v1.1. The replacement targets phase5 and does not suppress command failures. Its first phase5 CI attempt failed; engineering build remains NOT PASSED.

## Current release gate

- Figure source and PDF assets: **generated and structurally checked; final-size visual proof pending**.
- Master source/table portability: **source paths repaired; no compile proof**.
- Engineering build: **NOT PASSED**.
- Scientific audit: **PARTIAL; primary-source claim checks and theory-specific energy identities remain open**.
- Editorial/journal readiness: **NOT PASSED**.
- `phase5-v1.1-source-audit.zip`: refreshed from the current phase5 tree; ZIP integrity check passed. It contains no compiled v1.1 PDF.
