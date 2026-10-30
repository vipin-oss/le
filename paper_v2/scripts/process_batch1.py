#!/usr/bin/env python3
"""Process batch 1 of atlas targets: extract text, match DOI to bibkey, extract fields.
ASCII only output. No non-ASCII characters.
"""
import csv
import os
import re
import sys
from pypdf import PdfReader

# Mapping: bibkey -> Google Drive downloaded file path (relative to paper_v2/)
PDF_FILES = {
    'AboDahab2020': '../google_drive/B03-013__1-s2.0-S221137972031737X-main.pdf',
    'Aldandani2026': '../google_drive/B02-006__P40_2026_HFF_Dispersion-Damping-Characteristics-Rayleigh-type-Waves-KG-Nonlocal.pdf',
    'Aldandani2026a': '../google_drive/B02-015__P50_2026_SciRep_Rayleigh-Surface-Wave-Dynamics-Porous-Piezo-thermoelectric-Smart.pdf',
    'Barak2023': '../google_drive/B01-005__P05_2023_SciRep_Behavior-Higher-order-MDD-Energy-Ratios-Interface-Thermoelastic.pdf',
    'Barak2023IJP': '../google_drive/B01-007__P07_2023_IJP_Energy-Analysis-Boundary-Interface-Elastic-Piezothermoelastic-Half-spaces.pdf',
    'Barak2023JTS': '../google_drive/B01-014__P14_2024_JTS_Energy-Transfer-Interface-Monoclinic-Piezothermoelastic-Thermoelastic-Half.pdf',
    'Barak2023MMMS': '../google_drive/B01-012__P12_2023_MMMS_Effect-Memory-Stiffness-Energy-Ratios-Interface-Distinct.pdf',
    'Barak2023a': '../google_drive/B01-017__P17_2024_MAMS_Memory-dependent-Fractional-Order-Analysis-Initially-Stressed-Piezo-thermoelastic.pdf',
    'Biot1956': '../google_drive/1.1722351.pdf',
    'Chen2004': '../google_drive/B03-009__j.ijengsci.2004.04.002.pdf',
    'Das2024': '../google_drive/B01-024__P24_2024_PhysScr_Size-dependent-Effect-Interaction-Surface-Waves-Micropolar-Thermoelastic.pdf',
    'Das2025': '../google_drive/B01-032__P32_2025_EJMSOL_Fractional-Memory-Effects-Wave-Reflection-Pre-stressed-Microstructured.pdf',
    'Das2025a': '../google_drive/B02-012__P46_2026_MAMS_Hydro-thermo-electromechanical-Response-Size-dependent-Porous-Piezoelectric-Medium-Memory-dependent.pdf',
    'Das2026': '../google_drive/B02-014__P48_2026_IJMMD_Klein-Gordon-Nonlocal-Dynamics-Porous-Piezo-thermoelastic-Medium.pdf',
}

# DOI -> bibkey mapping (lowercase keys for case-insensitive matching)
DOI_TO_KEY = {
    '10.1016/j.rinp.2020.103270': 'AboDahab2020',
    '10.1108/hff-11-2025-0930': 'Aldandani2026',
    '10.1038/s41598-026-59340-x': 'Aldandani2026a',
    '10.1038/s41598-023-44339-5': 'Barak2023',
    '10.1007/s12648-022-02568-w': 'Barak2023IJP',
    '10.1080/01495739.2023.2253879': 'Barak2023JTS',
    '10.1108/mmms-10-2022-0209': 'Barak2023MMMS',
    '10.1080/15376494.2023.2211065': 'Barak2023a',
    '10.1063/1.1722351': 'Biot1956',
    '10.1016/j.ijengsci.2004.04.002': 'Chen2004',
    '10.1088/1402-4896/ad4829': 'Das2024',
    '10.1016/j.euromechsol.2024.105565': 'Das2025',
    '10.1080/15376494.2025.2516213': 'Das2025a',
    '10.1007/s10999-026-09892-7': 'Das2026',
    '10.1007/s00245-016-9365-1': 'DellOroPata2016Viscoelasticity',
    # From old atlas for completeness
    '10.1007/s10483-025-3280-7': 'Huang2025',
    '10.1007/s10409-023-23419-x': 'Yu2024',
    '10.1007/s00419-026-03092-7': 'Srivastava2026',
    '10.1007/s12648-019-01635-z': 'Abouelregal2019',
    '10.1016/j.ijheatmasstransfer.2005.10.016': 'Quintanilla2006',
    '10.1080/15397734.2020.1852088': 'Ma2020',
    '10.1108/hff-04-2022-0259': 'Gupta2023IJNMF',
    '10.1108/hff-04-2023-0208': 'Yadav2023',
}


def normalize_doi(doi):
    """Normalize DOI to lowercase for case-insensitive matching."""
    if not doi:
        return None
    return doi.lower().strip().rstrip('.,;)')


def extract_text_from_pages(pdf_path, page_indices):
    """Extract text from specific page indices (0-based)."""
    texts = {}
    try:
        reader = PdfReader(pdf_path)
        for idx in page_indices:
            if idx < len(reader.pages):
                try:
                    texts[idx] = reader.pages[idx].extract_text() or ''
                except Exception:
                    texts[idx] = ''
            else:
                texts[idx] = ''
    except Exception as e:
        print(f'ERROR reading {pdf_path}: {e}', file=sys.stderr)
    return texts


def extract_doi(page1_text):
    """Extract DOI from page 1 text."""
    m = re.search(r'10\.\d{4,}/[-._;()/:A-Za-z0-9]+', page1_text, re.IGNORECASE)
    if m:
        doi = m.group(0).strip().rstrip('.,;)')
        return doi
    return None


def clean_text(text):
    """Clean extracted text: remove excessive whitespace, control chars."""
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def get_section_text(texts_by_page, section_keywords):
    """Find text near section headers matching keywords."""
    result = []
    for idx in sorted(texts_by_page.keys()):
        text = clean_text(texts_by_page[idx])
        text_lower = text.lower()
        for kw in section_keywords:
            if kw in text_lower:
                # Find the section and grab surrounding text
                pos = text_lower.find(kw)
                start = max(0, pos - 200)
                end = min(len(text), pos + 1500)
                result.append(text[start:end])
    return ' '.join(result)


def classify_geometry(text_all):
    """Classify geometry class from text."""
    text_lower = text_all.lower()
    if 'spherical cavity' in text_lower:
        return 'sphere/cavity'
    if 'cylindrical tunnel' in text_lower:
        return 'cylinder/sphere/cavity'
    if 'cylindrical' in text_lower:
        return 'cylinder/sphere/cavity'
    if any(k in text_lower for k in ['half-space', 'half space', 'semi-infinite']):
        return 'half-space'
    if any(k in text_lower for k in ['plate', 'layer', 'slab', 'film']):
        return 'plate/layer'
    if any(k in text_lower for k in ['rod', 'bar', 'beam', 'nano-beam', 'nanobeam']):
        return 'rod/bar/beam'
    if 'interface' in text_lower:
        return 'interface'
    if 'strip' in text_lower:
        return 'strip'
    if any(k in text_lower for k in ['infinite medium', 'unbounded', 'whole space']):
        return 'infinite medium'
    return 'other'


def extract_model(text_all):
    """Extract heat-flux law model from text."""
    text_lower = text_all.lower()
    models = []
    if 'dual-phase-lag' in text_lower or 'dpl' in text_lower:
        models.append('DPL')
    if 'three-phase-lag' in text_lower or 'tpl' in text_lower:
        models.append('TPL')
    if 'memory-dependent' in text_lower or 'mdd' in text_lower:
        models.append('MDD')
    if 'fractional' in text_lower:
        models.append('fractional')
    if 'green-naghdi' in text_lower:
        models.append('GN')
    if 'lord-shulman' in text_lower:
        models.append('LS')
    if 'nonlocal' in text_lower:
        models.append('nonlocal')
    if 'moore-gibson-thompson' in text_lower or 'mgt' in text_lower:
        models.append('MGT')
    if not models:
        return '-'
    return '/'.join(models)


def extract_fields(text_all):
    """Extract coupled fields from text."""
    text_lower = text_all.lower()
    fields = []
    if 'thermo' in text_lower or 'thermal' in text_lower:
        fields.append('thermal')
    if 'elastic' in text_lower:
        fields.append('elastic')
    if 'piezo' in text_lower:
        fields.append('piezoelectric')
    if 'magnetic' in text_lower or 'magneto' in text_lower:
        fields.append('magnetic')
    if 'electric' in text_lower:
        fields.append('electric')
    if 'moisture' in text_lower or 'hygro' in text_lower:
        fields.append('moisture')
    if 'gravity' in text_lower:
        fields.append('gravity')
    if 'diffusion' in text_lower or 'diffusivity' in text_lower:
        fields.append('diffusion')
    if 'fluid' in text_lower:
        fields.append('fluid')
    if not fields:
        return '-'
    return '+'.join(fields)


def extract_bcs(text_all):
    """Extract boundary/interface conditions - one line."""
    text_lower = text_all.lower()
    bcs = []
    if 'interface condition' in text_lower:
        bcs.append('interface conditions')
    if 'boundary condition' in text_lower:
        bcs.append('boundary conditions')
    if 'free surface' in text_lower:
        bcs.append('free surface')
    if 'cavity' in text_lower:
        bcs.append('cavity boundary')
    if 'half-space' in text_lower or 'half space' in text_lower:
        bcs.append('half-space boundary')
    if not bcs:
        return '-'
    return '; '.join(bcs)[:200]


def extract_method(text_all):
    """Extract method: analytical/numerical."""
    text_lower = text_all.lower()
    methods = []
    if 'laplace' in text_lower:
        methods.append('Laplace transform')
    if 'normal mode' in text_lower:
        methods.append('normal mode analysis')
    if 'variational' in text_lower or 'reciprocity' in text_lower:
        methods.append('variational principle')
    if 'taylor' in text_lower:
        methods.append('Taylor series expansion')
    if 'analytical' in text_lower:
        methods.append('analytical')
    if 'numerical' in text_lower:
        methods.append('numerical')
    if not methods:
        return '-'
    return ', '.join(methods)


def extract_finding(texts_by_page):
    """Extract finding from abstract and conclusion sections."""
    # Look in abstract section (usually page 1)
    abstract_text = ''
    conclusion_text = ''
    
    for idx in sorted(texts_by_page.keys()):
        text = clean_text(texts_by_page[idx])
        text_lower = text.lower()
        
        # Find abstract
        if 'abstract' in text_lower and not abstract_text:
            pos = text_lower.find('abstract')
            # Skip if "abstract" appears in references or keywords
            snippet = text[pos:pos+2000]
            if len(snippet) > 100:
                abstract_text = snippet
        
        # Find conclusion
        if any(k in text_lower for k in ['conclusion', 'concluding remarks']):
            pos = -1
            for k in ['conclusion', 'concluding remarks']:
                p = text_lower.find(k)
                if p >= 0:
                    pos = p
                    break
            if pos >= 0:
                snippet = text[pos:pos+2000]
                if len(snippet) > 100:
                    conclusion_text = snippet
    
    # Try to extract a good finding sentence
    search_text = abstract_text + ' ' + conclusion_text
    if not search_text.strip():
        search_text = ' '.join(clean_text(t) for t in texts_by_page.values())
    
    # Look for finding patterns
    findings = []
    for pattern in [r'we show[^.]*\.', r'we find[^.]*\.', r'results show[^.]*\.', 
                    r'it is found[^.]*\.', r'this paper[^.]*\.', r'this study[^.]*\.',
                    r'in this paper[^.]*\.', r'in this study[^.]*\.']:
        for m in re.finditer(pattern, search_text, re.IGNORECASE):
            findings.append(m.group(0).strip())
    
    if findings:
        return findings[0][:300]
    
    # Fallback: look for sentences with key result words
    sentences = re.split(r'[.!?]+', search_text)
    for s in sentences:
        s = s.strip()
        if len(s) > 40 and any(k in s.lower() for k in ['effect', 'influence', 'impact', 'result', 'conclud', 'find', 'show', 'reveal', 'demonstrat']):
            return s[:300]
    
    return '-'


def find_evidence_page(texts_by_page, bibkey):
    """Find page number with key content - prefer abstract/conclusion pages."""
    for idx in sorted(texts_by_page.keys()):
        text = clean_text(texts_by_page[idx]).lower()
        if 'abstract' in text or 'conclusion' in text:
            return str(idx + 1)
    return '1'


def main():
    os.makedirs('atlas', exist_ok=True)

    # Read atlas_targets.csv to get ordered list
    targets = []
    with open('atlas/atlas_targets.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            targets.append(row)

    # Deduplicate by bibkey+doi, keep order
    seen = set()
    unique_targets = []
    for t in targets:
        key = (t['bibkey'], t['doi'])
        if key not in seen:
            seen.add(key)
            unique_targets.append(t)

    print(f'Total unique targets: {len(unique_targets)}')

    # Process batch 1 (first 15)
    batch1 = unique_targets[:15]
    print(f'Batch 1: {len(batch1)} targets')

    matched = []
    unmatched = []

    for t in batch1:
        bibkey = t['bibkey']
        doi = t['doi']
        pdf_filename = t['pdf_filename']

        print(f'\n--- Processing: {bibkey} | {doi} | {pdf_filename}')

        pdf_path = PDF_FILES.get(bibkey)
        if not pdf_path or not os.path.exists(pdf_path):
            print(f'  PDF not found for {bibkey}')
            unmatched.append((pdf_filename, doi, bibkey, 'PDF not found in Google Drive'))
            continue

        # Extract text from key pages: first 5 + last 3
        reader = PdfReader(pdf_path)
        num_pages = len(reader.pages)
        page_indices = list(range(min(5, num_pages)))
        if num_pages > 5:
            page_indices.extend(list(range(max(5, num_pages - 3), num_pages)))
        # Remove duplicates while preserving order
        page_indices = list(dict.fromkeys(page_indices))

        texts = extract_text_from_pages(pdf_path, page_indices)

        page1_text = texts.get(0, '')
        all_text = ' '.join(texts.values())

        # Extract DOI from page 1
        extracted_doi = extract_doi(page1_text)
        norm_doi = normalize_doi(extracted_doi)
        print(f'  Extracted DOI: {extracted_doi} (normalized: {norm_doi})')

        # Match DOI to bibkey (case-insensitive)
        matched_bibkey = None
        if norm_doi and norm_doi in DOI_TO_KEY:
            matched_bibkey = DOI_TO_KEY[norm_doi]

        if not matched_bibkey:
            print(f'  DOI not matched to any bib key')
            unmatched.append((pdf_filename, extracted_doi or '-', bibkey, 'DOI not found in bib'))
            continue

        print(f'  Matched to: {matched_bibkey}')

        # Extract fields
        geometry_class = classify_geometry(all_text)
        model = extract_model(all_text)
        fields = extract_fields(all_text)
        bcs = extract_bcs(all_text)
        method = extract_method(all_text)
        finding = extract_finding(texts)
        evidence_page = find_evidence_page(texts, bibkey)

        matched.append((matched_bibkey, geometry_class, model, fields, bcs, method, finding, evidence_page, pdf_filename, extracted_doi))

        print(f'    geometry: {geometry_class}')
        print(f'    model: {model}')
        print(f'    fields: {fields}')
        print(f'    bcs: {bcs}')
        print(f'    method: {method}')
        print(f'    finding: {finding[:150]}...' if len(finding) > 150 else f'    finding: {finding}')
        print(f'    evidence_page: {evidence_page}')

    # Write atlas_batch1.csv (ONLY matched papers)
    atlas_path = 'atlas/atlas_batch1.csv'
    with open(atlas_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['bibkey', 'geometry_class', 'model', 'fields', 'bcs', 'method', 'finding', 'evidence_page'])
        for row in matched:
            writer.writerow(row[:8])
    print(f'\natlas_batch1.csv written: {len(matched)} matched rows')

    # Write MATCH_REPORT_batch1.csv
    report_path = 'atlas/MATCH_REPORT_batch1.csv'
    with open(report_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['pdf_filename', 'extracted_doi', 'matched_bibkey', 'reason'])
        matched_pdfs = {row[8] for row in matched}
        for row in matched:
            writer.writerow([row[8], row[9], row[0], 'DOI matched to bib key'])
        for row in unmatched:
            writer.writerow([row[0], row[1], 'unmatched', row[3]])
    print(f'MATCH_REPORT_batch1.csv written: {len(matched) + len(unmatched)} rows')

    # Print summary
    print(f'\n=== BATCH 1 SUMMARY ===')
    print(f'Total targets: {len(batch1)}')
    print(f'Matched: {len(matched)}')
    print(f'Unmatched: {len(unmatched)}')


if __name__ == '__main__':
    main()