import os
import re

scripts_dir = 'jlpt-exam-prep/scripts'
target_writes = {}

for f in os.listdir(scripts_dir):
    if f.endswith('.py'):
        p = os.path.join(scripts_dir, f)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        matches = re.findall(r"src/data/([a-zA-Z0-9_\-\.]+)", content)
        if matches:
            for m in set(matches):
                target_writes.setdefault(m, []).append(f)

print("Files in src/data referenced by scripts:")
for fname, script_list in sorted(target_writes.items()):
    print(f"  {fname} (in {len(script_list)} scripts, e.g. {script_list[:3]})")
