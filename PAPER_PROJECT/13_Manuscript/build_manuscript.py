"""build_manuscript.py — assembles the manuscript (docx + md), highlights, supplementary workbook and cover letter
from the analysis outputs.  Run after analyze_v2.py and make_figures.py.  Every number comes from JSON/CSV outputs."""
import os, sys, json, csv, re, glob
sys.dont_write_bytecode = True
ROOT = '/home/user/PAPER_PROJECT'; MS = os.path.join(ROOT, '13_Manuscript')
sys.path.insert(0, MS); sys.path.insert(0, os.path.join(ROOT, '06_Source_Code', 'src'))
import numpy as np
import docbuilder as db
import ms_static as S
import ms_results as R
from ms_results import g, pc, mp, sci

T1, T2, T3, T4, EAB, CIRC = R.T1, R.T2, R.T3, R.T4, R.EAB, R.CIRC
refs = json.load(open(os.path.join(ROOT, '01_Literature', 'REFERENCES_VERIFIED.json')))

# ---------------------------------------------------------------- derived statements
a12 = g(T4, 'M_12phi_sig_interp', default={}); a6e = g(T4, 'extrapolated_6phi', default={})
amp_best = a6e.get('amplitude', a12.get('amplitude'))
dyn = [r for r in T2.get('dynamic', []) if r['model'] == 'CV']; qs = [r for r in T2.get('quasi_static', []) if r['model'] == 'CV']
dmax = max([r['D'] for r in dyn + qs] or [float('nan')]); lmax = max([r['Lambda'] for r in dyn] or [float('nan')])
base_amp = g(EAB, 'baseline_6phi', 'amplitude')
names = {'E3_K_iso': 'conductivity', 'E4_C_iso': 'stiffness', 'E2_alpha_iso': 'thermal-expansion'}
ratios = {k: EAB[k]['amplitude'] / base_amp for k in names if k in EAB and base_amp}
if ratios.get('E3_K_iso', 0) >= 0.85 and ratios.get('E2_alpha_iso', 1) < 0.9 and ratios.get('E4_C_iso', 0) > 1.1:
    short_driver = 'the competition of expansion and stiffness anisotropy (conductivity anisotropy is minor)'
elif ratios:
    d_ = min(ratios, key=ratios.get); short_driver = f"{names[d_]} anisotropy" if ratios[d_] < 0.9 else 'the combined anisotropy'
else:
    short_driver = 'the combined anisotropy'
driver_txt = short_driver
dmax_all = max([r['D'] for r in dyn] or [float('nan')]); d10max = max([r['D'] for r in dyn if r['a_nm'] >= 10] or [float('nan')]); pkmax = max([abs(r['peak_shift']) for r in dyn + qs] or [float('nan')])
e1r = EAB.get('E1_alpha_cheng298', {}).get('mean_over_baseline')

abstract = (f"Thermal stresses around cavities in low-symmetry crystals depend on crystal orientation, cavity shape and "
            f"heat-conduction law, yet transient studies treat isotropic or highly symmetric media. We study monoclinic "
            f"\u03b2-Ga\u2082O\u2083 with a circular and an equal-area elliptical cavity (axis ratio 2) under a Gaussian wall-temperature "
            f"pulse in plane strain, with Fourier and Lord\u2013Shulman conduction as the primary models and a two-relaxation-time "
            f"kernel as an exploratory variant. The response of a quiescent medium to one pulse is obtained from a "
            f"frequency-domain finite-difference solver by Bromwich inversion on a shifted contour and verified against exact "
            f"and independent solutions (peak error {pc(abs(R.N['v9d_worst192']) if R.N['v9d_worst192'] is not None else None, 2)} at the finest grid, second order). The peak wall "
            f"stress of the circle is orientation-invariant to round-off and equals {mp(g(CIRC, 'radial_interp', 'f_ext'), 3)} MPa/K. The ellipse converts "
            f"crystal orientation into a peak-stress modulation of {pc(amp_best, 1)} on the extrapolated sweep ({pc(a12.get('amplitude'), 1)} on the "
            f"production grid), numerical uncertainty {100*T4.get('u_num', float('nan')):.1f} percentage points; ablations attribute it to competing expansion and "
            f"stiffness anisotropy, conductivity anisotropy being minor. Thermal memory (hypothetical relaxation times to 20 ps) "
            f"changes the circular-cavity wall-stress history by at most {pc(dmax_all, 1)} ({pc(d10max, 1)} at 10 nm and larger) and the peak by at most "
            f"{pc(pkmax, 1)}; the residual size dependence is a quasi-static collapse in the memory number plus an O(\u03b5\u00b2) inertia "
            f"correction. Thermoelastic feedback stays below the bound 5\u03b4. Results are properties of a verified continuum model: "
            f"no experimental validation exists, relaxation times are hypothetical, the expansion data are uncertain by more than "
            f"an order of magnitude, and continuum validity at 5\u201350 nm is not established.")
n_abs = len(abstract.split())
highlights = ['Bromwich inversion gives a verified single-pulse thermoelastic cavity response',
              'Circular-cavity peak wall stress is orientation-invariant to round-off',
              f'Ellipse turns crystal orientation into a {pc(amp_best, 1)} peak-stress modulation',
              f'Thermal memory shifts the peak wall stress by under {pc(pkmax, 1)} for \u03c4 up to 20 ps',
              'Verified, not validated: expansion data set the absolute stress scale']
hl_ok = [(h, len(h)) for h in highlights]

# ---------------------------------------------------------------- assemble blocks
blocks = [('title', 'Orientation-dependent wall stress around circular and elliptical cavities in monoclinic β-Ga\u2082O\u2083 under a transient thermal pulse: a verified continuum study with thermal-memory and mechanism ablations'),
          ('authors', '[AUTHOR INPUT REQUIRED: author names, affiliations, ORCID iDs and corresponding author]'),
          ('h1', 'Abstract'), ('p', abstract),
          ('p', '**Keywords:** thermoelasticity; cavity; monoclinic crystal; β-Ga\u2082O\u2083; Lord–Shulman theory; Bromwich inversion'),
          ('h1', 'Highlights'), ('bullets', highlights)]
blocks += S.intro() + S.model() + S.analytic() + S.method()
# Fig. 1 inserted at the end of Section 2.1 by position
idx = next(i for i, x in enumerate(blocks) if x[0] == 'h2' and x[1].startswith('2.2'))
blocks.insert(idx, ('fig', os.path.join(ROOT, '11_Figures', 'fig1_setup.png'), 'Problem set-up: (a) circular and (b) equal-area elliptical cavity in the a\u2013c plane of the crystal (crystal rotated by \u03c6); (c) wall-temperature pulse and quantity-of-interest window.', 6.6, 'setup'))
blocks += [('p', 'Software and AI assistance (Methods disclosure): the finite-difference solver of the preliminary analysis was reviewed, corrected where noted, extended and verified with the help of an AI agent (Section 4 lists the tests; code, tests and raw data are in the data package). All numbers in this paper are produced by the analysis scripts from stored raw outputs.')]
blocks += R.verification() + R.results() + R.discussion() + R.conclusions()
blocks += [('h1', 'Declarations'),
           ('p', '**CRediT authorship contribution statement:** [AUTHOR INPUT REQUIRED].'),
           ('p', '**Declaration of competing interest:** [AUTHOR INPUT REQUIRED].'),
           ('p', '**Funding:** [AUTHOR INPUT REQUIRED: name the grant, or state that no funding was received].'),
           ('p', '**Data availability:** the Python source code, verification suite, per-run raw outputs (npz/json, including the frequency-domain transfer values), analysis and figure scripts, and the production matrix are provided in the project data package (SHA-256 code freeze `CODE_FREEZE_v2_gate.json`). to be deposited at [PUBLIC REPOSITORY/DOI TO BE INSERTED].'),
           ('p', '**Declaration of Generative AI and AI-assisted technologies in the writing process.** [TEMPLATE — to be reviewed, edited and confirmed by the authors; Elsevier requires this statement above the references.] During the preparation of this work the author(s) used an AI agent (Arena.ai Agent Mode; the underlying models are provided by the service) to review and extend the numerical code and the verification suite, to run and analyse the simulations, and to draft the text and the figures. After using this tool the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the publication.')]
blocks += [('h1', 'References'), ('refs', [r['text'] for r in refs])]
blocks += [('h1', 'Appendix A. Nomenclature'),
           ('p', 'The symbols used in this paper are listed in Table 8.'),
           ('table', ['Symbol', 'Meaning', 'Unit'],
            [['a', 'cavity radius (circle) / reference length', 'm'], ['χ', 'ellipse aspect parameter (semi-axes a√χ, a/√χ)', '—'], ['φ', 'rotation of the crystal about the b-axis', 'deg'],
             ['Q, C_{ij}', 'plane-strain stiffness block, stiffness constants', 'Pa'], ['β = Cα', 'thermal-stress vector', 'Pa/K'], ['K', 'conductivity tensor (a–c block)', 'W/(m K)'],
             ['ρ, c_{p}', 'density, specific heat', 'kg/m³, J/(kg K)'], ['τ', 'relaxation time', 's'], ['κ̄, t_{th}', 'thermal diffusivity, a²/κ̄', 'm²/s, s'],
             ['Λ = τ/t_{th}', 'memory number', '—'], ['ε = κ̄/(c_{ref}a)', 'elastic number', '—'], ['δ', 'thermoelastic coupling number', '—'],
             ['s, γ_{B}, T', 'Laplace variable, Bromwich abscissa and period', '1/s, 1/t_{th}, t_{th}'], ['σ̂', 'peak wall hoop stress per kelvin', 'Pa/K'],
             ['A_{φ}', 'orientation modulation (max − min)/mean', '—'], ['D', 'thermal-memory deviation', '—'],
             ['θ, T_{0}', 'temperature rise; reference temperature (293 K)', 'K, K'],
             ['u', 'displacement in the a–c plane', 'm'],
             ['ϵ', 'small-strain tensor (Voigt ϵ_{11}, ϵ_{33}, γ_{13})', '—'],
             ['σ', 'stress tensor', 'Pa'],
             ['α', 'thermal-expansion vector', '1/K'],
             ['R', 'outer radius of the finite domain (R = 80a)', 'm'],
             ['p(t), t_{0}, t_{w}', 'wall-temperature pulse, its centre and width', 'K, t_{th}, t_{th}'],
             ['F(t)', 'radial integral of θ in Eq. (2)', 'K m²'],
             ['λ, μ, m, γ_{T}', 'Lamé constants of the isotropic control; m = λ + 2μ; γ_{T} = (3λ + 2μ)α', 'Pa, Pa, Pa, Pa/K'],
             ['C̄ = C_{33}', 'stiffness scale of the feedback number δ', 'Pa'],
             ['g(s)', 'conduction kernel: 1 (Fourier); 1/(1 + sτ) (CV); two-term (MCV3, exploratory)', '—'],
             ['N_{r} × N_{θ}', 'grid size (radial × angular)', '—']], 'Nomenclature.', [1.3, 3.9, 1.3])]

# ---- resolve @@fig:key@@ / @@tab:key@@ placeholders by order of appearance
fn = tn = 0; num = {}
for x in blocks:
    if x[0] == 'fig': fn += 1; (num.__setitem__('fig:' + x[4], fn) if len(x) > 4 else None)
    if x[0] == 'table': tn += 1; (num.__setitem__('tab:' + x[5], tn) if len(x) > 5 else None)
def rep(t):
    return re.sub(r'@@(fig|tab):(\w+)@@', lambda m: (('Fig. ' if m.group(1) == 'fig' else 'Table ') + str(num.get(m.group(1) + ':' + m.group(2), '??'))), t)
new_blocks = []
for x in blocks:
    x = list(x)
    if x[0] in ('p', 'note'): x[1] = rep(x[1])
    elif x[0] == 'bullets': x[1] = [rep(t) for t in x[1]]
    elif x[0] == 'fig': x[2] = rep(x[2])
    elif x[0] == 'table': x[3] = rep(x[3])
    new_blocks.append(tuple(x))
blocks = new_blocks
unres = [t for x in blocks if x[0] in ('p',) for t in re.findall(r'\?\?', x[1])]
db.build_docx(blocks, os.path.join(MS, 'manuscript_IJHMT.docx'))
db.build_md(blocks, os.path.join(MS, 'manuscript_IJHMT.md'))
open(os.path.join(MS, 'highlights.txt'), 'w').write('\n'.join(highlights) + '\n')
n_words = sum(len(re.findall(r'\w+', b[1])) for b in blocks if b[0] == 'p')
print(f'manuscript written; abstract {n_abs} words (limit 250); highlight lengths {[l for _, l in hl_ok]} (limit 85); body paragraphs ~{n_words} words')
json.dump(dict(abstract_words=n_abs, highlight_lengths=[l for _, l in hl_ok], body_words=n_words, driver=driver_txt, amp_best=amp_best), open(os.path.join(MS, 'MANUSCRIPT_STATS.json'), 'w'), indent=1)
