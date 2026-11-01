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

- **Reference register levels** (after step 26): 62 R2, 127 R1, 4 R3, 4 R1-noDOI, 7 R0 over **204 rows**,
  **198 distinct bibkeys**. The R0 count is the one the blueprint's P2 exit condition turns on; the 323 in the
  blueprint is the manuscript's own bibliography count, and only 199 keys exist inside this repository.
- **Register:** 224 rows in `paper_v2/claim_register.csv`; **111** of them carry the verdict
  `SOURCE NOT AVAILABLE`. That 111 is the denominator for everything below.
- **Closed by reading a source: 83.** 40 (first two uploads) + 25 (fourth batch) + 1 (the work found by the
  drive sweep) + 8 (held sources read on 2026-11-01) + 4 (the books of the fifth batch) + 5 (the sixth round:
  CR092, CR093, CR136, CR168 read, and CR137 carried by Carlson, the other citation in its parenthesis).
- **Still to order: 1 claim / 1 work** - Born and von Karman 1912, for the chain dispersion relation.
  `related_books_2026-11-01.csv` names the books that would do instead if the 1912 volume cannot be found.
- **Waived by the author: 4** (CR209, CR210, CR177, CR050) - declared unimportant on 2026-11-01, so no
  evidence is produced and the sentences citing them have to be dropped.
- **Held but not yet read at claim level: 4** (CR127, CR152, CR166, CR196).
- **Register-level, no file needed: 19.**
- 83 + 1 + 4 + 4 + 19 = **111**, with no claim counted twice. This was recomputed from the CSVs during step 17
  as a set union, not by hand.
- **Everything that came in:** 107 files from the author across five deliveries (40 + 25 + 1 + 3 + ... see the
  ledger's section 1), 95 distinct works identified, plus an earlier library inventory of 117 files yielding
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
- **Step 17** (summary in `SUMMARY_step17.md`): the twelve held sources were attacked - eight read
  at claim level, four could not be re-located; the nineteen register-level rows got their own pass, which
  turned up a duplicate citation and a wrong DOI; this README was written; everything was audited once.
- **Step 18:** the request list was **re-ordered by priority, not by discovery**. `sources_still_needed_full.csv`,
  its `.md` mirror and the one-page PDF all carry the same 13 works in the same new order: ranks 1-5 are the
  five that carry the model, the definition and the two standard references; ranks 6-9 are the four papers
  with a working DOI; ranks 10-13 are one-sentence attributions. Nothing was added or removed - 13 works,
  14 claims, 4 verified DOIs, exactly as before. If the order is ever changed again, the CSV, the `.md` and
  the PDF must change together, because the PDF is built from the CSV.
- **Step 18b, English titles.** Four rows in the PDF now carry an English line under the printed one, and the
  CSV deliberately does not: (a) Cattaneo 1948 prints the Italian title that the 2011 reprint record holds, so
  the English line is a translation of it; (b) Danilovskaya 1950, Vernotte 1958 and Born and von Karman 1912
  have no title in any record found and none in the register, so their English lines are the customary
  renderings, printed with the words "not verified" beside them, for ordering and searching only - they must
  never be quoted as titles. Their CSV rows still say "no title asserted", and that must stay true until a
  title is read off a record or a page. For Vernotte, two 1958 Comptes Rendus notes exist and the register
  gives only the volume, so which note the sentence means is still open.

- **Step 19:** the four books arrived and were opened. **Tzou** (2nd edition 2015), **Podlubny** (1999) and
  **Boley and Weiner** (Dover reprint of the 1960 text) matched their rows and four claims closed: CR002 and
  CR112 (the two-lag statement, p.64 and p.62), CR039 (Caputo's derivative, section 2.4.1, p.79), CR169
  (suddenly applied thermal loads, ch.9). The fourth book, a *Thermoelasticity*, is **Parkus** (Springer
  1976), not Nowacki - opened anyway, and it cannot serve the sentence either (no reciprocity theorems;
  "variational" appears only in its reference list), so the Nowacki row stays. The author also declared four
  recent papers unimportant: CR209, CR210, CR177 and CR050 are in `waived_by_author_2026-11-01.csv` with what
  has to happen to the sentences that cite them. The request list is now **6 works / 6 claims**.

- **Step 20:** every title on the request list is now a title read from a record, so no row says "no title
  asserted". Cattaneo and Carlson come from their Crossref records (Cattaneo from the 2011 reprint chapter);
  Nowacki, Vernotte, Danilovskaya and Born-von-Karman come from independent records that print the title,
  because no publisher record exists for those printings. The Carlson chapter also got its verified DOI
  (10.1007/978-3-662-39776-3_2). Two citation errors surfaced while doing this - see findings 10 and 11.

- **Step 21:** eight items arrived in the sixth round (three of them byte-identical copies of the Parkus book
  already rejected) and six are distinct works. **Carlson** came whole - 49 pages - and closed CR136 outright
  (sect. 24, variational principles, pp. 338-342) and CR137 at sentence level (the same sentence is carried by
  Carlson, so the Nowacki citation is now a wording decision). **Ignaczak and Ostoja-Starzewski (2010)**
  closed CR092 and CR168 as a secondary source and printed the Vernotte entry that CR093 needed, which
  **Tzou** then closed properly ("the CV wave model originated by Cattaneo (1958) and Vernotte (1958, 1961)",
  p.62). **Sneddon** (C.I.M.E. 1972) backs CR136 a second time, variational principles only. Two items were
  **not usable**: a one-page Cattaneo extract (front page of his 1966 C.I.M.E. course, no argument on it) and
  Grigull and Sandner's *Heat Conduction*, an engineering text with no Cattaneo and no Vernotte. The request
  list is now **1 work / 1 claim**, and `related_books_2026-11-01.csv` sets out what to fetch instead.

- **Step 22:** the evidence was turned into **paper edits**, since the `.tex` files are not in this repository and
  must not be touched: `P3_evidence_claims_B/PAPER_EDIT_SHEET_2026-11-01.csv` and its `.md` mirror carry **23
  items** - 5 mandatory sentence changes, 5 soften-or-re-cite, 9 bibliography fixes, 4 pending - each with the
  sentence as written, what is wrong, what to do, a suggested wording and the evidence that was read. The five
  DOI lookups that the register-level pass had left open were also done: CR110, CR126 and CR154 got verified
  DOIs, CR122 a probable one (flagged), CR083 failed twice and says so. The one-page PDF is now two pages - the
  request list and, on page 2, the mandatory edits.

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

8. **Two caveats travel with the book evidence.** The Tzou copy is the **2015 second edition** while the
   manuscript cites the 1997 first edition, so either the edition is added to the reference or the year is
   checked. The Boley and Weiner copy is a **reflowable EPUB with no page numbers**, so its quotes are cited
   by chapter; the copyright page confirms the 1960 Wiley text.
9. **The Nowacki row has now defeated two batches**: a two-page journal note in the fourth, and Parkus's book
   in the fifth. If a copy comes again, read the author name on the title page first.

10. **The Nowacki citation mixes two books.** The Pergamon/PWN *Thermoelasticity* is 1962 (first edition) or
    1986 (second, xii + 566 pp., ISBN 978-0-08-024767-0, chapter DOIs under 10.1016/b978-0-08-024767-0). The
    Nowacki book of **1975** is *Dynamic Problems of Thermoelasticity* (Noordhoff, Leyden). So "Nowacki 1975,
    Thermoelasticity, Pergamon" cannot be satisfied by any single book: the year and the title belong to two
    different works. This is probably why this row defeated two batches.
11. **The Carlson year is out by one.** Crossref dates *Linear Thermoelasticity*, pp. 297-345 of Handbuch der
    Physik VIa/2, to **1973**; the manuscript says 1972.
12. **Cattaneo's 1948 note and Cattaneo's 1958 note are two different papers, and the sources split.** The
    register row is the 1948 Italian note in the Modena *Atti* (vol. 3), and the 2010 Oxford monograph credits
    the relaxation law to **Cattaneo (1948)** - that is what closed CR092. Tzou, by contrast, credits
    "Cattaneo (1958)", the French note in C. R. Acad. Sci. Paris 247 (his bibliography prints pp. 431-433),
    which is why the two dates must not be mixed when the reference is written.
13. **CR137 is a citation problem, not an evidence problem.** The sentence "variational formulations and
    reciprocity theorems for classical thermoelasticity are available" is carried in full by Carlson, the
    other citation in the same parenthesis: sect. 24 for the variational principles (pp. 338-342), sect. 13
    (p. 319) and sect. 21 (p. 331) for the reciprocal theorems, the second one built as "a counterpart of
    Graffi's reciprocal theorem". Nowacki's book adds nothing that is not already there, so the author can
    simply drop it - which is why the row left the list without a third failed order.
14. **The word "independent" is the author's, not the sources'.** Neither Tzou nor the 2010 monograph says
    Vernotte's note was independent of Cattaneo's; they credit two authors jointly for one model. The evidence
    for CR093 is sound, but that one word should be softened or owned.

15. **A whole sentence lost both of its citations.** "For DPL and TPL (first-order truncations) an energy
    functional exists but its construction is more involved ... (Quintanilla 2003; Chirita 2016)" is not carried
    by either: Quintanilla (2003) proves a stability threshold and constructs no functional, and Chirita, D'Apice
    and Zampoli (2016) work through fading memory and construct none either. That is items I001 on the edit
    sheet, and it is the strongest single finding of the paper-level pass.
16. **The piezoelectric-bar sentence cites a couple-stress paper.** Mindlin and Tiersten (1962) has no electric
    field and no quasi-electrostatic bar; all 34 pages were searched. Drop it from that sentence (I002) - it
    belongs in the couple-stress discussion.
17. **Four of the five open bibliography lines are now closed.** CR110 doi:10.1080/01495739608946173,
    CR154 doi:10.1115/1.2822615 (the publisher spells the third author *Vedevarz*), CR126 book
    doi:10.1007/978-90-481-3074-0 (2010 edition, ISBN 9789048130733; the record lists two authors, not three),
    and CR122 doi:10.1007/s00245-016-9365-1 - probable only, and its print year is 2017 against the cited 2016.
    Chen and Nunziato (1974) was not found in two queries and still carries no DOI.

- **Step 23:** the blueprint was read against the repository instead of against memory. `PUBLICATION_READINESS_2026-11-01.md`
  says what is actually finished: the **design freeze is 8 of 9** (only "expert readers named" is open) but the
  blueprint's own **submission checklist is 0 of 6**, P0 and P5 have not started (no originality matrix, no
  model-selection guide, no controversy table anywhere in the repository), P1 has 7 open defects of 10, P2 still
  carries **32 R0 references** in a register that covers 119 entries against a bibliography of 323, the atlas has
  **8 of 40** cases carried through, and there are 14 benchmark records and 42 second-implementation comparisons.
  `check_readiness.py` recomputes every number in that note from the CSVs, so the note cannot drift.
  (The 32 R0 references it recorded were repaired in step 24; the note's own numbers were updated with it.)

- **Step 24:** the 32 R0 rows were re-decided instead of re-fetched, and the answer was that most of them were
  never about a paper we lacked. **Seven of the 32 rows carried a DOI that resolves to a different paper** -
  the Jackson 1970 row pointed at Green and Naghdi 1992, the Rayleigh 1885 row at a 2024 Moore-Gibson-Thompson
  paper, the Pennes 1948 row at a 2023 bioheat paper, and so on - and five more carried a candidate *title*
  from another work. Two of the borrowed DOIs were pasted from neighbouring rows (Li2021 and Zhang2021), which
  is why the wrong entries stayed plausible. The rows were corrected against records opened today and against
  full texts already read in this cycle: **8 completed, 8 replaced, 4 promoted to R3 because the text was
  already read, 2 level-aligned, 1 memory-built bib entry confirmed, 2 confirmed as they were, 7 still R0**.
  The register now reads **62 R2 / 42 R1 / 4 R3 / 4 R1-noDOI / 7 R0** over 119 rows, and those 119 rows carry
  only **113 distinct bibkeys** - six are duplicated across batches 003 and 004, and only Bleustein1968 has two
  different levels. The seven survivors are Chadwick 1960, Auld 1973, Duhamel 1837, Scruby 1990 and Gulyaev
  1969, each with a named next action in `P2_verification/`. In the same pass the four held sources were
  finally pinned down: **none of the four is in the library** (five name and title-phrase searches each), but
  **all four citations are real** - Muller and Ruggeri 1998, Gurtin and Williams 1966 (ZAMP 17, 626-633),
  Li, Zhang, Li and He 2019 (IJHMT 144, 118664) and Eringen 1974 (IJES 12, 1063-1077) - so what is left is the
  reading, not the reference. Their claim verdicts are untouched: all four stay `SOURCE NOT AVAILABLE`.

- **Step 26:** the agent's own queue from the pending list was worked. Three things happened.
  (1) **The register grew from 119 rows to 204**: every bibkey in the repository's three bibliography files
  that had no verification row now has one - 86 keys were missing, 85 carried a DOI, and all 85 were checked
  against the Crossref record with a title match of 0.80 or better. Those rows are labelled R1 with a note
  saying they are **title-level** verifications: the DOI and the title were read off the record, the volume
  and pages still come from the bib entry. Nothing was promoted to R2 and nothing was promoted on a guess.
  (2) **Chen and Nunziato 1974 is no longer a missing paper.** DOI 10.1007/BF01590264 is *Thermodynamic
  restrictions on the relaxation functions of the theory of heat conduction with finite wave speeds*, ZAMP
  **25**, 791-798, 1974, by Peter J. Chen and Jace W. Nunziato. Five title searches had failed; the DOI was in
  the bibliography the whole time. **Coleman and Gurtin 1967** is likewise located: J. Chem. Phys. **47**,
  597-613, DOI 10.1063/1.1711937 - which is the DOI the Gulyaev 1969 entry had wrongly borrowed, now recorded
  on both rows. This clears the two open queries behind edit items I001 and I003.
  (3) **The nine catalogue R0 rows were each given an outcome** (`P2_verification/CATALOGUE_R0_2026-11-01.csv`):
  Carlson, Achenbach and Cattaneo resolved (Cattaneo as the 2011 reprint, not the 1948 original), Tzou flagged
  as an edition trap - the DOI on the record is the 2014 Wiley second edition, not the 1997 first - and five
  rows left print-only (Vernotte 1958, Nowacki 1975, Duhamel 1837, Chadwick 1960, Gulyaev 1969).

- **Step 25:** the pending-to-publish list was written as its own page, because the readiness note answers
  "how far along are we" and this one answers "what is left". `PUBLISH_PENDING_2026-11-01.md` has the six
  11b gates with their current state (**0 of 6**), the item-by-item detail behind each, an owner split
  (author / agent / money-or-library / needs-Overleaf / needs-other-people), a dependency-ordered week plan
  and a measurable definition of done per gate. Two findings came out of writing it: **the 134 pages and the
  35 scripts are not in this repository at all** - they live in the Overleaf project, so four separate items
  (the page audit, the 9 script assertions, D6/D8/D9, the clean build) are blocked until the pull runs on the
  author's machine; and **`refs_extra.bib` plus `refs_new.bib` plus the landmark file carry only 199 unique
  keys**, so the 323-entry register target cannot be reached from this repository either - it needs the
  manuscript's own bibliography. It also names the one thing nobody had written down: the 34 PARTLY SUPPORTED
  claims are in no edit sheet at all, so they are pending author wording work that no previous job covered.

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

### The readiness checker

```bash
cd paper_v2/arena_deliverables && python3 check_readiness.py; echo "exit=$?"
```

It must end with `PASS all checks (phases=8, claims=224, refs=119, defects=10)` and exit 0. It recomputes the
claim register, the reference registers, the atlas, the benchmarks, the second implementation and the defect
register, and fails if the readiness note prints a number that is no longer true.

Run it **from its own directory** - it resolves every path relative to the file's location, and several
earlier failures were nothing more than being run from the repository root. It checks, among other things:
the request list's row and claim counts, that no requested work is already held, that every verdict file's
claims exist in the register, that no quote is longer than 27 words, that no repository file leaks a drive
identifier or a link, and that the ledger's four buckets add up to the register's 111.

The one-page PDF is rebuilt by a script that lives outside the repository (kept out of git deliberately,
because it embeds a link). **The checker does not open the PDF** - it only reads the CSVs - so after any
rebuild the PDF has to be verified by hand: extract its text with `pypdf` and confirm it is one page, that the
single open work is printed with its note, that every DOI or ISBN on it still matches
`related_books_2026-11-01.csv`, and that the numbers agree with the CSV. That was done in step 21.

### The pending-list checker

```bash
cd paper_v2/arena_deliverables && python3 check_publish_pending.py; echo "exit=$?"
```

It must end with `PASS all checks (gates=6, 11b=0 of 6, R0=7, atlas=8 of 40)` and exit 0. It re-reads both
blueprint checklists, the claim register, both reference registers, the three bib files, the atlas, the
benchmark registry, the second implementation, the defect register and the edit sheet, and fails if the
pending list prints a number that has moved - including the ones that would quietly make the plan look closer
to submission than it is (11b ticking a box, R0 falling without a source, the atlas jumping).

### The P2 pass checker

```bash
cd paper_v2/arena_deliverables/P2_verification && python3 check_p2_pass.py; echo "exit=$?"
```

It must end with `PASS all checks (register=204 rows, R0=7, resolution=32, held=4)` and exit 0. It re-reads the
verification register, the 32-row resolution table and the four-row held-sources table, and fails if a level
count moves, if one of the seven wrong DOIs comes back onto the row it had been pasted into, if a held source is
ever claimed as read, or if the four claim verdicts stop saying `SOURCE NOT AVAILABLE`.

### Pulling the latest from Overleaf

The author's manuscript lives on Overleaf and is linked to a git remote there. `pull_from_overleaf.sh`
(in this folder) does the pull: it clones the Overleaf project into a throw-away directory and lands the
whole project in `paper_v2/from_overleaf/<UTC stamp>/`, with a `CHANGED_FILES.md` beside it listing every
file that is new and every file that differs from the copy already in the repository. It never overwrites
anything outside that folder, so the standing rule that `.tex` files are not edited by the agent still
holds - replacing a manuscript file stays a human decision.

```bash
cd paper_v2/arena_deliverables
./pull_from_overleaf.sh <the-overleaf-git-url> main
```

Overleaf prints that git URL under **Menu -> Git** (it is the Overleaf host followed by the project id),
and the git token under **Account -> Git integration**.
Type the token at git's own prompt; it is never stored by the script and must never appear in a file, a
commit or a chat message.

Two hard facts, recorded so nobody spends an hour rediscovering them:

- **`git.overleaf.com` is not reachable from this sandbox** - the TLS handshake is refused, and only
  GitHub and the package registries are open. `github.com` answers fine. So the script has to be run on a
  machine that can open Overleaf in a browser, or the pull has to come through GitHub.
- **No Overleaf credential exists here**, and none should be sent. The alternative route needs no token at
  all: connect the Overleaf project to a GitHub repository (Overleaf: **Menu -> Sync -> GitHub**) and then
  the latest manuscript is one `git fetch` away, doable from this sandbox.

## 8. What is still open

1. **In the paper: 23 edit items**, 5 of them mandatory (`PAPER_EDIT_SHEET_2026-11-01.md`). These are the
   changes the evidence forces on the manuscript, and the manuscript is not in this repository, so they are
   written to be worked through in Overleaf. Nothing on the sheet needs a new source.
2. **From the author: 1 work / 1 claim** - Born and von Karman (1912), Physikalische Zeitschrift 13, for
   CR181. If that volume cannot be found, the substitute is a book: Born and Huang, *Dynamical Theory of
   Crystal Lattices* (DOI 10.1093/oso/9780192670083.001.0001), listed first in
   `related_books_2026-11-01.csv`. Polizzotto (2001) is held but its text will not extract, so CR195 still
   waits for a readable copy.
3. **Four held sources are cited correctly and still unread** (CR127 Muller and Ruggeri; CR152 Gurtin and
   Williams 1966; CR166 Li et al. 2019; CR196 Eringen 1974). Step 24 confirmed every one of the four against a
   publisher record and confirmed that none of the four is in the library, so more searching will not help. Two
   of them can be closed by wording instead of by a copy - CR152 can rest on Coleman and Noll 1963, which is
   already at R1, and CR196's historical half is carried by the 1974 title itself - and both are written up as
   proposals, not edits, in `P2_verification/HELD_SOURCES_2026-11-01.csv`. CR127 needs the book; CR166 needs one
   clause removed.
4. **The nineteen register-level works are half-closed.** Chen and Nunziato 1974 and Coleman and Gurtin 1967
   now have located records and register rows (step 26), so edit items I001 and I003 no longer wait on a
   catalogue lookup. The other seventeen cannot be given rows from here: their bibkeys exist only in the
   manuscript's bibliography, so they wait for the Overleaf pull. **Sixteen of them can be ordered today**, and three need no order because
   they are already held (CR003 and CR114 are one paper, and CR199 is now readable). Of the sixteen: nine
   already carry a correct DOI in the register line, two got a verified DOI today, and five still need a
   catalogue lookup before an order can be placed (CR083, CR110, CR122, CR126, CR154). Whether to spend an
   order on them is the author's call, not an evidence call.
5. **The pending-to-publish list is `PUBLISH_PENDING_2026-11-01.md`** - six gates, owner split, week plan,
   definition of done, and the four ways this could still slip. Read it with the readiness note: that one says
   where the work stands, this one says what is left and in what order.
6. **Publication readiness is documented, not assumed.** `PUBLICATION_READINESS_2026-11-01.md` is the one page to
   read before promising a submission date: the critical path is the P1 page-by-page audit, the P5 synthesis
   (model-selection guide and controversy table) and the three expert reviews, in that order of effort.
7. **CR199 (Yang 2018) is now readable** - a 309-page copy was opened today and its title page read. Its
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
- Don't paste an Overleaf git token (or any other credential) into a file, a commit or a chat message, and
  don't let an Overleaf pull overwrite a `.tex` file in place - land it in `paper_v2/from_overleaf/` and let
  the author decide what to replace.
- Don't re-run `check_reaudit_1.py` expecting a pass: it fails on the committed register by design (20 rows /
  39 flagged) and the register is frozen. That failure is pre-existing and is not to be fixed by editing the
  register.
