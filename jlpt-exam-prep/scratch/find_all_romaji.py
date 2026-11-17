import re, os, glob

romaji_list = [
    'kau', 'matsu', 'toru', 'nomu', 'asobu', 'shinu', 'kaku', 'oyogu', 'iku', 'itte', 'itta',
    'hanasu', 'dasu', 'taberu', 'miru', 'okiru', 'suru', 'kuru', 'pun', 'hatachi', 'takai',
    'desu', 'deshita', 'shizuka', 'hairu', 'kaeru', 'yomu', 'ki-te', 'ki-ta', 'juppun'
]

results = []

for root, _, files in os.walk('jlpt-exam-prep'):
    if any(p in root for p in ['node_modules', 'dist', '.git']):
        continue
    for file in files:
        if file.endswith(('.ts', '.tsx', '.json', '.py', '.md')):
            p = os.path.join(root, file)
            with open(p, 'r', encoding='utf-8') as f:
                content = f.read()
            for r in romaji_list:
                # Look for (romaji) or (word romaji)
                pattern = rf'\([^\)]*?\b{r}\b[^\)]*?\)'
                for m in re.finditer(pattern, content, re.IGNORECASE):
                    start = max(0, m.start() - 30)
                    end = min(len(content), m.end() + 30)
                    results.append((p, m.group(0), content[start:end].replace('\n', ' ')))

print(f'Total findings: {len(results)}')
by_file = {}
for p, match, ctx in results:
    by_file.setdefault(p, []).append((match, ctx))

for p, items in by_file.items():
    print(f'=== {p} ({len(items)} items) ===')
    for m, c in items[:10]:
        print(f'   {m}  -->  {c}')
