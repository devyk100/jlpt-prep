import pymupdf
import time
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
doc = pymupdf.open(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N2\Shin_Kanzen_Masuta_N2-Bunpou.pdf")

t0 = time.time()
for pno in range(17, 22): # 5 pages
    pix = doc[pno].get_pixmap(dpi=120)
    res, _ = ocr(pix.tobytes("png"))
    lines = [line[1] for line in (res or [])]
    print(f"Page {pno+1}: {len(lines)} lines extracted in {time.time()-t0:.2f}s")
    t0 = time.time()
