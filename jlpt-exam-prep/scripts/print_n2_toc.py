import fitz, json

paths = json.load(open('jlpt-exam-prep/audit/books/paths.json'))
doc = fitz.open(paths['n2'])
toc = doc.get_toc()
print(f"Total entries in N2 PDF: {len(toc)}")
for lvl, title, page in toc:
    print(f"  p.{page}: {title}")
doc.close()
