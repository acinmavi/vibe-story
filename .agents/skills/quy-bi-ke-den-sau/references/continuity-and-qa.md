# Pre-write, blind-review, gatekeeping and commit process

1. Before each chapter read arc row, timeline and knowledge ledger. Identify 2 stakes and 1 permanent change.
2. Writer only sees POV-known facts. A separate mystery reviewer receives `clue-ledger.csv` without `solution-sealed.md`. Reviewer lists at least 2 plausible hypotheses and why evidence narrows them.
3. Canon reviewer checks dates (28 Jun, 2 Jul, 29 Aug, 31 Aug, Sep), what MC can know, Tarot Club external continuity, Old Neil, Sefirah ownership, potion rules.
4. Knowledge reviewer checks whether any statement is a firsthand fact, prior-book memory, guess or author-only fact. Mark author-only leak as critical.
5. Plot reviewer checks alternate choices: why not report to church? why not inform Klein? who benefits? What could go wrong?
6. Prose reviewer checks Vietnamese naturalness, scene rhythm, exposition disguised as dialogue, overlong internal monologue, forced humor and copied canon dialogue. Do not mimic identifiable wording of original.
7. Apply changes and update `continuity/` and `arcs/` when effect reaches future chapters. Run `python3 .agents/skills/quy-bi-ke-den-sau/scripts/check_project.py .` then commit. No push.
8. Mandatory first review gate and separate next-arc gate. Do not infer approval from silence. Human must explicitly approve chapter 1.
9. Prior to arc 2, record arc 1 emotional and informational debts paid/unpaid. Every next arc needs new primary mystery, new scene type, own arc climax, at least two long-tail impacts.
