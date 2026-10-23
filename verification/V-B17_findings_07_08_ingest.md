# V-B17 — findings 07 and 08 ingested; MGT stability wording separated; readiness table

**Batch:** B17. **Date:** 2026-10-23. **Input read in full:** `control/FULLTEXT_FINDINGS_08.md` (F23–F27) and `control/FULLTEXT_FINDINGS_07.md` (F19–F22), `origin/claude/control` @ **`3f6efa8`** (explicit refspec `refs/heads/claude/control:refs/remotes/origin/claude/control --force`).
**No manuscript edit.** This repo still holds no `.tex`; every fix below is a report to the authors.

---

## Task

1. Add F23–F27 fact rows (Caputo 1967, Sherief 2010, Wang & Li 2021 (I), Lasiecka & Wang 2015, Dell'Oro–Lasiecka–Pata 2016, Shakeriaski 2021), plus the still-missing F19–F21 rows (Quintanilla 2019, Bazarra 2021, Mindlin 1974).
2. Plan: Caputo and Sherief → s.11 eligible; `LIT-0040` → s.12 secondary survey; Lasiecka–Wang and Dell'Oro et al. → s.4.9/4.10 for their PDE results; Wang & Li (I) → s.11 conceptual; Quintanilla and Mindlin → s.4.9/4.10 and s.5. Remove all of these from `PDF_REQUEST_LIST_3`.
3. Mark the MGT stability condition `gamma = b - tau c^2` as **acoustic-form-only** in the ledgers.
4. Update the gap list (close what closed) and produce `REFERENCE_READINESS.csv` — eligible sources per section, before/after.

## Method

- Both findings files read end to end; every equation transcribed from the supervisor's text into the facts rows, with the transcription route stated (supervisor page render / OA copy). **I opened none of these papers.**
- Read levels: `PRIMARY-SOURCE-CHECKED (supervisor …)` where the supervisor read the printed equation, `SECONDARY-SOURCE` for the survey, and the phrase "NOT opened by this verifier" in every row that did not come from my own reading.
- Plan rows edited one field at a time through `csv.DictReader`/`DictWriter`; new rows appended with their `lit_id` checked against the existing set first.
- Ledger corrections were appended to `note` (never by rewriting history) and the one genuine verdict change is called out below.
- Baseline for the readiness table is the R3 report (`arena/b5e608f8-le` @ `3092fa3`), whose numbers count rows that were **Crossref-verified and technically eligible** — a different measure from "plan row marked YES", which the new CSV states explicitly.

## Result

### 1. Facts (116 → 125; nine rows added or updated)

| key | source | what was recorded |
|---|---|---|
| `Caputo1967` | F23 | definition (5), reconstructed from the proof page (display not legible); Laplace transform (6); **operator born in viscoelasticity, not heat conduction**; fitted order ≈ 0.15 |
| `Sherief2010Fractional` | F24 | (2.29) fractional flux; (2.37) energy with the operator on **both** temperature rate and coupling; α→1 gives LS, α→0 gives Biot with `k' = k/(1+τ₀)` |
| `WangLi2021I` | F25 | Definition 1 (eq 1); MDD-vs-FD conceptual argument; **no thermoelastic equations at all** |
| `LasieckaWang2015MGT` | F26 | abstract acoustic MGT with memory, eq (1); decay follows the kernel; γ > 0 as relayed (extraction garbled — flagged) |
| `DellOroLasieckaPata2016MGT` | F26 | abstract equation; subcritical `αβ > γ` exponential, critical `αβ = γ` exponential **iff A bounded** |
| `Shakeriaski2021Survey` | F27 | 21 pp, ~142 refs, six tables; tables 1–5 by geometry, table 6 classification; GL changes constitutive laws, LS the energy equation; **no MDD/MGT/nonlocal sections** |
| `Quintanilla2019MGT` | F19 | (1.3), (2.4), (2.5), (3.5); `K_ij = k_ij − τ k*_ij`; 3-D ellipticity (2.8)/(2.9); 1-D `k > τk*` stable, `k < τk*` unstable (Thm 4.7, Sec 5) |
| `Bazarra2021MGTradial` | F20 | second MGT variant with τ inside the **stress** law; `k̄ = k − τk* > 0`; radial decay |
| `Mindlin1974Thermopiezo` | F21 | balance laws; **Fourier** law `h_i = −K_ij θ,j`; Gibbs-function constitutive form; reduced 5-unknown system; energy principle |

Base rows added for the four papers that had none: `LIT-0511` Sherief 2010, `LIT-0512` Mindlin 1974, `LIT-0513` Bazarra 2021, `LIT-0514` Lasiecka–Wang 2015, `LIT-0515` Dell'Oro–Lasiecka–Pata 2016. DOIs for 0511–0515 were each resolved at OpenAlex this session (Sherief bronze OA; Bazarra green, UPCommons 2117/341851; Lasiecka–Wang bronze; Dell'Oro bronze, authorship confirmed as Dell'Oro/Lasiecka/Pata).

### 2. Plan (206 → 211 rows)

- `LIT-0035` Caputo → **s.11**, `technical_claim_eligible=YES`, grade A, and **moved out of s.4.11**. s.4.11 is the fractional-hereditary subsection and cites this same row; the plan keeps one row per source, which is why s.4.11 now shows no row of its own — stated in the row and in GAP-25 rather than left to look like an omission.
- `LIT-0511` Sherief 2010 → **s.11**, YES, grade A.
- `LIT-0040` Shakeriaski → **s.12**, YES, grade B, `role = comparative survey (SECONDARY)`; explicitly **not** citable for equations, numbers or stability claims, and its borrowed `MPL < GN-III < LS` ordering must be attributed onward.
- `LIT-0448` Wang & Li (I) → **s.11** (was s.6), YES, conceptual only; the note records that s.6 loses the row.
- `LIT-0514`, `LIT-0515` → **s.4.9** (PDE results), grade B (abstract-level); `LIT-0513` → **s.4.9** with s.4.10 noted; `LIT-0041` Quintanilla keeps s.4.10 and gains s.4.9 for its PDE side.
- `LIT-0512` Mindlin 1974 → **s.5**, YES, grade A.

### 3. The MGT stability condition — one verdict change and one correction

- **`EQ-050` → `CORRECT`** (was `UNCLEAR`). This is the manuscript's MGT constitutive display (`τ q̇ + q = −kT_{,i} − k*ϑ_{m,i}`, `ϑ̇_m = T`). My earlier note said "the equation is not MGT (MGT carries q-dot)" — **that was wrong**: the display does carry `τ q̇`, and it is Quintanilla's (2.4) up to his sign convention (his `q` is minus the usual heat flux). Upgraded for the constitutive form and the 1-D decay/instability dichotomy only, **not** for 3-D rates. Confidence LOW → HIGH.
- **`gamma = b − τc²` marked `ACOUSTIC-FORM-ONLY`** in three places: notes on `EQ-050`, `EQ-168` and `EQ-173`; a correction block inside `V-B3a_energy-balance-interface-flux.md`; and the banner/comment in `V-B2_wave_speeds.py`, which now says the block tests the acoustic form and its output must not be quoted for thermoelastic MGT. The printed thermoelastic condition is `K_ij = k_ij − τk*_ij ≻ 0`, i.e. `k > τk*` in 1-D.
- Two model families are now kept apart in writing: **acoustic** (Moore–Gibson PDE; `αβ ≷ γ`) and **thermoelastic** (Quintanilla; `k ≷ τk*`). F26's own wording says not to mix them; the facts rows for both MGT papers say so independently.

### 4. Gaps

| gap | new status |
|---|---|
| **GAP-25** (s.4.11 Caputo) | **CLOSED** — Caputo supplied and read (F23), plan row eligible |
| **GAP-24** (s.4.9 had no plan rows) | **CLOSED as a labelling defect** — three s.4.9 rows, all eligible; the six-source bar is still not met |
| GAP-09 (fractional) | **partly closed** — Caputo + Sherief in hand; Povstenko and Gorenflo/Luchko still missing |
| GAP-21 (s.11) | **partly closed** — three new eligible sources |
| GAP-18 (s.5) | **partly closed** — Mindlin 1974 read (1 of 6); Eringen, Cowin/Nunziato, Iesan, Mindlin 1961, Tiersten still missing |
| GAP-22 (s.12) | **still open** — one eligible (secondary) source of six |
| GAP-17/19/20/23 | unchanged |

### 5. `REFERENCE_READINESS.csv` (21 rows; one per section plus TOTAL)

Interesting columns: `r3_baseline_eligible` (R3's Crossref-verified count), `eligible_now` (plan rows marked YES), then the honest split — `eligible_full_or_primary`, `eligible_partial_abstract`, `eligible_metadata_only`.

| section | R3 | now | full/primary | partial | six-source bar |
|---|---:|---:|---:|---:|---|
| 4.9 | 0 | 3 | 3 | 0 | no |
| 4.11 | 0 | 0 (cites s.11) | — | — | no |
| 5 | 3 | 5 | 4 | 1 | no |
| 8 | 1 | 1 | 1 | 0 | no |
| 10 | 0 | 4 | 3 | 1 | no |
| 11 | 2 | **10** | **9** | 1 | **YES** |
| 12 | 0 | 1 | 1 | 0 | no |
| 13 | 1 | 11 | 1 | 10 | YES (but 10 of 11 are abstract-level) |
| **TOTAL** | 55 | 96 | 68 | 27 | 6 of 21 |

The table is deliberately unflattering: `eligible_now` counts YES rows whatever the read level, so the full/partial split is what a section can actually lean on. Section 13 "meets the bar" only because ten abstract-level reads count as eligible-at-grade-B, and the CSV says so in the note column.

## Evidence / Sources

- `control/FULLTEXT_FINDINGS_07.md` F19–F22 and `control/FULLTEXT_FINDINGS_08.md` F23–F27, `origin/claude/control` `3f6efa8`, read 2026-10-23.
- OpenAlex records (2026-10-23) for `10.1016/j.ijsolstr.2009.09.034`, `10.1177/1081286521994258`, `10.1016/j.jde.2015.08.052`, `10.1016/j.jde.2016.06.025` (authorship confirmed: Dell'Oro, Lasiecka, Pata), `10.1016/0020-7683(74)90047-X`, `10.1111/j.1365-246X.1967.tb02303.x`.
- Local: `FULLTEXT_FACTS.csv` (125), `LITERATURE_BASE.csv` (515), `REFERENCE_PLAN.csv` (211), `REFERENCE_GAPS.csv` (25), `EQUATION_LEDGER.csv` (176), `REFERENCE_READINESS.csv` (21), `PDF_REQUEST_LIST_3.md`.

## Checks done

- **Identity before insertion:** every new `lit_id` checked against the base (0511–0515 were free); the two Shakeriaski papers kept as **separate** facts rows (`Shakeriaski2021ModGL` vs `Shakeriaski2021Survey`) because they are different papers.
- **Verdict discipline:** `EQ-050`'s flip is argued from the display itself plus a primary source; no other verdict moved. Each MGT row now names which of the two model families it is talking about.
- **Self-correction recorded in place:** the withdrawn `gamma = b − τc²` claim is left visible in `V-B3a` inside a correction block rather than silently deleted, and the script banner says the same.
- **Plan integrity:** 211 rows, no duplicate `lit_id`, 14 columns; s.4.11's zero rows explained rather than hidden.
- **Two MGT variants documented:** F19 (no τ in stress) and F20 (τ in stress) are both recorded, so "the MGT model" cannot be used unqualified in the review.
- **Read-level honesty:** nine of the nine new facts rows are supervisor-read and say "NOT opened by this verifier"; none claims FULL by me.

## Confidence

- **HIGH** for the transcriptions themselves as *records of what the supervisor relayed* — they are entered verbatim in substance, with the caveats the findings themselves carry (Caputo's (5) reconstructed; Lasiecka–Wang's γ condition garbled).
- **HIGH** that `EQ-050` is the MGT constitutive law: the display carries `τq̇` and matches (2.4) up to sign.
- **HIGH** that the acoustic and thermoelastic conditions are different and must not be merged.
- **MEDIUM** for the PDE statements (abstract-level only; no theorem numbers for the critical case were relayed).
- **LOW** for any numerical claim from these papers — no numbers were transcribed.

## NOT verified / open issues

1. **I did not open any of these seven papers.** Everything is `PRIMARY-SOURCE-CHECKED` at team level, `SECONDARY`/relayed from my side.
2. **Caputo's definition (5)** was reconstructed from the proof page; the display itself was illegible. If the review quotes the definition, someone must re-read that page.
3. **Lasiecka–Wang's γ > 0** was garbled in extraction; the facts row says do not quote the exact form without re-reading page 1.
4. **Quintanilla's internal inconsistency** ((2.1) `α,j` vs (2.5)/(3.5) `θ,j`) is recorded but unresolved — the authors must say which form they quote.
5. **Sections 5, 8, 10 and 12 are still below six sources**; only 4.8, 6, 7, 9, 11 and (nominally) 13 clear the bar.
6. **The manuscript changes are the authors'**: s.11 must name the fractional convention, s.4.9/4.10 must separate acoustic from thermoelastic MGT, s.5 should add the Mindlin Fourier limit, s.12 must mark the survey as secondary.
