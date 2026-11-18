import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp = json.load(f)

skm2_pts = [p for p in sp if p.get('book') == 'Shin Kanzen Master N2' or 'skm2' in p.get('id', '') or 'added-n2' in p.get('id', '')]
print(f"Total N2 points in studyPoints.json: {len(skm2_pts)}")

# Group by chapter
by_ch = {}
for p in skm2_pts:
    ch = p.get('chapter', 'Unknown')
    by_ch.setdefault(ch, []).append(p)

for ch, pts in sorted(by_ch.items()):
    print(f"{ch}: {len(pts)} cards")
    for p in pts:
        print(f"   [{p['id']}] {p['title']}")
