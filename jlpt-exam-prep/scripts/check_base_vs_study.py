import json

with open("jlpt-exam-prep/content/base-reviewed.json", "r", encoding="utf-8") as f:
    base = json.load(f)

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    study = json.load(f)

print(f"base-reviewed.json: {len(base)} cards")
print(f"studyPoints.json: {len(study)} cards")

base_ids = {b['id'] for b in base}
study_ids = {s['id'] for s in study}
print("In study but not base:", len(study_ids - base_ids), study_ids - base_ids)
print("In base but not study:", len(base_ids - study_ids), base_ids - study_ids)
