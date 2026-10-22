# V-B7b — open-access full texts read; read_level raised to FULL

**Task item:** B7b of `control/BRAVE_B7.md`. **Access date:** 2026-10-22.
**Scope:** for the open-access papers in the PDF list and in `CITATION_MAP.csv`, read the text
myself, then raise `read_level` to FULL in `LITERATURE_BASE.csv` and record in `CITATION_MAP.csv`
which claims are now supported at full-text level.

---

## 1. Task

> Raise read_level to FULL for every open-access paper in the PDF list and in CITATION_MAP (use only
> legal open archives: arXiv, PMC, publisher OA, institutional repositories); record in
> LITERATURE_BASE.csv and CITATION_MAP.csv which claims are now supported at full-text level.

Standing constraint applied throughout: **OA status is not reading.** A row was upgraded only if I
opened the text in this session. Where what opened was a preprint or an accepted manuscript rather
than the publisher's typeset version, that is stated per row.

## 2. Method

1. Candidate set = the six OA-marked DOIs from the OpenAlex lookups in the B7 PDF-list work, plus the
   OA rows already in `CITATION_MAP.csv` (`Van2018…`, `Quintanilla2019…`, `Rukolaine2014…`,
   `Barak2023Behavior…`).
2. Legal route only: publisher OA (Nature/Sci Rep), arXiv, and an institutional repository
   (UPC `upcommons`). No mirrors, no Sci-Hub, no ResearchGate copies.
3. Read targeted, not cover-to-cover: for each paper I went to the equations and sections that the
   manuscript anchors on, per the "what to check" column of `PDF_REQUEST_LIST.csv`.
4. Compared the manuscript's printed equations against the source **character by character in the
   mathematical content**, allowing only symbol renaming, and recorded the mapping.
5. Updated `LITERATURE_BASE.csv` (`read_level`) only for what I read, with the version read named in
   the cell; updated `CITATION_MAP.csv` (`read_level`) only for claims the reading actually touches,
   naming the source and, where the support is partial, exactly which part is still open.
6. Regenerated `literature_base.bib` (428 keys, unchanged key set — see §5.4).

## 3. Result

### 3.1 What was read, and in which version

| # | Paper | Version read (legal) | `read_level` now |
|---|---|---|---|
| 1 | Barak, Ahmad, Kumar et al. (2023), *Behavior of higher-order MDD on energy ratios at the interface of thermoelastic and piezothermoelastic mediums*, **Sci. Rep.** 13, DOI 10.1038/s41598-023-44339-5 | publisher gold OA (CC-BY) HTML, sections 1–3 + eqs (1)–(11), (42)–(50) | FULL |
| 2 | Chiriţă, Ciarletta & Tibullo (2017), *On the thermomechanical consistency of the time differential dual-phase-lag models of heat conduction*, **Int. J. Heat Mass Transfer** 114:277–285, DOI 10.1016/j.ijheatmasstransfer.2017.06.071 | **arXiv:2103.10068** (submitted version; the journal's version of record is closed) | FULL (preprint) |
| 3 | Quintanilla (2019), *Moore–Gibson–Thompson thermoelasticity*, **Math. Mech. Solids** 24(12):4020–4031, DOI 10.1177/1081286519862007 | **UPC repository** `hdl.handle.net/2117/169798` (accepted version, "reprinted by permission of SAGE") | FULL (accepted version) |
| 4 | Kovács & Ván (2018), *Thermodynamical consistency of the dual-phase-lag heat conduction equation*, **Contin. Mech. Thermodyn.**, DOI 10.1007/s00161-017-0610-x | **arXiv:1709.06825** | FULL (preprint) |
| 5 | Kovács & Ván (2018), *Second sound and ballistic heat conduction: NaF experiments revisited*, **Int. J. Heat Mass Transfer**, DOI 10.1016/j.ijheatmasstransfer.2017.10.041 | **arXiv:1708.09770** | FULL (preprint) |
| 6 | Bongarti, Charoenphon & Lasiecka (2021), *Vanishing relaxation time dynamics of the JMGT equation arising in nonlinear acoustics*, **J. Evol. Equ.**, DOI 10.1007/s00028-020-00654-2 | **arXiv:2011.11141** (preprint of the journal paper) | FULL (preprint) |

`LITERATURE_BASE.csv` now reads `FULL (…)` on exactly 6 of 428 rows: LIT-0042, LIT-0427, LIT-0041,
LIT-0425, LIT-0234, LIT-0211. The other 422 remain `metadata only`. **The 308 blank-author rows are
untouched** (a CI `--enrich` job is Arena's, not mine).

### 3.2 Manuscript equations now traceable to a printed source

**(a) MDD operator and kernel — `sec06_transport.tex:92–105`, eqs (6.7) and (6.8).**
Source eq. (1): `D_τ f(t) = (1/τ)∫_{t−τ}^{t} κ(t−ζ) f′(ζ)dζ`; source eq. (2):
`κ(t−ζ) = 1 − (2β/τ)(t−ζ) + (α²/τ²)(t−ζ)²`, with the three sub-cases printed. The manuscript's
(6.7)/(6.8) are **identical in form** with τ → ω. Support is at second hand in one sense: Sci Rep
2023 is reproducing Wang & Li 2011, not Wang & Li themselves. So the manuscript's own hedge
("inherited candidate") can be replaced by "matches the formulation as reproduced in Barak et al.
2023, eqs (1)–(2)" — which is stronger than nothing and weaker than the primary. Request row 3 stays.

**(b) Piezothermoelastic constitutive pair — `appA_equation_register.tex:85–91`, EQ-027/EQ-028.**
Source eq. (3) `σ_ij = c_ijro e_ro − η_ijr E_r − β_ij T` and eq. (6)
`D_i = ε_ij E_j + η_ijr e_jr + p_i T`, with `E_i = −φ,_{i}` (eq. 5) and `D_i,i = 0` (eq. 7).
The manuscript prints `σ_ij = c_ijkl ε_kl − e_kij E_k − β_ij T` and
`D_i = κ_ij E_j + e_ikl ε_kl + p_i T`. **Same structure, renaming only** (η→e for the piezoelectric
tensor, ε→κ for permittivity, e→ε for strain). Both register entries can move off UNVERIFIED.
*Caution to record:* in the source, `ε_ij` is the **permittivity**; in the manuscript, `ε_kl` is the
**strain**. A reader comparing the two texts will see ε mean opposite things. That is a notational
trap for §9, not an error in either paper.

**(c) Energy flux with the electric term — `energy_flux_derivations.tex:317–344` (OPEN item 10).**
Source eq. (45) prints, in the authors' notation,
`P = −Re(σ₁₃ u̇₁ + σ₃₃ u̇₃ − φ Ḋ₃ + K₃ T̄,₃ T/T₀)`, i.e. the electric term enters with a **minus**
sign as `−φḊ₃`, and the energy ratios follow at eqs (47)–(49). This is the first printed source I have
seen that uses exactly the sign the manuscript's withheld candidate used. One paper is not a
derivation — the manuscript's own OPEN verdict is correct to keep — but the candidate is no longer
unsupported.

**(d) GN flux-law mapping — `sec12_comparative.tex:101,108`.** Two independent full texts agree:
Quintanilla 2019 states type III has `q_i = k*α,_{i} + kθ,_{i}`, with "when k* = 0 we recover the
type I" and "type II is obtained when k = 0"; Sci Rep 2023 Cases 4 and 5 set `K_ij = 0` for GN-II and
retain both terms for GN-III. Therefore **GN-III contains the Fourier term and GN-II does not**, which
is the mapping B6a reported as inverted in Table 12-B (GN-II ↔ Fourier, GN-III ↔ Cattaneo). The B6a
defect now rests on full text rather than on inference from titles.
*Scope of this check:* the GN **flux-law attribution** only. It says nothing about the other rows of
that table.

**(e) DPL truncation orders and admissibility — `sec04:175–213`, CL-024.** Chiriţă et al. 2017:
for approximation order ≥ 5 in either lag "the corresponding characteristic equation has at least a
complex root having a positive real part" ⇒ instability; for orders ≤ 4 the model "can be compatible
with the thermodynamics, provided some appropriate restrictions are assumed upon the delay times";
the admissible set printed in their conclusion is
`(m,n) ∈ {(0,0),(1,0),(0,1),(2,1),(1,2),(2,2),(3,2),(2,3),(3,3),(3,4),(4,3),(4,4)}`.
Cross-referenced against my own tags (V-B2p §2): T2 = (2,1) ✔ in the set, T4 = (2,2) ✔, T3 = (1,2) ✔,
**T1 = (1,1) is absent**. This does **not** contradict V-B2p: T1's "always stable" is a *linear
stability* verdict on the symbol, whereas Chiriţă's set is about *second-law compatibility* of the
constitutive equation. Two different questions. The review must not merge them, and if the manuscript
currently calls first-order-in-both DPL "thermodynamically admissible", that sentence has no support
in the one source that treats the question — flagged for Arena, not adjudicated here.

**(f) MGT is a relaxation of GN-III, not a new family — `sec04:191–200`, CL-025.** Quintanilla 2019
derives the MGT heat equation by inserting a relaxation parameter into the GN-III flux
(eqs (1.3)/(2.4)): `τ q̇_i + q_i = k*α,_{i} + kθ,_{i}`, with `k* = 0` recovering Cattaneo–Maxwell and
`τ → 0` a damped hyperbolic equation; 3-D well-posedness and stability are proved, and the 1-D
analysis gives exponential decay or instability depending on the constitutive parameters. He also
states that GN-III itself "predicts the instantaneous propagation of the thermal waves" — i.e. the
finite-speed motivation for MGT. This directly supports the T1 dating defect: MGT is 1960s acoustics
plus a 2019 re-reading of GN-III, not a 2019 discovery.

**(g) Vanishing-relaxation limit — CL-025.** Bongarti et al., eqs (1.1)–(1.3): `τ>0` gives a
hyperbolic-like third-order system and finite propagation, `τ=0` gives the parabolic Westervelt
equation; they prove **strong** convergence of solutions to Westervelt as `τ→0`, with rates, and note
that semigroup existence for the linearisation fails when the diffusivity is zero. That is the exact
statement CL-025 needed, and it is stronger than the vague "vanishing relaxation limit is delicate".

### 3.3 A literature conflict I could not resolve (recorded, not smoothed over)

Kovács & Ván (arXiv:1709.06825, read earlier this session) conclude that the first-order Taylor
truncation of the DPL law is consistent with the second law when `τ_q, τ_T ≥ 0`; Chiriţă et al.
(§3.2(e)) omit the pair (1,1) from their admissible set. The frameworks differ (thermodynamic
consistency of the constitutive equation via a fading-memory reformulation vs. a direct
second-law test on the truncated operator), and the two statements may therefore be about different
objects — but I have **not** reconciled them and I will not present either as the field's position
until I have. If the manuscript asserts a single verdict on first-order DPL's admissibility, that
sentence is the one to re-examine first.

### 3.4 NaF second-sound evidence — CL-026 / §13

Kovács & Ván (arXiv:1708.09770) re-analyse the NaF second-sound experiments, including the
Jackson–Walker–McNelly samples #607167J and #7204205W, and argue ballistic rather than hydrodynamic
heat transport explains them. This supports the review's §13 sentence that the experimental basis of
second sound required re-interpretation. It does **not** replace the primary sources: the measurement
paper (Ackerman et al. 1966) and the theory papers (Guyer & Krumhansl 1964, 1966) are still
unread — request rows 7, 12, 32.

### 3.5 What changed in the tracking files

`LITERATURE_BASE.csv`: 6 `read_level` cells changed from `metadata only` to `FULL (…)`, each naming
the version read. Row count unchanged at 428; distinct DOIs 428; blank-author rows 308.

`CITATION_MAP.csv`: `read_level` rewritten on **8 of 17** rows — CL-010, CL-013, CL-014, CL-015,
CL-019, CL-024, CL-025, CL-026. The other 9 (CL-006, CL-016, CL-017, CL-018, CL-020, CL-021, CL-023,
CL-027, CL-028) are untouched because none of the six papers bears on them.
Each rewritten cell names the source and, where support is partial, the part that is still open and
the request-row number that would close it. **No `risk` field and no `claim_short` field was altered**;
no verdict in `CLAIM_LEDGER.csv` or `EQUATION_LEDGER.csv` was changed by B7b.

## 4. Evidence / sources

All accessed 2026-10-22.

1. Barak, M. S.; Ahmad, H.; Kumar, R. et al. (2023). *Behavior of higher-order MDD on energy ratios at
   the interface of thermoelastic and piezothermoelastic mediums.* Scientific Reports **13**, article
   `10.1038/s41598-023-44339-5`. https://www.nature.com/articles/s41598-023-44339-5 — **full text,
   gold OA**. (The rendered page did not display the author block; the author string is the Crossref
   record already in `LITERATURE_BASE.csv` as LIT-0042. I did not independently confirm the full
   author list and do not assert it beyond that.)
2. Chiriţă, S.; Ciarletta, M.; Tibullo, V. (2017). *On the thermomechanical consistency of the time
   differential dual-phase-lag models of heat conduction.* Int. J. Heat Mass Transfer **114**:277–285.
   DOI 10.1016/j.ijheatmasstransfer.2017.06.071. Read as **arXiv:2103.10068** (submitted version).
3. Quintanilla, R. (2019). *Moore–Gibson–Thompson thermoelasticity.* Math. Mech. Solids
   **24**(12):4020–4031. DOI 10.1177/1081286519862007. Read as the **accepted manuscript** deposited in
   UPC Commons, `https://upcommons.upc.edu/bitstreams/d8d032a2-dd33-4313-8f4f-dc0c7f2f6470/download`
   (handle 2117/169798).
4. Kovács, R.; Ván, P. (2018). *Thermodynamical consistency of the dual-phase-lag heat conduction
   equation.* Contin. Mech. Thermodyn. DOI 10.1007/s00161-017-0610-x. Read as **arXiv:1709.06825**.
5. Kovács, R.; Ván, P. (2018). *Second sound and ballistic heat conduction: NaF experiments revisited.*
   Int. J. Heat Mass Transfer. DOI 10.1016/j.ijheatmasstransfer.2017.10.041. Read as **arXiv:1708.09770**.
6. Bongarti, M.; Charoenphon, S.; Lasiecka, I. (2021). *Vanishing relaxation time dynamics of the
   Jordan Moore–Gibson–Thompson equation arising in nonlinear acoustics.* J. Evol. Equ.
   DOI 10.1007/s00028-020-00654-2. Read as **arXiv:2011.11141v1** (22 Nov 2020).

## 5. Checks done

1. **Verbatim comparison** of the manuscript's (6.7)/(6.8) against source eqs (1)–(2), and of EQ-027/
   EQ-028 against source eqs (3)–(7), symbol by symbol; the renaming table is in §3.2.
2. **Independent corroboration of the GN mapping** in two full texts (Quintanilla 2019, Sci Rep 2023)
   that do not cite each other for it.
3. **Cross-check of Chiriţă's admissible (m,n) set against my own truncation tags** — which is what
   surfaced the (1,1) absence and the Kovács–Ván tension (§3.3). Done deliberately, because the
   convenient conclusion (that the literature unanimously supports my T-tags) is the one to distrust.
4. **Key stability:** normalising the garbled author strings of LIT-0425 and LIT-0427 ("Robert Kovacs
   and Peter Van"; "Stan Chirita and …") would have **renamed the BibTeX keys** and broken B6c's frozen
   key set (`Van2018Thermodynamical` → `Kovacs2018Thermodynamical`). I therefore **reverted** the
   author-field edit and left the strings as they are; the correct author names are recorded here
   instead (§4 items 4–5: Róbert Kovács, Péter Ván; Stan Chiriţă, Michele Ciarletta, Vincenzo Tibullo).
   `literature_base.bib` regenerated and verified to contain 428 keys including
   `Van2018Thermodynamical`.
5. **Idempotency:** the update script asserts the previous value before writing, so a second run
   cannot silently re-apply or drift; a failed assertion aborted one run mid-way and the state was
   re-read before retrying (recorded so the transcript is not mistaken for a double edit).
6. **No upgrade for the two blocked items** — Wang & Li 2011 and Kumar et al. 2023 — despite both being
   flagged OA. Their `read_level` is unchanged.

## 6. Confidence

- **(a) MDD form, (b) piezo constitutive pair: HIGH** for "the manuscript matches a printed source";
  **MEDIUM** for "the manuscript matches Wang & Li", because the match is to a reproduction.
- **(c) the −φḊ sign: MEDIUM.** One source, one group, and the source is one of the papers the
  manuscript is partly in dialogue with. Consistency, not derivation.
- **(d) GN-II/GN-III flux mapping: HIGH** as a reading of the two texts; **MEDIUM** as a claim about
  how the GN papers themselves label the 1992/1993 sequence (unresolved, request rows 4–5).
- **(e) DPL order ≥5 instability: HIGH** as a reading of Chiriţă et al.; the (1,1) observation is
  **MEDIUM** because it depends on their framework's scope (rigid conductor).
- **(f)/(g) MGT: HIGH** for the derivation route (GN-III + relaxation) and for the strong-convergence
  result being claimed; **MEDIUM** that the preprint versions state what the journal versions state.
- **NaF: MEDIUM** — a re-analysis read at preprint level.

## 7. NOT verified / open issues

1. **All six reads are preprints or accepted versions except the Sci Rep paper.** No publisher
   typeset was opened for items 2–6. Page numbers must therefore not be quoted from this session's
   reading; where I cite a page range it comes from the Crossref record, not from the PDF in hand.
2. **Wang & Li 2011 primary not read.** The bronze OA PDF endpoint refused the request. The manuscript
   equation match is to a secondary reproduction. Request row 3.
3. **Kumar et al. 2023 Phys. Scr. not read** despite a CC-BY-NC-ND flag — IOP served the abstract with
   an access banner. Request row 21.
4. **Kovács–Ván vs Chiriţă on first-order DPL: unresolved** (§3.3). Do not let a later summary collapse
   it into one verdict.
5. **No verdict changed.** B7b upgraded read levels and the evidentiary basis of existing findings; it
   did not re-adjudicate a single ledger row. Re-adjudication is B8 work, after Arena's fixes.
6. **Coupling to elasticity is not covered** by any of these six: all the DPL admissibility results are
   for the rigid heat conductor. Whether the (m,n) and threshold results survive in the coupled
   thermoelastic system is not established by anything I read (V-B2p §7.5 already flagged this).
