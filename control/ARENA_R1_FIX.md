# ARENA — ROUND 1 FIX ORDER (Mission: most reliable, most-cited review on wave mechanics in generalized continua, target AMR. Round: R1 build gate)
Read control/BLUEPRINT.md first. Work on your own arena/* branch (arena/40393d9f-le). control/ and verification/ are read-only for you.

## Claude's independent build of your branch (commit c185ce8), TeX Live pdflatex+bibtex, same 4-pass sequence as phase5/scripts/build_master.sh
Your CI failed with a bare exit 1 because pdflatex hits FATAL errors. They are only these three (all introduced by the v1.1 edits; v1.0 did not have them):
1. phase5/master/sections/sec04_thermoelastic.tex:17, sec17_conclusions.tex:49, sec16_future.tex:325, sec15_challenges.tex:360: the command `\ref` was destroyed. The text reads `Figure~<newline>ef{fig:...}` (backslash-r was turned into a newline by a string/escape bug in whatever script or edit produced the text). Restore `\ref{...}`.
2. phase5/master/appendices/appF_reproducibility.tex:6: `\texttt{../README_build.md}` (and every other \texttt with an underscore): underscores must be escaped `\_` (or use \path/\detokenize). Fixed in the patch for the whole file.
3. phase5/master/appendices/energy_flux_derivations.tex:344: markdown-style backticks `-phi dot(D_i)` in LaTeX text mode: the underscore causes "Missing $ inserted". Replaced by a math expression in the patch.
Ready-made patch (applies to phase5/master only): control/patches/r1_build_fixes.patch  (`git apply` it, or redo the same edits).
ROOT CAUSE TO FIX, not only the symptoms: find what produced `\r`->newline. Re-scan ALL files you generated or edited in v1.1 (tex, bib, csv, md) for other escape damage: lines starting with `ef{`, `ight`, `ho`, `angle`, `abla`, `ewcommand`, `extbf`, `heta`, tabs, form feeds. Report what you found.

## Result of that build after the three fixes (so you know what "green" looks like)
148 pages, 0 LaTeX errors, 0 undefined citations/references, bibtex clean, scratch text ("Wait, this simplification...") gone. STILL OPEN (your remaining R1 work): 686 Overfull \hbox warnings, worst 517 pt, 246 pt, 129 pt, 98 pt, 97 pt (tables: tabularx/longtable layout in sec06, sec07, sec15, sec16 and T1-T8); 148 pages vs 161 in v1.0 -> explain exactly what content was removed or moved (do not hide it).

## Gate to pass R1 (all must be shown with logs/commit hash, no PASS without execution)
a) fresh clone: `bash phase5/scripts/build_master.sh` exits 0 in CI, and the CI run link/number is given.
b) 0 errors, 0 undefined refs/cites, no hbox overfull above 10 pt anywhere, none in tables.
c) font embedding report, page count, pdfinfo, and a contact sheet of the final PDF pages saved under phase5/reports/.
d) DEFECT_STATUS.csv updated: every defect FIXED/PARTLY/NOT DONE/DISPUTED with evidence.
e) Do NOT touch scientific content in this round except where the fix requires it; log every content change in DECISIONS.
Push, then report commit hash and CI run number in chat.

## UPDATE 12:55 IST — Claude rebuilt arena/40393d9f-le @4e2a062 (your own fixes): 0 LaTeX errors, 148 pp, 0 undefined. Fatal defects are GONE. Do not spend more CI runs on error hunting.
Remaining R1 work is ONLY layout. 683 Overfull, 299 of them > 10 pt, concentrated on a few pages (see control/reports/overfull_by_page_4e2a062.md, pages of Claude's 148-page build):
- p31 (Table 3 "Wave types and governing characteristics", 180 boxes, 73 > 10 pt), p84 (Table 22 "limiting relationships between the families", 229 boxes), p96 (section 14.4 table, 101 boxes), p120 (157 boxes, worst 246 pt), p82 (single 517 pt box next to Table 20 notation), p66 (98 pt), p62 (80 pt), p30 (63 pt).
- Fix by redesigning those tables: landscape/sidewaystable or split tables, `tabularx`/`\small`+`\raggedright` `p{}` columns with explicit widths, shorter cell text, `\allowbreak` in long macros/paths. No unbreakable \texttt strings. Rebuild with 4 passes locally if you can get a TeX; otherwise use ONE CI run per batch of fixes, not per single fix.
- Explain 161 -> 148 pages (what was removed/merged).
Gate b) of R1 (no overfull > 10 pt) stays open until this is done.
