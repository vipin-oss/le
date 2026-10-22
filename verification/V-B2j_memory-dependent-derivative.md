# V-B2j — Memory-dependent derivative (Wang & Li) in thermoelasticity

**Access date 2026-10-22.**

## Task

As V-B2a, for the memory-dependent derivative (MDD) and its use in thermoelasticity.

## Method

1. **Provenance.** Wang, J.-L. & Li, H.-F. (2011) "Surpassing the fractional derivative: Concept of the memory-dependent derivative", *Comput. Math. Appl.* **62**(3):1562–1567, DOI 10.1016/j.camwa.2011.04.028. Crossref 448. Read level: **record only — full text NOT opened.**
2. No openly readable statement of the MDD definition *and* its thermoelastic use was found in this session. The definition below is the universally used one; it is labelled accordingly.
3. I derived the dispersion consequences generically in terms of the memory kernel, which is the part that can be checked without the paper.

## Result

### R1. Definition (standard)

For a memory (delay) window ω_m > 0 and a kernel K:

    D_{ω_m} f(t) = (1/ω_m) ∫_{t−ω_m}^{t} K(t − s) f'(s) ds

Common kernels: K ≡ 1 ("constant"), K = 1 − (t−s)/ω_m, K = [1 − (t−s)/ω_m]², and exponential forms. **The model is only defined once K and ω_m are both specified** — a point frequently omitted in the thermoelasticity literature.

Limit: as ω_m → 0⁺, D_{ω_m}f → f'(t) for any normalised kernel (the kernel-weighted average of f' over a shrinking window). So MDD is a *smoothing of the time derivative*, not a fractional operator.

### R2. Use in thermoelasticity

The standard substitution replaces the temperature rate in the heat equation by an MDD:

    ρc D_{ω_m}θ + βT₀ D_{ω_m}ε_kk = k_th ∇²θ

i.e. the classical (Biot) heat equation with both time derivatives "delayed". Variants replace only θ̇, or apply the MDD to the flux law q + τ D_{ω_m}q = −k∇θ (an "MDD-Cattaneo" hybrid).

### R3. Parameters

As V-B2a, plus **ω_m [s]** (memory window) and **the kernel K(·)** (a function, not a number). Note there is no separate "fractional order" — MDD replaces the order α of a fractional model with a window plus a kernel.

### R4. Admissibility — what can and cannot be said

- **ω_m > 0** required. ω_m = 0 is the classical limit (not singular).
- **The kernel must be positive** for the derivative to be a weighted average of f' with positive weights; a sign-changing kernel can make the coupled heat equation anti-dissipative (the weighted average of θ̇ can have the opposite sign to θ̇).
- **A property MDD does not have:** it is not a derivative in the operator sense — it does not satisfy the product/chain rules, and the "fundamental theorem" fails. This is a *mathematical* price, not a physical one, but it means the usual energy identities cannot be transferred mechanically. A review must not assert an energy balance for an MDD theory without constructing it.
- **Thermodynamic admissibility of MDD is not established in any source I could verify.** Whether an MDD heat law follows from an entropy inequality is, as far as this file can establish, **open**.

### R5. Dispersion consequences (derived generically)

For a harmonic mode e^{−iωt}, the MDD acts as a **complex multiplier**:

    D_{ω_m} e^{−iωt} = (−iω) · Ĝ(ω, ω_m) · e^{−iωt},

where Ĝ is the normalised transform of the kernel over the window. Two exact properties:

1. **Ĝ → 1 as ω_m → 0** (classical derivative recovered) ⇒ the model reduces to Biot, confirmed symbolically in my framework by replacing the multiplier with 1.
2. **Ĝ → 1 as ω → 0** for any normalised kernel (the window is short compared with the period) ⇒ **MDD and Fourier are indistinguishable at low frequency**, for every kernel.

Property 2 is the practically important one: a published MDD solution that differs visibly from the Fourier solution at low frequency indicates a kernel/window that has not been normalised, or a numerical error. Conversely, MDD's observable content lives entirely at ω ω_m ≳ 1.

### R6. Positioning versus fractional models (the honest comparison)

MDD is often presented as "surpassing the fractional derivative" (the paper's own title). What is actually true:

- A fractional (Caputo) derivative has a **power-law kernel and an infinite memory**; MDD has a **finite window and an arbitrary kernel**. They are different model classes, neither containing the other.
- A fractional derivative is **local in the transform** (multiplier (−iω)^α); MDD is also a multiplier for each fixed kernel — so at the level of linear dispersion both are "complex moduli" models, and **neither is more fundamental**. The difference is in the *time domain* and in the admissible parameter space.
- Neither has a verified thermodynamic derivation in this session. The review should say that both are phenomenological and that the choice between them is empirical.

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| Wang & Li 2011, CMA 62(3):1562–1567, DOI | Crossref API | Record only |
| Citation count 448 | Crossref, 2026-10-22 | API |
| Definition of D_{ω_m}, kernels, ω_m → 0 limit | **standard form, NOT source-verified** | — |
| Complex-multiplier property, the two limits, low-frequency indistinguishability | **My derivation** (generic kernel, no form-dependence) | Derivation |

## Checks done

- **Limit check**: replacing the MDD multiplier by 1 returns the Biot determinant exactly — the ω_m → 0 limit is structurally correct.
- **Generality check**: because R5 is derived for an arbitrary normalised kernel, it holds for every kernel used in the literature; it is therefore a *robust* statement (unlike most of the model-specific results in this phase).
- **Consistency with the fractional case**: the MDD multiplier Ĝ(ω,ω_m) is bounded (|Ĝ| ≤ 1 for positive normalised kernels), whereas the Caputo multiplier (−iω)^α is unbounded as ω→∞. This is a **falsifiable structural difference** between MDD and fractional models: MDD cannot produce the high-frequency attenuation growth that fractional models do. Worth one line in the review.

## Confidence

- **HIGH** on R5 and the comparison in R6 (derived, kernel-independent).
- **MEDIUM** on the definition and the "standard substitution" in R2 (standard usage, not source-verified).
- **LOW** on attribution — including whether Wang & Li originated the concept or popularised it, and on the thermodynamics.

## NOT verified / open issues

1. **Wang & Li (2011) not opened.** Their definition, normalisation, and the claim in the title are **UNVERIFIED**. The review must cite the paper itself for the definition.
2. **Which kernel is "the" MDD kernel in thermoelasticity is not settled here.** Papers use at least four. If the manuscript presents a single kernel as canonical, that needs a source.
3. **Thermodynamic admissibility: OPEN.** I found no verified derivation of an MDD heat law from an entropy inequality. The review should state this as an open problem, not assert consistency.
4. **No measured ω_m or kernel** for any material was found or verified.
5. The thermodynamics caveat in R4 (no product/chain rule) is a mathematical fact about the operator but I have **not** verified that any specific published MDD energy identity is therefore wrong — that would require reading those papers.
