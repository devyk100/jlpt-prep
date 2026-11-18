with open('jlpt-exam-prep/content/expansion.tsv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    if 'たらどう' in line:
        print(f"Line {idx}: {line}")
