import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    ex = json.load(f)

p3b = [e for e in ex if e.get("bookId") == "skm-n2" and "Part 3" in e.get("chapter", "") and any(f"Chapter {i}" in e.get("chapter", "") for i in range(7, 13))]

print(f"Total P3B items: {len(p3b)}")
with open("jlpt-exam-prep/scripts/p3b_raw.json", "w", encoding="utf-8") as out:
    json.dump([{"id": e["id"], "ch": e["chapter"], "q": e["question"], "opts": e["options"], "corr": e["options"][e["correctIndex"]]} for e in p3b], out, ensure_ascii=False, indent=2)
print("Dumped to p3b_raw.json")
