#!/bin/bash
# Phase 2 finalize — run after the production runs and the verification suite have finished.
# Each step is logged under Phase_02_Verification/verification/; nothing here deletes a prior artifact.
PY=/home/user/.venv-q1/bin/python
cd /home/user/le || exit 1
LOG=Phase_02_Verification/verification
mkdir -p $LOG
run () { echo "### $*"; "$@" > "$LOG/$1.log" 2>&1; echo "exit=$? -> $LOG/$1.log"; }

#[ ] echo "=== 1/8 re-analysis (adds E_ablations_M, matched-grid control, per-pulse-width wall errors) ==="
cp PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2.json $LOG/ANALYSIS_V2_before_phase2.json
$PY PAPER_PROJECT/08_Experiments/analyze_v2.py > $LOG/analyze_v2.log 2>&1; echo "analyze exit=$?"
tail -4 $LOG/analyze_v2.log
$PY Phase_02_Verification/diff_analysis.py $LOG/ANALYSIS_V2_before_phase2.json PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2.json > $LOG/ANALYSIS_DIFF.md 2>&1
head -6 $LOG/ANALYSIS_DIFF.md

echo "=== 2/8 provenance table + test report ==="
$PY PAPER_PROJECT/08_Experiments/make_provenance.py > $LOG/make_provenance.log 2>&1; echo "provenance exit=$?"; tail -2 $LOG/make_provenance.log
$PY PAPER_PROJECT/07_Tests/make_test_report.py > $LOG/make_test_report.log 2>&1; echo "test report exit=$?"; tail -2 $LOG/make_test_report.log

echo "=== 3/8 code freeze (six .py files changed in this phase) ==="
$PY PAPER_PROJECT/06_Source_Code/make_code_freeze.py submission_2026_10_03b > $LOG/make_code_freeze.log 2>&1; echo "freeze exit=$?"; tail -3 $LOG/make_code_freeze.log

echo "=== 4/8 rebuild manuscript + companion ==="
( cd PAPER_PROJECT/13_Manuscript && $PY build_manuscript.py > ../../$LOG/build_manuscript.log 2>&1; echo "ms exit=$?"; tail -3 ../../$LOG/build_manuscript.log
  cd /home/user/le/PAPER_PROJECT/13_Manuscript && $PY build_calculations.py > ../../$LOG/build_calculations.log 2>&1; echo "calc exit=$?"; tail -3 ../../$LOG/build_calculations.log )

echo "=== 5/8 tex + bib ==="
$PY tools/md_to_tex.py > $LOG/md_to_tex.log 2>&1; echo "md_to_tex exit=$?"; tail -2 $LOG/md_to_tex.log
$PY tools/md_to_tex.py -i PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md -o PAPER_PROJECT/13_Manuscript/FINAL_REVISED_CALCULATIONS.tex -c > $LOG/md_to_tex_calc.log 2>&1; echo "md_to_tex -c exit=$?"; tail -2 $LOG/md_to_tex_calc.log
$PY tools/refs_to_bib.py > $LOG/refs_to_bib.log 2>&1; echo "refs_to_bib exit=$?"; tail -2 $LOG/refs_to_bib.log

echo "=== 6/8 static gates ==="
$PY tools/audit_tex.py -t PAPER_PROJECT/13_Manuscript/FINAL_REVISED_MANUSCRIPT.tex -m PAPER_PROJECT/13_Manuscript/manuscript_IJHMT.md > $LOG/audit_ms.log 2>&1; echo "audit ms exit=$?"; tail -3 $LOG/audit_ms.log
$PY tools/audit_tex.py -c -t PAPER_PROJECT/13_Manuscript/FINAL_REVISED_CALCULATIONS.tex -m PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md > $LOG/audit_calc.log 2>&1; echo "audit calc exit=$?"; tail -3 $LOG/audit_calc.log
$PY tools/check_tex_commands.py > $LOG/check_commands.log 2>&1; echo "commands exit=$?"; tail -2 $LOG/check_commands.log
$PY tools/check_crossrefs.py > $LOG/check_crossrefs.log 2>&1; echo "crossrefs exit=$?"; tail -2 $LOG/check_crossrefs.log
$PY tools/test_md_to_tex.py > $LOG/conversion_tests.log 2>&1; echo "conversion tests exit=$?"; tail -2 $LOG/conversion_tests.log
$PY tools/renumber_crossrefs.py > $LOG/renumber.log 2>&1; echo "renumber exit=$?"; tail -2 $LOG/renumber.log

echo "=== 7/8 PDFs ==="
$PY tools/md_to_pdf.py > $LOG/pdf_ms.log 2>&1; echo "pdf ms exit=$?"; tail -2 $LOG/pdf_ms.log
$PY tools/md_to_pdf.py -i PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md -o PAPER_PROJECT/13_Manuscript/calculations_IJHMT.pdf -r "Worked calculations — cavity thermoelasticity in monoclinic beta-Ga2O3" > $LOG/pdf_calc.log 2>&1; echo "pdf calc exit=$?"; tail -2 $LOG/pdf_calc.log
$PY tools/verify_pdf.py > $LOG/verify_ms.log 2>&1; echo "verify ms exit=$?"; tail -3 $LOG/verify_ms.log
$PY tools/verify_pdf.py -p PAPER_PROJECT/13_Manuscript/calculations_IJHMT.pdf -m PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md -c -r "Worked calculations — cavity thermoelasticity in monoclinic beta-Ga2O3" > $LOG/verify_calc.log 2>&1; echo "verify calc exit=$?"; tail -3 $LOG/verify_calc.log

echo "=== 8/8 done ==="
