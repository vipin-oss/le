# VERIFICATION_PLAN — Phase 2 (pre-defined; §26–27)
Date: 30 September 2026. Each case: source, equations, solver, criterion, interpretation. Confirmatory vs exploratory marked.

## V1 — Operator dispersion/consistency (CONFIRMATORY)
Plane-wave probe of discrete thermal + elastic operators (1D periodic line extracted from the metric FD core, κ-analytic): numerical phase speed vs analytic s_T(k)=√(κ̂(ω,k)) thermal (Fourier: diffusive), elastic bulk speed c_L(k)=√(C̄11/ρ). Criterion: ≤2% speed error for k·h ≤ 0.5; observed order ≥1.8. Source: analytic (our derivation). Implementation: src/verify_dispersion.py.

## V2 — Grid convergence (CONFIRMATORY)
QoI σ̂ and modes on N×M ∈ {48×24, 96×48, 192×96} for 2 fixed configs (circle φ=45 Λ=0.3; ellipse χ=2 φ=30 Λ=0.3). Criterion: |σ̂_fine−σ̂_med| ≤ 2% of σ̂_fine (production grid = 96×48; if fails, production at 192×96 with cost re-check). Source: Richardson-style self-convergence (no external reference).

## V3 — Rotation covariance (CONFIRMATORY; identity test)
Circle + uniform wall pulse; rotate ALL tensors (K,C,β) by φ′=37° (non-symmetric angle); solution must rotate: σ̂ invariant to ≤1e-10 rel; field map rotated back must match to ≤1e-10 (discrete circle is exact on polar grid). This is an exact discrete identity if metrics/covariance implemented correctly. Source: group-theoretic identity (our derivation).

## V4 — Uncoupled null (CONFIRMATORY; exact)
Set α→0 (β=0): temperature field identical to pure-anisotropic-conduction solve; u≡0, σ≡0 to machine precision (≤1e-12 rel to stress scale). Source: exact.

## V5 — Memory limit (CONFIRMATORY; exact limit)
CV with τ=1e-6·t_th and MCV3 with (τa,τb)=(1e-6,2e-6)t_th vs Fourier: wall fields ≤1e-3 rel. Source: model limit (exact asymptotically).

## V6 — Steady anisotropic conduction, circle (CONFIRMATORY; analytic)
Steady (ω=0) isotropic-K, circle: θ(r)=θ_w·ln(R_out/r)/ln(R_out/a) on annulus [a,R_out]. FD vs analytic ≤1% of range. Anisotropic-K generalization: conformal/linear-map analytic for confocal ellipse approx — SECONDARY (≤5% expected from non-confocal outer). Source: textbook Laplace solution (derived in SYMBOLIC_CHECKS.md).

## V7 — Static mechanical patch test (CONFIRMATORY; analytic)
Uniform θ field on full domain with free cavity+fixed outer: σ from plane-strain thermoelastic formula σ = −βθ + C:ε(u), with u from static solve; energy identity ∫σ:ε = ∫βθ·tr… simpler patch: uniform θ, domain without cavity (solid disc), fixed outer → u=0 exactly? No: uniform θ with free inner and fixed outer gives a known radial field for isotropic: use that (derived closed form for annulus isotropic thermal expansion, Timoshenko-type). Criterion ≤1.5%. Source: derived (SYMBOLIC_CHECKS.md).

## Benchmarks (Phase 8, external-ish)
- B-FG: Florence-Goodier steady circular-hole uniform-heat-flow hoop-stress formula (J. Appl. Mech. 26 (1959) 293–294) — STEADY limit of our solver (insulated hole variant differs from our Dirichlet wall — use only as order-of-magnitude sanity, NOT confirmatory; recorded). 
- B-Huang: PILOT_HUANG_2025_01 source-case curves — NOT a direct benchmark of this geometry; used only as code-family precedent (the thermal operators are the same family).

## Physical validation: NOT_AVAILABLE (see PHYSICAL_VALIDATION_PLAN.md)
## Error metrics & criteria per SCIENTIFIC_ACCEPTANCE_PLAN items 13–15.
