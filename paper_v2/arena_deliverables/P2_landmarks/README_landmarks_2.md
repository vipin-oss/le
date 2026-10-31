# Task 3 — missing landmark literature

`landmarks_2.csv` lists the landmark works that the manuscript discusses by name (or
plainly depends on) but does not cite, with the DOI checked on the publisher/DOI page
for each entry. Nothing under `scripts/` or `sections/` was modified.

## How the entries were produced

1. Every candidate was searched on the web and the DOI, volume and pages were read
   from the **publisher page itself** (`link.springer.com`, `link.aps.org`,
   `journals.sagepub.com`, `aimsciences.org`, `nature.com`), not from a citation
   string in a secondary paper. Where the only source for a DOI is the citing
   literature this is said explicitly in `verified_from`.
2. `paper_sources.zip` was then searched for the same works: 362 bib keys, 337 of
   them cited from `sections/*.tex`, were extracted and the citation count of each
   landmark was computed, so that "missing" means *absent from the bibliography* and
   "uncited" means *present in `refs*.bib` but never cited*.
3. No DOI was inferred. The one book without a DOI is marked `NOT FOUND`.

## Missing works (8 rows)

| id | work | DOI | why it matters |
|---|---|---|---|
| LM-01 | Callaway 1959, *Phys. Rev.* **113**, 1046 | 10.1103/PhysRev.113.1046 | single-mode relaxation-time closure behind every Cattaneo/GK flux law |
| LM-02 | Jeffreys 1929, *The Earth*, 2nd ed., CUP | NOT FOUND (book) | origin of the two-lag "Jeffreys-type" law the text names |
| LM-03 | Gurtin & Pipkin 1968, *Arch. Rational Mech. Anal.* **31**, 113 | 10.1007/BF00281373 | hereditary finite-speed conduction; **in `refs.bib` but cited 0 times** |
| LM-04 | Jordan 2014, *DCDS-B* **19**, 2189 | 10.3934/dcdsb.2014.19.2189 | Maxwell–Cattaneo derivation of the MGT equation |
| LM-05 | Conti, Pata & Quintanilla 2020, *Asymptot. Anal.* **120**, 1 | 10.3233/ASY-191576 | MGT with a memory kernel (Cattaneo-with-memory) |
| LM-06 | Straughan 2011, *Heat Waves*, Springer AMS 177 | 10.1007/978-1-4614-0493-4 | one-stop monograph for the whole model hierarchy |
| LM-07 | Chen 2021, *Nat. Rev. Phys.* **3**, 555 | 10.1038/s42254-021-00334-1 | 2020s review of non-Fourier/phonon-hydrodynamic regimes |
| LM-08 | Kaur, Singh & Craciun 2023, *Discov. Mech. Eng.* **2**, 2 | 10.1007/s44245-023-00009-4 | 2023 review of these models for beams/resonators |

## Landmarks that are already in the paper (no action)

Citation counts are `\cite*` occurrences over `main.tex` + `sections/*.tex`.

| landmark | key in `refs*.bib` | citations |
|---|---|---|
| Cattaneo 1948 / Vernotte 1958 | `Cattaneo1948`, `Vernotte1958` | 4 / 4 |
| Lord & Shulman 1967 | `Lord1967` | 5 |
| Green & Naghdi 1991, 1992, 1993 | `Green1991`, `GreenGN1992`, `Green1993` | 6 / 3 / 8 |
| Chen & Nunziato 1974 | `ChenNunziato1974` | 2 |
| Guyer & Krumhansl 1966 (I and II) | `GuyerKrumhansl1966`, `GuyerKrumhansl1966II` | 5 / 6 |
| Joseph & Preziosi 1989, 1990 | `Joseph1989`, `Joseph1990` | 3 / 4 |
| Chandrasekharaiah 1998 review | `Chandrasekharaiah1998` | 3 |
| Hetnarski & Ignaczak 1999 | `HetnarskiIgnaczak1999` | 4 |
| Tzou 1995 (DPL) | `Tzou1995` | 5 |
| Quintanilla 2019 (MGT) | `Quintanilla2019` | 7 |
| Ignaczak & Ostoja-Starzewski 2010 | `IgnaczakOstoja2010` | 2 |
| Shakeriaski et al. 2021 review | `Shakeriaski2021` | 2 |
| Gurtin & Pipkin 1968 | `GurtinPipkin1968` | **0 (never cited)** |

## Consequences for the manuscript

* The claim "the flux laws follow from the phonon Boltzmann equation" currently has
  no closure reference; LM-01 (and the already-cited Guyer–Krumhansl 1966) supply it.
* The "Jeffreys-type" label and the MGT model are named without a citation for the
  origin; LM-02/LM-04/LM-05 close that gap.
* Gurtin–Pipkin is the one case where the entry exists and is simply never used;
  citing it costs nothing and removes a hole in the hereditary-conduction paragraph.
* `landmarks_2.csv` is additive: it proposes what to cite and where, and does not
  touch `sections/*.tex` (per the standing rule that only Claude edits the sources).

Validator: `python3 check_landmarks_2.py` prints `PASS all checks (rows=8, columns=13)`
and exits 0; its output is in `check_landmarks_2_log.txt`.
