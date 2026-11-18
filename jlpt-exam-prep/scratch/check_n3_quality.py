import json
import re

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

with open("jlpt-exam-prep/src/data/annotations.json", "r", encoding="utf-8") as f:
    annotations = json.load(f)

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    study_points = json.load(f)

pts_map = {p["id"]: p for p in study_points}
n3_exercises = [e for e in exercises if e.get("bookId") == "skm-n3"]

print(f"Total SKM N3 exercises: {len(n3_exercises)}")

# 1. Missing explanations / options / generic reasons
missing_overall = 0
invalid_counts = 0
generic_reasons = []
invalid_gids = []

for e in n3_exercises:
    expl = e.get("explanation", {})
    if not expl or not expl.get("overall"):
        missing_overall += 1
    opts = expl.get("options", [])
    if len(opts) != len(e.get("options", [])):
        invalid_counts += 1
    for opt in opts:
        r = opt.get("reason", "")
        if "option" in r.lower() or "distractor" in r.lower() or len(r) < 10:
            generic_reasons.append((e["id"], r))
    if e.get("grammarPointId") not in pts_map:
        invalid_gids.append((e["id"], e.get("grammarPointId")))

print(f"Missing overall explanations: {missing_overall}")
print(f"Invalid option counts in explanation: {invalid_counts}")
print(f"Generic reasons count: {len(generic_reasons)}")
if generic_reasons:
    print(f"Sample generic reasons: {generic_reasons[:5]}")
print(f"Invalid grammarPointIds: {len(invalid_gids)}")
if invalid_gids:
    print(f"Sample invalid grammarPointIds: {invalid_gids[:5]}")

# 2. Annotation coverage
missing_tokens = set()
for e in n3_exercises:
    texts = [e.get("question", "")] + e.get("options", [])
    for text in texts:
        parts = re.split(r'([一-龯々〆ヵヶぁ-んァ-ヶー]+)', text)
        for p in parts:
            if re.match(r'^[一-龯々〆ヵヶぁ-んァ-ヶー]+$', p) and p not in annotations:
                missing_tokens.add(p)

print(f"Missing annotation tokens in SKM N3: {len(missing_tokens)}")
if missing_tokens:
    print(f"Sample missing tokens: {list(missing_tokens)[:20]}")
