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
        if len(r) < 15 or r in ["【不正解】禁止。", "【不正解】論文調。", "【不正解】比較。"]:
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

print(f"Total short generic items: {len(generic_items)}")
for item in generic_items:
    print(f"[{item['exerciseId']}] ({item['chapter']}) Q: {item['question']}")
    print(f"   Opt {item['optionIndex']}: '{item['optionText']}' (Correct={item['isCorrect']}) -> Reason: '{item['reason']}'")
    print(f"   Overall: {item['overall']}\n")
