# Continuity, QA and reader gates

## Truth categories

- Author-truth: immutable facts in sealed arc files and world bible.
- Character-knowledge: per-character facts and when they learned them; a character cannot infer facts beyond seen evidence + competence.
- Reader-knowledge: facts published by chapter; author-only documents never treated as published.
- Promise ledger: foreshadowed questions, evidence, expected payoff and status.

## Before drafting a chapter

Read chapter beat from outline, recent 2–3 chapters, relevant character knowledge, rule ledger, unfinished promises and arc truth (author role only). List what each character knows, wants and mistakenly believes at scene start. Confirm each pivotal action is possible with their actual tools/time.

## After drafting

- Check chapter for lore contradictions, character position, exact clock/date, physical inventory, wounds, costs, and known facts.
- Add observed events to `continuity/canon-log.md` only when chapter is approved as canon for this drafting pass.
- Update `continuity/character-knowledge.json`, `continuity/open-loops.json`, and `continuity/story-state.json` after chapter commit.
- Read next planned chapter to ensure its setup survived revisions.

## Independent reviewer rubric (0–5, weights)

Causal/solution fairness 30%, character competence and agency 20%, tension and pacing 20%, original voice and humor 15%, continuity and world-promise 15%. Give evidence + severity for each failure. A 5/5 score from the same authoring model is not trustworthy; keep an independent review pass.

Blocking failures: newly invented solution rule, impossible character knowledge, major temporal contradiction, copied distinctive scene, artificial stupidity of other characters, erased lasting consequence, chapter >= 002 before explicit user approval.

## Review gate

Run project validator: `python3 .agents/skills/webnovel-studio/scripts/check_project.py .`.
Approval exists only after an explicit human utterance (e.g., 'Tôi duyệt chương 1, viết tiếp arc 1') in the current Codex conversation. Agent records exact statement and time in approvals JSON. Do not infer approval from the existence of a task, a comment praising a sentence, or silence.

When a chapter is approved by the user, preserve the approved snapshot through Git and record it in review notes. Never rewrite an approved chapter quietly; propose a change and request permission if continuity later requires it.
