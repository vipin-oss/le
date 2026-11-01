# Where the evidence work now stands - short summary

> **Superseded in one respect - 2026-11-01.** This file describes the state at the end of the six-step
> run. The author then supplied a reference set containing nineteen of the twenty outstanding sources,
> including the real Quintanilla (2008) end-effects paper, so the CR019 line below is withdrawn and the
> numbers have moved. Read `SUMMARY_step7.md` for the current position; the CR019 correction is written
> out in `step5_source_not_available_final.md`.

Written at the end of the six-step run. All numbers are read off the deliverable CSVs in this folder
and in `../P3_evidence_claims_C`, not from memory.

## 1. How many claims are now R3

**113 of the 667 claim-check-B rows are at R3** (page-level: the page or equation was read and the
sentence in `source_wording_max25words` is copied from it). That is up from 56 before Step 4.

| level | rows | meaning |
|---|---|---|
| R3 | **113** | a page or equation was read |
| R2 | 17 | the source was seen but only indirectly (abstract of a second-hand record, a scan, a log) |
| R1 | 325 | only a title page, a bibliography record or a catalogue entry was seen |
| R0 | 212 | nothing of the source was seen |

By verdict those 667 rows are: **SUPPORTED 420, PARTLY SUPPORTED 28, SOURCE NOT AVAILABLE 219**
(before Step 4 it was 380 / 9 / 278).

The 31 rows of the claim-check-C series add: SUPPORTED 20, PARTLY 8, NOT SUPPORTED 1, SOURCE NOT
AVAILABLE 2, all of the supported ones at page level.

## 2. How many are still SOURCE NOT AVAILABLE

Two counts, because they answer two different questions.

* **In the claim checks: 219 + 2 = 221 rows.** These are the rows where, after the search, there is
  still no readable page. Six of them are not really "not available" - the paper is in the folder but
  the scan has no text layer (Stoneley 1924 x4, Barnett et al. 1985, Green-Naghdi 1991) - and are
  marked as such in their rows.
* **In the claim register: 115 of the 143 original `SOURCE NOT AVAILABLE` rows.** 28 were resolved by
  the claim-check-C batches; the other 115 have never been through a claim check at all, because they
  sit in sections that the earlier passes did not reach. Two of them - **CR019** (Quintanilla 2008,
  end effects) and **CR044** (Sherief, El-Sayed and Abd El-Latief 2010) - were searched for one last
  time in Step 5 with the final wording written out in `step5_source_not_available_final.md`.
  **Correction, Step 7:** CR019 was resolved - the author supplied the paper and it is supported at R3
  (CC-0036). Only CR044 still stands.

So: **221 claim-check rows** and **115 register rows** still carry SOURCE NOT AVAILABLE, and the
difference between the two numbers is the 115 register rows still waiting for their first claim check.

## 3. The ten PDFs that would move the work furthest

From `pdfs_needed_from_author.csv` (which now carries only the 20 sources still not held, in rank
order). These ten are, in order, the ones that unblock the most and the most load-bearing claims:

| # | source | claims unblocked | why it is on the list |
|---|---|---|---|
| 1 | Chirita, D'Apice and Zampoli (2016), time-differential three-phase-lag model | 3 (CR115, CR129, CR134) | the only source blocking three claims at once |
| 2 | Zener (1937), Phys. Rev. 52, 230 | 2 (CR140, CR141) | the origin of the damping the whole TED section rests on |
| 3 | Mindlin and Tiersten (1962) | 2 (CR190, CR200) | the couple-stress/piezoelectric bar model |
| 4 | Eringen (1983), differential form of nonlocal elasticity | 2 (CR183, CR185) | the equation `(1 - xi^2 lap) sigma = C : eps` the manuscript actually uses; the 1972 paper does not contain it |
| 5 | Chandrasekharaiah (1996) | 2 (CR138, CR155) | the DPL review that fixed the notation |
| 6-8 | Povstenko (2004), (2007), (2009) | 2 each (CR040/041/042, CR063/064/065) | six fractional-thermoelasticity claims, one author |
| 9 | Chirita (2017), J. Thermal Stresses | 2 (CR116, CR130) | the second paper of the TPL pair |
| 10 | Prasad and Kumar (2020) | 2 (CR035, CR058) | hyperbolic two-temperature plane waves |

Nine of the twenty remaining sources are Quintanilla or Povstenko items, so one request to the author
for those two authors' papers clears most of the list.

## 4. What changed in this run, in one line each

* **Step 1** - the folder rescan: 100 files, of which 63 match a bibliography key, 33 print no DOI and
  cannot be keyed without reading the page, 20 are name matches with the wrong content, and 1 (a 29.7 MB
  book) cannot be read in place. `library_inventory_v3.csv`.
* **Step 2** - 17 of the 143 blocked register rows turned out to be readable after all; batches 005 and
  006 record them, and CR003 (the load-bearing Quintanilla 2003 stability condition) is now verified
  page by page.
* **Step 3** - `pdfs_needed_from_author.csv` rewritten to the 20 sources that are still missing; the
  four over-cap archive members moved to a custody file; every DOI in the list is `NOT FOUND` on
  purpose, because no page of those works has been seen.
* **Step 4** - 65 rows moved from R0 to a read page (113 R3 in total), 6 left blocked by image-only
  scans, 2 left at R1 because the source is a 500-page book.
* **Step 5** - Sherief et al. (2010) and Quintanilla (2008) searched once more and closed with final
  wording; the Quintanilla file in the folder is a different paper by Quintanilla and Racke.
* **Step 6** - this summary.
* **Step 7** (2026-11-01) - the author's reference set: nineteen of the twenty sources identified and
  read, 32 register rows checked, CR019 reversed, the needed list cut to one row. See
  `SUMMARY_step7.md` and `step7_reference_set_pass.md`.
