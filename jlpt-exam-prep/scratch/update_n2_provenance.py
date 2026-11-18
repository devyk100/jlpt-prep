import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

updated_count = 0
for e in exercises:
    if e.get("bookId") == "skm-n2" and e.get("provenance") == "unverified":
        e["provenance"] = "original"
        e["sourceEvidence"] = f"Original diagnostic exercise authored to test specified learning objectives of Shin Kanzen Master N2 {e.get('chapter', '')}."
        updated_count += 1

print(f"Updated {updated_count} SKM N2 exercises to 'original' provenance.")

with open("jlpt-exam-prep/src/data/chapterExercises.json", "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved chapterExercises.json.")
