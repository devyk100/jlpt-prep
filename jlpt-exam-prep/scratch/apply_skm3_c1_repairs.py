import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c1_repairs = {
    ('skm3-c1-ex-1', '際して'): "Incorrect. 〜に際して (or 〜に際し) is a formal written expression meaning 'on the formal occasion of' (e.g., 開会に際して = on the occasion of the opening). It cannot express consuming food while it is still warm.",
    ('skm3-c1-ex-1', 'ところで'): "Incorrect. ところで functions as a conversational transition ('by the way') or, after ta-form, a concessive conditional ('even if'). It cannot express an ongoing window of favorable opportunity.",
    ('skm3-c1-ex-2', 'ところで'): "Incorrect. V-たところで expresses concessive conditional meaning 'even if [one tries]... it will be futile' (相談したところで解決しない). It cannot express spontaneous internal transition during an activity.",
    ('skm3-c1-ex-2', 'たびに'): "Incorrect. 〜たびに means 'every single time' (会うたびに = every time we meet). The sentence describes a single specific occurrence of drifting off to sleep unnoticed during the teacher's lecture.",
    ('skm3-c1-ex-3', 'てから'): "Incorrect. Simple chronological 〜てから ('after doing X') does not enforce the negative consequence restriction required by 契約書にサインはできません; stating that signing is strictly impossible without consulting a lawyer requires the prerequisite conditional 〜てからでないと.",
    ('skm3-c1-ex-3', 'た後で'): "Incorrect. 〜た後で merely indicates a neutral chronological order ('after having done X'). It lacks the strong conditional prerequisite restriction ('not until / unless...') that governs the negative predicate サインはできません.",
    ('skm3-c1-ex-3', 'たところで'): "Incorrect. 〜たところで means 'even if [action is taken], [no useful result will follow]' (今さら弁護士に相談したところで、どうにもならない). It contradicts the conditional prerequisite required to enable signing.",
    ('skm3-c1-ex-4', 'とおり'): "Incorrect. 〜とおり (or 〜どおり) means 'in accordance with' or 'just as' (計画のとおり = as planned). It cannot indicate an imminent temporal phase ('just about to head out').",
    ('skm3-c1-ex-5', 'る最中'): "Incorrect. 最中 (さいちゅう) indicates being right in the peak middle of an active process (食事の最中 / 会議をしている最中). It cannot express the immediate completion of an action that just finished, and appending *る最中 directly to past stem 終わっ- is morphologically invalid.",
    ('skm3-c1-ex-5', 'るばかり'): "Incorrect. [Verb-dict] + ばかりだ expresses an ongoing monotonic trend or worsening tendency ('continues to...'). Immediate completion just a moment ago requires たところだ (食べ終わったところです).",
    ('skm3-c1-ex-5', 'たはず'): "Incorrect. はず expresses objective expectation or deduction ('should / ought to be'). Stating one's own immediate completion of a meal right this second (たった今) requires the temporal completion phase 〜たところだ.",
    ('skm3-c1-ex-6', 'うちに'): "Incorrect. 〜うちに indicates taking advantage of a temporary, perishable opportunity window before conditions change. A planned duration lasting throughout the entire summer vacation (ずっと実家に滞在していた) requires the continuous temporal noun 間 (夏休みの間).",
    ('skm3-c1-ex-6', '最中に'): "Incorrect. 〜最中に indicates an unexpected interruption occurring during the middle of a dynamic action. It cannot pair with the continuous durational predicate ずっと実家に滞在していました.",
    ('skm3-c1-ex-7', '降るうちに'): "Incorrect. Affirmative 降るうちに would literally mean 'while it is raining', which contradicts the objective of hurrying home to avoid getting wet. Expressing 'before the rain starts' requires the negative form 降らないうちに.",
    ('skm3-c1-ex-7', '降った'): "Incorrect. The past form 降った cannot connect with うちに to express an impending prospective opportunity window. Expressing 'before it starts raining' requires the non-past negative 降らないうちに.",
    ('skm3-c1-ex-7', '降っている'): "Incorrect. Continuous 降っている implies that rain is already actively falling. The speaker looks at darkening skies and proposes returning before rain begins, requiring 降らないうちに."
}

count = 0
for ex in exercises:
    if ex.get('bookId') == 'skm-n3' and ex.get('chapter') == 'Part 1 · Chapter 1':
        for opt in ex.get('explanation', {}).get('options', []):
            key = (ex['id'], opt.get('text'))
            if key in c1_repairs:
                opt['reason'] = c1_repairs[key]
                count += 1

print(f"Updated {count} distractor reasons in SKM N3 Chapter 1.")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved chapterExercises.json successfully!")
