# manuscript_v2 — version log

| version | date | base | what changed |
|---|---|---|---|
| v1.1 | 2026-10-28 | branch `arena/36bc8cc8-le` | received sources: 17 sections, 6 appendices (2 compiled), 126-page build. Frozen in `paper_v2/versions/v1.1_source_snapshot/` |
| v1.2 | 2026-11-01 | v1.1 | cycle 1: new 259-word abstract, 11 keywords, `abstract` environment, Declarations (CRediT/funding/competing interests/data availability/generative-tool statement), `\today` instead of a hard-coded date, stale duplicate `tables/` removed, all six appendices compiled (A–F), two dangling findings closed, two declared-provisional figures reported instead of hidden |
| v1.2a | 2026-11-01 | v1.2 | page-level audit cycle (26 checks, 0 FAIL). `appendices/appA_equation_register.tex`: legend extended by two labels that were already in use (`VERIFIED-SYMBOLIC`, `WITHHELD`) — no verdict changed; two cross-references re-pointed after the un-`\input` file `appendices/energy_flux_derivations.tex` moved to `paper_v2/working_notes/`; `references_local.bib`: Chester 1963 DOI verified against Crossref and recorded; Cattaneo 1948 and Vernotte 1958 now state plainly that no DOI exists. Pre-edit copies in `paper_v2/versions/v1.2_edits_2026-11-01/` |

Build: `cd master && pdflatex main && bibtex main && pdflatex main && pdflatex main` (or `make`, see `master/BUILD.md`).
Figures are not in git: they are supplied in the submission zip and, in this workspace, live outside the repository.
