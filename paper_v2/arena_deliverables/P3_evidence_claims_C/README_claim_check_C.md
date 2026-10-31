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
