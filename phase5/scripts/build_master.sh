#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Surface concise diagnostics as GitHub check annotations when a build command
# fails, since the signed Actions log/artifact endpoints may not be reachable.
failure_reported=0
report_failure() {
  local rc=$?
  if (( rc == 0 || failure_reported )); then return 0; fi
  failure_reported=1
  local command=${BASH_COMMAND}
  trap - ERR EXIT
  set +e
  if [[ "${GITHUB_ACTIONS:-}" == "true" ]]; then
    printf '::error title=Phase5 build failure::exit %s; command: %s\n' "$rc" "${command//%/%25}"
    for logfile in "$ROOT/master/build/process.log" "$ROOT/master/build/main.log" "$ROOT/master/build/main.blg"; do
      if [[ -f "$logfile" ]]; then
        while IFS= read -r line; do
          line=${line//%/%25}; line=${line//$'\r'/%0D}
          printf '::error title=%s-diagnostic::%s\n' "$(basename "$logfile")" "$line"
        done < <(grep -niE '^! |error|couldn.t|not found|undefined|Overfull \\\\([hv]box)' "$logfile" | head -3 || true)
      fi
    done
    if [[ -f "$ROOT/master/build/process.log" ]]; then
      local tail_summary
      tail_summary=$(tail -35 "$ROOT/master/build/process.log" | tr '\n' ' ')
      tail_summary=${tail_summary//%/%25}; tail_summary=${tail_summary//$'\r'/%0D}
      printf '::error title=Phase5 build-log tail::%s\n' "$tail_summary"
    fi
  fi
  exit "$rc"
}
trap report_failure ERR EXIT

for cmd in latexmk pdflatex bibtex pdffonts pdfinfo; do
  command -v "$cmd" >/dev/null || { echo "ERROR: required build tool not found: $cmd" >&2; exit 127; }
done
python3 "$ROOT/scripts/audit_inventory.py"
"$ROOT/scripts/build_figures.sh"
python3 "$ROOT/scripts/validate_figures.py"
cd "$ROOT/master"
mkdir -p build
latexmk -C -outdir=build main.tex
: > build/process.log
# Keep source includes/figures resolvable from the master directory while
# directing all generated TeX files to build/. Run BibTeX from build/ so it
# resolves main.aux and any auxiliary files relative to the output directory;
# BIBINPUTS exposes the source-local database.
export TEXINPUTS="$PWD/build//:$PWD//:${TEXINPUTS:-}"
export BIBINPUTS="$PWD//:${BIBINPUTS:-}"
run_pdflatex() {
  local pass="$1"
  printf '\n=== pdfLaTeX pass %s ===\n' "$pass" | tee -a build/process.log
  pdflatex -interaction=nonstopmode -file-line-error -halt-on-error -output-directory=build main.tex 2>&1 | tee "build/pass${pass}.log" | tee -a build/process.log
}
run_pdflatex 1
printf '\n=== BibTeX (from output directory) ===\n' | tee -a build/process.log
(
  cd build
  bibtex main 2>&1 | tee bibtex.log | tee -a process.log
)
run_pdflatex 2
run_pdflatex 3
run_pdflatex 4
printf '\n=== Build-log gates ===\n' | tee -a build/process.log
python3 "$ROOT/scripts/check_build_log.py" build/main.log 2>&1 | tee -a build/process.log
printf '\n=== PDF metadata ===\n' | tee -a build/process.log
pdfinfo build/main.pdf | tee build/pdfinfo.txt | tee -a build/process.log
printf '\n=== PDF fonts ===\n' | tee -a build/process.log
pdffonts build/main.pdf | tee build/pdffonts.txt | tee -a build/process.log
if grep -qvE '^(name|[-[:space:]]|$)' build/pdffonts.txt; then
  if awk 'NR>2 && $4 != "yes" {bad=1; print "UNEMBEDDED FONT:", $0} END {exit bad}' build/pdffonts.txt; then
    echo "All reported PDF fonts are embedded."
  else
    echo "ERROR: at least one font is not embedded." >&2
    false
  fi
fi
printf 'Build complete: %s\n' "$ROOT/master/build/main.pdf"
