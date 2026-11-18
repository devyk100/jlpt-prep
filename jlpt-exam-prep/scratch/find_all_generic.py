import json
import re

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

generic_phrases = [
    "ungrammatical", "non-standard", "invalid", "distractor", "not correct",
    "incorrect formation", "formation error", "wrong form", "wrong particle",
    "not a valid", "doesn't make sense", "does not make sense", "meaning error",
    "incorrect. ungrammatical", "incorrect connection", "incorrect option",
    "非文", "不自然", "文法的に不適切", "意味が通じない"
]

found = []
for e in exercises:
    expl = e.get("explanation", {})
    opts = expl.get("options", [])
    for idx, opt in enumerate(opts):
        r = opt.get("reason", "")
        r_lower = r.lower()
        matched = [p for p in generic_phrases if p in r_lower]
        if matched and (len(r) < 60 or "ungrammatical" in r_lower or "非文" in r_lower or r.startswith("Incorrect.") and len(r) < 40):
            found.append({
                "id": e["id"],
                "bookId": e.get("bookId"),
                "chapter": e.get("chapter"),
                "question": e.get("question"),
                "optionIndex": idx,
                "optionText": opt.get("text"),
                "reason": r,
                "matched": matched
            })

print(f"Total potentially generic reasons found: {len(found)}")
from collections import Counter
print("By book:", Counter(x["bookId"] for x in found))
print("\nSample 15 matches:")
for x in found[:15]:
    print(f"[{x['id']} - {x['bookId']} - {x['chapter']}] Opt {x['optionIndex']} '{x['optionText']}': {x['reason']}")
