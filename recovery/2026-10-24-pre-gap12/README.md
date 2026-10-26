# Recovered pre-GAP-12 backup snapshot

This directory contains **copies only** of selected artifacts from the user-owned Google Drive folder `[REDACTED: private storage reference]` ([REDACTED: private storage reference], created 2026-10-24T14:32:22.789Z). The folder description states that it is a secondary backup of pre-GAP-12 local-only evidence files and archive-verification metadata, with original repository files copied rather than modified.

The copies are deliberately kept under `recovery/2026-10-24-pre-gap12/`, not restored over active paths. The embedded `critical_manifest.csv` and Drive checksums were verified against the recovered bytes. The map is an older R3B snapshot, not the current R3F map or the later 96-claim matrix; it must not be used to infer current claim status or overwrite a protected map.

## Included

- `phase5/reports/R3B_CITATION_MAP.csv` — backup copy of the local-only R3B citation map; size 27,190 bytes; SHA-256 `8644c294505f380a3506c97cf7f8c5ca9e345081ec0ca05d70d447dff7571b96`.
- `phase5/references/source_provenance.csv` — source provenance snapshot; size 2,896 bytes; SHA-256 `6c9c8e18d9fccf46660d76fc0198bdcf2cbd87d507b24eb2285181e14a09a63c`.
- `[REDACTED: private storage reference]` — primary-source PDF recorded by the backup manifest; size 417,924 bytes; SHA-256 `2fb87be7850bf6e3b3c56e2e75d6207719684c9b73f31b513b6590ead67c30c2`.
- `critical_manifest.csv`, `branch-file-classification.csv`, `le-working-state-manifest.csv`, and their SHA-256 records. The working-state manifest contains 1,307 unique paths and describes a 2026-10-24 pre-GAP-12 state.

## Missing full snapshot

The backup records the full archive as `[REDACTED: private storage reference]` with expected SHA-256 `8bff8a6c9c4a5e6b5e45921b7e4f4640f77c9c882b0c707e7287da5a11412cdc`. The Drive folder's metadata says that archive exceeded the connector's 100 MB direct-upload limit and was not included. The recorded local path is absent in this environment. This historical archive is not a substitute for the current post-GAP-12/R3F project package.

A separate user-owned Drive file `R3.zip` ([REDACTED: private storage reference]) was inventoried and its CRCs and Drive checksums verified. It contains 20 PDFs only; it is a source collection, not the manuscript, claim matrix, scripts, tests, or control records. No files were extracted from it.
