import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exs = json.load(f)

l1_exs = [e for e in exs if e.get('bookId') == 'genki-1' and e.get('chapter') == 'Lesson 1']

print(f"Total L1 exercises: {len(l1_exs)}\n")
for i, e in enumerate(l1_exs):
    print(f"--- Exercise {i+1}: {e['id']} ---")
    print(f"Context: {e.get('context')}")
    print(f"Question: {e.get('question')}")
    print(f"Translation: {e.get('translation')}")
    print(f"Options: {e.get('options')}")
    print(f"Correct: [{e.get('correctIndex')}] {e['options'][e['correctIndex']]}")
    print(f"Grammar Point ID: {e.get('grammarPointId')}")
    print(f"Provenance: {e.get('provenance')} | Evidence: {e.get('sourceEvidence')}")
    print("Explanations:")
    exp = e.get('explanation', {})
    if isinstance(exp, dict):
        print(f"  Overall: {exp.get('overall')}")
        for opt_exp in exp.get('options', []):
            print(f"    - {opt_exp.get('text')} (isCorrect: {opt_exp.get('isCorrect')}): {opt_exp.get('reason')}")
    else:
        print(f"  String explanation: {exp}")
    print()
