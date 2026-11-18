import json
import re
from pathlib import Path

root = Path('c:/JLPT/jlpt-exam-prep')
base = json.loads((root / 'content/base-reviewed.json').read_text(encoding='utf8'))

for x in base:
    ident = x['id']
    b = next((b for prefix, b in [('g1-', 'g1'), ('g2-', 'g2'), ('skm3-', 'n3'), ('skm2-', 'n2')] if ident.startswith(prefix)), None)
    if not b: continue
    m = re.search(r'-(?:l|u|c)(\d+)-', ident)
    # Check if matched or in fix
    print(f"{ident} -> {b} -> m={m.group(1) if m else None}")
