import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c5_repairs = {
    ('skm3-c5-ex-1', 'ことから'): "Incorrect. 〜ことから indicates that an observable fact provides the rationale for a name, appellation, or discovery (e.g. 富士山に似ていることから). It cannot express direct physical causality for a transportation delay caused by snow.",
    ('skm3-c5-ex-2', 'ために'): "Incorrect. 〜ために indicates direct physical or logical cause-and-effect (e.g. 大雪のために遅延). The historical or perceptual clue that gives rise to a name or appellation ('called Little Fuji because of resemblance') uniquely takes ことから (〜ことから…と呼ばれている).",
    ('skm3-c5-ex-3', 'ことから'): "Incorrect. 〜ことから indicates that a clue or characteristic gave rise to a name or logical deduction. Passing an exam thanks to a teacher's guidance is a favorable personal outcome, which requires the gratitude expression おかげで.",
    ('skm3-c5-ex-3', 'あまり'): "Incorrect. 〜のあまり expresses that extreme emotional intensity causes an abnormal outcome (e.g. 嬉しさのあまり泣いた). Dedicated guidance is a beneficial source of support, not an uncontrollable emotional surge.",
    ('skm3-c5-ex-4', 'ことから'): "Incorrect. 〜ことから expresses the basis for a name or intellectual discovery. Failing to perform well in an athletic match due to lack of sleep is an unfavorable personal result, which takes the blame expression せいで (睡眠不足のせいで)."
}

count = 0
for ex in exercises:
    if ex.get('bookId') == 'skm-n3' and ex.get('chapter') == 'Part 1 · Chapter 5':
        for opt in ex.get('explanation', {}).get('options', []):
            key = (ex['id'], opt.get('text'))
            if key in c5_repairs:
                opt['reason'] = c5_repairs[key]
                count += 1

print(f"Updated {count} distractor reasons in SKM N3 Chapter 5.")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved chapterExercises.json successfully!")
