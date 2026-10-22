# R3a Crossref verification method

Scope: REFERENCE_PLAN rows whose `plan_section` is s.4.1–s.4.12. Each `lit_id` is joined to `LITERATURE_BASE.id`; the DOI is read only from the capitalized `DOI` column. `CITATION_MAP.csv` supplies claim-to-key associations, and `LITERATURE_ROW_INDEX.csv` is checked only for consistency/history (its old HTTP status never upgrades a row to VERIFIED).

For each unique DOI, the job requests `https://api.crossref.org/works/<URL-encoded DOI>` with `le-crossref-enrichment/1.0 (mailto:vipin@gurugramuniversity.ac.in)`. `CROSSREF_REQUEST_LOG.csv` records DOI, HTTP status, UTC time, metadata-file path, and error. `crossref_raw/` contains an allowlisted Crossref metadata projection (DOI, type, title, authors, issued/published dates, venue, publisher, volume/issue/pages, ISSN/ISBN); abstracts, links, reference lists, and full-text material are excluded.

`CROSSREF_VERIFY.csv` compares DOI, normalized title, year, and venue against `LITERATURE_BASE`. Venue comparison removes a trailing volume/page locator and expands a fixed set of common journal abbreviations; no row-index HTTP code is treated as verification evidence. `VERIFIED` requires DOI, title, year, and venue all to match. A Crossref HTTP 404 is `NOT-FOUND`; a returned record with any disagreement is `MISMATCH`. Network/decoding failures fail the job instead of being relabelled as NOT-FOUND.

`R3A_VERIFIED_REFERENCES.bib` includes only `VERIFIED` rows with `technical_claim_eligible=YES`, a nonempty Crossref author field, and no conflicting existing BibTeX key. New author and bibliographic fields are taken from the saved metadata JSON. Metadata-only/NONE rows are excluded.

Counts: 81 plan rows in scope; 81 rows with a Crossref DOI; 81 unique DOI requests; 14 bibliography-ready keys. No DOI records are handled separately in R3_STATUS.md as printed-source leads, not fabricated DOI matches.
