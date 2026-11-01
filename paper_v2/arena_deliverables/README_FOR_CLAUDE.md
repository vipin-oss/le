# README for the next reader (written 2026-11-01, for a cold start)

This file is the running log of the evidence work done on the manuscript's reference list. It is written so
that someone picking this up tomorrow with no memory of today can work out what was done, what the numbers
mean, where every number comes from, and what is still open. Nothing here is remembered from conversation:
every figure is computed from the CSV files in this folder, and the commands that recompute them are at the
end.

> **Amendments (later on 2026-11-01, take precedence over the numbered ground rules below).**
> 1. The author lifted the "no `.tex` edits" rule: sources **may** be edited, provided the pre-edit file is
>    kept as a version and every change is committed with this README and `CHANGELOG_v2.md` updated. In this
>    file, rule 1 of section 2 is therefore **superseded**; the rule that `scripts/` is read-only stands.
> 2. The page-level audit has begun and is reported in `P1_audit/PAGE_LEVEL_AUDIT_2026-11-01.md`
>    (26 checks, 0 FAIL). It is a *different* question from the source audit: "did the document a reader
>    receives contain what the sources say, with nothing unresolved and nothing broken?"
> 3. Where a number in this file disagrees with the measured build, the measured build wins; the retired
>    numbers are listed in section 12 of `manuscript_v2/REVIEW_CYCLES.md`.

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

- **Steps 44-45 (revision cycle 1, manuscript v1.2):** the author asked for a submission-grade paper, so the sources are now versioned and revised instead of only audited. `paper_v2/versions/v1.1_source_snapshot/` holds the manuscript **exactly as received** (branch `arena/36bc8cc8-le`, tip 2026-10-28) and is never edited; `paper_v2/manuscript_v2/` is the working master, revised in named cycles logged in `manuscript_v2/REVIEW_CYCLES.md` (author → reviewer → editor → author) and versioned in `manuscript_v2/CHANGELOG_v2.md`. **v1.2 changes:** a new **259-word abstract** (the old one was 123 words and said only what the review covers; every scoped statement of the old one is kept verbatim), **11 keywords**, the abstract wrapped in a real `abstract` environment (in v1.1 the text was `\input` raw and ran into the notation section), a **Declarations** section (CRediT, funding, competing interests, data availability, generative-tool statement) placed before the bibliography, `\today` instead of a hard-coded date, the **stale duplicate `tables/` root removed**, and **all six appendices now compiled** (A–F; v1.1 compiled only B and C, so the equation register, the figure-status table, the table index and the reproducibility notes were unreachable). That resolved two of the three findings: the dangling `Eringen1968b` citation lived **only** in the stale duplicate table copy (the live copy never had it — no bib entry was invented), and the duplicate-label complaint disappeared with the duplicate root. The two unused figures are **not** forced in: `appD_figures.tex` declares `fig07-theory-map` and `fig18-taxonomy` provisional, so the audit now reports them as declared and the appendix says so in print. **The submission zip is built and verified by `make_submission_zip.py`, which verifies the *staged* tree and refuses to write a zip that fails**: `/home/user/deliverables/le_review_v1.2_2026-11-01.zip` — 63 files, 40 `.tex`, 16 figure PDFs, 48,402 words, 0 problems. It contains tex, bib, tables, figures, build instructions, the review-cycle log, the version log and the P1 audit report. No TeX engine exists in this sandbox (no `pdflatex`, CTAN and raw.githubusercontent blocked), so compilation stays on Overleaf; every static check runs here.

- **Step 43:** the P1 audit has actually started, on the sources. `P1_audit/audit_sources.py` runs **12 mechanical checks** over the landed manuscript - 49 `.tex` files, 438 labels, 144 reference targets, 219 citations against 144 bib entries, 18 figure includes, 58 includes - and **`check_source_audit.py` re-derives every finding from the sources** instead of trusting the CSV. Three real findings, none of them cosmetic: (1) **`Eringen1968b` is cited in `tables/source/T3_coupled_multiphysics.tex` but exists in no bib file** - a dangling citation; (2) **eight table sources exist twice** in the tree (`master/tables/source/T1..T8` and `tables/source/T1..T8`), so a label is defined twice and the tree is ambiguous about which copy is live; (3) **`fig07-theory-map.pdf` and `fig18-taxonomy.pdf` are drawn and shipped but never included** - the taxonomy figure in particular is not in the taxonomy section. What passes is worth stating too: every one of the 144 reference targets resolves, no `\label` is defined twice within a live path, every included figure exists, every `\input` exists, no placeholder text, every bib entry has author/title/year, and the header counts (17 sections, 7 appendices, 18 figures, 8 tables) match the tree. 294 labels are defined but never referenced - informational, and normal for a manuscript that grew section by section. The page-level pass (signs, dimensions, derivations) has not started; the report says so in its own words.

- **Step 42:** the author said the manuscript was on GitHub, and it was. It is not in `paper_v2/` on this branch, and it is not in `review-paper-v2` (that branch holds only `ARENA_SUMMARY.tex` plus three `.bib` files); it is in an **earlier session branch, `arena/36bc8cc8-le`** (tip 2026-10-28), under `phase5/`. It has been landed in `paper_v2/from_overleaf/phase5/` - **165 text files, 1.8 MB**: `master/main.tex` (214 lines, 17 numbered sections, 7 appendices, 18 figures, 8 tables), `master/frontmatter/abstract.tex`, `master/sections/sec01..sec17`, 49 `.tex` and 45 `.py` files. The 54 MB of figures, SVGs and compiled PDFs stay **outside** the repository in `/home/user/manuscript/`, per the standing rule. Three numbers in the old gates were simply wrong and are corrected here: the build is **126 pages** (phase 5 v1.1) or **161 pages** (phase 4), never the long-quoted **134**; there are **45 scripts**, not 35; and **D2 is not reproducible** - the string "coupled dispersion polynomial" occurs nowhere in the v1.1 sources, and the abstract that is really there is scoped and says "model-specific assumptions". The page-by-page audit can now actually start, against the 126-page build.

- **Step 41:** the DjVu was converted, so **Musgrave is no longer an unread row.** No DjVu codec exists in this image and Debian mirrors are out of reach, but npm is not: `djvujs-dist` is a pure-JS DjVu decoder, and its ES sources, bundled with rollup and run under Node with a handful of browser shims, render every page to raw pixels. All **306 pages** were rendered, downsampled 2x and assembled into a **306-page PDF at /home/user/books/musgrave.pdf (96 MB, outside the repository)**. The pages then gave up the book's real identity, which is not what its file name said: the title page prints **Crystal Acoustics - Introduction to the Study of Elastic Waves and Vibrations in Crystals**, **M. J. P. Musgrave**, Reader in Applied Mathematics, Imperial College London, **Holden-Day**, San Francisco/Cambridge/London/Amsterdam; the copyright page prints **Copyright 1970 by Holden-Day, Inc.** and **Library of Congress card 79-95651**, and **no ISBN** - a pre-ISBN printing. Row 21 of `BOOKS_HELD_2026-11-01.csv` was rewritten accordingly (title, year, publisher, 306 pages, no ISBN) and its notes record the file-name-vs-printed-title mismatch instead of quietly fixing it. `check_books_held.py` was taught that the pre-ISBN exemption now covers arrival 21 too, and still prints **21 arrivals, 19 usable, all 13 ranks**. The conversion log is not committed (generated artefacts stay out of Git); what is committed is the *identity read off the pages*.

- **Step 40:** three more books, all extras rather than wish-list gaps - **Auld, *Acoustic Fields and Waves in Solids* vol. I** (Wiley 1973, 438 pp, ISBN 0-471-03700-1, read off its title and copyright pages); **Carcione, *Wave Fields in Real Media*** (Pergamon 2001, Handbook of Geophysical Exploration 31, 415 pp, ISBN 0-08-043929-2); and **Musgrave, *Crystal Acoustics***, supplied as **DjVu**, which no codec in this environment can render - so its row says plainly that **no page of it has been read** and that the identification is container-level only (291 pages with a text layer). `BOOKS_HELD_2026-11-01.csv` is now **21 arrivals, 19 usable**, still covering all 13 ranks; the three extras carry `wishlist_rank = extra` and say in their notes that the title-match test does not apply to them, so the wish-list invariant is untouched. `check_books_held.py` was taught the `extra` rank (rank arithmetic is now gated on `.isdigit()`) and prints **21 arrivals**. Nothing is claimed for any of the three yet: Auld is a second reader for BK-15, Carcione for BK-11, Musgrave for the anisotropy family, and each is *in hand*, not *read*.

- **Step 39:** BK-15 is written and **the atlas is closed on the invariant side: 40 of 40 cases now have a fully
  executable invariant, none partial, and still 0 case-level results.** The six coupled multifield cases
  (AT-04, AT-05, AT-06, AT-09, AT-13, AT-40) were blocked on one sentence - "piezo/magneto branch speeds need the
  coupled constitutive matrix" - and Eringen & Maugin, *Electrodynamics of Continua I* (1990), **§5.11, printed
  pp. 165-166, eqs. (5.11.4)-(5.11.6)** print that matrix with (5.11.1) as the single quadratic free energy it comes
  from. `P3_atlas/bench_multifield.py` assembles the 12x12 Hessian and executes six invariants: the Hessian is
  symmetric (**max |W - W^T| = 0.000e+00**); it is positive definite (min eigenvalue 5.1205e-01 after diagonal
  scaling - the raw matrix spans 1e11 to 1e-8 in double precision); open circuit stiffens, **C\* - C is PSD with
  max eigenvalue 2.7148e+05 and a stiffening of 1.13e-06 of max(C)**, which is the honest size for quartz-like
  coupling; the three acoustic branches are real and **never below the bare elastic ones over 48 directions**
  (min difference 3.3061e+01); the 6mm piezoelectric limit reproduces the closed form
  **C44\* = C44 + e15^2/chi11 to 0.000e+00 relative**; and switching the coupling off returns C exactly while a
  dielectric constant scaled by 1e12 removes the stiffening to 1e-24. `P3_atlas/check_multifield.py` recomputes all
  six from scratch (55 checks) rather than trusting the CSV. The atlas rows were updated - `coverage = yes`,
  `applicable_benchmarks = BK-15`, `missing_invariant` now records where the invariant came from - while
  `case_level_result` stays **no** for all six, because those papers were still read at title and metadata level
  only: an executable invariant is not a result, and the atlas is still **0 case-level results of 40**. The three
  coverage-split assertions in `check_surface.py`, `check_porous.py` and `check_thermoelastic.py` were moved from
  34/0/6 to **40/0/0**, and the family check now expects multifield among the covered families. The gate in
  `check_publish_pending.py` prints **atlas=40/0/0 of 40**; `PUBLISH_PENDING_2026-11-01.md` and
  `PUBLICATION_READINESS_2026-11-01.md` were corrected from 34 to 40 in the same place.

- **Step 38:** the last six items arrived - **all three needs are met.** `P3_evidence_claims_B/BOOKS_HELD_2026-11-01.csv`
  is now **18 rows / 16 usable books covering all thirteen wish-list ranks**: the real **Eringen and Maugin I**
  (469 pp., ISBN 978-1-4612-3226-1), the real **Povstenko, *Fractional Thermoelasticity*** (261 pp.), plus
  three spares (Eringen and Maugin II, Maugin 1988, Povstenko's diffusion-wave book) and **Achenbach** (436 pp.,
  1973 printing, no ISBN). The two earlier misfires stay on the record, each marked superseded. **What did not
  change: atlas coverage is still 34/40.** BK-15 is now *executable* - the constitutive theory is in hand - but
  no benchmark has been built from it yet, and `check_books_held.py` (24 checks, PASS) asserts both statements so
  the README cannot upgrade them quietly. `check_books_wanted.py` now reports **nothing outstanding**, and the
  request page `BOOKS_OUTSTANDING_2026-11-01.*` carries a delivery banner and a checker that proves all three
  needs arrived. **Next: BK-15 in `P3_atlas/` - build the invariant from Eringen and Maugin and take coverage
  34/40 -> 40/40.**

- **Step 37:** the missing three now carry **verified substitutes**. `P3_evidence_claims_B/BOOKS_OUTSTANDING_2026-11-01.csv`
  (9 rows) + `.md` + a one-page PDF in this folder + `check_books_outstanding.py` (19 checks, PASS): for
  **BK-15** the primary stays Eringen and Maugin I (`10.1007/978-1-4612-3226-1`) with **Volume II**
  (`10.1007/978-1-4612-3236-0`) and **Maugin 1988, *Continuum Mechanics of Electromagnetic Solids***
  (`10.1016/c2009-0-08748-0`) as substitutes; for **fractional thermoelasticity**, Povstenko 2015 with the
  **2024 second edition** (`10.1007/978-3-031-64587-7`) and his diffusion-wave book
  (`10.1007/978-3-319-17954-4`); for the optional **rank 12**, Achenbach with **Miklowitz 1978**
  (`10.1016/c2009-0-08749-2`) and **Graff 1975**, which has **no Crossref book record** and is therefore
  carried as *no DOI recorded* - the only Crossref hit for that title is a 1979 review, which must not be cited
  as the book. Eight of the nine DOIs were opened against a Crossref record today. The honest answer to "do you
  need any other book" is **no**: the three are the whole list, with rows 2/3, 5/6 and 8/9 alternatives to each
  other, and the checker proves no row repeats a book already held.

- **Step 36:** **CR127 closed** - the second reading job from the shelf. The claim ("the entropy depends
  also on the heat flux q_i, which must enter the state space") had been unjudgeable for the whole project;
  Muller and Ruggeri (1998), **§3.5, printed p. 24**, settles it with eq. (3.27) (the Grad distribution over
  the thirteen moments), eq. (3.29) `s = (k/m) ln(T^(3/2)/rho) + varsigma - t_<ij>t_<ij>/(4 rho p^2 T) -
  q_i q_i/(5 p^2 T)`, eq. (3.30) (the entropy flux, which is **not** `q_i/T`) and the sentence "the specific
  entropy ... depends on t_<ij> and q_i ... These facts confirm the conjectures of extended TIP". Record:
  `P3_evidence_claims_B/RET_ENTROPY_READ_2026-11-01.csv` (7 rows) + `.md`; `check_ret_entropy.py` (16 checks,
  PASS) tests the structure - negative correction, **even in q** (|diff| <= 1e-30), **no t-q cross term**
  (1e-25) - and *not* the coefficients: `1/4` and `1/5` are quoted as printed, because a naive evaluation of
  (3.27) does not fix both without the book's moment normalisation and fitting it would be manufactured. That
  limit is CSV row 7 and a paragraph of the readout. Proposal CR127 SNA -> SUPPORTED; register untouched.

- **Step 35:** the books arrived - twelve items against thirteen rows. They were identified from their own
  title and copyright pages (`P3_evidence_claims_B/BOOKS_HELD_2026-11-01.csv`, 12 rows, plus a `.md` mirror
  and `check_books_held.py`): **ten are fully usable** - Coussy, Gorenflo et al., Hetnarski and Eslami (2nd
  ed.), Muller and Ruggeri (2nd ed.), Jou et al. (4th ed.), Mainardi, Eringen *Nonlocal*, Eringen
  *Microcontinuum I*, Brekhovskikh (2nd ed. 1980), Ewing/Jardetzky/Press (1957, no ISBN) - **one is a single
  chapter** (Povstenko: Chapter 1 only, 11 pp.) and **one is not the book at all**: the file that arrived
  under *Electrodynamics of Continua I* is a **one-page book review** in the *Journal of Applied Mechanics*.
  So **BK-15 stays open, coverage stays 34/40**, and Achenbach did not arrive. Two catalogue years were
  corrected from the copies themselves: Eringen *Nonlocal* is **2002** (not 2004), and Muller and Ruggeri's
  printed ISBN is **978-1-4612-7460-5** (the earlier note carried the eBook ISBN). **The first reading job is
  already done: CR046.** Gorenflo et al. was read on printed pp. 25-27, 47, 208, 219
  (`ML_TAIL_READ_2026-11-01.csv`/`.md`): **Prop. 3.6, eq. (3.4.15), p. 26** puts
  `E_a(z) = -sum_k z^(-k)/Gamma(1-a k) + O(|z|^(-1-p))` on the sector containing the negative real axis -
  the exponential term of (3.4.14) is absent there, so the tail is a power law `t^(-a)` with constant
  `1/Gamma(1-a)` - and **Prop. 3.23 (Pollard), p. 47** gives complete monotonicity for `0 <= a <= 1`, which
  is the "decay". Eq. (8.1.31) p. 208 is the solution-level version and (8.1.80) p. 219 names the constants.
  `check_ml_tail.py` (18 checks, PASS) validates its evaluator against the book's own closed form (8.1.30) to
  **3.8e-38** and then measures the remainder: truncating (3.4.15) at `p = 2` leaves a residual decaying like
  `t^(-3a)` - measured **8.5 / 123.4 / 503.7** against `10^(3a) = 7.9 / 125.9 / 501.2`. Proposal:
  **CR046 PARTLY -> SUPPORTED**, register untouched. Two limits are written into the readout: "heavy tails"
  is the manuscript's adjective, not the book's (the book says *algebraic decay*), and Luchko 2010 - the
  claim's second bibkey - is not this book and is not verified by this job. The shelf queue, in order:
  **BK-11 with Coussy** (the only tier-A item that actually arrived), CR127 with Muller and Ruggeri, CR182 and
  the micropolar sentences with the two Eringen books, the named-theory attributions with Hetnarski and
  Eslami, BK-13/BK-14 with Brekhovskikh, and the EIT sentences with Jou et al.

- **Step 34:** the author offered to send any book, so the first question was whether a book can unblock
  anything. It cannot: of the **111** claims at `SOURCE NOT AVAILABLE`, **109** already have a claim-level file
  (the source was supplied, read, or covered at one remove), and the two left are **CR181** (the 1912 note, now
  carried at one remove by Born and Huang 1954) and **CR144** (Kumar, Devi and Sharma 2017 - a journal paper,
  not a book). So the want list is about strength, not about unblocking, and it is deliberately short:
  `P3_evidence_claims_B/BOOKS_WANTED_2026-11-01.csv` (**13 rows**, 14 columns) plus a `.md` mirror, a
  one-page PDF in this folder, and `check_books_wanted.py` (19 checks, PASS). Every title, author, year, DOI
  and ISBN was resolved against a Crossref record today and the row records where; the one work with no
  Crossref record (Ewing, Jardetzky and Press 1957) says **no DOI recorded** and is ranked last, and no row
  repeats a work already held (the checker compares the titles against the library list, the author-supplied
  list and the books already read). Tiers: **A = 2, B = 8, C = 3**. The three worth sending:
  (1) **Eringen and Maugin, *Electrodynamics of Continua I*** (Springer 1990, `10.1007/978-1-4612-3226-1`) -
  the only item that closes an atlas invariant, **BK-15**, i.e. the six multifield cases, and takes coverage
  from 34/40 to **40/40**; (2) **Coussy, *Poromechanics*** (Wiley 2004, `10.1002/0470092718`) - turns **BK-11**
  from field-counting into a model check; (3) **Gorenflo, Kilbas, Mainardi and Rogosin, *Mittag-Leffler
  Functions, Related Topics and Applications*** (Springer 2014, `10.1007/978-3-662-43930-2`) - closes the one
  mandatory gap that cannot be closed from here, the `alpha < 1` asymptotic tail for CR046. Tier B is
  reinforcement (Povstenko, Hetnarski and Eslami, Muller and Ruggeri, Jou et al., Mainardi, Eringen nonlocal,
  Eringen microcontinuum); tier C is optional depth (Brekhovskikh, Achenbach, Ewing et al.). None of the
  thirteen is already held - the checker proves that by comparing every title with the library list, the
  author-supplied list and the books already read - and the mirror also lists the eight works that must **not**
  be sent again, so the list cannot turn into a request for a second copy.

- **Step 33:** the last open claim's book arrived. Born and Huang, *Dynamical Theory of Crystal Lattices* (1954),
  was read on printed pp. 55-57 and p. 79 as page images - `P3_evidence_claims_B/BORN_HUANG_1954_READ_2026-11-01.csv`,
  eleven rows, with a `.md` readout. It settles two of the three things CR181 needed: §5 credits the chain model
  "due originally to Born and Kármán" and its footnote prints *Phys. Zeit.* **13**, 297 (1912), i.e. the
  attribution and the reference survive; and eq. (5.9) prints the exact dispersion whose equal-mass limit is the
  manuscript's formula (limit vs (5.9): 3.6e-15; limit's long-wave coefficient vs the book's own p. 57 value:
  7e-09; the manuscript's `omega = 2 sqrt(kappa_s/m) abs(sin(ka/2))`: 8.9e-16 over 500 wavelengths). It does not
  settle the third: **the book never displays the monatomic formula** - §5 is titled "Vibrations of a diatomic
  chain" and the equal-mass case appears only as a limit - and the 1912 note itself is still unread. So CR181 is
  recorded as **PARTLY SUPPORTED** (not written into the register, which keeps its verdict column) and the fix is
  a citation change: the book for the formula, 1912 for the model, exactly as the book's footnote does. The
  request-list row stays, for a direct quotation only, and now says so in both the CSV and the mirror.

- **Step 32:** the 34 partly supported claims each got a decision. `P3_evidence_claims_B/PARTLY_SUPPORTED_EDIT_SHEET_2026-11-01.csv`
  (34 rows, 14 columns) and its `.md` mirror carry, per claim, the sentence as written, the register's recorded
  finding, a **gap code**, an **action code**, what would close it and a priority: **21 mandatory, 13 optional**.
  The gaps are not uniform - 12 are wrong-or-loose attributions, 12 are cases where the register found the source
  narrower without reducing it to one clause, 4 need one specific page read as an image, 2 are bibliography
  mismatches (CR116, CR130 - the file is a single-author *Journal of Thermal Stresses* paper, the entry says
  Chirita, Ciarletta and Tibullo in *IJHMT*), 2 are words presented as the source's that are not in it, 1 is
  only a modern name, and 1 needs a co-cited source that was never supplied. The sheet changes no verdict
  (`check_partly_sheet.py` re-reads the register and asserts all 34 are still PARTLY SUPPORTED), writes no new
  physics sentence, and asks for no new paper.

- **Step 31:** the branch count is now a benchmark for any number of fields. `P3_atlas/bench_porous.py` adds
  **BK-11** as the algebra of extending the template to m extra fields - explicitly *not* a porous model, which
  this repository does not have: the bordered determinant is a polynomial of degree m+1 in K, so there are m+1
  branches, one propagating and m diffusive. Six rows, all passing, tied to the verified code at m = 1
  (`second_impl.coupled_K_roots` to 1.5e-15) and in the decoupled limit (`second_impl.thermal_k` to 3.8e-14);
  the elastic branch sits at K/K_iso = 0.9091 for m = 1, which is exactly 1/(1+eps), and softens only slowly as
  fields are added (0.8163, 0.7643, 0.7045). Coverage is now **34 full / 0 partial / 6 none of 40**; the six
  left are the coupled multifield cases, and BK-15 stays unwritten because there is no coupled piezo/magneto
  constitutive model here to write it against.

- **Step 30:** the thermoelastic surface wave is now a benchmark, not a gap. `P3_atlas/bench_thermoelastic.py`
  adds **BK-10**: one shear partial wave plus a coupled longitudinal/thermal pair, free and insulated surface,
  3x3 determinant solved for complex s at real k, reusing the bulk quadratic of `second_impl.py` with
  `K -> chi = k^2 (1 + gamma^2)`. Six rows, all passing: beta -> 0 reproduces the classical Rayleigh ratio
  **0.9194016868 c_S** to 2e-16; the four dissipative models decay (passivity) while GN-II and MGT are exactly
  neutral (2e-20); Fourier, DPL and GN-III reach the isothermal elastic root by k = 50 (1.7e-06); Q^-1 <= 6.9e-03;
  nothing exceeds c_S. The deciding detail was a sign - `beta T = -(rho c1^2 chi + rho s^2) phi`. With the other
  sign the dissipative models grow and the lossless ones stay neutral, which no passive medium can do, and both
  halves of that test are now checked so the sign cannot silently flip back. Coverage moves to
  **29 full / 5 partial / 6 none of 40**; left are BK-11 (porous, m > 2) and BK-15 (coupled multifield).

- **Step 29:** the three wave families that had no invariant got one. `P3_atlas/bench_families.py` adds
  **BK-12** (Rayleigh-Lamb plate), **BK-13** (layered Love waves) and **BK-14** (interface, Snell plus flux) as
  14 rows, all passing, each anchored on a closed form derived independently of the code - the S0 limit
  **1.632981** against sqrt(2/(1-nu)) = 1.632993, both branches converging on c_R = 0.919402 c_S at kh = 20 to
  9e-08, the Love cut-off **3.627658** against pi/sqrt(1/c1^2-1/c2^2) = 3.627599, and a flux residual of 2e-16
  against R^2 + T^2 (Z2/Z1) = 1. The coverage map therefore moves from **12 full / 11 partial / 17 none** to
  **23 full / 11 partial / 6 none of 40**, and `check_surface.py` enforces the new split. Two real bugs were
  caught by the anchors: the Rayleigh polynomial in this form has a degenerate root at x = 0, so bisecting from
  zero returned c_R = 1e-08, and the transmitted flux is T^2 (Z2/Z1), not T^2 (Z2 cos2)/(Z1 cos1). BK-15 is
  **not** written on purpose: no coupled piezo/magneto constitutive model exists in this repository, so a number
  for it would describe a model nobody uses. That leaves BK-10, BK-11 and BK-15, and 6 multifield cases.

- **Step 28:** the checksum half of defect D4 is done. `make_release_manifest.py` walks the repository and
  writes `RELEASE_MANIFEST_2026-11-01.csv` - one row per file with its SHA-256, its size and a coarse class -
  which is what an archive deposit needs (`--check` recomputes and reports drift instead of failing, because a
  manifest belongs to the release commit, not to every commit). It covers 177 files and 9.8 MB today. The other
  half of D4, the clean-environment run, still has to happen where the code runs: `scripts/requirements.txt`
  lives with the manuscript, not here.

- **Step 27:** the atlas was measured instead of counted loosely. The old line "8 of 40 cases carried
  through to results" was wrong twice: the eight rows in the benchmark file are *families* (BK-01 to BK-08),
  not cases, and no case can have a result while every paper is read at title level. The truthful numbers,
  now enforced by both document checkers: **40 cases planned, 12 with a fully executable invariant, 11 with a
  partial one, 0 case-level results**. `P3_atlas/bench_surface.py` then added the missing **BK-09**, the elastic
  Rayleigh invariant, with six checks - and it lands on two independent anchors, 0.955300 c_S in the
  incompressible limit (classical 0.9553) and 0.919402 c_S at Poisson ratio 1/4 (classical 0.9194). And
  `atlas_case_coverage.csv` gives every one of the 40 cases a row: which invariant applies, whether it runs
  today, and for the 17 that have none, the exact invariant that is missing (BK-10 to BK-15, listed with the
  closed form each has to satisfy). That is the atlas roadmap: five invariants, then 17 cases, then the papers.

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

### The atlas checkers

```bash
cd paper_v2/arena_deliverables/P3_atlas && python3 bench_surface.py && python3 check_surface.py; echo "exit=$?"
```

`bench_surface.py` recomputes BK-09 and rewrites `atlas_case_coverage.csv`; `check_surface.py` must end with
`PASS all checks (BK-09=6 rows, coverage=12/11/17 of 40)` and exit 0. `check_atlas_benchmarks.py` and
`check_atlas_plan.py` stay as they were (40 rows, 8 families, 8 benchmarks).

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
   CR181. This is now the *only* outstanding source request of any kind; the book wish list step 34 produced is
   about strengthening the paper and every row on it is optional (`P3_evidence_claims_B/BOOKS_WANTED_2026-11-01.md`
   opens by saying so). Of the thirteen rows, **ten arrived as usable books in step 35**; what is still
   outstanding is **rank 1 (Eringen and Maugin - the file that came was a one-page review of it)**, **rank 4
   (Povstenko - Chapter 1 only)** and **rank 12 (Achenbach, not sent)**. The shelf and its state are
   `P3_evidence_claims_B/BOOKS_HELD_2026-11-01.csv`. If that volume cannot be found, the substitute is a book: Born and Huang, *Dynamical Theory of
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


---

## 13. Page-level audit of the compiled v1.2 build (added 2026-11-01)

The author compiled v1.2 himself and the PDF was measured against the sources it came from. Method and
row-level results: `P1_audit/audit_pages.py`, `P1_audit/page_audit_results.csv`,
`P1_audit/section_pagemap.csv`, narrative in `P1_audit/PAGE_LEVEL_AUDIT_2026-11-01.md`. Gate:
`python3 P1_audit/check_page_audit.py` → `PASS (checks=26, fail=0, ...)`.

Measured, so nobody has to guess tomorrow:

| Quantity | Value |
|---|---|
| Pages / words | 140 / 63,584 (author's rebuild, 16:58:57 UTC; the first build measured 63,503) |
| Body (sections 1–17) | pp. 14–120, 43,543 words |
| References | pp. 121–126; 107 cited works, 144 `.bib` entries (37 uncited reserve) |
| Appendices A–F | pp. 127, 134, 136, 137, 139, 140 |
| Numbered equations | **136** (the "166" used in planning was never counted; retired) |
| Figures / tables | 16 (1–16) / 53 (1–53), both contiguous |
| Unresolved refs / missing cites / leaked LaTeX | 0 / 0 / 0 |
| Equation register | 29 rows: DERIVED 2, PRIMARY-SOURCE-CHECKED 4, CONDITIONAL 3, VERIFIED-SYMBOLIC 1, UNVERIFIED 16, OPEN 2, WITHHELD 1 |

Four things were changed as a result, all recorded in `CHANGELOG_v2.md` (entry `v1.2a`) with pre-edit copies
in `paper_v2/versions/v1.2_edits_2026-11-01/`:

1. Appendix A legend gained the two labels it was already using; **no verdict was rewritten**.
2. The un-`\input` file `appendices/energy_flux_derivations.tex` left the build tree for `paper_v2/working_notes/`.
3. Chester 1963's DOI was verified against Crossref and recorded; Cattaneo 1948 and Vernotte 1958 now say
   plainly that no DOI exists.
4. `P1_audit/check_source_audit.py` now asserts the **frozen v1.1 snapshot** is untouched and that every change
   to the working sources is declared in the version log — the old assertion forbade editing at all, which
   contradicted amendment 1.

**Rebuild verified.** The author rebuilt and the four fixes were confirmed *in the PDF*, string by string (section 5 of
`P1_audit/PAGE_LEVEL_AUDIT_2026-11-01.md`): legend labels, EQ-014/EQ-029 rows, the re-pointed Appendix-A sentence,
`doi: 10.1103/physrev.131.2013` on Chester 1963, and the two "No DOI assigned" notes. The drift check (P25) now passes.

**Equation inventory done, register expansion still open.** `P1_audit/equation_inventory.csv` now lists all
136 printed equations (number, label, section, subsection, file) and the list agrees exactly with the numbering
the PDF prints; `P1_audit/register_linkage.csv` records how far each of the 29 register rows can be tied to a
printed equation — **11 of 29 mechanically, 4 need a choice among restatements, 14 are prose-only**. The register
was not edited: which row means which equation, and whether to expand 29 → 136 or to keep a curated register, is
the author's decision, not the auditor's.
