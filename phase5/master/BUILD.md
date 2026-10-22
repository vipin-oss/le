# Phase5 v1.1 master source build notes

## Build prerequisites

The reproducible script expects `latexmk` (for cleaning), `pdflatex`, `bibtex`, `pdfinfo`, `pdffonts`, Python 3, Node.js/npm, and the pinned JavaScript dependencies in `../tools/package-lock.json`. The GitHub workflow installs the TeX/PDF toolchain and runs `npm ci` before invoking the build.

## Build command

From the repository root:

```sh
npm --prefix phase5/tools ci --ignore-scripts
bash phase5/scripts/build_master.sh
```

The script runs static source and figure checks, regenerates the 18 figure PDFs from SVG, cleans generated outputs, then runs four fail-fast pdfLaTeX passes with an explicit BibTeX step. It sets source/include and bibliography search paths, checks the final log for fatal errors, unresolved refs/citations, missing graphics, and overfull boxes above 1 pt, and records PDF page/font metadata. No LaTeX errors or warnings are suppressed.

Output is `phase5/master/build/main.pdf`. A PDF is a v1.1 build only if this command succeeds from the current source. Do not substitute `v1.0-baseline.pdf`, which is a preserved 161-page pre-edit artifact. Inspect the full logs and every final page; successful compilation alone does not establish scientific correctness.

## Package topology

- `master/`: editable LaTeX source, local bibliography, build configuration, and preserved v1.0 baseline.
- `master/tables/source/`: portable table inputs copied for the manuscript.
- `master/figures/source/`: editable SVG artwork and generated PDF renditions.
- `../scripts/`: build, figure conversion, inventory, and audit utilities.
- `../reports/`: scientific, literature, figure, build, provenance, and quality-gate records.

The original phase4 source tree is preserved. See `../reports/version-provenance.md` for artifact distinctions and current blockers.
