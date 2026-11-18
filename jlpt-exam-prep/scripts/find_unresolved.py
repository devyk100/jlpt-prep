import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    ex = json.load(f)

GENERIC_MARKERS = [
    '語用論的制約に反します', '文脈上の時間関係', '文体・語用論', '文脈上の意味論',
    'モダリティ・感情表現の制約に反します', '文の組み立て・構造的呼応に反します',
    '文脈上の文型体系・機能制約に反します', '文体・語用論・結束性において不適切です'
]

unresolved = []
for e in ex:
    if e.get("bookId") == "skm-n2":
        opts = e.get("explanation", {}).get("options", [])
        bad_opts = [o for o in opts if any(p in o.get("reason", "") for p in GENERIC_MARKERS)]
        if bad_opts:
            unresolved.append({
                "id": e["id"],
                "ch": e["chapter"],
                "q": e["question"],
                "options": e["options"],
                "bad_opts": [(o["text"], o.get("reason")) for o in bad_opts]
            })

print(f"Total unresolved exercises: {len(unresolved)}")
with open("jlpt-exam-prep/scripts/unresolved_reasons.json", "w", encoding="utf-8") as out:
    json.dump(unresolved, out, ensure_ascii=False, indent=2)
print("Saved to unresolved_reasons.json")
