# V-B12 — `REFERENCE_PLAN.csv`: what the manuscript should cite, from what base

| field | content |
|---|---|
| **Task** | B12: build the citation plan for the manuscript — ~180–200 records drawn from `LITERATURE_BASE.csv`, each mapped to a manuscript section, a role, a read level, an evidence grade and an own-group flag; plus a separate list of the sections whose primary sources are missing. |
| **Deliverable** | `verification/REFERENCE_PLAN.csv` — **193 rows**, 14 columns. `verification/REFERENCE_GAPS.csv` — **16 rows**. |
| **Result** | 193 of 499 base records selected; **42 of the manuscript's 56 existing cite keys** are backed by a base row and appear in the plan; **77 records are evidence-bearing today** (61 full-text read, 16 partial); **116 are metadata only** and are marked `must_read_first = YES`. |
| **Confidence** | HIGH on the arithmetic and on the key mapping (machine-checked against `REFERENCE_AUDIT.csv` DOIs). HIGH that the 116 metadata rows cannot support a technical claim as the plan stands. LOW on whether those rows, once read, will say what the manuscript needs — that is what the read-before-cite flag is for. |

## 1. How the selection was made

The base is 499 records, of which 404 are `metadata only`. A plan built by "most cited" or "most relevant title" would have looked complete and been evidentially empty. Selection was driven by four rules, in this order:

1. **The manuscript's own 56 cite keys go in first** — by construction these are the standard sources the argument already leans on. 42 mapped to a base row by DOI; 8 have no base row at all and became gap rows; `Guyer1990` is FABRICATED in `REFERENCE_AUDIT.csv` and `Abdalla2022` is OFF-TOPIC, so both are excluded rather than planned.
2. **Quotas per section**, set from the manuscript's section weights: §3: 6, §4.1: 10, §4.3: 9, §4.4: 9, §4.5: 8, §4.6: 8, §4.7: 9, §4.8: 10, §4.10: 8, §4.11: 5, §4.12: 9, §5: 10, §6: 16, §7: 14, §8: 8, §9: 22, §10: 16, §11: 14, §13: 8.
3. **Within a quota, evidence first, then citation count.** Read rows outrank metadata rows, always.
4. **Caps.** Own-group references capped at **18** (achieved: 18). Lotfy-authored records: the base contains **no *Crystals* row at all** — the seven *Crystals* variants met in tier 3 were never added to the base — so the "only one Lotfy variant" rule costs nothing and the plan contains **no** Lotfy record.

## 2. The columns, and why three of them exist

The request was for `lit_id, citekey, proposed_section, role, read_level, evidence_quality, own_group`. Seven columns cannot enforce the two hard rules, so the file carries more:

* **`evidence_grade`** — **A** = full text read this session with equation numbers seen; **B** = partial read (scope, abstract, selected equations); **C** = metadata only.
* **`technical_claim_eligible`** — `YES` only for A and B. **This is the mechanical enforcement of "no NONE or METADATA-only paper may be evidence for a technical claim".** 77 rows YES, 116 rows NO.
* **`must_read_first`** — `YES` for every C row. Such a row may stand in the reference list, but nothing may be asserted on its authority until it is read.
* **`plan_section`** vs **`proposed_section`** — the first is the section the quota accounting placed the row in; the second is the base's own label. They differ for nine rows, see §4.

`citekey` carries its provenance in `citekey_source`: **42** existing manuscript keys, **115** new author-year keys, **36** *provisional* keys built from the title because the base author field is blank. Those 36 will have to be re-keyed on enrichment, and the column says so per row.

## 3. Section coverage — the number that matters

| section | rows | primary | review | method | evidence-ready (A/B) | must read first |
|---|---|---|---|---|---|---|
| s.3 | 6 | 4 | 0 | 0 | 0 | 6 |
| s.4.1 | 10 | 8 | 2 | 0 | 0 | 10 |
| s.4.3 | 9 | 8 | 0 | 1 | 2 | 7 |
| s.4.4 | 9 | 7 | 0 | 2 | 1 | 8 |
| s.4.5 | 8 | 5 | 2 | 1 | 1 | 7 |
| s.4.6 | 8 | 7 | 0 | 1 | 1 | 7 |
| s.4.7 | 9 | 7 | 0 | 2 | 2 | 7 |
| s.4.8 | 10 | 10 | 0 | 0 | 8 | 2 |
| s.4.10 | 8 | 8 | 0 | 0 | 2 | 6 |
| s.4.11 | 1 | 1 | 0 | 0 | 0 | 1 |
| s.4.12 | 9 | 8 | 0 | 1 | 5 | 4 |
| s.5 | 9 | 9 | 0 | 0 | 3 | 6 |
| s.6 | 15 | 14 | 0 | 1 | 9 | 6 |
| s.7 | 14 | 14 | 0 | 0 | 8 | 6 |
| s.8 | 8 | 7 | 0 | 1 | 1 | 7 |
| s.9 | 22 | 22 | 0 | 0 | 22 | 0 |
| s.10 | 16 | 4 | 0 | 12 | 4 | 12 |
| s.11 | 14 | 14 | 0 | 0 | 6 | 8 |
| s.13 | 8 | 2 | 5 | 0 | 2 | 6 |
| **total** | **193** | **159** | **9** | **22** | **77** | **116** |

**Two questions are hidden in this table.** The *rows / primary* columns answer "does the section have 6–8 primary or standard sources to cite?" — yes for every major section except §4.11. The *evidence-ready* column answers "how many can support a technical sentence today?", and there the answer is **under 6 in fourteen of nineteen sections**: §3 (0), §4.1 (0), §4.3 (2), §4.4 (1), §4.5 (1), §4.6 (1), §4.7 (2), §4.10 (2), §4.11 (0), §4.12 (5), §5 (3), §8 (1), §10 (4), §13 (2). That is the honest state of the review and the reason the plan flags rows rather than certifying them.

Three sections deserve a sentence each:

* **§9 is fully evidence-ready (22/22).** The tier-2 reading programme did what it was supposed to do: interface conditions, four-parameter stiffness models and energy-partition papers were read at full-text level.
* **§10 is method-heavy (12 of 16 rows are `method`)** — its records are well-posedness and dissipation papers harvested in B5b-2, not interface energy partitions. §10's own subject, the energy-partition identity at EQ-10.12, rests on **four** primary rows. If §10 is meant to be about energy partition rather than about well-posedness, the section and its evidence are talking past each other.
* **§4.8 is the best classical section (8 of 10 ready)** because the `τ_q²/2` truncation and the `0 ≤ τ_v < τ_θ < τ_q` ordering were found printed in five separate files during the tier-1 and tier-2 batches.

## 4. Correction applied to nine rows

The base's `proposed_section` for the foundational records is a bulk placeholder — `LIT-0002`, `LIT-0003`, `LIT-0004`, `LIT-0007` and `LIT-0035` all carry `s.4.1` and `sub_area = "classical coupled thermo…"`. Used as-is, the plan would have put Lord–Shulman, Green–Lindsay, Green–Naghdi I and Tzou 1995 in the Biot section — which contradicts the section vocabulary `DRIVE_PRIORITY.md` states (s.4.1 Biot, s.4.3 LS, s.4.4 GL, s.4.5–4.6 GN, s.4.7–4.8 DPL/TPL, s.4.10 MGT, s.4.12 two-temperature).

Nine rows were therefore re-labelled by model identity, with the base label kept in `notes`: `LIT-0002` → §4.3, `LIT-0003` → §4.4, `LIT-0004` → §4.5, `LIT-0005` → §4.6, `LIT-0007` → §4.7, `LIT-0035` → §4.11, `LIT-0013` and `LIT-0014` (Joseph, *Heat waves*) → §3, `LIT-0431` (Roy Choudhuri 2007) → §4.8. `LITERATURE_BASE.csv` itself was **not** edited; the correction lives in the plan.

## 5. The gap list (`REFERENCE_GAPS.csv`)

Sixteen rows; eight of them block writing:

| gap | section | what is missing | why it blocks |
|---|---|---|---|
| GAP-01 | s.4.1 | **Cattaneo 1948** | origin of the finite-speed flux law; no base row, no DOI |
| GAP-03 | s.4.4 | **the GL 1972 energy equation as printed** | the base *has* GL (`LIT-0003`) but no equation was ever read, and B4 found the manuscript's eq. (4.9) wrong |
| GAP-04 | s.4.5 | **Green & Naghdi 1992, *JTS* 15, 253** | the GN-II primary under the usual numbering is absent entirely, while `DRV-0185` calls the 1993 paper "model II" — the numbering is contested and the manuscript must declare its own |
| GAP-06 | s.4.7 | **Tzou 1997, ASME JHT 119(1), 110** | the DPL paper itself; key cited 4× in the manuscript, no base row |
| GAP-08 | s.4.10 | **Moore & Gibson 1960** | §4.10 names MGT and has no primary |
| GAP-09 | s.4.11 | **fractional-calculus primaries** | 4 base rows for the whole section and 1 in the plan; Caputo 1967 is the only fractional primary present |
| GAP-10 | s.4.12 | **Chen & Gurtin 1968; Gurtin & Williams** | every 2TT statement traces to these; the base holds only later papers |
| GAP-12 | s.9 | **Achenbach 1973** | the energy-flux / average-intensity definition behind every ratio; key cited 11×, no base row |

Non-blocking but recorded: Vernotte's page numbers (GAP-02), GN 1993 as printed (GAP-05), Chiriţă et al. 2016 tensor-form admissibility (GAP-07), the NaF re-analysis existing only as a preprint (GAP-11), Nowacki 1975 (GAP-13), one thermoelastic quasicrystal primary for §13 (GAP-14), and the two removals — `Guyer1990` (fabricated, already replaced by LIT-0008/0009/0010/0011) and `Abdalla2022` (off-topic).

## 6. Exclusions applied

* **Preprints and review copies:** base rows `LIT-0211`, `LIT-0234`, `LIT-0425` excluded. `LIT-0470` was *not* excluded — its `why` mentions a preprint only because it supersedes one.
* **Fabricated / off-topic:** `Guyer1990`, `Abdalla2022`.
* **Own-group:** 22 base records flagged; 18 in the plan (cap respected).
* **Lotfy:** no *Crystals* row exists in the base; no Lotfy record in the plan.

## 7. Checks done

1. Key mapping by DOI, machine-checked; the 8 no-DOI keys were then tried by surname+year and, failing that, recorded as gaps rather than guessed.
2. Section quotas asserted; 193 rows delivered.
3. No duplicate `citekey`; no duplicate `lit_id`.
4. Own-group count asserted ≤ 18 after selection.
5. `evidence_grade` derived mechanically from the base `read_level`; every C row has `must_read_first = YES` and `technical_claim_eligible = NO`; consistency asserted (0 inconsistent rows).
6. No preprint or review-copy row survived into the plan (asserted).
7. Row width asserted equal to header on write for all five CSVs touched this turn.

## 8. NOT verified / open issues

* **This is not a citation audit.** Grade A means the paper was read; it does not mean the paper supports the sentence the manuscript will write with it.
* **36 keys are provisional** because the base author field is blank; they will change on enrichment.
* §4.11 has one row and no evidence-ready source. §10's role mix needs a decision from the author — energy partition or well-posedness, not both under one heading.
* The plan does not touch the manuscript, per the verifier's mandate.
* `LITERATURE_BASE` is 499 after the four B10e promotions; every count here is against 499, not the 495 quoted in earlier files.
