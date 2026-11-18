import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp = json.load(f)

l6_cards = [p for p in sp if p.get('book') == 'Genki I' and p.get('chapter') == 'Lesson 6']
print(f"Genki I Lesson 6 Cards count: {len(l6_cards)}")
for c in l6_cards:
    print(f"[{c['id']}] {c['title']} ({len(c.get('sentences', []))} sentences)")
    print(f"   Table: {c.get('table', {}).get('title') if c.get('table') else 'None'}")
    print(f"   Connection: {c.get('connection')}")
    print(f"   Nuance: {c.get('nuance')[:100]}...")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)

l6_exs = [e for e in exs if e.get('bookId') == 'genki-1' and e.get('chapter') == 'Lesson 6']
print(f"\nGenki I Lesson 6 Exercises count: {len(l6_exs)}")
for i, e in enumerate(l6_exs):
    print(f"[{e['id']}] Q: {e['question']} | Ans: {e['options'][e['correctIndex']]} | Context: {e.get('context')}")
