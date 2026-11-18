import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
cards = json.load(open(ROOT / "content/base-reviewed.json", encoding="utf-8"))
cards_by_id = {c["id"]: c for c in cards}

for cid in ["skm2-c1-ni-saishite", "skm2-c1-tatan-ni", "added-n2-1-69", "added-n3-p3-1-131", "added-g2-13-20"]:
    c = cards_by_id.get(cid, {})
    s_ids = [s.get("id") for s in c.get("sentences", [])]
    print(f"{cid}: sentences={len(c.get('sentences', []))}, IDs={s_ids}")
    if "examples" in c:
        print(f"   examples={len(c.get('examples', []))}")
