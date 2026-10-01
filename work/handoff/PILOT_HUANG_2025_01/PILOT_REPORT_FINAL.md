# PILOT COMPLETE — source case reproduced (limited scope)

Date:30September2026. **Label:PILOT—NOTFINALVALIDATION**, but source-case mathematical reproduction: **SUCCESS within documenteduncertainty**.

## Verdict
Independent computations reproduce Huang2025 Figure5 CV/MCV3 curves at t*=.06,tau*=.04: **175/177 digitizedsourcepoints within combined graphical+numerical envelope (98.9%)**; MCV3 **102/102**. No parameterfitting;source values unchanged. Two outliers are identifieddigitizationartifacts,keptinrecord, curvesnotadjusted.

## Limitingcases—PASS
- Thermal wavefront speed: source nu=1/sqrt(tau)=5; derived characteristic speed5.00176 (0.035%).
- Thermal front: source x=.3; derived .30011. Elasticfront: source≈.06; derived .05998.
- alpha=0 uncoupled thermallimit: exact(7e-18); tails~1e-88≈0.

## Verificationchainretained
40equation/BC/matrixchecksPASS(~1e-15);deHoog48/64probesPASS;FVM-vs-deHoogprobes<=8e-6scaled;fullprofile+sourcecomparisonnowdone.
**Cohen80cross-checkFAIL retained as documented**:largeinconsistentvalues;rootcauseunconfirmed;excludedfromverdictbecause2independentmethods+sourcefigagree. Failurehistorypreserved.

## Limits
Mathematicalsourcecaseverification,NOTphysicalvalidation. No beta/ellipse/newmaterial/manuscript. No novelty/Q1claim. ActualCPU53.2s(cap1800),noGPU.

## Nextoptions(userdecides)
1. beta-Ga2O3+circle/ellipse coupledproblem fullplan; 2. Bagri/Gordeliyreferencecase; 3. manuscriptdirection. Explicitchoice required.
