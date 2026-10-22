# Independent verification — Phase B1

Role: independent verifier. I did not see, and did not edit, the manuscript. Everything below was derived or checked from sources I could open; everything I could not check is listed under each file's "NOT verified" heading.

**Phase status: B1 complete (a, b, c). B2 and B3 not started — awaiting go-ahead.**

## Files

| File | Contents | Confidence |
|---|---|---|
| `V-B1a_amr-landscape.md` | 13 AMR reviews 2018–2026 (metadata, refs, cites, page counts), descriptive statistics, AMR length/author policy with quotes, and the finding that AMR has no recent thermoelasticity review | HIGH on bibliographic + policy; MEDIUM on page statistics; figures/tables UNVERIFIED |
| `V-B1b_competing-reviews.md` | 14 existing reviews/primary sources across 5 sub-areas, coverage/omission assessment, honest "is the field covered?" verdict, ranked list of what a constructive review can add | HIGH on bibliography; MEDIUM on coverage judgements (no full texts read) |
| `V-B1c_most-cited.md` | 15 most-cited papers with Crossref **and** OpenAlex counts, runner-ups, index-dependent rank pairs flagged, and explicit statement that Google Scholar/Scopus/WoS were unavailable | HIGH as Crossref/OpenAlex counts; NOT a Google Scholar ranking |

**Revision log (after supervisor audit of B1):** (1) the "Length: open" quote in V-B1a now carries the exact URL, the exact sentence, the read date and a note that it is an ASME-wide page, not an AMR-specific one; (2) AMR digitisation caveat added for the 1998 Chandrasekharaiah DOI (print 1998, publisher page 2009); (3) the 2026 Research Square preprint is re-characterised in V-B1b from its verified 15-section list — overlap is partial, and it has **no** interface-partition, two-temperature, MDD, fractional or piezothermoelastic content; (4) OpenAlex counts added for all 15 rows in V-B1c, with the two index-dependent rank swaps flagged.

## Environment constraints (affect what "verified" means here)

- Direct `curl` from the sandbox to the open internet is blocked (`asmedigitalcollection.asme.org`, `doi.org`, `scholar.google.com`, `api.crossref.org` all returned HTTP 000). The web-fetch and web-search tools *do* have access, so all lookups were routed through them.
- **Google Scholar is unreachable.** Scopus and Web of Science have no credentials. Citation counts therefore come from **Crossref** `is-referenced-by-count` and **OpenAlex** `cited_by_count`, plus **Semantic Scholar** for cross-checks. These are systematically lower than Google Scholar counts (see V-B1c).
- **No subscription access to ASME, Taylor & Francis, Elsevier, Springer or OUP full texts.** All PDF links redirect to paywalled abstract pages. Consequence: page counts are verifiable (printed on the publisher's abstract page), but **figure counts, table counts and section counts are not**, and no competing review's body text could be read.
- AMR stopped depositing page ranges to Crossref around 2018 and now uses article numbers (`040801`), so "number of pages" for recent AMR articles is only obtainable from the publisher's article page or the PDF.

## Conventions used

- Every factual claim about a paper carries DOI (or stable publisher URL) and the read level: *record only* / *abstract* / *body*.
- Negative results ("no review exists on X") are stated together with the search that produced them and the bound on their strength.
- Citation counts always name the index and the retrieval date (all 2026-10-22).
- Confidence labels in each file refer to that file's claims, not to the project as a whole.

## Standing open items for the handler

1. **Figures/tables/sections for the 13 AMR reviews** need ASME access; the DOIs are listed in V-B1a and the columns can be filled quickly once PDFs are available.
2. **The 2026 Research Square preprint** "Thermodynamic Admissibility, Finite-Speed Heat Transport, and Wave Stability in Generalized Thermoelasticity: A Critical Review with Analytical Proofs" (DOI 10.21203/rs.3.rs-10734164/v1) targets nearly the same scope as this project. It is unrefereed. Someone should track whether it is published.
3. **V-B1c must not be presented as a Google Scholar ranking.** Re-run with GS/Scopus if available.
