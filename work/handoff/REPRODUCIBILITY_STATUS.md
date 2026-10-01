# Reproducibility status

Date:30 September2026.

New scientific source code/environment:NOT_STARTED.
Reference-case reconstruction:NOT_RUN.
Validation reproduction:NOT_RUN.
Convergence/error-study reproduction:NOT_RUN.
Principal result/figure/table reproduction:NOT_RUN.

Input reading and source-screening provenance:available in recorded manifests/logs. Metadata/workbook artifact construction:RUN_SUCCESS when BUILD_REVIEW_ARTIFACTS.py completes, not scientific numerical reproduction.

RECOVERY_PRE_EXECUTION_REVIEW_01.zip is a notes/control checkpoint. It includes canonical master, current control/state, screening tables/logs and prior summaries/manifests. It deliberately excludes third-party PDFs/images/full extracted paper texts and original manuscript/code archives. Inputs remain accessible in the shared workspace through recorded paths/URLs/checksums; the ZIP is NOT an offline-complete source/input or final-research package. Third-party redistribution rights must be checked before a future final archive.

## alit source-review update
All3requestedPDFsavailable atrecordedpaths/hashes; source-case equation/conditionnotes andlocalprintedtableinputsavailable. Authorcode/rawcoupledprofilearrays notsupplied. Numericalreference/convergence/principalresultreproduction NOT_RUN. Newnotescheckpoint deliberatelyexcludes protectedsourceinputs/fulltexts/images/completetabletranscriptions. No offline-complete/finalresearcharchive claimed.

## Executedpilotupdate
Pilotcode/inputs/frozenplan/environment/code/sourcehashes/runcommands/actualoutputs/failuresprovided. Actualbasic/FVM/inversionrunsrecorded;wholepilotacceptanceBLOCKED. No fresh-environment reproductiontest performed. Fullprofile/sourcegraphvalidation/principalnew-researchresultreproductionNOT_EXECUTED. Recoveryincludesownnewnumericalartifactsandcurrentcontrol/priornotes;protectedsourcePDF/images/figure-derivedreferencefilesexcluded. SourcePDFatrecordedpathneededforcodeprovenance/referencedata,notredistributed.


## 30 September 2026 FINAL reproduction commands (pilot complete)
```
cd /home/user/PILOT_HUANG_2025_01
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_basic_checks.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_fvm.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_inverse_probes.py   # Cohen FAIL preserved
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_fvm_extension.py    # CV6400
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_source_and_limiting_cases.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python summarize_existing_diagnostics.py
python build_pilot_report.py   # legacy blocked report
# Final report: PILOT_REPORT_FINAL.html (self-contained, base64 figure)
```
Notes: (i) Cohen-80 output is a retained FAILURE, not physics. (ii) source-figure comparison requires reference_local/ (private, excluded from recovery zip; hash manifest DIGITIZATION_PROVENANCE.json). (iii) hardware 2-CPU sandbox; raw timings bounded, not portable.
- 2026-09-30 PROJECT_CRYSTAL_GEOMETRY_01 FINAL PACKAGE: environment captured (data/ENVIRONMENT.json: Python 3.13.14 / numpy 2.3.5 / scipy 1.17.1 / matplotlib 3.10.9); code freeze (data/CODE_FREEZE.json, sha256 of 8 code files, change-rule stated); single-script analysis reproduction verified (double-run IDENTICAL); RECOVERY_CRYSTAL_GEOMETRY_01.zip + sha256 manifest (code/inputs/scripts/logs/per-run npz/figures/manuscript; NO third-party PDFs — paths/hashes only where sources are external). Compute totals recorded in COMPUTE_STATUS.md (~0.6 CPU-h).
