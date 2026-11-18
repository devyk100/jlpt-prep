import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
matrix = json.load(open(ROOT / "audit/source-coverage-matrix.json", encoding="utf-8"))
cards = json.load(open(ROOT / "content/base-reviewed.json", encoding="utf-8"))

cards_by_id = {c["id"]: c for c in cards}

authentic_rows = []
problematic_rows = []

for idx, m in enumerate(matrix):
    cid = m.get("cardId")
    b = m.get("sourceBook")
    sec = m.get("sourceSection")
    ex_ids = m.get("exampleIds", [])
    status = m.get("status")
    
    # Check if card exists in base-reviewed
    card = cards_by_id.get(cid)
    if not card:
        problematic_rows.append((idx, cid, b, sec, "Card does not exist in base-reviewed", ex_ids))
        continue
    
    # Check actual sentence IDs of the card
    real_s_ids = {s.get("id") for s in card.get("sentences", []) if "id" in s}
    for ex in card.get("examples", []):
        if isinstance(ex, dict) and "id" in ex:
            real_s_ids.add(ex["id"])
    
    # Check if claimed exampleIds match real_s_ids
    invalid_ids = [eid for eid in ex_ids if eid not in real_s_ids]
    if invalid_ids or not ex_ids:
        problematic_rows.append((idx, cid, b, sec, f"Invalid/fabricated exampleIds: {invalid_ids}", list(real_s_ids)))
    else:
        authentic_rows.append((idx, cid, b, sec, ex_ids))

print("=== SOURCE COVERAGE MATRIX AUDIT ===")
print(f"Total rows: {len(matrix)}")
print(f"Authentic rows with verified example IDs: {len(authentic_rows)}")
print(f"Problematic rows with invalid/fabricated example IDs: {len(problematic_rows)}")

by_book_prob = {}
for idx, cid, b, sec, reason, _ in problematic_rows:
    by_book_prob[b] = by_book_prob.get(b, 0) + 1
for b, count in by_book_prob.items():
    print(f"  {b}: {count} problematic rows")
