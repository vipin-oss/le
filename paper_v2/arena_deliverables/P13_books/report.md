# P13 — book evidence for the "Wider material classes" sentences

Scope: evidence only. No `.tex` was edited, no script outside this folder was edited, no PDF and no
library location is recorded here. Six books were re-read chapter by chapter after locating each
chapter in its table of contents; nothing was read cover to cover. Quotes are at most 15 words and
carry an equation or theorem number plus the **printed** page. Where the book itself prints an
ISBN or a DOI, it is recorded; nothing is inferred from a catalogue.

Deliverables in this folder: `report.md`, `evidence.csv` (63 rows), `books_status.csv`,
`books_inventory.csv` (the P12 inventory, see §9), `refs_P13.bib`, `check_p13.py`.

---

## 1. What was found

Six files, all identified positively from their own title and copyright pages:

| key | book | edition / year | pages | state |
|---|---|---|---|---|
| Tzou2015 | *Macro- to Microscale Heat Transfer: The Lagging Behavior* | 2nd, Wiley 2015 | 573 | complete |
| Eringen1999 | *Microcontinuum Field Theories I: Foundations and Solids* | Springer 1999 | 336 | complete |
| Ignaczak2010 | *Thermoelasticity with Finite Wave Speeds* | OUP 2010 | 432 | complete |
| Deymier2013 | *Acoustic Metamaterials and Phononic Crystals* (ed.) | Springer 2013 | 386 | complete |
| Laude2015 | *Phononic Crystals* | De Gruyter 2015 | 420 | complete |
| Auld1973 | *Acoustic Fields and Waves in Solids*, **Volume I** | Wiley 1973 | 438 | **fragment — Volume I only** |

Two of the six are not what the brief assumed:

* **Auld is Volume I only.** Its copyright page prints `ISBN 0-471-03700-1 (V.1)` and
  `ISBN 0-471-03702-8 (Set)` (p. iv). Volume I runs chapters 1–8 plus appendices 1–3; chapter 8 is
  *Piezoelectricity*, p. 265. There is no acoustoelectric, piezoelectric-semiconductor or
  carrier-transport chapter anywhere in the contents. Volume II (chapters 9–13) was **not
  supplied**, so nothing whatsoever can be said about Volume II — see S3.
* **Deymier is an edited volume**, not a monograph: chapter 5 (*Dynamic Mass Density and Acoustic
  Metamaterials*) is by Mei, Ma, Yang, Yang and Sheng. It must be cited with chapter authorship.

Nowacki was **not supplied**. Nothing in this deliverable is attributed to Nowacki; the only
contact with that name in the supplied books is Ignaczak's "solution of Nowacki type" (Section 7.4)
and Nowacki's radiation conditions quoted in a footnote.

Printed-page conventions (the PDF offset drifts, so each page number below was taken from the page
itself): Tzou, printed = PDF − 21; Eringen, −16 in ch. 2 and −14 in ch. 5 (the header offset
drifts, so headers were read individually); Ignaczak, −19; Deymier, −14; Laude, −12; Auld, −10.

---

## 2. What was actually read, and how

Chapter locations came from each table of contents first, then only the relevant sections were
opened: Tzou ch. 1 §1.3, ch. 2 §2.1–2.5, ch. 12 (memory-integral and two-step sections);
Eringen ch. 2 §2.1–2.3, ch. 5 §5.1 and §5.11, ch. 6 §6.1 and the chapter remark; Ignaczak
Introduction, ch. 1 (all of §1.1–1.3), ch. 3, ch. 4 openings, ch. 6 §6.2–6.3, ch. 10 opening,
ch. 11 closing remark, ch. 12 §12.1; Deymier Preface, contents, ch. 5 §5.1 (openings); Laude
Preface, contents, §2.3.3, ch. 10 §10.1 (openings); Auld copyright page, contents, preface,
chapter 7 closing pages, chapter 8 opening page, appendix 2 property table, and the attenuation
discussion.

Three text-layer caveats, all disclosed because they limit what a quote can prove:

1. Tzou's PDE pages are badly OCR-mangled. Equations are therefore cited by number and never
   transcribed from the text layer.
2. Eringen's OCR drops subscripts and fuses symbols. Equation numbers are reliable; symbol strings
   in `evidence.csv` marked `verbatim=eq` are ASCII transliterations of the printed formula, not
   OCR output.
3. Laude's extraction joins words (`Localresonances`, `effectivemassdensity`). Word quotes from
   Laude were taken from pages where the spacing is intact.

`evidence.csv` separates the two kinds of row: `verbatim=yes` (a literal word string from the book),
`verbatim=eq` (an equation transcribed into ASCII), and `kind=absence` (a term that does **not**
occur, which no automated check in this repo can confirm — see §10).

---

## 3. Tzou: what the book actually says about the lags

* Fourier is the simultaneous-response law, eq. (2.1), p. 62; the book says so and adds that the
  immediate response implies infinite speed (p. 62). Single-phase lag is a one-delay flux law,
  eq. (2.2), p. 62.
* Dual-phase lag is eq. (2.6), p. 63: one lag on the flux, one on the gradient. This is the only
  place the two lags enter the constitutive law.
* **Only a first-order Taylor expansion is performed** — "The first-order expansion containing the
  linear effect of" (2.7), p. 62 — and the book explicitly defends stopping there: "The linear
  expansion becomes sufficient in these cases" (p. 66, for picosecond–femtosecond lags). There is
  no second-order-expansion DPL equation in Tzou.
* The resulting first-order DPL temperature equation (2.10) keeps the mixed derivative, and the book
  is blunt about the consequence: it "completely destroys the wave structure, and the energy
  equation is parabolic in nature" (pp. 68–69).
* Tzou maps the two lags onto the Guyer–Krumhansl phonon model, (2.11), p. 68
  (`τT = 9τN/5`, `τq = τR`), and states that "the dual-phase-lag model is equivalent to the
  phonon-scattering model". A second mapping, (2.12), p. 68, sends the same two lags onto the
  two-step phonon–electron model.
* Damping: the mode classification uses `B = τT/(2τq)` — "Recalling that τT = τq as B = 1/2"
  (p. 81) — and regime change happens only "For the case of B ≤ 1/2 or τT ≤ τq" (p. 86). In other
  words **Tzou's boundary between wave-like (underdamped) and non-wave-like (overdamped) behaviour
  is τT = τq**, not τT = τq/2.
* Chapter 12 carries the Gurtin–Pipkin integral model (12.21)–(12.23) p. 432, its exponential-kernel
  reduction (12.24)–(12.27) p. 432, and a temperature equation with a third-order time derivative
  (12.32) p. 433; the hyperbolic two-step model is (12.13)–(12.15) p. 429.

### The transfer-function question — answered

**Tzou never writes a transfer function of the form `[1+τT s]/[1+τq s]`.** The string
"transfer function" does not occur in the book at all, and no Laplace-domain ratio of that shape is
printed anywhere (checked over the whole extracted text). Tzou stays in the time domain.

**Ignaczak does provide the operator that is algebraically that ratio**, though still in the time
domain: Remark 1.2, eq. (R1.2.1), p. 16 prints
`qi + τq q̇i = −kij(ϑ + τT ϑ̇),j`, i.e. `(1 + τq ∂/∂t) q = −k (1 + τT ∂/∂t) ∇ϑ`. Taking a Laplace
transform of that operator gives exactly `q̃ = −k [(1+τT s)/(1+τq s)] ∇ϑ̃`. The book does not print
the s-domain form, so the honest statement is: *the operator ratio is in Ignaczak p. 16 (R1.2.1);
the transfer function itself is in neither book.*

---

## 4. Ignaczak & Ostoja-Starzewski: the model inventory

| model | heat-flux statement | eq. | page |
|---|---|---|---|
| classical | Fourier | (1.1.20) | 21 (footnote 16 cross-reference) |
| Lord–Shulman (one relaxation time) | `qi + t0 q̇i = −kijθ,j` = Maxwell–Cattaneo | (R1.1.8) | 12 |
| same, field-equation form | `ϑ,i = −λij(qj + t0q̇j)` | (1.2.14) | 13 |
| dual-phase lag | `qi + τq q̇i = −kij(ϑ + τT ϑ̇),j` | (R1.2.1) | 16 |
| Green–Lindsay (two relaxation times) | flux stays classical Fourier; `t1` enters the **stress**, `t0` the **entropy** | (1.3.30), (1.3.31), (1.3.33) | 21 |
| Green–Naghdi 1991 | entropy **balance** law with thermal displacement `α = ∫T dτ` | text | 322 |
| Green–Naghdi type II | no energy dissipation; displacement–temperature system | (12.1.2) | 322 |
| Green–Naghdi type III | finite-speed transport **with** dissipation | (12.1.3) | 322 |

Two structural facts matter for the review and are easy to get wrong:

1. **Green–Lindsay is not a heat-flux-kernel theory in this book.** The flux reduces to `q = −k∇ϑ`
   with footnote 16 calling it "the classical Fourier law of heat conduction" (p. 21); the two
   relaxation times live in the stress (1.3.30) and the entropy (1.3.31).
2. **Green–Naghdi types are not presented through a heat-flux law at all.** They are given as
   displacement–temperature systems (12.1.2)/(12.1.3) p. 322 with the thermal displacement as the
   primitive. The book never writes a `q` for them, so "GN lies inside a heat-flux template" is
   something the book neither states nor supports.

Results actually proved (theorem number and page):

* uniqueness — **Theorem 3.1** (L–S, displacement–temperature) p. 37; **3.2** (L–S, stress–heat
  flux) p. 39; **3.3** (G–L, displacement–temperature) p. 40; **3.4** (G–L, stress–temperature)
  p. 41;
* continuous dependence — **Theorem 3.5**, p. 42; existence — **Theorem 3.6**, p. 43;
* domain of influence — **Theorem 4.1** (L–S) p. 54, **Theorem 4.2** (G–L) p. 56;
* wave speeds — two fundamental disturbances with
  `v(1,2)^-2 = ½(1 + t0 + εt1 ± Δ^½)`, (6.3.1), (6.3.2), p. 127, from the decomposition theorem of
  §6.2;
* wave fronts — Definition 10.1 and the whole of ch. 10 (moving discontinuity surfaces in L–S and
  G–L media), p. 257 ff.; shock and acceleration waves in §10.2–10.3, pp. 261, 270;
* a physics caveat worth citing: Maxwell–Cattaneo violates Galilean invariance, §12.1.2,
  (12.1.4)–(12.1.6), p. 323, following Christov and Jordan.

### The Quintanilla / DPL-stability question — answered

* **Tzou never cites Quintanilla** (no occurrence anywhere in the book) and states no stability
  theorem for DPL; his nearest statement is the damping classification above, with the boundary at
  `τT = τq` (pp. 81–86).
* **Ignaczak cites Quintanilla 2003 only in the bibliography** (p. 399, *J. Thermal Stresses* 26,
  713–721, "A condition on the delay parameters in the one-dimensional dual-phase-lag
  thermoelasticity theory"), and never reproduces its condition in the text. The only DPL
  well-posedness-type statement in the book is **Theorem 1.1, p. 18**: in the shifted frame
  `t* = t + τT`, the DPL temperature field is governed by a hyperbolic equation if
  `τ = τq − τT > 0`, elliptic if `< 0`, parabolic if `= 0`. "Stability" as a word appears once
  (p. 319) and only as a pointer to Leslie and Scott.
* So **neither book states `τT > τq/2`.** Both books place the wave-like/non-wave-like boundary at
  `τT = τq`. That is a different quantity from a stability threshold, and the two must not be run
  together in the review.

---

## 5. Deymier and Laude: local resonance and effective properties

Deymier, Preface p. vii, gives the cleanest contrast available in the library:
phononic crystals control dispersion "through Bragg scattering" (period comparable to wavelength),
while acoustic metamaterials "have the added feature of local resonance" and "their properties do
not rely on periodicity"; local resonance "may lead to negative effective dynamic mass density".

Chapter 5 then prints the formulas:

* (5.1), p. 159 — the static, volume-averaged density `ρeff = f D1 + (1 − f)D2`;
* (5.2), p. 160 — the dynamic mass `Deff V = M0 + nm/(1 − ω²/ω0²)`, i.e. a frequency-dependent
  effective mass with the resonance in the denominator, followed by "negative dynamic mass is
  possible at finite frequencies" (p. 160);
* (5.3), p. 160 — the operational definition `Deff = ⟨f⟩/⟨a⟩`.

Laude has a whole chapter on *Locally-resonant crystals* (ch. 10, p. 301) and introduces local
resonance as a gap mechanism in §2.3.3, p. 44 ("Local resonances can also open band gaps"), with
resonant gaps sitting "much lower in frequency than would be expected in the case of Bragg band
gaps" (§10.1, p. 303). But **Laude prints no effective-mass formula**: the only mention is a
footnote (p. 301) saying homogenisation gives "the effective mass density and effective elastic
constants will be some mean value".

**Neither volume has a thermal, phononic-heat-transport or thermoelastic-damping chapter.**
"Thermoelastic" does not occur in Deymier at all; the damping chapter (ch. 6, p. 201) is viscoelastic.

---

## 6. Eringen: is the thermal sector an extra field?

No. Section 2.3, p. 49, is explicit:

* "The energy balance law (2.1.2) is formed with a single heat vector q";
* "there are no microheat tensors for the micromorphic continuum of grade one" — microheat tensors
  belong to *higher-grade* theories only (Eringen 1970b, Grot 1969);
* "in harmony with a single heat vector q, a single absolute temperature" is posited.

The linear theories then fill in the conduction sector:

* micropolar, §5.1: free energy (5.1.9) and dissipation potential (5.1.11) p. 104, heat flux
  (5.1.13) p. 105 `qk = (1/T0)KklT,l + MkṪ` — a Fourier term plus a temperature-rate term, which is
  then dropped: "we neglect the temperature-rate dependence", (5.1.15), p. 105;
* microstretch, §6.1: flux (6.1.7) p. 251 `Kkl qk = T0 T,l`, and the conduction equation (6.1.15)
  p. 252;
* moduli counts in Table 5.1, p. 106; four plane-wave speeds with cut-offs, (5.11.13)–(5.11.21),
  §5.11, p. 149;
* a chapter-6 remark notes that the "generalized" thermo-microstretch of Singh and Kumar (1998)
  amounts to a second-order time derivative in the conduction equation (p. 264 region) — i.e. the
  relaxation is added *by hand*, on top of a single-temperature sector.

That is the precise sense in which a thermal micropolar theory "carries its own heat equation": it
carries the **classical one**, with one temperature and one heat vector. It does not enrich the
thermal sector.

---

## 7. Verdicts on the five review sentences

| id | sentence (abridged) | verdict | basis |
|---|---|---|---|
| S1 | thermal couple-stress/multipolar/micropolar theories carry their own heat equation and heat-flux law; whether G(s) changes is structural, not a result | **PARTLY SUPPORTED** | heat-flux laws do exist and are printed: Eringen (5.1.13) p. 105, (6.1.7) p. 251, conduction equation (6.1.15) p. 252, all with a single temperature and a single heat vector (§2.3, p. 49). Couple-stress and multipolar are not in Eringen1999 (micropolar ch. 5, microstretch ch. 6 only); the thermal couple-stress evidence remains Toupin 1962 and Green–Rivlin 1964 from P11. The second half of the sentence is the review's own framing: no book states it, and since the thermal sector is classical, "G(s) unchanged" is an assumption about what one inserts, not a theorem. |
| S2 | a locally resonant array is commonly described by a frequency-dependent effective modulus or mass | **SUPPORTED** | Deymier (5.1)–(5.3), pp. 159–160, and Preface p. vii; Laude ch. 10 p. 301 and footnote p. 301. Only the **mass** side has a printed formula; the modulus side is stated qualitatively (Deymier p. vii: negative "mass density and bulk modulus"). |
| S3 | carrier coupling in piezoelectric semiconductors adds fields, so they lie outside the single-kernel construction; a heat-flux kernel has been inserted in semiconductor models by others | **SOURCE NOT AVAILABLE** | only Auld Volume I was supplied, and Volume I has no acoustoelectric chapter: ch. 8 is *Piezoelectricity* (p. 265), and `drift`, `diffusion`, `carrier transport` do not occur (`carrier` occurs once, p. 255, in a Faraday-rotation remark about "current carriers or magnetic spins"). Volume II was not supplied, so no book in the library can either support or refute this sentence. P11's PARTLY verdict from journal sources stands unchanged; the book leg is missing. |
| S4 | Guyer–Krumhansl and GL lie outside the single-kernel heat-flux template; Green–Naghdi types lie inside | **PARTLY SUPPORTED** — and partly contradicted | *GK*: Tzou derives it from the BTE ((1.16)–(1.17), pp. 12–13) and then shows DPL **is** the GK model, (2.11), p. 68 ("equivalent to the phonon-scattering model"). So in the book's own reading GK is *inside* the two-lag family, which contradicts the sentence as written. *GL*: Ignaczak's flux is classical Fourier ((1.3.33), p. 21); the relaxation sits in the stress (1.3.30) and entropy (1.3.31), so GL is outside a *flux*-kernel template but is itself exactly a first-order operator on the gradient via `φ = θ + t1θ̇` ((1.3.21), p. 20). *GN*: no heat-flux law is ever written for GN I/II/III ((12.1.2)–(12.1.3), p. 322), so "lies inside" is unsupported by the book. |
| S5 | Quintanilla 2003: stability iff τT > τq/2 for dual-phase-lag | **NOT SUPPORTED** (by these books) | the inequality is in neither book. Ignaczak: Theorem 1.1, p. 18 gives hyperbolic/elliptic/parabolic according to the sign of `τq − τT`; Quintanilla 2003 appears only in the bibliography (p. 399) with a title about "a condition on the delay parameters", and its condition is never reproduced. Tzou: no stability theorem, no Quintanilla citation, and a damping classification whose critical point is `τT = τq` ((2.59), pp. 81–86). Both books therefore put the boundary at `τT = τq`, not `τT = τq/2`. The sentence must either be re-derived from the primary paper (not in the library) or dropped. |

---

## 8. Sentences the books contradict or force us to reword

1. **S4, Guyer–Krumhansl.** Tzou (2.11), p. 68, is an equivalence claim: the DPL with
   `τT = 9τN/5`, `τq = τR` reproduces the Guyer–Krumhansl phonon-scattering model. A sentence that
   says GK "lies outside the single-kernel template" reads as contradicted unless the template is
   defined narrowly (and differently from DPL). Recommended rewording: *GK carries spatial
   gradients of the flux, so it is outside a single **time**-kernel template; it is nevertheless the
   physical content of the two-lag model in Tzou's reading (eq. (2.11), p. 68).*
2. **S5, the number τT > τq/2.** Both books put the change of character at `τT = τq`
   (Ignaczak Theorem 1.1 p. 18; Tzou `B = τT/(2τq)` with `B = 1/2`, pp. 81–86). If the review's
   `τq/2` is a *stability* (decay) threshold from Quintanilla and the books' `τq` is a
   *wave-type* threshold, the review is comparing two different thresholds under one word. This
   must be said explicitly.
3. **S4, Green–Lindsay.** The review sentence groups GL with GK. Ignaczak separates them sharply:
   GL's flux is Fourier (p. 21), GK's is not.
4. **S5, Taylor order.** If the review says the DPL temperature equation is obtained by a
   second-order Taylor expansion, that is not what Tzou does: only first order is carried
   ((2.7), p. 62), with an explicit defence on p. Wise wording: *the first-order expansion is the
   common one; higher orders are a modelling choice.* Ignaczak does not expand at all — it keeps
   the exact delay (R1.2.1), p. 16.
5. **S3** cannot be carried by any book in the library (see §7). Keep the P11 journal sourcing and
   mark the book leg as unavailable.

---

## 9. Where these chapters are worth citing

| review section | cite | why |
|---|---|---|
| `s03_foundations` | Eringen §2.1–2.3, pp. 36–50 (single heat vector, single temperature, C–D inequality (2.3.6)); Ignaczak ch. 1, pp. 1–29 (classical / L–S / G–L side by side); Tzou §1.3, pp. 12–15 (operator–determinant method) | gives the balance-law skeleton and the one-temperature postulate behind any single-kernel construction |
| `s05_hyperbolic` | Ignaczak Thms 3.1–3.4, pp. 37–41; Thms 4.1–4.2, pp. 54–56; (6.3.1), p. 127; ch. 10, p. 257 ff.; Tzou ch. 12, pp. 429–437 | uniqueness, existence, domain of influence, two finite speeds, wave fronts — the strongest single source in the library |
| `s06_lags` | Tzou §2.1–2.5, pp. 62–86 ((2.1)–(2.12), (2.55)–(2.59)); Ignaczak Rem. 1.2 and Thm 1.1, pp. 16–18; Tzou (12.21)–(12.32), pp. 432–433 | the lag taxonomy, the first-order truncation, the damping map, and the integral-kernel equivalence |
| `s12_size` | Eringen §5.1, pp. 104–106 with Table 5.1; §5.11, p. 149; Deymier (5.1)–(5.3), pp. 159–160; Laude §2.3.3, p. 44 and ch. 10, p. 301 | characteristic lengths and moduli counts on one side, frequency-dependent effective mass on the other |
| `s13_multiphysics` | Eringen §2.3, p. 49 (microheat only at higher grade); Ignaczak §12.1.2, p. 323 (Galilean invariance); Deymier Preface, p. vii and ch. 5, pp. 159–160 | where a second temperature/heat vector would have to enter, and the known pathologies of the one-lag flux law. **Auld cannot be cited for the acoustoelectric leg.** |

---

## 10. Inventory, refs_P8, and the gates

* `books_inventory.csv` is written here because **no P12 `books_inventory.csv` exists** in this
  repository on any branch (checked before starting). It lists the six supplied books and one
  **NOT SUPPLIED** row for Nowacki. If P12 later appears, this file supersedes it for books.
* `refs_P8.csv` needed **no `pdf_status` change**: none of the six books is an entry there (they are
  new keys), and the one Eringen entry in it — `Eringen1990ThermoMicrostretch`, the 1990 IJES paper,
  R0 / NOT CHECKED — is a different work from Eringen1999, so the book cannot upgrade it. It stays
  NOT CHECKED. Eringen1999's chapter 6 only points at that literature.
* New keys `Tzou2015`, `Eringen1999`, `Ignaczak2010`, `Deymier2013`, `Laude2015`, `Auld1973` were
  checked against the existing 73 unique keys in `P8_coverage` (`refs_P8.csv` + `refs_P8.bib`):
  no collision.
* Gates: `check_p8.py`, `check_p9.py`, `check_p10.py`, `check_p11.py`, `check_p13.py` and
  `check_readme_paths.py` all print PASS and exit 0 (results in the turn report).

### Limitations we are not hiding

* `kind=absence` rows are statements that a term does not occur. They were established by searching
  the full extracted text, but no gate in this repository can re-verify them, because the books are
  not in the repository. `check_p13.py` counts and reports them (6 rows) instead of pretending they
  are machine-checked.
* No second-order-expansion DPL equation exists in Tzou and no DPL stability theorem exists in either
  book, so nothing here can be used to support a `τT > τq/2` claim. That claim remains
  NOT VERIFIED pending the primary Quintanilla paper.
* Auld Volume II was never seen; every statement about it is a statement about its absence.
