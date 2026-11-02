# Coverage gaps after the P8 batch

Measured on the rewritten text in `paper_v2/arena_deliverables/P7_language/` (51 `.tex` files,
`abstract_original.tex` excluded). Counts are case-insensitive string matches, so they are a
rough index of presence, not of substance.

| Topic | Mentions in current text | Verdict after this batch |
|---|---|---|
| piezoelectric | 88 | covered |
| Eringen / nonlocal | 50 | covered |
| porous / micropolar | 32 / 32 | mentioned, not developed |
| semiconductor | 26 | **name-checked only** — no carrier equation anywhere |
| couple-stress | 12 | vocabulary only, no energy stated |
| tissue | 12 | covered as an application |
| flexoelectric | 11 | mentioned in two places |
| gradient elasticity | 10 | vocabulary only |
| Mindlin | 9 | almost all "Mindlin–Tiersten" |
| strain gradient | 6 | vocabulary only |
| magneto-electro-elastic | 4 | one sentence |
| laminated | 1 | one sentence |
| **Toupin** | **0** | gap — this batch supplies the refs, not the text |
| **metamaterial** | **0** | **largest gap** |
| **phononic / band gap** | **0 / 0** | largest gap |
| **locally resonant** | **0** | largest gap |
| **quasicrystal** | **0** | gap |
| **graphene / nanotube / CNT** | **0 / 0 / 0** | gap |

## Provided by this batch

72 references, 18 per area, no key overlapping the paper's 362 existing keys:
`refs_P8.bib`, `refs_P8.csv` (with per-reference target section and inside/outside flag),
`outlines_P8.md` (one page per area), `pdfs_needed_P8.csv` (what must be read next).

## Still missing after this batch

1. **Nothing here is above R0.** Every entry is a Crossref match on title/venue/volume/pages.
   No abstract, no full text, no equation number has been checked. Any sentence in
   `outlines_P8.md` that says "state equation X" is a *plan*, and the equation number field is
   marked `NOT VERIFIED` on purpose.
2. **No quantitative content.** No band-gap width, no internal length `ℓ`, no carrier mobility,
   no acoustoelectric gain, no metamaterial mass density. The batch deliberately carries no
   numbers, because none were read.
3. **Thermoelastic damping *of* a phononic crystal is an open question, not a covered result.**
   No reference was found that treats TED of a locally resonant array including the band
   structure. If the review claims it, it must be flagged as a question in `s17_open`.
4. **Missing sources that could not be verified at all**, so they are *not* in the bib:
   - Koiter, "Couple-stresses in the theory of elasticity" (1964, Proc. K. Ned. Akad. Wet.
     B67) — no Crossref DOI found; **NOT VERIFIED**.
   - Steigmann–Ogden surface elasticity and the dell'Isola–Placidi second-gradient lineage —
     not searched to a verified record in this batch; **NOT VERIFIED**.
   - Any textbook treatment of gradient thermoelasticity (e.g. a dedicated chapter) — only
     journal articles were verified.
5. **Citation trap recorded.** "Thermal metamaterials and devices" is Li et al. **2021**,
   *Nature Reviews Materials* **6**:488–507 (`10.1038/s41578-021-00283-2`). A widely repeated
   2012 *Nature Materials* attribution was checked and is **not** the source; do not cite it.
6. **Group/country spread is asserted, not audited.** The lists were built to mix founding
   authors (Toupin, Mindlin, Green–Rivlin, Biot, Sigalas–Economou, Kushwaha, Hutson–White,
   Shechtman), later reviews, and 2015–2026 papers from several countries, but no affiliation
   field was collected, so a per-country count cannot be reported from this batch.

## What would close the gaps, in order

1. Obtain the 30 PDFs in `pdfs_needed_P8.csv`; read the four or five that carry equations
   (Toupin 1962/1964, Mindlin 1965, Hussein 2014, Hutson–White 1962) and lift the equation
   numbers — that alone moves Area (a) and Area (c) from R0 to R3.
2. Read one full text per area at R2 to fix the "what it shows" sentences.
3. Only then write `s13c_metamaterials` (Area b), the carrier paragraph (Area c), and the
   higher-grade paragraph (Area a).
4. A per-country/affiliation audit needs metadata the Crossref title query did not return;
   it would require one extra query per DOI or the PDFs themselves.
