# R4A deletion-audit method and reconciliation

## Scope and row interpretation

- The audited source diff is `26dffda..a636514`, limited to 24 manuscript section/table files (371 insertions, 564 deletions). The CSV contains 593 sentence/table audit units across 23 files; pure layout commands and headers were excluded, while mixed scientific table rows remain claim-tracked.
- `file:line` identifies the deleted-side location in `26dffda`; `deleted_text_short` is a sanitized excerpt. `PROCESS-TEXT` means the deleted unit is editorial, bibliographic, formatting, notation, or research-planning text rather than a scientific claim. An `OCL-###` value points to a stable row in `OPEN_CLAIMS_LEDGER.csv`. Reasons do not claim that deleted wording survives or has been scientifically verified.
- Of 593 rows, 62 retain one or more pre-existing ledger IDs (64 distinct IDs are referenced, including deletion-block mappings). The 531 former `NONE` rows are resolved as 202 `PROCESS-TEXT` units and 329 scientific-claim links to 314 distinct newly added claim entries; duplicate claims/topics were merged. No `NONE` values remain. The audit maps all linked IDs to the ledger; a locator is traceability, not evidence of verification.

## Ledger and figure reconciliation

- `PROCESS_LANGUAGE_INVENTORY.csv` has 164 phrase-hit rows and 139 unique `(file,line)` locations. Of those, 125 phrase-hit rows fall on deleted lines in the scoped diff: 100 unique deleted locations plus 25 repeated phrase hits across 16 locations. The remaining 39 unique inventory locations are not deleted in this scoped diff.
- The 139 unique inventory locations reconcile to A=16, B=5, and C=118. The pre-existing ledger rows `OCL-001`–`OCL-123` remain in order with B=5, C=118, and A=0 because the A-class locations are not open claims.
- `OPEN_CLAIMS_LEDGER.csv` now contains 439 rows: the original 123 plus 314 distinct scientific claim entries and two C-class figure claims. Totals are B=144 and C=295. IDs are sequential through `OCL-439`; the additional rows specify author/year leads where available and a concrete equation, assumption, scope, or source check. A source lead or bibliography match does not verify a claim.
- F07 (`fig07-theory-map.svg`; Section 4) is linked to `OCL-438`, class C. Its provisional cross-family limiting arrows and generalized flux labels remain unverified; it stays excluded. F18 (`fig18-taxonomy.svg`; Section 14) is linked to `OCL-439`, class C. Its inherited gap-population labels do not align with the current Q1–Q8 framing; it stays excluded. Neither figure is restored.

## Validation cautions

The audit is a traceability aid, not independent scientific verification. Source identity/presence is distinguished from claim verification. Deleted excerpts and linked IDs were reconciled against the stated source lines and current ledger; duplicate historical claims were merged without changing the original 123 ledger rows. The audit does not restore process-status tags to manuscript prose. The omitted quadratic candidate-kernel wording is specifically explained in Section 6, and its numerical form is not asserted.
