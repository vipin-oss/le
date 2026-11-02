# Cluster synthesis for Table 2 (`tab:streams`, `sections/s02_history.tex`)

Table 2 classifies representative literature into nine *problem types*. Its own caption states the
basis: "selection from the reference list; classification by the titles and stated subjects of the
works". The synthesis below is therefore written at two levels only: (i) the composition of each row,
taken from the table itself, and (ii) what the manuscript body does with those keys, taken from the
`\citep` sentences. **No claim about what an individual paper did is made here unless that paper's
text was read**; content-level entries live in `paper_notes.csv`, and only six keys there are
`FULLTEXT`/`ABSTRACT` sourced (Green1972, Green1993, Quintanilla2003DPL, Huberman2019, Chen2001,
DreyerStruchtrup1993). Everything else in Tier 1 is marked `NOT-READ` with its citation site recorded.

Nine rows, 72 cited keys in total (some keys appear in more than one row: family counts below are
over distinct keys).

---

## 1. Plane waves, stability, dispersion — 4 keys

`Prasad2020`, `Tiwari2021`, `vanDerMerwe2021`, `Sarkar2019`. Four works carry a cluster for which the
review's own machinery (§5, the dispersion equation `eq:unified`, the `tab:compare` table) supplies the
substantive results; none of the four is Tier 1, so no equation or number in the manuscript rests on
them. `Sarkar2019` is used twice: Table 2 and the type-II paragraph of `sections/s05_hyperbolic.tex`
l.57, where nonlocal type II is named as a conservative reference model for dispersion; that sentence
attributes the *combination* (nonlocal elasticity plus type II) to the paper but no result.
`vanDerMerwe2021` is the row's only comparison-based work ("modal comparison of heat laws"), and it is
the one the review's own comparative tables would most naturally benchmark against — yet §5 constructs
its comparison from first principles without reference to it. `Tiwari2021` (nonlocal TPL) and
`Prasad2020` are single-model papers cited once each in Table 2 and in the catalogue only.
The cluster is the thinnest in the table relative to how much of §5 depends on plane-wave analysis:
76 of the 416 cited keys are used in §5, but only these four are offered as representative plane-wave
literature. Same-author concentration is nil (four different first authors, one key each).

## 2. Surface waves — 6 keys

`Biswas2020a`, `Biswas2020` (2 of 6, one group), `Tung2019`, `Gupta2024`, `Aldandani2026`,
`IvanovSavova1991`. The cluster pairs five constitutive-enrichment studies (porous nonlocal
orthotropic; piezothermoelastic layer; nonlocal piezoelastic Rayleigh; nonlocal piezo-semiconductor
Rayleigh; one further entry) with a single energy-flux paper, `IvanovSavova1991`, which is the only
member of the row that touches the topic §6 actually develops — the energy carried by a surface wave.
That asymmetry is visible in the section itself, where §6 derives surface-wave energy flux and
thermoelastic Rayleigh structure from the governing equations and cites the enrichment papers as
prior art rather than as sources of results. All six appear in §3, §6 and the appendix catalogue, so
this is the one cluster whose keys are consistently used in the body and not only catalogued.
`Biswas2020a` and `Biswas2020` are one author group; the remaining four are separate.

## 3. Reflection at free or insulated boundaries — 7 keys

`Das2008`, `Kalkal2020`, `Singh2020b`, `Yadav2023`, `Gupta2024a`, `Singh2020c`, `Jiao2024`. Seven
works, seven essentially distinct physical settings (isothermal/insulated half-space; nonlocal
micropolar with rotation; piezothermoelastic fibre-reinforced; one further Rayleigh/reflection study;
nonlocal piezo-semiconductor; flexoelectric; flexomagnetic). `Singh2020b`, `Singh2020c` and `Gupta2024a`
share the Singh surname stem and `Gupta2024`/`Gupta2024a` are adjacent entries of one author's output,
so the row is roughly four independent groups dressed as seven works. §7 develops reflection
coefficients from the coupled boundary conditions; the seven papers are cited as instances of the
problem class, and Table 2 attaches no equation or numerical reflection coefficient to any of them.
This cluster illustrates the general property of Table 2 that it is a *map of the field*, not a
*provenance table*: it says which problem type a paper belongs to and never what the paper found.

## 4. Interfaces and energy partition — 16 keys

`Barak2023`, `Barak2023IJP`, `Barak2023JTS`, `Barak2023MMMS` (4); `Gupta2023IJNMF`, `Gupta2023Energy`
(2); `Kumar2023PhysScr`, `Kumar2019`, `Kumar2022`, `Kumar2024`, `Kumar2024a`, `Kumar2025`,
`KumarKansal2017`, `Kumar2018` (8); `Fu2013`; `Liu2020`. This is the largest row and the most
concentrated: **14 of 16 keys (87.5 %) come from three author groups** (Kumar 8, Barak 4, Gupta 2),
leaving two independent works (`Fu2013` micropolar imperfect interface, `Liu2020` graded
piezoelectric). The cluster is cited in §3, §6 and §9, and §9 is where the manuscript's own
energy-partition argument sits, so the concentration matters: the review's §9 discussion of net flux
versus mode-by-mode fractions at lossy interfaces is built on a literature in which two surnames
account for three quarters of the entries. The four Barak entries and the two Gupta entries are
same-stem year-variants, which is exactly the pattern the general citation census reports (Gupta 48,
Kumar 41, Barak 29, Das 26, Singh 22 of 416).

## 5. Transient response, rods, bodies — 11 keys

`Singh2019`, `Singh2020a`, `Biswas2019`, `Sur2019`, `Sur2025`, `Bayones2021`, `Li2019`,
`Abouelregal2023`, `Abouelregal2020`, `Abouelregal2020a`, `Lata2020`. Eleven keys, three of them one
author's (`Abouelregal2020`, `Abouelregal2020a`, `Abouelregal2023`) and two pairs from two further
groups. Eight of the eleven are Tier 1 in `paper_notes.csv` because they are cited at points where the
manuscript states a solution or a response — the highest Tier-1 density of any cluster except
fractional models. `Abouelregal2020` and `Abouelregal2020a` are also cited in `sections/s06_lags.tex`
l.37 for the practice of truncating the lag equations to higher order, i.e. as examples of a
procedure the review criticises rather than as evidence for a result. §5 uses seven of these keys and
§4 six, so the cluster spans both the hyperbolic and the transient chapters.

## 6. Damping in resonators — 2 keys

`Yang2021`, `Kumar2017`. **Two works stand behind the entire resonator-damping problem type**, against
16 for interfaces and 11 for transient response, and both are Tier 1. This is the cluster in which the
evidence base is thinnest relative to the weight the manuscript puts on it: §9.3 asserts that
resonator Q data discriminate between heat laws, and the row offers two entries, neither of which is
a measured-Q study of the kind §9.3.3 would need. The bibliographic profile of the field (thermoelastic
damping as a design constraint in MEMS/NEMS resonators) is represented elsewhere in the cited set only
by `Lifshitz2000` and `Zener1937`, neither of which sits in this row. `missing_literature.csv` records
`10.1109/JMEMS.2006.883573` (Duwel et al., *J. MEMS* 15:1437–1445, 2006) as the work that would fill
this row if the manuscript is to keep the resonator claim.

## 7. Fractional and memory models — 11 keys

`Povstenko2004`, `Povstenko2009`, `Povstenko2011Cattaneo`, `Povstenko2016` (4, one group);
`Wang2011`, `Wang2021`, `WangLi2025IV` (3); `Sherief2010Fractional`, `Ezzat2011`, `Yu2024`,
`Bachher2019`. Ten of eleven keys are Tier 1, the highest density in the table, and the cluster is
cited in §3, §5 and §10. The composition is one group with four fractional-heat papers, a second with
three memory-dependent-derivative papers, and four independents; `Wang2011` is additionally the entry
used in `sections/s16_synthesis.tex` l.16 to label the "MDD" row of the heat-law synthesis table, so
it is load-bearing for the review's own taxonomy rather than only for the problem list. `Caputo1967`
and `Gorenflo1997` in the bibliography are the mathematical sources for the operators and are cited
outside this row. No content-level claim is recorded for any key in this cluster.

## 8. Size effects — 10 keys

`Eringen1972`, `Eringen1983` (2), `Askes2006`, `Askes2011` (2), `Maranganti2006`, `Maranganti2007` (2),
`Aifantis1992`, `Lazar2022`, `Zang2014`, `Li2018`. The row is unusual in being built on *pairs* of
methodological papers (Eringen's nonlocal elasticity foundations, Askes–Aifantis gradient-elasticity
comparisons, Maranganti–Sharma length-scale calibration) rather than on single application papers, and
§1 uses four of the ten while §5 uses nine. Only `Eringen1972` and `Aifantis1992` are Tier 1, which is
consistent with the review's position that nonlocal lengths are calibration-dependent: the argument is
carried by the review's own §8 analysis, not by results quoted from these papers. The pairing pattern
is also the reason the "same author group" count matters less here than in rows 4, 5 and 7.

## 9. Variational and uniqueness theory — 5 keys

`Marotti2013`, `Srivastava2026`, `Chandrasekharaiah1996`, `Chirita2016`, `Tibullo2017`. The smallest
row alongside the resonator one, and the only one organised around a *method* rather than a geometry.
`Chirita2016` and `Tibullo2017` are one group (Chiriţă and co-workers, cited in
`sections/s02_history.tex` l.65 for thermodynamic compatibility and continuous dependence of the
time-differential lag models), `Chandrasekharaiah1996` is the uniqueness source used in
`sections/s05_hyperbolic.tex` l.57, and `Marotti2013`/`Srivastava2026` are cited in §4 and §11.
Two of the five are Tier 1. Read against `missing_literature.csv`, this row is where
`10.1007/978-1-4614-0493-4` (Straughan, *Heat Waves*, 2011) belongs and is absent.

---

## Cross-cluster observations

1. **The table is a taxonomy, not a provenance log.** Every row classifies works by problem type; no
   row records a method, a result or a number. That is the gap this evidence base exists to close.
2. **Concentration is concentrated.** Row 4 (14/16 in three groups) and row 7 (7/11 in two groups)
   carry most of the review's interface and memory content; rows 1, 8 and 9 are dispersed.
3. **Weight is inversely related to support in one case.** Row 6 (resonators) has two keys; row 4
   (interfaces) has sixteen. If §9.3.3 is kept, row 6 needs at least one measured-Q study.
4. **Tier-1 density tracks how the keys are used**, from 0/4 (row 1) and 2/11 (row 5's complement) to
   10/11 (row 7). Keys that only illustrate a problem class are correctly Tier 2.

---

## Appendix — Step 8 QA checks

| Check | Result |
|---|---|
| All 416 cited keys present in `paper_notes.csv` | PASS — 416 rows, keys identical to `ref_inventory.csv` |
| Every Tier-1 row has a non-empty `page_or_eq_ref` | PASS — 78/78 (6 source locators, 72 manuscript citation sites explicitly labelled `mss:`) |
| Tier-1 size inside the 60–80 band | PASS — 78 |
| `source_used` truthful | PASS — 3 `FULLTEXT` (Green1993, Quintanilla2003DPL, Chen2001), 3 `ABSTRACT` (Green1972, Huberman2019, DreyerStruchtrup1993), 410 `NOT-READ` |
| No fabricated bibliographic data | PASS — every DOI in `missing_literature.csv` returned a Crossref record this session; one previously suspected DOI (`10.1038/ncomms2640`) was **falsified** by Crossref (it resolves to a soft-X-ray ptychography paper) and replaced by the correct `10.1038/ncomms2630` |
| 15-row spot re-verification | PASS — 15 rows drawn at random from Tier 1: key present in the `.bib`, DOI string identical to `ref_inventory.csv`, cited at the recorded `mss:` site, `used_in_sections` consistent with that site |
| Cluster key counts | PASS — 72 keys over 9 rows, all present in the inventory, 0 unknown keys |
