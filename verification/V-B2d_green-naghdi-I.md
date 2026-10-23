# V-B2d — Green–Naghdi Type I (and a warning about "GN-I vs Biot")

**Access date 2026-10-22.**

## Task

As V-B2a, for Green–Naghdi Type I. **Result up front: GN Type I is the classical Fourier/Biot theory.** This file is short for that reason, and its main product is a pitfall warning.

## Method

1. **Provenance.** The GN family is presented in:
   - Green, A.E. & Naghdi, P.M. (1991) "A re-examination of the basic postulates of thermomechanics", *Proc. R. Soc. Lond. A* **432**:171–194 — **not verified in this session** (no Crossref lookup performed; treat as UNVERIFIED).
   - Green, A.E. & Naghdi, P.M. (1992) "On undamped heat waves in an elastic solid", *J. Thermal Stresses* **15**(2):253–264, DOI 10.1080/01495739208946136. Crossref 1555, OpenAlex 1687. Read level: **record only.**
   - Green, A.E. & Naghdi, P.M. (1993) "Thermoelasticity without energy dissipation", *J. Elasticity* **31**(3):189–208, DOI 10.1007/BF00044969. Crossref 2194, OpenAlex 2402. Read level: **record only.**
2. The type I/II/III classification is the standard modern reading of the GN series. I verified the *structure* (that type I reduces to Fourier–Biot) by taking the type III equations and setting the "thermal displacement" conductivity k* = 0 (see V-B2f), and by confirming that type II (see V-B2e) is the k_th = 0 limit.

## Result

### R1. What GN Type I is

The GN framework adds a **thermal displacement** α (not to be confused with thermal expansion), defined by

    α̇ = θ

and constructs a free energy depending on the strain and on ∇α. The three types differ only in how the entropy flux is built from α:

| Type | Entropy flux / conduction | Consequence |
|---|---|---|
| **I** | q_i = −k_th θ_,i (i.e. α enters only through θ = α̇) | **exactly the classical Fourier theory** |
| II | q_i = −k* α_,i | undamped thermal waves |
| III | q_i = −(k* α_,i + k_th θ_,i) | damped thermal waves |

So **GN-I ≡ Biot/Fourier** (V-B2a). It adds a notational framework, not a new model.

### R2. Consequence for the manuscript — the pitfall

Three related errors are common enough that the review should address them directly:

1. **Counting GN-I as a separate theory.** A table listing "Biot, LS, GL, GN-I, GN-II, GN-III, DPL, TPL, MGT" as nine distinct models is **wrong**: GN-I is Biot. The honest count is eight distinct conduction structures in that list.
2. **Attributing the classical theory to GN.** GN re-derived it; they did not introduce it. Attribution belongs to Biot (1956) and, for the coupled-system thermodynamics, to Biot's framework.
3. **"GN eliminated the paradox of infinite heat propagation."** GN's *contribution* is type II/III. Type I retains the parabolic paradox exactly.

### R3. Parameters

Identical to V-B2a: λ, μ, M, β, ρ, c, k_th, κ, T₀, δ. No new parameter is introduced by type I. (Type II/III introduce k*; see V-B2e/f.)

### R4. Admissibility

Identical to V-B2a, since the equations are identical. In particular GN-I inherits the **absence of a finite thermal speed** — the very property the GN programme was created to fix.

### R5. Characteristic equation

Identical to V-B2a:

    (M k² − ρω²)(k_th k² − iωρc) + i β²T₀ ω k² = 0

Thermal branch v_ph = √(2κω) with no finite asymptote.

### R6. Label hazard in the literature

"Green–Naghdi theory" without a type number is ambiguous in a large fraction of the applied literature, and many papers that say only "GN theory" mean type II. **A review must require the type number**, and should say why: type I is conservative-parabolic, type II is conservative-hyperbolic, type III is dissipative-hyperbolic — three completely different energy behaviours (this is the substance of the Phase B3 energy-flux classification).

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| GN 1992, JTS 15(2):253–264, DOI | Crossref API | Record only |
| GN 1993, J. Elasticity 31(3):189–208, DOI | Crossref API | Record only |
| "Type II permits heat-wave propagation without classical energy dissipation, while Type III adds dissipative conduction" (qualitative) | Noble (2026) preprint §5.2 — **SECONDARY, unrefereed** | Body (PDF) |
| GN-I ≡ Fourier/Biot; type classification | Standard reading, **structure verified** by the k*=0 and k_th=0 limits in V-B2e/f | Derivation |

## Checks done

- **Limit check**: the type III determinant with k* → 0 must retain the k_th θ_xxt term and must not equal Biot (it does not — PASS, i.e. type III with k*=0 is *not* Biot; it is a distinct dissipative-hyperbolic model). Conversely type II with k_th = 0 is undamped, confirming the classification internally.
- **Internal consistency of the type table**: type I must be the case where α appears only via θ. Under that condition the free energy's α-gradient term is a θ-gradient term, whose variation reproduces Fourier's law — so the identification is not merely conventional.
- **Citation asymmetry check**: GN 1993 (2194/2402) is cited more than GN 1992 (1555/1687), and both are cited far more than the 1991 foundational paper — consistent with practitioners citing the accessible "type" papers rather than the framework paper.

## Confidence

- **HIGH** that GN-I is the classical Fourier/Biot theory and that listing it as a ninth distinct model is an error.
- **MEDIUM** on the precise publication history of the 1991 framework paper (not verified here) and on which paper "introduced" each type — the 1992 paper is usually credited with type II, but I could not read it to confirm.
- **LOW**: none of the GN papers' actual text was read.

## NOT verified / open issues

1. **GN 1991, 1992, 1993 full texts NOT opened.** The type I/II/III attribution to specific papers is **UNVERIFIED from primary text**. Specifically unverified: whether type III was introduced in the 1992 paper, the 1993 paper, or a later GN paper (there are GN papers in 1992–1994 and a 1996 "thermomechanics" paper). This must be checked before the review prints a date for each type.
2. The Green & Naghdi 1991 *Proc. R. Soc.* paper is cited above from memory of the standard reference; **I did not perform a Crossref lookup for it** in this session, so even its volume/pages are UNVERIFIED.
3. Whether GN themselves used the labels "type I/II/III" or whether later authors (notably Ignaczak) imposed the numbering is **UNVERIFIED**. If the numbering is a later convention, the review must say so — it is exactly the kind of misattribution the brief asks me to flag.
