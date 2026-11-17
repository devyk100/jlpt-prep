import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

with open("jlpt-exam-prep/src/data/bookSources.json", "r", encoding="utf-8") as f:
    books = json.load(f)

app_points_by_id = {p['id']: p for p in points}

print("=== SIDE-BY-SIDE AUDIT REPORT GENERATOR ===")

for b in books:
    b_id = b['id']
    b_name = b['name']
    b_level = b['level']
    print(f"\n=======================================================")
    print(f"BOOK: {b_name} ({b_level})")
    print(f"Total sections in app bookSources: {len(b['sections'])}")
    
    total_cards = 0
    total_sentences = 0
    total_quizzes = 0
    
    for sec_idx, sec in enumerate(b['sections']):
        sec_name = sec['name']
        grammar_ids = sec['grammarIds']
        total_cards += len(grammar_ids)
        
        # Check details of cards in this section
        sec_sentences = 0
        sec_quizzes = 0
        has_table = False
        lumped_cards = []
        
        for gid in grammar_ids:
            pt = app_points_by_id.get(gid)
            if not pt:
                print(f"  [ERROR] Missing card in studyPoints: {gid} in section {sec_name}")
                continue
            s_count = len(pt.get('sentences', []))
            q_count = len(pt.get('quiz', []))
            sec_sentences += s_count
            sec_quizzes += q_count
            total_sentences += s_count
            total_quizzes += q_count
            if 'table' in pt:
                has_table = True
            # Check if title suggests multiple lumped patterns (e.g. contains '・', 'vs', '/')
            if '・' in pt['title'] or ' vs ' in pt['title']:
                lumped_cards.append((pt['id'], pt['title'], s_count))
        
        # Summarize section
        # print(f"  Section {sec_idx+1}: {sec_name} | {len(grammar_ids)} cards, {sec_sentences} ex, {sec_quizzes} qz {'[TABLE]' if has_table else ''}")
        if lumped_cards:
            pass # print(f"     Lumped multi-pattern cards: {len(lumped_cards)}")

    print(f"Summary for {b_name}: {total_cards} cards, {total_sentences} examples, {total_quizzes} quiz questions.")
