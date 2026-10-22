# V-B1b — Competing reviews (last 15 years, plus the two older AMR benchmarks)

**Access date for all sources: 2026-10-22 (UTC).** Every entry states how much I actually read.

---

## Task

List existing reviews (any journal, last ~15 years) on generalized thermoelasticity, nonlocal elasticity, fractional/memory heat conduction, MGT, and wave reflection/transmission at interfaces. For each: what it covers, what it omits, whether it derives or only collects results, and what a "constructive" review (derive, compare, unified framework, when each theory fails, open problems) could add. Be honest if the field is already well covered.

---

## Method

1. Crossref `query.bibliographic` / `query.title` lookups and OpenAlex `type:review` + `title.search` filters, per sub-area. Crossref returns the bibliographic record; OpenAlex classifies type and gives citation counts.
2. Negative checks are stated as such: for MGT I enumerated all **352** works with "Moore-Gibson-Thompson" in the title in OpenAlex (`filter=title.search:Moore-Gibson-Thompson`, first 25 by citations inspected, `select=type`) and **none** is typed `review`. For reflection/transmission and for fractional/memory heat conduction I searched Crossref titles and found no dedicated review.
3. Read level is recorded per item. I did **not** have full text of any competing review: all are paywalled. So "what it omits" is inferred from published abstracts, tables of contents where visible, and the citing statements of the papers — **not** from reading the body. This is the weakest part of this file and is flagged again under Confidence.

---

## Result

### R1. Reviews directly on generalized thermoelasticity / second sound

| # | Reference | Covers | Derives or collects? | Gaps visible from the abstract/record | Read level |
|---|---|---|---|---|---|
| 1 | **Chandrasekharaiah, D.S. (1986)** "Thermoelasticity with second sound: A review", *Appl. Mech. Rev.* **39**(3):355–376. DOI 10.1115/1.3143705. 835 Crossref cites. | Finite-speed ("second sound") theories existing up to 1986; formulations on different grounds; solutions of initial-boundary value problems. | **Derives** — "concise derivations of the governing equations presented" (author's abstract). | Stops at 1986: no Green–Naghdi II/III (1992/93), no DPL (1995), no TPL (2007), no MGT (2019), no memory-dependent derivative (2011), no fractional heat conduction, no nonlocal coupling, no interface energy partition. | Publisher abstract (full) + Crossref record. Body not read. |
| 2 | **Chandrasekharaiah, D.S. (1998)** "Hyperbolic thermoelasticity: a review of recent literature", *Appl. Mech. Rev.* **51**(12):705–729. DOI 10.1115/1.3098984. 1149 Crossref cites. | Papers 1986–1998; thermal-relaxation theory and temperature-rate-dependent (Green–Lindsay) theory. | Derives/summarises (continuation of #1). | Stops at 1998. Pre-dates every model family in our brief except LS and GL. A Comment on #1/#2 and the author's Response were published (AMR **56** (2003) 453, DOI 10.1115/1.1539097) — evidence the reviews themselves were contested. | Publisher abstract (partial) + Crossref record. Body not read. |
| 3 | **Hetnarski, R.B. & Ignaczak, J. (1999)** "Generalized thermoelasticity", *J. Thermal Stresses* **22**(4–5):451–476. DOI 10.1080/014957399280832. 602 Crossref cites. | The five then-current models: L–S (1967), G–L (1972), H–I (1996), G–N (1993), C–T (Chandrasekharaiah–Tzou, 1998); domain-of-influence theorems, uniqueness, 1-D closed-form solutions. | Both: compares formulations and reports theorems. | 1999 cut-off. Narrows to *transient thermoelastic waves* only. Explicitly notes that none of the five models had been validated by a combined thermoelastic experiment at that time — a statement now ~27 years old and worth re-testing. No TPL, MGT, MDD, fractional, nonlocal, two-temperature, interface partition. | Full abstract (read from publisher page). Body not read. |
| 4 | **Shakeriaski, F., Ghodrat, M., Escobedo-Diaz, J. & Behnia, M. (2021)** "Recent advances in generalized thermoelasticity theory and the modified models: a review", *J. Comput. Des. Eng.* **8**(1):15–35. DOI 10.1093/jcde/qwaa082. 58 S2 cites. Open access (CC BY-NC). | Five second-sound theories: MPL (multi-phase-lag), LS, GL, DPL; effect of higher-order time derivatives; solution techniques. | Mostly **collects**: organises literature; does not appear to re-derive or cross-check. | No MGT (predates it), no memory-dependent derivative, no nonlocal/gradient coupling, no energy-flux partition, no admissibility/stability synthesis; "limitations" discussed per-theory rather than as a single testable criterion. | Abstract + conclusion (both read in full). Body not read. |
| 5 | **Anonymous / unrefereed preprint (2026)** "Thermodynamic Admissibility, Finite-Speed Heat Transport, and Wave Stability in Generalized Thermoelasticity: A Critical Review with Analytical Proofs", Research Square preprint, DOI 10.21203/rs.3.rs-10734164/v1, posted 2026-08-28. | Claims: unified continuum-thermodynamic framework; Fourier–Biot, Cattaneo–Maxwell/LS, GL, GN, DPL, Guyer–Kurmhansl, MGT; nondimensional benchmark graphs; model-selection map. | Claims to derive/prove. | **Not peer reviewed.** Its claimed scope overlaps our mission almost exactly, including "model-selection map" and admissibility proofs. | Abstract only. |

### R2. Nonlocal / gradient elasticity

| # | Reference | Covers | Derives or collects? | Gaps | Read level |
|---|---|---|---|---|---|
| 6 | **Eltaher, M.A., Khater, M.E. & Emam, S.A. (2016)** "A review on nonlocal elastic models for bending, buckling, vibrations, and wave propagation of nanoscale beams", *Appl. Math. Model.* **40**(5–6):4109–4128. DOI 10.1016/j.apm.2015.11.026. | Eringen nonlocal beam models: bending, buckling, vibration, wave propagation; FG nanobeams. | Collects + one worked derivation (Hamilton's principle for a FG beam). | Beam theories only; no 3-D nonlocal wave propagation, no nonlocal–thermoelastic coupling, no comparison with gradient (Mindlin) alternatives, no critical assessment of the well-known paradoxes (e.g. nonlocal cantilever stiffening). | Publisher abstract (read in full). Body not read. |
| 7 | **Askes, H. & Aifantis, E.C. (2011)** "Gradient elasticity in statics and dynamics: An overview of formulations, length scale identification procedures, finite element implementations and new results", *Int. J. Solids Struct.* **48**(15):1962–1990. DOI 10.1016/j.ijsolstr.2011.03.006. 855 Crossref cites. | Gradient (Mindlin-type) elasticity: formulations, length-scale identification, FE implementation. | Overview with derivations. | Statics/dynamics of gradient elasticity only; not thermoelastic, not nonlocal-integral, no waves-in-generalized-continua synthesis. | Bibliographic record + title/scope. Abstract not read in full. |
| 8 | **"A review on stress-driven nonlocal elasticity theory"** (2021), *J. Comput. Appl. Mech.* (DOI 10.22059/jcamech.2021.331410.653), 35 cites; and **"A review of size-dependent elasticity for nanostructures"** (2018), same journal (DOI 10.22059/jcamech.2018.259334.289), 38 cites. | Stress-driven (integral) nonlocal formulations. | Likely collects. | Narrow; low citation counts; not authoritative for a flagship review's citation base. | Metadata only — **not read**. Listed for completeness. |

### R3. Fractional / memory-dependent heat conduction

| # | Reference | Status | Gap |
|---|---|---|---|
| 9 | No dedicated review article found. Crossref title search (`review fractional heat conduction memory dependent`) returned only book chapters and specialised papers (e.g. *Encyclopedia of Continuum Mechanics* entry "Fractional Heat Conduction", 2020, 0 cites; *Fractional Calculus with Applications in Mechanics*, ch. 7, 2014). | **Negative result** | Fractional and memory-dependent heat conduction is covered only inside monographs (Povstenko; Atanacković et al.) — **those monograph records were not verified in this session**. No review compares Caputo vs Caputo–Fabrizio vs Atangana–Baleanu kernels vs Wang–Li memory-dependent derivative *inside a thermoelastic coupling*, which is exactly where the literature is inconsistent. |
| 10 | Wang, J.-L. & Li, H.-F. (2011) "Surpassing the fractional derivative: Concept of the memory-dependent derivative", *Comput. Math. Appl.* **62**:1562–1567. DOI 10.1016/j.camwa.2011.04.028. 448 Crossref cites. | **Primary source, not a review** — listed because it is the seed of the MDD literature. | — |

### R4. Moore–Gibson–Thompson (MGT) thermoelasticity

| # | Reference | Status | Gap |
|---|---|---|---|
| 11 | Quintanilla, R. (2019) "Moore–Gibson–Thompson thermoelasticity", *Math. Mech. Solids* **24**(12):4020–4031. DOI 10.1177/1081286519862007. 409 cites. | **Primary source.** | — |
| 12 | **No review exists.** Of 352 OpenAlex works with "Moore–Gibson-Thompson" in the title (retrieved 2026-10-22), none is typed `review`; the top-cited 25 are all research articles (thermoelasticity, two-temperature MGT, dipolar bodies, plates, decay rates, memory, well-posedness). | **Negative result, strong** | MGT is the single most obvious gap: a large, active, mathematically sophisticated literature (352 titled works, several 100+ citation papers) with **no survey at all**. Note also that the MGT *equation* has a separate lineage in acoustics (Jordan; Kaltenbacher–Lasiecka–Polymilis) that thermoelasticity papers routinely do not cite — a constructive review should reconcile both lineages. |

### R5. Reflection/transmission/absorption at interfaces

| # | Reference | Status | Gap |
|---|---|---|---|
| 13 | No dedicated review of thermoelastic reflection/transmission found. Crossref title search returned individual papers only, e.g. "Reflection and transmission of thermoelastic waves at the corrugated interface of crystalline structure" (*J. Therm. Stresses*, 2021, 6 cites); "Reflection/transmission of plane waves at an imperfectly bonded interface of two orthotropic generalized thermoelastic half-spaces" (*Mater. Sci. Eng. A*, 2008, 22 cites); "Reflection and transmission of thermoelastic waves in multilayered media" (*Geophysics*, 2022, 12 cites); "Reflection and Transmission of Inhomogeneous Plane Waves in Thermoelastic Media" (*Front. Earth Sci.*, 2022, 9 cites). | **Negative result, medium strength** | The literature is a large set of one-off boundary-value papers with different sign conventions, different interface conditions and different definitions of "energy reflection coefficient". **Nobody appears to have unified the energy-flux bookkeeping or checked that R+T+A=1 across theories.** This is the strongest constructive opportunity in the whole brief. |
| 14 | Nayfeh, A. & Nemat-Nasser, S. (1971) "Thermoelastic waves in solids with thermal relaxation", *Acta Mech.* **12**:53–69. DOI 10.1007/BF01178389. 171 cites. | **Primary source** (reflection at a free surface with relaxation). | — |

### R6. Honest assessment: is the field already covered?

Partly — and not where we intend to compete.

- **Well covered, do not re-tread:** the 1967–1998 model set (LS, GL, GN, H–I) is exhaustively surveyed by #1–#3. Anything we say about these models that repeats #1–#3 adds nothing; we must add comparison, corrected attributions, and stability/uniqueness results stated in one notation.
- **Partially covered:** 2000–2020 (DPL, TPL, fractional, two-temperature) is covered only by catalogue-style reviews (#4) that do not derive, do not compare and do not test admissibility.
- **Not covered at all (verified):** MGT (352 titled works, no review); energy-flux partition at interfaces (no review); memory-dependent derivative within thermoelasticity (no review); nonlocal/gradient continuum wave mechanics (covered only for beams, #6).
- **Competitive risk (real):** preprint #5 targets almost exactly our stated scope, including "analytical proofs" and a "model-selection map". It is unrefereed and its provenance should be treated with caution, but if it is revised and published it will be the first mover on the "critical/admissibility" framing. Two consequences: (i) our review must be differentiated on what #5 does *not* claim to do — the interface energy partition (B3) and the cross-theory numerical benchmarks; (ii) we should not build the paper's novelty on "first critical review", which would be falsifiable.

### R7. What a "constructive" review can add (ranked by defensibility)

1. **Energy-flux bookkeeping at interfaces, unified and checked numerically.** Derive one energy balance covering Fourier, LS, GL, GN-I/II/III, DPL, TPL, MGT; state which theories admit a conserved energy and which only a dissipation inequality; define A (absorbed) precisely; verify R+T+A=1 numerically. Nothing in R1–R5 does this.
2. **Admissibility as a single testable criterion** (positivity of energy + well-posedness of the symbol + finite propagation speed where claimed), applied uniformly, with the parameter ranges where each model is *unstable or ill-posed* named explicitly.
3. **Attribution audit.** Re-check who introduced each model and each parameter from primary sources (B2), and document the recurring sign/notation inconsistencies across the literature.
4. **MGT survey** — fills a verified void; must connect the acoustics lineage to the thermoelastic one.
5. **2018–2026 coverage** that #1–#4 cannot have.

What will *not* be new: derivations of LS/GL/GN from first principles, domain-of-influence theorems, uniqueness theorems — all previously published, some of it by Chandrasekharaiah and by Hetnarski–Ignaczak. They may be restated for completeness, with citation, but not sold as contributions.

---

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| #1 Chandrasekharaiah 1986, 39(3):355–376, 22 pp, derives equations | AMR article page (search-indexed snippet giving the publisher abstract verbatim) + Crossref 10.1115/1.3143705 (835 cites) | Publisher abstract; record |
| #2 Chandrasekharaiah 1998, 51(12):705–729, 1149 cites; Comment/Response AMR 56:453 | Crossref 10.1115/1.3098984 and 10.1115/1.1539097; AMR article-abstract URL 51/12/705 | Crossref records; publisher pages |
| #3 Hetnarski & Ignaczak 1999, 22(4–5):451–476, five models, "none verified by combined experiment" | Taylor & Francis abstract page (tandfonline 10.1080/014957399280832); Crossref 602 cites | Full abstract |
| #4 Shakeriaski et al. 2021, 8(1):15–35, five theories | OUP article page; S2 API (58 cites, open access) | Abstract + conclusion |
| #5 preprint scope and posting date | researchsquare.com/article/rs-10734164/v1; DOI 10.21203/rs.3.rs-10734164/v1 | Abstract |
| #6 Eltaher et al. 2016, 40(5–6):4109–4128 | ScienceDirect record via search; Crossref DOI | Full abstract |
| #7 Askes & Aifantis 2011, 48:1962–1990, 855 cites | Crossref 10.1016/j.ijsolstr.2011.03.006 | Record; abstract not fully read |
| #8 stress-driven nonlocal reviews, 35 and 38 cites | OpenAlex type:review search | Metadata only |
| #9 no fractional/MDD heat-conduction review | Crossref `query.title` search | Search result only — negative |
| #11 Quintanilla 2019, 24:4020–4031, 409 cites | Crossref 10.1177/1081286519862007 | Record |
| #12 no MGT review; 352 titled works | OpenAlex `filter=title.search:Moore-Gibson-Thompson` (count 352), first 25 inspected | Structured query |
| #13 no interface-partition review; sample papers | Crossref `query.title` search | Search results only — negative |
| #14 Nayfeh & Nemat-Nasser 1971 | Crossref 10.1007/BF01178389 (171 cites) | Record |

## Checks done

- Negative results were obtained by **enumerating and inspecting**, not by assuming absence: all 352 MGT-titled works were counted and the 25 most-cited inspected for type `review`; AMR's full 2018–2026 list was scanned (see V-B1a).
- Citation counts for competing reviews taken from a single consistent index per row (Crossref where available), so rows are comparable.
- The "omissions" column was generated by comparing the *stated scope in the abstract* against the model list in the brief, not by memory of the papers' contents.

## Confidence

- **HIGH**: the bibliographic facts (authors, year, journal, volume, pages, DOI) of items #1–#7, #10–#11, #14; the absence of an MGT review; the absence of an interface-partition review (bounded by the searches described).
- **MEDIUM**: "derives vs collects" for #1–#4 (inferred from abstracts and author statements), and my reading of what each review omits.
- **LOW**: the claim that fractional/MDD heat conduction has no review anywhere (my Crossref title search is low-recall; a review may exist under a title like "anomalous diffusion in thermal transport"); the status of the two low-cited nonlocal reviews (#8), which I did not read.

## NOT verified / open issues

1. **No competing review body text was read** — all paywalled. Every "what it omits" statement is an inference from abstracts. Before submission these claims must be re-checked against the actual texts, especially #1–#3, which we will be measured against. A wrong "previous reviews omit X" claim about Chandrasekharaiah or Hetnarski–Ignaczak would be damaging.
2. **Preprint #5 is unverified in content.** Unknown authorship quality, unknown whether it will be published. It should be monitored; a literature search shortly before submission is warranted.
3. **Monographs not verified in this session:** Ignaczak & Ostoja-Starzewski, *Thermoelasticity with Finite Wave Speeds* (OUP, 2010); Dhaliwal & Singh, *Dynamic Coupled Thermoelasticity* (1980); Nowacki, *Dynamic Problems of Thermoelasticity* (1975); Tzou, *Macro- to Microscale Heat Transfer* (2nd ed. 2014); Povstenko's fractional heat-conduction book. These are the standard references for B2 and **must be checked from the actual books**, not from citations to them. Flagged for B2.
4. **Two-temperature reviews:** OpenAlex returned a 2019 item "A Review On Two-Temperature Theory Of Generalized Thermoelasticity" with **no DOI** — venue and quality unknown; not counted. Verify or discard in B2.
5. Journals I did not systematically search: *J. Thermal Stresses* (review issues), *Applied Mechanics Reviews* pre-2018 (partly covered in V-B1a), *Encyclopedia of Thermal Stresses* (Springer, 2014) — the encyclopedia contains review-length entries (e.g. Ignaczak & Hetnarski, "Generalized Thermoelasticity: Mathematical Formulation", pp. 1974–1986) that a referee may consider prior coverage.
