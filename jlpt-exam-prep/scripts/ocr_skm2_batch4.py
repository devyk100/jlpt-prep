import fitz
import numpy as np
import cv2
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
pdf_path = r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N2\Shin_Kanzen_Masuta_N2-Bunpou.pdf"
doc = fitz.open(pdf_path)

# Target pages: 106, 110, 114, 118, 122, 126
target_pages = [106, 110, 114, 118, 122, 126]

for p in target_pages:
    page = doc[p - 1]
    pix = page.get_pixmap(dpi=150)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
    if pix.n == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    elif pix.n == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    result, _ = ocr(img)
    text = "\n".join([line[1] for line in result]) if result else ""
    print(f"\n==================== PDF Page {p} (Printed p. {p-10}) ====================")
    print(text[:450])
