# WP3 reference-hygiene audit — citation keys and B22 Crossref dispositions

**Status:** The targeted B22 bibliography identity and Crossref-register checks are reproducible and now run in strict CI. WP3 is not complete: the working bibliography contains 39 uncited entries whose disposition has not been established, and unresolved source-access/metadata limits remain. No entry was deleted or promoted by this audit.

## Automated checks

Content commit `552ba67` added `verify_reference_hygiene.py` and wired it into CI, together with the existing Kumar split verifier. The strict run `40514426363` passed; output commit `9f3afae` was fast-forwarded to the fixed branch. The checks cover the active `main.tex` include tree and the saved B22 comparison records, not scientific validity of cited claims.

The active TeX tree has 104 distinct citation keys; all resolve to unique entries among the 143 keys in `references_local.bib`. No missing or duplicate keys were found. Thirty-nine bibliography entries are not cited from the active include tree. They are listed below as **unresolved working-bibliography candidates**, not as stale or safe-to-delete records; the script reports their count and deliberately does not delete them. The active document contains no `\nocite{*}` command.

The itemized `CROSSREF_FINAL.csv` has 14 rows: eight for `Quintanilla2003DPL` and six for `DellOroPata2016Viscoelasticity`. The verifier checks that the bibliography and evidence register preserve the following limits:

- **Quintanilla DOI conflict remains unresolved.** The earlier R4B source note reports the first page as `10.1080/01495730390203518`; the B22 held-cover report says `10.1080/713855996`. The saved Crossref response identifies the latter; the former returned 404. The held paper could not be reopened to reconcile the reports. Both reports remain visible, the bibliography retains the Crossref-matching candidate but `verified=NO`, and `CROSSREF_FINAL.csv` records `CONFLICT-UNRESOLVED`. This CI check reuses saved responses; it made no new Crossref request and does not claim the source-page dispute is settled.
- **Dell’Oro–Pata 2016 remains only partly checked.** The bibliography now records *Applied Mathematics and Optimization* 76:641–655 based on the B22 targeted comparison row. No raw Crossref DOI response is available in the current saved set; the authors/title/year comparisons marked not independently rechecked remain so, and the bibliography retains `verified=NO`.
- **Kumar identity split remains bounded.** The saved DOI match belongs to Kumar and Kansal’s CMST interface paper, not the Kumar/Devi/Sharma library article. `verify_kumar2017_reference_split.py` passes; the latter remains without a DOI and `verified=NO`. The eight directly Kumar-linked rows (OCL-076, OCL-278, OCL-279, OCL-285, OCL-288, and OCL-292–OCL-294) remain B/C; OCL-286, OCL-287, and OCL-291 are separate source-read Class A claims and remain A.

No new bibliography entry was added, no source text was copied, and no scientific claim class was promoted. The CI verifier tests record consistency and citation-key integrity only; source-page and claim-level verification remains governed by the ledger and the recorded source limits.

## Uncited working-bibliography candidates — retained, not dispositioned

`Cattaneo1948`, `Chandrasekharaiah1984`, `Chandrasekharaiah1986`, `ChenGurtin1968`, `Chirita2016`, `DubnerAbate1968`, `Durbin1974`, `Fu2013`, `GorenfloKilbasMainardiRogosin2014`, `Green1991`, `Gupta2024a`, `Gupta2025`, `GurtinWilliams1966`, `HetnarskiIgnaczak1999`, `HonigHirdes1984`, `IvanovSavova1991`, `Jiao2024`, `Kumar2008`, `Kumar2017`, `Kumar2018`, `Kumar2025`, `Kumawat2023`, `Li2019`, `Liu2020`, `Luchko2010`, `MarchandMcDevittTriggiani2012`, `Nowacki1975`, `Nowacki1978`, `Singh2020c`, `Srivastava2026`, `Stehfest1970`, `Stroh1958`, `Stroh1962`, `Tzou1997`, `Vernotte1958`, `WangLi2025IV`, `Yadav2023`, `Yu2018ModifiedGL`, `vanDerMerwe2021`.

## Strict build and presentation spot check

CI `40514426363` produced 121 pages; undefined references/citations 0; privacy-token matches 0; internal-path matches 0; strict manuscript-tag matches 0; overfull boxes >1 pt 0; near-overfull boxes >0.5 pt 0; 18 figure PDFs rendered/16 master includes; deletion-audit `NONE` rows 0. Ten A/V ledger rows were checked against this latest PDF: OCL-164, OCL-165, OCL-166, OCL-167, OCL-169, OCL-445, OCL-466, OCL-467, OCL-480, and OCL-499. Their rendered locations and bounded checks are listed in `Q5_FIGURE11_WORKFLOW_AUDIT.md`. Printed p. 58 was re-rendered and visually checked again; the corrected Figure 11 connectors, labels, and caption remain clear.

**Next:** continue WP3 only where source access and ledger anchors permit; do not automatically remove the 39 uncited entries. WP4 equation audit remains the next broader work package, while Q3’s model-specific source-to-manuscript, admissibility, energy, boundary, and interface-flux questions remain open, including OCL-492.
