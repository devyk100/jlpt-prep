import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

p3_exercises = [ex for ex in exercises if 'p3' in ex.get('id', '') or 'Part 3' in ex.get('chapter', '')]
print(f"Total Part 3 discourse grammar exercises: {len(p3_exercises)}")

# Inspect by chapter
by_ch = {}
for ex in p3_exercises:
    ch = ex.get('chapter', 'Unknown')
    by_ch.setdefault(ch, []).append(ex)

for ch, exs in by_ch.items():
    print(f"\n--- Chapter: {ch} ({len(exs)} exercises) ---")
    # Sample first exercise
    first = exs[0]
    print(f"  Sample ID: {first['id']}")
    print(f"  Prompt:    {first.get('question')[:60]}...")
    print(f"  Context:   {first.get('context')[:60]}...")
    print(f"  Key:       {first['options'][first['correctIndex']]}")
    print(f"  Exp:       {first['explanation']['overall'][:80]}...")
