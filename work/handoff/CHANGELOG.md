# Changelog

## 2026-09-30 — Control/evidence update
- Stored user-supplied MASTER_PROMPTv2.1 plus version/date/checksum; prior v2.0 working-control text is superseded, historical reports retained.
- Added a bounded pre-execution journal/reference/evidence screen, workbook and logs.
- Read full5-page Klimm material-characterization source and2019 APL correction text; no numerical model was executed.
- Recorded2025 primary SCImago category quartiles and current publisher indexing lists separately from unverified current JCR quartiles.
- Held uncorrected tensor import and broader physical-prediction claims pending source/mapping/data.
- Created a notes/control recovery checkpoint, excluding original/third-party source inputs.
- No original bibliography, manuscript, code, model equation, parameter set or numerical result was altered.

## 2026-09-30 — alit source-review checkpoint
- Preservedalit.zip/3PDFswithhashes;matchedDOIs,44documentpages.
- Read relevantfull-source equations/cases; sourceaccessB01–B03nowresolved. Priorblockedpreviewreportsretainedashistory.
- Addedcaseblueprints,operatorindex,manualanalyticalsourcechecks andprivateprintedtablereferences; not newsolverresults.
- RecordedMGN2internalmismatch,alpha-unitdisposition and restrictedkernelreductions/DCnormalization. No originalPDF/model/code modified.
- Updatedlateststate/currentstatuses; proposedpilotnotapproved/run.
- Recoverycheckpoint excludesprotectedinputs/fulltext/images/completetableextractions.

## 2026-09-30 — ExecutedHuangreferencepilot/BLOCKED
- Prespecifiedplan/input/source/referencehashesfrozenbeforeoutputs;sourcePDEparametersretained.
- Implemented/executed40basicchecks,7FVMruns andinversionprobe/refinement/algorithmchecks.
- InitialdeHoogzero-transformerror andCVrefinementfailurepreserved;analyticendpointandpost-result6400meshcorrectionslogged.
- Cohen80numericalcrosscheckFAILaftercorrectediteration;frozengatenotpassed;STOPaftertwoiterations.
- Createdowncomputeddiagnosticplots/tables/recoveryevidence;sourcegraph/fullprofileacceptanceNOT_EXECUTED.
- No beta/ellipseproduction/sourcePDF/FEM4originalalteration orsourceparameterfitting.

## 2026-09-30 — PROJECT_CRYSTAL_GEOMETRY_01 operator correction chain (D014)
SUPERSEDED (preserved as history): data/VERIFY.json old results (V0–V5 PASS, V6/V7 FAIL on composed-D@D operator + wrong domain); all solver outputs of Phase 5–7 smoke tests.
FIXES: (1) conservative flux-form operator src/cg_ops.py (parity null mode of composed D@D documented in logs); (2) FD-computed metrics (commuting mixed partials → patch identity exact); (3) eta-half uy deta sign; (4) grid domain R=80·a (was absolute 80 m with a=1e-8); (5) V6 exact-solution units; (6) J-row scaling + row equilibration (SI round-off); (7) hysteretic damping η_d=0.05 dynamic-only (undamped finite-domain resonances), sensitivity {0.02,0.1} planned.
RE-VALIDATED (logs/verify_rerun_v3.log, 403 CPU-s): V0 PASS, V1 PASS, V2 PARTIAL (med-fine 2.35% circle / 6.80% ellipse — per plan: documented grid uncertainty + 192×96 confirmatory spot checks), V3 PASS 6.3e-14 (machine), V3b PASS, V4 PASS, V5 PASS 1.1e-7, V6 PASS 9.5e-6, V7 PASS 0.68%.
Code freeze pending production; run_production.py matrix pre-registered (DECISION_LOG D015).
