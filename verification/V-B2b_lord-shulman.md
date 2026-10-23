# V-B2b — Lord–Shulman (single relaxation time)

**Access date 2026-10-22.** No subscription full text; every equation derived here.

## Task

As V-B2a, for Lord–Shulman (LS) theory.

## Method

1. **Provenance.** Lord, H.W. & Shulman, Y. (1967) "A generalized dynamical theory of thermoelasticity", *J. Mech. Phys. Solids* **15**(5):299–309, DOI 10.1016/0022-5096(67)90024-5. Crossref 4068, OpenAlex 4521. Read level: **record only — full text NOT opened.**
2. Derived the heat law from Cattaneo–Maxwell (τ_q q̇ + q = −k_th∇θ) plus the energy balance, then the coupled 1-D system and its dispersion relation.
3. Checks in `V-B2_wave_speeds.py`: (i) τ₀→0 must return the Biot determinant exactly — **PASS**; (ii) rigid-limit thermal speed must equal √(κ/τ₀) — confirmed numerically for three τ₀; (iii) the Fourier→LS transition frequency 1/τ₀ is visible in the numeric branches.

## Result

### R1. Heat law

Cattaneo–Maxwell (a single relaxation time τ₀ for the heat flux):

    τ₀ q̇ + q = −k_th ∇θ

Eliminating q with ρc θ̇ + βT₀ ε̇ = −∇·q gives the **hyperbolic** heat equation

    (1 + τ₀ ∂/∂t)(ρc θ̇ + βT₀ ε̇) = k_th ∇²θ

Written out: τ₀ρc θ̈ + ρc θ̇ + τ₀βT₀ ε̈ + βT₀ ε̇ = k_th∇²θ.

So τ₀ multiplies **both** the thermal-inertia term and the coupling term. (Many papers move τ₀ onto only one of them; see open issue 2.)

### R2. Coupled equations, 1-D

    ρ ü = M u_xx − β θ_x
    ρc(θ̇ + τ₀θ̈) + βT₀(u̇_x + τ₀ü_x) = k_th θ_xx

### R3. Parameters

λ, μ, M, β, ρ, c, k_th, κ, T₀, δ as in V-B2a, **plus**

| Symbol | Meaning | Units | Notes |
|---|---|---|---|
| τ₀ | heat-flux relaxation time | s | the single new parameter |
| c_h = √(κ/τ₀) | thermal wave speed (rigid limit) | m/s | follows from R1 |

### R4. Admissibility

- **τ₀ ≥ 0** and **k_th > 0**: with τ₀ < 0 the heat equation is backward-hyperbolic — one branch grows in time for every wavenumber (anti-damping). τ₀ = 0 returns Biot (PASS in checks).
- **c > 0, M > 0, ρ > 0**; k_th → 0 with τ₀ > 0 leaves an undamped wave equation (no dissipation at all).
- **Finite thermal speed** c_h = √(κ/τ₀) exists for every τ₀ > 0. This is LS's defining success.
- **Physical admissibility is not implied by τ₀ > 0.** Thermodynamic derivations that *derive* Cattaneo's law require an enlarged state (heat-flux inertia in the free energy); a purely phenomenological τ₀ > 0 can be mathematically well posed while having no admissible free energy. Flagged for the review: "well posed" ≠ "thermodynamically admissible".

### R5. Characteristic equation and speeds

    [M k² − ρω²,  −iβk;   (1−iωτ₀)βT₀ωk,   k_th k² − iωρc(1−iωτ₀)] (U,Θ)ᵀ = 0

    det = 0  ⇒  (M k² − ρω²)[k_th k² − iωρc(1−iωτ₀)] + iβ²T₀ωk²(1−iωτ₀) = 0

Rigid limit (β→0): τ₀ω² + iω = κk², so k² = (τω² + iω)/κ and

    v_ph → √(κ/τ₀) = c_h  as ω → ∞,  with v_ph ≈ √(2κω) for ωτ₀ ≪ 1

**Numbers (steel-like constants):** κ = 1.254×10⁻⁵ m²/s.

| τ₀ (s) | c_h = √(κ/τ₀) (m/s) | frequency above which LS departs from Fourier |
|---|---|---|
| 1e−12 | 3541.4 | ≳ 159 GHz |
| 1e−11 | 1119.9 | ≳ 15.9 GHz |
| 1e−10 | 354.1 | ≳ 1.59 GHz |

(Departure scale is ω ≈ 1/τ₀, i.e. f ≈ 1/(2πτ₀).)

### R6. The check most likely to catch a wrong "LS" plot

At 1 GHz with τ₀ = 10⁻¹¹ s, ωτ₀ = 0.063 — **LS is still within 0.2% of Fourier**. A published LS dispersion curve that visibly differs from Fourier at MHz frequencies is either using a much larger τ₀ than stated, or has mis-scaled τ₀. Our script reproduces exactly this: LS thermal branch = 12.6 m/s at 1 MHz, identical to Biot to three figures.

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| Lord & Shulman 1967, JMPS 15(5):299–309 | Crossref API | Record only |
| Coupled 1-D form ρc(T_t + τ_q T_tt) + βθ₀(tr ε̇ + τ_q tr ε̈) = kΔT | Noble (2026) preprint §4.1, DOI 10.21203/rs.3.rs-10734164-v1 — **SECONDARY, unrefereed**; states "one common linear form", explicitly noting notational variance | Body (PDF) |
| c_h = √(α/τ_q) with α = k/(ρc) | Same preprint, Proposition 2 — **SECONDARY**. I re-derived it independently (rigid limit) and got the identical expression | Body + my derivation |
| τ₀→0 ⇒ Biot | My symbolic check | Derivation |

## Checks done

1. **Limit check (symbolic)**: `dets[LordShulman].subs(τ₀,0) − dets[Biot] = 0` → **PASS**.
2. **Analytic vs numeric**: c_h = √(κ/τ₀) at three τ₀ reproduced from the numeric branch solver.
3. **Regression against Biot**: at 1 MHz the LS and Biot thermal branches agree to 3 significant figures, as they must when ωτ₀ ≪ 1. This is a genuine test that the τ₀ terms are assembled correctly.
4. **Independent confirmation of a third party's proposition**: the preprint's Prop. 2 (finite characteristic speed) is correct as far as the principal part is concerned; I verified the characteristic polynomial ∂_t² − c_h²∂_x² is unchanged by the damping term τ₀⁻¹∂_t.

## Confidence

- **HIGH** on the derivation, the dispersion relation, the τ₀→0 limit and c_h.
- **MEDIUM** on attribution detail (that Lord & Shulman introduced *exactly* this flux-relaxation route rather than a temperature-rate route — both are described in the literature, and I could not read the paper to see which they used).
- **LOW** on any statement about what LS themselves claimed regarding admissible τ₀ values.

## NOT verified / open issues

1. **Full text of LS (1967) not opened.** Their own derivation route (Cattaneo flux relaxation vs an entropy-flux relaxation) is **UNVERIFIED**. This matters because the brief's hint — "one relaxation" — is right, but *where* the relaxation sits is exactly the point on which papers disagree.
2. **Placement of τ₀ on the coupling term is not uniform in the literature.** Two variants appear: τ₀ on the thermal term only, and τ₀ on both thermal and coupling terms. They give different dispersion at O(δωτ₀). Our review must pick one and say so; this is a candidate NOTATION.md/energy-balance inconsistency (flagged again in V-B2z).
3. **Physical magnitude of τ₀ is unresolved in this file.** Values 10⁻¹⁴–10⁻⁹ s are quoted in the literature for different materials/regimes; I did not verify any measured value. Do not print a "typical τ₀" without a primary source.
4. Whether LS's theory is thermodynamically admissible in the strict Coleman–Noll sense (rather than merely well posed) is **not settled here**; see the MGT/GN discussion in V-B2i and V-B2z.
