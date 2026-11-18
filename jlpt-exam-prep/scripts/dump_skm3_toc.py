import json
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
results = {}
for p in range(3, 13):
    img_path = f'c:/JLPT/jlpt-exam-prep/scripts/skm3_p{p}.png'
    res, _ = ocr(img_path)
    lines = [r[1] for r in res] if res else []
    results[f"p{p}"] = lines

with open('c:/JLPT/jlpt-exam-prep/scripts/skm3_toc_ocr.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print('Saved SKM N3 TOC OCR to skm3_toc_ocr.json')
