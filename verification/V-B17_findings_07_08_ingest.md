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

---

# B18 appendix (2026-10-23) — Laplace-inversion sources, s.8 readiness, GAP-09/12/13, second pass on four items

**Batch:** B18. **Branch:** `arena/04fdf32e-le`, base `288ccc4`. **Control read:** `origin/claude/control` @ **`0be11f2`** (`control/FULLTEXT_FINDINGS_09.md`, F28–F29), fetched with the explicit refspec and read end to end.
**No manuscript edit.** Everything below is a report and a change inside `verification/`.

## Task (the four numbered orders)

1. Put **Dubner–Abate 1968** and **Stehfest 1970** into `FULLTEXT_FACTS`; move them in `LITERATURE_BASE` and in the readiness table (section 8 primary count).
2. Check **Durbin 1974** and **Honig–Hirdes 1984** OA status at Crossref/OpenAlex and add both to `PDF_REQUEST_LIST`.
3. Write the status of **GAP-09, GAP-12, GAP-13**: which source closes each, and whether it is in Drive or on the request list.
4. Second reading pass on the proposed four **s.10 / s.8** items: read only what Drive actually carries, every fact carrying a **page or equation number**.

## Method

- **Identification of the four items (order 4).** The phrase "four s.10/s.8 items" has no single written source in this repo — I grepped every `V-*.md` for "second reading pass", "second pass" and for s.8/s.10 proposals and found no list. So I reconstructed the set from my own readiness table, which is the only place where a count of four exists: `REFERENCE_READINESS.csv` before this batch gave **s.10 = 3 full/primary** (`LIT-0432`, `LIT-0465`, `LIT-0466`) and **s.8 = 1 full/primary** (`LIT-0268`). 3 + 1 = **the four**. `LIT-0490` (De 2020, s.10) is PARTIAL and was **not** in the set. If the authors meant a different four, this paragraph is where to correct me.
- **Read route.** For the first time in this project the PDF text layer was obtained *directly*: `google_drive__download_file` writes the PDF into the sandbox and `pypdf` (installed in-sandbox) extracts page-tagged text. Bash has no route to `drive.google.com` (TLS blocked: `SSL_ERROR_SYSCALL`), so this tool path is the only one. PDFs were extracted **in `/tmp/pdfs`**, and deleted after the facts were written; **no PDF and no extracted text entered the repo**.
- **`google_drive__read_file_text` is not sufficient for long papers**: above roughly 12–14 k characters it returns the head and the tail and drops the middle, which is exactly where a section 6 (energy ratios) sits. That is why the download route was used.
- Bibliographic data (volume/issue/pages, OA verdict) for the four items was re-queried at **OpenAlex on 2026-10-23** in one batched call, and Durbin separately; the Durbin *title* comes from that record, not from memory.
- Facts rows were **edited in place** (one row per paper, per the B10c/B10d rule) rather than duplicated: the `eq_no` cell now carries the page anchor and the second-pass detail.

## Result

### 1. F28 / F29 ingested — two new facts rows, two new base rows, s.8 raised

- Facts rows **`DubnerAbate1968`** and **`Stehfest1970`** added (FACTS 125 → 127). Both are marked **`SECONDARY-SOURCE`** in `status` *and* in `read_level`, with the words "supervisor-transcribed … not opened by this verifier". That is the standing rule for supervisor-relayed material, and it is why I did **not** copy B17's `PRIMARY-SOURCE-CHECKED (supervisor …)` wording (see "open issues" 1).
- Base rows **`LIT-0516`** (Dubner & Abate 1968) and **`LIT-0517`** (Stehfest 1970) added (base 515 → 519 including the two below).
- Plan rows added for both at **s.8**, `technical_claim_eligible=YES` because the equations were transcribed with printed numbers; `evidence_grade=B` because no page render was seen by me.
- `REFERENCE_READINESS.csv`, **s.8 row: `eligible_full_or_primary` 1 → 3**, `eligible_now` 1 → 3, `plan_rows_total` 8 → 12, `delta_vs_r3` 0 → 2. TOTAL row: plan 211 → 215, eligible 96 → 98, full/primary 68 → 70, delta +41 → +43. The s.8 `note` and the TOTAL `note` both carry the caveat that two of the three are supervisor-transcribed.

**What the two papers actually license (from the findings note, transcribed):**

| | what is printed | where it is usable, and its limit |
|---|---|---|
| Dubner & Abate 1968, *J. ACM* **15**(1), 115–123, `10.1145/321439.321446` | eq (3) `Re F(s)` as the cosine transform of `e^{-at}f`; eq (4) cosine inversion integral; eqs (9)–(10) Fourier-cosine coefficients `A(ω_k)=Re F(a+ikπ/T)`; **eq (15)** working formula; eqs (14), (16), (17) error `O(C e^{-aT})`, `aT=10 ⇒ ~1e-5`, and `|f|≤C t^m` | s.8 method only. It samples **Re F on the real axis** and assumes **f real**; the paper's own tests show degradation for oscillatory and step-like `f` (unit step `U(t−25)`, damped sines). Do not present it as validated for a full complex-spectrum wave response. |
| Stehfest 1970, *Comm. ACM* **13**(1), 47–49, `10.1145/361953.361969` | Gaver expectation + Salzer combination; `F_a=(ln2/T)Σ V_i P(i ln2/T)`, **N even**; `V_i` depend on N only; only real-axis `P(s)`, `s>0`, sampled; accuracy rises with N until rounding dominates; Table I: `t^{-1/2}`, `ln t`, `t^3/6` good to ~3–4 digits, `e^{-t}` degrades for `T≥5` with a sign change at `T=8–10` | s.8 method only. The "real-axis sampling suits smooth, monotone responses" sentence is **supervisor inference**, not Stehfest's text — if the review uses it, it must be labelled as inference or dropped. Table I column assignment is **not** render-checked. |

### 2. Durbin 1974 and Honig–Hirdes 1984 — OA status and list position

- **Honig, G.; Hirdes, U. (1984)**, *A method for the numerical inversion of Laplace transforms*, *J. Comput. Appl. Math.* **10**(1), 113–132, `10.1016/0377-0427(84)90075-x` — OpenAlex `oa_status: **bronze**`, and its `oa_url` is the DOI itself, i.e. the publisher copy is free. **Added to Part A of `PDF_REQUEST_LIST_3` as A12**, with the note that the library already uses it (see item 4 below). Base row `LIT-0518`, plan row s.8, `technical_claim_eligible=NO` (metadata only).
- **Durbin, F. (1974)**, *Numerical inversion of Laplace transforms: an efficient improvement to Dubner and Abate's method*, *Comput. J.* **17**(4), 371–376, `10.1093/comjnl/17.4.371` — OpenAlex `is_oa: false`, `oa_status: **closed**`, `any_repository_has_fulltext: false`. **Added to Part B as B21.** Base row `LIT-0519`, plan row s.8, `technical_claim_eligible=NO`.
- List arithmetic after the batch: A6 and A7 moved into **Part A0** (supplied, F28/F29), A12 and B21 added ⇒ **still 29 outstanding, but now 3 open access / 21 paywalled / 5 print** (was 4 / 20 / 5). Part A0 now holds 8 items. GAP-19's coverage line rewritten.

### 3. GAP-09, GAP-12, GAP-13 — who closes each, and where that source is

All three were checked the same way: `DRIVE_INVENTORY.csv` grepped case-insensitively for the author or the work (370 rows, 371 lines). **Zero rows** for `povstenko`, `mainardi`, `gorenflo`, `luchko`, `achenbach`, `nowacki`, `durbin`, `honig`, `laplace`.

| gap | section | the source that closes it | where it is | status after B18 |
|---|---|---|---|---|
| **GAP-09** | s.4.11 / s.11 | Povstenko 2009 (B14), Povstenko 2015 book (B15), Mainardi 2010 (B16), Gorenflo–Kilbas–Mainardi–Rogosin 2014 (B17) | **all four on the request list, none in Drive** | **PARTLY CLOSED** (Caputo F23 and Sherief F24 are in; the special-function machinery is not). No further reading in the library can close it. |
| **GAP-12** | s.9 / s.10 | Achenbach 1973, *Wave Propagation in Elastic Solids* | **request list Part C item C3 — print-era, NO DOI; not in Drive.** The Elsevier chapter DOIs `10.1016/b978-0-7204-0325-1.*` are the 1975 reprint and the front matter is marked WITHDRAWN — do not substitute them for the book | **OPEN.** Until a copy arrives, the energy-flux definition is quoted at one remove (the applied papers cite Kumar & Sharma 2021b for it, not Achenbach). |
| **GAP-13** | s.10 | Nowacki, *Dynamic Problems of Thermoelasticity* | **not in Drive; no verified book DOI.** OpenAlex resolves only a **one-page 1977** item in *J. Appl. Mech.* **44**(2), 366 with this title and W. Nowacki among the authors (`10.1115/1.3424081`) — a pointer/review record, **not the book**. Publisher/edition are **UNVERIFIED** and I did not guess them | **OPEN**, non-blocking: the identity at `EQ-10.12` is already printed in `LIT-0472` eq (80) and in the energy-ratio papers read this session; Hetnarski–Ignaczak 1999 (list B12) would give the standard-review backing and is paywalled. |

### 4. Second reading pass on the four items — what the pages and equations actually say

Read by local extraction of the Drive PDFs (all four are in the library). Printed page numbers exist only in the IJAME paper; the three Springer items are online-first or Academia.edu copies with **no printed pagination**, so the anchor is the PDF page plus the equation number. All bibliographic fields below were re-verified at OpenAlex on 2026-10-23.

**(a) Aldawody, Hendy & Ezzat 2019**, *On dual-phase-lag magneto-thermo-viscoelasticity theory with memory-dependent derivative*, *Microsyst. Technol.* **25**(8), 2915–2929, `10.1007/s00542-018-4194-6` — **closed** (no OA), Drive `DRV-0137`, 15 pp.
- §8, **PDF p.9**: the inversion formula it uses is printed as `g(t) = (e^{dt}/2π)∫…`, then the Fourier-series approximation at **eq (86)** with coefficients at **eq (87)** `c_k = (e^{dt}/L) Re[e^{ikπt/L} ḡ(d+ikπ/L)]`; **PDF p.10**: the **Korrektur** correction at **eq (88)**, `g(t) ≈ g_N^K(t) = g_N(t) − e^{−2dL} g_{N'}(2L+t)`, followed by the ε-algorithm.
- The paper names the method at **PDF p.3** ("the inversion … is completed utilizing a numerical approach proposed by Honig and Hirdes (1984)") and again at the start of §8. **This is the concrete reason A12 matters**: a paper the review already uses for second-order DPL + MDD cannot be reproduced without that algorithm.
- The law it prints is unchanged from my first read: second order in `τ_q`, **first** order in `τ_θ`, with the quoted rationale `τ_θ >> τ_q > 0` (Roychoudhuri 2007) — the T2-style truncation, i.e. an attribution caution, not a manuscript error.

**(b) Kumar, Barak, Kumari, Gupta & Ahmad 2024**, *The effect of viscosity and hyperbolic two-temperature on energy ratios in elastic and piezoviscothermoelastic half-spaces*, *Mech. Time-Depend. Mater.* **28**(3), 937–957, `10.1007/s11043-023-09657-1` — **closed**, Drive `DRV-0029` (own group).
- **PDF p.11, eq (6.1):** `P = −Re{σ13 ū̇1 + σ33 ū̇3 + K3 T̄,3 T/T0 − φ D̄̇3}`; **eq (6.2)** the elastic-half-space flux; **eqs (6.3)–(6.5)** the *average* fluxes for incident, reflected and the four transmitted waves.
- **PDF p.12:** ratios at **eqs (6.6)–(6.9)**; interaction ratios at **eq (6.10)**; and energy conservation printed as an **identity**: `Σ_{s=1..4} (E_s^s + E_int + E_RP + E_RS) = 1` at **eq (6.11)**, with `E_int = Σ_{s≠t} E_st`.
- The **"nearly equal to one"** sentence that my earlier facts row quoted is in the **conclusions, PDF p.20** ("the sum of their energy ratios is nearly equal to one for every angle of incidence") — it is a numerical observation about the eight models tested, **not** the content of (6.11). The identity itself is exact. This distinction is now written into the facts row.

**(c) Kumar & Kumari 2024**, *Response of stiffness and viscosity on the energy ratios at piezo-visco-thermo-elastic medium*, *Int. J. Appl. Mech. Eng.* **29**(1), **54–72**, `10.59441/ijame/174992` — **gold OA, CC-BY-NC-ND** (the only genuinely OA item of the four), Drive `DRV-0031`.
- **Printed p.62, section 6:** flux `P = −Re{σ13 u̇1 + σ33 u̇3 ∓ φ Ḋ3 + K T,3 T}` at **eq (6.1)**, elastic flux at **(6.2)**, average fluxes at **(6.3)–(6.5)**.
- **Printed p.63:** reflected ratios **(6.6)**, transmitted **(6.7)**, the SV-wave versions **(6.8)–(6.9)**, the interaction flux **(6.10)**, and conservation again as an **identity**: `Σ_{s=1..4} E_s^s + E_RP + E_RS + E_int = 1` at **eq (6.11)**.
- **Cross-paper check (the one substantive new finding of this pass):** the two sister papers print the *same* identity at the *same* equation number, but their **thermal flux term differs in form** — MTDM (6.1) writes `K3 T̄,3 T/T0` in the integrand with the overbar on the derivative, IJAME (6.1) as extracted writes `K T,3 T` with no `T0`. The IJAME extraction of (6.1) is visibly garbled (symbols dropped), so **I am not calling this an inconsistency** — I am flagging that the two forms must not be merged in the manuscript, and that if the review quotes one flux formula "used by the group", it should be quoted from one paper with its own equation number.

**(d) Biswas 2020**, *Surface waves in piezothermoelastic transversely isotropic layer lying over piezothermoelastic transversely isotropic half-space*, *Acta Mech.* **232**(2), 373–387, `10.1007/s00707-020-02848-8` — **closed** (Academia.edu copy in Drive, `DRV-0167`, 15 pp.), was s.8's only eligible row.
- **PDF p.2, eq (3):** `K_ij ∂T,ij/∂t + K*_ij T,ij = ∂²/∂t²[ρ C_v T + T0(β_ij u_i,j − p_i φ,i)]` — GN-III printed with **both** the `K` and `K*` groups, exactly the structural discriminator B03 needed; **eq (5)** stress with `−β_ij T − e_kij E_k`, **eq (6)** electric displacement with `+ p_i T`.
- **PDF p.3, eqs (7)–(10):** the layer system, with the same GN-III balance at **eq (10)** including the pyroelectric `p3 φ1,z` term. No energy ratio, no flux integral — this paper supports the s.8 Rayleigh surface-wave label and the s.4.6 GN-III label, nothing in s.10.

**Verdict on the four:** all four are genuinely read at full-text level *by this verifier, this session* (download + local extraction), with equation numbers and (where the copy prints them) page numbers. Nothing in them contradicts the manuscript. Two corrections/limits are now recorded: the conservation statement is an **identity with an interaction term** in both own-group papers (the "close to one" wording is a numerical conclusion), and the **thermal flux term differs between the two papers** in the extraction and must be quoted per paper.

## Evidence / sources

- `control/FULLTEXT_FINDINGS_09.md` (F28, F29) at `origin/claude/control` **`0be11f2`** — read in full; the only route to the two Laplace papers, because **neither PDF is in Drive** (see 5 below).
- OpenAlex 2026-10-23, one batched DOI query for `10.1007/s00542-018-4194-6`, `10.1007/s11043-023-09657-1`, `10.59441/ijame/174992`, `10.1007/s00707-020-02848-8`; separate queries for `10.1093/comjnl/17.4.371` and `10.1115/1.3424081` (`select=…,authorships,biblio,open_access`).
- Drive files read this batch, by inventory id: **DRV-0137, DRV-0029, DRV-0031, DRV-0167** (ids in `FULLTEXT_FACTS.csv`); extracted in `/tmp/pdfs`, deleted after.
- CSV/markdown changed: `FULLTEXT_FACTS.csv` (+2 rows, 4 edited), `LITERATURE_BASE.csv` (+4 rows, 4 edited), `REFERENCE_PLAN.csv` (+4 rows, all s.8), `REFERENCE_READINESS.csv` (s.8 + TOTAL), `REFERENCE_GAPS.csv` (GAP-09/12/13 status appended), `PDF_REQUEST_LIST_3.md` (A0 = 8, Part A = 3, Part B = 21, GAP-19 row).

## Checks done

- **No invented identifiers.** Durbin's title, author and pages were taken from the OpenAlex record after my first text for it was written from memory — the memory version was wrong (it would have been "Numerical inversion of Laplace transforms efficiently"); the record gives *…: an efficient improvement to Dubner and Abate's method*. The guessed DOI trap from B16b (`10.1016/0377-0427(84)90039-6` = Bellen 1984) was **not** reused; the Honig–Hirdes DOI is the `90075-x` one.
- **List arithmetic re-counted, not asserted:** A0 8 + A 3 + B 21 + C 5 = 37 items covering the gaps, of which 29 outstanding (3 OA / 21 paid / 5 print).
- **Plan integrity:** 215 rows, no duplicate `lit_id` (0516–0519 checked free before use); s.8 now 12 rows; no row changed section.
- **Facts integrity:** still one row per paper; the four second-pass rows keep their `inv_id`/`drive_id` and only gained page/eq detail plus the identity-vs-inequality correction.
- **Read-level honesty:** the four second-pass reads are **my** reads (FULL), the two Laplace papers are **not** (SECONDARY-SOURCE, "not opened by this verifier"), and the two new s.8 items are metadata-only. Where a copy carries no printed page numbers I say "PDF p." rather than inventing a journal page.
- **Privacy:** no folder name from the private/personal area was written anywhere; files referenced by `inv_id` + file name only.

## Confidence

- **HIGH** that both Laplace algorithms are now in the base with their working formulas and error behaviour, and **HIGH** on the OA verdicts for all four new identifiers (each from an OpenAlex record fetched this session).
- **HIGH** that the four second-pass items were read at full-text level by me, and **HIGH** on every equation number quoted above (each was seen in the extracted text of the specific PDF named).
- **HIGH** that eq (6.11) in both own-group papers is an identity with an explicit interaction term, and that "nearly equal to one" is the conclusions' wording.
- **MEDIUM** for the IJAME (6.1) thermal-term comparison: the extraction there is garbled, so the difference is *observed in extraction*, not *verified on the render*.
- **MEDIUM** for the Dubner–Abate / Stehfest facts: correct as a record of what the supervisor relayed, but no page render was seen by me; Stehfest's Table I column assignment is explicitly unverified.
- **LOW** for anything numerical beyond the error bounds quoted verbatim from the findings note.

## NOT verified / open issues

1. **I have not opened the Dubner–Abate or Stehfest PDFs.** Their rows are `SECONDARY-SOURCE`, not `PRIMARY-SOURCE-CHECKED`. This is deliberately stricter than B17's F23–F27 wording; if the team wants the earlier convention applied here too, that is a one-field change — but then the standing rule "supervisor-relayed is never PRIMARY-SOURCE-CHECKED" needs to be re-decided explicitly, because the two conventions now coexist in `FULLTEXT_FACTS.csv`.
2. **Neither Laplace PDF is in Drive.** A Drive-wide name search returns only the Malla–Reddy webinar, and `DRIVE_INVENTORY.csv` has no Dubner/Stehfest/Honig/Durbin/Laplace row at all. They were supplied to the supervisor, not through the inventory; that is why the two rows have free-text `inv_id`s.
3. **s.8 is still below the six-source bar (3 of 6)**, and two of those three are supervisor-transcribed. Honig–Hirdes (A12, free) and Durbin (B21, closed) would take it to 5 if obtained and read; Stroh 1958/1962, Chadwick–Sneddon 1958 and Joseph–Preziosi 1989/1990 are still paywalled.
4. **GAP-12 and GAP-13 cannot be closed from inside the library.** Both need a book (Achenbach 1973; Nowacki, edition unverified) and neither has a usable DOI.
5. **Ijame (6.1) needs a render check** before any sentence compares the two flux formulas.
6. **The "four items" identification in this batch is my reconstruction** (3 + 1 from the readiness table). If the authors meant De 2020 or a different set, say so and I will re-run the pass on the correct four.
