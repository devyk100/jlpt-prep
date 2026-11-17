import json
import sys
import os

sys.path.append(os.path.abspath('scratch'))
import generate_skm3_full as skm3

with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Keep all non-SKM-N3 exercises
non_skm3 = [x for x in existing if x.get('bookId') != 'skm-n3']
print(f"Non-SKM-N3 exercises (Genki I + II): {len(non_skm3)}")

skm3_exercises = skm3.get_skm3_all_exercises()
print(f"SKM N3 exercises: {len(skm3_exercises)}")

all_exercises = non_skm3 + skm3_exercises
print(f"Total exercises: {len(all_exercises)}")

# Check duplicate IDs
ids = [x['id'] for x in all_exercises]
assert len(ids) == len(set(ids)), f"Duplicate IDs: {len(ids)} vs {len(set(ids))}"

with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(all_exercises, f, ensure_ascii=False, indent=2)

print("Saved successfully to src/data/chapterExercises.json!")
