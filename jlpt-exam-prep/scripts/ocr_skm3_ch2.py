import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
doc = pymupdf.open(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf")

# Inspect PDF pages 41, 42, 43 (printed pages 18, 19, 20)
for pno in [40, 41, 42]:
    pix = doc[pno].get_pixmap(dpi=150)
    res, _ = ocr(pix.tobytes("png"))
    print(f"=== PDF Page {pno+1} (Printed p. {pno+1-23}) ===")
    for l in (res or []):
        print(l[1])
