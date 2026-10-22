#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Surface concise diagnostics as GitHub check annotations when a build command
# fails, since the signed Actions log/artifact endpoints may not be reachable.
report_failure() {
  local rc=$?
  trap - ERR
  if [[ "${GITHUB_ACTIONS:-}" == "true" ]]; then
    printf '::error title=Phase5 build failure::line %s; exit %s; command: %s\n' "${BASH_LINENO[0]:-?}" "$rc" "${BASH_COMMAND//%/%25}"
    for logfile in "$ROOT/master/build/latexmk.log" "$ROOT/master/build/main.log" "$ROOT/master/build/main.blg"; do
      if [[ -f "$logfile" ]]; then
        while IFS= read -r line; do
          line=${line//%/%25}; line=${line//$'\r'/%0D}
          printf '::error title=%s diagnostic::%s\n' "$(basename "$logfile")" "$line"
        done < <(grep -niE '^! |error|couldn.t|not found|undefined|Overfull \\\\([hv]box)' "$logfile" | head -40 || true)
      fi
    done
    if [[ -f "$ROOT/master/build/latexmk.log" ]]; then
      while IFS= read -r line; do
        line=${line//%/%25}; line=${line//$'\r'/%0D}
        printf '::error title=latexmk tail::%s\n' "$line"
      done < <(tail -20 "$ROOT/master/build/latexmk.log")
    fi
  fi
  exit "$rc"
}
trap report_failure ERR

for cmd in latexmk pdflatex bibtex pdffonts pdfinfo; do
  command -v "$cmd" >/dev/null || { echo "ERROR: required build tool not found: $cmd" >&2; exit 127; }
done
python3 "$ROOT/scripts/audit_inventory.py"
"$ROOT/scripts/build_figures.sh"
python3 "$ROOT/scripts/validate_figures.py"
cd "$ROOT/master"
mkdir -p build
latexmk -C -outdir=build main.tex
# BibTeX runs from the auxiliary/output directory under -outdir; place the
# local database there and also expose the source tree for TeX inputs.
cp references_local.bib build/references_local.bib
export TEXINPUTS="$PWD//:${TEXINPUTS:-}"
export BIBINPUTS="$PWD//:${BIBINPUTS:-}"
latexmk -pdf -g -interaction=nonstopmode -file-line-error -halt-on-error -outdir=build main.tex 2>&1 | tee build/latexmk.log
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
