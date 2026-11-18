import json

with open('jlpt-exam-prep/scratch/problematic_reasons.json', 'r', encoding='utf-8') as f:
    items = json.load(f)
with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = {e['id']: e for e in json.load(f)}

g2_items = [x for x in items if x['bookId'] == 'genki-2']
for i in range(29, 60):
    it = g2_items[i]
    e = exercises[it['id']]
    opt_idx = it.get('optionIndex')
    opt = e['explanation']['options'][opt_idx]
    print(f'{i+1}. {it["id"]} [{e["chapter"]}] Q: {e["question"]} | Opt {opt_idx}: "{opt["text"]}" -> "{opt["reason"]}"')
