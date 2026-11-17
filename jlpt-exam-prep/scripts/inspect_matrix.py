import json

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", "r", encoding="utf-8") as f:
    sc = json.load(f)

for i, item in enumerate(sc):
    print(f"{i+1}. [{item.get('sourceBook')}] {item.get('sourceSection')} - {item.get('grammarItem')} ({item.get('cardId')}) -> status: {item.get('status')}")
