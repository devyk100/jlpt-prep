import json

matrix = json.load(open('jlpt-exam-prep/audit/source-coverage-matrix.json', encoding='utf-8'))
study_points = json.load(open('jlpt-exam-prep/src/data/studyPoints.json', encoding='utf-8'))
sp_map = {sp['id']: sp for sp in study_points}

total = len(matrix)
checked = [r for r in matrix if r.get('status') == 'checked']
reopened = [r for r in matrix if r.get('status') == 'reopened']
has_missing_work = [r for r in matrix if r.get('missingWork')]
missing_card_ids = [r for r in matrix if r.get('cardId') and r.get('cardId') not in sp_map]

print(f"Total rows: {total}")
print(f"Checked rows: {len(checked)}")
print(f"Reopened rows: {len(reopened)}")
print(f"Rows with non-empty missingWork: {len(has_missing_work)}")
print(f"Rows with missing cardId in studyPoints.json: {len(missing_card_ids)}")

if missing_card_ids:
    for r in missing_card_ids:
        print(f"  Missing cid: {r.get('cardId')} in section {r.get('sourceSection')}")
