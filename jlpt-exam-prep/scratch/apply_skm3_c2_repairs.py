import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

c2_repairs = {
    ('skm3-c2-ex-1', 'ほどに'): "Incorrect. 〜ほど indicates extent, degree, or comparative approximation ('to the extent that...'). Following an instruction manual step-by-step to assemble an item requires とおりに (説明書に書いてあるとおりに = exactly as written in the instructions).",
    ('skm3-c2-ex-2', 'に対して'): "Incorrect. 〜に対して indicates a target of an action, stance, or direct contrast between two distinct entities (e.g. 兄に対して弟は...). Expressing variation across categories ('cultures differ depending on the country') requires によって (国によって違います).",
    ('skm3-c2-ex-2', 'について'): "Incorrect. 〜について introduces a topic of inquiry or speech ('regarding / about'). It cannot express causal variation across categories ('differ depending on').",
    ('skm3-c2-ex-3', 'とおりに'): "Incorrect. 〜とおりに denotes conformity with a model, instruction, or plan (e.g. 指示のとおりに). Recalling high school days each time a specific song plays is an invariable repeated occurrence, which requires たびに (聞くたびに).",
    ('skm3-c2-ex-3', 'うちに'): "Incorrect. 〜うちに expresses seizing an opportunity window before conditions change, or an unnoticed internal development. Invariable recurrence triggered repeatedly by a stimulus requires たびに.",
    ('skm3-c2-ex-4', 'ば練習するたびに'): "Incorrect. 〜たびに means 'every time' and connects to dictionary form (練習するたびに); combining it with the conditional ba-stem (*練習すれば練習するたびに) creates an ungrammatical hybrid. Proportional increase ('the more... the more...') requires 〜ば〜ほど.",
    ('skm3-c2-ex-4', 'ば練習するとおり'): "Incorrect. 〜とおり expresses conformity ('in accordance with'). Pairing conditional 〜ば with とおり (*練習すれば練習するとおり) is an ungrammatical combination; proportional progression requires 〜ば〜ほど (練習すれば練習するほど上手になります).",
    ('skm3-c2-ex-4', 'ば練習するうちに'): "Incorrect. While 練習するうちに ('while practicing') is a valid clause on its own, concatenating it with conditional 〜ば (*練習すれば練習するうちに) is morphologically invalid. The proportional correlative pattern is strictly [Verb-ば] [Verb-dict] ほど.",
    ('skm3-c2-ex-5', 'たびに'): "Incorrect. 〜たびに expresses invariable habitual recurrence ('every single time someone walks'). The speaker is asking the listener to do an incidental favor on one specific outing ('while you are out on your walk, could you drop this in the mailbox?'), requiring ついでに.",
    ('skm3-c2-ex-5', 'うちに'): "Incorrect. 〜うちに indicates taking advantage of a perishable temporal window before a state alters (e.g. before soup gets cold). Performing an opportunistic secondary task during a planned walk requires ついでに (散歩のついでに).",
    ('skm3-c2-ex-5', 'とおりに'): "Incorrect. 〜とおりに denotes following directions or models faithfully. An incidental secondary errand performed during a primary outing requires the opportunistic connector ついでに."
}

count = 0
for ex in exercises:
    if ex.get('bookId') == 'skm-n3' and ex.get('chapter') == 'Part 1 · Chapter 2':
        for opt in ex.get('explanation', {}).get('options', []):
            key = (ex['id'], opt.get('text'))
            if key in c2_repairs:
                opt['reason'] = c2_repairs[key]
                count += 1

print(f"Updated {count} distractor reasons in SKM N3 Chapter 2.")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved chapterExercises.json successfully!")
