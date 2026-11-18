from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
for p in [47, 48]:
    img_path = f'c:/JLPT/jlpt-exam-prep/scripts/skm3_pdf_{p}.png'
    res, _ = ocr(img_path)
    print(f"=== PDF {p} (printed {p-23}) ===", flush=True)
    if res:
        for r in res:
            print(f"  {r[1]}", flush=True)
