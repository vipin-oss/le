# P19 — patch tables for the seven referee items

Target: `review-paper-v2` @ `6457295` ("Figures: larger lettering (>=7 pt effective)
for AMR/ASME; 153 pp"), read from `paper_v2/overleaf_package.zip` and
`paper_v2/main.pdf` on that branch. Nothing in the manuscript was edited: every
finding below is a patch table for the author to apply after checking.

## What the target actually is

The package holds 415 BibTeX entries in seven files (`refs.bib`, `refs_extra.bib`,
`refs_new.bib`, `refs_atlas.bib`, `refs_P8.bib`, `refs_P10.bib`, `refs_P13.bib`,
391 articles, 21 books, 3 chapters), 52 section files, and a PDF of 153 pages.
The numbering used in this directory was derived from the source and then checked
against the PDF in three independent ways:

* 89 numbered equations: the PDF prints "89 numbered equations" on p. 119;
* 41 figures and 24 tables: the PDF carries Figure 1–41 and Table 1–24 (the last
  two tables are `longtable`s, which is why a plain `table`-environment count gives 22);
* 61 of the 63 caption texts matched the printed caption on the page the PDF puts
  it on, and the eighteen objects referenced from captions were each located by number.

The 157-page revision that P17 and P18 read has different numbers: the Green–Lindsay
equation is Eq. (38) here and was Eq. (39) there, the regime map is Fig. 39 here and
was Fig. 37 there. Numbers in this directory are for the 153-page build only.

## Task 1 — `bib_patch.csv`

The seven references of the P17 `pages_fix` list now carry their DOIs in the
database, so the only open field is the page: none of the seven has a `pages` or
`eid` field, and all seven are article-number journals. All seven were re-queried
at Crossref in one batch on 2026-11-02 and the article numbers confirmed:
014110, 031301, 372, 77, 102103, 190, 105. Volume, issue and year agree with the
Crossref record in all seven cases. The patch field is `eid`, which `asmejour.bst`
supports for article numbers (`asmejour.bst` lines 153 and 1161–1162); `pages`
would render but prints a page range.

One recorded oddity, not a patch: `Julius2017` has year 2017 (online 10 Oct 2017)
while volume 140 issue 3 is the March 2018 printed issue. Whichever convention the
author chooses, it should be stated once.

## Task 2 — `author_name_patch.csv`

Fifteen entries carry at least one given-name-first author (33 author tokens). For
fourteen of them Crossref deposits the surname and given name explicitly, so the
conversion to "Surname, Given" is unambiguous; `Eringen2002` has the same author as
`Eringen1999` and no author list in its own Crossref record, so it is marked
RECORDED rather than VERIFIED. One case cannot be inverted: in `Seema2024` the
first author is a mononym (Crossref deposits family "Seema" with no given name), and
that entry already mixes forms; it is flagged NOT-VERIFIED with no patch.

One detail worth knowing: the Crossref record for `Gupta2024b` has the second
author's given and family names swapped (given "Barak", family "M.S."), so the
surname there comes from the other entries, not from Crossref.

## Task 3 — `journal_patch.csv`, `journal_uniform_names.csv`

The database uses 144 distinct journal names and all but one are written in full.
Six journals show inconsistency:

* *European Journal of Mechanics - A/Solids* — one entry of seven writes the
  separator as `--`;
* *Proceedings of the Royal Society of London* — three spellings, and no single
  title can serve all four papers because the journal changed its title twice
  (ISSN 0950-1207 for 1905–1934, 0080-4630 for 1934–1990, 0962-8444 for 1990–1995),
  so the recommendation is the era title of each volume;
* *Zeitschrift für angewandte Mathematik und Physik* — four spellings for one ISSN
  (0044-2275), including the "ZAMP" suffix and one missing umlaut; the deposits
  themselves are inconsistent;
* *Applied Mathematics & Optimization* — one entry writes "and" for "&";
* *Atti Sem. Mat. Fis. Univ. Modena* — the only abbreviated non-ASME journal name;
  expansion proposed but the journal has no Crossref record (0 results);
* *Comptes Rendus de l'Académie des Sciences* — a LaTeX accent escape in the field
  where the rest of the database is UTF-8; the 1958 title could not be verified.

The ASME privilege is not exercised: the nine ASME entries (one *Journal of Applied
Mechanics*, four *Journal of Heat Transfer*, four *Applied Mechanics Reviews*) are
already written in full, so nothing changes for them.

## Task 4 — `r12_abstract_vs_table4.csv`

Table 4 is `tab:param` ("parameter choices in the template"), printed on p. 14 with
seven rows. The abstract names nine families. The sets differ in both directions:
Green–Lindsay is named in the abstract and has no row (though it has its own
subsection, a row in Table 15 and an entry in the verification register), while
Green–Naghdi is one item in the abstract and two rows in the table. Fractional and
memory-dependent models are named in the abstract but cannot be rows of this table,
because the text after it says they keep the same `G(s)` with `s` replaced. The
P17 report itself gives two counts for the same table (seven at line 228, eight at
line 218); the source and the PDF both have seven. Discrepancy table only, no fix.

## Task 5 — `r15_caption_refs.csv`

Twenty-one cross-references sit inside figure and table captions in this build
(10 `\eqref`, 7 `\cref`, 1 `\Cref`, 3 `\ref`), and all twenty-one resolve to the
object the caption means. Each row gives the number the PDF prints for the target
(Eq. (9), Eq. (14), Eq. (27), Eq. (34), Eq. (38) is not referenced, Eq. (42),
Eq. (43), Eq. (49), Eq. (59), Eq. (68), Eq. (69), Eq. (70), Eq. (74), Eq. (79),
Section 4.3, Section 10.1, Section 11.1, Appendix D, Figure 39, Table 23), the page
the target sits on, the page the caption sits on, and the `sections/*.tex` line of
the target definition, so that every claim in the table can be checked in seconds.
There is no hard-coded number in any of the 63 captions,
so the P17 defect (a caption that typed "Figure 39" when the regime map was
Figure 37) cannot recur: the decision-sequence caption now carries `\Cref{fig:regime}`
and the PDF prints "Figure 39", which is the regime map on p. 85. The second half
of R15 — the caption of Fig. 39 mixing the two loci ωτ₀ = 1 and τ₀ω\* = 1 — is
still there and is recorded as a statement note, with no numbering error and no patch.

## Task 6 — `doi_less_refs.csv`, `editor_paragraph.md`

Fourteen entries carry no DOI: the referee list of thirteen plus `Scruby1990`, which
the P16 pass did not check. Six are pre-DOI journal articles, four are monographs
that were never registered, one is a chapter in a multi-author book, one is an
article in a journal that is not a Crossref member, and two are books for which a
DOI exists only for a different edition (`Nowacki1975`, which the database already
cites in the 1986 Pergamon edition with ISBN 978-0-08-024767-0, and `Tzou1997`).
The DOI evidence is the P16 Crossref record of 2026-11-02 and was not re-queried;
the one ISBN marked VERIFIED-EXTERNALLY is the Nowacki 1986 ISBN, confirmed in P18.
`editor_paragraph.md` gives the four-sentence editor-facing paragraph.

## Task 7 — `gl_ordering.md`

**SOURCE NOT AVAILABLE.** No copy of Green & Lindsay (1972) pp. 5–6 and no copy of
Ignaczak & Ostoja-Starzewski (2010) p. 21 exists in this sandbox, so the inequality
is not transcribed and no external claim is made about it. What the manuscript
prints can be recorded, and in this build the three locations agree: below Eq. (38)
(p. 27), Table 15 (p. 87) and Table 22 (p. 118) all print τ₁ ≥ τ₀ > 0, and the text
gives the mapping τ₁ = α, τ₀ = h/d together with the restrictions it attributes to
Green & Lindsay (dα − h ≥ 0, h > 0), from which the printed ordering follows
algebraically. Whether those restrictions really stand at Eqs. (4.14) and (4.16) of
the 1972 paper remains NOT VERIFIED. Two page images would close the item.

## Gates

`python3 check_p19.py` runs 38 checks (schemas, status vocabulary, DOI allowlist,
no first person, no binary artefacts, README row, and a `git status` check that no
`.tex`, `.bib` or `.bst` file of the manuscript is modified). The gates of P8–P19
all pass before the push.
