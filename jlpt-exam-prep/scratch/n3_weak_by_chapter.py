import json
from collections import Counter

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

n3 = [e for e in exercises if e.get('bookId') == 'skm-n3']
weak_by_chapter = Counter()
for e in n3:
    ch = e.get('chapter', 'Unknown')
    for opt in e['explanation']['options']:
        if not opt['isCorrect']:
            r = opt['reason']
            if len(r) < 35 or ('ungrammatical' in r.lower() and len(r) < 70) or '非文' in r:
                weak_by_chapter[ch] += 1

print("Weak distractors by chapter in SKM N3:")
for ch, count in sorted(weak_by_chapter.items()):
    print(f"  {ch}: {count}")
