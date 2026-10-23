# V-B9b — The thermal-channel factor: `T₀/T` or `T/T₀` in EQ-10.12 / EQ-10.14?

**Order:** `control/BRAVE_B9.md` item 2 @ `origin/claude/control` `79999f7`. **Access date:** 2026-10-22.
**Code:** `V-B9a_checks.py` CHECK 4. **Scope of this file: the thermal channel of a time-averaged,
linearized, harmonic energy flux — nothing else.**

---

## 1. Task

Resolve the `T₀/T` vs `T/T₀` factor in **EQ-10.12** (and its twin EQ-10.14) from the **rendered page** of
Sci Rep 2023 eq (45) — a page render, not the text layer — and derive which form is dimensionally and
thermodynamically right for `q_total = σ v + q` with `q = −K∇T`, under the entropy-flux convention.
State the sub-system.

## 2. Method

1. **Which equation is in question.** The factor appears in the **legacy** register
   (`phase4/…/appA_equation_register.tex:114,116`) and in **legacy** `sections/sec10_energy.tex:114`
   (eq `eq:10.9`), plus its caption (`:185`) and prose (`:118`). The **live** register's §10 is
   `EQ-10.1–10.6, 10.11–10.13` and the live `sec10_energy.tex` no longer prints a three-channel flux at
   all — so **no live row asserts the factor**. The live `EQ-10.12` is `ΣR + ΣT = 1`, which is a
   different (and correct) statement, audited in `V-B9a` and `V-B9c`.
2. **Render evidence.** Fetched the **publisher PDF** of `10.1038/s41598-023-44339-5`
   (`nature.com/articles/s41598-023-44339-5.pdf`, 11 chunks; chunk 4 carries the energy section). In the
   PDF, eq (45) reads (transcribed from the rendered equation, alt-math preserved):
   `P = −Re( σ₁₃ ū̇₁ + σ₃₃ ū̇₃ − φ D̄̇₃ + K₃ T̄,₃ · T/T₀ )`.
   The **HTML** rendering read earlier in B8a/V-B7b gives the same factor. Two independent rendering
   paths agree, so the printed factor is **`T/T₀`**, not `T₀/T`.
3. **Convention in the source.** `T` in Barak et al. is the **temperature increment**: eq (37) writes the
   temperature field as `T = Σ Θ_i H_i exp[iω(−x₁/c − q_i x₃ + t)]`, eq (38) imposes `T = Tᵉ`
   (continuity of the increments), eq (10) uses `βᵉT₀ᵉ ∂ₜₜ(∇·uᵉ)` with `Tᵉ` the increment, and eq (15)
   writes `ρC_E T̈ + T₀(β₁ü₁,₁ + …)`. Their nomenclature row "T = thermal temperature" is loose; the
   equations are all increment-based.
4. **The manuscript's convention.** `frontmatter/notation.tex:24` (both trees): "`T` — Temperature
   increment, `T − T₀`"; live `sec03_foundations.tex:449` writes it `Θ − T₀`. So in the manuscript `T` is
   also the increment. This is what settles the verdict — see §3.2.
5. **Dimension check first, as ordered.** *It does not decide anything.* `T/T₀` and `T₀/T` are both
   dimensionless, and `K_iT,_{i}` is `W m⁻²` either way. A dimensional argument can only eliminate a
   form if `T` means the increment, in which case `T₀/T = T₀/θ` has units `K/K` only by courtesy of a
   dimensionless ratio that diverges as `θ → 0`. The deciding test is the **second-order time average**.

## 3. Result

### 3.1 The derivation (two lines of algebra, done twice)

The exact energy flux of a thermoelastic conductor is `J = q − σv` — **no temperature ratio**
(`V-B3d` §2.4, obtained by combining momentum × v, the constitutive law × ε̇ and the heat equation ×
θ/T₀). For a harmonic field `T = T₀ + θ` with `⟨θ⟩ = 0`, `q` is first order and `⟨q⟩ = 0`, so the *mean*
thermal flux is the second-order quantity

  `⟨J_th⟩ = ⟨θ q⟩ / T₀`   … (★)

(★) is not an assumption: in `V-B3d` §3.4 the numerical implementation of `(1/2T₀)Re[θ̂q̂*]` was checked
against an independent bulk-dissipation integral and closed to `10⁻⁶`–`10⁻⁵` in every frequency row, for
Biot and LS, while the wrong normalisation (`T₀²` instead of `T₀`) failed to close. That check is the
second method.

Now expand the printed thermal channel `K₃T,₃·(factor)` with `K T,₃ = −q` (valid in the source and in
the manuscript, both of which use `q = −K∇T`), inside the source's **own** bracketing
`P = −Re[…]`:

| printed factor | bracket term | `P_th = −Re[bracket]` averaged |
|---|---|---|
| `T/T₀` (source; `T = θ`) | `−q·θ/T₀` | `+⟨θq⟩/T₀` ✔ matches (★) |
| `T₀/T` (legacy register and legacy §10) | `−q·(1 − θ/T₀)` | `−⟨θq⟩/T₀` ✘ sign inverted, and zero at first order |

`V-B9a_checks.py` CHECK 4 prints exactly this table. The `T₀/T` form is not merely "a different but
equivalent normalisation": it produces **minus** the correct mean thermal flux, and because the error is
second order it is invisible to any first-order or dimensional check — which is presumably how it
survived into a row tagged `VERIFIED`.

### 3.2 Which one is "thermodynamically right"

Under the entropy-flux convention the energy flux is temperature × entropy flux, `T(q/T)`. Expanded
about `T₀` this gives `q` exactly, and to the order at which a harmonic mean is non-zero it gives
`q·θ/T₀` — i.e. the flux **weighted by the relative temperature excess**. `T/T₀` *is* that weight;
`T₀/T` is its reciprocal, which is the weight that appears in the **entropy** flux
`q/T ≈ (q/T₀)(1 − θ/T₀)`, not in the energy flux. So: the right multiplier of `K∇T` in the energy
channel, in the source's convention, is `θ/T₀` = `T/T₀` (T = increment). Under the manuscript's own
notation table, `T` *is* the increment, so the manuscript's `T₀/T` is `T₀/θ`: not a weight at all, and
singular as `θ → 0`. There is no notation in which the legacy tuple (increment `T`, bracketing
`−Re[…]`, `+K_iT,_{i}`) makes `T₀/T` correct.

### 3.3 Verdict (scoped)

* **Legacy appA `EQ-10.12` and `EQ-10.14`, legacy `sec10_energy.tex:114/118/185`: `WRONG-CONFIRMED`** —
  factor inverted, with respect to the source they cite, in the thermal channel of a time-averaged
  harmonic flux. Sub-system: linearized thermoelasticity/piezothermoelasticity, harmonic `e^{−iωt}`,
  time average, entropy-flux convention, `T` = increment. Not disputed: the three-channel *structure*
  (mechanical + electrical + thermal), the mechanical and electrical channels, or any non-harmonic use.
* **The `VERIFIED` tag is unsupported** for a second, independent reason: the note claims confirmation
  "across 8 full-text sources" (P05, P07, P08, P11, P12, P14, P23, P25). I have read **one** of the
  eight (P05 = the Sci Rep 2023 paper above) and it **disagrees**. The other seven are not in my hands
  (`PDF_REQUEST_LIST.csv` carries five of them as closed/journal-only). One source, disagreeing, cannot
  support "8/8 confirmed".
* **Live register: no equivalent row**, so this is a legacy-tree defect only. Live `EQ-10.12`
  (`ΣR+ΣT=1`, lossless limit, cross-term caveat) is `CORRECT-CONDITIONAL` and unaffected.

### 3.4 A note on the source's own consistency

The same paper's eq (53), the transmitted-wave flux, normalises the thermal term by `T₀` alone
(`(ι/ω)(K₃/T₀)Δ̄₅sΘ_s`), not by `T/T₀`. That is consistent with (★): in the mode-flux formula the
`θ/T₀` weight is already absorbed into the amplitude products. So the source is internally consistent
on the normalisation; only the legacy register's transcription is not.

## 4. Evidence / sources

* Barak, M. S.; Ahmad, H.; R. Kumar; R. Kumar; Gupta, V.; Awwad, F. A.; Ismail, E. A. A. (2023).
  "Behavior of higher-order MDD on energy ratios at the interface of thermoelastic and
  piezothermoelastic mediums." *Scientific Reports* **13** (article number not captured in my page reads).
  DOI `10.1038/s41598-023-44339-5`. Gold OA.
  Access 2026-10-22, publisher PDF, `nature.com/articles/s41598-023-44339-5.pdf`, chunks 1–6 of 11;
  equations (1)–(10), (36)–(45), (47)–(58) read in the rendered PDF. Access level: **FULL** for those
  sections.
* Manuscript: `phase4/manuscript/appendices/appA_equation_register.tex` lines 114, 116;
  `phase4/manuscript/sections/sec10_energy.tex` lines 114, 118, 185;
  `phase4/manuscript/frontmatter/notation.tex:24`; `phase5/master/frontmatter/notation.tex:24`.
* `V-B3d_coupled-interface-rta.md` §2.4 and §3.4 (the independent dissipation-integral check of `θq/T₀`).
* `V-B9a_checks.py` CHECK 4 (the expansion table above, reproducible).

## 5. Checks done

1. **Two rendering paths** (PDF this session; HTML in B8a) give the same factor `T/T₀` — the render
   requirement in the order is met, and the HTML-only reading is no longer the sole basis.
2. **Notation checked on both sides** before calling the factor wrong: source `T` = increment (eqs 10,
   15, 37, 38), manuscript `T` = increment (notation tables in both trees). Without this step the
   verdict would have been "convention-dependent" instead of WRONG.
3. **Dimension check performed and explicitly found non-decisive** (both ratios dimensionless); the
   deciding test is stated instead of pretending a dimension argument settles it.
4. **Second method for (★):** an independent numerical dissipation integral (`V-B3d` §3.4) rather than
   a second algebraic manipulation of the same expression.
5. **Grep of my own V-files before the WRONG verdict** (standing rule): `V-B8a` §3.3/§3.8 records this
   as `UNRESOLVED`; `V-B7b:75` records the source's `T/T₀` from the HTML. Neither contradicts the
   verdict; B8a's `UNRESOLVED` is now closed.
6. Confirmed the defect does **not** exist in the live tree, so the verdict cannot be read as a
   live-manuscript finding.

## 6. Confidence

* What the source prints (`T/T₀`): **HIGH** (two renders, same equation, same position).
* The algebra of §3.1 and the sign inversion: **HIGH** (one-line expansion, checked by script).
* "`T₀/T` is wrong rather than merely differently normalised": **HIGH** under the manuscript's own
  `T` = increment notation; it would drop to "wrong in the cited convention, defensible in an
  absolute-temperature convention" if the manuscript used `T` for absolute temperature — it does not,
  and its own notation table says so.
* Thermodynamic reading (`T/T₀` = relative-excess weight; `T₀/T` = entropy-flux reciprocal): **MEDIUM** —
  this is a correct statement of the entropy-flux construction, but "thermodynamically right" is a
  judgement about which expansion is retained, and I state the sub-system for that reason.

## 7. NOT verified / open issues

* **Seven of the eight named sources were not read** (P07 IJP 2023, P08 HFF 2023, P11 HFF 2023, P12 MMMS
  2023, P14 JTS 2024, P23 IJAME 2024, P25 MTDM 2024). If one of them genuinely prints `T₀/T` *and*
  uses absolute-temperature notation, the register's "8 sources" claim would still be a claim about
  structure, not about the factor — but I cannot say what they print. Status: **UNVERIFIED**, not
  "disagreeing".
* I did not open Tzou's book or the 1995/1997 papers for this item; the entropy-flux convention used
  here is the standard one and matches my own verified computation, not a citation.
* The source's nomenclature is internally loose ("T = thermal temperature" while the equations use the
  increment). I used the equations. A reader who follows only the nomenclature would reconstruct a
  different reading of eq (45); that ambiguity is in the source and is recorded, not resolved.
* Not checked: whether any *live* prose (not the register) still mentions `T₀/T`. The string search over
  the live tree returned no occurrence outside `phase4/`, but a paraphrase ("reference temperature over
  local temperature") would evade a string search and I did not read live §10 for it beyond the
  equation check.
