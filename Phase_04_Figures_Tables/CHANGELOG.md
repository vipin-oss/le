# Phase 4 changelog — figures and tables regenerated from verified data

Generated documents are listed with the file that was changed to change them. The two documents were rebuilt
after the verification artefact was completed, and all gates re-run.

## 1. Figures

- `PAPER_PROJECT/08_Experiments/make_figures.py` re-run in full: all eight figures regenerated from
  `09_Raw_Data/production`, `09_Raw_Data/convergence`, `10_Processed_Data/ANALYSIS_V2.json` and
  `07_Tests/TEST_RESULTS.json` (log: `figure_rerun.log`).
- Comparison against the committed PNGs, pixel-array and digest: `verification/figure_render_diff.json`
  (1–16 px raster-extent differences under matplotlib 3.11.2, no content change).
- **No figure file was replaced.** The committed binaries stay as submitted with the frozen documents; the
  unpinned plotting environment is recorded as a gap for Phase 8 (P4-4).

## 2. Tables, captions and prose

- `verification/audit_phase4.py` added: T1 determinism, T2 cell provenance, T3 carried-literal sweep, with
  `verification/phase4_tables.json` as its output. Outcome 3 × PASS: 320/320 table cells and 587/587 prose and
  caption numbers traced to a stored artefact or to a constant the builders compute; both Markdown documents
  and `highlights.txt` byte-reproducible; `SUPPLEMENTARY_TABLES.xlsx` cell-reproducible.

## 3. Builders

- `build_manuscript.py` — the placeholder guard moved onto the generated text (render to
  `.manuscript_IJHMT.pending.md`, guard, `os.replace`), so a failing build can no longer overwrite the last
  good document and a stale clean file can no longer license a dirty build. The docx build follows the guarded
  Markdown, so the three artefacts cannot disagree.
- `build_calculations.py` — the guard, which ran after the write, now restores the previous bytes before
  re-raising, so an aborted build leaves the last good companion in place.
- Phase 3's `n/a` guard (abstract and highlights) is unchanged and still correct; only its position relative to
  the write was wrong.

## 4. Data artefact and documents

- `07_Tests/TEST_RESULTS.json` — re-run to completion: 28 cases, 27 PASS, 0 FAIL, one exploratory INFO, wall
  1202 s (`suite_rerun_20261003c.log`). The file that was in the branch was a 24-case mid-run capture.
- Regenerated, in this order (the order is the point, see P4-1): `make_code_freeze.py
  submission_2026_10_03c` → `build_manuscript.py` → `build_calculations.py` → `build_supplement.py` →
  `md_to_tex.py` (both) → `md_to_pdf.py` (both) → mirrors copied → gates.
- Refreshed: `manuscript_IJHMT.md/.pdf/.docx`, `calculations_IJHMT.md/.pdf`, `MANUSCRIPT_STATS.json`,
  `highlights.txt`, `SUPPLEMENTARY_TABLES.xlsx`, `FINAL_REVISED_MANUSCRIPT.tex/.pdf`,
  `FINAL_REVISED_CALCULATIONS.tex/.pdf`.
- Gates after the final build, all green: `tools/audit_tex.py`, `tools/audit_tex.py -c` (companion),
  `tools/check_tex_commands.py`, `tools/check_crossrefs.py`, `tools/verify_pdf.py` on each of the four PDFs.
  Zero `n/a` in either document; the manuscript quotes the manifest digest that is on disk.
- `CODE_FREEZE_submission_2026_10_03c.json` regenerated (27 files) as the last code-side step before the final
  build; `submission_2026_10_03b`, `submission_2026_10_03`, `submission_2026_10_02` and the gate manifest are
  untouched.

## 5. Cross-phase corrections recorded rather than rewritten

- `Phase_03_Mathematical_Audit/REPORT.md` §7 gained an "Amendment (Phase 4)" note: the `n/a` episode was a
  guard-ordering defect in the builders as well as a build-while-the-suite-runs ordering mistake. The original
  text is left in place; the amendment states what the extra step found.
- Phase 3 items P3-15 (verification re-run) closed here with its log, and P3-8 (the `n/a` guard) closed with
  the corrected diagnosis; Phase 4's ledger names both.

## 6. What Phase 5 inherits

Nothing from this phase is left dangling except P4-4 (pin the plotting environment in the reproducibility
note, or ship figures as data plus script with a version). Figures are content-stable and every printed number
in both documents is now traceable, so the remaining work on them is presentation (labels, colour-blind
safe palettes, vector output for the journal) rather than correctness — that is the Phase 5 question.
