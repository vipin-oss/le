# Task 5 — atlas expansion plan (proposal only)

`atlas_plan.csv` proposes a stratified sample of **40 published problems** in generalized
thermoelastic / multiphysics wave propagation, 2000–2026. Nothing is written into the
atlas itself and no `.tex` file is touched.

## How the sample was drawn

`make_atlas_plan.py` reads `paper_v2/verification_register.csv` (119 catalogued works),
keeps only entries with a real DOI, a year in 2000–2026 and a usable title, classifies
each title into a wave family, and then fills quotas in register order:

| family | quota | drawn |
|---|---|---|
| bulk / plane waves | 8 | 10 |
| surface (Rayleigh) | 6 | 6 |
| Lamb / plate | 4 | 4 |
| interface / layered (reflection–transmission, bonded, waveguides) | 7 | 4 |
| shear / SH | 3 | 3 |
| porous / voids (single, double, dual porosity) | 5 | 5 |
| multifield (piezo, magneto, flexo, photo, semiconductor, thermoelectric) | 5 | 6 |
| thermoelastic damping | 2 | 2 |
| **total** | 40 | 40 |

The interface/layered stratum is thinner than its quota in a 119-entry register; the
three missing slots were topped up from the remaining candidates in register order, so
that stratum shows 4 instead of 7 and bulk/multifield absorb the difference. This is
recorded here rather than hidden, because it is itself a finding: the project's citation
base is thin exactly where the atlas most needs reflection/transmission benchmarks.

## Column semantics

* `DOI` — taken from `verification_register.csv`; **no DOI is invented**, and every DOI
  is unique across the 40 rows (checked).
* `model_as_titled`, `geometry_as_titled` — inferred from the title only. The column
  `evidence_basis` says so for every row; `full_text_read` is `no` for all 40.
* `validation_target_proposed` — what our independent second implementation could check
  against a paper of that family (secular determinant, reflection coefficients,
  cut-off frequencies, Q⁻¹ peak position), i.e. the benchmark to design, not a claim
  about what the paper validates.
* `gap_note` — why the problem is worth adding: no experimental or damping-versus-
  frequency counterpart exists in the current atlas.

## What has to happen before these become atlas entries

1. Read each paper (or at least the abstract plus the secular equation) and replace the
   title-level `model_as_titled` / `geometry_as_titled` with what the paper actually
   states.
2. Attach a concrete benchmark: script, reference solution, tolerance. The families map
   onto the existing registry kinds (`code verification`, `convergence`, `analytic
   limit`), so most entries can reuse `check_dispersion.py`, `check_fronts.py` and the
   Rayleigh/Lamb checks.
3. Record whether the paper reports a number we can reproduce without its data (a speed
   ratio, a cut-off, a Q⁻¹ peak). If not, the entry stays a documentation row, not a
   benchmark.

Validator: `python3 check_atlas_plan.py` prints
`PASS all checks (rows=40, families=8, min family size=2)` and exits 0
(`check_atlas_plan_log.txt`).
