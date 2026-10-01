# PROJECT_STATE_PHASE_09 — Convergence and robustness (2026-10-01)

## Phase 9 — status PASS (numerical uncertainty quantified in Phase 12)
**Completed:** mesh-direction / clustering study C4 (`10_Processed_Data/CONVERGENCE_DIRS.json`, φ = 30° ellipse): radial refinement at γ = 3.5 changes the peak by −8.7%, angular by +3.0%; γ = 5 vs 6.5 differ by 0.7% → γ = 5 adopted (P9-D001); γ = 3.5 triplets (orders 0.8–1.35) kept in `09_Raw_Data/convergence_gamma3p5/`; production grid family R48/T48/M/R192/T144 with separate radial/angular Richardson; Bromwich-plan independence (C2) and outer-radius sensitivity (C3): `CONVERGENCE_RESULTS.json`; verification-level convergence orders (V6–V11) ≈ 2.
**Stability:** no instability observed; solver backward errors ≤ 1e-16 relative; wall-pulse reconstruction error 6.3e-9 in all runs.
**Files:** `05_Numerical_Method/CONVERGENCE_REPORT.md`, `STABILITY_REPORT.md`.
**Next:** Phase 10.

## Common context (self-contained recovery summary, MASTER_PROMPT §65)
- **Project:** β-Ga₂O₃ cavity thermoelasticity (circular vs equal-area elliptical cavity, monoclinic crystal, a–c plane, Fourier / Cattaneo–Vernotte / two-relaxation-time conduction) → verified continuum parametric study; target manuscript for IJHMT (journal choice user-owned; D017 working target).
- **Research type / evidence route:** computational scientific study with analytical verification anchors (§15). Verification (Track A): exact + independent 1-D references, grid studies. Physical validation: **APPLICABLE — EVIDENCE_UNAVAILABLE**.
- **Equations / assumptions / method:** `04_Theory/FORMULATION_ADDENDUM.md`, `05_Numerical_Method/NUMERICAL_METHOD_V2.md`; model unchanged from the handoff; time reconstruction by Bromwich inversion (P7-D002, **flag for user**); undamped; grid γ = 5 (P9-D001).
- **Baseline:** `/home/user/work/handoff/` (read-only, 304 files, 303/303 SHA-256). Handoff defects fixed: rotate_Q_beta sign (G1), T1 forced PASS (G2), periodic-synthesis artefact (G3), H3 evaluated on the artefact and on the full window (G4), documentation (G5).
- **Approvals:** D013 blanket authorization for phases 1→13 (user message 2026-10-01 "Continue Phases 7→13 under D013"); user-owned: model changes, compute > 4 CPU-h, journal, submission.
- **Decision / change history:** `DECISION_LOG.md`, `CHANGELOG.md` (this folder); handoff D001–D018 in the handoff.
- **Rejected ideas:** `REJECTED_IDEAS.md` (this folder).
