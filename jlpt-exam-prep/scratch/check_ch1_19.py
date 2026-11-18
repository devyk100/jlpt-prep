import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

# Inspect Chapters 1 to 19 of SKM2 Part 1
for ch_idx in range(1, 20):
    ch_name = f"Part 1 · Chapter {ch_idx}"
    ch_exs = [ex for ex in exercises if ex.get('chapter') == ch_name]
    for ex in ch_exs:
        # Check if explanation option 0 text matches correct option text
        exp_opts = ex.get('explanation', {}).get('options', [])
        c_idx = ex.get('correctIndex')
        correct_text = ex['options'][c_idx]
        exp_correct = [o['text'] for o in exp_opts if o.get('isCorrect')]
        if not exp_correct or exp_correct[0] != correct_text:
            print(f"[{ex['id']}] Mismatch in correct text: options[{c_idx}]='{correct_text}' vs exp='{exp_correct}'")
