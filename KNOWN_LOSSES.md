# Known losses and unavailable work

**Decision:** stop all recovery of the 24–25 October work. No attempt was made here to reconstruct or restore it. Existing checkpoint/manifests were moved under `archive/recovery/` as historical records only; they were not used to rebuild missing artifacts.

| Unlocated work | Current disposition | What is available instead |
|---|---|---|
| 96-claim traceability matrix | Lost/unlocated; will not be recovered. | `phase5/reports/OPEN_CLAIMS_LEDGER.csv` is the current open-claim register (439 rows). It is not a reconstruction of the 96-claim matrix. |
| Defect register | Lost/unlocated; will not be recovered. | `phase5/reports/DEFECT_STATUS.csv` is a separate current project status file, not the lost register. |
| D4/D5 packet | Lost/unlocated; will not be recovered. | Open items remain in the current claim and audit records; no D4/D5 packet is recreated. |
| 43 test scripts | Lost/unlocated; will not be recovered. | The strict CI workflow and extant `phase5/scripts/` are the only available checks. They are not represented as the missing 43 scripts. |

## Current audit records

- [`phase5/reports/OPEN_CLAIMS_LEDGER.csv`](phase5/reports/OPEN_CLAIMS_LEDGER.csv) is authoritative for current open-claim tracking: 439 rows, class B = 144 and class C = 295. A named source lead does not independently verify a claim.
- [`phase5/reports/R4A_DELETION_AUDIT.csv`](phase5/reports/R4A_DELETION_AUDIT.csv) is authoritative for the text removed in the R4A scope: 593 rows, zero `NONE` ledger identifiers. It records removals; it does not recreate the lost matrix or packet.

These records replace the **current tracking function only**. They are not equivalent reconstructions of the missing work. See [`phase5/reports/README.md`](phase5/reports/README.md) for authority and history by file.
