# V-B2i — Moore–Gibson–Thompson (MGT) thermoelasticity

**Access date 2026-10-22.**

## Task

As V-B2a, for MGT. This is the model with the strongest verified result in Phase B2: I independently reproduced its stability criterion and both of its characteristic speeds.

## Method

1. **Provenance.** Quintanilla, R. (2019) "Moore–Gibson–Thompson thermoelasticity", *Math. Mech. Solids* **24**(12):4020–4031, DOI 10.1177/1081286519862007. Crossref 409, OpenAlex 409. Read level: **record only — full text NOT opened.**
   - **Dating correction:** Crossref gives `issued` 2019-07-21; the volume is 24(12) 2019. The paper is very frequently cited as **2018** — that is wrong (it is a 2019 publication; the 2018 date presumably comes from a preprint or from the online-first confusion). Recorded again from V-B1c because it is exactly the sort of repeated error the brief asks me to flag.
2. Obtained the *scalar MGT prototype* and its stability criterion from an openly readable source (Noble 2026 §8.1–8.2, PDF).
3. **Independently re-derived** the Routh–Hurwitz threshold and **verified it numerically** by root computation in three regimes (see R4). Also computed the rigid-case dispersion analytically and confirmed both frequency limits.

## Result

### R1. The MGT equation and its heat-transport reading

The MGT equation originates in acoustics as a third-order-in-time wave equation. The scalar thermal prototype is

    τ T_ttt + T_tt − b ΔT_t − c² ΔT = 0

with τ > 0 a relaxation time and b > 0, c² > 0 effective coefficients. In thermoelasticity the temperature equation is coupled to strain-rate terms and to the momentum balance.

Physically MGT is what one gets when the heat flux relaxation of Cattaneo is retained **without** discarding the second time derivative of temperature — i.e. it is "Cattaneo with thermal inertia" rather than "Cattaneo linearised in τ". That is why it is a *third*-order theory like TPL, but derived from a different starting point (flux relaxation in an acoustics-like setting rather than a thermal-displacement lag).

### R2. Coupled equations, 1-D (form used here)

    ρ ü = M u_xx − β θ_x
    ρc(τ θ⃛ + θ̈) + βT₀(τ u⃛_x + ü_x) = −k_th θ_xx + b θ̇_xx

⚠ **Flag:** the coupled MGT thermoelastic form of Quintanilla includes the strain-rate coupling through the same τ-weighted operator, but I could **not** verify his exact coupling terms (full text unavailable). The thermal prototype in R1 **is** established (secondary source); the coupling in R2 is my construction consistent with it. Treat the coupled 1-D determinant below as "the mathematics of this stated system", not as Quintanilla's equation.

### R3. Parameters

As V-B2a, plus

| Symbol | Meaning | Units |
|---|---|---|
| τ | MGT relaxation time | s |
| b | effective thermal rate coefficient (multiplies ∇²θ̇) | m²/s |
| c² | effective thermal wave coefficient (multiplies ∇²θ) | m²/s² |
| **γ = b − τc²** | **the MGT stability number** | m²/s |

γ is the quantity that matters and the one that published parameter studies most often fail to report.

### R4. Admissibility — the MGT stability number (independently verified)

For a mode e^{st+iκx} the rigid prototype gives the cubic

    τs³ + s² + bκ²s + c²κ² = 0

Monic form s³ + a₁s² + a₂s + a₃ with a₁ = 1/τ, a₂ = bκ²/τ, a₃ = c²κ²/τ. Routh–Hurwitz for a cubic requires a₁ > 0, a₂ > 0, a₃ > 0 **and a₁a₂ > a₃**. The first three hold when τ, b, c² > 0. The last gives

    (1/τ)(bκ²/τ) > c²κ²/τ   ⇒   **b > τc²   i.e.   γ > 0**

**Independent numeric verification** (root computation of the cubic, κ = 10³ m⁻¹):

| τ (s) | b (m²/s) | c² (m²/s²) | γ = b − τc² | max Re(s) | verdict |
|---|---|---|---|---|---|
| 1e−11 | 2.5e−5 | 1.254e6 | **+1.25e−5** | −6.23 | stable |
| 1e−11 | 1.254e−5 | 1.254e6 | **+1.7e−21** (≈0) | −1.49e−10 (≈0) | **marginal** |
| 1e−11 | 9.0e−6 | 1.254e6 | **−3.54e−6** | **+1.77** | **UNSTABLE** |
| 1e−11 | 1.0e−6 | 1.254e6 | **−1.15e−5** | **+5.77** | **UNSTABLE** |

Four things this establishes:
1. The criterion γ > 0 is **correct** for the rigid prototype (independently of the source that states it).
2. γ = 0 is genuinely the boundary: the max real part collapses to ~10⁻¹⁰ (numerically zero).
3. γ < 0 produces **exponential growth**, with the growth rate *increasing* as γ becomes more negative.
4. **Positivity of τ, b, c² is not sufficient.** This is the substantive warning: a parameter study that reports only "τ, b, c² > 0" can be presenting unstable solutions as physical.

**If violated:** the temperature field grows without bound; in the coupled system this feeds the strain and the elastic branch also grows. There is no bounded solution and no meaningful reflection/transmission coefficient — which matters directly for Phase B3.

### R5. Characteristic equation and wave speeds

Rigid-case dispersion (derived and verified):

    k² = ω²(1 − iωτ)/(c² − iωb)

Two clean limits, both confirmed numerically:

| frequency | v_ph | limit |
|---|---|---|
| low (ωτ ≪ 1) | → √(c²) | acoustic-like conduction |
| high (ωτ ≫ 1) | → √(b/τ) | MGT characteristic speed |

**Numbers** (τ=10⁻¹¹, b=2.5×10⁻⁵, c²=1.254×10⁶):

| f | v_ph | attenuation length |
|---|---|---|
| 1 kHz | 1119.8 m/s | 5.71×10⁶ m |
| 1 MHz | 1119.8 m/s | 5.71 m |
| 1 GHz | 1123.6 m/s | 5.78 µm |
| 100 GHz | 1575.0 m/s | 64 nm |

with predicted asymptotes √(c²) = 1119.8 m/s and √(b/τ) = 1581.1 m/s. At 100 GHz the computed 1575.0 m/s is 0.4% below the asymptote — the expected finite-ωτ deviation, not an error.

**The MGT signature:** the phase speed *increases* with frequency between the two plateaus, i.e. MGT is **normally dispersive in the thermal branch**, where LS and GN-II are asymptotically non-dispersive. That is the observable that could in principle discriminate MGT from LS/GN-II.

**Coupled-system caveat:** in the full coupling the third thermal mode can become purely evanescent (Re k = 0), so "phase velocity" is undefined for it; the script reports that honestly rather than printing ω/Re k → ∞ as a speed. For such modes quote an attenuation length, not a speed. (This is a mistake I have seen implied in published dispersion plots; it is worth one sentence in the review.)

### R6. Where MGT fails

- It needs γ > 0, a constraint on **three** parameters jointly — hard to verify experimentally and routinely ignored.
- It has the same parameter-identification problem as TPL: τ is not independently measured in any work I could verify.
- Its advantage over TPL is that it arises from flux relaxation (a mechanism with a physical argument) rather than a thermal-displacement lag.

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| Quintanilla 2019, MMS 24(12):4020–4031, DOI, issued 2019-07-21 | Crossref API | Record only |
| Scalar prototype τT_ttt + T_tt − bΔT_t − c²ΔT = 0; cubic τs³+s²+bκ²s+c²κ²; Routh–Hurwitz ⇒ γ = b − τc² > 0 | Noble (2026) preprint §8.1–8.2, DOI 10.21203/rs.3.rs-10734164/v1 — **SECONDARY, unrefereed** | Body (PDF) |
| γ criterion, the numerical table, k² = ω²(1−iωτ)/(c²−iωb), both speeds | **My own derivation + numeric verification** | Derivation |
| MGT's acoustics lineage | Not verified in this session | — |

## Checks done

1. **Independent re-derivation** of the threshold via Routh–Hurwitz (not taken on trust).
2. **Four-point numeric verification** of the criterion, including the marginal case (γ≈0 → max Re s ≈ 0 to 10⁻¹⁰) and two unstable cases with growing growth rates. This is a strong test: a criterion that merely *looked* right would not reproduce the marginal behaviour.
3. **Both speed asymptotes** confirmed: √(c²) at low frequency (exact match to 5 s.f.) and √(b/τ) approached at high frequency (0.4% at ωτ ≈ 6.3).
4. **Consistency with the source's Proposition 4**: the preprint claims the same criterion; I confirm it for the rigid prototype, which is the scope it states. I did not verify their claim for the coupled system.
5. **Dating correction** made against a commonly repeated error (2018 vs 2019), cross-checked against two indices.
6. **Reporting-integrity check**: I detected and did *not* report meaningless phase speeds for evanescent modes.

## Confidence

- **HIGH** on: γ = b − τc² > 0 for the rigid prototype; the marginal behaviour at γ = 0; both characteristic speeds; the numerical table.
- **MEDIUM** on the coupled 1-D system in R2, and hence on using my coupled determinant for anything quantitative.
- **LOW** on Quintanilla's exact coupled formulation, and on the acoustics-lineage attribution.

## NOT verified / open issues

1. **Quintanilla (2019) full text not opened.** The coupled MGT thermoelastic equations are **UNVERIFIED**; R2 is my construction. The manuscript must take its MGT system from the paper, not from this file.
2. **The acoustics lineage is unattributed here.** MGT papers usually trace the equation to Moore & Gibson (1960) and Thompson (1972), and the mathematical analysis to Kaltenbacher–Lasiecka–Polymilis and to Jordan. **None of those references was verified in this session.** If the review draws a lineage diagram, every arrow needs a verified citation.
3. **Coupled-system stability is an open question in this file.** γ > 0 is established for the rigid prototype only; whether it is also sufficient for the coupled thermoelastic system depends on the coupling terms I could not read.
4. **No measured τ, b, c² for any material** was found or verified. Any parameter table must be sourced.
5. The claim that MGT is "normally dispersive" (R5) is verified for the rigid model; coupling could alter it, and that should be checked numerically before printing.
