import json

with open("jlpt-exam-prep/scratch/problematic_reasons.json", "r", encoding="utf-8") as f:
    items = json.load(f)

g1_items = [x for x in items if x["bookId"] == "genki-1"]
g2_items = [x for x in items if x["bookId"] == "genki-2"]

print(f"Genki I problematic items: {len(g1_items)}")
for x in g1_items:
    print(f"[{x['id']} - {x['chapter']}] Q: {x['question']}")
    print(f"   Opt {x['optionIndex']}: '{x['optionText']}' -> Reason: '{x['reason']}'")

print(f"\nGenki II problematic items: {len(g2_items)}")
for x in g2_items[:15]:
    print(f"[{x['id']} - {x['chapter']}] Q: {x['question']}")
    print(f"   Opt {x['optionIndex']}: '{x['optionText']}' -> Reason: '{x['reason']}'")
