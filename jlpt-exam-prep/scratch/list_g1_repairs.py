import json

with open('jlpt-exam-prep/scratch/problematic_reasons.json', 'r', encoding='utf-8') as f:
    items = json.load(f)
with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = {e['id']: e for e in json.load(f)}

g1_items = [x for x in items if x['bookId'] == 'genki-1']
for i, it in enumerate(g1_items):
    e = exercises[it['id']]
    opt = e['explanation']['options'][it['optionIndex']]
    print(f"{i+1}. {it['id']} [{e['chapter']}] Q: {e['question']} | Opt {it['optionIndex']}: '{opt['text']}'")
    print(f"   Current: {opt['reason']}")
