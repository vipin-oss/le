# V-B16b — section-12 labelling fix and the missing-sources request list

**Batch:** B16b. **Date:** 2026-10-23. **Base:** `arena/04fdf32e-le` @ `1e4941d` (accepted), fresh fetch of `claude/control` @ `33e92d5`.
**Deliverables:** `PDF_REQUEST_LIST_3.md` (36 items), `api_log/B16B_openalex_checks.csv` (31 verified records), `REFERENCE_PLAN.csv` relabelled, `REFERENCE_GAPS.csv` GAP-22 updated.

## Task

1. Fix the section-12 labelling defect: comparative papers must carry `plan_section` s.12.
2. Build `PDF_REQUEST_LIST_3.md` (~40 items, prioritised) for the sections carrying GAP-18…GAP-25 — s.5 (multiphysics / piezothermoelastic coupling), s.8 (mathematical methods), s.10 (energy flux / partition), s.11 (fractional), s.12 (comparative surveys), s.4.9 (MGT) — each item with a Crossref/OpenAlex-verified DOI, journal, volume/pages, an OA link where one exists, and the gap it fills; items without a verifiable DOI labelled "NO DOI - printed source".
3. Order: OA first (the handler can download those directly), paywalled second.

## Method

- **Label audit:** every `REFERENCE_PLAN` row was scanned for comparative/review/survey wording in its title or notes; the misfiled ones were found in s.7 (a gradient-elasticity overview) and s.4.1 (a review of generalized thermoelasticity models). Two comparative papers that had **no plan row at all** were added. Nothing was duplicated: a `lit_id` appears once, so a misfiled paper was **moved**, with the move written into its `notes`.
- **Identifier verification:** DOIs were queried in batches against `api.openalex.org/works?filter=doi:…&select=doi,title,publication_year,biblio,open_access`. A record that came back supplied the title, year, volume, first–last page and the OA verdict used in the list. **A DOI that returned nothing, or returned a different paper, was discarded** — this happened four times (see "Corrections" below). Where a guessed DOI failed, a `title.search` query was run instead; where that also failed, the item was left out rather than listed on a guess.
- **OA column:** taken from OpenAlex `open_access.oa_status` / `oa_url`. No Unpaywall pass was run beyond that; the list says so.

## Result

### A. Section 12 is now labelled (4 rows, was 0)

| row | move | why |
|---|---|---|
| `LIT-0026` — Askes & Aifantis, gradient elasticity overview | **s.7 → s.12** | an overview that compares gradient-elasticity variants; it is not a primary model source |
| `LIT-0040` — Shakeriaski et al., *Recent advances in generalized thermoelasticity theory and the modified models: a review* | **s.4.1 → s.12** | a review; it was never a section-4.1 primary, and it is unread anyway |
| `LIT-0307` — MDD vs fractional (IV) | **added, s.12** | had no plan row; comparative by construction |
| `LIT-0428` — van der Merwe et al., DPL vs Cattaneo–Vernotte vs Fourier | **added, s.12** | the cleanest side-by-side comparison available; now `must_read_first=YES` |

`GAP-22` was rewritten to say "partly fixed — four rows, all metadata-only, none eligible yet", because four rows are not six read sources. Section 4.1 drops to nine rows and section 7 to thirteen; **no eligible count changed**, since both moved rows were already ineligible.

### B. The request list (36 items: 11 OA, 20 paywalled, 5 print)

- **Part A, open access (11):** Caputo 1967 (this one item unblocks the whole fractional section); Sherief–El-Sayed–Abd El-Latief 2010; Wang & Li (I) and (IV); **Shakeriaski et al. 2021 — which is `LIT-0040`, already in the plan and never read**, because the library file with a similar name is a different paper; Dubner & Abate 1968 and Stehfest 1970 (the two Laplace-inversion algorithms the state-space literature uses); Lasiecka & Wang 2015 and 2016; Dell'Oro & Lasiecka 2016; Quintanilla 2019 (already read, link recorded).
- **Part B, paywalled but verified (20):** the micropolar/void/piezothermoelastic core for s.5 (Mindlin 1974, Nowacki 1978 and 1984, Cowin & Nunziato 1983, Nunziato & Cowin 1979, Iesan 1986); the mathematical-methods core for s.8 (Stroh 1958 and 1962, Chadwick & Sneddon 1958, Joseph & Preziosi 1989 and its addendum, Hetnarski & Ignaczak 1999); an energy-flux paper for s.10; Povstenko 2009 and two fractional books for s.11; Marchand–McDevitt–Triggiani 2012 and van der Merwe 2021; Moore & Gibson 1960 (already read, listed for completeness).
- **Part C, print-era (5):** Mindlin 1961, Tiersten 1969, Achenbach 1973, Auld 1973, Ignaczak & Ostoja-Starzewski 2010 — all marked **NO DOI — printed source**, with the Achenbach warning about the WITHDRAWN Elsevier chapter DOIs carried over from the earlier audit.

### C. Corrections made while verifying (four guessed DOIs were wrong)

| my guess | what it actually is | consequence |
|---|---|---|
| `10.1007/BF01173644` "Chandrasekharaiah 1988, piezoelectric thermoelasticity" | a 1980 paper on persuasive communication | discarded; **Chandrasekharaiah 1988 is not in the list** |
| `10.1080/01495737808926942` "Nowacki 1978, general theorems" | a 1978 magnetothermoelasticity paper | discarded; the correct DOI is `…08926940`, found by title search |
| `10.1145/321439.321449` "Dubner & Abate" | *A Permutation Network* | discarded; the correct DOI is `…321446` |
| `10.1080/14786435808237006` "Stroh 1958" | a 1958 fluid equation-of-state paper | discarded; the correct DOI is `…08565804` |

This is the reason the list was assembled DOI-by-DOI rather than from memory: four of my first guesses resolved to real, unrelated papers, which is exactly how a fabricated citation gets into a bibliography.

### D. Items deliberately **not** listed

- **Thompson 1972** — F14 names it with Moore & Gibson 1960, but no 1972 Thompson paper on relaxing-gas acoustics with a DOI surfaced. Excluded, with a line in the list telling the authors not to cite it until it is identified.
- **Chandrasekharaiah 1988** — no verified identifier (see table above).
- **s.13 second-sound primaries** (Chester 1963, Sham 1967, Chandrasekharaiah 1986) — outside this batch's scope and not searched; the list says so rather than implying they were checked.

## Evidence / Sources

Every DOI in the list and in `api_log/B16B_openalex_checks.csv` was resolved on 2026-10-23 through the OpenAlex API; that file records the DOI, the title as returned, year, venue, volume, pages, OA status and OA URL for 31 records, so any entry can be re-checked without re-querying. Prior context: `V-B16_batch1_applications.md`, `R3_STATUS.md` @ `arena/b5e608f8-le` `3092fa3`, `control/FULLTEXT_FINDINGS_04.md` F14.

## Checks done

- **Every DOI machine-verified**; nothing carried over from memory. Four wrong guesses caught and replaced.
- **Titles matched, not just resolved:** a record whose title did not match the intended paper was rejected even though the DOI existed (the four above).
- **No duplicate ordering:** A5 = `LIT-0040`, A11 = `LIT-0041`, B15 = `LIT-0007`-adjacent, B20 = the F14 paper — each flagged in its row so the handler does not buy twice.
- **Plan integrity after the relabel:** 206 rows, no duplicate `lit_id`, section counts re-counted (`s.12` 4, `s.4.1` 9, `s.7` 13, `s.5` 10, `s.8` 8, `s.10` 16, `s.11` 15); columns unchanged.
- **Gap integrity:** 25 rows, GAP-22 status rewritten rather than deleted, so the original defect stays auditable.

## Confidence

- **HIGH** for all 31 machine-verified identifiers and for the OA/closed verdicts (single source, OpenAlex, queried today).
- **HIGH** that the s.12 relabel is correct: the four papers compare models or summarise a family; none is a primary derivation.
- **MEDIUM** for the five Part-C entries: the works are standard and certainly exist, but publisher, edition and page ranges were **not** re-verified this session, and the list says so.
- **LOW** for anything about whether these papers actually contain what the sections need — none of them has been read. The list is a shopping list, not evidence.

## NOT verified / open issues

1. **None of the 36 has been obtained yet.** No `FULLTEXT_FACTS` row, no `technical_claim_eligible=YES`, no `read_level` change was made on the strength of this list.
2. **Thompson 1972** remains unidentified and uncitable.
3. **Chandrasekharaiah 1988** remains unidentified.
4. **s.13's six second-sound primaries were not searched** in this pass; `GAP-23` stands unchanged.
5. **OA status can change**; OpenAlex reports it as of 2026-10-23.
6. **Section 12 still has four metadata-only rows** — the labelling defect is fixed, the evidence defect is not. Six read comparative sources are needed and five of them are in this list (A3–A5, B12, B19).
7. **Unpaywall was not queried separately** for the paywalled items; a green copy may exist for some.
