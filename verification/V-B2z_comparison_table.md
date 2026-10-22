# V-B2z — Comparison table of canonical models, and catalogue of repeated mistakes

**Access date 2026-10-22.** Companion to V-B2a … V-B2m and to `V-B2_wave_speeds.py`.

## Task

One table with columns: model | heat law | finite wave speed? | dissipative? | energy-conserving? | key parameter(s) | known pitfalls/misuses. Plus a flagged list of commonly repeated mistakes.

## Method

Everything in the table is a **derived** or **computed** statement, except where the cell is marked with a source label. The "finite speed", "dissipative" and "energy-conserving" columns were decided from the **principal part** of each heat operator (which fixes propagation class) and from the presence/absence of a dissipative (odd-in-temperature) term — not by taking any author's word for it.

Sources for the heat-law forms: mostly standard published forms; where I could obtain an openly readable statement of the actual law it is noted in the individual files. **No primary full text was opened** (see `README.md`). Read-level per model is in each V-B2x file.

## Result

### R1. The table

| Model | Heat law | Finite wave speed? | Dissipative? | Energy-conserving? | Key parameter(s) | Known pitfalls / misuses | Primary source opened? | Printable as-is? |
|---|---|---|---|---|---|---|---|---|
| **Biot / Fourier** (Biot 1956) | q = −k_th∇θ; ρcθ̇ + βT₀ε̇ = k_th∇²θ | **No** (parabolic) | **Yes** | No | δ = T₀β²/(ρcM); κ | v_ph = √(2κω) → ∞; often blamed for a "paradox" that is simply its domain of validity | no | **yes** |
| **Lord–Shulman** (1967) | τ₀q̇ + q = −k_th∇θ | **Yes**, c_h = √(κ/τ₀) | **Yes** | No | τ₀ | τ₀ placement varies; τ₀ rarely measured; terms often mis-scaled (LS≈Fourier below 1/2πτ₀) | no | conditional — τ₀ placement must be stated |
| **Green–Lindsay** (1972) | Fourier for q; relaxation on **temperature-rate** terms | **Yes**, c_h = √(κ/τ₀) — **closed form, verified** (V-B2c §R7.3); supersedes "not verified" | **Yes** | No | τ₀ (on θ̈), τ₁ (on θ̇ in stress); ordering **τ₁ ≥ τ₀ > 0** — sourced 2026-10-22 in `V-B2c` §R8 (S1 `α≥α₀`, S2 `0<τ₀<τ₁`); **no flux relaxation** (GL keeps Fourier, unlike LS) | **No flux relaxation** (it does not); **my earlier (τ₁,τ₂) labelling is a notation defect, not a relabelling of (τ₀,τ₁)**; GL ≡ LS when the two times coincide; with pure Fourier q it is a telegrapher equation, unlike DPL-T1 | no | **no** — form and ordering unsourced |
| **GN Type I** | = Fourier | **No** | Yes | No | (none new) | **GN-I IS the classical Biot theory — not a separate ninth model** | no | **yes** (as an identity) |
| **GN Type II** (1992/93) | q = −k*∇α, α̇ = θ; ρcθ̈ + βT₀ε̈ = k*∇²θ | **Yes**, exactly; **non-dispersive** | **No** | **Yes** | k* [conductivity×time] | "No dissipation" is a strong physical claim; k* values incomparable across papers (units!) | no | conditional — state k* units |
| **GN Type III** | q = −(k*∇α + k_th∇θ) | Yes (asymptote) | **Yes** (via k_th) | No | k*, k_th | ≥3 inequivalent published forms differing in the **principal part**; k*=0 is **not** Biot | no | conditional — state which variant |
| **DPL** (Tzou 1995) | q(t+τ_q) = −k_th∇θ(t+τ_T) | **Truncation-dependent — see V-B2p.** T2 (2nd order τ_q, 1st τ_T): **YES**, c∞ = √(2κτ_T)/τ_q; T1 (1st order both): **NO** (v∝√ω, overdamped); T4 (2nd order both): **NO** (band-limited, ω≤1/τ_T, v_ph→0) | Yes (τ_T ≥ 0) | No | τ_q, τ_T | **Stability (T2): τ_T > τ_q/2 — the direction τ_q > τ_T/2 is WRONG** (Q&R 2006; re-derived via Routh–Hurwitz; k_c = [κ(τ_q/2−τ_T)]^{−1/2}); **τ_T < 0 ⇒ ill-posed**; truncations with (time order) − (Δ-order) ≥ 3 are ill-posed (DQR 2009 Thm 1.3); **the delay equation itself is ill-posed, so a stable truncation is not an approximation of it** | no (for DPL itself; DQR 2009 — a *third-party* analysis — was read in full) | conditional — **must name the truncation (T1/T2/T3/T4) in every sentence** |
| **TPL** (Roy Choudhuri 2007) | as DPL + ½τ_v²∂_t² on the thermal operator | **NOT established** (3rd order in time) | Yes | No | τ_q, τ_T, τ_v | ½τ_v² vs τ_v² factor varies; admissibility contested; stiff fast modes (~1/τ_v) dominate numerics; invisible below 1/2πτ_v; DQR's τ₁>τ₂>τ₃ ordering applies to the delay form | no | **no** |
| **MGT** (Quintanilla 2019) | τT_ttt + T_tt = b∇²T_t + c²∇²T | **Yes**: √(b/τ) at high ω, √(c²) at low ω | **Yes** | No (has decay functional for γ>0) | τ, b, c², **γ = b − τc²** | **γ > 0 is required and is often not reported**; positivity of τ,b,c² is NOT sufficient; frequently mis-dated as 2018 | no | conditional — γ>0 must be stated |
| **MDD** (Wang & Li 2011) | ρc D_ω θ + βT₀ D_ω ε = k_th∇²θ | **No** | Kernel-dependent | No | ω_m **and** kernel K | Model undefined without the kernel; not a derivative (no product/chain rule); thermodynamics unestablished; indistinguishable from Fourier at low ω | no | conditional — kernel must be stated |
| **Caputo fractional** (1967) | ᶜD^αθ = κ∇²θ, 0<α≤1 | **No** | **Yes** | No | α | **Does not fix the finite-speed problem** (parabolic class); attenuation ∝ ω^{α/2}; dimensionally inconsistent unless κ carries fractional units; α=1 must equal Fourier exactly | no | **yes** |
| **Two-temperature** (Chen–Gurtin 1968) | q = −k_th∇φ; T = φ − a∇²φ | **No** (adds length, not time) | Yes | No | a [m²] | Orthogonal to all relaxation theories (composes with them); short-wavelength low-pass filter; does **not** create a thermal wave; a<0 ill-posed (argued, not computed) | no | **yes** |
| **Eringen nonlocal** (1972/1983) | (elastic, not thermal) σ − (e₀a)²∇²σ = C:ε | **Yes** (frequency cutoff ω_max = c/ℓ) | No | **Yes** | ℓ = e₀a | **Softens**: v_ph → 0; differential form is not exactly the integral model; "e₀" calibration is problem-specific | no | **yes** |
| **Mindlin gradient** (1962/1964) | (elastic) strain-gradient free energy | **No** — v_ph → ∞ (worse than classical) | No | **Yes** | ℓ (general theory: 5 constants) | **Stiffens**: v_ph → ∞; at identical ℓ and k it differs from nonlocal by a factor **10⁶**; single-ℓ reduction is a modelling choice | no | **yes** |
| **Piezothermoelastic** (Mindlin 1961; Nowacki; Chandrasekharaiah 1984/1988) | q = −k∇θ (classical) or LS/GL form; **+ D_i = ε_ijE_j + e_ijk e_jk + p_iθ**, ∇·D = 0, E = −∇φ (quasi-static) | **Inherited from the heat law** — piezo adds no propagating branch; "quasi-static electric mode" is a **constraint, not a mode** | Inherited | No | e (piezo), ε, p (pyro), β | **"Isotropic piezoelectric" is impossible** (needs 6mm); pyroelectric term must appear in **both** D_i and the heat equation; c_E vs c_D differ by ~10 % (electric BC!); indexing of e_kij varies | no | **no** — equations unattributed |
| **Guyer–Krumhansl** (1966) | q + τq̇ = −k∇θ + ℓ²(Δq + 2∇∇·q) ⇒ τθ̈ + θ̇ = κθ_xx + 3ℓ²θ̇_xx (1-D) | **No for ℓ>0** (short waves overdamped; "second sound" is a **band-limited** k∈(k₁,k₂) resonance); **ℓ=0 ⇒ Cattaneo, √(κ/τ)** | Yes | No | τ, ℓ (with a **factor-3 convention**) | **factor 3 from the 1-D reduction is absorbed differently across papers**; nonlocal length ≠ nonlocal-elasticity length; not a higher-order *time* truncation, so DQR's theorem does not apply | no | **no** — coefficient structure unverified |

### R1b. The two revision-R5 columns: what they mean

- **"Primary source opened?"** — has a *primary* full text (the paper that introduced the model)
  been read in this verification set? **The answer is "no" for every row, including the two new
  ones.** The single primary full text opened anywhere in this set is Dreher, Quintanilla & Racke
  (2009) — and that is a **third-party analysis of DPL**, not the source of DPL. A table whose
  column reads "no" everywhere is not a defect; it is the honest state of the evidence and it tells
  the handler exactly what to obtain before submission. Do not upgrade a cell to "yes" on the basis
  of having read a review that quotes the paper.
- **"Printable as-is?"** — may the statements in that row be printed *as they stand*, with the
  source labels attached? `yes` = derived here and source-independent (identities, symmetry
  statements, closed forms checked two ways); `conditional` = printable only with a specified
  qualifier (truncation, variant, kernel, units, sign convention); `no` = the row contains a defect
  or an unattributed form that must be resolved first. **Five rows are `no`: GL, TPL,
  piezothermoelasticity, Guyer–Krumhansl and — in the sense that its *stability* statement was
  wrong before this revision — DPL is `conditional` but its previously printed cell was wrong.**
- **The two cross-cutting files are not models.** `V-B2p` (DPL truncation order) and `V-B2q`
  (micropolar/porous/semiconductor) do not add rows of their own: `V-B2p` is a *disambiguation* of
  the DPL row (which truncation?), and `V-B2q` covers three families whose defining feature is that
  they are **not** heat-conduction generalisations at all (they add kinematics/transport, and
  inherit whatever thermal speed the chosen heat law gives them). Listing them as further items in
  a Fourier→LS→GL→GN→… progression would be a category error; see `V-B2q` §3.4.

### R2. The three grouping facts a review should state on one page

1. **Propagation class is a property of the principal part, not of the "generality" of the theory.** Biot, Caputo, MDD and 2T are all non-finite-speed; LS, GL, GN-II/III, MGT are finite-speed; DPL depends on the Taylor truncation (finite for T2 only — `V-B2p`); TPL remains unestablished. "Generalized" does not imply "hyperbolic".
2. **Dissipation and finite speed are independent axes.** GN-II has finite speed and *no* dissipation; Biot and Caputo have dissipation and *no* finite speed; MGT and GN-III have both; DPL-T1 has dissipation and *no* finite speed while DPL-T2, on the same constitutive law truncated differently, has both.
   **A corollary that only became visible in revision R1/R2:** propagation class is a property of the *truncation/principal part*, so two papers using "the same" DPL or GL equations can disagree about finite speed without either being wrong — which is exactly the trap the review should warn about. A table with a single "generality" ordering is meaningless.
3. **Only GN-II (and the purely elastic nonlocal/gradient models) conserve energy.** Every thermoelastic conduction model except GN-II is dissipative. This is the classification Phase B3 needs, and it is why "energy flux" at an interface has to be treated separately for GN-II.

### R3. Catalogue of commonly repeated mistakes

Ordered by how often I met them and how damaging they are.

**M1. GN Type I counted as a distinct theory.** GN-I ≡ Biot/Fourier (V-B2d). A nine-model list containing both is a single-theory inflation. *Confidence: HIGH.*

**M2. Green–Lindsay described as having a heat-flux relaxation.** It does not: q remains Fourier; the relaxation sits on the temperature-rate terms (V-B2c). Papers that write GL with a τ on q have written LS. *Confidence: HIGH that this is the standard reading; MEDIUM that it matches GL's 1972 text (not opened).*

**M3. MGT thermoelasticity dated 2018.** Quintanilla's paper is *Math. Mech. Solids* **24**(12):4020–4031, `issued` 2019-07-21 (both indices agree). *Confidence: HIGH.*

**M4. DPL used with τ_T < 0 and reported as a solution.** For τ_T < 0 the rigid model is unstable above k_c = 1/√(κ|τ_T|) (verified numerically for two values of τ_T, straddling each threshold). Growth rates reach ~10¹¹ s⁻¹. Any such "solution" is a mesh artefact. *Confidence: HIGH (rigid model); the coupled case is not settled here.*

**M5. "DPL/TPL have finite propagation speed" asserted without proof.** Established for the τ_T = 0 sub-case (= LS) only. For τ_T ≠ 0 the operator is higher order and finite propagation needs a real theorem. Marked **NOT established** rather than "yes". *Confidence: MEDIUM — this is a gap in the literature as much as a mistake.*

**M6. TPL with ½τ_v² in one paper and τ_v² in another.** Factor 2 on the highest-order term; not cosmetic. *Confidence: HIGH that both forms exist; the canonical one is UNVERIFIED.*
> **CORRECTION 2026-10-22 (`V-B8a` §3.2): WITHDRAWN to UNVERIFIED.** The premise is wrong: Roy Choudhuri's TPL law (2007, eq 3) has **no τ_v² term**; it is first order in all three lags with an explicit `k*∇v` piece. The two "forms" I compared were not recorded and I could not re-locate them this session. Do not cite this item.

**M7. GN-II k* quoted without its calibration.** k* has units conductivity×time, so a bare number is meaningless. Setting k* = k_th/τ₀ makes GN-II reproduce the LS speed to within the coupling δ (verified: 1125.9 vs 1119.9 m/s). *Confidence: HIGH.*

**M8. Caputo heat equation written dimensionally inconsistently.** κ must carry fractional units (or be non-dimensionalised); most papers write κ in m²/s next to a fractional time derivative. *Confidence: HIGH that the inconsistency exists; I did not count instances.*

**M9. "Fractional / memory-dependent models resolve the infinite-speed paradox."** They do not: both are non-finite-speed (V-B2k R4, V-B2j R5). They change the attenuation law, not the propagation class. *Confidence: HIGH.*

**M10. Isothermal vs isentropic moduli silently swapped.** The elastic speed differs by O(δ) (~1% for steel, δ = 0.0102). Papers comparing "their" wave speed with "the classical" speed without stating which moduli were used manufacture discrepancies of exactly this size. *Confidence: HIGH on the O(δ) magnitude; the specific papers committing it were not audited.*

**M11. "Nonlocal/gradient effects" treated as one effect.** At identical ℓ and k the two differ by 10⁶ (V-B2m). They are opposite physics. *Confidence: HIGH.*

**M12. τ₀, τ_q, τ_T, τ_v, a, ℓ, k*, e₀a quoted as "typical material values" without a source.** I could verify **no** measured value of any of these in this session. *Confidence: HIGH (absence of verification).*

**M13. Coupled nonlocal-thermoelastic systems presented as thermodynamic.** The nonlocal operator is applied to the elastic law and the heat equation left local; no entropy-inequality derivation was verified. *Confidence: MEDIUM (absence of evidence).*

**M14 — a defect I committed myself, recorded deliberately.** In the first run of `V-B2_wave_speeds.py`, the DPL and TPL rows had the sign of the k_th k²(1−iωτ_T) term wrong, so both failed the τ → 0 limit check against Biot. The limit checks caught it and I corrected it. This is why the limit checks exist and why every equation in the manuscript needs a verifier who did not write it.

### R4. Verification status by model (what the manuscript may and may not print)

| Model | Equations | Admissibility | Wave speeds | Overall |
|---|---|---|---|---|
| Biot | HIGH (derived) | MEDIUM | HIGH (√(2κω) verified) | usable |
| LS | HIGH (derived; form secondary) | MEDIUM | HIGH | usable |
| GL | **MEDIUM/LOW — form not source-verified** | LOW | LOW (no closed form) | **do not print GL equations without the 1972 paper** |
| GN-I | HIGH (identity) | HIGH | HIGH | usable |
| GN-II | HIGH (derived) | MEDIUM | HIGH (exact) | usable |
| GN-III | MEDIUM (variant problem) | LOW (contested) | HIGH (for stated form) | usable with variants stated |
| DPL | HIGH (form secondary but explicit) | **HIGH for rigid** | HIGH | usable |
| TPL | **LOW (form unresolved)** | LOW | MEDIUM | **needs the 2007 paper** |
| MGT | MEDIUM (coupled form unverified) | **HIGH for rigid prototype** | HIGH (rigid) | usable with coupled caveat |
| MDD | MEDIUM | LOW | HIGH (generic) | usable with kernel stated |
| Caputo | HIGH (standard math) | MEDIUM | HIGH | usable |
| 2T | MEDIUM | MEDIUM | HIGH (structural) | usable |
| Nonlocal/gradient | HIGH (derived) | MEDIUM | HIGH | usable |

## Evidence / Sources

All rows summarise V-B2a…V-B2m, where each claim carries its own source and read level. Numerical values are outputs of `V-B2_wave_speeds.py` (reproducible with that file alone; steel-like constants stated in V-B2a R3).

## Checks done

- Every "finite speed / dissipative / energy-conserving" entry was decided by inspecting the principal part and the presence of an odd-order temperature term — not copied from a table in any paper.
- The five symbolic limit checks (LS→Biot, DPL→Biot, TPL→Biot, GN-III k*→0 ≠ Biot, GN-II rigid exactness) all pass after the M14 correction.
- Numeric cross-checks: Fourier √(2κω) (0.4%); GN-II non-dispersiveness across 6 decades; GN-II ↔ LS speed agreement; MGT both asymptotes; Caputo α=1 ≡ Fourier; nonlocal/gradient opposite asymptotics.
- Consistency of the "dissipative" column with the "energy-conserving" column: only GN-II is both non-dissipative and energy-conserving, which is the required internal consistency.

## Confidence

- **HIGH** on the classification columns and on mistakes M1–M3, M6–M11.
- **MEDIUM** on M5, M12, M13 (absences of verification rather than positive findings) and on GL/TPL equation-level status.
- **LOW**: nothing in the table is *presented* as LOW-confidence, but see R4 — GL and TPL equations should not be printed from this file.

## NOT verified / open issues

1. **No primary full text was opened for any of the 14 models.** Every "equation" column is either standard published form or my derivation from it. The two rows that are genuinely unsafe to print without the source paper are **GL** and **TPL**.
2. **Coupled (as opposed to rigid) stability is unresolved for DPL, TPL and MGT.** My rigorous results are for the rigid models. Generalising them to the coupled systems requires the sources on coupled-DPL/MGT stability that I did not open.
3. **"Energy-conserving" for GN-II is asserted on the basis of the absence of a dissipative term.** The actual conserved functional was not constructed — that is Phase B3's job, and it must be done before the review claims GN-II energy conservation at an interface.
4. **No experimental values for any parameter** in the "key parameter" column were verified.
5. The mistake catalogue is **not a systematic literature survey** — it is what I encountered while verifying these 14 models. A proper prevalence claim ("X% of papers do Y") would need a coded sample and was not attempted.
6. Piezothermoelasticity is in the mission statement but **not** in this phase's model list; it is unverified here and would need its own file (candidate V-B2n) if the review covers piezoelectric coupling.
