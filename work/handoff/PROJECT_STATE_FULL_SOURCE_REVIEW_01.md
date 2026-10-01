# Latest recovery state — full-source benchmark review01

Date:30 September2026 (Asia/Calcutta). Canonical user master: `/home/user/MASTER_PROMPT.md`, FINAL MASTER PROMPTv2.1, sections0–90. Previous cumulative state: `PROJECT_STATE_PRE_EXECUTION_REVIEW_01.md` (historical, source access was then blocked).

## Current task / approval boundary

User asked the assistant to find good published reference/limiting-case routes before execution, requested exact PDF titles/DOIs, then supplied `https://github.com/vipin-oss/BFS-FEM-MATLAB/blob/main/alit.zip`. This authorizes receiving/reading those sources and assessing/reconstructing source-case specifications, not automatic simulation/production or final topic approval.

Current task:requested full-source reading/benchmark compatibility screen. **Source access RESOLVED; scientific execution/readiness PARTIAL.** No complete formal Phase0A-1/0A-2/1/2 claimed. Numerical solver/pilot/production NOT_RUN. No final research direction/model/material/journal, production compute or formal acceptance plan approved.

## User-confirmed aim

Recent heat-conduction model + different materials; BOTH crystal/material symmetry and geometric symmetry; COUPLED THERMOELASTIC RESPONSE. Provisional agent idea:monoclinic beta-Ga2O3/circular-elliptical cavity with2025 modified CV/GN family. Still not selected/approved; novelty/significance unconfirmed. A source-benchmark copper case does not select copper as the new research material.

## Preserved prior work

- Published workbook48records/47distinct suppliedDOIs, not47independentlyverifiedpublications. IDs36/41duplicate; ID47proposed DOIcorrection10.1016/j.jppr.2026.02.007. Originalunchanged.
- Eight representativepublishedPDFs plusall8suppliedunpublishedmanuscripts read atsection level, not comprehensiveequation audits. PreviousCrossref12successes/36rate-limits unresolved.
- Corpus already covers thermal/wave/memory/MGT/KG models; gradient/BFS/nonlinear/electromechanical topics; GKidentifiability; QCphason-class discrimination. Futureoverlap includespublishedANDunpublishedwork.
- `paper_springer.pdf` authorattributionto userunconfirmed (AnnuRani/M.S.Barak ontitlepage).
- FEM4sourcepackage inspected:89coreMATLABfiles,113total;static2D C1BFSmechanics+C0potential,36elementDOFs. No existingthermal/transient solver certified; originalunchanged/unexecuted. Sourcehcritfactor-two note preserved.
- Threejournalfamilies had2025primarySCImagoQ1category checks andpublisherSCIE/Scopuslists inpreviousscreen. Not primarycurrentJCRquartile/independentMJLcertification. No finaljournalselection/ranking.

## New input and actual actions

- `alit.zip`:1,274,111bytes;3PDFs;1,544,618uncompressedbytes.
- Git blob/API + actual content match: `70586950b70674a0f5365341cb2f2f1fc7929a9d`.
- Originalarchive: `/home/user/RESEARCH_PROJECT_INPUT/LITERATURE/USER_SUPPLIED_BENCHMARKS/alit.zip`.
- ExtractedPDFs: `.../USER_SUPPLIED_BENCHMARKS/ALIT_01/`.
- Exacttitles/DOIsmatched B01/B02/B03.
- Pages:B01=18,B02=11,B03=15;44documentpages, not44individuallyauditedproofpages.
- Nativepage-markedtextsextracted; relevantfull-sourceformulation/BC/IC/method/input/example/result/conclusionsectionsread. Keyequations/material/operator/tables renderedandread.
- Limitedmanualanalyticalsourcechecks performed; no numericalfield/inversion/benchmarktested.
-64printedB03tablereferencevalues transcribed/visuallychecked, notindependentlyrecomputed or measured.
-2additional searches:focusedHuangcorrectionquery(noverifiedrelevantmatch;notproofnoneexists) andRef52metadata/DOI.
- OriginalZIP/PDFs/sourceequations remainunchanged; noauthorcode/rawcoupledprofile/experimentaldatasetinarchive.

## Exact source cases now known

### B01 — Huang2025, DOI10.1007/s10483-025-3280-7

ActualsourceTable1:CV,sixMCV,GN,fourMGNrows (12nominalrows, not12certifiedindependentkernels). Classicalelasticity + temporalheatrelaxation, notMindlinmechanicalgradientmodel.

Primaryproposal:Figure5 dimensionless 1Dsemi-infinite longitudinalcase, `t*=0.06,tau*=0.04`, withCVparent andMCV3candidate.

- Atx0:sigma=0,theta=T0H(t); dimensionless theta*=H(t*).
- Atinfinity:u,theta decay.
- Sourceuses LaplaceM,N withoutinitialterms; completehigher-orderhistorylist notexplicit inrelevantsection. Record causalzero-prehistory/compatiblememory as reconstructionassumption beforecode.
- Table2:lambda77.6GPa,mu38.6GPa,alpha1.78e-5(unitheaderissue),rho**8945kg/m3**,cE**381J/(kgK)**,T0=293K.
- `rho*u_tt=(lambda+2mu)u_xx-gamma*theta_x`; `sigma=(lambda+2mu)u_x-gamma*theta`; `k*N*theta_xx=M*(gamma*T0*u_xt+rho*cE*theta_t)`.
- **Macts onstrain-ratecouplingANDtemperature-rate.**
- `gamma=(3lambda+2mu)alpha`; normalizationEqs53–56; `g=gamma/(k*n2)=gamma/(rho*cE)`. Untabulatedphysicalk doesnotblockdimensionlesscase, butSIconversionneedsit.
- MCV3 Eq21/Table1: `q+3tau*q_t+tau^2*q_tt=-k*gradtheta-k*tau*gradtheta_t`.
- Decayingroots/amplitudes inEqs63–66; rootsneedRepositive/degeneratecases handled. Surfaceamplitudeidentity manuallychecked theta_hat=1/s,sigma_hat=0.
- ReferenceFig5curvesnotdigitized/rawarraysnotprovided. MATLABinversioncitationBrancik1999,code/settingsnotprovided. No reproducedcurve/error.
- Fig4MCV1comparisonusesRef52, notexperiment; exacttime/tau notfullylistedthere. Ref52DOI10.1016/j.euromechsol.2020.104043metadata confirmed;fulltextnotread. NotrequiredforfirstexplicitFig5assessment.

### B02 — Bagri/Eslami2007, DOI10.1016/j.ijmecsci.2007.04.004

Use**LS cylinder**asfirstcurvedcommon-lawreference, notdirectGL/GNIIoverlay.

- Isotropic/homogeneouslonghollowcylinder,planestrain,m1,a1,b2.
- Sourceillustrativedimensionlessc1=1,c2=0.535,epsilon=0.02,cK=1,tau0=4. Not measured/named copper; do notreuseB01materialinstead.
- f(t)=1-(1+100t)exp(-100t),smoothedsteptoward1,notpulse.
- Inner:q_r=f(t),u=0 (fixed). Outer:theta=0,sigma_rr=0 (free).
- SourceEq27explicitzero u,u_t,theta,theta_t,q.
- f_hat=10000/[s(s+100)^2]. LaplaceBesselsolutions43–53;Figs2–4referenceprofiles,notrawtables.
- Innernormalopposesincreasingr;fluxsignmatters.
- CV/classicalstress/energycommonlawwithB01checkedanalytically; fieldsnotidenticalbecausegeometry/BCs/scalesdiffer.
- DisplayedGNplotsaretypeII(k=0);B01GNhas typeIIIstructurek*=k/tau. Nontrivialjoint/independentlimitneeded. GLchangesstress/entropytemperature-rateterms notinnativeB01law.
- No sourcereproductionorerrorcomputed. Exactcoupledcharacteristicroots/uncertaintymustguidefrontchecks,notforcinguncoupledspeedinterpretations.

### B03 — Gordeliy2008, DOI10.1016/j.ijheatmasstransfer.2007.10.021

- Heat-onlyclassicaldiffusionT_t=laplacianT;initialincrement0;unboundedexterioroftwocircles.
- Centredistance rho scaleslength; t=kappa_diffusivity*time/rho^2.
- R2=.3;R1=.2/.3/.5/.6. L2temperature0;L1either1(Table1)orcosphi1(Table2).
- A/Bspecifiedlocalpolarpositions; derivedconsistentglobalconventioncentres(0,0)/(1,0)givesA(-1.5,0),B(2.5,0).
-64printedvalues,t=1/10/100plussteady, transcribedlocally.
- ExampleSOURCE_REPORTED_COMPUTATION(notourresult):Table1,R1=.2,R2=.3,A,t1,T=.15440.
- Epsilon1e-6or1e-5nearclosecavities is chieflyBCdiagnostic;5decimalprinting/source/numericaluncertaintyneedseparatebudget,notuniversal5percentpass.
- Do notreplacebounded-infinitysourceproblemwithfinitecoldouterboundaryatlate/steadytimes. NegativecosinecaseincrementsnotnegativeKelvin.
- AuthorCOMSOL/literaturecomparisonis mathematicalverification,notexperiment. Notcoupledstressvalidation.

## Limited analytical/source quality findings

Status**ANALYTICALLY_CHECKED withconditions**, not fullprojectverification/admissibility:

1. Equal-unit/compatible-historyMCV5 kernel reducesCVwith2k;MGN3reducesGNwithk/2. Unequalnetworkparameters/arbitraryextraICs outsideidentity. Nofirst-discoverynoveltyclaimed.
2. MCV1/2are restrictedfirst-orderrelaxationfamilies relatedbyconsistentphysicalk/taureparameterization;axis/timeconversionsmustmatch.
3. DCconductivityCV/MCV1/3/6=k;MCV2/4/5=2k. GN/MGNhaveDCpole. Reproducepublishedcasesfaithfully; matched-static-conductivity controls separatelylogged.
4. **MGN2printedEq36**doesnotreduceEq37/Table1forequalparameters. Visualread/manualliminationEq35confirmsinconsistency. ACTION_REQUIRED ifbranchselected;nosilentfix/noofficialerratumclaimed.
5. Table2alphaunitm/Kstyleinconsistentwithstresscouplingrequiring1/K. Proposedsamevalue1.78e-5as1/K,recordbeforeimplementation;notnewmeasurement.
6. Sourceoperatorsmodifytime-order, notautomaticstrain-gradientspatialphysics/C1requirement.

## Scientific status / decisions

- Newprojectdirection/material/modelbranch/journal/evidenceroute:NOT_APPROVED.
- Novelty/significance/closest-five/currentgap:NOT_COMPLETED/UNCONFIRMED.
- Newtensor/anisotropiclaw:NOT_DERIVED;do notsubstitutetensorsintoscalar conductivityratios blindly.
- FormalScientificAcceptancePlan:NOT_CREATED (Phase1unapproved).
- Numericalverification/convergence/sourcecasereproduction:NOT_STARTED / NOT_RUN.
- Limitedsourcealgebrachecks:doneasabove;notcodeverification/globalproof.
- Physicalvalidation:NOT_STARTED;new-materialtransientT/stressevidenceunestablished. PropertysourceB04/B05doesnotvalidatenewmodelbycopiedinputs;APPLICABLE—EVIDENCE_UNAVAILABLEremainsprovisionalforpredictivenew-materialclaims,notNOT_APPLICABLE.
- Scientificsolvercode:NOT_IMPLEMENTED. ExistingFEM4originalunchanged/unexecuted.
- Scientificpilot/productionruns:0. Source/data/documentprocessingonlyexecuted.
- Userhardware/licences/preferredruntime/experimentaccess/deadline:UNKNOWN.

## Exact next action / proposed pilot (not approval)

STOPandwaitforexplicitnextscoped-phaseauthorization. NoextraPDFneededforfirstdimensionlessHuangFigure5CV/MCV3assessment.

PossibleauthorizedPhase0A2feasibilitypilot:referencecasesONLY, firstB01CVparentthenMCV3;freezeunit/history/inversion/diagnostics/referenceuncertaintyplanbeforeexecution. Proposedmaximum0.5CPU-hour,noGPU,50MBnewpilotdata—notobservedruntime/estimate/approval. LabelPILOT—NOTFINALVALIDATION. No beta-Ga2O3/ellipseproduction ormanuscript.

Formalresearchdirection/material/geometry/acceptance/method/productiongatesremainv2.1. ProductionaboveANY4CPU-hours/1GPU-hour/5GBrequiresapproval;sourceuploadisnotexecutionauthorization. Aftertwosubstantivecriticalsciencefailuresstopwithblocker;nonewcriticalnumericalphasehasbeenattemptedyet.

## Recovery artifacts

- RootMASTER_PROMPT.md/version/date/provenance;rootDECISION_LOG.md,CHANGELOG.md,VALIDATION_STATUS.md,COMPUTE_STATUS.md,REPRODUCIBILITY_STATUS.md,RESEARCH_PROFILE.md.
- `/home/user/BENCHMARK_SOURCE_REVIEW/ALIT_01/FULL_SOURCE_REVIEW.md` mainreport.
- ANALYTICAL_SOURCE_CHECKS.md;SOURCE_BENCHMARK_READINESS.xlsx;BENCHMARK_CASES.json;MODEL_OPERATORS.csv/.json;SOURCE_ISSUES.json;SOURCE_MANIFEST.json;PDF_MANIFEST.json;PACKAGE_INVENTORY.csv/.json;SEARCH_LOG.md;SOURCE_RIGHTS.md;BUILD_SOURCE_REVIEW_ARTIFACTS.py.
- Localprotected/extractedinputs:EXTRACTED_TEXT/,RENDERED_CHECKS/,REFERENCE_EXCERPTS_LOCAL/B03_PRINTED_REFERENCE_VALUES.csvandoriginJSON. Theseare sourceinputs/readingviews,notoursolveroutputs.
- `RECOVERY_FULL_SOURCE_REVIEW_01.zip`:cumulativenotes/controlcheckpoint,notfinalresearch/offline-completeinputarchive. OriginalZIP/PDFs,fulltext/images/completetablenumericextractions excludedpendingrightsreview;localpaths/URLs/hashesrecorded.
- PriorPRE_EXECUTION_REVIEW/andRESEARCH_READING/HEAT_MODEL_EXPLORATION/CODE_REVIEWreportsretainedashistory.

No submission-ready project or completednumberedresearch-phasepackageexists.
