###################REPRODUCE_FROM_SCRATCH###################

Everything below was run inside the sandbox that produced this archive, on 2026-10-04,
with the interpreter `/home/user/.venv-repro/bin/python`. Where a step was not attempted, that is said in words.

## Clean-room recipe (what a new machine does)

```bash
unzip PAPER_PROJECT_COMPLETE_REPRODUCIBILITY_ARCHIVE.zip
cd PAPER_PROJECT_COMPLETE_REPRODUCIBILITY_ARCHIVE
# 1. the archive mirrors PAPER_PROJECT/, so recreate that layout:
mkdir -p ../rp && cp -r 01_PROGRAM/src ../rp/PAPER_PROJECT/06_Source_Code/src 2>/dev/null || true
sh bootstrap_paths.sh          # or place the tree at the path the scripts expect
python3 -m venv .venv && . .venv/bin/activate
pip install -r 01_PROGRAM/environment/requirements.txt
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

```json
{
 "verdict": "PASS",
 "run_date": "2026-10-04T04:21:50",
 "wall_s": 43.0,
 "environment": {
  "python": "Python 3.11.2",
  "libraries": {
   "numpy": "2.3.5",
   "scipy": "1.17.1",
   "matplotlib": "3.10.9",
   "pymupdf": "1.28.2",
   "fitz": "1.28.2",
   "docx": "1.2.0",
   "openpyxl": "3.1.5",
   "PIL": "12.3.0",
   "reportlab": "5.0.1",
   "mpmath": "1.3.0"
  },
  "cpu_count": 2,
  "ram_MB": 3939,
  "kernel": "Linux e2b.local 6.1.158+"
 },
 "steps": [
  {
   "name": "environment probe",
   "command": "/home/user/.venv-repro/bin/python -c \"import numpy, scipy, matplotlib\"",
   "exit_code": 0,
   "detail": {
    "python": "Python 3.11.2",
    "libraries": {
     "numpy": "2.3.5",
     "scipy": "1.17.1",
     "matplotlib": "3.10.9",
     "pymupdf": "1.28.2",
     "fitz": "1.28.2",
     "docx": "1.2.0",
     "openpyxl": "3.1.5",
     "PIL": "12.3.0",
     "reportlab": "5.0.1",
     "mpmath": "1.3.0"
    },
    "cpu_count": 2,
    "ram_MB": 3939,
    "kernel": "Linux e2b.local 6.1.158+"
   }
  },
  {
   "name": "analyze_v2",
   "command": "/home/user/.venv-repro/bin/python PAPER_PROJECT/08_Experiments/analyze_v2.py",
   "exit_code": 0,
   "detail": [
    "  tw= 2.4: circle 0.8579  ellipse(90) 0.9886  ellipse(150) 1.3649  A2 31.98%  ratios 1.152, 1.591",
    "## Numerical quality of the stored runs",
    "  runs 175/175; max backward error 7.226266702964897e-17; max wall-pulse error (t<=6) 1.0054844078071441e-10; (t<=12) 0.3196191972977383; by pulse width: t_w=0.3: 6.8e-11/7.3e-09 (n=3), t_w=0.6: 1.0e-10/1.5e-08 (n=3), t_w=1.2: 3.5e-11/6.3e-09 (n=166), t_w=2.4: 5.7e-13/3.2e-01 (n=3)",
    "WROTE /home/user/le/PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2.json"
   ]
  },
  {
   "name": "make_provenance",
   "command": "/home/user/.venv-repro/bin/python PAPER_PROJECT/08_Experiments/make_provenance.py",
   "exit_code": 0,
   "detail": [
    "provenance rows: 175 -> /home/user/le/PAPER_PROJECT/10_Processed_Data/PRODUCTION_PROVENANCE.csv"
   ]
  },
  {
   "name": "make_figures",
   "command": "/home/user/.venv-repro/bin/python PAPER_PROJECT/08_Experiments/make_figures.py",
   "exit_code": 0,
   "detail": [
    "wrote /home/user/le/PAPER_PROJECT/11_Figures/fig5_memory.png",
    "wrote /home/user/le/PAPER_PROJECT/11_Figures/fig6a_mesh.png",
    "wrote /home/user/le/PAPER_PROJECT/11_Figures/fig6b_ablation.png",
    "wrote /home/user/le/PAPER_PROJECT/11_Figures/fig7_pulse_width.png"
   ]
  },
  {
   "name": "reproduce",
   "command": "/home/user/.venv-repro/bin/python PAPER_PROJECT/08_Experiments/reproduce.py",
   "exit_code": 0,
   "detail": [
    "('V11 peak error 96x48', 0.0027, 0.0027484576755259634, 0.01794728723183826, 0.05, 'PASS', 'stored 4 digits')",
    "('principal result: ellipse phi=90 peak (interp, Pa/K) re-computed vs stored', -961654.3309977308, -961654.3309977308, 0.0, 1e-09, 'PASS', '')",
    "('principal result: nodal peak', -959287.0616127604, -959287.0616127604, 0.0, 1e-09, 'PASS', '')",
    "REPRODUCTION REPORT written"
   ],
   "report": "PAPER_PROJECT/07_Tests/REPRODUCTION_TEST_REPORT.md",
   "overall": "11 PASS, 0 FAIL",
   "fail_lines": 0
  }
 ],
 "files_regenerated": [
  {
   "path": "PAPER_PROJECT/11_Figures/fig1_setup.png",
   "sha_before": "c485b987744740a64349031c5aa08f9e86aa5ac5b60fd729f94b9fbf48feecdf",
   "sha_after": "c485b987744740a64349031c5aa08f9e86aa5ac5b60fd729f94b9fbf48feecdf",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/11_Figures/fig2_phi_sweep.png",
   "sha_before": "6d642cad0a71fd0f931c66c4fbd838e001849f608ace805d940a5c220fdf6a27",
   "sha_after": "6d642cad0a71fd0f931c66c4fbd838e001849f608ace805d940a5c220fdf6a27",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/11_Figures/fig3_wall_profiles.png",
   "sha_before": "4d3067555dc4549793697741f01dea0a955940a383e0331ffdea8136ae365b0e",
   "sha_after": "4d3067555dc4549793697741f01dea0a955940a383e0331ffdea8136ae365b0e",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/11_Figures/fig4_verification.png",
   "sha_before": "383fc8f168e058f3fc89ee9255088448d93148ef24575ab50ffcbf6b5867988d",
   "sha_after": "383fc8f168e058f3fc89ee9255088448d93148ef24575ab50ffcbf6b5867988d",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/11_Figures/fig5_memory.png",
   "sha_before": "c1905d40c9abb33c6e513e1d654a7c7b1daf13dd65f43297e348c96d41351e29",
   "sha_after": "c1905d40c9abb33c6e513e1d654a7c7b1daf13dd65f43297e348c96d41351e29",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/11_Figures/fig6a_mesh.png",
   "sha_before": "c6d3b67eaf91666aefe3fef1a956013bac7f2163cfd441d3c8f88cb662619c38",
   "sha_after": "c6d3b67eaf91666aefe3fef1a956013bac7f2163cfd441d3c8f88cb662619c38",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/11_Figures/fig6b_ablation.png",
   "sha_before": "3e88449b5463374fe9b6b0424df01e5b608b03fc8eb86c64fb2d2c4ceb1ae793",
   "sha_after": "3e88449b5463374fe9b6b0424df01e5b608b03fc8eb86c64fb2d2c4ceb1ae793",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/11_Figures/fig7_pulse_width.png",
   "sha_before": "fd98891335469bdc7cccc6f916c64d0855bf75fa7ce2814ca2307802064dc2b3",
   "sha_after": "fd98891335469bdc7cccc6f916c64d0855bf75fa7ce2814ca2307802064dc2b3",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2.json",
   "sha_before": "2c88206f6485d93f67f3dc318688a83663703280e0f0cd20213915180efc40c7",
   "sha_after": "2c88206f6485d93f67f3dc318688a83663703280e0f0cd20213915180efc40c7",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2_TABLES.md",
   "sha_before": "1533b7a35d8fdead7306849338163c668f74a8c88c2495beaa1402190acfcd10",
   "sha_after": "1533b7a35d8fdead7306849338163c668f74a8c88c2495beaa1402190acfcd10",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/10_Processed_Data/CONVERGENCE_RESULTS.json",
   "sha_before": "521783b7f7a31cb7a694b29cb23a7e7e63a8adafb7b4bc399c1951dcd25e3234",
   "sha_after": "521783b7f7a31cb7a694b29cb23a7e7e63a8adafb7b4bc399c1951dcd25e3234",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/10_Processed_Data/PRODUCTION_PROVENANCE.csv",
   "sha_before": "04613382ede7535a1201f15cc5819055303a42559192173bfb8e556bdfb6791c",
   "sha_after": "04613382ede7535a1201f15cc5819055303a42559192173bfb8e556bdfb6791c",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/12_Tables/D_lambda_eps.csv",
   "sha_before": "60562a2f0f7978601246df0145e303163a0502160af6c6af1c7c39b8ac5775bc",
   "sha_after": "60562a2f0f7978601246df0145e303163a0502160af6c6af1c7c39b8ac5775bc",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/12_Tables/ablations_E.csv",
   "sha_before": "22d26738f8a1b96120c2f89d175e186f7f7e68e76373a8a048130900c348008b",
   "sha_after": "22d26738f8a1b96120c2f89d175e186f7f7e68e76373a8a048130900c348008b",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/12_Tables/ablations_E_M.csv",
   "sha_before": "db9bf86515e0312d2dd3ec882f8988d484111754efe50d7db21f90c1cecd322c",
   "sha_after": "db9bf86515e0312d2dd3ec882f8988d484111754efe50d7db21f90c1cecd322c",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/12_Tables/convergence_ellipse_6phi.csv",
   "sha_before": "27023c279998d01730fb6daaecbc05ff074fb574d6a2fea0b6a225585f11183c",
   "sha_after": "27023c279998d01730fb6daaecbc05ff074fb574d6a2fea0b6a225585f11183c",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/12_Tables/phi_sweep_ellipse.csv",
   "sha_before": "9675e0d3b0ca6f8261cf441986335de4bd225fdcea0c694c3c275a07deb45f52",
   "sha_after": "9675e0d3b0ca6f8261cf441986335de4bd225fdcea0c694c3c275a07deb45f52",
   "identical": true
  },
  {
   "path": "PAPER_PROJECT/12_Tables/pulse_width_F.csv",
   "sha_before": "143f3b595e90dbeffc15b62b1302a384a5a2f028ac827feab71275c61be51cf7",
   "sha_after": "143f3b595e90dbeffc15b62b1302a384a5a2f028ac827feab71275c61be51cf7",
   "identical": true
  }
 ],
 "n_files_compared": 18,
 "n_changed": 0,
 "n_missing_after_run": 0,
 "reproduce_overall": "11 PASS, 0 FAIL",
 "notes": [
  "reproduce.py overwrote 07_Tests/REPRODUCTION_TEST_REPORT.md and 11_Figures/fig2_phi_sweep.png as part of its own procedure; that is by design, and `git checkout --` restores the shipped copies",
  "generated by PAPER_PROJECT/00_Project_Control/run_reproduction_check.py; the comparison is byte-level on purpose - a hash that matches settles the question, one that does not tells you exactly which artifact to look at"
 ]
}
```
