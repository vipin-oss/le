# CHANGELOG

## Repository history (this is real git history, not a reconstruction)

```
2026-10-03 2877ac1 Phase 11: generated docs, manifest ordering, file/dir shadow check; clean-room fixes
2026-10-03 031ba76 Phase 11: sidecar for the archive checksums; invariant content-level checksum
2026-10-03 3017658 Phase 11: verified companion-check invocation, md_to_pdf step documented, content-level checksum
2026-10-03 628509c Phase 11 (new): the complete reproducibility archive - builder, manifests, reproduction driver, restorer
2026-10-03 6ad7aff Phase 10: sidecar re-recorded against the current tree, with the reproduction recipe
2026-10-03 a6b2a4f Phase 10: add the author fill-in form to the repo and to the upload bundle
2026-10-03 a64d525 Phase 10: de-stale the author-input list against what Phases 9-10 actually delivered
2026-10-03 b48f96b Phase 10: changelog entry for the reproducible deposit archive and the bundle manifest fix
2026-10-03 2f30d05 Phase 10: deposit archive reproducible from the tree; bundle manifest covers PROVENANCE/README.txt too
2026-10-03 abb5265 Phase 10: deposit archive is a pure function of the tree; checksum of record updated
2026-10-03 8f4c4c0 Phase 10: deposit-package checksum of record, reproducible from commit 03921ee
2026-10-03 03921ee Phase 10: make the deposit package byte-reproducible from its commit
2026-10-03 e52fec4 Phase 10: deposit-package checksum refreshed for the current build
2026-10-03 91216d3 Phase 10: make the upload bundle deterministic in mtimes too
2026-10-03 bb62db4 Phase 10: checksum of record for the complete deposit package
2026-10-03 f47031f Phase 10: downloadable submission bundle IJHMT_submission_bundle.zip
2026-10-03 6214d96 Phase 10 follow-up: connection_audit resolves \graphicspath for figure references
2026-10-03 bc34fec Phase 10: self-contained LaTeX artwork, uploadable cover letter, author-side compile check
2026-10-03 f8a2bb1 Phase 9: refreshed final_consistency output after the phase commit (0 failures)
2026-10-03 64a9eee Phase 9: closeout - submission-grade figure renditions and the deposit package
2026-10-03 f62cb69 Phase 8 audit output: re-run after the phase commit (0 failures, clean working tree)
2026-10-03 65be82c Phase 8: final consistency audit, submission checklist, cover letter - programme complete (Phases 1-8)
2026-10-03 cce50c4 Phase 7: language, style, internal vocabulary and duplication - documents re-anchored to freeze 2026-10-03i
2026-10-03 bf64f34 Phase 6 manifest (4 files)
2026-10-03 f14bfbb Phase 6: Q1 (IJHMT/Elsevier) conformance restructuring complete - back matter, Data availability, AI disclosure
2026-10-03 c36830f Phase 6 note: mirror PDFs rebuilt with tools/md_to_pdf.py -i/-o after the renumbering; verify_pdf triage
2026-10-03 e4c9035 Phase 6 (part 1): Elsevier numbered-citation style end to end, reordered reference list, back-matter order, freeze re-anchored to 2026-10-03e
2026-10-03 f75eb5b Phase 5 note: the .tex cites by key while the Markdown carries literal numbers (settled in Phase 6/8)
2026-10-03 9b7751e Phase 5: literature audit and introduction repositioning (54 -> 55 references)
2026-10-03 4c000a5 Phase 4: figures and tables provened against the stored data; two real defects found and fixed
2026-10-03 33ea8f6 Phase 3 record: REPORT, FINDINGS_LEDGER, CHANGELOG, manifest; programme state moved to Phase 4
2026-10-03 6d62242 Phase 3 close-out: audit harness re-created and green; companion wording finished
2026-10-03 8b26bc8 Phase 3 (recover after sandbox reset): re-materialise the verified edits + regenerate all deliverables
2026-10-03 ca05217 Phase 2 reports: corrigendum on the dynamic peak-shift bound (0.958%, not 0.53%) - manuscript value already correct
2026-10-03 8623908 Phase 2 verification: V0 re-specified (27/28 PASS, 0 FAIL) with the coarse-grid value kept on record; ablations re-run at the production grid; matched-grid shape ratios; Bromwich validity qualified per pulse width; 1-ulp cross-environment re-solve; freeze submission_2026_10_03b
2026-10-03 a596b43 Phase 1 audit: 43 findings (15 A / 22 B / 6 C), no artifact changed; resumable program state
2026-10-03 adc4988 00_Project_Control/CHANGELOG: record the published download artifact (dist/ zip, tag final-2026-10-03)
2026-10-03 08d4285 dist: publish RESEARCH_PROJECT_FINAL.zip (2026-10-03 build) for download
2026-10-03 7bad2dd connection_audit: report 'branch on GitHub, ahead of main by N' once the branch is pushed
2026-10-03 e067b3a Provenance pass: deposited code freeze made current; paper <-> repo connection audited
2026-10-02 18368e9 Merge pull request #1 from arena/01a0f67f-le
```

## What the history does not cover

- Everything before 2026-10-01 is preserved as documents, not as commits: the project arrived as
  `le.zip` and its internal logs (`work/handoff/CHANGELOG.md`, `DECISION_LOG.md`,
  `CURRENT_PROJECT_STATE.md`, archived at `01_PROGRAM/handoff_baseline/`) are the record for that
  period. So: for the hand-off/pilot work, HISTORICAL CHANGELOG NOT AVAILABLE as version control -
  the narrative logs are available and shipped.
- The scientific change log of the paper itself (what was corrected and when) is in
  `07_DOCUMENTATION/corrections_log/CORRECTIONS_LOG.md` and the phase reports under
  `07_DOCUMENTATION/phases/`; the parameter/figure/manuscript level changes are summarised in
  `07_DOCUMENTATION/phases/Phase_10_Submission_Package/CHANGELOG.md`.
- Code-level versions are hash-based, not commit-based, by design: see the twelve
  `CODE_FREEZE_*.json` manifests in `01_PROGRAM/freeze/` (latest: `submission_2026_10_03j`).
