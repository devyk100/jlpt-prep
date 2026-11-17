import json

with open("jlpt-exam-prep/content/reading-overrides.json", "r", encoding="utf-8") as f:
    overrides = json.load(f)

overrides["枚"] = ["まい", "counter for flat objects (sheets, stamps, tickets)"]

with open("jlpt-exam-prep/content/reading-overrides.json", "w", encoding="utf-8") as f:
    json.dump(overrides, f, ensure_ascii=False, indent=2)

print("Added 枚 to reading-overrides.json!")
