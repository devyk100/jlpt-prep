import json

pts = json.load(open('c:/JLPT/jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
g2_pts = [p for p in pts if p.get('book') == 'Genki II']
print(f"Total Genki II points: {len(g2_pts)}")
for p in g2_pts:
    print(f"{p.get('chapter', '')} | {p['id']} | {p['title']}")
