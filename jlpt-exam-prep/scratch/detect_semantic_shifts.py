import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

print("=== CHECKING CONTEXT / TRANSLATION / QUESTION ALIGNMENT ===")

by_chapter = {}
for ex in exercises:
    ch = ex.get('chapter', 'Unknown')
    by_chapter.setdefault(ch, []).append(ex)

for ch, ex_list in by_chapter.items():
    # Check a few keywords between question and translation if possible, or print summaries
    mismatches = []
    for ex in ex_list:
        q = ex.get('question', '')
        tr = ex.get('translation', '')
        ctx = ex.get('context', '')
        
        # Check specific obvious semantic disconnects:
        # e.g., question mentions typhoon/weather but translation mentions bridge/salary, etc.
        if '台風' in q and ('bridge' in tr.lower() or 'overtime' in tr.lower() or 'salary' in tr.lower()):
            mismatches.append((ex['id'], q, tr))
        elif '残業' in q and ('typhoon' in tr.lower() or 'weather' in tr.lower() or 'bridge' in tr.lower()):
            mismatches.append((ex['id'], q, tr))
        elif 'プライバシー' in q and ('promotion' in tr.lower() or 'weather' in tr.lower()):
            mismatches.append((ex['id'], q, tr))
        elif '航空機' in q and ('volcan' in tr.lower() or 'bridge' in tr.lower()):
            mismatches.append((ex['id'], q, tr))
        elif 'ウイルス' in q and ('bank' in tr.lower() or 'financial' in tr.lower()):
            mismatches.append((ex['id'], q, tr))

    if mismatches:
        print(f"Chapter [{ch}] has {len(mismatches)} obvious keyword mismatches!")
        for m in mismatches:
            print(f"  {m[0]}: Q='{m[1]}' vs Tr='{m[2]}'")
