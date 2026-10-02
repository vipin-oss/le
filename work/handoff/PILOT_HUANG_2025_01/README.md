# Huang2025 CV/MCV3 bounded reference pilot

**Status: BLOCKED — PILOT, NOT FINAL VALIDATION.** Read PILOT_REPORT.html or PILOT_REPORT.md first.

## Scope

User authorized the single proposed Phase0A2reference-only pilot: t*=0.06,tau*=0.04,sourceB01Huang2025Table2/Eqs44–66/Fig5. No beta-Ga2O3/ellipse production/finalproject/journal approval. Exactsource/plan/input/referencehashes were frozen before numerical outputs.

## What ran

- Basic coupledPDE/constitutive/boundary/root/matrix/channel checks.
- Independentfinite-volume runs:CV800/1600/3200 plus a loggedpost-result6400extension;MCV3800/1600/3200.
- deHoog32/48/64 andCohen80 inversion at fixedsourceprobes.
- Existing-data diagnostics and figures/workbook/report.

Cohenfailed the pre-specifiedcrosscheck; firstdeHoogdriveralso abortedatidenticallyzeroboundary stress before documentedendpoint handling. Failedlogs/code andinitialmeshfailurepreserved. Sourceparameters/criteria unchanged. No additional solver run afterseconditerationfailedPASS. Thecomplete sourcegraph/fullprofile comparison remainsunexecuted.

## Files

- src/physics.py:source coefficients/transform,spatialmatrix,derivedequivalentCVchannels.
- src/fvm.py:independenttime-domainfinitevolumePDEmethod.
- run_basic_checks.py;run_fvm.py;run_inverse_probes.py;run_fvm_extension.py:executedscientificdrivers.
- summarize_existing_diagnostics.py;build_pilot_report.py:postprocessALREADYCOMPUTEDdataonly.
- versions/v01_before_endpoint_fix/:initialcode before correction;logs/P03_ERROR.txt andP03_INVERSION_PROBES.json preservefailedattempt.
- case_input.json,PILOT_PLAN_FROZEN.md,PLAN_FREEZE_RECORD.json,AUTHORIZATION.md:scope/source/criteria/provenance.
- data/:actualownnumericaloutputs,notexperimentaldata.
- reference_local/:protectedsourceimage/figure-derivedreferences;privateandnotredistributedincheckpoint.
- logs/:actualCPU/wall/RSS/code/input/source/environmentrecords.
- PILOT_RESULTS.xlsx:actualnumbers/statuses;plots showownexecutedprofiles/probes,notpublishedfigureoverlay.

## Reproduction / do not overwrite history

Environment actuallyused:Python3.13.14,numpy2.3.5,scipy1.17.1,mpmath1.3.0,matplotlib3.10.9,PyMuPDF1.28.2,openpyxl3.1.5. MATLAB/Octave were unavailable;userhardware isunknown. requirements.txt records the installedversions,not bundledthirdpartylibraries.

For a newly **authorized** reproduction/diagnostic:use a freshversionedworkingcopy andnewrunIDs/CPUledger;do not rerun automatically over archiveddata. Preservecase_input/planhashes. Numericalrunprovenance currentlyexpects the legitimatelyprovidedB01PDFatitsrecordedpath forchecksum; if relocating, changeonlythe sourcepath in a documentedcopiedinput and preserve/verify the sourcechecksum. OriginalsourcePDF isnotredistributedhere.

Commands actuallyused are in PILOT_REPORT.md. Thecurrentcorrectedprobe drivercompletes but reports scientificcrosscheckFAIL. Theoldinitialdriver is archived forfailuretrace,not to be mistaken for current code.

A fresh-environment reproductiontest hasnot beenperformed;no bitwise/reproductionguarantee isclaimed. Requirements/runtime/sourcepath and scientifictolerances mustbe checkedbefore reuse. Recoverycheckpoint isnot anoffline-complete literature/input orfinalsubmissionarchive.

## Next

STOP. User must authorize diagnostic-only follow-up or anexplicitloggedpost-resultmethod-plan revision. Do notdropCohenfailure silently, tuneparameters, generatebeta/ellipseproduction or manuscriptclaims from a falselydeclaredPASS.
