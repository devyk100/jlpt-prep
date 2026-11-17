import pymupdf
import os

def render_page(pdf_path, pno, out_path):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    doc = pymupdf.open(pdf_path)
    pix = doc[pno-1].get_pixmap(dpi=150)
    pix.save(out_path)
    print(f"Rendered {os.path.basename(pdf_path)} page {pno} -> {out_path}")

# Genki 1: Lesson 3 (p. 84 - 89 in book, let's check around PDF p. 95-105)
# Let's find exact PDF pages for Genki 1 Lesson 3 and Lesson 12
render_page(r"C:\Users\devyk\Downloads\にほんご\Genki (N5)\Genki Textbook 1 - 3rd Edition.pdf", 96, r"c:\JLPT\jlpt-exam-prep\audit\pdf_inspect\interior\g1_l3_p96.png")
render_page(r"C:\Users\devyk\Downloads\にほんご\Genki (N5)\Genki Textbook 1 - 3rd Edition.pdf", 97, r"c:\JLPT\jlpt-exam-prep\audit\pdf_inspect\interior\g1_l3_p97.png")

# Genki 2: Lesson 13 (starts book p. 22, let's find PDF page)
render_page(r"C:\Users\devyk\Downloads\にほんご\Genki Textbook 2 - 3rd Edition.pdf", 30, r"c:\JLPT\jlpt-exam-prep\audit\pdf_inspect\interior\g2_l13_p30.png")
render_page(r"C:\Users\devyk\Downloads\にほんご\Genki Textbook 2 - 3rd Edition.pdf", 31, r"c:\JLPT\jlpt-exam-prep\audit\pdf_inspect\interior\g2_l13_p31.png")

# SKM N3: Chapter 1 (book p. 16, PDF p. 16 or around there)
render_page(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf", 16, r"c:\JLPT\jlpt-exam-prep\audit\pdf_inspect\interior\skm3_c1_p16.png")
render_page(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf", 17, r"c:\JLPT\jlpt-exam-prep\audit\pdf_inspect\interior\skm3_c1_p17.png")

# SKM N2: Chapter 1 (PDF p. 17 or book p. 8)
render_page(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N2\Shin_Kanzen_Masuta_N2-Bunpou.pdf", 17, r"c:\JLPT\jlpt-exam-prep\audit\pdf_inspect\interior\skm2_c1_p17.png")
render_page(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N2\Shin_Kanzen_Masuta_N2-Bunpou.pdf", 18, r"c:\JLPT\jlpt-exam-prep\audit\pdf_inspect\interior\skm2_c1_p18.png")
