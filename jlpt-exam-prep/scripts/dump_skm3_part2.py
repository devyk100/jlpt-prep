import pymupdf, json
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
doc = pymupdf.open(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf")

pages_data = {}
for pno in range(126, 138): # PDF pages 127 to 138
    pix = doc[pno].get_pixmap(dpi=150)
    res, _ = ocr(pix.tobytes("png"))
    lines = [l[1] for l in (res or [])]
    pages_data[pno + 1] = lines

with open("jlpt-exam-prep/scripts/skm3_part2_ocr.json", "w", encoding="utf-8") as f:
    json.dump(pages_data, f, ensure_ascii=False, indent=2)

print("Saved skm3_part2_ocr.json with", len(pages_data), "pages")
