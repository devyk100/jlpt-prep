import json
from pathlib import Path

root = Path('c:/JLPT/jlpt-exam-prep')
base = json.loads((root / 'content/base-reviewed.json').read_text(encoding='utf8'))
expansion_lines = [l for l in (root / 'content/expansion.tsv').read_text(encoding='utf8').splitlines() if l.strip()]

print(f"Total cards in base-reviewed.json: {len(base)}")
print(f"Total lines in expansion.tsv: {len(expansion_lines)}")

base_ids = set(c['id'] for c in base)
expansion_ids = set()
for i, line in enumerate(expansion_lines, 1):
    b, s = line.split('|')[:2]
    expansion_ids.add(f"added-{b}-{s.lower()}-{i}")

overlap = base_ids.intersection(expansion_ids)
print(f"Overlap between base-reviewed and expansion.tsv: {len(overlap)} cards")
