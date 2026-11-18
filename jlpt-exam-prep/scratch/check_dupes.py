"""Check the duplicate questions."""
import json

ROOT = r"C:\JLPT\jlpt-exam-prep"
ex = json.load(open(f"{ROOT}/src/data/chapterExercises.json", "r", encoding="utf-8"))

dupes = {}
for e in ex:
    q = e["question"]
    dupes.setdefault(q, []).append(e["id"])

for q, ids in dupes.items():
    if len(ids) > 1:
        print(f"Duplicate question: {q[:80]}")
        for eid in ids:
            e = next(x for x in ex if x["id"] == eid)
            print(f"  {eid} (ch: {e['chapter']}, correct: {e['options'][e['correctIndex']]})")
        print()
