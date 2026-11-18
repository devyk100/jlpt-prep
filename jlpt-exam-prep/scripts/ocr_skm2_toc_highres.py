import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
doc = pymupdf.open(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N2\Shin_Kanzen_Masuta_N2-Bunpou.pdf")

# Inspect TOC pages: PDF pages 5 and 6
for pno in [4, 5]:
    pix = doc[pno].get_pixmap(dpi=200)
    res, _ = ocr(pix.tobytes("png"))
    print(f"=== TOC PDF Page {pno+1} ===")
    for l in (res or []):
        print(l[1])
