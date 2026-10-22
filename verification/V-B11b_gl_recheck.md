# V-B11b — Green–Lindsay recheck against the PRIMARY system (BRAVE_B11 condition 2)

**Order:** `control/BRAVE_B11.md` condition 2 @ `origin/claude/control` `a0ace86`. **Access date:** 2026-10-22.
**Primary text:** Green & Lindsay (1972), *J. Elasticity* **2**:1–7, DOI `10.1007/BF00045689`, eqs (4.11),
(4.13), (4.14), (4.16) — relayed by the supervisor from the PDF in `control/FULLTEXT_FINDINGS_01.md`
item F1. **I have not opened the paper myself**; the equation content below is quoted from that relay,
and every verdict that depends on it is tagged `primary via supervisor relay`.
**Code:** `V-B11b_gl_interface.py` (a patched copy of the frozen `V-B3d_coupled_interface.py`).
**Scope: isotropic linear GL, 1-D normal incidence and the dispersion relation; the rigid (β = 0)
thermal problem is treated separately in §3.5.**

---

## 1. Task

Re-open and re-classify `V-B2c` R8, `V-B4` W1, `CLAIM_LEDGER` CL-006, `EQUATION_LEDGER` (4.9) row,
`V-B2z` GL cells and the `V-B3` GL interface numbers, using the original GL equations: Fourier flux,
stress `β(T + τ₁Ṫ)`, energy `k∇²T = ρc(Ṫ + τ₀T̈) + βT₀ ė_kk` with **no τ₀ on the coupling**. Redo the GL
dispersion and the GL R/T/A with that coupling. Frozen counts may change only where a verdict changes,
and every change must be listed.

## 2. Method

1. Wrote the primary system down in 1-D, frequency domain, `e^{i(kx−ωt)}`:
   `σ = M u,x − β(T + τ₁Ṫ)`, `ρü = σ,x`, `k T,xx = ρc(Ṫ + τ₀T̈) + βT₀ u̇,xx`, `q = −kT,x`.
2. Built the coupled determinant as a quadratic in `x = k²`:
   `(Mx − ρω²)(k_th x − iωρc(1 − iωτ₀)) − i x ω β²T₀ (1 − iωτ₁) = 0`
   in the same bookkeeping as `V-B3d` (`A(k²) = Mk² − ρω²`, coupling `+ikβ`), and the eigenvector
   `(u, θ) ∝ (−ikβ, (Mk² − ρω²)/(1 − iωτ₁))` — the `τ₁` factor is the only change from Biot.
3. Patched `V-B3d_coupled_interface.py` (frozen, validated) with two new branches:
   `GL` (primary coupling) and `GL_ms` (the manuscript's `(1 + τ₀∂_t)` on the coupling as well). Nothing
   else in the harness changed; the material set, interface conditions, flux definition and total-field
   `R,T` are identical to the frozen case.
4. **Harness validation before any GL number is quoted:** the Biot branch must reproduce `V-B3d`'s
   frozen 4.46 × 10¹¹ Hz row. It does, to all printed digits, with solver residual `1.2 × 10⁻¹⁶`.
5. Limit checks: `τ₀ = τ₁ = 0` must reduce to Biot; `τ₁ = τ₀` must **not** equal LS (in the corrected
   slot structure the stress still carries a rate).

## 3. Result

### 3.1 The corrected GL system (primary, relayed)

| element | Green–Lindsay 1972 | manuscript (4.9) |
|---|---|---|
| stress | `σ_ij = 2μe_ij + [λe_kk − β(T + τ₁Ṫ)]δ_ij` | same (not disputed) |
| heat flux | `q_i = −k θ_,i` — **Fourier, no relaxation** | §4.4 states LS's Cattaneo law immediately above it |
| energy | `k∇²T = ρc(Ṫ + τ₀T̈) + βT₀ ė_kk` — **coupling carries no τ** | `βT₀(u̇_,ii + τ₀ü_,ii)` — coupling carries τ₀ |
| ordering | `τ₁ ≥ τ₀ > 0` from (4.14) `dα − h ≥ 0` with (4.16) `d,h,α > 0` | not stated |

The manuscript's row is therefore **LS's energy operator with GL's stress law**. It is a real variant —
my own `V-B2c` §R8 S2 (Singh 2020) writes exactly that uniform operator — but it is not GL 1972, and the
manuscript attaches the Green–Lindsay name to it.

### 3.2 GL dispersion: what the missing/extra `τ₀` does

Rigid branch (β = 0), unchanged by any of this: `c_h = √(κ/τ₀) = 354.14 m/s` for the steel-like data.
Coupled branches: the secular equation is **quadratic in `k²`** for both GL and the variant, so the
branch count cannot distinguish them; what changes is the coupling product, `ixωβ²T₀(1 − iωτ₁)` for GL
against `ixωβ²T₀(1 − iωτ₀)(1 − iωτ₁)` for the variant. At low frequency (`ωτ ≪ 1`) the two coincide;
they separate once `ωτ₀ ≳ 1`.

### 3.3 GL interface numbers (steel | aluminium, perfect contact, normal incidence)

`τ₀ = 10⁻¹⁰ s`, `τ₁ = 5 × 10⁻¹⁰ s` (GL ordering), `T₀ = 300 K`. `R`, `T` from the **total** field flux
`J = −⟨σv⟩ + ⟨θq⟩/T₀`, `A = 1 − R − T` (a definition, not a check).

| f [Hz] | `R_GL` | `R_ms(4.9)` | ΔR | `T_GL` | `\|k_t\|/\|k_e\|` GL |
|---|---|---|---|---|---|
| 10⁶ | 0.208019 | 0.208043 | −2.4×10⁻⁵ | 0.791981 | 671.4 |
| 10⁸ | 0.207935 | 0.208136 | −2.0×10⁻⁴ | 0.792065 | 67.21 |
| 10¹⁰ | 0.211742 | 0.208077 | **+3.7×10⁻³** | 0.788258 | 16.77 |
| 10¹¹ | 0.211836 | 0.208078 | **+3.8×10⁻³** | 0.788164 | 16.66 |
| 4.46×10¹¹ | 0.211836 | 0.208078 | +3.8×10⁻³ | 0.788164 | 16.66 |
| 10¹² | 0.211837 | 0.208078 | +3.8×10⁻³ | 0.788163 | 16.66 |

* The **difference is real and saturates at ≈ 1.8 % relative in `R`** (3.8×10⁻³ absolute) once
  `ωτ₀ ≫ 1`; it is not a rounding artifact.
* The variant is *insensitive* to frequency above 10⁸ Hz (R pinned at 0.20808), whereas primary GL keeps
  moving and saturates at 0.21184. The manuscript's form therefore produces a flat high-frequency
  partition that the original theory does not.
* For comparison the frozen LS row of `V-B3d` at 10¹⁰ Hz is `R = 0.208360`; **GL at `τ₁ = τ₀` gives
  0.211742**, so GL and LS are numerically distinguishable at equal times — see §3.4.

### 3.4 Limit checks

| check | expectation | result |
|---|---|---|
| Biot reproduction | frozen `V-B3d` row | `R = 0.212026`, `T = 0.787974`, residual `1.2×10⁻¹⁶` ✔ |
| `τ₀ = τ₁ = 0` → Biot | exact | GL(0,0) `R = 0.209017407`, `T = 0.790982593`; Biot `0.209017407` / `0.790982593` ✔ |
| GL at `τ₁ = τ₀` vs LS | must differ | GL `R = 0.211742` vs LS `0.208360` at 10¹⁰ Hz — they differ ✔ |
| `A = 1 − R − T` | identically 0 | ≤ 3.3×10⁻¹⁶ in every GL row (definition, not evidence) |

**Retraction:** my earlier diagnostic in `V-B2c` §R5 ("GL ≡ LS when the two times coincide") is
**WRONG** for the primary system. It was an artifact of the wrong slot assignment R8 already corrected;
with `τ₁` on the stress and `τ₀` only on `T̈`, GL at equal times still keeps a stress-rate term and a
different coupling, and the numbers above separate them.

### 3.5 The independent check does *not* close for GL — and that is the finding

`V-B3d`'s informative check is that `T·J_i` equals the bulk dissipation integral
`∫⟨D⟩dx` with `⟨D⟩ = (k/(2T₀))|∂ₓθ̂|²`. For GL the integral/`T·J_i` ratio comes out **−0.021 at 10⁶ Hz,
−0.019 at 10⁸ Hz, ≈0 above 10¹⁰ Hz** — it does **not** equal 1. GL's energy identity is not Biot's
(the `τ₁` stress rate breaks the simple balance), so this file cannot supply an independent validation of
the GL partition. **Consequence:** the GL `R,T` above rest on flux continuity at the interface *only* and
are `CORRECT-CONDITIONAL` on that definition. This is exactly the caution `V-B3a` §7 already carried
("do not print a GL energy identity from this file") — it is now quantified rather than asserted.

### 3.6 Verdict changes (each one listed, as ordered)

| item | before | after | basis |
|---|---|---|---|
| `EQUATION_LEDGER` **EQ-042** (`sec04:101`, 4.9) | CORRECT-CONDITIONAL | **WRONG-CONFIRMED** — as a statement of GL 1972; a legitimate *variant* if relabelled | F1 primary; §3.1; ΔR 3.8×10⁻³ |
| `CLAIM_LEDGER` **CL-006** | WRONG (PROBABLE), MEDIUM | **WRONG-CONFIRMED**, HIGH | ordering primary-sourced (4.14)/(4.16) |
| `V-B2c` **R8** | "the manuscript's GL system is the standard one and my charge was wrong" | **charge partly right**: the slot table (R8.2) is right, but (4.9)'s coupling term is not GL | F1 |
| `V-B2c` **R5** diagnostic | "GL ≡ LS when τ₁ = τ₂ = τ₀" | **retracted** | §3.4 (numbers differ) |
| `V-B2z` GL cell | "no — form and ordering unsourced" | form **and** ordering now primary-relayed; still **do not print from `V-B2c`** (flux law must be stated) | F1 |
| `V-B3b` GL row (thermal-only `R = 0.567289`, `T = 0.432711`) | unchanged | **still correct** — GL's flux is Fourier, so the rigid problem *is* Biot's | §3.5 first line |
| `V-B3` coupled GL numbers | absent / LS-contaminated | replaced by §3.3, with the caveat of §3.5 | this file |
| `V-B4` **W1** | "withdrawn — the manuscript was right and I was wrong" | **partly right**: (4.9) is not GL 1972. My stated *reason* (one free energy forces one time) was wrong and stays withdrawn | F1 |

Frozen counts: `EQUATION_LEDGER` **176** (one verdict changed, no row added); `CLAIM_LEDGER` **53**
(one verdict changed).

## 4. Evidence / sources

* Green, A. E.; Lindsay, K. A. (1972). "Thermoelasticity". *J. Elasticity* **2**(1):1–7.
  DOI `10.1007/BF00045689`. **Not opened by me.** Content quoted from
  `control/FULLTEXT_FINDINGS_01.md` F1 (supervisor read the PDF; eq. (4.13) is on p. 5 of the paper, so
  the handler can verify it directly).
* Lord & Shulman (1967), eq. (23) — contrast term `(3λ+2μ)α_T T₀(ė + τ₀ë)`; via the same relay (F2).
* `V-B3d_coupled-interface-rta.md` (frozen) for the harness and for the Biot/LS reference numbers.
* `V-B11b_gl_interface.py` output (reproducible, stdlib + numpy; run with any Python 3 that has numpy).

## 5. Checks done

1. **Harness validated against a frozen table before use** (Biot row reproduced to all digits).
2. **Two limit checks** (`τ₀=τ₁=0` → Biot; `τ₁=τ₀` ≠ LS) so the GL branch cannot be silently the LS
   branch — which is precisely the defect being corrected.
3. **The `τ₁` factor is in exactly two places** (stress and eigenvector) and nowhere else; the dispersion
   keeps the same `k²`-quadratic structure, so branch counting is unaffected and cannot mask an error.
4. **The independent dissipation check was run and reported as failing** rather than dropped.
5. Every verdict change is tied to a line of the primary relay or to a printed number above (§3.6).
6. Ledger row counts verified after the edit (176 / 53) — the frozen counts did not move.

## 6. Confidence

* That the primary GL energy equation has **no** `τ₀` on the coupling, and that the manuscript's does:
  **HIGH** (single primary statement, relayed with page attribution; the LS contrast in F2 is consistent).
* The GL interface numbers (§3.3): **MEDIUM-HIGH** — the harness is validated and the numbers are
  reproducible, but the partition has *no* independent energy check for GL (§3.5), so they are only as
  good as the flux-continuity definition.
* `ΔR ≈ 3.8×10⁻³`: **HIGH** as a computed difference at fixed data; **MEDIUM** as a physical statement,
  because it depends on the chosen `τ₀ = 10⁻¹⁰ s`, `τ₁ = 5×10⁻¹⁰ s` pair and the steel/Al data.
* Ordering `τ₁ ≥ τ₀ > 0`: **HIGH** (two independent statements in F1's reading, plus (4.14)/(4.16)).

## 7. NOT verified / open issues

* **I did not open Green–Lindsay 1972.** Everything here is conditional on the relay in
  `FULLTEXT_FINDINGS_01.md`. If that relay is wrong on the coupling term, this entire file inverts — the
  risk is stated plainly, and one page (p. 5, eq. 4.13) settles it.
* **GL's energy identity is not established.** No free-energy/Lyapunov functional for GL was constructed
  or sourced, so "GL dissipation ≥ 0" and "GL R+T+A closes independently" both remain **unverified**.
  `V-B3a`'s "do not print a GL energy identity" stands.
* The GL numbers use **one** material pair and **one** `(τ₀, τ₁)` pair. The `τ₁` dependence is not
  mapped; I did not sweep it, so "ΔR saturates at 1.8 %" is a statement about this parameter point.
* Only **normal incidence, 1-D, perfect contact** is solved. Oblique incidence (`V-B3c`'s literature) and
  interface thermal resistance are untouched.
* `τ₁` was set to `5τ₀` arbitrarily within GL's admissible range (the ordering is the only constraint I
  have). A different ratio changes the numbers; I did not test whether any admissible ratio reproduces
  the manuscript's flat high-frequency branch.
* The variant `GL_ms` is *my reconstruction* of what (4.9) means (uniform operator applied to both
  temperature and strain-rate terms). If the manuscript intends something else, §3.3's `R_ms` column is
  the wrong comparator.
