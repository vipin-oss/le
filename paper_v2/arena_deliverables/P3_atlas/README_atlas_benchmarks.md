# Task 5, second half — the 40 proposals as runnable benchmarks

`atlas_plan.csv` proposes 40 atlas problems, each with a free-text
`validation_target_proposed` ("number of propagating branches", "SH dispersion and
cut-off frequencies", …). Free text cannot be run. This layer turns those targets
into **eight executable benchmark families with pinned tolerances**, and maps
every one of the 40 problems onto the families its wave type must satisfy.

## What is claimed, and what is not

The 40 papers are known at title/metadata level only (`full_text_read = no` in
`atlas_plan.csv`). No secular equation, parameter table or figure from any of
them has been read. A benchmark of the form "reproduce Fig. 3 of paper X" would
therefore be fiction.

What *is* checkable today are **invariants of the model class**: the properties
any correct implementation of coupled thermoelasticity with these wave types has
to show, whatever the paper's particular parameters. Those are the eight
benchmarks below. Every row of `benchmark_map.csv` carries
`paper_equation_read = no` and a `what_is_still_missing` column stating the next
step (read the paper's dispersion relation, add a paper-specific reference at the
same tolerance).

## The eight benchmarks

| id | what it tests | reference | tolerance |
|---|---|---|---|
| BK-01 | the coupled dispersion is quadratic in K = k², so exactly two roots, for all six models and two frequencies | model structure | exact |
| BK-02 | ω → 0: elastic-branch speed tends to the adiabatic √(1+ε) = 1.0488088 | closed form | 1e-9 (measured 3.2e-14) |
| BK-03 | ω → ∞: Fourier → isothermal 1.0; LS → the GN-II fast root 1.1705367 | closed form | 1e-6 / 1e-5 (measured 4.9e-8 / 2.8e-7) |
| BK-04 | Q⁻¹ of the elastic branch: one interior maximum, at ωτ ≈ 1, height ≈ Δ/2 = 0.04545 | Zener Debye peak | position 20 %, height 15 % (measured 9.9 % / 10.2 %) |
| BK-05 | **attenuation vs frequency, low**: α/ω² constant over ω ∈ [10⁻³, 10⁻²] (Rayleigh) | asymptotic law | 1e-3 (measured 5.1e-5) |
| BK-06 | **attenuation vs frequency, high**: α saturates instead of growing (Fourier → 0.0500, LS → 0.1802) | asymptotic law | 1e-3 (measured 1.2e-4) |
| BK-07 | GN-II is lossless (Q⁻¹ = 0) and its two speeds are the closed form at every frequency | closed form | 1e-12 (measured 5.6e-16) |
| BK-08 | no growing bar mode: Re s ≤ 0 for 6 models × 5 wavenumbers | Lyapunov / Routh–Hurwitz | 1e-12 (measured 1.8e-15) |

BK-05 and BK-06 are also the only attenuation-versus-frequency material the
project now has: they are *model-side* scaling laws, not measurements (the
measured attenuation rows of Task 4 remain blocked — see
`../P3_experiments/README_experiments_2.md`).

## Mapping the 40 problems

`benchmark_map.csv` assigns benchmarks by wave family:

| family | problems | benchmarks |
|---|---|---|
| bulk | 10 | BK-01, 02, 03, 05, 06, 07, 08 |
| multifield | 6 | BK-01, 03, 08 |
| surface (Rayleigh) | 6 | BK-01, 02, 08 |
| porous / voids | 5 | BK-01, 05, 08 |
| interface / layered | 4 | BK-01, 03, 08 |
| Lamb / plate | 4 | BK-01, 02, 04, 08 |
| shear / SH | 3 | BK-01, 03, 07, 08 |
| TED / damping | 2 | BK-04, 08 |

## Files and how to run them

| file | content |
|---|---|
| `bench_atlas.py` | the eight benchmarks; drives `../P4_second_impl/second_impl.py` and nothing else |
| `bench_atlas_results.csv` | measured value, reference, tolerance, error and verdict for each benchmark |
| `bench_tolerances.csv` | the tolerance table: reference, reference type, tolerance, script, families it applies to |
| `make_benchmark_map.py` | regenerates `benchmark_map.csv` from `atlas_plan.csv` (`--check` verifies it is stable) |
| `benchmark_map.csv` | 40 rows: problem → benchmarks, with `paper_equation_read = no` and the missing step |
| `check_atlas_benchmarks.py` | validator for the whole layer (stdlib only) |

```
python3 bench_atlas.py --check          # 8 PASS lines, exit 0
python3 make_benchmark_map.py --check   # deterministic output, exit 0
python3 check_atlas_benchmarks.py       # PASS all checks (rows=40, benchmarks=8, families=8)
```

`bench_atlas.py` needs numpy (like the rest of the project's scripts); the two
checkers are standard library only. Nothing under `scripts/` is imported, run or
modified.
