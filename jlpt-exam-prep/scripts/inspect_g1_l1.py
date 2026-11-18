import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp = json.load(f)

g1_l1_cards = [p for p in sp if p.get('book') == 'Genki I' and ('Lesson 1' in p.get('chapter', '') or 'l1' in p.get('id', ''))]
print(f"Genki I Lesson 1 Cards count: {len(g1_l1_cards)}")
for c in g1_l1_cards:
    print(f"[{c['id']}] {c['title']} ({len(c.get('sentences', []))} sentences)")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)

g1_l1_exs = [e for e in exs if e.get('bookId') == 'genki-1' and e.get('chapter') == 'Lesson 1']
print(f"\nGenki I Lesson 1 Exercises count: {len(g1_l1_exs)}")
for e in g1_l1_exs:
    print(f"[{e['id']}] Q: {e['question']} | Correct: {e['options'][e['correctIndex']]} | Context: {e.get('context', 'None')}")
