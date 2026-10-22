# control/ — coordination folder (written only by Claude, the supervisor)
Branch: claude/control. Nobody else edits this branch.
- BLUEPRINT.md: roles, rounds, gates, anti-drift rules (read first).
- STATUS.md: current round, gate state, what each AI should do now.
- ARENA_R1_prompt.md: Arena's current task (round 1).
- BRAVE_NEXT.md: Brave's current task (Phase B1 first; wait for go before B2/B3).
- ARENA_ADDENDUM_NOT_YET.md: journal/format/authors task. DO NOT start until STATUS.md says round 1 gate passed.
Where results go: Arena -> its own arena/* branch. Brave -> branch brave/verification, folder verification/. Claude reads both and writes verdicts into STATUS.md.
