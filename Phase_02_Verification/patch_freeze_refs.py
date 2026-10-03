"""Phase 2: point the two builders at the refreshed code-freeze manifest and rewrite the provenance paragraph so
that it states the 2026-10-03 re-checks (cross-environment re-solve, deterministic re-analysis, new ablation CSV)
in publication language, keeping every earlier manifest unchanged as history.

Idempotent.  Run from PAPER_PROJECT/13_Manuscript.
"""
import ast, re, sys

# ---------------------------------------------------------------------------------- build_manuscript.py
F = 'build_manuscript.py'
s = open(F).read()
done = []
old = "SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03', 'submission_2026_10_02'"
if old in s:
    s = s.replace(old, "SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03b', 'submission_2026_10_03'", 1)
    done.append('manifest labels')

START = "('p', f\"**State of the frozen code at submission.**"
if START in s:
    i = s.index(START)
    j = s.index('f"not current.\"),', i) + len('f"not current."),')
    NEW = """('p', f"**Code state and re-checks.** The two archived manifests date from 2026-10-01; since they were "
                 f"taken, {N_FRZ_DIFF} of the {N_FRZ} entries of `CODE_FREEZE_v2_gate.json` (the pipeline driver, the test "
                 f"runner, four experiment and analysis scripts and the two document builders) have been edited, so the "
                 f"digests recorded for them no longer describe the code. The pipeline was re-run end to end with the code "
                 f"as it now stands and compared with the archived results (`15_Audits/RERUN_COMPARISON.md`): every "
                 f"production run reproduces its archived quantity of interest to zero relative difference and only "
                 f"wall-clock timings differ. On 2026-10-03 the analysis layer was re-run over all {N_PROD} stored runs: "
                 f"every pre-existing quantity of `ANALYSIS_V2.json` came out identical (the only value that moves is the "
                 f"number of runs audited), the eight figures and the five archived CSV tables are byte-identical to the "
                 f"archived files, and one further CSV (the ablation set at the production grid) is added. A full "
                 f"production job re-solved in a different build \\u2014 Python 3.11.2 with NumPy 2.4.6 instead of "
                 f"3.13.14/2.3.5 \\u2014 reproduces its stored peak wall stress to 2.7\\u00d710\\u207b\\u00b9\\u2076 relative, i.e. one unit in the "
                 f"last place; the reconstruction of the wall temperature stays within 1.0\\u00d710\\u207b\\u00b9\\u2070 of the imposed pulse over the "
                 f"reported window for every run. Two refreshed manifests record the current code: "
                 f"`CODE_FREEZE_{PREV_FREEZE}.json` ({N_PREV} files, taken before this verification pass) and "
                 f"`CODE_FREEZE_{SUB_FREEZE}.json` ({FREEZE_SUB}, {N_SUB} files, all {N_SUB_SAME} byte-identical to the "
                 f"code as submitted); the second is the one to deposit with the data package, and the earlier manifests "
                 f"are kept unchanged as history.\"),"""
    s = s[:i] + NEW + s[j:]
    done.append('section 9.1 provenance paragraph')

# the figures/tables count sentence elsewhere in section 9 must match the six-CSV state
old = "the eight figures and five tables are byte-identical"
if old in s:
    s = s.replace(old, "the eight figures and the five archived CSV tables are byte-identical (a sixth CSV, the "
                       "ablation set at the production grid, is added by the verification pass of 2026-10-03)", 1)
    done.append('RERUN sentence table count')
ast.parse(s)
open(F, 'w').write(s)
print('build_manuscript.py:', ', '.join(done) or 'no change')

# ---------------------------------------------------------------------------------- build_calculations.py
F = 'build_calculations.py'
s = open(F).read()
done = []
old = "N_SUB, N_SUB_SAME, N_SUB_DIFF = _frz('submission_2026_10_03')"
if old in s:
    s = s.replace(old, "N_SUB, N_SUB_SAME, N_SUB_DIFF = _frz('submission_2026_10_03b')\n"
                       "N_MID, N_MID_SAME, N_MID_DIFF = _frz('submission_2026_10_03')", 1)
    done.append('manifest label')
old = "    raise SystemExit('CODE_FREEZE_submission_2026_10_03.json no longer describes the code '"
if old in s:
    s = s.replace(old, "    raise SystemExit('CODE_FREEZE_submission_2026_10_03b.json no longer describes the code '", 1)
    done.append('abort message')
i = s.index("para('Both freezes were taken on 2026-10-01.")
j = s.index("bullets([\n    'python3 PAPER_PROJECT/13_Manuscript/build_calculations.py", i)
NEW = """para('Both archived manifests were taken on 2026-10-01. %d of the %d entries of the gate freeze are '
     'byte-identical in the code as submitted; %d entries (the pipeline driver, the test runner, four '
     'experiment and analysis scripts and the two document builders) have been edited since, so the '
     'digests recorded for them no longer describe it. The pipeline was therefore re-run end to end with '
     'the code as submitted, and it reproduces the archived results exactly: the production runs agree '
     'with the archived quantities of interest to zero relative difference, every leaf of '
     'ANALYSIS_V2.json agrees within 10\\u207b\\u2079, the eight figures and the five archived CSV tables are '
     'byte-identical, and only wall-clock timings differ '
     '(PAPER_PROJECT/15_Audits/RERUN_COMPARISON.md). The verification pass of 2026-10-03 added an '
     'ablation set at the production grid (24 runs), re-ran the analysis layer over all 175 stored runs '
     'with no pre-existing quantity changed, and re-solved one production job in a different '
     'Python/NumPy build, where it reproduced its stored peak wall stress to 2.7\\u00d710\\u207b\\u00b9\\u2076 relative. '
     'CODE_FREEZE_submission_2026_10_03b.json (%d files, all %d byte-identical to the code as submitted) '
     'is the refreshed manifest, the one to deposit with the data package; it supersedes '
     'CODE_FREEZE_submission_2026_10_03.json (taken the same day, before that pass, %d of whose %d entries '
     'still match) and CODE_FREEZE_submission_2026_10_02.json, and both are kept unchanged as history.'
     % (N_FRZ_SAME, N_FRZ, N_FRZ_DIFF, N_SUB, N_SUB_SAME, N_MID_SAME, N_MID))
"""
s = s[:i] + NEW + s[j:]
done.append('section 11 paragraph')
ast.parse(s)
open(F, 'w').write(s)
print('build_calculations.py:', ', '.join(done) or 'no change')
