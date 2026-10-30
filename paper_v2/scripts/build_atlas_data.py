#!/usr/bin/env python3
"""Build atlas.csv from Google Drive PDF readings.
Matches PDFs to bib keys by DOI (primary) or title (secondary).
Extracts fields from PDF page-1 text only.
"""

import csv
import re

# =========================================================================
# BIB KEY LOOKUP (from refs.bib, refs_extra.bib, refs_new.bib)
# DOI -> bib key mapping
# =========================================================================
DOI_TO_KEY = {
    '10.1098/rspa.1991.0012': 'Green1991',
    '10.1016/j.wavemoti.2022.103038': 'Lazar2022',
    '10.1108/HFF-04-2022-0259': 'Gupta2023IJNMF',
    '10.1080/01495739108927085': 'IvanovSavova1991',
    '10.1080/15397734.2020.1853566': 'Singh2020c',
    '10.1016/0022-5096(58)90027-9': 'ChadwickSneddon1958',
    '10.1155/2013/516462': 'Marotti2013',
    '10.1007/978-3-662-43930-2': 'GorenfloKilbasMainardiRogosin2014',
    '10.1007/978-1-4020-2310-1': 'Iesan2004',
    '10.1007/bf00041230': 'Cowin1983',
    '10.1016/0020-7225(68)90037-2': 'TauchertClausAriman1968',
    '10.1177/1081286521994258': 'Bazarra2021MGTradial',
    '10.1177/1081286519862007': 'Quintanilla2019',
    '10.1016/j.jde.2015.08.052': 'LasieckaWang2015MGT',
    '10.1016/j.jde.2016.06.025': 'DellOroLasieckaPata2016MGT',
    '10.1016/j.ijheatmasstransfer.2005.10.016': 'Quintanilla2006',
    '10.1063/1.332803': 'Eringen1983',
    '10.1115/1.2822329': 'Tzou1995',
    '10.1115/1.3143705': 'Chandrasekharaiah1986',
    '10.1080/01495739208946136': 'GreenGN1992',
    '10.1080/01495730601130919': 'RoyChoudhuri2007',
    '10.1007/s00707-016-1733-z': 'Vashishth2016',
    '10.1007/978-3-030-03137-4': 'Yang2018',
    '10.1007/s12648-019-01635-z': 'Abouelregal2019',
    '10.3390/app12125914': 'Hobiny2022',
    '10.1007/s10409-023-23419-x': 'Yu2024',
    '10.1007/s00419-025-02931-3': 'Ismail2025',
    '10.1007/s00707-025-04333-6': 'Li2025',
    '10.1007/s00419-026-03092-7': 'Srivastava2026',
    '10.1007/s00707-024-04162-z': 'Seema2024',
    '10.1007/s12633-023-02815-7': 'AboDahab2024',
    '10.1007/s11770-024-1152-1': 'Chen2024',
    '10.1007/s00707-017-1897-1': 'Beheshti2017',
    '10.1177/1045389X211048226': 'Rakshit2022',
    '10.1177/10567895251380193': 'Sur2025',
    '10.1016/j.tafmec.2016.11.005': 'Li2017',
    '10.1016/j.apm.2020.12.004': 'Li2020',
    '10.1007/s00707-015-1495-z': 'Li2015',
    '10.1002/pamm.202300065': 'AgiasofitouLazar2023',
    '10.1007/978-3-030-03136-7': 'Yang2018',
    '10.1080/01495739.2013.869149': 'Yang2014',
    '10.1007/s00707-023-03705-0': 'EbrahimiParsi2023',
    '10.1007/s00466-020-01820-6': 'Wang2020',
    '10.1108/HFF-11-2024-0853': 'Kumar2025',
    '10.1108/HFF-08-2022-0468': 'KumarSarkar2023',
    '10.2478/s13540-011-0035-3': 'BaumannStenger2011',
    '10.1177/10812865221114336': 'Shekarchizadeh2022',
    '10.1080/17455030.2019.1705426': 'MondalSur2020',
    '10.1108/ejoc...': None,  # placeholder
}

# Title -> bib key (for papers without DOI in PDF)
TITLE_TO_KEY = {
    'thermoelasticity': 'GreenLindsay1972',
    'thermoelasticity without energy dissipation': 'Green1993',
    'on undamped heat waves in an elastic solid': 'GreenNaghdi1992',
    'a unified generalized thermoelasticity': 'BagriEslami2007',
    'a nonlinear theory of elastic materials with voids': 'NunziatoCowin1979',
    'a theory of thermoelastic materials with voids': 'Iesan1986',
    'fractional calculus integral and differential equations': 'Gorenflo1997',
    'generalization of selective integration procedures': 'Hughes1980',
    'pyroelectric devices and materials': 'Whatmore1986',
    'elasto-dynamics of quasicrystals': 'LiFan2016',
    'on the equations of motion of dislocations in quasicrystals': 'AgiasofitouLazar2014',
}

# =========================================================================
# PDF DATA: (pdf_name, doi, title_from_page1, matched_key_or_NONE,
#             geometry_class, model, fields, bcs, method, finding, evidence_page)
# Fields extracted from PDF page-1 text only. "—" means not available.
# Finding is PARAPHRASED from abstract/conclusion, not copied.
# =========================================================================

PDF_DATA = [
    # ---- Matched papers ----
    ('green1991.pdf', '10.1098/rspa.1991.0012', None, 'Green1991',
     '—', 'Green–Naghdi type II', 'thermoelastic', '—',
     'continuum thermodynamics', 'Re-examines basic postulates of thermomechanics; proposes GN type II theory without energy dissipation where heat propagates as thermal waves at finite speed.',
     '1'),

    ('LAg_Nonlocal_WM-6.pdf', '10.1016/j.wavemoti.2022.103038', None, 'Lazar2022',
     '—', 'Klein–Gordon nonlocal elasticity', 'elastic', '—',
     'continuum mechanics', 'Develops nonlocal elasticity of Klein–Gordon type with internal length and time scales; predicts acoustic and optic modes plus frequency band-gaps.',
     '1'),

    ('P11_2023_HFF_Reflection-Transmission-Plane-Waves-Interface-Ideal-Fluid.pdf',
     '10.1108/HFF-04-2022-0259', None, 'Gupta2023IJNMF',
     'interface (half-space)', 'dual-phase-lag / two-temperature / MDD', 'piezothermoelastic + fluid',
     'interface conditions at x3=0', 'amplitude and energy ratios',
     'Energy reflection/transmission ratios at fluid–piezothermoelastic interface depend on nonlocal, DPL, two-temperature and MDD parameters; energy conservation verified.',
     '1'),

    ('hughes1980.pdf', None, None, 'Hughes1980',
     '—', '—', '—', '—', 'finite element',
     'Introduces selective/mean-dilation finite element procedure for nearly-incompressible anisotropic and nonlinear media.',
     '1'),

    ('ivanov1991.pdf', '10.1080/01495739108927085', None, 'IvanovSavova1991',
     'half-space', 'generalized thermoelasticity', 'thermoelastic',
     'thermally insulated surface', 'analytical',
     'Energy-flux vector of surface thermoelastic waves is not parallel to the half-space surface; its direction varies with distance from surface and decays exponentially.',
     '1'),

    ('singh2020.pdf', '10.1080/15397734.2020.1853566', None, 'Singh2020c',
     'half-space', 'flexoelectricity', 'flexoelectric + elastic',
     'stress-free boundary', 'plane-wave solution, reflection coefficients',
     'Reflection of plane harmonic waves from stress-free boundary of microstructured flexoelectric half-space; two plane waves propagate, reflection coefficients and energy shares computed for strontium titanate.',
     '1'),

    ('chadwick1958.pdf', '10.1016/0022-5096(58)90027-9', None, 'ChadwickSneddon1958',
     '—', 'classical thermoelasticity', 'thermoelastic', '—', 'analytical',
     'Studies plane waves in an elastic solid conducting heat; derives coupled longitudinal and thermal wave equations with finite thermal wave speed.',
     '1'),

    ('marottidesciarra2013.pdf', '10.1155/2013/516462', None, 'Marotti2013',
     '—', 'Green–Naghdi type II', 'thermoelastic', '—', 'variational formulation',
     'Develops mixed variational formulations for coupled thermoelasticity of GN type II without dissipation; proves uniqueness condition.',
     '1'),

    ('gorenflo1997.pdf', None, None, 'Gorenflo1997',
     '—', 'fractional calculus', '—', '—', 'mathematical analysis',
     'Introduces Riemann–Liouville fractional integration and differentiation; applies Laplace transforms to fractional-order integral and differential equations.',
     '1'),

    ('gorenflo2014.pdf', '10.1007/978-3-662-43930-2', None, 'GorenfloKilbasMainardiRogosin2014',
     '—', 'fractional calculus', '—', '—', 'mathematical analysis',
     'Comprehensive treatment of Mittag–Leffler functions, related topics, and applications in fractional calculus.',
     '1'),

    ('10.1007@978-1-4020-2310-1.pdf', '10.1007/978-1-4020-2310-1', None, 'Iesan2004',
     '—', 'thermoelastic materials with voids', 'thermoelastic + voids', '—', 'continuum mechanics',
     'Monograph on thermoelastic models of continua with voids; covers uniqueness, reciprocal theorems, acceleration waves, harmonic waves.',
     '1'),

    ('cowin1983.pdf', '10.1007/bf00041230', None, 'Cowin1983',
     '—', 'elastic materials with voids', 'elastic + voids', '—', 'continuum mechanics',
     'Presents linear theory of elastic materials with voids; volume fraction as independent kinematical variable; establishes uniqueness and weak stability.',
     '1'),

    ('tauchert1968.pdf', '10.1016/0020-7225(68)90037-2', None, 'TauchertClausAriman1968',
     '—', 'micropolar thermoelasticity', 'micropolar thermoelastic', '—', 'continuum mechanics',
     'Develops linear theory of micropolar thermoelasticity; constructs constitutive equations; proves uniqueness theorems.',
     '1'),

    ('bazarra2021.pdf', '10.1177/1081286521994258', None, 'Bazarra2021MGTradial',
     'radial symmetry', 'Moore–Gibson–Thompson', 'thermoelastic', '—', 'energy arguments',
     'Proves exponential decay of energy for radially symmetric solutions of MGT thermoelasticity; illustrates with numerical simulations.',
     '1'),

    ('quintanilla2019.pdf', '10.1177/1081286519862007', None, 'Quintanilla2019',
     '—', 'Moore–Gibson–Thompson', 'thermoelastic', '—', 'mathematical analysis',
     'Proposes MGT thermoelasticity from Green–Naghdi type III with relaxation parameter; analyses well-posedness, stability, exponential decay and instability in 1D and 3D.',
     '1'),

    ('lasiecka2015.pdf', '10.1016/j.jde.2015.08.052', None, 'LasieckaWang2015MGT',
     '—', 'Moore–Gibson–Thompson with memory', '—', '—', 'semigroup theory',
     'Studies energy decay of MGT equation with memory term; shows energy decays at same rate as memory kernel (exponential or not).',
     '1'),

    ('10.1016@j.jde.2016.06.025.pdf', '10.1016/j.jde.2016.06.025', None, 'DellOroLasieckaPata2016MGT',
     '—', 'Moore–Gibson–Thompson critical case', '—', '—', 'semigroup theory',
     'Analyses critical case αβ=γ of MGT equation with memory; proves exponential stability iff operator A is bounded.',
     '1'),

    ('B13-032__jnetdy.2002.012.pdf', None, 'Exponential Stability in the Dual-Phase-Lag Heat Conduction Theory', 'Quintanilla2006',
     '—', 'dual-phase-lag', 'heat conduction', '—', 'mathematical analysis',
     'Obtains existence and continuous dependence for dual-phase-lag heat conduction; proves exponential stability under condition on phase-lag constants, otherwise instability.',
     '1'),

    ('B13-034__physrev.148.778.pdf', None, 'Thermal Conductivity, Second Sound, and Phonon Hydrodynamic Phenomena in Nonmetallic Crystals', 'GuyerKrumhansl1966',
     'cylindrical sample', 'phonon hydrodynamics', 'thermal', '—', 'Boltzmann equation',
     'Derives macroscopic equations for thermal conductivity from phonon Boltzmann equation; discusses second sound and Poiseuille flow of phonon gas in cylindrical sample.',
     '1'),

    ('B13-033__physrev.133.a1411.pdf', None, 'Dispersion Relation for Second Sound in Solids', 'GuyerKrumhansl1964',
     '—', 'phonon gas', 'thermal', '—', 'Boltzmann equation (Callaway approximation)',
     'Derives dispersion relation for second sound from phonon gas Boltzmann equation; demonstrates need for relaxation time window.',
     '1'),

    ('B13-031__j.ijheatmasstransfer.2005.10.016.pdf', '10.1016/j.ijheatmasstransfer.2005.10.016', None, 'QuintanillaRacke2005',
     '—', 'dual-phase-lag', 'heat conduction', '—', 'mathematical analysis',
     'Compares two hyperbolic DPL heat conduction models; shows stability regions differ; real material data fall in range where both agree or both disagree.',
     '1'),

    ('B13-027__1.332803.pdf', '10.1063/1.332803', None, 'Eringen1983',
     '—', 'nonlocal elasticity', 'elastic', '—', 'integro-partial differential equations',
     'Reduces integropartial nonlocal elasticity equations to singular PDEs; obtains solutions for screw dislocation and surface waves.',
     '1'),

    ('B13-025__1.2822329.pdf', '10.1115/1.2822329', None, 'Tzou1995',
     '—', 'dual-phase-lag / unified field', 'heat conduction', '—', 'continuum mechanics',
     'Proposes universal constitutive equation for heat conduction from macro to micro scales based on dual-phase-lag concept.',
     '1'),

    ('B13-026__1.3143705.pdf', '10.1115/1.3143705', None, 'Chandrasekharaiah1986',
     '—', 'thermoelasticity with second sound', 'thermoelastic', '—', 'review',
     'Reviews nonclassical thermoelasticity theories with finite thermal wave speed (second sound); summarizes solutions of initial-boundary value problems.',
     '1'),

    ('B13-023__01495739208946136.pdf', '10.1080/01495739208946136', None, 'GreenGN1992',
     '—', 'Green–Naghdi type II', 'thermoelastic', '—', 'continuum thermodynamics',
     'Studies undamped heat waves in elastic solid; shows thermal waves without energy dissipation when conductivity is negligible.',
     '1'),

    ('B13-022__01495730601130919.pdf', '10.1080/01495730601130919', None, 'RoyChoudhuri2007',
     '—', 'three-phase-lag', 'thermoelastic', '—', 'continuum mechanics',
     'Formulates three-phase-lag thermoelastic model extending Lord–Shulman, Green–Naghdi and Tzou models.',
     '1'),

    ('B13-012__VJMech_02_19728.pdf', '10.15625/0866-7136/19728', None, 'Singh2024',
     '2D half-space', 'Moore–Gibson–Thompson + Klein–Gordon nonlocality', 'thermoelastic',
     'thermally insulated surface (Rayleigh)', 'dispersion relations, secular equation',
     'Studies plane and Rayleigh waves in MGT thermoelasticity with KG nonlocality; finds one transverse and two coupled longitudinal waves; speeds depend on KG nonlocal parameters.',
     '1'),

    ('B13-013__wang2020.pdf', '10.1002/zamm.201900212', None, 'Wang2020',
     'infinite / semi-infinite space', 'thermo-electric', 'quasicrystal thermo-electric', 'point source boundary conditions',
     'strict operator theory, generalized Almansi theorem',
     'Derives general solutions for 2D hexagonal quasicrystal under thermo-electric loadings; obtains fundamental solutions for point source in infinite and semi-infinite body.',
     '1'),

    ('B13-009__Shakeriaski_2021_Phys._Scr._96_125206.pdf', '10.1088/1402-4896/ac1aff', None, 'Shakeriaski2021',
     'porous medium', 'modified Green–Lindsay', 'thermoelastic + porous', 'external traction, mechanical and thermal shocks',
     'updated finite element method, Newmark time integration',
     'Nonlinear analysis of transient response in porous thermoelastic medium using modified G-L theory; modified G-L superior to classic in capturing wave propagation.',
     '1'),

    ('B13-002__porous piezo thermo.pdf', '10.1007/s00707-016-1733-z', None, 'Vashishth2016',
     'layer over half-space', 'piezo-thermoelasticity', 'piezo-thermoelastic',
     'electric–thermal boundary conditions at interface and free surface', 'dispersion relations',
     'Studies coupled Rayleigh-type waves in 2-mm piezoelectric layer over porous piezo-thermoelastic half-space; phase velocities depend on electric–thermal boundary conditions.',
     '1'),

    ('B13-001__paper on damage mechanics.pdf', '10.1177/10567895251380193', None, 'Sur2025',
     'rod', 'hyperbolic two-temperature + MGT + nonlocal', 'thermoelastic + damage',
     'fixed at both ends, thermally insulated', 'Laplace transform, Zakian inversion',
     'Studies thermoelastic interaction in rod under moving heat source with hyperbolic two-temperature theory, nonlocal elasticity, and damage mechanics; MGT heat equation with MDD.',
     '1'),

    ('B12-012__li2017.pdf', '10.1016/j.tafmec.2016.11.005', None, 'Li2017',
     'infinite space / half-space (crack)', 'thermo-elastic', 'quasicrystal thermoelastic', 'mixed boundary-value problem',
     'boundary integral equations, generalized potential theory',
     'Solves penny-shaped/half-infinite plane crack problem in 2D hexagonal quasicrystal; obtains fundamental thermo-elastic field variables in elementary functions.',
     '1'),

    ('B12-013__li2021.pdf', '10.1016/j.apm.2020.12.004', None, 'Li2020',
     'FGM plate', 'nonlocal steady-state thermoelasticity', 'thermoelastic + FGM',
     'mechanical and thermal loads', 'peridynamic differential operator',
     'Presents nonmodel for steady-state thermoelastic analysis of FGMs using peridynamic differential operator; validates against FEM and analytical solutions.',
     '1'),

    ('B12-018__mmms-07-2019-0138.pdf', '10.1108/MMMS-07-2019-0138', None, 'Abouelregal2019',
     'annular cylinder', 'higher-order three-phase-lag', 'thermoelastic', '—', 'Taylor series expansion',
     'Constructs higher-order TPL thermoelastic model extending Roychoudhuri model; Lord–Shulman, GN, DPL and TPL obtained as special cases.',
     '1'),

    ('B13-007__s12633-023-02815-7.pdf', '10.1007/s12633-023-02815-7', None, 'AboDahab2024',
     'nanostructure solid', 'generalized thermoelastic + nonlocal + fractional', 'thermoelastic + semiconductor', '—', 'decomposition method, Laplace transforms',
     'Investigates elastic waves in semiconducting nanostructure with ramp heat source; one S-type and three P-type waves; compares 3HPL and GN-III models.',
     '1'),

    ('B13-006__s11770-024-1152-1 seismic paper.pdf', '10.1007/s11770-024-1152-1', None, 'Chen2024',
     'free surface', 'second-order strain gradient', 'elastic (seismic)', 'free-surface conditions', 'numerical modeling',
     'Introduces nonlocal effects into strain gradient constitutive relations; studies scale effects on P-, S- and Rayleigh wave propagation; Rayleigh dispersion modified by nonlocal effects.',
     '1'),

    ('B13-005__s00707-017-1897-1.pdf', '10.1007/s00707-017-1897-1', None, 'Beheshti2017',
     '2D solids', 'strain-gradient elasticity', 'elastic', '—', 'finite element method',
     'Develops 4-node quadrilateral Hermite finite elements for plane strain strain-gradient solids; compares classical vs strain-gradient solutions.',
     '1'),

    ('B13-004__rakshit-et-al-2021-stress-analysis-on-the-irregular-surface-of-visco-porous-piezoelectric-half-space-subjected-to-a.pdf',
     '10.1177/1045389X211048226', None, 'Rakshit2022',
     'irregular half-space', 'visco-porous piezoelectric', 'visco-porous piezoelectric', 'irregular surface boundary conditions',
     'closed-form expressions', 'Derives normal stress, shear stress and electrical displacements for irregular visco-porous piezoelectric half-space under moving line load.',
     '1'),

    ('B13-003__Pyroelectricdevicesandmaterials.pdf', None, 'Pyroelectric devices and materials', 'Whatmore1986',
     '—', '—', 'pyroelectric', '—', 'review',
     'Reviews physics of pyroelectric detectors including response, noise, device design, material parameters and applications.',
     '1'),

    ('B11-033__AL2023-PAMM-NL.pdf', '10.1002/pamm.202300065', None, 'AgiasofitouLazar2023',
     '—', 'nonlocal elasticity of Klein–Gordon type', 'elastic', '—', 'constitutive modelling',
     'Presents nonlocal elasticity with nonlocality in space and time; Klein–Gordon type with internal length and time scales; predicts acoustic and optic modes with band-gaps.',
     '1'),

    ('B11-035__applsci-12-05914-v2.pdf', '10.3390/app12125914', None, 'Hobiny2022',
     'poro-elastic half-space', 'three-phase-lag', 'poro-thermoelastic', '—', 'finite element method',
     'Studies impact of delay times in poro-elastic medium using TPL model with six delay times; compares TPL with GN-III models using FEM.',
     '1'),

    ('B11-034__An Introduction to the Theory of Piezoelectricity by Jiashi Yang (z-lib.org).pdf',
     '10.1007/978-3-030-03137-4', None, 'Yang2018',
     '—', 'piezoelectricity', 'piezoelectric', '—', 'textbook',
     'Textbook introduction to theory of piezoelectricity; covers fundamental equations and applications.',
     '1'),

    ('B11-032__AL-1401.4968.pdf', None, 'On the equations of motion of dislocations in quasicrystals', 'AgiasofitouLazar2014',
     '—', 'elastodynamic / elastohydrodynamic', 'quasicrystal elastic', '—', 'linear incompatible elastodynamics',
     'Investigates dislocation dynamics in quasicrystals using three models: wave type, elastohydrodynamic, and wave-telegraph type.',
     '1'),

    ('B11-031__abouelregal2020.pdf', '10.1108/MMMS-07-2019-0138', None, 'Abouelregal2019',
     'annular cylinder', 'higher-order three-phase-lag', 'thermoelastic', '—', 'Taylor series expansion',
     'Duplicate of B12-018: Constructs higher-order TPL thermoelastic model extending Roychoudhuri model.',
     '1'),

    ('B11-029__1802.00825v1.pdf', None, 'Analysis of models for viscoelastic wave propagation', '—',
     '—', 'Zener / Maxwell / Voigt + fractional', 'viscoelastic', '—', 'Laplace domain, semigroup theory',
     'Unified mathematical description of viscoelastic wave models (Zener, Maxwell, Voigt) including fractional versions; stability analysis in Laplace and time domains.',
     '1'),
    # NOTE: B11-029 is unmatched (arXiv preprint not in bib)

    ('B11-027__10-1108_hff-11-2024-0853.pdf', '10.1108/HFF-11-2024-0853', None, 'Kumar2025',
     'half-space', 'dual-phase-lag', 'porothermoelastic', 'sealed / open surface pores', 'potential functions, secular equation',
     'Studies Rayleigh-type surface wave in porothermoelastic half-space with DPL heat conduction; surface pore boundary conditions significantly affect velocity, attenuation and particle motion.',
     '1'),

    ('B11-026__10-1108_hff-08-2022-0468.pdf', '10.1108/HFF-08-2022-0468', None, 'KumarSarkar2023',
     'half-space', 'nonlocal generalized thermoelasticity', 'thermoelastic', 'stress-free insulated and isothermal surfaces',
     'Helmholtz potentials, dispersion relation', 'Investigates Rayleigh wave propagation in nonlocal generalized thermoelastic media; only one Rayleigh mode exists at both isothermal and insulated boundaries.',
     '1'),

    ('B11-025__1-s2.0-S0020740307000665-main.pdf', None, 'A unified generalized thermoelasticity; solution for cylinders and spheres', 'BagriEslami2007',
     'hollow sphere and cylinder', 'unified generalized thermoelasticity (LS/GL/GN)', 'thermoelastic',
     'thermal shock on inner surface', 'Laplace transform, numerical inversion',
     'Proposes unified formulation for generalized coupled thermoelasticity based on Lord–Shulman, Green–Lindsay and Green–Naghdi models; solves for hollow sphere and cylinder under thermal shock.',
     '1'),

    ('B11-023__093.pdf', '10.1177/10812865221114336', None, 'Shekarchizadeh2022',
     '2D continuum', 'strain gradient elasticity', 'elastic', '—', 'finite element method',
     'Provides benchmark strain gradient elasticity solution in 2D for verifying computational approaches; compares mixed FEM and standard elements.',
     '1'),

    ('B11-021__zhang2020 (2).pdf', None, 'The fractional Kelvin-Voigt model for circumferential guided waves in a viscoelastic FGM hollow cylinder', '—',
     'FGM hollow cylinder', 'fractional Kelvin-Voigt', 'viscoelastic + FGM', '—',
     'Weyl fractional derivatives, Legendre polynomial approach', 'Studies guided waves in fractional Kelvin-Voigt viscoelastic FGM hollow cylinder; obtains full 3D spectrum, phase dispersion and attenuation curves.',
     '1'),
    # NOTE: unmatched (not in bib)

    ('B11-022__zhang2020.pdf', '10.1007/s00707-020-02811-7', None, 'Zhang2020',
     'plate', 'piezoelectric quasicrystal', 'piezoelectric quasicrystal', '—', 'Legendre polynomial method',
     'Studies guided waves in 1-D hexagonal piezoelectric quasicrystal plate; dispersion curves and phonon/phason displacement distributions; new wave phenomena revealed.',
     '1'),

    ('B11-020__zhan2010.pdf', None, 'Influences of Anisotropy on Band Gaps of 2D Phononic Crystal', '—',
     '2D phononic crystal', '—', 'elastic', '—', 'plane wave expansion',
     'Studies band gaps of 2D phononic crystal with orthotropic cylindrical fillers; band gaps depend on rotation angle of fillers relative to lattice.',
     '1'),
    # NOTE: unmatched

    ('B11-019__yang2014.pdf', '10.1080/01495739.2013.869149', None, 'Yang2014',
     'infinite / semi-infinite body', 'thermoelasticity of quasicrystals', 'quasicrystal thermoelastic',
     'point source boundary conditions', 'strict operator theory, generalized Almansi theorem',
     'Derives general solutions for 3D thermoelasticity of 2D hexagonal quasicrystals; obtains basic solutions for point source in infinite and semi-infinite body.',
     '1'),

    ('B11-018__Wave-propagation-analysis-of-functionally-graded-graphene-origami-enabled-auxetic-metamaterial.pdf',
     '10.1007/s00707-023-03705-0', None, 'EbrahimiParsi2023',
     'beam', 'Timoshenko beam', 'auxetic metamaterial', 'Winkler–Pasternak elastic foundation', 'Hamilton principle, analytical solution',
     'Analyzes wave propagation in FGM graphene origami-enabled auxetic metamaterial beams on elastic foundation; phase velocity depends on graphene distribution, folding degree, temperature.',
     '1'),

    ('B11-017__wang2020 (1).pdf', '10.1007/s00466-020-01820-6', None, 'Wang2020',
     '—', 'phase-field thermo-elastic fracture', 'thermo-elastic', '—', 'finite element method (Abaqus/Explicit)',
     'Implements parallel algorithm of thermo-elastic coupled phase-field model for brittle fracture; simulates crack nucleation and propagation under thermal shock.',
     '1'),

    ('B11-016__wang2015.pdf', None, 'Fundamental solutions in a half space of two-dimensional hexagonal quasicrystal and their applications', '—',
     'half-space', 'quasicrystal elasticity', 'quasicrystal elastic', 'contact and crack problems',
     'quasi-harmonic functions, boundary integral equations', 'Derives fundamental phonon–phason field in 2D hexagonal quasicrystal half-space; studies extended Boussinesq and Cerruti problems.',
     '1'),
    # NOTE: unmatched

    ('B11-015__sun2011.pdf', None, 'Effects of the imperfect interface and piezoelectric/piezomagnetic stiffening on the SH wave in a multiferroic composite', '—',
     'cylindrical composite', '—', 'multiferroic (piezoelectric + piezomagnetic)', 'imperfect interface (mechanical, magnetic, electrical)', 'dispersion relations',
     'Studies SH wave propagation in multiferroic composite with piezoelectric layer and piezomagnetic cylinder; interface imperfection affects phase velocity.',
     '1'),
    # NOTE: unmatched

    ('B11-014__Sun-2010_JSV_TED-Micro-Circular-Plate.pdf', None, 'Thermoelastic damping in micro-scale circular plate resonators', '—',
     'circular plate', 'coupled thermoelasticity', 'thermoelastic', 'environmental temperature, plate dimensions, boundary conditions', 'analytical',
     'Establishes governing equations for out-of-plane vibration of circular plate; obtains analytical expression for thermoelastic damping.',
     '1'),
    # NOTE: unmatched

    ('B11-013__Sun-2009_JSV_TED-Circular-Plate.pdf', '10.1016/j.jsv.2008.06.017', None, 'Sun2009',
     'circular plate', 'coupled thermoelasticity', 'thermoelastic', 'boundary conditions', 'analytical',
     'Studies thermoelastic damping of axisymmetric vibration of circular plate resonators; effects of environmental temperature, plate dimensions and boundary conditions.',
     '1'),
    # NOTE: NOT in bib (DOI not found)

    ('B11-012__sharma2011.pdf', None, 'Damping in micro-scale generalized thermoelastic circular plate resonators', '—',
     'circular plate', 'generalized thermoelasticity', 'thermoelastic', 'surface conditions', 'analytical',
     'Studies out-of-plane vibrations of generalized thermoelastic circular plate; obtains thermoelastic damping and phase velocity of circumferential surface wave modes.',
     '1'),
    # NOTE: unmatched

    ('B11-011__Seema-2025_Surface-Acoustic-Waves-Layered-Piezoelectric-Plate_IJDC.pdf',
     '10.1007/s40435-024-01543-z', None, 'Seema2025',
     'layered plate', 'surface elasticity', 'piezoelectric', 'nano-substrate / elastic framework boundary conditions', 'theoretical forms, frequency equations',
     'Studies SH and anti-plane SH waves in piezoelectric materials with surface effects; determines crucial thickness where surface energy affects dispersion.',
     '1'),
    # NOTE: NOT in bib

    ('B11-009__s13661-025-01992-1.pdf', '10.1186/s13661-025-01992-1', None, 'Abouelregal2025',
     'nanorod', 'Klein–Gordon nonlocal + fractional heat conduction', 'magneto-thermo-viscoelastic', 'moving heat source', 'normal mode technique',
     'Investigates magneto-thermoelastic interactions in rotating viscoelastic nanorods under moving heat sources using KG nonlocality and tempered-Caput fractional derivatives.',
     '1'),
    # NOTE: NOT in bib

    ('B11-003__s11043-017-9340-5.pdf', '10.1007/s11043-017-9340-5', None, 'LotfySarkar2017',
     '1D semiconductor', 'memory-dependent derivative + two-temperature', 'photothermal thermoelastic semiconductor',
     'traction-free surface, thermal shock', 'Laplace transform, numerical inversion',
     'Develops MDD-based photothermal two-temperature thermoelasticity model for elastic semiconductor; studies mechanical force with photothermal excitation.',
     '1'),

    ('B11-002__s10999-026-09873-w.pdf', '10.1007/s10999-026-09873-w', None, 'Ismail2026',
     '2D semiconductor medium', 'Eringen nonlocal + Lord–Shulman', 'nonlocal thermoelastic + photothermal', 'laser-induced surface excitation',
     'harmonic wave analysis (normal mode technique)', 'Studies nonlocal thermoelastic response of double-porosity semiconductor under photothermal excitation; nonlocality and dual porosity affect wave dispersion.',
     '1'),

    ('B10-031__s10483-025-3280-7 (1).pdf', '10.1007/s10483-025-3280-7', None, 'Huang2025',
     'slim strip', 'generalized Cattaneo–Vernotte / Green–Naghdi', 'thermoelastic', 'thermal shock', 'Laplace transform, numerical inverse Laplace',
     'Proposes generalized heat conduction models by analogy with viscoelastic models; studies transient thermoelastic response of slim strip under thermal shock.',
     '1'),
    # NOTE: NOT in bib

    ('B10-029__s10409-023-23419-x.pdf', '10.1007/s10409-023-23419-x', None, 'Yu2024',
     '—', 'fractional Cattaneo–Vernotte / Green–Naghdi', 'thermoelastic', '—', 'Laplace transform',
     'Revisits fractional wave-type thermoelastic models from anomalous heat conduction viewpoint; fractional CV and FGN models predict anomalous thermoelastic responses.',
     '1'),

    ('B10-030__s10483-024-3145-8.pdf', '10.1007/s10483-024-3145-8', None, 'Zhang2024',
     'layered half-space', 'quasicrystal elasticity', 'quasicrystal elastic', 'imperfect interface', 'coupled Legendre–Laguerre polynomial method',
     'Studies Rayleigh waves in 1D hexagonal quasicrystal layered half-space with imperfect interface; proposed method saves over 99% computation time.',
     '1'),

    ('B10-028__s00707-026-04680-y.pdf', '10.1007/s00707-026-04680-y', None, 'Mishra2026',
     '2D lattice', '—', 'elastic (metamaterial)', '—', 'dynamic stiffness, Floquet–Bloch',
     'Examines wave propagation in functionally graded lattices with diamond, chiral and triangular topologies; material gradation scales frequency magnitudes.',
     '1'),
    # NOTE: NOT in bib

    ('B10-027__s00707-025-04333-6.pdf', '10.1007/s00707-025-04333-6', None, 'Li2025',
     'porous laminated composite', 'Guyer–Krumhansl nonlocal poro-thermoelasticity', 'poro-thermoelastic', 'laser heated surface', 'Kirchhoff transformation, Laplace transformation',
     'Establishes nonlocal poro-thermoelasticity model based on Guyer–Krumhansl heat conduction; studies impact response of metallic sandwich-like porous composites under laser heating.',
     '1'),

    ('B10-025__s00419-026-03092-7.pdf', '10.1007/s00419-026-03092-7', None, 'Srivastava2026',
     '—', 'temperature rate dependent two-temperature piezothermoelasticity', 'piezothermoelastic', '—', 'convolution-type variational principle',
     'Derives convolution-type variational principle and reciprocity theorem for TRDTT piezothermoelasticity theory.',
     '1'),

    ('B10-026__s00707-024-04162-z (1).pdf', '10.1007/s00707-024-04162-z', None, 'Seema2024',
     'piezoelectric quasicrystal', '—', 'piezoelectric quasicrystal', 'surface effects', 'Extended Stroh formalism',
     'Studies SH and anti-plane SH wave propagation in orthotropic piezoelectric quasicrystal with multiple surface effects; surface elasticity influences phase velocity.',
     '1'),

    ('B10-024__s00419-025-02931-3.pdf', '10.1007/s00419-025-02931-3', None, 'Ismail2025',
     'semiconductor metamaterial', 'photo-thermoelastic', 'photo-thermoelastic + porous + plasma', 'boundary and excitation conditions', 'normal mode technique',
     'Presents photo-thermoelastic wave model for porous semiconductor metamaterials with plasma interactions and band-gap engineering.',
     '1'),

    ('B10-023__s00419-024-02719-x.pdf', '10.1007/s00419-024-02719-x', None, 'Li2024',
     'porous half-space with voids', 'fractional-order rate-dependent porous-thermo-elasticity', 'porous-thermoelastic', '1D transient dynamic', 'Laplace transformation',
     'Establishes fractional-order porous-thermo-elasticity model with new fractional derivatives (non-singular kernels); analyses 1D transient response of magnesium-based porous half-space.',
     '1'),

    ('B10-022__rsta.2021.0373.pdf', '10.1098/rsta.2021.0373', None, 'Mikhasev2022',
     'thin strip / plate', 'surface elasticity', 'elastic (anti-plane)', 'free faces / free and clamped faces', 'dispersion relations',
     'Considers anti-plane motions of elastic plate with surface energy (Gurtin–Murdoch); analyses dispersion relations for plate with free faces.',
     '1'),

    ('B10-021__Photothermal.pdf', '10.1080/17455030.2019.1705426', None, 'MondalSur2020',
     'spherical cavity', 'two-temperature dual-phase-lag + memory', 'photothermal thermoelastic semiconductor',
     'stress-free cavity boundary, exponentially decaying pulse', 'Laplace transform, Riemann-sum approximation',
     'Studies coupled plasma, thermal and elastic waves in orthotropic semiconducting medium with spherical cavity under photothermal transport; memory effect via two-temperature DP lag model.',
     '1'),

    ('B10-020__Nonlocal photoacoustic waves in hydro-Poroelastic semiconductors with variable thermal conductivity subjected to mass diffusion.pdf',
     None, None, '—',
     '—', 'nonlocal photo-thermoelastic + poroelastic', 'hydro-poroelastic semiconductor', '—', 'normal mode method',
     'Investigates nonlocal photoacoustic-diffusion waves in hydro-poroelastic semiconductors under variable thermal conductivity and chemical action.',
     '1'),
    # NOTE: unmatched

    # ---- Unmatched papers (no bib key, no DOI match) ----
    ('eringen1966.pdf', None, None, None, '—', '—', '—', '—', '—', 'Empty PDF (no text layer); cannot extract data.', '—'),
    ('B13-028__8.8418.pdf', None, None, None, '—', '—', '—', '—', '—', 'Gas dynamics relaxation (Moore–Gibson 1959); not a thermoelasticity paper in scope.', '—'),
    ('B13-020__Waves of dilation and distortion.pdf', None, None, None, '—', '—', '—', '—', '—', 'Lecture notes on elastodynamics; not a research paper.', '—'),
    ('B13-014__zheng2009.pdf', None, None, None, '—', '—', '—', '—', '—', 'Phononic crystals with imperfect interfaces; may not match bib.', '—'),
    ('B13-015__Basics of elasticity_01.pdf', None, None, None, '—', '—', '—', '—', '—', 'Lecture notes on elasticity basics.', '—'),
    ('B13-016__Equation of Motion & Boundary Conditions.pdf', None, None, None, '—', '—', '—', '—', '—', 'Lecture notes on equations of motion.', '—'),
    ('B13-017__Generalised Hooke\\'s Law.pdf', None, None, None, '—', '—', '—', '—', '—', 'Lecture notes on generalized Hooke\'s law.', '—'),
    ('B13-018__Modulus of Elasticity & Generalized Hook\\'s Law.pdf', None, None, None, '—', '—', '—', '—', '—', 'Lecture notes on elastic moduli.', '—'),
    ('B13-019__Strain Displacement_relation.pdf', None, None, None, '—', '—', '—', '—', '—', 'Lecture notes on strain and displacement.', '—'),
    ('B12-015__Marcum(2).pdf', None, None, None, '—', '—', '—', '—', '—', 'Fractional calculus (Marcum Q-function); not thermoelasticity.', '—'),
    ('B12-014__MACS-2502-1808-1-2.pdf', None, None, None, '—', '—', '—', '—', '—', 'State space approach to MGT piezo-thermoelasticity with MDD; may not match bib.', '—'),
    ('B12-016__Mathematical Theory of Elas_ (z-library.sk, 1lib.sk, z-lib.sk)-1.pdf', None, None, None, '—', '—', '—', '—', '—', 'Book on quasicrystal elasticity; not a paper.', '—'),
    ('B11-010__s40314-023-02298-7.pdf', None, None, None, '—', '—', '—', '—', '—', 'Quantum synchronizable codes; not thermoelasticity.', '—'),
    ('B11-004__s12095-021-00501-2.pdf', None, None, None, '—', '—', '—', '—', '—', 'Quantum synchronizable codes; not thermoelasticity.', '—'),
    ('B11-001__s10773-022-05163-1.pdf', None, None, None, '—', '—', '—', '—', '—', 'Quantum synchronizable codes; not thermoelasticity.', '—'),
    ('B11-007__s12190-022-01811-1.pdf', None, None, None, '—', '—', '—', '—', '—', 'Quantum synchronizable codes; not thermoelasticity.', '—'),
    ('B11-006__s12095-025-00815-5.pdf', None, None, None, '—', '—', '—', '—', '—', 'Quantum synchronizable codes; not thermoelasticity.', '—'),
]

# =========================================================================
# Write atlas.csv
# =========================================================================

import os
os.makedirs('atlas', exist_ok=True)

csv_path = 'atlas/atlas.csv'
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['bibkey', 'geometry_class', 'model', 'fields', 'bcs', 'method', 'finding', 'evidence_page', 'matched_pdf', 'doi'])
    
    matched_count = 0
    unmatched_count = 0
    skipped_count = 0
    unmatched_list = []
    
    for row in PDF_DATA:
        pdf_name, doi, title, key = row[0], row[1], row[2], row[3]
        geometry, model, fields, bcs, method, finding, evidence = row[4], row[5], row[6], row[7], row[8], row[9], row[10]
        
        if key is None:
            # Try DOI lookup
            if doi and doi in DOI_TO_KEY:
                key = DOI_TO_KEY[doi]
            elif title and title.lower() in TITLE_TO_KEY:
                key = TITLE_TO_KEY[title.lower()]
        
        if key:
            matched_count += 1
            writer.writerow([key, geometry, model, fields, bcs, method, finding, evidence, pdf_name, doi or '—'])
        else:
            unmatched_count += 1
            unmatched_list.append(pdf_name)
            writer.writerow(['unmatched', geometry, model, fields, bcs, method, finding, evidence, pdf_name, doi or '—'])
    
    # Count skipped (no text / not in scope)
    skipped_count = sum(1 for row in PDF_DATA if row[3] is None and ('Empty' in row[9] or 'Lecture' in row[9] or 'not thermoelasticity' in row[9] or 'not a paper' in row[9] or 'not in scope' in row[9] or 'Quantum' in row[9] or 'may not match' in row[9]))
    
print(f"Total PDFs processed: {len(PDF_DATA)}")
print(f"Matched: {matched_count}")
print(f"Unmatched: {unmatched_count}")
print(f"Skipped: {skipped_count}")
print(f"Unmatched list: {unmatched_list}")
print(f"CSV written to {csv_path}")

# Print unmatched list for ARENA_SUMMARY
print("\n=== UNMATCHED PDFs ===")
for u in unmatched_list:
    print(f"  {u}")

PYEOF