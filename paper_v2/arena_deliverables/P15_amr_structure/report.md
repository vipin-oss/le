# P15 — What Applied Mechanics Reviews actually looks like, and what our paper must become

Evidence only. No `.tex` was edited, no PDF is in this repository, and no library location, folder or
Drive identifier is written here. Every number below was read off the PDF or counted from the source
tree; where a number could not be read it says **NOT READ**.

Deliverables in this folder: `report.md` (this file), `amr_papers.csv` (one row per AMR article, 28
fields), `restructure_plan.md` (the proposal, section by section), `check_p15.py` (the gate).

---

## 0. Which AMR articles the library holds — three, and the third was hiding

**Found and read in full (85 pages of PDF between them):**

| # | Article | Journal reference | Pages | DOI printed? |
|---|---|---|---|---|
| 1 | Chandrasekharaiah, D. S., "Thermoelasticity with second sound: A review" | *Appl. Mech. Rev.* **39**(3) (1986) 355–376 | 22 | no (pre-DOI) |
| 2 | Chandrasekharaiah, D. S., "Hyperbolic thermoelasticity: A review of recent literature" | *Appl. Mech. Rev.* **51**(12), Part 1 (1998) 705–729 | 25 | no |
| 3 | Hussein, M. I., Leamy, M. J., Ruzzene, M., "Dynamics of Phononic Materials and Structures: Historical Origins, Recent Progress, and Future Outlook" | *Appl. Mech. Rev.* **66** (2014), article 040802 | 38 (paged 040802-1 … 040802-38) | yes, 10.1115/1.4026911 at the end of the abstract |

Articles 1 and 2 are the same author's Part I and Part II; article 3 is the modern quantitative review.
Together they span **twenty-eight years** of the journal, which is why the "varies" column in §3 is as
useful as the "invariant" one.

**How the third was found — and why a name search misses all of this.** The library's own inventory sheet
has a journal column with 500 rows, and **zero of them name *Applied Mechanics Reviews***; all three AMR
articles are filed as unidentified or as bare DOI numbers. So the search had to be done three ways:

1. **DOI prefix 10.1115/1** (ASME). Five files in the library carry such a number. Three are AMR:
   10.1115/1.4026911 (article 3), 10.1115/1.3098984 (a second copy of article 2), and
   10.1115/1.3143705 (**article 1**, which nobody had identified: opening it shows "Appl Mech Rev vol 39,
   no 3, Mar 1986 355"). The other two are **not** AMR: 10.1115/1.2822329 is Tzou 1995 in *ASME J. Heat
   Transfer* 117, 8–16, and 10.1115/1.332803 belongs to *J. Appl. Phys.* (AIP), not ASME.
2. **Author and title keywords**: "Hussein", "Chandrasekharaiah", "Applied Mechanics", "review",
   "survey", "overview", "advances", "second sound", "Noda", "Hetnarski", "Tauchert". The extra hit
   "Chandrasekharaiah 1988" is *Acta Mechanica* 71, 39–49 — not AMR.
3. **Full-text search** of the library for "Applied Mechanics Reviews": 60+ hits, all of them citations
   *of* AMR inside other papers plus the three AMR articles themselves.

**Missing, and listed rather than guessed:**

* **Noda, N., "Thermal stresses in materials with temperature-dependent properties", *Appl. Mech. Rev.*
  44 (1991) 383–397, DOI 10.1115/1.3119511** — cited by our own review, **not in the library**, so
  **NOT READ** (P8 already carried it as `NOT CHECKED`).
* Any other AMR review of waves, thermoelasticity or metamaterials: not in the library, therefore not
  read. No non-AMR review was substituted to pad the sample.

---

## 1. Article 1 — Chandrasekharaiah 1986 (AMR 39(3):355–376), read in full

* **22 pages**, printed 355–376; page 355 reads "Appl Mech Rev vol 39, no 3, Mar 1986 © Copyright 1986
  American Society of Mechanical Engineers".
* **Six numbered sections**, headings in capitals with a period after the number:
  *1. INTRODUCTION · 2. LAW OF HEAT CONDUCTION · 3. THERMOELASTICITY · 4. THERMOELASTICITY WITH THERMAL
  RELAXATION · 5. TEMPERATURE-RATE DEPENDENT THERMOELASTICITY · 6. CONCLUDING REMARKS.*
* **No numbered subsections.** Sections 4 and 5 — the two longest — run as continuous prose; where the
  author needs a break he uses unnamed paragraphs.
* **Equations numbered per section**: (2.1)–(2.9), then section 3, 4 and 5 series up to (5.58);
  **142 numbered equations** in all.
* **Figures 0; tables 2** — TABLE I (p. 364, "Numerical data for an aluminium material in the contexts of
  CTE and ETE") and TABLE II (p. 371). Roman numerals, plain numeric columns, no rules-and-shading
  styling.
* **Abstract 131 words**, no DOI, no keywords line.
* **References**: alphabetical, unnumbered, author-year format —
  `Beevers, C E (1973). Stability of waves and shock structure…, Acta Mech, 17, 55-68.` About **238
  entries in the main list** and **about 74 more in a second list headed ADDITIONAL REFERENCES**
  (pp. 375–376) — a device no other article in the sample uses. Counts are from year tokens in the
  extracted text; the article itself states no total.
* **ACKNOWLEDGEMENTS on p. 372, immediately before REFERENCES**, and the last section before them is
  **6. CONCLUDING REMARKS** (p. 372).
* **Citation in text is author-year**: "(Biot, 1956)", "(Parkus, 1976)".
* **History is in the opening section** — there is no dedicated historical section.
* The article closes with a short **author biography** (last page).

## 2. Article 2 — Chandrasekharaiah 1998 (AMR 51(12):705–729), read in full

* **25 pages**, printed 705–729; page 705 reads "Appl Mech Rev vol 51, no 12, Part 1, December 1998" and
  "ASME Reprint No AMR260".
* **Eight numbered sections**: *1 INTRODUCTION · 2 HYPERBOLIC HEAT CONDUCTION · 3 THERMOELASTICITY WITH
  THERMAL RELAXATION · 4 TEMPERATURE-RATE DEPENDENT THERMOELASTICITY · 5 UNIFIED APPROACH TO ETE AND
  TRDTE · 6 THERMOELASTICITY WITHOUT ENERGY DISSIPATION · 7 OTHER THEORIES · 8 CONCLUDING REMARKS.*
* **No numbered subsections** anywhere.
* **Equations 141, numbered per section** — (2.1) … (2.28), 3.x, 4.x, 5.x, (6.1) … (6.57), (7.1) … (7.8).
* **Figures 0; tables 0.** No boxed summary, no nomenclature, no appendix.
* **Abstract 101 words**; no keywords; no DOI on the page.
* **References 338** — stated in the abstract itself ("There are 338 references"). A line-based count of
  the extracted text finds 330 entry starts; the gap is line wrapping, so the article's own 338 stands.
  Format: alphabetical, unnumbered, author-year, abbreviated journals.
* **ACKNOWLEDGEMENT on p. 724, immediately before REFERENCES**; last section **8 CONCLUDING REMARKS**
  (p. 723); **author biography** on p. 729.
* **Citation in text is author-year**: "(Chandrasekharaiah, 1986a)", "(Joseph and Preziosi 1989, 1990)".
* **No dedicated historical section** — history sits in §§1–2 and defers to Part I.
* **§7 "OTHER THEORIES" (p. 722) is where dual-phase lag first enters an AMR review.** Our paper has to
  differentiate itself from that eight-page treatment explicitly, because AMR's readers have seen this
  material before.

## 3. Article 3 — Hussein, Leamy & Ruzzene 2014 (AMR 66:040802), read in full

* **38 pages**, paginated with an **article number** (040802-1 … 040802-38); footer "*Transactions of the
  ASME*".
* **Six numbered sections**: *1 Introduction · 2 Basic Concepts · 3 Computational Analysis Techniques ·
  4 Theoretical Studies · 5 Experimental Studies · 6 Outlook.*
* **Subsections, verbatim** — §1: *1.1 Historical Origins*; *1.2 Periodic Materials and Structures in
  the 20th Century* (with *1.2.1 Composite Materials*); *1.3 Phononic Crystals*; *1.4 Acoustic/Elastic
  Metamaterials*. §3: *3.1 Overview of Band Structure Computational Techniques*; *3.2 Model Reduction for
  Band Structure Calculations*.
* **Figures 43; tables 0.** No boxed summary, no nomenclature, no appendix.
* **Equations 86, numbered sequentially** (1)…(86) — the numbering convention changed since the 1990s.
* **Abstract 259 words**, ending with `[DOI: 10.1115/1.4026911]`; **no keywords**.
* **References 408**, numbered [1]…[408], **in order of appearance** (Newton [1], Rayleigh [2] at first
  mention), entries in ASME house format: initials after surname, year, quoted title, abbreviated journal,
  volume, page or article number, no DOIs.
* **Acknowledgment on p. 040802-31, immediately before References**; last section **6 Outlook**
  (p. 040802-30).
* **History first**: §1.1 "Historical Origins" — the title advertises it.
* **Figure style**: colour used freely — 28 of the 43 embedded images carry colour, 15 are greyscale line
  art; captions **sentence case, no terminal period, self-contained, panel labels (a), (b) inside the
  caption, median 34 words**.

---

## 4. The AMR pattern, as the three articles actually print it

**Invariant across all three (safe to design against):**

1. A descriptive title, an author block with affiliation and e-mail, and a **single-paragraph abstract**.
2. **Few numbered top-level sections** — 6, 8, 6. Never dozens.
3. A **flat or two-level heading tree**: one of the three articles has no subsections at all, and the
   2014 one stops at three levels only once (1.2.1).
4. **Acknowledgements immediately before the references**, at the very end of the body.
5. **The last section is the conclusion**: "CONCLUDING REMARKS" (1986, 1998) or "Outlook" (2014). No
   data or appendix comes after it except the reference list.
6. **No nomenclature and no appendix in any of the three.** Nothing sits between the last section, the
   acknowledgements and the references.
7. **History at the front** — either a labelled first subsection (2014) or the opening paragraphs of
   §1 (1986, 1998). Never a separate "history" chapter far into the paper.
8. **Equations are numbered, and every equation that matters carries a number** (142, 141, 86).
9. **The reference list is the largest single object in the back matter** (about 312, 338, 408 entries).

**Varies between them — so it is a template choice, not a rule:**

| Feature | 1986 | 1998 | 2014 | Recommendation for us |
|---|---|---|---|---|
| Citation | author-year | author-year | numeric [n], order of appearance | **follow 2014** (current ASME) — and we already do |
| Reference list | alphabetical + ADDITIONAL REFERENCES list | alphabetical | numbered, order of appearance | numbered; no second list |
| Equation numbering | per section | per section | sequential | **sequential** (our current) |
| Figures | 0 | 0 | 43, colour, long captions | ours has 40 — keep, reformat captions |
| Tables | **2** (data tables) | 0 | 0 | the sample never exceeds 2; ours has 26 |
| Abstract length | 131 words | 101 words | 259 words | 200–250 |
| Keywords line | none | none | none | none in the PDF |
| Author biography | yes | yes | no | drop (the practice died with the format change) |
| Section-heading case | CAPITALS with "1." | CAPITALS | Title case, "1" | Title case, no period after the number |

**What AMR does *not* do, and we currently do**: highlights box, graphical abstract, keywords line, a
table-of-contents page, a nomenclature block, CRediT statement, competing-interest declaration, ten
appendices, 26 tables. None of these is forbidden — ASME's current policy *requires* some of the
declarations — but none of them appears in any of the three articles, and the sample's own house style is
markedly leaner than ours in every one of those dimensions.

---

## 5. Our paper, front to back, against that pattern

Source of truth: the compiled **`main.pdf` on branch `review-paper-v2`, 173 pages**, whose PDF outline I
read directly (222 entries, 54 top-level). Numbered sections run **1 … 39**; appendices A … J follow;
the last thirty-odd pages are registers. Measured from that same PDF:

| Quantity | Our paper (173-page build) | AMR 1986 | AMR 1998 | AMR 2014 |
|---|---|---|---|---|
| Pages | **173** | 22 | 25 | 38 |
| Numbered top-level sections | **39** | 6 | 8 | 6 |
| Appendices | **10** | 0 | 0 | 0 |
| Figures | **40** | 0 | 0 | 43 |
| Tables | **26** | 2 | 0 | 0 |
| Numbered equations | **90** (sequential) | 142 (per section) | 141 (per section) | 86 (sequential) |
| References | **414** (numbered, order of appearance) | ≈312 | 338 | 408 |
| Abstract words | **329** | 131 | 101 | 259 |
| Keywords | **11** | none | none | none |
| Nomenclature | **yes** (p. 10) | no | no | no |
| Contents page | **yes** (p. 2) | no | no | no |
| CRediT / declarations | **yes** | no | no | no |

Front-to-back map (our 173-page build → what AMR does in the same position):

| Position | Ours | AMR | Action |
|---|---|---|---|
| p. 1 | Title + long subtitle; author; date | title; author block with ASME membership line and e-mail footnote | shorten the title, move the subtitle into the abstract, add the ASME membership footnote |
| p. 1 | **Highlights** box, 5 bullets | none | fold into §1 as a bulleted "what this review adds", no box |
| p. 2 | **Graphical abstract** as Figure 1 | none, but colour figures are normal | renumber as **Fig. 1** and present it as the road map of §1 |
| p. 2 | **Contents** page | none | remove from the journal PDF (keep in the repository build) |
| pp. 2–3 | **Abstract**, 329 words | 131 / 101 / 259 | cut to ≤250 and move the remainder into §1 |
| p. 3 | **Keywords**, 11 | none in any of the three | keep only in the submission metadata |
| p. 10 | **Nomenclature** | none in any of the three | merge into Appendix F (glossary + working formulas), or keep if the Editor insists |
| pp. 11–16 | §1 Introduction, §2 Historical development | §1 Introduction **with** 1.1 Historical Origins | merge: history becomes §1.1 |
| pp. 19–27 | §3 Foundations, §4 Preliminaries, §5 Kinetic origin | §2 Basic Concepts | merge into one §2 |
| pp. 29–42 | §6 Classical, §7 LS/GL/GN, §8 DPL/TPL/MGT, §9 Fidelity | theory block of 2014's §2 and §4 | one §3 with four subsections |
| pp. 43–47, 70–77 | §10–§12 fractional/memory/causality; §24 size; §25 wider classes | no counterpart in the sample | one §4 "beyond the template" |
| pp. 48–68 | §13–§23 waves, surfaces, interfaces | 2014's §2 and §4 treatment of dispersion | one §5 with eleven subsections |
| pp. 77–80 | §26 couplings, §27 piezo SH waves | no counterpart | §6 |
| pp. 82–90 | §28 methods, §29 FD benchmark, §32 worked examples | 2014's §3 Computational Analysis Techniques | §7 |
| pp. 86–91 | §30 applications, §31 regime guide, §33 experiments | 2014's §5 Experimental Studies | §8 |
| pp. 94–106 | §34 synthesis, §35 atlas, §36 reporting, §37 taxonomy, §38 open problems | 2014's §6 Outlook | §9 synthesis (with the one master table); atlas and reporting become appendices; open problems merge with §39 |
| p. 109 | §39 Conclusions | §6 Outlook / §8 Concluding remarks | final section "Conclusions and outlook" |
| p. 109 | Acknowledgements, CRediT, competing interest | Acknowledgements immediately before the references | keep, in AMR's position |
| pp. 110–140 | Appendices A–J, 10 items | none | keep (they carry the paper's value); for the journal PDF only with the Editor's agreement |
| pp. 141+ | References, 414 | ≈312 / 338 / 408 | reformat to ASME house style |

The full proposal — which section merges where, what is renamed, what moves to an appendix, where the
single summary table and the outlook go, and how all 173 pages survive intact — is
**`restructure_plan.md`**.

---

## 6. Reference style: we are closer to ASME than the brief assumed

**What our source actually does.** `main.tex` loads
`\usepackage[numbers,sort&compress]{natbib}` and sets `\bibliographystyle{unsrtnat}`, and the compiled
PDF cites numerically — the first citation on p. 11 reads "the classical coupled theory of Biot [1]".
So our citations are **already numeric, bracketed and numbered in order of appearance**, which is exactly
the 2014 AMR convention. The brief's premise ("our unsrtnat/natbib author-year") is not what the file
does.

**What is genuinely different is the *entry format*, not the citation scheme.**

| Property | AMR 2014 (what we must match) | Our current output |
|---|---|---|
| Citation in text | [n], ranges as [286,404–407] | [n], ranges via `sort&compress` — **already correct** |
| Order | order of appearance | `unsrtnat` — **already correct** |
| Entry shape | `Hussein, M. I., and Leamy, M. J., 2014, "Title," ASME J. Vib. Acoust., 135(4), p. 040201.` | `Hussein, M. I., Leamy, M. J. (2014). Title. Applied Mechanics Reviews, 66:040802. doi: …` |
| Journal names | **abbreviated**, ASME list ("Appl. Mech. Rev.", "ASME J. Heat Transfer") | **full names** |
| Title | in **quotes**, title case | no quotes, sentence case |
| Year | after the author list, before the title | in parentheses after the authors |
| Page or article number | `p. 040802` / `pp. 529–532` | `66:040802` / `27(3):240–253` |
| DOI | not printed in any of the three AMR articles | printed in every entry |
| Proceedings | `Proc. SPIE, Vol. 1, IEEE, pp. 529–532` | `In: Proceedings of …` |

**What must change, concretely:**

1. **Replace the bibliography style.** `\bibliographystyle{unsrtnat}` → `\bibliographystyle{asme2e}`
   (ASME's own `.bst` for its journals), keeping `\usepackage[numbers,sort&compress]{natbib}`; if the AMR
   template ships `asmejour.bst` with the ASME class, use that. Do **not** keep `unsrtnat`.
2. **Abbreviate journal names across all four bib files** (`refs, refs_extra, refs_new, refs_atlas`):
   `Applied Mechanics Reviews` → `Appl. Mech. Rev.`, `International Journal of Heat and Mass Transfer` →
   `Int. J. Heat Mass Transf.`, `Journal of Thermal Stresses` → `J. Therm. Stresses`, and so on for the
   414 entries; re-check for near-duplicates afterwards.
3. **Drop `doi` and `url` fields** from the printed list, and convert `66:040802` to an article-number
   form (`p. 040802`) — none of the three AMR articles prints a DOI in the list.
4. **Protect the numbering.** After the style swap verify that the first citation is still [1] and the
   last [414]; a `.bst` change can reorder if any `\nocite` is present.
5. **Keep the second-list habit out.** Article 1 has an ADDITIONAL REFERENCES list; that is a 1986
   device, not a current one. One list only.
6. **Nothing changes about which works are cited** — all 414 stay; only their rendering changes.

---

## 7. What the pre-submission inquiry should say

* AMR review length is open, so 173 pages is permitted; but the three AMR reviews in the library are 22,
  25 and 38 pages — **we are proposing a paper four to eight times longer than the journal's own recent
  practice**, with 414 references against 408 (the largest in the sample). That contrast is the single
  most useful sentence to put in the inquiry, because it lets the Editor answer the length question
  before a reviewer does.
* Say plainly that Appendices A–J (~31 pages: derivations, registers, catalogue, glossary, benchmarks)
  can move to ASME supplementary material at no loss of content if the Editor prefers.
* Say that the front matter will be brought to AMR house style: no highlights box, no contents page, no
  keywords in the PDF, history merged into §1.1, one summary table instead of 26, a final "Conclusions
  and outlook", and the references reformatted with ASME's own bibliography style.

---

## 8. Limits of this study (what is NOT READ)

* **Three AMR articles, all read page by page** — but only **one** is from the current (post-2010)
  template. Where the three disagree I recommend the 2014 side and say so; where all three agree I call it
  a pattern, not a rule. A fourth, modern AMR review would test the table policy best.
* **Noda 1991 (AMR 44:383)** is cited by our review and absent from the library: **NOT READ**, listed,
  not guessed.
* Counts are from the PDFs: page counts and printed page ranges from the page footers, reference counts
  as stated in the article (1998) or as the highest printed number (2014) or counted from year tokens
  (1986, where the text states no total), abstract lengths from the abstract text, figure and table
  counts from the figure/table captions, equation counts from the numbered equations. The "28 of 43
  images carry colour" figure is a pixel-level count of the embedded images, so it describes the artwork,
  not the printed plate.
* Our paper's counts in §5 come from the 173-page build's own PDF: 40 figure captions ("Figure n:"), 26
  table captions, highest equation number 90, 414 distinct reference numbers, 39 numbered sections, 54
  top-level outline entries. The older 164-page snapshot measured in P6 gave 337 references and 25
  tables; the difference is the reference sets added in P8/P10/P13. Both sets of numbers are recorded;
  neither is guessed.
