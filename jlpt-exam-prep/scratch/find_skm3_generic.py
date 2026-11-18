import json
import re

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

n3 = [e for e in exercises if e.get('bookId') == 'skm-n3']

generic_items = []
for e in n3:
    for idx, opt in enumerate(e['explanation']['options']):
        if not opt['isCorrect']:
            r = opt['reason']
            # If starts with "Incorrect." and total length < 55 or has "ungrammatical" or "非文"
            if r.startswith("Incorrect.") and (len(r) < 55 or 'ungrammatical' in r.lower()):
                generic_items.append({
                    'id': e['id'],
                    'chapter': e.get('chapter'),
                    'question': e['question'],
                    'opt_idx': idx,
                    'text': opt['text'],
                    'reason': r
                })

print(f"Total generic English distractor reasons in SKM N3: {len(generic_items)}")
from collections import Counter
print(Counter(x['chapter'] for x in generic_items))
for x in generic_items[:15]:
    print(f"[{x['id']} - {x['chapter']}] Opt '{x['text']}': {x['reason']}")
