import json
import re

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

print(f"Total exercises: {len(exercises)}")

blank_patterns = [
    r'（　　）',
    r'（　）',
    r'（\s+）',
    r'\(\s*\)',
    r'＿＿\s*★\s*＿＿', # star questions
    r'＿＿'
]

no_blank = []
star_count = 0
standard_count = 0

for idx, ex in enumerate(exercises):
    q = ex.get('question', '')
    opts = ex.get('options', [])
    c_idx = ex.get('correctIndex', 0)
    eid = ex.get('id', f'idx-{idx}')
    
    # Check if star mark question
    if ex.get('type') == 'star-mark' or '★' in q or ex.get('reconstructedSentence'):
        star_count += 1
        continue
        
    # Standard question: find blank
    # Match standard Japanese fullwidth parentheses with spaces or ASCII
    m = re.search(r'（[^）]*）|\([^)]*\)|＿＿+', q)
    if not m:
        no_blank.append((eid, q))
    else:
        standard_count += 1

print(f"Star exercises: {star_count}")
print(f"Standard exercises with blank: {standard_count}")
print(f"Exercises without blank: {len(no_blank)}")
if no_blank:
    for item in no_blank[:5]:
        print(f"  {item[0]}: {item[1]}")
