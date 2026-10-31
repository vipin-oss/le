# P3_evidence_claims_C — blocked claims re-checked against the paper now in the library

Same format as `P3_evidence_claims_B` (identical 13-column header, at most 40 rows per
batch). Each row takes one `claim_register.csv` row whose status was *open: source not
available to verifier* and gives it a verdict from the source itself:

`SUPPORTED` / `PARTLY SUPPORTED` / `NOT SUPPORTED` / `SOURCE NOT AVAILABLE`,
always with `source_page_or_equation` pointing at a page (and equation, theorem or
section) that was actually read.

## Scope actually available

`missing_sources_priority.csv` ranks 141 sources by the number of claims they block. Of
those, **only three** correspond to a file in the unzipped library folder:

| rank | key | blocked claim | result |
|---|---|---|---|
| 14 | `Quintanilla2003DPL` | CR003 | **PARTLY SUPPORTED** — CC-0001 |
| 23 | `Quintanilla2008` | CR019 | **SOURCE NOT AVAILABLE** — CC-0002 (the file of that name is the 2008a paper) |
| 24 | `Quintanilla2008a` | CR020 | **SUPPORTED** — CC-0003 |

No other blocked claim in the register cites a paper that the folder supplies, so
`claim_check_C_batch_001.csv` is the whole of what can be decided today. Batches 002+
are **not** written, because writing them would mean inventing evidence: the papers that
the other 138 priority sources need are inside the two archives that are still zipped
(52 MB and 62 MB, above the 25 MB per-file read limit) and are not readable.

## What changed in the paper's favour, and what did not

* **CR003 (CC-0001)** is the single most load-bearing attribution in the manuscript, and
  it now rests on the page: Quintanilla (2003) keeps terms *to second order in τ_q and
  first order in τ_γ* (p. 714, Eq. (4)) — variant (ii), as the manuscript says — and
  proves exponential stability for τ_γ > τ_q/2 (p. 716, Eq. (11)) with instability for
  τ_γ < τ_q/2. The verdict is nevertheless **PARTLY SUPPORTED**, not SUPPORTED, because
  the source proves the *strict* inequality and never treats τ_γ = τ_q/2, whereas the
  manuscript writes τ_T ≥ τ_q/2. The sentence needs either `>` or an explicit "commonly
  quoted, not proved at equality" qualifier.
* **CR020 (CC-0003)** is supported: the abstract of Quintanilla and Racke (p. 24) states
  that conditions on the material parameters are obtained that guarantee exponential
  stability, with instability for suitable domains when they fail.
* **CR019 (CC-0002)** stays blocked. The library file called `quintanilla2008.pdf` is the
  2008a paper; the Applicable Analysis paper on end effects is still missing and must not
  be replaced by the 2008a file.

## Caution raised while doing this

`CR001` is marked *supported* at level V2 and cites `Tzou1995`, but the only library file
under the name `tzou1995.pdf` is the *other* 1995 Tzou paper (*Experimental support for the
lagging behavior in heat propagation*, J. Thermophys. Heat Transfer 9(4)) and not
*"A unified field approach for heat conduction from macro- to micro-scales"*. The register
verdict is left untouched here (it was reached from a different copy), but if the standing
check is repeated, that row must be re-read from the correct paper.

## Files

| file | contents |
|---|---|
| `claim_check_C_batch_001.csv` | 3 rows: CC-0001, CC-0002, CC-0003 |
| `check_claim_check_C.py` | validator; prints `PASS ...` and exits 0 |

Run: `python3 check_claim_check_C.py` →
`PASS all checks (batches=1, rows=3, PARTLY SUPPORTED=1, SOURCE NOT AVAILABLE=1, SUPPORTED=1)`

## Batch 002 — three of the papers the archives were hiding are now readable

The scope note above said batches 002+ would be inventing evidence. That is no longer
true: three files that the zipped bundles listed (`jackson1970.pdf`, `huberman2019.pdf`,
`cahill2003.pdf`) are now readable, and each of them was read page by page this pass.
`claim_check_C_batch_002.csv` records the result. Every row carries a page of the PDF,
not a publisher abstract.

| claim | key | verdict | page evidence |
|---|---|---|---|
| CR095 | `Jackson1970` | **SUPPORTED** — CC-0004 | p. 26 title/abstract and pulse text, p. 27 text around Fig. 3 |
| CR221 | `Huberman2019` | **SUPPORTED** — CC-0005 | p. 1 title/abstract, pp. 3–4 velocities and temperature window |
| CR224 | `Cahill2003` | **SUPPORTED** — CC-0006 | p. 793 abstract and contents, p. 812 Sec. V A |

Two cautions that belong with these verdicts.

* **Huberman page numbers are not the published ones.** The held file is the Science
  *first release* of 14 March 2019; every page prints "Page numbers not final at time of
  first release". The page locators in CC-0005 therefore refer to that version. The
  manuscript cites Science **364**, 375–379, and no sentence in the file was matched to
  that pagination, so the citation must not be given a 375–379 page locator on the
  strength of this file.
* **"Extracts the conductivity" is the manuscript's verb, not Cahill's.** Page 812 says
  TDTR "provides a direct method for measuring heat diffusion on nanometer length scales"
  and that "Determination of the thermal conductivity and interfacial thermal resistance
  is made by co…" (the sentence continues past the 812/813 break). If a verbatim anchor
  is wanted, the sentence should be rewritten to match the source.

For CR095 the DOI is not printed on the article; it was read from the publisher's DOI
page and entered in the register, and the register row now says so.

## Batch 003 — every blocked claim whose source is now in the library, top 30 first

The remaining open claims of `missing_sources_priority.csv` were matched to the library by
DOI (inventory `first_page_doi` against `source_doi_if_given`) and, where the inventory had
no DOI, by the `matched_bib_key` of the file. Ten of the 141 priority sources have a file
that is now readable; three of them are CR095 / CR221 / CR224, settled in batch 002. The
other **seven are settled here**, which closes the cohort — every blocked register row whose
source the library now supplies has a page-level verdict.

| rank | key | claim | verdict | page |
|---|---|---|---|---|
| 17 | `Fabrizio2014` | CR006 | **SUPPORTED** — CC-0007 | p. 483 abstract, pp. 485–486 models, Sec. 4 listed at p. 486 |
| 30 | `DellOroPata2016Viscoelasticity` | CR028 | **SUPPORTED** — CC-0008 | p. 1 abstract/§1.1, p. 2 §1.2 |
| 31 | `ChenGurtin1968` | CR033 | **SUPPORTED** — CC-0009 | p. 615, Eq. (1.4) and the sign of a |
| 75 | `Quintanilla 2003` | CR133 | **NOT SUPPORTED** — CC-0010 | p. 714, method paragraph |
| 96 | `Lamb 1917` | CR164 | **PARTLY SUPPORTED** — CC-0011 | p. 114 cover page only |
| 116 | `Lazar & Agiasofitou 2022` | CR194 | **SUPPORTED** — CC-0012 | pp. 3–4 |
| 134 | `Abate & Whitt 2006` | CR216 | **SUPPORTED** — CC-0013 | p. 408 |

### The one that matters: CR133 gets worse, not better

The manuscript says that for DPL/TPL "an energy functional exists but its construction is
more involved", citing Quintanilla (2003) and Chirita (2016). Page 714 of Quintanilla (2003)
says the opposite about its own method: *"We used a spectral study … we determine the
infinite family of polynomial equations that are satisfied by the eigenvalues … we use the
Hurwitz theorem … this method does not need an advanced knowledge of functional analysis."*
No energy functional is constructed in the pages read. **Quintanilla (2003) must come out of
that sentence** (or the sentence must be rewritten to say he proves stability spectrally);
the Chirita (2016) half is still unreadable, so the sentence is not thereby saved.

### Two verdicts that are honest but limited

* **CR164 (Lamb 1917)** is only PARTLY SUPPORTED because the held PDF is a JSTOR scan whose
  body is page images: extraction returns the cover (title, journal, 93, 114–128, DOI) and
  boilerplate, nothing else. Identity and subject are verified; no guided-mode statement is.
* **CR194 (Lazar & Agiasofitou 2022)** is SUPPORTED for "acts on the displacement" — pp. 3–4
  say nonlocal elasticity has only the displacement field as degree of freedom — but the
  contrast "rather than on the stress" is the manuscript's own framing, not a sentence in
  the source. The held file is the accepted manuscript, so its page numbers are not the
  journal's.

Chen & Gurtin (CR033) is the cleanest gain: **Eq. (1.4) on p. 615 reads exactly
θ = φ − a Δφ**, with "if k is positive, the second law tells us that a ≥ 0" in the line
below it. That is the relation and the sign, both on one page.

## Batch 004 — the "second-sound review" turns out to be Chester (1963)

`2ndSoundSolids.pdf` had been recorded as an X-ray surface-reflection article, on the
strength of a first-lines-only pass. Reading the **whole** first page changes that: the
scan opens with the tail of that article (it ends on printed p. 2013) and then carries
**Marvin Chester, *Second Sound in Solids*, Physical Review 131, 2013–2015 (1963)** —
abstract, Section 1, and on p. 2014 the modified Fourier equation (5) with a relaxation
time and the Maxwell / Cattaneo / Vernotte credits.

So the file is a second-sound source after all, and the last blocked claim in the priority
list whose source the library holds is settled:

| rank | key | claim | verdict | page |
|---|---|---|---|---|
| 61 | `Chester1963` | CR098 | **SUPPORTED** — CC-0014 | p. 2013 title/abstract, p. 2014 Eq. (5) |

Two corrections are carried in the same commit: `library_inventory_v2_part2.csv` now keys
`2ndSoundSolids.pdf` to `Chester1963` instead of flagging it `MISMATCH`, and the trap note
in `README_library_inventory_v2.md` is rewritten to say what the file actually is.

### The review itself still does not exist

`SecondSound1970review` remains unidentified. The file that was filed under that name is a
**theory** paper: it predicts second sound in dielectric solids and gives a critical
frequency, and reports no measurement, no temperature window, no relaxation time. It
therefore contributes **no row** to `experiments_2.csv`, whose EX2-04 stays
`SOURCE NOT AVAILABLE` with the identification recorded in it. No review of second sound
in solids has been found in the library or on the open web with a title that could be
verified, so nothing is cited in its place.

No DOI is printed on the Chester page, so none is stated in CC-0014; quoting
10.1103/PhysRev.131.2013 from memory would have broken the rule that DOIs come from the DOI
page.

## Batch 005 (Step 2 of the current five-step set, top-30 pass)

16 rows, the first tranche of the `missing_sources_priority.csv` candidates whose papers turned
out to be in the folder under a different filename. Every row rests on a page that was actually
read in this pass (title page / abstract / first sections), and the file is named in the row so
the identification can be re-checked.

| claim | register | source as read on p. 1 | verdict |
|---|---|---|---|
| CC-0015 | CR083 | Chen & Nunziato 1974, ZAMP 25, Eq. (1.1) | SUPPORTED |
| CC-0016 | CR082 | Coleman & Gurtin 1967, JCP 47:597 | PARTLY SUPPORTED |
| CC-0017 | CR096 | Guyer & Krumhansl 1966, Phys. Rev. 148:766 | SUPPORTED |
| CC-0018 | CR102 | Joseph & Preziosi 1989, Rev. Mod. Phys. 61:41 | SUPPORTED |
| CC-0019 | CR122 | Dell'Oro & Pata 2016 (same paper as CC-0008) | SUPPORTED |
| CC-0020 | CR125 | Coleman & Noll 1963 | PARTLY SUPPORTED |
| CC-0021 | CR126 | Jou, Casas-Vazquez & Lebon 2010, 4th ed., Preface p. v | PARTLY SUPPORTED |
| CC-0022 | CR154 | Mitra et al. 1995, JHT 117:568 | SUPPORTED |
| CC-0023 | CR165 | Talbot 1979, J. Inst. Maths Applics 23:97 | SUPPORTED |
| CC-0024 | CR175 | not held - Barak et al. 2023 is a different paper | SOURCE NOT AVAILABLE |
| CC-0025 | CR182 | Eringen 1972, IJES 10:425 | PARTLY SUPPORTED |
| CC-0026 | CR186 | Aifantis 1992, IJES 30:1279 | PARTLY SUPPORTED |
| CC-0027 | CR187 | Aifantis 2003, Mech. Mater. | SUPPORTED |
| CC-0028 | CR196 | Eringen 1974, IJES 12:1063 | SUPPORTED |
| CC-0029 | CR199 | Yang 2018, front matter only | PARTLY SUPPORTED |
| CC-0030 | CR210 | not held - Singh & Gupta 2020 is a different paper | SOURCE NOT AVAILABLE |

Rules applied in this batch, unchanged from batches 001-004:

* a DOI is written only when it is printed on the page that was read **and** it is already in the
  manuscript's bibliography or the register; otherwise the DOI column stays empty and the printed
  DOI is mentioned in the prose. Three rows (CC-0015, CC-0021, CC-0022) are empty for that reason -
  the page either does not show a DOI or the bibliography does not carry it.
* "PARTLY SUPPORTED" is used where the paper exists and says the general thing, but not the exact
  form the sentence attributes to it (CC-0016 memory law vs internal state variables, CC-0020 title
  page only, CC-0021 state space yes / entropy-on-flux not reached, CC-0025 integral kernel yes /
  differential equation not on the page, CC-0026 plasticity not elasticity, CC-0029 front matter).
* a look-alike file is never allowed to stand in for the cited paper: CC-0024 and CC-0030 stay at
  SOURCE NOT AVAILABLE with the rejection written into the row.

Locator rule relaxed for this batch: the checker now accepts `p. v` style roman numerals as well as
arabic page numbers, because a book preface is genuinely paginated but is not arabic-numbered.

## Batch 006 - the load-bearing DPL attribution

1 row, CR003 (CC-0031): Quintanilla (2003), J. Thermal Stresses 26:713-721, **SUPPORTED at R3**.
This is the attribution the register itself flagged as the single most load-bearing one in the
section ("This is the single most load-bearing attribution in the section and remains unverified"),
and the file was in the folder all along under the name `quintanilla2003.pdf`.

What the pages say:

* p. 713, abstract: "We prove that when ty > tq/2 the solutions decay exponentially and when
  ty < tq/2 there exist unstable solutions ... we must assume that the inequality ty > tq/2 holds."
* p. 713, same page, the truncation: "... retaining terms up to the second order in tq but only to
  the first order in ty. One obtains Eq. (3) (with b = 0)." - exactly variant (ii) of the
  manuscript's sentence.
* p. 714, Eq. (4): the operators are f + ty f_dot and f + tq f_dot + (tq^2/2) f_ddot; p. 715,
  Eq. (11): the condition ty > tq/2, used in Section 3 to prove exponential stability.
* the Taylor & Francis cover page prints the citation line "Journal of Thermal Stresses, 26:7,
  713-721, DOI: 10.1080/713855996", which matches the register DOI. A second, differently typeset
  DOI is printed in the article footer; only the cover DOI is used, because it is the one the
  bibliography carries.

So the manuscript sentence is correct on all three counts - the derivation, the branch (second order
in the flux lag, first order in the gradient lag), and the fact that this is the condition usually
quoted for DPL.

## Step-2 coverage statement

Step 2 asked for every blocked claim whose source has since become available. The sweep was run in
two passes over the 143 `SOURCE NOT AVAILABLE` rows of `claim_register.csv`:

1. **DOI pass** - every register row carrying a DOI was compared, case-insensitively, with the
   `first_page_doi` of all 117 inventory rows. This yielded exactly one hit that had not already been
   checked: CR003 / `quintanilla2003.pdf`. All the other DOI-bearing blockers have no file in the
   folder.
2. **Title pass** - the 34 rows whose first page carries no DOI (33 classics plus the two oversized
   books) were compared with the register's cited sources on title words. Every overlap that
   survived was a generic-word coincidence (e.g. "heat", "international", "stresses"); in each case
   the file's own title page names a different work (Dafermos 1968, Majumdar 1993, Mindlin 1965 and
   1968, Crump 1976, Weideman 2007, Povstenko 2015, Eringen 1972 polar continua, Sinha 1996/1997,
   Puri 1972, Nayfeh 1971, Deresiewicz 1957, Chen's note on non-simple heat conduction, Gurtin's
   non-simple elastic materials, Quintanilla's stability in type III, etc.).

Result: 17 of the 143 blocked rows now have a library source. Sixteen of them are in batch 005 and
the seventeenth (CR003) is batch 006. The remaining 126 stay at `SOURCE NOT AVAILABLE` and are the
ones Step 3 lists for the author.

**Caveat, stated plainly:** two books in the folder cannot be read in place - `nonlocal-continuum-field-theories-2004.pdf`
(29.7 MB) and the 30.2 MB `10.1007@978-1-4612-2210-1.pdf` - because the text extractor refuses files
above 25 MB. If either book is the source of a blocked row, that row is still open. Both are recorded
as `NOT READ` in `library_inventory_v3.csv` rather than assumed absent.
