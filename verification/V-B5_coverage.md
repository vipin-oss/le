# V-B5 — citations and literature base (Round R3)

**Task.** B5a: audit the 56 keys in `phase5/master/references_local.bib`. B5b: build a
DOI-verified candidate base of ≥400 records. B5c: this report. B5d: `make_bibtex.py`.

**Result in one line.** The audit found **one fabricated reference and eleven metadata defects**;
the literature base stands at **149 records, not 400** — the shortfall is stated in §4 with the exact
reason and the exact remaining work.

---

## 1. B5a — the 56 existing keys

Full table: `verification/REFERENCE_AUDIT.csv` (56 rows, one per key). Counts by verdict:

| verdict | n | meaning |
|---|---|---|
| OK | 38 | DOI resolves in Crossref and title/author/year/volume agree |
| NO-DOI | 4 | book or pre-1960 journal: no DOI exists, verifiable only in a library |
| KEY MISMATCH | 2 | the key attributes the paper to the wrong authors |
| TYPO | 2 | author initial wrong |
| YEAR CHECK / YEAR WRONG | 3 | year is the online-first year, or plainly wrong |
| CHECK PAGES / CHECK | 2 | page range or venue wrong |
| SUSPECT | 1 | entry cannot be verified at all |
| ATTRIBUTION | 1 | real paper, but cited in a way that misdates the theory |
| LOW VALUE | 1 | real but 0 citations, in a weak venue, supporting a claim with better sources |
| OFF-TOPIC | 1 | real paper, nothing to do with this subject |
| **FABRICATED** | **1** | **DOI does not exist and no such paper can be found** |

### 1.1 The fabricated reference (decisive)

`references_local.bib` entry `Guyer1990`:

> Guyer, J. E. and McCracken, J. A. (1990). "Second sound in solids." *Physical Review A* **41**:6371–6381. DOI `10.1103/PhysRevA.41.6371`.

- Crossref lookup of that DOI returns **"Resource not found"** (checked 2026-10-22; the same route
  returns Biot 1956 normally, so the route is not at fault).
- A bibliographic search on those authors plus "second sound" returns **no 1990 Physical Review A
  paper**, and no author named McCracken in this literature.
- The real anchors, all found in Crossref, all missing from the bibliography:

| what it is | reference | DOI |
|---|---|---|
| dispersion relation for second sound | Guyer & Krumhansl, *Phys. Rev.* **133**:A1411 (1964) | `10.1103/PhysRev.133.A1411` |
| phonon hydrodynamics / thermal conductivity + second sound | Guyer & Krumhansl, *Phys. Rev.* **148**:778 (1966) | `10.1103/PhysRev.148.778` |
| first derivation of a finite thermal-wave speed in solids | Chester, *Phys. Rev.* **131**:2013 (1963) | `10.1103/PhysRev.131.2013` |
| the experiment | Ackerman, Bertman, Fairbank & Guyer, *PRL* **16**:789 (1966) | `10.1103/PhysRevLett.16.789` |

This matters beyond one line: the manuscript cites `Guyer1990` in the paragraph on the
**experimental** phase (sec02:17), which is the paragraph that establishes "second sound was
measured". The citation that carries that claim does not exist. A referee who checks it will not
read further.

### 1.2 Wrong attribution to a named author (serious, 5 citations)

`Eringen1968b` → DOI `10.1016/0020-7225(68)90037-2` resolves to *"The linear theory of micropolar
thermoelasticity"*, IJES **6**:37–47 — whose authors are **Tauchert, Claus and Ariman**, not
Eringen. The key is cited **5 times**, including in §5 (multiphysics) and §7 (nonlocal), i.e. in the
places where the review is building an argument about Eringen's programme. Either rename the key to
`Tauchert1968` or cite Eringen's own micropolar papers.

### 1.3 The rest, briefly

- **`Sharma2022`** → the paper is **Sherief & Hussein**, *Acta Mechanica* **234**:535–552 (2023);
  the key and the entry name authors who did not write it, and use the online year. Cited 4×.
- **`Iesan2013`** → *Thermoelastic Models of Continua* is **2004**, not 2013.
- **`Povstenko2004`** → JTS **28**(1):83–102 is **2005** (DOI year is the online year).
- **`Barak2023JTS`** → vol **47**(2):189–216 is **2024**.
- **`Vernotte1958`** → the bib's pages (449–482) are not the famous note; Vernotte's
  heat-conduction paradox note is *C. R. Acad. Sci.* **246**:3154 (1958). **Check the page range.**
- **`Nowacki1975`** → "Nowacki, Z." should be **W.** (Witold). **`Gorenflo1997`** → "I." should be
  **R.** (Rudolf). **`Luchko2010`** → "Luchko, I., AMS 35" could not be matched to any real volume;
  probably a mis-remembered title.
- **`Abdalla2022`** → a 240-page **cosmology** review, cited in the conclusions
  (`sec17:79`). It cannot support any statement in this paper. Delete.
- **`Quintanilla2019`** (MGT) → real and correct, but the bibliography contains **no Moore & Gibson
  (1960) and no Thompson (1972)** entry, so a reader is left with the impression that MGT is a 2019
  theory. Add the two originals.
- **`Marotti2013`** → 0 citations, Hindawi "Journal of Engineering", supporting variational
  principles that have far stronger sources. Replace.
- **`Achenbach1973`** is the single most-cited item (11×) and **`Chandrasekharaiah1986`** — an AMR
  review of exactly this subject — is cited **once**. That ratio is what a hostile referee notices
  first.

### 1.4 What the audit could not do

Claim-support was judged only where I had already read the context (`§9.7`, `§10`, `§3.8`, `sec02`);
the other rows say UNVERIFIED. The two §9.7 attributions (`Barak2023*`, `Gupta2023IJNMF`) remain
**not checkable** here — the papers' flux conventions are not quoted in the manuscript and I did not
open them (`V-B4` CL-021/022).

---

## 2. B5b — the literature base (`LITERATURE_BASE.csv`)

**149 records, every one returned by Crossref (or OpenAlex for the DOI lookup), all with DOIs
except the four archival items already in the bibliography.** No record in the file was written from
memory; the invented-entry rule is the reason the file is short (§4).

Coverage by sub-area:

| sub-area | n | sub-area | n |
|---|---|---|---|
| classical coupled thermoelasticity | 23 | second sound / ballistic heat | 8 |
| memory-dependent / fractional | 21 | piezothermoelasticity | 6 |
| Green–Naghdi | 17 | energy flux / dissipation / well-posedness | 5 |
| dual/triple phase lag | 13 | Moore–Gibson–Thompson | 2 |
| nonlocal / gradient / Eringen | 11 | Green–Lindsay | 2 |
| Lord–Shulman | 10 | numerical methods | 1 |
| two-temperature | 10 | **reflection–transmission / interfaces** | **1** |
| plane waves / dispersion / Rayleigh–Lamb | 10 | micropolar / porous / semiconductor | 9 |

Era profile: 1 record in the 1950s, 9 in the 1960s, 9 in the 1970s, 13 in the 1980s, 14 in the
1990s, 23 in the 2000s, 37 in the 2010s, **43 from 2020 on**. That is the right shape for a review
that claims to cover the modern period.

### 2.1 The ten most important records in the base

Ranked by citations, then by role (the ranking is not the point; the last two entries are):

| # | record | cites | why it is here |
|---|---|---|---|
| 1 | Eringen 1983, *J. Appl. Phys.* 54:4703 | 4812 | the differential nonlocal model the review uses as (7.2) |
| 2 | Lord & Shulman 1967 | 4521 | the theory the review opens with |
| 3 | Caputo 1967 | 4469 | the fractional operator of §6 |
| 4 | Green & Lindsay 1972 | 2947 | the two-time theory, still unopened by this project |
| 5 | Biot 1956 | 2854 | the coupled framework everything modifies |
| 6 | Green & Naghdi 1993 | 2402 | the lossless reference model |
| 7 | Tzou 1995 | 2148 | DPL |
| 8 | Joseph & Preziosi 1989, *RMP* | 1654 | the mathematical status of heat waves |
| 9 | Chandrasekharaiah 1998, *AMR* | 1284 | **a predecessor AMR review; must be engaged with, not merely cited** |
| 10 | Ezzat 2010, *J. Heat Transfer* 132, "Theory of fractional order generalized thermoelasticity" | 387 | the most-cited fractional-thermoelasticity model paper after Caputo |

### 2.2 Obvious holes, stated as holes

1. **Interface/reflection–transmission physics: 1 record.** This is the manuscript's own headline
   mechanism (§9, and the three-B3/B4/B5 threads of this project) and the base has essentially
   nothing on it. The Sinha–Elsibai, Sharma–Kumar–Chand, Singh–Kumar, Abd-Alla and A.N. Sinha papers
   named in `V-B3c` §3.4 are **not in the base** because I did not re-verify them in this tranche.
2. **Well-posedness / stability / uniqueness: 5 records.** For a review whose central claim is that
   "no single admissibility condition applies", the mathematical-analysis literature is the missing
   half of the argument. Quintanilla's and Racke's series are barely represented; Dreher–Quintanilla–
   Racke 2009 (the one full text this project has actually opened) is **not** in the base.
3. **Experiments and measured parameters: 1 record.** No measured relaxation time, no measured
   nonlocal length, no second-sound velocity table. The review says repeatedly that these parameters
   are rarely measured — that claim needs the measurement papers in the bibliography, not only in
   the prose.
4. **Moore–Gibson–Thompson: 2 records** and neither is an original (Moore & Gibson 1960, Thompson
   1972). 
5. **Green–Lindsay: 2 records**, and the GL equation dispute of `V-B4_recheck` shows exactly why
   more are needed.
6. **Books: 1.** Hetnarski & Ignaczak, Ignaczak & Ostoja-Starzewski, and the Nowacki/Povstenko
   monographs the manuscript cites are not represented as records.

### 2.3 What a hostile referee in each sub-area would say

- **Classical/LS (a Chandrasekharaiah or Ignaczak referee):** "The review cites the 1998 AMR review
  four times and never says what it established, and it re-derives results that are in it. Also, it
  states the LS system without saying that the flux law is Cattaneo's and that Cattaneo (1948) and
  Vernotte (1958) are the same law independent of LS."
- **Nonlocal (an Eringen-school referee):** "The review presents the differential nonlocal model
  without the sentence that matters — that it is the Helmholtz-kernel approximation, that it produces
  a finite *frequency* cutoff and not a finite speed, and that it has no length-scale identification
  procedure that is not circular. Askes & Aifantis 2011 is cited but its main warning (gradient and
  nonlocal forms are not interchangeable) is not used."
- **Well-posedness (a Quintanilla referee):** "Three of the models in this review are ill-posed for
  ranges of their parameters. The review says 'admissibility depends on the model' and stops. Which
  ranges? For DPL the answer is known (τ_θ > τ_q/2); for TPL it is known to be delicate; for MGT it
  is a one-line Fourier argument. Giving the answer would have cost a page."
- **Second sound / experiment (a Kovacs-type referee):** "The review's own bibliography cites a
  second-sound paper that does not exist, and does not cite the 2015 heat-pulse experiments
  (Kovacs & Ván) that the whole finite-speed discussion turns on."
- **Interfaces:** "Section 9 asserts that energy ratios are the most sensitive test of a generalized
  theory and then reports no numbers of its own and no verified numbers from anyone else."
- **Numerics:** "One numerical-methods record. The FE/finite-difference literature is larger than
  the entire model literature and is what practitioners actually use."

### 2.4 The twenty names, checked rather than assumed

| name | in the base? | what to do |
|---|---|---|
| Chandrasekharaiah, D.S. | **yes**, 3 (1986, 1996, 1998) | engage the 1998 AMR review explicitly; a referee will be from this school |
| Ignaczak, J. | **yes**, 1 (1985) | add Ignaczak & Ostoja-Starzewski's monograph and the 1999 Hetnarski–Ignaczak review |
| Quintanilla, R. | **yes**, 6 | **essential**: this is the group that decides whether a model is admissible |
| Racke, R. | **no** | must add (Dreher–Quintanilla–Racke 2009; the DPL stability series) |
| Tzou, D.Y. | **yes**, 2 | already the DPL source |
| Hetnarski, R.B. | **no** | must add: the 1999 review and the Ignaczak–Ostoja-Starzewski book are the standard references |
| Ezzat, M.A. | **yes**, 5 | well represented |
| Youssef, H.M. | **yes**, 2 | the two-temperature GN chain |
| Abouelregal, A.E. | **yes**, 2 | heavily published, weakly cited: use sparingly |
| Sherief, H.H. | **yes**, 2 | add Sherief's 1980 anisotropic and 1986 state-space work |
| Eringen, A.C. | **yes**, 4 | keep; fix the 1968 attribution |
| Mindlin, R.D. | **no** | must add (1964 couple-stress, 1965 strain-gradient) — the manuscript cites Mindlin nowhere |
| Sharma, J.N. / Kumar, R. | **partial** (Kumar yes, Sharma no) | add Sharma–Kumar–Chand 2003; the interface section needs it |
| Singh, B. | **no** | add Singh & Kumar 1998 (micropolar reflection) |
| Biswas, S. | **no** | not verified as central here; do not add on the strength of this list alone |
| Marin, M. | **yes**, 1 (co-author) | adequate |
| Sur, A. / Kanoria, M. | **no** | add if the two-temperature/TPL application section stays |
| Bera, R.K. | **yes**, 1 (2004) | adequate |
| Hetnarski (see above) / Nowacki | Nowacki **no** | add Nowacki's monograph and fix the W./Z. initial |
| Kovacs, R. / Van, P. | **no** | **must add** (heat-pulse experiments) if "second sound was measured" is claimed |

---

## 3. B5d — `make_bibtex.py`

Converts `LITERATURE_BASE.csv` to BibTeX with stable keys `FamilyYearWord`, checks duplicate DOIs,
detects key collisions, and prints the records without a DOI. It also **fetches missing author
lists from Crossref by DOI** (`--enrich`) so that the 50 rows whose author block was not captured in
this tranche can be completed without re-harvesting. Run: `python make_bibtex.py --enrich`.

## 4. Why the base is 149 and not 400 — and what closes the gap

The blocker is not access, it is transfer: Crossref returns ~700 bytes per record to this workspace
and the API had to be read through a page-fetch tool, so each 25 records costs a separate call. In
the time available I harvested four query sets (relaxation-time/wave, Green–Naghdi, dual-phase-lag,
and a broad "thermoelasticity + waves + generalized heat conduction" sweep) and stopped at 149
verified records rather than pad the file with entries I had not seen — the invented-entry rule is
the whole point of the exercise, and one invented row would have cost more than the 251 missing ones.

The gap closes mechanically: the same four queries with `rows=100` cached to disk, plus nine further
queries (interface/reflection, well-posedness, MGT originals, second-sound experiments, Mindlin,
Hetnarski/Ignaczak monographs, Racke series, numerical methods, 2024–2026), which are exactly the six
holes listed in §2.2. I recommend B5b-2 to finish this before any prose revision — the base is the
part of the review a referee can check line by line.

## 5. Checks done

1. All 56 keys resolved against Crossref/OpenAlex by DOI, with title/author/year/volume compared.
2. One DOI confirmed non-existent by direct Crossref lookup, then confirmed absent by bibliographic search.
3. The four genuine second-sound anchors located in Crossref and added to the base.
4. Every one of the 149 base records carries a DOI returned by Crossref/OpenAlex in this session.
5. Duplicate-DOI check on the base (0 duplicates after dedupe).

## 6. Confidence

HIGH on the fabricated entry, the two key mismatches, and the year defects (DOI-level evidence).
MEDIUM on claim-support verdicts (context read for a minority of keys; the rest are marked UNVERIFIED).
HIGH on the base counts (computed from the file).

## 7. NOT verified

- Whether the §9.7 attributions are supported by the papers they cite: **not opened**, still not checkable.
- Author lists for 50 of the 149 base rows (captured from DOI-level queries only). `--enrich` fixes this.
- The 251 missing records. Everything else in this file is at DOI granularity.
