import json
from collections import Counter

data = json.load(open("jlpt-exam-prep/scratch/n3_to_enrich.json", encoding="utf-8"))

short_reasons = []
for ex in data:
    for opt in ex["expl_options"]:
        r = opt.get("reason", "")
        if len(r) < 22 or "非文" in r or "要素です" in r:
            short_reasons.append(r)

counts = Counter(short_reasons)
print(f"Total short reasons: {len(short_reasons)}, Unique: {len(counts)}")
for r, c in counts.most_common(35):
    print(f"  ({c}x) {r}")
