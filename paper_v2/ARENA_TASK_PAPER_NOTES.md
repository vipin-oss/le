# Arena task: per-paper notes for the review (read the papers; invent nothing)

Goal: the manuscript currently lists cited works by name/number (Table 2, Appendix catalogue) without saying what each work did. A critical review must say what each study did, with what model/method, what it found, and what its limit is. Build the evidence base for that.

## Inputs
- Reference list: `refs*.bib` in `overleaf_package.zip` (416 cited keys; the list actually printed is in `main.bbl`).
- Full texts: the author's Google Drive PDFs (file names are publisher codes, e.g. bf01135371.pdf, 1.4026911.pdf, physrevlett.86.2297.pdf). Match each PDF to a bib key through the DOI/title on its first page. Books in Drive (Tzou, Ignaczak and Ostoja-Starzewski, Auld, Laude) are chapters/sources, not abstracts.
- For works with no PDF in Drive: use the publisher/Crossref/arXiv abstract by DOI. If no abstract can be obtained, write NOT-READ. Do not guess from the title.

## Deliverable 1: `paper_v2/paper_notes.csv`
One row per cited bib key. Columns:
`bibkey, doi, source_used (FULLTEXT|ABSTRACT|NOT-READ), problem_geometry, heat_law, coupled_fields, method, main_result (1 sentence, only what the source states), limitation_or_caveat (1 sentence, only if the source states it or it follows directly from the setup, else empty), used_in_sections (where the manuscript cites it), tier (1|2)`
Rules: every statement must be traceable to the text read; quote numbers exactly; no evaluation words (novel, important) unless the source says so; if the manuscript attributes something to the work that the source does not support, put it in a second file `paper_v2/attribution_mismatches.csv` (bibkey, manuscript line, claim, what source says).

Tier 1 = works whose results are used in the manuscript's argument (about 60-80). Tier 2 = the rest.

## Deliverable 2: `paper_v2/cluster_synthesis.md`
For each cluster of Table 2 (plane waves/stability, surface waves, reflection, interfaces, transient, damping in resonators, fractional/memory, size effects, variational/uniqueness): 4-8 sentences stating, from paper_notes.csv only, what the cluster studied, which heat laws/geometries recur, whether parameters were tied to measurement, and which comparisons are missing. Cite bibkeys.

## Deliverable 3: `paper_v2/missing_literature.csv`
Works the review should cite but does not (experimental thermal transport: hydrodynamic phonons, ballistic transport, TDTR; resonator TED measurements; Guyer-Krumhansl/nonequilibrium thermodynamics: Cimmelli, Kovacs, Van, Sellitto, Jou; Straughan; MGT: Kaltenbacher et al.). Columns: `doi, authors, title, year, why_needed, section_where_it_belongs`. Every DOI must be resolved against Crossref and the title/author/year compared with the record. Max 40 rows, best first.

## Constraints
- Do not edit manuscript sources. Work only on the files above.
- Report counts: how many FULLTEXT, ABSTRACT, NOT-READ, and mismatches found.
- Commit to branch `review-paper-v2`, folder `paper_v2/`.
