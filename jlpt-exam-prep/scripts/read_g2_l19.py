import json

with open("jlpt-exam-prep/scripts/g2_l19_ocr.json", encoding="utf-8") as f:
    data = json.load(f)

print(f"Pages in g2_l19_ocr.json: {list(data.keys())}")
for p, lines in list(data.items())[:2]:
    print(f"=== Page {p} ===")
    for l in lines[:10]:
        print("  ", l)
