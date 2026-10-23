# V-B10e — Promotion of four tier-3 files to tier-2 reading

| field | content |
|---|---|
| **Task** | Promote `DRV-0319`, `DRV-0321`, `DRV-0325`, `DRV-0348` from tier-3 (metadata only) to tier-2 full-text reading under the standing tier-2 rules, i.e. one `FULLTEXT_FACTS` row per paper recording the law as printed, equation numbers, printed stability/ordering statements, the energy-ratio definition if any, and the conflict with the manuscript. |
| **Deliverable** | four rows appended to `verification/FULLTEXT_FACTS.csv` (96 → **100**); four records appended to `verification/LITERATURE_BASE.csv` (**LIT-0496–LIT-0499**, 495 → **499**); tier and read level updated for the four rows in `verification/DRIVE_PRIORITY.csv`. |
| **Method** | re-downloaded from the Drive ids recorded in `DRIVE_TIER3_METADATA.csv`, copied to `/tmp`, text extracted with PyMuPDF, read in the extracted text; equation numbers are the printed numbers, not reconstructed. PDFs deleted before the commit. |
| **Result** | two genuine corrections to the manuscript's sourcing, one printed counter-example, and one printed ordering that the manuscript currently asserts without a source. Details below. |
| **Confidence** | HIGH on all four: equations read in the text layer, numbers quoted as printed, and every negative statement (no energy ratio, no admissibility) is a full-text search result, not an impression. |

## 1. What each paper actually contributes

**`DRV-0319` — Huang, Yan, Wu & Yu 2025, *Appl. Math. Mech.* **46**(8), 1533–1550, `10.1007/s10483-025-3280-7` → LIT-0496.**
The paper builds CV and GN as *thermal networks*: a thermal-elastic unit and a thermal-viscous unit in series (CV, eq. 5) or in parallel (GN, eq. 8). Six MCV and four MGN networks then produce flux laws of **second order in time**, e.g. `q + 3τq̇ + τ²q̈ = −k∇T − kτ∇Ṫ` (21) and a family carrying `∇T̈` (40, 43).

This matters more than it looks. In an *exact* derivation from a unit network the coefficient of `q̈` is **τ²**, not `τ_q²/2`. The `τ_q²/2!` that the manuscript (§4.8) and half the literature use is a Taylor-truncation artefact. The manuscript may keep the truncation — it is a legitimate convention — but it cannot present `τ_q²/2!` as the natural or unique second-order coefficient while this paper exists in its own reading list. No ordering, no admissibility, no energy ratio.

**`DRV-0321` — Yu, Wu & Deng 2024, *Acta Mech. Sin.* **40**, 423419, `10.1007/s10409-023-23419-x` → LIT-0497.**
Fractional thermoelasticity from anomalous conduction, organised as a **general operator map** `F_q q = F_θ ∇θ` (33) with seven models in Table 2 (fractional CV I–IV, fractional GN I–III) and their Laplace forms in Table 3. This is a *third* route beyond DPL, distinct from Taylor truncation in time and from integer higher-order flux laws (the latter is `DRV-0014`, already read). §4.11 should either present all three routes or say which one it presents.

**`DRV-0325` — Srivastava & Mukhopadhyay 2026, *Arch. Appl. Mech.* **96**, 107, `10.1007/s00419-026-03092-7` → LIT-0498.**
TRDTT piezothermoelasticity. Two printed facts the manuscript currently lacks:

* the two-temperature relation itself is **rate dependent**, `A_ij φ,_ij = (1 + t₁∂/∂t)φ − (1 + t₁∂/∂t)θ` (6) — the GL relaxation sits *inside* the 2TT relation;
* the relaxation ordering **`t₁ ≥ t₂ > 0` is printed as a standing assumption** immediately after eq (8), next to `ρ > 0` and the positivity of the elastic tensor.

And one structural point: the flux law is plain Fourier in the conductive temperature, `−k_ij φ,_i = q_i` (5), with **no relaxation on the flux**. The hyperbolic character comes from the energy equation and the 2TT relation. That is a fourth distinct placement of the relaxation time, and it belongs in the §6 discussion that currently distinguishes "relaxation on the flux" from "relaxation on the temperature".

**`DRV-0348` — Hu, Wang & Ding 2000, *Rep. Prog. Phys.* **63**, 1–39 → LIT-0499.**
The canonical quasicrystal elasticity framework that batch 6's eight-file quasicrystal sub-corpus assumes but never states: phonon and phason strains, `F` expanded to second order (4.12), conjugate stresses (4.25), generalized Hooke law `T = C:E + R:W`, `H = Rᵀ:E + K:W` (4.26–4.27), and Table 1 giving independent-constant counts per Laue class (1D triclinic 21/6/18 = 45). It is **isothermal**: it cannot support a phason-damping or thermoelastic claim, and the row says so.

## 2. What the four promotions do *not* give

* **No energy ratios.** All four were searched for energy-ratio content; none defines one. Only one paper in this whole stretch of reading (`DRV-0179`, already in `FULLTEXT_FACTS.csv`) prints an interface energy identity.
* **No admissibility.** `DRV-0319` prints no restriction on its second-order coefficients; `DRV-0321` prints none on the fractional orders. The only printed ordering found in this batch is §4.4's `t₁ ≥ t₂ > 0` in `DRV-0325`.

## 3. A duplication I have to own

Before starting the promotions I re-downloaded eleven files (`DRV-0176`–`DRV-0190`) that I believed were still unread. They were not: **B07 (commit `f6c3142`) had already read all of them** and already wrote the ten facts rows and the base rows LIT-0470–LIT-0477. My session notes did not carry B07's content forward, so I repeated the download.

It was not wasted, because it turned into an independent second reading: I re-derived `DRV-0177` eq (4) (hyperbolic 2TT), `DRV-0178` eq (9), `DRV-0179` eq (79)–(80) (the exact unity identity with its interaction term), `DRV-0182` eqs (8)–(9) (the explicit "second order in τ_q, first order in τ_θ and τ_v" statement plus the `0 ≤ τ_v < τ_θ < τ_q` ordering), `DRV-0185` eq (2) (`k*` form, no energy ratios), `DRV-0186` eqs (14)–(15), `DRV-0187` eq (11), `DRV-0188` eqs (14)–(15) and `DRV-0189` eqs (1)–(3) — and every number agreed with what B07 recorded. No new facts rows were written for them; no rows were duplicated. The lesson for the next session is written into the plan: **check `FULLTEXT_FACTS.key` before downloading anything.**

## 4. Checks done

1. Duplicate check by DOI against all 495 pre-existing base rows before appending — all four were absent, so four new rows were created rather than four rows upgraded.
2. `FULLTEXT_FACTS` keys checked against the existing 96 — no collision.
3. Every "none printed" claim is a full-text regex search over the extracted text (`Taylor`, `truncat`, `well-posed`, `ill-posed`, `entropy`, `energy ratio`, `energy flux`, `thermodynamic`), not an absence of memory.
4. Equation numbers transcribed from the text layer and spot-checked against the surrounding prose.
5. Row width asserted equal to header on write; `inv_id` uniqueness re-asserted on `DRIVE_PRIORITY.csv`.
6. No PDF, no extracted text and no long quotation entered the repository.

## 5. NOT verified / open issues

* `DRV-0348`: sections 5 (dislocation theory) were skimmed only; the row says "FULL for secs 1–4".
* `DRV-0319`: the numerical section was not read; no claim in the row depends on it.
* `DRV-0325`: dated 2026 in the printed volume (received 2025, revised March 2026, accepted April 2026). I take the printed date; I did not check whether the issue is formally assigned.
* `DRV-0348` carries **no DOI** on the retrieved copy (PII printed instead), so LIT-0499 has an empty DOI field by design, not by omission.
* Promotion to the base changes the denominator used in earlier self-citation arithmetic: the base is now **499**, not 495.
