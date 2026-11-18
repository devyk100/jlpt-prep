from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
for p in range(35, 43):
    img_path = f'c:/JLPT/jlpt-exam-prep/scripts/skm3_pdf_{p}.png'
    res, _ = ocr(img_path)
    if res:
        print(f"=== PDF {p} ===")
        for r in res:
            text = r[1]
            if any(k in text for k in ['第1課', '第 1 課', '1課', 'うちに', '間', 'ところ', 'てから', '16']):
                print("  ", text)
