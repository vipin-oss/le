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
