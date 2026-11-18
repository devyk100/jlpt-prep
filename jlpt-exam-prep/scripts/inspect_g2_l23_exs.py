import json

with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

l23_exs = [e for e in exercises if e.get('chapter') == 'Lesson 23']
print(f"Total exercises for Lesson 23: {len(l23_exs)}")
for e in l23_exs:
    print(f"{e.get('id')} | {e.get('grammarPointId')} | {e.get('grammarPointTitle')} | {e.get('question')}")
