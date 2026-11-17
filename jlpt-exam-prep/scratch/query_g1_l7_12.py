import json

pts = json.load(open('c:/JLPT/jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
for p in pts:
    if p.get('book') == 'Genki I':
        ch = p.get('chapter', '')
        for i in range(7, 13):
            if f'Lesson {i}' in ch:
                print(f"{ch} | {p['id']} | {p['title']}")
