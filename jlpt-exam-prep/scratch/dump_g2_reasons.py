import json

with open("jlpt-exam-prep/scratch/problematic_reasons.json", "r", encoding="utf-8") as f:
    items = json.load(f)

g2_items = [x for x in items if x["bookId"] == "genki-2"]
print(f"Genki II items to repair: {len(g2_items)}")

for i, x in enumerate(g2_items):
    print(f"{i+1}. [{x['id']} - {x['chapter']}]")
    print(f"   Q: {x['question']}")
    print(f"   Opt {x['optionIndex']}: '{x['optionText']}'")
    print(f"   Current Reason: '{x['reason']}'\n")
