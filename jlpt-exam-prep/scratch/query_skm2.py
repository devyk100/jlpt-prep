import json

pts = json.load(open('c:/JLPT/jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
skm2_pts = [p for p in pts if p.get('book') == 'Shin Kanzen Master N2']
print(f"Total SKM N2 points: {len(skm2_pts)}")
chapters = set(p.get('chapter', '') for p in skm2_pts)
print(f"Chapters ({len(chapters)}): {sorted(list(chapters))}")
