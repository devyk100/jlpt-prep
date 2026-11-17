import json
import sys
import os

sys.path.append(os.path.abspath('scratch'))

import generate_genki2_exercises as g2_part1
import generate_all_genki2 as g2_part2
import append_g2_part2 as g2_part3
import append_g2_part3 as g2_part4
import append_g2_part4 as g2_part5

# Load existing exercises
with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Keep all Genki I exercises (Lessons 1 to 12)
genki1 = [x for x in existing if x.get('bookId') == 'genki-1']
print(f"Genki I exercises: {len(genki1)}")

# Collect all Genki II exercises
genki2_13_14 = g2_part1.get_genki2_exercises() # L13, L14 (20 Qs)
genki2_15_16 = g2_part2.get_all_genki2_exercises()[20:] # L15, L16 (20 Qs)
genki2_17_18 = g2_part3.get_genki2_l17_to_l23() # L17, L18 (20 Qs)
genki2_19_20 = g2_part4.get_genki2_l19_to_l23() # L19, L20 (20 Qs)
genki2_21_23 = g2_part5.get_genki2_l21_to_l23() # L21, L22, L23 (30 Qs)

genki2_all = genki2_13_14 + genki2_15_16 + genki2_17_18 + genki2_19_20 + genki2_21_23
print(f"Genki II exercises: {len(genki2_all)}")

all_exercises = genki1 + genki2_all
print(f"Total Combined Exercises: {len(all_exercises)}")

# Verify uniqueness of IDs
ids = [x['id'] for x in all_exercises]
assert len(ids) == len(set(ids)), f"Duplicate IDs found! Total: {len(ids)}, Unique: {len(set(ids))}"

with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(all_exercises, f, ensure_ascii=False, indent=2)

print("Successfully written to src/data/chapterExercises.json!")
