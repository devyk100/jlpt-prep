import json

with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c2_exs = [e for e in exercises if e.get('chapter') == 'Part 1 · Chapter 2' and e.get('bookId') == 'skm-n3']
print(f"Total exercises for SKM N3 Chapter 2: {len(c2_exs)}")
for e in c2_exs:
    print(e.get('id'), '|', e.get('grammarPointId'), '|', e.get('question'))
