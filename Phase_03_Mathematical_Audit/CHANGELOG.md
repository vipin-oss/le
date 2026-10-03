# Phase 3 changelog — mathematical audit

Every entry lists the file that was changed and, for generated documents, the builder that was changed
instead. Nothing in the two documents was hand-edited; the documents are the output of the builders listed.
Verified by `verification/audit_phase3.py` (22 PASS, 3 INFO, 0 FAIL) and by the project's document gates.

## 1. Source code

- `PAPER_PROJECT/06_Source_Code/src/cg_bromwich.py`
  - `BromwichPlan.t_valid_max` computed as `T - (t0 + 2.5 * tw)` instead of the hard-coded `T - 5.5`, with a
    docstring that says why the bound follows from the pulse width and not from causality, and what it costs
    the wide-pulse case (11.5 against 14.5 t_th). Baseline behaviour unchanged.
  - Module header states the width dependence next to the alias and growth figures it quotes.
- Four source files: a comment naming an internal brief as the origin of a tolerance now names the test brief
  that actually contains it. Values untouched.

## 2. Builders

- `ms_static.py` — Section 2.1 plane-strain-class paragraph; Section 2.2 norm-convention sentence for δ, with
  the computed invariance and the factor between the two contractions; helpers that compute δ, its lattice
  spread and the plane-strain-convention sensitivity, so those statements print numbers rather than repeat
  them; the Section 4.6 DFT sentence converted to print `t_w*sqrt(pi)/T` from the plan.
- `ms_derivation.py` — Eq. (33) printed with the norm macros that render; the `c_ref` wording corrected.
- `ms_numerics.py` — Section 4.4 DFT comparison prints the computed mean; the validity criterion is stated as
  the rule with both numbers instead of one number.
- `ms_results.py` — Table 4 caption and provenance (no internal brief named); the Section 6.4 feedback
  sentence recomputed from the shipped plan constants; every "frozen/internal/pre-registered" phrase
  replaced by the fact it stood for.
- `build_manuscript.py` — code-freeze labels moved to `submission_2026_10_03c` with the superseded manifest
  named; the Section 9.1 list of files that drifted from the gate manifest computed from the manifests; the
  numerical-methods disclosure paragraph (as first written / corrected / verified); the AI declaration split
  per journal policy; an `n/a` guard that aborts the build if a required input number is missing from the
  abstract or a highlight.
- `build_calculations.py` — the same freeze chain and the same computed drift list; the audit paragraph in
  Section 10.3 (what the audit changed, and the explicit statement that no stored run and no reported value
  changed); the AI declaration rebuilt from the same text as the manuscript's; the last two internal
  designations removed ("earlier internal analysis" to "the analysis as first written", "pre-registered" to
  "fixed before the runs").
- `PAPER_PROJECT/13_Manuscript/cover_letter.md` — hand-maintained, so edited directly: writing use and
  research use named separately, with the wording flagged for author confirmation and reviewers left to the
  authors.

## 3. Regenerated deliverables

`manuscript_IJHMT.md`, `calculations_IJHMT.md`, `MANUSCRIPT_STATS.json`, `highlights.txt`,
`SUPPLEMENTARY_TABLES.xlsx`, both `.pdf`, both `.docx`, `FINAL_REVISED_MANUSCRIPT.tex`/`.pdf`,
`FINAL_REVISED_CALCULATIONS.tex`/`.pdf` and the figure set. After the last edit, the PDFs were re-rendered and
the TeX regenerated from the regenerated Markdown.

Gates, all green after the final build: `audit_tex.py` (manuscript), `audit_tex.py -c` (companion),
`check_tex_commands.py`, `check_crossrefs.py`, `verify_pdf.py` for all four PDFs. A stale-string scan
(`0.27 of the peak`, `frozen criterion`, `frozen threshold`, `frozen bound`, `earlier internal analysis`,
`MASTER_PROMPT`, `pre-registered`, `n/a`) returns zero in both documents.

## 4. Code freeze

`CODE_FREEZE_submission_2026_10_03c.json` added (27 files, every digest verified byte-identical to the code as
submitted). Regenerated as the last step after each builder edit. `submission_2026_10_03b`,
`submission_2026_10_03`, `submission_2026_10_02` and the gate manifest are untouched, as required.

## 5. Deliberate non-changes

- The O(1) first row of the wall refinement probe: cause identified (one-sided metric derivatives in the probe,
  REPORT 7), scheme left alone, finding recorded.
- `C_bar = C33` stays the nondimensionalisation reference; it is not a bulk modulus and no sentence calls it
  one (REPORT 2, A8).
- The uniform-temperature patch test is not cited as evidence of accuracy: it holds by construction (C6).
- `run_tests.py`'s hard-coded `date = '2026-10-01'` (the date that suite was authored) left as is and handed
  to Phase 8, where the release record is written.
- Historical documents (`CHANGELOG.md`, `FINAL_QA_REPORT.md`, `JOURNAL_FIT.md` in `13_Manuscript`) keep their
  own dated counts; refreshing them is Phase 8 work, not a Phase 3 edit.
- No number was changed to improve an appearance. The one code-side numerical statement that changed (the
  validity bound) leaves the baseline case identical.

## 6. Process

- The `n/a` episode: a build ran while the suite was rewriting `TEST_RESULTS.json`; the diagnosis, the wrong
  suspicion about path resolution, and the ordering rule that follows from it are in REPORT 7.
- Sandbox resets deleted the uncommitted directory twice. Recovery: `git fetch` + `git reset --hard` to the
  pushed branch tip, `sh bootstrap_paths.sh`, environment recreated. Since then every stage of the phase is
  committed and pushed as it is finished, and the harness and the patch scripts are part of the branch.
- Full Phase-3 replay is possible from the branch: the idempotent patch scripts in `verification/`, then the
  builders, then the freeze, then the gates (REPORT 10).
