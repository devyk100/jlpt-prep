import json

with open('jlpt-exam-prep/scratch/problematic_reasons.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = {e['id']: e for e in json.load(f)}

g1_items = [x for x in items if x['bookId'] == 'genki-1']
print(f'Genki I items: {len(g1_items)}')

for i, it in enumerate(g1_items):
    ex = exercises[it['id']]
    print(f'=== #{i+1}: {it["id"]} ({it["chapter"]}) ===')
    print('Q:', ex['question'])
    print('Trans:', ex['translation'])
    print('Options:', ex['options'])
    print('Correct Index:', ex['correctIndex'])
    opt_info = ex['explanation']['options'][it['optionIndex']]
    print(f'Target Opt [{it["optionIndex"]}]: "{opt_info["text"]}"')
    print(f'Current Reason: "{opt_info["reason"]}"')
    print()
