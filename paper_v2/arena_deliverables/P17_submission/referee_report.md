# Independent referee report — Applied Mechanics Reviews

**Manuscript.** "Waves in Thermoelastic and Multiphysics Continua: Generalized Heat Conduction, Coupled Fields and Size Effects"
**Author.** Vipin Gupta, Gurugram University
**Version read.** The compiled paper of 2 November 2026, 157 pages, taken from the submitted package on the manuscript branch (`main.pdf`, 1,535,378 bytes; 157 pages).
**Report date.** 2 November 2026.

---

## 0. What was read, and how this report was produced

This report was written from the compiled paper only, as a referee who has not seen any earlier internal audit, checklist or merge log of the manuscript. Nothing in the sections below is carried over from an earlier review of the same material.

Coverage of the read, stated plainly so that the author can discount what was not read:

* the front matter and the abstract in full (p. 1–2);
* **p. 1–35 in full** — Sections 1, 2, 3 and 4 to Section 4.4 inclusive;
* **p. 84–92 in full** — Sections 10 and 11, the acknowledgements and the declarations;
* **p. 36–83 in extract** — all section and subsection headings, the opener and the summary of every subsection, all 41 figure and 25 table captions, and the full text of Sections 6.9 (flexure), 7.1 (further couplings) and 8.2 (the finite-difference benchmark); the detailed numerical results on p. 36–58 and p. 62–83 were **not** read line by line, and no finding in this report rests on them except where a page is cited;
* the declarations and nomenclature (p. 92–95);
* Appendices A, B, C, D (p. 95–97) and L (p. 124–126) in full; Appendix E sampled by its ten subsection openers (p. 97–109); Appendix J read in full including the coverage inventory (p. 113–120); Appendix K read in full (p. 121–123);
* the reference list on p. 127–154 checked **automatically** against the citation markers in the text (every one of the 414 is cited at least once; the renumbering consequences in Section 4 were computed the same way), with a sample of entries inspected by eye — the list was not proofread entry by entry, and no finding here depends on a proofread of it;
* Tables 19–21 on p. 155–157;
* all 41 figure captions and all 25 table captions;
* the *typography* of every figure was measured from the PDF content streams (minimum set size of the lettering on each page), because legibility at print size is part of what a review journal buys.

Numbers used throughout: 11 numbered sections, 12 appendices (A–L), 41 figures, 25 tables, 90 numbered equations, 414 references, 157 pages, of which the body is 94 pages, the appendices 32 pages (p. 95–126) and the reference list 28 pages (p. 127–154).

Findings carry one of three labels, used in the sense a review journal uses them:

* **critical** — the manuscript cannot go to production as it stands, or a statement in it is not true of the document as printed;
* **major** — the manuscript can be reviewed but not accepted until the point is answered or fixed;
* **minor** — a correction of detail that does not affect any conclusion.

---

## 1. Overall assessment and recommendation

This is an unusually disciplined manuscript. The organisation around one heat-flux template with three lags (Eq. (14), p. 13) is genuinely useful, the reduction table (Table 4, p. 14) is the kind of thing a reader will photograph, and the evidence protocol of Section 2.4 with the page-level provenance table (Table 6, p. 29) is more than most reviews offer. The dispersion polynomial (34) is derived and symbolically checked; the DPL truncation analysis of Section 4.3.1 is a real contribution; and the paper is candid about its own limits, including the limits of its literature coverage.

Three problems nevertheless stand between this manuscript and a submission that a referee can process without irritation.

1. **It is not yet a single document.** Appendix J and Table 23 describe a *different* manuscript — 136 equations, section titles that do not exist in this paper, LaTeX labels (`eq:3.1`) — and say so in print ("the source manuscript from which this material is merged"). Tables 19–21 are printed after the last reference, under the running head "References", 58 pages after the text that cites them. These are not stylistic points: they tell a referee that the paper has been assembled from parts and not read once, end to end, in its final form.
2. **The fit to *Applied Mechanics Reviews* is asserted, not demonstrated.** AMR's remit is to organise, clarify and summarise the existing literature. This manuscript does that, but it also contains a substantial amount of new derivation and new computation, and it never says which is which against the five canonical reviews it cites ([6]–[10], [158]). The differentiation from Chandrasekharaiah (1986, 1998), Hetnarski–Ignaczak (1999, 2000), Ignaczak–Ostoja-Starzewski (2010) and Tzou (2015) is one sentence on p. 2.
3. **At 157 pages it exceeds what a review journal can print** without a decision about what is main text and what is supplementary, and that decision has a hidden cost: 75 of the 414 references (18 %) are never cited in the body, 66 of them being cited only in the catalogue of Appendix E, so a naive move of the appendices detaches one reference in six from the main text.

**Recommendation.** Major revision before formal submission. Three items must be fixed before the manuscript is sent anywhere, because each is a defect that a referee would read as evidence that the paper had not been read once in final form: **R5** (the Green–Lindsay stability condition stated two opposite ways), **R6** (the appendix that carries the paper's verification statistics describes a different manuscript) and **R14** (Tables 19–21 printed after the reference list). R1–R4 and R9–R13 are substantive and need a considered reply; R7, R8, R15, R16 and M1–M9 are corrections.

---

## 2. Fit with AMR's review purpose

### R1 · The paper is a review and a research monograph at the same time, and does not say which parts are which — **major**

Table 1 (p. 5) lists six contributions C1–C6 with the section that delivers each and the evidence that supports it. That table is excellent and is exactly the right instrument. It answers "what does this paper claim", but not "what is new to the literature". Several of C1–C6 are new results in the ordinary sense — the comparative dispersion polynomial (34), the truncation-dependence of the DPL stability statement (Section 4.3.1, Fig. 10), the finite-difference benchmark of Section 8.2, the five-axis taxonomy of Section 10.2 — while others are the review's proper business (the synthesis of Tables 14–15, the decision guide of Fig. 40). A referee at AMR has to decide whether to recommend a review or a research paper, and the manuscript does not give the information needed to decide.

*Required action.* Extend Table 1 with one column that classifies each contribution as *review* (organises existing work) or *new* (not previously published), and add one sentence to Section 1 stating the split. If the paper is submitted as a review, the new material should be presented as the review's own synthesis and its claims to novelty stated once, in Section 1, not scattered through the abstract and the section summaries.

### R2 · Differentiation from the five canonical reviews is one sentence — **major**

On p. 2: "Good reviews of generalized thermoelasticity already exist [6–9, 19, 20]. What they do not supply is a treatment for a reader who wants to use the theories on wave problems and to compare them reliably." That is the whole of the positioning. It is not enough for AMR, because the five works named are precisely the ones a referee will have in mind, and each covers a large part of what this manuscript covers:

* [6] Chandrasekharaiah, *Thermoelasticity with second sound: a review*, Appl. Mech. Rev. 39 (1986);
* [7] Chandrasekharaiah, *Hyperbolic thermoelasticity: a review of recent literature*, Appl. Mech. Rev. 51 (1998);
* [8] Hetnarski & Ignaczak, *Generalized thermoelasticity*, J. Thermal Stresses 22 (1999);
* [9] Hetnarski & Ignaczak, *Nonclassical dynamical thermoelasticity*, Int. J. Solids Struct. 37 (2000);
* [10] Ignaczak & Ostoja-Starzewski, *Thermoelasticity with Finite Wave Speeds*, OUP (2010);
* [158] Tzou, *Macro- to Microscale Heat Transfer: The Lagging Behavior*, 2nd ed. (2015).

The manuscript cites all six and uses [158] twice, both times for DPL specifics ("Tzou's own derivation of the model uses the first-order expansion", p. 31; the type classification, p. 31). Nowhere does it state what these works already do, what has changed since 1998 and 2010, and which sections of this paper exist because the earlier reviews did not cover them.

*Required action.* Add a short subsection to Section 1 (or to Section 2.1) with a comparison table: rows = the five reviews plus this paper; columns = heat-law coverage, wave problems, interfaces, multiphysics, size effects, fractional and memory models, numerical methods, literature cut-off year, number of references. This is cheap to compile from the manuscripts themselves and it converts the paper's strongest asset — that it truly does cover things the older reviews do not — into a document a referee can check. It is also the material that the "what is new" statement of the cover letter needs.

### R3 · The literature coverage is declared "deliberate rather than exhaustive", and no search protocol is given — **major**

Section 2.4 (p. 6) states: "Not every cited work was read page by page; coverage of the literature is deliberate rather than exhaustive". AMR's review purpose, as stated in its own guidance, rests on comprehensive citation. The disclaimer is honest, and honesty is worth more than a false claim; but a review with 414 references and no stated search strategy leaves the referee unable to judge whether the field is covered or merely sampled. There is no database named, no keyword string, no date window, no inclusion or exclusion rule, and no statement of how the 414 works were found.

*Required action.* Add four sentences to Section 2.2 or 2.4: the databases searched (or the snowballing procedure, if that is what was done), the date window, the inclusion rule (for example "any work that states a heat-conduction law for a thermoelastic continuum and solves a wave, resonance or interface problem"), and the exclusion rule. A snowball strategy is a perfectly respectable answer; saying so in one sentence removes the objection. If the search was not systematic, say that instead, and describe how the sample was chosen.

### R4 · The abstract's headline claim attributes a practice to the literature without naming a single example — **major**

The abstract (p. 1) states that "one widely repeated stability statement for the dual-phase-lag model is shown to depend on the order of the Taylor truncation". Section 4.3.1 (p. 30) supports the *technical* half of this with unusual care: three truncations are separated, the three thresholds are attributed correctly ([43] for τ_T > τ_q/2, [10, 158] for the type change at τ_T = τ_q, [159] for τ_T = (2−√3)τ_q), and Fig. 10 plus `fig_stability.py` show the growth rate for variants (i) and (ii). What is not supported is the attribution: the text says "the literature often quotes it as the stability condition of DPL thermoelasticity" and that papers "impose" it, and then names no paper. Section 10.1.4 repeats the claim as pitfall 1 ("The τ_T ≥ τ_q/2 condition belongs to the second-order-in-τ_q truncation").

A review that corrects a practice owes the reader the examples. Three to five would be enough, each with the page or equation where the condition appears.

*Required action.* Cite the papers that state τ_T ≥ τ_q/2 for the first-order model, with the equation number. If the practice is less widespread than the abstract implies, weaken the wording to "the condition is sometimes quoted" and adjust the abstract accordingly.

---

## 3. Scientific correctness and overclaim

### R5 · The Green–Lindsay stability condition is stated two ways in the same paper — **critical**

Table 15 (p. 85), column "Well-posed when", gives for Green–Lindsay: `τ0 ≥ τ1 ≥ 0`. Table 22 (p. 114), in the row for Eq. (39), gives the basis of the primary-source check as: "no τ0 term on the strain-rate coupling; `τ1 ≥ τ0 > 0`".

The two orderings are opposite, and one of them is wrong. This is not a pedantic catch: Table 15 is the comparative table a reader will use to choose a model, and the GL ordering is the condition under which the theory is stable. The manuscript's own evidence protocol (Section 2.4, item 2) promises that every registered equation carries a status from a fixed vocabulary; it does not promise that the two tables agree, but a referee will notice.

*Required action.* Settle the ordering against Green & Lindsay (1972) and make Tables 15, 22 and the text of Section 4.2.2 agree. If the sign of the inequality depends on which coefficient is called τ0 (GL's own τ0/τ1 versus the later literature's), say so in one sentence in Section 4.2.2 and use one convention in both tables.

### R6 · The equation-verification register describes another manuscript — **critical**

Appendix J is presented (Section 2.4, item 1) as the register that "records which is which" — which statements are derived here and which are attributed. The register itself is Table 22, 11 rows, and each row is good. But Table 23, "Coverage inventory of the equation register" (p. 115), then states:

* "all 136 printed equations of the source manuscript in printed order";
* "Of 136 printed equations, 11 carry a status and 125 do not";
* and its caption: "Section titles, equation numbers (e.g. eq:3.1) and labels refer to the source manuscript from which this material is merged, not to the equations of this paper."

This paper prints **90** equations (the highest number in the body is (90), p. 112). Its section titles do not include "Foundations of Continuum Wave Mechanics". A LaTeX label `eq:3.1` is printed as text. Whatever the internal history, the effect on a referee is that the evidence appendix refers to a document the referee does not have, and the coverage statistic — the one number in the paper that tells a reader how much of it is checked — is about something else.

*Required action.* Rebuild Table 23 against the 90 equations of this paper: one row per printed equation, with its number in this paper and its status. If 11 of 90 carry primary status, say so plainly — that is a defensible statement about a review of this size, and it is exactly the kind of honesty the rest of the manuscript practises. Delete the reference to merging and to any source manuscript, and make sure no LaTeX label survives into print.

### R7 · The manuscript contains an order-of-magnitude slip in a worked estimate, next to a threshold it does not compare with — **major**

Section 6.9.3 (p. 60) argues that the parabolic (Lifshitz–Roukes) result suffices for flexural damping, with the numbers "τ_q ∼ 10⁻¹² s, h ∼ 100 nm and α ∼ 10⁻⁴ m²/s", concluding that "the product ωτ_q at the Zener peak is of order 10⁻²".

Using the paper's own relaxation time, τ_Z = h²/(π²α) (stated on p. 24), the Zener peak sits at ω = π²α/h², so

  ω τ_q = π² α τ_q / h² = 9.87 × 10⁻⁴ × 10⁻¹² / 10⁻¹⁴ ≈ 0.099 ≈ 10⁻¹.

The stated order of magnitude is a factor of ten low. The difference matters because Section 4.4.4 (p. 35) sets ωτ_q ≲ 0.3 as the range in which a truncated lag law may be trusted as an approximation of the delay law: at 0.1 the parabolic result is within a factor 3 of the paper's own validity boundary, not two orders of magnitude below it. Either the lag time intended was 10⁻¹³ s (which gives 10⁻²) or the stated order is wrong.

*Required action.* Recompute the number and state it with the intermediate values, then compare the result explicitly with the 0.3 threshold of Section 4.4.4 — for example "ωτ_q ≈ 0.1 at the peak, still below the 0.3 limit, but only by a factor 3". The conclusion survives; the arithmetic and the missing comparison do not.

### R8 · The Kramers–Kronig sum rule is stated twice, with two different right-hand sides — **minor**

Eq. (20) on p. 16 reads

  ∫₀^∞ Q⁻¹ d ln ω = π (v₀ − v∞)/v̄ ,

and the same relation reappears as Eq. (29) on p. 21 with c₀, c∞, c̄. Duplication is harmless in itself, but the two statements are not identical and neither matches the printed check:

* p. 16 says "For the Debye form Q⁻¹ = εx/(1+x²) the left side is πε/2 and the right side is π(√(1+ε) − 1) ≈ πε/2". At ε = 0.01, π(√1.01 − 1) = 1.5668 × 10⁻², while the value printed in the same sentence as the right-hand side is 1.562991 × 10⁻².
* π(v₀ − v∞)/v̄ with v₀ = c₁√(1+ε), v∞ = c₁ gives 1.5630 × 10⁻² at ε = 0.01, which matches the printed value.

So the numbers in the text come from Eq. (20) with the /v̄ normalisation, while the sentence describes the un-normalised form. The reader who checks the sentence reproduces neither number.

*Required action.* Keep one relation (in Section 3.3.4), and in the Debye check write the formula that the numbers actually come from. Eq. (29) can be deleted or made a forward reference.

### R9 · Eight figures are adapted from copyrighted sources and the submission needs the permissions — **major**

The captions "Geometry after [1]" (Figs. 4 and 6, from Biot 1956, *J. Appl. Phys.*), "after [32]" (Fig. 9, Lord & Shulman 1967, *J. Appl. Phys.*), "after [15, 186]" (Fig. 18), "after [87]" (Fig. 19), "after [288]" (Fig. 25), "after [22]" (Fig. 29, Nowacki's monograph) and "after [12, 78]" (Fig. 34), and "after [35]" (Fig. 36) mark eight figures as derived from published figures. ASME requires written permission for any figure reproduced or adapted from a copyrighted source, and the permission is normally collected before the files are sent, not after acceptance. Fig. 41 (p. 125) shows that the author can draw schematics from scratch — its caption says so explicitly.

*Required action.* Either obtain the permissions (AIP, Elsevier, Springer as appropriate) and note them in the cover letter, or redraw the eight figures from the equations and change the captions from "after [x]" to "redrawn after the formulation of [x]". The second route is cheaper and removes the dependency.

### R10 · Several listed subjects are surveyed "at the level of structure", not treated — **minor**

The abstract lists "piezoelectric, magneto-thermoelastic, diffusive and microstructural couplings" among the subjects "treated in turn". Section 7.1 (p. 66) is explicit that only the piezoelectric coupling is treated in detail: "the other couplings are then surveyed at the level of structure". The magneto-thermoelastic, diffusive, porous and micropolar couplings appear as rows of Table 11 (p. 70) and Table 14 (p. 85) and as prose. The manuscript is right; the abstract is one notch stronger than the manuscript.

*Required action.* Qualify the abstract list, or add one computed result for one of the surveyed couplings.

### R11 · Self-citation is handled better than most papers, but the proportion is not declared — **minor**

38 of the 414 references (9.2%) are co-authored by the author. Appendix K handles this in the honest way — Table 24 is headed "Wave problems from groups other than the author's" and Table 25 "Studies from the author's group ... (not independent evidence)" — and Section 2.4's sixth rule forbids personal characterisation of errors, which the manuscript obeys. What is missing is the number itself, stated once, in the front matter.

*Required action.* One sentence in Section 2.4: the proportion, the reason those works are cited (they are part of the literature being reviewed), and the pointer to Tables 24–25 as the separation of evidence from non-evidence. The cover letter should repeat it.

### R12 · The abstract's list of models that "arise as parameter choices" does not match Table 4 — **major**

See the claim-by-claim table (`abstract_claims.csv`, claim C3). Table 4 (p. 14) has eight rows: classical, Lord–Shulman, DPL first order, GN-II, GN-III, TPL, MGT. Green–Lindsay is not a member of Eq. (14) — Section 3.2.3 says correctly that its temperature-rate terms live in the stress and entropy relations, with the heat flux kept in Fourier form — and the fractional and memory-dependent laws replace s by non-integer powers or kernels, so they cannot be parameter choices of (14) either. The abstract's formulation ("arise, or fail to arise, as parameter choices") is technically defensible, but it lists nine named families in a sentence whose table contains seven, and a reader will take the list as a promise about the table.

*Required action.* Either add a final column to Table 4 marking "not a member — see Section x" for GL, fractional and MDD, or reword the abstract.

---

## 4. Length, structure and the supplementary-material decision

The full plan, with page counts per appendix and the consequences of each move, is in `supplement_plan.md`. Summary of the recommendation:

**Current shape.** Body 94 pp (Sections 1–11); Appendices A–L 32 pp (p. 95–126); references 28 pp (p. 127–154); three misplaced tables 3 pp (p. 155–157).

**Immediate moves that cost nothing.**

| Move | Pages saved | Comment |
|---|---|---|
| Tables 19–21 from p. 155–157 into Appendices D, H and I | 3 | they are today printed after the last reference, under the running head "References" |
| Appendix J (equation register) to supplementary | 8 | it is a machine-readable artefact, not a narrative |
| Appendix E (classified catalogue) to supplementary **with a 1-page key-works summary kept in the main text** | 12 | 70 of the 414 references are cited only here; see the warning below |
| Appendix K, Tables 24–25 to supplementary | 3 | the evidence separation is stated in Section 2.4 instead |

**Total after the moves: about 118 pages.** That is still long for AMR. A second, harder decision is needed, and the manuscript should propose it rather than leave it to the editor:

* Section 3.1 (history, p. 7–10, 4 pp) can be cut to 2 pp without losing any citation, by turning the prose into the timeline of Fig. 3 plus a paragraph;
* Section 5.1–5.2 (fractional and memory models, p. 35–39, 5 pp) can move to supplementary with the key formulas kept in the main text (Eq. (49) and the two model families);
* Section 9.1 (applications by field, p. 78–80, 3 pp) can move in its entirety; Section 9.2's regime map (Fig. 37) is the part a reader needs;
* Section 10.2 (taxonomy, p. 86–89, 4 pp) can be compressed to the two tables (16 and 17) and one page of text.

Those four moves take the paper to about **100 pages**, which is a length AMR can print for a review with 400 references.

**The hidden cost of moving Appendix E.** 72 of the 414 references (17.4%) are cited only in the appendices — 66 only in the catalogue of Appendix E, 5 only in Appendix K, 1 only in Appendix F–I — and a further 3 only in the misplaced Tables 19–21, so 75 in all never appear in the body. If E moves as it stands, the reference list loses 66 anchors from the main text, the numbering compacts, and the main text is no longer self-contained. This has to be handled deliberately: keep a condensed key-works paragraph in Section 2.5 or 3.1 that cites the 20–30 works a reader of the main text actually needs, and let the catalogue carry the rest. This should be decided before the numbering is frozen.

---

## 5. Figures and tables

The item-by-item list is in `figure_table_list.csv` (41 figures, 25 tables; number, printed page, section, caption opening, source or script, units, measured lettering height, finding, severity, action). What follows is the summary a referee would write.

### R13 · Figure lettering is below print size on 26 of the 41 figures — **major**

Measured from the PDF content streams: body text is set at 10.9 pt, table body at 8.0 pt, and **26 pages carry text below 6 pt**; the 24 figure pages among them hold 26 of the 41 figures, since pp. 56 and 61 carry two each. The minima, page by page: 4.2 pt on p. 37 (Fig. 13), p. 40 (Fig. 15) and p. 50 (Fig. 21); 4.5 pt on p. 20 (Fig. 5) and p. 32 (Fig. 11); 4.9 pt on pp. 25, 31, 34, 51, 54, 61 and 67 (Figs. 8, 10, 12, 22, 24, 30, 33); 5.2 pt on p. 125 (Fig. 41); and 5.6 pt on eleven further pages (Figs. 7, 14, 16, 17, 25 and 26, 27, 28, 31, 32, 38, 39). Two table pages sit exactly at 6.0 pt (Table 13 on p. 80, Table 20 on p. 156), so they are at the limit rather than inside it. ASME's production rule is that lettering must remain legible after reduction; in practice nothing below about 6–7 pt survives. The four-panel figures (7, 10, 11, 12, 13, 15, 38) are the worst affected.

*Required action.* Regenerate every figure at a final width of the AMR text block with a minimum lettering size of 7 pt, or split the four-panel figures into two two-panel figures. The scripts exist, so this is a parameter change and a rerun, not new work.

### R14 · Tables 19–21 are printed after the reference list — **critical**

Table 19 (scripts and what they verify) is on p. 155, Table 20 (parameters for the computed figures) on p. 156 and Table 21 (benchmark registry) on p. 157. All three are printed *after* reference [414] on p. 154 and carry the running head "References". Their callouts are in Appendix D (p. 96–97) and Appendix I (p. 113) — 42 to 58 pages earlier. The benchmark registry is cited again in the text of Appendix I ("Table 21 lists the fourteen benchmarks run by `run_checks.py`", p. 113) while the table sits 44 pages later.

*Required action.* Move each table into the appendix that cites it. This is a one-line placement fix per table and it removes the single most visible sign that the document was not read in final form.

### R15 · Two cross-references in figure captions are wrong — **minor**

* Fig. 40 (p. 87), the decision sequence, ends: "The threshold ωτ ≪ 0.05 follows from the regime map of Figure 39." The regime map is **Figure 37** (p. 79). Figure 39 (p. 84) is the two-panel Lord–Shulman-versus-classical difference plot.
* Fig. 39 (p. 84) marks "the dotted red line is ωτ₀ = 1" and then says "Near τ₀ω\* ≈ 1 the thermal and elastic speeds coincide". These are different loci: the red line is the diagonal ωτ₀ = 1, while c_T = c₁ requires τ₀ = 1/ω\*, a horizontal line at τ₀ω\* = 1 that is not drawn. The hybridisation the caption describes happens at the crossing of the two, near (ω/ω\*, τ₀ω\*) = (1, 1).

*Required action.* Correct the first; for the second, draw and label both lines, or say "at τ₀ω\* ≈ 1 and ω ≈ ω\*".

### R16 · Table 4 mixes dimensional and dimensionless entries without saying so — **minor**

Table 4 (p. 14) lists k, k\*, τ_q, τ_T, τ_v for eight theories. The parameters are not commensurable — k is a conductivity, k\* a conductivity per unit time, the τ's are times — and the table shows bare symbols with no units row and no normalisation. Since the table is the pivot of the review (Eq. (14) is the template), one row of units, or a sentence saying that each entry is in the units of its own model, would prevent the misreading that the numbers are meant to be comparable.

### R17 · Units are stated, parameters are stated, and the schematics are labelled — **no action, recorded as a strength**

Every computed figure states its normalisation in the caption (dimensionless axes, ε, τω\*, ν, h), Tables 3, 13 and 20 state the physical inputs at 300 K, and the nine schematic figures are labelled as drawn for this review or adapted from a named source. Of the 41 figures, 36 display computed results and all 36 are traceable to a named script — 4 in the caption or the surrounding text (`fig_refyears.py`, `fig_stability.py`, `fig_lag_truncation.py`, `fig_flexTED.py`), the other 32 through Table 20; the remaining 5 are schematics. The only gap is that Table 20, which carries most of the mapping, is printed in the wrong place (R14).

---

## 6. The abstract, claim by claim

The sentence-by-sentence table is `abstract_claims.csv`: 12 claims, 8 supported by the body, 4 partly supported, none unsupported. The four partial cases are R4 (the "widely repeated" attribution), R12 (nine model families in the abstract, seven rows in Table 4), R10 (the couplings that are surveyed rather than treated) and claim C12 ("all quantitative figures are generated by accompanying scripts", which is true but whose supporting tables are printed after the references). Two further observations on the abstract as a whole:

* It is 247 words — inside the 250-word ceiling the manuscript set for itself, but long for a review abstract, and worth checking against the journal's current guidance before submission. The two sentences that carry the manuscript's novelty — the template sentence and the truncation sentence — are buried in the middle; moving them first would cost nothing.
* The sentence "Damping in flexure is validated against exact solutions" uses "validated" for a comparison with an exact solution of the same continuum model, not with measurement; the declarations state that no experiment was performed. "Checked against" would be exact.

---

## 7. Minor corrections

| # | Page | Finding | Severity |
|---|---|---|---|
| M1 | p. 4 | "**Table Table 1** collects the contributions" — duplicated word in the sentence that introduces the paper's contribution table. | minor |
| M2 | p. 3 | "**The authors' aim** is that a reader…" — first person plural in body prose. The rest of the manuscript is impersonal; this is the only such remnant found in Sections 1–11. | minor |
| M3 | p. 154 ([22]) vs p. 126 ([12]) | Ref. [22] gives "Nowacki, **Z.**, 1975, *Thermoelasticity*, Pergamon Press"; ref. [12] gives "Nowacki, **W.**". The same author appears under two initials. Verify the initial and, for the monograph, the edition (the second edition is 1986). | minor |
| M4 | p. 113 | The running head of the page reads "J Per-equation verification register" while the page opens the last part of Appendix I and its Table 21. | minor |
| M5 | p. 16 and p. 21 | Eq. (20) and Eq. (29) are the same Kramers–Kronig sum rule, in two notations; see R8. | minor |
| M6 | p. 30–31 | "the high-wavenumber growth rate saturates, at τ_q Re s = 0.571 for τ_T/τ_q = 0.3" — the digits are given to three places for a number read off a saturation plateau; two would be honest. Not an error, a precision-claims point. | minor |
| M7 | p. 85, Table 15, row GN-III | "no (strict)" in the finite-front column is well chosen; the same qualifier is missing in the row "DPL, 1st order", where the column reads "no (strict)" but the well-posedness column reads "no instability found (numerical, not a proof)". The two parenthetical styles in one row are hard to read. Editorial only. | minor |
| M8 | p. 89–91 | Section 11.1 and Table 17 state the research agenda twice: the table restates the gaps discussed in the prose, and the prose refers forward to the table. One of the two can go. | minor |
| M9 | p. 127 ([10]) | Ref. [10], Ignaczak & Ostoja-Starzewski, is dated 2010. The publisher's record (Crossref, DOI 10.1093/acprof:oso/9780199541645.001.0001, ISBN 9780199541645) gives a print date of 24 September 2009; both years are in use in the literature. Either is defensible, but the convention should match the one used for the other books in the list, and the DOI would be worth adding if the journal wants one for a monograph. | minor |

---

## 8. Literature a thermoelasticity referee will expect, and does not find here

Two suggestions, both verified against Crossref on 2 November 2026, and one older item that carries no DOI and is flagged accordingly. These are offered as additions, not as a claim that the coverage is inadequate — the reference list is genuinely strong (Chadwick 1960, Chadwick & Sneddon 1958, Nowacki, Achenbach, Coleman, the full Ignaczak sequence, Quintanilla & Racke, Jou–Casas-Vázquez–Lebon, the 2019 graphite second-sound measurement, the whole fractional school).

**(1) VERIFIED.** Chen, G., 2001, "Ballistic-Diffusive Heat-Conduction Equations," *Physical Review Letters*, **86**, pp. 2297–2300, DOI 10.1103/PhysRevLett.86.2297.
*Why expected.* The review's flexure and Lamb-wave summaries (p. 59–60) say that below about 10 nm, or when ballistic transport matters, "kinetic/GK is the appropriate refinement" — Guyer–Krumhansl is offered as the only route. Chen's ballistic-diffusive equations are the standard two-channel alternative for exactly that regime, and the review has no citation to it. One sentence and one reference would close the gap; a comparison of the two routes would be a small addition with real value.

**(2) VERIFIED.** Dreyer, W., and Struchtrup, H., 1993, "Heat pulse experiments revisited," *Continuum Mechanics and Thermodynamics*, **5**, pp. 3–50, DOI 10.1007/BF01135371.
*Why expected.* The manuscript is careful about what the heat-pulse experiments do and do not show (Section 6.4, Fig. 22; Section 9.3), and this is the paper that re-analysed those experiments and set the terms of the subsequent debate. A review that discusses hyperbolic heat conduction and pulse experiments without it will be asked for it.

**(3) UNVERIFIED (no DOI exists; not checked against a database here).** Peshkov, P. L., 1944, "Second sound in helium II," *Journal of Physics (USSR)*, **8**, p. 381.
*Why mentioned.* Section 3.1 (p. 8) introduces second sound through its observation "in solid helium and in sodium fluoride" and cites [27, 28] — both correct. Second sound was first observed in superfluid helium, and the historical paragraph begins with Cattaneo and Vernotte; one clause would complete the arc. Marked UNVERIFIED because the 1944 record has no DOI and was not retrievable in the environment used for this report; the author should verify the volume and page before adding it, or omit it.

---

## 9. What should not be changed

A referee's report that lists only faults is a poor instrument. The following are the parts of this manuscript that make it worth reviewing, and they should survive revision intact.

* **Table 6 (p. 29), page-level provenance.** Naming the printed page and equation of the primary text for each attribution, and stating what the check does *not* cover, is the single best thing in the paper. It is also unusual: most reviews give no way to discount their own claims.
* **Table 10 (p. 66), computed baseline against printed values.** Recomputing values that the original papers tabulate, and printing the comparison, is the kind of check that makes a review citable.
* **Section 4.3.1 and Fig. 10.** The three-truncation analysis is a genuine contribution, correctly attributed to [43], [10,158] and [159], and it is the part of the paper most likely to be cited.
* **Section 4.4.3, the sign change of attenuation in the exact delay law at ωτ_q = π/2.** A neat, checkable observation with a correct root (`k_w = √(ρcω/k) e^{i(π/4 − ωτ_q/2)}`), and the honest note that the truncations avoid the behaviour only because they discard the high-frequency part of the delay.
* **The pitfalls checklist (Section 10.1.4, 17 items, p. 86).** This is what a reader will photograph second, after Table 4.
* **Section 2.4's protocol and the Declarations.** Funding, competing interests, code availability and a specific, non-generic statement of generative-tool use, including the admission that not every cited work was read page by page. This is exactly the standard AMR should want.

---

## 10. Findings by severity

| Severity | Items |
|---|---|
| critical (3) | R5 Green–Lindsay ordering contradicts itself between Tables 15 and 22 · R6 Appendix J/Table 23 describe another manuscript (136 equations, source-manuscript labels) · R14 Tables 19–21 printed after the reference list |
| major (8) | R1 review-versus-research split not stated · R2 differentiation from [6]–[10], [158] is one sentence · R3 no search protocol and an explicit disclaimer of exhaustive coverage · R4 "widely repeated" unattributed · R7 order-of-magnitude slip in the flexure estimate · R9 eight adapted figures without permissions · R12 abstract lists nine families, Table 4 has seven · R13 figure lettering down to 4.2 pt on 26 figures |
| minor (14) | R8 duplicated sum rule with two right-hand sides · R10 couplings surveyed rather than treated · R11 self-citation proportion not declared · R15 two caption cross-reference errors · R16 Table 4 units · M1–M9 |

Count: 3 critical, 8 major, 14 minor. Nothing in the report is a finding about a claim being false; every finding is about a claim being either under-supported or about the document not showing what it already knows.

---

*This report is a drafting aid for the author. Every page number, equation number, quotation and count it cites was checked against the compiled 157-page PDF, and the two Crossref records in Section 8 were retrieved on 2 November 2026. The limits of the read are stated in Section 0; where a finding rests on a page, that page was read.*
