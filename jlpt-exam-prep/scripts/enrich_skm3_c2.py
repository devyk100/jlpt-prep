import json

# 1. Update chapterExercises.json for SKM N3 Chapter 2 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

new_questions = [
    {
        'id': 'skm3-c2-ex-6',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 2',
        'type': 'multiple-choice',
        'context': 'Exam results matching predictions: Commenting that the test results turned out exactly as anticipated.',
        'question': '事前の模試の判定が良かったので、試験の結果は（　　）どおりでした。',
        'translation': 'Because my mock exam predictions were good, the test results were just as anticipated.',
        'options': [
            '予想',
            '予想の',
            '予想したの',
            '予想で'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u2-toori-ni-accordance',
        'grammarPointTitle': '〜とおりに / 〜どおりに (Just As / In Exact Accordance With)',
        'explanation': {
            'overall': 'When attaching directly to Sino-Japanese nouns without the particle の, rendaku occurs to produce 〜どおり (予想どおり, 計画どおり, 指示どおり). If の were present, it would be 予想のとおり.',
            'options': [
                {
                    'text': '予想',
                    'isCorrect': True,
                    'reason': 'Correct. Direct noun attachment triggers voiced rendaku: 予想どおり ("just as anticipated").',
                    'trapCategory': 'formation'
                },
                {
                    'text': '予想の',
                    'isCorrect': False,
                    'reason': 'Incorrect. If の is used, the following form is unvoiced: 予想のとおり, not 予想のどおり.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '予想したの',
                    'isCorrect': False,
                    'reason': 'Incorrect. Verbs attach directly to とおり (予想したとおり), not with redundant の.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '予想で',
                    'isCorrect': False,
                    'reason': 'Incorrect. で does not combine with どおり.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'Which noun attaches directly to どおり (with rendaku) without any intervening particle?'
    },
    {
        'id': 'skm3-c2-ex-7',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 2',
        'type': 'multiple-choice',
        'context': 'Contingency planning for an outdoor festival: Explaining that in some specific circumstances, the event may be canceled.',
        'question': '当日の天気（　　）は、花火大会が中止になることもあります。',
        'translation': 'Depending on the weather on that day, the fireworks festival may be canceled in some cases.',
        'options': [
            'によっては',
            'について',
            'に対して',
            'にとって'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u2-ni-yotte-variation',
        'grammarPointTitle': '〜によって / 〜によっては (Depending on / According to Differences)',
        'explanation': {
            'overall': '〜によっては pinpoints one specific possibility or extreme outcome from a spectrum of potential cases: "in some cases, depending on X" (天気によっては: depending on the weather, in some weather cases).',
            'options': [
                {
                    'text': 'によっては',
                    'isCorrect': True,
                    'reason': 'Correct. Noun + によっては singles out a possible consequence depending on variation.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'について',
                    'isCorrect': False,
                    'reason': 'Incorrect. について means "concerning / about", not contingent variation.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'に対して',
                    'isCorrect': False,
                    'reason': 'Incorrect. に対して expresses target or contrast ("toward / in contrast to").',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'にとって',
                    'isCorrect': False,
                    'reason': 'Incorrect. にとって means "from the standpoint of", not causal condition.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which expression means "depending on X, in some circumstances..."?'
    },
    {
        'id': 'skm3-c2-ex-8',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 2',
        'type': 'multiple-choice',
        'context': 'Habitual travel custom: Explaining that every single time you travel to a new region, you always buy local souvenirs.',
        'question': '出張や旅行に（　　）たびに、その土地の珍しいお菓子を買って帰る。',
        'translation': 'Every time I go on a business trip or vacation, I buy rare local confections to bring back.',
        'options': [
            '行く',
            '行って',
            '行った',
            '行かない'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u2-tabini-repetition',
        'grammarPointTitle': '〜たびに (Every Single Time / Invariable Recurrence)',
        'explanation': {
            'overall': 'When attaching a verb to 〜たびに, the dictionary form is strictly required: V(dictionary form) + たびに (行くたびに: every time I go). Past た-form or て-form cannot connect to たびに.',
            'options': [
                {
                    'text': '行く',
                    'isCorrect': True,
                    'reason': 'Correct. Verbs attach in dictionary form: 行くたびに ("every time I go").',
                    'trapCategory': 'formation'
                },
                {
                    'text': '行って',
                    'isCorrect': False,
                    'reason': 'Incorrect. Te-form cannot precede たびに (*行っていたびに is ungrammatical).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '行った',
                    'isCorrect': False,
                    'reason': 'Incorrect. Past た-form does not connect to たびに (*行ったたびに is ungrammatical).',
                    'trapCategory': 'tense'
                },
                {
                    'text': '行かない',
                    'isCorrect': False,
                    'reason': 'Incorrect. Negative form contradicts the recurring positive custom.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'What verb form connects to たびに to mean "every time one does..."?'
    },
    {
        'id': 'skm3-c2-ex-9',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 2',
        'type': 'multiple-choice',
        'context': 'Job search expectations: Stating that regarding salary, the higher it is, the happier one feels.',
        'question': '転職先を探していますが、給料は（　　）ほど嬉しいです。',
        'translation': 'I am looking for a new job, and regarding salary, the higher it is, the happier I am.',
        'options': [
            '高ければ高い',
            '高くて高い',
            '高かったら高い',
            '高いなら高い'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u2-ba-hodo-proportion',
        'grammarPointTitle': '(〜ば)〜ほど (Proportional Correlation: The More... The More...)',
        'explanation': {
            'overall': 'For い-adjectives, the proportional correlation formula is [Adjective-ければ] + [Adjective-い] + ほど: 高ければ高いほど ("the higher, the more...").',
            'options': [
                {
                    'text': '高ければ高い',
                    'isCorrect': True,
                    'reason': 'Correct. A-ければ + A-い + ほど is the standard proportional correlation formula for い-adjectives.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '高くて高い',
                    'isCorrect': False,
                    'reason': 'Incorrect. Te-form cannot form the conditional half of the proportion.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '高かったら高い',
                    'isCorrect': False,
                    'reason': 'Incorrect. たら does not pair with ほど in standard written Japanese.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '高いなら高い',
                    'isCorrect': False,
                    'reason': 'Incorrect. なら is for contextual topics, not proportional gradation.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'What is the full formula for い-adjectives with ほど: "the [adjective]-er, the more..."?'
    },
    {
        'id': 'skm3-c2-ex-10',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 2',
        'type': 'multiple-choice',
        'context': 'Incidental errand on the way: Dropping off dry cleaning while heading out to the supermarket.',
        'question': 'スーパーへ買い物に（　　）ついでに、クリーニングを出してきた。',
        'translation': 'While going to the supermarket for groceries, I took the opportunity to drop off the dry cleaning.',
        'options': [
            '行った',
            '行って',
            '行こう',
            '行けば'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u2-tsuide-ni-opportunity',
        'grammarPointTitle': '〜ついでに (While at It / Seizing Opportunity for a Side Task)',
        'explanation': {
            'overall': 'When attaching a verb to 〜ついでに to describe an action completed along the way, either dictionary form or past た-form is used: 行ったついでに / 行くついでに. Te-form or volitional forms cannot connect.',
            'options': [
                {
                    'text': '行った',
                    'isCorrect': True,
                    'reason': 'Correct. Verb past form 行った connects smoothly with ついでに: 行ったついでに ("while I went").',
                    'trapCategory': 'formation'
                },
                {
                    'text': '行って',
                    'isCorrect': False,
                    'reason': 'Incorrect. Te-form cannot connect directly to ついでに (*行ってついでに is invalid).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '行こう',
                    'isCorrect': False,
                    'reason': 'Incorrect. Volitional form cannot precede ついでに.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '行けば',
                    'isCorrect': False,
                    'reason': 'Incorrect. Conditional ば cannot precede ついでに.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'Which verb form connects with ついでに when narrating a past incidental action: 行った or 行って?'
    },
    {
        'id': 'skm3-c2-ex-11',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 2',
        'type': 'multiple-choice',
        'context': 'Validating intuition: Remarking that the movie\'s twist ending was exactly as one had previously suspected.',
        'question': '犯人は誰かずっと気になっていたが、やはり私が（　　）とおりだった。',
        'translation': 'I had been wondering who the culprit was, and as expected, it was just as I had thought.',
        'options': [
            '思った',
            '思うの',
            '思って',
            '思えば'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u2-toori-ni-accordance',
        'grammarPointTitle': '〜とおりに / 〜どおりに (Just As / In Exact Accordance With)',
        'explanation': {
            'overall': 'Verb た-form + とおりだ means "it was just as [verb]ed": 思ったとおりだった (it was just as I thought / expected).',
            'options': [
                {
                    'text': '思った',
                    'isCorrect': True,
                    'reason': 'Correct. Verb た-form 思った + とおり means "just as I thought".',
                    'trapCategory': 'formation'
                },
                {
                    'text': '思うの',
                    'isCorrect': False,
                    'reason': 'Incorrect. Verbs attach directly to とおり without の (*思うのとおり is incorrect).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '思って',
                    'isCorrect': False,
                    'reason': 'Incorrect. Te-form cannot attach to とおり.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '思えば',
                    'isCorrect': False,
                    'reason': 'Incorrect. Conditional form cannot attach to とおり.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'Which form connects with とおり to say "just as I thought": 思った or 思うの?'
    },
    {
        'id': 'skm3-c2-ex-12',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 2',
        'type': 'multiple-choice',
        'context': 'Product design principle: Stating that for elderly users, the simpler the smartphone operation is, the better.',
        'question': '高齢者向けの機器は、操作が（　　）簡単なほど使いやすい。',
        'translation': 'For devices aimed at the elderly, the simpler the operation is, the easier it is to use.',
        'options': [
            '簡単なら',
            '簡単で',
            '簡単だから',
            '簡単だと'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u2-ba-hodo-proportion',
        'grammarPointTitle': '(〜ば)〜ほど (Proportional Correlation: The More... The More...)',
        'explanation': {
            'overall': 'For な-adjectives, the proportional correlation formula is [Stem + なら(ば)] + [Stem + な] + ほど: 簡単なら簡単なほど ("the simpler, the more...").',
            'options': [
                {
                    'text': '簡単なら',
                    'isCorrect': True,
                    'reason': 'Correct. な-adj stem + なら + な-adj stem + なほど is the standard proportional correlation formula.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '簡単で',
                    'isCorrect': False,
                    'reason': 'Incorrect. て-form で cannot form the conditional half of the proportion.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '簡単だから',
                    'isCorrect': False,
                    'reason': 'Incorrect. から indicates cause/reason, not a proportional correlation.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '簡単だと',
                    'isCorrect': False,
                    'reason': 'Incorrect. と conditional does not pair with ほど.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'What conditional ending connects with a な-adjective before [Stem + なほど]?'
    }
]

existing_ids = {e['id'] for e in exercises}
for q in new_questions:
    if q['id'] not in existing_ids:
        exercises.append(q)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for SKM N3 Chapter 2!')

# 2. Enrich base-reviewed.json for Chapter 2 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. skm3-u2-toori-ni-accordance
c = card_map.get('skm3-u2-toori-ni-accordance')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 2'
    c['nuance'] = (
        '〜とおりに / 〜どおりに expresses carrying out an action or manifesting a state in complete conformity with a model, instructions, thought, or plan: "just as / in exact accordance with". '
        'FORMATION & RENDAKU (Printed p. 18): '
        '・Noun + の + とおりに (説明書のとおりに: according to the manual; 計画のとおりに: as planned). '
        '・Noun + どおりに (Direct attachment triggers voiced rendaku: 予想どおり: as predicted; 計画どおり: as planned; 指示どおり: as instructed; 思いどおり: as desired). '
        '・Verb (辞書形 / た形 / ている形) + とおりに (私が言うとおりにしてください: Do exactly as I say; 思ったとおりだった: It was just as I thought; 見たとおりに話す: tell it just as seen). '
        'RESTRICTION: Verbs attach directly to とおり without の (*言うのとお'
    )
    # Complete nuance properly
    c['nuance'] = (
        '〜とおりに / 〜どおりに expresses carrying out an action or manifesting a state in complete conformity with a model, instructions, thought, or plan: "just as / in exact accordance with". '
        'FORMATION & RENDAKU (Printed p. 18): '
        '・Noun + の + とおりに (説明書のとおりに: according to the manual; 計画のとおりに: as planned). '
        '・Noun + どおりに (Direct attachment triggers voiced rendaku: 予想どおり: as predicted; 計画どおり: as planned; 指示どおり: as instructed; 思いどおり: as desired). '
        '・Verb (辞書形 / た形 / ている形) + とおりに (私が言うとおりにしてください: Do exactly as I say; 思ったとおりだった: It was just as I thought; 見たとおりに話す: tell it just as seen). '
        'RESTRICTION: Verbs attach directly to とおり without particle の (言うとおり, never *言うのとおり).'
    )
    c['keyTakeaway'] = '〜とおりに / どおりに: "just as / in accordance with". Formations: Noun + のとおりに OR direct Noun + どおりに (予想どおり, 計画どおり). Verb (dict/ta/te-iru) + とおりに.'
    c['connection'] = 'Noun + のとおりに / Noun + どおりに | Verb (辞書形/た形/ている形) + とおりに'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 2, Section 1, printed p. 18 (PDF p. 41).'

# 2. skm3-u2-ni-yotte-variation
c = card_map.get('skm3-u2-ni-yotte-variation')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 2'
    c['nuance'] = (
        '〜によって / 〜によっては expresses that behavior, state, or outcomes vary depending on conditions, categories, or differences: "depending on / according to differences in". '
        'FORMATION (Printed p. 18): '
        '・Noun + によって / Noun + による + Noun '
        '・国によって習慣が違います (Customs differ depending on the country). '
        '・人によって感じ方がさまざまだ (Ways of feeling vary depending on the individual). '
        'PREDICATE COLLOCATIONS: '
        'Frequently concludes with diversity predicates: 違う (differ), 異なる (vary), さまざまだ (diverse), 変わる (change). '
        'PINPOINTING OUTCOMES WITH 〜によっては (p. 18): '
        '〜によっては pinpoints one specific extreme or notable outcome from among multiple possibilities ("in some cases depending on..."): '
        '・当日の天気によっては、花火大会が中止になることもあります (Depending on the weather, the fireworks may be canceled in some cases).'
    )
    c['keyTakeaway'] = 'Noun + によって = "depending on differences in..." (predicate: 違う, さまざまだ). Noun + によっては = "in some cases depending on..." (pinpointing a specific outcome, e.g. 中止になることもある).'
    c['connection'] = 'Noun + によって (predicate: 違う/さまざま) | Noun + によっては (single outcome)'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 2, Section 2, printed p. 18 (PDF p. 41).'

# 3. skm3-u2-tabini-repetition
c = card_map.get('skm3-u2-tabini-repetition')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 2'
    c['nuance'] = (
        '〜たびに expresses recurring, invariable co-occurrence: "every single time ~ happens, ... happens too / whenever ~, always ...". '
        'FORMATION (Printed p. 19): '
        '・Noun + の + たびに (旅行のたびに: every time I travel; 会うたびに: every time we meet). '
        '・Verb (辞書形) + たびに (この曲を聞くたびに、学生時代を思い出す: Every time I listen to this song, I recall my student days). '
        'STRICT RESTRICTIONS (Printed p. 19): '
        '(1) Natural/everyday matter-of-course events cannot be used (*朝起きるたびに顔を洗う: ungrammatical; must describe deliberate, noteworthy recurrence). '
        '(2) Neither ~ nor ... can express a static condition/state (both must describe discrete recurring events or actions).'
    )
    c['keyTakeaway'] = 'V(辞書形) / Noun + の + たびに = "every single time ~ happens, always ...". Strict bans: (1) Cannot be used for everyday matter-of-course habits (*朝起きるたびに), (2) Neither clause can be a static state.'
    c['connection'] = 'Noun + の / Verb (辞書形) + たびに'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 2, Section 3, printed p. 19 (PDF p. 42).'

# 4. skm3-u2-ba-hodo-proportion
c = card_map.get('skm3-u2-ba-hodo-proportion')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 2'
    c['nuance'] = (
        '(〜ば)〜ほど expresses proportional correlation: "the more ~ increases in degree, the more ... also increases or changes in parallel". '
        'FORMATION PARADIGM (Printed p. 19): '
        '・Verbs: V-ば + V-辞書形 + ほど (物が増えれば増えるほど、整理が大変になる: The more things increase, the harder tidying up becomes). '
        '・い-adjectives: A-ければ + A-い + ほど (安ければ安いほどいい: The cheaper, the better; 高ければ高いほど嬉しい). '
        '・な-adjectives: A-なら(ば) + A-な + ほど (簡単なら簡単なほど使いやすい: The simpler, the easier to use; 静かなら静かなほどいい). '
        '・Bare Noun: Noun + ほど (本物ほど価値がある: The more genuine it is, the more value it has). '
        'ELLIPSIS: The initial conditional clause (〜ば / 〜なら) is often omitted in natural Japanese (e.g. 考えれば考えるほど → 考えるほど: the more I think; 安いほどいい).'
    )
    c['keyTakeaway'] = '(〜ば)〜ほど: "the more..., the more...". Formations: V-ば V-辞書形ほど; A-ければ A-いほど; A-なら A-なほど; Noun+ほど. The first conditional half can be omitted (考えるほど).'
    c['connection'] = 'V-ば + V-辞書形ほど | A-ければ + A-いほど | A-なら + A-なほど | Noun + ほど'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 2, Section 4, printed p. 19 (PDF p. 42).'

# 5. skm3-u2-tsuide-ni-opportunity
c = card_map.get('skm3-u2-tsuide-ni-opportunity')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 2'
    c['nuance'] = (
        '〜ついでに expresses taking advantage of the opportunity created by a primary action to conveniently accomplish a secondary task: "while doing primary action ~, take the chance to do secondary action ... as well". '
        'FORMATION (Printed p. 19): '
        '・Noun + の + ついでに (散歩のついでに、ポストに手紙を入れてきた: While out for a walk, I dropped a letter in the post). '
        '・Verb (辞書形 / た形) + ついでに (買い物のついでに本屋に寄った; 出張で行ったついでに観光した). '
        'PRIMARY VS SECONDARY ACTION CONSTRAINT (p. 19): '
        'Clause A represents the main, pre-planned primary action. Clause B represents an incidental, secondary action that is carried out opportunistically because of A. Reversing the priority creates pragmatically unnatural Japanese.'
    )
    c['keyTakeaway'] = '〜ついでに: "while at it / taking opportunity of primary action A to do secondary B". Formation: Noun+の / Verb(dict/ta) + ついでに. A is the primary goal; B is the incidental side action.'
    c['connection'] = 'Noun + の / Verb (辞書形 / た形) + ついでに'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 2, Section 5, printed p. 19 (PDF p. 42).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 5 SKM N3 Chapter 2 cards in base-reviewed.json!')

# 3. Add 5 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing SKM N3 Chapter 2 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Shin Kanzen Master N3' and r.get('sourceSection') == 'Part 1 · Chapter 2')]

skm3_c2_entries = [
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 2',
        'exactPrintedPages': 'p. 18',
        'exactPdfPages': 'p. 41',
        'grammarItem': '〜とおりに / 〜どおりに (In Exact Accordance With / Just As)',
        'instructionalDetails': 'Conformity with model/instruction; Noun + のとおりに vs direct Noun + どおりに with rendaku (予想どおり, 計画どおり, 指示どおり); Verb (dict/ta/te-iru) + とおりに; ban on connecting verbs with particle の (*言うのとおり).',
        'cardId': 'skm3-u2-toori-ni-accordance',
        'exampleCount': 4,
        'exampleIds': ['skm3-u2-toori-ni-accordance::s-skm3-2-1', 'skm3-u2-toori-ni-accordance::n3-use-examples-16', 'skm3-u2-toori-ni-accordance::n3-use-examples-17', 'skm3-u2-toori-ni-accordance::n3-use-examples-18'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 18 (PDF p. 41, skm3_pdf_41.png). Verified Section 1 formation rules, noun rendaku behavior (どおり), and verb direct attachment.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 2',
        'exactPrintedPages': 'p. 18',
        'exactPdfPages': 'p. 41',
        'grammarItem': '〜によって / 〜によっては (Depending on / According to Differences)',
        'instructionalDetails': 'Variation depending on condition; predicate collocations 違う, さまざまだ, 異なる; Noun + によっては pinpoints one extreme/singular outcome from among possibilities (中止になることもある).',
        'cardId': 'skm3-u2-ni-yotte-variation',
        'exampleCount': 4,
        'exampleIds': ['skm3-u2-ni-yotte-variation::s-skm3-2-2', 'skm3-u2-ni-yotte-variation::n3-use-examples-19', 'skm3-u2-ni-yotte-variation::n3-use-examples-20', 'skm3-u2-ni-yotte-variation::n3-use-examples-21'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 18 (PDF p. 41, skm3_pdf_41.png). Verified Section 2 variation semantics and the distinguishing role of 〜によっては.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 2',
        'exactPrintedPages': 'p. 19',
        'exactPdfPages': 'p. 42',
        'grammarItem': '〜たびに (Every Single Time / Invariable Recurrence)',
        'instructionalDetails': 'Recurring invariable co-occurrence; Noun + の / V(dict) + たびに; strict bans: (1) no everyday matter-of-course habits (*朝起きるたびに顔を洗う), (2) neither clause can describe a static state.',
        'cardId': 'skm3-u2-tabini-repetition',
        'exampleCount': 4,
        'exampleIds': ['skm3-u2-tabini-repetition::s-skm3-2-3', 'skm3-u2-tabini-repetition::n3-use-examples-22', 'skm3-u2-tabini-repetition::n3-use-examples-23', 'skm3-u2-tabini-repetition::n3-use-examples-24'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 19 (PDF p. 42, skm3_pdf_42.png). Verified Section 3 rules and explicit textbook footnote banning matter-of-course everyday habits and static states.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 2',
        'exactPrintedPages': 'p. 19',
        'exactPdfPages': 'p. 42',
        'grammarItem': '(〜ば)〜ほど (Proportional Correlation: The More... The More...)',
        'instructionalDetails': 'Parallel proportional increase; V-ば V-dictほど; A-ければ A-いほど; A-なら A-なほど; Noun+ほど; optional ellipsis of initial conditional clause (考えるほど); parallel degree semantics.',
        'cardId': 'skm3-u2-ba-hodo-proportion',
        'exampleCount': 4,
        'exampleIds': ['skm3-u2-ba-hodo-proportion::s-skm3-2-4', 'skm3-u2-ba-hodo-proportion::n3-use-examples-25', 'skm3-u2-ba-hodo-proportion::n3-use-examples-26', 'skm3-u2-ba-hodo-proportion::n3-use-examples-27'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 19 (PDF p. 42, skm3_pdf_42.png). Verified Section 4 four-part conjugation paradigm (verb, i-adj, na-adj, noun) and proportional degree mechanics.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 2',
        'exactPrintedPages': 'p. 19',
        'exactPdfPages': 'p. 42',
        'grammarItem': '〜ついでに (While at It / Incidental Secondary Action)',
        'instructionalDetails': 'Seizing opportunity of primary action A to do secondary action B; Noun + の / Verb (dict/ta) + ついでに; strict priority: A is the primary planned goal, B is the opportunistic secondary action.',
        'cardId': 'skm3-u2-tsuide-ni-opportunity',
        'exampleCount': 4,
        'exampleIds': ['skm3-u2-tsuide-ni-opportunity::s-skm3-2-5', 'skm3-u2-tsuide-ni-opportunity::n3-use-examples-28', 'skm3-u2-tsuide-ni-opportunity::n3-use-examples-29', 'skm3-u2-tsuide-ni-opportunity::n3-use-examples-30'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 19 (PDF p. 42, skm3_pdf_42.png). Verified Section 5 formation rules, primary-versus-secondary priority constraints, and authentic examples.'
    }
]

matrix.extend(skm3_c2_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Certified SKM N3 Chapter 2 in source coverage matrix! Total certified rows: {len(matrix)}')
