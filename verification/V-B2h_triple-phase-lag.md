# V-B2h — Triple-phase-lag (TPL) thermoelasticity (Roy Choudhuri)

**Access date 2026-10-22.**

## Task

As V-B2a, for three-phase-lag. ⚠ Largest variant-uncertainty in the set: see §NOT verified 1–2.

## Method

1. **Provenance.** Roy Choudhuri, S.K. (2007) "On a thermoelastic three-phase-lag model", *J. Thermal Stresses* **30**(3):231–238, DOI 10.1080/01495730601130919. Crossref 766, OpenAlex 804. Read level: **record only — full text NOT opened.**
2. No openly readable statement of the TPL equations was found in this session (the 2026 preprint does not treat TPL at all — a notable gap in that review, and one of our differentiators).
3. I therefore derive consequences of the **structure** that TPL must have (three lags: τ_q, τ_T, and a "thermal displacement" lag τ_v), and I flag which part is form-dependent. The third-order polynomial analysis below holds for any TPL written in the standard form.

## Result

### R1. Heat law (standard form, NOT source-verified)

TPL adds a second-order term to the flux side of DPL, motivated by the thermal displacement:

    (1 + τ_q ∂_t + ½τ_v² ∂_t²)(ρc θ̇ + βT₀ ε̇) = k_th(1 + τ_T ∂_t)∇²θ

Three lags: **τ_q** (flux), **τ_T** (gradient), **τ_v** (thermal-displacement / "phase lag of the thermal displacement"). Written out, the operator on the left is now **third order in time**.

### R2. Coupled equations, 1-D

    ρ ü = M u_xx − β θ_x
    (1 + τ_q∂_t + ½τ_v²∂_t²)(ρcθ̇ + βT₀u̇_x) = k_th(1 + τ_T∂_t)θ_xx

### R3. Parameters

As V-B2a, plus τ_q, τ_T, τ_v [s]. **The literature does not agree on the coefficient of τ_v²**: ½τ_v² appears in some papers, τ_v² in others. That factor changes the third-order term's coefficient by 2 — a factor-2 error in a damping/inertia coefficient is exactly the kind of defect the ledger should catch. Flagged as unresolved.

### R4. Admissibility

- **τ_v > 0, τ_q > 0, k_th > 0, c > 0, M > 0, ρ > 0.**
- The added inertia (½τ_v²∂_t²) makes the thermal operator **third order in time**. Third-order-in-time systems need not be stable even with all coefficients positive in the rigid case — unlike the quadratic DPL case, **Routh–Hurwitz for a cubic requires an extra inequality** (a₁a₂ > a₃), not just positivity.
- **Verified numerically** (rigid TPL, τ_v = 10⁻¹⁰, τ_q = 10⁻¹¹, τ_T = 10⁻¹¹ s): stable at k = 1, 10³, 10⁵, 10⁷ m⁻¹, with the two fast roots at ≈ −10⁹ s⁻¹ (i.e. the τ_v scale) and one slow root tracking −κk². So for this parameter set TPL is stable, and the fast modes are *stiff* — they set the explicit time-step limit, not the physics. (This stiffness is the practical reason TPL simulations are awkward, and is worth one sentence in the review.)
- If τ_v → 0, TPL → DPL. If additionally τ_T → 0, TPL → LS. Both nestings are structural.

### R5. Characteristic equation

The Θ-row of the 2×2 system becomes

    k_th k²(1 − iωτ_T) − iωρc(1 − iωτ_q − ½ω²τ_v²)

so

    (Mk² − ρω²)[k_thk²(1−iωτ_T) − iωρc(1−iωτ_q−½ω²τ_v²)] + iβ²T₀ωk²(1−iωτ_q−½ω²τ_v²) = 0

**Numbers:** thermal branch 1125.9 → 1127.5 → 399.4 m/s at 1 kHz → 1 MHz → 1 GHz is *not* the right reading — the script's TPL branches track Biot at 1 GHz because ωτ ≪ 1 there; TPL's third-order character only appears when ωτ_v ~ 1, i.e. ≳ 1.6 GHz for τ_v = 10⁻¹⁰ s. **Practical statement for the review: TPL's extra lag is invisible below ~1/(2πτ_v); with realistic τ_v it cannot be distinguished from DPL at engineering frequencies.** That is a falsifiability problem for TPL identification, not a mathematical one.

### R6. The known controversy (must be sourced before we repeat it)

Several recent papers argue that the TPL model, as originally formulated, is **not thermodynamically admissible** (no Lyapunov function / negative entropy production for some parameter ranges), and alternative "TPL" formulations have been proposed. I did **not** open any of these and cannot confirm the claim. It is, however, the single most important open question about TPL, and a review that lists TPL as just another model without mentioning the admissibility controversy would be behind the literature.

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| Roy Choudhuri 2007, JTS 30(3):231–238, DOI | Crossref API | Record only |
| Nesting TPL ⊃ DPL ⊃ LS ⊃ Biot | **Structural, derived** from the operator (each lag → 0) | Derivation |
| Third-order stability requiring a₁a₂ > a₃ | Standard Routh–Hurwitz; applied by me | Derivation |
| Numeric stability of the rigid TPL at the stated parameters | My computation | Derivation |
| Equations in R1–R2 | **standard form, NOT source-verified** | — |

## Checks done

1. **Nesting (structural)**: setting τ_v = 0 in the TPL operator gives the DPL operator exactly; setting τ_T = 0 as well gives the LS operator exactly. Verified by operator substitution. (The script's symbolic check `TPL(tq=tT=tv=0) == Biot` PASSES, which confirms the endpoint of the chain.)
2. **Order check**: TPL's thermal operator is third order in time, DPL's second, LS's second, Biot's first — a monotone escalation that must be reflected in any numerical scheme.
3. **Stability (numeric)**: cubic Routh–Hurwitz applied to the rigid model at four wavenumbers; stable, with the fast pair at the τ_v scale. I report this as a *specific parameter set*, not a theorem.
4. **Stiffness observation** quantified: the τ_v roots sit at ≈10⁹ s⁻¹ while the physical (diffusive) root sits at 10⁻⁵ to 10⁻¹ s⁻¹ — five to ten orders of magnitude separation. That is a concrete numerical warning.

## Confidence

- **HIGH** on the nesting relations and the order/stiffness statements (structure, not form).
- **MEDIUM** on the equations in R1–R2 being Roy Choudhuri's.
- **LOW** on everything about the admissibility controversy, the ½ factor, and Roy Choudhuri's stated conditions.

## NOT verified / open issues

1. **TPL form: UNVERIFIED.** Two inequivalent published forms exist (τ_v²/2 vs τ_v², and whether the third-order term multiplies the whole heat operator or only the thermal part). **Do not print a TPL equation without the 2007 paper in hand.**
2. **Which physical mechanism τ_v represents is unclear in the sources I could reach.** It is often described as the lag of the thermal displacement gradient. A review should describe it operationally (a third time scale) and say plainly that its microphysical basis is weaker than τ_q's.
3. **Admissibility controversy: UNVERIFIED.** No source opened. If the manuscript takes a position on TPL's thermodynamic status, that position needs a primary citation, not this file.
4. **No experimental value for τ_v** was found or verified.
5. The script's TPL numeric branches at 1 GHz should **not** be read as "TPL ≈ Biot at 1 GHz" without noting that ωτ_v = 0.6 there but the printed phase speeds are dominated by the Biot-like branch. The rigid cubic analysis in R4 is the reliable statement.
