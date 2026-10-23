# V-B2f — Green–Naghdi Type III (damped thermal waves)

**Access date 2026-10-22.**

## Task

As V-B2a, for GN Type III. Type III is the "both terms" member of the GN family and is where the literature is most inconsistent, so this file also records the variant problem.

## Method

1. **Provenance.** The type III equations are attributed to the GN sequence 1992/1993 — see V-B2e for the verified bibliographic records of both. **Which paper introduced type III is UNVERIFIED** (open issue 1).
2. Derived the 1-D system from q_i = −(k*α_,i + k_th θ_,i) and the energy balance, then the dispersion relation.
3. Checks in `V-B2_wave_speeds.py`: (i) k*→0 does **not** return Biot (symbolic PASS — type III with k*=0 is still dissipative-hyperbolic, a distinct model); (ii) numeric branches show the correct limits: agreeing with GN-II at low frequency and deviating at high frequency.

## Result

### R1. Heat law

Type III adds ordinary conduction to the type II flux:

    q_i = −( k* α_,i + k_th θ_,i ),    α̇ = θ

With ρc θ̇ + βT₀ ε̇ = −∇·q and (∇·q) evaluated with both terms:

    ρc θ̈ + βT₀ ε̈ = k* ∇²θ + k_th ∇²θ̇

Both a wave term (k*, second order in time) and a diffusive term (k_th, mixed) are present.

### R2. Coupled equations, 1-D

    ρ ü = M u_xx − β θ_x
    ρc θ̈ + βT₀ ü_x = k* θ_xx + k_th θ̇_xx

### R3. Parameters

As V-B2a **plus** k* (see V-B2e). **Two** conductivity-like constants now coexist, with different units — this is the single largest source of unit errors in the GN-III literature.

### R4. Admissibility

- **k* ≥ 0 and k_th ≥ 0**, with **not both zero** (both zero ⇒ no conduction at all).
- **k_th ≥ 0** is what provides dissipation; **k_th < 0** makes the mixed term anti-dissipative and short-wavelength modes grow — the model is then unstable, and this is easy to hit numerically because k_th also appears as "just another coefficient".
- The k* = 0 sub-case is **not** Fourier: it retains the θ̈ term. Only k* = 0 **and** the α-framework dropped gives Biot.
- Finite thermal speed exists whenever k* > 0; the speed is √(k*/(ρc)) at high frequency, with k_th controlling attenuation.

### R5. Characteristic equation and speeds

    (M k² − ρω²)(k* k² + iω k_th k² − ρcω²) + iβ²T₀ ω² k² = 0

(the Θ-entry of the heat row is k* k² + iω k_th k² − ρcω² — note the mixed term is **imaginary**, which is the mathematical statement of "dissipative").

**Numbers** (k* = 4.5×10¹², k_th = 45):

| f | thermal v_ph | comment |
|---|---|---|
| 1 kHz | 1125.9 m/s | identical to GN-II — diffusion term negligible |
| 1 MHz | 1125.9 m/s | still GN-II-like |
| 1 GHz | 1127.5 m/s | the k_th term finally bites (0.14% change) |

Attenuation grows with frequency but far more slowly than Fourier's √ω. **This is the physically attractive feature of type III**: finite speed *and* damping, i.e. the two things LS and GN-II each have only one of.

### R6. The variant/inconsistency problem (important for the review)

GN-III is written in at least three inequivalent ways in the literature:

- (a) k*∇²θ + k_th∇²θ̇  ← used here;
- (b) k*∇²α + k_th∇²θ with α̇ = θ, which after time-differentiation differs from (a) by the placement of the time derivative;
- (c) formulations where k_th multiplies ∇²θ rather than ∇²θ̇, which changes the order of the equation and its stability class.

Because these differ in the **principal part**, they are not interchangeable at high frequency. A review that says "GN-III" without specifying which form is under-specifying the model. This is a defect-table candidate: any manuscript equation for GN-III should be accompanied by its order and its k_th=0 / k*=0 limits.

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| GN 1992 / 1993 bibliographic data (see V-B2e) | Crossref API | Record only |
| "Type III adds dissipative conduction" (qualitative) | Noble (2026) preprint §5.2 — **SECONDARY, unrefereed** | Body (PDF) |
| q = −(k*α_,i + k_thθ_,i) and the R5 determinant | **standard form, NOT source-verified**; determinant derived by me | Derivation |

## Checks done

1. **Symbolic limit check**: k*→0 does not equal the Biot determinant (**PASS**, and the script asserts the *inequality* deliberately — this is the one place where a "limit check" must confirm non-equality).
2. **Numeric continuity between types**: GN-III → GN-II as the k_th term becomes negligible (1125.9 m/s at 1 kHz and 1 MHz, matching GN-II to 5 s.f.). Correct behaviour for a model that is supposed to contain GN-II as a limit.
3. **High-frequency discrimination**: at 1 GHz the branches separate (1127.5 vs 1125.9) and the mixed term's imaginary character produces attenuation. This confirms the term is doing what it should, not merely present.
4. **Order check**: the θ-equation is third order in time (θ̈ plus θ̇_xx) — a different class from GN-II (second order). Any numerical scheme for "GN-III" that is stable for GN-II is not automatically stable here.

## Confidence

- **HIGH** on the mathematics of the stated form: the determinant, the limits, the numerics, and the observation that k*=0 is not Biot.
- **MEDIUM** on the form (a) being the canonical GN-III.
- **LOW** on attribution: which GN paper introduced type III, and whether GN themselves wrote form (a) or (b).

## NOT verified / open issues

1. **Which paper introduced type III: UNVERIFIED.** Candidates are GN 1992 (*J. Thermal Stresses*), GN 1993 (*J. Elasticity*), and later GN papers (1994, 1996). Do not print a date for type III without checking.
2. **Form (a) vs (b) vs (c) is unresolved here.** I could not open any GN paper to settle it. The manuscript must pick a form, state its order, and give both limits; it must **not** claim the choice is immaterial.
3. **Thermodynamic admissibility of GN-III is genuinely contested** in the literature (whether a free energy exists that yields both terms with positive dissipation). I could not verify the status. Treat any claim that GN-III is "thermodynamically consistent" as needing a source.
4. **k* units.** Because k* has units conductivity×time, numerical values in papers are meaningless unless the calibration is stated. I verified no values at all.
5. No dispersion figure from any published GN-III paper was compared with these numbers; the comparison would be a valuable R2-ledger item if Arena produces such figures.
