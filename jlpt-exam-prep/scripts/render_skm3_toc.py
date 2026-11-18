import fitz

doc = fitz.open(r'C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf')
# The Table of Contents is typically in the first 8-12 pages
for p in range(2, 12):
    pix = doc[p].get_pixmap(dpi=150)
    pix.save(f'c:/JLPT/jlpt-exam-prep/scripts/skm3_p{p+1}.png')
print('Rendered SKM N3 pages 3-12')
