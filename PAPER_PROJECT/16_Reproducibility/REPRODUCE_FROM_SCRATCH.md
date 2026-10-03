###################REPRODUCE_FROM_SCRATCH###################

Everything below was run inside the sandbox that produced this archive, on 2026-10-04,
with the interpreter `/usr/bin/python3`. Where a step was not attempted, that is said in words.

## Clean-room recipe (what a new machine does)

```bash
unzip PAPER_PROJECT_COMPLETE_REPRODUCIBILITY_ARCHIVE.zip
cd PAPER_PROJECT_COMPLETE_REPRODUCIBILITY_ARCHIVE
# 1. the archive mirrors PAPER_PROJECT/, so recreate that layout:
mkdir -p ../rp && cp -r 01_PROGRAM/src ../rp/PAPER_PROJECT/06_Source_Code/src 2>/dev/null || true
sh bootstrap_paths.sh          # or place the tree at the path the scripts expect
python3 -m venv .venv && . .venv/bin/activate
pip install -r 01_PROGRAM/environment/requirements_pinned_from_handoff.txt
pip install python-docx pillow
# 2. integrity
sha256sum -c 09_ARCHIVE_METADATA/SHA256SUMS.txt
# 3. re-derive everything that is cheap, in order
python3 01_PROGRAM/experiments/analyze_v2.py
python3 01_PROGRAM/experiments/make_provenance.py
python3 01_PROGRAM/experiments/make_figures.py
python3 01_PROGRAM/experiments/reproduce.py
# 4. compare with what shipped
diff <(git diff --no-index 11_Figures/fig2_phi_sweep.png 08_FINAL_OUTPUTS/figures/fig2_phi_sweep.png 2>/dev/null | head) /dev/null && echo "figures identical"
```

## What is expected

- `analyze_v2.py` prints a short summary and rewrites `10_Processed_Data/ANALYSIS_V2.json` and
  `ANALYSIS_V2_TABLES.md`; the shipped copies are in `03_DATA/processed/` and `08_FINAL_OUTPUTS/`,
  so a byte-comparison is meaningful.
- `reproduce.py` writes `07_Tests/REPRODUCTION_TEST_REPORT.md` and, on the environment it was
  developed in, ends `Overall: 11 PASS, 0 FAIL` with relative differences of 0.00e+00 on the
  closed-form and interpolation items (see the stored report in `04_REPRODUCTION/`). It needs
  `07_Tests/TEST_RESULTS.json`, which ships in the archive.
- `make_figures.py` rewrites the eight PNGs in `11_Figures/`; identical to the shipped PNGs
  except for matplotlib metadata, so compare pixel content if bytes differ.
- Full-suite re-run (`run_tests.py`) takes about 20 min on 2 vCPU and needs ~1 GB headroom for the
  heaviest grids; if it is killed, that is the same failure mode the project recorded (see
  `COMPUTE_STATUS.md`) - reduce to the light grids rather than calling it a numerical discrepancy.

## Compiling the manuscript

```bash
cd 02_OVERLEAF && pdflatex FINAL_REVISED_MANUSCRIPT && bibtex FINAL_REVISED_MANUSCRIPT \
  && pdflatex FINAL_REVISED_MANUSCRIPT && pdflatex FINAL_REVISED_MANUSCRIPT
```

`elsarticle.cls` and `elsarticle-num.bst` come from the Elsevier LaTeX bundle shipped by TeX Live
and Overleaf; they are **not** inside this archive because the project never kept a copy whose
provenance could be verified (NOT AVAILABLE in the repository). `Phase_10_Submission_Package/compile_check.sh`
(archived at `08_FINAL_OUTPUTS/manuscript/compile_check.sh`) runs the same sequence and triages the
log; with no TeX engine installed it prints the commands instead of failing.

## Fresh reproduction result, if the builder was given one

NOT AVAILABLE for this build: the archive builder was run without `--repro`, so no fresh run was
recorded by the packager. The stored reports in `04_REPRODUCTION/` are the reproduction
evidence that ships with the archive, and they were produced by the scripts listed there.
