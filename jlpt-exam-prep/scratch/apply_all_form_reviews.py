import json

# Import updates from both scripts
with open('jlpt-exam-prep/scratch/repair_form_reviews.py', 'r', encoding='utf-8') as f:
    code1 = f.read()

with open('jlpt-exam-prep/scratch/append_form_reviews_d_g.py', 'r', encoding='utf-8') as f:
    code2 = f.read()

scope1 = {}
exec(code1, scope1)
updates1 = scope1.get('updates', {})

scope2 = {}
exec(code2, scope2)
updates2 = scope2.get('updates', {})

all_updates = {}
all_updates.update(updates1)
all_updates.update(updates2)

print(f"Total Form Review updates to apply: {len(all_updates)}")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

ex_map = {q['id']: q for q in exercises}

applied = 0
for qid, upd in all_updates.items():
    if qid in ex_map:
        q = ex_map[qid]
        q['context'] = upd['context']
        q['translation'] = upd['translation']
        exp = q.setdefault('explanation', {})
        exp['overall'] = upd['overall']
        exp['options'] = upd['options']
        q['options'] = [o['text'] for o in upd['options']]
        q['correctIndex'] = next(i for i, o in enumerate(upd['options']) if o['isCorrect'])
        applied += 1
    else:
        print(f"Warning: {qid} not found in chapterExercises.json")

print(f"Successfully applied {applied} Form Review updates.")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved chapterExercises.json successfully.")
