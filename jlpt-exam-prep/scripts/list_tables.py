with open('jlpt-exam-prep/src/data/mugUpTables.ts', encoding='utf-8') as f:
    text = f.read()

import re
keys = re.findall(r'(\w+):\s*\{\s*title:\s*[\'"]([^\'"]+)[\'"]', text)
print(f"Total Master Mug-up Tables: {len(keys)}")
for k, t in keys:
    print(f"  {k}: {t}")
