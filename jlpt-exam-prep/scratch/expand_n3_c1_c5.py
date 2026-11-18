import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

expansions = {
    ('skm3-c1-ex-9', 'だから'): "Incorrect. The prerequisite pattern 'not until / unless' is formed by [Verb-て] からでないと. The explanatory particle だから ('because') does not connect after て (*てだから) and cannot establish a prerequisite dependency.",
    ('skm3-c1-ex-10', 'ばかり'): "Incorrect. Although 〜たばかり expresses having just done something, attaching direct object を (*食べているばかりを) to express being caught in the act is ungrammatical; catching someone in the middle of a continuous physical act requires [Verb-ている] ところを.",
    ('skm3-c2-ex-6', '予想で'): "Incorrect. Nouns connect to どおり either directly with rendaku (予想どおり) or with particle の unvoiced (予想のとおり). The instrumental particle で cannot connect to どおり (*予想でどおり).",
    ('skm3-c2-ex-8', '行って'): "Incorrect. The recurring event marker 〜たびに requires the non-past dictionary form of verbs (行くたびに). Connective te-forms cannot precede たびに (*行ってたびに is ungrammatical).",
    ('skm3-c2-ex-8', '行った'): "Incorrect. 〜たびに describes recurring habitual actions and requires the non-past dictionary form (行くたびに). The past ta-form cannot attach to たびに (*行ったたびに is ungrammatical).",
    ('skm3-c2-ex-10', '行こう'): "Incorrect. 〜ついでに requires dictionary form or past ta-form of verbs (行くついでに / 行ったついでに). The volitional form cannot precede ついでに (*行こうついでに).",
    ('skm3-c2-ex-10', '行けば'): "Incorrect. The conditional ba-form cannot modify the temporal noun ついでに (*行けばついでに). Verbs must be in the plain attributive form.",
    ('skm3-c2-ex-11', '思って'): "Incorrect. 〜とおり functions syntactically as a noun and requires plain attributive verb forms (思ったとおり / 思うとおり). The connective te-form cannot modify とおり directly (*思ってとおり).",
    ('skm3-c2-ex-11', '思えば'): "Incorrect. The conditional ba-form cannot modify the noun とおり (*思えばとおり); plain past form 思ったとおり is required.",
    ('skm3-c3-ex-4', 'に違いない'): "Incorrect. 〜に違いない expresses the speaker's strong objective conviction or deduction ('must be / no doubt that...'). Recommending the best course of action for curing a cold ('sleeping warmly is by far the best choice') requires に限る (寝るに限る).",
    ('skm3-c3-ex-4', 'に決まっている'): "Incorrect. 〜に決まっている expresses an emphatic certainty or predetermined inevitability ('it is bound to be'). Stating one's personal judgment that an action is the single best remedy requires に限る.",
    ('skm3-c5-ex-3', 'せいで'): "Incorrect. 〜せいで attributes blame for an undesirable misfortune or failure. Passing an exam after hard study is a joyous success, which requires the gratitude expression おかげで (ご指導のおかげで合格できました).",
    ('skm3-c5-ex-4', 'おかげで'): "Incorrect. 〜おかげで expresses gratitude for a beneficial or happy result. Failing to perform well in an athletic match due to lack of sleep is an undesirable failure, which takes the blame expression せいで (睡眠不足のせいで)."
}

count = 0
for ex in exercises:
    for opt in ex.get('explanation', {}).get('options', []):
        key = (ex.get('id'), opt.get('text'))
        if key in expansions:
            opt['reason'] = expansions[key]
            count += 1

print(f"Applied {count} expansions.")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved chapterExercises.json successfully!")
