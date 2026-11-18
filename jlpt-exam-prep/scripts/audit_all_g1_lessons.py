import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp = json.load(f)

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)

g1_cards = [p for p in sp if p.get('book') == 'Genki I']
g1_exs = [e for e in exs if e.get('bookId') == 'genki-1']

lessons = {}
for p in g1_cards:
    ch = p.get('chapter', 'Unknown')
    lessons.setdefault(ch, {'cards': [], 'exercises': []})
    lessons[ch]['cards'].append(p)

for e in g1_exs:
    ch = e.get('chapter', 'Unknown')
    lessons.setdefault(ch, {'cards': [], 'exercises': []})
    lessons[ch]['exercises'].append(e)

for ch in sorted(lessons.keys(), key=lambda x: int(x.replace('Lesson ', '')) if 'Lesson ' in x else 99):
    c_len = len(lessons[ch]['cards'])
    e_len = len(lessons[ch]['exercises'])
    print(f"{ch}: {c_len} cards, {e_len} exercises")
