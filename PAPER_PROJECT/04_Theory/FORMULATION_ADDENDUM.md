# FORMULATION_ADDENDUM — model statement, dimensionless structure, admissibility (Phase 3 refresh, 2026-10-01)

Scope: the physical model of `PROJECT_CRYSTAL_GEOMETRY_01/MATHEMATICAL_FORMULATION.md` is **unchanged**. This addendum (i) restates it in the form actually solved, (ii) states the initial condition that the handoff pipeline did not implement, (iii) records the dimensionless structure and two analytical results that govern how the numerical results must be read, and (iv) covers thermodynamic admissibility, well-posedness, dimensions and limiting cases (MASTER_PROMPT §30–33), which the handoff lacked as separate artefacts. Labels: ESTABLISHED = published theory; PROPOSED = defined by this project; ANALYTICALLY_CHECKED = derived/checked here; RUN_SUCCESS = tested (see `07_Tests/TEST_REPORT.md`).

## 1. Model (plane strain in the a–c plane, linear, small strain)
Unknowns θ (temperature rise above T0 = 293 K), u = (u₁, u₃). Voigt strain ε = (ε₁₁, ε₃₃, γ₁₃).
- Constitutive: σ = Q ε − β θ, with Q the 3×3 plane-strain block of the monoclinic stiffness (C11, C13, C15, C33, C35, C55; only these six of the 13 Adachi constants enter) and β = C·α the thermal-stress vector (needs C12, C23, C25 through the b-axis expansion α₂; α₅ = 0 assumed). ESTABLISHED (anisotropic thermoelasticity, Biot 1956).
- Momentum: ∇·σ = ρ ü.
- Heat: Cattaneo–Vernotte flux law q + τ q̇ = −K∇θ with energy balance −∇·q = ρ c_p θ̇ + T0 β:ε̇ gives ∇·(K∇θ) = (1 + τ∂ₜ)(ρ c_p θ̇ + T0 β:ε̇), i.e. the Lord–Shulman equation with one relaxation time (ESTABLISHED; anisotropic form: Dhaliwal & Sherief 1980). In the Laplace domain: ∇·(K g(s) ∇θ) = s(ρ c_p θ + T0 β:ε), g = 1 (Fourier), g = 1/(1 + sτ) (CV/LS).
- MCV3-type kernel g = ½/(1 + ½sτ) + ½/(1 + 2sτ): **PROPOSED** (exploratory sensitivity kernel, not derived from a free energy). It is positive real (each term is), hence a passive flux law; this is the only admissibility property claimed for it.
- Boundary conditions: cavity wall θ = p(t), traction-free (σ·n = 0); outer boundary R = 80a: θ = 0, u = 0 (clamped, cold).
- **Initial condition:** quiescent medium, θ = 0, u = u̇ = 0 as t → −∞; p(t) = exp(−((t − t₀)/t_w)²), t₀ = 2.5 t_th, t_w = 1.2 t_th on the whole real line (no truncation step at t = 0).
- Geometry: circle radius a, or equal-area ellipse of semi-axes a√χ (along the crystal-a direction at φ = 0) and a/√χ, χ = 2; crystal rotated by φ in the a–c plane.
- Material data (all PARAMETER_TABLE; classification per MASTER_PROMPT §81): Cij — literature (Adachi 2018, verified against the paper); K = [[12.13, −0.992], [−0.992, 14.09]] W/(m·K) — literature (Klimm 2023, verified); α = (1.54, 3.37, 3.15)×10⁻⁶ 1/K — literature, secondary-quoted (Orlandi 2015; **alternative 298 K values are ≈10× smaller, Cheng 2018 abstract** → sensitivity block E1); ρ = 5880 kg/m³ — literature; c_p = 560 J/(kg·K) — assumed (literature spread 485–540); τ = 1–20 ps — hypothetical (sensitivity-only).

## 2. Dimensionless groups
t_th = a²/κ̄, κ̄ = √det K/(ρ c_p) = 3.9588×10⁻⁶ m²/s (t_th = 25.26 ps at a = 10 nm). Λ = τ/t_th = τκ̄/a². ε = κ̄/(c_ref a), c_ref = √(C33/ρ) = 7686 m/s (ε = 0.0515 at a = 10 nm). δ = T0 β·β/(ρ c_p C̄) = 1.078×10⁻³ (dimension check: K·(Pa/K)²/((Pa/K)·Pa) = 1 ✓). χ, φ. Elastic echo (first return of the longitudinal wave to the wall): t_echo = 2(R/a − 1) ε t_th = 16.3, 8.14, 4.07, 1.63 t_th for a = 5, 10, 20, 50 nm.

## 3. Two analytical results (ANALYTICALLY_CHECKED; numerical confirmation cited)
**(R1) Scaling / collapse.** For ρ → 0 (quasi-static elasticity) and δ → 0 (no thermoelastic feedback) the temperature problem in the variables (r/a, t/t_th) depends only on Λ, χ, φ and R/a, and the stress per unit wall temperature is a linear functional of θ with no further length scale. Hence the thermal-memory deviation D = max|σ_CV − σ_F|/max|σ_F| is a function of Λ alone: pre-registered hypothesis H3 ("collapse in Λ alone") is an **identity of the quasi-static uncoupled limit**; the numerical question is only the size of the O(ε) inertial/echo and O(δ) feedback corrections. (Confirmed: tests BQS pair, `10_Processed_Data/ANALYSIS_V2.json`.)
**(R2) Local–instantaneous wall response.** For the isotropic circle in quasi-static plane strain the Lamé solution with free wall and clamped outer boundary gives
 σ_θθ(a,t) = −2μ g_T p(t) − 2(λ + m) g_T F(t) / (R² + (λ + m)a²/(2μ)),  g_T = γ_T/m, m = λ + 2μ, γ_T = (3λ + 2μ)α, F = ∫ₐᴿ r θ dr.
The second term is O((a/R)²) ≈ 1e-3 of the first; so for the **isotropic circle** the peak wall hoop stress is, to 0.1%, the local constraint response −(2μγ_T/m) p(t_peak) (984.6 kPa/K for the isotropic control; 985.7 kPa/K including the far-field term) and is insensitive to how heat is conducted into the bulk; the thermal-memory effect on it is therefore small (D ≲ 1e-2 in the production data). For the anisotropic circle the response is only approximately local (peak varies ≤ 5.4% between pulse widths 0.3 and 2.4 t_th; stress/temperature ratio within ≈ 4% for 2 ≤ t ≤ 3). For the ellipse locality fails: the isotropic ellipse has a peak ≈ 1.5× that of the isotropic circle, and the crystal-orientation modulation (≈ 29%) decreases only weakly when the heated layer is thinned (pulse-width test: 32.0% → 24.8% for t_w = 2.4 → 0.3 t_th); in the thin-layer limit every tangent direction would occur and the modulation would have to vanish, but that limit is not reached in the accessible range (layer thickness ≳ tip radius of curvature 0.35a). Wall hoop stress under a prescribed wall temperature is therefore a poor probe of the heat-conduction law; interior stresses or heat flux are the discriminating observables.

## 4. Thermodynamic admissibility (MASTER_PROMPT §30)
| Property | Status |
|---|---|
| Q symmetric positive definite (Mandel form), all φ | ANALYTICALLY_CHECKED + RUN_SUCCESS (test U3: min eigenvalue 126.6 GPa, spectrum invariant under rotation to 1e-10) |
| K symmetric positive definite, all φ | RUN_SUCCESS (eigenvalues 11.72, 14.50 W/(m·K); the handoff's 11.36/14.86 is a documentation error) |
| ρ, c_p, T0 > 0; τ ≥ 0 | by construction |
| LS/CV model: uniqueness and energy decay for anisotropic media under these conditions | ESTABLISHED (Dhaliwal & Sherief 1980) — relied upon, not re-derived |
| Flux kernels g(s): Re g(s) > 0 for Re s ≥ 0 (passivity) | ANALYTICALLY_CHECKED: Re[1/(1+sτ)] = (1 + τ Re s)/|1 + sτ|² > 0; sums with positive weights keep the property (MCV3) |
| Free-energy / Clausius–Duhem derivation, entropy production for MCV3 | **NOT DONE** (MCV3 stays labelled exploratory) |
| Undamped model (no hysteretic damping): energy conservation up to the dissipation of the heat flux | consistent with LS theory; hysteretic damping of the handoff removed (P7-D002) |

## 5. Well-posedness (MASTER_PROMPT §31)
Second-order coupled hyperbolic–parabolic-type system (LS: hyperbolic, finite speeds). Boundary conditions complete: one thermal condition on each boundary (Dirichlet) and two mechanical conditions on each (traction-free wall; clamped outer). Initial data zero. Uniqueness: Dhaliwal & Sherief (ESTABLISHED). Existence/stability not analysed here; numerical stability is demonstrated by convergence (Phase 9) and by evaluating the operator on Re s = γ > 0 where the undamped finite-domain resonances are bounded away from the evaluation line.

## 6. Dimensional audit (MASTER_PROMPT §33)
σ [Pa] = Q [Pa]·ε [–] − β [Pa/K]·θ [K]; Λ, ε, δ, χ dimensionless (above); P(s) = √π t_w e^{(s t_w/2)² − s t₀} is the Laplace transform of a dimensionless pulse; transfer values H are per kelvin of wall amplitude (hoop H in Pa/K); all stresses in the results are Pa per K of pulse amplitude, multiply by the amplitude in kelvin.

## 7. Limiting cases and their tests
α = 0 ⇒ u = σ = 0 (V4) · τ → 0 ⇒ Fourier (V5) · ω → 0 ⇒ steady log profile and steady Lamé stress (V6, V7, V8 against closed forms) · isotropic circle ⇒ axisymmetric exact/semi-analytic 1-D references (V9, V11) · crystal rotation ⇒ exact covariance of the circle for lattice rotations (V3, T1) · plane-strain block and rotation of Q, β vs independent 6×6 / 3-D rank-4 assemblies (U0, U1) · real-system symmetry (V12) · Bromwich inversion vs ODE/time-domain references (U4–U8).

## 8. What is not claimed
No physical validation (APPLICABLE — EVIDENCE_UNAVAILABLE); no claim that Fourier or CV conduction is valid for 5–50 nm cavities in β-Ga₂O₃ (phonon mean free paths up to ~0.7–1 µm; gray estimate ~3 nm); τ, c_p and the expansion set are parameters with uncertainty, so absolute stresses carry a parameter uncertainty of up to an order of magnitude through α; relative effects (modulation, ratios, scaling) are the content of the study.
