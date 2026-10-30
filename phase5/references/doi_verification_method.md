# DOI verification method and evidence status (pre-enrichment)

## Finding

The repository version of `phase5/references/doi_verification.csv` contains no Crossref response bodies, request log, or script that generated its historical `YES` values. The notes identify Crossref as the asserted source, but do not record the request URL, response fields, title/author/year comparisons, HTTP status, or a saved raw response. I therefore cannot reconstruct how each historical `YES` was produced and do not treat those values as verified evidence. Every row without a saved response is now explicitly `UNVERIFIED`; this is not a finding that the DOI or work is false.

## Method to be used by the manually triggered workflow

The `Manual Crossref enrichment and audit` workflow requests `https://api.crossref.org/works/<URL-encoded DOI>` with a polite User-Agent containing the handler's mailto address. It saves the unmodified response JSON per DOI under `phase5/references/crossref_raw/` and records the DOI, HTTP status, UTC timestamp, raw-file path, and any error in `crossref_request_log.csv`. The generated local-bibliography audit compares title, first-author family name, year, and page/article-number fields. A row is marked matched only when all four comparisons are YES; missing page data remain UNVERIFIED, and any disagreement is a mismatch. Requests are deduplicated by DOI and duplicate source records are listed in `duplicate_doi_audit.csv`; enriched BibTeX uses stable `LIT-####` record IDs as keys. BibTeX enrichment consumes only fields present in the saved raw response.

No-DOI records remain `UNVERIFIED` for DOI resolution and require a separate archival/catalogue record if their bibliographic facts are to be upgraded. A Crossref metadata match verifies metadata only; it does not verify that a cited paper supports a scientific claim.

## Named records requiring care

The historical CSV's Guyer 1990 DOI, Eringen 1968b authorship/key, Vernotte 1958 page range, Abdalla 2022 relevance, and the stated Sharma/Iesan/Povstenko/Barak metadata remain subject to raw-response or archival cross-check. No disputed bibliography entry has been deleted here. Unsupported scientific attributions are tracked separately in the R2 decision log.
