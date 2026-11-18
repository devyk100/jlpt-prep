import json

with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

l19_exs = [e for e in exercises if e.get('chapter') == 'Lesson 19']
print(f"Total exercises for Lesson 19: {len(l19_exs)}")
for e in l19_exs:
    print(f"{e.get('id')} | {e.get('grammarPointId')} | {e.get('grammarPointTitle')} | {e.get('question')}")
