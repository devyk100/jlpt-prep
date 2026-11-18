import json
import re

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

with open("jlpt-exam-prep/src/data/annotations.json", "r", encoding="utf-8") as f:
    annotations = json.load(f)

g2_points = [p for p in points if p.get("book") == "Genki II"]
g2_exercises = [e for e in exercises if e.get("bookId") == "genki-2"]

print("=== CHECKING GENKI II STUDY POINTS TABLE LINKS ===")
for p in g2_points:
    tags = p.get("tags", [])
    matrix_tags = [t for t in tags if "matrix:" in t]
    print(f"Point {p['id']} ({p['chapter']}): matrix tags = {matrix_tags}")

print("\n=== CHECKING GENKI II EXERCISES FEEDBACK QUALITY ===")
generic_count = 0
missing_explanation = 0
for e in g2_exercises:
    expl = e.get("explanation", {})
    if not expl or not expl.get("overall"):
        print(f"Exercise {e['id']} missing overall explanation!")
        missing_explanation += 1
    options = expl.get("options", [])
    if len(options) != len(e.get("options", [])):
        print(f"Exercise {e['id']} option count mismatch: {len(options)} vs {len(e.get('options', []))}")
    for opt in options:
        r = opt.get("reason", "")
        if "option" in r.lower() or "distractor" in r.lower() or len(r) < 10:
            generic_count += 1
            print(f"  Generic reason in {e['id']}: {r}")

print(f"Missing explanations: {missing_explanation}, Generic reasons: {generic_count}")

print("\n=== CHECKING ANNOTATION COVERAGE FOR GENKI II EXERCISES ===")
missing_spans = set()
for e in g2_exercises:
    # check question
    q = e.get("question", "")
    for span in re.findall(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff々〆ヵヶー]+', q):
        if span not in annotations:
            missing_spans.add(span)
    # check options
    for opt in e.get("options", []):
        for span in re.findall(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff々〆ヵヶー]+', opt):
            if span not in annotations:
                missing_spans.add(span)

print(f"Total missing annotation spans in Genki II exercises: {len(missing_spans)}")
if missing_spans:
    print(f"Sample missing: {list(missing_spans)[:20]}")
