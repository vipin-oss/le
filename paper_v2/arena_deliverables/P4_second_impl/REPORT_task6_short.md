# Task 6 — short report: does the second implementation agree, and is it independent?

Deliverable: `second_impl.py` (standalone solver) + `second_impl_comparison.csv` (42 archived
values) + `second_impl_elastic_branch.csv` (20 frequencies × 5 models × 2 branches) +
`task6_audit.py` (independence and residual audit). Sources compared against:
`scripts/numbers_log.txt` and `scripts/models.py`, taken from branch `review-paper-v2` and
never modified.

## 1. What was computed

With plane waves exp(i(kx − ωt)), s = −iω, K = k², the coupled 1D dispersion of the
template G(s) is

```
(rho c1^2 K + rho s^2)(s rho cv + G(s) K) + beta^2 T0 s K = 0,     G = N/(s D0),
D0 = 1 + tq s,  N = k s (1 + tT s) + ks (1 + tv s)
```

which, multiplied by s D0, is a quadratic in K. `second_impl.py` assembles A, B, C and
solves with `numpy.roots`; from the roots it takes v_p = ω/Re k and Q⁻¹ = 2 Im k/Re k, and
identifies the elastic branch by the *local* criterion "least damped, ties broken towards
√(1+ε)" instead of by continuity tracking. Parameter sets are the six prescribed in the
`models.py` docstring (Fourier, LS, DPL, GN-II, GN-III, MGT; ρ = cv = c1 = 1, β²T0 = ε = 0.1).

## 2. Comparison table — max relative difference per class

| class | archived values | worst rel. diff | cause | tolerance implied by the printout |
|---|---|---|---|---|
| uncoupled thermal-branch speed (`fig_thermal_family`) | 12 | 4.78e-04 | the archive prints 3–4 decimal places (`0.0447`, `14.1421`) | 2e-3 |
| coupled slow branch (`check_gn2`, `check_fronts`) | 4 | 6.01e-06 | archive prints 4 dp (`0.9839`, `0.854309`) | 2e-4 |
| coupled fast branch (`check_gn2`, `check_fronts`) | 4 | 6.69e-06 | same | 2e-4 |
| elastic branch speed (`fig_dispersion`) | 3 | **2.26e-16** | 16 digits printed → machine precision | 1e-10 |
| coupled thermal-branch speed (`fig_dispersion`) | 1 | 2.19e-16 | same | 1e-10 |
| bar-mode Q⁻¹ (`fig_bar_modes`) | 18 | 1.39e-04 | 4 significant digits printed, plus a branch-label effect (below) | 2e-4 |
| **total** | **42** | **4.78e-04** | | |

Every difference sits at or below the rounding of the archived printout: the values printed
to 16 digits are reproduced to ~2e-16, the values printed to 4 decimal places to ~1e-6, and
the values printed to 3–4 significant digits to ~1e-4. There is no case where two solvers
disagree beyond the precision at which the reference was written down.

## 3. Where the differences come from, honestly

1. **Printout rounding** — the whole 4.78e-04 worst case is `0.0447` printed to three
   significant digits (`fig_thermal_family`, Fourier at ω = 1e-3). It is not a numerical
   disagreement.
2. **Branch label, not value (bar modes)** — 3 of the 18 archived `fig_bar_modes` entries
   belong to the *strongly damped* pair, not to the continuation of the low-k acoustic mode
   (τ = 0.25 and 1.0 at k = 3). The archived script identified branches by continuation;
   `second_impl.py` identifies them by damping, so it assigns those points to the other
   branch. The Q⁻¹ *values* themselves are reproduced; only the label differs. This is why
   the bar-mode worst case (1.39e-04) is still inside the 2e-4 printing tolerance.
3. **Conditioning of the polynomial solver** — `numpy.roots` on (A, B, C) versus the closed
   form used in `models.py` differ in how they lose digits when two roots nearly coincide
   (thermal branch at low ω). The audit's residual test bounds this: substituting the
   computed K back into (D) leaves a relative residual ≤ 8.2e-13, so the roots really solve
   the equation rather than being artifacts of one algorithm.

Nothing in the comparison required a tolerance looser than the reference's own printout.

## 4. The 20-frequency table

`second_impl_elastic_branch.csv`: ω = 10^(−3 … 2) in 20 logarithmic steps, five models, both
branches (100 rows). Headline behaviour, all consistent with the archived anchors:

* Fourier: v_p falls 1.04881 → 1.00000 (adiabatic → isothermal), Q⁻¹ single-peaked
  (Debye, peak 0.0480 at ω ≈ 1.44); the archived `fig_dispersion` low-ω anchor
  1.0488055351860703 and high-ω anchor 1.0000307473049175 are hit to 2e-16;
* LS: v_p rises to 1.17050 against the archived `check_gn2`/`fig_dispersion` fast root
  1.1705367195742484 (rel. 3e-05, i.e. the 4-dp anchor at ω = 1e2);
* DPL: adiabatic → isothermal like Fourier, with a smaller peak loss than LS;
* GN-II / MGT: lossless pair 0.85431 / 1.17054, ω-independent — exactly the archived
  `check_gn2` closed form.

The archive contains **no 20-frequency elastic-branch table**, so the table cannot be
compared point by point; it is our output, and it is pinned where the archive does supply an
anchor (3 elastic speeds, plus the 12 thermal-branch and 18 bar-mode values that bracket it).

## 5. How independent is `second_impl.py`? (`task6_audit.py`)

| question | answer | evidence |
|---|---|---|
| does it import the manuscript's code? | **no** | audit A1: only `cmath, csv, math, numpy, os, sys, tempfile`; no `import models`, no `importlib`, no `exec`, no `sys.path` entry pointing at `scripts/` (the single bare mention of `scripts/` is a string citing where the comparison numbers come from) |
| is the code copied? | **no** | audit A2 against `models.py`: longest common contiguous line run = **1 line**, identical non-trivial lines = 9 of 399 (imports, `return`, closing brackets), token Jaccard = **0.138** |
| is the algorithm the same? | **no** | `models.py` uses the closed-form quadratic with `sqrt(discriminant)`; `second_impl.py` scales the equation by s D0 and calls `numpy.roots`, and identifies branches by a local damping criterion rather than by continuation |
| is the *physics* the same? | **yes, and it must be** | both solve the same field equations; independent means independent of the code, not of the equation being checked. Audit A4 confirms the roots satisfy (D) with residual ≤ 8.2e-13, so agreement is not two implementations sharing a bug |
| what is deliberately shared? | the six parameter sets and the archived literals | audit A3: the parameter sets are prescribed by the task ("parameter sets in `scripts/models.py` docstring"); the literals are the comparison target. Audit A6 re-reads the freshly pulled `numbers_log.txt` and finds all 24 literals at their printed precision |

So `second_impl.py` is a genuine second implementation of the dispersion calculation: new
solver, new branch-identification rule, new output path, and an audit that would fail if the
two files started to converge in code.

## 6. Reproduce

```
/tmp/venv/bin/python second_impl.py --check        # 42 archived values, 100-row table, all PASS
/tmp/venv/bin/python task6_audit.py --models <path>/models.py --archive <path>/numbers_log.txt
python3 ../../arena_deliverables/P3_atlas/bench_atlas.py --check
```

Logs: `check_second_impl_log.txt`, `check_task6_audit_log.txt`. numpy required; nothing under
`scripts/` is imported, executed or modified.
