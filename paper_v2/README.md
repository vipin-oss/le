# Review manuscript, current build (v2)

- `paper_sources.zip`: complete LaTeX sources (main.tex, sections/, scripts/, figures/, tables/, refs.bib, refs_extra.bib, refs_new.bib).
- `main.pdf`: current build, 119 pages, 323 references.

Build: `pdflatex main; bibtex main; pdflatex main; pdflatex main`. Figures: run the scripts in `scripts/`.

Known to-do: verify `refs_extra.bib` (32 entries typed from memory) and spot-check `refs_new.bib` (Crossref/library-derived, first author only); the catalogue in Appendix D is classified by title keywords only.
