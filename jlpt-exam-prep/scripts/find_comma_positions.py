import json, re

with open("jlpt-exam-prep/scripts/reconstruction_inspection_34.json", encoding="utf-8") as f:
    items = json.load(f)

# The original sentences before comma removal (stored in our git diff step 7209):
# Let's see: we know from the previous git diff where the comma was in each sentence!
for item in items:
    assembled = item["assembled"]
    frags = item["ordered_fragments"]
    q = item["question"]
    # Check clause boundaries
    # E.g. in skm3-p2-c1-q6: assembled has 'かどうかまだ', original had 'かどうか、まだ' (between frag 3 and frag 4)
    # in skm2-p2-c1-q2: assembled has '甲斐があって彼は', original had '甲斐があって、彼は' (between frag 2 and frag 3)
    print(f"=== {item['id']} ===")
    print(f"  Frags: [1] {frags[0]}  [2] {frags[1]}  [3(★)] {frags[2]}  [4] {frags[3]}")
    print(f"  Assembled: {assembled}")
