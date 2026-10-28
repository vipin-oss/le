# Archive policy

`archive/` holds superseded project phases, old source-only bundles, and pre-existing recovery/checkpoint records. It is retained for provenance, not as an active working tree.

- [`INDEX.csv`](INDEX.csv) lists every file moved here, its former and current path, a short description, and its status (`CURRENT`, `SUPERSEDED`, or `ARCHIVE-ONLY`). The present inventory has 105 moved files: 82 `SUPERSEDED`, 23 `ARCHIVE-ONLY`, and 0 `CURRENT` (the latter is expected because this folder is an archive).
- [`EXCLUDED_SOURCE_TEXTS.csv`](EXCLUDED_SOURCE_TEXTS.csv) has 102 path-only disposition records: 51 standalone third-party full-text files removed from Git and their 51 duplicate members removed from the legacy v1.0 ZIP. No extracted article text is retained in the table or sanitized bundle.
- `recovery/` is archived without using it to restore or reconstruct the unavailable 24–25 October work. See the root [`KNOWN_LOSSES.md`](../KNOWN_LOSSES.md).
- `phase0/`, `phase1/`, `phase2/`, and `phase3/` are historical project stages. The bundles under `deliverables/` are superseded archival packages, not current releases. The v1.0 legacy ZIP was sanitized by removing its 51 embedded extracted-text copies; it is not a byte-identical snapshot. Remaining PDFs in the bundles are project-generated manuscript or figure outputs, not publisher papers.

Archive presence is not evidence that a claim or source was checked. Use `phase5/reports/OPEN_CLAIMS_LEDGER.csv` for current open claims and `phase5/reports/R4A_DELETION_AUDIT.csv` for removed text.
