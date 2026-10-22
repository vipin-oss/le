# V-B8a — TPL law re-audit against FULLTEXT_FINDINGS_02 (F6, F7, F8, F9)

**Order:** `control/FULLTEXT_FINDINGS_02.md` @ `origin/claude/control` `630c93b`, "Orders arising →
BRAVE" (items 1 and 2) plus the F9 addendum order.
**Access date:** 2026-10-22. **Files touched:** this sheet only; `V-B8a_tpl_checks.py` (checks);
two banner edits in my own `V-B2h` and `V-B2z`. No manuscript file was read for wording, none edited.
**Ledger counts unchanged:** `EQUATION_LEDGER.csv` 176 rows, `CLAIM_LEDGER.csv` 53 — see §3.3 for
why I did **not** add rows.

---

## 1. Task

The three instructions, verbatim in intent:

1. Re-audit **EQ-019**, **every TPL row of `EQUATION_LEDGER`**, and **appA Eq 10.12** against **F6**.
2. For **any second-order (τ²/2) TPL form the manuscript uses**, find the primary source and give its
   status tag. **Do not guess.**
3. **Grep my own V-files first**; a WRONG verdict only with an explicit statement of which
   sub-system was checked.

F8 (DPL stability, condition (4.1), τ_T > τ_q/2) is confirmatory of `V-B2p` — recorded in §3.7, no
action.

## 2. Method

1. **Fetched and read** `FULLTEXT_FINDINGS_02.md` in full at `630c93b` (F1–F9 and both order blocks).
2. **Located the objects.** `EQ-019` and `EQ-10.12` do **not** exist in one manuscript: the repo
   carries two states, and the two rows are quoted by F7/F9 from the **legacy** one. Both were
   audited and are distinguished throughout:
   - **legacy** = `phase4/manuscript/` (v1.0 line; `appendices/appA_equation_register.tex:62`,
     `sections/sec04_thermoelastic.tex:191–199`, `appendices/energy_flux_derivations.tex:266–297`);
   - **live** = `phase5/master/` (v1.1 revision I have audited since B1;
     `appendices/appA_equation_register.tex:64` and `:115`, `sections/sec04_thermoelastic.tex:186–190`).
   Source of both: `origin/arena/40393d9f-le` @ `11b3330`, extracted read-only to `/tmp/ms`.
3. **Own V-files grepped first** (instruction 3), before writing any verdict:
   ```
   grep -rn "TPL\|triple\|EQ-019\|10\.12" verification/*.md
   python3 -c "...EQUATION_LEDGER model column, sec04 rows..."
   ```
   Results in §3.2. Prior verdicts found: `V-B2h` (form UNVERIFIED, ½ factor LOW confidence),
   `V-B2z` M6 (factor-2 issue) and M14 (self-recorded sign defect), `V-B2d` (GN-I ≠ separate theory).
   **No prior V-file gave EQ-019 or EQ-10.12 a verdict at all** — they were never in a ledger
   (§3.3), so there is no earlier WRONG/CORRECT to overturn.
4. **Independent full texts**, to avoid resting only on F6: two open-access papers that print Roy
   Choudhuri's law were read this session (`10.1038/s41598-020-73590-3` Zhang/Sun/Yang 2020, eqs (3),
   (4), (7), (8); `10.1038/s41598-020-70388-1` Abouelregal et al. 2020, eqs (7)–(11)), plus the
   already-read `10.1038/s41598-023-44339-5` (Sci Rep 2023, eqs (8) and its limiting-case table).
5. **Two mechanical checks** (`V-B8a_tpl_checks.py`, no sympy, SI-exponent bookkeeping):
   (A) dimensional exponents of the printed second-order term, (B) Taylor-truncation bookkeeping of
   the three-lag law order by order. Both run clean; output quoted in §3.4–§3.5.
6. **Provenance search** for a second-order TPL form: Crossref/OpenAlex OA lookup on candidate DOIs,
   arXiv API (`all:"three-phase-lag"`, 2 hits), and targeted web search; every candidate that could be
   opened was opened. What could not be opened is named, not assumed (§3.6).

## 3. Result

### 3.1 What F6 establishes, and what I could confirm myself

Roy Choudhuri 2007 (`10.1080/01495730601130919`), as read by Claude at F6:

- **eq (3)** `q(P,t+τ_q) = −[ k ∇T(P,t+τ_T) + k* ∇v(P,t+τ_v) ]`, `v̇ = T`, `k* > 0`,
  ordering `0 ≤ τ_v < τ_T < τ_q`;
- **eq (4)** first-order Taylor in **all three** lags;
- **eq (9)** the eliminated heat equation, **no ½τ_v² term anywhere**.

Two open-access papers read by me this session state the same law, independently of F6:

| source (full text, 2026-10-22) | printed law | truncation |
|---|---|---|
| Zhang, Sun & Yang 2020, Sci Rep **10**, `10.1038/s41598-020-73590-3`, eq (4) + eq (8) | `q(r,t+τ_q) = −[k∇T(r,t+τ_T) + k*∇v(r,t+τ_v)]`; "Taylor's series expansion … up to the **first-order** terms in τ_q, τ_T and τ_v" | first order, all three |
| Abouelregal et al. 2020, Sci Rep **10**, `10.1038/s41598-020-70388-1`, eqs (7)–(11) | general higher-order TPL: `(1+Σ τ_q^r/r! ∂ᵗʳ) q = −K(1+Σ τ_φ^r/r! ∂ᵗʳ)∇φ`, with the third lag on the temperature side (two-temperature) | any order, `τ^r/r!` |
| Barak et al. 2023, Sci Rep **13**, `10.1038/s41598-023-44339-5`, eq (8) + "Case 9" | same higher-order TPL with MDD; **Case 9** (`p=l=1`, `n=2`) labelled "Roy Choudhuri" | p=l=1, n=2 |

The Zhang paper also repeats the ordering `0 ≤ τ_v < τ_T < τ_q` and attributes it to Choudhuri
(ref. 14). **F6 is therefore corroborated on the structural points by two independent OA texts I read
myself.** One honest wrinkle: Sci Rep 2023's "Case 9" assigns **n = 2** (second order in τ_q) to Roy
Choudhuri, whereas F6 read Roy Choudhuri's eq (4) as first order in all three. The primary wins; the
secondary mapping is loose. It is, however, exactly how a second-order form gets retro-fitted onto
Roy Choudhuri's name — worth knowing when tracing where the manuscript's form came from (§3.6).

### 3.2 My own prior verdicts on these objects (grep-first record)

| my file | prior statement | status now |
|---|---|---|
| `V-B2h` R1/R2 | TPL heat law written as `(1+τ_q∂_t+½τ_v²∂_t²)(ρcθ̇+βT₀ε̇) = k_th(1+τ_T∂_t)∇²θ`, labelled "standard form, NOT source-verified" | **REFUTED as an attribution** — no such operator is Roy Choudhuri's (§3.1). The *algebra* downstream of it (R4–R5 stability, stiffness, nesting) remains valid **for that hypothetical operator only**. Sub-system: rigid heat conductor, 1-D linear, frozen coefficients. |
| `V-B2h` R3 | "the literature does not agree on the coefficient of τ_v²: ½τ_v² vs τ_v²" | **PREMISE WITHDRAWN.** The disagreement I recorded was not about Roy Choudhuri's law, which has no τ_v² term at all. I can no longer state that "two inequivalent published forms exist" — I could not re-locate them this session. Treated as retracted, not silently deleted. |
| `V-B2z` M6 | "TPL with ½τ_v² in one paper and τ_v² in another … HIGH that both forms exist, canonical UNVERIFIED" | **DOWNGRADED to UNVERIFIED.** The two papers were not recorded, so the claim is unfalsifiable as it stands; the honest version is §3.6. |
| `V-B2z` M14 | my own sign defect in the DPL/TPL rows of `V-B2_wave_speeds.py`, caught by the τ→0 limit check | unchanged, still stands |
| `V-B2_wave_speeds.py:75–78` | `TQ = (1 − iωτ_q − ω²τ_v²/2)`, comment "(1+tq d/dt + tv²/2 d2/dt2)" | runs on the **hypothetical** operator; not a statement about Roy Choudhuri. Numbers in `V-B2h` R4/R5 inherit that scope. |
| `V-B2d` §39 | GN-I counted separately is wrong | unaffected |
| `EQUATION_LEDGER.csv` | **zero** TPL rows, **zero** appA rows (176 rows: sec03–sec12, appB, appD–F, energy_flux, T1, T4) | see §3.3 |

### 3.3 Audit 1 — EQ-019, three loci

**(a) Legacy `appA_equation_register.tex:62` (EQ-019, tagged VERIFIED) and legacy
`sections/sec04_thermoelastic.tex:191–199` (eq 4.17, section titled "*Triple-phase-lag (TPL) theory
(Tzou, 1997)*"):**

```
q_i(t+τ_q) = −k[ T_{,i}(t+τ_T) + (τ_ν/2) ∂_t² T_{,i}(t+τ_ν) ]        (legacy eq 4.17 / EQ-019)
```

Four independent defects, each checkable without the 2007 paper:

1. **The `k* ∇v` term is missing.** TPL's distinguishing content is the thermal-displacement
   gradient; without it the law is not three-phase-lag at all (F6, F7; confirmed in §3.1 by two OA
   texts). §NOTES: this is the only defect that changes the *model*, not just its transcription.
2. **The §-term is dimensionally impossible.** `[T_{,i}] = K·m⁻¹`; `[∂_t²T_{,i}] = K·m⁻¹·s⁻²`; the
   printed coefficient `τ_ν/2` carries `s¹`, so the bracket mixes `K·m⁻¹` with `K·m⁻¹·s⁻¹`.
   `τ_ν²/2` (`s²`) is required for consistency — see the script's check (A).
3. **No Taylor truncation of Roy Choudhuri's law can produce it.** With `v̇ = T`, the `r`-th term on
   the `∇v` axis is `τ_v^r/r! · ∂ᵗʳ∇v = τ_v^r/r! · ∂ᵗ⁽ʳ⁻¹⁾∇T`; a second time-derivative of `∇T`
   therefore needs **r = 3**, coefficient `τ_v³/6`, and **r = 2** gives `τ_v²/2 · ∂_t∇T` — a first
   derivative. Check (B). So the printed term is not a truncation of any order.
4. **The attribution.** "TPL constitutive law (Tzou 1997)" points at a print monograph with no DOI
   and no page cited. Roy Choudhuri 2007 is the peer-reviewed origin (F6, F7; `V-B1c` #14 already
   ranked it in the most-cited set). Whether Tzou's 1997 book also contains a three-lag formulation
   is **UNVERIFIED** — I cannot open it — so the defect I assert is *"unsupported as printed"*, not
   *"Tzou's book lacks it"*.

**(b) Live `appA_equation_register.tex:64`:** the row now reads "Legacy TPL lag equation withdrawn
pending source check", tag UNVERIFIED. **That withdrawal is correct and now has a documented basis**
(§3.1 + (a) above). It should be replaced by Roy Choudhuri's actual law, not by any second-order
variant (§3.6), and the third lag's symbol should follow the source (`τ_v` for the thermal-displacement
gradient), which the live text already does.

**(c) Live `sections/sec04_thermoelastic.tex:186–190`:** the heading still reads
"Triple-phase-lag (TPL) theory **(Tzou, 1997)**" and the body says "TPL denotes formulations that add
further lagged or thermal-displacement terms … The inherited v1.0 formula is omitted here". The body
is defensible; **the heading's attribution is not** — and the same attribution appears in
`sections/sec01_scope.tex:45` ("(Tzou, 1995/1997)"). Two live attribution defects, independent of
the withdrawn equation. Recorded for Arena; I do not edit.

**(d) `EQUATION_LEDGER` TPL rows: there are none.** 176 rows, model column counted: DPL 4,
DPL (delayed form) 1, DPL (first order) 1, MGT 2, MDD 9, GN-II 4, GN-III 2 … **TPL 0**. The 17 sec04
rows run EQ-036 … EQ-052 and skip from EQ-049 (`sec04:179`, DPL first order, CORRECT) to EQ-050
(`sec04:196`, MGT-like, UNCLEAR). The reason is structural, not an oversight: in the live manuscript
the TPL subsection carries **no displayed equation**, so there was no equation for B6a to ledger.
The ledger also contains **no appA rows at all** (no `appA` file prefix), so **appA EQ-019 and
EQ-10.12 were outside the 229-statement audit by construction**.

I did **not** add TPL rows. Adding them would move the frozen count 176 → 178 and break the
229-statement statistic Claude accepted at `fafb778`. If Claude wants TPL covered equation-wise, the
right move is a separate small ledger for appA (the register), re-frozen as its own count — say the
word and I will build it.

### 3.4 Audit 1 — appA EQ-10.12

**(a) Legacy `appA_equation_register.tex:114`**, tag **VERIFIED**:

```
J_i^{TPL+MDD} = σ_{ji}v_i − φḊ_i + (T₀/T) K_i T_{,i}
"Confirmed across 8 full-text sources: P05 (Sci Rep 2023, Eq 45), P07 (IJP 2023, Eq 47),
 P08 (HFF 2023, Eq 6.1), P11 (HFF 2023, Eq 6.1), P12 (MMMS 2023, Eq 6.8), P14 (JTS 2024,
 Eq 6.1), P23 (IJAME 2024, Eq 6.5), P25 (MTDM 2024, Eq 6.1); identical 3-channel structure"
```

Four findings, in increasing order of how much they matter:

1. **The row is a flux *structure*, not a TPL statement — so it cannot carry a VERIFIED tag that
   insulates the TPL law.** A flux that is stated for "TPL+MDD" inherits whatever lag law the eight
   sources used. If the lag law is mis-transcribed (§3.3a), a VERIFIED flux does not rescue it, and
   the row's wording invites a reader to think the TPL part was checked. It was not.
2. **"8 sources" is one school, not eight independent checks.** I can map six of the eight onto
   `LITERATURE_BASE` rows by title/journal/year, and **all six carry Barak and/or Gupta as authors**
   (LIT-0042, 0043, 0044, 0045, 0046, 0047; LIT-0048 is the seventh). Agreement inside one research
   programme is *consistency*, not corroboration. The register should say "eight papers of the same
   group using one template", which is what the record shows.
3. **The thermal channel's factor is the reciprocal of the one source I have read.** Sci Rep 2023
   eq (45) prints `P = −Re(σ₁₃ū̇₁ + σ₃₃ū̇₃ − φD̄̇₃ + K₃T̄,₃·T/T₀)`; the register writes `(T₀/T)K_iT_{,i}`.
   `T/T₀` vs `T₀/T` — **unless** the source's `T̄` is a differently normalised symbol, which the HTML
   rendering does not settle. Tagged **UNRESOLVED**, needs the typeset PDF (request row 9 area /
   row 20); I do not call it an error on a rendered page.
4. **The electrical channel's sign is the one thing the row gets right against my earlier reading.**
   Sci Rep 2023 has `−φḊ₃`; the register has `−φḊ_i`. Consistent. (This is what `V-B7b` §3.2c already
   recorded, and it survives.)

**(b) Live `appA_equation_register.tex:115`:** EQ-10.12 is now `ΣR + ΣT = 1`, CONDITIONAL, "Lossless
limit only; **mode-wise use requires cross-term accounting**". The live register already anticipates
F9's cross-term point. **The residual risk is in the prose, not the register**: §9.7 body
(`sections/sec09_interfaces.tex`, "The pattern and its limits") states "Across this body of work the
pattern is consistent: **the conservation identity survives extension to generalized media**". F9
reports that in Barak et al. the unity result holds only because the cross terms are lumped into
`E_int`, which can be negative or non-physical per mode. If that is right, the body sentence is
**too strong as written** and the review must state the cross-term bookkeeping explicitly.
My own position: I read Sci Rep 2023 eqs (45)–(50) (per-wave fluxes `⟨P^e_IP⟩`, `⟨P^e_RP⟩`, …) and
the chunk I saw does **not** display a closure statement or a cross-term definition, so I can neither
confirm nor refute F9 from that paper. **Evidence level for finding (b): F9 = supervisor's full-text
reading of Barak JTS; mine = none on the closure claim.** Flagged, not adjudicated.

### 3.5 Audit 2 — provenance of a second-order (τ²/2) TPL form

**Question:** the manuscript uses a second-order TPL term. Which primary source has it?

| candidate | form as printed | did I read it? | status tag |
|---|---|---|---|
| **Roy Choudhuri 2007**, JTS 30(3):231–238 | first order in all three lags; **no τ²/2 term at all** | no (closed). F6 read eqs 1–9; I corroborated the *structure* in two OA texts | **PRIMARY-SOURCE-CHECKED for "first order only"** — by F6, and independently by §3.1's two OA texts |
| **Abouelregal, Khalil, Mohammed, Nasr, Zakaria & Ahmed 2020**, Sci Rep **10**, `10.1038/s41598-020-70388-1`, eqs (9)–(11) | general higher-order TPL: `(1+Σ_{r=1}^{m} τ_q^r/r! ∂ᵗʳ) q = −K(1+Σ_{r=1}^{n} τ_φ^r/r! ∂ᵗʳ)∇φ`; at `r=2` the coefficient **is** `τ²/2`; third lag on the two-temperature side | **YES, full text, OA (CC-BY)** | **PRIMARY-SOURCE-CHECKED (by me).** This is a genuine primary for a second-order TPL form — with lags `(τ_q, τ_φ, τ_θ)`, **not** `τ_v`, and with the second-order term on the **gradient** axis (n) or flux axis (m) |
| **Barak et al. 2023**, JTS, `10.1080/01495739.2023.2253879`, eq (2.5) (as reported at F9) | `(1+τ_vD_s)K*_{ij}u_{,ij} + (1+τ_TD_s)K_{ij}Ṫ_{,ij} = (1+τ_qD_s+(τ_q²/2)D_s²)[…]` — second order in **τ_q**, on the energy bracket | **no** (closed; my request row 9) | **SECONDARY** — F9's reading only; I have not seen it |
| **the manuscript's printed form** `(τ_ν/2)∂_t²T_{,i}(t+τ_ν)` | second order on `∇T` with the **first** power of `τ_ν` | legacy + live source both read | **NO PRIMARY FOUND**, and **not obtainable** from Roy Choudhuri's law at any truncation order (§3.3a items 2–3) |

**Status answer, stated plainly.** There are exactly two legitimate second-order TPL constructs I
can point to: `(τ_q²/2)` on the flux/energy axis (Barak/Gupta, **secondary**, F9), and the general
`τ^r/r!` family (Abouelregal et al. 2020, **primary, read**). Neither is a second-order term in
`τ_v` on `∇T`, and **neither prints the manuscript's `τ_ν/2` coefficient**. The manuscript's form is a
hybrid that matches no source I can open, and it fails a dimensional check on its own. If Arena wants
a second-order TPL, the defensible options are (i) stay with Roy Choudhuri's first-order law, or
(ii) adopt Abouelregal et al. 2020 eq (9) with explicit orders `(m,n,p)` and its own citation, in
which case the third lag is a temperature lag, not a thermal-displacement lag, and the model is a
two-temperature model — a different claim than the review currently makes.

### 3.6 F9's order to Brave — §9.7 attributions against what Barak actually does

F9 says: re-tag EQ-019 with F9's form; check manuscript §9.7 attributions against F9. Applied:

- **EQ-019**: if a second-order form is kept, F9's is `(τ_q²/2)` on the **energy bracket** with `τ_v`
  and `τ_T` first order. Tag: **CONDITIONAL on Quintanilla–Racke stability**, secondary source. Not
  adopted by me as "the" TPL law; Roy Choudhuri's first-order law is what "TPL" means.
- **§9.7 item 3** (live `sec09_interfaces.tex`, "History-dependent transmission") attributes to
  `Barak2023MMMS` / `Barak2023JTS` mechanism claims (kernel-weighted history; monoclinic anisotropy
  acting through separate mechanisms). F9's reading of Barak JTS gives the flux bookkeeping and the
  cross-term structure, **not** a demonstration that memory and anisotropy "act through separate
  mechanisms and can therefore be separated experimentally". On F9's account the manuscript goes
  beyond the source. **UNVERIFIED** — I have not read either paper (request rows 9, 18).
- **§9.7 item 1** ("Electromechanical stiffness shift … conservation identity remains satisfied")
  attributes to `Barak2023IJP`. Same closure question as §3.4(b). **UNVERIFIED.**
- F9 also notes Barak cites the normal acoustic flux from Kumar & Sharma (2021) and Guha & Singh
  rather than deriving it. The manuscript does not claim a derivation, so no defect — recorded as a
  consistency note only.

### 3.7 F8 (DPL stability) — confirmatory, no action

Quintanilla 2002 condition (4.1) is `τ_T > τ_q/2` ⇒ exponential stability, matching `V-B2p` §3.1,
which derived the same threshold by Routh–Hurwitz on the 1-D symbol and flagged the second-order-in-
`τ_q`, first-order-in-`τ_T` truncation (T2) as the model it applies to. **Sub-system:** rigid heat
conductor, 1-D, linear, frozen coefficients — *not* the coupled thermoelastic system. F8 does not
extend it either. Nothing to change; the earlier `V-B2p` caveat that the coupled case is unproven
stands.

### 3.8 Verdict summary (each with its sub-system)

| object | verdict | sub-system checked | basis |
|---|---|---|---|
| legacy EQ-019 / eq 4.17, **as printed** | **WRONG-CONFIRMED** | the constitutive flux law only; rigid heat conductor, 1-D scalar; **not** any dispersion, solution or energy result derived from it | §3.1 + §3.3a items 1–3 (F6; 2 OA full texts; truncation bookkeeping; dimension check) |
| legacy EQ-019 **attribution** "Tzou 1997" | **WRONG-CONFIRMED as unsupported** | attribution only; the 1997 book itself is UNVERIFIED | §3.3a item 4 |
| legacy appA EQ-10.12, tag VERIFIED | **downgrade to UNVERIFIED/OPEN** | the TPL+MDD flux register row for a piezothermoelastic interface; mechanical + electrical channels not disputed | §3.4a items 1–3 |
| live appA EQ-019 (withdrawn) | **CORRECT** | withdrawal of the lag equation | §3.3b |
| live section heading + `sec01:45` "TPL (Tzou, 1997)" | **WRONG-CONFIRMED as unsupported** | attribution only | §3.3c |
| live appA EQ-10.12 (`ΣR+ΣT=1`, CONDITIONAL) | **CORRECT-CONDITIONAL**, keep | lossless limit; cross-term caveat already printed | §3.4b |
| live §9.7 "the conservation identity survives" | **UNVERIFIED — too strong if F9 is right** | energy partition at a bonded bimaterial interface | §3.4b, F9 |
| `V-B2h` R1/R2 operator | **my own attribution refuted**; algebra valid only for that hypothetical operator | rigid 1-D heat conductor | §3.2 |
| `V-B2z` M6 | **withdrawn to UNVERIFIED** | TPL coefficient | §3.2 |

## 4. Evidence / sources

All accessed 2026-10-22.

1. **Roy Choudhuri, S. K. (2007).** "On a thermoelastic three-phase-lag model." *J. Thermal Stresses*
   **30**(3):231–238. DOI `10.1080/01495730601130919`. **Access level: abstract/metadata only to me**
   (OpenAlex `is_oa:false`, `closed`); the equations as printed are known to me **only through F6**,
   which is a primary reading by the supervisor. Corroborated structurally by sources 2–3.
2. **Zhang, Q.; Sun, Y.; Yang, J. (2020).** "Bio-heat response of skin tissue based on three-phase-lag
   model." *Scientific Reports* **10**, DOI `10.1038/s41598-020-73590-3`. **FULL TEXT (gold OA,
   CC-BY)**; eq (4) the lagged law, eq (7)/(8) the first-order Taylor form, and the `0 ≤ τ_v < τ_T < τ_q`
   ordering attributed to Choudhuri as its ref. 14.
3. **Abouelregal, A. E.; Khalil, K. M.; Mohammed, F. A.; Nasr, M. E.; Zakaria, A.; Ahmed, I.-E. (2020).**
   "A generalized heat conduction model of higher-order time derivatives and three-phase-lags for
   non-simple thermoelastic materials." *Scientific Reports* **10**, DOI `10.1038/s41598-020-70388-1`.
   **FULL TEXT (gold OA, CC-BY)**; eqs (7)–(11) give the general higher-order TPL with `τ^r/r!`
   coefficients, and eq (11) the eliminated heat equation. Cited by Sci Rep 2023 as its ref. 33
   (higher-order TPL without MDD).
4. **Barak, M. S. et al. (2023).** "Behavior of higher-order MDD on energy ratios at the interface of
   thermoelastic and piezothermoelastic mediums." *Scientific Reports* **13**, DOI
   `10.1038/s41598-023-44339-5`. **FULL TEXT (gold OA, CC-BY)** — read at `V-B7b`; this session re-read
   eq (8), the "Case 1–11" limiting-case list, and eqs (42)–(50) (Δ matrix, flux eq 45, per-wave
   fluxes eqs 47–50).
5. **Barak, M. S. et al. (2023/24).** "Energy transfer at the interface of monoclinic
   piezothermoelastic and thermoelastic half spaces with MDD." *J. Thermal Stresses* **47**, DOI
   `10.1080/01495739.2023.2253879`. **NOT read by me**; everything attributed to it here comes from
   **F9**. Request row 9.
6. **Quintanilla, R. (2002).** *J. Non-Equilib. Thermodyn.* **27**(3):217–227, DOI
   `10.1515/jnetdy.2002.012`. Condition (4.1) as reported at **F8** (supervisor's reading);
   corroborates `V-B2p` independently.
7. **`control/FULLTEXT_FINDINGS_02.md`** @ `630c93b` — F6, F7, F8, F9 and the two order blocks.

## 5. Checks done

1. **Grep-first honouring instruction 3** — all my `.md` files and the ledger's model column searched
   for TPL before any verdict was written; the table in §3.2 is the result, including the two places
   where I am now refuting my own earlier text.
2. **Dimensional check (A)** on the printed term, in real space and in the frequency domain; both
   give the same answer (the `s¹` coefficient is inadmissible, `s²` is right).
3. **Truncation bookkeeping (B)**, order by order to `r = 4`, showing the index shift from `∇v` to
   `∇T`; this is what rules out the printed term at *any* order, which a source-comparison alone
   could not do.
4. **Three-way source triangulation** for the law's structure (F6 + two OA full texts), so the
   central factual claim does not rest on a single reader.
5. **Self-consistency:** the Sci Rep 2023 "Case 9" mapping was checked against F6 and the conflict
   recorded rather than dropped (§3.1).
6. **Count check:** `EQUATION_LEDGER.csv` — 176 rows, TPL model count 0, appA prefix count 0;
   verified by parsing the CSV, not by eye. `CLAIM_LEDGER.csv` untouched at 53.
7. **No artifact edited outside `verification/`**; the two manuscript trees were read at
   `origin/arena/40393d9f-le` @ `11b3330` and not modified.
8. **Script reproducibility:** `python3 V-B8a_tpl_checks.py` runs to completion with the stdlib only
   (`fractions`); output quoted in §3.3, §3.5.

## 6. Confidence

- **That Roy Choudhuri's law is first order in all three lags with no τ²/2: HIGH.** F6's primary read
  plus two independent OA texts I read myself.
- **That the legacy EQ-019 term is dimensionally inadmissible and not a truncation of that law at any
  order: HIGH.** Pure bookkeeping; two independent routes.
- **That no primary source prints the manuscript's `τ_ν/2 ∂_t²∇T`: HIGH for "I could not find one",
  MEDIUM for "none exists".** I searched Crossref/OpenAlex/arXiv and opened everything reachable; a
  print-only or non-indexed source cannot be excluded.
- **Provenance of legitimate second-order TPL: MEDIUM–HIGH.** One primary read (Abouelregal et al.
  2020), one secondary (Barak via F9, unread).
- **§9.7 closure/cross-term finding: MEDIUM, and it is not mine** — it is F9's, on a paper I have
  not read. Recorded as such.
- **Attribution defects (Tzou 1997): HIGH that the citation as printed is unsupported; the book's
  content is UNVERIFIED.**

## 7. NOT verified / open issues

1. **Roy Choudhuri 2007 itself is still not read by me.** Everything I say about its equations is
   F6 plus two secondary reproductions. Request row 14 stands — the primary is needed for the
   conventions (symbol for the thermal displacement, sign of `k*`, the exact ordering statement).
2. **Tzou 1997 (CRC monograph) not opened.** I cannot say whether it contains a three-lag
   formulation; therefore my attribution verdict is "unsupported as printed", not "false".
3. **Thermal-channel factor `T₀/T` vs `T/T₀`** — unresolved; the HTML rendering of Sci Rep 2023
   eq (45) does not settle whether `T̄` is the same quantity as the manuscript's `T`.
4. **Barak et al. JTS (F9's source) not read.** Any statement above sourced to F9 is a
   second-hand reading and is tagged so.
5. **`E_int` cross-term bookkeeping** — I have not seen it in any paper I read; the claim that it can
   be negative per mode is F9's and is unverified here.
6. **The coupled thermoelastic case** is untouched throughout: every stability/truncation statement
   is for the rigid heat conductor.
7. **`V-B2h`'s numeric stability/stiffness results** were computed on an operator that is now known
   not to be Roy Choudhuri's. They remain valid for that operator and are now explicitly scoped; I
   did **not** re-run them for the correct TPL because the correct TPL's eliminated equation
   (F6's eq 9) would need its own parameter study, which is not what this order asked for.
