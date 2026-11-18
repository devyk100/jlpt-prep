import json

with open('jlpt-exam-prep/audit/source-coverage-matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

for r in matrix:
    if r.get('sourceBook') == 'Shin Kanzen Master N2' and r.get('sourceSection') in [
        'Part 1 · Chapter 14', 'Part 1 · Chapter 15', 'Part 1 · Chapter 16', 'Part 1 · Chapter 17'
    ]:
        print(f"Sec: {r.get('sourceSection')}, Item: {r.get('grammarItem')}, CardId: {r.get('cardId')}, Status: {r.get('status')}")
        print(f"  Exact pp: {r.get('exactPrintedPages')}, Missing: {r.get('missingWork')}")
