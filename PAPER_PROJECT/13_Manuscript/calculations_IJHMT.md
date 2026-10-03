# Worked calculations for “Orientation-dependent wall stress around circular and elliptical cavities in monoclinic β-Ga₂O₃ under a transient thermal pulse”

*[AUTHOR INPUT REQUIRED: author names, affiliations, ORCID iDs and corresponding author]*

This document is the calculation companion to the manuscript of the same title. It contains no new physics, no new simulation and no new result: every number below is either recomputed here from the frozen source code (PAPER_PROJECT/06_Source_Code/src/, SHA-256 recorded in the code-freeze manifests) or read from the processed data package PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2.json, which is itself produced from the 300 runs stored in PAPER_PROJECT/09_Raw_Data/production/. Equation numbers in this companion are independent of those in the manuscript; where a step is quoted from the manuscript it is referenced as “Eq. (n) of the manuscript”. The purpose is that a reader can check every quantitative statement of the paper without re-running the code, and that a referee can see exactly which arithmetic stands behind each claim.

Two conventions are used throughout. First, all quantities are in SI units unless a unit is printed; stresses in tables are converted to MPa and thermal-stress moduli to MPa/K because those are the natural magnitudes. Second, numbers are printed as the code produces them and rounded only for display: a displayed value such as 1.3093 MPa/K is 1.30927… MPa/K in the arithmetic that follows.

## 1. Material data, frames and conventions

### 1.1 Frames, Voigt order and sign conventions

The crystallographic axes of monoclinic β-Ga₂O₃ are a, b, c with the twofold axis along b. The plane of the calculation is the a–c plane, i.e. the plane normal to the twofold axis, with laboratory coordinates x₁ = a and x₃ = c at zero rotation; x₂ = b is normal to the plane. Strains and stresses use the Voigt order (11, 33, 13) in the plane, with the engineering shear γ₁₃ = ε₁₃ + ε₃₁, so that the plane-strain stiffness block Q and the thermal-stress vector β are 3×3 and 3×1. The crystal frame and the laboratory frame coincide at rotation φ = 0; a rotation by φ about x₂ carries the crystal into the laboratory frame. Tension is positive and θ is the temperature rise above the reference temperature T₀ = 293 K.

### 1.2 The thirteen independent stiffness constants

Monoclinic symmetry (point group 2/m, unique axis b) leaves thirteen independent constants. The values used here are the literature values transcribed in PARAMETER_TABLE.md [15, 16] and are reproduced unchanged in Table C1; the two constants that do not enter the plane-strain block (C₄₄, C₄₆) are listed for completeness because they couple the out-of-plane shear components that the plane-strain ansatz excludes.

**Table C1.** Independent stiffness constants of monoclinic β-Ga₂O₃ (GPa), literature values [15]. C₁₅, C₂₅, C₃₅, C₄₆ are the monoclinic couplings that a higher-symmetry crystal would not have.

| C₁₁ | C₂₂ | C₃₃ | C₄₄ | C₅₅ | C₆₆ | C₁₂ | C₁₃ | C₂₃ | C₁₅ | C₂₅ | C₃₅ | C₄₆ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 242.800 | 343.800 | 347.400 | 47.800 | 88.600 | 104.000 | 128.000 | 160.000 | 70.900 | -1.620 | 0.360 | 0.970 | 5.590 |

The three in-plane monoclinic couplings are small but not negligible in the accounting that follows: C₁₅ = -1.62 GPa, C₂₅ = 0.36 GPa and C₃₅ = 0.97 GPa. They are the reason the plane-strain block Q is fully populated rather than block-diagonal, and they are the reason the thermal-stress vector acquires a shear component β₅ once the crystal is rotated (Section 3).

### 1.3 Thermal expansion, and what α₅ = 0 removes

The expansion tensor is diagonal in the crystal frame with components α_a = 1.54×10⁻⁶ K⁻¹, α_b = 3.37×10⁻⁶ K⁻¹ and α_c = 3.15×10⁻⁶ K⁻¹ [17]. The thermal shear α₅ = 2ε₁₃^{th} is **not** available in the source data and is set to zero. This is a limitation, not an approximation that has been verified: it removes the only mechanism that would generate an in-plane thermal shear at φ = 0, and it is carried through every number in this document. Its consequence is quantified in Section 10, where the alternative expansion set of [18] changes the absolute stress scale by a factor of about 16.

The a- and c-axis expansions differ by a factor 2.05, so the expansion tensor is not isotropic in the plane of the calculation; this is the seed of the orientation dependence that the manuscript measures.

### 1.4 Conductivity tensor: principal values and orientation

The in-plane conductivity block is

**Table C2.** In-plane conductivity block K (W m⁻¹ K⁻¹), axes ordered (a, c) [16]. The off-diagonal term is what makes the conduction tensor non-diagonal in the crystal frame.

| K_aa | K_ac | K_ca | K_cc |
|---|---|---|---|
| 12.130 | -0.992 | -0.992 | 14.090 |

Its eigenvalues and the orientation of its principal axes follow from the standard two-dimensional expressions.

$$ K_{1,2}=\frac{K_{11}+K_{33}}{2}\pm\sqrt{\left(\frac{K_{11}-K_{33}}{2}\right)^2+K_{13}^2},\qquad \tan 2\psi_K=\frac{2K_{13}}{K_{11}-K_{33}} \qquad (1) $$

Numerically:

- trace/2 = (12.130 + 14.090)/2 = 13.1100 W m⁻¹ K⁻¹;
- half-difference = (12.130 − 14.090)/2 = -0.9800, off-diagonal = -0.992;
- square-root term = √(-0.9800² + -0.992²) = 1.3944 W m⁻¹ K⁻¹;
- principal values K₁ = 11.716 and K₂ = 14.504 W m⁻¹ K⁻¹, ratio K₂/K₁ = 1.238;
- principal axes at ψ_K = -67.33° from the a axis, i.e. the conductivity tensor is *not* diagonal in the crystal frame;
- isotropic scale k̄ = √(det K) = √(12.130 × 14.090 − -0.992²) = 13.0356 W m⁻¹ K⁻¹.

The conductivity anisotropy is therefore a factor 1.24 in the plane — modest compared with the stiffness anisotropy — and the manuscript’s ablation E3 (isotropic conductivity, Section 10) shows that it is not what drives the orientation modulation.

### 1.5 Density, heat capacity and the derived scales

The mass density ρ = 5880 kg m⁻³ is a literature value; the specific heat capacity c_p = 560 J kg⁻¹ K⁻¹ is **estimated** (Debye-model value at Θ_D = 685 K, flagged ESTIMATED in PARAMETER_TABLE.md). Because c_p enters the diffusivity and the coupling number linearly, this estimate propagates directly into both. The derived scales are:

- diffusivity κ̄ = k̄/(ρc_p) = 13.0356/(5880 × 560) = 3.959e-06 m² s⁻¹;
- wave-speed scale c_ref = (C₃₃/ρ)^{1/2} = (347.4×10⁹/5880)^{1/2} = 7686.46 m s⁻¹;
- reference modulus C̄ = C₃₃ = 347.4 GPa;
- thermal-stress scale ‖β‖ = 2.0517 MPa K⁻¹ (Section 2);
- coupling number δ = T₀‖β‖²/(ρc_pC̄) = 1.078e-03 (Section 5).

## 2. Plane-strain reduction of the monoclinic law

### 2.1 Setting the b-direction strain to zero

The three-dimensional Voigt law of a monoclinic crystal, written in the axes (a, b, c) with Voigt order (11, 22, 33, 23, 13, 12), is σ = C ε − β θ. Plane strain in the a–c plane means ε₂₂ = 0, γ₂₃ = 0 and γ₁₂ = 0, so the strain vector reduces to ε = (ε₁₁, 0, ε₃₃, 0, γ₁₃, 0). Inserting this into the law and keeping the rows that carry in-plane stresses gives

$$ \boldsymbol{\sigma}=\mathbf{Q}\boldsymbol{\epsilon}-\boldsymbol{\beta}\theta,\qquad\boldsymbol{\epsilon}=(\epsilon_{11},\ \epsilon_{33},\ \gamma_{13}), \qquad (2) $$

where Q is the (11, 33, 13) **sub-block** of C and β is the corresponding sub-vector of the thermal-stress vector. Note what this is not: Q is not the condensed (Schur-complement) plane-strain stiffness of a material in which the out-of-plane stress is relaxed to zero. The out-of-plane normal stress is whatever the constraint ε₂₂ = 0 produces,

$$ \sigma_{22}=C_{12}\epsilon_{11}+C_{23}\epsilon_{33}+C_{25}\gamma_{13}-\beta_2\theta,\qquad \beta_2=C_{12}\alpha_a+C_{22}\alpha_b+C_{23}\alpha_c+C_{25}\alpha_5, \qquad (3) $$

and it does no work, because the strain it is conjugate to vanishes by construction. With the data of Section 1, β₂ = 1.5791 MPa K⁻¹. The two out-of-plane shear stresses σ₂₃ and σ₁₂ are non-zero only through the monoclinic couplings C₄₄, C₄₆ and the corresponding strains, which are zero; they are therefore identically zero in this reduction.

### 2.2 The reduced block Q

Reading the sub-block off Table C1 gives, in GPa,

**Table C3.** Plane-strain stiffness block Q (GPa) in the crystal frame. Q₁₅, Q₃₅ are the monoclinic couplings C₁₅, C₃₅.

| Q₁₁ | Q₁₃ | Q₁₅ | Q₃₃ | Q₃₅ | Q₅₅ |
|---|---|---|---|---|---|
| 242.8 | 160.0 | -1.62 | 347.4 | 0.97 | 88.6 |

The eigenvalues of Q are 88.51, 126.86 and 463.43 GPa — a factor 5.24 between the softest and the stiffest in-plane mode, which is the stiffness anisotropy that the orientation sweep probes. The block is symmetric positive definite, so the quasi-static elasticity problem is well posed.

### 2.3 The thermal-stress vector β, term by term

The thermal-stress vector is β = C α, restricted to the plane. Writing each component out with the numbers inserted (GPa × 10⁻⁶ K⁻¹ = MPa K⁻¹):

β₁ = C₁₁α_a + C₁₂α_b + C₁₃α_c + C₁₅α₅ = 0.00037 + 0.00043 + 0.00050 + 0 = 0.00131 MPa K⁻¹

β₃ = C₁₃α_a + C₂₃α_b + C₃₃α_c + C₃₅α₅ = 0.00025 + 0.00024 + 0.00109 + 0 = 0.00158 MPa K⁻¹

β₅ = C₁₅α_a + C₂₅α_b + C₃₅α_c + C₅₅α₅ = -0.00000 + 0.00000 + 0.00000 + 0 = 0.00000 MPa K⁻¹

so that β = (1.3093, 1.5796, 0.0018) MPa K⁻¹ and ‖β‖ = 2.0517 MPa K⁻¹. Two observations matter for what follows. First, β₁ ≠ β₃ (1.3093 against 1.5796 MPa K⁻¹): the two in-plane directions are not equivalent, and a cavity wall that runs along one direction is loaded differently from a wall that runs along the other. Second, β₅ = 0.0018 MPa K⁻¹ is zero to five decimal places, and it is zero *only* because α₅ was set to zero: the last column of the arithmetic above, C_i5 α₅, is identically zero while the first three columns are not. This is the limitation flagged in Section 1, and Section 3 shows that it does not survive a rotation of the crystal.

### 2.4 Scales derived from the reduced law

The plane-strain law supplies the two scales that non-dimensionalise the problem: the wave-speed scale c_ref and the stress scale per kelvin ‖β‖. Their ratio fixes the elastic number ε = κ̄/(c_ref a) of Section 5. Numerically c_ref = 7686.46 m s⁻¹ and ‖β‖ = 2.0517 MPa K⁻¹, so that a temperature rise of 1 K at a perfectly constrained wall would produce a stress of order 2 MPa — the magnitude against which the computed peaks of the manuscript (of order 1 MPa K⁻¹) should be read.

## 3. Rotation of the crystal

### 3.1 Rotation matrix and the fourth-order transformation

Let c_φ = cos φ and s_φ = sin φ. A rotation of the crystal by φ about the b axis (that is, a rotation of the material relative to the cavity) is represented in the (x₁, x₃) plane by

**Table C4.** Rotation matrix R(φ) in the (x₁, x₃) plane; below it is written c_φ = cos φ, s_φ = sin φ.

| R₁₁ | R₁₃ | R₃₁ | R₃₃ |
|---|---|---|---|
| cos φ | −sin φ | sin φ | cos φ |

$$ C^{\prime}_{abcd}=R_{ai}R_{bj}R_{ck}R_{dl}\,C_{ijkl}, \qquad (4) $$

and the rotated plane-strain block is read off from the rotated fourth-order tensor with the same Voigt convention as before. The in-plane expansion tensor transforms as a second-order tensor, α′ = R diag(α_a, α_c) Rᵀ, and the b-axis expansion enters separately, because a rotation about b leaves the b direction itself unchanged: the constants that carry α_b into the plane are C₁₂, C₂₃ and C₂₅, and they transform into

$$ C^{\prime}_{12}=c_\varphi^2 C_{12}+s_\varphi^2 C_{23}-2c_\varphi s_\varphi\,C_{25} \qquad (5) $$

$$ C^{\prime}_{23}=s_\varphi^2 C_{12}+c_\varphi^2 C_{23}+2s_\varphi c_\varphi\,C_{25} \qquad (6) $$

$$ C^{\prime}_{25}=c_\varphi s_\varphi\left(C_{12}-C_{23}\right)+\left(c_\varphi^2-s_\varphi^2\right)C_{25} \qquad (7) $$

The signs of the cross terms are the part that is easy to get wrong, and the code carries a regression test for exactly this (test U1, manuscript Section 5): the term is invisible at φ = 0 and φ = 90°, where c_φ s_φ = 0, and it is maximal at φ = 45°.

### 3.2 The b-axis coupling worked at φ = 30°

With c_φ = 0.866025 and s_φ = 0.5:

- C′₁₂ = 0.7500×128.0 + 0.2500×70.9 − 2×0.8660×0.5×0.36 = 96.0000 + 17.7250 − 0.3118 = 113.4132 GPa;
- C′₂₃ = 0.2500×128.0 + 0.7500×70.9 + 2×0.5×0.8660×0.36 = 32.0000 + 53.1750 + 0.3118 = 85.4868 GPa;
- C′₂₅ = 0.4330×(128.0 − 70.9) + 0.5000×0.36 = 24.7250 + 0.1800 = 24.9050 GPa.

The cross term −2c_φ s_φ C₂₅ = -0.312 GPa is small compared with C₁₂ and C₂₃, but it is the term whose sign was wrong in the analysis as first written, and the manuscript records the correction.

### 3.3 The rotated expansion tensor and the induced thermal shear

The in-plane expansion tensor is diagonal in the crystal frame, so after rotation

$$ \alpha^{\prime}_{11}=c_\varphi^2\alpha_a+s_\varphi^2\alpha_c,\qquad\alpha^{\prime}_{33}=s_\varphi^2\alpha_a+c_\varphi^2\alpha_c,\qquad\alpha^{\prime}_{13}=c_\varphi s_\varphi\left(\alpha_c-\alpha_a\right). \qquad (8) $$

The third of these is the important one: at any angle that is not a multiple of 90°, the rotated expansion tensor has a non-zero in-plane shear component even though the crystal-frame thermal shear α₅ was set to zero. At φ = 30°, α′₁₃ = 0.4330 × (3.15 − 1.54)×10⁻⁶ = 0.6972×10⁻⁶ K⁻¹, which is 25.9% of the mean in-plane expansion. The thermal-stress vector inherits a shear component from it.

### 3.4 β′ at four angles

**Table C5.** Thermal-stress vector in the laboratory frame at four crystal rotations, computed with the transformation of Section 3.1 (test U1 of the manuscript).

| φ (deg) | β′₁ (MPa/K) | β′₃ (MPa/K) | β′₅ (MPa/K) | ‖β′‖ (MPa/K) |
|---|---|---|---|---|
| 0 | 1.3093 | 1.5796 | 0.0018 | 2.0517 |
| 30 | 1.3753 | 1.5136 | -0.1162 | 2.0484 |
| 45 | 1.4427 | 1.4462 | -0.1352 | 2.0472 |
| 90 | 1.5796 | 1.3093 | -0.0018 | 2.0517 |

Two features are quantitative, not qualitative. First, β′₅ grows from 0.0018 MPa K⁻¹ at φ = 0 to -0.1352 MPa K⁻¹ at φ = 45° and then falls back: the induced shear is an odd function of sin 2φ, so it vanishes at 0° and 90° and is extremal near 45°. Second, ‖β′‖ is not exactly rotation invariant — it varies by 0.22% over the quadrant — because the b-axis contribution (C′₁₂, C′₂₃, C′₂₅)α_b is not an isotropic tensor. The variation is small, so the *magnitude* of the thermal load is nearly orientation independent while its *distribution among components* is not: that is the mechanism the manuscript measures.

## 4. Isotropic control and the closed-form circular cavity

### 4.1 Construction of the control

The manuscript uses an isotropic control — an ablation, not a material claim — to test the numerical solution against a closed form. It is built to have the same bulk order as the crystal: the shear modulus is taken as μ = C₆₆, the Lamé constant as λ = C₁₂, and the expansion as the mean of the three crystal values. Then

- μ = 104.0 GPa, λ = 128.0 GPa, m = λ + 2μ = 336.0 GPa;
- α_iso = (1.54 + 3.37 + 3.15)/3 ×10⁻⁶ = 2.6867×10⁻⁶ K⁻¹;
- γ_T = (3λ + 2μ)α_iso = (3×128.0 + 2×104.0)×10⁹ × 2.6867×10⁻⁶ = 1.5905 MPa K⁻¹;
- g_T = γ_T/m = 1.5905/336.0 = 4.7337×10⁻⁶ K⁻¹.

The isotropic conductivity is the mean of the two principal values of K, k_iso = (K₁ + K₂)/2 = 13.1100 W m⁻¹ K⁻¹, i.e. an isotropic tensor with the same trace as the crystal block.

### 4.2 Closed form for the circular cavity

For a circular cavity of radius a in an isotropic solid in quasi-static plane strain, with a radially symmetric temperature field θ(r, t), the radial displacement u(r, t) satisfies

$$ \frac{\mathrm{d}}{\mathrm{d}r}\left[\frac{1}{r}\frac{\mathrm{d}(ru)}{\mathrm{d}r}\right]=g_T\,\frac{\mathrm{d}\theta}{\mathrm{d}r},\qquad g_T=\frac{\gamma_T}{m}=\frac{(3\lambda+2\mu)\alpha}{m}. \qquad (9) $$

Integrating twice between a and r, with G(r) = ∫_a^r r′θ(r′, t) dr′ and integration constants C₁ and C₂,

$$ u(r,t)=g_T\,\frac{G(r)}{r}+C_1 r+\frac{C_2}{r}. \qquad (10) $$

The hoop stress follows from the constitutive law, σ_θθ = λ u′ + m u/r − γ_T θ with u′ = ∂u/∂r. Substituting the expression above and using G(a) = 0 and G′(r) = r θ(r), the wall value at r = a is

$$ \sigma_{\theta\theta}(a,t)=\left(\lambda g_T-\gamma_T\right)\theta(a,t)+(\lambda+m)C_1+(m-\lambda)\frac{C_2}{a^2}, \qquad (11) $$

$$ \sigma_{\theta\theta}(a,t)=\sigma_{\theta\theta}^{\mathrm{local}}(a,t)+\sigma_{\theta\theta}^{\mathrm{far}}(a,t),\qquad\sigma_{\theta\theta}^{\mathrm{local}}(a,t)=-2\mu g_T\,\theta(a,t),\qquad\sigma_{\theta\theta}^{\mathrm{far}}(a,t)=(\lambda+m)C_1+2\mu\frac{C_2}{a^2}. \qquad (12) $$

because γ_T = m g_T and m − λ = 2μ. The first term is *local*: it involves the wall temperature only, not the temperature profile, and not the outer radius. The second term is everything else; with a traction-free or a fixed outer boundary at R = 80a it scales as (a/R)².

Numerically the local term is −2μ g_T = −2 × 104.0×10⁹ × 4.7337×10⁻⁶ = 0.9846 MPa K⁻¹. The processed data package reports the closed-form wall stress as 984599.37 Pa K⁻¹ from the local term alone and 985689.45 Pa K⁻¹ with the far-field term included, a difference of 1090.08 Pa K⁻¹ (0.111%). The numerical solution on grid T48 gives 980589.87 Pa K⁻¹, i.e. 0.52% from the closed form with the far field — the agreement quoted as verification test V3 in the manuscript.

### 4.3 Why the wall stress is a local response

The far-field term is proportional to (a/R)². With R = 80a, (a/R)² = 1.5625e-04. The manuscript reports the same conclusion from the numerical side: the local (first) term accounts for all but about 0.1% of the closed-form wall stress, which is why the orientation dependence of the anisotropic results can be interpreted as a local property of the material at the wall rather than as a consequence of the temperature profile in the bulk.

## 5. Non-dimensionalisation and the dimensionless groups

### 5.1 Scales

Lengths are scaled by the cavity radius a, times by the thermal time t_th = a²/κ̄, stresses by ‖β‖Θ with Θ the wall-temperature amplitude, and temperature by Θ. With a = 10 nm:

- t_th = a²/κ̄ = (10⁻⁸)²/3.959e-06 = 2.526e-11 s = 25.26 ps;
- the elastic number ε = κ̄/(c_ref a) = 3.959e-06/(7686.46 × 10⁻⁸) = 0.0515;
- the memory number Λ = τ/t_th: Λ = 0.0396 at τ = 1 ps, 0.1979 at τ = 5 ps and 0.7918 at τ = 20 ps;
- the coupling number δ = T₀‖β‖²/(ρc_pC̄) = 293×(2.0517×10⁶)²/(5880 × 560 × 347.4×10⁹) = 1.078e-03;

δ is the fraction of the thermal energy that is converted into mechanical work per unit temperature rise; it is small (1.078e-03), and the manuscript uses that smallness twice: to argue that the thermoelastic feedback is negligible, and to bound it.

### 5.2 Second-sound speed and the thermal wave

The Cattaneo–Vernotte law turns the heat equation into a hyperbolic equation whose characteristic speed is v_T = (κ̄/τ)^{1/2}. In the dimensionless groups this is v_T/c_ref = ε/√Λ, so that at fixed ε the wave slows as Λ^{−1/2} when the relaxation time is increased. Numerically:

**Table C6.** Second-sound speed implied by the Cattaneo–Vernotte law at a = 10 nm. The relaxation time is hypothetical: these are sensitivities, not measurements.

| τ (ps) | Λ | v_T (m/s) | v_T/c_ref | a/v_T (ps) |
|---|---|---|---|---|
| 1 | 0.0396 | 1989.7 | 0.25886 | 5.026 |
| 5 | 0.1979 | 889.8 | 0.11576 | 11.238 |
| 20 | 0.7918 | 444.9 | 0.05788 | 22.477 |

The transit time a/v_T is the time a thermal wave needs to cross the cavity radius; comparing it with t_th shows how far the model is from the diffusive limit for each τ.

### 5.3 The feedback bound

The manuscript bounds the thermoelastic feedback — the effect of the deformation on the temperature field through the T₀β:ε̇ coupling — by comparing the temperature change it can produce with the applied temperature change. The criterion, fixed before the runs were made, is |Δθ|/|θ| ≤ 5δ, with the factor five a margin chosen before the runs rather than fitted to them. With δ = 1.078e-03, 5δ = 5.391e-03, i.e. a feedback of at most about half a per cent. The criterion is then checked numerically by switching the coupling off (manuscript Section 6.4), which is the ablation that turns a bound into a measured effect.

## 6. Spatial discretisation

### 6.1 The map and its metrics

The annular region between the cavity boundary and a circle of radius R = 80a is mapped from a rectangle (ξ, η) ∈ [0, 1] × [0, 2π) by

$$ x=A(\rho)\cos\eta,\qquad y=B(\rho)\sin\eta,\qquad\rho(\xi)=\frac{\exp(\gamma\xi)-1}{\exp(\gamma)-1}, \qquad (13) $$

with A(ρ) = a_e + (R − a_e)ρ, B(ρ) = b_e + (R − b_e)ρ and a_e = a√χ, b_e = a/√χ for an ellipse of aspect ratio χ. The radial clustering parameter γ = 3.5 places the first radial interval at Δρ = 1.169e-03 of the total, i.e. the near-wall cell is 9.01 times thinner than it would be on a uniform grid — the resolution is needed because both the thermal boundary layer and the stress concentration live at the wall.

The Jacobian of the map is J = x_ξ y_η − x_η y_ξ. On the production grid (N_r × N_θ = 96 × 48, γ = 3.5) the Jacobian is positive everywhere: J ranges from 8.6096 to 22808.77 in units of a², a ratio of 2649.2. The metrics are differentiated analytically, not by finite differences, so the discrete operators are exact for the map quantities.

### 6.2 Contravariant coefficients of the two operators

Written on the mapped rectangle, both operators take the contravariant form

$$ \nabla\cdot(\mathbf{K}\nabla\theta)=\frac{1}{J}\left[\partial_\xi\left(A\,\partial_\xi\theta+B\,\partial_\eta\theta\right)+\partial_\eta\left(B\,\partial_\xi\theta+D\,\partial_\eta\theta\right)\right], \qquad (14) $$

with the coefficients (the notation follows cg_ops.thermal)

$$ A=\frac{K_{11}y_\eta^2-2K_{13}x_\eta y_\eta+K_{33}x_\eta^2}{J} \qquad (15) $$

$$ D=\frac{K_{11}y_\xi^2-2K_{13}x_\xi y_\xi+K_{33}x_\xi^2}{J} \qquad (16) $$

$$ B=\frac{K_{13}\left(x_\xi y_\eta+x_\eta y_\xi\right)-K_{11}y_\xi y_\eta-K_{33}x_\xi x_\eta}{J} \qquad (17) $$

and the momentum operator is built in exactly the same way from the plane-strain block Q (cg_ops.momentum). At the wall (ξ = 0) of the circular production grid the three coefficients evaluate to A = 1.4089, B = -0.9920 and D = 121.3087 W m⁻¹ K⁻¹; the mixed coefficient B is zero there by symmetry and non-zero for the ellipse, which is what makes the ellipse a genuinely two-dimensional test.

### 6.3 Discrete operators and boundary treatment

Both operators are discretised in the conservative form above, so that the discrete flux divergence of a constant field is identically zero (the V7 patch test of the manuscript). In the radial direction the second derivative is replaced by a second-order one-sided three-point formula in the first and last interior ring, where the centred stencil would reach outside the domain; in the circumferential direction the stencil is the centred second-order formula with periodic wrap-around, discretely exact for the trigonometric modes that the grid supports. Derivatives of the map (x_ξ, x_η, y_ξ, y_η, J) are evaluated analytically from the closed-form map.

### 6.4 Grid sizes, unknowns and cost

The unknown vector is U = (θ, u₁, u₃) at every node, i.e. 3N_rN_θ = 3 × 96 × 48 = 13824 complex unknowns per frequency. The production grid is N_r × N_θ = 96 × 48 with γ = 3.5; the convergence families use (48, 96, 192) × 48 and 96 × (48, 144) together with clustering parameters γ ∈ {2.5, 3.5, 4.5}. One frequency-domain solve per Bromwich node is required, so the cost of a run is the number of solves times one sparse factorisation; the counts are given in Section 8.

## 7. Frequency-domain system

### 7.1 Assembly

With the harmonic convention fields ∝ exp(+iωt), the semi-discrete equations are the single complex linear system

$$ \mathbf{A}(\omega)\,\mathbf{U}=\mathbf{f},\qquad\mathbf{A}(\omega)=\mathbf{A}_{\mathrm{base}}+\omega^2\mathbf{A}_{\mathrm{in}}+i\omega\,\mathbf{A}_{\mathrm{d}}+g(\omega)\,\mathbf{A}_{\mathrm{lap}}, \qquad (18) $$

where A_base holds the elastic stiffness and the steady conduction operator, A_in the mass matrix, A_d the (viscous-free) inertial coupling rows and A_lap the Laplacian of the heat equation, multiplied by the conduction kernel g(ω) of the chosen law. The four matrices are assembled once per grid and reused for every frequency, so a run costs one assembly and n_solves factorisations.

### 7.2 Conduction kernels

The three laws differ only in the scalar factor g(ω):

$$ g_{\mathrm{F}}(\omega)=1, \qquad (19) $$

$$ g_{\mathrm{CV}}(\omega)=\frac{1}{1+i\omega\tau}, \qquad (20) $$

$$ g_{\mathrm{MCV3}}(\omega)=\frac{1}{2}\frac{1}{1+i\omega\tau/2}+\frac{1}{2}\frac{1}{1+2i\omega\tau}, \qquad (21) $$

**Table C7.** Conduction kernels in the frequency domain. All three reduce to g = 1 as ωτ → 0, so the Fourier case is the limit of the other two.

| Law | kernel | status in this study |
|---|---|---|
| Fourier | g = 1 for every ω | baseline of every comparison |
| Cattaneo–Vernotte (one relaxation time) | g = 1/(1 + iωτ) | primary non-Fourier model (Lord–Shulman form) |
| Two relaxation times (MCV3) | average of two CV kernels with τ/2 and 2τ | exploratory sensitivity variant only |

The three kernels differ only in that scalar factor, which is why the whole model family is implemented as one assembly with g(ω) as a parameter.

Both non-Fourier kernels are positive-real (passive) for real ω, which is the property that keeps the response physically admissible (the same restriction is stated for a memory kernel in the general theory of heat conduction with finite wave speeds, manuscript reference [15]); the companion does not claim that either is the correct description of β-Ga₂O₃, and the relaxation time is treated as a hypothetical parameter throughout.

### 7.3 Boundary rows, scaling and the solve

The cavity wall carries the Dirichlet condition θ = 1 (per unit amplitude) and zero traction; the outer boundary carries θ = 0 and u = 0. Both are imposed by row replacement. Before factorisation every row is multiplied by the local Jacobian and then scaled so that its largest entry has unit modulus (row equilibration); without it the spread of magnitudes between the temperature rows and the displacement rows costs several digits of accuracy. The system is factorised with a sparse LU (SuperLU, splu) and improved by two steps of iterative refinement. The measured effect, over 175 production runs, is a backward error of at most 7.226e-17 and, after refinement, a forward-error floor of order 10⁻¹⁴ relative — the refinement is what makes the small differences of Section 9 (deviations of a few tenths of a per cent) resolvable at all.

## 8. Single-pulse response by Bromwich inversion

### 8.1 The contour and the inversion formula

The frequency-domain solver returns the response to a steady harmonic wall temperature. The response to a *single* pulse in a medium at rest is obtained by Laplace inversion on a vertical contour Re(s) = γ_B > 0,

$$ y(t)=\frac{\exp(\gamma_B t)}{T}\left[Y(\gamma_B)+2\,\mathrm{Re}\sum_{k=1}^{K}Y\!\left(\gamma_B+i\omega_k\right)\exp\left(i\omega_k t\right)\right],\qquad\omega_k=\frac{2\pi k}{T}, \qquad (22) $$

with Y(s) = H(s)P(s), where H is the transfer function evaluated at the complex frequency ω = −i s/t_th (the solver’s exp(+iωt) convention makes iω = s) and P is the two-sided Laplace transform of the Gaussian wall pulse p(t) = exp(−((t − t₀)/t_w)²),

$$ P(s)=\sqrt{\pi}\,t_w\,\exp\!\left[\left(\frac{s\,t_w}{2}\right)^2-s\,t_0\right]. \qquad (23) $$

This replaces the periodic-DFT synthesis of the handoff code, which returns the steady state of a pulse *train* rather than the response to one pulse: the distinction is quantitative, not cosmetic, because a pulse train accumulates heat in the medium between pulses.

### 8.2 Choice of the parameters

The defaults are T = 20.0 t_th, γ_B = 0.9/t_th, t₀ = 2.5 t_th, t_w = 1.2 t_th and ε_tr = 1e-10. They are fixed by three competing errors:

- alias error: periodising the inverse adds images at t ± nT; the n ≥ 1 images are suppressed by exp(−γ_B T) = exp(−18.0) = 1.523e-08, and the n ≤ −1 images by the Gaussian pre-history, which is negligible for t < t₀ − 5t_w = -3.5 t_th;
- truncation: K is chosen so that |P(s_K)|/|P(s_0)| < ε_tr. Because |P| grows like exp((ω t_w/2)²), the condition is ω_max = √(γ_B² + 4 ln(1/ε_tr)/t_w²) = √(0.81 + 4×23.026/1.44) = 8.0480, hence K, the smallest integer not below ω_max T/2π, is 26 and n_solves = K + 1 = 27;
- round-off: the factor exp(γ_B t) amplifies the truncation error, growing to exp(0.9 × 6) = 221.4 at t = 6 t_th and exp(0.9 × 12) = 49020.8 at t = 12 t_th.

The three balance to the validity window printed by the plan, 0 ≤ t ≤ 14.5 t_th (T − 5.5), comfortably beyond the quantity-of-interest window 0 ≤ t ≤ 6 t_th. The reconstruction is checked directly: the wall temperature recovered from H is compared with the prescribed Gaussian in every run, and the largest discrepancy over the QoI window is 1.005e-10 relative across 175 runs.

## 9. Quantities of interest: worked arithmetic

### 9.1 Peak wall stress and the trigonometric interpolant

The primary observable is the maximum over the wall and over the window of the modulus of the hoop stress,

$$ \hat\sigma=\max_{\eta}\ \max_{0\leq t\leq 6t_{th}}\left|\sigma_{\theta\theta}(\eta,t)\right|,\qquad \sigma_{\theta\theta}=t_x^2\sigma_{11}+2t_x t_y\,\sigma_{13}+t_y^2\sigma_{33}, \qquad (24) $$

with (t_x, t_y) the unit tangent of the wall. Taking the maximum over grid nodes quantises it and biases it low by an amount of order (Δη)², which is not negligible on the coarse grids; the manuscript therefore also evaluates the maximum of the trigonometric interpolant

$$ \sigma_{\theta\theta}(\eta,t)=\sum_k c_k(t)\,\exp(ik\eta),\qquad c_k=\frac{1}{N_\theta}\sum_j\sigma_{\theta\theta}(\eta_j,t)\,\exp(-ik\eta_j), \qquad (25) $$

and reports both. On the finest radial grid of the circle study the two differ by 0.024% (853664.7 against 853867.3 Pa K⁻¹), and refining the angular direction from 48 to 192 intervals changes the interpolated peak by 0.109% — the node-based and interpolant-based peaks are the same number to within the grid uncertainty, and the interpolant is used wherever a difference of a few tenths of a per cent matters.

### 9.2 Orientation modulation

The orientation modulation is the peak-to-peak spread of the wall stress over crystal rotations, normalised by its mean,

$$ A_\varphi=\frac{\max_\varphi\hat\sigma-\min_\varphi\hat\sigma}{\mathrm{mean}_\varphi\,\hat\sigma}. \qquad (26) $$

For the twelve-angle sweep on the production grid the values are min = 1.1255, max = 1.6685 and mean = 1.4854 MPa K⁻¹, so A_φ = (1.6685 − 1.1255)/1.4854 = 0.3656. The same quantity computed on the radial-extrapolated six-angle sweep is 0.2875, i.e. the modulation is resolved well beyond the numerical uncertainty of 0.0131.

### 9.3 Thermal-memory deviation

The thermal-memory deviation compares a non-Fourier run with the Fourier run at the same parameters,

$$ D=\frac{\max_{\eta,t}\left|\sigma_{\theta\theta}^{\mathrm{CV}}-\sigma_{\theta\theta}^{\mathrm{F}}\right|}{\max_{\eta,t}\left|\sigma_{\theta\theta}^{\mathrm{F}}\right|},\qquad0\leq t\leq 6t_{th}. \qquad (27) $$

**Table C8.** Thermal-memory deviation D of the circular cavity at a = 10 nm, dynamic and quasi-static, from the processed data package. Both are well below the numerical uncertainty of the grid.

| τ (ps) | Λ | D (dynamic) | D (quasi-static) | difference |
|---|---|---|---|---|
| 1 | 0.0396 | 0.00109 | 0.00040 | 0.00069 |
| 5 | 0.1979 | 0.00529 | 0.00202 | 0.00327 |
| 20 | 0.7918 | 0.01569 | 0.00707 | 0.00862 |

Two features of these numbers are worth stating explicitly. First, D is small in absolute terms — of the order of tenths of a per cent to a few per cent — so the thermal-memory effect is a correction, not a change of regime. Second, the dynamic D exceeds the quasi-static D by a systematic margin, which is the inertial contribution rather than the conductive one; the manuscript separates the two by comparing against the quasi-static family.

### 9.4 Richardson extrapolation, step by step

The radial convergence study for the ellipse (isotropic control) gives peak values f₄₈ = 1509477.6, f₉₆ = 1500999.7 and f₁₉₂ = 1497301.6 Pa K⁻¹ at N_r = 48, 96, 192. Assuming a clean power law f_n = f_∞ + C n^{−p}, three grids determine p:

$$ p=\frac{\ln\left[(f_{48}-f_{96})/(f_{96}-f_{192})\right]}{\ln 2}=\frac{\ln\left[8477.9/3698.2\right]}{\ln 2}=1.1969, \qquad (28) $$

and then the extrapolated value is

$$ f_\infty=f_{192}+\frac{f_{192}-f_{96}}{2^{p}-1}=1497301.6+\frac{-3698.2}{1.2925}=1494440.2\ \mathrm{Pa\,K^{-1}}, \qquad (29) $$

so the correction applied to the finest grid is -2861.3 Pa K⁻¹ (-0.191% relative) and the extrapolated value differs from the production grid by 0.44%. The observed order p = 1.197 is below the formal second order of the stencils, which is expected: the wall stress is extracted at a boundary where one-sided formulas and a curved boundary both reduce the effective order, and the clustering parameter interacts with it. The manuscript quotes the extrapolated value with the observed order and reports the numerical uncertainty u_num = 0.0131 from the same budget.

### 9.5 Uncertainty budget

Two uncertainties are tracked and never added in quadrature, because they are of different kinds. The numerical uncertainty u_num = 0.0131 (relative) comes from the grid: it is the largest residual spread of the convergence families after extrapolation, and the resolvability threshold fixed before the runs was 0.0656. The parameter uncertainty is separate and larger: it comes from the spread of the published thermal-expansion data and is quantified in Section 10. The manuscript keeps them apart throughout, because the first is a property of the discretisation and can be reduced by computing, while the second is a property of the material data and cannot.

## 10. Ablations: what each ingredient contributes

### 10.1 Mechanism ablations

**Table C9.** Mechanism ablations on the six-angle ellipse sweep. A_φ is the orientation modulation; the last column is the change of the absolute stress scale.

| Variant | A_φ | mean peak (MPa/K) | mean / baseline |
|---|---|---|---|
| baseline (all anisotropy) | 0.2901 | 1.1707 | 1.0000 |
| isotropic conductivity (K → k_iso I) | 0.2722 | 1.1613 | 0.9920 |
| isotropic stiffness (Q → Q_iso) | 0.4559 | 1.4869 | 1.2702 |
| isotropic expansion (α → mean) | 0.2078 | 1.1973 | 1.0228 |
| alternative expansion set [18] | 0.2991 | 0.0737 | 0.0630 |

Read the table in two columns at a time. The modulation A_φ collapses to 0.2078 when the expansion is made isotropic and to 0.4559 when the stiffness is made isotropic, while it barely moves when the conductivity is made isotropic (0.2722 against a baseline of 0.2901). The conclusion is that the orientation dependence is driven by the elastic and expansion anisotropy, not by the conduction anisotropy.

### 10.2 The expansion data: the dominant uncertainty

The last row is the one that matters for the absolute magnitude of every stress quoted in the manuscript. Replacing the reference expansion set with the alternative set of [18] divides the mean peak wall stress by 15.88 — a factor of about 15.9 — while changing the modulation only from 0.2901 to 0.2991. The two effects are therefore separable: the *shape* of the orientation dependence is robust to which expansion set is used, while the *scale* is not. This is why the manuscript reports the modulation dimensionlessly and the stress per kelvin, and why it states the >10× uncertainty in the absolute stress scale prominently rather than in a footnote.

## 11. Reproduction

### 11.1 What to run, and what it must reproduce

The companion inherits the provenance of the manuscript. The source code is frozen under PAPER_PROJECT/06_Source_Code/CODE_FREEZE_v2_gate.json (gate freeze, 15 files) and CODE_FREEZE_v2_final.json (24 files), each entry carrying a SHA-256 of the file; the raw output of the 175 production runs and the convergence families is in PAPER_PROJECT/09_Raw_Data/production/; the processed numbers quoted here are in PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2.json. Regenerating this document is a single command:

Both archived manifests were taken on 2026-10-01. 8 of the 15 entries of the gate freeze are byte-identical in the code as submitted; 7 entries (cg_bromwich.py, cg_pipeline.py, run_tests.py, analyze_v2.py, make_figures.py, production_matrix.py and run_production_v2.py) have been edited since, so the digests recorded for them no longer describe it. The pipeline was therefore re-run end to end with the code as submitted, and it reproduces the archived results exactly: the production runs agree with the archived quantities of interest to zero relative difference, every leaf of ANALYSIS_V2.json agrees within 10⁻⁹, the eight figures and the five archived CSV tables are byte-identical, and only wall-clock timings differ (PAPER_PROJECT/15_Audits/RERUN_COMPARISON.md). The verification pass of 2026-10-03 added an ablation set at the production grid (24 runs), re-ran the analysis layer over all 175 stored runs with no pre-existing quantity changed, and re-solved one production job in a different Python/NumPy build, where it reproduced its stored peak wall stress to 2.7×10⁻¹⁶ relative. The mathematical audit that followed re-derived the constitutive algebra and every printed analytical identity symbolically and re-checked the discretisation, kernel and inversion conventions against the shipped code; it corrected two typographical statements in the model description, made the plane-strain class and the norm convention of δ explicit, and replaced the hard-coded validity window of the inversion by the bound it was an instance of (t ≤ T − (t_{0} + 2.5t_{w}): 14.5 t_{th} for the baseline t_{w} = 1.2 t_{th}, 11.5 t_{th} for t_{w} = 2.4 t_{th}). No stored run and no reported value changed. CODE_FREEZE_submission_2026_10_03e.json (27 files, all 27 byte-identical to the code as submitted) is the refreshed manifest, the one to deposit with the data package; it supersedes CODE_FREEZE_submission_2026_10_03d.json (taken the same day, before this change, 25 of whose 27 entries still match), CODE_FREEZE_submission_2026_10_03c.json, CODE_FREEZE_submission_2026_10_03b.json, CODE_FREEZE_submission_2026_10_03.json and CODE_FREEZE_submission_2026_10_02.json, all kept unchanged as history.

- python3 PAPER_PROJECT/13_Manuscript/build_calculations.py — rebuilds this document from the frozen source and the processed data;
- python3 tools/md_to_tex.py -i PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md -o PAPER_PROJECT/13_Manuscript/FINAL_REVISED_CALCULATIONS.tex --companion — the LaTeX source;
- python3 tools/md_to_pdf.py -i … -o … — the preprint PDF.

### 11.2 Status of the calculations and of the model

This companion treats Fourier and Lord--Shulman conduction as the primary conduction laws: every number that carries a physical interpretation is computed with one of them. The two-relaxation-time kernel is carried as an exploratory sensitivity kernel only, and no statement in this document depends on it. Nothing here is a validation: every comparison is against an exact solution of the same mathematical model or against an independent implementation of it, and no experimental validation exists for the configuration studied. The continuum validity of the model at the 5–50 nm scale of the study is not established, and the relaxation times used are hypothetical parameters rather than measured ones. The thermal-expansion data that set the absolute stress scale differ between sources by more than an order of magnitude, which is why the orientation modulation is reported dimensionlessly and the stress is reported per kelvin; the modulation survives the change of expansion set, the scale does not.

Code and data will be deposited on acceptance; the persistent identifier is [PUBLIC REPOSITORY/DOI TO BE INSERTED].

## Declarations

**CRediT authorship contribution statement:** [AUTHOR INPUT REQUIRED].

**Declaration of competing interest:** [AUTHOR INPUT REQUIRED].

**Funding:** [AUTHOR INPUT REQUIRED: name the grant, or state that no funding was received].

**Data availability:** the Python source code, the verification suite, the per-run raw outputs and the processed analysis package from which every number in this companion is recomputed are provided in the project data package (SHA-256 code freeze CODE_FREEZE_v2_gate.json), to be deposited at [PUBLIC REPOSITORY/DOI TO BE INSERTED].

**Declaration of Generative AI and AI-assisted technologies in the writing process.** [TEMPLATE — to be reviewed, edited and confirmed by the authors; Elsevier requires this statement above the references.] During the preparation of this work the author(s) used a generative-AI assistant (Arena.ai Agent Mode; the underlying models are provided by the service) for the writing process: drafting and revising the text and the figure captions, and checking the internal consistency of the manuscript, the calculation companion and the tables. After using this tool the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the publication. The same class of tool was also used in the research process — reviewing and extending the numerical code and the verification suite, and running the simulations — which the journal policy places in the methods rather than in this declaration; the numerical-methods section of the manuscript records that use. No AI tool generated a physical result, no AI tool was used to produce or select any number reported here, and no AI tool is an author or is cited as a source.

