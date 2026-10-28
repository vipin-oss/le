# Decisions for the author

## Backup-branch request

- **Request:** Create and push a separate backup branch for autonomous checkpoints.
- **Constraint:** This workspace is bound to its active Arena branch; no second branch was created or pushed.
- **Options:** Keep checkpoints on the active branch; after this session, the author may create an independent backup in their own Git workflow.
- **Recommendation:** Preserve the active branch and its remote history; do not rewrite or force-push it. This note does not authorize any external publication or sharing.

## B23 remediation decisions

### Exact versus reduced energy flux

- **Decision:** Retain the exact Eulerian fixed-volume balance with the total-energy advective flux. Keep $q_i-\sigma_{ij}v_j$ only as the explicitly qualified first-order small-amplitude wave-flux convention.
- **Reason:** The material balance and continuity give $\partial_t(\rho h)+\nabla\cdot(q-\sigma v+\rho h v)=\rho f\cdot v+\rho r$. The source-independent symbolic check now derives this from field residuals. The first-order order statement does not establish equivalence for second-order cycle-averaged total-energy fluxes.
- **Author action:** If later revisions use the reduced flux for a second-order thermomechanical energy ratio, identify the material/reference-plane convention or add an independently derived condition under which the omitted advective mean vanishes.

### B23 source-accessibility disagreement

- **Decision:** Retain the four class-A rows OCL-195, OCL-207, OCL-404, and OCL-405; the B23 report's claim that none of their original sources was accessible is contradicted by source-library records and page-level checks now available for Mindlin pp. 625–626, Biot pp. 241–242, and Barak p. 3. The DOI-matched Kumar article was re-opened at p. 1; its p. 17 conclusion remains supported by the same-date source-page note.
- **Qualification:** The current Drive text reader has no page-range selector. It exposed the Kumar article prefix, not printed p. 17, so the p. 17 observation is carried from the existing same-date page-read note rather than claimed as a duplicate read in this interval. The source article is now identifiable and re-openable.
- **Recommendation:** No PDF needs to be added to the repository. Keep source-library accessibility described without recording file IDs, links, or folder names.

### Coupled Biot cross-term example

- **Decision:** Do not retain the unverified numeric cross-term example in the manuscript. Its surviving summary does not define reference planes or provide the complete mode/flux convention needed to reproduce the reported values. The manuscript now relies on the fully specified one-dimensional welded benchmark, which derives the cross-term cancellation only for that lossless longitudinal case.
- **Recommendation:** Restore a coupled-system numerical example only after its original calculation, flux definitions, and reference planes are made independently reproducible. The internal working note remains an audit record, not manuscript evidence.

### Remote-plane power conventions

- **Decision:** Define $P_i$, $P_r$, and $P_t$ as signed, time-averaged modal-flux contributions at explicitly stated remote planes, with $+x$ normal and positive incident/reflected/transmitted magnitudes. The remote-plane balance requires the left net flux to be $P_i-P_r$; any residual incident--reflected cross term must be included explicitly rather than silently discarded.
- **Recommendation:** For each future numerical application, state the model-correct flux, reference planes, averaging convention, and cross-term treatment.

### Bibliography and source register

- **Decision:** Treat Crossref page omissions as metadata gaps rather than page evidence. The Das2026 and Maranganti2006 locators are now labelled as unverified article-number notes and no longer printed as page ranges; Eringen1966a remains marked ARBITRATED.
- **Decision:** Re-date/narrow MISSING_SOURCES entries to distinguish DOI resolution from source-page access. DOI resolution alone does not validate a claim or prove that a full text is present.

## WP3 bibliography disposition (2026-10-28)

Thirty-seven entries in `phase5/master/references_local.bib` are not cited by the PDF build. Cattaneo1948 and Vernotte1958 are now cited (Section 2, OCL-532); Vernotte's page range was corrected (OCL-533; `phase5/reports/BIB_CHECK_2026-10-28.md`). Uncited entries do not change the PDF, because the build prints only cited keys. The agent did not delete any entry. The author decides, per key, whether to cite it after a source check, keep it, or remove it:

| Key | Note for decision |
| --- | --- |
| Green1991 | GN-I source (Q3 family); cite only after page check, else keep in MISSING_SOURCES |
| Tzou1997 | no citing sentence; keep or remove (author decision) |
| Chandrasekharaiah1986 | review on hyperbolic thermoelasticity; cite if Section 2 needs it |
| Nowacki1975 | classical thermoelasticity monograph; cite for classical background if used |
| Yu2018ModifiedGL | no citing sentence; keep or remove (author decision) |
| Li2019 | no citing sentence; keep or remove (author decision) |
| Srivastava2026 | no citing sentence; keep or remove (author decision) |
| Kumawat2023 | no citing sentence; keep or remove (author decision) |
| Kumar2017 | Kumar identity split (OCL kumar records); cite only per the split decision |
| Kumar2018 | no citing sentence; keep or remove (author decision) |
| Kumar2008 | no citing sentence; keep or remove (author decision) |
| Kumar2025 | no citing sentence; keep or remove (author decision) |
| Gupta2025 | no citing sentence; keep or remove (author decision) |
| Gupta2024a | no citing sentence; keep or remove (author decision) |
| Yadav2023 | no citing sentence; keep or remove (author decision) |
| Jiao2024 | no citing sentence; keep or remove (author decision) |
| Fu2013 | no citing sentence; keep or remove (author decision) |
| Liu2020 | no citing sentence; keep or remove (author decision) |
| Bazarra2021MGTradial | no citing sentence; keep or remove (author decision) |
| DubnerAbate1968 | numerical Laplace inversion; as Stehfest1970 |
| Stehfest1970 | numerical Laplace inversion; cite only with a stated numerical claim |
| Chandrasekharaiah1984 | no citing sentence; keep or remove (author decision) |
| Nowacki1978 | no citing sentence; keep or remove (author decision) |
| MarchandMcDevittTriggiani2012 | no citing sentence; keep or remove (author decision) |
| Stroh1958 | anisotropic elasticity (Stroh formalism); relevant to Section 5 anisotropic waves if claims are added |
| Stroh1962 | as Stroh1958 |
| GorenfloKilbasMainardiRogosin2014 | fractional-calculus book; cite only with a checked claim |
| vanDerMerwe2021 | no citing sentence; keep or remove (author decision) |
| Chirita2016 | no citing sentence; keep or remove (author decision) |
| ChenGurtin1968 | MISSING source (MISSING_SOURCES); do not cite as evidence |
| GurtinWilliams1966 | Gurtin–Williams theory; cite only if a claim is added |
| WangLi2025IV | no citing sentence; keep or remove (author decision) |
| Durbin1974 | numerical Laplace inversion; as Stehfest1970 |
| HonigHirdes1984 | no citing sentence; keep or remove (author decision) |
| Luchko2010 | fractional-calculus reference; cite only with a checked claim |
| HetnarskiIgnaczak1999 | MISSING primary text (MISSING_SOURCES); do not cite as evidence |
| HetnarskiIgnaczak2000 | check identity against MISSING_SOURCES before any use |

Recommended default: keep all entries until the author decides; cite a key only after a source check and a ledger row; do not cite the two MISSING-source keys as evidence.

## WP7 journal pack decisions (2026-10-28)

- **Target venue:** Physics Reports (invited route; proposal ≤ 1000 words) versus Applied Mechanics Reviews (contact-first; title, abstract, timeline). Drafts for both are in `phase5/reports/journal/`. Nothing has been sent. The author chooses the venue.
- **Scope:** the current manuscript (about 123 pages) exceeds the Rapid Review length. A regular review needs an author-defined scope for the proposal.
- **Not read:** data policy, AI-use policy, conflicts/funding forms, and reference-style requirements for both journals. The fit memo states these as unchecked.
- **Author fields:** names, affiliations, contact, funding, conflicts, editor choice, and the AI-use wording are left as placeholders.

## Source-library mismatches (2026-10-28)
Source: partial re-copy of the private library ledger (B2). Full text was not read for the rows below.

| Key | Manuscript use | Finding | Decision needed |
|---|---|---|---|
| Ezzat2011 | `sec04_thermoelastic.tex` line 264: "fractional-order heat conduction with two temperatures \cite{Ezzat2011}" | Library copy is a different paper (DOI 10.1016/j.apm.2011.04.004). Publisher landing page (secondary check, 2026-10-28) confirms the bib entry DOI 10.1007/s00033-011-0126-3, ZAMP 62 pp.937–952 (2011). Full text of the ZAMP paper has not been read. | Keep the citation with the author confirming it, or replace it with a source that has been read. Do not treat the claim as verified. |
| Eringen1968b | Not cited in the manuscript (ledger only) | Library file is Tauchert, Claus and Ariman (1968), not Eringen 1968. | Remove the ledger key, or find the Eringen 1968 file. |
| Chen–Gurtin 1968 (ZAMP 19:614–627, DOI 10.1007/BF01594969) | Two-temperature background (Sec. 4, Sec. 11) | Not in the library (MISSING). The ZAMP reference list in the Ezzat paper (secondary) lists it. | Author to confirm the relation against the primary paper, or cite as not checked. |

## Attribution checks for the family table (2026-10-28 overnight, W2.8)
Checks use the bibliography entries and, where stated, the publisher landing page (secondary check, labelled). No entry has been deleted.

| Item | Finding | Decision needed |
|---|---|---|
| Tzou 1995 | Both 1995 papers are held: the body cites Tzou1995 (J. Heat Transfer 117:8–16, the DPL law paper; no DOI is printed on the paper, Crossref record 10.1115/1.2822329 retained as metadata) and the companion Tzou1995a (JTHT 9(4):686–693, DOI 10.2514/3.725). | None; both 1995 papers are held. |
| Hetnarski and Ignaczak 1999 vs 2000 | Two bibliography entries: 1999 J. Thermal Stresses 22:451–476 ("Generalized thermoelasticity") and 2000 IJSS 37:215–224 ("Nonclassical dynamical thermoelasticity"). Neither is cited in the body. | Keep or remove each; the year should follow the entry, not be inferred. |
| Chen–Gurtin 1968 vs Gurtin–Pipkin | The library file for the 1968 key is a Gurtin–Pipkin paper (different work); the Chen–Gurtin primary is not in the library. | Obtain the Chen–Gurtin paper or mark the two-temperature statement as unchecked. |
| Dell'Oro–Pata two-author vs Dell'Oro–Lasiecka–Pata three-author | The body cites the three-author JDE paper (critical-case MGT result). The two-author AMO viscoelasticity note is in the bibliography but not cited in the body. | Author to keep or remove the two-author entry. |
| Quintanilla 2003, DOI 10.1080/713855996 | Publisher landing page (secondary check, 2026-10-28) gives the same title as the bibliography entry (J. Thermal Stresses 26:713–721). | None; the DOI is consistent with the title. |

## Section 14 taxonomy reconciliation (overnight, WP6-07)
The evidence matrix (97 rows, 44 distinct raw theory labels, no multi-labelled rows) does not reproduce the earlier twelve-family table (96 assignments) or the earlier 95-record figure. The text now states the matrix counts (verified by `verify_reference_counts.py`) and labels the table as an editorial grouping.
Decision needed: (a) provide a labelled mapping from the 44 raw labels to the twelve families, so the table can be regenerated; or (b) replace the table with counts per raw label. Until then the table is not evidence of distribution.
