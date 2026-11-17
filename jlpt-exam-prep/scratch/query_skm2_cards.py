import json

pts = json.load(open('c:/JLPT/jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
for p in pts:
    if p.get('book') == 'Shin Kanzen Master N2' and 'Part 1 · Chapter' in p.get('chapter', ''):
        print(f"{p['chapter']} | {p['id']} | {p['title']}")
