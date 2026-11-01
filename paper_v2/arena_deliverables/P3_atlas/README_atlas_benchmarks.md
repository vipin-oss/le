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

---

## BK-09 and the coverage map (added 2026-11-01)

Two gaps were fixed here, and one wrong number.

**The wrong number.** "8 of 40 cases carried through to results" appeared in the readiness note and
the pending list. It was wrong twice: the eight rows in `bench_atlas_results.csv` are *benchmark
families* (BK-01 ... BK-08), not atlas cases, and no case can have a case-level result because every
paper in the plan was read at title and metadata level only. The honest statement is now in both
documents and enforced by their checkers: **40 cases planned, 12 with a fully executable invariant,
11 with a partial one, and 0 case-level results.** (Step 29 raised the first number to 23 - see the
section at the end of this file; the figures in the rest of this section are the step-28 state.)

**The missing surface family.** The plan has eight wave families; the benchmarks covered bulk and
damping only. `bench_surface.py` adds **BK-09**, the elastic Rayleigh invariant, from the secular
equation `(2 - x^2)^2 = 4 sqrt(1 - x^2) sqrt(1 - eta x^2)` with `x = c_R/c_S` and
`eta = (c_S/c_L)^2`. Six checks, all passing, and two of them are anchors against the classical
table rather than self-consistency: the incompressible limit comes out at **0.955300 c_S** (classical
0.9553) and the quarter-ratio value at **0.919402 c_S** (classical 0.9194). Uniqueness, the residual
(1e-13), the range and monotonicity in Poisson's ratio are checked as well.

**The coverage map.** `atlas_case_coverage.csv` has one row for each of the 40 planned cases, saying
which invariant applies, whether it is executable today, and - where it is not - the invariant that is
missing, named as BK-10 ... BK-15 with the closed form it has to satisfy:

| missing | needed for | cases |
|---|---|---|
| BK-10 thermoelastic Rayleigh secular determinant | surface (Rayleigh) beyond the elastic limit | 6 (partial today) |
| BK-11 branch-count invariant for m > 2 | double-porosity models, which have a third branch | 5 (partial today) |
| BK-12 Rayleigh-Lamb plate determinant and its A0/S0 limits | Lamb / plate | 4 |
| BK-13 layered Love-wave cut-offs | shear / SH | 3 |
| BK-14 Snell plus energy-flux continuity | interface / layered | 4 |
| BK-15 coupled piezo/magneto branch speeds | multifield | 6 |

That is the atlas roadmap in one page: write five invariants, then the 17 uncovered cases become
checkable, and only after the papers are read can any of them become a comparison with a paper.
Three of the five are written - BK-12, BK-13 and BK-14, next section - which leaves BK-10, BK-11 and
BK-15 and takes the uncovered count from 17 to 6.

```bash
python3 bench_surface.py     # recomputes BK-09 and the coverage map
python3 check_surface.py     # PASS all checks (BK-09=6 rows, BK-12/13/14=14 rows, coverage=23/11/6 of 40)
```

---

## BK-12, BK-13, BK-14: the three families that had no invariant (added 2026-11-01, step 29)

Three of the five missing invariants are written now, so eleven of the seventeen uncovered cases
have an executable check. Each is anchored on a closed form that was **not** derived from the same
code that computes the number - otherwise the check would only prove the code agrees with itself.

`bench_families.py` writes `bench_families_results.csv`, 14 rows, all PASS:

| benchmark | row | measured | classical anchor |
|---|---|---|---|
| BK-12 | S0 speed at kh = 0.02, nu = 1/4 | 1.632981 c_S | sqrt(2/(1-nu)) = 1.632993 |
| BK-12 | A0 speed at the same point | 0.018851 c_S | 0 (flexural branch vanishes with kh) |
| BK-12 | both branches against c_R at kh = 20 | 9.2e-08 c_S | c_R = 0.919402 c_S |
| BK-12 | branch count at kh = 1 | S 3, A 4 | Rayleigh-Lamb tan/tan and tan/cot system |
| BK-12 | monotonicity over kh = 20 -> 0.02 | 22 points per branch | S0 falls, A0 rises |
| BK-13 | modes below the first cut-off | 1 | one mode below omega_1 |
| BK-13 | modes above omega_1 and omega_2 | 2 then 3 | one more mode per cut-off |
| BK-13 | upper mode as omega -> omega_1 | c2 - c = 1.6e-02 | approaches c2 |
| BK-13 | measured cut-off | 3.627658 | pi / sqrt(1/c1^2 - 1/c2^2) = 3.627599 |
| BK-13 | layer faster than the half-space | 0 modes | Love waves need c1 < c < c2 |
| BK-14 | energy flux below the critical angle | 2.2e-16 residual | R^2 + T^2 (Z2/Z1) = 1 |
| BK-14 | Snell residual at 20 degrees | 0.0 | sin(theta1)/c1 = sin(theta2)/c2 |
| BK-14 | critical angle (c2/c1 = 1.7) | 36.032 deg | asin(c1/c2) |
| BK-14 | normal-incidence reflection | -0.276596 | (Z1-Z2)/(Z1+Z2) |

Two bugs were found while writing these, and both are worth recording because they are the kind
that would have produced a confident wrong number:

- the Rayleigh cubic in the form used here has a **degenerate root at x = 0** (both sides are 4
  there). Bisecting from 0 walks the bracket to zero and returns `c_R = 1e-08` instead of 0.9194.
  The bracket starts at 0.5 now, where the residual is negative and at 1 it is positive.
- the transmitted energy flux is `T^2 * (Z2/Z1)`, not `T^2 * (Z2 cos2)/(Z1 cos1)`; the wrong form
  leaves a 0.3 residual at grazing angles and looks like physics instead of algebra.

The coverage map therefore reads **23 full / 11 partial / 6 none of 40**:

| missing | needed for | cases |
|---|---|---|
| BK-10 thermoelastic Rayleigh determinant | surface (Rayleigh) beyond elastic | 6 (partial) |
| BK-11 branch-count invariant for m > 2 | double porosity | 5 (partial) |
| BK-15 coupled piezo/magneto branch speeds | multifield | 6 |

BK-15 is deliberately **not** written. The repository has no coupled piezo/magneto constitutive
model, so any number produced for it would describe a model nobody in this project uses; the six
multifield cases stay uncovered until a paper supplies that model.

```bash
python3 bench_families.py    # recomputes BK-12, BK-13, BK-14 ...
python3 check_surface.py     # ... and checks them (PASS, exit 0)
```
