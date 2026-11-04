#!/usr/bin/env python3
"""Build Arc2 reading files from validated chapter sources; never edit chapters."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
state = json.loads((root / "continuity/story-state.json").read_text())
approval = json.loads((root / "approvals/approval.json").read_text())["arc002"]
last = state["last_written_chapter"]
if not approval["approved"] or not 31 <= last <= approval["end_chapter"]:
    raise SystemExit("Arc2 reader is outside the approved chapter range")
paths = [root / f"chapters/{n:03d}.md" for n in range(31, last + 1)]
texts = [path.read_text().strip() for path in paths]
for number, text in zip(range(31, last + 1), texts):
    if not text.startswith(f"# Chương {number:03d} — "):
        raise SystemExit(f"Invalid chapter heading: {number:03d}")
if (root / f"chapters/{last + 1:03d}.md").exists():
    raise SystemExit("Unrecorded next chapter exists; update and review state first")
count = len(paths)
target = approval["target_chapters"]
status = "Hoàn tất" if count == target else "Đang viết"
book = (f"# Arc002 — Cánh cửa cuối ca\n\n{status}:031–{last:03d} "
        f"({count}/{target} chương). Bản đọc liền chỉ gồm những chương đã có.\n\n")
book += "\n\n---\n\n".join(texts) + "\n"
index_path = root / "DOC_TRUYEN.md"
index = index_path.read_text().split("## Arc002 —", 1)[0]
index += ("## Arc002 — Cánh cửa cuối ca\n\n"
          f"Đã có {count}/{target} chương. [Đọc liền](ARC_002.md). Arc1 giữ nguyên.\n\n"
          "| Chương | Tên | Từ |\n|---:|---|---:|\n")
for path, text in zip(paths, texts):
    title = text.splitlines()[0].split(" — ", 1)[1]
    index += f"|{path.stem}|[{title}](chapters/{path.name})|{len(text.split())}|\n"
(root / "ARC_002.md").write_text(book)
index_path.write_text(index)
print(f"Synced Arc2 reader: {count}/{target} chapters, {sum(len(t.split()) for t in texts)} words")
