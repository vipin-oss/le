# PROJECT_STATE_PHASE_08 — Verification complete; production in progress (30 Sep 2026)

## Outcome
V0–V7 verification suite PASSED on the corrected conservative flux-form operator
(V2 = PARTIAL per pre-defined plan handling). Production matrix (38 runs) executing
at 96×48. No physical-validation claims (NOT_AVAILABLE, recorded).

## What was done (this phase)
1. Root-cause chain for V6/V7 failure (parity null mode of composed D@D) — documented
   DECISION_LOG D014; conservative operator `src/cg_ops.py` (MappedOps) implemented.
2. Subsequent fixes: FD metrics (commuting mixed partials), eta-half uy() sign, grid
   domain R=80·a (was 1 nm→80 m absolute), V6 exact-solution units, J-row scaling +
   row equilibration (SI round-off), hysteretic damping η_d=0.05 for dynamic runs.
3. Suite re-run (logs/verify_rerun_v3.log, 403 CPU-s): V0 PASS, V1 PASS, V2 PARTIAL
   (med-fine 2.35% circle / 6.80% ellipse), V3 PASS 6.26e-14, V3b PASS, V4 PASS,
   V5 PASS 1.09e-7, V6 PASS 9.5e-6, V7 PASS 0.68%.
4. Pre-registered production design (D015): R=80a (deviation justified causally),
   frozen pulse t0=2.5 t_th, tw=1.2 t_th, QoI window t≤6 t_th, matrix A/B/C/D = 38 runs.

## Evidence for next phase
- data/VERIFY.json (final V0–V7), logs/verify_rerun_v3.log, data/PROD/*.json + *.npz
  (production per-run QoIs + time series), data/PROD/PRODUCTION_SUMMARY.json.
- Code: src/cg_ops.py (operator), src/cg_solver.py (HarmonicSolver + row equilibration
  + energy_coupling flag), run_verify.py (suite), run_production.py (matrix).

## Known limitations / honest status
- V2 PARTIAL: ellipse σ̂ grid uncertainty ~6.8% (96 vs 192) → T4 amplitudes need
  192×96 confirmatory spot checks or Richardson treatment; documented per plan.
- η_d=0.05 damping is a documented regularization of undamped finite-domain
  resonances; sensitivity {0.02, 0.1} to be reported with claims.
- α5 (thermal shear expansion) unmeasured → 0 (LIMITATION); c_p ESTIMATED;
  τ_q HYPOTHETICAL (dimensionless-study label mandatory).
- Physical validation NOT_AVAILABLE (no β-Ga₂O₃ transient/cavity dataset located).

## Exact next action
1. Finish production (38 runs) → analysis (H1–H5 / T1–T4): φ-covariance table,
   D(Λ) monotonicity + size-collapse, feedback bound vs 5δ, ellipse amplitude vs noise,
   angular modes (H5), η_d sensitivity (2 configs × 2 η).
2. 192×96 confirmatory spot checks for T4 (2 runs) if ellipse amplitude near threshold.
3. Figures + MANUSCRIPT skeleton (Phase 12–13 gates: full-text comparison with the
   closest prior work R2.3/R1.1 still REQUIRED before novelty claims).

## Addendum — production + analysis complete (30 Sep 2026, later same day)
- Production 38 runs DONE (1039 CPU-s). data/ANALYSIS.json + data/ANALYSIS_TABLE.md + figures/fig1-4.
- T1/H1: circle covariance machine-class (V3 6.3e-14; 0/90° pair 4e-10); peak-scatter 0.3% = sampling artifact (documented).
- T4/H2: ellipse σ̂(φ) amplitude 36.6% (96×48) / 32.7% (192×96 spot) ≫ 2% → RESOLVABLE, grid-robust. HEADLINE RESULT.
- T2/H3: pure-Λ collapse REFUTED (78% residual at equal Λ); D(Λ) monotone within each size family (D: 3e-4→0.103 for Λ 0.03→3.2) → two-parameter (Λ,ε) validity map reported.
- T3/H4: interior θ(r≈2a) coupling deviation 2.2e-4 ≤ 5δ=5.4e-3 → WITHIN-BOUND (≈0.2δ).
- H5: m2/m0: iso-circle 5e-11 (exact null), aniso-circle 0.085, iso-ellipse 0.204, aniso-ellipse 0.309 → interaction grows m≥2 ✓.
- η_d sensitivity {0.02,0.1}: QoIs shift ≤0.2% → conclusions ROBUST to damping choice.

## Addendum 2 — Phase 11–12 closed (30 Sep 2026)
PRIOR_WORK_COMPARISON_R2.md + JOURNAL_SCREENING.md + SEARCH_LOG §live-2026-09-30 +
RECOVERY_CRYSTAL_GEOMETRY_01.zip (121 files, 2.3 MB, sha256 manifest) written.
PROJECT_STATE_PHASE_11.md / _12.md self-contained records.
