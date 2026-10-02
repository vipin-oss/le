# MATHEMATICAL_FORMULATION — Phase 3 (+ EQUATION_INVENTORY content)
Date: 30 September 2026. Labels: [L]=established literature, [D]=derived here, [P]=proposed extension (with limits).

## 1. Governing equations (time domain, small-strain coupled thermoelasticity)
(L1)[L] Momentum: σ_ij,j = ρ ü_i  (i,j∈{1,3}; 2D plane strain, fields independent of x2=b)
(L2)[L] Stress law: σ_ij = C_ijkl ε_kl − β_ij θ,  ε_kl = ½(u_k,l+u_l,k)
(L3)[L] β_ij = C_ijkl α_kl (thermal-stress moduli; Voigt: β_m = C_mn α_n)
(L4)[L] Energy: ρ c_E θ̇ + T0 β_ij ε̇_ij = −q_i,i
Plane-strain effective 2D C (monoclinic C2/m, unique axis b, plane x1-x3) [D from Adachi Voigt]:
  σ11 = C11 ε11 + C13 ε33 + C15 γ13 − β1 θ
  σ33 = C13 ε11 + C33 ε33 + C35 γ13 − β3 θ
  σ13 = C15 ε11 + C35 ε33 + C55 γ13 − βs θ      (γ13=2ε13)
  β1 = C11α1 + C12α2 + C13α3 + C15α5 ;  β3 = C13α1 + C23α2 + C33α3 + C35α5 ;  βs = C15α1 + C25α2 + C35α3 + C55α5   (α5=0 here)
  (out-of-plane reaction σ22 = C12ε11+C23ε33+C25γ13 − (C12α1+C22α2+C23α3)θ — not solved, recorded)
Derivation check [D]: specialises to isotropic β_ij = (3λ+2μ)α δ_ij for C isotropic, α isotropic ✓ (SYMBOLIC_CHECKS).

## 2. Heat flux laws (the "recent heat conduction model" family)
(L5)[L] Fourier: q = −K∇θ,  K 2×2 SPD (real β-Ga2O3 a-c block, K13≠0).
(P1)[P] CV (Cattaneo-Vernotte / Lord-Shulman-type):  τ_q q̇ + q = −K∇θ   (τ_q>0; K from [L]).
(P2)[P] MCV3-type two-channel (Huang-2025 Eq-family, our verified equivalent): q = q_a+q_b,
      (1+τ_a ∂t) q_a = −w_a K ∇θ,  (1+τ_b ∂t) q_b = −w_b K ∇θ,  w_a+w_b=1 (w_a=w_b=1/2 as verified in pilot reduction; MCV5→CV(2k) identity preserved).
[P] extension label: the 1D verified operators (Huang-2025, pilot-verified) act on each tensor component with the SAME scalar memory factor g(ω); for isotropic K and 1D fields they reduce EXACTLY to the verified 1D transfer functions (EQUATION_TO_CODE_MAP test T-reduce). No tensor-valued memory (unconstrained by data).

## 3. Harmonic (frequency-domain) form — solver equations [D]
Fields ∝ e^{iωt}, complex amplitudes (θ, u1, u3):
  (H1) Momentum: (C_ijkl u_k,l − β_ij θ)_,j + ρ ω² u_i = 0
  (H2) Heat:  ∇·(K g(ω) ∇θ) = iω [ρ c_E θ + T0 β_ij ε_ij(u)]
      g(ω)=1 (Fourier); 1/(1+iωτ_q) (CV); ½/(1+iωτ_a)+½/(1+iωτ_b) (MCV3).
  Derivation: L4 with q=−K g ∇θ ⇒ −∇·q = iω(ρcθ+T0β:ε) ⇒ ∇·(K g ∇θ) = iω(...). For CV verify: τ q̇+q=−K∇θ ⇒ q̂=−K∇θ/(1+iωτ) ⇒ g=1/(1+iωτ) ✓ reduces to pilot M/N family (T-reduce).
  Note [P/D]: the coupling term uses the SAME memory factor as the flux law (consistent with Huang-2025 "M acts on both thermal and strain-rate energy terms" — pilot E-verified); Fourier branch: plain.

## 4. BCs/ICs
- Cavity wall Γc: σ·n = 0 (traction-free); θ = θ̂(ω) (wall-temperature pulse spectrum) — DECISION: temperature BC (well-posed for memory models; flux-BC would require extra evolution condition on q·n; prior cavity literature uses prescribed boundary temperature).
- Outer Γo (|x|=25a): u = 0, θ = 0. Causality: analysis window t ≤ t0+6tw < 2·24a/c_max ✓ (checked numerically in logs).
- IC: zero (linear).
  Well-posedness (summary; WELL_POSEDNESS.md): harmonic system (H1)-(H2) is elliptic-elliptic for ω≠0 with SPD data → unique solvable; ω=0 handled by steady check V6.

## 5. Nondimensionalization [D]
L0=a (equal-area cavity radius), t0=a²/κ̄, κ̄=√(det K_2D)/(ρ c_E), θ0=10K, σ0=|β|θ0, u0=σ0 a/C̄, C̄=C33.
Groups: ε=κ̄/(c_ref a) (inertia), Λ=τ κ̄/a² (memory), δ=T0|β|²/(ρ c_E C̄) (coupling), χ (aspect), φ (crystal angle). c_ref=√(C33/ρ).
Size sweep: a ∈ {5,10,20,50} nm ⇒ (ε,Λ) along Λ=(τ c_ref²/κ̄)ε²; τ sweep moves Λ independently.

## 6. Quantities of interest
Hoop stress on cavity wall: σ_θθ = n_i σ_ij n_j with n = outward normal of the ELLIPSE at wall (analytic from mapping). Modes: σ_θθ(ϑ,t) = Σ_m a_m(t) cos/sin mϑ (least squares on 72 wall points). Layer gradient G=−∂θ/∂n at wall peak-load time.

## 7. Limiting cases (pre-run)
(α=0 ⇒ u=σ=0 exactly) (τ→0 ⇒ Fourier) (ω→0 ⇒ steady log for circle/isotropic) (isotropic K,C,α ⇒ axisymmetric θ̂, σ̂ constant on circle wall — analytic expectation for wall hoop by symmetry) (φ-rotation identity) — all in VERIFICATION_PLAN V3–V7.

## 8. Thermodynamic admissibility (THERMODYNAMIC_ADMISSIBILITY.md details)
K SPD ✓ (eigs 11.36, 14.86 W/mK); C plane-strain block SPD ✓ (checked numerically, eigs>0); τ>0 ⇒ CV/MCV3 dissipative; free energy F=½C ε:ε−β:ε θ−ρcθ²/(2T0)·... standard Biot form; entropy production ≥0 for g(ω) with positive real dissipation (documented).
