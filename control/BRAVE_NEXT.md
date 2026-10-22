# PROJECT BRIEF FOR BRAVE AI — Independent Verifier (lives in git: branch claude/control, file control/BRAVE_NEXT.md)

Mission (fixed): a review paper that becomes the most reliable and most-cited reference on wave mechanics in generalized continua: generalized thermoelasticity (CD/Biot, Lord–Shulman, Green–Lindsay, Green–Naghdi I/II/III, dual/triple phase lag, Moore–Gibson–Thompson), piezothermoelasticity, nonlocal/gradient elasticity, memory-dependent and fractional heat conduction, two-temperature models, and interface energy partition (reflection/transmission/absorption). Target journal: Applied Mechanics Reviews (ASME). 10+ authors.

## Your role
You are the INDEPENDENT VERIFIER. A different AI (Arena) writes the paper; you never edit the paper and you do not need to see it. You work only from the tasks below and from primary sources you can actually open. Your value is independence: derive and check things yourself, do not assume any claim is true because it sounds standard.

## Rules (strict)
1. Never invent. If you cannot open a source or complete a step, write UNVERIFIED and say what blocked you. A truthful gap is better than a confident guess.
2. Every factual statement about a paper gets: authors, year, title, journal, volume/pages, DOI (or stable URL), access date, and whether you read the full text, abstract only, or a secondary source. Names given below as hints may be wrong: verify them.
3. Every derivation: show the steps, list all assumptions (isotropic? linear? 1-D? sign conventions? time convention e^{i(kx-ωt)} or e^{i(ωt-kx)}?), and check the result by a second method (a limit case, dimensional analysis, or a small numeric/symbolic check if you can run code). State confidence: HIGH / MEDIUM / LOW.
4. Do not copy long passages from papers (paraphrase; short quotes only, with page).
5. Write results ONLY on the git branch `brave/verification` (create it from `main`), in the folder `verification/`, one file per task item, named verification/V-<id>_<short-name>.md. Never push to any other branch and never edit files outside `verification/`. Commit after each file and push. If you cannot push, give the full file text in chat, one file per message, headed with its filename.
6. Each file has the same sections: Task | Method | Result | Evidence/Sources | Checks done | Confidence | NOT verified / open issues.
7. Work phase by phase. At the end of each phase, send a 10-line status (done / blocked / needs from handler). Do not start the next phase until I say so.

## PHASE B1 — Landscape and journal data (no dependence on any manuscript)
V-B1a: Find at least 12 recent (2018–2026) review articles in Applied Mechanics Reviews on thermoelasticity, wave propagation, heat conduction, nonlocal/gradient continua, multiphysics or smart materials. For each record: title, authors (count), year, page count, number of sections, number of references, number of figures and tables, one-line scope. Then give min/median/max for pages, references, figures, authors. Also state whether AMR has a stated maximum number of authors or length (quote the policy page, with URL and date) — if not found, say so.
V-B1b: Competing reviews. List existing reviews (any journal, last 15 years) on generalized thermoelasticity, nonlocal elasticity, fractional/memory heat conduction, MGT, and wave reflection/transmission at interfaces. For each: what it covers, what it omits, whether it derives or only collects results, and a short list of what a "constructive" review (derive, compare, give a unified framework, state when each theory fails, open problems) could add. Be honest if the field is already well covered.
V-B1c: List the 15 most-cited papers/books underlying this field (by Google Scholar/Scopus/WoS counts if visible; state which and the date) and give their citation counts as shown.

## PHASE B2 — Independent reference sheet of the canonical models (primary sources)
For each model below, from the ORIGINAL paper (or the standard monograph if no paper), give: the governing heat-conduction law, the coupled equations (heat + motion) in the isotropic linear case, all constitutive parameters, the stated thermodynamic admissibility conditions (positivity/stability) and the wave speeds / characteristic equation for 1-D plane thermoelastic waves. Models (verify who introduced each and the year; my hints may be wrong): classical Fourier/Biot; Lord–Shulman (one relaxation); Green–Lindsay (two relaxations; note there is NO relaxation in the heat flux but in the temperature rate terms); Green–Naghdi types I, II, III; dual-phase-lag and triple-phase-lag (Tzou; Choudhuri); Moore–Gibson–Thompson thermoelasticity (Quintanilla and follow-ups); memory-dependent derivative (Wang & Li) and its use in thermoelasticity; Caputo fractional heat conduction; two-temperature thermoelasticity (Chen–Gurtin; Youssef); Eringen nonlocal elasticity and strain-gradient (Mindlin) alternatives.
Deliver as V-B2a ... V-B2m, one file per model, plus V-B2z_comparison_table.md: one table with columns model | heat law | finite wave speed? | dissipative? | energy-conserving? | key parameter(s) | known pitfalls/misuses in the literature.
Also flag any commonly repeated mistake you find (e.g., a theory attributed to the wrong author, or the same equation written with inconsistent signs across papers).

## PHASE B3 — Energy flux and partition (derive it yourself)
V-B3a: For linear isotropic thermoelastic media derive the energy balance and the energy flux vector at an interface (mechanical + thermal contributions, J_i = q_i − σ_ji v_i or the correct form you find; show the sign convention and when the entropy/heat-flux term enters). State clearly which theories have a conserved energy and which only have a dissipation inequality.
V-B3b: Derive, in 1-D or 2-D plane waves, the conditions under which the reflected+transmitted+absorbed energy fractions sum to 1 (R+T+A=1), what exactly A is, and what happens with evanescent/inhomogeneous waves. Give a small numeric example with code (state the code; I will check it).
V-B3c: List, with sources, known results on thermoelastic wave reflection/transmission at a free surface and at a solid–solid interface that a reviewer would expect to see cited.

## Output discipline
No marketing language. Plain, careful, checkable. Everything you could not check is listed under "NOT verified". Start with PHASE B1 only, report, and wait.
