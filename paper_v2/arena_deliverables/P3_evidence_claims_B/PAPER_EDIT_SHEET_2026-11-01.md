# Paper edit sheet - what to change in the manuscript, sentence by sentence

Updated 2026-11-01, step 22. **23 items.** Every item below comes from a verdict file in this folder, not from memory: a sentence is here because a source was read and it did not carry the sentence, or because the bibliography line is provably wrong. The suggested wordings are editorial suggestions - mine, for the author to accept, change or reject; the evidence line under each item is what has to stay true.

**How to read the priority column.** `P1 must change` - a citation in the sentence fails on the very thing the sentence asserts, so the sentence or the citation has to go. `P2 soften or re-cite` - part of the sentence is carried, part is not. `P3 bibliography` - only the reference line changes. `P4 pending` - nothing can be decided until a copy arrives; these need no author decision today.

| priority | items |
|---|---|
| P1 must change | 5 |
| P2 soften or re-cite | 5 |
| P3 bibliography | 9 |
| P4 pending | 4 |

## P1 - the sentence or its citation has to change

These are the items where the manuscript is contradicted by the source, not merely under-cited.

### I001 - CR133 CR134 (A2-b006-D6)

> For DPL and TPL (first-order truncations) an energy functional exists but its construction is more involved than for the other members of the template (Quintanilla 2003; Chirita 2016).

- **What is wrong.** Both citations attached to this sentence fail on the one thing it asserts - that an energy functional exists. Quintanilla (2003) proves exponential stability for tau_y > tau_q/2 and instability below it (abstract, p.713); it does not construct an energy functional. Chirita, D'Apice and Zampoli (2016) treat the three-phase-lag model through fading memory and thermodynamic restrictions and construct no functional either.
- **Do this.** Either attach a paper that actually builds the functional for DPL and TPL, or rewrite the sentence to the claim the two citations do carry (a stability threshold), and drop the functional clause.
- **Suggested wording.** *For DPL and TPL the question that has been settled is stability, not the functional: the one-dimensional dual-phase-lag problem is exponentially stable for tau_y > tau_q/2 and unstable below it (Quintanilla 2003), and the three-phase-lag model is covered by fading-memory arguments (Chirita, D'Apice and Zampoli 2016).*
- **Evidence read.** Register row CR133 read against the Quintanilla abstract (p.713) and p.714; register row CR134 read against the Chirita, D'Apice and Zampoli abstract

### I002 - CR200 (A2-b007-E24)

> The one-dimensional piezoelectric bar in the quasi-electrostatic approximation follows Yang (2018) and Mindlin and Tiersten (1962).

- **What is wrong.** Mindlin and Tiersten (1962) is a couple-stress theory of linear elasticity: no electric field, no piezoelectric coupling, no quasi-electrostatic bar. A full-text search of all 34 pages returns nothing that could carry the sentence. The other half of the sentence (Yang 2018) is held but its chapter has not been read yet.
- **Do this.** Drop Mindlin and Tiersten from this sentence - they belong in the couple-stress discussion, not here - and keep Yang (2018), whose chapter still has to be read.
- **Suggested wording.** *The one-dimensional piezoelectric bar in the quasi-electrostatic approximation follows Yang (2018).*
- **Evidence read.** Mindlin and Tiersten 1962, Arch. Rational Mech. Anal. 11, all 34 pages searched
- **Pending.** CR199 half: Yang (2018) chapter not read yet

### I003 - CR087 CR083 (A2-b002-S1)

> For a law with memory the second law restricts the relaxation function and the entropy flux, not only the signs of the coefficients (Coleman and Gurtin 1967; Chen and Nunziato 1974).

- **What is wrong.** Coleman and Gurtin (1967) treats materials with internal state variables whose evolution obeys ordinary differential equations, and the second law enters as the Clausius-Duhem inequality (3.2) restricting response functions. It does not state that the second law restricts the relaxation function and the entropy flux. The companion citation, Chen and Nunziato (1974), could not be found in two Crossref queries at all.
- **Do this.** Rewrite the sentence to what Coleman and Gurtin actually do (state variables, Clausius-Duhem), or produce the page that states the relaxation-function restriction. For Chen and Nunziato 1974, do a catalogue lookup - no DOI may be printed for it. The Chen and Nunziato 1974 citation itself is item I018.
- **Suggested wording.** *For a law with memory the second law enters through the Clausius-Duhem inequality and restricts the response functions of the material, not only the signs of its coefficients (Coleman and Gurtin 1967).*
- **Evidence read.** Coleman and Gurtin 1967, section on the Clausius-Duhem inequality (3.2); Crossref searched twice for Chen and Nunziato 1974
- **Pending.** Chen and Nunziato 1974 needs a manual catalogue lookup

### I004 - CR062 (A1-b002-A34)

> Further variants (fractional DPL and TPL, with fractional orders on one or both sides of the lag equation) are numerous; reviews and critical discussions of the logic of fractional thermoelasticity are given in [Povstenko2016, Yu2024, Gorenflo1997, Povstenko2004, Povstenko2007, Povstenko2009].

- **What is wrong.** The sentence is about fractional thermoelasticity but one of its two supports, Gorenflo and Mainardi (1997), is a fractional-calculus text: its abstract lists Riemann-Liouville calculus, the Laplace-transform technique, Abel integral equations and relaxation and oscillation equations - nothing on thermoelasticity. The other support, Povstenko (2015), is the right book but the phrase 'three-phase-lag' does not appear in the first 40 pages scanned, so the DPL/TPL grouping is not carried by it either.
- **Do this.** Either cite a fractional-thermoelasticity review that discusses DPL and TPL together, or split the sentence: keep the fractional variants on Povstenko and drop the TPL grouping.
- **Suggested wording.** *Further variants (fractional DPL and TPL, with fractional orders on one or both sides of the lag equation) are numerous; the fractional ones are reviewed by Povstenko (2015).*
- **Evidence read.** Gorenflo and Mainardi 1997 abstract read in full; Povstenko 2015 first 40 pages scanned

### I023 - CR209 CR210 CR177 CR050 (A2-b007-E28)

> Rayleigh-type waves in a nonlocal micropolar thermoelastic half-space containing void pores were computed by Kumar and Tomar (2024); temperature-rate-dependent thermoelasticity with memory-dependent derivative, including energy and uniqueness theorems, was developed by Singh et al. (2020). // Energy ratios have been computed for fluid-piezothermoelastic and fluid-double-porous interfaces (Gupta et al. 2023; Kumar and Sharma 2019; Kumar et al. 2025). // Wang and Li's comparison with the fractional derivative [Wang2021, WangLi2025IV] discusses the relation of the two.

- **What is wrong.** The author declared these four citations unimportant on 2026-11-01, so no evidence will be produced for them - and a sentence cannot rest on a source that will not be shown.
- **Do this.** Remove the four citations and rewrite the two sentences so that nothing depends on them; the works are listed in waived_by_author_2026-11-01.csv with the wording that has to change.
- **Suggested wording.** *(author's call - the sentences have to lose these names, not gain replacements)*
- **Evidence read.** waived_by_author_2026-11-01.csv

## P2 - part of the sentence is not carried

The subject is covered by the source, but one clause or one word is not.

### I005 - CR060 (A1-b002-A34)

> Further variants (fractional DPL and TPL, with fractional orders on one or both sides of the lag equation) are numerous; reviews and critical discussions of the logic of fractional thermoelasticity are given in [Povstenko2016, Yu2024, Gorenflo1997, Povstenko2004, Povstenko2007, Povstenko2009].

- **What is wrong.** Same sentence as I004. The Povstenko monograph does not use 'three-phase-lag' in the pages scanned, so the half of the sentence that puts fractional DPL and TPL under one book is not carried.
- **Do this.** Fold into the I004 edit; nothing separate is needed if I004 is applied.
- **Evidence read.** Povstenko 2015, first 40 pages

### I006 - CR182 CR184 (A2-b007-E15)

> Nonlocal elasticity is written with the Yukawa-type kernel and the equation (1 - xi^2 nabla^2) sigma_ij = C_ijkl eps_kl (Eringen 1972, 1983, 2002).

- **What is wrong.** The word 'Yukawa' appears in none of the three cited works - not in the 1972 paper, not in the 1983 one, not anywhere in the 386 pages of the 2002 book. The equation is real but belongs to the 2002 book: (1 - xi^2 grad^2) sigma = C : epsilon is equation (6.9.12), p.113, with an extra quartic term.
- **Do this.** Drop 'Yukawa-type' or mark it as the authors' own label, and cite the equation to Eringen (2002), eq. (6.9.12), p.113, not to the 1972 paper.
- **Suggested wording.** *Nonlocal elasticity writes the stress-strain relation as (1 - xi^2 nabla^2) sigma_ij = C_ijkl eps_kl (Eringen 2002, eq. (6.9.12)).*
- **Evidence read.** Eringen 1972 (16 pages) and Eringen 2002 (386 pages) searched; equation read at p.113

### I007 - CR172 (A2-b007-E9)

> For anisotropic media the Stroh formalism gives a first-order state-vector system; this is the route taken for piezothermoelastic layers and half-spaces (Biswas 2020).

- **What is wrong.** Biswas (2020), Acta Mechanica, has the geometry but not the Stroh formalism: the word does not occur in the pages read, and the paper's own references credit the Stroh route to Biswas (2018), J. Thermal Stresses.
- **Do this.** Re-cite the sentence to Biswas (2018), or attach the 2020 paper only for the geometry.
- **Suggested wording.** *For anisotropic media the Stroh formalism gives a first-order state-vector system; this is the route taken for piezothermoelastic layers and half-spaces (Biswas 2018).*
- **Evidence read.** Biswas 2020, Acta Mechanica 232 - pages read for the fourth batch

### I008 - CR188 (A2-b007-E18)

> The dispersive-stabilised versions, with a gradient of inertia as well as of strain (Askes and Aifantis 2006, 2011), interpolate between the Eringen and gradient dispersion relations.

- **What is wrong.** The eight pages of Askes and Aifantis supplied contain neither 'inertia' nor 'acceleration', so the 'gradient of inertia as well as of strain' half of the sentence is not carried by the copy in hand. The interpolation claim itself is not contradicted.
- **Do this.** Supply a page (or the 2011 paper rather than the 2006 one) that states the inertia gradient, or soften to 'a gradient of strain, and in later work a gradient of inertia'.
- **Suggested wording.** *The dispersive-stabilised versions, with a gradient of strain and, in the later work, of inertia (Askes and Aifantis 2006, 2011), interpolate between the Eringen and gradient dispersion relations.*
- **Evidence read.** Askes and Aifantis 2006, the eight pages supplied
- **Pending.** a page stating the inertia gradient

### I009 - CR137 (A2-b006-D9)

> Variational formulations and reciprocity theorems for classical thermoelasticity are available (Marotti de Sciarra 2013; Carlson 1972; Nowacki 1975).

- **What is wrong.** Nothing was read in Nowacki. The sentence itself is carried in full by Carlson, the other citation in the same parenthesis, so the Nowacki reference adds no support and cannot be confirmed without the book. The citation also mixes two books: the Pergamon Thermoelasticity is 1962 or 1986, and the 1975 Nowacki book is Dynamic Problems of Thermoelasticity.
- **Do this.** Drop Nowacki 1975 from the citation and keep Carlson (1973); or supply the book if the citation is to be kept.
- **Suggested wording.** *Variational formulations and reciprocity theorems for classical thermoelasticity are available (Marotti de Sciarra 2013; Carlson 1973).*
- **Evidence read.** Carlson, sect. 24 pp. 338-342; sect. 13 p. 319; sect. 21 p. 331

## P3 - bibliography lines only

| item | claims | fix | verified in |
|---|---|---|---|
| I010 | CR136 | Carlson, D. E. (1973), Linear Thermoelasticity, Handbuch der Physik VIa/2, pp. 297-345, DOI 10.1007/978-3-662-39776-3_2. | Crossref chapter record |
| I011 | CR092 | Cattaneo, C. (1948), Sulla conduzione del calore, Atti del Seminario Matematico e Fisico dell'Universita di Modena, 3. | Front page of the 1966 C.I.M.E. course; Tzou 2nd ed. bibliography p.59 for the 1958 note |
| I012 | CR117 | doi:10.1016/j.amc.2020.125934 | Crossref lookup of the recorded DOI and of the corrected one |
| I013 | CR003 CR114 | Quintanilla, R. (2003), A condition on the delay parameters in the one-dimensional dual-phase-lag thermoelastic theory, J. Thermal Stresses 26, 713-721. | Register rows CR003 and CR114 compared; the file is held and was read |
| I014 | CR110 | Chandrasekharaiah, D. S. (1996), A uniqueness theorem in the theory of thermoelasticity without energy dissipation, J. Thermal Stresses 19(3), 267-272, doi:10.1080/01495739608946173. | Crossref, 2026-11-01 (Journal of Thermal Stresses 19, 267-272, 1996) |
| I015 | CR154 | Mitra, K., Kumar, S., Vedevarz, A. and Moallemi, M. K. (1995), Experimental evidence of hyperbolic heat conduction in processed meat, J. Heat Transfer 117, 568-573, doi:10.1115/1.2822615. | Crossref, 2026-11-01 (volume 117, pages 568-573, 1995) |
| I016 | CR126 | Jou, D., Casas-Vazquez, J. and Lebon, G. (2010), Extended Irreversible Thermodynamics, 4th ed., Springer, Dordrecht, doi:10.1007/978-90-481-3074-0. | Crossref book record 10.1007/978-90-481-3074-0, 2010, ISBN 9789048130733/9789048130740 |
| I017 | CR122 | Dell'Oro, F. and Pata, V. (2016), On the Moore-Gibson-Thompson equation and its relation to linear viscoelasticity, Appl. Math. Optim. 76, 641-655, doi:10.1007/s00245-016-9365-1. | Crossref candidate list for Applied Mathematics and Optimization, 2026-11-01 |
| I018 | CR083 | (no wording change - the citation is incomplete, not wrong) | Crossref searched twice, 2026-11-01 |

## P4 - nothing to decide today

- **I019 (CR181).** The 1912 volume is not held and no scan was found; the relation itself is standard but its attribution to Born and von Karman 1912 has not been read anywhere. - *pending:* Born and Huang (1954) - the author is supplying it
- **I020 (CR127 CR152 CR166 CR196).** No readable copy could be found on 2026-11-01 for Muller and Ruggeri, Gurtin and Williams (1966), Li et al. (2019) or Eringen (1974). - *pending:* agent-side search
- **I021 (CR195).** The copy held has no extractable text, so the claim cannot be read. - *pending:* a text-based copy
- **I022 (CR199).** A 309-page copy was opened and its title page read, but the chapter that carries the piezoelectric bar has not been checked. - *pending:* agent-side read

## What this sheet does not do

- It does not edit the manuscript. The `.tex` files are not in this repository and are not to be touched by the agent; the sheet is written so it can be worked through in Overleaf, top to bottom.
- It does not re-open a verdict. Where a claim is `SUPPORTED`, the sentence stays as it is, even if the English could be better.
- It does not print a DOI that has not been resolved. Four DOIs on this sheet were looked up today (CR110, CR126, CR154, CR122 - the last one flagged as probable, not confirmed); the fifth lookup (CR083) failed twice and says so.
