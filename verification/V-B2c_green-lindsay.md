# V-B2c — Green–Lindsay (two relaxation times)

**Access date 2026-10-22.** No subscription full text. ⚠ This file carries a larger UNVERIFIED block than the others: see §NOT verified.

## Task

As V-B2a, for Green–Lindsay (GL) theory. The brief's hint: "two relaxations; note there is NO relaxation in the heat flux but in the temperature rate terms" — this hint is the specific thing I test below.

## Method

1. **Provenance.** Green, A.E. & Lindsay, K.A. (1972) "Thermoelasticity", *J. Elasticity* **2**(1):1–7, DOI 10.1007/BF00045689. Crossref 2929, OpenAlex 2947. Read level: **record only — full text NOT opened.**
2. Searched for an open-access statement of the GL linearised equations. **Result: not found.** The one openly readable critical review I could obtain (Noble 2026 §5.1) describes GL only qualitatively — it gives no equations. That is itself a finding worth recording: a 2026 "critical review with analytical proofs" does not write down the GL system it discusses.
3. Consequence: the GL system below is the **standard form as commonly used**, not transcribed from a source I opened. It is labelled accordingly, and only the *mathematical* consequences of the stated form are verified.

## Result

### R1. Constitutive structure (as commonly written)

GL introduces two relaxation times τ₁, τ₂ by rate-dependence of the **entropy/temperature** terms, not of the heat flux:

    σ_ij = λ ε_kk δ_ij + 2μ ε_ij − β (θ + τ₁ θ̇) δ_ij
    ρη = ρc θ + β T₀ ε_kk + ...      (entropy carries τ₁ as well)
    q_i = −k_th θ_,i                  ← **no relaxation in the flux**

and the heat equation

    ρc(θ̇ + τ₁ θ̈) + βT₀(ε̇_kk + τ₂ ε̈_kk) = k_th θ_,ii

with the ordering constraint

    τ₂ ≥ τ₁ ≥ 0

**The brief's hint is corroborated at the level of structure**: GL keeps Fourier's law for q (no flux relaxation) and puts the relaxation on the temperature-rate / temperature-rate-of-strain terms. This is what distinguishes GL from LS, and it is why the two theories are *not* interchangeable despite both having "relaxation times".

### R2. Coupled equations, 1-D

    ρ ü = M u_xx − β(θ_x + τ₁ θ̇_x)
    ρc(θ̇ + τ₁θ̈) + βT₀(u̇_x + τ₂ü_x) = k_th θ_xx

### R3. Parameters

As V-B2a, plus τ₁, τ₂ [s] with **τ₂ ≥ τ₁ ≥ 0**. Note there is **no** τ on the heat flux, so GL does not have a clean "thermal wave speed √(κ/τ)" of the LS type.

### R4. Admissibility

- **τ₂ ≥ τ₁ ≥ 0** is GL's own ordering requirement. If τ₁ > τ₂, the theory predicts a *faster* response of the temperature than of the strain it is coupled to; the natural energy functional loses positivity and one branch can grow. (Stated as a structural expectation — I did not verify a published instability theorem for τ₁ > τ₂.)
- **k_th > 0, c > 0, M > 0, ρ > 0** as before.
- **Finite thermal speed**: GL does produce a finite propagation speed (this is its purpose), but unlike LS the speed is not simply √(κ/τ); its expression follows from the full cubic/quartic in ω and I have **not** verified the published closed form.

### R5. Characteristic equation

Because the coupling term carries τ₂ while the thermal terms carry τ₁, the determinant is

    (M k² − ρω²)(k_th k² − iωρc(1−iωτ₁)) + iβ²T₀ωk²(1−iωτ₂) = 0

⚠ **This is my construction from the R1 form**, not a transcription. It has the correct LS-like structure but with **two different prefactors** (1−iωτ₁) and (1−iωτ₂) — which is the mathematically essential content of "two relaxation times". Anyone checking our review's GL equation should check exactly this: if a paper writes the same (1−iωτ) in both places, it has silently collapsed GL into LS.

**Diagnostic worth putting in the paper:** GL ≡ LS when τ₁ = τ₂ = τ₀. Therefore any published "comparison of LS and GL" whose two curves coincide in the limit τ₁→τ₂ is correct, and any that reports them as qualitatively different *at* τ₁ = τ₂ contains an error.

### R6. When GL fails

- It has no flux relaxation, so it cannot represent heat-flux inertia (the physical content of Cattaneo). Where flux inertia is the mechanism (very high frequency, rarefied phonon transport), GL is the wrong tool.
- τ₁, τ₂ are not independently measurable in any experiment I could verify; they are fitted. A review should say that plainly.

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| Green & Lindsay 1972, J. Elasticity 2(1):1–7 | Crossref API | Record only |
| "two nonnegative times, one entering stress/entropy–temperature coupling and one entering the thermal equation"; "without using a heat-flux rate in exactly the Lord–Shulman manner" | Noble (2026) preprint §5.1, DOI 10.21203/rs.3.rs-10734164-v1 — **SECONDARY, unrefereed, and QUALITATIVE ONLY (no equations given)** | Body (PDF) |
| GL equations in R1–R2 | **standard form, NOT source-verified** — labelled UNVERIFIED | — |

## Checks done

- **Structural check**: the τ₁/τ₂ asymmetry in R5 is a *derived* consequence of the R1 form and preserves the correct limits (τ₁=τ₂=τ₀ ⇒ LS form; τ₁=τ₂=0 ⇒ Biot). I verified the τ₁=τ₂=0 limit symbolically reduces to the Biot determinant.
- **Cross-theory consistency**: GL's heat flux is Fourier, so the energy-flux expression used in Phase B3 should be the same as Biot's for GL — a constraint that will be used in B3 to test the manuscript.
- **Honest negative**: I could not obtain any open-access statement of the GL equations, from a review or otherwise. Two searches.

## Confidence

- **HIGH** that the τ₁/τ₂ structure described above is the standard GL construction and that GL ≡ LS at τ₁=τ₂ (this is a mathematical identity of the stated form, checkable by substitution).
- **MEDIUM** on the exact placement of τ₂ (on ε̈_kk vs on the whole coupling bracket). Variants exist.
- **LOW** on essentially all bibliographic content of the GL paper itself, and on the ordering constraint being *theirs* rather than a later imposition.

## NOT verified / open issues

1. **GL (1972) full text NOT opened.** The equations in R1–R2 are the common textbook form. **Everything about what Green & Lindsay actually wrote is UNVERIFIED**, including: the exact entropy expression, whether τ₂ multiplies ε̈_kk or the whole bracket, and whether they stated τ₂ ≥ τ₁.
2. **This is the weakest file in Phase B2.** It is also, uncomfortably, the model on which the manuscript is most likely to make a confident-sounding claim ("GL has two relaxations, one in the flux…"), because the brief's hint asserts something specific. I can confirm the *standard modern reading* (no flux relaxation; relaxation on temperature-rate terms) but **not** that it matches the 1972 paper. If the handler can supply the 7-page PDF, this file can be upgraded to HIGH in ~20 minutes.
3. **No GL dispersion relation from a primary source** was compared against R5. The cubic/quartic structure is mine.
4. The claim "GL produces a finite thermal speed" is standard but I have **not** verified the closed-form GL speed, and I would not let the manuscript print one without a source.
5. Ignaczak & Ostoja-Starzewski, *Thermoelasticity with Finite Wave Speeds* (OUP, DOI 10.1093/acprof:oso/9780199541645.001.0001, registered **2009-09-24**, 208 citations) is the obvious monograph source for GL. **SECONDARY-SOURCE ONLY and NOT opened** — note the book is commonly cited as 2010; Crossref registers 2009.
