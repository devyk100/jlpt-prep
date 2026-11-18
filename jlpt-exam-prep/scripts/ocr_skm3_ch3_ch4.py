import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
doc = pymupdf.open(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf")

# Inspect PDF pages 44 to 49 (printed pages 21 to 26)
for pno in range(44, 50):
    pix = doc[pno].get_pixmap(dpi=150)
    res, _ = ocr(pix.tobytes("png"))
    print(f"=== PDF Page {pno+1} (Printed p. {pno+1-23}) ===")
    for l in (res or [])[:8]:
        print("  ", l[1])
