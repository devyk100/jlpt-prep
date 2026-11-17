import os, glob, re

source_dir = 'jlpt-exam-prep/audit/source-text'

def audit_book(prefix, name):
    files = sorted(glob.glob(os.path.join(source_dir, f'{prefix}-p*.txt')))
    print(f"=== {name} ({len(files)} pages) ===")
    
    # Extract lines that look like section titles, grammar numbered headings, or major patterns
    headings = []
    for f in files:
        page_num = os.path.basename(f).replace(f'{prefix}-p', '').replace('.txt', '')
        with open(f, encoding='utf-8', errors='ignore') as fp:
            lines = [l.strip() for l in fp if l.strip()]
        for l in lines:
            # Match patterns like:
            # Genki: "1 X は Y です", "2 質問の「か」", "Lesson 1", "第 1 課"
            # SKM: "1 〜うちに", "第1章", "1課", "■", "【", "〜"
            if re.search(r'^(第\s*\d+\s*[課章]|Lesson\s*\d+|\d+\s+[X〜A-Za-z\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]+|[1-9]\s+[A-Z\u3040-\u309F\u4E00-\u9FAF])', l):
                if len(l) < 50:
                    headings.append((page_num, l))
            elif '〜' in l and ('Verb' in l or 'Noun' in l or '意味' in l or '接続' in l or '【' in l):
                if len(l) < 60:
                    headings.append((page_num, l))
    
    print(f"Detected potential grammar pattern headers in source text: {len(headings)}")
    for p, h in headings[:25]:
        print(f"  p.{p}: {h}")
    return headings

g1_heads = audit_book('g1', 'Genki I')
g2_heads = audit_book('g2', 'Genki II')
n3_heads = audit_book('n3', 'Shin Kanzen Master N3')
n2_heads = audit_book('n2', 'Shin Kanzen Master N2')
