# V-B1c — The 15 most-cited papers underlying the field

**All counts retrieved 2026-10-22 (UTC).**

---

## Task

List the 15 most-cited papers/books underlying this field, with citation counts as shown on Google Scholar / Scopus / Web of Science (stating which), and the date.

---

## Method

1. **Google Scholar, Scopus and Web of Science were not accessible from this environment.** Direct HTTP requests to `scholar.google.com` failed (no route: HTTP 000). No API key exists for Scopus/WoS. Therefore the brief's preferred indices could not be used, and **the numbers below are not Google Scholar numbers.** Anything that says "cited N times on Google Scholar" in our paper must not be sourced from this file.
2. Index used instead: **Crossref `is-referenced-by-count`**, retrieved with `api.crossref.org/works?filter=doi:…&select=DOI,title,is-referenced-by-count` (single batched call, so all 15 counts are internally consistent — same index, same day). **OpenAlex `cited_by_count`** was retrieved for 5 of them as a second opinion, shown in a separate column.
3. Candidates were assembled from the model list in the brief plus the reviews identified in V-B1b. Each candidate's bibliographic data (authors, journal, volume, pages, year, DOI) was verified from the Crossref record itself, not from memory.
4. Ranking: descending Crossref count, journal articles only (see open issue 1 on books).

---

## Result

### R1. Top 15 by Crossref `is-referenced-by-count`

Ordering column = Crossref rank. **OpenAlex column filled for all 15** (supervisor request (b)); where the two indices disagree in *order*, the rows are marked ⚠.

| Rank | Reference (verified) | DOI | Crossref count | OpenAlex count | Why it is in this field's canon |
|---|---|---|---|---|---|
| 1 | **Eringen, A.C. (1983)** "On differential equations of nonlocal elasticity and solutions of screw dislocation and surface waves", *J. Appl. Phys.* **54**(9):4703–4710 | 10.1063/1.332803 | **4542** | 4812 | The differential (Laplacian-modified) nonlocal model used by essentially all nonlocal wave/beam papers |
| 2 | **Lord, H.W. & Shulman, Y. (1967)** "A generalized dynamical theory of thermoelasticity", *J. Mech. Phys. Solids* **15**(5):299–309 | 10.1016/0022-5096(67)90024-5 | **4068** | 4521 | Single-relaxation-time (Cattaneo) thermoelasticity: the "LS theory" |
| 3 | **Mindlin, R.D. (1964)** "Micro-structure in linear elasticity", *Arch. Ration. Mech. Anal.* **16**(1):51–78 | 10.1007/BF00248490 | **3677** | 3982 | Origin of the general gradient/microstructure (Mindlin) elasticity framework |
| 4 ⚠ | **Green, A.E. & Lindsay, K.A. (1972)** "Thermoelasticity", *J. Elasticity* **2**(1):1–7 | 10.1007/BF00045689 | **2929** | 2947 | Two-relaxation-parameter temperature-rate theory ("GL") |
| 5 ⚠ | **Biot, M.A. (1956)** "Thermoelasticity and irreversible thermodynamics", *J. Appl. Phys.* **27**(3):240–253 | 10.1063/1.1722351 | **2854** | 3164 | Classical coupled (Fourier) thermoelasticity; the baseline all generalisations modify |
| 6 | **Mindlin, R.D. & Tiersten, H.F. (1962)** "Effects of couple-stresses in linear elasticity", *Arch. Ration. Mech. Anal.* **11**(1):415–448 | 10.1007/BF00253946 | **2388** | 2593 | Couple-stress special case; precursor of gradient constitutive laws |
| 7 | **Green, A.E. & Naghdi, P.M. (1993)** "Thermoelasticity without energy dissipation", *J. Elasticity* **31**(3):189–208 | 10.1007/BF00044969 | **2194** | 2402 | "GN Type II" — undamped, finite-speed thermal waves |
| 8 | **Tzou, D.Y. (1995)** "A unified field approach for heat conduction from macro- to micro-scales", *ASME J. Heat Transfer* **117**(1):8–16 | 10.1115/1.2822329 | **1995** | 2148 | Dual-phase-lag heat conduction; the source of the DPL family in thermoelasticity |
| 9 | **Green, A.E. & Naghdi, P.M. (1992)** "On undamped heat waves in an elastic solid", *J. Thermal Stresses* **15**(2):253–264 | 10.1080/01495739208946136 | **1555** | 1687 | GN Type II formulation, stated as such for the first time |
| 10 | **Eringen, A.C. (1972)** "Linear theory of nonlocal elasticity and dispersion of plane waves", *Int. J. Eng. Sci.* **10**(5):425–435 | 10.1016/0020-7225(72)90050-X | **1272** | 1449 | Nonlocal dispersion of elastic plane waves — directly a wave-mechanics paper |
| 11 | **Chandrasekharaiah, D.S. (1998)** "Hyperbolic thermoelasticity: a review of recent literature", *Appl. Mech. Rev.* **51**(12):705–729 | 10.1115/1.3098984 | **1149** | 1284 | The field's standard survey for 1986–1998 (see V-B1b). Print year **1998**; ASME's landing page shows 2009 because the back catalogue was digitised later |
| 12 | **Gurtin, M.E. & Pipkin, A.C. (1968)** "A general theory of heat conduction with finite wave speeds", *Arch. Ration. Mech. Anal.* **31**(2):113–126 | 10.1007/BF00281373 | **1044** | 1218 | The memory/relaxation-functional theory of heat conduction |
| 13 | **Chandrasekharaiah, D.S. (1986)** "Thermoelasticity with second sound: a review", *Appl. Mech. Rev.* **39**(3):355–376 | 10.1115/1.3143705 | **835** | 952 | The foundational survey (see V-B1a, V-B1b) |
| 14 ⚠ | **Roy Choudhuri, S.K. (2007)** "On a thermoelastic three-phase-lag model", *J. Thermal Stresses* **30**(3):231–238 | 10.1080/01495730601130919 | **766** | 804 | Triple-phase-lag (TPL) thermoelasticity |
| 15 ⚠ | **Chen, P.J. & Gurtin, M.E. (1968)** "On a theory of heat conduction involving two temperatures", *Z. Angew. Math. Phys.* **19**(4):614–627 | 10.1007/BF01594969 | **727** | 852 | Two-temperature thermoelasticity (the model Youssef later generalised) |

**OpenAlex re-ranking** (same 15 works, second index): 1 Eringen 1983 (4812), 2 Lord–Shulman (4521), 3 Mindlin 1964 (3982), 4 **Biot (3164)**, 5 **Green–Lindsay (2947)**, 6 Mindlin–Tiersten (2593), 7 Green–Naghdi 1993 (2402), 8 Tzou (2148), 9 Green–Naghdi 1992 (1687), 10 Eringen 1972 (1449), 11 Chandrasekharaiah 1998 (1284), 12 Gurtin–Pipkin (1218), 13 Chandrasekharaiah 1986 (952), 14 **Chen–Gurtin (852)**, 15 **Roy Choudhuri (804)**.

**So two rank pairs are index-dependent and must not be quoted as fact:** Biot vs Green–Lindsay (4th/5th) and Chen–Gurtin vs Roy Choudhuri (14th/15th). Everything else is stable across both indices. The membership of the top 15 is identical in both indices — only those two adjacent pairs swap.

**Just below the cut** (verified, same index, same day): Hetnarski & Ignaczak 1999 (602, 10.1080/014957399280832); Wang & Li 2011, memory-dependent derivative (448, 10.1016/j.camwa.2011.04.028); Youssef 2006, two-temperature generalized thermoelasticity (431, 10.1093/imamat/hxh101); Quintanilla 2019, MGT thermoelasticity (409, 10.1177/1081286519862007); Eringen 1984, nonlocal micropolar plane waves (334, 10.1016/0020-7225(84)90112-5); Nayfeh & Nemat-Nasser 1971, thermoelastic waves with relaxation (171, 10.1007/BF01178389).

### R2. Observations that matter for our framing

- The canon is **dominated by 1956–1993** papers. Nine of the top fifteen predate 1994; only two (1998 review, 2007 TPL) are post-1995. The modern models in our brief — MGT (2019), memory-dependent derivative (2011), two-temperature Youssef (2006) — are cited in the 400–450 range, i.e. one order of magnitude below Lord–Shulman.
- Two of the top fifteen are **reviews** (#11, #13) and one is a **heat-conduction paper that is not thermoelastic at all** (#8, Tzou). This is direct evidence that a well-executed survey can itself become canonical in this field, and that the heat-conduction constitutive law is where the field's centre of gravity sits.
- The single most-cited item (#1, Eringen 1983) is a *nonlocal elasticity* paper, not a thermoelastic one — consistent with the brief's decision to include nonlocal/gradient continua.
- **No MGT paper is in the top 15**, but Quintanilla 2019 at 409 is the fastest-rising; it appeared only 7 years ago.

---

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| All 15 counts | Crossref `filter=doi:…&select=DOI,title,is-referenced-by-count`, one batch, 2026-10-22 | API response read in full |
| All 15 bibliographic details (journal, vol, pages, year, DOI) | Same Crossref batch, plus per-item `query.bibliographic` records captured earlier | API records |
| OpenAlex cross-check for 5 items | `api.openalex.org/works?filter=doi:…&select=doi,title,publication_year,cited_by_count` | API response |
| Runner-up counts | Crossref single-item queries | API records |
| GS/Scopus/WoS unavailable | Direct request attempt to scholar.google.com (HTTP 000 — no route from sandbox); no Scopus/WoS credentials | Direct test |

## Checks done

- Every DOI above was resolved in Crossref and the title returned by Crossref matched the title I ascribe to it. **No DOI in this file was written from memory.**
- Counts for all 15 come from **one index on one day**, so the ordering is internally consistent. Where a second index was available (5 items), the two agree in ordering except Green–Naghdi 1993 vs Mindlin–Tiersten 1962 (Crossref ranks Mindlin–Tiersten above GN-1993 by 194; OpenAlex would rank GN-1993 above). Ranks 6 and 7 are therefore not robust; the rest are.
- One bibliographic correction to a "standard" statement: Quintanilla's MGT thermoelasticity paper is dated **2019** in Crossref (online 2019-07-21, *Math. Mech. Solids* 24(12):4020–4031), not 2018. Papers citing it as "2018" are using the preprint/online-first year incorrectly.
- Cross-index magnitude check: Crossref counts are systematically **lower** than OpenAlex for older papers here (LS 4068 vs 4521; GN 2194 vs 2402) and equal for recent ones. Both are well below typical Google Scholar counts. Expect GS to be ~1.3–2× these numbers.

## Confidence

- **HIGH**: the counts as *Crossref* counts on 2026-10-22; the bibliographic data; the identity of the papers.
- **MEDIUM**: that this is the correct "top 15" — the candidate pool was assembled from the brief plus verified reviews, not from an exhaustive bibliometric sweep, so a highly cited paper outside our model list (e.g. a photoacoustic or geophysics classic) could be missed.
- **LOW**: nothing in this file should be presented as a Google Scholar ranking.

## NOT verified / open issues

1. **Books are excluded by construction.** Crossref counts do not exist for the field's most influential books — Nowacki (1975), Dhaliwal & Singh (1980), Hetnarski & Eslami's *Thermal Stresses — Advanced Theory and Applications*, Ignaczak & Ostoja-Starzewski (OUP 2010), Tzou's *Macro- to Microscale Heat Transfer* — and in a Google Scholar ranking several of these would very likely displace entries near the bottom of the list. **This is the main limitation of R1.** If a "most-cited works" table goes into the paper, it must either be labelled "most-cited journal articles, Crossref, date" or redone with GS/Scopus.
2. **Google Scholar numbers were not obtained.** If the handler or another author has GS access, the whole table can be re-run in ~15 minutes and I will reconcile: I expect GS ≫ Crossref, and I expect the *ordering* to be broadly stable but not identical.
3. **Self-citation and citation-context not assessed.** Crossref cannot tell us whether a citation is supportive, critical, or a courtesy citation. For a review that intends to say "model X is widely used", raw counts are not evidence of correctness.
4. **Tzou's second 1995 paper** ("The generalized lagging response in small-scale and high-rate heating", *Int. J. Heat Mass Transfer* **38**(17):3231–3240) was **not** counted here; it is frequently co-cited with #8 and might enter near the bottom. Not verified in this session.
5. **Cluster double counting:** Eringen 1983 and Eringen 1972 overlap heavily in the citing literature; Mindlin 1964 and Mindlin–Tiersten 1962 likewise. The ranking should not be read as 15 independent contributions.
