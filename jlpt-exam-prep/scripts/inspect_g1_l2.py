import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp = json.load(f)

l2_cards = [p for p in sp if p.get('book') == 'Genki I' and p.get('chapter') == 'Lesson 2']
print(f"Genki I Lesson 2 Cards count: {len(l2_cards)}")
for c in l2_cards:
    print(f"[{c['id']}] {c['title']} ({len(c.get('sentences', []))} sentences)")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)

l2_exs = [e for e in exs if e.get('bookId') == 'genki-1' and e.get('chapter') == 'Lesson 2']
print(f"\nGenki I Lesson 2 Exercises count: {len(l2_exs)}")
for e in l2_exs:
    print(f"[{e['id']}] Q: {e['question']} | Correct: {e['options'][e['correctIndex']]} | Context: {e.get('context', 'None')}")
