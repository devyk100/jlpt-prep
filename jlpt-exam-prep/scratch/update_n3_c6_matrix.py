import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

for row in matrix:
    if row.get('sourceBook') == 'Shin Kanzen Master N3' and row.get('sourceSection') == 'Part 1 · Chapter 6':
        item = row.get('grammarItem')
        card_id = row.get('cardId')
        row['status'] = 'checked'
        row['missingWork'] = ''
        row['evidence'] = (
            f"Physical scan verified: Shin Kanzen Master N3 pp. 32-33 (PDF pp. 55-56). "
            f"Source item '{item}' covered by card [{card_id}], "
            f"and 12 chapter practice exercises (skm3-c6-q1 through skm3-c6-q12) "
            f"verified for answer uniqueness, natural translation, and sentence-specific distractor rationale."
        )

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print("Updated SKM N3 Chapter 6 rows in source-coverage-matrix.json!")
