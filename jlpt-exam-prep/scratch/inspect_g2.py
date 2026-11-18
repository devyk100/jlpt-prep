import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

with open("jlpt-exam-prep/src/data/mugUpTables.json", "r", encoding="utf-8") as f:
    tables = json.load(f)

with open("jlpt-exam-prep/src/data/annotations.json", "r", encoding="utf-8") as f:
    annotations = json.load(f)

g2_points = [p for p in points if p.get("book") == "Genki II"]
print(f"Total Genki II points: {len(g2_points)}")

lessons = {}
for p in g2_points:
    ch = p.get("chapter", "Unknown")
    lessons.setdefault(ch, []).append(p)

for ch in sorted(lessons.keys(), key=lambda x: int(x.replace("Lesson ", "")) if "Lesson " in x else 99):
    pts = lessons[ch]
    print(f"\n{ch}: {len(pts)} points")
    for p in pts:
        print(f"  - {p['id']}: {p['title']} (sentences: {len(p.get('sentences', []))})")

g2_exercises = [e for e in exercises if e.get("bookId") == "genki-2"]
print(f"\nTotal Genki II exercises: {len(g2_exercises)}")
ex_by_ch = {}
for e in g2_exercises:
    ch = e.get("chapter", "Unknown")
    ex_by_ch.setdefault(ch, []).append(e)

for ch in sorted(ex_by_ch.keys(), key=lambda x: int(x.replace("Lesson ", "")) if "Lesson " in x else 99):
    exs = ex_by_ch[ch]
    provs = {e.get("provenance") for e in exs}
    print(f"{ch}: {len(exs)} exercises, provenances: {provs}")

print("\nTables relevant to Genki II:")
g2_table_keys = [k for k in tables.keys() if "genki2" in k or k in ['givingReceivingMatrix', 'voiceMatrix', 'keigoMatrix', 'conditionalsMatrix']]
for k in g2_table_keys:
    t = tables[k]
    print(f"  - {k}: {t.get('title')} (headers: {t.get('headers')}, rows: {len(t.get('rows', []))})")
