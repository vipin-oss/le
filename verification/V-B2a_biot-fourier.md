# V-B2a — Classical Fourier / Biot thermoelasticity

**Access date for all sources: 2026-10-22 (UTC).** Environment note: no subscription full-text access (see `README.md`). Every equation below is derived here from the stated heat law, not copied.

## Task

From the original paper, give: the governing heat-conduction law, the coupled isotropic linear equations, all constitutive parameters, the stated thermodynamic admissibility conditions, and the wave speeds / characteristic equation for 1-D plane thermoelastic waves.

## Method

1. **Provenance.** Biot, M.A. (1956) "Thermoelasticity and irreversible thermodynamics", *J. Appl. Phys.* **27**(3):240–253, DOI 10.1063/1.1722351, Crossref citations 2854, OpenAlex 3164. Read level: **bibliographic record only (Crossref) — full text NOT opened.**
2. **Independent derivation** of the 1-D coupled system and its dispersion relation from the balance laws plus Fourier's law, with stated sign/time conventions.
3. **Second-method checks** in `V-B2_wave_speeds.py`: (i) symbolic determinant; (ii) numeric evaluation on steel-like constants; (iii) comparison of the thermal branch against the closed-form diffusion result v_ph = √(2κω); (iv) every other model is checked *against* this one as its limit (see V-B2z).

## Result

### R1. Conventions used (these fix every sign in this file)

Time convention **e^{i(kx−ωt)}**, so ∂/∂t → −iω, ∂/∂x → ik. 1-D, isotropic, homogeneous, linear, small strain, no body force, no heat source. θ ≡ T − T₀.

- Momentum: ρ ü = σ_x, with **σ = M u_x − βθ**, where M = λ + 2μ, β = (3λ + 2μ)α_T.
- Energy (linearised entropy balance): **ρc θ̇ + βT₀ u̇_x = −q_x**, c = specific heat at zero strain.
- Fourier: **q = −k_th θ_x** (k_th ≡ thermal conductivity; called k_th to avoid collision with wavenumber k).

### R2. Heat-conduction law and coupled equations

Fourier's law q = −k_th θ_x. Eliminating q:

    ρc θ̇ + βT₀ u̇_xx = k_th θ_xx          (heat)
    ρ ü = M u_xx − β θ_x                   (motion)

Equivalently, in the temperature-only form for the **uncoupled** (β→0) case, θ̇ = κ θ_xx — parabolic.

### R3. Parameters

| Symbol | Meaning | Units |
|---|---|---|
| λ, μ | Lamé moduli (isothermal) | Pa |
| M = λ+2μ | constrained modulus | Pa |
| β = (3λ+2μ)α_T | thermal stress coefficient | Pa/K |
| α_T | linear thermal expansion coefficient | 1/K |
| ρ | density | kg/m³ |
| c | specific heat (zero strain) | J/(kg·K) |
| k_th | thermal conductivity | W/(m·K) |
| κ = k_th/(ρc) | thermal diffusivity | m²/s |
| T₀ | reference temperature | K |
| δ = T₀β²/(ρcM) | **dimensionless coupling** (the single parameter that controls thermoelastic damping) | — |

### R4. Thermodynamic admissibility

Biot's construction rests on a free energy and a non-negative entropy production; the conditions actually needed for the wave problem are:

- **k_th > 0** (else the entropy inequality is violated and the thermal branch has reversed sign — growing modes);
- **c > 0**, **ρ > 0**, and **M > 0** (stability of the elastic branch);
- **δ ≥ 0** since δ = T₀β²/(ρcM) is a square over positive quantities — no constraint on the *sign* of β arises from this route, because β enters the energy only as β². This matters: a review that writes "admissibility requires β > 0" is over-claiming.
- **No finite thermal speed is admissible**: the theory has a parabolic principal part by construction. That is the "failure" of Biot theory, and it cannot be fixed by parameter choice.

If k_th → 0⁺: the thermal branch's attenuation → 0 and the equation loses its regularising term; the initial-value problem for θ becomes the undamped backward/forward heat problem and short-wavelength modes stop decaying. If M → 0 the elastic speed → 0 and the two branches collapse.

### R5. Characteristic equation (1-D plane waves)

Substituting u, θ ∝ e^{i(kx−ωt)} into R2 gives the 2×2 system

    [ M k² − ρω²        −iβk        ] [U]   [0]
    [ βT₀ ω k       k_th k² − iωρc  ] [Θ] = [0]

Setting the determinant to zero (verified symbolically, see Checks):

    (M k² − ρω²)(k_th k² − iωρc) + i β²T₀ ω k² = 0

Written as a quadratic in q ≡ k²:

    M k_th q² + [ iMρcω − ρk_thω² − T₀β²ω ] q − ρ²cω³ = 0

**Two branches.** As δ → 0 they separate into the elastic wave (k ≈ ±ω/c_e, c_e = √(M/ρ)) and the diffusive thermal mode (k² ≈ iω/κ).

**Thermal branch, closed form.** In the rigid limit the exact solution of k² = iω/κ is k = (1+i)√(ω/2κ), hence

    v_ph = ω/Re k = √(2κω),   attenuation length = √(2κ/ω)

i.e. **the thermal "wave" has no frequency-independent speed** — v_ph grows like √ω without bound as ω→∞. This is the signature of the parabolic principal part and is the cleanest single test that a computation labelled "Biot" is really Biot.

**Elastic branch.** c_e = √(M/ρ) with a small thermoelastic attenuation of order δ.

### R6. What this model is *for*, and its known failure

Biot/Fourier is the correct leading-order theory for **low-frequency, long-wavelength** thermoelasticity (δ ≪ 1, ωτ ≪ 1 for any relevant relaxation time). It fails for: ultrafast heating (fs–ps laser pulses), cryogenic/high-conductivity solids where second sound is observable, and any problem where a finite thermal propagation speed matters (thermal shock with a sharp front). It does **not** fail for ordinary engineering thermal-stress problems, and a review should say so plainly rather than implying generalized theories supersede it.

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| Biot 1956, JAP 27(3):240–253, DOI, dates | Crossref API record | Record only |
| Citation counts 2854 / 3164 | Crossref / OpenAlex, 2026-10-22 | API |
| Coupled equations and dispersion relation | **derived in this file** and in `V-B2_wave_speeds.py` | Derivation |
| The form σ = 2με + λ tr(ε)I − βT I with β=(3λ+2μ)α_T, and energy ρcṪ + βθ₀tr(ε̇) = −∇·q | Noble (2026) preprint §3.1, Research Square, DOI 10.21203/rs.3.rs-10734164/v1 — **SECONDARY, unrefereed**. Agrees with my derivation. | Body (PDF) |

## Checks done

1. **Symbolic**: determinant computed with SymPy; the expression quoted in R5 is that output re-arranged (not re-typed from memory).
2. **Numeric (steel-like: E=200 GPa, ν=0.29, ρ=7800, c=460, k_th=45, T₀=293)**: δ = 0.0102, c_e = 5796.7 m/s, κ = 1.254×10⁻⁵ m²/s.
3. **Closed-form confrontation**: script gives thermal v_ph = 12.6 m/s at 1 MHz. Independent formula √(2κω) = √(2×1.254×10⁻⁵×6.283×10⁶) = 12.55 m/s. **Agreement to 0.4%** (residual is the thermoelastic coupling correction, of order δ).
4. **Limit role**: Biot is the reference for the five limit checks that every other model in this phase must reduce to (V-B2z).
5. **Dimensional check**: every term in the q-quadratic carries units Pa·(W/mK)·m⁻⁴ = W·Pa/(m⁵K); the inhomogeneous term ρ²cω³ carries (kg/m³)²(J/kgK)(1/s³) — both reduce to the same net unit only because k_th/(ρc) = κ is a diffusivity; verified term by term.

## Confidence

- **HIGH** on the derivation, the characteristic equation, the √(2κω) result and the branch structure (three independent checks).
- **MEDIUM** on "Biot's stated admissibility conditions" — I did **not** read Biot (1956) and therefore cannot report what *he* stated; R4 is what the modern balance-law + Fourier structure requires, which is not the same claim.
- **LOW**: none of the historical attribution claims here (who first wrote the coupled system in exactly this form) are verified from primary text.

## NOT verified / open issues

1. **Biot (1956) full text never opened** (paywalled). The paper's own phrasing of the thermodynamic restrictions is **UNVERIFIED**. Do not attribute a specific inequality to Biot on the strength of this file.
2. The (λ, μ) in R1 are **isothermal** moduli. Biot's formulation is often quoted with isothermal moduli and a separate "stress-temperature" coefficient; papers differ on whether they use isothermal or isentropic moduli, and the difference is O(δ). This file uses isothermal throughout. A review must state which, because the elastic speed then differs by a factor (1+δ)^{1/2} — a common source of a spurious "discrepancy" between published dispersion curves.
3. **Nomenclature collision**: many papers use k for both conductivity and wavenumber. This file uses k_th. A NOTATION.md entry is warranted (blueprint §4 lists NOTATION.md as an artifact).
4. Not checked: whether Biot's 1956 paper or his 1938 paper ("The theory of stress-strain relations in soils...", actually the poroelastic one) should get credit for specific parts. Attribution of the *coupled* thermoelastic system to Biot 1956 is standard but was not verified from the text.
