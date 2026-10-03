#!/usr/bin/env bash
# compile_check.sh - author-side LaTeX compile check for the submission source.
#
# The sandbox in which this manuscript was produced has no TeX engine, so the two
# .tex files were verified statically only (tools/audit_tex.py, check_tex_commands.py,
# check_crossrefs.py, test_md_to_tex.py). Run this script once on a machine with TeX
# Live (or MiKTeX) installed; it writes COMPILE_CHECK.txt next to the sources and
# prints a verdict. It does not modify any document.
#
# Usage:  bash Phase_10_Submission_Package/compile_check.sh [dir-with-tex]
#         (default: PAPER_PROJECT/13_Manuscript)
set -u

ROOT=$(cd "$(dirname "$0")/.." && pwd)
MS=${1:-"$ROOT/PAPER_PROJECT/13_Manuscript"}
OUT="$MS/COMPILE_CHECK.txt"
PY=${PYTHON:-python3}

: > "$OUT"
say() { printf '%s\n' "$*" | tee -a "$OUT"; }

say "LaTeX compile check - $(date -Is)"
say "source dir: $MS"

if ! command -v pdflatex >/dev/null 2>&1; then
  say "RESULT: NO ENGINE - pdflatex not found on PATH."
  say "Install TeX Live (or MiKTeX) and rerun, or run the same steps by hand:"
  say "  cd $MS"
  say "  pdflatex FINAL_REVISED_MANUSCRIPT.tex && bibtex FINAL_REVISED_MANUSCRIPT && pdflatex FINAL_REVISED_MANUSCRIPT && pdflatex FINAL_REVISED_MANUSCRIPT"
  say "  pdflatex FINAL_REVISED_CALCULATIONS.tex && bibtex FINAL_REVISED_CALCULATIONS && pdflatex FINAL_REVISED_CALCULATIONS && pdflatex FINAL_REVISED_CALCULATIONS"
  say "The document class needed is elsarticle.cls (bundled with current TeX Live;"
  say "otherwise download it from Elsevier's LaTeX toolchain page and keep it beside the .tex)."
  say "Also re-run the static gates, which do work without TeX:"
  say "  \$PY tools/audit_tex.py && \$PY tools/check_crossrefs.py && \$PY tools/check_tex_commands.py"
  exit 2
fi

rc=0
for base in FINAL_REVISED_MANUSCRIPT FINAL_REVISED_CALCULATIONS; do
  tex="$MS/$base.tex"
  say ""
  say "== $base"
  if [ ! -f "$tex" ]; then say "  MISSING: $tex"; rc=1; continue; fi
  if [ ! -d "$MS/figures" ]; then
    say "  WARNING: no figures/ folder - regenerate it with"
    say "           \$PY Phase_10_Submission_Package/verification/make_tex_figure_set.py"
    say "           (without it, md_to_tex.py falls back to ../11_Figures/*.png paths)"
  fi
  tmp=$(mktemp -d)
  cp "$tex" "$MS/FINAL_REVISED_REFERENCES.bib" "$tmp"/ 2>/dev/null
  cp -r "$MS/figures" "$tmp"/ 2>/dev/null
  ( cd "$tmp" && pdflatex -interaction=nonstopmode "$base.tex" >pass1.log 2>&1;
    bibtex "$base" >bibtex.log 2>&1 || true
    pdflatex -interaction=nonstopmode "$base.tex" >pass2.log 2>&1
    pdflatex -interaction=nonstopmode "$base.tex" >pass3.log 2>&1 )
  log="$tmp/pass3.log"
  if [ ! -f "$tmp/$base.pdf" ]; then
    say "  FAIL no PDF produced; last 25 log lines:"
    tail -25 "$log" 2>/dev/null | sed 's/^/    /' | tee -a "$OUT"
    rc=1; rm -rf "$tmp"; continue
  fi
  pages=$("$PY" -c "
import re,sys
t=open('$log',encoding='utf-8',errors='replace').read()
m=re.findall(r'Output written on .*\((\d+) pages', t)
print(m[-1] if m else '?')" 2>/dev/null || echo '?')
  und_cite=$(grep -c "Citation .* undefined" "$log" 2>/dev/null || true)
  und_ref=$(grep -c "Reference .* undefined" "$log" 2>/dev/null || true)
  overfull=$(grep -cE "Overfull \\\\hbox \(([0-9]{2,}[0-9]*\.[0-9]+)pt" "$log" 2>/dev/null || true)
  warn_bib=$(grep -ci "warning" "$tmp/bibtex.log" 2>/dev/null || true)
  say "  pdf     : $tmp/$base.pdf -> $pages pages"
  say "  undefined citations: $und_cite (must be 0)"
  say "  undefined references : $und_ref (must be 0)"
  say "  overfull hboxes >= 100pt: $overfull (copy-editing signal, not a blocker)"
  say "  bibtex warnings      : $warn_bib"
  if [ "$und_cite" != "0" ] || [ "$und_ref" != "0" ]; then rc=1; fi
  cp "$tmp/$base.pdf" "$MS/COMPILE_CHECK_$base.pdf" 2>/dev/null
  say "  compiled PDF copied to $MS/COMPILE_CHECK_$base.pdf for inspection"
  rm -rf "$tmp"
done

say ""
if [ "$rc" = "0" ]; then
  say "RESULT: PASS - both documents compiled with no undefined citation or reference."
  say "Uploaded files: the .tex sources, FINAL_REVISED_REFERENCES.bib and the figures/ folder."
else
  say "RESULT: PROBLEMS - see the counters above (report them rather than editing the .tex by hand:"
  say "the sources are generated; change the builder and rerun tools/md_to_tex.py)."
fi
say ""
say "Report this file back to the project (it is the only record of the compile)."
exit "$rc"
