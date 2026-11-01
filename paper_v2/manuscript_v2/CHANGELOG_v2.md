# manuscript_v2 — version log

| version | date | base | what changed |
|---|---|---|---|
| v1.1 | 2026-10-28 | branch `arena/36bc8cc8-le` | received sources: 17 sections, 6 appendices (2 compiled), 126-page build. Frozen in `paper_v2/versions/v1.1_source_snapshot/` |
| v1.2 | 2026-11-01 | v1.1 | cycle 1: new 259-word abstract, 11 keywords, `abstract` environment, Declarations (CRediT/funding/competing interests/data availability/generative-tool statement), `\today` instead of a hard-coded date, stale duplicate `tables/` removed, all six appendices compiled (A–F), two dangling findings closed, two declared-provisional figures reported instead of hidden |

Build: `cd master && pdflatex main && bibtex main && pdflatex main && pdflatex main` (or `make`, see `master/BUILD.md`).
Figures are not in git: they are supplied in the submission zip and, in this workspace, live outside the repository.
