import json
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()

results = {}
for p in range(241, 251):
    img_path = f'c:/JLPT/jlpt-exam-prep/scripts/g2_p{p}_printed{p-8}.png'
    res, _ = ocr(img_path)
    lines = [r[1] for r in res] if res else []
    results[f"PDF_{p}_printed_{p-8}"] = lines

with open('c:/JLPT/jlpt-exam-prep/scripts/g2_l22_ocr.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved Lesson 22 OCR results to g2_l22_ocr.json")
