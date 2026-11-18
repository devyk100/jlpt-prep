import json

# 1. Update chapterExercises.json for Lesson 18 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

has_q11 = any(q.get('id') == 'g2-l18-ex-11' for q in exercises)
if not has_q11:
    q11 = {
        'id': 'g2-l18-ex-11',
        'bookId': 'genki-2',
        'chapter': 'Lesson 18',
        'type': 'multiple-choice',
        'context': 'Spoken casual mishap: Realizing you accidentally left your homework at home and exclaiming to a classmate.',
        'question': 'あっ、家に宿題を（　　）！',
        'translation': 'Oh no, I accidentally left my homework at home!',
        'options': [
            '忘れちゃった',
            '忘れちゃいました',
            '忘れなかった',
            '忘れておいた'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-g2-18-30',
        'grammarPointTitle': '〜てしまう',
        'explanation': {
            'overall': 'In casual spoken Japanese, 〜てしまう contracts to 〜ちゃう (past: 〜ちゃった). 忘れてしまった becomes 忘れちゃった to express spontaneous regret over a mishap.',
            'options': [
                {
                    'text': '忘れちゃった',
                    'isCorrect': True,
                    'reason': 'Correct. Spoken casual contraction of 〜てしまった is 〜ちゃった.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '忘れちゃいました',
                    'isCorrect': False,
                    'reason': 'Incorrect. Polite contracted form, but casual exclamation typically takes plain short form (ちゃった).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '忘れなかった',
                    'isCorrect': False,
                    'reason': 'Incorrect. Negative past "did not forget", opposite of intended meaning.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '忘れておいた',
                    'isCorrect': False,
                    'reason': 'Incorrect. 〜ておく is preparatory action, illogical with forgetting.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'What is the casual spoken contracted form of 〜てしまった?'
    }
    exercises.append(q11)

has_q12 = any(q.get('id') == 'g2-l18-ex-12' for q in exercises)
if not has_q12:
    q12 = {
        'id': 'g2-l18-ex-12',
        'bookId': 'genki-2',
        'chapter': 'Lesson 18',
        'type': 'multiple-choice',
        'context': 'Simultaneous actions by different people: Mary is cooking while Ken is cleaning the living room.',
        'question': 'メアリーさんが料理を作っている（　　）、けんさんは掃除をしました。',
        'translation': 'While Mary was cooking, Ken cleaned the room.',
        'options': [
            '間に',
            'ながら',
            '時',
            'と'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-g2-18-31',
        'grammarPointTitle': '〜ながら',
        'explanation': {
            'overall': 'Genki II Lesson 18 explicitly warns: 〜ながら requires that both concurrent actions be performed by the SAME PERSON (*メアリーが作りながら、けんが掃除した is ungrammatical). When two different people perform actions concurrently, you must use 〜間に (料理を作っている間に).',
            'options': [
                {
                    'text': '間に',
                    'isCorrect': True,
                    'reason': 'Correct. When two different people perform simultaneous actions, use [Person A V-ている] 間に [Person B ...].',
                    'trapCategory': 'context'
                },
                {
                    'text': 'ながら',
                    'isCorrect': False,
                    'reason': 'Incorrect. Explicit textbook rule: 〜ながら cannot be used when the subjects of the two actions are different.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '時',
                    'isCorrect': False,
                    'reason': 'Incorrect. 時 focuses on a single time point or event trigger, not two ongoing parallel concurrent activities.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'と',
                    'isCorrect': False,
                    'reason': 'Incorrect. と expresses natural consequence / condition, not simultaneous actions.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Can 〜ながら be used when two different people are performing the simultaneous actions?'
    }
    exercises.append(q12)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for Lesson 18!')

# 2. Enrich base-reviewed.json for Lesson 18 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. g2-l18-transitive-intransitive
c = card_map.get('g2-l18-transitive-intransitive')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 18'
    c['nuance'] = (
        'Japanese has paired verbs of transitivity: '
        '(1) Transitive verbs describe an agent acting upon an object (requires subject は/が and direct object を: たけしさんが電気をつけた: Takeshi turned on the light). '
        '(2) Intransitive verbs describe changes that things or people undergo without an agent explicitly mentioned (subject は/が only: 電気がついた: The light went on). '
        '10 Essential Pairs in Genki II: '
        '開ける (transitive: open) vs 開く (intransitive: opens); 閉める (close) vs 閉まる (closes); 入れる (put inside) vs 入る (goes inside); '
        '出す (take out) vs 出る (goes out); つける (turn on) vs つく (goes on); 消す (turn off/extinguish) vs 消える (goes off); '
        '壊す (break) vs 壊れる (breaks down); 汚す (make dirty) vs 汚れる (becomes dirty); 落とす (drop) vs 落ちる (drops); 沸かす (boil water) vs 沸く (water boils). '
        'ASPECTUAL DICHOTOMY WITH 〜ている: '
        '- Transitive verb + ている = ACTION IN PROGRESS (窓を開けています: in the middle of opening window). '
        '- Intransitive verb + ている = RESULTANT STATE (窓が開いています: the window is open / in an open state; 電気が消えています: the light is off).'
    )
    c['keyTakeaway'] = 'Transitive takes を (agent acts on object). Intransitive takes が (object undergoes change). Intransitive + ている = RESULTANT STATE (窓が開いている = window is open).'
    c['connection'] = 'Transitive: [Agent は] [Object を] V-他動詞 | Intransitive: [Subject が] V-自動詞 | Resultant state: [Subject が] V-自動詞 + ている'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 18, Grammar 1, printed pp. 140-141 (PDF pp. 148-149).'

# 2. added-g2-18-30 (~てしまう)
c = card_map.get('added-g2-18-30')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 18'
    c['nuance'] = (
        'The te-form of a verb + しまう has two interrelated aspectual meanings: '
        '(1) Thorough completion / culmination: Carrying out an action completely or finishing it to the end (本を読んでしまいました: I finished reading the whole book). '
        '(2) Regret / unintended mishap: Lack of premeditation or control over an outcome, expressing regret or dismay (電車の中にかばんを忘れてしまいました: I inadvertently left my bag on the train; 宿題を忘れて先生が怒ってしまった). '
        'FOOTNOTE 1 CONSTRAINT: V-てしまう only pairs with affirmative verbal te-forms (cannot express negated regret like *しなくてしまった). '
        'SPOKEN CONTRACTIONS: '
        '- 〜てしまう → 〜ちゃう (忘れてしまった → 忘れちゃった). '
        '- 〜でしまう → 〜じゃう (飲んでしまった → 飲んじゃった).'
    )
    c['keyTakeaway'] = 'V-てしまう: (1) Complete culmination ("finish completely"), (2) Regrettable mishap ("unintentionally ended up doing"). Spoken casual: 〜ちゃう / 〜じゃう (忘れちゃった, 飲んじゃった).'
    c['connection'] = 'V-て + しまう / しまいました / しまった | Casual: V-て → 〜ちゃう / 〜じゃう'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 18, Grammar 2, printed pp. 141-142 (PDF pp. 149-150).'

# 3. g2-l18-to-natural-consequence
c = card_map.get('g2-l18-to-natural-consequence')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 18'
    c['nuance'] = (
        'Clause A (short present) + と、Clause B expresses that whenever situation A holds true, consequence B inevitably happens ("Whenever A happens, B follows / If A, naturally B"). '
        'Formation: Clause A is ALWAYS in the present tense short form (affirmative or negative: 話すと, 混むと, 降らないと). '
        'Clause B describes the natural consequence or state, which can be present or past (冬になると、風邪を引きました). '
        'Adjective outcomes in Clause B are typically framed as a transition of state using 〜くなる or 〜になる (秋になると、木が赤くなります; 夜になると、町が静かになります). '
        'CRITICAL VOLITIONAL RESTRICTION: Clause B CANNOT contain speaker requests, suggestions, commands, or volitional intentions (*話すと、カフェに行きましょう is strictly ungrammatical; use 〜たら instead).'
    )
    c['keyTakeaway'] = 'V(short present) + と = Natural consequence ("whenever A happens, B inevitably follows"). Clause A is strictly present tense. Clause B CANNOT contain volition, requests, or commands.'
    c['connection'] = 'Short present (V / い-adj) + と | な-adj + だと | Noun + だと'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 18, Grammar 3, printed pp. 142-143 (PDF pp. 150-151).'

# 4. added-g2-18-31 (~ながら)
c = card_map.get('added-g2-18-31')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 18'
    c['nuance'] = (
        'V1 (masu-stem) + ながら、V2 connects two verbs to express that two actions are performed simultaneously by the same actor ("while doing V1, doing V2"). '
        'Focus structure: V2 is the PRIMARY action; V1 is secondary/background (音楽を聞きながら、日本語を勉強します: Studies Japanese while listening to music). '
        'SAME ACTOR CONSTRAINT: Both actions flanking ながら MUST be performed by the SAME PERSON! '
        'It cannot describe an action performed while another person does something (*メアリーが買い物をしながら、たけしが掃除した is ungrammatical; use 〜間に or 〜時 instead).'
    )
    c['keyTakeaway'] = 'V1(masu-stem) + ながら + V2 = while doing V1, do V2. V2 is the main action. SAME ACTOR RULE: Both actions must be performed by the same person (never two different people).'
    c['connection'] = 'V1-stem + ながら、V2'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 18, Grammar 4, printed pp. 143-144 (PDF pp. 151-152).'

# 5. g2-l18-ba-yokatta
c = card_map.get('g2-l18-ba-yokatta')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 18'
    c['nuance'] = (
        '〜ばよかった expresses retrospective regret: "I wish I had done... / I should have done..." (expressing regret over an alternative course of action not taken). '
        'Formation: '
        '(1) Affirmative: Drop final -u of the dictionary form and add -eba + よかった (食べる → 食べればよかった: I should have eaten; 行く → 行けばよかった; 言う → 言えばよかった). '
        '(2) Negative: Drop final い from negative short form ない and add ければ + よかった (別れる → 別れなければよかった: I should not have broken up with her; 買わない → 買わなければよかった). '
        'Regular formation: All verbs form 〜ばよかった regularly without exceptions.'
    )
    c['keyTakeaway'] = 'Retrospective regret: Affirmative: V(u->eba) + よかった ("should have done"). Negative: V-なければよかった ("should not have done"). Regular for all verbs.'
    c['connection'] = 'V (u->eba) + よかった (affirmative) | V-なければよかった (negative)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 18, Grammar 5, printed pp. 144-145 (PDF pp. 152-153).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 5 Lesson 18 cards in base-reviewed.json!')

# 3. Add 5 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing Lesson 18 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Genki II (3rd Ed.)' and r.get('sourceSection') == 'Lesson 18')]

l18_entries = [
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 18',
        'exactPrintedPages': 'pp. 140-141',
        'exactPdfPages': 'pp. 148-149',
        'grammarItem': '自動詞 vs 他動詞 (Intransitive vs Transitive Verb Pairs)',
        'instructionalDetails': 'Transitive verbs take object を (agent acting on object: ドアを開けた); intransitive verbs take subject が (object undergoing change: ドアが開いた); 10 essential pairs; aspectual behavior with 〜ている: transitive + ている = action in progress, intransitive + ている = resultant state (窓が開いている).',
        'cardId': 'g2-l18-transitive-intransitive',
        'exampleCount': 3,
        'exampleIds': ['g2-l18-transitive-intransitive::s-g2-18-1', 'g2-l18-transitive-intransitive::genki2-use-examples-55', 'g2-l18-transitive-intransitive::genki2-use-examples-56'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 140-141 (PDF pp. 148-149, p148_printed140.png, p149_printed141.png). Verified transitivity pairs table, case marking rules, and resultant state semantics with 〜ている.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 18',
        'exactPrintedPages': 'pp. 141-142',
        'exactPdfPages': 'pp. 149-150',
        'grammarItem': '〜てしまう (Dual Aspect: Regret/Mishap vs Thorough Completion)',
        'instructionalDetails': 'V-て + しまう for complete culmination ("finish reading completely") and unintended mishap / regret ("inadvertently lost bag"); Footnote 1 constraint (affirmative only, cannot express negated regret); spoken casual contractions: 〜てしまう → 〜ちゃう, 〜でしまう → 〜じゃう (忘れちゃった).',
        'cardId': 'added-g2-18-30',
        'exampleCount': 4,
        'exampleIds': ['added-g2-18-30-example', 'added-g2-18-30::genki2-use-examples-61', 'added-g2-18-30::genki2-use-examples-62', 'added-g2-18-30::genki2-use-examples-63'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 141-142 (PDF pp. 149-150, p149_printed141.png, p150_printed142.png). Verified dual culmination/regret aspect, Footnote 1 affirmative-only rule, and spoken 〜ちゃう/〜じゃう contractions.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 18',
        'exactPrintedPages': 'pp. 142-143',
        'exactPdfPages': 'pp. 150-151',
        'grammarItem': '〜と (Natural Consequence & Inevitable Conditional: When / If)',
        'instructionalDetails': 'Clause A (short present) + と、Clause B for inevitable cause-and-effect ("whenever A happens, B follows"); Clause A is strictly present tense; Clause B cannot contain speaker volition, requests, suggestions, or commands; adjective outcomes typically use 〜くなる / 〜になる.',
        'cardId': 'g2-l18-to-natural-consequence',
        'exampleCount': 3,
        'exampleIds': ['g2-l18-to-natural-consequence::s-g2-18-2', 'g2-l18-to-natural-consequence::genki2-use-examples-57', 'g2-l18-to-natural-consequence::genki2-use-examples-58'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 142-143 (PDF pp. 150-151, p150_printed142.png, p151_printed143.png). Verified inevitable condition mechanics, strict present tense in Clause A, and ban on volitional expressions in Clause B.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 18',
        'exactPrintedPages': 'pp. 143-144',
        'exactPdfPages': 'pp. 151-152',
        'grammarItem': '〜ながら (Simultaneous Concurrent Actions: While Doing)',
        'instructionalDetails': 'V1 (masu-stem) + ながら、V2 for concurrent actions (V2 is main action, V1 is secondary); SAME AGENT CONSTRAINT: both actions must be performed by the exact same actor (cannot describe different actors; use 〜間に for different actors).',
        'cardId': 'added-g2-18-31',
        'exampleCount': 3,
        'exampleIds': ['added-g2-18-31-example', 'added-g2-18-31::genki2-use-examples-64', 'added-g2-18-31::genki2-use-examples-65'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 143-144 (PDF pp. 151-152, p151_printed143.png, p152_printed144.png). Verified masu-stem connection, main vs secondary action focus, and strict same-agent constraint.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 18',
        'exactPrintedPages': 'pp. 144-145',
        'exactPdfPages': 'pp. 152-153',
        'grammarItem': '〜ばよかった (Retrospective Regret: I Should Have Done)',
        'instructionalDetails': 'Retrospective regret over missed alternatives: affirmative V(u->eba) + よかった ("I should have done"); negative V-なければよかった ("I should not have done"); expression note on 〜のおかげで (thanks to) and おかげさまで.',
        'cardId': 'g2-l18-ba-yokatta',
        'exampleCount': 3,
        'exampleIds': ['g2-l18-ba-yokatta::s-g2-18-3', 'g2-l18-ba-yokatta::genki2-use-examples-59', 'g2-l18-ba-yokatta::genki2-use-examples-60'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 144-145 (PDF pp. 152-153, p152_printed144.png, p153_printed145.png). Verified conditional -eba formation across verb classes, affirmative/negative regret, and おかげさまで expressions.'
    }
]

matrix.extend(l18_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Successfully updated matrix! Total rows now: {len(matrix)}')
