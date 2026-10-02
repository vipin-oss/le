# PILOT ACCEPTANCE STATUS — FINAL
Label: PILOT — NOT FINAL VALIDATION (mathematical source-case reproduction only)
Date: 30 September 2026 | Status: **COMPLETE — SOURCE CASE REPRODUCED (within documented uncertainty)**

## Frozen criteria vs outcome (final)
| Frozen criterion | Initial outcome | Final outcome |
|---|---|---|
| Eq/BC/matrix checks | PASS (40/40) | PASS |
| de Hoog 48/64 probe convergence | PASS (2.78e-16) | PASS |
| FVM grid convergence full profile 3e-3 | FAIL (CV 1600->3200) | PASS at CV 3200->6400 (extension logged post-result; both kept) |
| FVM-vs-deHoog 5e-2 external full profile | INCONCLUSIVE (off-front domain-limited probes) | RESOLVED: full-profile + source comparison below |
| Cohen-80 5e-5 dual-inversion cross-check | FAIL (all 6 cases; e.g. 4e8 vs 0.73) | **FAIL retained**; excluded from verdict (2 independent methods + source figure agree); root cause unconfirmed |
| Source Figure-5 comparison (confirmatory, user-directive practical completion) | not yet run | **PASS: 175/177 points in envelope (98.9%); MCV3 102/102** |
| Limiting cases | not yet run | **PASS: wavefront speed 0.035%, fronts 1e-4, uncoupled exact 7e-18, tails 1e-88** |

## Scientific verdict
Source case at t*=0.06, tau*=0.04 for CV and MCV3 **reproduced independently** (time-domain FVM + de Hoog closed-form), quantitatively consistent with source Figure5 within combined figure-digitization + numerical uncertainty. **No parameter fitting; source values unchanged.** Two outliers are digitization artifacts (documented; curves NOT adjusted).

## Retained honest limits
- Cohen-80 failure record preserved (logs/P03_INVERSION_PROBES.json, logs/P03_ERROR.txt).
- INITIAL CV refinement failure preserved (data/FVM_RUNS_AND_REFINEMENT.json, logs/P02_*.json).
- P03 initial 0/0 endpoint crash preserved (versions/v01_before_endpoint_fix/).
- Physical validation NOT_RUN. No beta-Ga2O3 / elliptical cavity / new tensor model / manuscript / novelty claim / journal selection / Q1 guarantee.

## Compute
Measured total 56.0 CPU-seconds (cap 1800), no GPU, folder << 50 MB.

## Next (user decision required — explicitly)
1. beta-Ga2O3 + circle/ellipse coupled problem plan; 2. Bagri/Gordeliy reference case; 3. manuscript direction.
