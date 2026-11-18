import json
import re

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

with open("jlpt-exam-prep/src/data/mugUpTables.json", "r", encoding="utf-8") as f:
    tables = json.load(f)

with open("jlpt-exam-prep/src/data/annotations.json", "r", encoding="utf-8") as f:
    annotations = json.load(f)

n3_points = [p for p in points if p.get("book") == "Shin Kanzen Master N3"]
print(f"Total SKM N3 points: {len(n3_points)}")

chapters = {}
for p in n3_points:
    ch = p.get("chapter", "Unknown")
    chapters.setdefault(ch, []).append(p)

print("\nSKM N3 Chapters & Review Units:")
for ch, pts in sorted(chapters.items(), key=lambda x: x[0]):
    print(f"  {ch}: {len(pts)} points -> {[p['id'] for p in pts]}")

n3_exercises = [e for e in exercises if e.get("bookId") == "skm-n3"]
print(f"\nTotal SKM N3 exercises: {len(n3_exercises)}")
ex_by_ch = {}
for e in n3_exercises:
    ch = e.get("chapter", "Unknown")
    ex_by_ch.setdefault(ch, []).append(e)

for ch, exs in sorted(ex_by_ch.items(), key=lambda x: x[0]):
    provs = {e.get("provenance") for e in exs}
    types = {e.get("type") for e in exs}
    print(f"  {ch}: {len(exs)} exercises, types: {types}, provenances: {provs}")

print("\nSKM N3 Master Tables in mugUpTables:")
for k, t in tables.items():
    if "n3" in k.lower() or "timesequence" in k.lower():
        print(f"  {k}: {t.get('title')} (rows: {len(t.get('rows', []))})")
