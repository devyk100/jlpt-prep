import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

n3_exercises = [e for e in exercises if e.get("bookId") == "skm-n3"]

short_items = []
for e in n3_exercises:
    expl = e.get("explanation", {})
    opts = expl.get("options", [])
    for idx, opt in enumerate(opts):
        r = opt.get("reason", "")
        if len(r) < 20 or r in ["【不正解】非文です。", "【不正解】禁止。", "【不正解】論文調。", "【不正解】比較。"] or "番目の要素です" in r:
            short_items.append({
                "exerciseId": e["id"],
                "chapter": e["chapter"],
                "type": e.get("type", "multiple-choice"),
                "question": e["question"],
                "optionIndex": idx,
                "optionText": opt.get("text", e["options"][idx] if idx < len(e["options"]) else ""),
                "isCorrect": opt.get("isCorrect"),
                "reason": r,
                "overall": expl.get("overall")
            })

print(f"Total short items to enrich in SKM N3: {len(short_items)}")

# Count by chapter
by_ch = {}
for item in short_items:
    by_ch[item["chapter"]] = by_ch.get(item["chapter"], 0) + 1

for ch, cnt in sorted(by_ch.items()):
    print(f"  {ch}: {cnt} items")
