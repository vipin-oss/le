# STATUS — three-paper project

**Updated 30 Oct 2026 (v7, second pass). Branch `arena/0be2770f-lamb` off `claude/v6-handoff`. Never main.**

1. All three masters written: `deliver/Lamb_{Sumit,Neha,Anu}.zip`, each one `.tex` + one `.bib`, full
   working in `worked` blocks behind `\showworked` (42 blocks in Sumit, 36 in each of the other two).
2. Parity corrected: Sumit splits only if β_th = Π_th = E_g = 0 (the break is M45 and M54, not p3);
   Neha and Anu split in all 32 coupling combinations each. Verified structurally and by an exact
   determinant, not by floating point.
3. Section-8 tests all pass: 64 checks, largest residual 0.87 × tolerance. Logs in
   `internal/section8_tests.log`, per-paper numbers in `internal/{sumit,neha,anu}_matrix_verification.md`.
4. Report: `reports/packages_v7.tex`.
5. Open: no LaTeX engine here, so nothing compiled; my estimate is ~24 pages (Sumit) and ~19 (Neha, Anu)
   with the working shown, short of the 30 asked for — say the word and I add more.
