import json

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

problematic = []
for e in exercises:
    expl = e.get("explanation", {})
    opts = expl.get("options", [])
    for idx, opt in enumerate(opts):
        r = opt.get("reason", "")
        # Check for ungrammatical / generic tags
        r_clean = r.strip()
        is_bad = False
        reasons_found = []
        
        if any(w in r.lower() for w in ["ungrammatical", "pseudo-construction", "hybrid construction", "hybrid formation", "hybrid past", "non-standard"]):
            is_bad = True
            reasons_found.append("ungrammatical_or_hybrid")
        if len(r) < 30 and not opt.get("isCorrect"):
            is_bad = True
            reasons_found.append("too_short")
        if r.lower() in ["incorrect. ungrammatical.", "incorrect. ungrammatical", "incorrect. not correct.", "incorrect. wrong form.", "incorrect. wrong particle."]:
            is_bad = True
            reasons_found.append("exact_generic")
        if "非文となります" in r or "非文です" in r:
            is_bad = True
            reasons_found.append("hibun")
        if "成立しません" in r and len(r) < 65:
            is_bad = True
            reasons_found.append("generic_seiritsu")

        if is_bad:
            problematic.append({
                "id": e["id"],
                "bookId": e.get("bookId"),
                "chapter": e.get("chapter"),
                "question": e.get("question"),
                "translation": e.get("translation"),
                "optionIndex": idx,
                "optionText": opt.get("text"),
                "isCorrect": opt.get("isCorrect"),
                "reason": r,
                "flags": reasons_found
            })

print(f"Total problematic option reasons found: {len(problematic)}")
from collections import Counter
print("By book:", Counter(x["bookId"] for x in problematic))
print("By flag:", Counter(f for x in problematic for f in x["flags"]))

with open("jlpt-exam-prep/scratch/problematic_reasons.json", "w", encoding="utf-8") as f:
    json.dump(problematic, f, ensure_ascii=False, indent=2)
