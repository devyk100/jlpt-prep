import json
import re

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

patterns = [
    r'不自然です',
    r'文脈として不自然',
    r'文脈に合',
    r'意味が通',
    r'正しくありません',
    r'間違いです',
    r'誤りです',
    r'使えません。?$',
    r'適切ではありません。?$'
]

findings = []
for ex in exercises:
    eid = ex.get('id')
    opts = ex.get('explanation', {}).get('options', [])
    for idx, opt in enumerate(opts):
        r = opt.get('reason', '')
        # check if reason is just generic
        for pat in patterns:
            if re.search(pat, r):
                # check if the reason is very short or just the generic pattern
                if len(r) < 35 or r.endswith('不自然です。') or r.endswith('使えません。') or r.endswith('適切ではありません。'):
                    findings.append((eid, idx, opt.get('text'), r, pat))

print(f"Total potentially weak/generic reasons found: {len(findings)}")
for f in findings[:25]:
    print(f"[{f[0]}] opt {f[1]} ({f[2]}): {f[3]}")
