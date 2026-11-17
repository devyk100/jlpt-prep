import fitz, os

base = r"C:\Users\devyk\Downloads\にほんご"
books = {
    "g1": os.path.join(base, "Genki (N5)", "Genki Textbook 1 - 3rd Edition.pdf"),
    "g2": os.path.join(base, "Genki Textbook 2 - 3rd Edition.pdf"),
    "n3": os.path.join(base, "Shin Kanzen Master N3", "Shin_Kanzen_Master_N3-Bunpou.pdf"),
    "n2": os.path.join(base, "Shin Kanzen Master N2", "Shin_Kanzen_Masuta_N2-Bunpou.pdf")
}

for k, path in books.items():
    print(f"\n==========================================")
    print(f"Checking {k}: {path}")
    doc = fitz.open(path)
    print(f"Total pages: {len(doc)}")
    
    # Scan pages 1 to 20 for text
    found_text_pages = []
    for pno in range(min(25, len(doc))):
        page = doc[pno]
        txt = page.get_text()
        if len(txt.strip()) > 30:
            found_text_pages.append(pno + 1)
            # Check if it mentions Contents / 目次
            if any(w in txt.lower() for w in ['content', '目次', 'lesson', '第1課', '第１課', '第1章', '第１章']):
                print(f"  [TOC / Heading Found on Page {pno + 1}]:")
                lines = [l.strip() for l in txt.split('\n') if l.strip()]
                for l in lines[:15]:
                    print(f"    {l}")
    if not found_text_pages:
        print("  NO embedded text found in first 25 pages (scanned image PDF).")
    else:
        print(f"  Pages with text: {len(found_text_pages)} pages: {found_text_pages[:10]}")
    doc.close()
