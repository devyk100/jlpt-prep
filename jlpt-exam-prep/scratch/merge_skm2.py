import json
import sys
import os

sys.path.append(os.path.abspath('scratch'))
import generate_skm2_exercises as skm2

with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Keep non-SKM-N2
non_skm2 = [x for x in existing if x.get('bookId') != 'skm-n2']
print(f"Non-SKM-N2 exercises: {len(non_skm2)}")

skm2_exercises = skm2.get_skm2_exercises()
print(f"SKM N2 exercises: {len(skm2_exercises)}")

all_exercises = non_skm2 + skm2_exercises
print(f"Total Grand Collection: {len(all_exercises)}")

ids = [x['id'] for x in all_exercises]
assert len(ids) == len(set(ids)), f"Duplicate IDs: {len(ids)} vs {len(set(ids))}"

with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(all_exercises, f, ensure_ascii=False, indent=2)

print("Saved successfully to src/data/chapterExercises.json!")
