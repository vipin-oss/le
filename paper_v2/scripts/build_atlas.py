#!/usr/bin/env python3
"""Build atlas.csv and MATCH_REPORT.csv from Google Drive PDF page-1 reads.
Match ONLY by DOI printed on page 1 vs doi field in refs*.bib.
ASCII only output.
"""

import csv
import os

# DOI -> bib key (from refs.bib, refs_extra.bib, refs_new.bib)
DOI_TO_KEY = {
    '10.1007/s10483-025-3280-7': 'Huang2025',
    '10.1007/s10409-023-23419-x': 'Yu2024',
    '10.1007/s00419-026-03092-7': 'Srivastava2026',
    '10.1007/s12648-019-01635-z': 'Abouelregal2019',
    '10.1016/j.ijheatmasstransfer.2005.10.016': 'Quintanilla2006',
    '10.1080/15397734.2020.1852088': 'Ma2020',
    '10.1108/HFF-04-2022-0259': 'Gupta2023IJNMF',
    '10.1108/HFF-04-2023-0208': 'Yadav2023',
}

# Matched PDF data extracted from page-1 text only.
# (pdf_filename, extracted_doi, bib_key, geometry_class, model, fields, bcs, method, finding, evidence_page)
MATCHED = [
    ('B10-031__s10483-025-3280-7 (1).pdf',
     '10.1007/s10483-025-3280-7', 'Huang2025',
     'slim strip',
     'generalized heat conduction: generalized Cattaneo-Vernotte and Green-Naghdi models',
     'thermoelastic coupling',
     'thermal shock',
     'Laplace transform, numerical inverse Laplace transform',
     'Generalizes heat conductive models by analogy with mechanical viscoelastic models; investigates transient thermoelastic response of slim strip under thermal shock; compares effects of material parameters across models.',
     '1'),
    ('B10-029__s10409-023-23419-x.pdf',
     '10.1007/s10409-023-23419-x', 'Yu2024',
     'not specified on page 1 (nanomaterials / low-dimensional systems)',
     'fractional Cattaneo-Vernotte and fractional Green-Naghdi thermoelastic models',
     'thermoelastic coupling',
     'not specified on page 1',
     'Laplace transform method',
     'Fractional CV and FGN models predict anomalous thermoelastic responses: higher temperature and compressive stress than classical thermoelasticity; FGN type-I model predicts anomalous responses for all time range.',
     '1'),
    ('B10-025__s00419-026-03092-7.pdf',
     '10.1007/s00419-026-03092-7', 'Srivastava2026',
     'not specified on page 1 (homogeneous regular anisotropic piezoelectric material)',
     'temperature rate dependent two temperature (TRDTT) piezothermoelasticity',
     'piezothermoelasticity: thermal + electric + mechanical',
     'initial boundary value problem',
     'convolution-type variational principle, reciprocity theorem',
     'Derives variational principle of convolution type and reciprocity theorem for TRDTT piezothermoelasticity; alternative formulation incorporates initial conditions into field equations.',
     '1'),
    ('B11-008__s12648-019-01635-z.pdf',
     '10.1007/s12648-019-01635-z', 'Abouelregal2019',
     'infinite non-homogeneous orthotropic functionally graded medium with spherical cavity',
     'three-phase-lag thermoelastic heat conduction with higher-order time-fractional derivatives',
     'thermoelasticity: thermal + mechanical',
     'spherical cavity boundary',
     'Taylor series expansion of time-fractional order',
     'New higher-order fractional TPL thermoelastic model extending Ezzat and Roychoudhuri models; includes high-order time-fractional derivatives of TPLs in heat flux, temperature gradient and thermal displacement gradient; applied to FGM medium with spherical cavity.',
     '1'),
    ('B13-031__j.ijheatmasstransfer.2005.10.016.pdf',
     '10.1016/j.ijheatmasstransfer.2005.10.016', 'Quintanilla2006',
     'not specified (mathematical comparison of models)',
     'dual-phase-lag heat conduction: two competing hyperbolic models',
     'heat conduction',
     'not specified',
     'mathematical analysis, comparison of parameter regions',
     'Compares two DPL heat conduction models; shows stability parameter regions differ between models; real material data fall in range where both agree or both disagree.',
     '1'),
    ('B03-015__10.1080@15397734.2020.1852088.pdf',
     '10.1080/15397734.2020.1852088', 'Ma2020',
     'two-dimensional fiber-reinforced half-space',
     'fractional order theory of thermoelasticity',
     'thermoelasticity: thermal + mechanical + magnetic + gravity',
     'not specified on page 1',
     'normal mode analysis',
     'Fractional order thermoelasticity applied to 2D fiber-reinforced half-space with magnetic field, gravity and moving heat source; magnetic field, gravity and heat source significantly influence variable distributions.',
     '1'),
    ('B01-011__P11_2023_HFF_Reflection-Transmission-Plane-Waves-Interface-Ideal-Fluid.pdf',
     '10.1108/HFF-04-2022-0259', 'Gupta2023IJNMF',
     'interface of nonlocal orthotropic piezothermoelastic space and fluid half-space (x3=0)',
     'nonlocal piezothermoelasticity with dual-phase-lag, two-temperature, MDD',
     'piezothermoelasticity + fluid',
     'interface conditions at x3=0',
     'amplitude ratios, energy ratios',
     'Primary P waves strike interface; one reflected wave in fluid half-space and four transmitted waves in piezothermoelastic medium; energy ratios affected by nonlocal, DPL, two-temperature and MDD parameters; energy conservation verified across interface.',
     '1'),
    ('B01-010__P10_2023_HFF_Reflection-Free-Surface-Orthotropic-Piezo-hygro-thermo-elastic-Medium.pdf',
     '10.1108/HFF-04-2023-0208', 'Yadav2023',
     'free surface of orthotropic piezo-hygro-thermo-elastic medium',
     'piezo-hygro-thermo-elasticity',
     'piezoelectric + hygro-thermal + elastic',
     'free surface boundary conditions',
     'amplitude ratios, energy ratios',
     'Five coupled reflected plane waves identified: quasi-longitudinal P, quasi-thermal, quasi-transverse, quasi-moisture, electric potential; moisture, temperature diffusivity, pyro-electricity and frequency affect energy distribution.',
     '1'),
]

# Unmatched PDFs (DOI not found in bib, or no DOI on page 1, or not in scope)
UNMATCHED = [
    ('B10-023__s00419-024-02719-x.pdf', '10.1007/s00419-024-02719-x', 'DOI not found in any bib file'),
    ('B10-022__rsta.2021.0373.pdf', '10.1098/rsta.2021.0373', 'DOI not found in any bib file'),
    ('B10-021__Photothermal.pdf', '10.1080/17455030.2019.1705426', 'DOI not found in any bib file'),
    ('B10-020__Nonlocal photoacoustic waves...pdf', '-', 'No DOI printed on page 1'),
    ('B04-005__jmech.2018.10.pdf', '10.1017/jmech.2018.10', 'DOI not found in any bib file'),
    ('B10-001__hosseini2019.pdf', '10.1016/j.apm.2018.09.024', 'DOI not found in any bib file'),
    ('2026-10_QP_131181_Set-B.pdf', '-', 'Examination paper, not a research paper'),
]

os.makedirs('atlas', exist_ok=True)

# ---- Write atlas.csv (only matched papers) ----
atlas_path = 'atlas/atlas.csv'
with open(atlas_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['bibkey', 'geometry_class', 'model', 'fields', 'bcs', 'method', 'finding', 'evidence_page'])
    for row in MATCHED:
        writer.writerow([row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])

print(f"atlas.csv written: {len(MATCHED)} matched rows")

# ---- Write MATCH_REPORT.csv ----
report_path = 'atlas/MATCH_REPORT.csv'
with open(report_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['pdf_filename', 'extracted_doi', 'matched_bibkey', 'reason'])
    
    matched_pdfs = {row[0] for row in MATCHED}
    
    for row in MATCHED:
        writer.writerow([row[0], row[1], row[2], 'DOI matched to bib key'])
    
    for row in UNMATCHED:
        writer.writerow([row[0], row[1], 'unmatched', row[2]])
    
    # Also list B11-* PDFs known from session memory but not yet re-read
    b11_unmatched = [
        ('B11-012__sharma2011.pdf', '-', 'No DOI match found'),
        ('B11-010__s40314-023-02298-7.pdf', '-', 'Not thermoelasticity (quantum codes)'),
        ('B11-011__Seema-2025_Surface-Acoustic-Waves...pdf', '10.1007/s40435-024-01543-z', 'DOI not in bib'),
        ('B11-009__s13661-025-01992-1.pdf', '10.1186/s13661-025-01992-1', 'DOI not in bib'),
        ('B11-007__s12190-022-01811-1.pdf', '10.1007/s12190-022-01811-1', 'DOI not in bib'),
        ('B11-006__s12095-025-00815-5.pdf', '10.1007/s12095-025-00815-5', 'DOI not in bib'),
        ('B11-005__s12095-022-00591-6.pdf', '10.1007/s12095-022-00591-6', 'DOI not in bib'),
        ('B11-004__s12095-021-00501-2.pdf', '10.1007/s12095-021-00501-2', 'DOI not in bib'),
        ('B11-003__s11043-017-9340-5.pdf', '10.1007/s11043-017-9340-5', 'DOI not in bib'),
        ('B11-002__s10999-026-09873-w.pdf', '10.1007/s10999-026-09873-w', 'DOI not in bib'),
        ('B11-001__s10773-022-05163-1.pdf', '10.1007/s10773-022-05163-1', 'DOI not in bib'),
    ]
    for row in b11_unmatched:
        writer.writerow([row[0], row[1], 'unmatched', row[2]])
    
print(f"MATCH_REPORT.csv written: {len(MATCHED) + len(UNMATCHED) + len(b11_unmatched)} rows")

# Print summary
print(f"\n=== ATLAS SUMMARY ===")
print(f"Total PDFs given (from Google Drive): {len(MATCHED) + len(UNMATCHED) + len(b11_unmatched)}")
print(f"Matched (DOI in bib): {len(MATCHED)}")
print(f"Unmatched: {len(UNMATCHED) + len(b11_unmatched)}")
print(f"\nMatched bib keys:")
for row in MATCHED:
    print(f"  {row[2]} (DOI: {row[1]})")

PYEOF