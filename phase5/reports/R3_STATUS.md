# R3 evidence-verification and build status

**Current R3a result:** 81 rows; **77 VERIFIED / 3 MISMATCH / 1 NOT-FOUND**. The R3a comparison was regenerated only from the 81 saved Crossref JSON responses; no new R3a requests were made. R3b is verified dynamically by the single strict CI run associated with the `[R3B-CROSSREF]` content commit.

## R3a verification — Sections 4.1–4.12

The same saved JSON was re-evaluated under the documented relaxed title, venue, and date comparison rules. **Nineteen** rows record `reclassified_from=MISMATCH`. Final R3a result: **77 VERIFIED / 3 MISMATCH / 1 NOT-FOUND**. Among technically eligible rows, **21 are VERIFIED and bibliography-ready, 0 are MISMATCH, and 1 is NOT-FOUND**. The 21 eligible sources are cited only for their mapped, model-specific claims; conditional and secondary-source labels remain in force. `Chandrasekharaiah1998` is the one additional BibTeX-ready Crossref record, cited only as `SECONDARY-SOURCE` historical background, never as equation-level evidence.

The three unresolved Crossref metadata mismatches are `Iesan2013` (venue mismatch), `Zenkour2016` (venue mismatch), and `Masui2025` (venue mismatch). `Youssef2018` is NOT-FOUND (Crossref HTTP 404) and remains uncited. The R3a title-overlap human-check list has **zero candidates**; the 404 is not a title-match human-check case. See `CROSSREF_VERIFY.csv`, `CROSSREF_METHOD.md`, and `CROSSREF_HUMAN_CHECK.md` for the full comparison and provenance.

### R3a evidence-ready counts by plan section

| Plan section | Verified, technically eligible and bibliography-ready sources | Status / gap |
|---|---:|---|
| 4.1 | 0 | No eligible verified source in scope |
| 4.2 | 0 | No eligible verified source in scope |
| 4.3 | 2 | Lord–Shulman; model-specific fractional/nonlocal LS variant |
| 4.4 | 1 | Rate-dependent two-temperature comparison |
| 4.5 | 1 | Rheological network comparison; no admissibility claim inferred |
| 4.6 | 1 | Nonlocal GN-III variant |
| 4.7 | 2 | Distinct second-order DPL truncations; no universal ordering inferred |
| 4.8 | **8** | Multiple distinct TPL/DPL variants; not a single universal law |
| 4.9 | 0 | No plan row labelled 4.9; MGT source is mapped at plan s.4.10 and cited in the MGT subsection |
| 4.10 | 2 | MGT and memory-dependent/fractional comparison |
| 4.11 | 0 | No eligible verified source in scope |
| 4.12 | 4 | Comparative two-temperature examples; `Youssef2018` is NOT-FOUND and uncited |

Only section 4.8 reaches six evidence-ready R3a sources. Gaps are not padded with unverified records.

### No-DOI printed-source leads

Cattaneo (1948), Vernotte (1958), Achenbach (1973), Nowacki (1975), and Tzou (1997 book) remain separately identified as **“NO DOI - printed source”**. No DOI was invented or assigned to these leads.

## R3b verification and evidence

- Scope: 90 REFERENCE_PLAN rows from sections 5–9 and 11–13; 47 technically eligible DOI rows queried; 47 unique Crossref requests.
- R3b Crossref results: 40 VERIFIED, 5 MISMATCH, 2 NOT-FOUND, 4 NO-DOI; 39 metadata-only rows INELIGIBLE and not queried.
- Technical-eligible R3b rows: 39 VERIFIED and bibliography-ready; 1 VERIFIED but not bibliography-ready; 4 NO-DOI; 5 MISMATCH; 2 NOT-FOUND.
- R3b mapped citations inserted: 39 unique verified eligible keys; new BibTeX keys added in this build: 35. No metadata-only or unverified row is inserted as technical evidence.
- Sections meeting ≥6 evidence-ready sources across R3a/R3b: 4.8 (8), 6 (7), 7 (6), 9 (19).
- R3b human-check list: `CROSSREF_R3B_HUMAN_CHECK.md`.
- R3a final counts after cached-response reclassification: 77 VERIFIED / 3 MISMATCH / 1 NOT-FOUND; 19 rows record `reclassified_from=MISMATCH`; 21 technical-eligible bibliography-ready keys; 1 background-only review key.
- R3a title human-check list: `CROSSREF_HUMAN_CHECK.md`.
- Frozen `CITATION_MAP.csv` exact-key matches in the R3b candidate set: 0. Section-specific additions are mapped in `R3B_CITATION_MAP.csv` from the eligible plan rows and their documented source claims.
- Remaining gaps: Section 10 is reserved for R3c; Section 11 GAP-09 remains open; R3b MISMATCH, NOT-FOUND, and NO-DOI rows remain uncited. R3b rows with a title overlap below 0.60 are in `CROSSREF_R3B_HUMAN_CHECK.md`.

### R3b unresolved identifiers (not cited)

- LIT-0439 `Guo2019` — MISMATCH: normalized venue does not match Crossref container-title/short-container-title
- LIT-0442 `Deswal2015` — MISMATCH: normalized venue does not match Crossref container-title/short-container-title
- LIT-0443 `Ezzat2012` — MISMATCH: normalized venue does not match Crossref container-title/short-container-title
- LIT-0029 `Wang2011` — MISMATCH: normalized venue does not match Crossref container-title/short-container-title
- LIT-0438 `Quintanilla2009` — MISMATCH: normalized venue does not match Crossref container-title/short-container-title
- LIT-0457 `Faleh2020` — NOT-FOUND: Crossref returned HTTP 404
- LIT-0440 `Kumar2017a` — NOT-FOUND: Crossref returned HTTP 404
- LIT-0499 `Hu2000` — NO-DOI: no DOI recorded; not Crossref-verifiable; keep uncited under this phase
- LIT-0437 `Eringen1978` — NO-DOI: no DOI recorded; not Crossref-verifiable; keep uncited under this phase
- LIT-0484 `Singh2021` — NO-DOI: no DOI recorded; not Crossref-verifiable; keep uncited under this phase
- LIT-0485 `Kumar2020` — NO-DOI: no DOI recorded; not Crossref-verifiable; keep uncited under this phase
- LIT-0471 `Bassiouny2021` — VERIFIED: Crossref author metadata is empty; do not emit BibTeX

## R3c verification and evidence

- Scope: REFERENCE_PLAN s.10 and s.4.11; Section 10 has 4 technical-eligible rows and 12 ineligible plan rows not queried; Section 4.11 has 1 plan row(s), 0 eligible; 13 total rows across both sections are INELIGIBLE and unqueried.
- R3c new Crossref results for s.10 eligible rows: 3 VERIFIED, 1 MISMATCH, 0 NOT-FOUND, 0 NO-DOI.
- Verified and bibliography-ready s.10 eligible rows: 2; new-request citations inserted: 2; verified carry-forward s.10 citations reused from R3b: 1; new BibTeX keys added: 2.
- Kumar2017 is carried forward from R3b only because its plan row is technically eligible, proposed_section includes s.10.5, and R3b marked it VERIFIED/bibliography-ready: used.
- Barak 2023 Eq. (6.14) is not cited: its local BibTeX record has no technically eligible REFERENCE_PLAN row. No new citation is created from that record.
- Frozen CITATION_MAP exact-key matches among R3c s.10 eligible sources: 0. Claim IDs CL-013/014/015 are used as topic anchors in `R3C_CITATION_MAP.csv`; that file states the local plan-note rationale and does not imply supplied-map key matches.
- Sections meeting ≥6 evidence-ready sources across R3a/R3b/R3c: 4.8 (8), 6 (7), 7 (6), 9 (19).
- Limited primary sources are available for s.10 energy partition and s.4.11 fractional thermoelasticity. Section 10 Eq. (10.12) remains conditional/model-specific; own-group numeric observations are not presented as exact identities. Section 4.11 receives no technical citation because its only plan row is metadata-only.
- GAP-09, GAP-12, and GAP-13 remain open. Section 10 identity conditions, Section 4.11 fractional-source/admissibility questions, and all R3b unresolved rows are not closed by metadata verification alone.
- R3c title human-check list: `CROSSREF_R3C_HUMAN_CHECK.md`.
- R3c unresolved eligible rows (not cited):
  - LIT-0490 `De2020` — MISMATCH: normalized venue does not match Crossref container title
- R3c technically eligible but not cited because no claim mapping was authorized by the local map:
  - LIT-0432 `Aldawody2019` — Crossref VERIFIED; verified eligible source has no R3C_CITATION_MAP include=YES mapping; metadata only

## R3d verification and manuscript updates

- Scope: nine newly eligible REFERENCE_PLAN rows across s.4.9, s.4.10, s.5, s.11, and s.12; Crossref requests were dynamic in CI only.
- R3d Crossref: 9 VERIFIED, 0 MISMATCH, 0 NOT-FOUND, 0 NO-DOI; mapped and bibliography-ready: 9; unique mapped citations used: 9; new BibTeX keys: 5.
- Frozen CITATION_MAP exact-key matches among R3d candidates: 0. Each placement is separately auditable in `R3D_CITATION_MAP.csv`.
- Frozen REFERENCE_READINESS snapshot: s.4.9: 3 full/primary, 0 partial of 3 eligible; s.4.10: 2 full/primary, 0 partial of 2 eligible; s.5: 4 full/primary, 1 partial of 5 eligible; s.11: 9 full/primary, 1 partial of 10 eligible; s.12: one secondary / zero primary.
- Unique VERIFIED primary-source coverage by touched section after R3d (plan role excludes secondary surveys): s.4.9=4, s.4.10=3, s.5=4, s.10=3, s.11=5, s.12=0.
- Sections meeting the ≥6 VERIFIED primary-source bar across R3a/R3b/R3c/R3d: s.4.8 (8), s.6 (7), s.7 (6), s.9 (18).
- Section 4 separates thermoelastic MGT admissibility from acoustic MGT-with-memory decay; the acoustic gamma condition is not transferred to thermoelasticity. Section 5 cites Mindlin's Fourier thermopiezoelectric baseline and treats generalized Fourier limits as model-specific checks.
- Section 11 attributes the fractional operator's origin to viscoelasticity/geophysics, cites Sherief's operator on both rate terms, names the Gamma-normalized review convention, and attributes the MDD/FD contrast to Wang and Li (2021, Part I). Section 12 uses LIT-0040 as SECONDARY coverage only.
- 'Limited primary sources' is stated for the touched subsections with fewer than six primary sources; LIT-0040 is not counted as primary. GAP-09, GAP-12, and GAP-13 remain open; no gap is closed by metadata verification alone.
- R3d title human-check list: `CROSSREF_R3D_HUMAN_CHECK.md`.
- R3d unresolved identifiers (not cited):
  - None.

## R3e verification and Section 8 update

- Scope: only the two requested DOIs were queried; no other Crossref records were requested.
- R3e Crossref: 2 requested DOI rows; 2 VERIFIED, 0 MISMATCH, 0 NOT-FOUND, 0 NO-DOI; bibliography-ready: 2; mapped citations used: 2; new BibTeX keys: 2.
- Section 8 uses the checked Dubner--Abate Eq. (15) cosine/trapezoidal formula and/or Stehfest's even-N weights only when that row is Crossref-VERIFIED and bibliography-ready. Stehfest is restricted to the paper's stated rounding-error/N trade-off; no behavior inference is attributed to him.
- These two source-specific methods do not establish a broader comparison or ranking. Limited primary sources remain the stated scope for numerical Laplace inversion in Section 8.
- R3e unresolved rows (not cited):
  - None.

## R3f verification and manuscript update

- Scope: 24 mapped DOI works were queried; Cattaneo (1948) is separately recorded as NO-DOI and was not requested.
- R3f Crossref: 25 status rows; 21 VERIFIED, 3 MISMATCH, 0 NOT-FOUND, 1 NO-DOI; 24 requests; bibliography-ready: 21; citations selected only from VERIFIED/bibliography-ready rows; new BibTeX entries: 18.
- Cattaneo1948 venue corrected to Atti Sem. Mat. Fis. Univ. Modena 3:83--101 (1948), retained as `verified = {NO_DOI}`; Joseph--Preziosi (1989) prints a different page value, noted in the BibTeX verification note.
- Per-section checked-source counts (R3f read sources pass both the findings and Crossref gates; eligible-primary counts are shown separately):
  - s.2: 2 verified/read source(s), 0 eligible primary; updated cumulative eligible-read count not previously reported.
  - s.4: 1 verified/read source(s), 0 eligible primary; updated cumulative eligible-read count not previously reported.
  - s.4.9: 0 verified/read source(s), 0 eligible primary; updated cumulative eligible-read count 4.
  - s.4.10: 0 verified/read source(s), 0 eligible primary; updated cumulative eligible-read count 3.
  - s.5: 5 verified/read source(s), 5 eligible primary; updated cumulative eligible-read count 9.
  - s.8: 5 verified/read source(s), 5 eligible primary; updated cumulative eligible-read count 8.
  - s.10: 3 verified/read source(s), 1 eligible primary; updated cumulative eligible-read count 6.
  - s.11: 2 verified/read source(s), 0 eligible primary; updated cumulative eligible-read count 7.
  - s.12: 5 verified/read source(s), 5 eligible primary; updated cumulative eligible-read count 5.
- Sections at/above six eligible read sources: s.5=9, s.8=8, s.10=6, s.11=7. Sections below six: s.4.9=4, s.4.10=3, s.12=5. Scope notes were changed only for threshold-crossing sections; Section 4's MGT count excludes the acoustic Marchand source.
- Durbin's interval/error statement and Honig--Hirdes performance comparison are source-specific; Stroh is identified as purely elastic; no unsupported general ranking or thermoelastic attribution is added.
- The 1999 five-model experimental statement is explicitly dated. The C--T DPL thermoelastic attribution is kept distinct from Tzou's 1995 heat-law paper. The fractional-Cattaneo attribution to Povstenko (2011) remains CONDITIONAL.
- R3f unresolved Crossref rows before R3g arbitration (not newly cited/added in R3f): `ChadwickSneddon1958` (author mismatch), `HetnarskiIgnaczak1999` (author mismatch), and `Gorenflo1997` (venue mismatch); R3g separately arbitrates and cites these records.
- R3f corrective strict CI: content commit `2d5dc6bb46f133dc65c9536684d6d10bea05163e`, run `39988876745`, 160 pages, 0 undefined references/citations; strict layout gate passed.

## R3g supervisor arbitration, citations, and process-language audit

- Crossref verification rules were not changed. The three R3f registry rows remain `MISMATCH` in the original Crossref CSV; supervisor arbitration against the printed first pages designates each separately as `VERIFIED-BY-ARBITRATION` for citation use.
- `ChadwickSneddon1958`: Crossref's `Snedon` is corrected to printed `Sneddon`; `HetnarskiIgnaczak1999`: bibliography follows printed Richard B. Hetnarski and Jozef Ignaczak; `Gorenflo1997`: corrected chapter title, CISM anthology/volume, pages, and DOI follow the printed PDF. All three BibTeX records carry `verified = {ARBITRATED (supervisor, printed PDF)}`; reasons are in `CROSSREF_R3F_HUMAN_CHECK.md`.
- Added the arbitration-tagged source claims in Sections 2, 8, and 12; the Section 8 account is qualitative only for Chadwick--Sneddon, and the Hetnarski experiment statement is explicitly dated to 1999.
- Per-section verified/read source counts (primary-read count shown separately), combining R3f and R3g: s.2 4/0; s.4 1/0; s.4.9 0/0; s.4.10 0/0; s.5 5/5; s.8 7/6; s.10 3/1; s.11 2/0; s.12 6/5. Updated cumulative eligible-read counts: s.4.9=4, s.4.10=3, s.5=9, s.8=10, s.10=6, s.11=7, s.12=6; previous cumulative totals for s.2 and s.4 were not reported.
- Process-language inventory: `phase5/reports/PROCESS_LANGUAGE_INVENTORY.csv`, 162 line/phrase rows. Counts by phrase: eligible=5; read sources=4; R3=35; GAP-=11; UNVERIFIED=50; BACKGROUND-ONLY=1; SECONDARY-SOURCE=14; PRIMARY-SOURCE-CHECKED=38; supervisor=0; Brave=0; now has=4. Inventory records source file, line, phrase, and section; it did not drive manuscript edits.
- R3g content/source commit: `524c4b0f1579ffaad52543e8d9f44017f5645d0b`; infrastructure-only fix commit: `d81e99dcd522d1bf3c0d237d0b1a61578f71c09b`.
- Strict build after the infrastructure fix: run `40063975977` passed in 2m22s; PDF pages: 162; the >1 pt layout gate passed. (No R3a–R3f apply steps ran.)
- Report-only strict build metrics: run `40064319885`; build step `16` seconds; pages `162`; undefined references/citations `0`.
- Near-overfull warnings above 0.5 pt: `none`.
- Uncommitted local edits at content-commit time: none; all R3g changes and the inventory were included in that commit.

## Final strict build

The R3g strict build passed after the infrastructure-only TeX installation fix. The report-only run below captures the final warning inventory.

- Result: PASSED; the strict >1 pt layout gate passed.
- R3g content/source commit: `524c4b0f1579ffaad52543e8d9f44017f5645d0b`
- First strict CI run after the fix: `40063975977` (162 pages; workflow duration 2m22s)
- Report-only strict CI run: `40064319885`
- Build-step time: `16` seconds
- PDF pages: `162`
- Undefined references/citations: `0`
- Near-overfull warnings (>0.5 pt): `none`
- Section 8 lines 100–101: strict >1 pt gate passed; the warning inventory above records any residual overfull box above 0.5 pt after `\emergencystretch`.


The preserved R1/R2 baseline remains commit `0be9322`, CI run `39781561017`, 149 pages, and zero undefined references. MISMATCH, NOT-FOUND, and out-of-scope literature records are intentionally not promoted to citations; the undefined-reference count is a separate LaTeX build metric.

## B20 reconciliation addendum (2026-10-24; Arena, independent source follow-up)

Current R3 state: **NOT PASSED**. The earlier R3g s.12 `6 verified / 5 primary` count is retained as historical reporting only and is superseded by the authoritative `REFERENCE_READINESS.csv` count of **3/6**; GAP-22 remains OPEN. No authoritative plan/control file or manuscript file was changed.

B20 D1–D9 are preserved in `phase5/reports/scientific-audit.md`, including the FW-013 `.778` primary-source flag (corrected in the matrix to OPEN/UNVERIFIED), stale Gurtin–Williams status prose, the OPEN Gurtin–Williams 1966 versus Chen–Gurtin–Williams 1969 attribution question, the Chen–Gurtin descriptor mismatch, 97-row arithmetic, superseded failed build, and the 162-page/zero-`??` PDF check. Relevant source pages were directly inspected for Guyer–Krumhansl `.766` (printed pp. 766, 773), Povstenko `.511931` (pp. 97, 101, 113), the 2015 book's copyright page, and Chester (pp. 2013–2015). The equation/page outcomes and access limits are recorded in the scientific audit; no claim was transferred to a different paper.

The PDF contains visible process/status labels. Literal whole-PDF extraction counts and exact page sets are recorded in the scientific audit; the 40/9 counts differ by one from B20's section-file 39/8 counts, and the parser/file-scope discrepancy remains unresolved. The scan includes status-definition text on pp. 145 and 150, but that alone does not explain the difference. Blueprint requires status tags but does not decide whether they belong inline in referee-facing prose or in audit artifacts. This is an editorial blocker, not a manuscript change made here. The stale R3f Gurtin–Williams title is likewise retained only as history; the 1966 bibliography title is *On the Clausius–Duhem Inequality*. The Section 12 content/attribution question remains OPEN pending the candidate papers' relevant pages.

All five mandatory gaps (GAP-09/12/13/22/23) remain OPEN. The local bibliography still contains the Guyer–Krumhansl `.766` title/`.778` DOI-pages mismatch, `Povstenko2011` `.511929` citekey versus `.511931` source mismatch, and the unresolved `Povstenko2016` year/ISBN/DOI mismatch. Their identity findings are recorded, but bibliography and manuscript edits were out of scope; no R4 work started.

## Post-B20 bounded R3 remediation (2026-10-24)

The B20 history above is preserved; this update supersedes only its statements that the Guyer `.766` record, Section 11 Povstenko citation, and D4/D5 status labels were unchanged. Current state remains **R3 NOT PASSED**.

- Corrected `GuyerKrumhansl1966` to the verified `.766` paper: *Solution of the Linearized Phonon Boltzmann Equation*, *Physical Review* 148(2):766–778 (1966), DOI `10.1103/PhysRev.148.766`. `.778` is the separate companion article *Thermal Conductivity, Second Sound, and Phonon Hydrodynamic Phenomena in Nonmetallic Crystals*, pp. 778–788, DOI `10.1103/PhysRev.148.778`; FW-013 remains OPEN/UNVERIFIED and no equation support is transferred.
- Added `Povstenko2011Cattaneo` for the verified `.511931` article, DOI `10.1080/01495739.2010.511931`, and retargeted only the fractional-Cattaneo claims in Section 11. The original `Povstenko2011` remains the distinct `.511929` Dirichlet-problem article and remains cited for the radial-domain discussion. The local `Povstenko2016` book entry was left untouched: the supplied 2015 book record and local 2016/ISBN record remain discrepant, and edition equivalence is not established.
- Eq. (29), printed p. 101, supports a related fractional Cattaneo law with coefficient `zeta` and a Caputo derivative (Appendix A, p. 113). It does not support the exact `tau^alpha/Gamma(1+alpha)` prefactor. The related-law statement is checked; the exact prefactor mapping and Eq. 11.4 attribution remain CONDITIONAL/OPEN.
- Section 12 claims and citations at `sec12_comparative.tex:20,22` are unchanged; the labels were downgraded to UNVERIFIED because the candidate source pages were unavailable. They render on PDF p. 92. D4/D5 remain OPEN; the identified candidates and missing pages are documented in `scientific-audit.md`.
- Criteria unchanged: GAP-09 is partly closed but still open; GAP-12 and GAP-13 remain open; GAP-22 remains at authoritative 3/6; GAP-23 remains open. No gap was closed by metadata or a related-source location.
- Updated the source-line process inventory to 164 rows and documented the exact PDF/source crosswalk, whole-PDF counts, extraction limitations, and unresolved B20 parser/scope difference in `scientific-audit.md`. No process label was silently removed. Blueprint leaves the reader-facing versus internal-audit placement ambiguous; no relocation was made.
- Source commit `850d2b546931dc21faef5a57b2de09d425090175`; strict CI run `40075893625` succeeded, configured layout/build gates passed, PDF page count 162. Publication commit `5606ac460e41c79dd746aa66a45448a69a12be34`. The PDF text has no literal `??` artifacts. This does not satisfy the outstanding scientific evidence gates.

No authoritative plan/criteria or control-owned file was edited; no R4 work started. **R3 NOT PASSED.**

## B21 provenance-backed bibliography reconciliation (2026-10-24)

B21 (`arena/04fdf32e-le` @ `77769ef5116e79a6ca98f5ab414c81ae56aee93a`) establishes from the original recorded Drive archive that root member `povstenko2011.pdf` is the `.511931` fractional-Cattaneo paper; the archive contains no `.511929` member. The full archive SHA-256, member SHA-256, Drive ID, page/leaf map and inspection limits are preserved in `scientific-audit.md` and `literature-evidence-matrix.csv`. Eq. (29) is printed p. 101 / PDF leaf 6 and has source coefficient `zeta`; Appendix A begins p. 112 / leaf 17 and ends p. 113 / leaf 18. B21 reports close inspection of pp. 100–101 and 112–114, not a whole-article read. The exact Gamma-normalized coefficient remains OPEN/CONDITIONAL.

`Povstenko2011Cattaneo` remains mapped to `.511931`; `Povstenko2011` remains the distinct `.511929` Dirichlet-problem record and is used only in general/radial contexts. B21's archive includes no `.511929` source. The prior local `Povstenko2016` metadata (2016 / ISBN `9783319296370` / `NO_DOI`) is preserved in `scientific-audit.md`; the bibliography entry is corrected to the authenticated 2015 copy (print ISBN `978-3-319-15334-6`, eISBN `978-3-319-15335-3`, DOI `10.1007/978-3-319-15335-3`). The key is retained for citation stability; no separate 2016 edition is asserted. Only the book copyright leaf was checked; no mathematical convention is verified.

The previous LIT-0536 “metadata-only/not supplied” readiness snapshot is superseded for source availability by B21's archive-member provenance, but the authoritative plan/readiness criteria were not edited and no gap was closed. GAP-09 and all other mandatory gates remain open. **R3 remains NOT PASSED.** No R4 work started.
