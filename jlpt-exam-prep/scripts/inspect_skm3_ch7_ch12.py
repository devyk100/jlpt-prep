import json

with open("jlpt-exam-prep/scripts/skm3_ch7_ch12_ocr.json", encoding="utf-8") as f:
    data = json.load(f)

for ch, pages in data.items():
    print(f"\n==================== {ch} ====================")
    for p, lines in pages.items():
        print(f"--- {p} ---")
        for l in lines[:8]:
            print("  ", l)
