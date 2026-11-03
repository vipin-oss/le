# Evidence base for *Waves in Thermoelastic and Multiphysics Continua* — status report

Everything below is derived from sources that were actually opened. No row is written from a title or from memory: the `source_used` column says exactly what was consulted, and `page_or_eq_ref` always points into the **source**, never into the manuscript.

## 1. What exists

| File | Contents |
|---|---|
| `paper_notes.csv` | 416 rows, one per citation key in the inventory. Columns: `problem_geometry, heat_law, coupled_fields, method, main_result, limitation_or_caveat, page_or_eq_ref, used_in_sections, tier, source_used`. |
| `drive_pdf_map.tsv` | 131 Drive PDFs resolved: 64 cited keys matched, 53 uncited, plus unrelated / mislabelled / unidentified files. |
| `missing_pdfs.txt` | Cited keys with no PDF in the Drive folder (351). |
| `unmatched_pdfs.txt` | Drive files that could not be tied to a citation key. |
| `attribution_mismatches.csv` | 11 rows: places where the sentence around `\citep{key}` says something the source does not support. |
| `uncited_classics.csv` / `.bib` | 54 works present in the Drive folder (or identified from it) that the paper does **not** cite, ranked HIGH/MED/LOW. |
| `cluster_synthesis.md` | Grouped synthesis of what the evidence base shows, chapter by chapter. |
| `missing_literature.csv` | 9 genuinely missing strands (second-sound / TED experiments, EIT, Straughan, MGT …), every DOI Crossref-resolved. |

## 2. Coverage — the honest number

* **44 of 416 keys have source text**: 40 FULLTEXT (opening pages / abstract / the cited section read directly) and 4 ABSTRACT.
* **372 are NOT-READ.** For those the notes record *why* (no PDF in the folder, or an unreadable scan) and nothing else. NOT-READ is not a mistake; guessing is.
* Of the 64 cited keys that do have a verified PDF, **44 have been read** and 20 have not (chiefly Hussein2014-scale books, older scans, and files that trip the 25 MB extraction cap).
* Unreadable as delivered, not retried: `Eringen_1966.pdf` (image-only), `Lamb_1917.pdf`, `Stoneley_1924.pdf` (JSTOR cover), `Povstenko_2011.pdf`, `Unknown_01495730151078171.pdf` (Taylor & Francis cover sheets), `Lim_2015.pdf` (Elsevier cover sheet), `1.1729015.pdf` (AIP cover sheet), `Unknown_10.1007@978-1-4612-2210-1.pdf` (Müller–Ruggeri, 30 MB > extraction cap).
* Tier 1 is 78 keys, of which 31 have a verified PDF — so a substantial part of the body's equation-level claims **cannot** be checked against the source from this Drive folder alone.

## 3. Attribution findings

11 rows in `attribution_mismatches.csv`. The headline one is **not** an error: the "GN-III has finite speed / GN-III has infinite speed" disagreement is **TERMINOLOGY** — Green–Naghdi type III has unbounded phase speed at high frequency and no sharp front, while "finite speed" in the GN papers refers to the intermediate-regime speed √(k\*/ρc). Verified accurate: Quintanilla 2003 (DPL), Chen 2001 (ballistic→diffusive crossover), Dreyer–Struchtrup 1993, Biot 1956. Ten further rows are OK-BUT-VAGUE: the manuscript attributes a result to a paper that contains it only as a special case.

## 4. Uncited classics (KAAM 3)

54 rows, 9 HIGH. The HIGH set is the one that changes the paper's argument, not just its reference list:

* **Dafermos 1968** (10.1007/BF00276727) — existence and asymptotic stability for linear thermoelasticity; the theorem behind the review's "classical theory is asymptotically stable" sentence.
* **Liu 1972** (10.1007/BF00250688) — the Lagrange-multiplier entropy principle, i.e. the method behind Section 3's constitutive restrictions.
* **Gurtin–Pipkin 1968** (10.1007/BF00281373) — the third historical route to finite-speed conduction; the history section jumps from Cattaneo to Lord–Shulman without it.
* **Deresiewicz 1957** (10.1121/1.1908832) — two dilatational waves, both dispersed and attenuated: the classical-limit column of the dispersion table.
* **Achenbach 1968** (10.1016/0022-5096(68)90035-5) — how conduction bleeds amplitude out of a stress jump at a front.
* **Nayfeh–Nemat-Nasser 1971** (10.1007/BF01178389) — first systematic plane-harmonic-wave study of a relaxation theory.
* **Chandrasekharaiah 1988** (10.1007/BF01173936) — generalized (flux-as-constitutive-variable) thermoelasticity for piezoelectric media.
* **Zhang–Zuazua 2003** — where decay for type III was settled rigorously (DOI not resolvable on Crossref; entry carries a note instead of a DOI).
* **Chen 2021**, *Nat. Rev. Phys.* 3, 555 (10.1038/s42254-021-00334-1) — the modern map of which non-Fourier regimes have experimental support.

MED: Weideman–Trefethen 2007, Crump 1976, Puri 1972, Mindlin–Eshel 1968, Coleman 1964, Sinha–Elsibai 1996/1997, Romano et al. 2017, Azhdari et al. 2025. The remaining 36 rows are LOW and are labelled as Crossref-record-only, i.e. read no further than the title.

## 5. Known weaknesses of this deliverable

1. **372/416 NOT-READ.** The notes are a thin but truthful layer, not a full evidence base. Any sentence in the paper resting on a NOT-READ key is unverified.
2. **The 25 MB extraction cap** blocks the two big books (Müller–Ruggeri; Eringen 1999 extraction also failed at the provider) — they are recorded as unread rather than paraphrased.
3. **Crossref carries no abstracts** for APS/Elsevier/T&F DOIs (tested on 8 Tier-1 DOIs), so the 351 keys without a PDF cannot be filled in batch; each would need its publisher landing page read one at a time.
4. **Older scans are unreliable for numbers** (OCR of Chadwick–Sneddon 1958 destroys sub/superscripts); where a number was needed the page had to be rasterised and looked at, which was not possible for every file.
