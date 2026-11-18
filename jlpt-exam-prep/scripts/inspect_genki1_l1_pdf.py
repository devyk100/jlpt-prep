import pymupdf

doc = pymupdf.open(r"C:\Users\devyk\Downloads\にほんご\Genki (N5)\Genki Textbook 1 - 3rd Edition.pdf")
print("Total pages in Genki I:", len(doc))

# Search for Lesson 1 grammar section
for pno in range(35, 60):
    txt = doc[pno].get_text()
    if "Lesson 1" in txt or "第1課" in txt or "X は Y です" in txt:
        print(f"--- PDF Page {pno+1} (printed ~{pno-7}) ---")
        lines = [l.strip() for l in txt.split("\n") if l.strip()]
        for l in lines[:15]:
            print(f"  {l}")
