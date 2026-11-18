import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sps = json.load(f)

for sp in sps:
    if sp['id'] == 'g2-l14-tara-dou-desu-ka':
        print(json.dumps(sp, ensure_ascii=False, indent=2))
