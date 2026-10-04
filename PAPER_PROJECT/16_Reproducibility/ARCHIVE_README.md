# ARCHIVE_README - PAPER_PROJECT COMPLETE REPRODUCIBILITY ARCHIVE

Built 2026-10-04 from `arena/01a10176-le` at commit `acad8489707f667660d9ee9af5ce240b2543c3b7`, code freeze `submission_2026_10_03j`.
**1245 files.** Everything needed to understand, run, audit, modify and re-submit the paper is
inside this archive; the conversation and tooling that produced it are not needed and are not
referenced by any file as a source of truth.

## Structure

| folder | what is in it | start reading at |
|---|---|---|
| `01_PROGRAM/` | solver, experiment drivers, tests, builders, utilities, code freezes, the as-received baseline, environment files | `README_PROGRAM.md` |
| `02_OVERLEAF/` | manuscript `.tex`, companion `.tex`, `.bib`, vector figures, highlights | `README_OVERLEAF.md` |
| `03_DATA/` | raw per-run data (JSON + NPZ), processed analyses, CSV tables, provenance | `README_DATA.md`, then `DATA_DICTIONARY.md` |
| `04_REPRODUCTION/` | the reproduction test, verification-suite results and reports | `REPRODUCTION_TEST_REPORT.md` |
| `05_DERIVATIONS/` | formulation, numerical method, stability, convergence, acceptance criteria, the derivation companion | `MODEL_DESCRIPTION.md`, `NUMERICAL_METHOD.md` |
| `06_VALIDATION/` | validation results, literature/Crossref verification, project audits | `VALIDATION_INDEX.md` |
| `07_DOCUMENTATION/` | program control documents, the ten phase reports, the repository-level docs, corrections log | `PROJECT_OVERVIEW.md` |
| `08_FINAL_OUTPUTS/` | manuscript source and renderings, supplement workbook, cover letter, figures, checklists | `FIGURE_PROVENANCE.md` |
| `09_ARCHIVE_METADATA/` | this file, the status report, manifests, SHA-256 sums, gate transcripts | `FINAL_PACKAGE_STATUS.md` |

## Five-minute tour for a reviewer

1. `07_DOCUMENTATION/PROJECT_OVERVIEW.md` - what was done and where each thing lives.
2. `01_PROGRAM/README_PROGRAM.md` - how to run it, what the settings are, what was verified.
3. `03_DATA/DATA_DICTIONARY.md` - what every stored number means, in the stored precision.
4. `08_FINAL_OUTPUTS/FIGURE_PROVENANCE.md` - figure -> script -> data -> command.
5. `09_ARCHIVE_METADATA/FINAL_PACKAGE_STATUS.md` - what passes, what is partial, what is missing.

## Rules this archive was built under

- **No fabrication.** Missing information is written as `NOT DOCUMENTED` or `NOT AVAILABLE`; no
  parameter, result, DOI, version, command or provenance link was invented, and every generated
  statement cites the file it came from.
- **Nothing reworded to look better.** The one failing verification test, the OOM-killed run, the
  un-compilable LaTeX environment and the gitignored figure renditions are all stated in the
  sections above and in `FINAL_PACKAGE_STATUS.md`.
- **Determinism.** The zip is written with fixed entry stamps, fixed permissions and sorted order,
  and no file inside records the build clock, so `sha256sum` of the zip is a checksum of the tree.
  Rebuilding from the same commit reproduces the same bytes.
- **Excluded on purpose:** `PAPER_PROJECT/packages/` (generated archives), `__pycache__` and `*.pyc`,
  the 52 MB `le.zip` snapshot (it is the same content as the repository), `work/handoff.zip`
  (redundant with `01_PROGRAM/handoff_baseline/`), `.git`, editor swap files, and the gitignored
  600-dpi figure renditions (regenerate; see `08_FINAL_OUTPUTS/FIGURE_PROVENANCE.md`).
- Skipped while assembling: 15 path(s) matched the exclusion rules.

## Integrity

```bash
sha256sum -c 09_ARCHIVE_METADATA/SHA256SUMS.txt      # from the extracted archive root
```

`file_manifest_sha256.csv` additionally lists every file with its size and its path in the source
repository, so an archive path can be traced back to a repo path. `INTEGRITY_AUDIT.json` is the
machine-readable result of the final audit (figures, citations, paths, duplicates, junk).
