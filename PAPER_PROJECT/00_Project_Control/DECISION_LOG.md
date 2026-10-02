# DECISION_LOG — PAPER_PROJECT (session of 2026-10-01)

The handoff's decisions D001–D018 stay in `/home/user/work/handoff/DECISION_LOG.md`. They are history here, not re-asserted.

## P0-D001 (2026-10-01) — Phase 0 started without an explicit phase authorization
- Previous: no phase authorized (master prompt pasted twice; my phase-choice question was skipped).
- New: run Phase 0 only (intake; no compute, no scientific decision), then STOP.
- Reason: §88 user control vs. the user's recorded preference not to be asked repeatedly (handoff D013, D016, D017). Phase 0 is non-committal and revocable.
- Affected equations / code / results: none. Revalidation: not applicable.

## P0-D002 (2026-10-01) — Baseline protection
- `/home/user/work/handoff/` is a read-only baseline. A stray `__pycache__` created by my earlier execution was removed (304 files; 303/303 hashes OK). New work goes to `/home/user/PAPER_PROJECT/` and `/home/user/work/rerun/`.

## P0-D003 (2026-10-01) — Earlier blanket authorization (handoff D013) not assumed to carry over
- It was given to a previous agent session for phases 1→13; its user-owned exceptions still apply. Ask once, as one line, whether it stands.

## P0-D004 (2026-10-01) — Status relabel (no change of substance)
- Handoff "Physical validation NOT_AVAILABLE" → MASTER_PROMPT §14 label APPLICABLE — EVIDENCE_UNAVAILABLE.

## P0-D005 (2026-10-01) — T1 wording refined
- My earlier statement "T1 fails by ~5 orders" is refined. The plan text is ambiguous ("all φ,φ′" vs "on the 90° discrete-rotation identity"). Recorded numbers: all-φ scatter 3.04e-3; worst 90°-pair 1.58e-3; the reported 0°/90° pair 4.04e-10 is blind to the bug (s·c = 0). T1 fails under either reading except for that single pair; with the patch the all-φ spread is 3.2e-10.

## P7-D001 (2026-10-01) — Phases 7→13 authorized under handoff D013
- Previous: Phase 0 only. New: user message "Follow MASTER_PROMPT.md. Continue Phases 7→13 under D013." → phases 7–13 run without per-phase stops. User-owned gates stay (D013): compute > 4 CPU-h / 1 GPU-h / 5 GB, first-principle model changes, final journal choice, submission.
- Phases 1–6 are NOT re-opened (their documents carry the stale values listed in PROJECT_STATE_PHASE_00 §7 G5; corrected in `04_Theory/FORMULATION_ADDENDUM.md`, `05_Numerical_Method/NUMERICAL_METHOD_V2.md` and the new manuscript).

## P7-D002 (2026-10-01) — Single-pulse Bromwich synthesis replaces periodic DFT; hysteretic damping removed  **[FLAG FOR USER CONFIRMATION]**
- Previous: `cg_transient.synthesize` (periodic steady state of a pulse train, window 8 t_th) + hysteretic damping η_d = 0.05. New: Bromwich inversion on Re s = 0.9/t_th (`cg_bromwich.py`), undamped model.
- Reason: evidence in PROJECT_STATE_PHASE_00 §6 (G3/G4) and tests U4–U8, V11. The change makes the code compute what the problem definition states (one pulse, quiescent initial state); governing equations, BCs, ICs, geometry, parameters and the spatial discretisation are unchanged.
- Classification: I treated it as a **correction of the time-reconstruction (numerical), not a first-principle model change**, so I did not stop at the gate that I had announced for "approval of the synthesis-method change". This is the one decision the user may want to veto; if vetoed, results of the periodic route cannot be defended (documented artefact), so the alternative would be a long-window quasi-static model (a model change).
- Affected: all time-domain results (re-run); verification (new tests); manuscript (rewritten). Revalidation: done (Phase 7–9).

## P7-D003 (2026-10-01) — Iterative refinement in `HarmonicSolver.solve`
- Previous: LU solve only (forward-error floor ≈ 1e-8 in u and σ: diagnostic `07_Tests/diagnostics/diag_covariance_floor.py`). New: `refine = 2` steps (floor ≈ 1e-14). Mathematically identical problem; default of the new argument keeps the option switchable (`refine=0` = original behaviour).

## P7-D004 (2026-10-01) — Test definitions corrected before the final run (no criterion loosened)
- U3: Voigt-form eigenvalues are not rotation invariant → Mandel form. V3 (and the handoff's V3): displacement error was normalised by max(|u|, |θ|, …) (unit mix, blind to u and σ) → per-field normalisation + wall hoop covariance. V9: unweighted worst-case high-frequency transfer-function metric replaced by pulse-weighted spectral error + time-domain peak/series/D comparison. Run-1 failures are preserved in `07_Tests/logs/`.

## P9-D001 (2026-10-01) — Radial grid clustering γ_grid 3.5 → 5.0
- Evidence (`CONVERGENCE_DIRS.json`, φ = 30° ellipse, 96×48): γ = 3.5: 1.412 MPa/K; 5.0: 1.245; 6.5: 1.236. Doubling Nr at γ = 3.5 changes the peak by −8.7%, doubling Nt by +3.0%: the near-wall radial resolution controls the sharp-tip stress; the handoff grid (96×48, γ = 3.5) overestimated it by ≈ 12%. A discretisation-parameter change (not a model or method change). The γ = 3.5 triplet study (partial) is kept in `09_Raw_Data/convergence_gamma3p5/` with `CONVERGENCE_RESULTS_gamma3p5_partial.json`: observed orders 0.8–1.35, i.e. not in the asymptotic range.

## P9-D002 (2026-10-01) — Grid family and uncertainty method
- Radial family R48/M/R192 (48×96, 96×96, 192×96) and angular family T48/M/T144 (96×48, 96×96, 96×144), γ = 5; separate Richardson estimates (observed order, capped to [1, 3]); production grid M = 96×96. Memory limit (2 GB) excludes 192×192.

## P10-D001 (2026-10-01) — Criteria clarified and production matrix frozen
- See `02_Problem_Definition/ACCEPTANCE_CRITERIA_V2_FROZEN.md`: thresholds inherited; QoI interpolation added; D evaluated on t ≤ 6; T4 noise = numerical (grid) uncertainty instead of circle scatter; T5 added; blocks E and B2 labelled exploratory; production matrix `08_Experiments/production_matrix.py`.
- Block E (mechanism ablations, exploratory) runs on grid T48 (96×48, γ = 5) to save ≈ 20 CPU-min; its baseline is the T48 ellipse sweep; the angular error common to all variants (≈ 1.4% at φ = 30°, from C4) cancels in the amplitude comparison.

## P11-D001 (2026-10-01) — Block F added after the gate (before any F result existed): locality test by pulse width
- Reason: in the thin-layer (local) limit the peak over a convex wall is orientation-independent (every tangent direction occurs), so the ellipse's modulation must vanish as the thermal-layer thickness → 0 relative to the tip curvature radius; the statement "stress is a local response" needs a numerical test. Block F (exploratory): wall pulse widths t_w = 0.3, 0.6, 1.2 (baseline), 2.4 t_th; ellipse φ = 90°, 150° (extremes at the baseline) and circle φ = 0, grid T48. Code change: optional `pulse` argument in `run_config` (default = pre-registered pulse; baseline path unchanged; checked by `reproduce.py`). The two production workers already running were not affected; block F is run afterwards. Code freeze addendum: `CODE_FREEZE_v2_blockF.json`.
- **Outcome of block F (recorded after the run):** the modulation A₂ rose only weakly with the pulse width (24.8%, 27.7%, 30.0%, 32.0% for t_w = 0.3, 0.6, 1.2, 2.4) and the circle peak varied by 5.3% (narrowest pulse the outlier). The locality interpretation of the ellipse modulation, proposed before the run, was therefore **not supported**; the manuscript wording was changed after seeing this result (post-result, §25) to "non-local interaction of the heated region with the cavity shape; thin-layer limit not reached".

## P12-D001 (2026-10-01) — Analysis reporting decisions (after production)
- T2 reported twice (quasi-static and full dynamics): quasi-static SUPPORTED (exact scaling), dynamic NOT-SUPPORTED (residual 51.6% at the equal-Λ pair) — the pre-registered strict criterion is not softened; the explanation (O(ε²) inertia correction to a small effect) is an interpretation supported by the extended map (slopes 1.8–2.7) and the quasi-static ablation.
- T4: amplitude quoted from the extrapolated six-orientation sweep (28.7%) with grid-M twelve-orientation value (29.9%) and u_num = 1.31 percentage points; status RESOLVABLE against max(5 u_num, 2%) = 6.56%.
- `analyze_v2.py`: probe-deviation bug (axis order) found and fixed before the final run; numerics summary evaluates the wall-pulse error for t ≤ 6 (the t_w = 2.4 runs of block F carry the n = −1 alias for t > 8, QoI unaffected).

## P7-D002 — USER CONFIRMED (2026-10-01, continuation session)
- The user was asked explicitly and chose to **confirm** P7-D002: the single-pulse Bromwich
  inversion on Re s = 0.9/t_th (replacing the periodic-pulse-train DFT synthesis) stands, and the
  undamped model stands. The flag is resolved; no results change.

## R-D001 (2026-10-01, continuation session) — full re-run on different hardware
- Re-ran, from the frozen source, the whole chain: verification suite + supplement, production
  (150/150 runs), convergence C2/C3/C4, analysis, provenance, figures, supplement, manuscript and
  the reproduction test. Environment: Python 3.11.2 (recorded: 3.13.14) with the identical
  numpy 2.3.5 / scipy 1.17.1 / matplotlib 3.10.9 / python-docx 1.1.2 / openpyxl 3.1.5.
- Result: every scientific quantity is bit-identical (150/150 runs, max QoI relative difference
  0.0; 669 analysis leaves within 1e-9; 8 figures and 5 tables byte-identical; manuscript
  byte-identical). Only CPU/wall timings differ (1–8%). Full record: `RERUN_COMPARISON.md`.
- Delivered outputs were snapshotted to `baseline_provided/` before anything was overwritten.

## R-D002 (2026-10-01) — one-line portability edit to `13_Manuscript/ms_results.py`
- Cause: one f-string (the "Model scope" paragraph) nests single quotes inside a single-quoted
  f-string. That is PEP 701 syntax, legal only on Python ≥ 3.12, so the file cannot be imported
  on Python 3.11 (`SyntaxError: f-string: unmatched '['`); `build_manuscript.py` failed.
- Fix: inner `v['peak_change_R80_to_R160']` / `v['D_change_R80_to_R160']` / `CR.get('C3', {})`
  changed to double quotes only. No expression, number, formula or scientific content changed.
- Proof that it is cosmetic: the manuscript rebuilt with the edited file is byte-identical
  (md5 590301281df9ca130a6ec9ae5fecb2c8) to the delivered manuscript.
- Rationale for editing instead of changing environment: the recorded environment is Python
  3.13.14, where the original file is valid; CPython 3.13 could not be installed in this sandbox
  (no build headers, no package repository access). The edit makes the file valid on 3.11–3.13.

## R-D003 (2026-10-01) — code-freeze addendum
- `CODE_FREEZE_v2_blockF.json` was stale: `13_Manuscript/{build_manuscript,ms_results,ms_static}.py`
  had been edited after it (they implement the CORRECTIONS_LOG corrections) with no addendum.
- `06_Source_Code/CODE_FREEZE_v2_final.json` now records the current state of all 24 frozen files
  including those three and the R-D002 edit. Earlier freezes (`_v2_gate`, `_v2_blockF`) are kept
  unchanged for provenance.

## R-D004 (2026-10-01) — path bootstrap instead of patching frozen files
- 15 scripts hard-code `/home/user/PAPER_PROJECT` and `/home/user/work/handoff`; three of them
  (`run_tests.py`, `analyze_v2.py`, `make_figures.py`) are inside `CODE_FREEZE_v2_blockF.json`, so
  they were NOT edited. `bootstrap_paths.sh` (repository root) recreates the two paths as symlinks;
  all frozen SHA-256 hashes still verify.

## P13-D001 (2026-10-01) — Manuscript and packaging decisions
- Working target IJHMT (handoff D017; user-owned); abstract 231 words (limit 250, official guide); highlights ≤ 85 characters; AI-use declaration is a TEMPLATE for the authors; authors/CRediT/funding/conflicts left as placeholders; no repository DOI invented.
- Statements in the handoff manuscript about expansion consistency, MFP, K eigenvalues, reference metadata were corrected (CORRECTIONS_LOG).
- Cumulative packages PACKAGE_PHASE_07…13 are reconstructed at the end of the session (the per-phase snapshots were not taken when the phases ended) — stated in each MANIFEST.
