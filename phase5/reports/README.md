# Phase 5 reports and evidence guide

This folder mixes current authoritative registers with dated, historical snapshots. **Use the status column below; do not treat a Crossref metadata match as verification of a scientific claim.**

## Current sources of truth

- `OPEN_CLAIMS_LEDGER.csv` is the authority for current open claims (445 rows: A=13, B=138, C=294). A row/source lead remains open until its specific claim, source identity, and needed equation/result are checked.
- `R4A_DELETION_AUDIT.csv` is the authority for removed text (593 rows, zero `NONE` identifiers). It does not certify deleted claims or reconstruct missing work.
- `build-status.md` is the current strict-build status. The manuscript/source validation recorded here is run `40349268298`: 129 pages, successful engineering gates.
- `scientific-audit.md`, `equation-audit.csv`, and `figure-audit.csv` provide current context/registers, not blanket proof of scientific correctness or licensing.

## Reports and CSVs

| File | What it is | Status |
|---|---|---|
| [`APPA_LEDGER.csv`](APPA_LEDGER.csv) | Historical appendix-equation/claim register for the earlier appendix structure. | HISTORICAL |
| [`AUDIT_REPORT.md`](AUDIT_REPORT.md) | Narrative summary of the earlier engineering/scientific audit; not the current build status. | HISTORICAL |
| [`build-status.md`](build-status.md) | Current strict CI build state and verified engineering metrics. | CURRENT — AUTHORITATIVE BUILD STATUS |
| [`CROSSREF_HUMAN_CHECK.md`](CROSSREF_HUMAN_CHECK.md) | Manual human-review notes for the original Crossref metadata comparison. | HISTORICAL |
| [`CROSSREF_METHOD.md`](CROSSREF_METHOD.md) | Method and matching rules used for the original Crossref metadata pass. | HISTORICAL |
| [`CROSSREF_R3B_HUMAN_CHECK.md`](CROSSREF_R3B_HUMAN_CHECK.md) | R3B manual title/metadata review notes. | HISTORICAL |
| [`CROSSREF_R3B_METHOD.md`](CROSSREF_R3B_METHOD.md) | R3B Crossref request and comparison method. | HISTORICAL |
| [`CROSSREF_R3B_REQUEST_LOG.csv`](CROSSREF_R3B_REQUEST_LOG.csv) | R3B DOI request/HTTP response log. | HISTORICAL |
| [`CROSSREF_R3B_VERIFY.csv`](CROSSREF_R3B_VERIFY.csv) | R3B Crossref metadata comparison results. | HISTORICAL |
| [`CROSSREF_R3C_HUMAN_CHECK.md`](CROSSREF_R3C_HUMAN_CHECK.md) | R3C manual title/metadata review notes. | HISTORICAL |
| [`CROSSREF_R3C_METHOD.md`](CROSSREF_R3C_METHOD.md) | R3C Crossref request and comparison method. | HISTORICAL |
| [`CROSSREF_R3C_REQUEST_LOG.csv`](CROSSREF_R3C_REQUEST_LOG.csv) | R3C DOI request/HTTP response log. | HISTORICAL |
| [`CROSSREF_R3C_VERIFY.csv`](CROSSREF_R3C_VERIFY.csv) | R3C Crossref metadata comparison results. | HISTORICAL |
| [`CROSSREF_R3D_HUMAN_CHECK.md`](CROSSREF_R3D_HUMAN_CHECK.md) | R3D manual title/metadata review notes. | HISTORICAL |
| [`CROSSREF_R3D_METHOD.md`](CROSSREF_R3D_METHOD.md) | R3D Crossref request and comparison method. | HISTORICAL |
| [`CROSSREF_R3D_REQUEST_LOG.csv`](CROSSREF_R3D_REQUEST_LOG.csv) | R3D DOI request/HTTP response log. | HISTORICAL |
| [`CROSSREF_R3D_VERIFY.csv`](CROSSREF_R3D_VERIFY.csv) | R3D Crossref metadata comparison results. | HISTORICAL |
| [`CROSSREF_R3E_HUMAN_CHECK.md`](CROSSREF_R3E_HUMAN_CHECK.md) | R3E manual title/metadata review notes for the two requested records. | HISTORICAL |
| [`CROSSREF_R3E_METHOD.md`](CROSSREF_R3E_METHOD.md) | R3E Crossref request and comparison method. | HISTORICAL |
| [`CROSSREF_R3E_REQUEST_LOG.csv`](CROSSREF_R3E_REQUEST_LOG.csv) | R3E DOI request/HTTP response log. | HISTORICAL |
| [`CROSSREF_R3E_VERIFY.csv`](CROSSREF_R3E_VERIFY.csv) | R3E Crossref metadata comparison results. | HISTORICAL |
| [`CROSSREF_R3F_HUMAN_CHECK.md`](CROSSREF_R3F_HUMAN_CHECK.md) | R3F human review/arbitration notes for metadata records. | HISTORICAL |
| [`CROSSREF_R3F_METHOD.md`](CROSSREF_R3F_METHOD.md) | R3F Crossref request and comparison method. | HISTORICAL |
| [`CROSSREF_R3F_REQUEST_LOG.csv`](CROSSREF_R3F_REQUEST_LOG.csv) | R3F DOI/bibliographic request and HTTP response log. | HISTORICAL |
| [`CROSSREF_R3F_VERIFY.csv`](CROSSREF_R3F_VERIFY.csv) | R3F Crossref metadata status table. | HISTORICAL |
| [`CROSSREF_REQUEST_LOG.csv`](CROSSREF_REQUEST_LOG.csv) | Original DOI request/HTTP response log; metadata provenance only. | HISTORICAL |
| [`CROSSREF_VERIFY.csv`](CROSSREF_VERIFY.csv) | Original Crossref metadata comparison outcomes; not claim-level verification. | HISTORICAL |
| [`DECISIONS.md`](DECISIONS.md) | Earlier staged editorial/evidence decisions and their rationale. | HISTORICAL |
| [`DEFECT_STATUS.csv`](DEFECT_STATUS.csv) | Project issue/status tracker; distinct from the lost 24–25 October defect register. | CURRENT CONTEXT |
| [`equation-audit.csv`](equation-audit.csv) | Equation/model audit register with disposition, status, and remaining checks; not a universal derivation certificate. | CURRENT CONTEXT |
| [`figure-audit.csv`](figure-audit.csv) | Figure source, rendering, and provenance/licensing status register. | CURRENT CONTEXT |
| [`figure-contact-sheet.png`](figure-contact-sheet.png) | Overview sheet for the phase5 figure set, not the whole manuscript. | CURRENT OUTPUT |
| [`figure-render-inspection.txt`](figure-render-inspection.txt) | Structural/render inspection notes for the generated vector figures. | CURRENT CONTEXT |
| [`literature-evidence-matrix.csv`](literature-evidence-matrix.csv) | Inherited literature inventory/evidence matrix; not a claim-level certification or complete systematic search. | HISTORICAL INVENTORY |
| [`missing-source-pdf-links.md`](missing-source-pdf-links.md) | Historical source-access notes; publisher PDFs/full-text are not stored here. | HISTORICAL |
| [`OPEN_CLAIMS_LEDGER.csv`](OPEN_CLAIMS_LEDGER.csv) | Authoritative current open-claim register: 445 rows (A=13, B=138, C=294); a source lead is not proof. | CURRENT — AUTHORITATIVE OPEN CLAIMS |
| [`page-by-page-reconciliation.md`](page-by-page-reconciliation.md) | Earlier v1.0-to-v1.1 physical-page comparison (146-page build); now historical. | HISTORICAL |
| [`page-count-reconciliation.md`](page-count-reconciliation.md) | Earlier page-count/source-size reconciliation (146-page build); now historical. | HISTORICAL |
| [`phase-status.md`](phase-status.md) | Dated phase-end status snapshot from 2026-10-22. | HISTORICAL |
| [`PROCESS_LANGUAGE_INVENTORY.csv`](PROCESS_LANGUAGE_INVENTORY.csv) | Historical source-line inventory of process/status phrases; not a current gate or claim ledger. | HISTORICAL |
| [`quality-gates.md`](quality-gates.md) | Earlier quality-gate/overview review for the 146-page build; current result is in build-status.md. | HISTORICAL |
| [`R2_STATUS.md`](R2_STATUS.md) | R2-stage status snapshot. | HISTORICAL |
| [`R3_STATUS.md`](R3_STATUS.md) | Generated R3 evidence/status snapshot; conditional R3 workflows may refresh it. Not the current CI build status. | HISTORICAL SNAPSHOT |
| [`R3A_VERIFIED_REFERENCES.bib`](R3A_VERIFIED_REFERENCES.bib) | R3A bibliography snapshot associated with saved metadata checks. | HISTORICAL |
| [`R3B_CITATION_MAP.csv`](R3B_CITATION_MAP.csv) | R3B claim-to-source mapping snapshot. | HISTORICAL |
| [`R3B_VERIFIED_REFERENCES.bib`](R3B_VERIFIED_REFERENCES.bib) | R3B bibliography snapshot; metadata status does not establish claim verification. | HISTORICAL |
| [`R3C_CITATION_MAP.csv`](R3C_CITATION_MAP.csv) | R3C plan/map snapshot for the cited-source scope. | HISTORICAL |
| [`R3C_VERIFIED_REFERENCES.bib`](R3C_VERIFIED_REFERENCES.bib) | R3C bibliography snapshot. | HISTORICAL |
| [`R3D_CITATION_MAP.csv`](R3D_CITATION_MAP.csv) | R3D claim/section/source mapping snapshot. | HISTORICAL |
| [`R3D_VERIFIED_REFERENCES.bib`](R3D_VERIFIED_REFERENCES.bib) | R3D bibliography snapshot. | HISTORICAL |
| [`R3E_CITATION_MAP.csv`](R3E_CITATION_MAP.csv) | R3E mapping snapshot for the two requested methods/source records. | HISTORICAL |
| [`R3E_VERIFIED_REFERENCES.bib`](R3E_VERIFIED_REFERENCES.bib) | R3E bibliography snapshot. | HISTORICAL |
| [`R3F_CITATION_MAP.csv`](R3F_CITATION_MAP.csv) | R3F source/claim/section mapping snapshot. | HISTORICAL |
| [`R3F_SECTION_COUNTS.csv`](R3F_SECTION_COUNTS.csv) | R3F per-section source-count snapshot. | HISTORICAL |
| [`R3F_VERIFIED_REFERENCES.bib`](R3F_VERIFIED_REFERENCES.bib) | R3F bibliography snapshot. | HISTORICAL |
| [`R4A_DELETION_AUDIT.csv`](R4A_DELETION_AUDIT.csv) | Authoritative current record of removed manuscript text: 593 entries, zero NONE identifiers. | CURRENT — AUTHORITATIVE REMOVED TEXT |
| [`R4A_DELETION_AUDIT_NOTES.md`](R4A_DELETION_AUDIT_NOTES.md) | Method and interpretation notes for the current R4A deletion audit. | CURRENT CONTEXT |
| [`AUTONOMY_LOG.md`](AUTONOMY_LOG.md) | Timestamped actions and verification state for the autonomous R4B-AUTO work. | CURRENT PROCESS LOG |
| [`DECISIONS_FOR_AUTHOR.md`](DECISIONS_FOR_AUTHOR.md) | Narrow editorial decisions and unresolved author-facing choices. | CURRENT CONTEXT |
| [`MISSING_SOURCES.csv`](MISSING_SOURCES.csv) | References not located in the indexed material and safe next actions; absence is not inferred from uninspected archives. | CURRENT SOURCE-ACCESS REGISTER |
| [`R4B_SOURCE_FINDINGS.md`](R4B_SOURCE_FINDINGS.md) | Targeted source findings, page/equation anchors, source-identity limits, and remaining open items for R4B-AUTO. | CURRENT SOURCE FINDINGS |
| [`reviewer-simulations.md`](reviewer-simulations.md) | Synthetic reviewer simulations; not external peer review. | HISTORICAL / SIMULATED |
| [`scientific-audit.md`](scientific-audit.md) | Scientific audit narrative documenting checked derivations, limitations, and open questions; not a complete claim verification. | CURRENT CONTEXT |
| [`V-B3d-cross-term-check.md`](V-B3d-cross-term-check.md) | Focused derivation/check note for a B3d cross-term. | CURRENT TECHNICAL NOTE |
| [`version-provenance.md`](version-provenance.md) | Baseline/version history; header states current build, later sections preserve historical runs. | CURRENT + HISTORICAL PROVENANCE |

## Nested evidence and image folders

| Folder | Contents | Status |
|---|---|---|
| `crossref_raw/` | 81 saved initial-pass Crossref JSON metadata responses. | Historical metadata snapshot |
| `crossref_raw_r3b/` | 47 saved R3B Crossref JSON metadata responses. | Historical metadata snapshot |
| `crossref_raw_r3c/` | 4 saved R3C Crossref JSON metadata responses. | Historical metadata snapshot |
| `crossref_raw_r3d/` | 9 saved R3D Crossref JSON metadata responses. | Historical metadata snapshot |
| `crossref_raw_r3e/` | 2 saved R3E Crossref JSON metadata responses. | Historical metadata snapshot |
| `crossref_raw_r3f/` | 24 saved R3F Crossref JSON metadata responses. | Historical metadata snapshot |
| `v1.0-thumbnails/` | Seven contact-sheet images of the historical baseline PDF. | Historical visual overview |

The saved JSON is metadata evidence, not publisher full text. The 51 tracked third-party full-text files and 51 copies embedded in the legacy v1.0 ZIP were removed from the current tree; their path-only disposition table is [`../../archive/EXCLUDED_SOURCE_TEXTS.csv`](../../archive/EXCLUDED_SOURCE_TEXTS.csv).

## Interpretation limits

The R2/R3 maps, verification tables, bibliography snapshots, and status reports preserve the sequence of earlier work. Their labels such as “verified” describe their recorded scope at that time; they do not override the current open-claim ledger. The page-reconciliation reports describe an older PDF build. Use `build-status.md` for present engineering metrics and `scientific-audit.md` plus the ledgers for the current scientific/open state. The archived loss records are not recovery instructions.
