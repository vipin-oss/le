# Step 17 - the held sources read, the register-level pass, and the README

Date: 2026-11-01. Branch `arena/9b458c54-le`. Work done without any new material from the author.

## 1. Twelve claims had a source in hand and no reading. Eight are now read.

`SOURCE_READING_held_2026-11-01.csv`, 12 rows, same eight columns as the fourth-batch reading. Each read row
carries the page and a quotation of at most 27 words.

| claim | work | verdict | where |
|---|---|---|---|
| CR020 | Quintanilla and Racke (2008), stability in three-phase-lag conduction | SUPPORTED | p.5 |
| CR043 | Povstenko (2011), fractional Cattaneo-type equations | SUPPORTED | p.2 |
| CR060 | Povstenko (2015), Fractional Thermoelasticity (book) | PARTLY SUPPORTED | p.6 |
| CR162 | Sarkar, De and Sarkar (2019), waves in nonlocal type-II solids | SUPPORTED | p.1 |
| CR171 | Rayleigh (1885), waves along the plane surface | SUPPORTED | p.1 |
| CR182 | Eringen (1972), nonlocal polar elastic continua | PARTLY SUPPORTED | p.15 |
| CR184 | Eringen, Nonlocal Continuum Field Theories (book) | SUPPORTED | p.113 |
| CR204 | Abouelregal (2020), three-phase-lag with higher-order fractional derivatives | SUPPORTED | p.1 (title level) |

The four that could not be read - CR127 (Muller and Ruggeri), CR152 (Gurtin and Williams 1966), CR166 (Li et
al. 2019), CR196 (Eringen 1974) - were each identified from a real page in an earlier sweep, but no readable
copy could be re-located this time: seven name searches returned only the works already known. They are
recorded as held, not read, and they need no new PDF from the author.

## 2. Two findings that change the manuscript

1. **The nonlocal sentence splits across two Eringen sources.** The form (1 - xi^2 grad^2) sigma = C : epsilon
   is equation (6.9.12) on p.113 of the 2002 book (with an extra quartic term), and the word "Yukawa" occurs
   nowhere in that book's 386 pages. The 1972 paper contains neither the word nor the form; it does set up the
   nonlocal framework (kernels that die out with distance, p.13; section 5, p.15).
2. **The Povstenko book does not carry the three-phase-lag half of the sentence.** It is a monograph on
   fractional thermoelasticity and points to reviews on p.34, but "three-phase-lag" is not in the first 40
   pages scanned.

## 3. The nineteen register-level rows, in their own file

`register_level_pass_2026-11-01.csv`: for each row, what the citation line lacks, the full citation verified
against a record, whether the register's DOI resolves, whether the work is held, and whether it can be
ordered. Two findings:

1. **CR003 and CR114 are the same paper** (Quintanilla 2003, J. Thermal Stresses 26, 713-721), and it is held
   and read. One file, two rows, no order.
2. **The DOI recorded for CR117 is wrong.** 10.1016/j.amc.2021.126219 resolves to a graph-theory article
   (Appl. Math. Comput. 408). The correct record is van der Merwe, van Rensburg and Sieberhagen (2021),
   Appl. Math. Comput. 396, 125934, DOI 10.1016/j.amc.2020.125934.

Of the nineteen: three need no order (the two Quintanilla rows and Yang 2018, whose 309-page copy was opened
today), eleven carry a correct DOI, two got a verified DOI from a Crossref lookup today, and five still need a
catalogue lookup (CR083, CR110, CR122, CR126, CR154).

## 4. One README for the next reader

`paper_v2/arena_deliverables/README_FOR_CLAUDE.md`: the ground rules, where every file is, what every number
means and how it is computed, the findings that must not be lost, the exact command to re-run the checker, the
open items, and a don't-do list.

## 5. The audit

- Every checker in `paper_v2/arena_deliverables/` was re-run **from its own directory**: 16 checkers exist, 15
  pass and exit 0. The one failure is `P3_reaudit/check_reaudit_1.py`, which fails on the frozen register by
  design and has done so since the register was frozen; it is not to be fixed by editing the register.
- `P3_evidence_claims_B/check_pdfs_needed.py`: **117 checks, `PASS all checks (needed=1, library=34,
  findings=3)`, exit 0**, with the ledger's arithmetic recomputed from the CSVs:
  `111 blocked claims = 74 closed + 14 to order + 4 held + 19 register-level`.
- The four DOIs printed in the one-page PDF were re-resolved against Crossref today: all four are the cited
  works (Kumar and Tomar 2024; Kumar, Gupta, Pathania and Barak 2025; Singh, Sarkar and Pal 2020; Wang and Li
  2025).
- One regression was caught and reverted during the audit: appending the eight held-source verdicts to
  `claim_upgrade_2026-11-01.csv` broke four checks of its own checker, which binds that file to the 40 claims
  the author's first two uploads freed. The file is back at 40 rows and the held verdicts live in their own
  file. The README now warns about this.

## 6. Where the 111 stand

74 closed + 14 to order (13 works) + 4 held, not read + 19 register-level = 111.
