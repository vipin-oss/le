# BLUEPRINT — Multiphysics Wave Mechanics review (master control document)
Owner/Handler: Vipin Gupta. Supervisor/Auditor: Claude. Scholar (builder): Arena. Independent verifier: Brave AI. Version 1, 22 Oct 2026.

## 0. MISSION LOCK (never changes without Vipin's written OK)
Goal: the most reliable, most useful, most-cited review in generalized thermoelasticity / piezothermoelasticity / nonlocal-gradient continua / memory & fractional heat conduction / interface energy partition.
Target: Applied Mechanics Reviews (ASME) as PRIMARY (backups: ACME, Physics Reports), 10+ authors, genuine authorship.
Quality bar (all must hold for release): (1) compiles clean from fresh clone, (2) every equation verified by someone other than its writer, (3) every reference exists and supports its claim, (4) every claim carries a status tag, (5) journal format + authorship rules satisfied, (6) domain-expert (author) pass done.
Anything not serving these six = out of scope. If Arena or Brave proposes new scope, log it in DECISIONS.md and ask Vipin.

## 1. ROLES
- Vipin (handler): sets goal, final decisions, relays messages, brings the author team, decides disputes, approves scope changes. Only person who sends to journal/editor.
- Claude (supervisor): writes prompts, audits what Arena pushes (compile, defect table vs source, independent re-derivations), decides pass/fail per gate, escalates to Brave when it cannot settle something, keeps this blueprint and the status board current. Does NOT write the scholarly content.
- Arena (scholar): all scholarly + engineering work: derivations, literature, text, figures, LaTeX, tables. Pushes to git branch with commit hash.
- Brave AI (independent verifier): used ONLY when Claude cannot confirm something alone. Gets a self-contained verification brief (no Arena narrative, only the claim + sources) so it checks independently. Its answer is evidence, not a verdict: Claude weighs it, and disagreements go to Vipin/authors.
- Human authors (10+): domain-expert pass, final math/citation sign-off, section ownership, CRediT. No AI is an author; AI use is declared.

## 2. ESCALATION LADDER (for any check)
L1 Claude checks alone (compile, grep, consistency, DOI lookup, symbolic/numeric re-derivation in code).
L2 If Claude cannot settle (ambiguous source, heavy derivation, paywalled paper, conflicting results): Claude writes a Brave brief; Vipin pastes it into Brave; Vipin pastes answer back; Claude reconciles.
L3 If Claude and Brave disagree, or both are unsure: mark DISPUTED, send to the human author who owns that section; do not release the claim.
Rule: no claim is upgraded to DERIVED / PRIMARY-SOURCE-CHECKED on one AI's say-so if it is a core result.

## 3. ROUNDS AND GATES (move on only when the gate is met; any failure returns to the same round)
R1 Build + hygiene (Arena running now, arena_FINAL_prompt.md). Gate: fresh clone builds with 0 errors, 0 undefined refs, 18 figures visible, no scratch text, Overfull on tables fixed, DEFECT_STATUS.csv all rows FIXED/DISPUTED with evidence.
R2 Math truth. Every equation/derivation gets a verifier who did not write it (Claude by code/symbolic check; Brave for hard ones). Gate: EQUATION_LEDGER.csv: id | statement | source | verifier | method | status (DERIVED/CHECKED/CONDITIONAL/OPEN). Zero unresolved contradictions between sections (esp. flux sign, energy balance, R+T+A=1, secular equations, GL/two-temperature).
R3 Citations. Gate: REFERENCE_AUDIT.csv: key | DOI | exists? | claim it supports | supported? | checker. Zero fabricated or unsupported; every core claim traced to a primary source.
R4 Journal fit. Gate: JOURNAL_FIT_MATRIX.md, AMR-style proposal drafted (Vipin sends), length/reference budget from 10+ real AMR reviews, AMR-length version stands alone, ASME template compiles, AUTHOR_CONTRIBUTIONS.md + SECTION_OWNERS.md + AI-use declaration done.
R5 Author expert pass. Authors mark: wrong, weak, missing, overclaimed; add "when does each theory fail" and open problems. Gate: every section signed by its owner.
R6 Mock referee. Fresh reader (Brave or an external colleague) reviews as a hostile referee. Gate: all major points answered or consciously accepted. Then final proofread, submission package, Vipin submits.
Parallel track P: Vipin sends the proposal to the AMR Editor as soon as R4's draft exists (do not wait for R6), to learn author limit, length, reference style.

## 4. ARTIFACTS (single source of truth, in the git repo; Claude audits against these)
BLUEPRINT.md (this) · STATUS.md (one table: round, gate, state, owner, next action, last commit) · DECISIONS.md (every scope/format/dispute decision with date and who decided) · DEFECT_STATUS.csv · EQUATION_LEDGER.csv · REFERENCE_AUDIT.csv · JOURNAL_FIT_MATRIX.md · AUTHOR_CONTRIBUTIONS.md · SECTION_OWNERS.md · NOTATION.md (one glossary, one owner) · tags v1.1, v1.2... one per passed round.

## 5. ANTI-DRIFT RULES
1. Every Arena/Brave message must start with "Mission: <one line from section 0>, Round: Rn". Claude's prompts always do this.
2. Work not in the current round's gate is not done; no "bonus" restructuring mid-round.
3. No PASS without execution evidence (log, hash, output). "Looks fine" is not a pass.
4. Never delete or silently rewrite a claim: change it with a DECISIONS/DEFECT entry.
5. Numbers (pages, refs, figures) come from the AMR comparison data, not guesses.
6. Fabrication rule: if a source cannot be opened, the claim is tagged UNVERIFIED, never filled in.
7. Claude re-reads this blueprint at the start of each audit; if a request contradicts it, Claude flags it to Vipin first.

## 6. WHAT VIPIN HAS TO DO (the only manual steps)
a) Give Claude the Arena branch + commit hash after each run. b) When Claude issues a "Brave brief", paste it into Brave and paste the answer back. c) Decide DISPUTED items or hand them to the section author. d) Send the AMR proposal (draft ready from R4) and relay the Editor's reply. e) Organise the 10+ authors and the R5 pass. f) Final submission.

## 7. STANDARD MESSAGES
To Arena: "Mission: ... Round: Rn. Task: ... Gate: ... Deliver: branch+commit, updated STATUS.md and the round's ledger. No PASS without execution."
To Brave: "Verify independently. Claim: ... Sources: ... Task: re-derive / check this reference supports it. Return: result, steps, confidence, anything you could not verify. Do not assume the claim is true."
From Claude to Vipin after each audit: 10 lines max: gate result, what failed (with evidence), next action, what I need from you.

## 8. DEFINITION OF DONE
All six quality-bar items true, tagged release, mock-referee points closed, authors signed, Editor's format requirements met. Until then the paper is not "ready", however good it looks.
