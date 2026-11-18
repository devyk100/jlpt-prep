import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
books = json.load(open(ROOT / "src/data/bookSources.json", encoding="utf-8"))
n2 = [b for b in books if b["id"] == "skm-n2"][0]
base_cards = {c["id"]: c for c in json.load(open(ROOT / "content/base-reviewed.json", encoding="utf-8"))}

for i in range(6):
    s = n2["sections"][i]
    print(f"\n=== Section {i+1}: {s['name']} ===")
    for gid in s["grammarIds"]:
        c = base_cards.get(gid, {})
        print(f"  ID: {gid} | Title: {c.get('title')} | Formula: {c.get('formula')}")
