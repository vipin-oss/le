# P0-a - Prior Literature Originality Matrix, Batch 001

## Scope and handling
- Section 2 of `paper_v2/BLUEPRINT_v3.1.md` was read before source processing.
- `paper_v2/paper_sources.zip` was used read-only; only bibliography metadata was inspected for target identifiers.
- Drive indexes were used only as locators. Scientific content in the matrix comes only from opened PDFs and is tied to page-level evidence in the evidence CSV.
- The six specified targets are retained. One optional directly relevant constitutive-theory item was added because its PDF was present and opened in Drive.
- Only these four deliverables were created; no manuscript, bibliography, script, PDF, or blueprint was edited.

## Verification counts
| Level | Count | Meaning in this batch |
|---|---:|---|
| R0 | 5 | No matching target PDF was verified; rows remain unresolved. |
| R1 | 0 | No records at this level. |
| R2 | 0 | No abstract-only records; abstract-only would not count as full-text verification. |
| R3 | 2 | Full-text evidence was checked on cited pages; this does not mean each entire article was read end-to-end. |
| Total | 7 | Six first-batch targets plus one optional directly relevant theory item. |

## Matched full-text records
- `P0A005`: Chandrasekharaiah, 1998, `1.3098984.pdf`. First-page title, author, journal, year, and printed page 705 were checked. Evidence covers the review's ETE/TRDTE and Green-Naghdi coverage map, its half-space boundary-initiated-wave example, reported thermal-relaxation measurements, and the author's concluding appraisal. The DOI is not visible on PDF page index 1, so the matrix DOI is `-`. The abstract, Sections 1-2, selected Section 7 passages, and Section 8 conclusion were checked; the whole review was not read end-to-end.
- `P0A007`: Green and Naghdi, 1993, `B13-029__bf00044969.pdf`. The first page verifies title, authors, Journal of Elasticity, page range, and year. The checked abstract and selected Sections 2-4 support the non-dissipative type-II formulation, the shared potential for stress and entropy flux, finite-speed thermal waves, the Second-Law caveat, and a uniqueness result. The DOI is not printed on PDF page index 1 and was not inferred from the filename. The paper has no standalone conclusion section in the checked text; the entire article was not read end-to-end.

## R0 targets and unresolved items
- `P0A001`: Shakeriaski et al. (2021), DOI `10.1093/jcde/qwaa082`. A Shakeriaski-named candidate was opened, but its first page identified a different article and DOI; it was excluded.
- `P0A002`: critical review of non-Fourier bio-heating with phase lags, DOI `10.1016/j.ijthermalsci.2025.110376`. Exact DOI search returned no matching file.
- `P0A003`: `On the phase-lag Green-Naghdi thermoelasticity theories`, DOI `10.1016/j.apm.2016.01.010`. The corrected exact DOI search (valid fields and no sort) returned no matching file.
- `P0A004`: `On a multi-phase-lag model of coupled thermoelasticity`, DOI `10.1016/j.icheatmasstransfer.2020.104722`. Exact DOI search returned no matching file.
- `P0A006`: Joseph and Preziosi (1989), `Heat waves`, DOI `10.1103/revmodphys.61.41`. No matching paper PDF was verified; search results were indexes and unrelated files.
- For all R0 rows, scientific fields and unverified PDF metadata are `-` in the matrix; requested identifiers and search outcomes are in the match/verify CSV. No findings were inferred from indexes or filenames.
- DOI confirmation on the first PDF page remains unresolved for `P0A005` and `P0A007`. Their matrix DOI fields are `-`.
- No benchmark claim was populated. The reported relaxation-time measurements in `P0A005` are explicitly distinguished from direct validation of thermoelastic-wave predictions. No surface-wave coverage, thermodynamic admissibility, or experimental validation was inferred beyond the checked excerpts.
- Five target PDFs remain unresolved. Batch 002 was not started and is held pending author review.

## Evidence controls
- Every quoted excerpt in the evidence CSV is at most 25 words and ASCII-only.
- All populated names and excerpts are ASCII; no diacritics appeared in the transcribed fields, so no transliteration was required.
- Page references distinguish printed journal page numbers from one-based PDF page indices; rows without a matched PDF explicitly mark both page values as unavailable.
- Unsupported scientific fields are `-`. The R3 claims are restricted to the checked excerpts and cited pages; no claim is made that either complete article was read end-to-end.
- No manuscript novelty or originality claim is made in these deliverables.
