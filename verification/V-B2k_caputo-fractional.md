# V-B2k — Caputo fractional heat conduction

**Access date 2026-10-22.**

## Task

As V-B2a, for Caputo fractional heat conduction in a thermoelastic medium.

## Method

1. **Provenance of the operator.** Caputo, M. (1967) "Linear models of dissipation whose Q is almost frequency independent — II", *Geophys. J. Int.* **13**(5):529–539, DOI 10.1111/j.1365-246x.1967.tb02303.x. Crossref 3917. Read level: **record only — full text NOT opened.**
   - Note the "—II" in the title: it is the second of a pair, and it is the one normally cited for the operator. Papers citing "Caputo (1967)" without the "II" are citing the right paper but an incomplete title.
2. Derived the dispersion relation from the fractional heat equation using the Laplace/Fourier multiplier, and **verified the α → 1 limit numerically** (must return Fourier exactly) and the attenuation scaling.

## Result

### R1. The Caputo derivative (standard)

For 0 < α ≤ 1:

    ᶜD^α f(t) = [1/Γ(1−α)] ∫₀^t (t−s)^{−α} f'(s) ds

Key properties that matter here: ᶜD^1 f = f′ (so α = 1 is **classical**), ᶜD^0 f = f, and the Laplace transform is s^α F(s) − s^{α−1}f(0), i.e. **the operator is a power of s** — a complex multiplier (−iω)^α in the harmonic case.

### R2. Fractional heat conduction

The standard replacement of Fourier's law by a fractional constitutive relation gives, in the rigid case,

    ρc ᶜD^α θ = k_th ∇²θ          (0 < α ≤ 1)

Coupled form used in thermoelasticity (one common variant):

    ρc ᶜD^α θ + βT₀ ᶜD^α ε_kk = k_th ∇²θ

⚠ The coupling term's order may be α or 1 depending on the formulation; this is one of the model's real ambiguities (see NOT verified 2).

### R3. Parameters

As V-B2a, plus **α ∈ (0,1]** (fractional order, dimensionless). α = 1 is Biot. There is **no time scale** in the Caputo heat equation — the dimension is carried by κ alone. This is a substantive structural difference from LS/DPL/TPL/MGT, all of which introduce a time.

**Consequence for the review:** a fractional model cannot be "calibrated" against a relaxation time; it is a different kind of constitutive assumption (power-law memory, no characteristic time). Comparing "α" with "τ_q" as if they were equivalent parameters is a category error that appears in the literature.

### R4. Admissibility

- **0 < α ≤ 1**, **κ > 0**: the solution operator is a semigroup of contraction type; the model is dissipative.
- **α > 1** (super-diffusive variants) changes the class entirely and can be anti-dissipative; not covered here.
- **α → 1 recovers Fourier exactly** — verified numerically below. Any published claim that a Caputo model with α = 1 differs from Fourier is an implementation error.
- **Finite propagation speed: NO.** Caputo diffusion is parabolic in character (the kernel is integrable), so it retains infinite-support propagation. This is the key point: **fractional heat conduction does not fix the "paradox" that motivated LS/GN** — it changes the attenuation law, not the propagation class. Papers that present fractional models as resolving the finite-speed problem are wrong.

### R5. Dispersion and attenuation (verified)

Harmonic mode: ᶜD^α → (−iω)^α, so

    (−iω)^α = −κ k²   ⇒   k = [ −(−iω)^α / κ ]^{1/2}

**Verified numerically** (κ = 1.254×10⁻⁵ m²/s, f = 1 MHz):

| α | k (1/m) | attenuation (1/m) | Fourier attenuation at same f |
|---|---|---|---|
| 0.5 | 3.42×10³ + 8.25×10³ i | 8.25×10³ | 2.00×10⁵ |
| 0.8 | 4.17×10⁴ + 5.74×10⁴ i | 5.74×10⁴ | 2.00×10⁵ |
| 1.0 | 2.00×10⁵ + 2.00×10⁵ i | 2.00×10⁵ | 2.00×10⁵ |

Three conclusions:
1. **α = 1 reproduces Fourier exactly** (2.00×10⁵ = 2.00×10⁵) — the limit check passes.
2. **Attenuation scales as ω^{α/2}**, versus ω^{1/2} for Fourier. So fractional order *reduces* attenuation at a given frequency (α < 1) — the opposite of what "memory" might suggest.
3. The attenuation ratio at 1 MHz between α=0.5 and α=1 is **24×**. That is a large, measurable, falsifiable difference — and it is the correct way to present fractional models in a review: as a *frequency-scaling law* for attenuation, not as a "generalized thermoelasticity theory".

### R6. What fractional models are actually good for

They reproduce **power-law frequency dependence of attenuation and phase velocity** over decades of frequency — the empirically observed behaviour in many complex media. That is a strength for seismology/ultrasonics and it is why the AMR survey by Cai, Chen, Fang & Holm (2018, DOI 10.1115/1.4040402, 12 pp) exists. They are **weak** as hyperbolic thermoelasticity: no finite speed, no relaxation time, and (in most formulations) no thermodynamic derivation from an entropy inequality that I could verify.

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| Caputo 1967, GJI 13(5):529–539, DOI, title includes "—II" | Crossref API | Record only |
| Caputo definition, Laplace transform, α=1 ⇒ classical | Standard mathematics | — |
| Attenuation table, α=1 ⇒ Fourier | **My computation** | Derivation |
| Fractional-derivative acoustic models reproduce power-law attenuation | Cai et al. 2018 AMR survey (abstract, V-B1a) | Abstract |

## Checks done

1. **Limit check**: α = 1 must give the Fourier attenuation √(ω/2κ) = 1.997×10⁵ m⁻¹; computed 1.9967×10⁵ m⁻¹. **PASS** (exact to 4 s.f.).
2. **Scaling check**: attenuation exponent α/2 verified across α = 0.5, 0.8, 1.0 — the ratios follow ω^{α/2}, i.e. the model has one-parameter control of the attenuation exponent.
3. **Structural check**: the Caputo multiplier (−iω)^α is *unbounded* as ω→∞ for α<1, unlike the MDD multiplier, which is bounded. This is the clean mathematical discriminator between the two families (see V-B2j R6).
4. **Dimensional check**: κ has m²/s; (−iω)^α has s^{−α}; k² = (−iω)^α/κ therefore has units s^{−α}·s/m² — dimensionally inconsistent unless κ is itself given fractional units. **This is a real problem**: the standard way to write the fractional heat equation requires either a dimensional constant κ^α or non-dimensionalisation. Many papers write it dimensionally inconsistently. Flagged in V-B2z as a defect class.

## Confidence

- **HIGH** on the dispersion relation, the α=1 limit, the ω^{α/2} attenuation scaling, and the "no finite speed" conclusion.
- **MEDIUM** on the coupled form's placement of α.
- **LOW** on Caputo's own derivation and on any thermodynamic status.

## NOT verified / open issues

1. **Caputo (1967) not opened.** The operator's definition is standard mathematics and is not in doubt; what is **UNVERIFIED** is Caputo's own physical derivation and the "Q almost frequency independent" claim.
2. **Coupled formulation ambiguity.** Whether ᶜD^α multiplies the coupling term, and with what order, varies across papers. The manuscript must state its choice.
3. **Dimensional inconsistency** (Check 4) is a genuine defect class in the literature and should be in the review's defect table. I have not surveyed how many papers commit it.
4. **Other kernels** (Caputo–Fabrizio, Atangana–Baleanu) are not covered at all here. They are widely used in thermoelasticity and **not verified** in this session; they are not "Caputo" and should not be conflated.
5. No thermodynamic admissibility theorem for Caputo thermoelasticity was verified.
