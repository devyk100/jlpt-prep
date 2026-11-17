import json

with open("jlpt-exam-prep/src/data/annotations.json", "r", encoding="utf-8") as f:
    annotations = json.load(f)

for k in list(annotations.keys())[:5]:
    print(k, annotations[k])
