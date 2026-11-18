import os

source_dir = 'jlpt-exam-prep/audit/source-text'

for f in sorted(os.listdir(source_dir)):
    if f.startswith('n2-'):
        p = os.path.join(source_dir, f)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            c = fp.read()
        if 'くせ' in c or 'のに' in c:
            for line in c.splitlines():
                if 'くせ' in line:
                    print(f"File {f}: {line}")
