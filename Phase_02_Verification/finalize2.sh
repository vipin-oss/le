#!/bin/bash
# Phase 2 finalize, steps 4-7 only (rebuild documents, tex, gates, PDFs)
PY=/home/user/.venv-q1/bin/python
cd /home/user/le || exit 1
LOG=Phase_02_Verification/verification
echo "=== 4/8 rebuild manuscript + companion ==="
( cd PAPER_PROJECT/13_Manuscript && $PY build_manuscript.py > ../../$LOG/build_manuscript.log 2>&1; echo "ms exit=$?"; tail -4 ../../$LOG/build_manuscript.log
  $PY build_calculations.py > ../../$LOG/build_calculations.log 2>&1; echo "calc exit=$?"; tail -4 ../../$LOG/build_calculations.log )
echo "=== 5/8 tex + bib ==="
$PY tools/md_to_tex.py > $LOG/md_to_tex.log 2>&1; echo "md_to_tex exit=$?"; tail -2 $LOG/md_to_tex.log
$PY tools/md_to_tex.py -i PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md -o PAPER_PROJECT/13_Manuscript/FINAL_REVISED_CALCULATIONS.tex -c > $LOG/md_to_tex_calc.log 2>&1; echo "md_to_tex -c exit=$?"; tail -2 $LOG/md_to_tex_calc.log
$PY tools/refs_to_bib.py > $LOG/refs_to_bib.log 2>&1; echo "refs_to_bib exit=$?"; tail -1 $LOG/refs_to_bib.log
echo "=== 6/8 static gates ==="
$PY tools/audit_tex.py -t PAPER_PROJECT/13_Manuscript/FINAL_REVISED_MANUSCRIPT.tex -m PAPER_PROJECT/13_Manuscript/manuscript_IJHMT.md > $LOG/audit_ms.log 2>&1; echo "audit ms exit=$?"; tail -3 $LOG/audit_ms.log
$PY tools/audit_tex.py -c -t PAPER_PROJECT/13_Manuscript/FINAL_REVISED_CALCULATIONS.tex -m PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md > $LOG/audit_calc.log 2>&1; echo "audit calc exit=$?"; tail -3 $LOG/audit_calc.log
$PY tools/check_tex_commands.py > $LOG/check_commands.log 2>&1; echo "commands exit=$?"; tail -1 $LOG/check_commands.log
$PY tools/check_crossrefs.py > $LOG/check_crossrefs.log 2>&1; echo "crossrefs exit=$?"; tail -1 $LOG/check_crossrefs.log
$PY tools/test_md_to_tex.py > $LOG/conversion_tests.log 2>&1; echo "conversion tests exit=$?"; tail -1 $LOG/conversion_tests.log
$PY tools/renumber_crossrefs.py > $LOG/renumber.log 2>&1; echo "renumber exit=$?"; tail -1 $LOG/renumber.log
echo "=== 7/8 PDFs ==="
$PY tools/md_to_pdf.py > $LOG/pdf_ms.log 2>&1; echo "pdf ms exit=$?"; tail -1 $LOG/pdf_ms.log
$PY tools/md_to_pdf.py -i PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md -o PAPER_PROJECT/13_Manuscript/calculations_IJHMT.pdf -r "Worked calculations — cavity thermoelasticity in monoclinic beta-Ga2O3" > $LOG/pdf_calc.log 2>&1; echo "pdf calc exit=$?"; tail -1 $LOG/pdf_calc.log
$PY tools/verify_pdf.py > $LOG/verify_ms.log 2>&1; echo "verify ms exit=$?"; tail -4 $LOG/verify_ms.log
$PY tools/verify_pdf.py -p PAPER_PROJECT/13_Manuscript/calculations_IJHMT.pdf -m PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md -c -r "Worked calculations — cavity thermoelasticity in monoclinic beta-Ga2O3" > $LOG/verify_calc.log 2>&1; echo "verify calc exit=$?"; tail -4 $LOG/verify_calc.log
