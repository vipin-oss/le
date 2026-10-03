# Phase 10 changelog

- `verification/make_tex_figure_set.py`: materialises `13_Manuscript/figures/` (eight vector PDFs
  + README) from the Phase 9 renditions, regenerating them through the exporter if absent;
  verifies the names match the manuscript and prints per-file sha256.
- `tools/md_to_tex.py`: `\graphicspath{{figures/}}` in both preambles and extensionless
  `\includegraphics` names when the vector set is present, with automatic fallback to the
  `../11_Figures/*.png` paths when it is not (fallback exercised and verified).
- `tools/audit_tex.py`: figure existence now resolves `\graphicspath` directories and image
  extensions, and reports how many figures come from the vector set; a consistency check refuses
  a mixed vector/PNG figure list.
- `verification/make_cover_letter_package.py`: `cover_letter.docx` + `cover_letter.pdf` rendered
  from `13_Manuscript/cover_letter.md` at run time (no duplicated prose), author-input brackets
  bolded.
- `compile_check.sh`: author-side TeX Live compile + log triage into `COMPILE_CHECK.txt`, with a
  no-engine path that prints the commands and the headless static gates.
- Deposit package rebuilt: `RESEARCH_PROJECT_FINAL.zip` 603 files / 43,645,185 B (~46.6 MB unpacked) with MANIFEST.json,
  now containing the figure set, the 03j freeze and the cover letter.
- No builder or frozen source touched: the code freeze remains `submission_2026_10_03j` and the
  Markdown, .docx and preview PDFs were not rebuilt; only the two `.tex` files changed.

- `verification/make_upload_bundle.py` + `IJHMT_submission_bundle.zip` (2.62 MB, 29 entries, MANIFEST.json with a per-file SHA-256 for all 28 content files, deterministic rebuild, CRC-clean and hash-verified after building) - the upload set plus provenance in one downloadable file; the ~43.6 MB deposit package stays gitignored and is rebuilt with `make_packages.py final`.
