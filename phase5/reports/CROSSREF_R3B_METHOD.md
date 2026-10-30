# R3b Crossref verification method

Scope: REFERENCE_PLAN plan_section s.5–s.9 and s.11–s.13 (Section 10 is reserved for R3c). Each plan `lit_id` joins to `LITERATURE_BASE.id`; only `technical_claim_eligible=YES` rows are queried, using the capitalized `DOI` field. Ineligible rows remain in the audit as `INELIGIBLE` and generate no request. The frozen CITATION_MAP is consulted for exact claim-to-key matches. New manuscript placements use the local `R3B_CITATION_MAP.csv`, which maps these eligible plan keys to section-specific source claims; metadata-only rows are never used as technical evidence.

The comparison uses the same relaxed R3a criteria: title is acceptable when exact, a prefix/substring, or shared-token coverage of at least 0.60 of the shorter title; the base year may match a published-print/online/issued year or differ by at most one year; the normalized venue must match Crossref container-title/short-container-title; requested DOI must equal returned DOI. Crossref title overlap under 0.60 is MISMATCH and listed in `CROSSREF_R3B_HUMAN_CHECK.md`. A 404 is NOT-FOUND; no DOI is NO-DOI. Network/decoding errors fail the job.

Only VERIFIED `technical_claim_eligible=YES` rows with Crossref authors and no BibTeX-key/DOI conflict enter `R3B_VERIFIED_REFERENCES.bib` and the conditional citation map. BibTeX year uses Crossref `issued` year (published-print/online fallback).

Rows: 90; eligible DOI rows queried: 47; unique DOI requests: 47; eligible rows: 51; VERIFIED: 40; MISMATCH: 5; NOT-FOUND: 2; NO-DOI: 4; INELIGIBLE (not queried): 39; bibliography-ready eligible keys: 39.
