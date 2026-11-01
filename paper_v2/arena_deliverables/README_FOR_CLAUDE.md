# README for the next reader (written 2026-11-01, for a cold start)

This file is the running log of the evidence work done on the manuscript's reference list. It is written so
that someone picking this up tomorrow with no memory of today can work out what was done, what the numbers
mean, where every number comes from, and what is still open. Nothing here is remembered from conversation:
every figure is computed from the CSV files in this folder, and the commands that recompute them are at the
end.

---

## 1. What the job is

The manuscript (`paper_v2/` in this repository, `.tex` files) cites more than two hundred sources. For each
one, the job is to establish, from the source itself, whether the page or equation the manuscript points at
actually says what the sentence says. Where the source cannot be obtained, the claim is recorded as blocked
and a request list is built for the author. Where the source was supplied, the claim is closed with a page
number and a quotation.

Arena is an evidence worker here. It does not edit the manuscript, does not propose wording for the
manuscript, and does not guess.

## 2. Ground rules the author set (still in force)

1. **No `.tex` edits, ever.** `scripts/` is read-only. Evidence only.
2. **Nothing invented.** No guessed DOI, page, quotation, finding, or title. A title may be printed only if it
   was read off a real record or the page itself; otherwise say "not checked" or "no title asserted".
3. **A DOI must be checked against a real record before it is printed.** If a register DOI resolves to a
   different paper, that is a finding and it is flagged, not silently printed. (One such case exists - see
   section 6.)
4. **Never request a paper that is already held.** The held check must be exhaustive: by name, by title
   words, by DOI, by first page, and against the archive inventories.
5. **Unread source means "SOURCE NOT AVAILABLE", not "supported".** General knowledge is labelled as general
   knowledge.
6. **A file name is not evidence.** Every file is opened and its first page read before it counts. A name
   match on a different paper (Gurtin 1968 for Gurtin 1966; Nowacki's two-page note for Nowacki's book) is
   recorded as a mismatch and the request row stays.
7. **PDFs stay out of the repository.** The one exception is the assembled request-list PDF in this folder.
8. **No Drive identifiers, links or library folder names in any repository file.**
9. **The register's verdict column is frozen.** `paper_v2/claim_register.csv` is not edited. Claim-level
   findings go into the separate verdict files; register-level findings go into their own file.
10. **Every check must print a line beginning with `PASS` and exit 0.** A check that fails prints `FAIL` and
    exits 1.
11. **The request list is handed over as one complete list in one message**, with author names and DOIs, no
    repeats, no Drive content.
12. **No new batch files on every upload.** From step 15 on, the record is the ledger plus one claim-level
    verdict file per batch.

## 3. Where things are

All paths are relative to `paper_v2/arena_deliverables/`.

| file | what it is |
|---|---|
| `P3_evidence_claims_B/LEDGER_2026-11-01.md` | **start here.** One page that reconciles 111 blocked claims with everything that came in. |
| `P3_evidence_claims_B/sources_still_needed_full.csv` (+ `.md`) | the request list: 13 works / 14 claims, with author names, DOIs and DOI status |
| `P3_evidence_claims_B/claim_upgrade_2026-11-01.csv` | claim-level verdicts for the first two uploads: 40 rows. Do not append to it - its own checker binds it to exactly those 40 claims. |
| `P3_evidence_claims_B/SOURCE_READING_batch4_2026-11-01.csv` | claim-level verdicts for the fourth batch: 25 rows |
| `P3_evidence_claims_B/SOURCE_READING_held_2026-11-01.csv` | claim-level verdicts for held sources: 12 rows, 8 read, 4 not read |
| `P3_evidence_claims_B/batch4_2026-11-01.csv` | which of the 26 files in the fourth batch matched which row, and the one that did not |
| `P3_evidence_claims_B/register_level_pass_2026-11-01.csv` | the 19 rows whose citation line, not a PDF, was the problem: what is missing, the verified full citation, whether it resolves, whether it is held, whether it can be ordered |
| `P3_evidence_claims_B/supplied_by_author_2026-11-01.csv` | the 40 works supplied in the author's own uploads, page-1 verified |
| `P3_evidence_claims_B/source_reading_2026-11-01.csv` | the first claim-level reading pass, 40 rows |
| `P3_evidence_claims_B/library_available_sources.csv` | the earlier inventory of what the library already holds (34 usable works) |
| `P3_evidence_claims_B/pdfs_held_in_archives.csv` | works held inside archive bundles, with the custody record |
| `P3_evidence_claims_B/drive_held_sources_2026-11-01.csv` | eight works found in the drive sweep, each with the page-1 reading that identified it |
| `P3_evidence_claims_B/drive_recheck_2026-11-01.md` | the record of the whole-drive name sweep |
| `P3_evidence_claims_B/check_pdfs_needed.py` | **the checker.** Standard library only. Run it from its own directory. |
| `P3_evidence_claims_B/SUMMARY_step*.md` | one short summary per step, from 6 to 17 |
| `REFERENCE_LIST_still_needed_2026-11-01.pdf` | the one-page, one-click request list: 13 rows, author names, DOIs |
| `HANDOFF_FOR_ARENA.md` | the original six-task brief |

## 4. The numbers, and where each comes from

- **Register:** 224 rows in `paper_v2/claim_register.csv`; **111** of them carry the verdict
  `SOURCE NOT AVAILABLE`. That 111 is the denominator for everything below.
- **Closed by reading a source: 74.** 40 (first two uploads) + 25 (fourth batch) + 1 (the work found by the
  drive sweep) + 8 (held sources read on 2026-11-01).
- **Still to order: 14 claims / 13 works.** Tzou (1997) blocks two claims (CR002, CR112).
- **Held but not yet read at claim level: 4** (CR127, CR152, CR166, CR196).
- **Register-level, no file needed: 19.**
- 74 + 14 + 4 + 19 = **111**, with no claim counted twice. This was recomputed from the CSVs during step 17
  as a set union, not by hand.
- **Everything that came in:** 103 files from the author across four deliveries (40 + 25 + 1 + ... see the
  ledger's section 1), 92 distinct works identified, plus an earlier library inventory of 117 files yielding
  34 usable works and 3 claim-level findings.

If a future step changes any of these, the ledger and `check_pdfs_needed.py` both have to be updated in the
same commit, because the checker recomputes the ledger's arithmetic from the CSVs and fails if the printed
numbers disagree.

## 5. What was done, in order

- **Steps 1-10** (commits `93b242c` onwards): the six tasks of the handoff - register audit, source hunting,
  batch records. The evidence findings that came out of them were merged upstream and are not this branch's
  business.
- **Steps 11-13:** the request list was rebuilt three times as more sources turned up (48 works -> 39 -> 38),
  each time with author names and DOI status, and a one-click PDF was produced.
- **Step 14** (`82c73fa`): a whole-drive sweep found that one listed work had been held all along; the list
  was cut to 38 works and rebranded.
- **Step 15** (`eaccc43`): the first two uploads were read at claim level; one ledger page replaced batch-by-
  batch counting; batch files stopped being manufactured.
- **Step 16** (`ec44e96`): the fourth batch - 26 files, 25 matched their row, 1 did not; 23 supported, 2
  partly; the list cut from 38 works to **13**; the PDF rebuilt to one page.
- **Step 17** (this pass, summary in `SUMMARY_step17.md`): the twelve held sources were attacked - eight read
  at claim level, four could not be re-located; the nineteen register-level rows got their own pass, which
  turned up a duplicate citation and a wrong DOI; this README was written; everything was audited once.

## 6. Findings a reader must not lose

1. **CR182 and CR184 split one sentence.** The manuscript writes nonlocal elasticity with a "Yukawa-type"
   kernel and the form (1 - xi^2 grad^2) sigma = C : epsilon and cites Eringen 1972, 1983 and 2002 together.
   The 1972 paper has neither the word nor the form; the 2002 book has the form as equation (6.9.12), p.113
   (with an extra quartic term), and does not use the word "Yukawa" anywhere in its 386 pages. So the word is
   the author's own label, and the equation belongs to the book.
2. **CR060 over-reaches.** The Povstenko monograph is about fractional thermoelasticity, but "three-phase-lag"
   does not appear in the first 40 pages scanned, so grouping fractional DPL and TPL under it is not
   supported by the pages read.
3. **CR003 and CR114 are the same paper** (Quintanilla 2003, J. Thermal Stresses 26, 713-721), already held
   and read. When the reference list is rebuilt, these two entries should collapse into one.
4. **CR117's DOI in the register is wrong.** It resolves to a graph-theory paper. The correct one is
   10.1016/j.amc.2020.125934 (Appl. Math. Comput. 396, 125934). Do not print the old one.
5. **Two PARTLY rows from the fourth batch stay visible:** Askes (2006) - the eight pages sent contain no
   "inertia" or "acceleration" language - and Biswas (2020), Acta Mechanica - the geometry is there but the
   Stroh formalism is not; its own references credit Biswas (2018), J. Thermal Stresses.
6. **The fourth batch's one mismatch:** a two-page Journal of Thermal Stresses item was sent for the Nowacki
   (1975) book. It is not the book. The row stays on the list.
7. **A name match is not a hit:** the Gurtin and Pipkin (1968) paper is not the Gurtin and Williams (1966)
   ZAMP article; only part II of Guyer and Krumhansl is held, not part I.

## 7. How to re-run everything

Nothing needs installing for the checker (standard library only). If a PDF has to be opened, `pypdf` is
needed: `pip install -q --break-system-packages pypdf`.

```bash
cd paper_v2/arena_deliverables/P3_evidence_claims_B && python3 check_pdfs_needed.py; echo "exit=$?"
```

It must print a final `PASS all checks (...)` line and exit 0. Expected today:

```
PASS all checks (needed=1, library=34, findings=3)
exit=0
```

Run it **from its own directory** - it resolves every path relative to the file's location, and several
earlier failures were nothing more than being run from the repository root. It checks, among other things:
the request list's row and claim counts, that no requested work is already held, that every verdict file's
claims exist in the register, that no quote is longer than 27 words, that no repository file leaks a drive
identifier or a link, and that the ledger's four buckets add up to the register's 111.

The one-page PDF is rebuilt by a script that lives outside the repository (kept out of git deliberately,
because it embeds a link). **The checker does not open the PDF** - it only reads the CSVs - so after any
rebuild the PDF has to be verified by hand: extract its text with `pypdf` and confirm it is one page, thirteen
rows, and that the DOIs printed in it are still the four verified ones. That was done today and all four
resolved (Crossref) to the cited works.

## 8. What is still open

1. **From the author: 13 works / 14 claims** (the one-page PDF). Of these, Tzou (1997) and Nowacki (1975)
   matter most - one blocks two claims, the other is the row the fourth batch missed. Polizzotto (2001) is
   held but its text will not extract, so CR195 waits for a readable copy.
2. **Four held sources need locating by content, not by name** (CR127 Muller and Ruggeri; CR152 Gurtin and
   Williams 1966; CR166 Li et al. 2019; CR196 Eringen 1974). Seven name searches failed on 2026-11-01. The
   productive approach is to enumerate the library's PDFs and open anything whose first page matches the
   title, or to search the archives in which the inventory says they sit.
3. **Sixteen of the nineteen register-level works can be ordered today**, and three need no order because
   they are already held (CR003 and CR114 are one paper, and CR199 is now readable). Of the sixteen: nine
   already carry a correct DOI in the register line, two got a verified DOI today, and five still need a
   catalogue lookup before an order can be placed (CR083, CR110, CR122, CR126, CR154). Whether to spend an
   order on them is the author's call, not an evidence call.
4. **CR199 (Yang 2018) is now readable** - a 309-page copy was opened today and its title page read. Its
   sentence ("the one-dimensional piezoelectric bar follows Yang and Mindlin and Tiersten") has not been
   checked against the book's chapter yet; that is a half-hour job with the copy in hand.

## 9. Don't do this

- Don't edit `.tex` files or the register's verdict column.
- Don't print a DOI that has not been resolved against a record today.
- Don't invent a title, a page or a quote to fill a gap - write "not checked" and move on.
- Don't create a new batch file for a new delivery; add to the ledger and to a claim-level verdict file.
- Don't append other claims to `claim_upgrade_2026-11-01.csv`: its checker binds it to the 40 claims the
  author's first two uploads freed, and appending breaks four of its checks (this happened in step 17 and was
  reverted). A new job gets a new file.
- Don't put drive identifiers, links, library folder names or uploaded file names into any file in this
  repository.
- Don't commit PDFs; the request-list PDF in this folder is the only one that belongs in git.
- Don't re-run `check_reaudit_1.py` expecting a pass: it fails on the committed register by design (20 rows /
  39 flagged) and the register is frozen. That failure is pre-existing and is not to be fixed by editing the
  register.
