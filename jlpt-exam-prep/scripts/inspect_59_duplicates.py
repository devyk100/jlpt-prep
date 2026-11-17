import json

pts = json.load(open('jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
books = json.load(open('jlpt-exam-prep/src/data/bookSources.json', encoding='utf-8'))

mapped_ids = set()
for b in books:
    for sec in b['sections']:
        for gid in sec['grammarIds']:
            mapped_ids.add(gid)

unmapped = [p for p in pts if p['id'] not in mapped_ids]
print(f"Total unmapped: {len(unmapped)}")

for u in unmapped:
    # See if there is another card with very similar title or grammar
    print(f"{u['id']}: '{u['title']}' | level: {u.get('level')} | tags: {u.get('tags')}")
