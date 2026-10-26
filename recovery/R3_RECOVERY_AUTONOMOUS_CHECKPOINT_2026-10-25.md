# R3 authorized recovery and scientific-repair checkpoint — 2026-10-25

**Overall: NOT PASSED / NOT SUBMISSION READY.** This is an additive recovery record, not a certification of the current R3 project, manuscript, mappings, or gates. No elapsed duration is reported: a verified run-start timestamp was not recorded.

## Repository and safety state

- Branch: `arena/b5e608f8-le` (active); HEAD: `fad98f923e76563e3fe4e8852d85cd68fc7c6fc5`.
- Final local status before writing this checkpoint: tracked tree clean, `git diff --check` passed, no staged changes. `git ls-files` contains only `README.md`. Existing untracked `R3_DEEP_CLAIM_TRACEABILITY_RECOVERY_CHECKPOINT_2026-10-25.md` was read and preserved; recovery material is additive under `recovery/`.
- No branch/ref changes, fetch/pull, synchronization, staging, commit, push, reset, rebase, merge, or protected manuscript/control-file edit occurred. No dependency was installed. No external message or library request was sent.
- The temporary `google_drive/` staging directory created for downloads was removed after copying needed evidence into `recovery/`. No `[REDACTED: private storage reference]` content was downloaded, opened, extracted, or used. A prior Drive folder-list response had incidentally displayed a sibling-file metadata row; no action was taken on it.

## Recovery inventory and provenance

1. The checkout is still a hand-off/cleared repository, not the current R3 project: `README.md` is the only tracked file. The authoritative current 96-claim matrix, manuscript, bibliography, current claim maps, R3F validator/tests, current defect/gate registers, D4/D5 control decision, GAP-23 criteria, and FW-013 origin remain unavailable. Bounded Drive searches for the current matrix/manuscript/validator/defect and control records returned no files.
2. The full pre-GAP-12 workstate archive at `[REDACTED: private storage reference]` remains unavailable. Its recorded expected SHA-256 is `8bff8a6c9c4a5e6b5e45921b7e4f4640f77c9c882b0c707e7287da5a11412cdc`; the archive bytes themselves were not found. No old archive was restored over any current file.
3. A separately preserved historical backup now contains its README, critical manifest and sidecar, historical workstate manifest and sidecar, source-provenance CSV, branch-file classification, historical R3B citation map, evidence-inspections CSV, and Wang–Li 2011 PDF. Structural checks recorded: 1,307 unique historical manifest paths; 810 classification rows; 47 unique claim IDs in the historical map; 9 source-provenance records. A CSV-width check found historical `source_provenance.csv` row `SRC-006` has unquoted commas in its notes (9 cells against a 7-column header). The byte-exact source is preserved; an additive `source_provenance_normalized.csv` copy joins those note fragments without dropping data. These are historical artifacts, not proof of current R3 completeness.
4. Authorized source archives were independently checked against Drive metadata and ZIP CRCs: `R3.zip` (20 PDFs; 57,872,167 uncompressed bytes), `paper.zip` (4 PDFs), and `RP_2.zip` (16 PDFs; 16,385,183 uncompressed bytes). They are source collections, not the missing R3 project snapshot. Only selected, verified source members were retained; archive inventories and content hashes are recorded under `recovery/primary-sources/`.
5. The 18-row dated recovery inventory distinguishes available historical/source items from missing current project artifacts. The evidence manifest added alongside this checkpoint lists all 25 retained artifacts across `recovery/` and the preserved prior root checkpoint; it excludes itself and its sidecar. Its own SHA-256 is recorded in the companion `.sha256` sidecar.

## Source identity and scientific work completed

- **Guyer–Krumhansl `.766`:** `[REDACTED: private storage reference]`, SHA-256 `b6dd6daa7ece2cfd84bcd390973ae6b977989010f5228e106f25b3d17118f23d`. PDF metadata identifies “Solution of the Linearized Phonon Boltzmann Equation,” *Physical Review* 148, 766 (1966), DOI `10.1103/PhysRev.148.766`. The article body and cited page were not extracted.
- **Guyer–Krumhansl `.778`:** `[REDACTED: private storage reference]`, SHA-256 `746bc094f64baf7dbddce2a5a6e394bfbc6688a1ab0b6a8123b5c87c4e663765`. Extracted text explicitly refers to the preceding `.766` paper as paper “I.” This establishes that the bibliographic identities are distinct and the cross-reference exists; the exact printed page/PDF leaf was not verified. No FW-013 mapping was changed.
- **Achenbach candidate:** a user-owned `R3.zip` member named `achenbach1968.pdf` was retained as `[REDACTED: private storage reference]` (675,911 bytes; SHA-256 `1a491c4bb9412f69f74ce60eb7346e8bcba17ec638a5dd2abd78e7678462dce7`). Its PDF Info exposes only `PII: 0022-5096(68)90035-5`; no author or source passage was extracted. This is a candidate source copy only—not verification of the requested Achenbach book pages or a claim mapping. Two matching Drive DOCX copies remain outlines/book lists rather than source pages. No new Nowacki source or response was located; the existing library request remains pending.
- **Unresolved archive identity discrepancy:** R3.zip member `10.1007@978-1-4612-2210-1.pdf` (30,174,826 bytes; SHA-256 `c05aed09b8cc7f531e147dcdad7c6c2d28b7b8bb196a776cf9f00c6375a52dda`) has an embedded PDF Info title `978-1-4612-7460-5_Book_PrintPDF.pdf` and author field `halbulario`. The member body was not read; the item was not cited or used. Its filename/metadata mismatch is recorded in `recovery/primary-sources/archive-source-discrepancies.csv` for later identity validation.
- A conditional classical local-energy-flux derivation is preserved at `recovery/independent/classical-local-energy-flux-derivation.md`. It is a standalone balance-law derivation under stated classical assumptions; it was not compared with the unavailable manuscript and does not verify a manuscript claim.
- No active claim mapping, bibliography entry, manuscript passage, D4/D5 label, control record, or owner decision was modified. No R3F defect could be confirmed or repaired because the relevant code and current inputs are absent.

## Checks performed and limitations

- Integrity checks: `critical_manifest.csv` passes its sidecar check. The bytes of `le-working-state-manifest.csv` hash to the exact digest recorded in `le-working-state-manifest.sha256`; that sidecar names the archive-internal path `manifest.csv`, so filename-based `sha256sum -c` cannot resolve it in this flat recovery folder. The full archive remains absent and its archive hash is therefore unverified. Recovered-file hashes, uniqueness checks, and missing-core-path checks passed (missing paths remain explicitly missing). Current/generated CSVs parse consistently. The preserved historical `source_provenance.csv` has the documented SRC-006 width defect; its additive normalized copy validates as 9 records by 7 columns.
- ZIP member CRC tests passed for the three downloaded archives; selected PDF member hashes were computed and cross-checked. The two GK identities were not conflated.
- Repository checks: `git diff --check` passed; no tracked or staged changes.
- No `pytest`, `sympy`, LaTeX, command-line PDF extraction/rendering, or Python PDF library was available. No package was installed. ImageMagick PDF rendering was denied by its security policy; therefore source-body/page inspection was not achieved for `.766` or the Achenbach candidate.
- The 96-claim audit, manuscript/bibliography review, R3F regression suite, build, symbolic checks, interface jump/power convention review, and live preflight/apply were **not run**. Preflight/apply remains prohibited while D4/D5 is unresolved. No historical test count is treated as a current passing result.

## Gate states

| Gate | State | Evidence / blocker |
|---|---|---|
| Current authoritative R3 inventory and completeness | **BLOCKED / PARTIAL RECOVERY** | Historical backup and selected sources recovered; current project snapshot absent. |
| 96-claim matrix and manuscript audit | **NOT RUN / BLOCKED** | Current matrix and manuscript unavailable; no current claim population examined. |
| Primary-source claim verification | **NOT PASSED** | Source identities partially clarified, but no current claim passage/page mapping verified. |
| GAP-23 six-source criteria | **OPEN / UNVERIFIED** | Authoritative GAP-23 record and current evidence matrix absent. |
| FW-013 origin and mapping | **OPEN / UNVERIFIED** | `.766`/`.778` identities distinguished, but origin/claim/page mapping absent. |
| D4/D5 control resolution | **UNRESOLVED** | Authoritative decision record/owner ruling unavailable; no control action taken. |
| R3F/audit software and tests | **NOT RUN / BLOCKED** | Current validator, scripts, tests, and inputs unavailable. |
| Interface jump/power and generalized-flux manuscript review | **NOT RUN / BLOCKED** | Actual manuscript conventions and current claim mappings unavailable. |
| Preflight/apply | **NOT RUN** | Must remain disabled while D4/D5 conflict is unresolved. |
| Overall | **NOT PASSED / NOT SUBMISSION READY** | Mandatory recovery, evidence, control, and validation gates remain unmet. |

## Changed-file scope

All new or copied material is untracked under `recovery/`; the prior root checkpoint remains untouched. The historical R3B map and source-provenance CSV were copied from temporary staging into the separate pre-GAP-12 recovery folder after the final inventory check showed they had not yet been retained there. The only scientific addition is the explicitly conditional classical flux derivation; no project code or protected scientific/control content was changed. The evidence manifest and its sidecar list exact file hashes.

## Next executable action

Recover the **current authoritative R3 project snapshot and control packet** (not the historical pre-GAP-12 archive and never `[REDACTED: private storage reference]`) into a separate location, verify its provenance and hashes, and compare paths before any restoration. Required contents include the current manuscript and bibliography, 96-claim matrix and criteria/history, current maps, R3F/audit code and tests, defect/gate registers, D4/D5 owner decision, GAP-23 criteria, and FW-013 origin. Then run isolated R3F regression tests before resuming claim-level primary-source verification. Until that package and the unresolved control decision are available, keep all gates blocked and status **NOT PASSED / NOT SUBMISSION READY**.
