import json

with open("jlpt-exam-prep/audit/BOOK_SKM_N2_POINTS.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f if l.strip()]

for i, l in enumerate(lines):
    if ' | ' in l and not l.endswith(('| 0', '| 1', '| 2', '| 3')):
        print(f"{l}")
