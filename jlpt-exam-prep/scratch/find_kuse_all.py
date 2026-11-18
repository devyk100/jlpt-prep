import os

for root, dirs, files in os.walk('jlpt-exam-prep/audit'):
    for f in files:
        if f.endswith('.txt') or f.endswith('.json') or f.endswith('.md'):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    c = fp.read()
                if 'くせに' in c:
                    print(f"Found in: {p} (length {len(c)})")
            except Exception as e:
                pass
