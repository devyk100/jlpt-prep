import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
exs = json.load(open(ROOT / "src/data/chapterExercises.json", encoding="utf-8"))
p2 = [e for e in exs if e.get("bookId") == "skm-n3" and "Part 2" in e.get("chapter", "")]

print(f"Total SKM N3 Part 2 exercises: {len(p2)}")
for e in p2[:6]:
    print("----------------------------------------------------------------")
    print(f"ID: {e['id']} | Type: {e['type']}")
    print(f"Q: {e['question']}")
    print(f"Options: {e['options']} | Correct: {e['options'][e['correctIndex']]}")
    print(f"Translation: {e['translation']}")
    print("Option explanations:")
    for opt in e.get("explanation", {}).get("options", []):
        print(f"  * {opt['text']} (isCorrect={opt['isCorrect']}): {opt['reason']}")
