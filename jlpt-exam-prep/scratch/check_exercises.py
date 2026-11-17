import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for ex in data:
    s = json.dumps(ex, ensure_ascii=False)
    for kw in ['(juppun)', '(hatachi)', '(matsu)', '(kau)']:
        if kw in s:
            print(f'Ex: {ex.get("id")} ({ex.get("chapter")})')
            print('  Found:', kw)
            print('  Explanation:', ex.get('explanation'))
            for o in ex.get('options', []):
                if kw in str(o):
                    print('  Option:', o)
