# Crossref / first-page reconciliation (B22 continuation)

This register compares every bibliography `source` field that says a primary
paper's first page confirms metadata (`Quintanilla2003DPL` and
`DellOroPata2016Viscoelasticity`). The itemized comparisons are in
`CROSSREF_FINAL.csv`.

## Evidence provenance and limits

The saved Quintanilla Crossref lookup responses in `crossref_final/` were
copied unchanged from the read-only B22 audit artifacts on 2026-10-27. They
record a matching work at DOI `10.1080/713855996` and no record for
`10.1080/01495730390203518`. The B22 artifact reports that its held Taylor &
Francis cover page prints `10.1080/713855996`. By contrast, the earlier local
source note `R4B_SOURCE_FINDINGS.md` reports that its inspected first page
printed `10.1080/01495730390203518`. The exact source copy could not be found in
the targeted Drive searches or locally for reinspection. Both source-page
reports are preserved; the DOI conflict is unresolved, so the bibliography
uses the Crossref-matching candidate but marks `verified = {NO}`. This is not a
claim that the source-page dispute has been settled.

Sandbox network egress does not permit direct requests to `api.crossref.org`.
Accordingly, this continuation does not claim to have run a new title/author/
journal Crossref query. Quintanilla comparisons use the saved B22 DOI responses
and reported source-cover inspection. Dell'Oro–Pata's volume/pages comparison
uses the B22 saved comparison row; no raw DOI response for that work was in the
available B22 raw-response set. Fields not present in those saved records are
marked `NOT-IN-SAVED-RESPONSE`, not inferred.


## Dell'Oro–Pata locator disposition

The bibliography locator is now filled as *Applied Mathematics and Optimization* 76:641–655 from the saved B22 Crossref comparison row. The bibliographic first-page inspection independently confirms authors, title, DOI, and copyright year, but the raw Crossref DOI response is not available in the current branch and direct Crossref egress is blocked. The entry therefore retains `verified = {NO}`; `CROSSREF_FINAL.csv` labels the locator comparison as B22-reported rather than independently re-fetched.
