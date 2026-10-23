# V-B3c — Literature on reflection/transmission in generalized thermoelasticity

**Phase B3, item c.** Access date 2026-10-22.

> **DEPTH MARKER.** This is a **record-level survey**: six items were verified bibliographically
> (Crossref), **no full text was opened**, so **not one equation or number from these papers was
> checked**. It is a map of where to look plus a list of what to check when the PDFs arrive. It does
> **not** support any claim about what these papers conclude.

---

## 1. Task

B3c: literature on reflection/transmission for the models of §B3a (Biot, LS, GL, GN-II, GN-III, MGT).

## 2. Method

1. Crossref bibliographic queries, restricted to reflection/refraction of plane waves in
   generalized thermoelastic media, plus energy-decay papers for the stability sub-question.
2. Record author/year/title/journal/volume/pages/DOI/counts and access level for each hit.
3. **Do not** paraphrase conclusions: without the full text, a "this paper shows R+T=1" sentence
   would be invention.
4. Supply a per-paper checklist derived from `V-B3b` (C1)–(C5), so the survey becomes actionable.

## 3. Result

### 3.1 The six verified records

| # | Reference | Model | Topic | Access level |
|---|---|---|---|---|
| 1 | Li, Y.; Li, L.; Wei, P.; Wang, C. (2018). "Reflection and refraction of thermoelastic waves at an interface of two couple-stress solids based on Lord–Shulman thermoelastic theory." *Applied Mathematical Modelling* **55**: 536–550. DOI `10.1016/j.apm.2017.10.040`. Crossref 31. | **LS** + couple stress | reflection **and refraction** at an interface (the closest match in the list to a $R/T$ study) | record only |
| 2 | Kumar, R.; Gupta, R. R. (2012). "Plane waves reflection in micropolar transversely isotropic generalized thermoelastic half-space." *Mathematical Sciences* **6**: 6. DOI `10.1186/2251-7456-6-6`. Crossref 4. | generalized (micropolar, TI) | reflection at a free surface | record only (**open access — the cheapest full text to obtain**) |
| 3 | Singh, B. (2018). "Reflection of plane waves from surface of a generalized thermo-viscoelastic porous solid half-space with impedance boundary conditions." *Mechanics and Mechanical Engineering* **22**(4): 1483–1496. DOI `10.2478/mme-2018-0116`. Crossref 3. | generalized thermo-viscoelastic + porous | reflection with **impedance** boundary conditions (a lossy boundary — relevant to $A\neq0$, `V-B3b` §3.3) | record only |
| 4 | Yadav, A. K. (2021). "Reflection of plane waves in a fraction-order generalized magneto-thermoelasticity in a rotating triclinic solid half-space." *Mechanics of Advanced Materials and Structures* **29**: 4273–4290. DOI `10.1080/15376494.2021.1926017`. Crossref 27. | fractional-order magneto-thermoelastic | reflection, oblique, anisotropic + rotation | record only |
| 5 | Lazzari, B.; Nibbi, R. (2016/2017). "Energy decay in Green–Naghdi thermoelasticity with diffusion and dissipative boundary controls." *Journal of Thermal Stresses* **40**: 917–927. DOI `10.1080/01495739.2016.1261262`. Crossref 13. | **GN** + diffusion | **decay/stability**, not reflection — included because it is the closest GN stability source found | record only |
| 6 | Green, A. E.; Naghdi, P. M. (1993). "Thermoelasticity without energy dissipation." *Journal of Elasticity* **31**(3): 189–208. DOI `10.1007/BF00044969`. Crossref **2194**. | **GN-II (source paper)** | the model itself | record only |

Item 6 closes a bibliographic gap carried since Phase B2: the **1993 *J. Elasticity* GN paper is now
Crossref-verified** with volume/pages/DOI and a large citation count. (The 1991 *Proc. R. Soc. A*
"re-examination" paper is **still** unverified — `V-B2z`/`V-B2d` note stands.)

### 3.2 The gap that matters

**No paper was found or verified that reports energy-flux partition coefficients $(R,T,A)$ computed
with each model's own flux.** The literature found is dominated by *amplitude* reflection
coefficients at free surfaces (items 2–4), not by interface energy budgets between two media
(items 1 is the exception in kind, but only at record level here). Consequences:

1. A review sentence of the form "reflection and transmission coefficients have been computed for
   LS/GL/GN" is **supportable** at the level of "such papers exist" (items 1–4).
2. A review sentence of the form "these studies satisfy $R+T+A=1$ in the sense of `V-B3b`" is
   **not supportable** from this survey, because none of them was read and $R,T,A$ in the sense of
   `V-B3b` require (i) an interface between two *different* media and (ii) the model's own flux.
   Most of the located work is single-half-space reflection with a *free* or *impedance* boundary,
   where there is no transmitted branch and hence no $T$ at all.
3. A review sentence of the form "an energy partition with $A\neq0$ has been reported for these
   models" is **not supportable** either. The only mechanism that produced $A>0$ in my own
   computation was a Kapitza conductance or a phase mismatch (`V-B3b` §3.3); item 3's impedance
   boundary condition is the closest thing in this list, and I have not read it.

**The honest summary for the manuscript:** interface energy partition for the generalized
thermoelastic models is a **gap in the literature as surveyed here**, not a settled topic. That is a
publishable observation only if stated as "not located by this survey" — which is exactly how it
should be phrased.

### 3.3 Checklist for when the PDFs arrive

For each paper, five questions, in order (each maps to a condition in `V-B3b` §3.1):

1. **Which flux did they use?** Look for $q_n=\ldots$ at the interface. If LS and they wrote
   $k_{\text{th}}\partial_n\theta$ without the $(1-i\omega\tau_0)^{-1}$, the results are wrong
   (§V-B3a §3.2). If GN-II and they wrote $\partial_n\theta$ where $\alpha$ belongs, likewise.
2. **How many conditions, and does the count match the operator's order?** (C4). Two for
   Biot/LS/GL/GN-II/GN-III; three for MGT.
3. **Is $R+T=1$ reported, and is it presented as a validation?** If yes to the second part, note that
   it follows from the interface conditions and is not a physical check (§V-B3b §3.2).
4. **Is the reported quantity an amplitude ratio or an energy ratio?** $|r|^2$ is **not** $R$ unless
   the two media are identical; the correct energy ratio carries $\operatorname{Re}\hat q$ weights.
   This is the single most likely numerical error in the corpus.
5. **If two media differ in $\tau_0$ (LS/GL) or in $k^*$ (GN), was the phase mismatch handled?**
   Otherwise $A$ is being silently set to zero (§V-B3b §3.3, M2).



## 3.4 (B3f) Search log, and what the standard reflection papers define as "energy ratios"

The negative result of §3.2 ("no flux-based R/T/A study located") is only useful if it is
**falsifiable**. This section records exactly how it was obtained, and lists the specific papers an
auditor should check against it.

### 3.4.1 Search record (falsifiable)

| item | value |
|---|---|
| **Database** | **Crossref only** — REST API, `api.crossref.org/works` (bibliographic query). No Scopus, Web of Science, Google Scholar, IEEE, Elsevier full-text, CNKI or MathSciNet search was run. |
| **Date of searches** | 2026-10-22 |
| **Parameters** | `rows=4` or `5`, `select=DOI,title,author,issued,container-title,volume,page,is-referenced-by-count` |
| **Query 1** | `reflection of plane waves generalized thermoelasticity half-space thermal relaxation` |
| **Query 2** | `reflection transmission energy flux interface Lord-Shulman Green-Lindsay thermoelastic` |
| **Query 3** | `Green Naghdi thermoelasticity reflection transmission interface energy flux ratio` |
| **Query 4** | `Sharma reflection of plane waves generalized thermoelastic half-space` |
| **Query 5** | `Sinha Elsibai reflection thermoelastic waves generalized theory` |
| **Query 6** | `Abd-Alla reflection of plane waves magneto-thermoelastic generalized` |
| **Result** | 6 queries, ~27 records inspected, 8 kept. **Zero papers located that compute an energy-flux partition \((R,T,A)\) between two dissimilar thermoelastic media with the model's own flux.** Query 3 — the one written specifically to find such a paper — returned **none**. |

**What would falsify the negative claim:** a paper (i) between two *dissimilar* media, (ii) reporting
transmitted as well as reflected energy, (iii) stating which flux it used. Item 2 below (Sinha &
Elsibai 1997) is the closest candidate and is exactly the paper that must be read to settle it.
Because the search was Crossref-only and title/abstract-driven, **absence here means "not located by
these six queries in this database on this date"**, nothing stronger.

### 3.4.2 Five (+1) specific papers, what each does, and what they define

**All six are UNVERIFIED as to content: none was opened.** The "what it does" column is derived from
the title and the Crossref record only; the "energy ratio definition" column is **NOT** a finding —
it is the question that must be answered on the page.

| # | Reference | DOI | What it does (from title/record) | What it defines as an "energy ratio" — **UNVERIFIED** |
|---|---|---|---|---|
| 1 | **Sinha, S. B.; Elsibai, K. A. (1996).** "Reflection of thermoelastic waves at a solid half-space with two relaxation times." *J. Thermal Stresses* **19**(8):749–762 | `10.1080/01495739608946205` | reflection at a **free** half-space, GL-type two relaxation times | unknown; the standard pattern would be \(|A_j/A_0|^2\) per reflected branch |
| 2 | **Sinha, S. B.; Elsibai, K. A. (1997).** "Reflection and refraction of thermoelastic waves at an interface of two semi-infinite media with two relaxation times." *J. Thermal Stresses* **20**(2):129–145 | `10.1080/01495739708956095` | **two semi-infinite media**, reflection **and** refraction, two relaxation times — the direct counterpart of `V-B3d` | unknown; this is **the** paper to check for a transmitted-energy definition |
| 3 | **Sharma, J. N.; Kumar, V.; Chand, D. (2003).** "Reflection of generalized thermoelastic waves from the boundary of a half-space." *J. Thermal Stresses* **26**(10):925–942 | `10.1080/01495730306342` | reflection at a half-space boundary, generalized (LS/GL) theory; **most cited in this group (193)** | unknown; likely the convention the field treats as standard |
| 4 | **Singh, B.; Kumar, R. (1998).** "Reflection of plane waves from the flat boundary of a micropolar generalized thermoelastic half-space." *Int. J. Engng. Sci.* **36**(7–8):865–890 | `10.1016/s0020-7225(97)00079-7` | micropolar + generalized thermoelasticity: a **fourth** reflected branch (microrotation) | unknown; tests the counting rule of `V-B3e` §3.2 |
| 5 | **Abd-alla, A. N. (2000).** "Relaxation effects on reflection of generalized magneto-thermoelastic waves." *Mech. Res. Commun.* **27**(5):591–600 | `10.1016/s0093-6413(00)00134-8` | magneto-thermoelastic: adds a magnetic field to the reflection problem | unknown; would require a Maxwell-stress term in the flux |
| 6 | **Sinha, A. N.; Sinha, S. B. (1974).** "Reflection of thermoelastic waves at a solid half-space with thermal relaxation." *J. Physics of the Earth* **22**:237–244 | `10.4294/jpe1952.22.237` | earliest LS-type reflection paper; the historical convention | unknown |

Also relevant and already tabulated in §3.1: Li, Li, Wei & Wang (2018), *Appl. Math. Model.*
**55**:536–550, `10.1016/j.apm.2017.10.040` — the only located paper that treats **reflection and
refraction between two dissimilar solids** with an LS law.

### 3.4.3 Why their definitions matter — a computed warning, not a criticism of unread papers

From `V-B3d` (where the computation *was* done), three different quantities are all called "R" and
they differ by up to \(8.6	imes10^{-4}\) at 1e11 Hz:

1. \(|	ext{amplitude}|^2\) per reflected branch (diagonal only) — what most reflection papers
   tabulate. **This is not an energy flux ratio** when the medium is attenuating, because with
   complex \(k\) the flux of a sum is not the sum of the fluxes.
2. the reflected **sum** flux (intra-side interference kept) — what is actually carried away.
3. the **total-field** flux (incident–reflected interference kept) — the only one for which
   \(1-R-T\) vanishes identically.

In the lossless case (GN-II) all three coincide exactly (`V-B3d` §3.3). So the question to ask of
papers 1–6 is precise and answerable: **do they report (1), (2) or (3), and is the interference term
stated?** A table of "energy ratios" that sums to 1 is consistent with (1) *and* an accidental
cancellation; only a stated definition settles it. **I do not claim any of these papers is wrong** —
I have not read them, and this is exactly what must be checked.

## 4. Evidence / Sources

All six references above are given with authors, year, title, journal, volume, pages, DOI, Crossref
citation count (snapshot 2026-10-22) and access level (**record only** for all six). Query strings
used: `reflection of plane waves generalized thermoelasticity half-space thermal relaxation`;
`reflection transmission energy flux interface Lord-Shulman Green-Lindsay thermoelastic`;
`Green Naghdi thermoelasticity reflection transmission interface energy flux ratio`.

**No full text of any of the six was opened.** Nothing in §3 is attributed to their content.

## 5. Checks done

1. **Bibliographic verification:** all six DOIs resolve through Crossref, with volume/pages/issue
   matching the records. Journal names checked against the records (one trap: item 3's journal,
   *Mechanics and Mechanical Engineering*, is easily confused with *Mechanics of Advanced Materials
   and Structures* — different publisher, different DOI prefix).
2. **Topical relevance check:** each item was classified by *what it does* (free-surface reflection
   vs interface transmission vs decay), not by its title's promise. Item 5 is *not* a
   reflection/transmission paper despite the query that found it.
3. **Gap check:** absence of a verified $R/T/A$ computation is stated as a **negative search
   result**, i.e. it means "not found by these three queries in Crossref", **not** "does not exist".
4. **Consistency with B3a/B3b:** the checklist in §3.3 is derived from the conditions and the flux
   definitions already established there, not imported from these papers.

## 6. Confidence

- **Bibliographic data: HIGH** (Crossref-verified records).
- **Topical classification: MEDIUM** (from titles and abstracts-absence; e.g. item 1 is described as
  "reflection and refraction … based on Lord–Shulman", which is what its title says and no more).
- **Any statement about what these papers conclude: NONE.** Not asserted.
- **The claim that this is a survey of the literature: LOW by construction** — three queries, one
  database, no full texts. It is a starting point.

## 7. NOT verified / open issues

1. **No full text opened** for any of the six; no equation, boundary condition, or numerical value
   from them is reproduced or confirmed.
2. **MGT reflection/transmission:** nothing found. Given `V-B3a` §3.6 (no canonical flux), an MGT
   $R/T$ paper should be read with the specific question "which energy functional?".
3. **GN-II / GN-III reflection–transmission:** nothing found by these queries. The GN literature
   found is about decay/stability (item 5), not interfaces.
4. **Biot (classical) interface $R/T$:** not queried separately — the classical thermoelastic
   interface problem is well covered in older literature (Chadwick, Deresiewicz-type treatments)
   but **I verified none of it**, and the brief's model list makes Biot the reference case that most
   needs a citation. **This is the largest single gap in B3c.**
5. **No Chinese/Japanese/Russian-language literature** was searched.
6. **Citation counts are snapshots** and are not significance claims.
7. **Item 2 is open access** — that is the highest-value, lowest-cost item for the handler to obtain
   and would immediately convert one row of this table from "record only" to "read".
