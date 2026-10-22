# V-B9c — Does `ΣR + ΣT (+ E_int) = 1` survive? Test on one concrete `V-B3d` case

**Order:** `control/BRAVE_B9.md` item 4 @ `origin/claude/control` `79999f7`. **Access date:** 2026-10-22.
**Code:** `V-B9a_checks.py` CHECK 5 (the source's own tables) and the frozen
`V-B3d_coupled_interface.py` (the concrete case).
**Scope: energy partition at a passive interface; 1-D normal incidence (my computation) and oblique
incidence, 7 modes, dissipative media (the cited paper's data). Not disputed: the algebra of the modal
decomposition itself.**

---

## 1. Task

The manuscript's §9.7 (`sections/sec09_interfaces.tex:197`) states: *"the conservation identity survives
extension to generalized media, but only when the energy flux is reconstructed from the constitutive
model actually being solved."* F9's objection is that this hides the cross terms `E_int` that the
Barak/Gupta papers carry. Test, on **one concrete case from `V-B3d`**, whether

  `Σ (mode-diagonal R, T) + (all cross terms) = 1`

is **automatic** (an algebraic consequence of flux continuity) or **only enforced by lumping**.

## 2. Method

1. Take the strongly coupled row already frozen in `V-B3d` §3.2 — Biot, steel-like | Al-like, perfect
   contact, normal incidence, `f = 4.46 × 10¹¹ Hz` (the frequency where `|k_t|/|k_e| = 1.00`, i.e. thermal
   and elastic wavelengths coincide). That file already reports **three** distinct partition
   coefficients for the same solution: `R_flux` (total field), `R_ref` (outgoing modes, cross terms
   between the two reflected modes retained), `R_mode` (diagonal only, what most papers compute). The
   three numbers therefore *are* the decomposition with and without cross terms; no new code is needed.
2. Compute the deficits `R_x + T − 1` for each definition and identify which term each deficit is.
3. Independently, read what the cited paper does: its `E_int` (eq 57) is a sum of **pairwise products of
   transmitted amplitudes** `H_s H̄_t` (`s ≠ t`), added to diagonals `‖H_s‖²` (eq 53), and asserted to
   close the budget in eq (58). Then check the paper's own printed numbers against eq (58)
   (`V-B9a_checks.py` CHECK 5).
4. Cross-check the limiting case: the lossless model (GN-II) in `V-B3d` must have all three definitions
   coincide — if it does, the cross terms are exactly the attenuation.

## 3. Result

### 3.1 The concrete case (`V-B3d`, Biot, 4.46 × 10¹¹ Hz, frozen)

| definition | value | `R + T − 1` |
|---|---|---|
| `R_flux` (total field) | 0.212026 | `2.2 × 10⁻¹⁶` |
| `R_ref` (outgoing modes + reflected-pair cross terms) | 0.211074 | `−9.5 × 10⁻⁴` |
| `R_mode` (diagonal only) | 0.211592 | `−4.3 × 10⁻⁴` |

`T = 0.787974` in all three rows (the transmitted side is a single decaying branch there).

Reading:

* `R_mode + T − 1 = −4.3 × 10⁻⁴` — the **diagonal** sum misses 1. That missing piece is *not* a cross
  term between two outgoing modes; it is the **incident–reflected interference** `2Re[σ̂_i v̂_r*]`, which
  comes from normalising by the incident flux while measuring the *total* field.
* `R_ref + T − 1 = −9.5 × 10⁻⁴` — adding the genuinely outgoing–outgoing cross term makes the deficit
  **larger**, by exactly that cross term (`R_ref − R_mode = −5.2 × 10⁻⁴`). So "add the cross terms and
  you get 1" is false in this case: the two omitted pieces have **opposite signs** and different
  physical origin.
* `R_flux` closes to `10⁻¹⁶` — but `R_flux` is *defined* as `(J_i − J_1)/J_i` with `J_1` the total field,
  so `R_flux + T = 1` is flux continuity, not a check.

### 3.2 Why the identity is not automatic

For a quadratic flux functional of the field amplitudes, the total is diagonal + **all** pairwise
products. That decomposition is exact — but it includes pairs that mix incident with outgoing
amplitudes, not only outgoing-with-outgoing. Any "energy ratio" normalised by the incident flux and
summed over the *outgoing* mode set alone is therefore short by the incident–outgoing interference
whenever the medium attenuates (`Im k ≠ 0`). In `V-B3d` that term is `∝ Im k` and vanishes for the
lossless model: at every frequency the GN-II row has all three definitions equal to
`0.208329` and `R + T − 1 ≤ 6.7 × 10⁻¹⁶`. That is the sharpest statement available: **the cross terms
are exactly the attenuation**; in a lossless generalized medium the question does not arise, and in a
dissipative one it cannot be waved away.

### 3.3 What the cited source actually does (`E_int` in Barak et al. 2023)

* eq (53): the transmitted flux of mode `s` is proportional to `‖H_s‖²` — **diagonal only**.
* eq (57): `⟨P_st⟩` carries the pairwise products `H_s H̄_t`; `E_int = Σ_{s≠t} E_st` (eq 58).
* eq (58): `Σ_s(ES_s + E_int + E_RP + E_RT + E_RS) = 1` — asserted as the conservation statement.
* Their printed values: `E_int` is `0` at `θ₀ = 0°` and reaches `−2.07` at `70°` for `n=p=l=1`, i.e. it
  is **O(1), not a correction**. And the sum of the nine printed numbers is **0.120 / 0.889 / 1.121** at
  `θ₀ = 0°, 30°, 70°` (CHECK 5). Eq (58) is therefore not satisfied by the paper's own tables; the
  0.12 at normal incidence is a factor-8 shortfall, not a rounding artefact.
* Consequence: in that literature the "identity" is **enforced by lumping** — `E_int` collects whatever
  the diagonal mode fluxes miss — rather than being an independent check. My case shows that even the
  lumping is incomplete unless the incident–outgoing interference is inside it.

### 3.4 Verdict on the §9.7 sentence (scoped)

"Reconstruct the flux from the constitutive model and the identity survives" is **necessary but not
sufficient**:

* `CORRECT-CONDITIONAL` if read as "with the model's own flux and a total-field definition, `R + T = 1`
  holds at a passive interface" — that is exactly what `V-B3d` shows to `10⁻¹⁶`.
* `WRONG-CONFIRMED` if read as "the identity survives for mode-projected energy ratios" — it does not,
  in either my computed case (`−4.3 × 10⁻⁴` diagonal, `−9.5 × 10⁻⁴` with outgoing cross terms) or the
  source's own tables (`0.12`–`1.12`).
* The sentence should say which of the two it means; as written the reader will take it as the second.

Note that live `EQ-10.12` already carries the right qualifier ("lossless limit only; mode-wise use
requires cross-term accounting"), so the §9.7 prose is looser than the register it summarises. That is a
**consistency** finding about the manuscript, not an addition to the 229-statement count.

## 4. Evidence / sources

* `V-B3d_coupled-interface-rta.md` §3.2 (table row `4.46 × 10¹¹ Hz`), §3.3, §3.4 — frozen at `ff1c472`;
  the `D₁`/`D₂` dissipation-integral checks closed to `10⁻⁶`–`10⁻⁵`, which is what makes the three
  `R` values trustworthy.
* Barak et al. (2023), *Sci. Rep.* **13**, DOI `10.1038/s41598-023-44339-5`, gold OA, access 2026-10-22,
  publisher PDF: eqs (53), (57), (58) and the tabulated values printed beneath Figs 2–9 (incident `P`).
  Access level: **FULL** for those equations and tables.
* Barak, R. Kumar, R. Kumar, Gupta, *J. Therm. Stresses* — `E_int` lumping (`²½τ_q²D_s²` plus `E_int`)
  as reported second-hand by the supervisor (F9); that primary was not read in this session.
* `V-B9a_checks.py` CHECK 5 (source tables) and CHECK 6 (`A = 1 − R − T` is a tautology).

## 5. Checks done

1. Used a **frozen, independently verified** numerical case rather than a new hand calculation; the case
   already contains a dissipation-integral validation.
2. Identified the physical origin of each deficit (incident–outgoing vs outgoing–outgoing) instead of
   reporting a single residual.
3. Tested the **lossless limit** as a control: all three definitions coincide to `6.7 × 10⁻¹⁶`, so the
   cross terms are indeed `∝ Im k`, not numerical error.
4. Checked what the cited source's `E_int` is *defined* as (pairwise transmitted products) before
   comparing it with my `E_int`-equivalent (which is a reflected-side interference term) — they are not
   the same object, and the file says so.
5. Gave the §9.7 sentence two scoped readings rather than one global verdict (no-WRONG rule: the
   sub-system is stated in §3.4).

## 6. Confidence

* The three `R` values and the two deficits: **HIGH** (frozen, reproducible, validated by an independent
  dissipation integral).
* "Cross terms = attenuation, vanishing for real `k`": **HIGH** (control case).
* That the source's printed tables violate its own eq (58): **MEDIUM-HIGH** — the numbers were read from
  the publisher PDF's figure tables, which are 2-significant-figure plot data; a 0.12 vs 1.00 gap is far
  outside that precision, but the individual digits are not authoritative.
* Generality beyond the two tested systems: **MEDIUM**. Both are passive, perfectly bonded, planar
  interfaces; a graded or lossy interface layer would add a genuine `A ≠ 0`, which neither case covers.

## 7. NOT verified / open issues

* `E_int` values were **not re-derived** from the source's eq (57); I used the paper's printed numbers.
  Re-deriving them would need the 7×7 system of eq (44) and the material table, which is a separate job.
* The `E_int` of the source (pairwise between **transmitted** modes) and the cross-term deficit in
  `V-B3d` (incident–reflected interference on the **reflected** side) are different objects. I did not
  construct a case where both appear together; that would be the clean test of eq (58) and is not done.
* Only **one** `V-B3d` frequency row is analysed in detail (the strongly coupled one). The trend across
  all rows (deficit `10⁻¹⁰` at `10⁶ Hz` growing to `8.6 × 10⁻⁴` at `10¹¹ Hz`) is in `V-B3d` §3.2 and is
  consistent, but I did not re-tabulate it here.
* §9.7's "limit is worth recording" paragraph (graded interfaces) is untouched: no claim there was
  tested.
* Whether the *live* manuscript's §10 or §9 anywhere defines `T` for the flux consistently is covered in
  `V-B9b`, not here.
