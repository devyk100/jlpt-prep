import re

with open("jlpt-exam-prep/src/data/bookSkmN2.ts", encoding="utf-8") as f:
    text = f.read()

pattern = r'id:\s*\"(skm2-c[0-9]+-[^\"]+|added-n2-[^\"]+)\"[\s\S]*?title:\s*\"([^\"]+)\"'
matches = re.findall(pattern, text)
print(f"Total card matches in bookSkmN2.ts: {len(matches)}")
for cid, title in matches[:20]:
    print(f"  {cid} -> {title}")
