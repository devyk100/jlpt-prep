import json

with open("jlpt-exam-prep/src/data/annotations.json", "r", encoding="utf-8") as f:
    annotations = json.load(f)

print(f"Total annotated terms in dictionary: {len(annotations)}")

# Check for known problematic glosses
suspicious = []
for term, data in annotations.items():
    gloss = data.get('gloss', '')
    reading = data.get('reading', '')
    if term in ['切る', '切り', 'きり'] and 'cut' in gloss.lower() and not 'limit' in gloss.lower() and not 'finish' in gloss.lower():
        suspicious.append((term, reading, gloss))
    if term == 'なら' and 'copula' in gloss.lower() and not 'if' in gloss.lower():
        suspicious.append((term, reading, gloss))
    if term in ['上で', 'うえで'] and 'after' in gloss.lower() and not 'basis' in gloss.lower() and not 'aspect' in gloss.lower():
        suspicious.append((term, reading, gloss))
    if term in ['わけ', 'もの', 'こと', 'ところ'] and len(gloss) < 15:
        suspicious.append((term, reading, gloss))

print(f"Suspicious global gloss entries: {len(suspicious)}")
for s in suspicious[:10]:
    print(f"  {s[0]} ({s[1]}): {s[2]}")
