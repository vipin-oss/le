# Restructure plan — from 39 flat sections to the AMR pattern, with nothing deleted

Target: *Applied Mechanics Reviews* (ASME), reviews of open length, no page charges, format as other ASME
journals. Baseline analysed from three AMR articles read in full (1986, 22 pp; 1998, 25 pp; 2014, 38 pp) —
see `report.md` §1–§4.

Current state, measured from the compiled PDF of the 173-page build: **39 numbered sections**, 10
appendices, 40 figures, 26 tables, 90 numbered equations, 414 references, 329-word abstract, 11 keywords,
a nomenclature block, a contents page, a highlights box and a graphical abstract.

The proposal keeps **every page and every result**. What changes is the number of top-level sections
(39 → 10), where the history sits, where the tables live, and the front and back matter.

---

## 1. Target outline (10 numbered sections, AMR-style)

| New | Title | Built from | Old sections | Pages |
|---|---|---|---|---|
| **1** | Introduction and scope | merge | 1, 2 | 11–18 |
| 1.1 | The problem that generalized thermoelasticity addresses | keep | 1.1 | 11 |
| 1.2 | Historical development of the theories reviewed | **move up, demote** | 2 | 16–18 |
| 1.3 | Why another review, and what this one adds | merge + absorbs the Highlights bullets | 1.2, 1.3 | 11–12 |
| 1.4 | Scope, conventions, and the template at a glance | merge; the graphical abstract becomes **Fig. 1** here | 1.4 + front-matter figure | 12 |
| 1.5 | Evidence protocol and reproducibility | merge | 1.5, 1.6 | 13–15 |
| **2** | Foundations: balance laws, the heat-flux template and admissible laws | merge | 3, 4, 5, 12 | 19–28, 47 |
| 2.1 | Balance laws for small disturbances; linear thermoelasticity | keep | 3.1, 3.2 | 19 |
| 2.2 | Beyond Fourier's law: the heat-flux template | keep | 3.3, 3.4 | 20–22 |
| 2.3 | Energy balance and energy flux | keep | 3.5 | 23 |
| 2.4 | Fourier–Laplace conventions, branches, damping and the sum rule | merge | 4.1–4.4 | 24–25 |
| 2.5 | Causality, finite signal speed and admissibility of a heat law | merge | 4.5–4.7 | 25–26 |
| 2.6 | Kinetic origin of the Cattaneo and Guyer–Krumhansl laws | keep | 5 | 27–28 |
| 2.7 | Effective modulus, causality and Kramers–Kronig relations | **move** (from §12 to foundations) | 12 | 47 |
| **3** | The theories as parameter choices of one template | merge | 6, 7, 8, 9 | 29–42 |
| 3.1 | Classical coupled thermoelasticity and its failure at short times | keep | 6 | 29–32 |
| 3.2 | Lord–Shulman, Green–Lindsay and the Green–Naghdi types I–III | keep | 7 | 33–37 |
| 3.3 | Dual-phase-lag, three-phase-lag and Moore–Gibson–Thompson | keep | 8 | 38–41 |
| 3.4 | How faithful is a Taylor truncation? | keep | 9 | 42 |
| **4** | Beyond rational heat laws: fractional, memory, size and further classes | merge | 10, 11, 24, 25 | 43–47, 70–76 |
| 4.1 | Fractional and memory-dependent models | merge | 10, 11 | 43–46 |
| 4.2 | Nonlocal and gradient models of size dependence | keep | 24 | 70–73 |
| 4.3 | Wider material classes: where the template reaches and where it stops | keep | 25 | 74–76 |
| **5** | Waves in unbounded and bounded media | merge | 13–23 | 48–69 |
| 5.1 | Plane waves in three dimensions | keep | 13 | 48–49 |
| 5.2 | Anisotropy: thermal coupling of quasi-longitudinal waves | keep | 14 | 50–51 |
| 5.3 | Reflection at a thermoelastic free surface | keep | 15 | 52 |
| 5.4 | Transient problems: heat pulses and thermal shock | keep | 16 | 53–55 |
| 5.5 | Resonance in finite bodies: rods and clamped bars | **merge two sections** | 17, 20 | 56, 61–62 |
| 5.6 | Thermoelastic Rayleigh waves | keep | 18 | 57–58 |
| 5.7 | Thermoelastic Lamb waves in a plate | keep | 19 | 59–60 |
| 5.8 | Thermoelastic damping in flexure: Zener and the exact Fourier solution | keep | 21 | 63 |
| 5.9 | Interfaces, reflection and energy partition | keep | 22 | 64–67 |
| 5.10 | Layered media: Love, Stoneley and Scholte waves | keep | 23 | 68–69 |
| **6** | Coupling to further fields | merge | 26, 27 | 77–81 |
| 6.1 | Piezo-thermoelastic coupling and exact renormalisation | keep | 26.1, 26.2 | 77–79 |
| 6.2 | Magneto-thermoelasticity, diffusion and microstructure | keep | 26.3–26.5 | 79–80 |
| 6.3 | Piezoelectric shear-horizontal surface waves | keep | 27 | 80–81 |
| **7** | Methods, benchmarks and worked examples | merge | 28, 29, 32 | 82–85, 90 |
| 7.1 | Analytical methods and numerical inversion | keep | 28.1, 28.2 | 82–83 |
| 7.2 | Time-domain numerics and a verification discipline | keep | 28.3, 28.4 | 83–84 |
| 7.3 | A finite-difference benchmark for hyperbolic heat conduction | keep | 29 | 84–85 |
| 7.4 | Worked examples: four quantitative checks | keep | 32 | 90 |
| **8** | Applications and the evidence base | merge | 30, 31, 33 | 86–93 |
| 8.1 | Applications by field | keep | 30 | 86–87 |
| 8.2 | A quantitative guide to application regimes | keep | 31 | 88–89 |
| 8.3 | Experimental evidence and parameter identification | keep | 33 | 91–93 |
| **9** | Synthesis: comparability, pitfalls and the summary table | merge | 34, 37 (+ four summary tables) | 94–96, 104–105 |
| 9.1 | **Table 1: the single comprehensive summary table** | new assembly of 8.6, 26.6, 31, 34.3 | — | — |
| 9.2 | When does the heat law matter? A regime map | keep | 34.1 | 94 |
| 9.3 | Taxonomy of the field, and when two studies are comparable | merge | 34.2, 37 | 94, 104–105 |
| 9.4 | Pitfalls checklist | keep | 34.4 | 95–96 |
| 9.5 | Decision guide | keep | 34.5 | 96 |
| **10** | Conclusions and outlook | merge | 39, 38 | 106–109 |
| 10.1 | Conclusions | keep | 39 | 109 |
| 10.2 | Open problems and research agenda | keep | 38 | 106–108 |
| 10.3 | Outlook | **new one-paragraph close**, assembled from the forward-looking sentences already in §38 and in the abstract | — | — |

Everything that does not appear above as a body section is in the appendix table below. **Nothing is
removed**: the six sections that disappear as top-level sections (2, 11, 12, 20, 37, 39) live on as
subsections, and the two that leave the body (35, 36) become appendices K and L.

## 2. Appendices (12, was ten plus the nomenclature)

| New | Title | Was | Pages |
|---|---|---|---|
| A | Derivations of the balance laws | App. A | 110 |
| B | Derivation and verification of the dispersion polynomial | App. B | 111 |
| C | Characteristic numbers and parameter estimates | App. C | 111–112 |
| D | Reproducibility: scripts and what each one verifies | App. D | 112 |
| E | Classified catalogue of the cited literature | App. E | 112–126 |
| **F** | **Nomenclature, glossary and summary of working formulas** | front-matter Nomenclature **+** App. F | 10 + 126–127 |
| G | Derivation of the weak-coupling relaxation form | App. G | 127–128 |
| H | Parameter register for the figures | App. H | 128 |
| I | Benchmark registry | App. I | 128–129 |
| J | Per-equation verification register | App. J | 129–140 |
| **K** | **Atlas of problems in the literature** | was §35 (body) | 97–100 |
| **L** | **Reporting standards for new work** | was §36 (body) | 101–103 |

Appendices K and L are the only two sections that leave the body. Both are catalogues/checklists, i.e.
exactly what AMR readers expect to find as supplementary material; neither contains a result of the
review, and both keep their page numbers in the total.

## 3. Where AMR expects the three things the brief asks about

**A single comprehensive summary table.** AMR's own reviews print **at most two tables** (1986: two data
tables; 1998 and 2014: none). We currently print 26. The plan therefore:

* builds **one master table, "Table 1"**, at the head of §9, with one row per model family and the columns
  *template / governing equation / stability or well-posedness condition / validity range / section of
  this review*;
* assembles it from four tables that already exist — the summary of template models (old 8.6), the table
  of couplings (old 26.6), the regime guide (old 31) and the comparative table (old 34.3) — so its content
  is not new claims but consolidated claims;
* keeps the four source tables, either where they stand or gathered into Appendix K, so no data is lost;
* treats the remaining ~21 tables as data tables (they are: parameter registers, benchmark results,
  numeric comparisons) and leaves them where their sections need them.

**An outlook section.** AMR ends with "CONCLUDING REMARKS" (1986 p. 372, 1998 p. 723) or "6 Outlook"
(2014 p. 040802-30). Our §38 (open problems) and §39 (conclusions) currently end the paper — the right
material in the wrong shape. Merge them into **§10 "Conclusions and outlook"**: 10.1 conclusions, 10.2
open problems, 10.3 a short forward-looking close. The acknowledgements, CRediT and declarations then
follow, and the references last — which is already AMR's order.

**A notation list.** None of the three AMR articles has a nomenclature block, and ours sits on p. 10
between the abstract and §1. Two options, in order of preference:

1. **Merge it into Appendix F**, which already holds the glossary and the working formulas — one symbol
   table in one place, front matter shortened by ~2 pages, nothing lost (recommended).
2. Keep it immediately after the abstract if the Editor's checklist for AMR asks for a nomenclature; it is
   then in the position ASME's other journals use.

## 4. Renames (title register)

| Old title | New title | Why |
|---|---|---|
| Historical development of the theories reviewed | **1.2 Historical development of the theories reviewed** | becomes a subsection of §1, as in AMR 2014 §1.1 |
| Mathematical preliminaries | **2.4 Fourier–Laplace conventions, branches and damping** | names the content instead of the genre |
| Fidelity of Taylor-truncated lag models | **3.4 How faithful is a Taylor truncation?** | AMR style: a question the section answers |
| Coupled fractional dispersion | **4.1 Fractional and memory-dependent models** (absorbed) | one page; it belongs inside its parent |
| Effective modulus, causality and Kramers–Kronig relations | **2.7 Effective modulus, causality and Kramers–Kronig relations** | moves to foundations |
| Anisotropy: thermal coupling of quasi-longitudinal waves in cubic crystals | **5.2 Anisotropy: thermal coupling of quasi-longitudinal waves in cubic crystals** | unchanged text, demoted |
| Thermal-wave resonance in a finite rod + Resonant modes of a clamped bar | **5.5 Resonance in finite bodies: rods and clamped bars** | same physics, one section |
| A taxonomy of the field, and when two studies are comparable | **9.3 Taxonomy of the field, and when two studies are comparable** | demoted into the synthesis |
| Atlas of problems in the literature | **Appendix K. Atlas of problems in the literature** | catalogue |
| Reporting standards for new work | **Appendix L. Reporting standards for new work** | checklist |
| Open problems and research agenda | **10.2 Open problems and research agenda** | joined to the conclusions |
| Conclusions | **10.1 Conclusions** | joined to the outlook |

Headings also change case: AMR's 2014 template uses **title case with no period after the number**
("3 Computational Analysis Techniques"), the 1980s–90s template used capitals with a period ("1.
INTRODUCTION"). Follow 2014.

## 5. Front matter (all content kept, nothing left dangling)

| Item | Now | Plan |
|---|---|---|
| Title | main title + a 12-word subtitle | keep the main title; move "A unified review with verified reductions, dispersion analysis and benchmark problems" into the abstract |
| Author block | name, institution, e-mail, date | ASME block: name, "Mem. ASME" if applicable, affiliation, e-mail; drop the `\today` date |
| Highlights box | 5 bullets on p. 1 | convert into a bulleted list at the start of **§1.3** (content untouched, box and colour removed) |
| Graphical abstract | Figure 1 on p. 2 | becomes **Fig. 1** of §1.4, captioned as the road map |
| Contents page | p. 2 | not printed in the journal PDF (it is a build product, not content) |
| Abstract | 329 words | cut to ≤250; the surplus sentences move into §1.3 |
| Keywords | 11, in the PDF | keep in the submission metadata only |
| Nomenclature | p. 10 | Appendix F, or after the abstract (§3 above) |

## 6. Mechanical changes the build needs

1. `\section` → ten `\section` calls with `\subsection` beneath; all `\input` lines stay, only their
   nesting changes. `\cref` labels are unchanged, so cross-references survive the merge.
2. The 39 section files keep their names; only `main.tex` changes. That keeps the diff reviewable and
   makes a rollback trivial.
3. `\bibliographystyle{unsrtnat}` → `asme2e` (or the `.bst` shipped with the AMR template); journals
   abbreviated across the four bib files; `doi`/`url` dropped from the printed list (see `report.md`
   §6).
4. Captions: `\captionsetup{name=Fig.,labelsep=space}` and no colon; sentence case; keep the long,
   self-contained captions (AMR 2014 median is 34 words); panel labels (a), (b) inside the caption.
5. Equation numbering stays sequential (AMR 2014 uses sequential; our 90 numbers do not move).
6. Tables renumbered from 1 after the new master table is created; the four source tables re-checked for
   duplicate rows once merged.
7. A full rebuild, then a diff of the PDF outline against this plan's target outline before submission.

## 7. Length — say it in the inquiry letter, do not "solve" it by cutting

173 pages against AMR's 22, 25 and 38. AMR has no page limit, so the paper is admissible as it stands;
but the honest framing for the pre-submission inquiry is: *"review of 173 pages including 12 appendices;
appendices A–J (≈31 pages) can move to supplementary material on request."* That sentence gives the
Editor a decision without forcing us to delete anything.

## 8. Risks, and how to keep this reversible

* **Reference churn.** Renumbering 414 references after a `.bst` swap can silently reorder them. Mitigate:
  rebuild, then assert that the first citation is [1] and the last is [414], and that `\nocite` appears
  nowhere.
* **Cross-reference breakage.** Merging sections renumbers "Sec. 12" style prose references. Mitigate:
  every such mention in the 39 section files goes through `\cref`; grep for literal "Sec." before
  rebuilding.
* **Table 1 could become a fifth summary.** Assemble it strictly from existing rows; it must not introduce
  a claim that is not already in 8.6, 26.6, 31 or 34.3.
* **Two dials the author may not want to turn** — the highlights box and the keywords line are the only
  items that leave the *article* (into §1.3 and into the metadata). Both are reversible in one line each.

---

## 9. Machine-readable map (checked by `check_p15.py`)

Old body section number, where it goes in the new build:

```
old=01 -> new=1.0
old=02 -> new=1.2
old=03 -> new=2.1-2.3
old=04 -> new=2.4-2.5
old=05 -> new=2.6
old=06 -> new=3.1
old=07 -> new=3.2
old=08 -> new=3.3
old=09 -> new=3.4
old=10 -> new=4.1
old=11 -> new=4.1
old=12 -> new=2.7
old=13 -> new=5.1
old=14 -> new=5.2
old=15 -> new=5.3
old=16 -> new=5.4
old=17 -> new=5.5
old=18 -> new=5.6
old=19 -> new=5.7
old=20 -> new=5.5
old=21 -> new=5.8
old=22 -> new=5.9
old=23 -> new=5.10
old=24 -> new=4.2
old=25 -> new=4.3
old=26 -> new=6.1-6.2
old=27 -> new=6.3
old=28 -> new=7.1-7.2
old=29 -> new=7.3
old=30 -> new=8.1
old=31 -> new=8.2
old=32 -> new=7.4
old=33 -> new=8.3
old=34 -> new=9.1-9.5
old=35 -> new=Appendix K
old=36 -> new=Appendix L
old=37 -> new=9.3
old=38 -> new=10.2
old=39 -> new=10.1
```

Old appendices:

```
old=App.A -> new=App.A
old=App.B -> new=App.B
old=App.C -> new=App.C
old=App.D -> new=App.D
old=App.E -> new=App.E
old=App.F -> new=App.F
old=App.G -> new=App.G
old=App.H -> new=App.H
old=App.I -> new=App.I
old=App.J -> new=App.J
```

Every number 1–39 appears exactly once above, and every appendix A–J once: no section and no
appendix of the 173-page build is dropped, merged away without a destination, or invented.
