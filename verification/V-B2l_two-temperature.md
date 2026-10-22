# V-B2l — Two-temperature thermoelasticity (Chen–Gurtin; Youssef)

**Access date 2026-10-22.**

## Task

As V-B2a, for two-temperature (2T) thermoelasticity.

## Method

1. **Provenance.**
   - Chen, P.J. & Gurtin, M.E. (1968) "On a theory of heat conduction involving two temperatures", *Z. Angew. Math. Phys. (ZAMP)* **19**(4):614–627, DOI 10.1007/BF01594969. Crossref 727, OpenAlex 852. Read level: **record only.**
   - Youssef, H.M. (2006) "Theory of two-temperature-generalized thermoelasticity", *IMA J. Appl. Math.* **71**(3):383–390, DOI 10.1093/imamat/hxh101. Crossref 431. Read level: **record only.**
   - Boley, B.A. & Tolins, I.S. (1962), *J. Appl. Mech.* **29**:637 — sometimes credited with the idea that the conductive temperature can differ from the thermodynamic one at short times. **NOT verified in this session** (no Crossref lookup performed).
2. Derived the dispersion consequences of the 2T relation, which is a **static (spatial) constraint** rather than a rate law — the key structural point.

## Result

### R1. The two-temperature structure

Chen–Gurtin introduce a **conductive temperature φ** distinct from the thermodynamic temperature T, related by a **spatial** (not temporal) equation:

    T = φ − a ∇²φ ,      a ≥ 0

and postulate Fourier's law in the conductive temperature:

    q = −k_th ∇φ

The energy equation becomes

    ρc Ṫ + βT₀ ε̇ = k_th ∇²φ

Substituting T = φ − a∇²φ:

    ρc(φ̇ − a∇²φ̇) + βT₀ ε̇ = k_th ∇²φ

**Structural point for the review:** 2T theory is **orthogonal** to the relaxation theories. It adds a *length*-like parameter a (units m²) and no time scale. LS/DPL/TPL/MGT add time scales and no length. That is why 2T is routinely combined with each of them (e.g. "2T-LS", "2T-GN-III") — and why a review should present it as a **modifier of the temperature field**, not as a competing model. Youssef (2006) did exactly this: 2T combined with LS.

### R2. Coupled equations, 1-D (Chen–Gurtin, classical conduction)

    ρ ü = M u_xx − β θ_x
    ρc(θ̇ − a θ̇_xx) + βT₀ u̇_x = k_th θ_xx

(with θ ≡ φ; the thermodynamic temperature is recovered as T = θ − aθ_xx.)

### R3. Parameters

As V-B2a, plus **a ≥ 0** (two-temperature parameter, m²). Often written as a = (mean free path)²/6 or with a named length ℓ, a = ℓ². **a = 0 ⇒ T ≡ φ ⇒ classical theory.**

Addition for Youssef-type 2T-LS: τ₀ as in V-B2b as well.

### R4. Admissibility

- **a ≥ 0** required. If a < 0 the relation T = φ − a∇²φ inverts the smoothing: T acquires *shorter*-wavelength content than φ, and the map between the two temperatures becomes unbounded at high wavenumber — the model is ill-posed. (This is the direct analogue of the DPL sign threshold in V-B2g: the unstable direction is short-wavelength, and the fix is the sign of a single parameter.)
- **k_th > 0, c > 0, M > 0, ρ > 0** as before.
- **Finite propagation speed: unchanged by 2T alone.** Adding a does **not** make the theory hyperbolic. Any claim that "two-temperature theory removes the infinite-speed paradox" is wrong unless the underlying conduction law is also hyperbolic (LS/GN/DPL). Worth an explicit sentence.
- **Thermodynamic status:** the Chen–Gurtin 2T theory is usually presented as a *constitutive hypothesis* about which temperature drives conduction, not as a consequence of an entropy inequality. I could not verify that it follows from one.

### R5. Dispersion (1-D, rigid, classical conduction)

In Fourier space the 2T relation is algebraic:

    T̂ = (1 + a k²) φ̂

so the heat equation becomes

    −iωρc(1 + a k²)φ̂ = −k_th k² φ̂   ⇒   k_th k² = iωρc(1 + a k²)

    ⇒   k² = iωρc / (k_th − iωρc a)  =  iω/(κ(1 − iω a/κ)) ... (rearranged)

**Consequences:**
- **k → 0**: k² ≈ iω/κ — classical diffusion recovered regardless of a.
- **k large / ω large**: the factor (1 + a k²) grows, so for fixed ω the admissible k is **smaller** than in Fourier: 2T theory *cuts off* short-wavelength thermal content. That is its purpose — it regularises the high-wavenumber behaviour without introducing a time scale.
- **Wave speed:** v_ph = ω/Re k still → √(2κω)-like growth; no asymptote. **2T does not create a thermal wave.**

### R6. Where 2T is genuinely useful, and the honest caveat

The 2T construction is best motivated where a *microstructural* temperature (phonon/electron populations, or a phase-mixture temperature) differs from a bulk-measured one — e.g. ultrafast laser heating of metals (electron vs lattice temperature), and porous/granular media. In those settings the two temperatures are physical, and a has a microscopic interpretation.

**Caveat for the review:** in most thermoelasticity papers a is a fitted parameter with no independent measurement, and the theory is used purely to smooth numerical results. The review should separate "2T as a physical two-population model" (defensible) from "2T as a regularisation knob" (which is what most of the applied literature does). This distinction is not, as far as I could verify, made anywhere in the existing review literature.

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| Chen & Gurtin 1968, ZAMP 19(4):614–627, DOI | Crossref API | Record only |
| Youssef 2006, IMA J. Appl. Math. 71(3):383–390, DOI | Crossref API | Record only |
| T = φ − a∇²φ, q = −k∇φ | **standard form, NOT source-verified** | — |
| 2T does not create a thermal wave; short-wavelength cutoff | **My derivation** | Derivation |

## Checks done

- **Limit check**: a = 0 returns the classical heat equation and hence the Biot determinant — structurally verified.
- **High-wavenumber check**: (1+ak²) → ∞ as k → ∞ means the effective diffusivity κ/(1+ak²) → 0; the model is a **low-pass filter** on thermal content with cutoff k ~ 1/√a. This is a clean, checkable characterisation, and it shows the model cannot produce a wave.
- **Orthogonality check** (logical, not numerical): a enters the equation multiplied by ∇²φ̇ (a *mixed* term), whereas τ₀ enters multiplied by φ̈ (a *temporal* term). Hence 2T and LS are independent modifiers and compose — which is exactly what Youssef (2006) does. Verified by inspection of the composed operator.
- **Ill-posedness of a < 0**: argued from the unboundedness of (1+ak²) for a<0; **not** verified by a numerical root computation (unlike the DPL case, where I did compute it). Marked MEDIUM.

## Confidence

- **HIGH** that 2T adds a length scale and not a time scale, and that it does not by itself produce finite thermal propagation.
- **MEDIUM** on R1–R2 being Chen–Gurtin's exact formulation (the relation T = φ − a∇²φ is universal in the literature, but I did not read the paper).
- **LOW** on the Boley–Tolins attribution and on the thermodynamic status.

## NOT verified / open issues

1. **Both primary papers not opened.** The exact form of Chen–Gurtin's energy equation, and Youssef's 2T-LS equations, are **UNVERIFIED**. In particular I did not verify whether Youssef couples the *thermodynamic* or the *conductive* temperature to the strain.
2. **Attribution of the two-temperature idea is contested.** Chen–Gurtin (1968) is the paper; Boley–Tolins (1962) and even earlier work are sometimes credited for the physical idea. **Neither alternative was verified here.** A review must not assert primacy without checking.
3. **a < 0 ill-posedness is argued, not computed.** Should be computed before it is stated as a theorem.
4. **No measured values of a** for any material were verified.
5. Whether the Chen–Gurtin theory is thermodynamically admissible (as opposed to mathematically well posed) is **OPEN** in this file.
