import json

sp = json.load(open(r"C:\JLPT\jlpt-exam-prep\src\data\studyPoints.json", "r", encoding="utf-8"))

targets = ["skm2-p2-kai-ga-aru", "skm2-p2-wo-oite", "skm2-p2-majiki", "skm2-p2-bekarazu"]
for c in sp:
    if c["id"] in targets:
        print("ID:", c["id"])
        print("  Title:", c["title"])
        print("  Meaning:", c["meaning"][:120])
        print("  Nuance:", c["nuance"][:250])
        print("  Sentences:", len(c.get("sentences", [])))
        print()
