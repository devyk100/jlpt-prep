import json

pts = json.load(open('jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
books = json.load(open('jlpt-exam-prep/src/data/bookSources.json', encoding='utf-8'))
pts_by_id = {p['id']: p for p in pts}

mapped_ids = set()
for b in books:
    for sec in b['sections']:
        for gid in sec['grammarIds']:
            mapped_ids.add(gid)

print("=== CANONICAL BOOK BREAKDOWN ===")
for b in books:
    b_id = b['id']
    b_name = b['name']
    b_level = b['level']
    total_cards = sum(len(s['grammarIds']) for s in b['sections'])
    total_sentences = sum(len(pts_by_id[gid].get('sentences', [])) for s in b['sections'] for gid in s['grammarIds'] if gid in pts_by_id)
    total_quizzes = sum(len(pts_by_id[gid].get('quiz', [])) for s in b['sections'] for gid in s['grammarIds'] if gid in pts_by_id)
    tables_in_book = sum(1 for s in b['sections'] for gid in s['grammarIds'] if gid in pts_by_id and pts_by_id[gid].get('table'))
    
    print(f"\n[{b_name}] ({b_level})")
    print(f"  Sections / Chapters: {len(b['sections'])}")
    print(f"  Canonical Cards: {total_cards}")
    print(f"  Example Sentences: {total_sentences} (avg {total_sentences/total_cards:.2f}/card)")
    print(f"  Quizzes: {total_quizzes} (avg {total_quizzes/total_cards:.2f}/card)")
    print(f"  In-Lesson Tables: {tables_in_book}")
    
    # Check section distribution
    min_sec = min((len(s['grammarIds']), s['name']) for s in b['sections'])
    max_sec = max((len(s['grammarIds']), s['name']) for s in b['sections'])
    print(f"  Chapter size range: {min_sec[0]} ({min_sec[1]}) to {max_sec[0]} ({max_sec[1]})")

print("\n=== UNMAPPED 59 CARDS BREAKDOWN ===")
unmapped = [p for p in pts if p['id'] not in mapped_ids]
print(f"Total unmapped: {len(unmapped)}")
levels_unmapped = {}
for u in unmapped:
    lvl = u.get('level', 'None')
    levels_unmapped[lvl] = levels_unmapped.get(lvl, 0) + 1
print(f"Levels of unmapped: {levels_unmapped}")

# Check which unmapped cards have 'Synthesis' or 'Decoded' or 'Trio' vs single point duplicates
synthesis_cards = [u for u in unmapped if 'synthesis' in u['title'].lower() or 'decoded' in u['title'].lower() or 'trio' in u['title'].lower() or 'ladder' in u['title'].lower() or 'survival' in u['title'].lower() or 'vs' in u['title'].lower()]
single_duplicates = [u for u in unmapped if u not in synthesis_cards]
print(f"Cross-grammar synthesis / comparison cards: {len(synthesis_cards)}")
print(f"Single-grammar duplicate cards: {len(single_duplicates)}")
for s in synthesis_cards[:5]:
    print(f"  Synthesis: {s['id']} -> {s['title']}")
for d in single_duplicates[:5]:
    print(f"  Single dup: {d['id']} -> {d['title']}")
