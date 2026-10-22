# Phase5 v1.1 master source build notes

## Build prerequisites

The reproducible script expects `latexmk`, `pdflatex`, `bibtex`, `pdfinfo`, `pdffonts`, Python 3, Node.js/npm, and the pinned JavaScript dependencies in `../tools/package-lock.json`. The GitHub workflow installs the TeX/PDF toolchain and runs `npm ci` before invoking the build.

## Build command

From the repository root:

```sh
npm --prefix phase5/tools ci --ignore-scripts
bash phase5/scripts/build_master.sh
```

The script runs the static inventory check, regenerates the 18 figure PDFs from their SVG sources, validates figure assets, cleans and compiles the master with `latexmk`, checks the LaTeX log for fatal errors, unresolved refs/citations, missing graphics and overfull hboxes above 1 pt, and records PDF page/font metadata. It fails fast. Run it only after installing all prerequisites.

The workflow produces the new manuscript at `phase5/master/build/main.pdf`; this is a new v1.1 build only if the command succeeds from the current source. Do not substitute `v1.0-baseline.pdf`, which is a preserved 161-page pre-edit artifact. Inspect the full log and every final page; a successful compilation alone does not establish scientific correctness.

## Package topology

- `master/`: editable LaTeX source, local bibliography, build configuration, and preserved v1.0 baseline.
- `master/tables/source/`: portable table inputs copied for the manuscript.
- `master/figures/source/`: editable SVG artwork and generated PDF renditions.
- `../scripts/`: build, figure conversion, inventory, and audit utilities.
- `../reports/`: scientific, literature, figure, build, provenance, and quality-gate records.

The original phase4 source tree is preserved. See `../reports/version-provenance.md` for the precise artifact distinction and current blockers.
