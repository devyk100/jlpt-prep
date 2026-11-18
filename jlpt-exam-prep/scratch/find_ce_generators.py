import os
import re

scripts_dir = 'jlpt-exam-prep/scripts'
writes_to_ce = []

for f in os.listdir(scripts_dir):
    if f.endswith('.py'):
        p = os.path.join(scripts_dir, f)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        if 'chapterExercises.json' in content and ('write' in content or 'dump' in content):
            # check if open for writing
            if re.search(r"open\([^,]+chapterExercises\.json[^,]*,\s*['\"]w['\"]", content) or "w" in content:
                writes_to_ce.append(f)

print(f"Scripts writing to chapterExercises.json: {len(writes_to_ce)}")
for s in writes_to_ce:
    print(f"  {s}")
