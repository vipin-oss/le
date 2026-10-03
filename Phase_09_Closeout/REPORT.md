# Phase 9 - closeout: submission-grade artwork and the deposit package

The 8-phase programme ended at Phase 8 with everything machine-checked except two items this
environment had marked "cannot be done here". Both are agent-doable after all, so this phase
closes them; nothing else changed, and no document was rebuilt because no builder was touched.

## 1. Artwork above the journal's resolution floor

`08_Experiments/make_figures.py` - a frozen file, one of the 27 in the code freeze, and the
script that produced the figures the paper's numbers were read from - saves at
`savefig.dpi = 200`. IJHMT asks for half-tone artwork at 300 dpi or better, so the figures were
below what the submission system wants.

The frozen script was **not edited**: its bytes are the provenance of the reported figures.
`verification/export_submission_figures.py` instead runs it with `Figure.savefig` wrapped, so
each of the eight figures is additionally written to `PAPER_PROJECT/11_Figures/submission/` as

* `figN.png` and `figN.tiff` at **600 dpi** (TIFF LZW-compressed; 0.7-1.4 MB each), and
* `figN.pdf` as **vector** output (17-31 KB each).

Because matplotlib re-renders rather than upscales, the 600-dpi files are genuine 600-dpi
artwork, not an interpolation of the 200-dpi PNGs. The script reads the dpi back out of each
file's PNG `pHYs` chunk and TIFF IFD rather than trusting its own settings, and prints
`RESULT: OK - every raster rendition is >= 300 dpi and all three formats exist for every figure`.

The generator writes its own PNGs into `11_Figures/` as it always does, so the phase restores
that directory from git afterwards and re-verifies the hashes: **the frozen 200-dpi figures are
byte-identical**, `git diff HEAD -- PAPER_PROJECT/11_Figures` is empty, the manuscript and its
33-page PDF still embed the originals, and `tools/verify_pdf.py` passes for both documents
without a rebuild. `13_Manuscript` was not rebuilt, so the code freeze stays valid and no new
manifest was needed.

Tracked: the eight vector PDFs and `submission/README.txt`. The raster renditions are
gitignored (~11 MB together) and regenerate with one command, recorded in `.gitignore`.

## 2. The deposit package now exists

`00_Project_Control/README`/"Start here" pointed at `PAPER_PROJECT/packages/*.zip`, which are
gitignored and had never been built here - `tools/connection_audit.py` failed on it. Rebuilt with
the project's own tool (`python3 PAPER_PROJECT/00_Project_Control/make_packages.py final`):

    PACKAGE_PHASE_09..13.zip, RESEARCH_PROJECT_FINAL.zip  - 610 files, 52.2 MB
    each zip carries MANIFEST.json with a SHA-256 per file

`RESEARCH_PROJECT_FINAL.zip` is the concrete object to hand to Zenodo/Figshare for the DOI that
the Data availability statement still shows as `[PUBLIC REPOSITORY/DOI TO BE INSERTED]`. It is
cumulative (phases <= 13 reconstructed from the files as they now stand), so it contains the
manuscript sources, the verification suite and its results, the raw per-run outputs, the figures
and this phase's artwork renditions; the deposit manifest inside it is
`06_Source_Code/CODE_FREEZE_submission_2026_10_03j.json`.

## Gates after the phase

`tools/audit_tex.py` ALL CHECKS PASSED; `tools/check_crossrefs.py` all resolve;
`tools/check_tex_commands.py` ALL DEFINED; `tools/verify_pdf.py` ALL CHECKS PASSED for the
manuscript and (`-c`) the companion; `tools/connection_audit.py` green apart from the
working-tree check, which the phase commit clears. `Phase_08_Final_Audit/verification/final_consistency.py`
still reports 0 failures.

## Still author-only, unchanged from Phase 8

author identity/ORCIDs, funding, competing interest, CRediT, the repository DOI (the package to
mint it from now exists), confirmation of the AI declaration, a real `pdflatex` compile of the
two `.tex` files, and the expert read of the formulation. The open literature item P5-1
(Cattaneo 1948 / Vernotte 1958 primary sourcing) stays with the authors and is disclosed in the
cover letter.
