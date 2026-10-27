# B23 — Independent adversarial verification

- **Audited commit:** `4caa9a89d68b058aca6a340704242b08b5498a2a` (branch `arena/b5e608f8-le`, fetched as `FETCH_HEAD`, extracted read-only to `/home/user/b23_src`)
- **My branch:** `arena/0be2770f-le` — this audit writes only under `verification/B23_*`
- **Date of checks:** 2026-10-27
- **Source set used:** 19 primary PDFs (18 from the B14/B23 source set + Kumar–Kansal 2017 retrieved from CMST), the 122-page build PDF, all TeX sources, both ledger CSVs, and Crossref live queries
- **Result:** **P0 = 0, P1 = 2, P2 = 7, INFO = 4**

---

## 1. P0 / P1 first

### P0 — none

### P1-1 (NEW) — classical energy-balance identity is missing the advective energy flux

**Location:** `phase5/master/sections/sec03_foundations.tex:315–355` (printed Eqs. 3.28–3.30); repeated wording in `phase5/scripts/verify_classical_flux.py:47–52`

Eq. (3.28) is printed as an *exact* identity:

```
∂/∂t (½ρ v_i v_i + ρ e) + ∂/∂x_j (q_j − σ_ji v_i) = ρ f_i v_i,     J_i = q_i − σ_ij v_j
```

and (3.30) then integrates it over a fixed volume and states total-energy conservation for an isolated system.

The mechanical power balance (3.12) and the internal-energy balance (3.14) are written with **material** derivatives
(`ρ d/dt(½v_i v_i) = …`). Converting a material derivative to the Eulerian form requires mass conservation:

`ρ Dφ/Dt = ∂_t(ρφ) + ∂_j(ρφ v_j)`.

So the correct fixed-volume statement carries the advective flux `ρ(½|v|² + e)v_j`:

```
∂_t(ρ(½|v|²+e)) + ∂_j( q_j − σ_ji v_i + ρ(½|v|²+e) v_j ) = ρ f_i v_i + ρ r
```

**Verified symbolically** in `verification/B23_verify_balance.py`: with the three printed balances imposed, the conserved form has residual 0, and the printed short form has residual exactly `−div[ρ(½|v|²+e)v]` (nonzero for any medium with `v ≠ 0` and non-uniform `E`).

**Why this is P1 rather than P2.** (3.28)–(3.30) are headline equations of Section 3 and the stated basis of the Section 10 flux programme. The omission is harmless at first order in the small-amplitude expansion (the advective term is O(v³, v²e)) and does not change any Section 9/10 harmonic result, but as printed the identity is exact-claim wording with a term missing.

**Second half of the finding — the audit could not catch it.** `phase5/scripts/verify_classical_flux.py` prints
`PASS: local balances imply E_dot + div(q - sigma*v) = rho*f.v + rho*r`, but it never forms `∂_t`, `div` or the velocity field: it asserts
`energy_rate + flux_divergence − body_power − heat_source == 0` where `energy_rate` was itself defined as that same expression. It is a definition-level tautology, so it cannot detect a missing term.

**Fix:** (a) in (3.28)–(3.30) either add `ρ(½|v|²+e)v_j` to the flux, or restrict the equations to a material volume / linearised small-amplitude setting and say so; (b) rewrite `verify_classical_flux.py` to build the field identity as in `B23_verify_balance.py` (or delete the PASS line).

### P1-2 (NEW) — the handler's evidence list does not exist in this repository state

The brief asks for “all class-A rows promoted since B22 with `evidence_mode` FRESH-READ dated 2026-10-27, ~20 rows”.
Recomputing from `phase5/reports/OPEN_CLAIMS_LEDGER.csv` (499 rows; columns `ledger_row_id, section, tex_file:line, old_text_short, class, what_was_changed, needed_source, resolved_by, evidence_mode` — there is **no** `status` or `ocl_id` column):

- rows whose `evidence_mode` contains `2026-10-27`: **4** — `OCL-195`, `OCL-207`, `OCL-404`, `OCL-405`;
- class counts: **A 48 / B 123 / C 310 / V 18** (matches `validate_claim_ledger.py`);
- rows with an empty `resolved_by`: **383**.

I therefore audited the named focus list (16 rows) plus those 4 fresh-read rows. Of the 4, **none** of the cited sources (Mindlin 1974, Kumar et al. 2023 *Phys. Scr.*, Biot 1956, Barak et al. 2023) exists in the accessible source set or in the Drive corpus (`search_files` for Mindlin/Biot returns 0 hits), so they are **NOT-CHECKABLE** here and rest on the internal note `phase5/reports/R4B_SOURCE_FINDINGS.md:129–141,329`.

**Fix:** publish the actual `evidence_mode` filter used to build the promotion list, and state in the ledger which rows have an externally re-openable source.

### P2 — seven items

| # | Item | Location | Fix |
|---|---|---|---|
| P2-1 | Eight bib entries carry `\&amp;` and print literally as “Heat **&amp;** Fluid Flow” / “Computers **&amp;** Mathematics …” | `references_local.bib:841, 857, 1316, 1537, 1565, 1620, 1715, 2119`; printed pp.114–119 | replace `\&amp;` with `\&` |
| P2-2 | T2 reduction row cites “Eq. (4.17)'s first-order expansion”, but no first-order expansion of the TPL law is displayed (printed (4.17) is the unexpanded phase-lag form) | `tables/source/T2_reduction_map.tex:18`; `sec04_thermoelastic.tex:180–188` | print the first-order TPL residual, or cite the DPL residual plus “expand (4.17) to first order” |
| P2-3 | Internal artifact references in print: work-package tag “V-B3d”, “The saved audit reports …”, and “the accompanying verification script” with no pointer | printed p.66, pp.69–70 | drop the tag; name the script path in a footnote or drop the sentence |
| P2-4 | `P_i, P_r, P_t` in Eq. (105) are defined only as “positive power magnitudes per unit area at remote planes”; a reader cannot reconstruct them from the printed flux | `sec10_energy.tex:96–112`, printed p.69 | define `P_i = ⟨J·n⟩` at the stated reference plane, with sign orientation |
| P2-5 | Crossref gaps: `Das2026` and `Maranganti2006` have no page in Crossref (bib page fields unverifiable); `Eringen1966a` has an empty Crossref title | `references_local.bib` | mark the two page fields as article-number/`verified={NO}`; leave Eringen as `ARBITRATED` |
| P2-6 | `MISSING_SOURCES.csv` is stale: all six listed leads now resolve by DOI (and Eringen 1966 + Chadwick–Sneddon 1958 exist as scans in the B14 set) | `phase5/reports/MISSING_SOURCES.csv` | re-date or narrow the “not located” wording |
| P2-7 | Four class-A rows promoted on 2026-10-27 rest on sources that are absent from the delivered source set (Mindlin 1974, Kumar 2023 *Phys. Scr.*, Biot 1956, Barak 2023), so they are not independently re-openable | `OPEN_CLAIMS_LEDGER.csv` OCL-195/207/404/405 | ship the four PDFs with the source set, or flag the rows as internal-evidence-only |

---

## 2. Item 1 — source-vs-`resolved_by` (26 rows)

Machine-readable table: `verification/B23_LEDGER_AUDIT.csv`.
Verdicts: **CONFIRMED 16 · WRONG 0 · OVERSTATED 0 · NOT-CHECKABLE 4 · NOT-APPLICABLE 6**.

| OCL | Class | Printed claim | Source anchor claimed | Verdict | What I actually read |
|---|---|---|---|---|---|
| 046 | A | sec04 DPL baseline | Dell'Oro–Lasiecka–Pata 2016 p.1; pp.5–6 Eq. (1.7) | CONFIRMED | p.1 identity/DOI; Thm 1.1 + (1.6) p.5; (1.7) p.6 |
| 143 / 144 | A | sec04 GL law | Green–Lindsay 1972 p.5 (4.3)–(4.7) | CONFIRMED | p.5 page image: (4.3)–(4.12) present, no `q̇` law |
| 145 | B | sec04 GL flux | GL 1972 p.5 (4.6), (4.8)–(4.11) | CONFIRMED | p.5: temperature-rate flux law present; row correctly held at B |
| 174 | A | sec04 MGT | Quintanilla 2019 p.3 (2.4)–(2.5); p.4 (3.1) | CONFIRMED | p.3 relaxed flux + MGT equation; p.4 (3.1) |
| 175 | A | sec04 MGT stability | Quintanilla 2019 p.3 (2.8)–(2.9); p.9 Thm 4.7; p.10 (5.8) | CONFIRMED | (2.8)/(2.9) p.3; Theorem 4.7 p.9; Λ₂ = n²/c(τ⁻¹k − k*) < 0 p.10 |
| 078 | A | sec10 surface-wave flux | Ivanov–Savova 1991 p.564 | CONFIRMED | p.564: flux not parallel to surface, depth variation, exponential decay |
| 154 / 155 | A | sec04 GN-II/DPL | GN 1993 printed p.202 (3.15)–(3.17) | CONFIRMED | printed p.202 (PDF p.14): (3.15)–(3.17), §4 uniqueness |
| 259 | A | sec07 nonlocal | Lazar–Agiasofitou 2022 p.10 (29)–(31); p.12 (39)–(40) | CONFIRMED | (29) `L t_ij = σ_ij`; (30) `L` on inertia + body force; (39)/(40) Klein–Gordon |
| 406 | A | T3/§5 void rows | Nunziato–Cowin 1979 p.177 (2.7)–(2.12); Cowin–Nunziato 1983 p.125 | CONFIRMED | p.177: mass, linear & angular momentum, equilibrated force, energy, entropy inequality; 1983 p.125 abstract |
| 407 | A | T3/§5 Iesan row | Iesan 1986 pp.67/70/71/72 | CONFIRMED | p.70 (2.14) void-volume deviation + (2.18)–(2.19); p.71 (2.22); p.72 (2.28) |
| 408 | A | T3/§5 micropolar | Tauchert–Claus–Ariman 1968 pp.37–38 | CONFIRMED | p.37 (2.1) balances incl. Clausius–Duhem; p.38 kinematics + micro-inertia `J` |
| 446 | B | sec08 | Marotti de Sciarra 2013 p.1 abstract | CONFIRMED | p.1 abstract; printed text stays at identification level |
| 448 | C | T5 row | Hughes 1980 printed p.1413 | CONFIRMED | p.1413 abstract; generic FE row correctly citation-free |
| 063 | B | sec08 | Chadwick–Sneddon 1958 title/DOI only | CONFIRMED | printed text asserts title-level identity only |
| 195 / 207 / 404 / 405 | A | §5, T3 | Mindlin 1974; Kumar 2023 *Phys. Scr.*; Biot 1956; Barak 2023 | NOT-CHECKABLE | sources absent from source set and Drive; internal note only |
| 131 / 196 / 197 / 198 / 481 / 485 | B/C | sec02, §5, T2, T6 | — | NOT-APPLICABLE | empty `resolved_by`; printed text is explicitly bounded/absent, so there is no promoted claim to test |

**No WRONG and no OVERSTATED rows found.** Every checked anchor matched the printed page/equation, including the equation *numbers* (this was a common failure mode in earlier rounds).

---

## 3. Item 2 — did the B22 fixes land?

| B22 item | Verdict | Evidence |
|---|---|---|
| F1 Table 23 DPL→LS limit | **LANDED** | `sec12_comparative.tex:107` prints “τ_T→0 with τ_q=τ_0”; `verify_unified_reductions.py` asserts the same row symbolically and asserts the `τ_q→0` wording is *absent* |
| F2 Quintanilla DOI | **LANDED** | bib `Quintanilla2003DPL` DOI `10.1080/713855996`, `verified={NO}`; `CROSSREF_FINAL.csv` 2–9 marks `CONFLICT-UNRESOLVED` |
| F3 interface cross-term is a real field check | **LANDED (substantive)**, see P2-3 for the residual wording | `sec10_energy.tex:148–152` now derives `σ̂_i v̂_r* + σ̂_r v̂_i* = ρ₁c₁²k₁ω[−A_iA_r*e^{2ik₁x} + A_rA_i*e^{−2ik₁x}]` and shows it is purely imaginary. My independent derivation (`B23_verify_interface.py`) gives `−2i A_iA_r c₁²k₁ω sin(2k₁x)`, i.e. the same object, and the time average is exactly zero |
| F4 Eq. (105) incident-flux definition | **LANDED with a P2 residual** | Eq. (105) now reads `R_rem + T_rem + A_bulk,L + A_int + A_bulk,R = 1` with `A_x = D_x/P_i`; the open B22 sub-point `A_int = D_Σ/P_i` is now printed explicitly (`sec10_energy.tex:98`) and `D_L, D_Σ, D_R` are defined in Eq. (107). Residual: `P_i, P_r, P_t` are defined only verbally (see P2-4) |
| F5 appA register gap | **LANDED** | `appA_equation_register.tex:181–184` now carries `EQ-10.13 … EQ-10.16`, and each description matches the printed equation (definitions / summed balance / 1-D fields / 2×2 matching) |
| F6 internal paths in print | **PARTIAL — P2 open** | no filesystem paths or Drive IDs remain anywhere in the 122-page text (full regex sweep, 0 hits), but page 66 still prints the work-package tag “V-B3d” and “The saved audit reports …”, and pp.69/70 say “the accompanying verification script” with no pointer to where that script ships |
| Kumar/KumarKansal split | **LANDED** | `verify_kumar2017_reference_split.py` PASS; CMST page confirms Kumar & Kansal 2017, CMST 23(1):43–56 |
| New open check from B22 (sec10:105 “interaction term in Eq. (80)”) | **CONFIRMED** | Kumar–Kansal 2017, printed Eq. (79) defines `E_RR = Σ_i Σ_j (E_ij − E_ii)` as the interaction share, and Eq. (80) is `E₁+E₂+E₁₁+E₂₂+E₃₃+E₄₄+E₅₅+E_RR = 1`. The manuscript's “model-specific … with an interaction term in Eq. (80)” is accurate |

---

## 4. Item 3 — Arena scripts re-run, plus independent re-implementations

**Arena's scripts, all re-run at `4caa9a8` (12/12 exit 0, all self-reported PASS):**
`phase5/verification/` — `verify_unified_reductions`, `verify_interface_energy`, `verify_interface_mode_counts`, `verify_gn3_source_mapping`, `verify_kumar2017_reference_split`, `verify_q1_notation`, `verify_q3_status_matrix`, `verify_q4_selection_guide`, `verify_reference_hygiene`, `verify_fig12_workflow`;
`phase5/scripts/` — `verify_classical_flux`, `validate_claim_ledger` (499 rows; classes A 48 / B 123 / C 310 / V 18).

**My independent re-implementations (written from the printed equations only):**

| File | What it checks | Result |
|---|---|---|
| `verification/B23_verify_reductions.py` | LS, DPL, TPL, MGT limits, GN-III→GN-II, Caputo order 2, Helmholtz `ξ→0` | 13/13 pass, incl. 2 intentional negative controls |
| `verification/B23_verify_interface.py` | 1-D welded-interface fluxes, cross term, `r`, `t`, `R+T=1`, impedance weighting | pass |
| `verification/B23_verify_balance.py` | symmetric-stress power identity + classical energy identity in 3-D | (i)/(ii) pass; (iii) exposes **P1-1** |
| `verification/B23_verify_counts.py` | ledger counts, cited-key/bib reconciliation, figure mirrors | 105 cited keys / 143 entries / 38 uncited; fig12 source = rendered (identical sha256); 10 step labels |

**Differences found (this is the useful part):**

1. `verify_unified_reductions.py` also asserts **TeX strings** (e.g. that `$\tau_T \to 0$, with $\tau_q=\tau_0$` appears and `$\tau_q \to 0$` does not, that MDD cells contain “Model-dependent”). String assertions break silently on rewording and cannot detect a wrong equation that is correctly described. My version tests only the algebra.
2. My version adds two checks Arena does not perform: **MGT → LS** at `k*=0, τ_m=τ_0` (passes), and the two **negative controls** `TPL(τ_v→0) ≠ DPL` and `TPL(all τ→0) ≠ Fourier` (residuals `k*v_{,i}`), confirming the manuscript is right *not* to claim those substitutions.
3. `verify_unified_reductions.py` builds the TPL law as `dpl + k*(v_{,i} + τ_v v̇_{,i})` — i.e. it silently assumes the first-order expansion of (4.17). That expansion is **not printed anywhere** (see P2-2), so the TPL row is not checkable from the printed text alone.
4. `verify_interface_energy.py` substitutes `A_r` from the reflection law before forming the cross term; mine keeps `A_i, A_r` independent and derives `r, t` from the matching conditions, then proves `R + T = 1` with the `Z₂/Z₁` weight and shows the unweighted `|r|²+|t|²−1 = 4Z₁(Z₁−Z₂)/(Z₁+Z₂)² ≠ 0`. Same physics, one extra falsification test.
5. `verify_classical_flux.py` is definition-level (see **P1-1**); it does not construct the field identity at all.
6. Not independently reproduced (structural claims accepted after reading the scripts): `verify_interface_mode_counts.py` (plane-strain determinant even and degree six), `verify_gn3_source_mapping.py` coefficient map, `verify_fig12_workflow.py` connector geometry (I checked only SVG identity and the ten step labels).

---

## 5. Item 4 — Crossref, 20 fresh + 6 `MISSING_SOURCES`

Raw responses saved (transcribed field-for-field from the Crossref JSON returned to this session; the sandbox has no outbound HTTP, so no byte-exact dump is possible):

- `verification/B23_crossref/raw_batch1.json` … `raw_batch4.json` (20 random bib entries, seed 23, `select=DOI,title,container-title,volume,page,issued,type,score`)
- `verification/B23_crossref/raw_missing_sources.json` (the 6 stale leads)
- `verification/B23_crossref/bib_vs_crossref.csv` (field-by-field comparison)
- Pretty-printed twins `*.pretty.json`

**Result: 20/20 sample DOIs resolve; 6/6 `MISSING_SOURCES` DOIs resolve.** Field differences:

| Key | Finding | Severity |
|---|---|---|
| `Das2026` | Crossref gives volume 22 and **no page**; bib `pages={77}` is unverifiable (article number?) | P2 |
| `Maranganti2006` | Crossref gives no page; bib `pages={014110}` is the article number — plausible but not corroborated | P2 (informational) |
| `Bayones2021` | Crossref issued 2021-04-21, volume 51 pp. 2501–2516 is the 2023 print issue; bib year 2021 is acceptable as online-first | INFO |
| `Eringen1966a` | Crossref **title field is empty** (IUMJ 15:909); title/journal/pages unverifiable from Crossref alone — consistent with the `ARBITRATED`/OCR origin, not an error | P2 |
| `ChadwickSneddon1958` | Crossref author typo “Snedon”; bib already `ARBITRATED`, manuscript correct | INFO |
| `KumarKansal2017` | Crossref title is the long “Reflection and Refraction … with Voids”; volume/pages/year (23(1):43–56, 2017) match the bib | INFO |
| `MISSING_SOURCES.csv` | **stale**: all six rows now resolve by DOI (Gorenflo–Mainardi 1997 `10.1007/978-3-7091-2664-6_5`; Gorenflo et al. 2014 `10.1007/978-3-662-43930-2`; Eringen 1966; Gupta 2023; Chadwick–Sneddon 1958; Green 1991). The “not located” wording should be dated or narrowed | P2 |
| all others | clean (title/journal/volume/pages/year match after normalisation) | — |

**NEW defect found through this comparison (P2-1):** eight bib entries carry a **double-escaped ampersand** `\&amp;`, which prints literally in the reference list:

`Gupta2023IJNMF`, `Gupta2023Energy`, `Sur2025`, `Aldandani2026`, `Das2008`, `Yadav2023`, `Kumar2022`, `Luchko2010`
→ printed as “International Journal of Numerical Methods for Heat **&amp;** Fluid Flow” on **pp. 114–119** and “Computers **&amp;** Mathematics with Applications” on p. 115.

---

## 6. Item 5 — text sweep of the 122-page build

**Process tags / paths / identifiers.** Full 122-page regex sweep for filesystem paths, `.tex/.csv`, `/home/`, Drive IDs, `drive.google`, `docs.google`, TODO/TBD, unresolved `??`: **0 hits**.
Residual hits: `V-B3d` (p.66), “saved audit” (p.66), “verification script” ×3 (pp.69, 70, 77 → see P2-3).

**Verbatim-lift sweep.** 1,222 manuscript sentences of ≥15 words against 17 source PDFs (scanned `eringen1966`, `green1991` excluded — no text layer). Cascade of contiguous word matches at n = 10, 9, 8, 7:

| Max run | Page | Source | Matched string | Reading |
|---|---|---|---|---|
| 10 | 33 | Green–Naghdi 1993 p.202 | “in the absence of heat supply r and body force b” | equation-setup boilerplate, source is cited in the same sentence |
| 10 | 45 | Cowin–Nunziato 1983 (67) | “is the equilibrated stress vector g is the intrinsic equilibrated” | symbol-gloss list, not prose |
| 9 | 59 | Marotti de Sciarra 2013 abstract | “variational formulation in the complete set of state variables” | abstract phrasing reused inside an explicit “X's abstract describes …” sentence |
| 8 | 116 | Gorenflo–Mainardi 1997 | “in fractals and fractional calculus in continuum mechanics” | book title |
| 7 | 24, 25, 69 | GN 1993, Kumar 2017, Ivanov 1991 | “the second law of thermodynamics in the”, “is the specific heat at constant strain”, “savova the energy flux vector connected with” | standard terms |

**Verdict: no sentence-level lift.** Longest contiguous overlap anywhere is 10 words and every instance is a symbol list, a book title, or standard equation-setup wording. Machine-readable list: `verification/B23_ngram_hits.csv` (7 rows total).

---

## 7. Verdict counts

| Domain | CONFIRMED / LANDED | PARTIAL | WRONG / NOT LANDED | NOT-CHECKABLE | N/A |
|---|---|---|---|---|---|
| Item 1 — source vs `resolved_by` (26 rows) | 16 | 0 | 0 | 4 | 6 |
| Item 2 — B22 fixes (7 items) | 5 | 1 (F6) | 0 | 0 | 1 (new check → CONFIRMED) |
| Item 3 — scripts (12 Arena + 4 mine) | 12 PASS / 4 PASS | — | 0 | 3 structural claims not re-derived | — |
| Item 4 — Crossref (26 DOIs) | 26 resolve | — | 0 | 2 page fields unverifiable | — |
| Item 5 — text sweep | 0 lifts | — | 0 | 2 scanned PDFs excluded | — |

New defects raised by B23: **P1 ×2, P2 ×7**. B22's P1 set is closed except the wording residuals listed above.

## 8. Top 5 risks

1. **P1-1** — Eqs. (3.28)–(3.30) state an exact energy-conservation identity without the advective flux `ρ(½v²+e)v`, and the audit script that “verifies” it is a tautology. A referee who checks this equation will find it immediately.
2. **P1-2** — the promotion evidence the brief describes (~20 fresh-read A rows) is not in the repository; only 4 rows match, and 4 of the 4 rest on sources nobody can re-open from the delivered set. Traceability, not content.
3. **P2-2** — the TPL reduction row points at “Eq. (4.17)'s first-order expansion”, which is never printed; the claim is true but only re-derivable by doing the expansion yourself.
4. **P2-1** — eight `\&amp;` escapes print literally in the reference list (pp.114–119): a visible typographic defect in an otherwise clean bibliography.
5. **P2-3/P2-4** — reader-facing loose ends: work-package tag `V-B3d` and “the saved audit reports …” on p.66; `P_i, P_r, P_t` in Eq. (105) defined only verbally, so Eq. (105) cannot be reconstructed from the printed flux.

## 9. Reproducing this audit

```bash
cd verification
python3 B23_verify_reductions.py     # 13/13
python3 B23_verify_interface.py      # fluxes, cross term, R+T=1
python3 B23_verify_balance.py        # P1-1 evidence
python3 B23_verify_counts.py         # ledger/bib/figure counts
# Arena's own scripts (read-only copy at /home/user/b23_src):
cd /home/user/b23_src/phase5 && python3 verification/verify_unified_reductions.py
python3 scripts/verify_classical_flux.py && python3 scripts/validate_claim_ledger.py
```
