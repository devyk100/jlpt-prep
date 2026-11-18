import pymupdf

doc_n2 = pymupdf.open(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N2\Shin_Kanzen_Masuta_N2-Bunpou.pdf")
print("=== SKM N2 All Bookmarks ===")
for lvl, title, page in doc_n2.get_toc():
    print(f"p.{page}: {title}")

doc_n3 = pymupdf.open(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf")
print("\n=== SKM N3 Searching First 25 Pages for TOC ===")
for pno in range(25):
    txt = doc_n3[pno].get_text()
    if len(txt.strip()) > 50:
        lines = [line.strip() for line in txt.split("\n") if line.strip()]
        first_few = " | ".join(lines[:6])
        print(f"Page {pno+1}: {first_few[:120]}")
