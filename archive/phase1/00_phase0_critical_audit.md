# Phase 0 Critical Audit

**Prepared:** 2026-10-21  
**Status:** Milestone A — Foundation audit (Completed and verified)  
**Audit standard:** Every Phase 0 claim checked against source evidence; unverified claims explicitly flagged

---

## 1. Executive Summary

Phase 0 successfully established the researcher's identity, mapped the research domain, audited existing
reviews, and proposed five candidate topics with Topic T1 (energy-flux partitioning at multiphysics
interfaces) recommended. The workspace maintains strong integrity standards (VERIFIED/SNAPSHOT/INFERRED/
UNVERIFIED tagging, DOI traceability, reproducible query logs).

However, several Phase 0 claims require correction or qualification before Phase 1 proceeds:

| # | Concern | Severity | Required action |
|---|---------|----------|-----------------|
| 1 | "Zero reviews located" is reported as though it proves novelty absence | Medium | Re-test against Scopus/Web of Science with alternative terminology |
| 2 | Weighted scores treated as comparative measurements rather than ordinal judgements | Low | Clarify in Phase 1 matrix |
| 3 | Citation counts from OpenAlex not cross-checked against Scopus/WoS | Medium | Cross-check key foundational works |
| 4 | Corpus volume counts based on title/abstract only, not full-text eligibility | Medium | Document as order-of-magnitude only |
| 5 | Author-programme fit scores risk over-weighting self-citation | Medium | Independently sampled corpus required |
| 6 | No experimental/numerical validation component in Phase 0 | Expected | Plan benchmarks in Phase 1 |

Details below.

---

## 2. Author Identification Audit

### 2.1 Confirmed (VERIFIED)

| Claim | Evidence | Status |
|-------|----------|--------|
| Name: Vipin Gupta | ORCID public record | VERIFIED |
| ORCID: 0000-0002-5238-1963 | ORCID record | VERIFIED |
| Position: Assistant Professor (Mathematics), Gurugram University | ORCID employment entry, 2024-06-28 | VERIFIED |
| Previous: Department of Mathematics, Indira Gandhi University, Meerpur | Author affiliations on articles; OpenAlex affiliation years | VERIFIED |
| Verified email domain: gurugramuniversity.ac.in | ORCID record | VERIFIED |
| CSIR funding File No. 09/1293(0003)/2019-EMR-I | Publisher acknowledgement text | VERIFIED |

### 2.2 Homonym Exclusion (VERIFIED)

| Homonym | ORCID | Field | Works | Citations | Action |
|---------|-------|-------|-------|-----------|--------|
| Biomedical researcher | 0000-0002-0607-5543 | Epidemiology/global health | 74 | 47,861 | EXCLUDED — not the wave-propagation author |

### 2.3 Unverified (explicitly documented in Phase 0)

- Google Scholar metrics (profile reCAPTCHA-blocked)
- Scopus Author ID and metrics
- Web of Science ResearcherID
- PhD year/institution/thesis
- Editorial board memberships, awards
- Full grant portfolio

**Audit verdict:** Author identification is solid. ORCID 0000-0002-5238-1963 is the correct identity. No corrections needed.

---

## 3. Publication Record Audit

### 3.1 Counts

| Metric | Phase 0 value | Source | Status | Audit note |
|--------|--------------|--------|--------|------------|
| Works (OpenAlex author profile) | 41 | OpenAlex author A5013823819 | SNAPSHOT | Split profiles exist |
| Works (ORCID filter) | 49 | OpenAlex author.orcid filter | SNAPSHOT | Includes preprints, book chapter |
| Citations (author profile) | 827 | OpenAlex | SNAPSHOT | Will drift; not cross-checked |
| h-index | 19 | OpenAlex | SNAPSHOT | Not cross-checked |
| i10-index | 28 | OpenAlex | SNAPSHOT | Not cross-checked |

### 3.2 Audit concerns

1. **41 vs 49 discrepancy:** Phase 0 correctly identifies this as a record-linkage artifact (split author profiles A5128895995, A5137960888 also carry ORCID 0000-0002-5238-1963). This is honestly documented.

2. **Citation counts not cross-checked:** OpenAlex citation counts are SNAPSHOT values from 2026-10-21. No Scopus or Web of Science cross-verification was performed. This matters because:
   - The recommended topic's justification partly rests on the researcher's "programmatic" publication record
   - Citation counts are used to rank foundational works (e.g., Chandrasekharaiah 1998 = 1149 cites in OpenAlex)
   
   **Required action:** Cross-check the top 10-15 most-cited works against Crossref (already done for foundational works) and, if accessible, Scopus/WoS.

3. **Corpus volume counts (686 reflection+thermoelastic; 1,036 nonlocal+thermoelastic; etc.):** These are OpenAlex title/abstract match counts, not full-text eligibility counts. They are order-of-magnitude context only, correctly labeled as such in Phase 0.

**Audit verdict:** Publication record is adequately documented with appropriate uncertainty labeling. No corrections needed to the record itself, but Phase 1 must not treat SNAPSHOT citation counts as definitive.

---

## 4. Domain Taxonomy Audit

### 4.1 Five-axis taxonomy (A–E)

The taxonomy classifies each work by:
- **A** Thermal law (Fourier → LS → GL → GN II/III → DPL → TPL → MGT → MDD → fractional)
- **B** Coupling field (elastic → thermoelastic → piezoelectric → poroelastic → semiconductor)
- **C** Pore structure (solid → voids → double porosity → saturated → micropolar)
- **D** Scale/size (local → nonlocal → size-dependent → micro/nano)
- **E** Geometry/boundary (half-space → interface → free surface → layered → cavity)

### 4.2 Audit concerns

1. **Tuple assignments are INFERRED, not VERIFIED:** Phase 0 explicitly states "this tuple structure is my own classification; no source states it explicitly." This is honest but means the five-axis decomposition should be treated as an analytical framework, not as data extracted from papers.

2. **Historical lineage table:** Foundational contributions (Biot 1956, Lord & Shulman 1967, Green & Lindsay 1972, Green & Naghdi 1991, Tzou 1995, Roy Choudhuri 2007, MDD 2011/2014, Quintanilla 2019) are Crossref-verified with DOIs and citation counts. This is solid.

3. **Governing equations:** Schematic equations are presented as representative of the model family, not as exact quotes from any specific paper. This is appropriate for a theoretical framework but must not be misrepresented as extracted content.

**Audit verdict:** Taxonomy is a useful analytical framework. Must be labeled as analyst-constructed, not source-extracted. No corrections needed, but Phase 1 must maintain this distinction.

---

## 5. Existing Review Analysis Audit

### 5.1 Search scope

Phase 0 searched OpenAlex (`type:review` and title-based filters) and Crossref (exact bibliographic match) across 9+ review-relevant slices:

| Search slice | Works found | On-target reviews |
|-------------|-------------|-------------------|
| piezo-thermoelastic + review | 0 | 0 |
| memory-dependent + review | 77 | 0 (thermoelastic interfaces) |
| fractional thermoelastic + review | 1 | 0 (unverified venue) |
| piezoelectric + wave + review | 163 | 0 (all energy-harvesting/SHM) |
| surface waves + review | 270 | 0 (all ocean/geophysical/metasurface) |
| reflection and transmission + review | 40 | 0 (none on elastic/piezoelectric) |
| poroelastic + review | 95 | 0 (all geotechnical/CO2/seismic) |
| flexoelectric + review | 23 | 0 (all materials/applications) |
| photothermal + semiconductor + review | 30 | 0 (all biomedical/therapy) |

### 5.2 Audit concerns

1. **"Zero reviews located" ≠ "no reviews exist":** Phase 0 correctly states this limitation but the recommendation text sometimes comes close to implying proof of absence. For example: "targets the largest verified gap: zero located reviews synthesize energy-flux definitions." This should be "zero located in OpenAlex/Crossref searches."

2. **OpenAlex `type:review` is incomplete:** Phase 0 acknowledges this. Reviews may exist that are not classified as `type:review` by OpenAlex or that don't have "review" in the title.

3. **Alternative terminology not searched:** Phase 0 did not search for "wave energy transport," "interface scattering," "energy transmission," "reflection coefficients," "elastic wave energy," "coupled-field energy balance," "acoustic and elastic impedance," "dissipative waves," etc. These are the exact alternative terms the Phase 1 protocol requires.

**Audit verdict:** The review saturation analysis is methodologically limited to OpenAlex/Crossref title/abstract searches. The "gap" claim is reasonable but unconfirmed against broader databases and alternative terminology. **This is the primary Phase 1 verification task.**

---

## 6. Topic Selection Reasoning Audit

### 6.1 Decision matrix

The weighted matrix assigns T1 a score of 4.37/5.00 vs T2 at 3.53/5.00. Weights sum to 1.000.

### 6.2 Audit concerns

1. **Ordinal scores treated as interval measurements:** The matrix computes weighted sums of 0–5 ordinal scores, which is mathematically questionable but acceptable as a decision aid if explicitly labeled. Phase 0 does label scores as "ordinal analyst judgements."

2. **Author-programme fit (weight 0.11) potentially over-weighted:** T1 scores 5/5 partly because the researcher's own series dominates energy ratios. This creates a self-referentiality risk that Phase 0 identifies but does not fully mitigate in the scoring.

3. **Sensitivity analysis is qualitative:** Sensitivity variants return "T1_leads" without showing recomputed scores. This reduces transparency.

**Audit verdict:** The decision matrix is a reasonable decision aid but its precision is overstated. Phase 1 should present it as a structured comparison, not a measurement.

---

## 7. Source Quality and Completeness Audit

### 7.1 Source types used

| Source type | Count | Verification approach |
|-------------|-------|----------------------|
| ORCID registry | 1 | Direct page fetch |
| OpenAlex API | ~25 | API query with full URL logged |
| Crossref API | ~12 | Exact bibliographic match + DOI verification |
| Publisher pages | 3 | Direct page fetch (ASME, Emerald, Springer) |

### 7.2 Completeness gaps

- No Scopus, Web of Science, Dimensions, Semantic Scholar, or arXiv searches
- No full-text reading of any corpus paper
- No backward/forward citation chasing
- Journal scope verification incomplete for several target journals

**Audit verdict:** Evidence base is adequate for Phase 0 scope (domain identification and topic recommendation) but insufficient to confirm novelty. Phase 1 must broaden the search.

---

## 8. Required Corrections for Phase 1

1. **Re-state novelty claims:** Change "no review exists" to "no review located in OpenAlex/Crossref searches as of 2026-10-21; unconfirmed against Scopus/Web of Science."

2. **Broaden literature search:** Execute searches with alternative terminology (wave energy transport, interface scattering, reflection coefficients, coupled-field energy balance, etc.) across multiple databases.

3. **Cross-check citation counts:** Verify key foundational work citation counts against Crossref (partially done) and Scopus/WoS if accessible.

4. **Independently sample corpus:** The review must not be built primarily on the researcher's own co-authorship network.

5. **Clarify scoring:** Present the decision matrix as ordinal comparison, not measurement.

---

## 9. Phase 0 Integrity Compliance

| Phase 0 integrity rule | Compliance | Evidence |
|----------------------|------------|----------|
| No invented citations/authors/DOIs | Yes | All DOIs Crossref/OpenAlex verified |
| DOI traceability to verification log | Yes | source_verification_log.csv |
| VERIFIED/SNAPSHOT/INFERRED/UNVERIFIED tagging | Yes | Applied consistently |
| Absence ≠ proof of nonexistence | Partially | Stated in limits; occasionally implied in recommendation |
| No citation count promises | Yes | Explicitly stated |
| Journal scope quoted only where retrieved | Yes | PARTIAL status used appropriately |
| Google Scholar inaccessibility stated | Yes | Clearly documented |

**Audit verdict:** Phase 0 meets its stated integrity standards. The primary gap is breadth of literature search, not integrity of what was searched.

---

## 10. Milestone A Status

**Milestone A — Foundation audit: COMPLETED AND VERIFIED**

Phase 0 is sound for its stated purpose (domain identification and topic recommendation). The recommended topic T1 remains defensible but unconfirmed as novel. Phase 1 must execute broader literature searches to confirm or refute the gap claim before manuscript development proceeds.

**Next action:** Proceed to Milestone B — Review protocol (registered_protocol_draft.md).