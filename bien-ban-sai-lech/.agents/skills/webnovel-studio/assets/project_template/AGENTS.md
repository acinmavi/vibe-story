# AGENTS.md — Biên Bản Sai Lệch

This file is the binding operating contract for Codex in this Git repo. All creative output must be ORIGINAL. Genre: Vietnamese contemporary urban supernatural mystery, procedural suspense, flawed clever investigator, deadpan situational humor. High-level inspiration: reader enjoys clever puzzle-driven long webnovels; never imitate an existing author, character, storyline, signature game mechanics, scenes or wording.

## Priority order

1. Explicit instructions and approvals from the human reader.
2. `approvals/approval.json` stage gate.
3. Immutable seeded world constraints in `bible/`, sealed truth in `arcs/arc-001/solution-sealed.md`.
4. Current `arcs/arc-001/outline.md`, clue ledger, character knowledge and published chapters.
5. Skill: `.agents/skills/webnovel-studio/SKILL.md` and its references.

## Startup

- Verify `git status --short` and current branch; local repo only; never push or make remote without explicit permission.
- Read approval status first. Initial phase: `chapter1_review`; `chapters/001.md` is an ORIGINAL chapter one draft already provided in the starter pack.
- Read and editorial-review chapter 001; improve it if needed without changing locked arc solution. Create/update `reviews/chapter-001-review.md` with objective issues and what changed.
- Run `python3 .agents/skills/webnovel-studio/scripts/check_project.py .` and fix failures.
- `git add` changes and make descriptive local commit if any. Report path/HEAD/QA/chapter for user review. STOP.
- **Do not** write `chapters/002.md` or any further prose before explicit human approval. No workaround: not scratchpad, temporary folder, hidden notes or spawned agent.

## Approval protocol

Upon **explicit** user instruction like "Tôi duyệt chương 1, viết tiếp arc 1":
- Set `approvals/approval.json` to `chapter1.approved=true`, `arc001_writing.approved=true`, `stage=arc1_writing`; record exact user's approval text, time and approved chapter 001 SHA-256. A user request merely to revise chapter 1 is not approval for arc.
- Use only approved `chapters/001.md` as canon. If its content changes later, ask again before changing published canon.
- Plan each batch of 2–4 subsequent chapters, follow `arcs/arc-001/outline.md` and `clue-ledger.csv`. Revise beat order if causal continuity requires; update ledger + note reason.
- Draft each chapter in natural Vietnamese, with 1,900–3,000 words as target (not a hard filler quota). Perform two revision passes for logic and language. Reviewer doesn't see sealed solution during blind test.
- Update continuity files, run QA and commit at each batch. Stop at chapter 030. Never begin arc 002 without separate explicit approval.

## Editorial quality

- Every scene changes knowledge, choice, cost or interpersonal dynamic.
- Each false hypothesis must be rational and testable. Major deductions cite accessible evidence, not secrets from author notes.
- Every recurring character gets independent objectives and consequential action; protagonist has limited knowledge and may be wrong.
- Preserve an eerie, concrete atmosphere and a few flashes of dry situational humor; avoid parroting source fiction's exact patterns.
- Power/phenomenon rules remain bounded. Ambiguity in world origin is permissible; ambiguity in a case's causal resolution is not.
- Track facts in `continuity/character-knowledge.json`, loops in `continuity/open-loops.json`, and major changes in `continuity/canon-log.md`.
- When factual research is needed (e.g., building code, rescue procedures), do not invent precise legal or safety claims; verify or mark them for research. Story is fiction, not an operational safety guide.

## Local repo discipline

Use `git init` only if no .git exists (bootstrap already initializes). No network required, no global git config. No destructive commands. Do not discard user's uncommitted changes. Commit source Markdown/JSON/CSV, not temporary caches. The local skill copy in `.agents/skills/webnovel-studio/` is part of repo for portability.

## Completion requirements

- Phase 1: project bootstrap, chapter 001 review, QA PASS, local git commit, report and WAIT for approval.
- Phase 2 (only after approval): finish chapters 002–030 + QA/continuity/review/commits, and report for arc-level approval.
- Phase 3 (only after further approval): design a new 20–50-chapter arc, compare `continuity/arc-fingerprints.json`, get concept approval before prose.
