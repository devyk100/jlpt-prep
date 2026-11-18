"""Sample exercises for review."""
import json, random

ROOT = r"C:\JLPT\jlpt-exam-prep"
ex = json.load(open(f"{ROOT}/src/data/chapterExercises.json", "r", encoding="utf-8"))

def show_exercise(e):
    print(f"  ID: {e['id']}")
    print(f"  Q: {e['question']}")
    print(f"  Opts: {e['options']}")
    ci = e["correctIndex"]
    print(f"  Answer: [{ci}] {e['options'][ci]}")
    ctx = e.get("context", "")
    if ctx:
        print(f"  Context: {ctx}")
    tr = e.get("translation", "")
    if tr:
        print(f"  Translation: {tr}")
    exp = e.get("explanation", {})
    for o in exp.get("options", []):
        reason = o.get("reason", "")
        print(f"    {o.get('text','')}: {reason[:220]}")
    print(f"  Provenance: {e.get('provenance', '')}")
    print()

# Genki I Lesson 1
g1l1 = [e for e in ex if e["bookId"] == "genki-1" and e["chapter"] == "Lesson 1"]
print(f"=== G1 Lesson 1: {len(g1l1)} exercises ===")
for e in g1l1[:3]:
    show_exercise(e)

# Genki II Lesson 17
g2l17 = [e for e in ex if e["bookId"] == "genki-2" and e["chapter"] == "Lesson 17"]
print(f"=== G2 Lesson 17: {len(g2l17)} exercises ===")
for e in g2l17[:2]:
    show_exercise(e)

# N3 chapter 1
n3c1 = [e for e in ex if e["bookId"] == "skm-n3" and e["chapter"] == "Chapter 1"]
print(f"=== N3 Chapter 1: {len(n3c1)} exercises ===")
for e in n3c1[:2]:
    show_exercise(e)

# N2 random sample
n2 = [e for e in ex if e["bookId"] == "skm-n2"]
print(f"=== N2: {len(n2)} total exercises ===")
random.seed(42)
for e in random.sample(n2, 3):
    show_exercise(e)

# Feedback quality scan
generic = 0
short = 0
for e in ex:
    for o in e.get("explanation", {}).get("options", []):
        r = o.get("reason", "")
        if r.strip() in ("Incorrect.", "Incorrect. Ungrammatical.", "Ungrammatical.", ""):
            generic += 1
        if len(r) < 15 and "Correct" not in r and "correct" not in r:
            short += 1

print(f"\n=== FEEDBACK QUALITY SCAN ({len(ex)} exercises) ===")
print(f"Generic 'Incorrect/Ungrammatical' only: {generic}")
print(f"Very short non-correct reasons (<15 chars): {short}")

# Provenance distribution
from collections import Counter
prov = Counter(e.get("provenance", "unset") for e in ex)
print(f"\n=== PROVENANCE DISTRIBUTION ===")
for p, n in prov.most_common():
    print(f"  {p}: {n}")
