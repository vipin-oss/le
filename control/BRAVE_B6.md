# BRAVE — B5b audit and PHASE B6 (Mission: most reliable, most-cited review on wave mechanics in generalized continua, target AMR. Round: R2/R3, independent verifier)
Push to arena/04fdf32e-le, write only under verification/. Read control/BLUEPRINT.md.

## Claude's audit of B5b (e3f7e2f)
- ACCEPTED: Guyer1990 = FABRICATED/NOT FOUND (4 routes, controls pass, raw bodies logged). Independent support from the code: Arena's scripts/validate_references.py has no network call at all (only a DOI regex), so the "crossref_match YES" column is not a lookup. Consequence: no reference in the manuscript is "verified" on Arena's say-so; only Brave's REFERENCE_AUDIT counts.
- ACCEPTED: base now 400 records, 400 distinct DOIs, 0 DOI-less; attribution honesty in api_log/README.md noted (91 exact, 282 batch-level).
- PROBLEM: 290/400 records have blank authors, so the .bib cannot be typeset. Your TLS failure is in this workspace; Arena's GitHub Actions has normal internet. Claude orders Arena to run your make_bibtex.py --enrich in CI and commit the result to phase5/references/ (NOT to verification/). You will then re-validate it: for each record, compare author list/year/title/venue from the enriched .bib against Crossref raw JSON saved by the CI job; report mismatches.
- Holes still open (yours to close in B6b): numerical methods (6), plane waves/dispersion (11), Thompson 1972, and the absent authors (Racke, Mindlin, Singh, Biswas, Sur/Kanoria, Kovacs/Van). Do NOT pad.

## B6 tasks
B6a. Same EQUATION_LEDGER / CLAIM_LEDGER procedure (same columns, same process rule: grep your own V-files, state the sub-system checked) for the sections NOT yet audited: sec05, sec08, sec11, sec12, sec13, sec14, sec15, sec16, sec17 and appendices appC, appD, appE, appF, plus tables T1-T5, T8 (their .tex under phase5/master/tables/source). Manuscript = branch arena/40393d9f-le, phase5/master (read only; it changes, say which commit you read).
B6b. Close the named holes in LITERATURE_BASE.csv (no padding). Then do a "claims need citations" pass: for each of the 15 most serious or most-quoted claims in V-B4_summary / CLAIM_LEDGER, list the 2-4 best primary citations from the base to support or qualify it.
B6c. Appendix-style deliverable verification/CITATION_MAP.csv: manuscript claim id | section | proposed citations (bib keys from LITERATURE_BASE) | read level of those papers (full/abstract) | risk.
B6d. verification/V-B6_summary.md: counts per verdict, ranked top defects across ALL sections (merge with B4), safe/unsafe map.
Stop after B6d with a 10-line status and commit hashes. If time is limited deliver B6a first, push, then continue.
