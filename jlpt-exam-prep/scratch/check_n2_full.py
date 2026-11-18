import json
import re

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

with open("jlpt-exam-prep/src/data/annotations.json", "r", encoding="utf-8") as f:
    annotations = json.load(f)

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

with open("jlpt-exam-prep/src/data/mugUpTables.json", "r", encoding="utf-8") as f:
    tables = json.load(f)

n2_exercises = [e for e in exercises if e.get("bookId") == "skm-n2"]
n2_points = [p for p in points if p.get("book") == "Shin Kanzen Master N2"]

print(f"Total SKM N2 points: {len(n2_points)}")
print(f"Total SKM N2 exercises: {len(n2_exercises)}")

# Check annotation coverage
missing_tokens = set()
for e in n2_exercises:
    texts = [e.get("question", "")] + e.get("options", [])
    for text in texts:
        parts = re.split(r'([一-龯々〆ヵヶぁ-んァ-ヶー]+)', text)
        for p in parts:
            if re.match(r'^[一-龯々〆ヵヶぁ-んァ-ヶー]+$', p) and p not in annotations:
                missing_tokens.add(p)

print(f"Missing annotation tokens in SKM N2 exercises: {len(missing_tokens)}")
if missing_tokens:
    print(f"Sample missing tokens: {list(missing_tokens)[:20]}")

print("\nSKM N2 Master Tables:")
for k, t in tables.items():
    if "n2" in k.lower():
        print(f"  - {k}: {t.get('title')} (rows: {len(t.get('rows', []))})")
