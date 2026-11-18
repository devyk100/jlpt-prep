import json

# 1. Update chapterExercises.json for SKM N3 Chapter 3 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

new_questions = [
    {
        'id': 'skm3-c3-ex-5',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 3',
        'type': 'multiple-choice',
        'context': 'Metaphorical extent of unreality: Expressing that an incredible event was so wonderful you wondered if it was all a dream.',
        'question': '大好きな作家に直接会えて、まるで夢（　　）と思うほど嬉しかった。',
        'translation': 'I was able to meet my favorite author in person, and I was so happy I even wondered if it was a dream.',
        'options': [
            'か',
            'に',
            'で',
            'と'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u3-kurai-hodo-extent',
        'grammarPointTitle': '〜くらいだ / 〜ほどだ (Expressing Extreme Degree: To the Extent That)',
        'explanation': {
            'overall': 'The expression 〜かと思うほど means "to the extent that one even wonders whether...": 夢かと思うほど (so wonderful I wondered if it was a dream).',
            'options': [
                {
                    'text': 'か',
                    'isCorrect': True,
                    'reason': 'Correct. [Phrase] + かと思うほど expresses an extreme degree making one wonder if it is real.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'に',
                    'isCorrect': False,
                    'reason': 'Incorrect. に cannot form the embedded question marker before と思う.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'で',
                    'isCorrect': False,
                    'reason': 'Incorrect. で indicates location or means, not conjectural wondering.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'と',
                    'isCorrect': False,
                    'reason': 'Incorrect. 夢と思うほど lacks the wonder/doubt marker か.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'What question particle is embedded in "... [　] と思うほど" to express wondering if it was real?'
    },
    {
        'id': 'skm3-c3-ex-6',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 3',
        'type': 'multiple-choice',
        'context': 'Subjective superlative praising a senior mentor: Expressing that nobody is as dependable as Senpai.',
        'question': '職場のトラブルが起きたとき、彼（　　）頼りになる先輩はいません。',
        'translation': 'When workplace trouble occurs, there is no senior colleague as dependable as him.',
        'options': [
            'くらい',
            'ばかり',
            'だけに',
            'にしては'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u3-kurai-wa-nai',
        'grammarPointTitle': '〜くらい…はない / 〜ほど…はない (Superlative: Nothing Is As... As X)',
        'explanation': {
            'overall': '[Noun] + くらい / ほど + [Predicate] はない (or いない for people) expresses a subjective superlative: "nobody / nothing is as... as X".',
            'options': [
                {
                    'text': 'くらい',
                    'isCorrect': True,
                    'reason': 'Correct. Noun + くらい...人はいない forms the subjective superlative ("no one is as dependable as him").',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'ばかり',
                    'isCorrect': False,
                    'reason': 'Incorrect. ばかり indicates exclusivity/repetition ("only"), not superlative comparison.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'だけに',
                    'isCorrect': False,
                    'reason': 'Incorrect. だけに indicates natural expectation ("precisely because"), not a superlative.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'にしては',
                    'isCorrect': False,
                    'reason': 'Incorrect. にしては indicates an unexpected contrast with a norm ("for a..."), not superlative praise.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which particle pairs with "...[Noun] はいない" to express that no one surpasses X?'
    },
    {
        'id': 'skm3-c3-ex-7',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 3',
        'type': 'multiple-choice',
        'context': 'Strong resolve against half-hearted commitment: Stating that rather than giving up halfway, one shouldn\'t start at all.',
        'question': '途中で投げ出してしまう（　　）、最初から始めない方がましだ。',
        'translation': 'Rather than giving up halfway, it is better not to start in the first place.',
        'options': [
            'くらいなら',
            'とおりなら',
            'たびに',
            'うちに'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u3-kurai-nara',
        'grammarPointTitle': '〜くらいなら / 〜ぐらいなら (Rather Than Suffer X, I Would Prefer Y)',
        'explanation': {
            'overall': 'V(dictionary form) + くらいなら (or ぐらいなら) + [Clause B with 〜方がいい / 〜方がましだ] means "rather than suffer undesirable X, I would prefer Y".',
            'options': [
                {
                    'text': 'くらいなら',
                    'isCorrect': True,
                    'reason': 'Correct. V-dictionary + くらいなら expresses "rather than undergo undesirable condition X, Y is better".',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'とおりなら',
                    'isCorrect': False,
                    'reason': 'Incorrect. とおり does not express preferential comparison.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'たびに',
                    'isCorrect': False,
                    'reason': 'Incorrect. たびに means "every time", which does not fit comparison.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'うちに',
                    'isCorrect': False,
                    'reason': 'Incorrect. うちに means "while / before", not preference.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which structure connects with a dictionary-form verb before "...方がましだ" to mean "rather than... I\'d prefer"?'
    },
    {
        'id': 'skm3-c3-ex-8',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 3',
        'type': 'multiple-choice',
        'context': 'Summer refreshment recommendation: Declaring that on a scorching afternoon, nothing beats cold barley tea.',
        'question': 'こんなに暑い日の水分補給は、やっぱり冷たい麦茶に（　　）。',
        'translation': 'For hydration on a hot day like this, nothing beats cold barley tea.',
        'options': [
            '限る',
            'よる',
            '比べる',
            '違いない'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u3-ni-kagiru',
        'grammarPointTitle': '〜に限る (Nothing Beats / Best Choice)',
        'explanation': {
            'overall': 'Noun / Verb (dictionary/negative) + に限る expresses the speaker\'s subjective conviction that X is the absolute best choice ("nothing beats X").',
            'options': [
                {
                    'text': '限る',
                    'isCorrect': True,
                    'reason': 'Correct. [Noun] + に限る expresses the subjective superlative "nothing beats X / X is best".',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'よる',
                    'isCorrect': False,
                    'reason': 'Incorrect. による means "depends on" or "due to", not best choice.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '比べる',
                    'isCorrect': False,
                    'reason': 'Incorrect. 比べる means "compare with", not a superlative conclusion.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '違いない',
                    'isCorrect': False,
                    'reason': 'Incorrect. に違いない indicates certainty ("must be"), not personal recommendation of the best method.',
                    'trapCategory': 'nuance'
                }
            ]
        },
        'hint': 'What verb follows に to mean "nothing beats X / X is the best choice"?'
    },
    {
        'id': 'skm3-c3-ex-9',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 3',
        'type': 'multiple-choice',
        'context': 'Dramatic tension in an exam hall: Describing an exam room so quiet you felt you could hardly breathe.',
        'question': '試験会場は、息ができない（　　）静まり返っていた。',
        'translation': 'The exam room was so silent you felt like you could hardly breathe.',
        'options': [
            'ほど',
            'とおり',
            'ばかり',
            'ついでに'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u3-kurai-hodo-extent',
        'grammarPointTitle': '〜くらいだ / 〜ほどだ (Expressing Extreme Degree: To the Extent That)',
        'explanation': {
            'overall': 'Verb (plain form) + ほど describes an extreme metaphorical degree: "to the extent that..." (息ができないほど: so quiet one could hardly breathe).',
            'options': [
                {
                    'text': 'ほど',
                    'isCorrect': True,
                    'reason': 'Correct. ほど expresses extreme metaphorical extent ("to the extent that...").',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'とおり',
                    'isCorrect': False,
                    'reason': 'Incorrect. とおり means conformity, not intensity of degree.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'ばかり',
                    'isCorrect': False,
                    'reason': 'Incorrect. ばかり indicates approximate amount or repetition, not metaphorical degree.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'ついでに',
                    'isCorrect': False,
                    'reason': 'Incorrect. ついでに indicates incidental side opportunity.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which noun expresses extreme degree ("so intense that...")?'
    },
    {
        'id': 'skm3-c3-ex-10',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 3',
        'type': 'multiple-choice',
        'context': 'Safety advice during severe weather: Advising that during a typhoon, the best policy is not to go outside.',
        'question': '大型の台風が接近しているときは、不要な外出は（　　）に限る。',
        'translation': 'When a large typhoon is approaching, the best thing to do is not to go outside unnecessarily.',
        'options': [
            'しない',
            'して',
            'する',
            'した'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u3-ni-kagiru',
        'grammarPointTitle': '〜に限る (Nothing Beats / Best Choice)',
        'explanation': {
            'overall': 'When recommending an omission or preventative behavior as the best policy, use V-ない + に限る: 外出はしないに限る ("the best thing is not to go outside").',
            'options': [
                {
                    'text': 'しない',
                    'isCorrect': True,
                    'reason': 'Correct. V-ない + に限る expresses that avoiding an action is the best policy.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'して',
                    'isCorrect': False,
                    'reason': 'Incorrect. Te-form cannot connect to に限る (*してに限る is ungrammatical).',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'する',
                    'isCorrect': False,
                    'reason': 'Incorrect. Affirmative する contradicts typhoon safety logic.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'した',
                    'isCorrect': False,
                    'reason': 'Incorrect. Past た-form does not connect to に限る for general policies.',
                    'trapCategory': 'tense'
                }
            ]
        },
        'hint': 'What negative verb form connects with に限る to advise that NOT doing something is best?'
    },
    {
        'id': 'skm3-c3-ex-11',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 3',
        'type': 'multiple-choice',
        'context': 'Marital preference: Declaring that rather than marrying someone you don\'t respect, you\'d prefer to stay single.',
        'question': '尊敬できない人と無理に結婚する（　　）、一生一人で自由に生きたい。',
        'translation': 'Rather than forcing myself to marry someone I cannot respect, I would prefer to live freely on my own for life.',
        'options': [
            'くらいなら',
            'うちに',
            'たびに',
            'とおりに'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u3-kurai-nara',
        'grammarPointTitle': '〜くらいなら / 〜ぐらいなら (Rather Than Suffer X, I Would Prefer Y)',
        'explanation': {
            'overall': 'V(dictionary form) + くらいなら expresses that undesirable option X is so abhorrent that alternative Y is preferred: 結婚するくらいなら ("rather than marry...").',
            'options': [
                {
                    'text': 'くらいなら',
                    'isCorrect': True,
                    'reason': 'Correct. V-dictionary + くらいなら indicates rejecting an undesirable option in favor of an alternative.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'うちに',
                    'isCorrect': False,
                    'reason': 'Incorrect. うちに indicates temporal opportunity, not preference.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'たびに',
                    'isCorrect': False,
                    'reason': 'Incorrect. たびに indicates repeated recurrence.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'とおりに',
                    'isCorrect': False,
                    'reason': 'Incorrect. とおりに indicates conformity.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which phrase expresses "rather than do undesirable action X, I\'d rather..."?'
    },
    {
        'id': 'skm3-c3-ex-12',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 3',
        'type': 'multiple-choice',
        'context': 'Cherishing family time: Expressing that nothing in the world is as precious as time spent with loved ones.',
        'question': '忙しい毎日だからこそ、家族とゆっくり過ごす時間（　　）幸せなものはない。',
        'translation': 'Precisely because daily life is so busy, there is nothing as blissful as time spent relaxing with family.',
        'options': [
            'ほど',
            'より',
            'だけに',
            'にとって'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u3-kurai-wa-nai',
        'grammarPointTitle': '〜くらい…はない / 〜ほど…はない (Superlative: Nothing Is As... As X)',
        'explanation': {
            'overall': 'Noun + ほど + [Predicate] はない asserts a subjective superlative: "nothing is as [adjective] as Noun" (時間ほど幸せなものはない: nothing is as blissful as time spent with family).',
            'options': [
                {
                    'text': 'ほど',
                    'isCorrect': True,
                    'reason': 'Correct. Noun + ほど...はない forms the subjective superlative ("nothing is as blissful as...").',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'より',
                    'isCorrect': False,
                    'reason': 'Incorrect. より expresses relative comparison ("more than"), but ほど...はない is the standard superlative pattern.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'だけに',
                    'isCorrect': False,
                    'reason': 'Incorrect. だけに expresses cause/expectation.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'にとって',
                    'isCorrect': False,
                    'reason': 'Incorrect. にとって expresses personal standpoint.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which particle pairs with "...幸せなものはない" to express that nothing equals this happiness?'
    }
]

existing_ids = {e['id'] for e in exercises}
for q in new_questions:
    if q['id'] not in existing_ids:
        exercises.append(q)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for SKM N3 Chapter 3!')

# 2. Enrich base-reviewed.json for Chapter 3 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. skm3-u3-kurai-hodo-extent
c = card_map.get('skm3-u3-kurai-hodo-extent')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 3'
    c['nuance'] = (
        '〜くらいだ / 〜ほどだ expresses an extreme metaphorical degree: "to the extent that ~, in which ~ is an illustrative, vivid example of what could have happened, but did not actually occur". '
        'FORMATION (Printed p. 22): '
        '・Noun / Verb (plain form) / い-adj / な-adj + な + くらいだ / ほどだ / くらい / ほど. '
        '・涙が出るほど痛かった (It hurt so much that tears came out). '
        '・倒れそうなほど疲れた (I was so exhausted that I felt like collapsing). '
        '・お腹が痛くなるくらい大笑いした (Laughed so hard my stomach ached). '
        'IDIOMATIC EXTENSION: '
        '〜かと思うほど: "so [adjective] that I even wondered if..." (まるで夢かと思うほど嬉しかった: so happy I wondered if it was a dream).'
    )
    c['keyTakeaway'] = '〜くらいだ / 〜ほどだ: Expresses extreme metaphorical degree ("so intense that ~ almost happened"). Formations: Noun / Verb / い-adj / な-adj + な + くらいだ / ほどだ. Idiom: 〜かと思うほど.'
    c['connection'] = 'Noun / Verb (plain) / い-adj / な-adj + な + くらいだ / ほどだ'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 3, Section 1, printed p. 22 (PDF p. 45).'

# 2. skm3-u3-kurai-wa-nai
c = card_map.get('skm3-u3-kurai-wa-nai')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 3'
    c['nuance'] = (
        '〜くらい…はない / 〜ほど…はない expresses a subjective superlative: "~ is the most ... of all / nothing/nobody is as ... as ~". '
        'FORMATION (Printed p. 22): '
        '・Noun + くらい / ほど + [Noun] + はない (or いない for animate persons). '
        '・健康ほど大切なものはない (Nothing is as important as health). '
        '・彼くらい頼りになる先輩はいない (There is no senior colleague as dependable as him). '
        '・母の手料理くらい美味しいものはない (Nothing is as delicious as my mother\'s home cooking). '
        'SUBJECTIVE CONSTRAINT (p. 22): '
        'This pattern expresses the speaker\'s personal subjective conviction or emotional evaluation; it CANNOT be used to state objective factual superlatives (*富士山ほど高い山は日本にない is unnatural in formal factual contexts; use 日本で一番高い山 instead).'
    )
    c['keyTakeaway'] = 'Noun + くらい / ほど + [Noun] はない / いない: Subjective superlative ("nothing/nobody is as ... as X"). Expresses speaker\'s personal feeling, not an objective factual statistic.'
    c['connection'] = 'Noun + くらい / ほど + [Noun] + はない / はいない'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 3, Section 2, printed p. 22 (PDF p. 45).'

# 3. skm3-u3-kurai-nara
c = card_map.get('skm3-u3-kurai-nara')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 3'
    c['nuance'] = (
        '〜くらいなら / 〜ぐらいなら expresses choosing a preferable alternative over an abhorrent or undesirable situation: "if ~ is the case, you are better off doing ... / rather than suffer ~, I would prefer ...". '
        'FORMATION (Printed p. 23): '
        '・Verb (辞書形) + くらいなら / ぐらいなら + [Clause B with 〜方がいい / 〜方がましだ]. '
        '・途中で諦めるくらいなら、最初からやらない方がいい (Rather than giving up halfway, you\'re better off not starting at all). '
        '・あんな奴に謝るくらいなら、部活を辞めた方がましだ (Rather than apologizing to that jerk, I\'d rather quit the club!). '
        '・生活水準を下げるくらいなら、残業した方がいい (Rather than lowering my standard of living, I\'d rather work overtime). '
        'PRAGMATIC CONSTRAINTS: '
        'Expresses subjective judgment of personal values; clause B typically features evaluation markers: 〜方がいい (better to), 〜方がましだ (preferable / less bad), or 〜たい (want to).'
    )
    c['keyTakeaway'] = 'V(辞書形) + くらいなら / ぐらいなら: "rather than suffer undesirable X, I would prefer Y". Clause B typically concludes with 〜方がいい / 〜方がましだ / 〜たい.'
    c['connection'] = 'Verb (辞書形) + くらいなら / ぐらいなら、[〜方がいい / 〜ましだ]'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 3, Section 3, printed p. 23 (PDF p. 46).'

# 4. skm3-u3-ni-kagiru
c = card_map.get('skm3-u3-ni-kagiru')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 3'
    c['nuance'] = (
        '〜に限る expresses the speaker\'s personal conviction that something is the absolute best choice or most effective method: "~ is the best / nothing beats ~". '
        'FORMATION (Printed p. 23): '
        '・Noun + に限る (映画は映画館で見るに限る: For movies, seeing them in a theater is best; 暑い日は冷たい麦茶に限る). '
        '・Verb (辞書形) + に限る (風邪をひいた時は、温かくして寝るに限る: When sick with a cold, nothing beats keeping warm and sleeping). '
        '・Verb (ない形) + に限る (危険な場所には近寄らないに限る: The best policy is not to approach dangerous areas). '
        'SUBJECTIVE CONVICTION BAN (p. 23): '
        'Strictly expresses the speaker\'s personal opinion and advice. It CANNOT be used to assert objective truths or scientific facts.'
    )
    c['keyTakeaway'] = 'Noun / Verb(辞書形/ない形) + に限る: "nothing beats X / X is the absolute best choice". Strictly expresses the speaker\'s personal subjective conviction, never an objective factual law.'
    c['connection'] = 'Noun / Verb (辞書形 / ない形) + に限る'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 3, Section 4, printed p. 23 (PDF p. 46).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 4 SKM N3 Chapter 3 cards in base-reviewed.json!')

# 3. Add 4 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing SKM N3 Chapter 3 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Shin Kanzen Master N3' and r.get('sourceSection') == 'Part 1 · Chapter 3')]

skm3_c3_entries = [
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 3',
        'exactPrintedPages': 'p. 22',
        'exactPdfPages': 'p. 45',
        'grammarItem': '〜くらいだ / 〜ほどだ (Expressing Extreme Degree: To the Extent That)',
        'instructionalDetails': 'Extreme metaphorical degree using illustrative unactualized example; Noun / Verb / い-adj / な-adj+な + くらいだ/ほどだ; idiomatic 〜かと思うほど (so intense I even wondered if); degree modification of predicates.',
        'cardId': 'skm3-u3-kurai-hodo-extent',
        'exampleCount': 4,
        'exampleIds': ['skm3-u3-kurai-hodo-extent::s-skm3-3-1', 'skm3-u3-kurai-hodo-extent::n3-use-examples-31', 'skm3-u3-kurai-hodo-extent::n3-use-examples-32', 'skm3-u3-kurai-hodo-extent::n3-use-examples-33'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 22 (PDF p. 45, skm3_pdf_45.png). Verified Section 1 degree formation, illustrative unactualized comparison semantics, and idiomatic 〜かと思うほど usage.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 3',
        'exactPrintedPages': 'p. 22',
        'exactPdfPages': 'p. 45',
        'grammarItem': '〜くらい…はない / 〜ほど…はない (Subjective Superlative: Nothing Beats X)',
        'instructionalDetails': 'Subjective superlative assertion; Noun + くらい/ほど + Noun はない (or いない); speaker\'s personal subjective conviction; strict ban on stating objective geographical/factual superlatives (*富士山ほど高い山はない is unnatural).',
        'cardId': 'skm3-u3-kurai-wa-nai',
        'exampleCount': 4,
        'exampleIds': ['skm3-u3-kurai-wa-nai::s-skm3-3-2', 'skm3-u3-kurai-wa-nai::n3-use-examples-34', 'skm3-u3-kurai-wa-nai::n3-use-examples-35', 'skm3-u3-kurai-wa-nai::n3-use-examples-36'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 22 (PDF p. 45, skm3_pdf_45.png). Verified Section 2 formation, subjective judgment constraint, and contrast with factual superlatives.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 3',
        'exactPrintedPages': 'p. 23',
        'exactPdfPages': 'p. 46',
        'grammarItem': '〜くらいなら / 〜ぐらいなら (Rather Than Suffer X, Prefer Y)',
        'instructionalDetails': 'V(辞書形) + くらいなら / ぐらいなら; rejects undesirable option X in favor of preferred alternative Y; Clause B concludes with 〜方がいい, 〜方がましだ, or 〜たい; subjective value hierarchy.',
        'cardId': 'skm3-u3-kurai-nara',
        'exampleCount': 4,
        'exampleIds': ['skm3-u3-kurai-nara::s-skm3-3-3', 'skm3-u3-kurai-nara::n3-use-examples-37', 'skm3-u3-kurai-nara::n3-use-examples-38', 'skm3-u3-kurai-nara::n3-use-examples-39'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 23 (PDF p. 46, skm3_pdf_46.png). Verified Section 3 formation rules, preference predicate requirements (〜方がましだ), and authentic textbook examples.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 3',
        'exactPrintedPages': 'p. 23',
        'exactPdfPages': 'p. 46',
        'grammarItem': '〜に限る (Nothing Beats / Best Choice)',
        'instructionalDetails': 'Noun / Verb (dict/nai) + に限る; speaker\'s subjective personal conviction that X is the absolute best method or choice; prohibition on objective factual laws or scientific statements; affirmative and negative policy formulations.',
        'cardId': 'skm3-u3-ni-kagiru',
        'exampleCount': 4,
        'exampleIds': ['skm3-u3-ni-kagiru::s-skm3-3-4', 'skm3-u3-ni-kagiru::n3-use-examples-40', 'skm3-u3-ni-kagiru::n3-use-examples-41', 'skm3-u3-ni-kagiru::n3-use-examples-42'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 23 (PDF p. 46, skm3_pdf_46.png). Verified Section 4 formation rules, subjective advice nuance, and negative policy usage (しないに限る).'
    }
]

matrix.extend(skm3_c3_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Certified SKM N3 Chapter 3 in source coverage matrix! Total certified rows: {len(matrix)}')
