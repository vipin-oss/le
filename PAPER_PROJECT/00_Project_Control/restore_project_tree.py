#!/usr/bin/env python3
"""restore_project_tree.py — rebuild a runnable project layout from the reproducibility archive.

The archive is organised for reading (01_PROGRAM, 03_DATA, ...), but the shipped code resolves paths
against the project layout it was written in (`PAPER_PROJECT/09_Raw_Data/...`, `tools/`,
`work/handoff/...`). This script replays `09_ARCHIVE_METADATA/file_manifest_sha256.csv`: every archived
file is copied back to the `source_path` recorded there, after verifying its sha256. There is no second
mapping table, on purpose — the manifest is the single source of truth for what came from where, so the
restorer cannot drift out of sync with the packager.

Usage
    python3 01_PROGRAM/restore_project_tree.py --into ../run-here
    cd ../run-here && sh bootstrap_paths.sh

Options
    --into DIR     destination for the restored tree (default: current directory)
    --only PREFIX  restore a subtree, e.g. --only PAPER_PROJECT/09_Raw_Data
    --list         print the mapping without copying anything

What a restored tree is not: it is not a git checkout (no `.git`), and it cannot contain files the
project never tracked — the 600-dpi/TIFF figure renditions and the generated archives under
`PAPER_PROJECT/packages/`. Each regenerates in one command; see `RUN_ORDER.md` and
`FIGURE_PROVENANCE.md`.
"""
import argparse
import csv
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARCH = os.path.abspath(os.path.join(HERE, '..'))
MAN_REL = os.path.join('09_ARCHIVE_METADATA', 'file_manifest_sha256.csv')

# things the archive carries for documentation but that must not be "restored" into a runnable tree
SKIP_DIR_PARTS = {'packages', '__pycache__', '.pytest_cache'}
SKIP_TOP = {'16_Reproducibility'}


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for c in iter(lambda: fh.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


def manifest_path():
    for cand in (os.path.join(ARCH, MAN_REL), os.path.join(HERE, MAN_REL),
                 os.path.join(os.getcwd(), ARCHIVE_ROOT_NAME, MAN_REL)):
        if os.path.isfile(cand):
            return cand
    sys.exit('cannot find ' + MAN_REL + ' next to this script; run it from inside the extracted archive')


ARCHIVE_ROOT_NAME = 'PAPER_PROJECT_COMPLETE_REPRODUCIBILITY_ARCHIVE'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--into', default='.')
    ap.add_argument('--only', default='')
    ap.add_argument('--list', action='store_true')
    a = ap.parse_args()
    man = manifest_path()
    rows = list(csv.DictReader(open(man, encoding='utf-8')))
    dest = os.path.abspath(a.into)
    n = skip = bad = 0
    for row in rows:
        arc, src, want = row['archive_path'], row['source_path'], row['sha256']
        parts = src.split('/')
        if SKIP_DIR_PARTS & set(parts) or (parts and parts[0] in SKIP_TOP) or '16_Reproducibility' in parts:
            skip += 1
            continue
        if a.only and not src.startswith(a.only):
            continue
        s = os.path.join(os.path.dirname(os.path.dirname(man)), arc) if not arc.startswith(ARCHIVE_ROOT_NAME) \
            else os.path.join(os.path.dirname(os.path.dirname(man)), arc.split('/', 1)[1])
        if not os.path.isfile(s):
            continue
        if sha256(s) != want:
            print('HASH MISMATCH (the archive is not intact):', arc)
            bad += 1
            continue
        if a.list:
            print(f'{arc}  ->  {src}')
            n += 1
            continue
        d = os.path.join(dest, src)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        shutil.copy2(s, d)
        n += 1
    if a.list:
        print(f'{n} files would be restored; {skip} documentation-only entries skipped; {bad} hash mismatches')
        return 0 if not bad else 1
    print(f'restored {n} files into {dest} ({skip} documentation-only entries skipped, {bad} hash mismatches)')
    if not bad:
        print('next: cd %s && sh bootstrap_paths.sh && python3 PAPER_PROJECT/13_Manuscript/'
              'build_manuscript.py -c' % dest)
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
