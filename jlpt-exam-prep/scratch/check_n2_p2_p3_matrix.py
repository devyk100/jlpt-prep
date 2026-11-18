import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

for r in matrix:
    if r.get('sourceBook') == 'Shin Kanzen Master N2' and ('Part 2' in r.get('sourceSection', '') or 'Part 3' in r.get('sourceSection', '')):
        print(f"Section: {r.get('sourceSection')}, Item: {r.get('grammarItem')}, Status: {r.get('status')}")
        print(f"Missing work: {r.get('missingWork')}")
        print(f"CardId: {r.get('cardId')}")
        print("-" * 40)
