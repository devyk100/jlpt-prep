import pymupdf

def dump_toc(pdf_path, name):
    doc = pymupdf.open(pdf_path)
    print(f"================== {name} ==================")
    print(f"Total pages: {len(doc)}")
    
    # Check embedded TOC / bookmarks
    toc = doc.get_toc()
    if toc:
        print(f"Found {len(toc)} bookmark items:")
        for lvl, title, page in toc[:30]:
            print(f"  [{lvl}] {title} (page {page})")
    else:
        print("No embedded bookmarks found. Searching pages 4-15 for 目次 (Table of Contents)...")
        for pno in range(3, 15):
            text = doc[pno].get_text()
            if "目次" in text or "もくじ" in text or "第1課" in text or "第1部" in text or "第１課" in text or "第１部" in text:
                print(f"--- Page {pno+1} ---")
                lines = [line.strip() for line in text.split("\n") if line.strip()]
                for l in lines[:25]:
                    print(f"  {l}")

dump_toc(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N3\Shin_Kanzen_Master_N3-Bunpou.pdf", "SKM N3")
dump_toc(r"C:\Users\devyk\Downloads\にほんご\Shin Kanzen Master N2\Shin_Kanzen_Masuta_N2-Bunpou.pdf", "SKM N2")
