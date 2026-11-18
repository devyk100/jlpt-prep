"""Sample content for honest quality review."""
import json, random

ROOT = r"C:\JLPT\jlpt-exam-prep"

with open(f"{ROOT}/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    sp = json.load(f)
with open(f"{ROOT}/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    ex = json.load(f)
with open(f"{ROOT}/src/data/mugUpTables.json", "r", encoding="utf-8") as f:
    tables = json.load(f)
with open(f"{ROOT}/src/data/annotations.json", "r", encoding="utf-8") as f:
    ann = json.load(f)

print("=" * 60)
print("CONTENT OVERVIEW")
print("=" * 60)
print(f"Study cards: {len(sp)}")
print(f"Exercises: {len(ex)}")
print(f"Tables: {len(tables)}")
print(f"Annotation entries: {len(ann)}")

# Book distribution for cards
from collections import Counter
books = Counter(c.get("book", "?") for c in sp)
for b, n in sorted(books.items()):
    print(f"  {b}: {n} cards")

# Chapter distribution for exercises
ex_chaps = Counter(e.get("chapter", "?") for e in ex)
print(f"\nExercise chapters: {len(ex_chaps)} distinct")
# Show first few
for ch, n in sorted(ex_chaps.items())[:8]:
    print(f"  {ch}: {n} exercises")
print("  ...")

print("\n" + "=" * 60)
print("GENKI I LESSON 1 - SAMPLE CARD")
print("=" * 60)
g1l1 = [c for c in sp if c.get("book") == "Genki I" and "Lesson 1" in c.get("chapter", "")]
print(f"Cards in Lesson 1: {len(g1l1)}")
for c in g1l1[:2]:
    print(f"\n  ID: {c['id']}")
    print(f"  Title: {c['title']}")
    print(f"  Meaning: {c['meaning']}")
    print(f"  Connection: {c['connection']}")
    nuance = c.get("nuance", "")
    print(f"  Nuance (first 400 chars): {nuance[:400]}")
    print(f"  Key Takeaway: {c.get('keyTakeaway', '')}")
    sents = c.get("sentences", [])
    print(f"  Sentences: {len(sents)}")
    for s in sents[:2]:
        print(f"    JP: {s.get('japanese', '')}")
        print(f"    EN: {s.get('english', '')}")
        lit = s.get("literal", "")
        if lit:
            print(f"    Literal: {lit}")

print("\n" + "=" * 60)
print("GENKI I LESSON 1 - SAMPLE EXERCISE")
print("=" * 60)
g1l1_ex = [e for e in ex if "Lesson 1" in e.get("chapter", "") and "Genki I" in e.get("book", "")]
print(f"Exercises in G1 L1: {len(g1l1_ex)}")
if g1l1_ex:
    for e in g1l1_ex[:2]:
        print(f"\n  ID: {e['id']}")
        print(f"  Q: {e['question']}")
        print(f"  Options: {e['options']}")
        ci = e["correctIndex"]
        print(f"  Correct: [{ci}] {e['options'][ci]}")
        exp = e.get("explanation", {})
        for opt_exp in exp.get("options", []):
            reason = opt_exp.get("reason", "")
            print(f"    {opt_exp.get('text','')}: {reason[:200]}")

print("\n" + "=" * 60)
print("SKM N3 CHAPTER 1 - SAMPLE CARD")
print("=" * 60)
n3c1 = [c for c in sp if "N3" in c.get("book", "") and "Chapter 1" in c.get("chapter", "")]
print(f"Cards in N3 Ch1: {len(n3c1)}")
if n3c1:
    c = n3c1[0]
    print(f"  Title: {c['title']}")
    print(f"  Meaning: {c['meaning']}")
    print(f"  Connection: {c['connection']}")
    print(f"  Nuance (400): {c.get('nuance','')[:400]}")
    print(f"  Takeaway: {c.get('keyTakeaway','')}")

print("\n" + "=" * 60)
print("SKM N2 - SAMPLE EXERCISE FEEDBACK QUALITY")
print("=" * 60)
n2ex = [e for e in ex if "N2" in e.get("book", "")]
print(f"N2 exercises: {len(n2ex)}")
# Check for generic feedback
generic_count = 0
short_reason_count = 0
for e in n2ex:
    exp = e.get("explanation", {})
    for opt_exp in exp.get("options", []):
        r = opt_exp.get("reason", "")
        if r in ("Incorrect.", "Incorrect. Ungrammatical.", "Ungrammatical."):
            generic_count += 1
        if len(r) < 20 and "Correct" not in r:
            short_reason_count += 1

print(f"Generic 'Incorrect/Ungrammatical' feedback: {generic_count}")
print(f"Very short non-correct reasons (<20 chars): {short_reason_count}")

# Show one N2 exercise with all feedback
random.seed(99)
sample = random.choice(n2ex)
print(f"\nSample N2 exercise:")
print(f"  ID: {sample['id']}")
print(f"  Q: {sample['question']}")
print(f"  Opts: {sample['options']}")
ci = sample["correctIndex"]
print(f"  Correct: [{ci}] {sample['options'][ci]}")
exp = sample.get("explanation", {})
for opt_exp in exp.get("options", []):
    r = opt_exp.get("reason", "")
    print(f"    {opt_exp.get('text','')}: {r[:250]}")

print("\n" + "=" * 60)
print("ANNOTATION COVERAGE SAMPLE")
print("=" * 60)
# How many cards have annotations?
card_ids_with_ann = set()
for a in ann:
    sid = a.get("sentenceId", "")
    card_id = sid.split("::")[0] if "::" in sid else ""
    if card_id:
        card_ids_with_ann.add(card_id)
print(f"Cards with at least one annotated sentence: {len(card_ids_with_ann)}")
print(f"Total study cards: {len(sp)}")

# Check tables
print(f"\n{'='*60}")
print("TABLE SAMPLE")
print("="*60)
if tables:
    t = tables[0] if isinstance(tables, list) else list(tables.values())[0]
    if isinstance(tables, dict):
        tkey = list(tables.keys())[0]
        print(f"First table key: {tkey}")
        t = tables[tkey]
    if isinstance(t, dict):
        print(f"  Title: {t.get('title','')}")
        print(f"  Headers: {t.get('headers', t.get('columns',''))}")
        rows = t.get("rows", [])
        print(f"  Rows: {len(rows)}")
        if rows:
            print(f"  First row: {rows[0]}")
    elif isinstance(t, list):
        print(f"  (array table, first entry: {t[0] if t else 'empty'})")
