import json

with open("jlpt-exam-prep/scratch/problematic_reasons.json", "r", encoding="utf-8") as f:
    items = json.load(f)

g1_items = [x for x in items if x["bookId"] == "genki-1"]
print(f"Genki I items to repair: {len(g1_items)}")

for i, x in enumerate(g1_items):
    print(f"{i+1}. [{x['id']} - {x['chapter']}]")
    print(f"   Q: {x['question']}")
    print(f"   Opt {x['optionIndex']}: '{x['optionText']}'")
    print(f"   Current Reason: '{x['reason']}'\n")
