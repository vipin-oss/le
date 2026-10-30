#!/usr/bin/env python3
"""Update ARENA_SUMMARY.tex section 7 with latest atlas metrics.
ASCII only output.
"""
import csv
import os


def main():
    # Read atlas.csv
    matched_bibkeys = []
    with open('atlas/atlas.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            matched_bibkeys.append(row['bibkey'])

    # Read MATCH_REPORT.csv
    unmatched_pdfs = []
    with open('atlas/MATCH_REPORT.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['matched_bibkey'] == 'unmatched':
                unmatched_pdfs.append(row['pdf_filename'])

    matched_count = len(matched_bibkeys)
    unmatched_count = len(unmatched_pdfs)
    total_count = matched_count + unmatched_count

    print(f'Matched: {matched_count}, Unmatched: {unmatched_count}, Total: {total_count}')

    # Read ARENA_SUMMARY.tex
    with open('ARENA_SUMMARY.tex', 'r') as f:
        content = f.read()

    # Build new metrics table
    new_table = ('\\begin{tabularx}{\\textwidth}{@{}lX@{}}\n'
                 '\\toprule\n'
                 '\\textbf{Metric} & \\textbf{Value} \\\\\n'
                 '\\midrule\n'
                 'PDFs given (from Google Drive, batches 1-3) & ' + str(total_count) + ' \\\\\n'
                 'Matched (page-1 DOI found in bib) & ' + str(matched_count) + ' \\\\\n'
                 'Skipped / unmatched (DOI not in bib, no DOI on page 1, or PDF not in Drive) & ' + str(unmatched_count) + ' \\\\\n'
                 'Atlas CSV & {\\tt atlas/atlas.csv} \\\\\n'
                 'Match report & {\\tt atlas/MATCH\\_REPORT.csv} \\\\\n'
                 'LaTeX section & {\\tt sections/s16b\\_atlas.tex} (table, not yet \\\\input in main.tex) \\\\\n'
                 '\\midrule\n'
                 '\\end{tabularx}')

    # Replace the metrics table - find between \begin{tabularx} and \end{tabularx} in section 7
    import re
    # Find the section 7 tabularx
    start_marker = '\\begin{tabularx}{\\textwidth}{@{}lX@{}}\n\\toprule\n\\textbf{Metric}'
    end_marker = '\\end{tabularx}'
    start_idx = content.find(start_marker)
    if start_idx >= 0:
        end_idx = content.find(end_marker, start_idx)
        if end_idx >= 0:
            end_idx += len(end_marker)
            content = content[:start_idx] + new_table + content[end_idx:]
            print('Replaced metrics table')
        else:
            print('WARNING: Could not find end of table')
    else:
        print('WARNING: Could not find start of table')

    # Replace bib keys list
    new_keys = 'All matched bib keys: ' + ', '.join(sorted(matched_bibkeys)) + '.'
    start_idx = content.find('All matched bib keys:')
    if start_idx >= 0:
        end_idx = content.find('\n', start_idx)
        if end_idx >= 0:
            content = content[:start_idx] + new_keys + content[end_idx:]
            print('Replaced bib keys list')
        else:
            content = content[:start_idx] + new_keys
            print('Replaced bib keys list (end of file)')
    else:
        print('WARNING: Could not find bib keys list')

    # Replace unmatched PDFs list
    new_unmatched = 'Unmatched PDFs: ' + ', '.join(sorted(unmatched_pdfs)) + '.'
    start_idx = content.find('Unmatched PDFs:')
    if start_idx >= 0:
        end_idx = content.find('\n', start_idx)
        if end_idx >= 0:
            content = content[:start_idx] + new_unmatched + content[end_idx:]
            print('Replaced unmatched PDFs list')
        else:
            content = content[:start_idx] + new_unmatched
            print('Replaced unmatched PDFs list (end of file)')
    else:
        print('WARNING: Could not find unmatched PDFs list')

    with open('ARENA_SUMMARY.tex', 'w') as f:
        f.write(content)
    print('ARENA_SUMMARY.tex updated')


if __name__ == '__main__':
    main()