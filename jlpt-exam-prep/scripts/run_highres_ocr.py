import pymupdf, json
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()

def extract_high_res(pdf_path, page_num):
    doc = pymupdf.open(pdf_path)
    page = doc[page_num]
    pix = page.get_pixmap(dpi=300) # High DPI for crisp Japanese text
    res, _ = ocr(pix.tobytes("png"))
    return [line[1] for line in (res or [])]

print("Extracting SKM N3 Page 127 (p. 105)...")
lines_n3_105 = extract_high_res(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf", 126)

print("Extracting SKM N2 Page 150 (p. 141)...")
lines_n2_141 = extract_high_res(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N2\Shin_Kanzen_Masuta_N2-Bunpou.pdf", 149)

with open("jlpt-exam-prep/scripts/highres_p2_sample.json", "w", encoding="utf-8") as f:
    json.dump({
        "skm3_p105": lines_n3_105,
        "skm2_p141": lines_n2_141
    }, f, ensure_ascii=False, indent=2)

print("Done saving highres_p2_sample.json")
