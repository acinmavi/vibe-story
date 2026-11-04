#!/usr/bin/env python3
"""Supplement structural QA with per-chapter length and frozen approval checks."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
approval = json.loads((root / "approvals/approval.json").read_text())
state = json.loads((root / "continuity/story-state.json").read_text())
chapters = sorted((root / "chapters").glob("*.md"))
errors = []
counts = []
for number, chapter in enumerate(chapters, 1):
    text = chapter.read_text()
    count = len(text.split())
    counts.append(count)
    if chapter.name != f"{number:03d}.md":
        errors.append(f"unexpected chapter: {chapter.name}")
    if not text.startswith(f"# Chương {number:03d} — "):
        errors.append(f"invalid heading: {chapter.name}")
    if not 1800 <= count <= 3000:
        errors.append(f"word count {chapter.name}: {count}")
if len(chapters) != state["last_written_chapter"]:
    errors.append("story state does not match chapter count")
arc2 = approval.get("arc002", {})
limit = arc2.get("end_chapter", 30) if arc2.get("approved") else 30
if len(chapters) > limit:
    errors.append(f"chapter count exceeds authorized limit {limit}")
if arc2.get("approved"):
    if not arc2.get("approval_text") or not arc2.get("approved_at_utc"):
        errors.append("arc 002 approval lacks explicit evidence")
    import re
    beats = [int(n) for n in re.findall(r"^\|\s*(\d{3})\s*\|", (root / "arcs/arc-002/CHAPTER_OUTLINE.md").read_text(), re.M)]
    if beats != list(range(arc2["start_chapter"], limit + 1)):
        errors.append("arc 002 outline does not match authorized range")
if approval["chapter1"]["approved_sha256"] != hashlib.sha256(chapters[0].read_bytes()).hexdigest():
    errors.append("approved chapter 001 changed")
for file in (root / "continuity").glob("*.json"):
    json.loads(file.read_text())
if errors:
    raise SystemExit("QA FAILED\n" + "\n".join(errors))
print(f"ARC QA PASS: {len(chapters)} chapters, {sum(counts)} words, range {min(counts)}–{max(counts)}, chapter 001 hash intact")
