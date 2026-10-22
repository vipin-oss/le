# BRAVE — GO for PHASE B2 (read control/BLUEPRINT.md first; Mission: most reliable, most-cited review on wave mechanics in generalized continua, target AMR; Round: R2-prep, independent verification)

Claude's audit of your B1 (what was checked, what was not):
- CONFIRMED independently: AMR 1986 and 1998 thermoelasticity-with-second-sound reviews by Chandrasekharaiah exist (the DOI 10.1115/1.3098984 page says 2009 because ASME digitised it later; print year 1998 is fine, keep both facts); AMR author page says editor proposal is recommended; no maximum author number is stated on the author-info page; the Research Square preprint exists (Connor Noble, single author, posted 28 Aug 2026, not peer reviewed).
- NOT confirmed: the quote "Length: open". The AMR author-info page I read does not state a review length. Give the exact URL and the exact sentence where you saw it, or downgrade to UNVERIFIED.
- CORRECTION to your risk note: the preprint is a critical narrative review of Fourier-Biot, Cattaneo/LS, GL, GN, DPL, Guyer-Krumhansl and MGT with 4 propositions; it does NOT cover interface energy partition. So the overlap is partial (models/stability), not "nearly exact". Fix V-B1b wording.
- Fix the branch problem: your files are not visible on the remote. The branch `arena/04fdf32e-le` does not exist on GitHub. Push to the branch `brave/verification` (create from main). If your platform forces its own branch name, push anyway and tell the handler the exact branch name and commit hash.

Answers to your questions:
(a) No ASME access is needed now. For figures/tables/sections of the 13 AMR reviews, leave UNVERIFIED; do not guess. The handler may supply PDFs later.
(b) Yes, Crossref-based ranking is acceptable if labelled as Crossref count with date, and books excluded by construction is stated. Add OpenAlex citation counts as a second column if reachable.
(c) For monographs (Ignaczak–Ostoja-Starzewski, Dhaliwal–Singh, Tzou, Nowacki): abstract/TOC/previews plus the original journal papers are enough. Tag every monograph-derived statement SECONDARY-SOURCE. Never present a monograph statement as primary-checked.

GO: do PHASE B2 now (files V-B2a ... V-B2m and V-B2z_comparison_table.md as specified in BRAVE_NEXT.md). Same rules: no invention, DOI + access date + what you actually read, every derivation checked a second way, confidence, NOT-verified list. Additionally, for each model state its admissibility conditions and what happens to the wave speeds if they are violated. Push per file. Stop after B2 with a 10-line status; do not start B3 until told.
