# PROJECT_STATE_PHASE_12 — Scientific analysis (2026-10-01)

## Phase 12 — status see below
**Frozen criteria evaluated** (`10_Processed_Data/ANALYSIS_V2_TABLES.md`): T1 PASS; T4 RESOLVABLE (A12(M) = 29.87%, extrapolated 6-φ amplitude 28.75%, u_num = 0.013111431611462776); T2 quasi-static SUPPORTED, dynamic NOT-SUPPORTED; T3 WITHIN-BOUND.
**Central story:** `CENTRAL_STORY.md` (this folder).
**Next:** Phase 13 manuscript.

## Common context (self-contained recovery summary, MASTER_PROMPT §65)
- **Project:** β-Ga₂O₃ cavity thermoelasticity (circular vs equal-area elliptical cavity, monoclinic crystal, a–c plane, Fourier / Cattaneo–Vernotte / two-relaxation-time conduction) → verified continuum parametric study; target manuscript for IJHMT (journal choice user-owned; D017 working target).
- **Research type / evidence route:** computational scientific study with analytical verification anchors (§15). Verification (Track A): exact + independent 1-D references, grid studies. Physical validation: **APPLICABLE — EVIDENCE_UNAVAILABLE**.
- **Equations / assumptions / method:** `04_Theory/FORMULATION_ADDENDUM.md`, `05_Numerical_Method/NUMERICAL_METHOD_V2.md`; model unchanged from the handoff; time reconstruction by Bromwich inversion (P7-D002, **flag for user**); undamped; grid γ = 5 (P9-D001).
- **Baseline:** `/home/user/work/handoff/` (read-only, 304 files, 303/303 SHA-256). Handoff defects fixed: rotate_Q_beta sign (G1), T1 forced PASS (G2), periodic-synthesis artefact (G3), H3 evaluated on the artefact and on the full window (G4), documentation (G5).
- **Approvals:** D013 blanket authorization for phases 1→13 (user message 2026-10-01 "Continue Phases 7→13 under D013"); user-owned: model changes, compute > 4 CPU-h, journal, submission.
- **Decision / change history:** `DECISION_LOG.md`, `CHANGELOG.md` (this folder); handoff D001–D018 in the handoff.
- **Rejected ideas:** `REJECTED_IDEAS.md` (this folder).
