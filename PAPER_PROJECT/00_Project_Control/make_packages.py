"""make_packages.py — cumulative packages PACKAGE_PHASE_07 … 13 (MASTER_PROMPT §67) and RESEARCH_PROJECT_FINAL.zip (§74).
Packages are RECONSTRUCTED at the end of the session from the final versions of the files that belong to phases <= N (the per-phase states were not
snapshotted when the phases ended); each zip contains a MANIFEST.json with SHA-256 per file.  Raw .npz data only in PACKAGE_PHASE_13 / FINAL."""
import os, sys, zipfile, hashlib, json, time
ROOT = '/home/user/PAPER_PROJECT'; PK = os.path.join(ROOT, 'packages'); os.makedirs(PK, exist_ok=True)
def files_under(rel, exts=None, skip=('__pycache__', '_claims', 'equations')):
    out = []
    for r, ds, fs in os.walk(os.path.join(ROOT, rel)):
        ds[:] = [d for d in ds if d not in skip]
        for f in fs:
            if exts and not f.endswith(exts): continue
            out.append(os.path.join(r, f))
    return out
CORE = ['00_Project_Control', '01_Literature', '02_Problem_Definition', '04_Theory', '05_Numerical_Method', '06_Source_Code', '07_Tests', '03_Validation', '14_Documentation']
def collect(n):
    fl = []
    for d in CORE:
        if d == '05_Numerical_Method' and n < 9: fl += [f for f in files_under(d) if 'NUMERICAL_METHOD_V2' in f]; continue
        if d == '03_Validation' and n < 8: continue
        if d == '14_Documentation' and n < 12: continue
        fl += files_under(d)
    fl += files_under('15_Audits')
    if n >= 9: fl += files_under('08_Experiments', ('.py', '.log', '.md')); fl += files_under('10_Processed_Data', ('.json', '.csv', '.md')) if n >= 11 else []
    if n >= 9: fl += files_under('09_Raw_Data/convergence', ('.json',)) + files_under('09_Raw_Data/convergence_gamma3p5', ('.json',))
    if n >= 11: fl += files_under('09_Raw_Data/production', ('.json',))
    if n >= 12: fl += files_under('11_Figures') + files_under('12_Tables')
    if n >= 13: fl += files_under('13_Manuscript', ('.docx', '.md', '.xlsx', '.txt', '.json', '.py', '.png')) + files_under('09_Raw_Data', ('.npz',))
    return sorted(set(f for f in fl if os.path.isfile(f) and '/packages/' not in f))
def build(zname, fl, note):
    man = {f[len(ROOT) + 1:]: hashlib.sha256(open(f, 'rb').read()).hexdigest() for f in fl}
    with zipfile.ZipFile(os.path.join(PK, zname), 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('MANIFEST.json', json.dumps(dict(created=time.strftime('%Y-%m-%dT%H:%M:%S'), note=note, n_files=len(man), sha256=man), indent=1))
        for f in fl: z.write(f, f[len(ROOT) + 1:])
    return os.path.getsize(os.path.join(PK, zname)), len(fl)
note = 'reconstructed at the end of the session from final versions of files belonging to phases <= N (MASTER_PROMPT §67/§68)'
for n in range(7, 14):
    sz, nf = build(f'PACKAGE_PHASE_{n:02d}.zip', collect(n) if n < 13 else collect(13), note)
    print(f'PACKAGE_PHASE_{n:02d}.zip: {nf} files, {sz/1e6:.2f} MB')
if len(sys.argv) > 1 and sys.argv[1] == 'final':
    full = []
    for r, ds, fs in os.walk(ROOT):
        ds[:] = [d for d in ds if d not in ('packages', '__pycache__', '_claims')]
        for f in fs: full.append(os.path.join(r, f))
    sz, nf = build('RESEARCH_PROJECT_FINAL.zip', sorted(full), 'final archive: whole PAPER_PROJECT (without packages/); see README.md')
    print(f'RESEARCH_PROJECT_FINAL.zip: {nf} files, {sz/1e6:.2f} MB')
