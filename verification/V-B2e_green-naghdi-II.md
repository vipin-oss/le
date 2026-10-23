# V-B2e — Green–Naghdi Type II (thermoelasticity without energy dissipation)

**Access date 2026-10-22.**

## Task

As V-B2a, for GN Type II. This is the first model in the set with a **conserved** energy and a finite thermal speed, so it is the cleanest test case for Phase B3.

## Method

1. **Provenance.** Green, A.E. & Naghdi, P.M. (1992) "On undamped heat waves in an elastic solid", *J. Thermal Stresses* **15**(2):253–264, DOI 10.1080/01495739208946136 (Crossref 1555 / OpenAlex 1687); and (1993) "Thermoelasticity without energy dissipation", *J. Elasticity* **31**(3):189–208, DOI 10.1007/BF00044969 (2194 / 2402). Read level: **record only — neither full text opened.**
2. Derived the 1-D system with the thermal-displacement variable α̇ = θ, then the dispersion relation.
3. Checks in `V-B2_wave_speeds.py`: (i) the rigid-limit condition is an **exact** wave equation (symbolic PASS); (ii) the numeric thermal branch is **non-dispersive** (1125.9 m/s at 1 kHz, 1 MHz and 1 GHz); (iii) the speed matches the LS speed √(κ/τ₀) when k* is calibrated as k_th/τ₀ — a cross-model consistency test.

## Result

### R1. Heat law

GN-II replaces the heat flux by a **thermal-displacement gradient**:

    q_i = −k* α_,i ,     α̇ = θ

where k* is a material constant ("conductivity" of the thermal displacement; **different units from k_th**). With the energy balance ρc θ̇ + βT₀ ε̇ = −∇·q and α̇ = θ:

    ρc θ̈ + βT₀ ε̈ = k* ∇²θ

**No θ̇ term** → no dissipation. The θ-equation is a wave equation.

### R2. Coupled equations, 1-D

    ρ ü = M u_xx − β θ_x
    ρc θ̈ + βT₀ ü_x = k* θ_xx

### R3. Parameters

As V-B2a, **minus** k_th as the conducting constant, **plus**

| Symbol | Meaning | Units |
|---|---|---|
| k* | GN thermal-displacement conductivity | W·s/(m·K) (conductivity × time) |
| c_T = √(k*/(ρc)) | thermal wave speed (rigid limit) | m/s |

Note k* has the units of (thermal conductivity)×(time), so a numerical value of k* is meaningless without stating the time scale it was calibrated on. **This is a real source of incomparable numbers across papers** (see Checks 3).

### R4. Admissibility

- **k* > 0**: required for a real thermal speed; k* < 0 gives k² < 0 for real ω — an evanescent/growing thermal field with no propagation (and, with coupling, an unstable branch).
- **c > 0, M > 0, ρ > 0.**
- **No dissipation term ⇒ the energy is conserved** (for insulated/periodic boundaries); there is no entropy production from conduction. This is the defining and most contested feature: see R6.
- **Finite thermal speed** c_T = √(k*/(ρc)), frequency-independent.

### R5. Characteristic equation and speeds

    [M k² − ρω²,  −iβT₀ω²k ] 
    [ −iβk,        k* k² − ρcω² ]
    ⇒  (M k² − ρω²)(k* k² − ρcω²) − β²T₀ ω² k² = 0

Rigid limit: k* k² = ρcω², i.e. **exactly** k = ω/c_T — dispersionless.

**Numbers:** with k* = k_th/τ₀ = 4.5×10¹² (τ₀ = 10⁻¹¹ s), c_T = 1125.9 m/s, and the numeric branch is 1125.9 m/s at **all three** frequencies tested. Compare LS with the same τ₀: 1119.9 m/s asymptotic. The ~0.5% difference is the thermoelastic coupling (δ = 0.01), not a calibration error — a useful cross-check between two theories that should agree at leading order.

**Second branch**: the elastic wave at 5765.9 m/s (vs 5767.1 for Biot) — GN-II's coupling slightly *softens* the elastic branch, consistently with it being a non-dissipative coupling.

### R6. The honest caveat: "without energy dissipation" is a strong physical claim

GN-II has no mechanism to attenuate a thermal pulse. Real second-sound experiments (solid He, NaF, Bi) observe **strong** attenuation of the thermal wave. So GN-II is either an idealisation valid over a limited window, or physically wrong for the materials where second sound is actually seen. A review that lists GN-II as one option among nine without saying this is not doing its job. The defence of GN-II is mathematical: it gives a well-posed, energy-conserving hyperbolic system, which is valuable for numerical and proof work (domain-of-influence theorems, uniqueness). **The review should separate "mathematically clean" from "physically adequate" — they are different virtues and GN-II has only the first.**

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| GN 1992 and 1993 bibliographic data | Crossref API | Record only |
| "Type II theory permits heat-wave propagation without classical energy dissipation" (qualitative) | Noble (2026) preprint §5.2 — **SECONDARY, unrefereed** | Body (PDF) |
| q = −k*α_,i with α̇ = θ; ρcθ̈ + βT₀ε̈ = k*∇²θ; c_T = √(k*/(ρc)) | **standard form, NOT source-verified** | — |
| Non-dispersive thermal branch | My numeric computation | Derivation |

## Checks done

1. **Symbolic (exact) check**: the rigid-limit thermal equation is literally `k* k² − ρcω² = 0` — a pure wave with no ω-dependence in the speed. **PASS** (script prints this check).
2. **Non-dispersiveness (numeric)**: v_ph = 1125.9 m/s at 1 kHz, 1 MHz, 1 GHz — identical to 5 significant figures. This is the property that distinguishes GN-II from every other model in the set and it is exactly what a reviewer should demand be demonstrated.
3. **Cross-model calibration**: setting k* = k_th/τ₀ reproduces the LS thermal speed (1119.9 vs 1125.9, difference explained by coupling δ=0.01). This proves the two models are *not* independent in their high-frequency limit, which is a substantive review point: GN-II and LS agree asymptotically.
4. **Dimensional analysis**: k*/(ρc) must be (m/s)²; k* has units W·s/(m·K) = kg·m/(s³·K); ρc is kg/(m³)·J/(kg·K) = kg/(m·s²·K); ratio = m²/s² ✓.

## Confidence

- **HIGH** on the mathematics: dispersion relation, exact non-dispersiveness, speed formula, and the GN-II/LS asymptotic agreement.
- **MEDIUM** on the form q = −k*α_,i being exactly GN's (it is the standard reading, and it is internally consistent with the "no dissipation" name).
- **LOW** on any statement about what GN proved in the 1992/1993 papers, and on the correct k* values for real materials.

## NOT verified / open issues

1. **Full texts not opened.** GN's own energy function and their proof of "no dissipation" are **UNVERIFIED**. In particular I have not verified whether their energy functional is positive definite for all admissible states — which is precisely what B3 will need.
2. **k* values for real materials are not established here.** No primary measurement was found or verified. Any table of k* in the manuscript must be sourced or dropped.
3. **Whether GN-II is experimentally falsified or merely untested** is not settled by this file. I found no verified second-sound attenuation data in this session. The review needs a sourced answer; without one it should say "untested at the required resolution", not "validated".
4. Type II is sometimes written with a temperature-only wave equation and the coupling absent; the coupled form in R2 is standard but I did not verify it against GN's text.
