#!/usr/bin/env python3
"""Update ARENA_SUMMARY.tex with new atlas metrics and regenerate s16b_atlas.tex.
ASCII only output.
"""
import csv
import re
import os


def esc(s):
    """Escape LaTeX special characters."""
    s = s.replace('&', '\\&')
    s = s.replace('%', '\\%')
    s = s.replace('$', '\\$')
    s = s.replace('#', '\\#')
    s = s.replace('_', '\\_')
    s = s.replace('\\', '\\textbackslash{}')
    return s


def main():
    # Read atlas.csv
    rows = []
    with open('atlas/atlas.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    print(f'Atlas rows: {len(rows)}')

    # Read MATCH_REPORT.csv
    report_rows = []
    with open('atlas/MATCH_REPORT.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            report_rows.append(row)

    print(f'Report rows: {len(report_rows)}')

    matched_count = len(rows)
    unmatched_count = sum(1 for r in report_rows if r['matched_bibkey'] == 'unmatched')
    total_count = len(report_rows)
    print(f'Matched: {matched_count}, Unmatched: {unmatched_count}, Total: {total_count}')

    # Generate s16b_atlas.tex
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
        for row in sorted(rows, key=lambda r: r['bibkey']):
            finding = esc(row['finding'])
            geometry = esc(row['geometry_class'])
            model = esc(row['model'])
            fields = esc(row['fields'])
            f.write(row['bibkey'] + ' & ' + geometry + ' & ' + model + ' & ' + fields + ' & ' + finding + ' \\\\\n')
        f.write('\\end{longtable}\n')
    print(tex_path + ' written')

    # Update ARENA_SUMMARY.tex
    tex_file = 'ARENA_SUMMARY.tex'
    with open(tex_file, 'r') as f:
        content = f.read()

    # Build new metrics table
    new_table = ('\\begin{tabularx}{\\textwidth}{@{}lX@{}}\n'
                 '\\toprule\n'
                 '\\textbf{Metric} & \\textbf{Value} \\\\\n'
                 '\\midrule\n'
                 'PDFs given (from Google Drive, batches 1+) & ' + str(total_count) + ' \\\\\n'
                 'Matched (page-1 DOI found in bib) & ' + str(matched_count) + ' \\\\\n'
                 'Skipped / unmatched (DOI not in bib, no DOI on page 1, or PDF not in Drive) & ' + str(unmatched_count) + ' \\\\\n'
                 'Atlas CSV & {\\tt atlas/atlas.csv} \\\\\n'
                 'Match report & {\\tt atlas/MATCH\\_REPORT.csv} \\\\\n'
                 'LaTeX section & {\\tt sections/s16b\\_atlas.tex} (table, not yet \\\\input in main.tex) \\\\\n'
                 '\\midrule\n'
                 '\\end{tabularx}')

    old_table = ('\\begin{tabularx}{\\textwidth}{@{}lX@{}}\n'
                 '\\toprule\n'
                 '\\textbf{Metric} & \\textbf{Value} \\\\\n'
                 '\\midrule\n'
                 'PDFs given (from Google Drive, batches 1+) & 41 \\\\\n'
                 'Matched (page-1 DOI found in bib) & 22 \\\\\n'
                 'Skipped / unmatched (DOI not in bib, no DOI on page 1, or PDF not in Drive) & 19 \\\\\n'
                 'Atlas CSV & {\\tt atlas/atlas.csv} \\\\\n'
                 'Match report & {\\tt atlas/MATCH\\_REPORT.csv} \\\\\n'
                 'LaTeX section & {\\tt sections/s16b\\_atlas.tex} (table, not yet \\\\input in main.tex) \\\\\n'
                 '\\midrule\n'
                 '\\end{tabularx}')

    if old_table in content:
        content = content.replace(old_table, new_table)
        print('Replaced metrics table')
    else:
        print('WARNING: Could not find old metrics table')

    # Build new bib keys list
    matched_bibkeys = sorted([r['bibkey'] for r in rows])
    new_keys = 'All matched bib keys: ' + ', '.join(matched_bibkeys) + '.'

    old_keys = ('Batch 1 matched bib keys: AboDahab2020, Aldandani2026, Aldandani2026a, '
                'Barak2023, Barak2023IJP, Barak2023JTS, Barak2023MMMS, Barak2023a, '
                'Biot1956, Chen2004, Das2024, Das2025, Das2025a, Das2026.\n'
                'Batch 1 unmatched: DellOroPata2016Viscoelasticity (PDF not found in Google Drive).\n'
                'All matched bib keys: AboDahab2020, Abouelregal2019, Aldandani2026, '
                'Aldandani2026a, Barak2023, Barak2023IJP, Barak2023JTS, Barak2023MMMS, '
                'Barak2023a, Biot1956, Chen2004, Das2024, Das2025, Das2025a, Das2026, '
                'Gupta2023IJNMF, Huang2025, Ma2020, Quintanilla2006, Srivastava2026, '
                'Yadav2023, Yu2024.')

    if old_keys in content:
        content = content.replace(old_keys, new_keys)
        print('Replaced bib keys list')
    else:
        print('WARNING: Could not find old bib keys list')

    # Build new unmatched PDFs list
    unmatched_pdfs = sorted([r['pdf_filename'] for r in report_rows if r['matched_bibkey'] == 'unmatched'])
    new_unmatched = 'Unmatched PDFs: ' + ', '.join(unmatched_pdfs) + '.'

    old_unmatched = ('Old unmatched PDFs: B10-023, B10-022, B10-021, B10-020, B04-005, '
                     'B10-001, 2026-10\\_QP\\_131181\\_Set-B, B11-012, B11-010, B11-011, '
                     'B11-009, B11-007, B11-006, B11-005, B11-004, B11-003, B11-002, B11-001.\n'
                     'Batch 1 unmatched: 10.1007@s00245-016-9365-1.pdf (DellOroPata2016Viscoelasticity, PDF not in Drive).')

    if old_unmatched in content:
        content = content.replace(old_unmatched, new_unmatched)
        print('Replaced unmatched PDFs list')
    else:
        print('WARNING: Could not find old unmatched list')

    with open(tex_file, 'w') as f:
        f.write(content)
    print('ARENA_SUMMARY.tex updated')


if __name__ == '__main__':
    main()