"""build_supplement.py — SUPPLEMENTARY_TABLES.xlsx (openpyxl) from the analysis outputs/tables; and cover_letter.md."""
import os, sys, json, csv, glob
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
ROOT = _pp_root(os.path.dirname(os.path.abspath(__file__))); MS = os.path.join(ROOT, '13_Manuscript')
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
def J(p):
    p = os.path.join(ROOT, p); return json.load(open(p)) if os.path.exists(p) else {}
TR = J('07_Tests/TEST_RESULTS.json'); AN = J('10_Processed_Data/ANALYSIS_V2.json')
wb = Workbook(); ws = wb.active; ws.title = 'README'
for r in [['SUPPLEMENTARY TABLES — verified continuum study of cavity thermoelasticity in monoclinic β-Ga2O3'], ['All values are computed by the scripts in the data package from stored raw outputs; stresses are Pa per K of wall-temperature amplitude.'],
          ['Sheets: Verification (all tests), PhiSweep_ellipse, Convergence_6phi, D_lambda_eps, Ablations, Parameters, Production_runs'], ['Status: verification only; physical validation APPLICABLE — EVIDENCE_UNAVAILABLE.']]:
    ws.append(r)
ws['A1'].font = Font(bold=True, size=12)
def sheet(name, header, rows):
    w = wb.create_sheet(name); w.append(header)
    for c in w[1]: c.font = Font(bold=True); c.fill = PatternFill('solid', fgColor='E7E6E6')
    for r in rows: w.append(r)
    for col in w.columns: w.column_dimensions[col[0].column_letter].width = min(60, max(10, max(len(str(c.value)) if c.value is not None else 0 for c in col[:30]) + 2))
sheet('Verification', ['test', 'status', 'criterion', 'values'], [[c['case'], c['status'], str(c.get('criterion', c.get('note', '')))[:400], '; '.join(f'{k}={v}' for k, v in c.items() if k not in ('case', 'status', 'criterion', 'note', 'plan'))[:600]] for c in TR.get('cases', [])])
for csvname, sh in (('phi_sweep_ellipse.csv', 'PhiSweep_ellipse'), ('convergence_ellipse_6phi.csv', 'Convergence_6phi'), ('D_lambda_eps.csv', 'D_lambda_eps'), ('ablations_E.csv', 'Ablations')):
    p = os.path.join(ROOT, '12_Tables', csvname)
    if os.path.exists(p):
        rows = list(csv.reader(open(p))); sheet(sh, rows[0], [[float(x) if x.replace('.', '', 1).replace('e', '', 1).replace('-', '', 2).replace('+', '', 1).isdigit() else x for x in r] for r in rows[1:]])
sheet('Parameters', ['parameter', 'value', 'class', 'source'], [
    ['C_ij (GPa)', 'C11 242.8, C22 343.8, C33 347.4, C44 47.8, C55 88.6, C66 104.0, C12 128.0, C13 160.0, C23 70.9, C15 -1.62, C25 0.36, C35 0.97, C46 5.59', 'literature', 'Adachi 2018'],
    ['K a-c (W/mK)', '12.13, -0.992, 14.09', 'literature', 'Klimm 2023'], ['alpha a,b,c (1/K)', '1.54e-6, 3.37e-6, 3.15e-6', 'literature (secondary-quoted), uncertain', 'Orlandi 2015'],
    ['alpha 298K-like (sensitivity only)', '0.10e-6, 0.20e-6, 0.20e-6', 'sensitivity-only', 'Cheng 2018 abstract-level'], ['rho', '5880 kg/m3', 'literature', ''], ['c_p', '560 J/kgK', 'assumed (literature 485-540)', 'Handwerg 2016'],
    ['tau', '1, 5, 20 ps', 'hypothetical', ''], ['R/a', '80', 'design', ''], ['pulse', 't0=2.5, tw=1.2 t_th', 'design', '']])
runs = []
for jp in sorted(glob.glob(os.path.join(ROOT, '09_Raw_Data', 'production', '*.json'))):
    q = json.load(open(jp)); runs.append([q['tag'], q.get('block'), q['model'], q['tau_ps'], q['chi'], q['phi'], q['a_nm'], f"{q['Nr']}x{q['Nt']}", q.get('gamma_grid'), q['sig_interp'], q['sig_nodal'], q['t_star'], q['back_max'], q['wall_pulse_err']])
sheet('Production_runs', ['tag', 'block', 'model', 'tau_ps', 'chi', 'phi', 'a_nm', 'grid', 'gamma_grid', 'sig_interp_Pa_per_K', 'sig_nodal', 't_star', 'backward_err', 'wall_pulse_err'], runs)
wb.save(os.path.join(MS, 'SUPPLEMENTARY_TABLES.xlsx')); print('SUPPLEMENTARY_TABLES.xlsx written with', len(wb.sheetnames), 'sheets')
