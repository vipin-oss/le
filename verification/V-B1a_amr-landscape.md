# V-B1a — Applied Mechanics Reviews: recent landscape and journal policy

**Access date for all sources in this file: 2026-10-22 (UTC).**

---

## Task

Find ≥12 recent (2018–2026) review articles in *Applied Mechanics Reviews* (AMR) on thermoelasticity, wave propagation, heat conduction, nonlocal/gradient continua, multiphysics or smart materials; record title, author count, year, page count, section count, reference count, figure/table count, one-line scope; give min/median/max for pages, references, figures, authors; and state whether AMR publishes a limit on number of authors or on length (quote the policy, with URL and date).

---

## Method

1. Pulled the complete Crossref record of AMR (ISSN 0003-6900) for `from-pub-date:2018-01-01, type:journal-article`: **128 items** returned (includes reviews, research articles, discussions, closures, errata, editorials — not only reviews).
   `https://api.crossref.org/journals/0003-6900/works?filter=from-pub-date:2018-01-01,type:journal-article&rows=200&select=DOI,title,page,published,volume&sort=published&order=desc`
2. Read all 128 titles and selected 13 whose subject matter is thermoelasticity / heat conduction / wave propagation / nonlocal-gradient / multiphysics / smart materials. (Criteria and exclusions listed under "NOT verified".)
3. For those 13: authors from Crossref / Semantic Scholar; `referenced_works_count` and `cited_by_count` from OpenAlex (`api.openalex.org/works?filter=doi:…`); citation counts cross-checked against Semantic Scholar Graph API.
4. Page counts: **not deposited to Crossref by ASME** (AMR uses 6-digit article numbers, e.g. `040801`, not continuous pagination since ~2018). Page counts are printed only on the publisher's article page as "<vol>(<iss>): <artno> (N pages)". I opened the publisher record for each candidate where possible and transcribed that line.
5. Journal policy: read AMR "About" page, ASME "Journal Submission Types", ASME "Writing a Research Paper", ASME *Guide for Journal Authors* (PDF), ASME "References" guideline page, and AMR's own author-information page (journaltool.asme.org).

---

## Result

### R1. The 13 selected 2018–2026 AMR records

`Pages` = verified from the publisher's own article page. `Refs` = OpenAlex `referenced_works_count`. `Cites` = OpenAlex `cited_by_count` / Semantic Scholar `citationCount`, both on 2026-10-22.

| # | DOI | Short title | Authors (n) | Year | Locator | Pages | Refs | Cites (OA/S2) | One-line scope |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.1115/1.4039557 | Water-vapour-pressure model, moisture-permeable materials under rapid heating | Chen L., Zhou J., Chu H.-w., Zhang G.-Q., Fan X.-J. (5) | 2018 | 70(2) | n/v | 84 | 14 / 11 | Vapour-pressure constitutive models for porous materials heated fast (fire/spallation context) |
| 2 | 10.1115/1.4040402 | Fractional-derivative modelling of power-law attenuation in acoustic waves | Cai W., Chen W., Fang J., Holm S. (4) | 2018 | 70(3):030802 | **12** | 111 | 81 / 85 | Fractional wave equations reproducing frequency-power-law attenuation/scattering |
| 3 | 10.1115/1.4044055 | Models of ultraslow diffusion in heterogeneous materials | Liang Y., Wang S., Chen W., Zhou Z., Magin R.L. (5) | 2019 | 71(4):040802 | **16** | 125 | 76 / 75 | Anomalous (sub-diffusive) transport models: fractional, distributed-order, structural |
| 4 | 10.1115/1.4042821 | Adjoint methods as design tools in thermoacoustics | Magri L. (1) | 2019 | 71(2) | n/v | 319 | 70 / 56 | Adjoint/sensitivity formulation for thermoacoustic stability and design |
| 5 | 10.1115/1.4046222 | Tunable and active phononic crystals and metamaterials | Wang Y.-F., Wang Y.-Z., Wu B., Chen W., Wang Y.-S. (5) | 2020 | 72(4):040801 | **35** | 538 (Crossref 544) | 502 / 470 | Band-gap engineering and tunable wave control incl. multifield coupling |
| 6 | 10.1115/1.4047707 | Damping models for structures with mechanical joints | Mathis A.T., Balaji N.N., Kuether R.J., Brink A.R., Brake M.R.W., Quinn D.D. (6) | 2020 | 72(4):040802 | n/v | 190 | 127 / 105 | Constitutive/numerical models of frictional joint damping |
| 7 | 10.1115/1.4054629 | Acoustic/elastic phase-gradient metasurfaces | Chen A.-L., Wang Y.-S., Wang Y.-F., Zhou H.-T., Yuan S.-M. (5) | 2022 | 74(2):020801 | **36** | 390 | 174 / 162 | Generalized-Snell-law metasurface design: elements, tunability, coding |
| 8 | 10.1115/1.4056131 | Thermomechanical constitutive models of shape-memory polymers | Zhao W., Liu L.-W., Lan X., Leng J., Liu Y.-J. (5) | 2022 | 75(2) | n/v | 134 | 77 / 73 | Phase-transition thermomechanics of SMPs and composites |
| 9 | 10.1115/1.4056726 | THCM continuum modelling of subsurface rocks | Siddiqui M.A.Q., Regenauer-Lieb K., Roshan H. (3) | 2023 (online) / 2024 (issue) | 76(3):031001 | **17** | 227 | 17 / 18 | Thermodynamics-based thermo-hydro-chemo-mechanical constitutive models |
| 10 | 10.1115/1.4064763 | Acoustic emission in ceramic-matrix composites | Tulshibagwale N., Brodnik N., Muir C., Hilmas A., Kiser J., Smith C., Almansour A.S., Presby M., Daly S. (9) | 2024 | 76(4) | n/v | 173 | 15 / 14 | AE signatures, damage mechanisms, monitoring methods for CMCs |
| 11 | 10.1115/1.4066020 | Fracture mechanics of magnetoelectroelastic materials | Feng W.-J., Yan Z., Ma P., Lv C.-F., Zhang C.-Z. (5) | 2024 (online) / 2025 (issue) | 77(4) | n/v | 261 | 12 / 11 | Crack problems in piezo/magnetostrictive multiphysics continua |
| 12 | 10.1115/1.4070541 | Acoustic metamaterials in wave manipulation | Wang G.-F., Chen Z.-Y., Yan J.-A., Lim C.W. (4) | 2025 | accepted-manuscript no. | ~108 (Crossref `page` = "1-108") | 0 (metadata gap) | 6 / 7 | "Peculiar" metamaterial functions and applications |
| 13 | 10.1115/1.4068387 | Fractal and Hurst effects in stochastic mechanics | Ostoja-Starzewski M., Jetti Y.S., Malyarenko A., Porcu E. (4) | 2025 (online) / 2026 (issue) | 78(5):050801 | **26** | 71 | 0 / 0 | Random fields with fractal/Hurst correlations in continuum mechanics |

`n/v` = page count not verified (article page not opened; see NOT verified).

### R2. Descriptive statistics

**Pages** (n = 6 verified of 13): 12, 16, 17, 26, 35, 36 → **min 12, median 21.5, max 36**.
Older same-topic AMR precedent (outside the 2018–2026 window, verified from Crossref/AMR records): Chandrasekharaiah 1986, 39(3):355–376 = **22 pp**; Chandrasekharaiah 1998, 51(12):705–729 = **25 pp**. Including these: min 12, median ≈ 21.5, max 36 over n = 8.

**References** (n = 12; item 12 has an OpenAlex metadata gap of 0 and is excluded): 71, 84, 111, 125, 134, 173, 190, 227, 261, 319, 390, 538 → **min 71, median 181.5, max 538**.

**Authors** (n = 13): 1, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 9 → **min 1, median 5, max 9**.

**Citation counts** (OpenAlex, n = 13): min 0, median 76, max 502.

**Figures and tables:** not obtainable — full text is paywalled for all 13 and no machine-readable figure/table count is published. **UNVERIFIED** for all 13 (see NOT verified).

**Sections:** not obtainable for the same reason. **UNVERIFIED** for all 13. Partial substitute: the publisher exposes per-article section anchors for open articles only; for one open article (10.1115/1.4062219, fish-swimming review, not part of the 13) the anchor list was Abstract / 1 Introduction / 2 Methods / 3 Topics of Analysis / 4 Summary and Conclusions / Funding / Data Availability / References — i.e. a flat 4-heading structure, but this is one anecdote and not evidence about the 13.

### R3. Subject-coverage finding (important for positioning)

**AMR has published no review article on generalized thermoelasticity, second sound, or heat-conduction waves in the 2018–2026 window.** Scanning all 128 Crossref items 2018-01-01 → 2026-10-22, the closest matches are the 13 above; none is a thermoelasticity review. Two AMR reviews cover this exact subject but are old: Chandrasekharaiah 1986 (39(3):355–376, DOI 10.1115/1.3143705, 835 Crossref citations) and Chandrasekharaiah 1998 (51(12):705–729, DOI 10.1115/1.3098984, 1149 Crossref citations). A published Comment on those two reviews and the author's Response appeared in AMR 56 (2003), p. 453 (DOI 10.1115/1.1539097).

Consequence: a new AMR review on wave mechanics in generalized continua would not be duplicating any recent AMR content, but would be measured against Chandrasekharaiah's two AMR reviews — which are the field's most-cited surveys.

**Dating caveat (added after supervisor audit):** the ASME landing page for DOI 10.1115/1.3098984 shows a **2009** date because ASME digitised the back catalogue later. The **print publication year is 1998** (*Appl. Mech. Rev.* **51**(12):705–729, December 1998, confirmed from the Crossref `issued` field and from the volume/issue/pagination). When citing, give 1998 as the publication year; if a date discrepancy is queried, the explanation is digitisation, not a second edition. The same caveat applies to any pre-2000 AMR DOI whose publisher page shows a recent "published online" date.

### R4. Stated policy on length and number of authors

**Length — Review Article: explicitly open.**

This quote was challenged by the supervisor and is now re-verified with full provenance. **Exact source:** ASME, *Journal Submission Types*, URL
`https://www.asme.org/publications-submissions/journals/information-for-authors/journal-guidelines/journal-submission-types`
**Exact sentence, under the heading "### Review Article"** (third block on the page, after "Research Paper" and "Technical Brief"):

> "Review articles undergo full peer review. A Review Article organizes, clarifies, and summarizes existing major works in science and engineering and provides comprehensive citations to a full spectrum of relevant literature. **Length: open.**"

Read in full twice: 2026-10-22 (initial) and 2026-10-22 (re-check after the challenge), both fetches showing the identical sentence.

**Two qualifications that must travel with this quote — do not let it harden into "AMR guarantees unlimited length":**

1. **It is an ASME-wide journal policy page, not an AMR-specific page.** It governs all ASME journals and is reached from AMR's own "Information for Authors" link. The AMR-specific author page (`https://journaltool.asme.org/home/AMRAuthorInfo.cfm`) says only "There are no page charges in AMR" and *does not state a review length* — the supervisor is correct on that point, and my original file did not claim otherwise, but it did not make the distinction explicit. It is now explicit.
2. **"Length: open" is a policy statement about there being no fixed cap, not a promise of acceptance at any length.** The same page gives word counts for other types, and the Editor can always require cutting. Practical implication for R4: use the observed AMR norms in R2/R5 of this file (median ~21.5 pp verified, max 36 pp in the 2018–2026 sample) as the de facto target, and treat "open" as permission, not budget.

Secondary corroboration, weaker: ASME's *Guide for Journal Authors* PDF also lists Review Article as "Length: Open" — `https://www.asme.org/getmedia/25d77d56-5186-4767-bb93-94211457ee93/asme_guide_for_journal_authors_final.pdf`, read 2026-10-22. That PDF was read via search-indexed text, **not** page-by-page; its table layout garbles the adjacent entries, so treat it as supporting evidence only. The primary quotation above stands on its own.

The 12,000-word cap found on ASME's site applies to **research papers**, not reviews: "A research paper should not exceed 12,000 words. – 1 journal page = 1000 words" (https://www.asme.org/publications-submissions/journals/information-for-authors/journal-guidelines/writing-a-research-paper, read 2026-10-22). Do not apply this to a review.

**Page charges:** none for AMR — "Page Charges and Length: There are no page charges in AMR." (AMR Author Info, https://journaltool.asme.org/home/AMRAuthorInfo.cfm, read 2026-10-22). *Caveat:* that page lists Harry Dankowicz as Editor-in-Chief; ASME's own 2023 special-issue text says Dankowicz's term ended September 2022, and the AMR "About" page gives a 2025 impact factor of 19.1. The journaltool page therefore appears stale on the editor's name — treat "no page charges" as likely but re-confirm with the current editorial office.

**Number of authors: no maximum stated anywhere I could find.** What exists is (a) an inclusion rule, and (b) a bibliographic rule that presupposes very long author lists:
> "ASME's policy is all contributors who have participated significantly in the technical aspects of a paper be recognized as co-authors or cited in the acknowledgments." (*Guide for Journal Authors*, PDF above)
> "If there are 11 or more authors, list the first seven in the bibliography, followed by 'et al.'" (ASME *References* guideline, https://www.asme.org/publications-submissions/journals/information-for-authors/journal-guidelines/references, read 2026-10-22)

So a 10+ author AMR review is not excluded by any published rule; the largest author count I observed in the 2018–2026 sample is 9.

**Submission route (practically important):** AMR *recommends* (does not require) that authors first send the Editor a proposal — title, abstract, timeline — using the journal's `prospectus.doc` form: "Authors are recommended to first contact the Editor with a proposal for a contribution. Such a proposal should include a title and abstract for the anticipated contribution as well as a likely timeline to completion. There is no penalty for submitting an unsolicited manuscript without first contacting the Editor…" (AMR Author Info, URL above). For a 10+ author, multi-model review this is the sensible first step and reduces the risk of a desk rejection.

**Journal scope/identity** (AMR About page, https://asmedigitalcollection.asme.org/appliedmechanicsreviews/pages/about, read 2026-10-22): review journal; scope includes "State-of-the-art surveys; Retrospective reviews; … Tutorials"; bimonthly; ISSN 0003-6900 / eISSN 2379-0407; Impact Factor 19.1, 2025 Journal Citation Reports (Clarivate, 2026). Scope explicitly includes "heat transfer", so a thermoelasticity review is in scope.

---

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| 128 AMR journal-articles since 2018-01-01 | Crossref REST API, journal 0003-6900 | Full API response read |
| Metadata of the 13 items (authors, vol/issue, dates, refs, cites) | Crossref + OpenAlex + Semantic Scholar Graph API | Full API records |
| Page counts 12/35/26/16/36/17 | Publisher article pages (asmedigitalcollection.asme.org), "May 2018, 70(3): 030802 (12 pages)" etc. | Publisher record read for each |
| Chandrasekharaiah 1986 = 22 pp; 1998 = 705–729 | AMR article page (snippet) + Crossref (10.1115/1.3098984, page 705-729) | Publisher page / Crossref |
| "Review Article … Length: open" | asme.org Journal Submission Types | Page read in full |
| No page charges | journaltool.asme.org AMRAuthorInfo.cfm | Page read in full |
| 11+ author citation rule | asme.org References guideline | Page read in full |
| IF 19.1 (2025 JCR) | AMR About page | Page read in full |

## Checks done

- Citation counts triangulated across **two independent indices** (OpenAlex, Semantic Scholar) for all 13: agree within ~0–20%; largest gap 127 vs 105 (item 6) and 502 vs 470 (item 5). Discrepancy flagged rather than averaged.
- Reference count cross-checked for one item against Crossref's deposited reference list: OpenAlex 538 vs Crossref 544 for 10.1115/1.4046222 (~1% difference). So OpenAlex reference counts are a slight **under**count; treat ±1–2%.
- Page counts are quoted verbatim from the publisher's own line, not inferred from article numbers.
- Negative claim ("no AMR thermoelasticity review 2018–2026") tested against the *full* 128-item list, not a keyword search.
- Policy claim ("no author maximum") is a *negative* result: I searched the four ASME policy pages above; absence of a rule on those pages is evidence but not proof.

## Confidence

- **HIGH**: 13 items exist with the stated DOIs, authors, years, volumes/issues; no recent AMR thermoelasticity review in 2018–2026; "Review Article — Length: open"; no page charges; no published author cap.
- **MEDIUM**: min/median/max for pages (n = 6 of 13, plus 2 same-topic precedents → n = 8); reference statistics (OpenAlex, ±1–2%).
- **LOW / none**: figures, tables, section counts (0 of 13 verified).

## NOT verified / open issues

1. **Figures and tables — UNVERIFIED for all 13.** Every one of the 13 is "Available to Purchase"; PDFs redirect to the abstract page and no figure/table count is published in any index. If the handler has AMR/ASME access, these are the 13 PDFs to open; I can then add the columns in ~20 minutes. Do not let anyone state figure counts for this table from memory.
2. **Section counts — UNVERIFIED for all 13**, same cause.
3. **Page counts missing for 7 of 13** (items 1, 4, 6, 8, 10, 11, plus item 12 uncertain). Page counts are not in Crossref/OpenAlex for AMR post-2018 because AMR uses article numbers. Recipe to fill: open `https://doi.org/<DOI>` and read the line "Appl. Mech. Rev. <Mon> <Year>, <vol>(<iss>): <artno> (N pages)".
4. **Item 12** (10.1115/1.4070541): Crossref `page` = "1-108" looks like accepted-manuscript pagination, not the published page count; OpenAlex reports 0 references (metadata gap). Do not cite "108 pages" as fact.
5. **Item 9 is labelled "Research-Article"** on the publisher page, not "Review Articles", although it is a review-style survey in a review journal. If the handler wants only formally-labelled reviews, the count of qualifying records is 12, not 13 — still ≥12.
6. **My selection of "relevant" is a judgement.** A reviewer might disagree with including joint damping (item 6) or acoustic emission (item 10), or with excluding, e.g., AMR items on contact mechanics or tribology. The 13 are documented so any such decision can be re-made.
7. **Crossref completeness of AMR 2018–2026 is assumed.** 128 items / ~8.8 years ≈ 14.5 per year ≈ 2.4 per bimonthly issue; plausible but not independently checked against the printed table of contents of all 53 issues.
8. Not checked: whether AMR has an *unpublished* editorial preference for shorter reviews or for ≤N authors. The Editor's proposal step (R4) is the place to ask.
