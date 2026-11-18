import sys
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()

for p in range(168, 176):
    img_path = f'c:/JLPT/jlpt-exam-prep/scripts/g2_p{p}_printed{p-8}.png'
    res, _ = ocr(img_path)
    print(f"=== Page PDF {p} (printed {p-8}) ===", flush=True)
    if res:
        for r in res:
            line = r[1]
            if any(k in line for k in ['Grammar', '尊敬語', 'お〜', 'お+', 'お +', 'はず', 'てくれて', 'ありがとう', 'てよかった', '1 ', '2 ', '3 ', '4 ']):
                print(f"  {line}", flush=True)
