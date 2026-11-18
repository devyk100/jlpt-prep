import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

n3_exercises = [e for e in exercises if e.get("bookId") == "skm-n3"]

generic_items = []
for e in n3_exercises:
    expl = e.get("explanation", {})
    opts = expl.get("options", [])
    for idx, opt in enumerate(opts):
        r = opt.get("reason", "")
        # Check if too short (< 15 chars), or contains placeholder/truncated tags like 【不正解】 without full sentence context
        if len(r) < 20 or "【不正解】" in r:
            generic_items.append({
                "exerciseId": e["id"],
                "chapter": e["chapter"],
                "question": e["question"],
                "optionIndex": idx,
                "optionText": opt.get("text", e["options"][idx] if idx < len(e["options"]) else ""),
                "isCorrect": opt.get("isCorrect"),
                "reason": r,
                "overall": expl.get("overall")
            })

print(f"Total items needing feedback expansion in SKM N3: {len(generic_items)}")
for item in generic_items[:15]:
    print(f"[{item['exerciseId']}] Opt: {item['optionText']} (Correct: {item['isCorrect']}) -> {item['reason']}")
