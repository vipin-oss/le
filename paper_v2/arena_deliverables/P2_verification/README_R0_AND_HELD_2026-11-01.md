# P2 pass, 2026-11-01: the R0 rows and the four held sources

This note covers the two jobs that were offered as movable without the author: **D**
(the R0 rows of the verification register) and **B** (the four sources that were held but
unread). It records what was decided, on what evidence, and what is still open. Every
number below is recomputed by `check_p2_pass.py` in this folder.

---

## 1. D — what the 32 R0 rows turned out to be

The R0 rows were not 32 unverifiable papers. They were 32 rows whose *candidate* record had
never been checked, and the candidates were often a different work entirely. Each row was
re-decided today against one of four kinds of evidence, in this order of preference:

1. the full text, where this cycle already read it (books and the Carlson chapter);
2. a publisher record opened today (Crossref), for title, authorship, venue, volume, pages;
3. a record already printed inside the row's own note, where the row contradicted itself;
4. nothing, which means the row stays R0.

| verdict | rows | meaning |
|---|---|---|
| METADATA_COMPLETED | 8 | the citation was right but volume, pages and author list were placeholders; now filled from the publisher record |
| METADATA_REPLACED | 8 | the candidate named a different work; replaced with the paper the bibkey actually is |
| UPGRADED_TO_R3 | 4 | the text was already read in this cycle, so the row was never an R0 candidate at all |
| LEVEL_ALIGNED | 2 | the row's own note already recorded a verified printed record while the level said R0; the level now matches its own evidence |
| MEMORY_ENTRY_CONFIRMED | 1 | a bib entry flagged "added from memory" is now confirmed by the publisher record |
| CONFIRMED_AS_CANDIDATE | 2 | the candidate was right (the same book, in two batches) |
| STILL_R0 | 7 | five distinct works, no usable record |

Levels before this pass: 62 R2, 23 R1, 2 R1-noDOI, 32 R0.
Levels after: **62 R2, 42 R1, 4 R3, 4 R1-noDOI, 7 R0** — 119 rows either way.

### 1.1 Seven candidate DOIs resolved to a different paper

This is the part a referee would have caught. Each of these rows carried a DOI that is
perfectly valid and belongs to somebody else:

| bibkey | DOI in the register | what that DOI actually is | correct DOI now |
|---|---|---|---|
| Jackson1970 | 10.1080/01495739208946136 | Green and Naghdi, *On undamped heat waves in an elastic solid*, J. Thermal Stresses 15 (1992) 253-264 | 10.1103/physrevlett.25.26 |
| Rayleigh1885 | 10.15625/0866-7136/19728 | Singh, *Wave propagation in context of Moore-Gibson-Thompson thermoelasticity with Klein-Gordon nonlocality* | 10.1112/plms/s1-17.1.4 |
| Mueller1967 | 10.1007/s00419-026-03092-7 | Srivastava and Mukhopadhyay 2026, *Reciprocity and variational theorems in temperature-rate-dependent two-temperature piezothermoelasticity* | 10.1007/BF00285677 |
| IgnaczakOstoja2010 | 10.1177/1081286519862007 | Quintanilla 2019, *Moore-Gibson-Thompson thermoelasticity* | none: the book has no DOI in what was opened, so the wrong one was removed rather than replaced |
| Kaminski1990 | 10.1016/j.apm.2021.02.028 | Li and Tian 2021, *Fractional order thermo-viscoelastic theory of biological tissue with dual phase lag* | 10.1115/1.2910422 |
| Mitra1995 | 10.1016/j.csite.2021.101211 | Zhang, Sun and Yang 2021, *Bio-heat transfer analysis based on fractional derivative and memory-dependent derivative* | 10.1115/1.2822615 |
| Pennes1948 | 10.1007/s11043-023-09647-3 | Megahid, Abouelregal and Sedighi 2023, *Modified MGT Pennes bioheat transfer model* | 10.1152/jappl.1948.1.2.93 |

Five more rows carried a candidate *title* that belongs to another work, with no DOI to
give it away: Ackerman1966 (the candidate was the Chandrasekharaiah 1986 Applied Mechanics
Reviews survey), Bleustein1968 (a 2026 phason and Lord-Shulman paper), Carlson1972 (Iesan
1986, *A theory of thermoelastic materials with voids*), Chadwick1960 (*Plane waves in an
elastic solid conducting heat*, which is a different paper), and Auld1973 (a 2024 article
about a 1973 book). Podlubny1999 carried a wrong title, a wrong year (1997) and the DOI of
an unrelated journal article.

The pattern is the same in all of them: the candidate column was filled from a search hit
that shared words with the bibkey, not from the reference itself. Two of the borrowed DOIs
are still in the register, correctly, on the rows they actually belong to — Li2021 and
Zhang2021 — which is exactly why the wrong entries looked plausible for so long: they were
real references from neighbouring rows, pasted one line off. That is worth naming in the
paper's own erratum trail: **a DOI is not evidence of identity until somebody reads what it
resolves to.**

### 1.2 What is still R0, and why

| bibkey | work | why it stays R0 |
|---|---|---|
| Chadwick1960 | *Thermoelasticity: the dynamical theory*, Progress in Solid Mechanics 1, 263-328 | no publisher record exists for the chapter and no copy was opened; a Crossref search returned nothing matching |
| Auld1973 | *Acoustic Fields and Waves in Solids*, Wiley 1973 | print-only book; no ISBN-level record was opened in this pass |
| Duhamel1837 | *Second memoire sur les phenomenes thermo-mecaniques*, J. Ecole Polytechnique 15 (25), 1-57 | only a secondary reference-list entry and a periodical-level catalogue record were ever seen; the 1837 issue page was never opened |
| Scruby1990 | *Laser Ultrasonics: Techniques and Applications* | WorldCat and Routledge disagree on the 1990 publisher and differ in the title's punctuation; unresolved |
| Gulyaev1969 | *Electroacoustic surface waves in solids*, JETP Letters 9 | the JETP article page prints p. 37 while the volume 9 index prints p. 63, and neither is the Radiotekhnika i Elektronika page; the disagreement is preserved |

Five distinct works, seven rows. Note that Gulyaev1969 *does* have a bib entry (a correction
to an earlier note in this file's history): it is not an orphan citation key, only an
unresolved page.

### 1.3 The register has duplicate rows

119 rows carry **113 distinct bibkeys**. Six bibkeys appear twice:

| bibkey | batches | levels now |
|---|---|---|
| Bleustein1968 | 002 and 004 | R1 and R2 |
| Danilovskaya1950 | 003 and 004 | R1-noDOI twice |
| Duhamel1837 | 003 and 004 | R0 twice |
| Jou2010 | 003 and 004 | R1 twice |
| Scruby1990 | 003 and 004 | R0 twice |
| BornKarman1912 | 003 and 004 | R1-noDOI twice |

Bleustein1968 is the only one where the two rows disagree on the level, which means one of
the two was verified twice by different routes. The duplicates were flagged, not deleted:
removing rows from a register that another checker counts is a change the author should sign
off, and "113 unique of 119 rows" is the honest way to state the register's coverage until
then.

---

## 2. B — the four held sources: citation verified, text still unread

The four claims that were parked as "held but unread" are CR127, CR152, CR166 and CR196.
None of the four works is in the library — that is now confirmed by name and title-phrase
searches, listed row by row in `HELD_SOURCES_2026-11-01.csv`. What this pass *could* do is
verify that each citation is a real paper, and it did: all four DOIs open a record whose
title, authors, venue and pages match the bib entry.

| claim | work | record verified today | text read |
|---|---|---|---|
| CR127 | Muller and Ruggeri 1998, *Rational Extended Thermodynamics* | yes: Springer Tracts in Natural Philosophy, 2nd ed., 1998 | no |
| CR152 | Gurtin and Williams 1966, *On the Clausius-Duhem inequality* | yes: ZAMP 17, 626-633, September 1966 | no |
| CR166 | Li, Zhang, Li and He 2019, bi-layered laser-pulse heating | yes: IJHMT 144, article 118664, December 2019 | no |
| CR196 | Eringen 1974, *Theory of nonlocal thermoelasticity* | yes: IJES 12, 1063-1077, December 1974 | no |

The claim verdicts are untouched: all four stay SOURCE NOT AVAILABLE. A verified citation is
not a read source, and this file does not pretend otherwise. What changed is the shape of the
remaining work — from "we do not know whether these papers exist" to "we know exactly what is
missing and what it would cost":

- **CR152** is the cheapest to close without the paper. The attribution to Gurtin and
  Williams can be re-based on Coleman and Noll 1963, which the register already holds at R1
  and which is where the Clausius-Duhem route is set out in the form the manuscript uses.
  That is a proposal for the author, not an edit.
- **CR196** is nearly free: the 1974 title is literally *Theory of nonlocal thermoelasticity*,
  so the historical half of the sentence ("Eringen extended nonlocality to thermoelasticity")
  is carried by the record itself. The sentence should be reworded to rest on the title and
  must not attribute a derivation to a paper nobody has read.
- **CR166** is a caution, not a finding: the sentence survives if it stops describing what the
  paper does.
- **CR127** genuinely needs the book, and the alternative source is unread too. It is the one
  of the four that cannot be closed by wording.

---

## 3. What this does and does not change

- The blueprint's P2 exit condition is "no R0 entries". It is **not met**: 7 rows remain.
  It is now 7, not 32, and every one of the 7 has a named next action.
- The submission checklist stays at 0 of 6.
- No claim verdict was changed, and nothing was written into any `.tex` file.
- No source was requested, and no new batch of files was created: this is one resolution
  table, one held-sources table, this note, and a checker.

The register's coverage is still 119 of the bibliography's 323 entries. Repairing the 32 rows
does not extend coverage; it makes the 119 that exist trustworthy, which is the precondition
for extending them.

---

## 4. Later the same day: the register grew from 119 to 204 rows

Repairing the 32 rows did not extend coverage, so a second pass the same day gave a row to every
bibkey in the repository's three bibliography files that had none. There were **86** such keys, and
**85** of them carried a DOI; each of the 85 was checked against the Crossref record, and a row was
added only where the record's title matched the bib entry (content-word overlap 0.80 or better on
all 85, most of them exact). The register now has **204 rows** over **198 distinct bibkeys**, at
**62 R2, 127 R1, 4 R3, 4 R1-noDOI, 7 R0**.

Two of those 85 were checked further, because earlier steps had left them open:

- **Chen and Nunziato 1974 is no longer missing.** DOI 10.1007/BF01590264 is *Thermodynamic
  restrictions on the relaxation functions of the theory of heat conduction with finite wave
  speeds*, ZAMP **25**, 791-798, 1974, by Peter J. Chen and Jace W. Nunziato. Five separate title
  searches had failed to find it; the DOI in the bibliography was right all along.
- **Coleman and Gurtin 1967** is *Thermodynamics with Internal State Variables*, J. Chem. Phys.
  **47**, 597-613, 1967, DOI 10.1063/1.1711937. That is the same DOI the Gulyaev 1969 bib entry had
  wrongly reused, which is now recorded on both rows.

These 85 rows are labelled R1 with a note that says exactly what was and was not checked: the DOI
and the title, not the volume and pages (those still come from the bib entry). The remaining gap to
the blueprint's 323 is **119 works**, and those are keys the repository does not hold - they live in
the manuscript's own bibliography, so that last stretch waits for the Overleaf pull.

### The nine catalogue R0 rows, one by one

The separate 238-entry catalogue check has its own nine R0 rows. Each is now recorded in
`CATALOGUE_R0_2026-11-01.csv` with the record that was opened and the exact action:

| key | outcome |
|---|---|
| Carlson1972 | **resolved**: DOI 10.1007/978-3-662-39776-3_2 (chapter also read in full) |
| Achenbach1973 | **resolved**: DOI 10.1016/c2013-0-04485-4, ISBN 9780720423679 |
| Cattaneo1948 | **resolved as a reprint**: DOI 10.1007/978-3-642-11051-1_5 is the 2011 reprint, not the 1948 original |
| Tzou1997 | **edition warning**: DOI 10.1002/9781118818275 is the 2014 Wiley second edition; pasting it into a 1997 entry would be a new fault |
| Gulyaev1969 | print-only, and its bib DOI 10.1063/1.1711937 belongs to Coleman and Gurtin 1967 and must go |
| Vernotte1958, Nowacki1975, Duhamel1837, Chadwick1960 | print-only; nothing changes until the printed pages are opened |

That leaves **five print-only rows** and **four that can be fixed by an edit to the bib file** -
edits that belong to the author, since the bibliography lives with the manuscript.

## 5. Reproduce

```
cd paper_v2/arena_deliverables/P2_verification && python3 check_p2_pass.py
```

The checker re-reads the register, the resolution table and the held-sources table, and
prints `PASS` only if the level counts, the row counts, the seven removed DOIs and the four
held records still agree with this note.
