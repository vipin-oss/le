# Claim register (v2, 31 Oct 2026)

`claim_register.csv`: 224 claim checks, one row per (manuscript statement, cited source). Schema follows BLUEPRINT_v3.1 section 5.2 (claim id, statement, source DOI, page/equation, verification level, verifier, status), plus the verifier's wording of what the source states.

| verdict | n |
|---|---|
| SUPPORTED | 50 |
| PARTLY SUPPORTED | 18 |
| NOT SUPPORTED | 2 |
| SOURCE NOT AVAILABLE | 154 |

Caveats
- Statements refer to the manuscript text at the time of each check; several were reworded afterwards (see `arena_changelog.md` and the git history). Rows flagged "partly/not supported" were reviewed when the wording was changed but have not been re-audited against the final text.
- "SOURCE NOT AVAILABLE" means the verifier did not have the PDF; it is not a finding against the claim. Priorities for supplying the sources are in the missing-sources lists.
- Covers the batches delivered so far (section 2-15 claims); sections not yet claim-checked are not in this file.
- Claim ids `CRnnn` are unique; the original ids are kept in `origin`. No file locations of the source library are recorded.
- Verification level R3 applies to the source record, not to the claim; the verdict is per claim.
