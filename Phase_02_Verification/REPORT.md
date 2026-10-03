# PHASE 2 — VERIFICATION AUDIT AND RE-RUNS
Date 2026-10-03 · follows `Phase_01_Audit/REPORT.md` · findings closed: **A1, A2, A5, A8, A9, A10** (partial: A10 text + Phase 4 caption work), evidence produced for A15.

## 1. What was done

| Step | Action | Result |
|---|---|---|
| 1 | Environment rebuilt (fresh sandbox: no numpy, `work/` symlinks gone) → `python3 -m venv /home/user/.venv-q1` + `pip install numpy scipy matplotlib python-docx openpyxl reportlab pymupdf`; `sh bootstrap_paths.sh` | Python 3.11.2, numpy 2.4.6, scipy 1.17.1, matplotlib 3.11.2 — **identical to the library set recorded in `CODE_FREEZE_submission_2026_10_03.json`**, different from the numpy that produced the data (2.3.5 / Python 3.13.14) |
| 2 | Cross-environment fidelity check: full re-solve of `A_chi1_phi000_M` (96×96, 58 s) against the archived run | `sig_interp` −8.5363872762e+05 → identical to **2.7e-16 relative (1 ulp)**; `t_star`, `wall_pulse_err` exact; `back_max` 7.3e-25 → 6.7e-25 (round-off floor, no meaning). `verification/FIDELITY_check.json` |
| 3 | Re-specified the failing verification case in `07_Tests/run_tests.py` (finding A1) and added the order assertion as its own case `V0b_metric_consistency_convergence_order`; the 96×48 value is recorded as information, never deleted | suite re-run (1101 CPU-s): **28 cases, 27 PASS, 0 FAIL, 1 exploratory (INFO)**; V0 observed orders χ=1 [1.998, 2.000], χ=2 [1.962, 1.995]; production grid 192×96 worst error 1.261e-3 (threshold 5e-3); the inherited coarse-grid value 5.028e-3 (0.56 % over) is reported in the table and in the §4 text |
| 4 | Removed the `n/a` cell (A2) by making the Table 5 row build itself from recorded values, and installed a **submission guard**: both document builders now abort if any generated table contains `n/a`, `??`, `TODO` or an empty cell | `audit_tex.py`, `verify_pdf.py`, `check_crossrefs.py`, `check_tex_commands.py`, 26 conversion tests, renumber check: all green |
| 5 | Extended the production matrix (A8, A10): the four mechanism ablations re-run at the production grid (block `EM`, 24 runs, 96×96) and the isotropic circle added at the production grid (`D_iso_circle_M`) — 25 new runs, 1696 CPU-s, now archived in `09_Raw_Data/production/` and in `PRODUCTION_PROVENANCE.csv` (175 runs) | see §2 |
| 6 | Re-ran the whole analysis layer over all 175 stored runs (`analyze_v2.py`, extended with the EM block, matched-grid control ratios, and per-pulse-width reconstruction errors) | `Phase_02_Verification/verification/ANALYSIS_DIFF.md`: **9 keys added, 0 removed, exactly 1 pre-existing value changed — `numerics.n_runs` 150 → 175** (the count of audited runs). Every physical quantity identical. The 5 archived CSV tables and the 8 figures are byte-identical; 1 new CSV (`12_Tables/ablations_E_M.csv`) |
| 7 | A5: audited the inversion validity claim against the stored series of every run (`bromwich_window_audit.py`) | reported window 0 ≤ t ≤ 6 t_th: worst deviation of the reconstructed wall temperature from the imposed pulse **1.005e-10**, 0 of 175 runs above 1e-6. Full stored window: t_w = 1.2 → 6.34e-9 (166 runs); t_w = 0.6 → 1.50e-8; **t_w = 2.4 → 3.196e-1 at t = 12** (3 runs, block F only). §4 now states the bound per pulse width instead of unconditionally |
| 8 | Re-pointed the manuscript generators at the verified data (all edits are in the builders, never in the generated `.md`): abstract attribution uses the production-grid ablation set; §5.3 table carries both resolutions with an explicit "same grid, same orientation set" rule; §5.2 states the matched-grid shape ratios with numerator/denominator/grid; A9's peak bound now names its subset; §9.1 rewritten as a factual re-check record | abstract 249 words (limit 250), body 10 030 words, 33 pp PDF; companion 14 pp |
| 9 | Code freeze: new `06_Source_Code/CODE_FREEZE_submission_2026_10_03b.json` (27 files, 27/27 current); the 2026-10-02 and 2026-10-03 manifests are **unchanged** and still cited as history in §9.1 | builders' staleness guard passes |

## 2. A8 — does the attribution survive at production resolution?

Mechanism ablations, ellipse, six orientations, amplitude = peak-to-trough over mean (`A_φ`), mean = mean peak (MPa/K):

| case | grid 96×48 (pre-registered) | **grid 96×96 (production)** | T48 → M change |
|---|---|---|---|
| baseline (full anisotropy) | 29.01 %, mean 1.1707 | **30.06 %, mean 1.1845** | amplitude +3.63 %, mean +1.18 % |
| E1 expansion set 298 K-like | amp 29.91 %, mean ×0.063 | **amp 30.96 %, mean ×0.063** | amplitude +3.50 % |
| E2 isotropic expansion | amp 20.78 %, mean ×1.023 | **amp 20.99 %, mean ×1.023** | +0.97 % |
| E3 isotropic conductivity | amp 27.22 %, mean ×0.992 | **amp 28.11 %, mean ×0.992** | +3.28 % |
| E4 isotropic stiffness | amp 45.59 %, mean ×1.270 | **amp 45.56 %, mean ×1.266** | −0.07 % |

Modulation relative to the baseline of the same grid: E2 0.716 → **0.698**, E3 0.938 → **0.935**, E4 1.572 → **1.515**.
**Verdict:** the mechanism ranking and every qualitative statement are unchanged at the production grid; the
mean-peak ratios (which drive the expansion-data scale claim, ×0.063) reproduce to the third decimal. The absolute
modulations move by up to 3.6 % between the two grids — which is *larger* than u_num for the baseline (1.3 pp at
12 orientations), and that is precisely why the sentence that mixed 29.9 % (M) with 29.0 % (T48) was a real defect.
The abstract's claim is now supported by production-resolution data and the builder switches automatically
(`EAB = EAB_M if present`), so it cannot silently fall back to the coarse grid while keeping the strong wording:
the guard `if ratios … else weaker wording` is evaluated on whichever set is used.

## 3. A10 — the three ellipse/circle ratios, now separated and matched

| quantity | definition | value |
|---|---|---|
| mean shape effect, matched grid | mean of the 12-orientation ellipse sweep at M ÷ circle peak at M | **1.3964** |
| extreme shape effect, matched grid | ellipse min and max at M ÷ circle at M | **1.132 / 1.549** |
| extrapolated pair | ellipse extrapolated mean ÷ circle radially extrapolated | 1.3729 (unchanged, now labelled as a pair of extrapolated sequences) |
| isotropic control, matched grid | iso ellipse at M ÷ iso circle at M (new run) | **1.5296** (the earlier cross-grid value was 1.5307; the conclusion is unchanged) |
| isotropic control, extrapolated | iso ellipse extrapolated ÷ iso circle at M | 1.5229 |

Every one of these is now emitted by the builder with its numerator/denominator/grid, and the phrase "on average"
is gone. §5.2 no longer reads 1.37 as both a shape factor and an orientation factor.

## 4. Corrections to the Phase 1 audit (self-audit, item 14)

* **A9 was mis-stated in its evidence, not in its conclusion.** The 1.4 % figure is *not* "the quasi-static extreme
  presented as the general bound": the generator computes `max |peak_shift|` over the dynamic **and** quasi-static
  rows, and the abstract said "the peak" for the memory study as a whole. The fix that was actually needed (and is
  now made) is to name the subset: the dynamic runs alone give 0.5 %.
* **A2's `n/a` was a symptom of a dead link, not a typo:** `ms_results.py` looked up a test case named
  `V0b_metric_consistency_production_grids` that `run_tests.py` never emitted, so the value was permanently None.
  The row is now built from the fields the suite really records, and the guard prevents any future dead lookup
  from shipping.
* **A13 stays open** (reference additions) — Crossref API unreachable from this sandbox; deferred to Phase 5 with
  web-search verification.

## 5. Left for later phases (do not repeat this phase)

* Phase 4: §5.3 table caption to add the "six-orientation vs 12-orientation subset" clarification (anchor drafted
  in this report — the patch was attempted and deferred cleanly), figure regeneration incl. renaming to
  `fig1…fig8`, 600 dpi, removal of "frozen criterion" text and of the superseded-run panels (A11),
  `12_Tables/` → 6 CSVs consistent with 11 article tables (A14/B5).
* Phase 5: A13 (Cattaneo 1948, Vernotte 1958, Coleman–Gurtin 1968) + B19 methodology refs + B21 claim↔citation matrix.
* Phase 6: A3 (author fields — author-owned), A4 (AI declaration split), A7 (internal language; note
  "the frozen threshold is max(5u_num, 2%) = 6.56 % … (T4)" in §5.2 and "T1/T3" labels in §5.4/§6.4), A12, A14.
* Phase 7: A6 (duplicated §4.6 prose) and B8/B9/B11 formatting + language.
* A15 (LaTeX compile) — still impossible here: `objects.githubusercontent.com` unreachable (HTTP 000), no TeX
  engine, `apt` unusable. Static gates + `verify_pdf` structural checks are the substitute, and the manuscript
  does not claim compilation.

## 6. Files changed by this phase (all inside the working branch, nothing overwritten destructively)

* code: `07_Tests/run_tests.py`; `08_Experiments/production_matrix.py`, `analyze_v2.py`;
  `13_Manuscript/build_manuscript.py`, `build_calculations.py`, `ms_results.py`, `ms_numerics.py`
* data: `09_Raw_Data/production/` +50 files (25 runs), `10_Processed_Data/ANALYSIS_V2.json`,
  `ANALYSIS_V2_TABLES.md`, `PRODUCTION_PROVENANCE.csv` (175 rows), `12_Tables/ablations_E_M.csv` (new)
* records: `07_Tests/TEST_RESULTS.json` (28 cases), `TEST_REPORT.md`; `06_Source_Code/CODE_FREEZE_submission_2026_10_03b.json`
* documents regenerated from the data: `manuscript_IJHMT.md/.docx`, `FINAL_REVISED_MANUSCRIPT.tex/.pdf` (33 pp),
  `calculations_IJHMT.md/.pdf` + `FINAL_REVISED_CALCULATIONS.tex/.pdf` (14 pp), `SUPPLEMENTARY_TABLES.xlsx` (8 sheets),
  `MANUSCRIPT_STATS.json`, `highlights.txt`, `FINAL_REVISED_REFERENCES.bib` (54 refs)
* docs: `PAPER_PROJECT/README.md` environment/verification lines
* this folder: `bromwich_window_audit.py`, `diff_analysis.py`, `finalize.sh`, `finalize2.sh`,
  `patch_ms_results.py`, `patch_builders2.py`, `patch_freeze_refs.py`, `patch_abstract_trim.py`, `historical/`, `verification/`
