# Task 6 — independent second implementation of the template dispersion

`second_impl.py` re-derives and re-solves the coupled 1D thermoelastic dispersion from
the field equations, **without importing, executing or copying anything from
`scripts/models.py`**. Nothing under `scripts/` was touched.

## Files

| file | content |
|---|---|
| `second_impl.py` | standalone solver (numpy only): template transfer function, coupled roots K = k², bar-mode roots, 20-frequency table, comparison with the archive, `--check` mode |
| `second_impl_comparison.csv` | 42 archived numbers vs values computed here, with the log block each number comes from |
| `second_impl_elastic_branch.csv` | phase speed and Q⁻¹ of the elastic branch and of the second branch at 20 frequencies for 5 models (100 rows) |
| `second_impl_report.md` | generated report: comparison table, per-class worst difference, full 20-frequency table |
| `check_second_impl_log.txt` | output of `python3 second_impl.py --check` (all lines `PASS`, exit 0) |

Run with `python3 second_impl.py` (rewrites the report and both CSVs) or
`python3 second_impl.py --check` (assertions only). Requirements: Python 3 and
numpy; runtime ≈ 1.5 s.

## What the code solves

With plane waves exp(i(kx − ωt)), s = −iω, K = k², the two field equations
(momentum and energy balance) give

```
(ρ c1² K + ρ s²)(s ρ cv + G(s) K) + β² T0 s K = 0,          (D)
```

where the template heat-flux law is written as `G = N/(s D0)`,
`D0 = 1 + tq s`, `N = k s (1 + tT s) + ks (1 + tv s)`. Multiplying (D) by `s D0`
turns it into a quadratic in K:

```
A K² + B K + C = 0
A = ρ c1² N
B = ρ c1² (s ρ cv)(s D0) + ρ s² N + β² T0 s² D0
C = ρ s² (s ρ cv)(s D0)
```

The roots are obtained with `numpy.roots` (no closed-form discriminant), the
spatial branch is fixed by Re k > 0 (else Im k > 0), and for real k the same
expression is assembled as a polynomial of degree ≤ 4 in s with
`numpy.polynomial` convolution. The elastic branch is identified by a **local,
physical criterion** — the least damped of the two propagating branches
(Q⁻¹ = 2 Im k / Re k), ties broken towards the adiabatic speed √(1+ε) — so the
label cannot be corrupted by branch-swapping in a tracking loop.

Parameter sets are those of the `scripts/models.py` docstring: Fourier, LS,
DPL (τ_T = τ_q/2), GN-II, GN-III, MGT, with ρ = cv = c1 = 1, β²T0 = ε = 0.1.

## Agreement with `scripts/numbers_log.txt` (42 archived values)

| class | archived values | source block | worst relative difference | tolerance |
|---|---|---|---|---|
| uncoupled thermal-branch speeds | 12 | `fig_thermal_family` | 4.8e-04 | 2e-03 (four decimal places printed) |
| coupled slow branch | 4 | `check_gn2`, `check_fronts` | 6.0e-06 | 2e-04 |
| coupled fast branch | 4 | `check_gn2`, `check_fronts` | 6.7e-06 | 2e-04 |
| elastic branch speed | 3 | `fig_dispersion` | 2.3e-16 | 1e-10 (16 digits printed) |
| coupled thermal branch speed | 1 | `fig_dispersion` | 2.2e-16 | 1e-10 |
| bar-mode Q⁻¹ | 18 | `fig_bar_modes` | 1.4e-04 | 2e-04 (four significant digits printed) |

Every difference is at or below the rounding of the archived printout; the
16-digit entries (`fig_dispersion`: LS elastic 0.9839644366553235, LS thermal
2.0298360266180757, classical elastic 1.0488055351860703 and 1.0000307473049175)
are reproduced to machine precision (~2e-16), as are the GN-II closed-form
speeds (0.8543089535574103 / 1.1705367195742484).

## Elastic branch at 20 frequencies

`second_impl_elastic_branch.csv`, ω = 10^(−3…2) in 20 logarithmic steps, five
models (Fourier, LS, DPL, GN-III, MGT); both branches are listed, so the
columns `v_p`, `Qinv` are the elastic branch and `v_p_other`, `Qinv_other` the
second branch. Headline behaviour:

* Fourier: v_p falls monotonically 1.04881 → 1.00000 (adiabatic → isothermal),
  Q⁻¹ single-peaked at ω ≈ 1.4 with Q⁻¹ = 0.0480 (Debye shape, as required);
* LS (τ = 1): v_p rises 1.04881 → 1.17050, the fast root of the archived
  high-frequency quadratic 1.1705367195742484 (rel. diff 3e-05);
* DPL: 1.04881 → 1.00000, but with a smaller peak loss than LS;
* GN-III, MGT: at these parameters MGT reduces exactly to G = 1/s (hence to the
  GN-II branch structure), so both models show the two near-lossless speeds
  0.85431 and 1.17054.

## Findings and limits

1. **No numerical disagreement in the archived checks.** All 42 archived
   numbers are reproduced within their printed precision, including the exact
   16-digit `fig_dispersion` values and the GN-II closed-form roots. The
   template polynomial, the branch convention and the Q⁻¹ definition used in
   `scripts/` are therefore independently confirmed.
2. **Branch labelling in `fig_bar_modes` (not a numerical error).** At
   τ > 0 and k ≥ 3 the printed Q⁻¹ (0.6735, 0.1897, 0.0629 for τ = 0.25) belongs
   to the *strongly damped* pair of modes, while the continuation of the low-k
   acoustic mode has Q⁻¹ = 0.0492, 0.0167, 0.0056 at the same wavenumbers. Both
   are modes of the same polynomial; the archived printout mixes the two by
   construction (ad-hoc root selection in that script). This matters for
   citation: a figure of "Q⁻¹ of the bar mode" that changes branch at k ≈ 0.5
   should be relabelled.
3. **Coverage.** The template covers Fourier, LS, DPL, GN-II, GN-III and MGT.
   Green–Lindsay is outside this single-lag template, so the GL front numbers in
   `check_fronts` were *not* used as a template check (only the LS ones were).
4. **Parameter sets differ between blocks.** `fig_thermal_family` uses ks = 0.25
   and τ = 1, `check_fronts`/`fig_dispersion` use τ = 0.25, `scripts/models.py`
   uses τ = 1. The comparison therefore stores the parameter set with every
   row; the 20-frequency table uses the docstring sets.
5. **Not a source check.** This file verifies internal numerical consistency of
   the scripts against their own archived output. It says nothing about whether
   the model choice is right for a given material; that is Tasks 3–5 and the
   evidence registers.
