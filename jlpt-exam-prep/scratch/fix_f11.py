import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

# Repair skm2-p1-form-review-f-q11
repaired_count = 0
for ex in exercises:
    if ex.get('id') == 'skm2-p1-form-review-f-q11':
        for opt in ex.get('explanation', {}).get('options', []):
            if opt.get('text') == 'など／など':
                opt['reason'] = '【不正解】「など」は名詞等の例示に用いられ、用言節を直接重ねて「〜など〜など」と不満・批判を並べ立てる列挙形式としては文法的に成立しません（不平・ケチつけの列挙には「だの／だの」を用いる）。'
                repaired_count += 1

print(f"Repaired {repaired_count} exercise(s).")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)
