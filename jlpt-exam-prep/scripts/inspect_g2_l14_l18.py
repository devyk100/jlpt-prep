import json

with open("jlpt-exam-prep/scripts/g2_l14_l18_ocr.json", encoding="utf-8") as f:
    data = json.load(f)

for lesson, pages in data.items():
    print(f"\n==================== {lesson} ====================")
    for p, lines in pages.items():
        print(f"--- {p} ---")
        for l in lines[:6]:
            print("  ", l)
