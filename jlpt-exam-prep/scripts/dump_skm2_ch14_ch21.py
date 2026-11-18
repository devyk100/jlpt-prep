import pymupdf, json
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
doc = pymupdf.open(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N2\Shin_Kanzen_Masuta_N2-Bunpou.pdf")

# In SKM N2, let's verify page offset around pp. 64 to 99
# Let's inspect pages 74 to 109 in the PDF (corresponding to printed pp. 64 to 99)
ch_ranges = {
    "Ch14": [73, 74, 75, 76],        # printed pp. 64-67 (0-indexed 73-76)
    "Ch15": [77, 78, 79, 80, 81],    # printed pp. 68-72
    "Ch16": [83, 84, 85, 86],        # printed pp. 74-77
    "Ch17": [87, 88, 89, 90],        # printed pp. 78-81
    "Ch18": [91, 92, 93, 94],        # printed pp. 82-85
    "Ch19": [95, 96, 97, 98],        # printed pp. 86-89
    "Ch20": [99, 100, 101, 102],     # printed pp. 90-93
    "Ch21": [105, 106, 107, 108]     # printed pp. 96-99
}

extracted = {}
for ch, pages in ch_ranges.items():
    print(f"Extracting SKM N2 {ch}...")
    ch_text = {}
    for pno in pages:
        pix = doc[pno].get_pixmap(dpi=150)
        res, _ = ocr(pix.tobytes("png"))
        ch_text[f"PDF_{pno+1}"] = [l[1] for l in (res or [])]
    extracted[ch] = ch_text

with open("jlpt-exam-prep/scripts/skm2_ch14_ch21_ocr.json", "w", encoding="utf-8") as f:
    json.dump(extracted, f, ensure_ascii=False, indent=2)

print("Saved skm2_ch14_ch21_ocr.json successfully!")
