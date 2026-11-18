import json

with open("jlpt-exam-prep/scripts/skm2_ch14_ch21_ocr.json", encoding="utf-8") as f:
    data = json.load(f)

for ch, pages in data.items():
    print(f"\n==================== {ch} ====================")
    for p, lines in pages.items():
        print(f"--- {p} ---")
        for l in lines:
            # Look for Japanese headings or grammar patterns
            if any(k in l for k in ["～", "課", "【", "普通形", "名詞", "動詞", "例", "意味", "注意"]):
                print("   *", l)
            elif len(l) > 0 and len(l) < 30:
                print("    ", l)
