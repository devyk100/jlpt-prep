import json

with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

skm3_exs = [e for e in exercises if e.get('bookId') == 'skm-n3']
print(f"Total exercises for skm-n3: {len(skm3_exs)}")

ch_map = {}
for e in skm3_exs:
    ch = e.get('chapter', 'Unknown')
    ch_map[ch] = ch_map.get(ch, 0) + 1

for ch, count in sorted(ch_map.items()):
    print(f"  {ch}: {count} exercises")
