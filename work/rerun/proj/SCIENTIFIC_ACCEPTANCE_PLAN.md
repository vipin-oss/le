# SCIENTIFIC_ACCEPTANCE_PLAN — Phase 1 (frozen before confirmatory runs; §24–25)
Date: 30 September 2026. Any change after confirmatory outputs seen = post-result, must be logged (PILOT_CHANGELOG rules apply).

1. **Research type:** computational scientific study (evidence route per §15) + analytical verification anchors.
2. **Exact contribution:** (i) verified coupled anisotropic generalized-thermoelastic cavity solver (monoclinic plane-strain, circle/ellipse, orientation φ); (ii) φ×χ×Λ/ε response study incl. symmetry-covariance audit; (iii) size-dependent validity map of Fourier vs CV/MCV3-type; (iv) honest upper bound on thermoelastic feedback (δ~1e-3).
3. **Scientific significance:** separates geometry effects, crystal-orientation effects, and thermal-memory effects in transient cavity thermoelasticity of a real monoclinic crystal — previously entangled in the literature (per bounded search).
4. **Unresolved limitation addressed:** no prior systematic orientation-mismatch × shape × memory analysis located (SEARCH_LOG.md gap statement, PROVISIONAL).
5. **Falsifiable questions:** H1–H5 (PROBLEM_DEFINITION.md).
6. **Decisive tests:** V1–V7 verification (below) + T1: σ̂(φ) for circle is constant to ≤1e-10 rel (covariance identity) while ellipse σ̂(φ) varies beyond numerical noise; T2: |Fourier−CV| at wall collapses vs Λ across sizes (similarity) with stated residual; T3: coupled-vs-uncoupled temperature difference ≤ C·δ bound.
7. **Admissibility requirements:** K SPD; plane-strain C block SPD; τ>0 for CV/MCV3 → positive dissipation; linear small-strain; ΔT/T0≪1; continuum a≥5nm flagged (THERMODYNAMIC_ADMISSIBILITY.md).
8. **Verification pathway:** V1 operator dispersion; V2 grid convergence; V3 rotation covariance; V4 α=0 null; V5 τ→0 limit; V6 steady log-solution (circle isotropic) exact; V7 static mechanical patch test (uniform θ ⇒ known stress). All pre-run.
9. **Physical validation:** NOT_AVAILABLE — no experimental transient or cavity dataset for β-Ga2O3 located; elastic/transport data are the material input, not validation targets. PHYSICAL_VALIDATION_PLAN.md records this scientifically. Consequence: claims restricted to verified computation within stated model; "physical validation" never claimed.
10. **Baselines:** B1 isotropic matched-modulus control; B2 uncoupled (no thermoelastic feedback); B3 Fourier (Λ=0).
11. **Ablations:** coupling on/off (4 corners); K13 on/off (conductivity misalignment); C15,C35 on/off (monoclinic shear-extension); α_b row on/off (out-of-plane expansion restraint).
12. **Primary QoIs:** σ̂(max wall hoop stress), θ*, t*, angular modes m=1..8, wall-layer gradient G(t0+tw), phase offset Δt(σ−θ).
13. **Error metrics:** absolute/relative for σ̂ (norm |·|/max|·|), angle L1 for θ*, mode-amplitude relative with absolute floor (1e-3 of m=0).
14. **Numerical accuracy required:** σ̂ grid-convergence ≤2% (production grid), covariance identity ≤1e-10, V6 log-check ≤1% of range, V5 ≤1e-3.
15. **Acceptance criteria (quantity-specific, confirmatory):**
   - T1: |σ̂(φ)−σ̂(φ′)|/σ̂ ≤ 1e-8 for circle (all φ,φ′) on the 90° discrete-rotation identity [refined pre-freeze: machine-precision-class criterion allowing LU roundoff; the 37° continuous test is secondary O(h²)]. PASS required for H1.
   - T2 (memory): define D(Λ)=max_t|σ̂_CV(Λ)−σ̂_Fourier|/σ̂_Fourier at wall; H3 supported if D(Λ) is monotone in Λ for Λ∈[0.01,1] AND size-collapse residual |D(a,τ)−D(Λ)| ≤ 25% of D across the a-sweep. NOT a universal 5% rule.
   - T3 (feedback bound): max relative change of wall-temperature field with coupling on vs off ≤ 5·δ (computed δ per run) — bound claim, either direction.
   - T4 (shape mismatch, H2): ellipse σ̂(φ) variation amplitude A_φ ≥ max(5×grid-noise, 2%) of σ̂ mean → "resolvable"; if A_φ < noise threshold → report NULL with resolution limit.
16. **Calibration strategy:** none (no fitting; all parameters sourced or labeled HYPOTHETICAL/ESTIMATED).
17. **Identifiability:** parameters separated by construction (φ, χ, Λ, ε independent axes in matrix; a-sweep moves along Λ∝ε² curve — recorded).
18. **Uncertainty:** material ± from Adachi errors → σ̂ sensitivity via linear propagation on ±Cij (exploratory); c_p ESTIMATED → report vs Λ,ε (c_p-independent axes); digitization N/A (no digitized inputs in this project); grid error from V2.
19. **Continue:** all V1–V7 PASS (or documented partial with bounded error) → production.
20. **Revise:** any V fails twice substantively → method revision logged; two-iteration valve (§77) then STOP-to-user if critical.
21. **Reject/abandon:** if covariance identity cannot be reached (geometry/metric bug), or SPD fails for real tensors, or production compute estimate exceeds thresholds (4 CPU-h/1 GPU-h/5 GB) → STOP for user approval.

**Freeze record:** PLAN_FREEZE.json with hashes written BEFORE any confirmatory output (see logs/).
