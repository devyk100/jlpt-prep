import json

with open('c:/JLPT/jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

def find_cards(query):
    print(f"=== Query: {query} ===")
    for c in cards:
        if query.lower() in c['id'].lower() or query.lower() in c['title'].lower():
            print(f"  {c['id']} | {c['title']} | {c.get('book')} {c.get('chapter')}")

find_cards('potential')
find_cards('volitional')
find_cards('transitive')
find_cards('adjective')
find_cards('te-form')
find_cards('short')
find_cards('keigo')
find_cards('passive')
find_cards('causative')
