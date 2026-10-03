# Phase 4 — Figures and tables regenerated from verified data

Objective: prove that every figure and every table in the submission comes out of the stored data through a
builder, with nothing hand-made, hand-typed or quietly carried over. Three checks, all in
`verification/audit_phase4.py`; the run log and the workbook/render evidence sit beside it.

Result: **T1 PASS, T2 PASS, T3 PASS** — and two real defects found on the way, both fixed (§3, §4), one of
which corrects the diagnosis recorded in Phase 3.

## 1. Figures

`08_Experiments/make_figures.py` regenerates all eight figures from `09_Raw_Data/production`,
`09_Raw_Data/convergence`, `10_Processed_Data/ANALYSIS_V2.json` and `07_Tests/TEST_RESULTS.json` (its own
header records that list; the script is data-driven and no image is produced by a generative model).

The regeneration was run here (`figure_rerun.log`) and compared against the committed PNGs
(`verification/figure_render_diff.json`): every figure reproduces, and each differs from the committed file by
1–16 px in overall raster size — a renderer difference (this sandbox has matplotlib 3.11.2; the committed
files were written by a different build), not a content difference. No axis, curve or label moved in a way
that changes what a figure says, and no figure number in either document had to be touched.

**Decision: the committed figures are kept as the submitted ones**, because they are the binaries the frozen
documents and the PDFs were built against; re-rendering them would churn eight binaries for layout pixels.
What the comparison does establish is a gap worth closing before submission: the plotting environment is not
pinned anywhere, so "regenerate the figures" is not yet a reproducible instruction. Carried to Phase 8 as
P4-4 (pin Python/NumPy/matplotlib versions in the reproducibility note, or ship the figures as data plus the
script and say which version was used).

## 2. Tables and prose: where does every number come from

- **T2 — cell provenance.** 20 tables across the two documents, 320 numeric cells. Each value is looked up in
  the artefacts the builders read — `TEST_RESULTS.json`, `ANALYSIS_V2.json`, `CONVERGENCE_RESULTS.json`,
  `CONVERGENCE_DIRS.json`, `MANUSCRIPT_STATS.json`, the parameter table, the archived CSV tables — or among
  the closed-form constants the builders compute from the shipped code (`cg_model`, `cg_grid`, and the
  manuscript builder's own helpers, which is how the computed DFT mean and the δ values are covered).
  **320 of 320 accounted for, 0 unmatched.**
- **T3 — carried literals.** Every number in prose and in figure captions of both documents (587 of them) is
  tested the same way. **0 unmatched**, including the numbers in the Fig. 2(b) caption, which is the evidence
  line for the rotation sign correction. The point of this check is the class of error found in Phase 3: a
  number typed into a sentence and then left behind when the data moved. There is now no such number in either
  document.
- **T1 — determinism.** Rebuilding from the unchanged code reproduces `manuscript_IJHMT.md`,
  `calculations_IJHMT.md` and `highlights.txt` byte for byte, and `SUPPLEMENTARY_TABLES.xlsx` sheet by sheet
  and cell by cell (its bytes differ only by the creation timestamp `openpyxl` writes into `docProps`, so the
  content comparison is the meaningful one). No table or caption has been hand-edited into a generated file.

## 3. Defect found and fixed: the placeholder guard checked the wrong artefact

Phase 3 added a submission guard that refuses to ship a table containing `n/a`, and recorded that the guard
"correctly refused to rebuild" over a stale document. The mechanism was the opposite in both builders, and it
is what actually caused the trouble:

- `build_manuscript.py` called `_no_placeholder_tables` on the file **before** rendering the new Markdown to
  it. A clean previous file therefore licensed a dirty new build, and the good document was overwritten with
  `n/a` cells; a dirty previous file conversely blocked a clean build. Now the blocks are rendered to a
  temporary file, that file is guarded, and only then is it moved into place — the guard sees the text being
  generated, and a failing build leaves the last good document untouched.
- `build_calculations.py` guarded **after** writing, so an abort left the bad companion on disk. It now
  restores the previous bytes before re-raising.

This corrects Phase 3 §7: the root cause was not only the build-while-the-suite-writes ordering (which remains
a real rule) but this guard-ordering defect. An "Amendment (Phase 4)" note has been appended there, and the
Phase 3 ledger item P3-8 carries a pointer to it.

## 4. Defect found and fixed: a truncated `TEST_RESULTS.json` had been committed

The committed `07_Tests/TEST_RESULTS.json` held 24 of 28 cases, all PASS, with the exploratory case and two
reported quantities absent — a mid-run snapshot captured when a sandbox reset interrupted the suite, committed
as if it were the finished record. Rebuilding from it is exactly what produced the `n/a` cells (§3), so the
document, not the data, looked at fault.

The suite was re-run to completion on the code as it now stands:
`TESTS DONE: 27 PASS, 0 FAIL` over 28 cases with one exploratory INFO, wall 1202 s, in
`suite_rerun_20261003c.log` — this is the record Phase 3 could only report as in flight (P3-15 is therefore
closed). Both documents were then rebuilt from the completed artefact and all gates pass again: abstract
249/250 words, highlights [78, 70, 69, 74, 69], 84 equations / 8 figures / 11 tables / 54 references,
companion 11 sections / 37 subsections / 29 equations / 9 tables / ~5244 words; `audit_tex` (both documents),
`check_tex_commands`, `check_crossrefs` and `verify_pdf` on all four PDFs green; `n/a` scan zero.

The code-freeze digest quoted by the manuscript also moved: the manifest had been regenerated after the last
build, so the document quoted the previous digest. Rebuilt in the correct order (freeze first, then the
documents), the manuscript now quotes `6beb28158e7f671a`, which is the digest of
`CODE_FREEZE_submission_2026_10_03c.json` as it stands on disk (P4-1 closed; the rule is in the changelog).

## 5. What was deliberately not changed

- The eight committed PNGs (see §1).
- Table 5's coarse-grid exceedance row (5.028e-03 against the inherited 5e-03 threshold) — reported, not
  suppressed; the same sequence satisfies the threshold at the production grid and its convergence order is
  its own case (V0b).
- The exploratory INFO case `V3c_nonaligned_37deg_EXPLORATORY` stays in the record as exploratory.
- No value in any table was edited to make a comparison look better; every value in both documents is either a
  stored quantity or a quantity a builder computes from the shipped code (§2).

## 6. Reproducing this phase

From the repository root, with the project environment (`numpy`, `scipy`, `matplotlib`, `openpyxl`):
`python3 Phase_04_Figures_Tables/verification/audit_phase4.py`. It rebuilds both documents into place, compares
them against their previous bytes, then checks every table cell and every prose number against the sources, and
writes `verification/phase4_tables.json`. Two rules the checks depend on, both learned the hard way here: run
this only when `07_Tests/run_tests.py` is **not** writing its results, and regenerate the code freeze **before**
the last document build, never after.
