"""Card and table quality check."""
import json

ROOT = r"C:\JLPT\jlpt-exam-prep"
sp = json.load(open(f"{ROOT}/src/data/studyPoints.json", "r", encoding="utf-8"))
tables = json.load(open(f"{ROOT}/src/data/mugUpTables.json", "r", encoding="utf-8"))

# Sentence counts
no_sent = sum(1 for c in sp if len(c.get("sentences", [])) == 0)
one_sent = sum(1 for c in sp if len(c.get("sentences", [])) == 1)
multi = sum(1 for c in sp if len(c.get("sentences", [])) >= 2)
print(f"Cards with 0 sentences: {no_sent}")
print(f"Cards with 1 sentence: {one_sent}")
print(f"Cards with 2+ sentences: {multi}")

# Empty fields
empty_nuance = [c["id"] for c in sp if not c.get("nuance", "").strip()]
empty_meaning = [c["id"] for c in sp if not c.get("meaning", "").strip()]
empty_conn = [c["id"] for c in sp if not c.get("connection", "").strip()]
empty_take = [c["id"] for c in sp if not c.get("keyTakeaway", "").strip()]
print(f"\nCards with empty nuance: {len(empty_nuance)}")
print(f"Cards with empty meaning: {len(empty_meaning)}")
print(f"Cards with empty connection: {len(empty_conn)}")
print(f"Cards with empty keyTakeaway: {len(empty_take)}")

# Tables
print(f"\nTables: {len(tables)}")
for t in tables[:5]:
    tid = t.get("id", "?")
    title = t.get("title", "?")
    rows = t.get("rows", [])
    print(f"  {tid} - {title} ({len(rows)} rows)")

# Check for any exercises with mismatched option counts
ex = json.load(open(f"{ROOT}/src/data/chapterExercises.json", "r", encoding="utf-8"))
bad_opt_count = 0
bad_exp_count = 0
for e in ex:
    opts = e.get("options", [])
    exp_opts = e.get("explanation", {}).get("options", [])
    if len(opts) != len(exp_opts):
        bad_exp_count += 1
    ci = e.get("correctIndex", -1)
    if ci < 0 or ci >= len(opts):
        bad_opt_count += 1

print(f"\nExercises with correctIndex out of range: {bad_opt_count}")
print(f"Exercises with options/explanation count mismatch: {bad_exp_count}")

# Check for N2 explanation language distribution
n2_ex = [e for e in ex if e["bookId"] == "skm-n2"]
jp_reasons = 0
en_reasons = 0
for e in n2_ex:
    for o in e.get("explanation", {}).get("options", []):
        r = o.get("reason", "")
        if r.startswith("【"):
            jp_reasons += 1
        elif r.startswith("Correct") or r.startswith("Incorrect"):
            en_reasons += 1

print(f"\nN2 feedback in Japanese style (【...】): {jp_reasons}")
print(f"N2 feedback in English style (Correct/Incorrect): {en_reasons}")

# Genki feedback language
g_ex = [e for e in ex if e["bookId"] in ("genki-1", "genki-2")]
gj = 0
ge = 0
for e in g_ex:
    for o in e.get("explanation", {}).get("options", []):
        r = o.get("reason", "")
        if r.startswith("【"):
            gj += 1
        elif "Correct" in r[:20] or "Incorrect" in r[:20]:
            ge += 1
print(f"\nGenki feedback in Japanese style: {gj}")
print(f"Genki feedback in English style: {ge}")
