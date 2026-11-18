import json

with open('jlpt-exam-prep/scratch/problematic_reasons.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = {e['id']: e for e in json.load(f)}

g2_items = [x for x in items if x['bookId'] == 'genki-2']
print(f'Genki II items: {len(g2_items)}')

for i, it in enumerate(g2_items):
    e = exercises[it['id']]
    # check if optionIndex is valid
    opt_idx = it.get('optionIndex')
    if opt_idx is not None and opt_idx < len(e['explanation']['options']):
        opt = e['explanation']['options'][opt_idx]
        print(f"{i+1}. {it['id']} [{e['chapter']}] Q: {e['question']} | Opt {opt_idx}: '{opt['text']}'")
        print(f"   Current: {opt['reason']}")
    else:
        print(f"{i+1}. {it['id']} [{e['chapter']}] - invalid opt_idx {opt_idx}")
