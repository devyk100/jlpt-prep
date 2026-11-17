import pymupdf
import os
import sys

def find_toc_pages(pdf_path, name, search_range=20):
    print(f"Checking {name}...")
    doc = pymupdf.open(pdf_path)
    out_dir = os.path.join(r"c:\JLPT\jlpt-exam-prep\audit\pdf_inspect", name)
    os.makedirs(out_dir, exist_ok=True)
    
    # Save pages as images
    for pno in range(min(search_range, len(doc))):
        page = doc[pno]
        pix = page.get_pixmap(dpi=150)
        out_path = os.path.join(out_dir, f"page_{pno+1:02d}.png")
        pix.save(out_path)
    print(f"Saved {search_range} pages to {out_dir}")

find_toc_pages(r"C:\Users\devyk\Downloads\にほんご\Genki Textbook 2 - 3rd Edition.pdf", "genki2", 18)
find_toc_pages(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf", "skm3", 16)
find_toc_pages(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N2\Shin_Kanzen_Masuta_N2-Bunpou.pdf", "skm2", 16)
