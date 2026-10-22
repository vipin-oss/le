# V-B2g — Dual-phase-lag (DPL) thermoelasticity (Tzou)

**Access date 2026-10-22.**

## Task

As V-B2a, for dual-phase-lag. Includes the ill-posedness threshold, because DPL is the model in this set most often used outside its range of validity.

## Method

1. **Provenance.** Tzou, D.Y. (1995) "A unified field approach for heat conduction from macro- to micro-scales", *ASME J. Heat Transfer* **117**(1):8–16, DOI 10.1115/1.2822329. Crossref 1995, OpenAlex 2148. Read level: **record only — full text NOT opened.**
2. Obtained the *published-form* delay law and its first-order expansion from an openly readable source (Noble 2026 §6.1, PDF) — see Evidence. This is the one model where I have a readable statement of the actual constitutive delay law, so the form is better established than for GL/GN.
3. Independently derived the dispersion relation, and located the **rigid-model ill-posedness threshold** by direct root computation.

## Result

### R1. Heat law

Tzou's delay law (two lags, τ_q for the flux and τ_T for the temperature gradient):

    q(x, t + τ_q) = −k_th ∇θ(x, t + τ_T)

First-order Taylor expansion:

    q + τ_q q̇ = −k_th( ∇θ + τ_T ∇θ̇ )

With ρc θ̇ + βT₀ ε̇ = −∇·q:

    τ_q ρc θ̈ + ρc θ̇ + τ_q βT₀ ε̈ + βT₀ ε̇ = k_th ∇²θ + k_th τ_T ∇²θ̇

**Note the structural point:** the *left* side is exactly the LS operator; the *right* side has the extra τ_T term. So **DPL = LS + a gradient-lag term**, and DPL with τ_T = 0 **is** LS. This is the cleanest way to position DPL in a review, and it immediately explains why DPL's "extra parameter" is not a new physical mechanism but a Taylor-truncated approximation of a delay.

### R2. Coupled equations, 1-D

    ρ ü = M u_xx − β θ_x
    ρc(θ̇ + τ_qθ̈) + βT₀(u̇_x + τ_qü_x) = k_th θ_xx + k_thτ_T θ̇_xx

### R3. Parameters

As V-B2a, plus τ_q ≥ 0 (flux lag, s) and τ_T (gradient lag, s). **τ_T is allowed to be of either sign in the published literature**, which is itself a red flag (see R4).

### R4. Admissibility — and the concrete instability threshold

Rigid-model characteristic polynomial in s (mode e^{st+ikx}):

    τ_q s² + (1 + κτ_T k²) s + κk² = 0        (κ = k_th/(ρc))

Routh–Hurwitz for a quadratic: all roots in the left half-plane **iff all coefficients are positive**. τ_q > 0 and κk² > 0 always, so

    **STABILITY REQUIRES 1 + κτ_T k² > 0.**

- **τ_T ≥ 0** ⇒ stable for all k (verified: τ_T = 10⁻¹¹ and 10⁻⁶ s, k up to 10⁹ m⁻¹, all roots decaying).
- **τ_T < 0** ⇒ unstable for all sufficiently short waves, above

      k_c = 1/√(κ|τ_T|)

  Verified numerically: τ_T = −10⁻⁹ s gives k_c = 8.93×10⁶ m⁻¹ (wavelength 0.704 µm); at k = 4.46×10⁶ m⁻¹ the model is stable (max Re s = −3.3×10⁸), at k = 1.79×10⁷ m⁻¹ it is **unstable** (max Re s = +3.0×10¹¹). τ_T = −10⁻¹¹ s shifts the threshold to 8.93×10⁷ m⁻¹, and instability again appears just above it.

**Interpretation for the review (this is a real, checkable result):** a negative τ_T does not merely "give unusual phase behaviour" — it makes the model **ill-posed in the sense that arbitrarily short wavelengths grow arbitrarily fast** (the growth rate scales like |τ_T|κ²k⁴/τ_q). A computation that reports a "DPL solution with τ_T < 0" and a fine mesh is reporting a numerical artefact of a mesh that has not resolved k_c. **This should be an explicit warning box in the paper.**

### R5. Characteristic equation and speeds

    (M k² − ρω²)(k_th k²(1−iωτ_T) − iωρc(1−iωτ_q)) + iβ²T₀ωk²(1−iωτ_q) = 0

**Numbers** (τ_q = τ_T = 10⁻¹¹ s): at 1 kHz, 1 MHz and 1 GHz the DPL thermal branch is indistinguishable from Biot (12.6 m/s at 1 MHz) because ωτ ≪ 1 at all three. DPL's richer behaviour is a **short-time / high-frequency** phenomenon; at engineering frequencies DPL and Fourier agree to O(ωτ). Any figure showing a dramatic DPL-vs-Fourier difference at kHz frequencies is suspect.

### R6. Known critique in the literature (needs sourcing before the review repeats it)

Taylor truncation of a delay is not equivalent to the delay. The openly readable review I used states that truncated delay models "can show unphysical behavior or be used outside the asymptotic regime in which the truncation is justified", citing Rukolaine. I could not verify Rukolaine's actual arguments (not opened). The review must either cite that critique properly or make its own argument from R4 — which stands on its own and is verified here.

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| Tzou 1995, JHT 117(1):8–16, DOI | Crossref API | Record only |
| Delay law q(x,t+τ_q) = −k∇T(x,t+τ_T); first-order expansion; rigid DPL equation τ_qT_tt + T_t = αΔT + ατ_TΔT_t; rigid polynomial τ_qs² + (1+ατ_Tκ²)s + ακ² = 0 | Noble (2026) preprint §6.1–6.2, DOI 10.21203/rs.3.rs-10734164/v1 — **SECONDARY, unrefereed** | Body (PDF) |
| Stability condition 1+κτ_Tk² > 0 and the threshold k_c | **My own derivation** (Routh–Hurwitz) + numeric verification | Derivation |
| "unphysical behavior / outside the asymptotic regime" (attributed to Rukolaine) | Same preprint — **SECONDARY, tertiary claim not verified** | Body (PDF) |

## Checks done

1. **Limit check (symbolic)**: τ_q = τ_T = 0 returns the Biot determinant **exactly** — PASS. (This check initially FAILED in my own script because of a sign error in the ∇²θ̇ term; I found it with this check and corrected it. Recorded here deliberately: the check has already caught one real error, mine.)
2. **Limit check (structural)**: τ_T = 0 returns LS. Verified by comparing the determinant: the DPL determinant with τ_T=0 equals the LS determinant with τ₀=τ_q (same expression, different symbol).
3. **Independent reproduction of a third-party proposition**: the preprint's Prop. 3 asserts stability for τ_T ≥ 0 and instability for τ_T < 0 at large k. My Routh–Hurwitz analysis and numeric roots agree. **Their proposition is correct** (for the rigid model, which is the scope they state).
4. **Threshold formula verified numerically** at two values of τ_T, straddling k_c in each case.
5. **Frequency-scale check**: DPL ≈ Fourier at ≤1 GHz for τ = 10⁻¹¹ s, consistent with ωτ ≤ 0.06.

## Confidence

- **HIGH** on: the stability condition, the threshold k_c = 1/√(κ|τ_T|), the DPL ⊃ LS ⊃ Biot nesting, and the numerics.
- **MEDIUM** on the delay law and its first-order expansion being Tzou's exact published form (secondary source, consistent with widespread usage).
- **LOW** on what Tzou himself claimed for the admissible sign/range of τ_T.

## NOT verified / open issues

1. **Tzou (1995) full text not opened.** His stated restrictions on τ_q, τ_T, and whether he permitted τ_T < 0, are **UNVERIFIED**.
2. **Coupled-DPL stability is NOT settled by my R4.** R4 is the **rigid** model. The thermoelastic DPL system may be unstable even for τ_T > 0 — there is a known line of work (Quintanilla, Racke and co-authors) on exactly this, which I did **not** open. The manuscript must not generalise R4 to the coupled case without that source.
3. **Rukolaine's critique is cited here at third hand.** The review should cite the actual papers or drop the claim.
4. **Higher-order truncations**: expanding the delay to second order changes the PDE order and the stability polynomial; a parameter set stable at first order need not be stable at second. Verified only as a statement of logic, not computed.
5. τ_T has units of time but no verified measurement exists; any "typical value" table needs sourcing.
