# P16 — ASME compliance: first person, DOIs, journal abbreviations, reference order

Evidence only: no `.tex` and no `.bib` file was edited. Everything below was measured on the package
the branch carries and checked against Crossref and the ASME author pages.

**Source package** — `paper_v2/overleaf_package.zip` as it stands on branch `review-paper-v2`
(175 members: `main.tex`, 51 files in `sections/`, 8 `.bib` files, figures). All 439 bib entries were
parsed with a brace-matching parser, not with a regex sweep.

**Headline numbers**

| Check | Result |
|---|---|
| First-person sentences | **77** to rewrite in **38 files** (37 section files + `main.tex`), listed one by one with a rewrite |
| References with no DOI | **31** — exactly the 31 keys supplied; **18 have a real DOI**, **13 have none** |
| Journal names in the bib | **155**; **4** are ASME titles (ASME abbreviation), **151** take ISO 4 |
| Reference style | the `.bib` field order is irrelevant, but **what prints is not ASME**: names print initials-first and the year prints last |

---

## 1. First person — `firstperson_fixes.csv`

**Method.** Each section file (and `main.tex`) was scanned with comments, math (`$…$`, `\[…\]`,
`\(…\)`) and display environments blanked out, so a pronoun inside an equation or a macro argument is
not reported. Sentences were cut on sentence-final punctuation and on structural commands
(`\section`, `\item`, `\caption`, …), so every row is a real sentence of the source, not a paragraph.
The pronoun set was `we, our, us, I`.

**What the scan found.** 82 sentences carried a pronoun token; **5 were false positives** — all of them
the Roman numeral I in "types I, II, III", "GN I--III", "linearized type I" and in one cited title
("… Derivative (I): Difference in temporal modeling"). **77 real hits remain**, and the CSV has one row
each:

| | count |
|---|---|
| rows | 77 |
| files | 38 (`sections/` ×37, plus `main.tex` ×8) |
| pronoun mix | `we` 68, `our` 7, `our`+`we` 1, `I` 1 |
| heaviest files | `s01_intro.tex` 9, `main.tex` 8, `s03_foundations.tex` 5, `s07c_modulus.tex` 4 |

The one `I` is a question in the glossary appendix, "How do I validate a code?", rewritten as "How can
a code be validated?". `main.tex` carries 3 Highlights bullets and 5 abstract sentences, which is why
the front matter is the densest single source of first person.

**How the rewrites were built.** Four devices only, all of them ASME-safe: "this review" / "this
section" as the subject, the passive with the original object as subject ("We derive X" → "X is
derived here"), "the author" where a single person is meant (Appendix A, one row), and "it is
recommended / it has been shown" for the methodological advice (5 rows). Nothing else was touched:
each row was machine-checked to keep

* the **multiset of all numbers** identical to the original,
* the **set of citation keys** (`\cite`, `\citep`, `\citet` arguments) identical,
* the **set of `\ref`/`\cref`/`\eqref` targets** identical,
* and **no first-person token** in the replacement.

Claims were not softened or strengthened. Where the original said "we have not verified it here", the
replacement says "it has not been verified here" — same admission, no first person. Where the original
said "we never merge the two into one unmarked sentence", the replacement keeps the categorical
statement ("The two are never merged into one unmarked sentence"), not a hedge.

**Two judgement calls worth the author's eye.** "We call them types rather than 'waves'" becomes "They
are called types rather than 'waves'" — passive, no loss. And "Our map in \cref{fig:layered}"
becomes "The map in \cref{fig:layered}", which is the one place where a pronoun echoed another figure in
another section; the reference itself is unchanged.

---

## 2. DOIs — `dois_found.csv`

**Method.** Every key was looked up in Crossref (bibliographic query and, for books, ISBN filter), and
the returned record was compared with the bib entry on **title, author, year and venue/pages**. A DOI
was accepted only when those agree. Where Crossref dates something differently from the bib, the row
says so rather than silently preferring one.

**The list is exactly the gap.** The compiled reference list prints **414 entries, 383 of them with a
`doi:` field, 31 without** — and the 31 keys supplied are precisely those 31 entries (checked against
the rendered list: Duhamel is [2], Danilovskaya [3], Chadwick [5], Achenbach [187], Pennes [334] and so
on). So this is not a sample: it is the complete set of DOI-less references.

**18 have a DOI that matches the entry**

| key | DOI | note |
|---|---|---|
| Achenbach1973 | 10.1016/C2013-0-04485-4 | book record, 1973, North-Holland series |
| Ackerman1966 | 10.1103/PhysRevLett.16.789 | PRL 16, 789–791, four authors match |
| Carlson1972 | 10.1007/978-3-662-39776-3_2 | pages 297–345 match exactly; Crossref dates the re-issue 1973 |
| Chester1963 | 10.1103/PhysRev.131.2013 | Phys. Rev. 131, 2013–2015 |
| Cohen2007 | 10.1007/978-0-387-68855-8 | book, 2007 |
| Eringen2002 | 10.1007/b97697 | Springer New York, ISBN 9780387952758; Crossref print year 2004 |
| IgnaczakOstoja2010 | 10.1093/acprof:oso/9780199541645.001.0001 | OUP monograph; Crossref online date 2009 |
| Jackson1970 | 10.1103/PhysRevLett.25.26 | PRL 25, 26–28 |
| Jou2010 | 10.1007/978-90-481-3074-0 | Jou & Lebon, 2010 |
| Kaminski1990 | 10.1115/1.2910422 | ASME J. Heat Transfer 112, 555–560 |
| Laude2015 | 10.1515/9783110302660 | De Gruyter 2015; Crossref carries the main title only |
| Mitra1995 | 10.1115/1.2822615 | ASME J. Heat Transfer 117, 568–573 |
| Pennes1948 | 10.1152/jappl.1948.1.2.93 | J. Appl. Physiol. 1, 93–122 |
| Podlubny1999 | 10.1016/S0076-5392(99)X8001-5 | book-level record, ISBN 9780125588409 |
| Rayleigh1885 | 10.1112/plms/s1-17.1.4 | Proc. London Math. Soc. s1-17, 4–11 |
| Scholte1947 | 10.1111/j.1365-246X.1947.tb00347.x | vol. 5, 120–126; Crossref files it under the journal's current name |
| Scruby1990 | 10.1201/9780203749098 | **reissue only**: the DOI is the 2019 Routledge reissue of the 1990 Adam Hilger book |
| Tzou2015 | 10.1002/9781118818275 | Wiley monograph; Crossref date 2014, bib says 2015 |

**13 have no DOI — and I did not invent one**

| key | why there is none |
|---|---|
| Auld1973 | 1973 Wiley book not registered; Crossref holds only a 1974 review of it |
| Boley1960 | 1960 Wiley book not registered; only two published reviews of it |
| BornKarman1912 | *Physikalische Zeitschrift* 13 (1912) — pre-DOI, not registered |
| Cattaneo1948 | *Atti Sem. Mat. Fis. Univ. Modena* 3 (1948) — not registered; the only title hit is a one-page 2011 CISM item |
| Chadwick1960 | *Progress in Solid Mechanics* vol. 1 — no chapter-level DOI |
| Danilovskaya1950 | *Prikl. Mat. Mekh.* 14 (1950) — not registered |
| Duhamel1837 | *J. École Polytechnique* 15 (1837) — pre-DOI |
| Gulyaev1969 | *JETP Letters* 9 (1969) — Crossref holds JETP Letters only from later volumes |
| Kumar2017 | *Applications and Applied Mathematics* is not a Crossref member journal |
| Love1911 | 1911 CUP monograph not registered; only a 2007 reprint of one chapter in an SEG volume |
| Nowacki1975 | a DOI exists only for the **1986** edition (10.1016/C2013-0-03247-1); using it under 1975 would misdate the source |
| Tzou1997 | a DOI exists only for the **2014 Wiley** second edition (10.1002/9781118818275), a different edition |
| Vernotte1958 | *Comptes Rendus* 246 (1958) — not registered for that period |

**Three cases need a decision from the author, not from me.** (i) *Scruby 1990* — the DOI is the
reissue's; either cite the reissue or leave the DOI out. (ii) *Nowacki 1975* and *Tzou 1997* — either
update the year/edition to the digitized one and quote its DOI, or accept a DOI-less reference.
(iii) *Kumar 2017* — the journal has no DOIs at all; if "every reference must include a DOI" is applied
as a hard rule, this citation is the one that cannot comply without being replaced.

---

## 3. Journal abbreviations — `journal_abbrev.csv`

**155 distinct journal names** appear in the `@article` entries (book titles, series and publishers are
not journals and are not in this file). Each row gives the full name as it stands in the bib, the
abbreviation, and the source.

**4 titles are ASME journals** and take the abbreviation from the ASME list on the journal reference
guidelines page (`https://www.asme.org/publications-submissions/journals/information-for-authors/journal-guidelines/references`):

| full name in bib | ASME abbreviation |
|---|---|
| Applied Mechanics Reviews | Appl. Mech. Rev. |
| Journal of Applied Mechanics | ASME J. Appl. Mech. |
| Journal of Heat Transfer | ASME J. Heat Transfer |
| Journal of Biomechanical Engineering | ASME J. Biomech. Eng. |

Two notes on that table. ASME's own list is printed without periods in most rows ("J Appl Mech") but
the same page's sample reference prints "ASME J Appl. Mech."; the periods version is used here because
it is what AMR itself printed in the 2014 review. And **ASME requires "ASME" in front of all ASME
titles**, which is why the three journal names carry it and the review title conventionally does not.
Also: the journal ASME now calls *Journal of Heat and Mass Transfer* (ASME list: "J. Heat Mass
Transfer") was still *Journal of Heat Transfer* when the two articles we cite were published (1990,
1995), so "ASME J. Heat Transfer" is the right form for them.

**151 titles take ISO 4** (LTWA word list). Where Crossref also publishes an abbreviated
`short-container-title`, it was used as corroboration — but Crossref's short title is often just the
full title again (e.g. "Applied Mathematics Letters"), so it is not an ISO 4 source and was not
followed blindly. Titles that are a single word are not abbreviated under LTWA (Nature, Science,
Materials, Mathematics, Meccanica, Fractals, Silicon, Heliyon).

**Bib hygiene worth fixing while this is done:** the same journal appears under several spellings —
`Applied Mathematics & Optimization` and `Applied Mathematics and Optimization`;
`European Journal of Mechanics - A/Solids` and `… -- A/Solids`; five spellings of the *Proceedings of
the Royal Society of London A*; three of *Zeitschrift für angewandte Mathematik und Physik*. They all
map to one abbreviation each here, but the duplicate spellings also mean the same journal can print two
different ways in the reference list.

---

## 4. Order and name form — `style_check.csv` (439 rows) and what actually prints

**In the files.** Every one of the 439 entries puts `title` before `year` in the `.bib` source
(0 of 439 have year first), and **15 entries** type the first author in given-name-first order instead
of `Surname, Initials`:

`Aifantis1992`, `Aifantis2003`, `Barak2023a`, `Eringen1999`, `Eringen2002`, `Guha2025`,
`Gupta2023a`, `Gupta2023b`, `Gupta2023c`, `Gupta2024b`, `Gupta2025a`, `MindlinTiersten1962`,
`Pathania2023`, `Seema2024`, `Yang2018`.

One entry has **no author field at all**: `Deymier2013` (a book; it carries an `editor`).

**But the field order in the `.bib` is not what decides the printed order** — the `.bst` does. So the
useful check is what the compiled list actually prints. It prints this (page 162 of the 173-page
build):

> [277] A. K. Khamis, A. A. El-Bary, Kh. Lotfy, and A. Bakali. Photothermal excitation … Alexandria
> Engineering Journal, 59:1–9, 2020. doi: 10.1016/j.aej.2019.11.016.

Compare ASME's own sample (same page as the abbreviation list):

> [3] Adams, Z., 2014, "Bending of an Infinite Beam on an Elastic Substrate," ASME J Appl. Mech., 3,
> pp. 221-228.

**Three differences, and all three come from the bibliography style, not from the entries:**

| | printed now | ASME |
|---|---|---|
| Name form | **initials first** ("A. K. Khamis") | **last name then initials** ("Khamis, A. K.") — the ASME page: "the last name of each author followed by initials and/or first name" |
| Year position | **last**, after journal, volume and pages | **after the authors, before the title** ("2014, “Title,”") |
| Journal name | full ("Alexandria Engineering Journal") | abbreviated ("Alex. Eng. J.") |
| DOI | printed (`doi: …`) | wanted for online articles — **this one is already right** |

So the 15 given-name-first entries and the 439 title-before-year fields are *cosmetic* in the source:
`plain`/`unsrt`-family BibTeX styles reorder both at typesetting time. What is not cosmetic is the
style file itself. Fixing part 4 therefore means

1. replacing `\bibliographystyle{unsrtnat}` with ASME's style (`asme2e`, or the `.bst` shipped with the
   AMR template), which alone fixes name order and puts the year after the authors;
2. normalising the 15 author fields and giving `Deymier2013` an author or an explicit editor form, so
   the source stays readable and no future style swap can flip them;
3. abbreviating the 155 journal names per §3 — no `.bst` can do that, because the bib stores full names.

---

## 5. What has to change, in order

1. **Apply `firstperson_fixes.csv`** (77 substitutions, 38 files) — all four invariants already checked.
2. **Add the 18 DOIs**, and decide the three judgement cases (Scruby reissue, Nowacki/Tzou editions,
   Kumar 2017). The 13 "no DOI" entries stay as they are; inventing a DOI for them would be a
   fabrication, and ASME's rule cannot be satisfied for a 1837 memoir.
3. **Abbreviate journals** with `journal_abbrev.csv`, and collapse the duplicate spellings of the same
   journal at the same time.
4. **Swap the bibliography style** to an ASME `.bst`, then re-check that the first citation is still [1]
   and the last [414].
5. **Normalise the 15 author fields** and the one authorless entry.

## 6. Limits

* Crossref was the only registry consulted; publisher pages were not fetched, so a DOI that Crossref
  does not hold is reported as absent rather than as "not found by me". For the thirteen, the reason
  given is the one the record supports (pre-DOI year, unregistered journal, different edition).
* "Match" is judged on the fields Crossref returns — title, authors, year, volume, pages. Where
  Crossref's date differs from the bib's (Eringen 2004/2002, Ignaczak 2009/2010, Carlson 1973/1972,
  Tzou 2014/2015, Scruby 2019/1990) the row says so; those are metadata conventions, not errors in the
  reference.
* The first-person scan covers `sections/*.tex` and `main.tex`. Files the manuscript includes that are
  not prose (figure `.tex` inputs in `figs_tikz/`, scripts) were not scanned; a pronoun inside a figure
  label would not reach print.
* The print-order evidence in §4 is from the 173-page build (`main.pdf` on the branch), not from a
  rebuild of the current sources; the `.bst` line is unchanged, so the rendering is unchanged.
