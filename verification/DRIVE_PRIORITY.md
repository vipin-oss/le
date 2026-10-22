# DRIVE_PRIORITY — read order for the paper library (task item V-B10b)

**Order:** `control/BRAVE_B10.md` @ `origin/claude/control` `6569d60` (incl. the ADDENDUM), B10b.
**Deliverables:** this file (the plan) + `verification/DRIVE_PRIORITY.csv` (row-level assignment for all
370 files: `inv_id, tier, batch, proposed_section, tier_basis, identity_or_reason, folder, file_name,
drive_id, dup_of, read_level`).
**Input:** `verification/DRIVE_INVENTORY.csv` (B10a, commit `a1cafed`). **No body was read for this file** —
identity comes from title pages already opened in B10a plus this turn's 12 title-page reads, or from the
file name / folder and is labelled as such.

---

## 1. Task

Rank the library by usefulness for the review — (1) governing-equation papers, (2) interface /
energy-partition papers, (3) the rest — and give every row the manuscript section where it would be cited.

## 2. Method

**Tiering rules.** Tier 1 = a paper that *states a governing equation or model* the review must describe
(GL, LS, GN I–III/V, DPL, TPL, MGT, MDD, nonlocal/gradient, Klein–Gordon, two-temperature) or a
Barak/Gupta paper that is the direct backing for §9.7 / EQ-10.12. Tier 2 = a paper whose subject is
reflection/transmission, imperfect bonding, or energy partition at an interface. Tier 3 = everything else
(beams, shells, flexoelectricity, semiconductor waves, textbooks, statistics/LaTeX files).

**Every row carries a `tier_basis`, and the four values are not interchangeable:**

* `TITLE-PAGE` (9 rows) — I opened the first page this session and read the title/journal. Identity is
  established.
* `NAME-ONLY` (2 rows) — I opened the title page but only have author+year confirmed (front matter was a
  repository cover sheet).
* `NAME-INFERRED` (44 rows) — tier and topic come from words in the file name (`nonlocal`, `two-temp`,
  `MDD`, `energy-ratio`). Identity is **not** established; the name can lie (a file called
  `rotating medium.pdf` could be any of a dozen papers).
* `FOLDER-INFERRED` (15 rows) — the file sits in a model-form folder (`Three-phase-lag`, `TPL`,
  `Two-temp`) and was classified by its neighbours. Weakest basis of all.

**Section vocabulary.** Section numbers follow the ones already used in `LITERATURE_BASE.csv`
(`proposed_section`), inferred from that column's own sub-area pairing: s.3 second sound/ballistic,
s.4.1 Biot, s.4.3 LS, s.4.4 GL, s.4.5–4.6 GN, s.4.7–4.8 DPL/TPL, s.4.10 MGT, s.4.12 two-temperature,
s.5 micropolar/porous/semiconductor, s.5.5 piezothermoelasticity, s.6 & s.11 MDD/fractional,
s.7 nonlocal/gradient, s.8 dispersion/Rayleigh–Lamb, s.9 interfaces (incl. §9.7), s.10 energy
flux/partition (EQ-10.12), s.13 evidence/applications. **I did not re-read the manuscript this turn**; if
a section number has moved, the mapping moves with it, not the paper.

## 3. Result — counts

| tier | files | distinct (duplicates removed) | batches |
|---|---|---|---|
| 1 — governing equations + §9.7/EQ-10.12 backing | **70** | 67 | 7 × ≤10 |
| 2 — interface / energy partition | **26** | 26 | after tier 1 |
| 3 — the rest | **274** | 271 | on request only |

Three tier-1 files are byte-level duplicates of another tier-1 file (`DRV-0231` = `DRV-0111`,
`DRV-0273` = `DRV-0272`, `DRV-0340` = `DRV-0272`), recorded in `dup_of` so B10c reads each paper once.

## 4. Tier 1 — 70 files, 7 batches

Batch 1 is deliberately the batch with the most established identities: 9 of its 10 rows are title-page
confirmed, because these are the originals the manuscript's §4 leans on.

| batch | inv_id | proposed section | file (short name) | identity / reason | basis |
|---|---|---|---|---|---|
| B01 | DRV-0058 | s.4.3 | `lord1967` | Lord & Shulman 1967, generalized thermoelasticity (LS) | TITLE-PAGE |
| B01 | DRV-0089 | s.4.4 | `Megahid, Abouelregal, Sedighi - 2023 - Modified` | Megahid, Abouelregal, Sedighi 2023 (name only) | NAME-ONLY |
| B01 | DRV-0127 | s.6; s.11 | `Wang, Li - 2011 - Surpassing the fractional der` | Wang & Li 2011, Surpassing the fractional derivative: MDD concept, Comput. Math. Appl. 62, 1562-1567 | TITLE-PAGE |
| B01 | DRV-0137 | s.4.7-4.8; s.10 | `Aldawody, Hendy, Ezzat - 2019 - On dual-phase-l` | Aldawody, Hendy, Ezzat 2019, DPL magneto-thermo-viscoelasticity with MDD | TITLE-PAGE |
| B01 | DRV-0143 | s.7 | `Sarkar, De, Sarkar - 2019 - Waves in nonlocal t` | Sarkar, De, Sarkar 2019, Waves in nonlocal thermoelastic solids of type II, JTS 42:9 1153-1170 | TITLE-PAGE |
| B01 | DRV-0148 | s.7 | `Eringen - 1978 - Nonlocal Continuum Mechanics a` | Eringen 1978, Nonlocal continuum mechanics and some applications | TITLE-PAGE |
| B01 | DRV-0149 | s.4.12 | `Youssef - 2006 - Theory of two-temperature-gene` | Youssef 2006, two-temperature theory, IMA J. Appl. Math. 71, 383-390 | TITLE-PAGE |
| B01 | DRV-0154 | s.4.7-4.8; s.7 | `Yang et al. - 2021 - Dual-phase-lag thermoelast` | Yang et al. 2021, DPL thermoelastic damping in nonlocal nanoplates, WRCM, DOI 10.1080/17455030.2021.1903117 | TITLE-PAGE |
| B01 | DRV-0183 | s.4.7-4.8; s.10 | `Spatial behaviour of solutions of the three-pha` | Quintanilla, TPL spatial behaviour (duplicate of DRV-0183) | TITLE-PAGE |
| B01 | DRV-0184 | s.4.7-4.8 | `On A Thermoelastic Three-Phase-Lag Mode` | Roy Choudhuri 2007 TPL (duplicate file of DRV-0184) | TITLE-PAGE |
| B02 | DRV-0022 | s.11 | `P32_2025_EJMSOL_Fractional-Memory-Effects-Wave-Reflection-Pre-stressed-Microstructured` | governing-equation / model-form paper (name cue "fractional") | NAME-INFERRED |
| B02 | DRV-0037 | s.11 | `P17_2024_MAMS_Memory-dependent-Fractional-Order-Analysis-Initially-Stressed-Piezo-thermoelastic` | governing-equation / model-form paper (name cue "fractional") | NAME-INFERRED |
| B02 | DRV-0111 | s.11 | `2019Amodifiedfractional-ordergeneralizedpiezoel` | governing-equation / model-form paper (name cue "fractional") | NAME-INFERRED |
| B02 | DRV-0152 | s.11 | `Ezzat, Karamany - 2011 - Fractional order heat ` | governing-equation / model-form paper (name cue "fractional") | NAME-INFERRED |
| B02 | DRV-0165 | s.11 | `Kumar-2017_CSM_Fractional-Energy-Ratios-Piezothermoelastic` | governing-equation / model-form paper (name cue "fractional") | NAME-INFERRED |
| B02 | DRV-0215 | s.4.12 | `two-temperature thermo-viscoelasticity with thr` | governing-equation / model-form paper (name cue "two temp") | NAME-INFERRED |
| B02 | DRV-0216 | s.4.12 | `Two-temperature theory in magneto-thermoelastic` | governing-equation / model-form paper (name cue "two temp") | NAME-INFERRED |
| B02 | DRV-0231 | s.11 | `2019Amodifiedfractional-ordergeneralizedpiezoel` | governing-equation / model-form paper (name cue "fractional") | NAME-INFERRED |
| B02 | DRV-0277 | s.11 | `Fractional_heat_conduction_with_variable_thermal_c` | governing-equation / model-form paper (name cue "fractional") | NAME-INFERRED |
| B02 | DRV-0288 | s.4.4 | `abouelregal2020` | Abouelregal 2020 (author+year only, title page not yet read) | NAME-ONLY |
| B03 | DRV-0006 | s.7 | `P48_2026_IJMMD_Klein-Gordon-Nonlocal-Dynamics-Porous-Piezo-thermoelastic-Medium` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B03 | DRV-0009 | s.7 | `P45_2026_CMT_Heat-Map-Analysis-Wave-Dynamics-Nonlocal-Kelvin` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B03 | DRV-0014 | s.7 | `P40_2026_HFF_Dispersion-Damping-Characteristics-Rayleigh-type-Waves-KG-Nonlocal` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B03 | DRV-0024 | s.7 | `P30_2025_HFF_Coupled-Thermo-mechanical-Dynamics-Rotating-Nano-beams-Spatiotemporal-Nonlocality` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B03 | DRV-0039 | s.6; s.11 | `P15_2024_MAMS_Fractional-MDD-Analysis-Piezo-photo-thermo-elastic-Waves-Semiconductor-Medium` | governing-equation / model-form paper (name cue "mdd") | NAME-INFERRED |
| B03 | DRV-0054 | s.6; s.11 | `Sur-2018_ActaMech_FE-Fiber-Reinforced-Cylinder-MDD` | governing-equation / model-form paper (name cue "mdd") | NAME-INFERRED |
| B03 | DRV-0222 | s.4.12 | `Effects of nonlocality and two temperature` | governing-equation / model-form paper (name cue "two temp") | NAME-INFERRED |
| B03 | DRV-0226 | s.6; s.11 | `mdd vs fract` | governing-equation / model-form paper (name cue "mdd") | NAME-INFERRED |
| B03 | DRV-0227 | s.6; s.11 | `mdd + fractional` | governing-equation / model-form paper (name cue "mdd") | NAME-INFERRED |
| B03 | DRV-0363 | s.4.12 | `2020Baljeet-porous thermo two temp` | governing-equation / model-form paper (name cue "two temp") | NAME-INFERRED |
| B04 | DRV-0034 | s.7 | `P20_2024_WRCM_Rayleigh-Wave-Nonlocal-Piezo-thermo-electric-Semiconductor-Medium-Fractional` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B04 | DRV-0050 | s.7 | `P04_2023_PNASI_Analysis-Waves-Boundary-Surfaces-Distinct-Media-Nonlocal` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B04 | DRV-0088 | s.7 | `Gupta, Das, Dutta - 2021 - Nonlocal stress anal` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B04 | DRV-0106 | s.7 | `Surface waves in porous nonlocal` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B04 | DRV-0112 | s.7 | `Li-2016_Nonlocal-Piezoelectric-Nanobeams` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B04 | DRV-0117 | s.7 | `2020_SSS_Nonlocal-MEET-Beams-Stability` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B04 | DRV-0120 | s.7 | `Li-2018_Heliyon_Nonlocal-Piezo-Thermoelastic` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B04 | DRV-0150 | s.7 | `Bachher, Sarkar - 2019 - Nonlocal theory of the` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B04 | DRV-0151 | s.7 | `Unknown - 2019 - Nonlocal Modeling, Analysis, a` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B04 | DRV-0212 | s.7 | `23 PI- 13 MAMS Reflection hygrothermal Nonlocal` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B05 | DRV-0029 | s.9.7; s.10 (EQ-10.12) | `P25_2024_MTDM_Effect-Viscosity-Hyperbolic-Two-temperature-Energy-Ratios-Elastic` | own-group interface energy-partition paper - direct backing for sec 9.7 and EQ-10.12 | NAME-INFERRED |
| B05 | DRV-0031 | s.9.7; s.10 (EQ-10.12) | `P23_2024_IJAME_Response-Stiffness-Viscosity-Energy-Ratios-Piezo-visco-thermo-elastic-Medium` | own-group interface energy-partition paper - direct backing for sec 9.7 and EQ-10.12 | NAME-INFERRED |
| B05 | DRV-0040 | s.9.7; s.10 (EQ-10.12) | `P14_2024_JTS_Energy-Transfer-Interface-Monoclinic-Piezothermoelastic-Thermoelastic-Half` | own-group interface energy-partition paper - direct backing for sec 9.7 and EQ-10.12 | NAME-INFERRED |
| B05 | DRV-0217 | s.7 | `Reflection of plane waves in a nonlocal micropo` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B05 | DRV-0218 | s.7 | `piezo+nonlocal_1` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B05 | DRV-0219 | s.7 | `piezo+nonlocal` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B05 | DRV-0272 | s.7 | `LAg_Nonlocal_WM-6` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B05 | DRV-0273 | s.7 | `LAg_Nonlocal_WM-6 (2)` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B05 | DRV-0330 | s.7 | `Nonlocal photoacoustic waves in hydro-Poroelastic semiconductors with variable thermal conductivity subjected to mass diffusion` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B05 | DRV-0340 | s.7 | `LAg_Nonlocal_WM-6 (1)` | governing-equation / model-form paper (name cue "nonlocal") | NAME-INFERRED |
| B06 | DRV-0042 | s.9.7; s.10 (EQ-10.12) | `P12_2023_MMMS_Effect-Memory-Stiffness-Energy-Ratios-Interface-Distinct` | own-group interface energy-partition paper - direct backing for sec 9.7 and EQ-10.12 | NAME-INFERRED |
| B06 | DRV-0045 | s.9.7; s.10 (EQ-10.12) | `P09_2023_PhysScr_Energy-Ratio-Response-Interface-Elastic-Dual-porous-Thermoelastic` | own-group interface energy-partition paper - direct backing for sec 9.7 and EQ-10.12 | NAME-INFERRED |
| B06 | DRV-0046 | s.9.7; s.10 (EQ-10.12) | `P08_2023_HFF_Energy-Analysis-Interface-Piezo-Thermoelastic-Half-Spaces` | own-group interface energy-partition paper - direct backing for sec 9.7 and EQ-10.12 | NAME-INFERRED |
| B06 | DRV-0047 | s.9.7; s.10 (EQ-10.12) | `P07_2023_IJP_Energy-Analysis-Boundary-Interface-Elastic-Piezothermoelastic-Half-spaces` | own-group interface energy-partition paper - direct backing for sec 9.7 and EQ-10.12 | NAME-INFERRED |
| B06 | DRV-0049 | s.9.7; s.10 (EQ-10.12) | `P05_2023_SciRep_Behavior-Higher-order-MDD-Energy-Ratios-Interface-Thermoelastic` | own-group interface energy-partition paper - direct backing for sec 9.7 and EQ-10.12 | NAME-INFERRED |
| B06 | DRV-0172 | s.4.12 | `plane waves hyper two temp` | folder is a model-form collection (Two-temp); identity not yet read | FOLDER-INFERRED |
| B06 | DRV-0173 | s.4.12 | `MPM240_04_youssef-Final` | folder is a model-form collection (Two-temp); identity not yet read | FOLDER-INFERRED |
| B06 | DRV-0174 | s.4.12 | `h_yp two` | folder is a model-form collection (Two-temp); identity not yet read | FOLDER-INFERRED |
| B06 | DRV-0175 | s.4.12 | `hyperobolic temp` | folder is a model-form collection (Two-temp); identity not yet read | FOLDER-INFERRED |
| B06 | DRV-0176 | s.4.12 | `hyperbolic two temper ` | folder is a model-form collection (Two-temp); identity not yet read | FOLDER-INFERRED |
| B07 | DRV-0177 | s.4.12 | `hyperbolic two temp` | folder is a model-form collection (Two-temp); identity not yet read | FOLDER-INFERRED |
| B07 | DRV-0178 | s.4.12 | `hyerpbolic two temp` | folder is a model-form collection (Two-temp); identity not yet read | FOLDER-INFERRED |
| B07 | DRV-0179 | s.4.12 | `energy` | folder is a model-form collection (Two-temp); identity not yet read | FOLDER-INFERRED |
| B07 | DRV-0182 | s.4.7-4.8 | `Thermoelastic interaction in the semi infinite ` | folder is a model-form collection (Three-phase-lag); identity not yet read | FOLDER-INFERRED |
| B07 | DRV-0185 | s.4.7-4.8 | `nonlocal thermoelastic` | folder is a model-form collection (Three-phase-lag); identity not yet read | FOLDER-INFERRED |
| B07 | DRV-0186 | s.4.7-4.8 | `modeling of memeory dependent` | folder is a model-form collection (Three-phase-lag); identity not yet read | FOLDER-INFERRED |
| B07 | DRV-0187 | s.4.7-4.8 | `Eigenfunction approach to generalized thermovis` | folder is a model-form collection (Three-phase-lag); identity not yet read | FOLDER-INFERRED |
| B07 | DRV-0188 | s.4.7-4.8 | `Effect of moving heat source on a magneto-therm` | folder is a model-form collection (Three-phase-lag); identity not yet read | FOLDER-INFERRED |
| B07 | DRV-0189 | s.4.7-4.8 | `Analysis of plane wave propagation under the pu` | folder is a model-form collection (Three-phase-lag); identity not yet read | FOLDER-INFERRED |
| B07 | DRV-0190 | s.4.7-4.8 | `Modeling of memory-dependent` | folder is a model-form collection (TPL); identity not yet read | FOLDER-INFERRED |
**What batch 1 already settles, and what it does not.** Title pages confirm that the library *does*
contain: Lord & Shulman 1967 (LS), Roy Choudhuri 2007 (TPL) **twice**, Quintanilla's TPL spatial-behaviour
paper, Wang & Li 2011 (MDD origin, *Comput. Math. Appl.* 62, 1562–1567), Eringen 1978 (nonlocal),
Youssef 2006 (two-temperature, *IMA J. Appl. Math.* 71, 383–390), Sarkar/De/Sarkar 2019 (nonlocal type II),
Aldawody–Hendy–Ezzat 2019 (DPL+MDD) and Yang et al. 2021 (DPL damping in nonlocal nanoplates).
It confirms equally that the library does **not** contain — at least not under a name that surfaced in
either enumeration — the following originals (§6 below).

## 5. Tier 2 — 26 files

| inv_id | proposed section | file (short name) | basis |
|---|---|---|---|
| DRV-0018 | s.9 | `P36_2025_JIOS_Response-Memory-Imperfect-Fluid-Double-Porous-Non` | NAME-INFERRED |
| DRV-0023 | s.9 | `P31_2025_CompStruct_Effects-Layer-Imperfections-Material-Gradation-Circumferential-Shear` | NAME-INFERRED |
| DRV-0033 | s.9 | `P21_2024_PhysScr_Reflection-Quasi-Plasma-Wave-Photo-piezo-Semiconductor-Medium` | NAME-INFERRED |
| DRV-0043 | s.9 | `P11_2023_HFF_Reflection-Transmission-Plane-Waves-Interface-Ideal-Fluid` | NAME-INFERRED |
| DRV-0044 | s.9 | `P10_2023_HFF_Reflection-Free-Surface-Orthotropic-Piezo-hygro-thermo-elastic-Medium` | NAME-INFERRED |
| DRV-0052 | s.9 | `P02_2021_TURCOMAT_Waves-Propagation-Interface-Two-Liquid-Saturated-Porous` | NAME-INFERRED |
| DRV-0053 | s.9 | `P01_2020_SST_Waves-Boundary-Surface-Transversely-Viscothermoelastic-Slab-Between` | NAME-INFERRED |
| DRV-0090 | s.9 | `Singh, Gupta - 2023 - Wave reflection by the fr` | NAME-INFERRED |
| DRV-0093 | s.9 | `Jiao et al. - 2024 - The dispersion and reflect` | NAME-INFERRED |
| DRV-0094 | s.9 | `j.tafmec.2008.07.010` | TITLE-PAGE |
| DRV-0095 | s.9 | `TheWavePropagationthroughtheImperfectInterfaceb` | NAME-INFERRED |
| DRV-0097 | s.9 | `Reflection of plane waves from the surface of a` | NAME-INFERRED |
| DRV-0099 | s.9; s.10; s.11 | `Response of fractional order on energy ratios a` | TITLE-PAGE |
| DRV-0123 | s.9 | `Liu-2020_EJMSOL_Reflection-Elastic-Waves` | NAME-INFERRED |
| DRV-0141 | s.9 | `Kumar, Chawla - 2013 - Reflection and refractio` | NAME-INFERRED |
| DRV-0144 | s.9 | `Kumar et al. - 2018 - Reflection of Plane Waves` | NAME-INFERRED |
| DRV-0146 | s.9 | `Kaur, Lata, Singh - 2020 - Reflection and refra` | NAME-INFERRED |
| DRV-0147 | s.9 | `Kaur, Lata, Singh - 2020 - Reflection and refra(1)` | NAME-INFERRED |
| DRV-0157 | s.9; s.10 | `MDD+energy ratio` | TITLE-PAGE |
| DRV-0158 | s.9 | `Effectsofstiffnessonreflection` | NAME-INFERRED |
| DRV-0167 | s.9 | `reflection` | NAME-INFERRED |
| DRV-0168 | s.9 | `MMMS-03-2015-0012` | TITLE-PAGE |
| DRV-0181 | s.9 | `Reflection_of_plane_waves_at_the_free_surface_o` | NAME-INFERRED |
| DRV-0223 | s.9 | `Wave propagation at the welded interface of an ` | NAME-INFERRED |
| DRV-0224 | s.9 | `Inhomogeneous wave reflection from the surface ` | NAME-INFERRED |
| DRV-0341 | s.9 | `Kumawat, Vishwakarma - 2023 - Circumferential SH wave in piezo-reinforced composite structure with imperfect interface bonding` | NAME-INFERRED |
Tier 2 is the set whose *subject* is the interface: reflection/transmission amplitudes, imperfect or
welded bonding, and the energy-ratio bookkeeping that §9–§10 actually depends on. Note the asymmetry with
tier 1: tier 2 is dominated by `NAME-INFERRED`, because interface papers are numerous and their titles say
so plainly, while tier-1 identity needs a title page.

## 6. Gaps the priority list exposes (these are findings, not oversights)

Reading the library against §4 and §10 of the manuscript, the following **primary sources are absent** and
must be obtained from outside Drive before §4/§9.7 can be called primary-sourced:

* **Green–Lindsay 1972** (`10.1007/BF00045689`) — not in the library. The supervisor holds it; B11's GL
  work stands on `control/FULLTEXT_FINDINGS_01.md` F1, not on a Drive file.
* **Green–Naghdi 1991/1992/1993** (GN-I/II/III, undamped and damped) — no file matches; the GN material in
  `Mendeley` is *about* GN, not by them. `s.4.5–4.6` is therefore second-hand in the library.
* **Tzou 1995 DPL original** — absent. The only "Tzou" file is Tzou & Bao 1995 (piezothermoelastic
  *shells*, `JSV` 184(3) 453–473, title-page confirmed), which is a different paper. Do not cite it as DPL.
* **Biot 1956** — absent (the library has Biot-era material only through secondary papers).
* **Moore-Gibson 1960 / Thompson 1972** (MGT origins) — absent; §4.10's own ledger flagged the missing
  originals (B5b), and the library does not repair that.
* **Green–Kubo / GK and Klein–Gordon originals** — absent; the KG files in the library are the group's own
  KG-nonlocal papers (`P43`, `P48`, `P40`, `P45`), i.e. applications, not the original.

Consequence for B10c: tier 1 can be *checked against the library* for LS, TPL, DPL-variant, MDD, nonlocal
and two-temperature, but **not** for GL, GN, MGT or Biot. Those four stay at their current status tags and
the B10 report must say so per batch.

## 7. Tier 3 — 274 files (summary)

| folder | tier-3 files |
|---|---|
| 2_Others_Papers_/Collected-from-My-Folders | 70 |
| 2_Others_Papers_/Collected-from-Drafts | 45 |
| 1_My_Published_Papers | 29 |
| 2_Others_Papers_/Mendeley | 17 |
| 2_Others_Papers_/Beam | 15 |
| 2_Others_Papers_/Nonlocal | 14 |
| 2_Others_Papers_/Used-in-P10 | 12 |
| 2_Others_Papers_/Flexo | 11 |
| 2_Others_Papers_/Reflection-piezo | 11 |
| 2_Others_Papers_/Used-in-P31 | 10 |
| 2_Others_Papers_/_root | 8 |
| 2_Others_Papers_/New-piezo | 7 |
| 2_Others_Papers_/Used-in-P17 | 7 |
| 2_Others_Papers_/Energy | 6 |
| 2_Others_Papers_/Reflection+piezo | 4 |
| Papers_root | 3 |
| 2_Others_Papers_/Piezo+MDD | 2 |
| 2_Others_Papers_/Used-in-P07 | 2 |
| 2_Others_Papers_/R-Poonia-Sir | 1 |
Tier 3 is not "worthless" — it is "not needed for the equation base". It carries the beam/shell/
flexoelectric/semiconductor literature that §13's application examples would cite, plus texts
(`Structural Mechanics` LibreTexts, `Mathematical Theory of Elasticity`, `An Introduction to the Theory of
Piezoelectricity`) and two files that are not papers at all (`Statistics Crash Course`, `latex_primer`).
I will not read tier 3 unless asked; its rows are still itemised in the CSV so nothing is lost.

### 6.1 How the absence was checked, and its limit

Checked by scanning all 370 file names against the originators' surnames (`green`, `naghdi`, `lindsay`,
`biot`, `moore`, `gibson`, `thompson`, `guyer`, `krumhansl`, `tzou`): **zero hits** except one `Tzou` file,
which is Tzou & Bao 1995 (shells). The nearest thing to a GK source in the library is
`DS chandrasekharahica.pdf` — almost certainly Chandrasekharaiah's generalized-thermoelasticity review,
which is a *secondary* summary and would need its own title-page check before it is used as a GK citation.

**Limit:** this is a filename check. An opaque name (`093.pdf`, `FullText2019.pdf`, `Full.pdf`,
`s40314-023-02298-7.pdf`) can conceal any paper, so the statement is "no file *named for* these authors
exists", not "these papers are certainly absent". The B10c batches will close the opaque names one by one,
and any hit will be reported as a correction to this section.

## 8. Self-citation balance — the 53 `1_My_Published_Papers` files

This is a review written by the group that owns a large share of the MDD / interface-energy-ratio
literature it surveys. That makes self-citation both unavoidable and dangerous, and it needs a rule, not a
vibe.

**What the numbers are now.**

| quantity | value |
|---|---|
| own PDFs in the library | 53 |
| own PDFs currently cited in `LITERATURE_BASE` (430 rows) | **9** |
| share of the bibliography that is own work | **≈2.1 %** |
| `LITERATURE_BASE` rows whose author string names Barak or Gupta | 8 (1.9 %) |
| own PDFs **not** cited at all | 44 |
| rows whose authors are blank, so ownership cannot be checked | **308 of 430** |

The last row matters: **the present self-citation share cannot be measured properly**, because 71 % of the
base has no author string. The 2.1 % is a floor, not the true figure — a Barak/Gupta paper among the 308
blank rows would be invisible to this count. B10d fixes that; until then any claim that "we barely cite
ourselves" is unsupported.

**How many to cite, and why.**

* **Recommendation: 12–20 own papers (≈3–5 % of a 430-reference review).** That is roughly double the
  current floor and still below the level a referee notices. Of those, 8 are forced by §9.7 and EQ-10.12 —
  they *are* the derivations being reviewed — and 4–8 more cover the MDD-variant and nonlocal-interface
  work that no other group has done.
* **Do not cite the other 33.** A library is not a bibliography. Adding an own paper because a PDF exists is
  precisely what a reviewer flags.
* **The hard ceiling is ≈10 % (43 refs).** Above that, on a review of a field the group dominates, the
  standard referee sentence appears ("the authors over-cite their own work") and it is unanswerable.

**Rules that make the number defensible.**

1. Cite an own paper **only where it is the primary source for a specific equation, number or definition
   used here** — never as background, never in a "many authors have studied…" list.
2. **Never more than three own citations in a row** without an independent work between them.
3. For every own paper cited for a *result*, name at least one independent group that reports the same or
   a comparable result (Vashishth & Sukhija, Kumar & Sharma, Sarkar/De, Sharma, Othman, Ezzat).
4. In §9.7, where the attributions are unavoidable, say plainly that the results are the group's own and
   are reproduced here with equation numbers, rather than citing them in the third person as if external.
5. Mark the group's **variant** forms (the uniform-operator GL of eq. 4.9, the second-order TPL) as variants
   in the self-citations too — a self-citation does not upgrade a variant into an original. This is exactly
   the error EQ-042/CL-006 now records.

**Where the 53 fall, by tier:** 17 tier 1 (8 for §9.7/EQ-10.12, 6 nonlocal §7, 3 MDD/fractional §6/§11),
7 tier 2 (§9 reflection/interface), 29 tier 3 (beams, poroelastic cylinders, semiconductor waves — cite
none of these in the review body; a handful may belong in §13 as application examples).

**How a reviewer will see it.** They will not count 430 entries. They will notice two things: (i) whether
the same three names recur in every section's citation block, and (ii) whether the paper's own results are
presented as *the* state of the art without independent corroboration. Twelve to twenty citations spread
over §6, §7, §9 and §10, each attached to a specific equation and each paired with independent work, reads
as expertise. Forty citations clustered in §9–§10 reads as a citation cartel, whether or not the science is
right.

## 9. B10c plan (7 batches, ≤10 papers each)

| batch | content | why this order |
|---|---|---|
| B01 | the 10 confirmed originals/variants (LS, TPL ×2 + Quintanilla, MDD origin, nonlocal Eringen, two-temperature Youssef, DPL+MDD Aldawody, DPL nonlocal Yang, Sarkar type II, Abouelregal) | they underwrite §4 and §7; highest certainty, so fastest to fetch facts |
| B02 | fractional-derivative set (7 files, 1 duplicate) + two-temperature block start + Abouelregal | §11 and §4.12; the fractional law is where the manuscript's own kernel claim lives |
| B03 | two-temperature rest + MDD set | completes §4.12 and §6 |
| B04–B05 | nonlocal/gradient set (23 files, 3 duplicates) | §7 is the largest single section in the base (40 rows) |
| B06 | own energy-ratio papers (8 for §9.7/EQ-10.12) | they carry the attributions; read after the originals so the comparison is to the source, not to the group |
| B07 | leftovers (Klein–Gordon own papers, "modeling of memory-dependent" etc.) | smallest marginal value |

For each paper `FULLTEXT_FACTS.csv` gets one row: key, heat/constitutive law **as printed with its
equation number**, stress and energy equation, parameter ordering/stability condition, energy-ratio
definition (R_flux / R_ref / R_mode, cross terms), status tag, and every conflict with the manuscript or
ledgers. Garbled text layer → render the page; still unreadable → `UNVERIFIED`, no guessing.
Batch 1 is where GL/GN/MGT gaps ( §6 ) get explicitly restated as "not checkable from this library".

## 10. Evidence / sources

* Tier-1 identities: 21 title pages opened across B10a and this turn (each `extraction_status: success`);
  the 12 new ones are Wang & Li 2011 (`Comput. Math. Appl.` 62, 1562–1567), Eringen 1978, Youssef 2006
  (`IMA J. Appl. Math.` 71, 383–390, DOI `10.1093/imamat/hxh101`), Roy Choudhuri 2007
  (`J. Therm. Stresses` 30:3, 231–238, DOI `10.1080/01495730601130919`), Quintanilla (TPL spatial
  behaviour), De/Sarkar et al. 2020 (`J. Heat Transfer`, DOI `10.1115/1.4046924`), Aldawody/Hendy/Ezzat
  2019, Yang et al. 2021 (`Waves Random Complex Media`, DOI `10.1080/17455030.2021.1903117`),
  Kumar & Sharma 2019 (`Appl. Math. Comput.` 358, 194–203), Biswas & Mukhopadhyay 2018
  (DOI `10.1080/01495739.2017.1393780`), Tzou & Bao 1995 (`JSV` 184(3), 453–473), Sarkar/De/Sarkar 2019
  (`J. Therm. Stresses` 42:9, 1153–1170, DOI `10.1080/01495739.2019.1618760`).
* Tier/section assignment for the remaining rows: `DRIVE_INVENTORY.csv` (file name + folder), no text read.
* Section vocabulary: `LITERATURE_BASE.csv` `proposed_section` column cross-tabulated against `sub_area`
  (e.g. all 27 GL rows carry `s.4.4`; all 40 nonlocal rows carry `s.7`; all 48 interface rows carry `s.9`).
* Self-citation counts: computed over `LITERATURE_BASE.csv` (430 rows, 8 with Barak/Gupta in the author
  string, 308 blank author strings) and `DRIVE_INVENTORY.csv` (53 own PDFs, 9 matched to a base id).

## 11. Checks done

1. **Counts reconcile:** 70 + 26 + 274 = 370 = the B10a file count; 67 distinct tier-1 = 70 − 3 duplicates.
2. **Every one of the 370 rows has exactly one tier, one `tier_basis`, and a non-empty `proposed_section`.**
3. **Duplicates flagged, not deleted:** 8 duplicate files overall (`dup_of`), 3 of them in tier 1, so B10c
   reads 67 papers, not 70.
4. **No row claims an identity it does not have:** the `NAME-INFERRED` and `FOLDER-INFERRED` labels are on
   59 of the 70 tier-1 rows and on all 26 tier-2 rows; only 9 tier-1 rows are title-page confirmed.
5. **Section numbers were not invented here** — they are the existing `LITERATURE_BASE.proposed_section`
   values, cross-checked against `sub_area` so that "s.7" means nonlocal and not, say, dispersion.
6. **Gap claims checked by filename scan** across all 370 names (§6.1), with the opaque-name limit stated.
7. **Self-citation arithmetic re-derived** from the two CSVs rather than quoted from memory: 9/430 = 2.1 %;
   12–20 own refs = 2.8–4.7 %; 43 = 10 %.
8. **Privacy:** no personal/private folder is named, listed or referenced; this file and the CSV contain only
   paper-library file names, ids and inferred topics.

## 12. Confidence

* Tier assignment for the 9 title-page-confirmed rows: **HIGH**.
* Tier assignment for `NAME-INFERRED` rows: **MEDIUM** — the cue word is usually decisive (`nonlocal`,
  `two-temperature`) but not always (`rotating medium.pdf`, `SHARMA for orthotropic.pdf`).
* Tier assignment for `FOLDER-INFERRED` rows: **LOW-MEDIUM** — folder membership is the group's own filing,
  which has already proved unreliable once (the `Three-phase-lag` folder contains a paper that is not
  obviously TPL).
* Batch ordering: **HIGH** as a plan, **UNVERIFIED** as a prediction of what each batch will contain.
* Self-citation restriction (12–20): a judgement, **MEDIUM**; the *numbers* it rests on are HIGH except the
  ownership of the 308 blank-author rows, which is **UNKNOWN**.

## 13. NOT verified / open issues

* **No body of any paper was read.** Every statement here about what a file contains is a statement about
  its title page, its name, or the folder it sits in. Nothing here may be cited as a literature fact.
* **The tier-1 list may contain wrong entries.** Two known-risky rows: `DRV-0151`
  (`Unknown - 2019 - Nonlocal Modeling, Analysis, a.pdf` — likely a numerical-analysis textbook, not a
  nonlocal-thermoelasticity paper) and the three `LAg_Nonlocal_WM-6` duplicates, whose identity is unknown
  beyond the words in the name. They stay in tier 1 because the cost of opening them is one page; if they
  are not what they claim, B10c reports it.
* **Section mapping is second-hand.** I could not open the manuscript this turn (the repo holds only
  `verification/`); the section numbers come from `LITERATURE_BASE`'s own column, not from the text.
* **The four missing originals (GL, GN, MGT, Biot) are a gap in the library, not in this analysis.** B10c
  cannot close them; they need PDFs from outside Drive.
* **No `read_level` was changed anywhere.** All 370 rows remain `NONE`; `LITERATURE_BASE` is untouched by
  this item.
* **Tier 3 was not inspected row by row** — it is a residual bucket, and its contents are asserted to be
  non-essential by elimination, not by examination.

---

## 14. Status at close of tier 1, and the tier-2 plan (B10d)

**Tier-1 status.** All seven batches are complete (`V-B10c_b01` … `V-B10c_b07`, commits `7986af0`, `943cce0`, `544079b`, `bf8ec09`, `ea9a7e8`, `a2a35b6`, and this batch). `FULLTEXT_FACTS.csv` holds **70 rows**, one per file, including the 3 duplicates and the one preprint that was later superseded by a journal version. Reading changed the classification of five of the 70, all now corrected in `DRIVE_PRIORITY.csv`: DRV-0179 is an interface/energy paper, not two-temperature; DRV-0185 is a Green–Naghdi reflection paper, not a nonlocal one (the file name `nonlocal thermoelastic.pdf` lied); DRV-0190 is a duplicate of DRV-0186; DRV-0177 is the journal version of the DRV-0176 preprint; and the two-temperature block belongs to §11.3, not §4.12.

**Tier-2 roster.** 26 files, all `s.9` except two that also touch `s.10`/`s.11`. Split: **7 own papers** in `1_My_Published_Papers`, 19 external, spread over 11 folders.

**Two actions before any reading.**

1. **Deduplicate first, on content, not on names.** `Kaur, Lata, Singh - 2020 - Reflection and refra.pdf` and `…(1).pdf` (DRV-0146 / DRV-0147) are near-certainly one paper; md5 plus the printed DOI decides. A duplicate found here is recorded in `dup_of` and read once — the tier-1 experience (DRV-0190: md5-distinct, same DOI) is why the check is by DOI, not by hash.
2. **Same evidence discipline as tier 1.** Every row gets the ten `FULLTEXT_FACTS` columns; no row without a printed equation number; `read_level = FULL` only for text actually read this session.

**Batches (3 × ≤10).**

| batch | files | content | why this order |
|---|---|---|---|
| T2-A | 9 | the 7 own papers + the 2 `Energy`-folder papers (DRV-0097, DRV-0099) | the own set carries the §9.7 attributions and must be read before the external papers so the comparison runs source → group, not group → source |
| T2-B | 9 | imperfect-boundary pair (DRV-0094, DRV-0095), flexo pair (DRV-0090, DRV-0093), nonlocal-interface (DRV-0123), `New-piezo` pair (DRV-0157, DRV-0158), `Reflection+piezo` pair (DRV-0167, DRV-0168) | the §9.3 interface-condition material; these are the papers that decide whether the manuscript's boundary conditions are stated correctly |
| T2-C | 8 | `Mendeley` set (DRV-0141, 0144, 0146/0147), `Used-in-P11` pair (0223, 0224), `R-Poonia-Sir` (0181), `Collected-from-My-Folders` (0341) | left-overs, plus the remainder of the reference-transfer set |

**What each tier-2 row must record, beyond the ten columns.** For every paper: (a) the **energy-ratio definition as printed** — whether each ratio is a flux ratio, a work ratio, or a modal energy ratio, and whether cross/interaction terms are defined; (b) whether the paper prints an **exact identity** (like DRV-0040 eq (6.14) and DRV-0179 eq (80)) or an **approximate/numerical unity statement** (like the five B06 own-group papers); (c) for the imperfect-boundary papers, the printed form of the interface condition (spring stiffness, mass layer, or displacement/temperature jump) with its equation number.

**Deliverable.** One `V-B10d_t2x.md` per batch plus a consolidated table in `V-B10d_summary.md`: paper → printed identity or approximation → equation number → section. That table is what §9.7 and §10.5 need, and it is the honest replacement for the current situation in which the manuscript's unity statement rests on two printed identities and a cluster of approximations.

## 15. Tier-3 plan — metadata-only pass (B10e), 274 files

**Scope, stated narrowly.** Title page and printed DOI only. **No body is read, no equation is recorded, no `FULLTEXT_FACTS` row is created.** The purpose is bookkeeping: find out what is in the library, which of it is already in `LITERATURE_BASE`, and which of it is own-group work. Nothing produced here may be cited as a literature fact — a title page tells you what a paper is, never what it says.

**Output.** A new file `verification/DRIVE_TIER3_METADATA.csv`, one row per file, columns:

| column | content |
|---|---|
| `inv_id` | from `DRIVE_INVENTORY.csv` |
| `file_name` | as filed |
| `first_author` | surname only, as printed on the title page |
| `journal` | as printed (book chapter / thesis / report flagged as such) |
| `year` | as printed |
| `DOI` | as printed on the title page or copyright line; **blank if not printed** — never resolved from a search engine, because a resolved DOI is no longer a title-page fact |
| `match_status` | `IN_BASE` / `NEW` / `AMBIGUOUS` / `UNREADABLE` / `NO_TITLE_PAGE` |
| `lit_id` | `LITERATURE_BASE` id when `IN_BASE`, else blank |
| `own_paper` | `Y` / `N` / `UNKNOWN`, from the folder and the author string |
| `evidence` | the literal title-page line the metadata came from (≤120 chars) |
| `notes` | only for exceptions |

**Method.**

1. Batches of **~35 files** (8 batches). Download 35 at a time, md5 all of them, extract only page 1 (and page 2 when page 1 is a repository cover sheet, which happened repeatedly in tier 1). Delete the batch before the next.
2. **Match to `LITERATURE_BASE` by DOI first, then by `first_author + year + journal`.** A name-only match is `AMBIGUOUS`, never `IN_BASE` — the tier-1 lesson is that a plausible file name can describe a different paper, and the same applies to a plausible author/year pair.
3. **Unreadable title pages are recorded, not guessed.** `UNREADABLE` means the extracted page 1 has no title line (scanned image, math-font garbling, cover sheet with no bibliographic data); `NO_TITLE_PAGE` means the file is not a paper at all (statistics, LaTeX source, figure lists).
4. **A DOI collision inside tier 3 is itself a result** — that is how DRV-0190 was found — so duplicates are recorded in `notes` and counted, not silently merged.
5. **Own-group files get no special treatment here.** They are flagged and counted; whether they are cited is a §14 question, not a metadata question.

**Deliverable and acceptance.** `V-B10e.md` with a reconciliation table: 274 = `IN_BASE` + `NEW` + `AMBIGUOUS` + `UNREADABLE` + `NO_TITLE_PAGE` + duplicates, with the residue named file by file. Plus one number that currently does not exist: **how many of the 274 are already in the bibliography**, and how many are own-group work that is not.

**Explicit limits, so this pass cannot be mistaken for reading.**

* No claim from this pass goes into the manuscript. A tier-3 file that later turns out to matter must be promoted and read under the tier-1 rules before any statement rests on it.
* `read_level` in `DRIVE_PRIORITY.csv` becomes `METADATA-ONLY` for these rows — deliberately distinct from `FULL` and from `NONE`, so the two can never be confused in a later audit.
* No folder that the privacy rule protects is named in the CSV, the V-file, or here; own-group files are referenced by `inv_id` and file name only.
* `LITERATURE_BASE` is **not** extended from this pass. Adding a row requires either a read (tier 1) or an explicit decision to keep a candidate — the pass produces candidates, not entries.

**Estimated cost.** 8 batches, one turn each, same shape as a tier-1 batch but roughly a third of the per-paper work. Stops on request at any batch boundary.
