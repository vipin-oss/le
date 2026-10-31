# P3 claim check, part A, batch 001

Scope: every sentence in `sections/s06_lags.tex`, `sections/s06b_delay.tex` and
`sections/s07_memory.tex` that makes a specific claim about a cited paper (who
derived, proved, proposed or formulated what, and under which condition).
Output: `claim_check_A_batch_001.csv` (56 rows, 30 claims) and
`missing_sources_A.csv` (36 sources).

## 1. Inputs

| File | Size (bytes) | Citation commands | Distinct keys cited |
|---|---|---|---|
| `sections/s06_lags.tex` | 11,644 | 24 | 37 |
| `sections/s06b_delay.tex` | 3,697 | 0 | 0 |
| `sections/s07_memory.tex` | 8,543 | 21 | 39 |

`s06b_delay.tex` (fidelity of Taylor-truncated lag models) contains no citation
at all: it compares truncations numerically with the exact delay law using the
manuscript's own computation. It therefore contributes no claim row, and its
numbers are manuscript results, not claim rows.

The three files were extracted from `paper_v2/paper_sources.zip` into a scratch
directory outside the repository. No `.tex`, `.bib`, `.pdf` or `.zip` file in the
repository was modified.

## 2. Claim selection

Thirty-eight claim-bearing sentences were identified across the two citing
sections. The task allows at most 30 claims, so 30 were kept (A1 to A30) and 8
were deferred (listed in section 7). The kept set favours sentences that
attribute a named result, condition, definition or model to a named source, and
keeps multi-source sentences intact (one row per cited source, so 30 claims give
56 rows).

## 3. Method

1. For each cited key, the bibliography entry was taken from the manuscript's own
   `.bib` files (key, authors, year, title, journal, volume, pages, DOI). Nothing
   was filled in from memory; fields the bib does not carry are written
   `(absent)`, and a missing DOI is written `no record`.
2. Each cited work was then searched for in the Drive library by author name,
   title fragment, DOI-derived file name and, for the highest-value missing
   items, by full-text search of a distinctive title phrase. Hits were opened and
   identified from the first page (title, byline, journal, volume, pages, DOI)
   before anything was read from them. A file that is merely a different paper by
   the same author was **not** used as a substitute: see A7, where the library
   holds a 2019 Abouelregal article that is not the cited 2020 Scientific Reports
   paper.
3. When the cited work was identified, the pages carrying the cited statement
   were read: in practice the abstract, the introduction, and the equation,
   definition or theorem that the manuscript sentence refers to.
4. Verdicts:
   - `SUPPORTED` - the source states what the manuscript says it states.
   - `PARTLY SUPPORTED` - part of the attribution holds and part does not (wrong
     linking relation, wrong companion theory, different fractional operator,
     scope not visible at the cited location).
   - `NOT SUPPORTED` - the source states something incompatible with the
     sentence. No row in this batch reached this verdict.
   - `SOURCE NOT AVAILABLE` - the work was not located in the library (or, for
     one file, was present but its text could not be extracted). No verdict on
     content is given, and no wording is quoted.
5. Verification levels, in the same spirit as the R0/R1/R2 levels used for the
   reference batches:
   - `V2` - verdict rests on the source's own equation, definition or theorem,
     read in the library copy.
   - `V1` - verdict rests on the source's abstract, title page or first-page
     statement, read in the library copy.
   - `V0` - no source text available; nothing verified.

## 4. Results

| Verdict | Rows |
|---|---|
| SUPPORTED | 15 |
| PARTLY SUPPORTED | 5 |
| NOT SUPPORTED | 0 |
| SOURCE NOT AVAILABLE | 36 |

| Level | Rows |
|---|---|
| V2 | 3 |
| V1 | 17 |
| V0 | 36 |

Found in the library: 20 rows of 56, covering 20 distinct works (no work is cited
by more than one of the 30 claims). Not found: 36 rows, 36 distinct works.

Claims by coverage:

- every cited source verified (8 claims): A6, A8, A9 (three sources), A10, A16,
  A17, A25, A30;
- some sources verified, some unavailable (8 claims): A1, A15, A18, A19, A20,
  A23, A24, A26;
- no verifiable source at all (14 claims): A2, A3, A4, A5, A7, A11, A12, A13,
  A14, A21, A22, A27, A28, A29.

## 5. Rows where the source does not say what the manuscript says

Five rows are `PARTLY SUPPORTED`. Each is a candidate correction; the manuscript
text was not edited.

| Claim | Source | What the source actually does |
|---|---|---|
| A18 | Aldandani 2026 | First page presents a piezo-thermo-electric semiconductor study with fractional, Klein-Gordon nonlocal and three-phase-lag ingredients; MGT is not named in title, keywords or abstract. The sentence attributes "fractional MGT" to it. |
| A19 | Youssef 2006 | Confirms two distinct temperatures (conductive and thermodynamic), but states the difference between them is proportional to the heat supply, not the relation theta = phi - a nabla^2 phi attributed jointly with Chen and Gurtin. |
| A20 | Bassiouny 2020 | Confirms a hyperbolic two-temperature fractional-order model, but the companion theory is one "with two relaxation times" (Green-Lindsay type), not Lord-Shulman or Green-Naghdi as the sentence says. |
| A23 | Ezzat and El Karamany 2011 | Confirms a fractional-order heat conduction law, but built on a modified Riemann-Liouville derivative and a new fractional Taylor series, not the Caputo operator written in the manuscript's display. |
| A24 | Gorenflo, Kilbas, Mainardi and Rogosin 2014 | The library copy is the Mittag-Leffler monograph; its scope fits, but the specific heavy-tail asymptotic for alpha < 1 was not located in the front matter read. Needs a page-level check of the asymptotic chapters before the sentence can be called supported. |

Two notes that are not verdict changes but worth a decision: the three
"combinations with memory-dependent derivatives" sources (A9) are TPL plus MDD
studies of half-spaces and rods, none of them a plane-wave analysis, and Biswas
2019 already contains a magnetic field, which the sentence reserves for Bayones
2021 (A10).

## 6. Sources not in the library

36 works cited by these 30 claims were not located (all listed in
`missing_sources_A.csv` with their bib metadata). They cluster in three groups:

- the analytical and well-posedness literature on DPL and TPL (Quintanilla 2002,
  2003, 2006, 2008, 2008a, 2009; Racke; Fabrizio and Lazzari; Rukolaine; Chirita
  and co-authors; Antaki; Julius and co-authors; van der Merwe and co-authors);
- the classical fractional-calculus and fractional-thermoelasticity sources
  (Caputo 1967; Podlubny 1999; all six Povstenko items; Sherief and co-authors;
  Luchko; Wang and Li part IV);
- the nonlinear-acoustics origin and the semigroup literature for MGT (Moore and
  Gibson 1960; Marchand, McDevitt and Triggiani 2012; Dell'Oro and Pata 2016),
  plus Chen and Gurtin 1968 and two of the three hyperbolic two-temperature items.

The library copy of the author's own material is rich (Gupta, Barak, Das,
Aldandani and co-authors), and that is what makes the available column of this
batch look thin: the theoretical sources the section leans on are largely the
ones missing. A2 is the clearest case - the only attribution of the
tau_T >= tau_q/2 condition to Quintanilla (2003) is unverified, and no copy of
that paper exists in the library.

Priority column in `missing_sources_A.csv` follows the stated rule: high if three
or more claims depend on the source, otherwise medium or low. Because the 30
claims of this batch each lean on a distinct source, every missing work carries
exactly one dependent claim and is therefore `low`; the list is ordered by
dependency count and then by author, so the acquisition order is a matter of
editorial judgement, not of the priority field. If the deferred sentences of
section 7 are added later, Quintanilla (2003) and the Povstenko group would rise
above `low`.

## 7. Deferred claim sentences (beyond the 30-claim limit)

1. "The thermodynamic compatibility and continuous dependence of the TPL model
   are studied in [Chirita2016]" (s06) - same source as A4.
2. "Stability and characterization of plane waves in the hyperbolic
   two-temperature theory are in [Prasad2020]" (s06) - same source as A20.
3. "Memory-dependent derivative modelling was introduced by [Wang2011]" (s07) -
   same source as A25.
4. "reviews and critical discussions of the logic of fractional thermoelasticity
   are given in [Povstenko2016, Yu2024, Gorenflo1997, Povstenko2004,
   Povstenko2007, Povstenko2009]" (s07) - six sources, three of which are present
   and could be checked cheaply.
5. "MDD versions of lag models replace the first-order derivatives ... [11 keys]"
   (s07).
6. "fractional order generalized thermoelasticity was developed by [Youssef2010]
   with its variational principle in [Youssef2010a]" (s07).
7. "fractional order theory of Cattaneo-type thermoelasticity using new
   fractional derivatives was introduced by [Yu2020]" (s07).
8. "the view of thermoelasticity and generalized thermoelasticity as wave
   hierarchies was presented by [Scott2007]; a theory of generalized
   thermoelasticity with memory-dependent derivatives was given by [Shaw2019]"
   (s07).

## 8. Limitations

- The text-extraction route used for the library PDFs does not preserve page
  numbers or page breaks. Locations are therefore given as equation numbers,
  definition and theorem numbers, section names and printed page numbers where
  the first page itself carries them. No page number was guessed and no location
  was inferred from position in the extracted text.
- One library file (a second copy of Tiwari 2021) failed text extraction; the
  same article was read successfully from another copy, so the row is unaffected.
- Absence was established by author-name, title-fragment, DOI-pattern and
  full-text searches of the library, not by an exhaustive catalogue of every
  file. A work recorded as `SOURCE NOT AVAILABLE` means "not located by these
  searches"; it is not a claim that the library contains no copy.
- Quoted wording is capped at 25 words and is reproduced as printed, including
  the extraction's spelling of accented names, which has been reduced to ASCII.

## 9. Files

- `claim_check_A_batch_001.csv` - 56 rows, 11 columns, header as specified.
- `missing_sources_A.csv` - 36 rows, 7 columns.
- `README_batch_001.md` - this note.
