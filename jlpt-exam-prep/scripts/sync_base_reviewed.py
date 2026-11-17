import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    study = json.load(f)

with open("jlpt-exam-prep/content/base-reviewed.json", "w", encoding="utf-8") as f:
    json.dump(study, f, ensure_ascii=False, indent=2)

print(f"Synced content/base-reviewed.json with all {len(study)} cards from studyPoints.json!")
