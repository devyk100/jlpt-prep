import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c3_repairs = {
    ('skm3-c3-ex-1', 'ばかり'): "Incorrect. 〜ばかり denotes exclusivity or repetition ('only / just'). Describing laughing so intensely that one's stomach began to hurt expresses extreme degree, which requires ほど (お腹が痛くなるほど大笑いしました).",
    ('skm3-c3-ex-1', 'とおり'): "Incorrect. 〜とおり denotes conformity to a model or plan ('just as / according to'). It cannot indicate an illustrative extreme degree of laughing.",
    ('skm3-c3-ex-1', 'ついで'): "Incorrect. 〜ついで denotes taking advantage of a main activity to do a side errand ('while at it'). It cannot express metaphorical degree.",
    ('skm3-c3-ex-2', 'から'): "Incorrect. Particle から marks a starting point, source, or cause ('from / since'). The subjective superlative pattern asserting that nothing surpasses a standard ('nothing is as precious as health') is strictly Noun + ほど…はない (健康ほど大切なものはありません).",
    ('skm3-c3-ex-2', 'だけ'): "Incorrect. だけ expresses restriction or limitation ('only'). It does not form the negative superlative construction 〜ほど…はない.",
    ('skm3-c3-ex-3', 'とおりなら'): "Incorrect. 〜とおり expresses conformity with a model ('in accordance with'). Pairing とおり with contextual conditional なら (*とおりなら) does not form a comparative preference; rejecting an abhorrent option in favor of an alternative ('rather than apologize, I'd rather quit') requires くらいなら (謝るくらいなら).",
    ('skm3-c3-ex-3', 'うちに'): "Incorrect. 〜うちに denotes seizing an opportunity window before conditions change ('while / before'). It cannot express comparative preference between two alternatives.",
    ('skm3-c3-ex-3', 'ついでに'): "Incorrect. 〜ついでに denotes performing an incidental secondary errand during a primary outing. It cannot express preferring one action over another."
}

count = 0
for ex in exercises:
    if ex.get('bookId') == 'skm-n3' and ex.get('chapter') == 'Part 1 · Chapter 3':
        for opt in ex.get('explanation', {}).get('options', []):
            key = (ex['id'], opt.get('text'))
            if key in c3_repairs:
                opt['reason'] = c3_repairs[key]
                count += 1

print(f"Updated {count} distractor reasons in SKM N3 Chapter 3.")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved chapterExercises.json successfully!")
