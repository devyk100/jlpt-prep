import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"

exercises = json.load(open(EXERCISES_PATH, encoding="utf-8"))

CHAPTER_PAGES = {
    "Part 1 · Chapter 1": "pp. 16–17",
    "Part 1 · Chapter 2": "pp. 18–21",
    "Part 1 · Chapter 3": "pp. 22–23",
    "Part 1 · Chapter 4": "pp. 24–25",
    "Part 1 · Chapter 5": "pp. 26–27",
    "Part 1 · Form review E": "pp. 74–77",
    "Part 1 · Form review F": "pp. 78–79",
    "Part 1 · Form review G": "pp. 80–83",
    "Part 1 · Form review H": "pp. 84–87",
    "Part 1 · Form review I": "pp. 88–91",
    "Part 1 · Form review J": "pp. 92–95",
}

tagged = 0
for e in exercises:
    if e.get("bookId") == "skm-n3" and e.get("chapter") in CHAPTER_PAGES:
        ch = e.get("chapter")
        e["provenance"] = "source-derived"
        e["sourceEvidence"] = f"Shin Kanzen Master N3 Bunpou, {ch}, Practice Drills, {CHAPTER_PAGES[ch]}"
        tagged += 1

print(f"Tagged {tagged} SKM N3 Part 1 (Ch 1-5, FR E-J) exercises.")

with open(EXERCISES_PATH, "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved successfully.")
