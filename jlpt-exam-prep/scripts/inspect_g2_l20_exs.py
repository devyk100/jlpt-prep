import json

with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

l20_exs = [e for e in exercises if e.get('chapter') == 'Lesson 20']
print(f"Total exercises for Lesson 20: {len(l20_exs)}")
for e in l20_exs:
    print(f"{e.get('id')} | {e.get('grammarPointId')} | {e.get('grammarPointTitle')} | {e.get('question')}")
