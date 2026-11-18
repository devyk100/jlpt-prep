import json

with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

l21_exs = [e for e in exercises if e.get('chapter') == 'Lesson 21']
print(f"Total exercises for Lesson 21: {len(l21_exs)}")
for e in l21_exs:
    print(f"{e.get('id')} | {e.get('grammarPointId')} | {e.get('grammarPointTitle')} | {e.get('question')}")
