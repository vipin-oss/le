# B22 — Independent verification of the `phase5` v1.1 revision

**Verifier:** B22 (adversarial, read-only on the author's branch)
**Target:** branch `arena/b5e608f8-le`, head `e56755f` (manuscript source `phase5/master/**`,
published PDF `phase5-v1.1-master.pdf`, 130 printed pages)
**Date:** 2026-10-27
**Deliverables in this folder:** this report, `B22_LEDGER_AUDIT.csv`, `B22_BIB_SPOTCHECK.csv`,
`B22_REDUCTION_AUDIT.csv`, `B22_derivation.py` (independent interface derivation),
`B22_verify_reductions.py` (independent reduction re-implementation), `crossref_b22/` (raw
Crossref material).

**Branch note.** The task sheet asked for work on `arena/04fdf32e-le`. This session is pinned to
`arena/0be2770f-le` and the environment forbids switching branches, so the deliverables are
committed there, under `verification/`. Nothing was written to `arena/b5e608f8-le`; no manuscript
`.tex` was modified.

---

## 1. Verdict counts

| verdict | findings | notes |
| --- | --- | --- |
| **WRONG** (claim false as printed) | **2** | F1 (Table 23 row), F2 (bib DOI + false provenance string) |
| **CONFIRMED-WITH-EVIDENCE-DEFECT** (claim true, cited evidence does not support it) | **1** | F3 (vacuous cross-term assertion) |
| **CONDITIONAL** (true only under an unstated reading / scope) | **4** | F4, F7, F9, F11 |
| **CONFIRMED** | **6** | F13–F18 |
| **INFO** (no defect, could be strengthened) | **1** | F12 |
| **NOT-CHECKABLE** | **1 grouped** | 7 of the 26 audited class-A ledger rows (no source held) |

Severity: **P0 = 0**, **P1 = 4** (F1–F4), **P2 = 6** (F5–F11 is 7 rows; F8 folded into F3's
follow-up), **P3/INFO = 1**.

Ledger audit coverage: **26 of 29 class-A rows** and **all 9 class-V rows**
(`B22_LEDGER_AUDIT.csv`). Result: A rows 17 CONFIRMED / 2 CONDITIONAL / 7 NOT-CHECKABLE;
V rows 8 CONFIRMED / 1 CONFIRMED-with-evidence-defect.

---

## 2. P1 findings

### F1 — P1, WRONG. Table 23 reduces dual-phase-lag to Lord–Shulman the wrong way round.
`phase5/master/sections/sec12_comparative.tex:105` — printed **p. 82, Table 23, row 2**:

> From: Dual phase-lag · To: Lord–Shulman · Limit: `\tau_q \to 0` · Removes: "the hyperbolic part
> of the phase-lag law"

With the manuscript's own DPL law (Eq. `eq:4.16`) the elimination gives
`T_xx + τ_T T_xxt = T_t/α + (τ_q/α) T_tt`. Setting `τ_q → 0` deletes the **second time
derivative**: the result is a gradient-lag (single-phase-lag on `∇T`) theory. It is not
Lord–Shulman, which is precisely the theory that *keeps* the `T_tt` term. The correct reduction of
DPL to LS is `τ_T → 0` with `τ_q` held at `τ_0` — which is exactly the substitution the project's
own `verify_unified_reductions.py` uses (and which I reproduced independently). The printed table
therefore contradicts the printed script, and no check anywhere tests this row.
*Fix:* change the limit to `τ_T → 0` and the gloss to "the temperature-gradient lag; the
flux-relaxation (hyperbolic) term survives". Keep a separate row for the `τ_q → 0` case if wanted,
naming it a gradient-lag model.

### F2 — P1, WRONG. `Quintanilla2003DPL` carries a dead DOI, and its provenance string asserts the opposite.
`phase5/master/references_local.bib` (`@article{Quintanilla2003DPL}`) gives
`doi = {10.1080/01495730390203518}`. Crossref returns **no record** for that DOI (direct lookup and
`filter=doi:`). The held source PDF (`pdfs/quintanilla2003.pdf`, Taylor & Francis wrapper) prints
on its own cover page, for exactly this article (JTS **26**:7, 713–721), the DOI
**`10.1080/713855996`** — a record Crossref does return.
Aggravating: the entry's `source` field reads "Primary paper first page confirms author, title,
journal, volume, pages, year, **and DOI**". The held first page contradicts that sentence. This is
the worst class of bib defect in a manuscript whose selling point is provenance discipline: a
self-certifying verification note that is not true.
*Fix:* replace the DOI with `10.1080/713855996`, add `verified = {YES}` with source
"Crossref + printed cover page", and drop the claim about the DOI from the old note.

### F3 — P1, claim true but the cited evidence is vacuous. `verify_interface_energy.py:44`.
The script's five "cross-term" lines are:

```python
z = sp.symbols("z", complex=True)
assert sp.simplify(sp.re(z - sp.conjugate(z))) == 0
```

`Re(w − w̄) ≡ 0` for **any** complex `w`; this asserts nothing about fields, fluxes, or the
interface. Yet printed §10.5 says the incident–reflected cross term "cancels in the time-averaged
normal flux", ledger **OCL-467** gives `resolved_by = verify_interface_energy.py` with
`evidence_mode = SYMPY-DERIVATION`, and printed p. 70 tells the reader the number is reproduced by
that script.

The underlying statement is **true** — I verified it with the actual two-wave field:
with `σ = iωZ u` forward, `σ = −iωZ u` backward and `⟨J⟩ = −½Re[σ v*]`, the total time-averaged
flux equals the modal sum exactly, while the cross term *before* averaging is
`−2i A_i A_r Z ω² sin(2kx)` (nonzero; see `B22_derivation.py`). Two real caveats the printed
sentence already handles correctly: real positive `Z` and same-medium counter-propagating `k`.
*Fix:* either replace the assertion with the two-field computation (five lines), or drop the script
from the OCL-467 evidence chain and cite the algebra instead.

Related, same script (folded here, P2-grade): of the **7 PASS lines**, only two are substantive
(the 2×2 solve with `det = −(Z1+Z2)`, and `R+T=1`). The control-volume closure, the
`1−R−T = D_L+D_Σ+D_R` identity and the `R+T+A_int` closure are true *by definition* of the terms
introduced two lines earlier (`D_L := P_i−P_r−J_L`, etc.), and the cross-term test is vacuous.
Also, `J_inc`, `J_ref`, `J_trans` are **postulated** (`±Zω²|A|²/2`), not derived from
`−½Re[σ v*]`; the printed text claims the "flux weighting" is reproduced by the script, so the
claim and the code differ in strength. Printing "7 PASS" invites a reader to over-credit the file.

### F4 — P1, CONDITIONAL. `A_int` in Eq. (105) is `D_Σ/P_i` only under a net-flux reading.
`sec10_energy.tex:96` defines `A_int = (J^{tot}_{1,n} − J^{tot}_{2,n})/J_{inc,n}`. The printed
narrative then identifies this with `D_Σ/P_i` from Eqs. (10.13)–(10.14). The two agree only if
`J_{inc,n}` is the **net** incident power `P_i`; read as the *modal* incident flux it is a different
quantity. The symbol name says "incident", the denominator in `D_Σ/P_i` is a net power.
*Fix (one clause):* state that `J_{inc,n}` denotes the net incident flux, or write Eq. (105) with
`P_i` explicitly. My earlier independent re-derivation reached the same conclusion (the counter
example was the double-counted bulk loss, which the printed text does now warn about correctly).

---

## 3. P2 findings

| id | location | finding | fix |
| --- | --- | --- | --- |
| F5 | `appendices/appA_equation_register.tex:181` | The register stops at `EQ-10.13` ("Generalized-theory energy fluxes", OPEN). Nothing registers the four new §10.5.1–10.5.2 equations (`eq:10.13`–`eq:10.16` in the source) or the worked-example 2×2 system, so the newest, most audit-relevant equations in Section 10 are the only ones without a register row. Worse, the register's own IDs `EQ-10.12`/`EQ-10.13` now sit next to LaTeX equation numbers `(10.13)`–`(10.16)` that mean different things. (Source-level finding: the v1.1 PDF text I hold does not contain the register table, so this cannot be checked in print.) | register the four new equations; consider disambiguating the register ID prefix from the printed equation numbers |
| F6 | printed **p. 65** and **p. 70** | Internal repository paths appear in the published text: `reports/V-B3d-cross-term-check.md` (p. 65) and `phase5/verification/verify_interface_energy.py` (p. 70, three occurrences). Nothing else leaked (no Drive links/IDs, folder or batch names, ledger IDs, TODO markers, e-mails, agent names). | either name the supplement generically ("the accompanying verification script") or ship the paths as a real supplement URL |
| F7 | `sec12_comparative.tex:108–109` | The two "memory-dependent + phase-lag" rows are **not checkable**: the manuscript never displays an MDD kernel, normalisation, or lag structure. As written, setting `τ_T = τ_ν = 0` does not remove memory (the kernel does), so "all memory except the phase-lag law" is unmotivated. | display the MDD law once (Section 4 already promises kernel-choices matter), or delete the two rows |
| F9 | `sec12_comparative.tex:71` | Quintanilla's conclusions are quoted with strict inequalities both ways (`τ_θ > τ_q/2` stable, `< ` unstable). The threshold itself (`=`) is not mentioned, so the sentence silently excludes the critical case. The source does treat the condition as the bifurcation; the manuscript should say so. | add "with the critical case at `τ_θ = τ_q/2` not decided by this statement" |
| F10 | `references_local.bib` | `DellOroPata2016Viscoelasticity` has neither volume nor pages (Crossref: Appl. Math. Optim. **76**:641–655). `Abdalla2022` (JHEAp, cosmology) is cited **nowhere** in any of the 37 `.tex` files. | complete the locator; delete the uncited entry |
| F11 | ledger **OCL-207** | Anchor "Kumar et al. (2023), printed p. 17" cannot be right for `Kumar2023PhysScr` (Phys. Scr. **98**:115211, article-numbered, ~11 pp.). The Kumar 2023 PDF I hold is a different paper (PNASI 93:573–585, 13 pp.) and contains no "approximately unity" statement. Claim direction matches the cited title, but the anchor must be re-recorded. | re-record the page, or hold the PDF |

---

## 4. Confirmed items

**F12 (INFO).** The reduction family in `verify_unified_reductions.py` is correct and I reproduced
every substitution from scratch (`B22_verify_reductions.py`, 11/11 independent checks). Two standard
reductions are missing although they hold: `MGT → GN-III flux` at `τ_m = 0`, and
`MGT → LS-type flux` at `k* = 0, τ_0 = τ_m`. Adding them would close the family; nothing false is
asserted by their absence.

**F13.** Tzou (1995) ledger rows OCL-166/167/168 are **CONFIRMED at equation level**. Held PDF
`pdfs/1.2822329.pdf` (9 pp., printed 8–16, footer "10 / Vol. 117"): printed **p. 10** carries
Eq. (15) (the Guyer–Krumhansl-type flux law) and Eq. (17) with `α = τ_R c²/3`, `τ_T = 9τ_N/5`,
`τ_q = τ_R`. The manuscript reproduces both **character for character**, including the printed `+∇T`
sign — which is a *faithful transcription* of a source whose sign differs from the usual GK form.
OCL-444 is also confirmed: the printed p. 8 abstract makes the temporal/spatial lag split the
manuscript attributes to it.

**F14.** Povstenko `.511931`, Eq. (29) on printed **p. 101** with `ζ` as the source coefficient, and
the Caputo remark in Appendix A on printed **p. 113** — both verified on the held PDF. The
manuscript's refusal to map `ζ` to a `Γ`-normalised `τ^α/Γ(1+α)` is correct.

**F15.** Page anchors for Guyer–Krumhansl (p. 766 article, p. 773), Chester (pp. 2014–2015,
Eqs. (5)–(8)), Biot (printed pp. 241–242 carry Eqs. (2.2), (3.x)) and Chandrasekharaiah (printed
p. 705 = review title) all check out against the held PDFs.

**F16.** Bibliography sample: 20 random DOI-bearing keys, **20/20 match** on
title/first-author/volume/pages, zero corrections needed (`B22_BIB_SPOTCHECK.csv`).

**F17. Retraction of an earlier suspicion.** I previously flagged `Povstenko2011` as carrying
`.511931` where it should carry `.511929`. That is wrong: the bib is correct. `.511929` is the
Dirichlet-problem article (34(1):51–67) and `.511931` is the Cattaneo article (34(2):97–114); both
keys carry the right DOI, pages and number. No action.

**F18.** Copied-text sweep (item 5, second half): 1003 manuscript sentences of ≥16 words compared
against 11 held source PDFs by shared 12-token n-grams (threshold ≥3). **Three hits, all
bibliography entries** (arxiv/journal titles of the manuscript's own reference list, p. 121/p. 124).
No body sentence reproduces source wording. Method is crude (token-level, no stemming), so it
supports "no long verbatim borrowings found", not a plagiarism clearance.

---

## 5. Item-by-item answers

1. **Interface re-derivation** — reproduced independently before reading the script
   (`B22_derivation.py`): `r = (Z1−Z2)/(Z1+Z2)`, `t = 2Z1/(Z1+Z2)`, `det = −(Z1+Z2)`,
   `R = (Z1−Z2)²/(Z1+Z2)²`, `T = 4Z1Z2/(Z1+Z2)²`, `R+T = 1`; `(Z1/Z2)|t|² ≠ T` while
   `|r|² + (Z2/Z1)|t|² = 1`; interface-local loss is identically zero for a welded lossless joint;
   remote-plane loss for attenuation `α` over `L` is `4r_z(e^{2αL}−1)e^{−2αL}/(r_z+1)²`.
   Section 10 is **mathematically correct**; the defects are provenance-level (F3, F4) and
   register-level (F5). No sentence in §10 that I read claims the 1D example proves a general
   conservation law — the hedging there is honest and, if anything, over-cautious. One wording
   note: the printed caption of the closure result calls `R+T+A_int=1` "algebraic closure", which
   is right, but a reader may still read "verified" as physical; §10.5.1's explicit warning covers it.
2. **Reductions** — see `B22_REDUCTION_AUDIT.csv`. 12 of 16 audited reductions hold as stated;
   1 is **wrong as printed** (F1, Table 23); 2 MDD rows are **not checkable** (F7); the Quintanilla
   delay condition is **conditional** on the strictness gap (F9). The script itself asserts nothing
   beyond equation-level substitution and says so; no general equivalence is claimed in the text I
   checked. Note the internal inconsistency: the *text* (Table 23) and the *script* disagree about
   the DPL→LS substitution.
3. **Ledger** — 26 class-A + 9 class-V rows (`B22_LEDGER_AUDIT.csv`). No class-A row in my sample
   mixes abstract-level evidence with an equation-level printed sentence: the three abstract-level
   rows (OCL-474/475/476) carry hedged, qualitative sentences, and OCL-045/046 stay class B with an
   explicit "keep hedged" instruction, which the printed text honours. The one genuine
   evidence-to-claim mismatch is on the **V** side, not the A side: OCL-467 (F3). Also worth the
   author's attention: 112 of 126 class-B rows have empty `resolved_by` **and** empty
   `evidence_mode`; that is consistent with B meaning "bounded, not upgraded", but a reader cannot
   tell B-by-choice from B-by-neglect.
4. **Bibliography** — see `B22_BIB_SPOTCHECK.csv`; raw in `crossref_b22/`. F2 is the one real
   defect; F10 the two housekeeping ones.
5. **Forbidden/privacy sweep** — F6 and F18.

---

## 6. Top five risks, in order

1. **F1** — a printed table states a reduction that is false for the manuscript's own DPL law and
   contradicts the project's own script. A referee who checks Table 23 will check exactly this row.
2. **F2** — a bib provenance string that says a page was read and that the DOI was confirmed, when
   the held page gives a different DOI. This is the failure mode the whole v1.1 revision claims to
   eliminate.
3. **F3** — the evidence chain for a printed physical claim runs through a vacuous assertion. The
   claim survives; the credibility of "checked symbolically" does not.
4. **F4** — the net-vs-modal reading of `J_{inc,n}` in Eq. (105)/Eq. (10.13)–(10.14). One clause
   away from being airtight, and it is the sentence most likely to be quoted by a reader who wants
   to replicate the split.
5. **F6/F7** — repository paths in print plus two unsupported table rows together read as
   "internally generated, not internally checked". Cheap to fix; disproportionate cost if left.

---

## 7. Reproduction

```
python3 verification/B22_derivation.py          # interface + cross term + control volume
python3 verification/B22_verify_reductions.py   # independent reduction checks (11/11)
```

Both only need `sympy`. To run the author's scripts you need the full `phase5/master` tree (the
Kumar-split script resolves `parents[2]` and fails if run from an extract). All three author scripts
run clean on the branch tree: `verify_interface_energy.py` (7 PASS), `verify_unified_reductions.py`
(4 PASS), `verify_kumar2017_reference_split.py` (1 line, passes).
