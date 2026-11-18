import json
import re

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

n2_exercises = [e for e in exercises if e.get("bookId") == "skm-n2"]
print(f"Total SKM N2 exercises: {len(n2_exercises)}")

short_n2 = []
for e in n2_exercises:
    expl = e.get("explanation", {})
    opts = expl.get("options", [])
    for idx, opt in enumerate(opts):
        r = opt.get("reason", "")
        if len(r) < 20 or "非文" in r or "要素です" in r:
            short_n2.append((e["id"], e["chapter"], opt.get("text", ""), r))

print(f"Total short items in SKM N2: {len(short_n2)}")
if short_n2:
    print(f"Sample short items in N2: {short_n2[:5]}")
