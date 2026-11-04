#!/usr/bin/env python3
"""Record a reviewed Arc2 batch. Input facts remain lead-writer curated."""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
batch = json.loads(Path(sys.argv[1]).read_text())
def load(name):
    return json.loads((root / name).read_text())
def save(name, data):
    (root / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
state = load("continuity/story-state.json")
resources = load("continuity/resources.json")
start, end = batch["start"], batch["end"]
assert start == state["last_written_chapter"] + 1
assert 2 <= end - start + 1 <= 4 and end <= 68
assert resources["cash_pence"] == batch["cash_start"]
assert batch["cash_start"] + batch.get("income", 0) - batch["expenses"] == batch["cash_end"]
for number in range(start, end + 1):
    text = (root / f"chapters/{number:03d}.md").read_text()
    assert text.startswith(f"# Chương {number:03d} — ") and 1800 <= len(text.split()) <= 3000
state.update(last_written_chapter=end, date_in_story=batch["date"], location=batch["location"])
resources.update(as_of_chapter=end, cash_pence=batch["cash_end"], iona_debt_pounds=batch.get("debt_end", resources["iona_debt_pounds"]))
resources["notes"].append(batch["money_note"])
save("continuity/story-state.json", state)
save("continuity/resources.json", resources)
knowledge = load("continuity/character-knowledge.json")
knowledge["as_of_chapter"] = end
knowledge["MC_verified"].extend(batch["facts"])
knowledge["current_snapshot"] = {"as_of_chapter": end, "date": batch["date"], "cash_pence": batch["cash_end"], "sequence": "9 Mystery Pryer, digestion incomplete", "location": batch["location"], "Klein_contact": "none; K0 unchanged", "knowledge_limit": batch["limits"]}
save("continuity/character-knowledge.json", knowledge)
for name in ["open-loops", "klein-investigation", "partnership-ledger", "tarot-meeting-ledger", "combat-loadouts", "cattleya-bernadette-ledger", "trade-ledger"]:
    path = f"continuity/{name}.json"
    data = load(path)
    data["as_of_chapter"] = end
    save(path, data)
fingerprints = load("continuity/arc-fingerprints.json")
arc = next(a for a in fingerprints["arcs"] if a["id"] == 2)
arc["chapter_range"] = f"031–068 authorized;031–{end:03d} written"
arc["actual_date"] = batch["date"]
save("continuity/arc-fingerprints.json", fingerprints)
current = f"# Trạng thái hiện tại — sau chương{end:03d}\n\nNgày {batch['date']}; {batch['location']}. Arc2 đã duyệt031–068; chưa được viết069/Arc3.\n\n"
current += f"Tiền {batch['cash_end']}p; nợIona {resources['iona_debt_pounds']}£. 8£công gồm1£ứng,7£chưa nhận nếu chưa có cảnh nghiệmthu. Phòng/vé khách trả trực tiếp. Seq9chưa tiêu hóa hoàn toàn; không tự cấp phép/côngthức/gray.\n\n"
current += "## Sự kiện mới đã viết\n\n" + "\n".join("- " + fact for fact in batch["facts"]) + "\n\n"
current += "## Giới hạn và việc cần theo\n\n" + batch["limits"] + "\n\n"
current += "Các sự kiện trước giữ nguồn tại KNOWLEDGE_LEDGER,resources,setup-payoff và bản thảo. Chìa cũ/gốc rãnh đã bàn giao;không tự đưa vềtúi. K0/Tarot/Cattleya/Bernadette không đổi khi không có cảnh mới.\n"
(root / "continuity/CURRENT_STATE.md").write_text(current)
print(f"Recorded reviewed batch {start:03d}–{end:03d};cash {batch['cash_end']}p")
