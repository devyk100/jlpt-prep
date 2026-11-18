import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

# Test targeted ambiguous pairs
test_cases = [
    {"name": "末に vs あげく", "tokens": ["末に", "あげく"]},
    {"name": "かねる vs かねない", "tokens": ["かねる", "かねない"]},
    {"name": "くせに vs のに", "tokens": ["くせに", "のに"]},
    {"name": "反面 vs 一方で", "tokens": ["反面", "一方で"]},
    {"name": "わけではない vs わけがない", "tokens": ["わけではない", "わけがない"]},
    {"name": "恐れがある vs かねない", "tokens": ["恐れがある", "かねない"]},
    {"name": "わりには vs にしては", "tokens": ["わりに", "にしては"]},
    {"name": "次第 vs 次第では", "tokens": ["次第", "次第では"]}
]

print("=== VERIFYING AMBIGUOUS DISTRACTOR EXCLUSIVITY ===")

for tc in test_cases:
    print(f"\n--- Testing Distractor Pair: {tc['name']} ---")
    matched_exercises = []
    for ex in exercises:
        opts_text = [o.get('text', '') for o in ex.get('explanation', {}).get('options', [])]
        opts_str = " ".join(opts_text)
        has_all = all(any(t in opt for opt in opts_text) for t in tc['tokens'])
        if has_all:
            matched_exercises.append(ex)
            
    print(f"Exercises containing both tokens as options: {len(matched_exercises)}")
    for ex in matched_exercises[:2]:
        print(f"  [Exercise ID: {ex['id']}]")
        print(f"  Prompt: {ex.get('question')}")
        print(f"  Context: {ex.get('context')}")
        print(f"  Translation: {ex.get('translation')}")
        print(f"  Correct Index: {ex.get('correctIndex')} ({ex['options'][ex.get('correctIndex')]})")
        for o_idx, opt in enumerate(ex.get('explanation', {}).get('options', [])):
            print(f"    Option {o_idx} [{opt.get('text')}]: isCorrect={opt.get('isCorrect')}")
            print(f"      Reason: {opt.get('reason')}")
