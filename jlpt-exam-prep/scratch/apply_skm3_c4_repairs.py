import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c4_repairs = {
    ('skm3-c4-ex-1', 'について'): "Incorrect. 〜について marks a topic of speech, thought, or investigation ('about / concerning'). It cannot express the coexisting negative and positive aspects of a job.",
    ('skm3-c4-ex-2', 'に対して'): "Incorrect. 〜に対して contrasts two opposing subjects or expresses a stance directed toward someone. Exchanging one language lesson for another ('in exchange for teaching me Japanese, I will teach English') requires the reciprocal compensation pattern かわりに.",
    ('skm3-c4-ex-2', 'について'): "Incorrect. 〜について marks a topic of inquiry ('regarding / concerning'). It cannot express reciprocal favor exchange or compensation.",
    ('skm3-c4-ex-4', '反面'): "Incorrect. 〜反面 expresses two coexisting contradictory facets within the same subject. Comparing price levels between two temporal standards ('compared to last year, this year's prices...') requires the comparative benchmark に比べて (去年に比べて)."
}

count = 0
for ex in exercises:
    if ex.get('bookId') == 'skm-n3' and ex.get('chapter') == 'Part 1 · Chapter 4':
        for opt in ex.get('explanation', {}).get('options', []):
            key = (ex['id'], opt.get('text'))
            if key in c4_repairs:
                opt['reason'] = c4_repairs[key]
                count += 1

print(f"Updated {count} distractor reasons in SKM N3 Chapter 4.")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved chapterExercises.json successfully!")
