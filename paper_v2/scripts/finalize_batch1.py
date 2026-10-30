#!/usr/bin/env python3
"""Clean batch1 output, fix non-ASCII/hyphenation, merge with old atlas,
generate final atlas.csv, MATCH_REPORT.csv, and s16b_atlas.tex.
ASCII only output.
"""
import csv
import os
import re
import sys
from pypdf import PdfReader


def clean_ascii(text):
    """Replace non-ASCII chars and fix PDF hyphenation artifacts."""
    if not text:
        return '-'
    # Replace en-dash/em-dash with hyphen
    text = text.replace('\u2013', '-').replace('\u2014', '-')
    text = text.replace('\u2019', "'").replace('\u2018', "'")
    text = text.replace('\u201c', '"').replace('\u201d', '"')
    # Fix hyphenated line breaks from PDF extraction
    text = re.sub(r'(\w)- (\w)', r'\1\2', text)  # "non- local" -> "nonlocal"
    text = re.sub(r'-\n', '', text)
    # Remove any remaining non-ASCII
    text = ''.join(c if ord(c) < 128 else '-' for c in text)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text if text else '-'


def read_csv(path):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def extract_better_finding(pdf_path, bibkey):
    """Re-extract finding from abstract and conclusion sections of a specific PDF."""
    try:
        reader = PdfReader(pdf_path)
        num_pages = len(reader.pages)
        # Read first 3 pages + last 3 pages
        page_indices = list(range(min(3, num_pages)))
        if num_pages > 3:
            page_indices.extend(list(range(max(3, num_pages - 3), num_pages)))
        page_indices = list(dict.fromkeys(page_indices))
        
        all_text = ''
        for idx in page_indices:
            try:
                t = reader.pages[idx].extract_text() or ''
                all_text += t + '\n'
            except Exception:
                pass
        
        all_text = clean_ascii(all_text)
        text_lower = all_text.lower()
        
        # Find abstract section
        abstract_text = ''
        for kw in ['abstract']:
            pos = text_lower.find(kw)
            if pos >= 0:
                abstract_text = all_text[pos:pos+1500]
                break
        
        # Find conclusion section
        conclusion_text = ''
        for kw in ['conclusion', 'concluding remarks']:
            pos = text_lower.find(kw)
            if pos >= 0:
                conclusion_text = all_text[pos:pos+1500]
                break
        
        search_text = abstract_text + ' ' + conclusion_text
        if not search_text.strip():
            search_text = all_text
        
        # Look for finding patterns
        findings = []
        for pattern in [r'we show[^.]*\.', r'we find[^.]*\.', r'results show[^.]*\.',
                        r'it is found[^.]*\.', r'this paper[^.]*\.', r'this study[^.]*\.',
                        r'in this paper[^.]*\.', r'in this study[^.]*\.',
                        r'the results[^.]*\.', r'findings show[^.]*\.']:
            for m in re.finditer(pattern, search_text, re.IGNORECASE):
                findings.append(m.group(0).strip())
        
        if findings:
            return clean_ascii(findings[0])[:300]
        
        # Fallback: sentences with result words
        sentences = re.split(r'[.!?]+', search_text)
        for s in sentences:
            s = s.strip()
            if len(s) > 40 and any(k in s.lower() for k in ['effect', 'influence', 'impact', 'result', 'conclud', 'find', 'show', 'reveal', 'demonstrat']):
                return clean_ascii(s)[:300]
        
        return '-'
    except Exception as e:
        print(f'Error re-extracting finding for {bibkey}: {e}', file=sys.stderr)
        return '-'


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


def main():
    # Read batch1 CSV
    batch1_rows = read_csv('atlas/atlas_batch1.csv')
    report_rows = read_csv('atlas/MATCH_REPORT_batch1.csv')
    
    # Clean batch1 rows: fix non-ASCII, hyphenation, improve weak findings
    for row in batch1_rows:
        bibkey = row['bibkey']
        
        # Clean all fields
        row['geometry_class'] = clean_ascii(row.get('geometry_class', ''))
        row['model'] = clean_ascii(row.get('model', ''))
        row['fields'] = clean_ascii(row.get('fields', ''))
        row['bcs'] = clean_ascii(row.get('bcs', ''))
        row['method'] = clean_ascii(row.get('method', ''))
        row['finding'] = clean_ascii(row.get('finding', ''))
        row['evidence_page'] = clean_ascii(row.get('evidence_page', ''))
        
        # Improve weak findings
        finding = row['finding']
        if finding == '-' or finding == 'this paper.' or len(finding) < 20:
            pdf_path = PDF_FILES.get(bibkey)
            if pdf_path and os.path.exists(pdf_path):
                better = extract_better_finding(pdf_path, bibkey)
                if better and better != '-' and len(better) > len(finding):
                    row['finding'] = better
                    print(f'Improved finding for {bibkey}: {better[:100]}...')
    
    # Read old atlas
    old_atlas = read_csv('atlas/atlas.csv')
    old_report = read_csv('atlas/MATCH_REPORT.csv')
    
    # Merge old + batch1 atlas (avoid duplicates by bibkey)
    merged_atlas = {}
    for row in old_atlas:
        merged_atlas[row['bibkey']] = row
    for row in batch1_rows:
        merged_atlas[row['bibkey']] = row
    
    # Write final atlas.csv (sorted by bibkey for consistency)
    atlas_path = 'atlas/atlas.csv'
    with open(atlas_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['bibkey', 'geometry_class', 'model', 'fields', 'bcs', 'method', 'finding', 'evidence_page'])
        for bibkey in sorted(merged_atlas.keys()):
            row = merged_atlas[bibkey]
            writer.writerow([
                row['bibkey'], row['geometry_class'], row['model'], row['fields'],
                row['bcs'], row['method'], row['finding'], row['evidence_page']
            ])
    print(f'\natlas.csv written: {len(merged_atlas)} total matched rows')
    
    # Merge MATCH_REPORT (old + batch1)
    merged_report = {}
    for row in old_report:
        merged_report[row['pdf_filename']] = row
    for row in report_rows:
        merged_report[row['pdf_filename']] = row
    
    report_path = 'atlas/MATCH_REPORT.csv'
    with open(report_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['pdf_filename', 'extracted_doi', 'matched_bibkey', 'reason'])
        for pdf in sorted(merged_report.keys()):
            row = merged_report[pdf]
            writer.writerow([row['pdf_filename'], row['extracted_doi'], row['matched_bibkey'], row['reason']])
    print(f'MATCH_REPORT.csv written: {len(merged_report)} total rows')
    
    # Generate s16b_atlas.tex longtable
    tex_path = 'sections/s16b_atlas.tex'
    with open(tex_path, 'w') as f:
        f.write('% Atlas of matched thermoelasticity papers from batch processing\n')
        f.write('% Geometry class id | Model | Fields | Finding\n')
        f.write('\\begin{longtable}{p{2.2cm}p{2.0cm}p{2.6cm}p{3.2cm}p{3.0cm}}\n')
        f.write('\\caption{Atlas of matched thermoelasticity papers: geometry class, model, fields, finding.}\\\\\n')
        f.write('\\toprule\n')
        f.write('Ref & Geometry class id & Model & Fields & Finding \\\\\n')
        f.write('\\midrule\n')
        f.write('\\endfirsthead\n')
        f.write('\\toprule\n')
        f.write('Ref & Geometry class id & Model & Fields & Finding \\\\\n')
        f.write('\\midrule\n')
        f.write('\\endhead\n')
        f.write('\\bottomrule\n')
        f.write('\\endfoot\n')
        
        for bibkey in sorted(merged_atlas.keys()):
            row = merged_atlas[bibkey]
            # Escape LaTeX special chars in finding
            finding = row['finding'].replace('&', '\\&').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#').replace('_', '\\_')
            finding = finding.replace('\\', '\\textbackslash{}')
            geometry = row['geometry_class'].replace('&', '\\&').replace('%', '\\%')
            model = row['model'].replace('&', '\\&').replace('%', '\\%')
            fields = row['fields'].replace('&', '\\&').replace('%', '\\%')
            f.write(f'{bibkey} & {geometry} & {model} & {fields} & {finding} \\\\\n')
        
        f.write('\\end{longtable}\n')
    print(f's16b_atlas.tex written')
    
    # Print summary
    matched_count = len(merged_atlas)
    unmatched_count = sum(1 for r in merged_report.values() if r['matched_bibkey'] == 'unmatched')
    total = len(merged_report)
    print(f'\n=== FINAL SUMMARY ===')
    print(f'Total PDFs processed: {total}')
    print(f'Matched: {matched_count}')
    print(f'Unmatched: {unmatched_count}')
    print(f'\nAll bib keys:')
    for bibkey in sorted(merged_atlas.keys()):
        row = merged_atlas[bibkey]
        print(f'  {bibkey}: geometry={row["geometry_class"]}, model={row["model"]}, page={row["evidence_page"]}')
    
    # Verify ASCII only
    for path in [atlas_path, report_path, tex_path]:
        with open(path, 'r') as f:
            content = f.read()
        non_ascii = [c for c in content if ord(c) > 127]
        if non_ascii:
            print(f'\nWARNING: {path} has non-ASCII characters: {set(non_ascii)}')
        else:
            print(f'{path}: ASCII only OK')


if __name__ == '__main__':
    main()