# V-B4-RECHECK — response to `control/ARBITRATION_B4.md` (Claude, 22 Oct 2026)

> **REVISION 2026-10-22 (BRAVE_B11 condition 2).** W1's *withdrawal* is itself revised: on the primary
> 1972 text (`control/FULLTEXT_FINDINGS_01.md` F1) the manuscript's (4.9) carries τ₀ on the strain-rate
> coupling, which Green–Lindsay's (4.13) does not. So **W1 was partly right** — the charge's stated
> *reason* (one free energy forces one relaxation time) was wrong and stays withdrawn, but the conclusion
> "the printed equation is not Green–Lindsay 1972" holds. `EQUATION_LEDGER` EQ-042 is re-graded
> WRONG-CONFIRMED on that narrow ground; `V-B11b_gl_recheck.md` §3.6 lists every change.


**Task.** Re-check W1 and W2 exactly as the arbitration asks; re-grade the three WRONG verdicts into
CONFIRMED-WRONG / PROBABLE / DISPUTED; make `V-B2c`, `V-B2z` and `V-B4` agree with each other.

**Method.** W1: source search for independent statements of the GL system with slot-level equations,
≥3 sources required, each with access details. W2: recompute the branch count with the *full* field
set (three displacements), isotropic and 6mm, symbolically. W3: prove the transform claim from the
definition rather than from a source.

## 1. Result in one line

**W1 and W2 are withdrawn — the manuscript was right and I was wrong. W3 stands as
CONFIRMED-WRONG.** Both of my errors have the same shape: I computed a *sub-problem* and asserted
the whole.

| # | my B4 verdict | re-graded | who was right |
|---|---|---|---|
| W1 — GL energy equation (4.9) | WRONG | **WITHDRAWN — DISPUTED, resolved against me** | manuscript / arbitration |
| W2 — degree 8 in (9.9) | WRONG | **WITHDRAWN — my test was a sub-problem** | manuscript |
| W3 — MDD Fourier symbol | WRONG | **CONFIRMED-WRONG** | me (derivation + numerics) |
| CL-006 ordering | WRONG, "τ₀ ≥ τ₁" | **verdict stands, my direction was backwards** | τ₁ ≥ τ₀ |
| CL-010 "no ordering condition applies" | WRONG | **CONFIRMED-WRONG (2 sources)** | me |
| A = D/\|J_inc\| (9.10) | UNCLEAR | unchanged, accepted by arbitration | me |

## 2. W1 — Green–Lindsay: withdrawn

### 2.1 What I claimed and why it was wrong

I claimed (4.9) is "a verbatim copy of the LS equation" because the stress (4.10) carries τ₁ while the
energy equation carries τ₀, and I argued that one free energy `ψ(ε,T,Ṫ)` forces the *same* time in
both. That argument is valid **only for a one-time model**: if the entropy is
`s = (β/ρ)ε_kk + (c_v/T₀)(T + τṪ)` then indeed the same τ appears in the stress and in the energy
equation, and the resulting theory has one relaxation time — it is LS with a shifted stress, not GL.
GL's two times are *independent constitutive parameters* introduced in the Green–Laws/GL entropy
inequality, where the entropy function and the stress function are not tied to a single τ. My
derivation therefore characterised a different model and told me nothing about (4.9).

The arbitration's reason (b) is exactly this, and it is correct.

### 2.2 Sources (all opened this session, 2026-10-22)

| # | source | access | energy-equation time sits on | stress time | ordering stated | finite speed stated |
|---|---|---|---|---|---|---|
| **S1** | Bera, Mondal, Mahapatra, Roymahapatra, Acharjya, "Generalized theory of thermoelasticity in isotropic and homogeneous thermoelastic solids", *Turkish J. Mathematics and Computer Science* (turcomat.org/index.php/turkbilmat, article 11902) | **full text, open** | `α₀` on `T̈` only: `−q_{i,i}+ρQ = ρc_e(Ṫ+α₀T̈) + βT₀u̇_{i,i}` (eq. 12/15); stress `τ_ij = λu_{i,i}δ+2μe_ij−β(T+α Ṫ)δ` (eq. 13); **Fourier law unchanged** (eq. 14) | `α` | **`α ≥ α₀ > 0`** | yes, `√(K/(ρc_eτ))` for LS; GL not given a speed in this source |
| **S2** | **Singh, B., "A GL Model on Thermo-Elastic Interaction in a Poroelastic Material Using Finite Element Method", *Symmetry* 12(3):488 (2020), DOI 10.3390/sym12030488** | **full text, open** | `τ₀s` acting on *both* the temperature and the strain-rate terms: `K_s∂²Θ_s/∂x² = (∂_t + τ_{0s}∂²_t)(F₁₁Θ_s+F₁₂Θ_f) + (∂_t + nτ_{0s}∂²_t)(T₀R₁₁∂_xu + …)` (eq. 11) | `τ₁s` in stress (eq. 13) and in the momentum equation (eq. 9) | **`0 < τ_{0s} < τ_{1s}`** (from the article's abbreviations block, not from an equation display) | not stated |
| **S3** | preprint "Thermodynamic Admissibility, Finite-Speed Heat Transport, and Wave Stability in Generalized Thermoelasticity: A Critical Review with Analytical Proofs", Research Square rs-10734164/v1 | **abstract/section text, open** | prose only: GL "introduces relaxation in constitutive relations **without using a heat-flux rate in exactly the Lord–Shulman manner** … two nonnegative times, **one entering stress/entropy-temperature coupling and one entering the thermal equation**" | separate time | "two nonnegative times", no explicit ordering | "can produce finite thermal propagation" |

**What the three agree on** (the only thing my verdict needed):

1. GL's heat-flux law is **plain Fourier** — no relaxation on `q`. (S1 eq. 14 explicitly; S3 explicitly.)
2. The **energy equation carries one time**, the **stress carries a different one** — they are
   independent constitutive parameters. (All three.)
3. Where an ordering is stated, the **stress time is the larger**: `α ≥ α₀` (S1), `0 < τ₀ < τ₁` (S2).

**What they differ on:** whether the strain-rate coupling term `βT₀ div u̇` carries the same time as
`T̈`. S1 does not put a time on it; S2 does. The manuscript's (4.9) applies the operator uniformly
(S2's choice). Both are published forms; the uniform one is the more common and is what a
`(1+τ₀∂/∂t)` reading of the energy equation gives.

### 2.3 Corrected verdict on (4.9)

**CORRECT-CONDITIONAL**, not WRONG. (4.9)+(4.10) is the standard GL slot structure with τ₀ = energy
time and τ₁ = stress time. The condition is documentation, and it is a real one:

> **D-1.** §4.4 never states GL's heat-flux law. (4.4) — the LS/Cattaneo relaxation
> `q_i + τ₀q̇_i = −kT_{,i}` — is printed 40 lines above and is the only flux law in the section. A
> reader who carries it into (4.9)/(4.10) gets DPL-with-equal-lags, not GL. S1/S3 both say GL keeps
> Fourier. **One line fixes this**, and without it the paper's $\tau_0$ means two different physical
> things in §4.3 and §4.4.
>
> **D-2.** The ordering, where stated: **τ₁ ≥ τ₀ > 0** (S1: `α ≥ α₀`; S2: `0 < τ₀ < τ₁`). The
> manuscript's "no universal ordering" is therefore wrong as a claim *in this family* (see CL-010).
> In the manuscript's notation the flux/energy time is τ₀ and the stress time is τ₁, so the
> condition to print is `τ₁ ≥ τ₀ > 0` — **the opposite direction to what I wrote in B4**.

### 2.4 Consistency corrections made to my own files

- `V-B2c` §R1/R2 used `(τ₁, τ₂)` with τ₁ on `T̈` and τ₂ on `ë_kk`, i.e. two times *inside* the energy
  equation. That is neither S1 nor S2. New **§R8** records the source-backed structure and
  supersedes the slot assignment in §R1–§R3. The file's *other* content (no flux relaxation, the
  `√(κ/τ₀)` thermal speed, the refusal to print an unsourced ordering) is unaffected — its R7.2
  ordering line (`τ₁ ≥ τ₀`) was right and is now sourced.
- `V-B2z` GL row: ordering was "UNVERIFIED"; now `τ₁ ≥ τ₀ > 0` with S1/S2 cited. GL still stays
  "**do not print the equations**", but for the sharper reason D-1: the manuscript does not state
  which flux law it means.
- `EQUATION_LEDGER` EQ-042: WRONG → CORRECT-CONDITIONAL, note rewritten. `CLAIM_LEDGER` CL-006:
  ordering direction corrected; CL-010 kept and strengthened.

## 3. W2 — secular degree: withdrawn

### 3.1 What I did wrong

I computed the determinant of the **coupled (u₁,u₃,T)** block and got degree 6, then compared it with
a polynomial that covers **all branches of the medium**. The shear branch is a branch of the medium
even when it does not couple to temperature. Counted properly, a 3-D medium has four branches
(qP, qSV, qSH, qT) and the secular polynomial has degree 2×4 = 8 in the vertical wavenumber.

### 3.2 Measurement (`V-B4_branch_count.py`, sympy, exact)

| block | fields | degree in q |
|---|---|---|
| P-SV-T, isotropic | u₁, u₃, T | **6** |
| shear, isotropic | u₂ | **2** |
| **total, isotropic** | | **8** |
| P-SV-T-φ, 6mm piezo-thermoelastic | u₁, u₃, φ, T | **8** |
| shear | u₂ | **2** |
| total, 6mm (before removing the quasi-static factor) | | 10 |

So degree 8 is what the full field set gives, and the manuscript's (9.9) is consistent with it. The
6mm case reaches 8 *within the coupled block alone*, because the elliptic Gauss row `div D = 0` is
quasi-static and raises the polynomial degree by one branch that is not a wave — which is precisely
the "remove the trivial factor" point in the arbitration. Whether the manuscript's `G₁…G₅` are
defined before or after removing it **cannot be decided from the display**, because the coefficients
are not given: that residue stays UNCLEAR, but the *degree* is not the defect.

### 3.3 One correction to the arbitration's own reasoning

The arbitration says 6mm gives "P-SV-T (3 branches) decoupled from SH-φ (1 branch with piezo
stiffening)". The count is right; the mechanism is not, *in the plane it names*. In the sagittal
plane x₁–x₃ with the c-axis along x₃, `E₂ = −∂φ/∂x₂ = 0`, so `D₂` never enters `div D = 0` and the
shear branch does **not** acquire `e₁₅²/ε₁₁` stiffening. The stiffening needs `∂₂ ≠ 0`. The branch
count (4) is unaffected, so the degree conclusion is safe; only the stated mechanism is wrong. If
Arena writes "piezo-stiffened SH" into the text for this plane, that sentence will be wrong.

### 3.4 What the manuscript should still add (unchanged from B4, reduced)

State the **medium and orientation** and say the polynomial **includes the decoupled shear branch**.
That is a scope sentence, not a correction.

## 4. W3 — MDD symbol: CONFIRMED-WRONG

From the definition (`sec06:86`), with `η = t−ξ`,

    D_ω f(t) = (1/ω)∫₀^ω κ(η) f'(t−η)dη
    ⇒ symbol σ(Ω) = (iΩ/ω) K̂(Ω),   K̂(Ω) = ∫₀^ω κ(η)e^{−iΩη}dη

The manuscript's factor is the `κ ≡ 1` special case. Evaluated with the inherited kernel
(`sec06:95`, `κ = 1 − 2βη/ω + α²η²/ω²`) in `V-B4_mdd_symbol_check.py` (exact integration, sympy):

| α | β | ω | Ω | exact σ | manuscript | \|ratio\| |
|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 3 | +1.989992+0.141120i | −1.989992−0.141120i | 1.000 |
| 1.0 | 0.5 | 1 | 3 | +1.594812+0.113096i | −1.989992−0.141120i | 0.801 |
| 1.0 | 0.0 | 1 | 3 | +2.631844−0.409115i | −1.989992−0.141120i | 1.335 |
| 0.5 | 0.25 | 2 | 0.5 | +0.182462+0.355184i | −0.229849−0.420735i | 0.833 |
| 1.0 | 0.5 | 1 | 12 | +0.109263−0.375466i | −0.156146+0.536573i | 0.700 |

`κ ≡ 1` is the only row where the magnitudes agree (the sign difference is the transform convention,
which is consistent inside the paper). For `κ ≠ 1` both magnitude and phase are wrong. This needs no
source: it is a property of the operator. **CONFIRMED-WRONG.** Fix: delete the line, or write
`σ(Ω) = (iΩ/ω)K̂(Ω)` with `K̂` defined.

## 5. My error log for this phase (for the record)

1. **Sub-problem generalisation, twice.** W1 tested a one-time free energy; W2 tested a two-field
   block. In both cases the sub-problem is exactly the case where the claim is true, which is why it
   looked decisive. The rule I should have applied, and did apply in B3d: *if a computation reproduces
   a claim only after you remove part of the system, the claim is about the part you removed.*
2. **Ordering direction.** I wrote `τ₀ ≥ τ₁` in B4 while `V-B2c` §R7.2 wrote `τ₁ ≥ τ₀`. The files
   disagreed and I did not notice; a self-consistency grep across my own V-files before publishing a
   WRONG would have caught it. That grep is now in the checklist below.
3. **Charge inflation.** Three WRONG became one. The B4 summary ranked W1 and W2 as the top two
   defects; the ranking was wrong, and the corrected top defect is the A-definition issue (accepted
   by the arbitration) followed by the §9.7 attributions and `appA`'s coverage.

Checklist addition: before any verdict of WRONG, (i) check the same statement in my own earlier
V-files, (ii) state explicitly which sub-system the check covers and whether the claim is about more.

## 6. Checks done

1. Three independent GL statements fetched and tabulated slot-by-slot, with access level and date.
2. Branch count recomputed block-by-block for the full field set, isotropic and 6mm (sympy, exact).
3. MDD symbol derived from the definition and evaluated exactly against the manuscript's expression.
4. Cross-check of the corrected verdicts against `V-B2c`, `V-B2z`, `V-B4` — the three files now agree:
   energy time τ₀ (on θ̈, and on the strain-rate term in the uniform form), stress time τ₁,
   ordering τ₁ ≥ τ₀ > 0, Fourier flux, `c_h = √(κ/τ₀)`.

## 7. Confidence

HIGH on W1's withdrawal (three sources agree on the slot structure; the arbitration's argument is
independently correct). HIGH on W2 (exact symbolic block degrees). HIGH on W3 (derivation plus exact
numerics). MEDIUM on the 6mm spurious-root bookkeeping (identified by degree count, not by locating
the root).

## 8. NOT verified / open issues

- Green & Lindsay 1972 is still **not opened**. Nothing above depends on it: the slot structure is
  supported by three secondary sources and by the arbitration's independent recollection.
- S3 is a **preprint** (Research Square) and carries no weight beyond corroboration.
- I did not locate a source that states the ordering `τ₁ ≥ τ₀` for GL *and* derives it from the
  entropy inequality; both orderings (`α ≥ α₀`, `0 < τ₀ < τ₁`) are asserted, not proved, in S1/S2.
  If Arena prints the ordering, the honest form is "as commonly imposed" with a citation.
- The 6mm result depends on my choice of the sagittal plane containing the c-axis; other orientations
  were not computed.
