# Equation to code / result map — pilot only

Source:B01Huang2025,DOI10.1007/s10483-025-3280-7. SourcePDFunchanged. No newtensor/physicalmodel isproposed.

| Source/model identity | Code | Executed evidence / limitation |
|---|---|---|
| SourceTable2/SIinputs;gamma,beta2,b,g | case_input.json;physics.derived_np;MPcoefficientbuilder | Sourcevaluesfixed;alphaunitinterpreted1/K fromdimensions. No k/SIspace/timeconversion guessed. |
| Table1CV/MCV3M,N | physics.operator | Two approved laws only. No other10sourcevariants implemented. |
| Eqs58–59coupledspace/temperatureequations | physics.roots_np,_mp_coeff;laplace_np/mp | Sourcequadratic decayingmodes; testednormalizedPDEresiduals. |
| SourceEq66modeamplitudes | laplace_np,laplace_mp | Boundary/stresssourcechecks andactualinversionprobes. Notphysicalvalidation. |
| Independentfirst-orderspatialPDEmatrix | laplace_matrix_np | DoesnotuseEq66; testedtransformagreement on40samples. |
| MCV3rationalidentity / twoCVchannels | cv_channels;transport;run_basic_checks | Independentlyderivedequivalentimplementation undercompatiblezerohistories,not anewlaw;identitytested. |
| SourcePDEfirst-ordertimeform | fvm.solve | Independenttime-domainPDEevolution,doesnotcallEq66. |
| Freeheatedendtheta1/sigma0 | fvm incomingcharacteristicconstraints;Eq66tests | ExactstatedBC. Analyticstress0endpointspecialcase correctsdeHoogzero-transform Q-Ddegeneracy;interior/tailnotclipped. |
| Halfspacecausalbound | transport/front_positions | L1rightboundary not reachedbyt.06;recordedderivedspeeds/mask. |
| qjrelaxation +transport | fvm.solve | ExactsourceStranghalfsteps,MUSCLMC/SSPRK2,CFL.45;7actualruns. |
| Sigma=beta2strain-btheta;u recoveredwithundisturbedfarend | fvm.solve | Actualstorednumericaloutputs;independentprobecomparisonpost-failurediagnostic only. |
| Numericalinverse | physics.inverse;run_inverse_probes | deHoogprobeconverges;Cohen80FAIL. No fullprofile/referenceagreementdeclared. |
| SourceFigure5graphicalinputs | prepare_reference.py;reference_local | Preparedbeforemodeloutputs;comparisonNOT_EXECUTED because gatefailed. Private,notexperimental. |
| Compute/provenance | common.Stage;logs/CPU_LEDGER.json | ActualstageCPU/wall/RSS/code/input/sourcehashes;noGPU. |
| Report / plots | summarize_existing_diagnostics.py;build_pilot_report.py | AlreadycomputeddataonlyafterSTOP;noadditionalmodelsolve. |

Version01initialerror/correction records preserved. The limitedimplemented/executedpilotevidence does not certify anewmaterialprediction,wholesourcemodeladmissibility,novelty,journalfit orsubmissionreadiness.
