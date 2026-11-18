import json

with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

l22_exs = [e for e in exercises if e.get('chapter') == 'Lesson 22']
print(f"Total exercises for Lesson 22: {len(l22_exs)}")
for e in l22_exs:
    print(f"{e.get('id')} | {e.get('grammarPointId')} | {e.get('grammarPointTitle')} | {e.get('question')}")
