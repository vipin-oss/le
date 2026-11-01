# Build instructions

This is the short build entry point; the current scientific/build state is in [`README.md`](README.md) and [`reports/build-status.md`](reports/build-status.md).

CI runs [`.github/workflows/latex-build.yml`](../.github/workflows/latex-build.yml) in a prebuilt TeX Live container. For a local Linux build, install complete TeX Live (`latexmk`, `pdflatex`, `bibtex`, `pdffonts`), Python 3 with `venv`, Node.js 20/npm, Poppler utilities, and DejaVu fonts. From the repository root:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r phase5/tools/requirements-audit.txt
npm ci --prefix phase5/tools
bash phase5/scripts/build_master.sh
```

The compiled PDF and diagnostic logs are written to `phase5/master/build/`. CI publishes the validated PDF and overview sheets under `phase5/build_outputs/`. A successful build is not a scientific verification or submission-readiness result.
