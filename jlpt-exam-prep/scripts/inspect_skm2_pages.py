import fitz
import numpy as np
import cv2
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
pdf_path = r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N2\Shin_Kanzen_Masuta_N2-Bunpou.pdf"
doc = fitz.open(pdf_path)

for page_idx in [2, 3, 4, 15, 16, 17, 18, 19, 20, 21, 22]:
    page = doc[page_idx]
    pix = page.get_pixmap(dpi=150)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
    if pix.n == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    elif pix.n == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    result, _ = ocr(img)
    text = "\n".join([f"{line[1]} (score: {line[2]})" for line in result]) if result else ""
    print(f"\n==================== PDF Page {page_idx + 1} (index {page_idx}) ====================")
    print(text[:600])
