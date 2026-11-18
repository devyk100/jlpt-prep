import json

matrix = json.load(open('jlpt-exam-prep/audit/source-coverage-matrix.json', encoding='utf-8'))
study_points = json.load(open('jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
sp_map = {sp['id']: sp for sp in study_points}
exercises = json.load(open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8'))
ex_chapters = set(ex.get('chapter') for ex in exercises)

print(f"Total study points: {len(study_points)}")
print(f"Total exercises: {len(exercises)}")

reopened = [(idx, r) for idx, r in enumerate(matrix) if r.get('status') == 'reopened']
print(f"Total reopened rows: {len(reopened)}")

for idx, r in reopened:
    cid = r.get('cardId')
    sec = r.get('sourceSection')
    item = r.get('grammarItem')
    sp = sp_map.get(cid)
    sp_status = "FOUND" if sp else "MISSING"
    num_sentences = len(sp.get('sentences', [])) if sp else 0
    print(f"Row {idx:3d} | {sec:22s} | cid: {str(cid):30s} | SP: {sp_status:7s} ({num_sentences} sents) | Item: {item[:30]}")
