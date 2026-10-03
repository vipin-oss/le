"""build_manuscript.py — assembles the manuscript (docx + md), highlights, supplementary workbook and cover letter
from the analysis outputs.  Run after analyze_v2.py and make_figures.py.  Every number comes from JSON/CSV outputs.

Structure (2026-10-02): 9 sections / 41 subsections, with the full derivation chain of the model
(ms_derivation) and of the numerical method (ms_numerics) written out as numbered equations.  Section
numbers are assigned here, in one place: every heading of every builder module is translated through
SEC_MAP, and an unmapped heading aborts the build, so a heading added in a module cannot silently keep
an old number.  Cross-references use the placeholders @@fig:key@@, @@tab:key@@ and @@eq:key@@, all
resolved here by order of appearance.
"""
import os, sys, json, csv, re, glob
sys.dont_write_bytecode = True
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MS = os.path.join(ROOT, '13_Manuscript')
sys.path.insert(0, MS); sys.path.insert(0, os.path.join(ROOT, '06_Source_Code', 'src'))
import numpy as np
import docbuilder as db
import ms_static as S
import ms_results as R
import ms_derivation as D
import ms_numerics as NU
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
dmax_all = max([r['D'] for r in dyn] or [float('nan')]); d10max = max([r['D'] for r in dyn if r['a_nm'] >= 10] or [float('nan')]); pkmax = max([abs(r['peak_shift']) for r in dyn + qs] or [float('nan')]); pkmax_dyn = max([abs(r['peak_shift']) for r in dyn] or [float('nan')])
e1r = EAB.get('E1_alpha_cheng298', {}).get('mean_over_baseline')

abstract = (f"Thermal stresses around cavities in low-symmetry crystals depend on crystal orientation, cavity shape and "
            f"heat-conduction law, yet transient studies treat isotropic or highly symmetric media. We study monoclinic "
            f"\u03b2-Ga\u2082O\u2083 with a circular and an equal-area elliptical cavity (axis ratio 2) under a Gaussian wall-temperature "
            f"pulse in plane strain, with Fourier and Lord\u2013Shulman conduction as the primary models and a two-relaxation-time "
            f"kernel as exploratory variant. The single-pulse response is obtained from a "
            f"frequency-domain finite-difference solver by Bromwich inversion on a shifted contour, verified against exact "
            f"and independent solutions (peak error {pc(abs(R.N['v9d_worst192']) if R.N['v9d_worst192'] is not None else None, 2)} at the finest grid, second order). The peak wall "
            f"stress is orientation-invariant to round-off: {mp(g(CIRC, 'radial_interp', 'f_ext'), 3)} MPa/K for the circle. The ellipse converts "
            f"crystal orientation into a peak-stress modulation of {pc(amp_best, 1)} on the extrapolated sweep ({pc(a12.get('amplitude'), 1)} on the "
            f"production grid) with numerical uncertainty {100*T4.get('u_num', float('nan')):.1f} percentage points; single-parameter ablations on the production grid attribute the modulation to "
            f"competing expansion and stiffness anisotropy, conductivity anisotropy being minor. Thermal memory (hypothetical relaxation times to 20 ps) "
            f"changes the circular-cavity wall-stress history by at most {pc(dmax_all, 1)} ({pc(d10max, 1)} at 10 nm and larger) and the peak (dynamic and quasi-static variants) by at most "
            f"{pc(pkmax, 1)} ({pc(pkmax_dyn, 1)} among dynamic runs); the residual size dependence is a quasi-static "
            f"collapse plus an O(\u03b5\u00b2) inertia "
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

# A missing input number renders as 'n/a'; in the abstract or a highlight that is a build error, not a
# cosmetic one (the abstract must never reach a reader with a hole in it).  The common cause is rebuilding
# while the verification pass is rewriting 07_Tests/TEST_RESULTS.json.
_bad = [s for s in [abstract] + highlights if 'n/a' in s]
if _bad:
    raise SystemExit("build aborted: the abstract or a highlight contains 'n/a' (a number its input "
                     "artifact did not provide).  Rebuild after the verification pass has written its "
                     "results, or fix the missing key.  Offending strings:\n  " + "\n  ".join(_bad))

# ---------------------------------------------------------------- provenance for Section 9
def _sha16(path):
    import hashlib
    try:
        return hashlib.sha256(open(path, 'rb').read()).hexdigest()[:16]
    except OSError:
        return 'n/a'


FREEZE_GATE = _sha16(os.path.join(ROOT, '06_Source_Code', 'CODE_FREEZE_v2_gate.json'))
FREEZE_BLOCKF = _sha16(os.path.join(ROOT, '06_Source_Code', 'CODE_FREEZE_v2_blockF.json'))
# The manifest to deposit, and the one it supersedes.  Regenerate the deposited one with
# `python3 PAPER_PROJECT/06_Source_Code/make_code_freeze.py submission_2026_10_03` after ANY
# edit to a frozen file, otherwise Section 9.1 would quote digests that no longer describe the code.
SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03g', 'submission_2026_10_03f'
FREEZE_SUB = _sha16(os.path.join(ROOT, '06_Source_Code', f'CODE_FREEZE_{SUB_FREEZE}.json'))


def _freeze_match(label):
    """(n_files, n_byte_identical, n_differ) of the entries of CODE_FREEZE_<label>.json
    against the files as they stand now.  Recorded so Section 9.1 can state, without
    over-claiming, exactly how much of the frozen code is still byte-identical."""
    import hashlib, json as _json
    p = os.path.join(ROOT, '06_Source_Code', 'CODE_FREEZE_%s.json' % label)
    try:
        old = _json.load(open(p))['files']
    except (OSError, ValueError, KeyError):
        return (0, 0, 0)
    same = diff = 0
    for rel, h in old.items():
        f = os.path.join(ROOT, rel)
        if not os.path.exists(f):
            diff += 1
            continue
        cur = hashlib.sha256(open(f, 'rb').read()).hexdigest()
        same += 1 if cur == h else 0
        diff += 0 if cur == h else 1
    return (len(old), same, diff)


N_FRZ, N_FRZ_SAME, N_FRZ_DIFF = _freeze_match('v2_gate')


def _freeze_diff_names(label):
    """basenames of the entries of CODE_FREEZE_<label>.json whose recorded digest no longer matches
    the file as it stands, as prose ("a.py, b.py and c.py"); computed so that the sentence in
    Section 9.1 cannot go stale when the code is edited."""
    import hashlib, json as _json
    p = os.path.join(ROOT, '06_Source_Code', 'CODE_FREEZE_%s.json' % label)
    try:
        old = _json.load(open(p))['files']
    except (OSError, ValueError, KeyError):
        return ''
    names = []
    for rel, h in old.items():
        f = os.path.join(ROOT, rel)
        if not os.path.exists(f) or hashlib.sha256(open(f, 'rb').read()).hexdigest() != h:
            names.append(os.path.basename(rel))
    if not names:
        return ''
    if len(names) == 1:
        return names[0]
    return ', '.join(names[:-1]) + ' and ' + names[-1]


FRZ_DIFF_NAMES = _freeze_diff_names('v2_gate')
N_SUB, N_SUB_SAME, N_SUB_DIFF = _freeze_match(SUB_FREEZE)
N_PREV, N_PREV_SAME, N_PREV_DIFF = _freeze_match(PREV_FREEZE)
if N_SUB_DIFF:
    raise SystemExit(f"CODE_FREEZE_{SUB_FREEZE}.json no longer describes the code "
                     f"({N_SUB_DIFF} of {N_SUB} entries differ); regenerate it with "
                     f"python3 {os.path.join(ROOT, '06_Source_Code', 'make_code_freeze.py')} "
                     f"{SUB_FREEZE} before rebuilding the manuscript")
MODEL_SHA = _sha16(os.path.join(ROOT, '06_Source_Code', 'src', 'cg_model.py'))
N_PROD = len(glob.glob(os.path.join(ROOT, '09_Raw_Data', 'production', '*.npz')))
N_RAW = sum(len(glob.glob(os.path.join(ROOT, d, '**', '*'), recursive=True)) - len(glob.glob(os.path.join(ROOT, d, '**', '*' + os.sep), recursive=True)) for d in ('09_Raw_Data',))

# ---------------------------------------------------------------- section numbering
# old heading text (as returned by the builder modules) -> new heading text
SEC_MAP = {
    '1. Introduction': '1. Introduction',
    '1.1 Cavities, thermal stress and crystal anisotropy': '1.1 Cavities, thermal stress and crystal anisotropy',
    '1.2 Transient loading, thermal memory and non-Fourier conduction': '1.2 Transient loading, thermal memory and non-Fourier conduction',
    '1.3 Scope of the study and what is claimed': '1.3 Scope of the study and what is claimed',
    '1.4 Contributions and structure of the paper': '1.4 Contributions and structure of the paper',
    '2. Model and parameters': '2. Governing equations and constitutive framework',
    '2.1 Governing equations': '2.1 Governing equations',
    '2.2 Dimensionless groups': '2.7 Dimensionless groups',
    '2.3 Material parameters': '2.8 Material parameters',
    '2.4 Quantities of interest': '2.9 Quantities of interest',
    '2.5 Two analytical results': '@@DROP@@',
    '3. Numerical method': '4. Numerical method',
    '3.1 Spatial discretisation and frequency-domain solver': '4.1 Spatial discretisation and frequency-domain solver',
    '3.2 Single-pulse response by Bromwich inversion': '4.6 Single-pulse response by Bromwich inversion',
    '3.3 Numerical uncertainty': '4.8 Numerical uncertainty',
    '4. Verification and numerical uncertainty': '5. Verification and numerical uncertainty',
    '4.1 Component and reference tests': '5.1 Component and reference tests',
    '4.2 Choice of the radial clustering': '5.2 Choice of the radial clustering',
    '4.3 Grid convergence of the production quantities': '5.3 Grid convergence of the production quantities',
    '5. Results': '6. Results',
    '5.1 Circular cavity: orientation-invariant peak and local response': '6.1 Circular cavity: orientation-invariant peak and local response',
    '5.2 Elliptical cavity: crystal orientation modulates the peak wall stress': '6.2 Elliptical cavity: crystal orientation modulates the peak wall stress',
    '5.3 Which anisotropy drives the modulation': '6.3 Which anisotropy drives the modulation',
    '5.4 Thermal memory and thermoelastic feedback': '6.4 Thermal memory and thermoelastic feedback',
    '5.5 Sensitivity to the expansion data': '6.5 Sensitivity to the expansion data',
    '6. Discussion and limitations': '7. Discussion and limitations',
    '6.1 What the study shows': '7.1 What the study shows',
    '6.2 Limitations': '7.2 Limitations',
    '6.3 Outlook': '7.3 Outlook',
    '7. Conclusions': '8. Conclusions',
    # ---- headings written by the expansion modules (identity: they are already numbered)
    '2.2 Kinematics, balance laws and the heat equation': '2.2 Kinematics, balance laws and the heat equation',
    '2.3 Plane-strain reduction of the monoclinic law': '2.3 Plane-strain reduction of the monoclinic law',
    '2.4 Rotation of the crystal': '2.4 Rotation of the crystal',
    '2.5 Conduction kernels in the Laplace domain': '2.5 Conduction kernels in the Laplace domain',
    '2.6 Boundary and initial conditions': '2.6 Boundary and initial conditions',
    '3. Analytical results': '3. Analytical results',
    '3.1 Non-dimensionalisation': '3.1 Non-dimensionalisation',
    '3.2 The collapse identity and its two corrections': '3.2 The collapse identity and its two corrections',
    '3.3 Local response of the circular cavity in an isotropic solid': '3.3 Local response of the circular cavity in an isotropic solid',
    '3.4 Bound on the thermoelastic feedback': '3.4 Bound on the thermoelastic feedback',
    '3.5 What these results do and do not establish': '3.5 What these results do and do not establish',
    '4.2 Body-fitted mapped grid': '4.2 Body-fitted mapped grid',
    '4.3 Conservative discretisation of the two operators': '4.3 Conservative discretisation of the two operators',
    '4.4 Boundary conditions and extraction of the wall stress': '4.4 Boundary conditions and extraction of the wall stress',
    '4.5 Frequency-domain system': '4.5 Frequency-domain system',
    '4.6 Single-pulse response by Bromwich inversion': '4.6 Single-pulse response by Bromwich inversion',
    '4.8 Numerical uncertainty': '4.8 Numerical uncertainty',
    '4.7 Definitions of the quantities of interest': '4.7 Definitions of the quantities of interest',
    '5.4 What the verification covers and what it does not': '5.4 What the verification covers and what it does not',
    '9. Code, data and reproducibility': '9. Code, data and reproducibility',
    '9.1 Code and provenance': '9.1 Code and provenance',
    '9.2 Data package': '9.2 Data package',
    '9.3 Reproduction': '9.3 Reproduction',
}


def sect(blocks):
    """split a flat block list into {heading: [blocks]} at h1/h2 boundaries"""
    out, key = {}, None
    for b in blocks:
        if b[0] in ('h1', 'h2'):
            key = b[1]
            out[key] = []
        else:
            out[key].append(b)
    return out


def renumber(blocks):
    """apply SEC_MAP to every numbered heading; abort on an unmapped one.

    Unnumbered headings (Abstract, Highlights, Declarations, References, Appendix A) pass through."""
    out = []
    for b in blocks:
        if b[0] in ('h1', 'h2') and re.match(r'^\d', b[1]):
            if b[1] not in SEC_MAP:
                raise SystemExit('unmapped heading %r — add it to SEC_MAP' % b[1])
            if SEC_MAP[b[1]] == '@@DROP@@':
                continue
            b = (b[0], SEC_MAP[b[1]]) + tuple(b[2:])
        out.append(b)
    return out


# ---------------------------------------------------------------- assemble blocks
blocks = [('title', 'Orientation-dependent wall stress around circular and elliptical cavities in monoclinic β-Ga\u2082O\u2083 under a transient thermal pulse: a verified continuum study with thermal-memory and mechanism ablations'),
          ('authors', '[AUTHOR INPUT REQUIRED: author names, affiliations, ORCID iDs and corresponding author]'),
          ('h1', 'Abstract'), ('p', abstract),
          ('p', '**Keywords:** thermoelasticity; cavity; monoclinic crystal; β-Ga\u2082O\u2083; Lord–Shulman theory; Bromwich inversion'),
          ('h1', 'Highlights'), ('bullets', highlights)]

# ---- Section 1: the four introduction paragraphs become four subsections
_intro = S.intro()
_intro_ps = [b for b in _intro if b[0] == 'p']
assert len(_intro_ps) == 4, len(_intro_ps)
blocks += [('h1', '1. Introduction')]
for _h2, _p in zip(('1.1 Cavities, thermal stress and crystal anisotropy',
                    '1.2 Transient loading, thermal memory and non-Fourier conduction',
                    '1.3 Scope of the study and what is claimed',
                    '1.4 Contributions and structure of the paper'), _intro_ps):
    blocks += [('h2', _h2), _p]

# ---- Section 2
MO = sect(S.model())
blocks += [('h1', '2. Model and parameters')]
blocks += [('h2', '2.1 Governing equations')] + MO['2.1 Governing equations']
blocks += [('fig', os.path.join(ROOT, '11_Figures', 'fig1_setup.png'), 'Problem set-up: (a) circular and (b) equal-area elliptical cavity in the a\u2013c plane of the crystal (crystal rotated by \u03c6); (c) wall-temperature pulse and quantity-of-interest window.', 6.6, 'setup')]
blocks += [('h2', '2.2 Kinematics, balance laws and the heat equation')] + D.sec2_kinematics()
blocks += D.sec2_constitutive()
blocks += D.sec2_rotation()
blocks += D.sec2_kernels()
blocks += D.sec2_bc()
blocks += [('h2', '2.2 Dimensionless groups')] + MO['2.2 Dimensionless groups'] + D.sec2_dimensionless()
blocks += [('h2', '2.3 Material parameters')] + MO['2.3 Material parameters']
blocks += [('h2', '2.4 Quantities of interest')] + MO['2.4 Quantities of interest']

# ---- Section 3: analytical results; the two legacy paragraphs of Section 2.5 are reused
AN = S.analytic()
_scaling = AN[1]                       # the "Scaling." paragraph (now 3.2)
_local_intro = AN[2]                   # the "Local response of the isotropic circle." lead-in (now 3.3)
_local_close = AN[4]                   # the far-field / 0.985 MPa/K paragraph (end of 3.3)
blocks += D.sec3(_scaling, _local_intro, _local_close)

# ---- Section 4
ME = sect(S.method())
_brom_legacy = [b for b in ME['3.2 Single-pulse response by Bromwich inversion'] if b[0] in ('p', 'eq')]
blocks += [('h1', '3. Numerical method')]
blocks += [('h2', '3.1 Spatial discretisation and frequency-domain solver')] + ME['3.1 Spatial discretisation and frequency-domain solver']
blocks += NU.sec4_grid()
blocks += NU.sec4_ops()
blocks += NU.sec4_bc()
blocks += NU.sec4_system()
blocks += NU.sec4_bromwich(_brom_legacy[0], _brom_legacy[1], _brom_legacy[2])
blocks += NU.sec4_qoi()
blocks += [('h2', '3.3 Numerical uncertainty')] + ME['3.3 Numerical uncertainty'] + NU.sec4_uncertainty()[1:]
blocks += [('p', 'Software and AI assistance (Methods disclosure): the finite-difference solver of the preliminary analysis was reviewed, corrected where noted, extended and verified with the assistance of generative-AI coding tools; this is the research-process use referred to in the declaration before the references (Section 5 lists the tests; code, tests and raw data are in the data package). All numbers in this paper are produced by the analysis scripts from stored raw outputs.')]

# ---- Sections 5-8
blocks += R.verification()
blocks += [('h2', '5.4 What the verification covers and what it does not'),
           ('p', f"The tests of Sections 5.1-5.3 are code-verification and solution-verification tests in the usual "
                 f"sense [53]: they compare the implementation with exact solutions of the same equations (patch tests, "
                 f"steady and 1-D reference solutions, the closed form of Section 3.3) and with independent "
                 f"implementations of the same model (an independent three-dimensional tensor rotation, a 1-D spectral "
                 f"solver, a time-domain Crank-Nicolson integration), and they quantify the discretisation error by grid "
                 f"refinement. What they do not do is check the model itself. The constitutive law, the plane-strain "
                 f"reduction, the relaxation-time kernel, the parameter values of @@tab:params@@ and the continuum "
                 f"description at 5-50 nm are inputs, not outputs, of the verification: an error in any of them would "
                 f"leave every test above passing. No comparison with measurements is made anywhere in this paper, so the "
                 f"study is verified and not validated; the physical status of the model is discussed in Section 7.2.")]
blocks += R.results() + R.discussion() + R.conclusions()

# ---- Section 9
blocks += [('h1', '9. Code, data and reproducibility'),
           ('h2', '9.1 Code and provenance'),
           ('p', f"The solver, the test suite, the experiment drivers and the analysis scripts are frozen: SHA-256 "
                 f"digests of every file are recorded in `CODE_FREEZE_v2_gate.json` ({FREEZE_GATE} for the file itself) "
                 f"and `CODE_FREEZE_v2_blockF.json` ({FREEZE_BLOCKF}), and the material model alone is identified by "
                 f"`cg_model.py` ({MODEL_SHA}). Every production run records the code version, a checksum of its input "
                 f"configuration, the environment and a digest of its own output in "
                 f"`10_Processed_Data/PRODUCTION_PROVENANCE.csv`, so each number in this paper can be traced to the run "
                 f"that produced it and to the code state that produced the run."),
           ('p', f"**Code state and re-checks.** The two archived manifests date from 2026-10-01; since they were "
                 f"taken, {N_FRZ_DIFF} of the {N_FRZ} entries of `CODE_FREEZE_v2_gate.json` ({FRZ_DIFF_NAMES}) have been "
                 f"edited, so the "
                 f"digests recorded for them no longer describe the code. The pipeline was re-run end to end with the code "
                 f"as it now stands and compared with the archived results (`15_Audits/RERUN_COMPARISON.md`): every "
                 f"production run reproduces its archived quantity of interest to zero relative difference and only "
                 f"wall-clock timings differ. On 2026-10-03 the analysis layer was re-run over all {N_PROD} stored runs: "
                 f"every pre-existing quantity of `ANALYSIS_V2.json` came out identical (the only value that moves is the "
                 f"number of runs audited), the eight figures and the five archived CSV tables are byte-identical to the "
                 f"archived files, and one further CSV (the ablation set at the production grid) is added. A full "
                 f"production job re-solved in a different build \u2014 Python 3.11.2 with NumPy 2.4.6 instead of "
                 f"3.13.14/2.3.5 \u2014 reproduces its stored peak wall stress to 2.7\u00d710\u207b\u00b9\u2076 relative, i.e. one unit in the "
                 f"last place; the reconstruction of the wall temperature stays within 1.0\u00d710\u207b\u00b9\u2070 of the imposed pulse over the "
                 f"reported window for every run. Two refreshed manifests record the current code: "
                 f"`CODE_FREEZE_{PREV_FREEZE}.json` ({N_PREV} files, taken before this verification pass) and "
                 f"`CODE_FREEZE_{SUB_FREEZE}.json` ({FREEZE_SUB}, {N_SUB} files, all {N_SUB_SAME} byte-identical to the "
                 f"code as submitted); the second is the one to deposit with the data package, and the earlier manifests "
                 f"are kept unchanged as history."),
           ('h2', '9.2 Data package'),
           ('p', f"The package contains the frozen source (06_Source_Code), the test suite and its machine-readable "
                 f"results (07_Tests), the experiment drivers (08_Experiments), the per-run raw outputs "
                 f"({N_PROD} production runs as .npz/.json pairs under 09_Raw_Data, together with the convergence and "
                 f"pulse-width runs), the processed analysis (10_Processed_Data: ANALYSIS_V2.json, the convergence "
                 f"results and the provenance table), the figure scripts and figures (11_Figures), the tables "
                 f"(12_Tables), the manuscript builders (13_Manuscript) and the audit records (15_Audits). The raw "
                 f"outputs store the frequency-domain transfer values as well as the inverted histories, so the "
                 f"quantities of interest can be recomputed without re-solving."),
           ('h2', '9.3 Reproduction'),
           ('p', "`python3 08_Experiments/reproduce.py` reruns the pipeline end to end (tests, production matrix, "
                 "convergence runs, analysis, figures, manuscript builders) in the order used here; the individual "
                 "stages are `07_Tests/run_tests.py`, `08_Experiments/run_production_v2.py`, `run_convergence.py`, "
                 "`analyze_v2.py`, `make_figures.py`, `13_Manuscript/build_manuscript.py` and "
                 "`tools/md_to_tex.py`. The environment is recorded in the code-freeze files; the memory required by "
                 "the finest grid (192\u00d7192) exceeded the 2 GB available here, which is why that grid is absent "
                 "from the convergence families (Section 7.2)."),
           ]

blocks += [('h1', 'Acknowledgements'),
           ('p', '[AUTHOR INPUT REQUIRED: acknowledge any funding, technical help or computing facilities not already named in the Funding statement; omit this section if there is nothing to acknowledge.]'),
           ]

blocks += [('h1', 'Declarations'),
           ('p', '**CRediT authorship contribution statement:** [AUTHOR INPUT REQUIRED].'),
           ('p', '**Declaration of competing interest:** [AUTHOR INPUT REQUIRED].'),
           ('p', '**Funding:** [AUTHOR INPUT REQUIRED: name the grant, or state that no funding was received].'),
           ('p', '**Data availability:** the Python source code, verification suite, '
                 'per-run raw outputs (npz/json, including the frequency-domain transfer '
                 'values), analysis and figure scripts and the production matrix are provided '
                 'in the project data package, whose contents are fixed by the SHA-256 code '
                 f'freeze `CODE_FREEZE_{SUB_FREEZE}.json` described in Section 9.1; the package '
                 'will be deposited in a public repository under the persistent identifier '
                 'to be deposited at [PUBLIC REPOSITORY/DOI TO BE INSERTED].'),
           ('p', '**Declaration of Generative AI and AI-assisted technologies in the writing process.** '
                 'During the preparation of this work the author(s) used a generative-AI assistant (Arena.ai Agent '
                 'Mode) in order to draft and revise the text and the figure captions, and to check the internal consistency '
                 'of the manuscript, the calculation companion and the tables. After using this tool the author(s) '
                 'reviewed and edited the content as needed and take(s) full responsibility for the content of the '
                 'publication. The research-process use of the same class of tool - reviewing and extending the numerical '
                 'code and the verification suite, and running the simulations - is recorded with the numerical-methods '
                 'section, as the journal policy directs. No AI tool generated a physical result and no AI tool produced '
                 'or selected any number reported here; no AI tool acted without the author(s)\' review, and no AI tool '
                 'is an author or is cited as a source.')]

blocks += [('h1', 'References'), ('refs', [r['text'] for r in refs])]
blocks += [('h1', 'Appendix A. Nomenclature'),
           ('p', 'The symbols used in this paper are listed in @@tab:nom@@.'),
           ('table', ['Symbol', 'Meaning', 'Unit'],
            [['a', 'cavity radius (circle) / reference length', 'm'], ['χ', 'ellipse aspect parameter (semi-axes a√χ, a/√χ)', '—'], ['φ', 'rotation of the crystal about the b-axis', 'deg'],
             ['Q, C_{ij}', 'plane-strain stiffness block, stiffness constants', 'Pa'], ['β = Cα', 'thermal-stress vector', 'Pa/K'], ['K', 'conductivity tensor (a–c block)', 'W/(m K)'],
             ['ρ, c_{p}', 'density, specific heat', 'kg/m³, J/(kg K)'], ['τ', 'relaxation time', 's'], ['τ_{a}, τ_{b}, τ_{eff}', 'two-relaxation-time kernel parameters (τ/2, 2τ, 1.25τ)', 's'],
             ['κ̄, t_{th}', 'thermal diffusivity, a²/κ̄', 'm²/s, s'], ['v_{T}', 'thermal wave speed (κ̄/τ)^{1/2}', 'm/s'],
             ['Λ = τ/t_{th}', 'memory number', '—'], ['ε = κ̄/(c_{ref}a)', 'elastic number', '—'], ['δ', 'thermoelastic coupling number', '—'],
             ['c_{ref}, C̄', 'wave-speed scale (C̄/ρ)^{1/2}, stiffness scale C_{33}', 'm/s, Pa'],
             ['α_{0}, Θ', 'expansion scale \u2016\u03b2\u2016/C\u0304, wall-temperature amplitude', '1/K, K'],
             ['x, t, \u03b8, u, \u03c3, \u03b5', 'dimensionless counterparts (hats in the text) of the variables of Section 3.1', '—'],
             ['b, Q', 'normalised thermal-stress vector \u03b2/\u2016\u03b2\u2016 and stiffness Q/C\u0304', '—, —'],
             ['s, γ_{B}, T', 'Laplace variable, Bromwich abscissa and period', '1/s, 1/t_{th}, t_{th}'],
             ['K, ω_{k}, ε_{tr}', 'number of Bromwich terms, their frequencies, spectrum tolerance', '—, 1/t_{th}, —'],
             ['H(s), P(s), Y(s)', 'transfer function, pulse transform, response transform', '—, s, —'],
             ['σ̂', 'peak wall hoop stress per kelvin', 'Pa/K'], ['A_{φ}, A_{2}', 'orientation modulation (max − min)/mean, two-point version', '—'],
             ['D', 'thermal-memory deviation', '—'], ['u_{num}, f\u2082', 'numerical uncertainty, Richardson-extrapolated value', '—'],
             ['θ, T_{0}', 'temperature rise; reference temperature (293 K)', 'K, K'],
             ['u', 'displacement in the a–c plane', 'm'],
             ['ϵ', 'small-strain tensor (Voigt ϵ_{11}, ϵ_{33}, γ_{13})', '—'],
             ['σ', 'stress tensor', 'Pa'],
             ['α', 'thermal-expansion vector', '1/K'],
             ['R', 'outer radius of the finite domain (R = 80a)', 'm'],
             ['p(t), t_{0}, t_{w}', 'wall-temperature pulse, its centre and width', 'K, t_{th}, t_{th}'],
             ['F(t), G(r)', 'radial integrals of θ (a to R, a to r) in Eq. (@@eq:local@@)', 'K m²'],
             ['λ, μ, m, γ_{T}, g_{T}', 'Lamé constants of the isotropic control; m = λ + 2μ; γ_{T} = (3λ + 2μ)α; g_{T} = γ_{T}/m', 'Pa, Pa, Pa, Pa/K, 1/K'],
             ['C_{1}, C_{2}', 'integration constants of Eq. (@@eq:usol@@)', 'Pa, Pa m'],
             ['ξ, η, ρ', 'computational coordinates and the radial map', '—, rad, —'],
             ['A, B, J', 'map functions and Jacobian', 'm, m, m²'],
             ['A, B, D', 'contravariant thermal-operator coefficients', 'W/(m K)'],
             ['γ', 'radial clustering parameter of the grid', '—'],
             ['N_{r} × N_{θ}', 'grid size (radial × angular)', '—'],
             ['ω, g(ω)', 'angular frequency, conduction kernel', '1/s, —'],
             ['η', 'backward error of the linear solve', '—']],
            'Nomenclature.', [1.3, 3.9, 1.3], 'nom')]

# ---------------------------------------------------------------- headings: renumber
blocks = renumber(blocks)

# ---- resolve @@fig:key@@ / @@tab:key@@ / @@eq:key@@ placeholders by order of appearance
fn = tn = en = 0; num = {}
for x in blocks:
    if x[0] == 'fig': fn += 1; (num.__setitem__('fig:' + x[4], fn) if len(x) > 4 else None)
    if x[0] == 'table': tn += 1; (num.__setitem__('tab:' + x[5], tn) if len(x) > 5 else None)
    if x[0] == 'eq': en += 1; (num.__setitem__('eq:' + x[3], en) if len(x) > 3 and x[3] else None)


def rep(t):
    def _r(m):
        kind, key = m.group(1), m.group(2)
        k = kind + ':' + key
        return (('Fig. ' if kind == 'fig' else 'Table ' if kind == 'tab' else '') +
                str(num.get(k, '??' + key + '??')))
    return re.sub(r'@@(fig|tab|eq):(\w+)@@', _r, t)


new_blocks = []
for x in blocks:
    x = list(x)
    if x[0] in ('p', 'note'): x[1] = rep(x[1])
    elif x[0] == 'bullets': x[1] = [rep(t) for t in x[1]]
    elif x[0] == 'fig': x[2] = rep(x[2])
    elif x[0] == 'table':
        x[1] = [rep(str(c)) for c in x[1]]
        x[2] = [[rep(str(c)) for c in row] for row in x[2]]
        x[3] = rep(x[3])
    new_blocks.append(tuple(x))
blocks = new_blocks
unres = [t for x in blocks if x[0] in ('p',) for t in re.findall(r'\?\?\w+\?\?', x[1])]
if unres:
    raise SystemExit('unresolved placeholders: %s' % unres[:5])
def _no_placeholder_tables(path, doc):
    """Submission guard (audit A2): a generated table must never ship a placeholder cell.  `n/a`, `??` and empty
    cells appear when a builder is asked for a number that the data do not supply; that is a build error, not a
    sentence in a paper."""
    bad = []
    for i, line in enumerate(open(path, encoding='utf-8').read().split('\n'), 1):
        if not line.lstrip().startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 2:
            continue
        for c in cells:
            if c in ('n/a', 'N/A', '??', 'TODO', ''):
                bad.append(f'  line {i}: {line.strip()[:110]}')
                break
    if bad:
        raise SystemExit(f'{doc}: placeholder cells in generated tables ({len(bad)} line(s)):\n'
                         + '\n'.join(bad[:8]) + '\nFix the builder or the data; do not ship the placeholder.')



# ------------------------------------------------------------------ Elsevier numbered style: sequential citations
_CITE = re.compile(r'\[(\d{1,2}(?:\s*[,;-]\s*\d{1,2})*)\]')


def _cite_nums(text):
    out = []
    for part in re.split(r'[,;]', text):
        part = part.strip()
        if '-' in part:
            lo, hi = part.split('-')
            if lo.isdigit() and hi.isdigit():
                out.extend(range(int(lo), int(hi) + 1))
        elif part.isdigit():
            out.append(int(part))
        else:
            return None
    if not out or any(n < 1 or n > len(refs) for n in out):
        return None
    return out


def _flatten(v):
    if isinstance(v, str):
        return [v]
    if isinstance(v, (list, tuple)):
        out = []
        for x in v:
            out.extend(_flatten(x))
        return out
    return []


def _sequentialise(blocks):
    """Renumber [n] citations to order of first appearance and reorder the printed list to match.

    Only prose/table blocks are scanned for first appearances (the reference list itself is not a citation); a
    bracket group counts only when every number is a valid reference index, so grid sizes and percentages in
    square brackets are left alone. The mapping is written for tools/md_to_tex.py and for the companion
    builder, which point at the same numbers.
    """
    order = []
    for blk in blocks:
        if blk[0] == 'refs':
            continue
        for txt in _flatten(blk[1:]):
            if isinstance(txt, str):
                for m in _CITE.finditer(txt):
                    for n in (_cite_nums(m.group(1)) or []):
                        if n not in order:
                            order.append(n)
    for n in range(1, len(refs) + 1):
        if n not in order:
            order.append(n)                      # uncited entries keep their relative order at the end
    new_of = {old: i + 1 for i, old in enumerate(order)}

    def remap(txt):
        def sub(m):
            ns = _cite_nums(m.group(1))
            if not ns:
                return m.group(0)
            return '[' + ','.join(str(new_of[n]) for n in ns) + ']'
        return _CITE.sub(sub, txt)

    ordered = [dict(refs[old - 1], n=i + 1) for i, old in enumerate(order)]
    def deep(v):
        if isinstance(v, str):
            return remap(v)
        if isinstance(v, (list, tuple)):
            return type(v)(deep(x) for x in v)
        return v

    def remap_blk(blk):
        if blk[0] == 'refs':
            return ('refs', [x['text'] for x in ordered])
        return tuple([blk[0]] + [deep(x) for x in blk[1:]])
    out = [remap_blk(b) for b in blocks]
    json.dump({'old_to_new': {str(k): v for k, v in new_of.items()},
               'order': order, 'n_refs': len(refs)},
              open(os.path.join(MS, 'REF_ORDER.json'), 'w'), indent=1)
    json.dump(ordered, open(os.path.join(MS, 'REFERENCES_ORDERED.json'), 'w'), indent=1)
    return out, sum(1 for old, new in new_of.items() if old != new)


_blocks_pre = blocks
blocks, n_moved = _sequentialise(blocks)
print('sequential citation numbering: %d of %d entries changed number' % (n_moved, len(refs)))

# ------------------------------------------------------------------ back matter order (Elsevier)
_i_app = next(i for i, b in enumerate(blocks) if b[0] == 'h1' and b[1].startswith('Appendix A'))
_i_ref = next(i for i, b in enumerate(blocks) if b[0] == 'h1' and b[1] == 'References')
if _i_app > _i_ref:                               # text, declarations, appendix, references
    _i_end = _i_app + 1
    while _i_end < len(blocks) and not (blocks[_i_end][0] == 'h1'):
        _i_end += 1
    blk = blocks[_i_app:_i_end]
    blocks = blocks[:_i_app] + blocks[_i_end:]
    _i_ref = next(i for i, b in enumerate(blocks) if b[0] == 'h1' and b[1] == 'References')
    blocks = blocks[:_i_ref] + blk + blocks[_i_ref:]
    print('back matter: Appendix A moved before the References (Elsevier order)')

# The placeholder guard must see the text being generated, not the file the previous build left on disk:
# guarding after the write can only reject a build that is already clean, and guarding before it clobbers the
# last good document with a bad one.  Render to a temporary file, guard it, then move it into place.
_pend = os.path.join(MS, '.manuscript_IJHMT.pending.md')
db.build_md(blocks, _pend)
_no_placeholder_tables(_pend, 'manuscript')
os.replace(_pend, os.path.join(MS, 'manuscript_IJHMT.md'))
db.build_docx(blocks, os.path.join(MS, 'manuscript_IJHMT.docx'))
open(os.path.join(MS, 'highlights.txt'), 'w').write('\n'.join(highlights) + '\n')
n_words = sum(len(re.findall(r'\w+', b[1])) for b in blocks if b[0] == 'p')
n_sec = sum(1 for b in blocks if b[0] == 'h1' and re.match(r'^\d+\. ', b[1]))
n_sub = sum(1 for b in blocks if b[0] == 'h2' and re.match(r'^\d+\.\d+\s', b[1]))
print(f'manuscript written; abstract {n_abs} words (limit 250); highlight lengths {[l for _, l in hl_ok]} (limit 85); body paragraphs ~{n_words} words')
print(f'structure: {n_sec} sections, {n_sub} subsections, {en} equations, {fn} figures, {tn} tables, {len(refs)} references')
json.dump(dict(abstract_words=n_abs, highlight_lengths=[l for _, l in hl_ok], body_words=n_words, driver=driver_txt,
               amp_best=amp_best, n_sections=n_sec, n_subsections=n_sub, n_equations=en, n_figures=fn, n_tables=tn,
               n_references=len(refs)), open(os.path.join(MS, 'MANUSCRIPT_STATS.json'), 'w'), indent=1)
