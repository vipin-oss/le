"""run_production_v2.py — Phase 11 production (v2).  Usage:  python run_production_v2.py heavy|light
'heavy' worker takes heavy jobs first (192x96 / 96x144; one at a time, 0.7-0.9 GB) and then helps with the rest;
'light' worker takes medium and light jobs only.  Jobs are claimed atomically (mkdir) so workers never duplicate work.
Cached results are skipped."""
import sys, os, json, time
sys.dont_write_bytecode = True
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import numpy as np
import production_matrix as pm
import cg_pipeline as cp

RAW = os.path.join(ROOT, '09_Raw_Data', 'production'); CLAIMS = os.path.join(RAW, '_claims')
os.makedirs(CLAIMS, exist_ok=True)
which = sys.argv[1] if len(sys.argv) > 1 else 'light'
J = pm.matrix()
order = {'heavy': 0, 'medium': 1, 'light': 2}
if which == 'heavy':
    J.sort(key=lambda j: order[j['cost']])
else:
    J = [j for j in J if j['cost'] != 'heavy']; J.sort(key=lambda j: order[j['cost']])
t0 = time.time(); cpu0 = time.process_time(); done = 0
for j in J:
    tag = j['tag']
    if os.path.exists(os.path.join(RAW, tag + '.json')):
        continue
    try:
        os.mkdir(os.path.join(CLAIMS, tag))
    except FileExistsError:
        continue
    kw = {k: j[k] for k in ('iso', 'energy_coupling', 'inertia_scale', 'variant', 'pulse') if k in j}
    q = cp.run_config(tag, j['model'], j['tau_ps'], j['chi'], j['phi'], j['a'], outdir=RAW, Nr=j['Nr'], Nt=j['Nt'], quiet=True, **kw)
    jp = os.path.join(RAW, tag + '.json'); d = json.load(open(jp)); d['block'] = j['block']; d['grid'] = j['grid']; json.dump(d, open(jp, 'w'), indent=1)
    done += 1
    print(f"[{which}] {tag}: sig_interp={q['sig_interp']:.6e} nodal={q['sig_nodal']:.6e} t*={q['t_star']:.3f} wall_err={q['wall_pulse_err']:.1e} "
          f"back={q['back_max']:.1e} ({q['wall_s']:.0f}s) [{done} new, elapsed {time.time()-t0:.0f}s]", flush=True)
print(f'PRODUCTION {which} DONE: {done} new runs, cpu {time.process_time()-cpu0:.0f}s wall {time.time()-t0:.0f}s')
