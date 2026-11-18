import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
books = json.load(open(ROOT / "src/data/bookSources.json", encoding="utf-8"))
matrix = {m.get("cardId"): m for m in json.load(open(ROOT / "audit/source-coverage-matrix.json", encoding="utf-8"))}
base_cards = {c["id"]: c for c in json.load(open(ROOT / "content/base-reviewed.json", encoding="utf-8"))}
n2 = [b for b in books if b["id"] == "skm-n2"][0]

missing = []
for s in n2["sections"]:
    for gid in s["grammarIds"]:
        if gid not in matrix:
            c = base_cards.get(gid, {})
            missing.append((s["name"], gid, c.get("title", "")))

print(f"Total missing: {len(missing)}")
for sname, gid, title in missing:
    print(f"  {sname} | {gid} | {title}")
