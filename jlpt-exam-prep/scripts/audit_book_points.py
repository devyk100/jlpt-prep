import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    app_points = {p['id']: p for p in json.load(f)}

def audit_book(filename, book_label):
    with open(f"jlpt-exam-prep/audit/{filename}", "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
    
    entries = []
    # format is: id | title | connection
    for line in lines:
        if line.startswith(('NO ', 'PARTICLE ', 'TIME ', 'UNFAVORABLE ', 'DECISION ', 'FORWARD ', 'UNRIVALED ')) or ' | ' not in line:
            continue
        parts = line.split(' | ')
        if len(parts) >= 2 and not line.endswith(('| 0', '| 1', '| 2', '| 3')):
            entries.append((parts[0].strip(), parts[1].strip(), parts[2].strip() if len(parts) > 2 else ''))

    print(f"=== {book_label} ===")
    print(f"Total entries parsed from {filename}: {len(entries)}")
    
    found = 0
    missing = []
    for ident, title, conn in entries:
        if ident in app_points:
            found += 1
        else:
            missing.append((ident, title))
            
    print(f"Mapped to app cards: {found} / {len(entries)}")
    if missing:
        print(f"Missing in app: {len(missing)}")
        for m in missing[:5]:
            print(f"   - {m[0]}: {m[1]}")

audit_book("BOOK_GENKI1_POINTS.txt", "Genki I")
audit_book("BOOK_GENKI2_POINTS.txt", "Genki II")
audit_book("BOOK_SKM_N3_POINTS.txt", "Shin Kanzen Master N3")
audit_book("BOOK_SKM_N2_POINTS.txt", "Shin Kanzen Master N2")
