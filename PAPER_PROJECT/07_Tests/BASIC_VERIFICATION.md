# BASIC_VERIFICATION — Phase 7 summary (2026-10-01; numbers in `TEST_REPORT.md` / `TEST_RESULTS.json`)

| Component class (§37) | Tests | Status | Remark |
|---|---|---|---|
| Constitutive functions | U0 (plane-strain block vs independent 6×6 Voigt assembly), U1 (rotation of Q and β vs independent 3-D rank-4 rotation, 27 angles), U3 (admissibility: Q SPD in Mandel form, K SPD, spectra rotation-invariant) | PASS | the shipped `rotate_Q_beta` fails U1 at 1.7e-3 (one cross-term sign) — U1b confirms the test can fail |
| Derivatives / metrics | V0 (linear-field metric consistency), V0b (same criterion on production grids), V1 (stencil dispersion) | V0 **FAIL** on the handoff-style 96×48 grid for χ = 2 (5.03e-3 vs 5e-3, angular-resolution dominated, 2nd-order convergent); V0b PASS (≤ 3.6e-3; production grid M: 1.5e-3); V1 PASS | reported, not hidden |
| Matrices / residuals | backward error after refinement (≤ 1e-16 relative in every run); iterative-refinement diagnostic (`diagnostics/diag_covariance_floor.py`: floor 1e-8 → 1e-14) | PASS | |
| Boundary conditions | V3 (θ, u, wall hoop covariance, all lattice φ, complex s: 6.5e-14), V3p (test power), V3d (peak-stress invariance 3.6e-15), V4 (β = 0 ⇒ σ = 0), V7 (uniform-θ annulus) | PASS | V3 at φ = 90° alone is blind to the rotation bug (6e-14 vs 3.0e-3 at 45°) |
| Conservation / limiting behaviour | V5 (τ → 0 ⇒ Fourier: 4e-7), V6 (steady log profile), V8 (steady thermal-gradient load vs closed form, order ≈ 2) | PASS | V8 closes the gap that the handoff suite V0–V7 had for the gradient-load path |
| Solver / transform components | V12 (conjugate symmetry 1.7e-15), U4–U8 (Bromwich inversion: identity, damped oscillator vs ODE, contour independence, vs time-domain Crank–Nicolson), U7 (1-D reference vs closed form) | PASS | |
| End-to-end single pulse | V11 (isotropic circle vs time-domain reference; peak error 1.2% / 0.27% / 0.07% on 48×24 / 96×48 / 192×96, order ≈ 2), V9a/d/e (dynamic coupled problem, Fourier/CV/MCV3, and D accuracy), V9b, V9c | PASS | |
Verification (Track A) only; physical validation APPLICABLE — EVIDENCE_UNAVAILABLE (see `03_Validation/VALIDATION_RESULTS.md`).
