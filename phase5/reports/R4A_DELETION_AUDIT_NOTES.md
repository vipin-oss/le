# R4A deletion-audit method and reconciliation

## Scope and row interpretation

- The audited source diff is `26dffda..a636514`, limited to the 24 manuscript section/table files (371 insertions, 564 deletions). The CSV contains 593 claim-bearing sentence or table-row units across 23 files. Pure layout commands, headers, and process-only statements are excluded; multiple claim sentences from one source line receive separate rows.
- `file:line` identifies the deleted-side location in `26dffda`. `deleted_text_short` is a sanitized excerpt. When `ledger_row_id` is an `OCL-###`, the row points to that stable row in `OPEN_CLAIMS_LEDGER.csv`. A `NONE` entry means no open-ledger item is assigned; its reason points to current, explicitly limited/hedged wording in the working manuscript. Current-line references in `reason` use working-tree line numbers and excerpts.
- Of 593 rows, 62 carry one or more ledger IDs (64 distinct OCL IDs are referenced, including rows mapped at deletion-block level); 531 are `NONE`. All 531 `NONE` reasons include a current hedge/scope locator; validation found zero missing or out-of-range locators and zero targets without an explicit limiting cue. Table-wide caveats may serve several rows in the same table. A locator is contextual traceability, not evidence that a deleted assertion survives or has been scientifically verified.

## Inventory-to-ledger reconciliation

- `PROCESS_LANGUAGE_INVENTORY.csv` has 164 phrase-hit rows and 139 unique `(file,line)` locations. Of those, 125 phrase-hit rows fall on deleted lines in the scoped diff: 100 unique deleted locations plus 25 repeated phrase hits across 16 locations. The remaining 39 unique inventory locations are not deleted in this scoped diff.
- The 139 unique inventory locations reconcile to A=16, B=5, and C=118. `OPEN_CLAIMS_LEDGER.csv` has 123 open items: B=5 and C=118; A=0 because the A-class locations are not open claims. No class totals were silently changed.
- Stable IDs `OCL-001` through `OCL-123` were added to the ledger in its existing row order. The ID column does not change claim wording, classes, or row order.

## Validation cautions

The audit is a traceability aid, not independent scientific verification. Source identity/presence is not treated as claim verification. A final source reconciliation found that all 593 excerpts map to their stated deleted-side lines; linked IDs were checked against the stable ledger, with block-level links retained only where the deletion belongs to that audited section. Current-line locators provide context for the narrowed scope or table-wide caveat; they do not imply that a deleted assertion survives. The audit does not restore process-status tags to manuscript prose. The omitted quadratic candidate-kernel wording is specifically explained in Section 6, and its numerical form is not asserted.
