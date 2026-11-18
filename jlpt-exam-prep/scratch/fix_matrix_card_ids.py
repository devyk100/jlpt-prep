import json

matrix = json.load(open('jlpt-exam-prep/audit/source-coverage-matrix.json', encoding='utf-8'))
study_points = json.load(open('jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
sp_map = {sp['id']: sp for sp in study_points}

mapping = {
    256: 'added-n2-16-95',
    257: 'skm2-c15-mono-nara',
    258: 'added-n2-17-97',
    259: 'added-n2-17-98',
    260: 'added-n2-17-98',
    261: 'added-n2-18-99',
    262: 'added-n2-18-100',
    264: 'added-n2-19-101',
    265: 'added-n2-19-102',
}

for idx, dest_id in mapping.items():
    r = matrix[idx]
    r['cardId'] = dest_id
    sp = sp_map[dest_id]
    sents = sp.get('sentences', [])
    r['exampleCount'] = len(sents)
    r['exampleIds'] = [s['id'] for s in sents]

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print("Updated 9 rows to valid destination card IDs.")

# Verify all card IDs
missing = [r for r in matrix if r.get('cardId') and r.get('cardId') not in sp_map]
print(f"Remaining missing card IDs: {len(missing)}")
