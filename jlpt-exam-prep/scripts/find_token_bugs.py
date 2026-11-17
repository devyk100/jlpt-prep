import json

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

for p in points:
    for s in p['sentences']:
        for t in s.get('tokens', []):
            if t['word'] in ['切り', '切る', 'きり'] and 'cut' in t.get('meaning', '').lower():
                print(f"Sentence: {s['japanese']}")
                print(f"  Token: {t['word']} -> {t['meaning']}")
            if t['word'] == 'なら' and 'copula' in t.get('meaning', '').lower():
                print(f"Sentence: {s['japanese']}")
                print(f"  Token: {t['word']} -> {t['meaning']}")
            if t['word'] in ['上で', 'うえで'] and 'after' in t.get('meaning', '').lower():
                print(f"Sentence: {s['japanese']}")
                print(f"  Token: {t['word']} -> {t['meaning']}")
