# Cover letter (draft — authors to complete; nothing here has been sent)

[Date] · [Editor-in-Chief], International Journal of Heat and Mass Transfer

Dear Editor,

We submit the manuscript "Orientation-dependent wall stress around circular and elliptical cavities in monoclinic β-Ga2O3 under a transient thermal pulse: a verified continuum study with thermal-memory and mechanism ablations" for consideration as an original research article. [Journal choice is the authors' decision; Journal of Thermal Stresses and Mechanics Based Design of Structures and Machines are alternatives, see JOURNAL_FIT.md.]

**What the paper does.** It studies the transient coupled thermoelastic response of a circular and an equal-area elliptical cavity (axis ratio 2) in monoclinic β-Ga2O3 under a Gaussian wall-temperature pulse, with Fourier, Lord–Shulman and a two-relaxation-time conduction law. The single-pulse response is obtained from a frequency-domain solver by Bromwich inversion and verified against exact and independent solutions; grid convergence is analysed with separate radial and angular families.

**Companion calculation document.** A separate companion (`FINAL_REVISED_CALCULATIONS.tex`, 29 numbered equations) accompanies the submission. It contains the worked arithmetic behind the paper — the plane-strain reduction, the crystal rotation, the closed-form isotropic cavity, the dimensionless groups, the grid metrics and contravariant coefficients, the Bromwich contour, the quantity-of-interest formulae, a step-by-step Richardson extrapolation and the uncertainty budget — with every number recomputed from the frozen source code or read from the processed data package. It is offered so that a referee can check the quantitative statements without re-running the code; it reports no new result and no new simulation.

**Main findings.** (i) The peak wall stress of the circle is orientation-invariant to round-off and equals 0.854 MPa/K. (ii) The ellipse converts crystal orientation into a peak-stress modulation of 29% (numerical uncertainty 1.3 percentage points); expansion and stiffness anisotropy compete, conductivity anisotropy is minor. (iii) Thermal memory changes the wall-stress history by at most 6.4% for relaxation times up to 20 ps, so the peak wall stress under a prescribed wall temperature is a poor probe of the conduction law; the size dependence is an exact quasi-static collapse in the memory number plus an elastic-inertia correction of order ε². (iv) Thermoelastic feedback is below the bound 5δ.

**Relevance to the journal.** The paper identifies which observable is — and is not — sensitive to non-Fourier conduction in a thermally loaded cavity and provides a verified numerical route for single-pulse responses from frequency-domain solvers; [authors to adapt to the journal's transfer-process emphasis].

**Limitations stated in the paper.** No experimental validation exists (verification only); relaxation times are hypothetical; continuum validity at 5–50 nm is not established; the stress scale depends on the thermal-expansion data by more than an order of magnitude; the elastic echo of the finite outer boundary is a model feature for cavities ≥ 20 nm.

**Declarations.** AI assistance: a generative-AI tool was used for the writing process (drafting, revising and internal consistency checks) and, separately, to review and extend the numerical code and its verification suite and to run the simulations; the manuscript states both in the form the journal requires — the writing use in the declaration above the references, the code and simulation use in the numerical-methods section — and the authors take full responsibility for every number [declaration wording to be reviewed and confirmed by the authors]. The manuscript is not under consideration elsewhere [authors to confirm]. Data and code: data package with SHA-256 code freeze; [repository DOI to be inserted]. Conflicts of interest, funding, CRediT: [authors].

Suggested reviewers: [authors to propose; none are proposed here]. Corresponding author: [name, e-mail].

Sincerely, [authors]
