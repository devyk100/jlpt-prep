import pymupdf

doc = pymupdf.open(r"C:\Users\devyk\Downloads\にほんご\Genki (N5)\Genki Textbook 1 - 3rd Edition.pdf")
print("Total pages:", len(doc))

# Let's check PDF pages 44 to 55 (0-indexed: 43 to 54)
for p in range(43, 55):
    pix = doc[p].get_pixmap(dpi=150)
    print(f"PDF page {p+1} (printed ~{p-7}): {pix.width}x{pix.height}")
