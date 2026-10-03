# Phase 8 changelog

- Final cross-artifact audit added (`verification/final_consistency.py` + `final_consistency.json`): references 55 = .bib = .tex \cite = PDF; monotone numbered style, no orphans; structure stats agree with MANUSCRIPT_STATS; freeze 03j hash-matches all 27 entries and the full history is byte-unchanged; suite sentence matches TEST_RESULTS.json (28/27/0/1); abstract, highlights, keywords, declarations and back-matter order conform; no banned words, no internal vocabulary. 0 failures.
- `tools/connection_audit.py`: deposit target now the newest submission manifest (was pinned to 10_03); companion pattern accepts the Phase 7 wording; manuscript §9.1 states both byte-identical and edited counts (8 of 15 / 7 edited) so the recomputation matches.
- `13_Manuscript/PDF_VERIFICATION.txt` regenerated from the actual verify_pdf runs (manuscript 33 pages, companion 14 pages, both ALL CHECKS PASSED).
- Legacy current-state docs superseded by banner: `FINAL_QA_REPORT.md`, `00_Project_Control/REPRODUCIBILITY_STATUS.md`.
- `13_Manuscript/cover_letter.md` refreshed to the current document and given the Cattaneo/Vernotte citation paragraph; `AUTHOR_INPUT_REQUIRED.md` A5/A6/A9/A10 updated.
- `SUBMISSION_CHECKLIST.md` written: what is machine-checked, what only the authors can close (identity, funding, competing interest, CRediT, repository DOI, AI confirmation, TeX compile, figure formats).
