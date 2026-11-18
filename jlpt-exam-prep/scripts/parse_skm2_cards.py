import json, re

with open("jlpt-exam-prep/src/data/bookSkmN2.ts", encoding="utf-8") as f:
    text = f.read()

# Match JSON-like objects in TS file
card_ids = re.findall(r'"id":\s*"([^"]+)"', text)
titles = re.findall(r'"title":\s*"([^"]+)"', text)

print(f"Card IDs in bookSkmN2.ts: {len(card_ids)}")
print(f"Titles in bookSkmN2.ts: {len(titles)}")

# Pair up
pairs = []
pos = 0
while True:
    m_id = re.search(r'"id":\s*"([^"]+)"', text[pos:])
    if not m_id:
        break
    m_title = re.search(r'"title":\s*"([^"]+)"', text[pos + m_id.end():])
    if not m_title:
        break
    cid = m_id.group(1)
    title = m_title.group(1)
    pairs.append((cid, title))
    pos += m_id.end() + m_title.end()

print(f"Paired: {len(pairs)}")
for cid, title in pairs[:15]:
    print(f"  {cid} -> {title}")
