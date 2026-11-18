import pymupdf, json
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
doc = pymupdf.open(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf")

# Chapters 7 to 12 (printed pp. 36-53 -> PDF pp. 59-76 -> 0-indexed 58-75)
ch_pages = {
    "Ch7": [58, 59],       # pp. 36-37
    "Ch8": [60, 61],       # pp. 38-39
    "Ch9": [66, 67],       # pp. 44-45
    "Ch10": [68, 69],      # pp. 46-47
    "Ch11": [72, 73],      # pp. 50-51
    "Ch12": [74, 75]       # pp. 52-53
}

extracted = {}
for ch, pages in ch_pages.items():
    print(f"Extracting SKM N3 {ch}...")
    ch_data = {}
    for pno in pages:
        pix = doc[pno].get_pixmap(dpi=150)
        res, _ = ocr(pix.tobytes("png"))
        ch_data[f"PDF_{pno+1}_printed_{pno+1-23}"] = [l[1] for l in (res or [])]
    extracted[ch] = ch_data

with open("jlpt-exam-prep/scripts/skm3_ch7_ch12_ocr.json", "w", encoding="utf-8") as f:
    json.dump(extracted, f, ensure_ascii=False, indent=2)

print("Saved skm3_ch7_ch12_ocr.json successfully!")
