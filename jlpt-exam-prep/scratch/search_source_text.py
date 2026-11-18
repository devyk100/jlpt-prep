import os
import re

source_dir = 'jlpt-exam-prep/audit/source-text'

targets = ['くせに', 'たらどう', '反面', '次第']

files = os.listdir(source_dir)
for t in targets:
    print(f"\n==================== SEARCHING FOR [{t}] IN SOURCE-TEXT ====================")
    found = 0
    for f in files:
        fpath = os.path.join(source_dir, f)
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        if t in content:
            found += 1
            print(f"--- File: {f} ---")
            lines = content.splitlines()
            for i, line in enumerate(lines):
                if t in line:
                    context_lines = lines[max(0, i-2):min(len(lines), i+5)]
                    print("\n".join(context_lines))
                    print("-" * 30)
            if found >= 3:
                break
