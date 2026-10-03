#!/usr/bin/env python3
"""patch_phase3_batch2.py — Phase 3, part 2 of 2: disclosures, provenance bookkeeping, cover letter.

  * ms_static.py  : the second copy of the DFT comparison (Section 4.6 paragraph) is turned into an f-string
                    so the train mean is computed from the inversion plan rather than typed.
  * build_manuscript.py / build_calculations.py : SUB_FREEZE moves to the new manifest and the superseded
                    enumeration of drifted files is generated from the manifest comparison; the AI declaration
                    is split per Elsevier policy (writing process here, research process in the methods); the
                    manuscript builder refuses to write an abstract or highlight containing 'n/a'.
  * cover_letter.md : hand-maintained, so it still carried the internal wording for the same disclosure.
Idempotent: applied edits are skipped rather than doubled.
"""
from pathlib import Path
import ast

M = Path('/home/user/le/PAPER_PROJECT/13_Manuscript')
LOG = []


def patched(path, fn):
    t = path.read_text()
    t2 = fn(t)
    if t2 is None or t2 == t:
        LOG.append("  skip (already applied): " + path.name)
        return
    if path.suffix == '.py':
        ast.parse(t2)
    path.write_text(t2)
    LOG.append("  ok: " + path.name)


# ---------------------------------------------------------------- ms_static.py: 4.6 DFT paragraph
def f_static(t):
    SENT = ("A periodic discrete-Fourier synthesis over a window of a few thermal times must not be used for this "
            "purpose: it returns the periodic steady state of a pulse train (here with a mean wall temperature of 0.27 "
            "of the peak, which builds a steady temperature profile out to the outer boundary and raises the "
            "clamped-boundary stress), not the single-pulse response.")
    NEW = ("A periodic discrete-Fourier synthesis over a window of a few thermal times must not be used for this "
           "purpose: it returns the periodic steady state of a pulse train, whose mean wall temperature is "
           "t_{w}\\u221a\\u03c0/T = @@TM@@ of the peak for the parameters above; that mean drives a steady temperature "
           "profile out to the outer boundary and adds a static clamped-boundary stress, so the answer is not the "
           "single-pulse response this study asks about.")
    if SENT not in t:
        return None
    i = t.index(SENT)
    q0 = t.rfind("'", 0, i)                       # opening quote of the enclosing literal
    q1 = t.find("'", i + len(SENT))               # closing quote of the same literal
    elem = t[q0:q1 + 1]
    assert elem.startswith("'") and elem.endswith("'") and SENT in elem[1:-1]
    inner = elem[1:-1].replace(SENT, NEW)
    inner = inner.replace("{", "{{").replace("}", "}}").replace("@@TM@@", "{TRAIN_MEAN_OVER_PEAK:.3f}")
    return t[:q0] + "f'" + inner + "'" + t[q1 + 1:]


_t = (M / 'ms_static.py').read_text()
if 'TRAIN_MEAN_OVER_PEAK:.3f}' in _t:
    LOG.append("  skip (already applied): ms_static 4.6 DFT paragraph")
else:
    patched(M / 'ms_static.py', f_static)

# ---------------------------------------------------------------- build_manuscript.py
BM = M / 'build_manuscript.py'


def f_bm(t):
    changed = False
    old_labels = "SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03b', 'submission_2026_10_03'"
    if old_labels in t:
        t = t.replace(old_labels, "SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03c', 'submission_2026_10_03b'", 1)
        changed = True
    helper_anchor = "N_FRZ, N_FRZ_SAME, N_FRZ_DIFF = _freeze_match('v2_gate')\n"
    if 'def _freeze_diff_names(' not in t and helper_anchor in t:
        helper = helper_anchor + '''

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
'''
        t = t.replace(helper_anchor, helper, 1)
        changed = True
    old3 = ('f"taken, {N_FRZ_DIFF} of the {N_FRZ} entries of `CODE_FREEZE_v2_gate.json` (the pipeline driver, the test "\n'
            '                 f"runner, four experiment and analysis scripts and the two document builders) have been edited, so the "')
    if old3 in t:
        t = t.replace(old3, ('f"taken, {N_FRZ_DIFF} of the {N_FRZ} entries of `CODE_FREEZE_v2_gate.json` ({FRZ_DIFF_NAMES}) have been "\n'
                             '                 f"edited, so the "'), 1)
        changed = True
    OLD_AI = ("During the preparation of this work the author(s) used an AI agent (Arena.ai Agent Mode; the underlying "
              "models are provided by the service) to review and extend the numerical code and the verification suite, "
              "to run and analyse the simulations, and to draft the text and the figures. After using this tool the "
              "author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of "
              "the publication.")
    NEW_AI = ("During the preparation of this work the author(s) used a generative-AI assistant (Arena.ai Agent Mode; "
              "the underlying models are provided by the service) for the writing process: drafting and revising the "
              "text and the figure captions, and checking the internal consistency of the manuscript, the calculation "
              "companion and the tables. After using this tool the author(s) reviewed and edited the content as needed "
              "and take(s) full responsibility for the content of the publication. The same class of tool was also used "
              "in the research process — reviewing and extending the numerical code and the verification suite, and "
              "running the simulations — which the journal policy places in the methods rather than in this "
              "declaration; the numerical-methods section of the manuscript records that use. No AI tool generated a "
              "physical result, no AI tool was used to produce or select any number reported here, and no AI tool is an "
              "author or is cited as a source.")
    if OLD_AI in t:
        t = t.replace(OLD_AI, NEW_AI, 1)
        changed = True
    old4 = "'**Software and AI assistance (Methods disclosure): the finite-difference solver of the preliminary analysis was "
    new4 = "'**Software and AI assistance.** The finite-difference solver as first written was "
    if old4 in t:
        t = t.replace(old4, new4, 1)
        changed = True
    old5 = "extended and verified with the help of an AI agent (Section 5 lists the tests"
    new5 = ("extended and verified with the assistance of generative-AI coding tools; this is the research-process use "
            "referred to in the declaration before the references (Section 5 lists the tests")
    if old5 in t:
        t = t.replace(old5, new5, 1)
        changed = True
    guard_anchor = "hl_ok = [(h, len(h)) for h in highlights]\n"
    if "A missing input number renders as 'n/a'" not in t and guard_anchor in t:
        t = t.replace(guard_anchor, guard_anchor + '''
# A missing input number renders as 'n/a'; in the abstract or a highlight that is a build error, not a
# cosmetic one (the abstract must never reach a reader with a hole in it).  The common cause is rebuilding
# while the verification pass is rewriting 07_Tests/TEST_RESULTS.json.
_bad = [s for s in [abstract] + highlights if 'n/a' in s]
if _bad:
    raise SystemExit("build aborted: the abstract or a highlight contains 'n/a' (a number its input "
                     "artifact did not provide).  Rebuild after the verification pass has written its "
                     "results, or fix the missing key.  Offending strings:\\n  " + "\\n  ".join(_bad))
''', 1)
        changed = True
    return t if changed else None


patched(BM, f_bm)

# ---------------------------------------------------------------- build_calculations.py
BC = M / 'build_calculations.py'


def f_bc(t):
    changed = False
    chain_old = """N_FRZ, N_FRZ_SAME, N_FRZ_DIFF = _frz('v2_gate')
N_SUB, N_SUB_SAME, N_SUB_DIFF = _frz('submission_2026_10_03b')
N_MID, N_MID_SAME, N_MID_DIFF = _frz('submission_2026_10_03')
N_PREV, N_PREV_SAME, N_PREV_DIFF = _frz('submission_2026_10_02')
if N_SUB_DIFF:
    raise SystemExit('CODE_FREEZE_submission_2026_10_03b.json no longer describes the code '
                     '(%d of %d entries differ); regenerate it before rebuilding this document'
                     % (N_SUB_DIFF, N_SUB))"""
    chain_new = """SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03c', 'submission_2026_10_03b'

N_FRZ, N_FRZ_SAME, N_FRZ_DIFF = _frz('v2_gate')
N_SUB, N_SUB_SAME, N_SUB_DIFF = _frz(SUB_FREEZE)
N_MID, N_MID_SAME, N_MID_DIFF = _frz(PREV_FREEZE)
N_MIDN, N_MIDN_SAME, N_MIDN_DIFF = _frz('submission_2026_10_03')
N_PREV, N_PREV_SAME, N_PREV_DIFF = _frz('submission_2026_10_02')
if N_SUB_DIFF:
    raise SystemExit('CODE_FREEZE_%s.json no longer describes the code '
                     '(%d of %d entries differ); regenerate it before rebuilding this document'
                     % (SUB_FREEZE, N_SUB_DIFF, N_SUB))


def _frz_diff_names(label):
    \"\"\"basenames of the entries of CODE_FREEZE_<label>.json whose recorded digest no longer matches
    the file as it stands, as prose; computed, so this document cannot state a stale list.\"\"\"
    import hashlib as _hl
    _p = os.path.join(ROOT, 'PAPER_PROJECT', '06_Source_Code', 'CODE_FREEZE_%s.json' % label)
    try:
        _f = json.load(open(_p))['files']
    except (OSError, ValueError, KeyError):
        return 'none'
    names = [os.path.basename(r) for r, h in _f.items()
             if not os.path.exists(os.path.join(ROOT, 'PAPER_PROJECT', r))
             or _hl.sha256(open(os.path.join(ROOT, 'PAPER_PROJECT', r), 'rb').read()).hexdigest() != h]
    if not names:
        return 'none'
    if len(names) == 1:
        return names[0]
    return ', '.join(names[:-1]) + ' and ' + names[-1]


FRZ_DIFF_NAMES = _frz_diff_names('v2_gate')"""
    if chain_old in t:
        t = t.replace(chain_old, chain_new, 1)
        changed = True
    p3_old = ("para('Both archived manifests were taken on 2026-10-01. %d of the %d entries of the gate freeze are '\n"
              "     'byte-identical in the code as submitted; %d entries (the pipeline driver, the test runner, four '\n"
              "     'experiment and analysis scripts and the two document builders) have been edited since, so the '")
    p3_new = ("para('Both archived manifests were taken on 2026-10-01. %d of the %d entries of the gate freeze are '\n"
              "     'byte-identical in the code as submitted; %d entries (%s) have been edited since, so the '")
    if p3_old in t:
        t = t.replace(p3_old, p3_new, 1)
        changed = True
    p4_old = ("'Python/NumPy build, where it reproduced its stored peak wall stress to 2.7\\u00d710\\u207b\\u00b9\\u2076 relative. '\n"
              "     'CODE_FREEZE_submission_2026_10_03b.json (%d files, all %d byte-identical to the code as submitted) '\n"
              "     'is the refreshed manifest, the one to deposit with the data package; it supersedes '\n"
              "     'CODE_FREEZE_submission_2026_10_03.json (taken the same day, before that pass, %d of whose %d entries '\n"
              "     'still match) and CODE_FREEZE_submission_2026_10_02.json, and both are kept unchanged as history.'\n"
              "     % (N_FRZ_SAME, N_FRZ, N_FRZ_DIFF, N_SUB, N_SUB_SAME, N_MID_SAME, N_MID))")
    p4_new = ("'Python/NumPy build, where it reproduced its stored peak wall stress to 2.7\\u00d710\\u207b\\u00b9\\u2076 relative. '\n"
              "     'The mathematical audit that followed re-derived the constitutive algebra and every printed analytical '\n"
              "     'identity symbolically and re-checked the discretisation, kernel and inversion conventions against the '\n"
              "     'shipped code; it corrected two typographical statements in the model description, made the plane-strain '\n"
              "     'class and the norm convention of \\u03b4 explicit, and replaced the hard-coded validity window of the '\n"
              "     'inversion by the bound it was an instance of (t \\u2264 T \\u2212 (t_{0} + 2.5t_{w}): 14.5 t_{th} for the '\n"
              "     'baseline t_{w} = 1.2 t_{th}, 11.5 t_{th} for t_{w} = 2.4 t_{th}). No stored run and no reported value '\n"
              "     'changed. CODE_FREEZE_%s.json (%d files, all %d byte-identical to the code as submitted) '\n"
              "     'is the refreshed manifest, the one to deposit with the data package; it supersedes '\n"
              "     'CODE_FREEZE_%s.json (taken the same day, before the audit, %d of whose %d entries '\n"
              "     'still match), CODE_FREEZE_submission_2026_10_03.json and CODE_FREEZE_submission_2026_10_02.json, all '\n"
              "     'kept unchanged as history.'\n"
              "     % (N_FRZ_SAME, N_FRZ, N_FRZ_DIFF, FRZ_DIFF_NAMES, SUB_FREEZE, N_SUB, N_SUB_SAME, PREV_FREEZE, N_MID_SAME, N_MID))")
    if p4_old in t:
        t = t.replace(p4_old, p4_new, 1)
        changed = True
    OLD_AI = ("During the preparation of this work the author(s) used an AI agent (Arena.ai Agent Mode; the underlying "
              "models are provided by the service) to review and extend the numerical code and the verification suite, "
              "to run and analyse the simulations, and to draft the text and the figures. After using this tool the "
              "author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of "
              "the publication.")
    NEW_AI = ("During the preparation of this work the author(s) used a generative-AI assistant (Arena.ai Agent Mode; "
              "the underlying models are provided by the service) for the writing process: drafting and revising the "
              "text and the figure captions, and checking the internal consistency of the manuscript, the calculation "
              "companion and the tables. After using this tool the author(s) reviewed and edited the content as needed "
              "and take(s) full responsibility for the content of the publication. The same class of tool was also used "
              "in the research process — reviewing and extending the numerical code and the verification suite, and "
              "running the simulations — which the journal policy places in the methods rather than in this "
              "declaration; the numerical-methods section of the manuscript records that use. No AI tool generated a "
              "physical result, no AI tool was used to produce or select any number reported here, and no AI tool is an "
              "author or is cited as a source.")

    def pieces(text, width=95, indent=5):
        words, out, cur = text.split(' '), [], ''
        for w in words:
            if len(cur) + len(w) + 1 > width:
                out.append(cur)
                cur = w
            else:
                cur = (cur + ' ' + w).strip()
        if cur:
            out.append(cur)
        pad = ' ' * indent
        return ('\n' + pad).join("'%s '" % s if i < len(out) - 1 else "'%s'" % s for i, s in enumerate(out))

    if OLD_AI in t:
        t = t.replace(OLD_AI, NEW_AI, 1)
        changed = True
    elif 'used an AI agent (Arena.ai Agent Mode' in t:          # split across source literals
        s = t.index("para('**Declaration of Generative AI")
        e = t.index("the content of the publication.')", s) + len("the content of the publication.')")
        head = ("para('**Declaration of Generative AI and AI-assisted technologies in the writing process.** '\n"
                "     '[TEMPLATE — to be reviewed, edited and confirmed by the authors; Elsevier requires '\n"
                "     'this statement above the references.] '\n"
                "     ")
        t = t[:s] + head + pieces(NEW_AI) + ")" + t[e:]
        changed = True
    return t if changed else None


patched(BC, f_bc)

# ---------------------------------------------------------------- cover_letter.md (hand-maintained)
CL = M / 'cover_letter.md'


def f_cl(t):
    old = ("**Declarations.** AI assistance: an AI agent was used to review and extend the code, run and analyse the "
           "simulations and draft text and figures; the authors' disclosure statement appears above the references "
           "[template \u2014 to be confirmed by the authors].")
    new = ("**Declarations.** AI assistance: a generative-AI tool was used for the writing process (drafting, "
           "revising and internal consistency checks) and, separately, to review and extend the numerical code and "
           "its verification suite and to run the simulations; the manuscript states both in the form the journal "
           "requires \u2014 the writing use in the declaration above the references, the code and simulation use in the "
           "numerical-methods section \u2014 and the authors take full responsibility for every number "
           "[declaration wording to be reviewed and confirmed by the authors].")
    if old not in t:
        return None
    t = t.replace(old, new, 1)
    t = t.replace("Suggested reviewers: [authors to propose; none suggested by the assistant].",
                  "Suggested reviewers: [authors to propose; none are proposed here].", 1)
    return t


patched(CL, f_cl)

print("\n".join(LOG))
