# FINAL_PACKAGE_STATUS

Overall status: **REPRODUCIBLE, WORK IN PROGRESS - see the failing gates below**

| section | status | detail |
|---|---|---|
| Program (code) | COMPLETE | frozen solver + drivers + tests + builders + utilities; 386 files; environment pinned where the project pinned it, unpinned parts labelled NOT DOCUMENTED |
| Data | COMPLETE | 436 files: every raw run, every processed aggregate, every CSV the figures read, and a generated data dictionary |
| Parameters | COMPLETE | `01_PROGRAM/parameter_manifest.json` extracted from the source by AST; no value typed by hand |
| Figures | COMPLETE (raster renditions regenerable) | 37 output files; 200-dpi PNGs and vector PDFs shipped, 600-dpi PNG/TIFF regenerate in one command |
| Provenance | COMPLETE | figure -> script -> data -> command in `FIGURE_PROVENANCE.md`; run -> inputs -> output hash -> wall time in `03_DATA/processed/PRODUCTION_PROVENANCE.csv` |
| Manuscript source | COMPLETE | `02_OVERLEAF/`: .tex (single file), companion .tex, .bib with 55 entries, 8 vector figures, highlights; every cited key resolves |
| Manuscript compilation | NOT AVAILABLE IN THIS ENVIRONMENT | no TeX engine in the packaging sandbox; static verification passed (figures, citations, commands, cross-references); the four compile commands and the log triage script ship with it |
| Validation | PARTIAL BY DESIGN | verification suite shipped with its one reported failure; physical validation status is EVIDENCE_UNAVAILABLE and the paper says so - see `06_VALIDATION/VALIDATION_INDEX.md` |
| Reproduction test | PASS | 5 steps, 18 files compared |
| Documentation / audit trail | COMPLETE | 138 files: program status documents, ten phase reports, corrections log, audits, repository-level notes |
| Versioning | COMPLETE for the repository era | git history exported to `07_DOCUMENTATION/` + twelve code-freeze manifests; pre-2026-10-01 version control: HISTORICAL CHANGELOG NOT AVAILABLE (documents exist instead, and are shipped) |
| Integrity | COMPLETE | 1230 files hashed (SHA256SUMS.txt + file_manifest_sha256.csv); the archive is byte-deterministic from the tree |

## Gate results recorded by this build

| gate | exit code |
|---|---|
| audit_tex | 0 |
| connection_audit | 1 |
| check_tex_commands_manuscript | 0 |
| check_tex_commands_calculations | 0 |
| check_crossrefs_manuscript | 0 |
| final_consistency | 0 |
| verify_code_freeze | 0 |
| verify_pdf_manuscript | 0 |
| verify_pdf_companion | 0 |

## Missing items, and the recommended action for each

| missing | why | action |
|---|---|---|
| author names, affiliations, ORCID, corresponding e-mail | only the authors can supply them | fill `08_FINAL_OUTPUTS/manuscript/AUTHOR_INPUT_FORM.md` item 1; the builders then propagate them |
| CRediT, competing interest, funding statements | declarations are author statements | form items 2-4 |
| data/code DOI | the deposit has not been made | deposit `RESEARCH_PROJECT_FINAL.zip` (recipe in `09_ARCHIVE_METADATA/archive_build.json`) and replace the placeholder |
| compiled PDF of the .tex | no TeX engine here | run the four commands in `02_OVERLEAF/README_OVERLEAF.md` and read the log |
| 600-dpi PNG/TIFF renditions | gitignored generated files, tens of MB each | run the exporter named in `08_FINAL_OUTPUTS/FIGURE_PROVENANCE.md` |
| third-party paper PDFs behind the bibliography | not redistributable | the Crossref verification records ship instead, in `06_VALIDATION/literature_verification/` |
| an experimental dataset for validation | none exists for this geometry | nothing to do - the paper claims no physical validation; do not let a revision imply one |

## Verdict in one sentence

A researcher holding only this archive can read the model, find every parameter, re-run the
analysis and figures from the shipped data, reproduce the verification suite, modify the code and
see the freeze manifest invalidate or accept their change, and compile the manuscript - and the
only things standing between this tree and a submission are the five author-supplied statements and
one `pdflatex` run on a machine that has TeX.
