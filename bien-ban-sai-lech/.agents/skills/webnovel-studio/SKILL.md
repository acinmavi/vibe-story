---
name: webnovel-studio
description: Plan, write, critique, and maintain an original long-form Vietnamese mystery webnovel with fair-play puzzles, distinctive character logic, suspense, restrained humor, continuity tracking, Git commits, and human approval gates. Use when bootstrapping the novel project, drafting or revising chapters, designing an arc, verifying clues and solutions, continuing approved arcs, or planning new nonrepeating arcs.
---

# Webnovel Studio — Vietnamese original fiction

Use this skill to build a complete, repeatable fiction-production workflow inside a local Git repository. Never imitate protected prose, characters, scenes, trademark settings, or unique plot devices of an existing novel. The target reading experience is clever problem-solving + eerie rule-bound mysteries + dry situational humor; the work itself must be original.

## Start and safety

1. Read `README_FIRST.md` in this skill folder and the project's `AGENTS.md`.
2. If the project does not exist, create it using `bash scripts/bootstrap.sh [optional-new-project-dir]` from this skill's own folder. The script **refuses to overwrite an existing path**, creates a project-local copy of the skill, initializes Git and commits the initial snapshot.
3. Inspect `approvals/approval.json` **before creating a new chapter**. The provided project starts in `chapter1_review`: chapter 001 is a first draft for the reader, and **writing chapter 002 or later is forbidden without an explicit new user approval**. Comments, silence, or an agent's own approval do not count.
4. With chapter 001 awaiting review, you may critique and polish chapter 001, produce the review note, run tests, commit changes locally, and STOP. Do not secretly draft future chapters even as temporary files.
5. Do not install third-party dependencies or fetch outside content just to run this skill. Do not push a remote or publish without explicit permission. Preserve the user's changes; never reset or clean an existing worktree.

## Workflow routing

- **Design or repair mystery/arc**: read `references/scenario-design.md`, `references/arc-factory.md`, project `arcs/arc-001/solution-sealed.md` and `arcs/arc-001/clue-ledger.csv` (only author/editor roles see sealed truth).
- **Draft or revise prose**: read `references/vietnamese-prose.md`, project story bible and chapter plan, plus the last 2–3 relevant chapters; update no canon until draft passes review.
- **Critique or continuity**: read `references/continuity-and-qa.md`. For blind-solver tests, NEVER expose `solution-sealed.md` or master secret; provide only the evidence excerpt visible to the reader at that point.
- **Continue after approval**: read `references/arc-factory.md`, user approval, `approvals/approval.json`, and `arcs/arc-001/outline.md`; generate in small verifiable batches with local Git commits.
- **Create future arcs**: read `references/nonrepeat-arc-design.md`, `continuity/arc-fingerprints.json`, `long-game/master-mystery.md` and current continuity status; avoid repeating setting, central mechanism, character cost, or final reveal.

## Quality contract

- Plot the real mechanism and solution before designing misleading clues; readers must have the relevant facts before the final inference. A reasonable reader may fail to guess, but must understand how it was possible afterward.
- Every important deduction needs visible evidence and at least one plausible alternative addressed. Protagonist cannot know information absent from their knowledge ledger. Knowledge outside character competence needs research or expert involvement.
- Never make supporting characters irrational to inflate the hero. Give them goals, information limits, and independent consequential choices.
- Each chapter must change the situation, relationships, evidence or stakes. Avoid formulaic recap, repetitive snark, unexplained power-ups, and fake cliffs every chapter.
- Write natural contemporary Vietnamese, with grounded tactile scene details, distinct character dialogue, no machine-translated Chinese idioms, no repeated slogans. No chapter 002+ before gate unlock.
- End each completed batch with `python3 .agents/skills/webnovel-studio/scripts/check_project.py .`, update continuity and review artifacts, then commit only project files using Git. On test failure, fix before committing.

## Useful in-project files

`AGENTS.md` (full operating contract), `bible/` (canon), `arcs/arc-001/` (30-chapter story arc), `continuity/` (knowledge and promises), `approvals/approval.json` (approval gate), `chapters/001.md` (first completed sample chapter), `reviews/` (reader feedback), `long-game/` (future arcs).

## Finish for phase 1

Report exact project path, Git HEAD, QA results and the location of `chapters/001.md`. Ask for approval or revision suggestions. **Stop**; do not do any second-arc or chapter 2 drafting until the user says to proceed.
