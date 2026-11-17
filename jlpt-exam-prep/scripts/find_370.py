import glob
import re

for filepath in glob.glob("jlpt-exam-prep/**/*.ts*", recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if '370' in content:
        print(f"Found '370' in {filepath}")
        for line in content.splitlines():
            if '370' in line:
                print(f"  {line}")
