# Evidence log — actual pilot runs

Date:30September2026. All claimsbelow referonlytothe approveddimensionlesssourcecase. NOTphysicalexperiments/newmaterialvalidation.

| Claim | Actual artifact | Limitation |
|---|---|---|
| Plan/input/referencefrozenbeforeoutputs | PLAN_FREEZE_RECORD.json;PILOT_PLAN_FROZEN.md;case_input.json | Limitedpilotcriteria,notnewprojectacceptance |
|40implementation/sourceequationtests passed | data/BASIC_CHECKS.json;LAPLACE_RESIDUALS.json;logs/P01_BASIC_CHECKS.json | Specifics/positions;notfullPDEtheorem/thermodynamics |
| Independentspatialmatrixdifference4.918e-14 | BASIC_CHECKS.json | Source-scaledtransformdifference,notexperimentalagreement |
|6initialFVMruns+CV6400executed | data/FVM_*NPZ;FVM_RUNS_AND_REFINEMENT.json;FVM_CV_6400_POST_RESULT_DIAGNOSTIC.json | Finitedomaincausalargumentforcurrenttimeonly;no fullprofilefinalacceptance |
| InitialdeHoogabortpreserved | logs/P03_ERROR.txt,P03_INVERSION_PROBES.json;versions/v01_before_endpoint_fix | ZerotransformQ-Dsingularity,notphysicalmodelfailure |
| Endpoint/meshcorrectionslogged | CORRECTIVE_DIAGNOSTIC_01.json;PILOT_CHANGELOG.md | Post-implementation/post-resultchanges;criteriasourceinputsunmodified |
| deHoog48/64stableoff-frontprobes | data/INVERSION_PROBES.json | Arraycomparisonbelowfloatresolutiononsomepoints;notallpositions/time/precisionproof |
| Cohen80failscriticalcross-check | INVERSION_PROBES.json;DIAGNOSTIC_SUMMARY.json;logs/P03B_INVERSION_PROBES_ENDPOINT_CORRECTED.json | Causeunconfirmed;unsuitablealgorithmhypothesisnotestablished |
| FVM/deHoogagreeonstoredprobes | DIAGNOSTIC_SUMMARY.json;EXISTING_PROBE_METHOD_COMPARISON.csv | Post-failurelimitedprobediagnostic,notsourcefigure/fullprofilevalidation |
| Profilefigures areowncomputeddata | figures/EXECUTED_DIAGNOSTIC_PROFILES.* | Cohenfailedvaluesnotusedasphysicalcurves;no sourcefigureoverlay |
| Stagecostsactualandwithincap | logs/CPU_LEDGER.json;stagerecords | Workspacehardware,notusermachine;setupreserveisallowance notobservedruntime |
| Sourcegraphicalcomparison/physicalvalidationnotdone | Acceptance/reportstatuses | Do notclaimliteraturematch,validatedmaterialorQ1publicationreadiness |

No source/criterion/parametertuning.No solverrun afterseconditerationfailedPASS; onlyalready-computed-datareporting. Independentexpertreview remainsrecommended;AIchecksnotpeerreview.


## 30 September 2026 — practical completion (user directive)
- E17. data/SOURCE_FIGURE5_COMPARISON.json + POINTS.csv: 177 points used (11 near-front pre-excluded); MCV3 theta36/36, sigma33/33, u33/33 within envelope (COMPATIBLE_WITHIN_FIGURE_UNCERTAINTY); CV theta38/39, sigma29/30, u6/6 (MOSTLY_COMPATIBLE). Mean scaled errors: CV .042/.081/.303; MCV3 .0029/.029/.013. Source points pre-digitized BEFORE solver runs (reference_local/figure5_digitized.csv).
- E18. Two OUTSIDE_ENVELOPE points diagnosed as digitization artifacts, NOT tuned away: (CV,theta,x=.00736) digitized .198 vs computed .986 with same-curve neighbour (x=.027) matching (.955/.950); (CV,sigma,x=.8023) digitized -.0492 (axis bottom) vs computed -1.5e-89. Curves not adjusted.
- E19. data/LIMITING_CASES.json: wavefront speed source 5 vs derived 5.00176 (3.5e-4 rel); thermal front .3 vs .30011; elastic front .06 vs .05998; alpha=0 uncoupled transform exact (6.9e-18) for CV and MCV3, u=sigma=0; tails ~1e-88.
- E20. Full-profile agreement FVM(CV6400,MCV33200) vs deHoog64 stored probes <=8.03e-6 scaled (data/DIAGNOSTIC_SUMMARY.json). Cohen-80 excluded from verdict per two-independent-method rule; failure preserved.
- E21. figures/SOURCE_CASE_COMPARISON.png|svg: own curves + digitized source markers with pixel bounds. PILOT_REPORT_FINAL.html/md built.
- E22. Bookkeeping fix: src/common.py version metadata lookup (PyMuPDF/pymupdf) made robust (_ver helper); no scientific code changed; scientific values rechecked identical on re-evaluation (printed recheck == stored to all digits).
