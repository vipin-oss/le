# Decision log

Date:30 September2026.

## D001 — Current master
Previous working rules:v2.0 and unapproved amendment suggestions. New decision:user supplied FINAL MASTER PROMPTv2.1; preserve it verbatim as canonical MASTER_PROMPT.md, sections0–90. Evidence:user message. Affected science/code/results:none. No scientific revalidation caused by saving the control text.

## D002 — Scope and execution gate
User confirmed BOTH material/crystal and geometric symmetry and COUPLED THERMOELASTIC RESPONSE. User subsequently asked for published-journal/benchmark evidence review before execution. Current authorization is that bounded review, not automatic implementation/pilot/production. Final direction/model/material/journal remain unapproved.

## D003 — Evidence classification
Limiting-case and theoretical comparisons are verification, not automatically physical validation. Experimental property inputs do not independently validate a new model when copied into it. Agreeing with a source is not guaranteed or to be forced.

## D004 — Source integrity
Current review found2019 correction DOI10.1063/1.5088513 to Jiang2018 DOI10.1063/1.5054573. Future use must include corrected version and coordinate mapping. The beta-Ga2O3/new-model proposal remains provisional. Affected current equations/code/results:none because no new model was implemented/run. Recheck/revalidate any future input derived from that source.

## D005 — Source-access blocker
Core recent-model/coupled benchmark full equations are not obtained. Do not invent them from abstracts or silently substitute an older model. Request legitimate PDFs and exact next-task approval. Journal-family checks are provisional, not final submission selection.

## D006 — alit full sources received / read
Date:30 September2026. User supplied alit.zip containing the exact3requestedpapers. Former accessblockersresolved; relevantsourceequations/BCs/ICs/material/casesinspected. Numericalverification/physicalvalidation remainunexecuted. No finalmodel/material/journalapproval inferred from upload.

## D007 — Proposed reference route / source issues
Recommend firstB01Figure5CVparent+MCV3sourcecase, thenB02LScylinder andB03heat-onlytables separately. Limitedmanualoperator/boundary/common-law checks recorded. MGN2Eq36mismatch andalphatableunit requiredocumenteddisposition;originalsourceunchanged. Match totalstaticconductivity in separatemechanismcontrols, notbysilentlychangingpublishedreferenceinputs. No sourcecorrectionimplemented, no solveroutputaffected.

## D008 — Execution hold
A possiblePhase0A2reference-onlyfeasibilitypilot hasproposedcap0.5CPU-hour/noGPU/50MB; this isnotobservedruntime/productionapproval. Needexplicitnextphase/scopeauthorizationandpre-runplan/criteria. No newmaterial/ellipsecavityproduction authorized.

## D009 — Bounded pilot authorized
Date:30September2026. User `ok do it` directly responds to the sole explicit limitedCV+MCV3Huangreferencepilotproposal. Scope:sourcecaseonly,planfreeze thenexecution,cap1800CPU-seconds/noGPU/50MB. No beta/ellipseproduction/finaltopicapproval inferred. Python chosen for the availableworkspace/runtime and appropriate analytical/numerical checks; same sourcePDEs,not finalprojectmethodselection.
Unit disposition:source numeric alpha interpreted1/K from its stress-law dimensions; source value/PDFunchanged. Zero causalprehistory recorded. Frozenpilotplan/input/source hashes in PILOT_HUANG_2025_01/PLAN_FREEZE_RECORD.json.

## D010 — Pilotcorrection and retainedfailures
Initialiteration:40basicchecksPASS;6FVMrunscompletebutCVlastpointrefinementcriterionnotmet; deHoogabortsonidenticallyzeroboundarystress. v01/error/stagerecordspreserved. Documentedanalyticzeroendpointonly andpost-resultCV6400diagnosticmesh;sourceparams/frontmask/criteriaunchanged.

## D011 — SafetyvalveSTOP
Correctediteration:CVrefinementmeetscriterion,deHoog48/64stableonprobes,butCohen80failsfrozencross-checkallsixmodel/QoIcombinations. Two pilotiterationsdidnotreachoverallPASS:STOPsolversperv2.1§77. Existing-dataFVM/deHoogprobecomparisonissupportivepartialdiagnosticevidence,notanexcusetodeletethefailedcriterion. No sourcegraph/fullprofilereproductionorphysicalvalidationclaimed. Usermustapproveadiagnostic-onlynextphaseoranexplicitloggedpost-resultmethod-planrevision.


## 30 September 2026
- D012. User pragmatic directive ("full validation kabhi nahi hoga; limiting cases + source-jaisi curves; source galat ho to honestly document"): accepted practical completion of source-case verification via source-figure comparison + limiting cases; no tuning/copying of source curves; Cohen failure retained. FINAL: source case REPRODUCED (175/177 points in envelope; MCV3 102/102; limiting cases pass). Phase closed; next direction awaiting explicit user choice.

## 30 September 2026 (Phases 1–9, PROJECT_CRYSTAL_GEOMETRY_01)
- D013. User message 7 ("ab aap jo prompt di thi uske according chlo mujse baar na pucho validation wala kaam ho gye ab un phase se chlo"): blanket authorization to proceed through MASTER_PROMPT v2.1 phases 1→13 for the β-Ga₂O₃ circular/elliptical cavity coupled-thermoelastic direction WITHOUT repeated approval requests. Still user-owned: production compute >4 CPU-h / 1 GPU-h / 5 GB, method changes of first-principle kind, journal selection, final submission. Direction = BOTH crystal symmetry (monoclinic C2/m tensors incl. K13, C15,C25,C35,C46) AND geometric symmetry (circle vs equal-area ellipse χ=2) with coupled thermoelastic response.
- D014. Critical discretization correction chain (ALL pre-fix results superseded): (a) composed first-derivative Laplacian (Dx@Dx+Dy@Dy) found to carry an exact odd-even parity null mode (j±1 entries cancel) — root cause of V6/V7 failures and silent pollution of earlier V2/V3; replaced by conservative flux-form operator (src/cg_ops.py MappedOps: thermal/momentum/beta_grad_rows/stress_first). (b) flux-form metrics recomputed as central differences of coordinate arrays so mixed partials commute exactly (patch identity holds). (c) sign error in eta-half uy() deta coefficients fixed (patch/quad tests then converged O(h²)). (d) grid domain bug: Grid(a=1e-8, R=80.0) built the domain 1 nm→80 m (R treated as absolute) while analytics assumed R=80a; all R fixed to 80·a. (e) V6 'exact' log formula also a-units-buggy. (f) SI-scale round-off: interior PDE rows ~1e20 vs unit BC rows; fixed by J_row scaling + row equilibration. (g) undamped finite-domain resonances (outer reflection 8.1 t_th at R=80a) make harmonic sampling grid-sensitive; hysteretic damping η_d=0.05 on Q in DYNAMIC runs adopted (undamped statics for V6/V7), sensitivity {0.02, 0.1} to be reported. All corrections logged in CHANGELOG; failed histories preserved (data/VERIFY.json superseded copies).
- D015. Production design deviations from frozen plan (pre-registered here BEFORE production outputs viewed): outer radius R=80a (plan said 25a; plan's causal claim fails — longitudinal round trip at 25a = 2.47 t_th < response peak of the frozen pulse t0=2.5 t_th; at 80a: 8.1 t_th long / 14.9 t_th shear, QoI window t≤6 t_th causally clean); pulse kept at frozen t0=2.5 t_th, tw=1.2 t_th (run_verify's t0=1.5/tw=0.5 was verification-only). Analysis QoI window t≤6 t_th pre-registered. Block matrix A(φ×χ Fourier 24 runs) + B(Λ/size 11) + C(feedback-off 1) + D(iso control 2) = 38 runs.
- D016. Manuscript package completion (30 Sep 2026): draft v1.0 with pre-registered outcomes (H1/T1 PASS machine-class identity + documented 0.30% peak-sampling scatter; H2/T4 RESOLVABLE 33–37%; H3/T2 strong form NOT-SUPPORTED — two-parameter (Λ,ε) map reported; H4/T3 WITHIN-BOUND 0.2δ; H5 exploratory trend). c_p worked example + θ_amp=10K example delivered (PARAMETER_TABLE §D promise closed). Code freeze + environment + determinism check done. Journal choice explicitly left open (user-owned; user skipped selection prompt twice — no default imposed; draft is journal-agnostic).

## D017 (30 Sep 2026) — Journal selection + format pass
- User message "yes go ahead" authorizes proceeding with journal selection + formatting
  (previous ask_user on journal was skipped twice; draft kept journal-agnostic meanwhile).
- PRIMARY target: International Journal of Heat and Mass Transfer (Elsevier) — best
  topic fit (thermal-wave + thermal-stress), Q1 (SCImago 2025 SJR 1.224, SECONDARY;
  JCR UNVERIFIED — check at submission). FALLBACK (switchable before submission):
  Mechanics of Advanced Materials and Structures (Q2) — methods emphasis; note its
  text-recycling/AI policy needs a fit check.
- Format pass executed: SUBMISSION_PACKAGE/ (manuscript_IJHMT.md with numbered refs
  [1]–[11] first-appearance, nomenclature, declarations; cover letter; title page;
  highlights; README with pre-submission TODOs). References with unverified
  titles/initials are EXPLICIT placeholder-flagged — nothing fabricated. Tzou (1995)
  added as the only content-level citation addition (kernel definitions).
- Abstract ~234 words — trim if current Guide requires ≤200 (recorded TODO).
- Submission remains USER-OWNED (authorship, affiliations, JCR check, final send).

## D018 (30 Sep 2026) — Full workspace recovery archive
- User request: everything done into one zip for workspace-loss recovery.
- Built FULL_RECOVERY_2026-09-30.zip: 571 files, 39 MB — ALL work (project, pilot,
  root logs, master prompt, user code/packages, user's own papers FEM_1..5/GK_heat/
  Quasi_crystal with verified own-authorship text) + README_RECOVERY.md restore guide +
  RECOVERY_MANIFEST.json (sha256 per file) inside the zip.
- EXCLUDED per standing no-third-party-PDF rule (14 items, EXCLUDED_FILES.json with
  paths+sha256+reasons): 8 accessible full-text PDFs, Klimm PDF, 3 benchmark PDFs +
  alit.zip, paper_springer.pdf (authorship unverifiable — conservative exclusion).
  Copies remain in workspace at original paths; hashes allow identification/re-obtain.
