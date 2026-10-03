#!/usr/bin/env python3
"""patch_phase3_batch1.py — Phase 3 (mathematical audit), part 1 of 2: source and model text.

Re-applies the audit's document and code edits idempotently (an edit whose replacement is already present is
skipped), so the script is safe to re-run after a workspace restore. Every entry is a correction the audit
established or a disclosure wording change; no reported result is altered and no number is re-rounded.

batch1: cg_bromwich.py (the inversion's validity bound), ms_static.py (computed convention helpers, the
plane-strain class paragraph, the delta-norm sentence, Table 4 wording), ms_derivation.py (Eq. (33), the
c_ref typo, two wording items), ms_numerics.py and ms_results.py (the superseded-scheme comparison, the
frozen/internal wording, the feedback sentence).  batch2: the AI declaration split, the freeze-chain
bookkeeping, the numerical-methods disclosure and the cover letter.
"""
from pathlib import Path
import ast

MS = Path('/home/user/le/PAPER_PROJECT/13_Manuscript')
SRC = Path('/home/user/le/PAPER_PROJECT/06_Source_Code/src')
LOG = []


def sub(path, old, new, label):
    t = path.read_text()
    if t.count(old) == 0 and t.count(new) >= 1:
        LOG.append("  skip (already applied): " + label)
        return
    n = t.count(old)
    assert n == 1, f"{path.name}: {n} matches for {old[:70]!r} [{label}]"
    t = t.replace(old, new, 1)
    ast.parse(t)
    path.write_text(t)
    LOG.append("  ok: " + label)


# ===================================================================== src/cg_bromwich.py
B = SRC / 'cg_bromwich.py'
sub(B, "    @property\n    def t_valid_max(self):\n        return self.T - 5.5",
    "    @property\n    def t_valid_max(self):\n"
    "        \"\"\"Largest time for which the backward image e^{+gamma*T}*y(t-T) is negligible.  A Gaussian pulse\n"
    "        has no compact support, so the bound follows from the pulse width rather than from causality:\n"
    "        t <= T - (t0 + 2.5*tw), i.e. 2.5 widths of pre-history, where the image is exp(-6.25) ~ 2e-3 of\n"
    "        the peak and e^{+gamma*T} * that is still far below the forward alias e^{-gamma*T}.  The previous\n"
    "        hard-coded T - 5.5 was this expression for the baseline tw = 1.2 and was too generous for wider\n"
    "        pulses (tw = 2.4 gives 11.5, not 14.5), which is the case used in the locality test.\n"
    "        \"\"\"\n"
    "        return self.T - (self.t0 + 2.5 * self.tw)", "C4: t_valid_max computed from the pulse width")
sub(B, "exp(-18) = 1.5e-8, valid for 0 <= t <= T - 5.5 = 14.5.",
    "exp(-18) = 1.5e-8; validity 0 <= t <= T - (t0 + 2.5*tw) = 14.5 for the baseline tw = 1.2 (11.5 for\ntw = 2.4: "
    "the bound tracks the pulse width, so wide-pulse runs are read only inside the peak window).",
    "C4: module header states the width dependence")

# ===================================================================== ms_static.py: computed helpers
S = MS / 'ms_static.py'
sub(S, "import cg_model as M\n", "import cg_model as M\nimport cg_bromwich as cb\n", "cb import for the plan constants")

HELPERS = '''
_A1, _A2, _A3 = M.alpha_crys
_Q0, _b0 = M.plane_strain_block()
_CBAR = M.Cij_GPa['C33'] * 1e9

_PLAN = cb.BromwichPlan()
TRAIN_MEAN_OVER_PEAK = float(_PLAN.tw * np.sqrt(np.pi) / _PLAN.T)


def delta_tensor_norm():
    """delta with the full tensor contraction beta:beta instead of the in-plane triple norm."""
    C = M.Cij_GPa
    b22 = (C['C12'] * _A1 + C['C22'] * _A2 + C['C23'] * _A3) * 1e9
    return M.T0 * (_b0[0] ** 2 + _b0[1] ** 2 + 2 * _b0[2] ** 2 + b22 ** 2) / (M.rho * M.cp_ESTIMATED * _CBAR)


def delta_orientation_spread():
    """delta on the phi-lattice with the same in-plane triple norm as delta_tensor_norm()."""
    ph = np.deg2rad(np.arange(0.0, 360.0, 1.0))
    v = []
    for p in ph:
        b = M.rotate_Q_beta(_Q0, _b0, p)[1]
        v.append(M.T0 * (b[0] ** 2 + b[1] ** 2 + 2 * b[2] ** 2) / (M.rho * M.cp_ESTIMATED * _CBAR))
    v = np.asarray(v)
    return float(v.min()), float(v.max())


def plane_strain_convention_sensitivity():
    """relative change of Q and beta if sigma_22 = 0 were imposed instead of u_2 = 0 (generalised plane
    strain versus the kinematic plane strain the solver actually uses)."""
    C = M.Cij_GPa
    C6 = np.zeros((6, 6))
    for i in range(6):
        C6[i, i] = C[f'C{i+1}{i+1}']
    for (i, j, k) in [(0, 1, 'C12'), (0, 2, 'C13'), (1, 2, 'C23'), (0, 4, 'C15'),
                      (1, 4, 'C25'), (2, 4, 'C35'), (3, 5, 'C46')]:
        C6[i, j] = C6[j, i] = C[k]
    ix = [0, 2, 4]
    S22 = C6[1, 1] * 1e9
    S2i = C6[1, ix] * 1e9
    Sii = C6[np.ix_(ix, ix)] * 1e9
    Qg = Sii - np.outer(S2i, S2i) / S22
    bg = np.array([(C['C11'] * _A1 + C['C12'] * _A2 + C['C13'] * _A3) * 1e9,
                   (C['C13'] * _A1 + C['C23'] * _A2 + C['C33'] * _A3) * 1e9,
                   (C['C15'] * _A1 + C['C25'] * _A2 + C['C35'] * _A3) * 1e9])
    b22 = (C['C12'] * _A1 + C['C22'] * _A2 + C['C23'] * _A3) * 1e9
    bg = bg - S2i * b22 / S22
    return (float(np.abs(Qg - _Q0).max() / np.abs(_Q0).max() * 100.0),
            float(np.abs(bg - _b0).max() / np.abs(_b0).max() * 100.0))


DELTA_T = delta_tensor_norm()
DELTA_MIN, DELTA_MAX = delta_orientation_spread()
SPREAD_REL = abs(DELTA_MAX / DELTA_MIN - 1.0)
PSQ, PSB = plane_strain_convention_sensitivity()

'''

t = S.read_text()
if 'def delta_tensor_norm():' not in t:
    anchor = "KEV = np.linalg.eigvalsh(K)\n"
    assert t.count(anchor) == 1, "ms_static: KEV anchor not found"
    t = t.replace(anchor, anchor + HELPERS, 1)
    ast.parse(t)
    S.write_text(t)
    LOG.append("  ok: computed-convention helpers")
else:
    LOG.append("  skip (already applied): computed-convention helpers")

# ===================================================================== ms_static.py: 2.1, 2.2, Table 4
sub(S, "        ('h2', '2.2 Dimensionless groups'),",
    "        ('p', f'The class is the kinematic plane strain: the fields are independent of x_{2} and u_{2} = 0. '\n"
    "              'For a monoclinic crystal with the unique axis normal to the plane the out-of-plane shear '\n"
    "              'stresses σ₁₂ and σ₂₃ vanish identically for every in-plane strain, so no relaxation step is '\n"
    "              'needed to make the constraint admissible and σ₂₂ enters as a reaction, not as a boundary '\n"
    "              'condition. The distinction is stated because the alternative convention — generalised plane '\n"
    "              f'strain, σ₂₂ = 0 — is not equivalent here: it would change the plane-strain block Q by {PSQ:.1f}% '\n"
    "              f'and the thermal-stress vector β by {PSB:.1f}% at the parameters of @@tab:params@@, so the class is '\n"
    "              'stated explicitly and the solver is built on the constraint, not on the stress.'),\n"
    "        ('h2', '2.2 Dimensionless groups'),", "A-P3: 2.1 plane-strain class paragraph")

sub(S, "where C\\u0304 = C_{{33}} is the stiffness scale of the plane-strain block. With the outer boundary at R = 80a",
    "where C\\u0304 = C_{{33}} is the stiffness scale of the plane-strain block and the norm in '\n"
    "              '@@eq:groups@@ is formed from the in-plane triple (β₁₁, β₃₃, β₁₃) with the shear slot weighted by 2, '\n"
    "              'the same triple that enters the thermal-stress scale γ_T of Section 3; the full tensor '\n"
    "              f'contraction β:β would give {DELTA_T*1e3:.3f}\\u00d710^{{\\u22123}}, a factor '\n"
    "              f'{DELTA_T/DELTA_MIN:.2f} larger, because it also counts the out-of-plane component β₂₂ that the '\n"
    "              'plane-strain class never uses. The triple norm is the in-plane part of the tensor contraction and '\n"
    "              f'is therefore invariant under in-plane rotation of the crystal (relative spread {SPREAD_REL:.0e} over '\n"
    "              'the 360-orientation lattice), so δ is a material constant of this model and not a directional '\n"
    "              'statistic; it is still only an order-of-magnitude criterion for Section 3.4, and the convention '\n"
    "              f'is stated for that reason. With the outer boundary at R = 80a",
    "P3-delta-norm: 2.2 convention sentence (tail stays an f-string)")

sub(S, "feedback number is \\u03b4 = T_{{0}}\\u03b2\\u00b7\\u03b2/(\\u03c1c_{{p}}C\\u0304)",
    "feedback number is \\u03b4 = T_{{0}}\\u2016\\u03b2\\u2016^{{2}}/(\\u03c1c_{{p}}C\\u0304)",
    "P3-delta-norm: 2.2 prose norm symbol")

sub(S, "'Parameters of the study and their status (MASTER_PROMPT classification: literature / assumed / "
       "hypothetical / design).'",
    "'Parameters of the study and their status (classification: literature / assumed / hypothetical / design).'",
    "A7: Table 4 caption drops the internal brief's name")
sub(S, "'80; t_{0} = 2.5, t_{w} = 1.2 t_{th}', 'design', 'pre-registered'",
    "'80; t_{0} = 2.5, t_{w} = 1.2 t_{th}', 'design', 'fixed in the design note before the production runs'",
    "A7: Table 4 provenance value")

# ===================================================================== ms_derivation.py
D = MS / 'ms_derivation.py'
sub(D, r"r'\epsilon=\frac{\bar\kappa}{c_{ref}a},\qquad \delta=\frac{T_0\,\boldsymbol{\beta}\cdot\boldsymbol{\beta}}'",
    r"r'\epsilon=\frac{\bar\kappa}{c_{ref}a},\qquad \delta=\frac{T_0\,\Vert\boldsymbol{\beta}\Vert^{2}}'",
    "P3-delta-norm: Eq. (33) printed form (mathtext parses \\Vert, not \\lVert)")
sub(D, "f'with c_{{ref}} = (\\u03c1^{{1}}C_{{33}}/\\u03c1)^{{1/2}} = {C_REF:.0f} m/s",
    "f'with c_{{ref}} = (C_{{33}}/\\u03c1)^{{1/2}} = {C_REF:.0f} m/s", "typo: stray rho in c_ref")
sub(D, "the same time scale. This motivates the frozen criterion used in Section 6.4: the feedback is negligible if '",
    "the same time scale. This motivates the criterion used in Section 6.4: the feedback is negligible if '",
    "A7: 'frozen criterion'")
sub(D, "f'defect that the earlier internal analysis carried and that tests U1 and V3 now exclude (Section 5.1).'",
    "f'defect carried by a superseded version of this analysis, which tests U1 and V3 now exclude (Section 5.1).'",
    "A7: 'earlier internal analysis'")

# ===================================================================== ms_numerics.py
NU = MS / 'ms_numerics.py'
sub(NU, "              'period T, in which the mean wall temperature is 0.27 of the peak, a steady temperature profile reaches the '\n"
         "              'outer boundary and the clamped boundary raises the stress. The two answers differ by more than the effects '\n"
         "              'studied here, which is why the earlier internal analysis had to be recomputed.'),",
    "              f'period T: the imposed wall temperature is then not a single pulse but a train with a nonzero mean '\n"
    "              f'of t_{{w}}\u221a\u03c0/T = {PLAN.tw*np.sqrt(np.pi)/PLAN.T:.3f} of its peak, a steady temperature profile '\n"
    "              'reaches the outer boundary, and the clamped boundary adds a static stress. The question posed in '\n"
    "              'Section 1 is the response to one isolated pulse, which is why the inversion of Eq. (@@eq:brom@@) is '\n"
    "              'used instead of a windowed Fourier synthesis of the sampled history.'),",
    "P3-0.27: computed train mean replaces the unsourced figure")
sub(NU, "'and the pre-registered detection criterion for the modulation is",
    "'and the detection criterion for the modulation, fixed before the production runs, is",
    "A7: 'pre-registered' criterion")

# ===================================================================== ms_results.py
R = MS / 'ms_results.py'
sub(R, "against the frozen bound 5δ = {sci(T3.get('bound_5delta'), 2)} (T3: {T3.get('status')}); the peak stress "
       "changes by {pc(T3.get('peak_stress_change'), 3)}.",
    "against the criterion 5δ = {sci(T3.get('bound_5delta'), 2)}, which the measurement satisfies by a factor "
    "{T3.get('bound_5delta')/max(T3.get('max_rel_dev'), 1e-300):.1f}; the peak stress changes by "
    "{pc(T3.get('peak_stress_change'), 3)}.", "C6/A7: 6.4 feedback sentence")
sub(R, "against the frozen criterion 10^{{−8}} (T1:", "against the criterion 10^{{−8}} (T1:",
    "A7: 'frozen criterion' (T1)")
sub(R, "the frozen threshold is max(5u_{{num}}, 2%)", "the detection threshold max(5u_{{num}}, 2%)",
    "A7: 'frozen threshold' (T4)")
sub(R, "against the frozen criterion.\",", "against the criterion.\",", "A7: 'frozen criterion' (highlight)")
sub(R, "the earlier internal analysis (periodic-pulse synthesis, rotation-tensor sign error, coarser wall mesh) "
       "compared with this work.",
    "a superseded version of the analysis (periodic-pulse synthesis, rotation-tensor sign error, coarser wall "
    "mesh) compared with this work, kept to show what the recomputation changed.",
    "A7: Fig. 5b caption")
sub(R, "the preliminary internal analysis from which this study started contained",
    "a superseded preliminary version of the analysis from which this study started contained",
    "A7: 6.2 limitations bullet")
sub(R, "are the pre-registered coarser set, kept for continuity.",
    "are the coarser set retained from the earlier design, kept for continuity.",
    "A7: ablation-table caption")
sub(R, "The pre-registered collapse in Λ alone therefore fails", "The collapse in Λ alone therefore fails",
    "A7: 6.4 collapse sentence")
sub(R, "turns the pre-registered hypothesis of collapse in Λ into a statement",
    "turns the hypothesis of collapse in Λ, fixed before the runs, into a statement",
    "A7: 6.1 contribution bullet")
sub(R, "# set when it is present; the 96x48 pre-registered set stays in the same table for continuity.  EAB_GRID is",
    "# set when it is present; the 96x48 coarser set stays in the same table for continuity.  EAB_GRID is",
    "comment aligned")
sub(R, "if EAB is EAB_M and EAB_T48.get('baseline_6phi'):      # the pre-registered coarser set, kept for continuity",
    "if EAB is EAB_M and EAB_T48.get('baseline_6phi'):      # the coarser set from the earlier design, kept for continuity",
    "comment aligned (2)")

print("\n".join(LOG))
print()
for f in (B,) + tuple(sorted(MS.glob('ms_*.py'))):
    ast.parse(f.read_text())
print("  all touched files parse OK")

import sys
sys.path.insert(0, str(MS)); sys.path.insert(0, str(SRC))
import ms_static as SS
print("  DELTA_T = %.4e   DELTA_MIN = %.7e   spread_rel = %.1e   PSQ = %.2f%%  PSB = %.2f%%  train mean = %.4f"
      % (SS.DELTA_T, SS.DELTA_MIN, SS.SPREAD_REL, SS.PSQ, SS.PSB, SS.TRAIN_MEAN_OVER_PEAK))
