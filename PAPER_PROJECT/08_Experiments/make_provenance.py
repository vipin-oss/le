"""make_provenance.py — run-level provenance table (MASTER_PROMPT §45): RUN_ID, code version, input checksum, reference-data version, environment, output location."""
import os, sys, json, glob, hashlib, csv, platform
sys.dont_write_bytecode = True
def _pp_root(_start):
    """walk up from _start to the PAPER_PROJECT directory (path-independent replacement
    for the hard-coded '/home/user/PAPER_PROJECT' that used to be here)."""
    _p = os.path.abspath(_start)
    while True:
        if os.path.basename(_p) == 'PAPER_PROJECT':
            return _p
        _q = os.path.dirname(_p)
        if _q == _p:
            break
        _p = _q
    return os.environ.get('PAPER_PROJECT_ROOT', '/home/user/PAPER_PROJECT')
ROOT = _pp_root(os.path.dirname(os.path.abspath(__file__)))
def sha(path): return hashlib.sha256(open(path, 'rb').read()).hexdigest()
freeze = os.path.join(ROOT, '06_Source_Code', 'CODE_FREEZE_v2_gate.json'); freeze_f = os.path.join(ROOT, '06_Source_Code', 'CODE_FREEZE_v2_blockF.json')
code_v = sha(freeze)[:16]; code_vf = sha(freeze_f)[:16] if os.path.exists(freeze_f) else ''
refdata_v = sha(os.path.join(ROOT, '06_Source_Code', 'src', 'cg_model.py'))[:16]
env = f"Python {sys.version.split()[0]}; numpy/scipy as in CODE_FREEZE; {platform.platform()}"
rows = []
for jp in sorted(glob.glob(os.path.join(ROOT, '09_Raw_Data', 'production', '*.json'))):
    q = json.load(open(jp)); tag = q['tag']
    cfg = {k: q.get(k) for k in ('model', 'tau_ps', 'chi', 'phi', 'a_nm', 'iso', 'coupled', 'energy_coupling', 'inertia_scale', 'Nr', 'Nt', 'Rfac', 'gamma_grid', 'variant', 'pulse_t0_tw', 'plan')}
    inp = hashlib.sha256(json.dumps(cfg, sort_keys=True, default=str).encode()).hexdigest()[:16]
    npz = jp.replace('.json', '.npz')
    rows.append([tag, q.get('block'), 'RUN_SUCCESS', (code_vf if q.get('block') == 'F' else code_v), inp, refdata_v, env, os.path.relpath(npz, ROOT), sha(npz)[:16], f"{q.get('wall_s', 0):.0f}", q.get('n_solves'), q.get('back_max'), q.get('wall_pulse_err')])
out = os.path.join(ROOT, '10_Processed_Data', 'PRODUCTION_PROVENANCE.csv')
with open(out, 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['RUN_ID', 'block', 'status', 'CODE_VERSION(freeze sha256[:16])', 'INPUT_CHECKSUM', 'REFERENCE_DATA_VERSION(cg_model sha256[:16])', 'ENVIRONMENT_VERSION', 'OUTPUT_LOCATION', 'OUTPUT_SHA256[:16]', 'wall_s', 'n_solves', 'backward_err', 'wall_pulse_err']); w.writerows(rows)
print('provenance rows:', len(rows), '->', out)
