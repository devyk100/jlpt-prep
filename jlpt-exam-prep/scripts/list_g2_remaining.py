import json

with open('c:/JLPT/jlpt-exam-prep/content/base-reviewed.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

for c in cards:
    ch = str(c.get('chapter', ''))
    bk = str(c.get('book', ''))
    cid = c.get('id', '')
    title = c.get('title', '')
    if any(k in ch for k in ['Lesson 19', 'Lesson 20', 'Lesson 21', 'Lesson 22', 'Lesson 23']):
        print(f"{cid} | {bk} | {ch} | {title}")
