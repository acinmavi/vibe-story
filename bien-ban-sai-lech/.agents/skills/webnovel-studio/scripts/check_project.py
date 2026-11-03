#!/usr/bin/env python3
"""Zero-dependency checks for an original serialized Vietnamese mystery project.

Usage: python3 .agents/skills/webnovel-studio/scripts/check_project.py [project_root]
This is structural QA, NOT a substitute for independent story critique.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []
    warnings: list[str] = []

    required = [
        "AGENTS.md", "README.md", "approvals/approval.json", "bible/world.md",
        "arcs/arc-001/arc-spec.md", "arcs/arc-001/solution-sealed.md",
        "arcs/arc-001/outline.md", "arcs/arc-001/clue-ledger.csv",
        "chapters/001.md", "continuity/story-state.json",
        "continuity/character-knowledge.json", "continuity/open-loops.json",
        "continuity/arc-fingerprints.json", ".agents/skills/webnovel-studio/SKILL.md",
    ]
    for rel in required:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")
    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        return 1

    def load(rel: str):
        try:
            return json.loads((root / rel).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON {rel}: {exc}")
            return {}

    approval = load("approvals/approval.json")
    state = load("continuity/story-state.json")
    ck = load("continuity/character-knowledge.json")
    loops = load("continuity/open-loops.json")
    fingerprints = load("continuity/arc-fingerprints.json")

    ch_files = sorted((root / "chapters").glob("[0-9][0-9][0-9].md"))
    nums = [int(p.stem) for p in ch_files]
    if not nums or nums[0] != 1:
        errors.append("chapters must start with 001.md")
    if nums != list(range(1, len(nums) + 1)):
        errors.append(f"chapters must be sequential without gaps: {nums}")
    if len(nums) > 30 and not approval.get("arc002", {}).get("approved", False):
        errors.append("chapter 031+ is locked until separate arc 002 approval")
    if len(nums) > 1:
        if not approval.get("chapter1", {}).get("approved", False):
            errors.append("chapters 002+ exist without explicit chapter 001 approval")
        if not approval.get("arc001_writing", {}).get("approved", False):
            errors.append("chapters 002+ exist without approval to write arc 001")
    if approval.get("stage") == "chapter1_review" and len(nums) > 1:
        errors.append("approval stage chapter1_review cannot contain chapter 002+")

    if approval.get("chapter1", {}).get("approved"):
        approved = approval["chapter1"]
        if not approved.get("approval_text") or not approved.get("approved_at_utc"):
            errors.append("chapter1 approval must contain human approval text + timestamp")
        expected = approved.get("approved_sha256")
        actual = hashlib.sha256((root / "chapters/001.md").read_bytes()).hexdigest()
        if not expected or expected != actual:
            errors.append("approved chapter 001 was changed or approval SHA-256 is missing")
    if approval.get("arc001_writing", {}).get("approved"):
        if not approval.get("chapter1", {}).get("approved"):
            errors.append("arc001_writing approved without chapter1 approved")
        if not approval["arc001_writing"].get("approval_text"):
            errors.append("arc001 approval must contain explicit user evidence")

    if state.get("last_written_chapter") != (max(nums) if nums else 0):
        errors.append("story state last_written_chapter mismatches chapter files")
    if state.get("phase") != approval.get("stage"):
        errors.append("story state phase mismatches approval stage")
    if not approval.get("chapter1", {}).get("approved") and state.get("do_not_write_after_chapter") != 1:
        errors.append("initial lock do_not_write_after_chapter must be 1")

    ch1 = (root / "chapters/001.md").read_text(encoding="utf-8")
    count = len(ch1.split())
    if count < 1800:
        errors.append(f"chapter 001 too short for current target: {count} words")
    elif count > 3400:
        warnings.append(f"chapter 001 longer than planned range: {count} words")
    if "# Chương 001" not in ch1:
        errors.append("chapter 001 missing title header")

    title_pattern = re.compile(r"^\|\s*(\d{3})\s*\|", re.MULTILINE)
    outline = (root / "arcs/arc-001/outline.md").read_text(encoding="utf-8")
    chapter_beats = [int(x) for x in title_pattern.findall(outline)]
    if chapter_beats != list(range(1, 31)):
        errors.append("arc 001 outline must have exactly 001..030 row entries")

    clues = []
    try:
        with (root / "arcs/arc-001/clue-ledger.csv").open(encoding="utf-8", newline="") as f:
            clues = list(csv.DictReader(f))
        if len(clues) < 8 or len(set(c["id"] for c in clues)) != len(clues):
            errors.append("clue ledger needs >=8 unique clue IDs")
        for c in clues:
            if int(c["first_chapter"]) > int(c["required_by_chapter"]):
                errors.append(f"clue revealed after its required payoff: {c['id']}")
            if not (1 <= int(c["first_chapter"]) <= 30):
                errors.append(f"clue outside first arc: {c['id']}")
    except (ValueError, KeyError, OSError, csv.Error) as exc:
        errors.append(f"clue ledger invalid: {exc}")

    if ck.get("as_of_chapter", 0) > len(nums):
        errors.append("character knowledge claims future chapters")
    if loops.get("as_of_chapter", 0) > len(nums):
        errors.append("open loop ledger claims future chapters")
    if not fingerprints.get("arcs"):
        errors.append("arc fingerprint history missing")

    banned = ["Ngoạn Gia Hung Mãnh", "Lý Ngang", "玩家凶猛", "李昂"]
    for p in ch_files:
        content = p.read_text(encoding="utf-8")
        if not content.startswith(f"# Chương {int(p.stem):03d}"):
            errors.append(f"chapter has invalid heading: {p.name}")
        for phrase in banned:
            if phrase.casefold() in content.casefold():
                errors.append(f"possible copied-world reference in {p.name}: {phrase}")

    for msg in warnings:
        print(f"WARN: {msg}")
    if errors:
        for msg in errors:
            print(f"FAIL: {msg}")
        print(f"QA FAILED with {len(errors)} error(s)")
        return 1
    print(f"QA PASS: {len(ch_files)} chapter(s), {count} words in chapter 001, "
          f"{len(chapter_beats)} outline beats, {len(clues)} tracked clues, "
          f"stage={approval.get('stage')}, no hidden extra chapter")
    print("NOTE: human literary critique and a real blind-solver review are still required")
    return 0


if __name__ == "__main__":
    sys.exit(main())
