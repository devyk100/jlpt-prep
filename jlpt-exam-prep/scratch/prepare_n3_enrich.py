import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

n3_exercises = [e for e in exercises if e.get("bookId") == "skm-n3"]

records = []
for e in n3_exercises:
    expl = e.get("explanation", {})
    opts = expl.get("options", [])
    has_short = False
    for idx, opt in enumerate(opts):
        r = opt.get("reason", "")
        if len(r) < 22 or "非文" in r or "要素です" in r:
            has_short = True
    if has_short:
        records.append({
            "id": e["id"],
            "chapter": e["chapter"],
            "question": e["question"],
            "translation": e.get("translation", ""),
            "options": e.get("options", []),
            "correctIndex": e.get("correctIndex"),
            "overall": expl.get("overall", ""),
            "expl_options": opts
        })

print(f"Total exercises needing reason enrichment: {len(records)}")
with open("jlpt-exam-prep/scratch/n3_to_enrich.json", "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)
