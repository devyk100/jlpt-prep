import json, re

# Load points from studyPoints.json
with open("jlpt-exam-prep/src/data/studyPoints.json", encoding="utf-8") as f:
    sp = json.load(f)

for p in sp:
    if p["id"] in ["skm2-c20-shidai-de-wa", "skm2-c15-kuse-ni", "skm2-c17-koto-kara", "skm2-c17-wake-de-wa-nai", "skm2-c14-hanmen"]:
        p["quiz"] = []
        p["tags"] = ["N2", "Shin Kanzen Master N2", p["chapter"]]

with open("jlpt-exam-prep/src/data/studyPoints.json", "w", encoding="utf-8") as f:
    json.dump(sp, f, ensure_ascii=False, indent=2)

# Update bookSkmN2.ts
with open("jlpt-exam-prep/src/data/bookSkmN2.ts", encoding="utf-8") as f:
    ts_text = f.read()

# We need each of the 5 points in bookSkmN2.ts to have quiz: [] and tags: [...]
for pid in ["skm2-c20-shidai-de-wa", "skm2-c15-kuse-ni", "skm2-c17-koto-kara", "skm2-c17-wake-de-wa-nai", "skm2-c14-hanmen"]:
    # Find the object in ts_text and add quiz and tags before the closing brace of that object
    p_obj = [p for p in sp if p["id"] == pid][0]
    # Replace the object in ts_text with full json formatting
    pattern = re.compile(r'\{\s*"id":\s*"' + pid + r'"[\s\S]*?\n  \}', re.MULTILINE)
    replacement = json.dumps(p_obj, ensure_ascii=False, indent=2)
    replacement = "  " + replacement.replace("\n", "\n  ")
    ts_text = pattern.sub(replacement, ts_text)

with open("jlpt-exam-prep/src/data/bookSkmN2.ts", "w", encoding="utf-8") as f:
    f.write(ts_text)

print("Updated bookSkmN2.ts and studyPoints.json with quiz and tags for the 5 points!")
