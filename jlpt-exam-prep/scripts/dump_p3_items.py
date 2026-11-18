import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    ex = json.load(f)

for c in range(1, 13):
    ch_name = f"Part 3 · Chapter {c}"
    items = [e for e in ex if e.get("bookId") == "skm-n2" and e.get("chapter") == ch_name]
    print(f"\n# === {ch_name} ({len(items)} items) ===")
    for e in items:
        corr = e["options"][e["correctIndex"]]
        print(f"'{e['id']}': {{'q': {repr(e['question'])}, 'corr': {repr(corr)}, 'opts': {repr(e['options'])}}},")
