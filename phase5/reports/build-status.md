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

Latest `python3 phase5/scripts/audit_inventory.py` result: **37 TeX files; 431 labels; 308 reference commands; 56 bibliography keys; 222 citation calls; 0 malformed truncated ref commands; 0 unescaped underscores in `\texttt` paths; 0 stray single Markdown-style backticks; 0 duplicate labels; 0 duplicate bibliography keys; 0 missing reference labels; 0 missing citation keys; 0 missing input/include files; 0 missing bibliography files; 0 missing PDF figure assets.** This is a source scan, not a TeX/BibTeX build. The inherited literature inventory contains 95 rows, including 47 blank DOI cells; no claim-level literature audit is implied.

## Compile status and blocker

**Strict build: PASSED in CI. Final PDF visual/page-level review: OPEN.** Local `bash phase5/scripts/build_master.sh` remains unavailable because TeX tools (including `latexmk`) are not installed; the strict GitHub workflow is the execution evidence.

The first 22 strict phase5 CI attempts failed (the first three with exit 12; subsequent attempts with exit 1). The latest attempt, run `39748215109` on commit `5df59c6d4d6d3eb0915d8fbc47fc2302cc330604`, completed successfully. The unchanged strict gate passed after targeted repairs to the section/table locations reported in earlier runs; no gate threshold was weakened. CI generated a **146-page** PDF, passed the required PDF-font check (the preceding detailed check reported all 77 resources embedded), rendered contact sheets, and uploaded the PDF/build-report artifact (`12412533778`, 6,022,695 bytes) and log artifact (`12412533786`, 134,570 bytes). The PDF metadata annotation reports `Pages=146`. PDF and contact-sheet archive contents remain unavailable locally because artifact download returns EOF, so no final visual inspection is claimed.

Detailed warning inventory from run `39745464117` reported zero duplicate `page.1` destinations, zero PDF-string token warnings, zero `[h]` float warnings, 416 underfull hboxes, and zero underfull vboxes. Run `39741493145` had reported 412 underfull hboxes. The exact underfull count from the latest successful run is not locally accessible; underfull warnings remain for justified review, without global suppression. `DEFECT_STATUS.csv` records resolved build defects and open visual/page-level review findings.

The inherited GitHub workflow used `|| true` around conversion and LaTeX steps and built `phase4/manuscript`; its earlier green status is not evidence for v1.1. The replacement targets phase5 and does not suppress command failures. Early phase5 CI attempts failed; the latest strict phase5 run `39748215109` passed.

## Current release gate

- Figure source and PDF assets: **generated and structurally checked; final-size visual proof pending**.
- Master source/table portability: **source paths repaired and strict CI build passed**.
- Engineering strict build: **PASSED (run 39748215109); overall R1 gate remains OPEN pending visual/page-level review and underfull-warning disposition**.
- Scientific audit: **PARTIAL; primary-source claim checks and theory-specific energy identities remain open**.
- Editorial/journal readiness: **NOT PASSED**.
- `phase5-v1.1-source-audit.zip`: refreshed from the current phase5 tree; ZIP integrity check passed. It contains no compiled v1.1 PDF.
