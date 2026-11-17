import json

pts = json.load(open('c:/JLPT/jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
skm3_pts = [p for p in pts if p.get('book') == 'Shin Kanzen Master N3']
print(f"Total SKM N3 points: {len(skm3_pts)}")
chapters = set(p.get('chapter', '') for p in skm3_pts)
print(f"Chapters ({len(chapters)}): {sorted(list(chapters))}")
