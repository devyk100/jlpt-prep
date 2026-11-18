import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ch_num in range(1, 27):
    ch_name = f"Part 1 · Chapter {ch_num}"
    ch_exs = [ex for ex in exercises if ex.get('chapter') == ch_name]
    if not ch_exs:
        continue
    # Check first 3 exercises of each chapter
    print(f"\n=== Chapter {ch_num} ({len(ch_exs)} exercises) ===")
    for ex in ch_exs[:2]:
        print(f"  {ex['id']}:")
        print(f"    Q:  {ex['question'][:50]}")
        print(f"    Ctx:{ex.get('context', '')[:50]}")
        print(f"    Tr: {ex.get('translation', '')[:60]}")
