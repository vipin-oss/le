# P10 — the "Wider material classes" section and the verdict update

Evidence only: no `.tex` file was edited on this branch or on any other.

## What was done

1. **Found the section where it actually lives.** It is not in this branch; it is in
   `review-paper-v2` (commit `acea1fd`), inside `paper_v2/overleaf_package.zip` as
   `sections/s12b_wider.tex` (41 lines, 8.6 kB, five subsections plus a summary table). The file
   cites 72 keys and **all 72 resolve** in the package's `refs*.bib` (434 entries).
   `Gupta2026HeatMap` exists in that bibliography but is **not cited** in the wider section;
   neither Oh et al. 2016 nor Hobiny/Abbas/Marin 2022 is in it at all.
2. **Quoted the three sentences verbatim** and re-judged them against the real wording — see
   `verdicts_P10.md` §2–§3.
3. **Bib entries verified from the PDFs** in `refs_P10.bib`: Oh 2016 and Hobiny 2022 as active
   entries, Gupta 2026 as a commented entry because it is already in the package as
   `Gupta2026HeatMap` (a second active key would duplicate it).
4. **Gupta 2026 upgraded R2 → R3** by extracting the PDF text locally: the heat-flux law is
   eq. **(2.15)** with the memory-dependent three-phase-lag kernel and the Klein–Gordon nonlocal
   operator, its elimination is eq. **(2.16)**, and the carrier equation is eq. **(2.17)** — all
   on **p. 6**. Supporting equations: (2.7)–(2.11) on p. 5; the memory operator (1.1) and its
   kernels (1.2) on p. 3.
5. **The eleven missing PDFs did not arrive.** Toupin 1962/1964, Mindlin 1964, Green–Rivlin 1964,
   Hutson 1962, White 1962, Liu 2000, Hussein 2014, Sigalas 1992, Kushwaha 1993 and Zubko 2013
   were re-searched on 2026-11-02 (author-name filenames, DOI-derived filenames, full-text title
   match). The S1 couple-stress half and the S2 Liu attribution therefore stay
   **SOURCE NOT AVAILABLE**; nothing was inferred about their contents.

## Verdicts after P10

| Sentence | Verdict | Anchor |
|---|---|---|
| S1 operator change | supported | Mindlin 1965, eqs. (1) p. 418, (17) p. 421, (19) p. 421, (20a) p. 422 |
| S1 "`G(s)` is not modified" | not demonstrated (absence) | no thermal field in Mindlin 1965; the section's own hedge says so |
| S1 couple-stress half | **SOURCE NOT AVAILABLE** | Toupin 1962/1964, Green–Rivlin 1964 absent |
| S2 frequency-dependent effective mass | supported | Oh 2016, eq. (4a) p. 4, eq. (10) p. 5 |
| S2 Liu 2000 attribution | **SOURCE NOT AVAILABLE** | Liu 2000 absent |
| S3 kernel in piezo-semiconductor | **supported, now R3** | Gupta 2026, eq. (2.15)/(2.16)/(2.17) p. 6; Hobiny 2022, eq. (3) p. 3 |

## Files

- `verdicts_P10.md` — the section quote, the three verdicts with page-cited equations, and the
  re-search result for the missing PDFs.
- `refs_P10.bib` — 2 active entries + 1 commented duplicate, all verified from the PDF title pages.
- `evidence_P10.csv` — level, pages read, equations with pages, which sentence each supports.
- `check_p10.py` — gate; prints `PASS` and exits 0. It also cross-checks against
  `../P8_coverage/existing_keys.txt` and `../P8_coverage/refs_P8.csv`.

## Related updates elsewhere

`../P9_verification/evidence_P9.csv` and `../P9_verification/verdicts_P9.md` now record Gupta 2026
as **R3** with eqs. (2.15)–(2.17) on p. 6, so the earlier folder is not stale.
