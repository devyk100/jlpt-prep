import fitz, os

base = r"C:\Users\devyk\Downloads\にほんご"
out_dir = r"jlpt-exam-prep\audit\pdf_inspect"

g1_path = os.path.join(base, "Genki (N5)", "Genki Textbook 1 - 3rd Edition.pdf")
doc1 = fitz.open(g1_path)

for pno in range(11, 24):
    page = doc1[pno]
    pix = page.get_pixmap(dpi=150)
    img_path = os.path.join(out_dir, f"g1_page_{pno+1}.png")
    pix.save(img_path)
    print(f"Saved Genki 1 page {pno+1} -> {img_path}")

doc1.close()
