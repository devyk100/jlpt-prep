import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

updated_count = 0
for e in exercises:
    if e.get("bookId") == "genki-2":
        e["provenance"] = "original"
        e["sourceEvidence"] = f"Original diagnostic exercise authored to test specified learning objectives of Genki II {e.get('chapter', '')}."
        updated_count += 1

with open("jlpt-exam-prep/src/data/chapterExercises.json", "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print(f"Successfully updated provenance for {updated_count} Genki II exercises in chapterExercises.json.")
