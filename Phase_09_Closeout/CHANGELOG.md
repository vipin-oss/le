# Phase 9 changelog

- Added `verification/export_submission_figures.py`: wraps `Figure.savefig` and runs the frozen
  `08_Experiments/make_figures.py` unchanged to emit 600-dpi PNG and LZW TIFF renditions plus
  vector PDFs of all eight figures into `PAPER_PROJECT/11_Figures/submission/`; reads the dpi back
  out of each file (PNG pHYs / TIFF IFD) and reports OK/PROBLEM; restores `11_Figures/` from git
  afterwards and verifies the frozen PNGs are byte-identical.
- `11_Figures/submission/`: 8 vector PDFs + README.txt tracked, raster renditions gitignored with
  the regeneration command recorded in `.gitignore`.
- Built the cumulative packages with `00_Project_Control/make_packages.py final`
  (`RESEARCH_PROJECT_FINAL.zip`, 610 files, 52.2 MB, MANIFEST.json with SHA-256 per file), so the
  "Start here" pointer and the deposit statement now have a real object behind them.
- `tools/connection_audit.py`: the missing-packages failure is gone; only the working-tree check
  remained and the phase commit clears it.
- No builder, document or code-freeze entry changed: no rebuild, no new manifest; verify_pdf and
  the static gates pass as before, and `final_consistency.py` still reports 0 failures.
