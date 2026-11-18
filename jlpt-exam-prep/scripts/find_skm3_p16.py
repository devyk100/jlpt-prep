import fitz

doc = fitz.open(r'C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf')
print("Total pages in SKM N3:", len(doc))
# Let's render PDF p. 30 to 45
for p in range(25, 42):
    pix = doc[p].get_pixmap(dpi=150)
    pix.save(f'c:/JLPT/jlpt-exam-prep/scripts/skm3_pdf_{p+1}.png')
print('Rendered SKM N3 PDF pages 26-42')
