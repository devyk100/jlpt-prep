import fitz, json

paths = json.load(open('jlpt-exam-prep/audit/books/paths.json'))

for k, p in paths.items():
    doc = fitz.open(p)
    toc = doc.get_toc()
    print(f"\n=======================================================")
    print(f"PDF [{k}]: {doc.name}")
    print(f"Page count: {len(doc)}, TOC entries: {len(toc)}")
    if toc:
        print("First 15 TOC entries:")
        for lvl, title, page in toc[:15]:
            print(f"  {'  ' * (lvl - 1)}* {title} (p. {page})")
    else:
        print("  (No embedded PDF outline/TOC; image-based or flat PDF)")
    doc.close()
