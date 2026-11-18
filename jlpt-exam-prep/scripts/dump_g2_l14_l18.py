import pymupdf, json
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
doc = pymupdf.open(r"C:\Users\devyk\Downloads\にほんご\Genki Textbook 2 - 3rd Edition.pdf")

# Lessons 14 to 18 page ranges (0-indexed page numbers: printed p + 8 - 1)
# Lesson 14: printed 50-55 -> PDF 58-63 -> 0-indexed 57-62
# Lesson 15: printed 74-77 -> PDF 82-85 -> 0-indexed 81-84
# Lesson 16: printed 96-103 -> PDF 104-111 -> 0-indexed 103-110
# Lesson 17: printed 118-123 -> PDF 126-131 -> 0-indexed 125-130
# Lesson 18: printed 140-145 -> PDF 148-153 -> 0-indexed 147-152

ranges = [
    ("L14", range(57, 63)),
    ("L15", range(81, 85)),
    ("L16", range(103, 111)),
    ("L17", range(125, 131)),
    ("L18", range(147, 153))
]

results = {}
for name, p_range in ranges:
    print(f"Processing Genki II {name}...")
    lesson_data = {}
    for pno in p_range:
        pix = doc[pno].get_pixmap(dpi=150)
        res, _ = ocr(pix.tobytes("png"))
        lesson_data[f"PDF_{pno+1}_printed_{pno+1-8}"] = [l[1] for l in (res or [])]
    results[name] = lesson_data

with open("jlpt-exam-prep/scripts/g2_l14_l18_ocr.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved g2_l14_l18_ocr.json successfully!")
