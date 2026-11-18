import json

with open("jlpt-exam-prep/scripts/g2_l19_ocr.json", encoding="utf-8") as f:
    data = json.load(f)

for p in ['PDF_172_printed_164', 'PDF_173_printed_165', 'PDF_174_printed_166', 'PDF_175_printed_167', 'PDF_176_printed_168', 'PDF_177_printed_169']:
    print(f"=== {p} ===")
    for l in data[p][:12]:
        print("  ", l)
