# Version and provenance record

**Current builder branch:** `arena/b5e608f8-le`<br>
**Current working version:** phase5 v1.1; a 130-page strict CI build passed in run `40435990048` on source commit `893c46f` (2026-10-27); output commit `b4257e0` publishes the current PDF and contact sheets.<br>
**Active source:** `phase5/master/`, with portable table inputs in `phase5/master/tables/source/` and figure assets in `phase5/master/figures/source/`.<br>
**Baseline:** the v1.0 source/PDF in `phase4/` and `phase5/master/v1.0-baseline.pdf` are historical comparison artifacts; phase4 is also read by current audit/reconciliation scripts.

The dated run IDs, branches, and 146-page v1.1 metrics in the sections below document earlier states. They are retained as provenance, not current build status. For current metrics use [`build-status.md`](build-status.md).

## What the baseline represents

- `phase4/manuscript/main.pdf` and `phase5/master/v1.0-baseline.pdf` are byte-identical, SHA-256 `b03dc426046a1473d3d6cf1088f9fc115c7103b4786c4eb2389ab968f640c636`; PyMuPDF reports 161 pages, producer `pdfTeX-1.40.25`, and embedded creation time `2023-11-14T22:13:20Z`.
- The baseline PDF was published into repository history in commit `00908ce` (“chore: publish compiled manuscript PDF (build 32)”, 2026-10-21). The CI workflow sets `SOURCE_DATE_EPOCH=1700000000`; the embedded PDF timestamp is therefore not evidence of the actual compile date.
- GitHub run `39654760555` is associated by the committed diagnostics with TeX Live 2023 and has source head `d4a9dafc79149455e7008845dc2a5a759dca3e10`. The latest diagnostics commit identifies successful run `39716768990`. The detailed signed GitHub run-log download failed with EOF in this environment, so this entry does not certify every diagnostic or artifact from those runs.
- The repository PDF is **not** the separately described 170-page/pdfTeX-1.40.29 PDF. That external file was not present in the workspace. Do not assert that the 161-page baseline disproves a missing-figure symptom in the unavailable 170-page file.
- A thumbnail survey of all 161 baseline pages is stored under `phase5/reports/v1.0-thumbnails/`. It shows rendered content and figures at overview scale, but it does not constitute final-size proofing. Several appendix-table pages show overflow/fragmentation and should be corrected in the working source.

## Working-copy provenance

The phase5 LaTeX source was copied from `phase4/manuscript/`; the original phase4 source is preserved. The manuscript initially referenced PDF figures while the source repository held SVGs. The 18 inherited SVGs were copied to the phase5 working tree and rendered with the pinned npm vector converter into corresponding PDFs. `master/figures/rendered/` retains pre-repair phase4 SVG snapshots for comparison; despite the directory name these are SVG sources, not rendered PDFs. The generated PDFs, mirrored SVGs, and eight editable tables are inside the phase5 manuscript package so relative paths are portable. SVG authorship/licensing provenance remains undocumented and is flagged in `reports/figure-audit.csv` rather than assumed.

Repairs in `phase5/scripts/repair_source.py` and subsequent source edits apply to phase5 only. The full file-by-file provenance, changes, and unresolved claims are documented in the phase5 scripts and audit registers. `../../archive/deliverables/phase5-v1.1-source-audit.zip` is a source/audit snapshot only; it contains no compiled phase5 PDF.

## Do not conflate these states

1. **v1.0 repository baseline** — 161-page tracked PDF; exists and was thumbnailed.
2. **Other reported PDF** — said to be 170 pages with pdfTeX 1.40.29; not available for inspection.
3. **phase5 v1.1** — versioned source, repaired relative paths, 18 generated PDF figures, static scans, and strict CI build. Strict CI run `39753968114` passed on manuscript/workflow commit `7c125de25cb0d3fd951152bdad74931cff3c55a6`; its output PDF and four 100-dpi contact sheets are committed under `phase5/build_outputs/` by follow-up commit `586181b06fc626c17ac1b5ae42e85c3cf0d23b7d`. The sheets were reviewed at overview scale; full-size proofing and science audit remain distinct.

The inherited build workflow's green status is not substituted for a phase5 compile: the old workflow compiled the phase4 tree and suppressed failures with `|| true`. The replacement strict phase5 workflow does not suppress command failures; its strict build gate passed first in run `39748215109`; runs `39750456893` and `39753968114` also passed. Requested Part 1 output/reconciliation checks are complete; 416 underfull hboxes are recorded with no obvious contact-sheet-scale damage. Part 2 remains unstarted.
