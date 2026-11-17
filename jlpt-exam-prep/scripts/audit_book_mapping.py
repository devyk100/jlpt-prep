import json

pts = json.load(open('jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
books = json.load(open('jlpt-exam-prep/src/data/bookSources.json', encoding='utf-8'))

# Build a mapping from card ID to (bookName, chapterName) from bookSources.json
sources_map = {}
for b in books:
    b_name = b['name']
    for sec in b['sections']:
        sec_name = sec['name']
        for gid in sec['grammarIds']:
            sources_map[gid] = (b_name, sec_name)

print("Total cards mapped in bookSources.json:", len(sources_map))

unmapped = [p['id'] for p in pts if p['id'] not in sources_map]
print("Cards in studyPoints NOT in bookSources.json:", len(unmapped))
if unmapped:
    print("Sample unmapped:", unmapped[:10])

# Now check which cards have missing or mismatched book/chapter in studyPoints
mismatches = 0
for p in pts:
    pid = p['id']
    if pid in sources_map:
        src_b, src_c = sources_map[pid]
        if not p.get('book') or not p.get('chapter'):
            mismatches += 1
            # print(f"Card {pid} missing book/chap in studyPoints, but in bookSources as {src_b} / {src_c}")

print(f"Cards mapped in bookSources that were missing book/chapter on card itself: {mismatches}")
