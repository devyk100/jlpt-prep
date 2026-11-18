import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    exercises = json.load(f)

# Inspect how many exercises have specific sourceEvidence vs generic block evidence
specific_count = 0
generic_count = 0

for ex in exercises:
    evid = ex.get("sourceEvidence", "")
    # Check if evid contains a specific page range or specific drill/item
    if "pp. " in evid and ("–" in evid or "-" in evid) and "Practice Drills" in evid:
        generic_count += 1
    else:
        specific_count += 1

print(f"Total: {len(exercises)} | Generic block evidence: {generic_count} | Specific: {specific_count}")
