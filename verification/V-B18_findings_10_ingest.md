# V-B18 — FINDINGS_10 ingested (25 papers), five corrections actioned, readiness recounted, identifiers re-verified

**Batch:** B18. **Date:** 2026-10-23. **Input read in full:** `control/FULLTEXT_FINDINGS_10.md` at `origin/claude/control` @ **`f95cf21`** (fetched with the explicit refspec `refs/heads/claude/control:refs/remotes/origin/claude/control --force`).
**No manuscript edit.** Everything below is a report and a change inside `verification/` and `api_log/`.

## Task

1. Ingest the 25 papers the supervisor read in FINDINGS_10 (F30–F49): `LITERATURE_BASE`, `FULLTEXT_FACTS`, `REFERENCE_PLAN`, `REFERENCE_READINESS`.
2. Action the five corrections the findings carry — in particular **C1: "Nowacki 1984" is actually Chandrasekharaiah 1984** — and fix the request list.
3. Put the 25 supplied items into **Part A0** of the request list.
4. **Recount the section-wise primary-read counts.**
5. Verify the remaining items' identifiers at **Crossref** and their OA status at **Unpaywall/OpenAlex**, and report in `V-B18`.
6. (From the earlier order, still owed:) `PDF_REQUEST_LIST_4.md` with Part A = open access, Part B = paywalled, **no guessed DOIs**.

## Method

- Findings file read end to end. Every one of the 25 papers was entered as **one facts row** and **one base row** (the B10c/B10d rule), each row stating that the equations are **supervisor-transcribed** and that **this verifier opened none of the PDFs**.
- **Identifier layer, separate from the reading layer:** 26 journal/chapter DOIs were pushed through **Crossref** (`api.crossref.org/works?filter=doi:…`, batched ten per call, `select=DOI,title,author,container-title,volume,issue,page,issued,type`) and the returned title / authors / journal / volume / issue / pages / year compared with the citation. Two items with no Crossref hit (Cattaneo 1948, Vernotte 1958) were searched bibliographically and **left with NO DOI** rather than given a plausible-looking one.
- **Access layer:** OpenAlex `open_access` for all 26 (two batched calls) plus **Unpaywall** for the four where the verdict mattered (Honig–Hirdes, Dell'Oro–Pata, Mainardi, Povstenko 2011). Every per-item result is in `api_log/B18_crossref_checks.csv` (28 rows = 26 identifiers + 2 outstanding books).
- **Readiness recounted mechanically**, not by hand: a script re-derived every section's counts from `REFERENCE_PLAN` with one fixed rule (full/primary = read_level starting FULL/PRIMARY/PREFACE/SECONDARY-READ; partial = PARTIAL / abstract-level / section-read; else metadata-only). This is why two numbers moved in directions nobody asked for — see "Result" 3.

## Result

### 1. The 25 papers are in — 27 new facts rows, 19 new base rows, 25 plan rows

- `FULLTEXT_FACTS`: 125 → **152** rows. New keys: `Nowacki1978`, `Chandrasekharaiah1984TPZ`, `CowinNunziato1983`, `NunziatoCowin1979`, `Iesan1986`, `Marchand2012MGT`, `Durbin1974`, `HonigHirdes1984`, `Stroh1958`, `Stroh1962`, `ChadwickSneddon1958`, `JosephPreziosi1989`, `JosephPreziosi1990`, `HetnarskiIgnaczak1999`, `IvanovSavova1991`, `Povstenko2009`, `GorenfloMainardi1997`, `Gorenflo2014Book`, `Luchko2010`, `Povstenko2015Book`, `WangLi2025IV`, `vanDerMerwe2021`, `Chirita2016`, `ChenGurtin1968`, `GurtinWilliams1966` — plus in-place updates to the existing `Aldawody2019`, `Kumar2024MTDMenergy`, `KumarKumari2024IJAME`, `Biswas2020ActaMech` rows from B18's earlier second pass.
- `LITERATURE_BASE`: 519 → **536**. Nineteen new rows (`LIT-0520`…`LIT-0536`) and eight existing metadata-only rows raised to read level with their facts folded in (`LIT-0013`, `LIT-0014` Joseph–Preziosi; `LIT-0020`…`LIT-0022` voids; `LIT-0032` Povstenko 2009; `LIT-0307` Wang–Li 2025; `LIT-0428` van der Merwe).
- `REFERENCE_PLAN`: 215 → **232**, every new row `technical_claim_eligible=YES` except the three that were not read (Mainardi 2010, Povstenko 2011, and the Povstenko 2015 book, which is preface-only and marked PREFACE).
- Every facts row carries the sentence "supervisor-transcribed … not opened by this verifier", and the two Laplace rows of the earlier B18 half carry the same wording. **No row in this batch is marked PRIMARY-SOURCE-CHECKED by me.**

### 2. The five corrections, actioned

| | correction | what I changed |
|---|---|---|
| **C1** | "Nowacki 1984 / J. Thermal Stresses 7:293-306" is **D. S. Chandrasekharaiah**, *A temperature-rate-dependent theory of thermopiezoelectricity* | Crossref record confirms `D.S. Chandrasekharaiah` on `10.1080/01495738408942213`. Base row `LIT-0521` created under the right author; **`PDF_REQUEST_LIST_4.md` carries the correction in a banner and no longer has a "Nowacki 1984" row.** The manuscript never cited it under Nowacki (supervisor grep), so this is a list defect only. |
| **C2** | `Cattaneo1948` in the manuscript bib is wrong: **Atti Sem. Mat. Fis. Univ. Modena 3, 83–101 (1948)** | Not a manuscript edit (not mine to make) — recorded in `PDF_REQUEST_LIST_4` item C1 and in GAP-02, with the note that Joseph–Preziosi 1989 print a different page ("3"), so the page range is unverified against a printed copy. |
| **C3** | `Luchko2010` as a book is dubious; the real paper is **Comput. Math. Appl. 59(5):1766–1772**, `10.1016/j.camwa.2009.08.015` | New base row `LIT-0535` with the exact Crossref title/pages; the facts row states the **limit**: it supports maximum principle / uniqueness / continuous dependence / Fourier-method existence for the time-fractional diffusion IBVP, and **not** "Laplace-domain Mittag-Leffler inversion". |
| **C4** | **Povstenko 2009 does not print a fractional Cattaneo law** | `LIT-0032`'s read level and `why` rewritten to the kernel classification actually printed — flux (8) `q = -k D_RL^{1-a} grad T`, (9) for 1<a<2, fractional heat equation (10), space-time (11), quasi-static (12). The manuscript sentence is marked **CONDITIONAL** in the facts row and in GAP-21; **`LIT-0536` (Povstenko 2011) added to the base and to the request list as the paper that must be read to settle it.** |
| **C5** | Hetnarski–Ignaczak call the thermoelastic DPL model the **"C-T model"** (Chandrasekharaiah–Tzou 1998) | Recorded in `LIT-0526` and its facts row, with the instruction that the manuscript's DPL attribution be checked (Tzou 1995 for the heat law, Chandrasekharaiah 1998 / Tzou for the thermoelastic theory). No verdict issued: the manuscript is not mine to rule on and I have not seen its DPL sentence. |

Two further printed cautions were captured rather than smoothed over: **Stroh 1958/1962 are purely elastic** (no thermal or piezo coupling), and **Chadwick–Sneddon's OCR numbers are unreliable** — neither may be quoted as a thermoelastic or numerical result.

### 3. Section-wise primary-read counts, recounted

`REFERENCE_READINESS.csv` rebuilt mechanically from the plan (rule in "Method"). Old → new, full/primary:

| section | was | now | bar (≥6) |
|---|---|---|---|
| s.5 | 4 | **9** | **YES** (was NO) |
| s.8 | 3 | **8** | **YES** |
| s.10 | 3 | **7** | **YES** (was NO) |
| s.11 | 9 | **14** | YES |
| s.4.8 | 8 | **9** | YES |
| s.4.9 | 3 | **4** | no |
| s.4.6 | 1 | **3** | no |
| s.12 | 1 | **3** | no (3 of 6) |
| s.13 | 1 | **1** | **NO — and it was wrong before** |
| s.9 | 11 | 11 | YES |
| s.6 / s.7 | 8 / 8 | 8 / 8 | YES |

**Eight of the twenty sections now clear the six-source bar** (s.4.8, s.5, s.6, s.7, s.8, s.9, s.10, s.11). Total plan rows 232; full/primary 97; partial 27; metadata-only 55 — the columns no longer double-count "eligible but unread".

**Two honest regressions**, both from applying one rule to every row rather than keeping hand-assigned labels:
- **s.13 drops from "YES" to NO.** Its 11 eligible rows were 10 abstract-level plus one partial; on a primary-read measure it has **one** source. The previous YES was a labelling artefact.
- **s.12 rises 1 → 3** but is still short: Wang–Li 2025 (F46) and van der Merwe (F47) are now read, plus the Shakeriaski survey. **GAP-22 stays open.**

### 4. Identifiers re-verified; the request list rewritten

`PDF_REQUEST_LIST_4.md` (new, supersedes list 3 for everything supplied): **Part A0 = 25 items** with Crossref-verified citations; **Part A = 1** (Dell'Oro–Pata 2016, green, PoliMi); **Part B = 3** (Povstenko 2011, the Povstenko 2015 book, Mainardi 2010 — all closed); **Part C = 7** print-era with **NO DOI**. **11 outstanding in total.**

Crossref quirks recorded verbatim rather than repaired silently: `10.1016/0022-5096(58)90027-9` spells the second author **"Snedon"**; `10.1080/014957399280832` crams both authors into one string and truncates "Ignacza"; `10.1007/978-3-7091-2664-6_5` carries a different container title (the CISM volume name) from the one the project used.

OA status (OpenAlex + Unpaywall): **bronze** Honig–Hirdes and Luchko 2010; **gold** Wang–Li 2025; **green** Dell'Oro–Pata 2016; **closed** for everything else, including both books and Povstenko 2011.

## Evidence / sources

- `control/FULLTEXT_FINDINGS_10.md` (F30–F49, corrections C1–C5) at `origin/claude/control` **`f95cf21`** — read in full.
- Crossref: five batched calls (`filter=doi:` up to ten DOIs each) on 2026-10-23 covering 26 identifiers; two bibliographic queries (Gorenflo–Mainardi CISM chapter, Vernotte 1958) — the latter returned **no** matching record.
- OpenAlex: two batched `open_access` calls covering 26 DOIs; Unpaywall `/v2/<doi>` for Honig–Hirdes, Dell'Oro–Pata, Mainardi, Povstenko 2011.
- Files written: `verification/FULLTEXT_FACTS.csv`, `LITERATURE_BASE.csv`, `REFERENCE_PLAN.csv`, `REFERENCE_READINESS.csv`, `REFERENCE_GAPS.csv`, `PDF_REQUEST_LIST_4.md`, and `api_log/B18_crossref_checks.csv` (28 rows).

## Checks done

- **No DOI from memory.** Every identifier in list 4 came back from Crossref in this session and its title was compared; the two that returned nothing were given "NO DOI" instead of a guess.
- **One facts row per paper**, with the inv_id naming the findings file and the F-number so any claim can be traced to the paragraph that produced it.
- **Read-level honesty at team level:** 25 new facts rows, 0 marked as read by me; the strings say "supervisor-transcribed" and "NOT opened by this verifier".
- **Plan integrity:** 232 rows, no duplicate `lit_id` (0520–0536 checked free first), 14 columns, section counts reconciled against the readiness table with the same classifier.
- **Corrections traced to source:** each of C1–C5 is quoted to the findings paragraph that carries it, and C1 additionally cross-checked against the Crossref author field — two independent sources agree.
- **No paper text or PDF in the repo.** The findings file is a summary written by the supervisor; I copied no equation display beyond the short printed forms already in the facts rows, and no PDF was downloaded in this half of the batch.

## Confidence

- **HIGH** that the 25 papers are correctly identified: Crossref title/author/journal/volume/pages agreed on all 24 that have DOIs, and the one that disagreed (C1's author) disagreed in exactly the way the supervisor flagged.
- **HIGH** on the OA verdicts (OpenAlex and Unpaywall agree on every item).
- **HIGH** that the readiness recount is arithmetically reproducible: it is scripted from one rule and the rule is stated.
- **MEDIUM** on the content of the facts rows: correct as records of what the findings relay, but no page render was seen by me, several equation displays were marked `[IMG]` in the supervisor's own extraction, and two (Chen–Gurtin (1.3), Chirita's delay inequalities) are explicitly incomplete.
- **LOW** for anything numerical: Chadwick–Sneddon's constants are flagged unreliable, Honig–Hirdes' 60×/30× comparison is problem-specific, and no table was transcribed.

## NOT verified / open issues

1. **`Papers_to_download.xlsx` and its "Extended list" sheet (69 DOIs) were never available to me.** Not in Drive under that name, not among the 50 spreadsheets the connector lists, not in `2_Others_Papers`. So the identifier work above covers the **26 DOIs this project carries**, not 69. If the workbook turns up, 69 DOIs is about seven batched Crossref calls.
2. **I opened none of the 25 PDFs.** Team-level primary, verifier-level secondary. The convention question from the last batch is still open: `FULLTEXT_FACTS` now mixes "PRIMARY-SOURCE-CHECKED (supervisor …)" (F23–F27) with "SECONDARY-SOURCE" (F28 onward).
3. **The `[IMG]` equations** (Nowacki 1978 (8)–(10), (16)–(18)) need page-render reading before anything is quoted verbatim. So do Chen–Gurtin (1.3) and the Chirita delay-time inequalities.
4. **C4 is not fully closed** — it needs Povstenko 2011 (list 4, B1, closed access). Until then the manuscript's fractional-Cattaneo sentence stays conditional.
5. **s.12 is still 3 of 6**, and **s.13 is 1 of 6** on a strict primary-read measure.
6. **Manuscript bib items are the authors' to fix**: Cattaneo 1948's journal/pages (C2), the Luchko book entry (C3), and the DPL attribution naming (C5). I have reported them; I have not edited anything outside `verification/` and `api_log/`.
