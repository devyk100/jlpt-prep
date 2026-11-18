import json, re

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    exercises = json.load(f)

aligned_count = 0
for ex in exercises:
    if ex.get("type") == "star-mark":
        q = ex["question"]
        order = ex.get("scrambleOrder", [])
        opts = ex.get("options", [])
        m = re.search(r"＿＿\s*＿＿\s*★\s*＿＿", q)
        if m:
            prefix = q[:m.start()].strip()
            suffix = q[m.end():].strip()
            exact_assembled = prefix + "".join(opts[p - 1] for p in order) + suffix
            if ex.get("reconstructedSentence") != exact_assembled:
                ex["reconstructedSentence"] = exact_assembled
                aligned_count += 1

with open("jlpt-exam-prep/src/data/chapterExercises.json", "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print(f"Aligned {aligned_count} star-mark reconstructedSentences to exact prompt+fragments concatenation.")
