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
- Deposit package rebuilt: `RESEARCH_PROJECT_FINAL.zip` (603 files, 43,645,185 B, ~46.6 MB unpacked) with
  `MANIFEST.json`, now containing the figure set, the 03j freeze and the cover letter.
- No builder or frozen source touched: the code freeze remains `submission_2026_10_03j` and the
  Markdown, .docx and preview PDFs were not rebuilt; only the two `.tex` files changed.

- `verification/make_upload_bundle.py` + `IJHMT_submission_bundle.zip` (2.62 MB, 29 entries, MANIFEST.json with a per-file SHA-256 for all 28 content files, deterministic rebuild, CRC-clean and hash-verified after building) - the upload set plus provenance in one downloadable file; the ~43.6 MB deposit package stays gitignored and is rebuilt with `make_packages.py final`.

- Made the deposit archive reproducible and closed a manifest gap (2026-10-03, after a workspace reset
  wiped the sandbox that had been serving the download links). `make_packages.py` stamped every entry with
  its on-disk mtime and put a live clock in `MANIFEST.json`, so `RESEARCH_PROJECT_FINAL.zip` hashed
  differently on each build and the sha256 the repo recorded could not be reproduced by anyone; an
  intermediate revision embedded `git HEAD`, which made the hash depend on the commit you stood on rather
  than the bytes you packaged. Both are gone - fixed `ZipInfo` stamps, permissions and compression, no
  clock inside the archive. Recorded hash `de9cfb1a4369c444...` (603 files, 43,645,185 B), reproduced
  unchanged after the commit that introduced it and across an mtime churn of the manuscript and analysis
  trees, with the archive's own manifest re-hashing 603/603 and `testzip()` clean. In the upload bundle,
  `PROVENANCE/README.txt` was written into the archive but never hashed, so `MANIFEST.json` silently
  omitted a file it claimed to cover; it is now covered (28 of 29 entries - the manifest excluding itself
  by construction), the bundle is 2,619,672 B, sha256 `7c50cadd6483437a...`, byte-identical across
  rebuilds. An earlier revision of the sidecar also carried blank hash fields from a bad `cut`
  invocation, fixed in the same pass, and the superseded hashes are listed in the sidecar with the reason
  each differs rather than deleted. No manuscript, figure, table or builder output changed; the `03j`
  freeze is untouched.
