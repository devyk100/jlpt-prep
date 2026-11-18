import json

# 1. Update chapterExercises.json for Lesson 19 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

has_q11 = any(q.get('id') == 'g2-l19-ex-11' for q in exercises)
if not has_q11:
    q11 = {
        'id': 'g2-l19-ex-11',
        'bookId': 'genki-2',
        'chapter': 'Lesson 19',
        'type': 'multiple-choice',
        'context': 'Public service / train announcement: Asking passengers to graciously watch their step on the train platform.',
        'question': '電車とホームの間が空いておりますので、足元に（　　）ください。',
        'translation': 'There is a gap between the train and the platform, so please watch your step.',
        'options': [
            'ご注意',
            'お注意',
            '注意して',
            'ご案内'
        ],
        'correctIndex': 0,
        'grammarPointId': 'g2-l19-o-kudasai',
        'grammarPointTitle': 'お + V-stem + ください (Polite Honorific Request: Please Graciously Do)',
        'explanation': {
            'overall': 'For compound suru-verbs (Chinese-origin Sino-Japanese nouns), the honorific request prefix is ご- rather than お-. Thus, 注意する becomes ご注意ください (Please be careful / watch your step).',
            'options': [
                {
                    'text': 'ご注意',
                    'isCorrect': True,
                    'reason': 'Correct. Sino-Japanese suru-noun 注意 takes the honorific prefix ご- to form ご注意ください.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'お注意',
                    'isCorrect': False,
                    'reason': 'Incorrect. お- is used with native Japanese wago verbs (お使いください), whereas Sino-Japanese nouns use ご-.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '注意して',
                    'isCorrect': False,
                    'reason': 'Incorrect. 注意してください is standard te-kudasai, not the formal honorific announcement form ご〜ください.',
                    'trapCategory': 'register'
                },
                {
                    'text': 'ご案内',
                    'isCorrect': False,
                    'reason': 'Incorrect. 案内 means guidance/information, which does not fit the context of watching one\'s footing.',
                    'trapCategory': 'vocabulary'
                }
            ]
        },
        'hint': 'What honorific prefix is used with Sino-Japanese suru-verbs in respectful requests: お- or ご-?'
    }
    exercises.append(q11)

has_q12 = any(q.get('id') == 'g2-l19-ex-12' for q in exercises)
if not has_q12:
    q12 = {
        'id': 'g2-l19-ex-12',
        'bookId': 'genki-2',
        'chapter': 'Lesson 19',
        'type': 'multiple-choice',
        'context': 'Logical expectation about office attendance: Deducting that Mr. Suzuki is supposed to be off work today because his schedule says so.',
        'question': '鈴木さんはカレンダーに「有休」と書いてあったから、今日は（　　）はずです。',
        'translation': 'Suzuki-san wrote "paid leave" on the calendar, so he is supposed to be off work today.',
        'options': [
            '休み',
            '休みな',
            '休みの',
            '休むの'
        ],
        'correctIndex': 2,
        'grammarPointId': 'added-g2-19-33',
        'grammarPointTitle': '〜はずです',
        'explanation': {
            'overall': 'When attaching 〜はずです to a noun, the particle の is mandatory between the noun and はず: Noun + の + はずです (e.g. 休みのはずです: supposed to be off work; 日本人のはずです: supposed to be Japanese).',
            'options': [
                {
                    'text': '休みの',
                    'isCorrect': True,
                    'reason': 'Correct. Nouns require の before はずです: [Noun] + のはずです.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '休み',
                    'isCorrect': False,
                    'reason': 'Incorrect. Nouns cannot attach directly to はず without の (*休みはず is ungrammatical).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '休みな',
                    'isCorrect': False,
                    'reason': 'Incorrect. な is used for な-adjectives (元気なはず), not nouns like 休み.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '休むの',
                    'isCorrect': False,
                    'reason': 'Incorrect. Verbs attach directly in short form without の (休むはずです, not 休むの).',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'What connecting particle is required when a noun precedes はずです?'
    }
    exercises.append(q12)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for Lesson 19!')

# 2. Enrich base-reviewed.json for Lesson 19 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. g2-l19-sonkeigo-verbs
c = card_map.get('g2-l19-sonkeigo-verbs')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 19'
    c['nuance'] = (
        'Honorific speech (尊敬語 sonkeigo) bestows honor upon, or exalts, the person performing an activity (used when speaking about superiors, teachers, customers, or guests; NEVER used to describe one\'s own actions). '
        'SPECIAL HONORIFIC VERBS (Genki II Table p. 164): '
        '・行く・来る・いる → いらっしゃる (long form: いらっしゃいます; て-form: いらっしゃって) '
        '・食べる・飲む → 召し上がる (めしあがります) '
        '・くれる → くださる (くださいます; request imperative: ください) '
        '・する → なさる (なさいます) '
        '・寝る → お休みになる (おやすみになります) '
        '・見る → ご覧になる (ごらんになります) '
        '・言う → おっしゃる (おっしゃいます) '
        '・〜ている → 〜ていらっしゃる (〜ていらっしゃいます) '
        'IRREGULAR CONJUGATIONS NOTE: いらっしゃる, おっしゃる, なさる, くださる conjugate irregularly in their polite long forms: they take -i instead of -ri before -masu (いらっしゃいます, おっしゃいます, なさいます, くださいます). '
        'FOOTNOTE 1 (COMPOUND VERBS): Special verbs also substitute into compound verbs ending with 来る: 持ってくる → 持っていらっしゃる, 連れてくる → 連れていらっしゃる. '
        'REGULAR HONORIFIC FORMULA (p. 165): '
        'For verbs without dedicated special forms: お + verb stem + になる (e.g. 先生は今朝の新聞をお読みになりましたか: Did the professor read this morning\'s paper?; お帰りになる, お話しになる). '
        'RESTRICTIONS: '
        '(1) One-syllable stem verbs (見る, 寝る, 出る) cannot use the regular お〜になる formula (special verbs ご覧になる, お休みになる must be used). '
        '(2) Suru-compound verbs use ご〜なさる or ご〜になる (ご案内になる, ご案内なさる).'
    )
    c['keyTakeaway'] = '尊敬語 exalts the actions of respected subjects (teachers/clients), NEVER oneself. Special verbs: いらっしゃる, 召し上がる, おっしゃる, なさる, ご覧になる, お休みになる, くださる. Regular formula: お + V-stem + になる. Never use on 1-syllable stems.'
    c['connection'] = 'Special honorific verbs OR お + V-stem + になる / ご + Noun + になる (subject は/が)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 19, Grammar 1, printed pp. 164-165 (PDF pp. 172-173).'

# 2. g2-l19-o-kudasai
c = card_map.get('g2-l19-o-kudasai')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 19'
    c['nuance'] = (
        'お + verb stem + ください expresses a respectful request or polite advice to an honored person ("please do... graciously"). '
        'It is much more respectful and formal than the standard 〜てください, and is the standard formula used in public announcements, hospitality, reception desks, and store attendants. '
        'FORMATION: '
        '(1) Native Japanese (wago) verbs: お + verb masu-stem + ください (切符をお取りください: Please take your ticket; どうぞお入りください: Please come in; お使いください: Please use it; 少々お待ちください: Please wait a moment). '
        '(2) Sino-Japanese (kango / suru-compounds): ご + Noun + ください (ご注意ください: Please be careful / watch out; ご覧ください: Please take a look; ご案内ください; ご遠慮ください: Please refrain). '
        'RESTRICTION: Does not apply to 1-syllable stem verbs without compound stems (e.g. *お見ください is forbidden; use ご覧ください).'
    )
    c['keyTakeaway'] = 'Respectful request / advice: Wago: お + V-stem + ください (お取りください). Suru-compounds: ご + Noun + ください (ご注意ください, ご覧ください). Formal public/business register.'
    c['connection'] = 'お + V-stem + ください | ご + Noun + ください'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 19, Grammar 2, printed p. 166 (PDF p. 174).'

# 3. added-g2-19-32 (~てくれてありがとう・〜てよかった)
c = card_map.get('added-g2-19-32')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 19'
    c['nuance'] = (
        'This section encompasses two closely related expressions of gratitude and emotional relief: '
        '(1) Gratitude for Specific Favors: 〜てくれてありがとう / 〜てくださってありがとうございました. '
        'Used to thank someone for performing a specific action: '
        '・Casual (peers, close friends, family): V-てくれてありがとう (手伝ってくれてありがとう: Thanks for helping me). '
        '・Polite Honorific (superiors, teachers, non-intimate associates): V-てくださって、ありがとうございました (推薦状を書いてくださって、ありがとうございました: Thank you for graciously writing a recommendation letter for me). '
        '・Negative favor ("thank you for not doing"): 〜ないでくれてありがとう / 〜ないでくださってありがとうございました. '
        '(2) Emotional Relief / Being Glad: 〜てよかった. '
        'Expresses retrospective relief or happiness that an event occurred or that an action was taken: '
        '・Affirmative: V-てよかった (日本語を勉強してよかったです: I am glad that I studied Japanese). '
        '・Negative: V-なくてよかった (きのう雨が降らなくてよかったです: I am glad that it did not rain yesterday; 行かなくてよかった: I am glad I did not go).'
    )
    c['keyTakeaway'] = 'Gratitude: Casual: V-てくれてありがとう. Polite/Superior: V-てくださってありがとうございました. Relief: V-てよかった (glad it happened) vs V-なくてよかった (glad it didn\'t happen).'
    c['connection'] = 'V-て + くれてありがとう / くださってありがとうございました | V-てよかった / V-なくてよかった'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 19, Grammar 3 & 4, printed p. 167 (PDF p. 175).'

# 4. added-g2-19-33 (~はずです)
c = card_map.get('added-g2-19-33')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 19'
    c['nuance'] = (
        '〜はずです expresses an expectation or logical deduction based on surrounding evidence, circumstances, or common sense: "supposed to be the case / should logically happen / must be". '
        'The speaker believes something is true or likely, though lacking 100% conclusive proof (今日日曜だから、銀行は閉まっているはずです: Banks must be closed, because today is Sunday). '
        'FORMATION (Attached to Short Forms): '
        '・Verbs: Short form (present/past, aff/neg) + はずです (届くはずです / 来ないはずです / 買ったはずです). '
        '・い-adjectives: Short form + はずです (面白いはずです / 寒くないはずです). '
        '・な-adjectives: な-adjective + な + はずです (元気なはずです: supposed to be healthy; 親切なはずです). '
        '・Nouns: Noun + の + はずです (日本人のはずです: supposed to be Japanese; 休みのはずです: supposed to be off). '
        'PRAGMATIC CONSTRAINTS: '
        '(1) Cannot be used for moral duty or legal obligation (e.g. "you are supposed to obey rules" must use べき or なければならない, not はず). '
        '(2) Strong negative conviction: 〜はずがない / 〜はずはありません (cannot possibly be the case).'
    )
    c['keyTakeaway'] = '〜はずです: Logical expectation based on evidence ("supposed to be / should be"). Formations: Verb-short / い-adj + はずです; な-adj + なはずです; Noun + のはずです. Cannot express moral duty.'
    c['connection'] = 'Short form predicate (+ な for な-adj, + の for Noun) + はずです'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 19, Grammar 5, printed p. 168 (PDF p. 176).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 4 Lesson 19 cards in base-reviewed.json!')

# 3. Add 4 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing Lesson 19 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Genki II (3rd Ed.)' and r.get('sourceSection') == 'Lesson 19')]

l19_entries = [
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 19',
        'exactPrintedPages': 'pp. 164-165',
        'exactPdfPages': 'pp. 172-173',
        'grammarItem': '尊敬語 (Honorific Speech: Special Verbs & Regular Formulas)',
        'instructionalDetails': 'Exalts actions of superiors/guests; special verbs (いらっしゃる, 召し上がる, おっしゃる, なさる, ご覧になる, お休みになる, くださる); irregular -i polite endings (いらっしゃいます); compound verbs with -kuru (持っていらっしゃる); regular formula お + V-stem + になる; restriction against 1-syllable stems (見る, 寝る).',
        'cardId': 'g2-l19-sonkeigo-verbs',
        'exampleCount': 4,
        'exampleIds': ['g2-l19-sonkeigo-verbs::s-g2-19-1', 'g2-l19-sonkeigo-verbs::genki2-use-examples-64', 'g2-l19-sonkeigo-verbs::genki2-use-examples-65', 'g2-l19-sonkeigo-verbs::genki2-use-examples-66'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 164-165 (PDF pp. 172-173, g2_p172_printed164.png, g2_p173_printed165.png). Verified special verbs table, irregular -i conjugations note, Footnote 1 compound verbs rule, and regular お〜になる formula.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 19',
        'exactPrintedPages': 'p. 166',
        'exactPdfPages': 'p. 174',
        'grammarItem': 'お + V-stem + ください (Polite Honorific Request / Respectful Advice)',
        'instructionalDetails': 'Polite requests/advice in business/public announcements; native wago verbs use お + V-stem + ください (お取りください, お入りください); Sino-Japanese suru-compounds use ご + Noun + ください (ご注意ください, ご覧ください); restriction on 1-syllable stems.',
        'cardId': 'g2-l19-o-kudasai',
        'exampleCount': 3,
        'exampleIds': ['g2-l19-o-kudasai::s-g2-19-2', 'g2-l19-o-kudasai::genki2-use-examples-67', 'g2-l19-o-kudasai::genki2-use-examples-68'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 166 (PDF p. 174, g2_p174_printed166.png). Verified polite request formula お + V-stem + ください and Sino-Japanese prefix ご- rule.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 19',
        'exactPrintedPages': 'p. 167',
        'exactPdfPages': 'p. 175',
        'grammarItem': '〜てくれてありがとう・〜てよかった (Gratitude & Emotional Relief)',
        'instructionalDetails': 'Expressing gratitude for actions: casual 〜てくれてありがとう vs polite/superior 〜てくださってありがとうございました (negative: 〜ないでくれて); expressing emotional relief: affirmative 〜てよかった (glad it happened) vs negative 〜なくてよかった (glad it did not happen).',
        'cardId': 'added-g2-19-32',
        'exampleCount': 4,
        'exampleIds': ['added-g2-19-32-example', 'added-g2-19-32::genki2-use-examples-69', 'added-g2-19-32::genki2-use-examples-70', 'added-g2-19-32::genki2-use-examples-71'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 167 (PDF p. 175, g2_p175_printed167.png). Verified gratitude hierarchy (〜てくれてありがとう vs 〜てくださってありがとうございました) and relief pairs (〜てよかった vs 〜なくてよかった).'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 19',
        'exactPrintedPages': 'pp. 168-169',
        'exactPdfPages': 'pp. 176-177',
        'grammarItem': '〜はずです (Logical Expectation: Supposed to Be)',
        'instructionalDetails': 'Belief/deduction based on evidence/common sense; short forms + はずです; な-adj + なはずです; Noun + のはずです; prohibition on moral/legal duty contexts (must use べき); negative conviction 〜はずがない / はずはない.',
        'cardId': 'added-g2-19-33',
        'exampleCount': 4,
        'exampleIds': ['added-g2-19-33-example', 'added-g2-19-33::genki2-use-examples-72', 'added-g2-19-33::genki2-use-examples-73', 'added-g2-19-33::genki2-use-examples-74'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 168-169 (PDF pp. 176-177, g2_p176_printed168.png, g2_p177_printed169.png). Verified logical expectation formation, な/の particle connections, and moral duty prohibition.'
    }
]

matrix.extend(l19_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Certified Lesson 19 in source coverage matrix! Total certified rows: {len(matrix)}')
