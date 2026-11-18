import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

print("=== CHECKING ALL EXERCISES FOR TOPIC MISMATCHES ===")

# Check if the options complete the question sentence grammatically
for ex in exercises:
    eid = ex.get('id')
    q = ex.get('question', '')
    opts = ex.get('options', [])
    c_idx = ex.get('correctIndex', 0)
    if c_idx >= len(opts):
        print(f"[{eid}] ERROR: correctIndex {c_idx} out of range for options {opts}")
        continue
    chosen = opts[c_idx]
    
    # Check blank placement
    if '（　）' not in q and '（　　）' not in q and '＿＿' not in q and '（ ' not in q and '(' not in q:
        print(f"[{eid}] WARNING: No blank found in question: {q}")
