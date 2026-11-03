# Language audit — *Waves in Thermoelastic and Multiphysics Continua*

**Report only. No manuscript file was edited in this pass.** The only files added are this summary and the
row-by-row table `paper_v2/language_audit_report.csv` (209 rows).

- Manuscript synced to `review-paper-v2` @ `e2e377f1b2ced5646f9fb19ebec78afc41833ecb` (commit `b157774`).
  Only `sections/s03d_admiss.tex` differed from the previous state (the author moved a `\citep{ChenNunziato1974}`
  to cover the initial-value sentence); `main.tex` and the other 52 section files were identical.
- Scope judged: language and reading experience only. Math, numbers, citations, the atlas "Reported result"
  cells and the `appD_catalogue` titles were **not** assessed.
- Measurement base: 1 592 prose sentences / 36 704 prose words outside tables, figures, catalogue and atlas
  rows (53 section files + abstract). Statistics in this summary are computed on that base.

## 1. Counts

| Type | Rows | Share |
|---|---:|---:|
| LONG/DENSE | 88 | 42 % |
| PRONOUN | 43 | 21 % |
| TONE | 25 | 12 % |
| FLOW | 12 | 6 % |
| PASSIVE/NOMINALIZATION | 11 | 5 % |
| GRAMMAR/SPELLING | 10 | 5 % |
| REPETITION | 8 | 4 % |
| TERMS | 7 | 3 % |
| STYLE | 5 | 2 % |
| **Total** | **209** | |

| Severity | Rows |
|---|---:|
| HIGH | 28 |
| MED | 157 |
| LOW | 24 |

47 files carry at least one row. The densest files (weighted rows per 1 000 prose words) are `s01_intro` (26.6),
`s15e_identify` (24.5), `s16b_atlas` (22.3, prose only), the abstract in `main.tex` (18.8), `s07b_fraccoupled`
(17.3), `appH_registry` (17.1), `s13_multiphysics` (16.8), `s07_memory` (16.7), `s17_open` (16.6).

## 2. Term-consistency table

Counts are over `sections/*.tex` + `main.tex`, case-insensitive, whole words.

| Concept | Variants used (count) | Where | Recommended single term |
|---|---|---|---|
| The delayed heat law | *lag* (181), *delay* (36), *relaxation time* (32) | *delay* concentrated in s06b, s02, s15c; *lag* everywhere else; *relaxation time* for τ₀, τ_R and τ_Z | **lag** for τ_q, τ_T, τ_v; **delay law** only for the un-truncated shift law; **relaxation time** only for τ₀, τ_R, τ_Z — with one sentence in §2 defining the three |
| The organizing object | *template* (71, of which *the template* 44), *heat-flux template* (8), *family* | s01b summary box, s03, s16c | **the heat-flux template** on first use, **the template** thereafter; **member** for a named theory — never *family* for the same thing |
| A member of the family | *heat law* (43), *heat-flux law* (17) | throughout | **heat law** (short form), **heat-flux law** only where the flux is the subject |
| Propagation speed | *phase speed* (28), *wave speed* (10), *phase velocity* (4), *speed* | *phase velocity* in s15e, s16b cells; *wave speed* in s01b, s02, s06, s11 | **phase speed** for Im/Re k; **front speed** or **c_s** for the thermal front; keep **group velocity** only where v_g is meant |
| The paper itself | *this review* (41: 11 "in this review", 11 "of this review"), *this paper* (7), *this work* (2), *the review* (11), *the paper* (6) | abstract, §1, §2, every summary box | **this review** as the only self-reference; delete or recast the rest |
| Checking apparatus | *the register* (23), *claim register* (1), *equation register* (0 as such), *evidence protocol*, *check* (83), *verification* (16) | §2, §18, App. C, App. H, App. EqReg | **the register** (single name), with **evidence protocol** reserved for §2's rules |
| Spelling of "nonlocal" | *nonlocal* (129), *non-local* (3 in own prose, 2 more inside verbatim titles) | s03b:31, s16b:62 (verbatim cell), catalogue | **nonlocal** in the paper's own prose (US spelling rule already followed elsewhere) |
| Spelling of "second sound" | *second sound* (18), *second-sound* (3) | s02:5, s15c:6 | **second sound** as a noun, **second-sound** only attributively — pick one and apply it |
| Spelling of compound modifiers | *memory-dependent* (59) vs *memory dependent* (2), *phase-lag* (70) vs *phase lag* (7), *half-space* (70) vs *half space* (9) | the minority forms are almost all inside verbatim catalogue titles and atlas cells (correctly left alone); the only prose exception is *phase lag* in s03b | keep hyphenated forms in prose; do not touch verbatim titles |

## 3. Top 15 repeated phrases / frames

| # | Phrase or frame | Count | Comment |
|---|---|---:|---|
| 1 | sentence-initial "The …" | 324 of 1 592 (20 %) | single dominant opener; with the claim→reason→consequence paragraph shape it produces a monotone rhythm |
| 2 | "is the" | 93 | definitional frame ("X is the …") used as the default sentence pattern |
| 3 | "therefore" | 49 | often marks a step that is not a deduction (3× in s06 alone) |
| 4 | "the template" | 44 | term density, fine once §2 fixes the term, heavy in s03/s16c |
| 5 | "heat law" | 43 | plus 17 "heat-flux law" (see table) |
| 6 | "this review" | 41 | the single most repeated self-reference |
| 7 | "so the" | 30 | causal cadence |
| 8 | "is not" | 30 | negation frame; contributes to the defensive tone rows |
| 9 | "so that" | 27 | purpose-clause cadence, one per paragraph in places |
| 10 | "which is" | 27 | relative-clause default |
| 11 | "rather than" | 27 | contrast frame; often replaces an argument |
| 12 | "does not" | 23 | |
| 13 | "That is" (all positions) | 23 | demonstrative hinge; 43 PRONOUN rows are of this family |
| 14 | "at high frequency" | 18 | also "at low frequency"; the frequency-limit paragraph shape recurs verbatim |
| 15 | "second sound" | 18 | content term, but 3 hyphenated variants |

Section-opening formulas worth counting as a frame on their own: three sections open with "This section …"
and seven paragraphs with "Here …"; four sections open with a two-to-five-word paragraph ("The theory above is isotropic.",
"Three limits follow directly.", "It is a map, not a derivation.", "The consequence for the literature is practical.").

## 4. Section scorecard

Score 1–5 (5 = publication-ready language). The *read* column says how the section was read:
**full** = every sentence; **target** = every sentence of 30+ words, every pronoun-initial sentence, and the
opening and closing sentence of every paragraph; **flag** = targeted read plus the automatic statistics only
(short sections whose prose is almost entirely inside tables or item lists).

| Section | Score | Read | One-line reason |
|---|---:|---|---|
| Abstract | 3 | full | clear and accurate, but four sentences open with "the review", one coy phrase ("appear, or fail to appear"), one orphan close |
| 1 Introduction | 2 | full | highest defect density in the paper: 41-word opener, four "first/second/third/fourth" stubs, list-shaped paragraphs, boilerplate transition, two weak demonstratives |
| 2 Review scope | 3 | full | eleven rows; five 30+ word claims written as balanced semicolon pairs, defensive asides ("rather than believed", "needs one caution"), hard-coded `Section~\ref` |
| 3 History | 3 | target | citation-heavy catalogue sentences (32–49 words) in a narrative that otherwise reads well |
| 4 Foundations | 3 | target | nine rows; long notational sentences, inverted "Here lies …", several bare "They" with competing antecedents |
| 5 Kinetic basis | 3 | target | "They explain these experiments" and a 45-word Cattaneo-closure sentence |
| 6 Conventions | 4 | target | two pronoun openings, otherwise clean |
| 7 Admissibility | 3 | target | definition sentence packs four claims; "necessary, not sufficient" paragraph is fine |
| 8 Classical theory | 3 | target | eight rows, four of them 31–44-word technical sentences with parentheticals inside the main clause |
| 9 Flexural damping | 4 | target | one pronoun row; equations and text otherwise well matched |
| 10 Hyperbolic theories | 3 | target | eleven rows, the densest technical prose in the paper; three 32–45-word sentences in §5.1 alone, plus a "not merely asymptotically" emphasis |
| 11 Lagging models | 3 | target | a capital "For" after a semicolon (36-word sentence), three one-line hinge paragraphs |
| 12 Delay fidelity | 3 | target | capital "The" after a colon in a 41-word sentence; evaluative section opening |
| 13 Memory models | 3 | target | eight rows: "The literature cites three motivations" (vague attribution), comma + capital "Here", two 39–49-word sentences |
| 14 Fractional dispersion | 4 | target | two rows; "Here …" opening |
| 15 Modulus and causality | 3 | target | "A wave measurement does not return k(ω)", "Three limits follow directly", bare "It is equivalent to …" |
| 16 Three-dimensional waves | 3 | target | capital "What" after a semicolon; 47-word reflection sentence |
| 17 Anisotropy | 3 | target | opens with the two-word paragraph "The theory above is isotropic." |
| 18 Reflection | 3 | target | passive opening, "is no gain" (informal), two bare demonstratives |
| 19 Transient problems | 3 | full | capital "With" after a semicolon, four "was … by \citep" passives, a 33-word front sentence, a circular summary close |
| 20 Thermal modes | 4 | target | one 30+ word sentence that mixes an integral, a comparison and an eigenfrequency |
| 21 Surface waves | 3 | full | three 30–33-word sentences in the results subsection; the physics text is otherwise careful |
| 22 Lamb waves | 4 | target | one three-word disclaimer sentence |
| 23 Bar modes | 4 | target | one colon sentence that hides a formula |
| 24 Interfaces | 3 | target | passive "It was solved", "That is not the same as …", entropy-production sentence |
| 25 Layered media | 3 | full | seven rows: a triple-passive opener, four 32–39-word sentences, a bare "He" |
| 26 Size effects | 3 | full | a 42-word calibration sentence, a 44-word damping sentence, four "by \citep" passives |
| 27 Wider classes | 3 | target | meta-opening, "It is a map, not a derivation", 45-word kernel sentence |
| 28 Multiphysics | 3 | full | seven "was … by \citep" sentences in one paragraph, a capital after a semicolon, two 41–42-word sentences |
| 29 Piezoelectric surface waves | 3 | target | two bare "It" openings |
| 30 Solution methods | 3 | full | "Second," with no "First,", a conversational verdict on its own table, three 34–36-word method sentences |
| 31 Numerical schemes | 4 | target | one informal verdict ("hides the real difficulty") |
| 32 Applications | 3 | target | a one-sentence orphan paragraph ("… was analyzed by \citep{Ma2020}") breaks the subsection pattern |
| 33 Worked examples | 4 | target | repeated 10⁴ and a bare "These" |
| 34 Experiments | 3 | target | "It was predicted …" with three citation groups, "They do not show …", "A mismatch can be blamed …" |
| 35 Regime guide | 3 | target | five-word opening paragraph, two 39–49-word sentences |
| 36 Identifiability | 3 | target | 53-word sentence carrying four checks and a singular-value vector |
| 37 Synthesis | 3 | target | capital "A" after a colon, 66-word threshold sentence, "It is a guide, not a substitute" |
| 38 Atlas | 3 | target | prose only: 37-word opening; the table cells themselves are source wording and were not assessed |
| 39 Taxonomy | 3 | target | eight rows; abstract vocabulary ("collapses", "earns its place"), bare "It"/"they" in four places |
| 40 Open problems | 3 | target | 51-word and 46-word items, "buys three kinds of result" |
| 41 Conclusions | 3 | target | three 31–44-word sentences in the final three paragraphs, where the reader is most likely to quote |
| 42 Reporting standards | 3 | target | four 33–39-word instructions, each mixing two instructions |
| 43 Declarations | 4 | target | one 45-word list sentence |
| App. A Balance laws | 4 | flag | one colon sentence |
| App. B, C | 4 | flag | App. C: one 43-word sentence |
| App. D Catalogue | 5 | not assessed | verbatim title list; language deliberately not judged |
| App. E Glossary | 5 | flag | definitions, no prose issues |
| App. Eq. register | 4 | flag | table-driven; prose is short |
| App. F Debye | 4 | flag | short prose |
| App. G Units | 4 | flag | one 31-word table note, length from unit definitions |
| App. H Registry | 4 | target | two 36–42-word requirement sentences |
| Nomenclature | 5 | flag | list of symbols |

**Top ten sections that need the most work** (weighted defect density, with the two longest sections kept in on
absolute count):
1. Introduction (§1, 26.6 per 1 000 words) 2. Multiphysics (§28, 16.8) 3. Memory models (§13, 16.7)
4. Hyperbolic theories (§10, 16.5 weighted rows — the largest absolute load outside §1)
5. Review scope (§2, 14.5 weighted) 6. Open problems + Conclusions (§40–41, 16.5)
7. Taxonomy (§39, 15.7) 8. Classical theory (§8, 12.0) 9. Layered media (§25, 15.7) 10. Identifiability (§36, 24.5).
The abstract is outside this ranking but is the fourth densest page in the manuscript (18.8).

## 5. What an editor will see in the first ten pages

1. **The abstract repeats its own frame.** "This review organizes …", "The review records …", "the review
   identifies …", "The review then treats …" in fifteen sentences, plus "appear, or fail to appear" — the first
   thing an AMR editor reads is the least edited prose in the paper.
2. **The Introduction reads as a list of stubs.** "The first is …", "The second is …", "The third is …",
   "The fourth is …" and then "One …", "A dispersion polynomial …", "Coupling to …", "Solution methods …" — seven
   short list-shaped paragraphs. A 41-word opening sentence is followed almost entirely by sentences under
   20 words, so the rhythm is extreme in both directions.
3. **Self-referential boilerplate arrives early and often**: "This review covers the following ground.",
   "That is the aim of this review.", "Three observations shaped the organization of this review."
4. **Six blunt punctuation faults of the same family** appear in the first half of the paper: a capital "For"
   after a semicolon (§11), a capital "The" after a colon (§12), a capital "Here" after a comma (§13), a capital
   "What" after a semicolon (§16), a capital "With" after a semicolon (§19) and a capital "Thermal" after a
   semicolon (§28). All six are residue of earlier sentence splitting and all six are one-character fixes.
5. **Cross-reference style changes with the page**: `Section~\ref` (58) beside `\cref`/`\Cref` (140) beside
   `Sec.~\ref` (8, in figure labels); `\eqref` (151) beside `\cref{eq:…}` (27) and `Equation~\eqref` (3).
6. **Scope section argues with an imagined critic**: "so that the claim can be checked rather than believed",
   "C5 needs one caution, because it is the row a reader is most likely to over-read", "The protocol has limits,
   and they are part of it". This is where the paper's credibility apparatus is introduced, and it currently
   sounds defensive rather than procedural.
7. **Citations used as the agent of a passive verb** ("… was studied by \citep{…}") first appear in §3 and
   recur 43 times; the worst single paragraph is in §28, with seven in a row.
8. **One-line hinge paragraphs** ("Two further developments widened the field.", "The consequence for the
   literature is practical.", "Three limits follow directly.", "The theory above is isotropic.") appear on
   nearly every second page and give the prose a stop-start feel.

## 6. Reading status

- **Full read** (every sentence): abstract, §1 Introduction, §2 Review scope, §19 Transient problems,
  §21 Surface waves, §25 Layered media, §26 Size effects, §28 Multiphysics, §30 Solution methods, §40 Open
  problems (prose and table captions), §41 Conclusions.
- **Targeted read** (every 30+ word sentence, every pronoun-initial sentence, every paragraph opening and
  closing, all summary boxes and captions): the remaining 44 section files listed as *target* in the scorecard.
- **Not read for language**: `appD_catalogue.tex` titles and the atlas "Reported result"/"Problem" cells —
  these are source wording and are excluded by the brief. No section of the paper was left unread otherwise.

## 7. Method and limits

- Sentence boundaries and word counts come from a local scanner that removes display math, tables, figures,
  citations, labels and cross-references before counting; inline math still contributes placeholders, so word
  counts for math-heavy sentences are approximate.
- Repetition counts are case-insensitive whole-word counts over `sections/*.tex` and `main.tex`.
- `suggested_fix` reproduces the original sentence with math, citations and numbers copied unchanged; where a
  sentence contains a table cell or a verbatim source quotation, the fix says so rather than rewriting it.
- No LaTeX engine is available in this environment, so nothing here has been compile-checked.
