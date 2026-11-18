import json

# 1. Update chapterExercises.json for Lesson 21 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

has_q11 = any(q.get('id') == 'g2-l21-ex-11' for q in exercises)
if not has_q11:
    q11 = {
        'id': 'g2-l21-ex-11',
        'bookId': 'genki-2',
        'chapter': 'Lesson 21',
        'type': 'multiple-choice',
        'context': 'Party preparation: Observing that the dining plates have already been deliberately arranged on the table in advance for guests.',
        'question': 'テーブルの上には、もうお皿がちゃんと（　　）。',
        'translation': 'On the table, the plates have already been properly arranged.',
        'options': [
            '並べてあります',
            '並んでいます',
            '並べています',
            '並びました'
        ],
        'correctIndex': 0,
        'grammarPointId': 'g2-l21-te-aru',
        'grammarPointTitle': '〜てある (Transitive Verb Resultant State: Deliberately Prepared)',
        'explanation': {
            'overall': 'When a resultant state was created intentionally by someone by way of advance preparation, transitive verb in te-form + ある (並べてあります) is used. In contrast, 並んでいます (intransitive + ている) describes a spontaneous state without highlighting deliberate human preparation, while 並べています describes an action currently in progress.',
            'options': [
                {
                    'text': '並べてあります',
                    'isCorrect': True,
                    'reason': 'Correct. Transitive verb 並べる + てある describes a deliberately prepared resultant state.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '並んでいます',
                    'isCorrect': False,
                    'reason': 'Incorrect. Intransitive 並ぶ + ている describes natural alignment without conveying deliberate preparatory intention.',
                    'trapCategory': 'nuance'
                },
                {
                    'text': '並べています',
                    'isCorrect': False,
                    'reason': 'Incorrect. Transitive verb + ている denotes an ongoing action in progress (currently placing plates), not a completed resultant state.',
                    'trapCategory': 'aspect'
                },
                {
                    'text': '並びました',
                    'isCorrect': False,
                    'reason': 'Incorrect. Past tense intransitive merely states an event finished in the past without describing the persisting resultant state.',
                    'trapCategory': 'tense'
                }
            ]
        },
        'hint': 'Which structure describes an intentional resultant state resulting from advance human preparation using a transitive verb?'
    }
    exercises.append(q11)

has_q12 = any(q.get('id') == 'g2-l21-ex-12' for q in exercises)
if not has_q12:
    q12 = {
        'id': 'g2-l21-ex-12',
        'bookId': 'genki-2',
        'chapter': 'Lesson 21',
        'type': 'multiple-choice',
        'context': 'Confidential request: Asking a coworker not to tell anyone about a private matter.',
        'question': 'これは秘密ですから、だれにも（　　）ほしいです。',
        'translation': 'This is a secret, so I want you not to tell anyone.',
        'options': [
            '言わないで',
            '言わなくて',
            '言って',
            '言わない'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-g2-21-39',
        'grammarPointTitle': '形容詞＋する・〜てほしい',
        'explanation': {
            'overall': 'To express that you want someone NOT to do something, use V-ないで + ほしい (言わないでほしい). V-なくて is ungrammatical before ほしい (*言わなくてほしい is incorrect).',
            'options': [
                {
                    'text': '言わないで',
                    'isCorrect': True,
                    'reason': 'Correct. The negative wish pattern is V-ないで + ほしい (言わないでほしい).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '言わなくて',
                    'isCorrect': False,
                    'reason': 'Incorrect. 〜なくて expresses reasons/causes, not negative desire (*言わなくてほしい is ungrammatical).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '言って',
                    'isCorrect': False,
                    'reason': 'Incorrect. 言ってほしい means "I want you to tell", which contradicts the secret context.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '言わない',
                    'isCorrect': False,
                    'reason': 'Incorrect. Bare negative short form without で cannot connect directly to ほしい.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'How do you form the negative wish "I want you NOT to do..." with ほしい?'
    }
    exercises.append(q12)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for Lesson 21!')

# 2. Enrich base-reviewed.json for Lesson 21 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. added-g2-21-38 (受身)
c = card_map.get('added-g2-21-38')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 21'
    c['nuance'] = (
        'Passive sentences (受身文 ukemi-bun) describe an event from the perspective of the recipient/victim. '
        'In Japanese, passive is very frequently used to express adversity or inconvenience caused by someone else\'s action ("suffering passive" / 迷惑受身). '
        'CONJUGATION PARADIGM (pp. 210-211): '
        '・Ru-verbs: drop -ru + rareru (食べる → 食べられる; 見る → 見られる; identical in form to potential verbs). '
        '・U-verbs: drop final -u, add -areru (飲む → 飲まれる; 待つ → 待たれる; 使う → 使われる; distinct from potential -eru). '
        '・Irregular: くる → こられる, する → される. '
        'Passive verbs conjugate regularly as ru-verbs (食べられた, 食べられない, etc.). '
        'THREE PASSIVE STRUCTURES: '
        '(1) Direct Passive: [Victim は] [Agent に] V-passive (私は先生に怒られました: I was scolded by the teacher). '
        '(2) Possessive / Affective Passive: [Victim は] [Agent に] [Belonging を] V-passive (私は友だちに車を使われました: A friend used my car on me; 泥棒に財布を盗まれました; 足を踏まれました). '
        '(3) Intransitive Adversity Passive: [Victim は] [Agent/Phenomenon に] V(intransitive)-passive (雨に降られました: I got rained on; 赤ちゃんに泣かれました: The baby cried on me). '
        'NEUTRAL/FAVORABLE PASSIVES (p. 212): Relatively few verbs express neutral/positive passive (誘われる: be invited; 紹介される: be introduced; 尊敬される: be respected).'
    )
    c['keyTakeaway'] = 'Passive: Ru: -rareru, U: -areru, くる→こられる, する→される. Conjugates as ru-verb. Used heavily for adversity ("suffering passive"): [Victim は] [Villain に] ([Item を]) V-passive. Rain: 雨に降られた.'
    c['connection'] = 'Ru: -rareru | U: -areru | くる→こられる | する→される | [Victim は] [Agent に] [Item を] V-passive'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 21, Grammar 1, printed pp. 210-212 (PDF pp. 218-220).'

# 2. g2-l21-te-aru (~てある)
c = card_map.get('g2-l21-te-aru')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 21'
    c['nuance'] = (
        '〜てある describes a resultant state that has been brought about intentionally by someone earlier as advance preparation, and that remains currently observable ("has been done and remains ready"). '
        'FORMATION: Transitive verb in te-form + ある (レストランの予約がしてあります: A restaurant reservation has been made; 窓が開けてあります: The window has been kept open; カレンダーに予定が書いてあります: The schedule has been written on the calendar). '
        'CASE MARKING: The direct object of the original transitive verb is usually marked with が (or topicalized with は), rather than を: [Item が] V(transitive)-てある. '
        'ASPECTUAL THREE-WAY DISTINCTION: '
        '(1) Transitive + ている: Action in progress (窓を開けています: currently in the middle of opening window). '
        '(2) Intransitive + ている: Spontaneous resultant state (窓が開いています: the window is open, no agent implied). '
        '(3) Transitive + てある: Intentional resultant state (窓が開けてあります: the window has been opened and left that way on purpose).'
    )
    c['keyTakeaway'] = 'Transitive V-て + ある = intentional resultant state ("has been done for a purpose and remains ready"). Object takes が (予約がしてある). Contrasts with intransitive + ている (開いている vs 開けてある).'
    c['connection'] = '[Noun が] V(transitive)-て + ある / あります'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 21, Grammar 2, printed p. 213 (PDF p. 221).'

# 3. g2-l21-aida-vs-aidani (~間に vs 〜間)
c = card_map.get('g2-l21-aida-vs-aidani')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 21'
    c['nuance'] = (
        'Both 〜間に and 〜間 express temporal relations during an ongoing background state A, but they differ fundamentally in aspect: '
        '(1) 〜間に (Momentary Event / In the Middle of): Event B is of short duration, beginning and ending inside the temporal span of A ("while / during"). '
        '・[A (V-ている / Noun の)] 間に、[B (momentary action)] '
        '・両親が日本にいる間に、京都へ連れていきたいです (I want to take my parents to Kyoto while they are in Japan). '
        '・留守の間に友だちが来ました (A friend came while I was out). '
        '・お風呂に入っている間に電話がありました (The phone rang while I was in the bath). '
        '(2) 〜間 (Continuous Event / Throughout the Entire Duration): Event B extends throughout the entire duration of activity A without interruption ("the whole time that / during all of"). '
        '・[A (V-ている / Noun の)] 間、[B (continuous action/state)] '
        '・留守の間、ずっと雨が降っていました (It rained continuously the whole time I was away). '
        '・子供が寝ている間、本を読んでいました (I read a book the whole time the child was sleeping).'
    )
    c['keyTakeaway'] = '〜間に = momentary event B occurs in the middle of ongoing state A (留守の間に友だちが来た). 〜間 = continuous event B extends throughout the entire duration of A (寝ている間、ずっと本を読んだ).'
    c['connection'] = '[V-ている / Noun の] 間に (momentary B) | [V-ている / Noun の] 間 (continuous B)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 21, Grammar 3, printed p. 214 (PDF p. 222).'

# 4. added-g2-21-39 (形容詞＋する・〜てほしい)
c = card_map.get('added-g2-21-39')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 21'
    c['nuance'] = (
        'This section encompasses two grammatical patterns: '
        '(1) Adjective + する ("to make something [adjective] / adjust deliberately", p. 215): '
        '・い-adjectives: drop final い, add く + する (冷たくする: make cold; 安くする: make cheaper; テレビの音を小さくする: turn down TV). '
        '・な-adjectives: add に + する (静かにする: make quiet; 部屋をきれいにする: clean the room). '
        '・Contrast: 〜くなる / 〜になる describes natural spontaneous change ("becomes"), whereas 〜くする / 〜にする describes deliberate agentive alteration ("makes it so"). '
        '(2) 〜てほしい ("want someone else to do something", p. 215): '
        '・[Person に] V-てほしい (私はルームメイトに部屋を掃除してほしいです: I want my roommate to clean the room; 先生に推薦状を書いてほしいです). '
        '・Negative wish ("want someone NOT to do"): [Person に] V-ないでほしい (言わないでほしい: I want you not to tell; 来ないでほしい: I want you not to come). Alternatively: 〜てほしくない.'
    )
    c['keyTakeaway'] = 'Adj+する: い-adj + くする / な-adj + にする = deliberately make/adjust. 〜てほしい: [Person に] V-てほしい = want someone to do. Negative wish: [Person に] V-ないでほしい.'
    c['connection'] = 'い-adj(drop い) + くする | な-adj + にする | [Person に] V-てほしい / V-ないでほしい'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 21, Grammar 4 & 5, printed p. 215 (PDF p. 223).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 4 Lesson 21 cards in base-reviewed.json!')

# 3. Add 4 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing Lesson 21 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Genki II (3rd Ed.)' and r.get('sourceSection') == 'Lesson 21')]

l21_entries = [
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 21',
        'exactPrintedPages': 'pp. 210-212',
        'exactPdfPages': 'pp. 218-220',
        'grammarItem': '受身 (Passive Sentences: Direct, Suffering, and Adversity Passives)',
        'instructionalDetails': 'Ru: -rareru, U: -areru, くる→こられる, する→される; conjugates as ru-verb; 3 passive types: direct passive, possessive/suffering passive ([Victim は] [Villain に] [Belonging を] V-passive), and intransitive adversity passive (雨に降られた); neutral/positive passives (誘われる, 尊敬される).',
        'cardId': 'added-g2-21-38',
        'exampleCount': 4,
        'exampleIds': ['added-g2-21-38-example', 'added-g2-21-38::genki2-use-examples-87', 'added-g2-21-38::genki2-use-examples-88', 'added-g2-21-38::genki2-use-examples-89'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 210-212 (PDF pp. 218-220, g2_p218_printed210.png to g2_p220_printed212.png). Verified passive conjugation paradigm, adversity/suffering passive mechanics, and neutral passive examples.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 21',
        'exactPrintedPages': 'p. 213',
        'exactPdfPages': 'p. 221',
        'grammarItem': '〜てある (Transitive Verb Resultant State: Deliberately Prepared)',
        'instructionalDetails': 'V(transitive)-て + ある for intentional resultant state prepared in advance; entity takes が (予約がしてある, 窓が開けてある); aspectual distinction: transitive + ている (action in progress) vs intransitive + ている (natural state) vs transitive + てある (intentional prepared state).',
        'cardId': 'g2-l21-te-aru',
        'exampleCount': 3,
        'exampleIds': ['g2-l21-te-aru::s-g2-21-1', 'g2-l21-te-aru::genki2-use-examples-90', 'g2-l21-te-aru::genki2-use-examples-91'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 213 (PDF p. 221, g2_p221_printed213.png). Verified transitive resultant state formation, particle が marking, and contrast with 〜ておく and intransitive 〜ている.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 21',
        'exactPrintedPages': 'p. 214',
        'exactPdfPages': 'p. 222',
        'grammarItem': '〜間に vs 〜間 (During a Moment vs Throughout the Entire Duration)',
        'instructionalDetails': '〜間に marks momentary event B occurring within duration A (留守の間に友だちが来た); 〜間 marks continuous event B extending throughout the entire duration of A (寝ている間、ずっと本を読んだ); formation with V-ている and Noun + の.',
        'cardId': 'g2-l21-aida-vs-aidani',
        'exampleCount': 3,
        'exampleIds': ['g2-l21-aida-vs-aidani::s-g2-21-2', 'g2-l21-aida-vs-aidani::genki2-use-examples-92', 'g2-l21-aida-vs-aidani::genki2-use-examples-93'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 214 (PDF p. 222, g2_p222_printed214.png). Verified aspectual dichotomy between momentary 間に and continuous 間 with authentic textbook examples.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 21',
        'exactPrintedPages': 'p. 215',
        'exactPdfPages': 'p. 223',
        'grammarItem': '形容詞＋する・〜てほしい (Deliberate Adjustment & Wanting Someone to Do)',
        'instructionalDetails': 'い-adj drop い + くする / な-adj + にする (deliberately make/alter); contrast with spontaneous なる; [Person に] V-てほしい (want person to do); negative wish [Person に] V-ないでほしい (want person not to do).',
        'cardId': 'added-g2-21-39',
        'exampleCount': 4,
        'exampleIds': ['added-g2-21-39-example', 'added-g2-21-39::genki2-use-examples-94', 'added-g2-21-39::genki2-use-examples-95', 'added-g2-21-39::genki2-use-examples-96'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 215 (PDF p. 223, g2_p223_printed215.png). Verified adjective + する alterations and 〜てほしい / 〜ないでほしい person marking with に.'
    }
]

matrix.extend(l21_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Certified Lesson 21 in source coverage matrix! Total certified rows: {len(matrix)}')
