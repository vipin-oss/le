# Task 4 — experimental data survey (first pass)

`experiments_1.csv` collects the measured numbers a generalized-thermoelasticity paper
needs, with the reading level of every entry stated explicitly. Nothing under
`scripts/` or `sections/` was touched.

## What was actually read

| level | entries | meaning |
|---|---|---|
| abstract only | 4 | the publisher's abstract page was read; the body was not |
| abstract plus excerpted article text | 1 | the publisher page also exposes part of the body (Science) |
| metadata only | 6 | DOI/title/journal verified (publisher page or the project register), body **and** abstract not read |

No full text was read. Consequently **only two entries carry a physical number**, and
one of those has no error bar:

* **EXP-01 — bismuth, 1.2–4.0 K, heat-pulse time of flight.** Saturated second-sound
  velocity `(0.78 ± 0.05) × 10^5 cm/s = 780 ± 50 m/s`, one third of √3 times the Debye
  velocity, independent of orientation. This is the single datum in the survey with a
  quoted uncertainty.
* **EXP-04 — graphite, 85–125 K, transient thermal grating.** Measured second-sound
  velocity ≈ 3200 m/s against an ab initio 3650 m/s; the authors themselves call the
  agreement qualitative and give no error bar.

Everything else is method-level: the NaF heat-pulse line (EXP-02, EXP-03), the TED
theory/experiment pair (EXP-05, EXP-06, EXP-11), and the pump–probe / TDTR measurements
that fix phonon mean free paths and electron–phonon times (EXP-07, EXP-08, EXP-09,
EXP-10).

## What this means for the manuscript

1. A claim of the form "relaxation times of order τ in material X are measured" is
   **not yet supportable from this survey**: no entry gives a directly measured τ with
   an uncertainty. The bismuth and graphite numbers are velocities and temperature
   windows, not relaxation times.
2. The honest statement the data does support is weaker and cleaner: second sound has
   been observed in bismuth (1.2–4.0 K, 780 ± 50 m/s), NaF (cryogenic, velocity falls
   short of the predicted limit) and graphite (85–125 K, ≈3.2 km/s) — i.e. the
   hydrodynamic window exists, and its width is material dependent.
3. For thermoelastic damping the benchmark is Zener/Lifshitz–Roukes: measured MEMS Q
   values vary by factors of two to three with material and geometry (EXP-06), so a
   damping prediction should be quoted as a band, not a single number, unless the
   device is specified.

## Next pass (needs the library PDFs)

* extract the actual τ values (and their fitting method) from EXP-03, EXP-06, EXP-08,
  EXP-09, EXP-10, EXP-11 — six entries currently block any quantitative comparison;
* add the attenuation-versus-frequency measurements the task asks for (ultrasonic and
  transient-grating attenuation fitted with LS/DPL); none is in this first pass because
  no such paper was verified at abstract level within this session;
* record page numbers for EXP-04 (the 3200/3650 m/s pair is currently located only as
  "article text near Fig. 2A").

Validator: `python3 check_experiments_1.py` prints `PASS all checks (rows=11, columns=13)`
and exits 0 (`check_experiments_1_log.txt`).
