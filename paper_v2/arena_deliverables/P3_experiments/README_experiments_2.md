# Task 4 — experimental data survey, second pass (attempted; blocked)

The first pass (`README_experiments_1.md`) read only abstracts and metadata and
left three jobs for a second pass:

1. extract the actual measured relaxation times (with uncertainties) from the
   six blocking entries;
2. add attenuation-versus-frequency rows;
3. pin page numbers for the graphite 3200 / 3650 m/s pair.

**None of the three could be done, because no full text was reachable in this
environment.** This note records exactly what was tried, what was found, and what
is delivered instead — a protocol that can be executed the moment the PDFs are
usable. No number has been invented, and `experiments_2.csv` was deliberately
**not** created: a measurements file containing no measurements would be a false
artefact.

## What was tried, and what came back

| step | query / action | result |
|---|---|---|
| 1 | library search for the four experimental author names (McNelly, Duwel, Brorson, Cahill), one combined query | 0 files |
| 2 | the same names as six *separate* single-term searches, plus Huberman and Zener | 0 files each |
| 3 | DOI-fragment searches (`physrev.52`, `physrevlett`, `1.1524305`, `aav3548`) | 0 files each |
| 4 | a known-present control search (`chadwick`) | 1 file — so the search itself works; the zeros are real absences of *loose* copies |
| 5 | full inventory listings of the per-topic PDF batch folders | no loose copy of any of the seven target papers |
| 6 | the library's own split-parts index | four of the seven targets **are** in the library — as members of two archive bundles (51.8 MB and 62.3 MB) |
| 7 | attempt to read an archive bundle directly | refused: "over the 25 MB extraction cap" |
| 8 | attempt to fetch the bundle from the shell | no outbound network from the sandbox (TLS handshake fails, exit 35) |

So the papers are *present* but *unreachable*: the only route to them is a
download of a 52–62 MB archive, which the extraction cap forbids and which the
sandbox cannot fetch by any other route. Publisher pages give abstracts only.

## Why this matters for the manuscript

The verdict of the first pass stands unchanged and is now supported by a second,
independent attempt to get the data:

* **No measured relaxation time with an uncertainty is available** to this work.
  A sentence of the form "the relaxation time in material X has been measured"
  must therefore stay out of the manuscript.
* The **attenuation-versus-frequency** rows the task asked for cannot be written
  either: two candidate measurement classes were identified (ultrasonic
  attenuation, transient/thermal grating), but **no specific paper could be
  verified**, so no row is added. Inventing one would break the rule that every
  row must name a source that was actually checked.
* What the first pass established remains the honest maximum: second sound has
  been observed in bismuth (1.2–4.0 K, 780 ± 50 m/s), NaF (velocity below the
  predicted limit) and graphite (85–125 K, ≈3.2 km/s), i.e. **the hydrodynamic
  window exists and its width is material dependent**.

## What is delivered instead: `extraction_protocol.csv`

Nine targets, one per blocking item (seven from the register plus the two
attenuation classes). For each: the quantity to pull out, the symbol the paper
uses, **the conversion to a relaxation time**, how to carry the uncertainty, and
where in the paper to look. Two targets are marked `BLOCKED_SOURCE_NOT_IDENTIFIED`
rather than `BLOCKED_ARCHIVE_OVER_CAP`, because for them it is not even the PDF
that is missing — no source has been identified yet.

The protocol is the part of the job that survives the access problem: whoever
gets the PDFs does not have to rediscover what to extract or how to convert it.

Validator: `python3 check_experiments_2.py` prints
`PASS all checks (rows=9, columns=11, blocked=9, read=0)` and exits 0
(`check_experiments_2_log.txt`). It also fails the build if any number with a
time unit appears in the file, so the protocol cannot silently acquire a value
that nobody read.

## To finish the pass when the PDFs are usable

1. put the PDFs outside the repository (they must not be committed);
2. read only the section named in `where_to_look`, and fill a *new* file
   `experiments_2_extracted.csv` with the schema of `extraction_protocol.csv`
   plus `value`, `unit`, `uncertainty`, `page`, `read_level`;
3. convert with the formula in `conversion_to_relaxation_time`, and record the
   paper's own definition if it differs;
4. only then write the τ sentence into the manuscript, as a range with the
   material, temperature and method attached — never as a single number.

## Addendum — `experiments_2.csv` now exists, still with zero measured values

Task 4 asks explicitly for `experiments_2.csv`, so the file is now present
(4 rows, one per experimental paper named in the task: Jackson 1970, Huberman 2019,
Cahill 2003, and the unidentified `2ndSoundSolids` review). It does **not** replace the
honest decision above; it makes it machine-checkable:

* every row has `status = SOURCE NOT AVAILABLE`, a named blocker, and **empty**
  `value`, `unit`, `uncertainty` and `page`;
* `read_level` starts with `none` for every row;
* the checker also enforces the forward rule — a row may only become
  `status = READ_AT_PAGE` if `value` is non-empty and `page` contains a page number,
  so a number can never be added without the page it came from.

Validator: `python3 check_experiments_2_csv.py`
→ `PASS all checks (rows=4, blocked=4, read=0)` (`check_experiments_2_csv_log.txt`).

The abstract-level numbers that are already known (bismuth 780 ± 50 m/s; graphite
≈3.2 km/s against 3650 m/s ab initio, no error bar) stay in `experiments_1.csv` with
`read_level = abstract only`, and are deliberately **not** copied into
`experiments_2.csv`, which is reserved for values read on a numbered journal page.

---

# Second revision — the pages were reached, so the numbers are in

The blocked version of `experiments_2.csv` (commit `cb8e45a`) has been replaced. Three of
the four Task-4 papers turned out to be readable as loose files, were read page by page,
and every number below was copied from a printed page. The schema grew three columns —
`material`, `temperature`, `model` — because a velocity or a conductivity without those
three is not evidence. The file now has 13 rows: 12 `READ_AT_PAGE`, 1 still
`SOURCE NOT AVAILABLE`.

## Jackson, Walker and McNelly (1970), `jackson1970.pdf`, pp. 26–28

* **No numerical second-sound velocity is printed in this Letter.** That is the single
  most important finding of the pass: the manuscript must not quote a c₂ value from
  Jackson. The velocity information sits in Fig. 3 (arrival time versus temperature,
  8–20 K), which was not digitised.
* What the text does give: second sound is first resolved at **15 K** (p. 26), the
  transverse pulse has already broadened by 12.5 K, and at **18 K** the peak arrival
  time "is essentially at the value expected from existing theory, but has yet to level
  off" (p. 27). No roll-off to the fully developed velocity is seen before diffusion
  takes over.
* Purity indicator on p. 26: thermal conductivity peak **240 W cm⁻¹ K⁻¹ at 16.5 K**,
  printed as "240 W/cm deg"; the sample is 8.3 mm long, (100) direction.

## Huberman et al. (2019), `huberman2019.pdf`

| quantity | value | page |
|---|---|---|
| measured second-sound velocity, 85 K | **about 3200 m/s**, no error bar | p. 3 (first release) |
| ab initio velocity, 85 K | **3650 m/s**, "somewhat higher than the measured" | p. 4 (first release) |
| temperature window at 10 µm grating | present at 104 K and 125 K, gone at 150 K and at 50 K | p. 4 (first release) |

Two cautions. The held PDF is the **first release of 14 March 2019**, and every page
prints "Page numbers not final at time of first release"; the locators say so in the cell
itself, and the checker refuses any first-release locator that does not. The 3200 m/s
number is a **fit slope times 2π** from the ω-versus-q inset, not a single waveform, and
the paper gives no uncertainty on either velocity.

## Cahill et al. (2003), `cahill2003.pdf`

This review contains **no second-sound measurement**; what it supplies is method and
compiled numbers.

* p. 812, Sec. V A: TDTR "provides a direct method for measuring heat diffusion on
  nanometer length scales"; thermal diffusivities **0.005 < D < 1 cm² s⁻¹**, and at
  *t* = 200 ps diffusion lengths **10 < l < 140 nm** with l = √(Dt).
* p. 808, Table I: superlattice conductivities collected from the review's references —
  Si/Si₀.₇₁Ge₀.₂₉ **22 (cross-plane) / 54 (in-plane) W m⁻¹ K⁻¹** at 50 Å/50 Å only;
  Si/Ge **1.6** at a 70 Å period; Si/Si₀.₇Ge₀.₃ **10** (100–300 K); InAs/AlSb **2.5**.
  These are the review's compilation, not measurements made for it, and the rows say so.

## What is still missing

**EX2-04**, the unidentified "second sound in solids" review, remains blocked: the file of
that name is an X-ray surface-reflection text, a name-versus-content mismatch. It is not
cited by any claim in the register and must stay uncited.

## EX2-04, resolved as far as it can go

The file `2ndSoundSolids` is not an X-ray paper after all: reading its whole first page
shows Chester (1963), *Second Sound in Solids*, Phys. Rev. 131, 2013–2015, whose abstract
predicts heat transport "by wave propagation rather than by diffusion" above a critical
frequency, and whose p. 2014 carries the modified Fourier equation with a relaxation time.
That settles register claim CR098 (`P3_evidence_claims_C`, CC-0014) — but it is a theory
paper, so **EX2-04 stays `SOURCE NOT AVAILABLE`**: there is still no review, and there are
still no measurements in the file.
