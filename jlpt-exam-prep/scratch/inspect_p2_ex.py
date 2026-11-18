import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

p2_ex = [e for e in exercises if e.get('bookId') == 'skm-n3' and e.get('chapter') == 'Part 2 · Chapter 1'][:3]
for e in p2_ex:
    print(f"=== {e['id']} ===")
    print("Q:", e['question'])
    print("ScrambleOrder:", e.get('scrambleOrder'))
    print("Reconstructed:", e.get('reconstructedSentence'))
    for opt in e['explanation']['options']:
        print(f"  Opt [{opt['text']}] (isCorrect: {opt['isCorrect']}): {opt['reason']}")
    print()
