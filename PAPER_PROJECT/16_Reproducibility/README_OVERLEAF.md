# README_OVERLEAF

## Files in this folder

| file | role |
|---|---|
| `FINAL_REVISED_MANUSCRIPT.tex` | the manuscript, single-file source (no `\input`/`\include` of other .tex files, so nothing else can go missing) |
| `FINAL_REVISED_CALCULATIONS.tex` | the derivation/numerics companion (same preamble, separate document; submitted as supplementary or kept with the code, author decision B8) |
| `FINAL_REVISED_REFERENCES.bib` | the bibliography, 55 entries |
| `figures/fig*.pdf` | the 8 vector figures the manuscript includes |
| `figures/README.txt` | how the figure set was produced |
| `highlights.txt` | the five highlights, as a text file for the submission system |

## In Overleaf

1. New project -> upload **this whole folder** (zip it as-is keeps `figures/` next to the source).
2. Menu -> Main document: `FINAL_REVISED_MANUSCRIPT.tex`. There is deliberately **no `main.tex`** in
   this archive: a second copy under another name is exactly how two competing "final" manuscripts
   get submitted. If a template insists on the name, rename the file rather than copying it.
3. Compiler: pdfLaTeX (default). BibTeX is run automatically by Overleaf when the document uses
   `\bibliography{...}` as this one does (2 line).

## Class and style files

- `\documentclass[preprint,12pt]{elsarticle}` and `\bibliographystyle{elsarticle-num}` are used
  as written. The class and `.bst` are **not vendored** here: `elsarticle.cls` is not present
  anywhere in the repository, and shipping an unverified copy would be worse than saying so.
  Both are provided by TeX Live (package `texlive-publishers`) and are preinstalled on Overleaf.
  Switching to the journal layout is a one-token change (`5p`, or `review` for double-spaced
  refereeing) - the author decision recorded as B1 in `08_FINAL_OUTPUTS/manuscript/AUTHOR_INPUT_REQUIRED.md`.
- The source defines 0 of its own macros (``); no `\input{macros}` exists.

## Static verification of this folder (no TeX engine exists in the packaging environment)

| check | result |
|---|---|
| `\input` / `\include` of other sources | none used (0 occurrences), so no missing subfiles |
| `\includegraphics` targets (8): fig1_setup, fig4_verification, fig6a_mesh, fig3_wall_profiles, fig2_phi_sweep, fig7_pulse_width, fig6b_ablation, fig5_memory | all resolve to `figures/fig*.pdf` in this folder |
| `\graphicspath` | `figures/` - resolved the same way pdflatex does, including extension probing |
| `\cite` keys used (55) vs keys in the `.bib` (55) | every cited key exists |
| bibliography entries never cited | 0 (none) |
| labels / references (154 / 130) | resolved by `tools/check_crossrefs.py`: see transcript |
| undefined-command scan (`tools/check_tex_commands.py`) | see 09_ARCHIVE_METADATA/VERIFICATION_GATES.txt |
| `elsarticle-num` numbering vs the printed numbers in the .md/PDF | the .tex is numbered by first citation (Phase 1); the mapping is in `08_FINAL_OUTPUTS/manuscript/REF_ORDER.json` and `REFERENCES_ORDERED.json` |

## What was NOT done here

- **The `.tex` has never been compiled by the people who wrote it.** No TeX engine exists in this
  sandbox (no `pdflatex`, `apt` unavailable to the sandbox user), so the compile is the author-side
  step in the checklist. The archive therefore records `NOT COMPILED IN THIS ENVIRONMENT`, together
  with the four commands to run and the log to check. A static check is not a compile: it catches
  missing files, undefined commands and dangling references, not overfull boxes or float placement.
- Scientific content was not touched to make anything compile; the requirement "do not change
  science to compile" is honoured by not compiling-and-editing here at all.
