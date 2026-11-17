import os
import glob
import re

def analyze_source_files(prefix, name):
    files = sorted(glob.glob(f"jlpt-exam-prep/audit/source-text/{prefix}-*.txt"))
    print(f"\n==========================================")
    print(f"=== {name} ({len(files)} pages) ===")
    
    # Extract headings / grammar points
    headings = []
    for f in files:
        page_name = os.path.basename(f)
        with open(f, 'r', encoding='utf-8') as fp:
            text = fp.read()
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        for l in lines:
            # Check for patterns like "1 X は Y です", "第1課", "Grammar 1", "【1】"
            if re.search(r'^(第\d+課|Lesson\s+\d+|Grammar|\d+\s+[A-Za-z\u3040-\u30ff\u4e00-\u9faf]|【\d+】|\[\d+\])', l):
                headings.append((page_name, l))
    
    print(f"Detected {len(headings)} candidate structural markers:")
    for h in headings[:25]:
        print(f"  [{h[0]}] {h[1]}")
    if len(headings) > 25:
        print(f"  ... and {len(headings) - 25} more")

analyze_source_files("g1", "Genki I")
analyze_source_files("g2", "Genki II")
analyze_source_files("n3", "Shin Kanzen Master N3")
analyze_source_files("n2", "Shin Kanzen Master N2")
