#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
for cmd in latexmk pdflatex bibtex pdffonts pdfinfo; do
  command -v "$cmd" >/dev/null || { echo "ERROR: required build tool not found: $cmd" >&2; exit 127; }
done
python3 "$ROOT/scripts/audit_inventory.py"
"$ROOT/scripts/build_figures.sh"
python3 "$ROOT/scripts/validate_figures.py"
cd "$ROOT/master"
mkdir -p build
latexmk -C -outdir=build main.tex
latexmk -pdf -g -interaction=nonstopmode -file-line-error -halt-on-error -outdir=build main.tex
python3 "$ROOT/scripts/check_build_log.py" build/main.log
pdfinfo build/main.pdf | tee build/pdfinfo.txt
pdffonts build/main.pdf | tee build/pdffonts.txt
if grep -qvE '^(name|[-[:space:]]|$)' build/pdffonts.txt; then
  if awk 'NR>2 && $4 != "yes" {bad=1; print "UNEMBEDDED FONT:", $0} END {exit bad}' build/pdffonts.txt; then
    echo "All reported PDF fonts are embedded."
  else
    echo "ERROR: at least one font is not embedded." >&2
    exit 1
  fi
fi
printf 'Build complete: %s\n' "$ROOT/master/build/main.pdf"
