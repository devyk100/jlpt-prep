import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp = json.load(f)

l4_cards = [p for p in sp if p.get('book') == 'Genki I' and p.get('chapter') == 'Lesson 4']
print(f"Genki I Lesson 4 Cards count: {len(l4_cards)}")
for c in l4_cards:
    print(f"[{c['id']}] {c['title']} ({len(c.get('sentences', []))} sentences)")
    print(f"   Table: {c.get('table', {}).get('title') if c.get('table') else 'None'}")
    print(f"   Connection: {c.get('connection')}")
    print(f"   Nuance: {c.get('nuance')[:100]}...")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)

l4_exs = [e for e in exs if e.get('bookId') == 'genki-1' and e.get('chapter') == 'Lesson 4']
print(f"\nGenki I Lesson 4 Exercises count: {len(l4_exs)}")
for i, e in enumerate(l4_exs):
    print(f"[{e['id']}] Q: {e['question']} | Ans: {e['options'][e['correctIndex']]} | Context: {e.get('context')}")
