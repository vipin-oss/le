# V-B2m — Eringen nonlocal elasticity and Mindlin strain-gradient elasticity

**Access date 2026-10-22.**

## Task

As V-B2a, for the two size-dependent elasticity frameworks that the brief groups as "nonlocal/gradient". They are treated together here because the review's most useful single observation about them is a **contrast**, not a parallel.

## Method

1. **Provenance.**
   - Eringen, A.C. (1972) "Linear theory of nonlocal elasticity and dispersion of plane waves", *Int. J. Eng. Sci.* **10**(5):425–435, DOI 10.1016/0020-7225(72)90050-X. Crossref 1272, OpenAlex 1449.
   - Eringen, A.C. (1983) "On differential equations of nonlocal elasticity and solutions of screw dislocation and surface waves", *J. Appl. Phys.* **54**(9):4703–4710, DOI 10.1063/1.332803. Crossref 4542, OpenAlex 4812 — **the single most-cited paper in the whole B1c list.**
   - Mindlin, R.D. (1964) "Micro-structure in linear elasticity", *Arch. Ration. Mech. Anal.* **16**(1):51–78, DOI 10.1007/BF00248490. Crossref 3677, OpenAlex 3982.
   - Mindlin, R.D. & Tiersten, H.F. (1962) "Effects of couple-stresses in linear elasticity", *Arch. Ration. Mech. Anal.* **11**(1):415–448, DOI 10.1007/BF00253946. Crossref 2388, OpenAlex 2593.
   All read level: **record only — none opened.**
2. Derived both 1-D dispersion relations and verified them symbolically and numerically (below).

## Result

### R1. Eringen nonlocal elasticity — the differential model

The integral nonlocal model is reduced (Eringen 1983) to the differential form

    σ_ij − (e₀a)² ∇²σ_ij = C_ijkl ε_kl

with **(e₀a)** the nonlocal length (a = internal length, e₀ = calibration constant, dimensionless). Combined with equilibrium/momentum ρü_i = σ_ij,j.

**1-D plane waves.** Eliminating σ gives, for a harmonic mode,

    ω² = c²k² / (1 + (e₀a)²k²)        ⇒        v_ph = c / √(1 + (e₀a)²k²)

**Verified symbolically** (SymPy: ω = c k/√(1+k²ℓ²)) and numerically (ℓ = 1 nm):

| k (1/m) | v_ph (m/s) |
|---|---|
| 0 | 5796.7 |
| 10⁶ | 5796.7 |
| 10⁹ | 4098.9 |
| 10¹² | **5.797** |

**Nonlocal ⇒ softening**: the phase speed decreases monotonically with k and → 0 as k → ∞. The model has a **finite intrinsic length** ℓ = e₀a and a **frequency cutoff** (no wave propagates above ω_max = c/ℓ).

### R2. Mindlin strain-gradient elasticity

The gradient model adds strain-gradient terms to the free energy, giving (1-D, one gradient length ℓ):

    ω² = c²k²(1 + ℓ²k²)        ⇒        v_ph = c √(1 + ℓ²k²)

**Verified symbolically** (SymPy: ω = c k√(1+k²ℓ²)) and numerically (ℓ = 1 nm):

| k (1/m) | v_ph (m/s) |
|---|---|
| 0 | 5796.7 |
| 10⁶ | 5796.7 |
| 10⁹ | 8197.8 |
| 10¹² | **5,796,703** |

**Gradient ⇒ stiffening**: the phase speed *increases* without bound with k.

### R3. The contrast that the review should lead with

At the **same** length ℓ = 1 nm and the **same** wavenumber k = 10¹² m⁻¹:

- nonlocal: v_ph = **5.8 m/s** (softens by a factor 10³)
- gradient:  v_ph = **5.8×10⁶ m/s** (stiffens by a factor 10³)

**A factor of 10⁶ between the two "size-dependent elasticity" models at identical parameters.** They are not two approximations of the same physics; they encode opposite length-scale physics (long-range attraction/softening vs local curvature penalty/stiffening). Any review, or any paper, that says "nonlocal/gradient effects" as if they were one effect is making a substantive error. This is, in my judgement, the single most useful clarification Phase B2 has produced.

**Second contrast — thermodynamic/well-posedness:**

- Mindlin's gradient theory has a **positive-definite free energy** (it is derived from one), is well posed, but **does not give a finite signal speed** (v_ph → ∞ as k → ∞) — it is *more* superluminal than classical elasticity, not less.
- Eringen's differential nonlocal model has a **finite frequency cutoff** but its differential form is **not** the exact equivalent of the integral model; the 1983 reduction is an approximation valid for a particular kernel, and the "nonlocal paradoxes" (e.g. stiffening of clamped beams, boundary-layer inconsistency) come from that mismatch.

### R4. Admissibility

- **ℓ² = (e₀a)² ≥ 0**: the sign is irrelevant in the differential model (it enters squared). A negative ℓ² gives the gradient-like dispersion, i.e. silently switches theories — a plausible mechanism for "nonlocal" papers that report stiffening.
- **Gradient:** ℓ² > 0 required for a positive-definite energy; ℓ² < 0 reverses the sign of the highest-order term and destroys well-posedness of the static problem (the energy is unbounded below).
- **Neither model is thermodynamically "more admissible" than classical elasticity** — both are conservative (no dissipation). Neither fixes the finite-speed problem of classical elasticity; the gradient model worsens it.
- **Coupling to thermoelasticity** is, in almost all published work, **ad hoc**: the nonlocal/gradient operator is applied to the elastic constitutive law and the heat equation is left local. No thermodynamic derivation of a coupled nonlocal-thermoelastic system was verified in this session.

### R5. Asymptotics and limits

- Both reduce to classical elasticity at k → 0 (v_ph → c) — verified numerically in both tables.
- Nonlocal: **dispersive at all k**, with v_ph → 0; physically this means the model cannot support wavelengths shorter than ~ℓ.
- Gradient: dispersive with v_ph → ∞; the model therefore has no natural short-wavelength cutoff and inherits the classical infinite-speed problem.

### R6. Where each is defensible

- **Gradient (Mindlin):** defensible where the microstructure is a genuine continuum with bending stiffness — cellular solids, lattice metamaterials, foams, bone. The length is then \(\ell\) = cell size and can be measured.
- **Nonlocal (Eringen):** defensible as a *phenomenological* softening model for nanostructures. The "e₀" calibration has no first-principles value, and the fact that a *single* e₀ is claimed to fit many different problems (buckling, vibration, wave propagation, different boundary conditions) is, to put it carefully, a strong claim that the literature has not established.

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| All four bibliographic records and citation counts | Crossref / OpenAlex API | Record only |
| σ − (e₀a)²∇²σ = C:ε ; ω²= c²k²/(1+ℓ²k²) | **standard form, NOT source-verified**; dispersion derived by me and verified by SymPy | Derivation |
| ω² = c²k²(1+ℓ²k²) for gradient | Same | Derivation |
| The 10⁶ contrast | **My computation** | Derivation |

## Checks done

1. **Symbolic verification** of both dispersion laws with SymPy (solutions returned: c k/√(1+k²ℓ²) and c k√(1+k²ℓ²)).
2. **k → 0 limit**: both recover v_ph = c = 5796.7 m/s exactly (verified in both tables).
3. **Numerical magnitude check** of the contrast at fixed k and ℓ — the 10⁶ ratio is arithmetic, not an estimate.
4. **Structural check**: the two laws are reciprocal-shaped — one divides by √(1+ℓ²k²), the other multiplies by it. This makes the opposite-signed asymptotics inevitable and independent of parameter choice, i.e. a **robust** result.
5. **Citation-order check**: Eringen 1983 (4542) outranks Mindlin 1964 (3677) in both indices — so the nonlocal differential model, not the gradient model, is the field's most-cited object. That has a consequence for how much space each deserves.

## Confidence

- **HIGH** on both dispersion relations, their limits, and the 10⁶ contrast.
- **MEDIUM** on the characterisation of the "nonlocal paradoxes" and on the claim that the 1983 differential form is an approximation to the integral model (this is well known but I did **not** verify it from Eringen's text).
- **LOW** on the physical defensibility judgements in R6 — these are my assessments, and the manuscript should present them as argued positions with citations, not as facts.

## NOT verified / open issues

1. **None of the four papers was opened.** In particular: Eringen's kernel and his 1983 reduction (approximation or exact?) is **UNVERIFIED**; Mindlin's full gradient constitutive law (he has five additional constants in the general case, not one ℓ) is **UNVERIFIED**. Mindlin's theory in general has **five** gradient constants plus the couple-stress reduction; reducing it to a single ℓ is a modelling choice, and the review must say so.
2. **The "e₀" calibration literature** (values 0.1–2 quoted for different problems) was not verified.
3. **Coupled nonlocal-thermoelastic systems** are ad hoc in everything I saw; no thermodynamic derivation verified. This is an explicit **open problem** the review could name.
4. **Nonlocal + relaxation combined** (e.g. "nonlocal LS thermoelasticity") is a large literature I did not survey in this phase; it belongs to Phase B3/B4 scope.
5. The claim that gradient elasticity "worsens" the infinite-speed problem is mathematically immediate from v_ph → ∞, but no published statement to that effect was verified.
