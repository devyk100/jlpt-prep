import json

# 1. Update chapterExercises.json for Lesson 23 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

has_q11 = any(q.get('id') == 'g2-l23-ex-11' for q in exercises)
if not has_q11:
    q11 = {
        'id': 'g2-l23-ex-11',
        'bookId': 'genki-2',
        'chapter': 'Lesson 23',
        'type': 'multiple-choice',
        'context': 'Reluctant waiting: Being kept waiting in the freezing cold for an entire hour because a friend overslept.',
        'question': '友だちが寝坊したため、寒い駅前で一時間も（　　）。',
        'translation': 'Because my friend overslept, I was kept waiting at the cold station front for a whole hour.',
        'options': [
            '待たされた',
            '待たせた',
            '待たせられた',
            '待たれた'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-g2-23-43',
        'grammarPointTitle': '使役受身',
        'explanation': {
            'overall': 'In standard modern Japanese, u-verbs (except those ending in す) form the contracted causative-passive by dropping -u and adding -asareru: 待つ → 待たされる (past: 待たされた: was made to wait / kept waiting against one\'s will). 待たせた is causative active ("I made someone wait"), while 待たれた is passive.',
            'options': [
                {
                    'text': '待たされた',
                    'isCorrect': True,
                    'reason': 'Correct. Standard contracted causative-passive form of 待つ is 待たされる (past: 待たされた).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '待たせた',
                    'isCorrect': False,
                    'reason': 'Incorrect. 待たせた is the causative active form ("I made someone wait"), reversing the roles.',
                    'trapCategory': 'voice'
                },
                {
                    'text': '待たせられた',
                    'isCorrect': False,
                    'reason': 'Incorrect. Uncontracted -aserareru is rarely used for regular u-verbs in modern Japanese.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '待たれた',
                    'isCorrect': False,
                    'reason': 'Incorrect. 待たれた is simple passive, not expressing the coercive delay of causative-passive.',
                    'trapCategory': 'voice'
                }
            ]
        },
        'hint': 'What is the contracted causative-passive form of the u-verb 待つ meaning "was made to wait"?'
    }
    exercises.append(q11)

has_q12 = any(q.get('id') == 'g2-l23-ex-12' for q in exercises)
if not has_q12:
    q12 = {
        'id': 'g2-l23-ex-12',
        'bookId': 'genki-2',
        'chapter': 'Lesson 23',
        'type': 'multiple-choice',
        'context': 'Office software inquiry: Asking a colleague to show you how to operate a newly installed software program.',
        'question': 'すみません、この新しいソフトの（　　）を教えてくれませんか。',
        'translation': 'Excuse me, could you please teach me how to use this new software?',
        'options': [
            '使い方',
            '使う方',
            '使って方',
            '使われ方'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-g2-23-45',
        'grammarPointTitle': '〜まで・〜方',
        'explanation': {
            'overall': 'To express "way of doing / how to do...", attach the suffix 方（かた） to the verb masu-stem: 使う (stem 使い) + 方 → 使い方 (how to use / way of using). Associated objects take の (ソフトの使い方).',
            'options': [
                {
                    'text': '使い方',
                    'isCorrect': True,
                    'reason': 'Correct. Verb masu-stem 使い + 方 forms the compound noun 使い方 ("how to use").',
                    'trapCategory': 'formation'
                },
                {
                    'text': '使う方',
                    'isCorrect': False,
                    'reason': 'Incorrect. Dictionary form before 方 means "the person who uses", not "how to use".',
                    'trapCategory': 'formation'
                },
                {
                    'text': '使って方',
                    'isCorrect': False,
                    'reason': 'Incorrect. Te-form cannot precede the suffix 方 (*使って方 is ungrammatical).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '使われ方',
                    'isCorrect': False,
                    'reason': 'Incorrect. 使われ方 means "how it is used (passive reception)", not how to operate it.',
                    'trapCategory': 'voice'
                }
            ]
        },
        'hint': 'What verb stem form connects with 方（かた） to mean "how to do"?'
    }
    exercises.append(q12)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for Lesson 23!')

# 2. Enrich base-reviewed.json for Lesson 23 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. added-g2-23-43 (使役受身)
c = card_map.get('added-g2-23-43')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 23'
    c['nuance'] = (
        'Causative-passive sentences (使役受身文 shieki-ukemi-bun) express that you were forced to do, or coerced/harassed into doing, something against your will ("made to do"). '
        'Sentence structure: [Puppet は] [Puppet Master に] [Action を] V-causative-passive (私は彼女に車を洗わされました: I was tricked by my girlfriend into washing her car; 先生に立たされました: I was made to stand by the teacher). '
        'CONJUGATION PARADIGM (pp. 254-255): '
        '・Ru-verbs: Drop -ru, add -saserareru (食べる → 食べさせられる: made to eat; 見る → 見させられる). '
        '・U-verbs ending in す: Drop -u, add -aserareru (話す → 話させられる; never contracts!). '
        '・All other u-verbs (Contracted Short Form): Drop -u, add -asareru (行く → 行かされる; 待つ → 待たされる; 飲む → 飲まされる; 買う → 買わされる; 取る → 取らされる; 書く → 書かされる). '
        '・Irregular verbs: くる → こさせられる, する → させられる. '
        'All causative-passive verbs conjugate regularly as ru-verbs (飲まされた, 飲まされない, etc.).'
    )
    c['keyTakeaway'] = 'Causative-passive: forced to do against one\'s will. Ru: -saserareru. U-verbs (except す): contracted -asareru (行かされる, 待たされる, 飲まされる). Verbs in す: -aserareru (話させられる). する→させられる.'
    c['connection'] = 'Ru: -saserareru | U (non-su): -asareru | す-verbs: -aserareru | [Puppet は] [Puppet Master に] V-causative-passive'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 23, Grammar 1, printed pp. 254-255 (PDF pp. 262-263).'

# 2. g2-l23-temo-even-if (~ても / 〜でも)
c = card_map.get('g2-l23-temo-even-if')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 23'
    c['nuance'] = (
        'Clause A + ても、Clause B expresses concessive condition: "B, even if A" (B is true in spite of condition A, or B does not change regardless of A). '
        'FORMATION (pp. 256-257): '
        '・Verbs (Affirmative): V-て + も (雨が降っても、バーベキューをします: We will have a barbecue even if it rains; 食べても). '
        '・Verbs (Negative): V-なくて + も (行かなくてもいいです; 食べなくても). '
        '・い-adjectives: Drop -i, add -くても (暑くても、エアコンをつけません: I won\'t turn on the AC even if it\'s hot; 高くても買います). Negative: -くなくても. '
        '・な-adjectives & Nouns: + でも (嫌いでも食べなさい: Eat it even if you hate it; 雨でも行きます: I\'ll go even if it rains; 子供でも分かります). Negative: じゃなくても. '
        'CONTRAST WITH 〜たら: '
        'たら indicates an if-then dependency (雨が降ったらバーベキューをしません: If it rains, we won\'t BBQ), whereas ても asserts that consequence B will happen regardless (雨が降ってもバーベキューをします).'
    )
    c['keyTakeaway'] = '〜ても / 〜でも: "even if A, B". Formation: V-ても / V-なくても; い-adj + くても; な-adj/Noun + でも. Expresses that consequence B holds regardless of condition A.'
    c['connection'] = 'V-て + も | い-adj(i->kute) + も | な-adj/Noun + でも'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 23, Grammar 2, printed pp. 256-257 (PDF pp. 264-265).'

# 3. g2-l23-koto-ni-suru-naru (~ことにする vs 〜ことになる)
c = card_map.get('g2-l23-koto-ni-suru-naru')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 23'
    c['nuance'] = (
        'This pattern contrasts personal conscious decisions against externally emerging arrangements: '
        '(1) V(short present) + ことにする ("decide to do", p. 257): '
        '・Describes a personal conscious choice made by the speaker (毎日ジョギングすることにしました: I have decided to jog every day; お酒をやめることにしました: I decided to quit drinking). '
        '・Negative decision: V-ないことにする (行かないことにしました: I decided not to go). '
        '(2) V(short present) + ことになる ("it has been decided that / turns out that", p. 258): '
        '・Describes an institutional decision, schedule, corporate assignment, or external circumstance outside one\'s individual agency (来月から大阪支社へ転勤することになりました: It has been decided that I will transfer to the Osaka branch; 会議が中止になることになりました: It turns out the meeting is canceled).'
    )
    c['keyTakeaway'] = '〜ことにする: personal internal decision ("I decided to do"). 〜ことになる: external arrangement / institutional outcome ("it has been decided that / turns out that"). Follows short present forms.'
    c['connection'] = 'V(short present) + ことにする (personal) | V(short present) + ことになる (external)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 23, Grammar 3, printed pp. 257-258 (PDF pp. 265-266).'

# 4. added-g2-23-44 (~ことにしている)
c = card_map.get('added-g2-23-44')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 23'
    c['nuance'] = (
        'V(short present) + ことにしている expresses doing something as a regular habitual practice based on personal resolve: "I make it a rule to... / I always make sure to...". '
        'The speaker has made up their mind to do (or not do) something and conscientiously sticks to that resolution as a sustained personal routine (p. 258). '
        '・Affirmative habit: 毎晩十一時までに寝ることにしています (I make it a rule to go to bed by 11 every night; 毎日野菜を食べることにしています). '
        '・Negative habit: V-ないことにしている (お酒を飲まないことにしています: I have made this firm decision not to drink and have strictly followed it; 夜はコーヒーを飲まないことにしています).'
    )
    c['keyTakeaway'] = 'V(short present) + ことにしている: personal ongoing policy / habitual rule ("make it a rule to do / make sure not to do"). Based on self-imposed discipline.'
    c['connection'] = 'V(short present aff/neg) + ことにしている'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 23, Grammar 3, printed p. 258 (PDF p. 266).'

# 5. added-g2-23-45 (~まで・〜方)
c = card_map.get('added-g2-23-45')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 23'
    c['nuance'] = (
        'This section encompasses temporal boundary marking with 〜まで and method nominalization with 〜方: '
        '(1) 〜まで ("until", pp. 258-259): '
        '・Clause A (short present affirmative) + まで、Clause B: Describes an action/state B that continues up to the moment change A coincides with its end. '
        '・STRICT TENSE CONSTRAINT: The verb in clause A is always in the short present affirmative form, even if the entire sentence describes a past event (雨がやむまで、カフェで待ちました: I waited at the café until the rain stopped; never *やんだまで). '
        '・Contrast with までに: まで = continuous duration until A; までに = deadline by which action occurs. '
        '(2) 〜方（かた） ("the way of doing / how to do", p. 259): '
        '・V(masu-stem) + 方 forms a compound noun denoting method (泳ぎ方: how to swim; 使い方: how to use; 考え方: way of thinking; 読み方: way of reading). '
        '・Suru-compounds: [Noun の] し方 (勉強の仕方: how to study; 運転の仕方: how to drive). '
        '・SYNTACTIC PARTICLES RULE: Any noun originally marked with object particles (を, に, で) is obligatorily marked with の before 〜方 (漢字を書く → 漢字の書き方; ソフトを使う → ソフトの使い方; never *漢字を書き方).'
    )
    c['keyTakeaway'] = '〜まで = until (verb before まで is strictly short present affirmative: やむまで待った). 〜方 = way of doing (V-stem + 方; object takes の: 漢字の書き方, 使い方).'
    c['connection'] = 'V(short present affirmative) + まで | [Noun の] V(masu-stem) + 方'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 23, Grammar 4 & 5, printed pp. 258-259 (PDF pp. 266-267).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 5 Lesson 23 cards in base-reviewed.json!')

# 3. Add 5 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing Lesson 23 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Genki II (3rd Ed.)' and r.get('sourceSection') == 'Lesson 23')]

l23_entries = [
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 23',
        'exactPrintedPages': 'pp. 254-255',
        'exactPdfPages': 'pp. 262-263',
        'grammarItem': '使役受身 (Causative-Passive Sentences: Coerced Action)',
        'instructionalDetails': 'Coerced into doing against one\'s will; Ru: -saserareru; U-verbs (non-su): contracted -asareru (行かされる, 待たされる, 飲まされる); す-verbs: -aserareru (話させられる); する→させられる; [Puppet は] [Puppet Master に] [Action を] V-causative-passive.',
        'cardId': 'added-g2-23-43',
        'exampleCount': 4,
        'exampleIds': ['added-g2-23-43-example', 'added-g2-23-43::genki2-use-examples-110', 'added-g2-23-43::genki2-use-examples-111', 'added-g2-23-43::genki2-use-examples-112'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 254-255 (PDF pp. 262-263, g2_p262_printed254.png, g2_p263_printed255.png). Verified causative-passive conjugation table, contracted -asareru rule, non-contracting す-verbs constraint, and puppet master case marking.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 23',
        'exactPrintedPages': 'pp. 256-257',
        'exactPdfPages': 'pp. 264-265',
        'grammarItem': '〜ても / 〜でも (Concessive Conditional: Even If / Even Though)',
        'instructionalDetails': 'B holds true even in case of A; affirmative: V-ても, い-adj + くても, な-adj/Noun + でも; negative: V-なくても, い-adj + くなくても, な-adj/Noun + じゃなくても; contrast with たら (independence vs dependency).',
        'cardId': 'g2-l23-temo-even-if',
        'exampleCount': 3,
        'exampleIds': ['g2-l23-temo-even-if::s-g2-23-1', 'g2-l23-temo-even-if::genki2-use-examples-113', 'g2-l23-temo-even-if::genki2-use-examples-114'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 256-257 (PDF pp. 264-265, g2_p264_printed256.png, g2_p265_printed257.png). Verified concessive condition formation, negative forms table, and contrast with たら.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 23',
        'exactPrintedPages': 'pp. 257-258',
        'exactPdfPages': 'pp. 265-266',
        'grammarItem': '〜ことにする vs 〜ことになる (Personal Decision vs Outside Emergence)',
        'instructionalDetails': 'V(short present) + ことにする = personal internal conscious decision; V(short present) + ことになる = institutional arrangement or external emergence outside speaker agency; negative forms V-ないことにする.',
        'cardId': 'g2-l23-koto-ni-suru-naru',
        'exampleCount': 3,
        'exampleIds': ['g2-l23-koto-ni-suru-naru::s-g2-23-2', 'g2-l23-koto-ni-suru-naru::genki2-use-examples-115', 'g2-l23-koto-ni-suru-naru::genki2-use-examples-116'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 257-258 (PDF pp. 265-266, g2_p265_printed257.png, g2_p266_printed258.png). Verified contrast between personal conscious decision (ことにする) and institutional assignment (ことになる).'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 23',
        'exactPrintedPages': 'p. 258',
        'exactPdfPages': 'p. 266',
        'grammarItem': '〜ことにしている (Personal Habitual Policy / Rule)',
        'instructionalDetails': 'V(short present aff/neg) + ことにしている = self-imposed sustained personal policy / habit ("make it a rule to do / make sure not to do"); denotes disciplined ongoing routine.',
        'cardId': 'added-g2-23-44',
        'exampleCount': 4,
        'exampleIds': ['added-g2-23-44-example', 'added-g2-23-44::genki2-use-examples-117', 'added-g2-23-44::genki2-use-examples-118', 'added-g2-23-44::genki2-use-examples-119'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 258 (PDF p. 266, g2_p266_printed258.png). Verified regular habitual practice nuance and affirmative/negative habit examples.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 23',
        'exactPrintedPages': 'pp. 258-259',
        'exactPdfPages': 'pp. 266-267',
        'grammarItem': '〜まで・〜方 (Until Event Coincides & Way of Doing / How to Do)',
        'instructionalDetails': 'Clause A + まで (verb before まで is strictly short present affirmative: 雨がやむまで待った); contrast with deadline までに; V(masu-stem) + 方 (method noun: 使い方, 泳ぎ方); suru-compounds [Noun の] し方; object takes particle の (漢字の書き方).',
        'cardId': 'added-g2-23-45',
        'exampleCount': 4,
        'exampleIds': ['added-g2-23-45-example', 'added-g2-23-45::genki2-use-examples-120', 'added-g2-23-45::genki2-use-examples-121', 'added-g2-23-45::genki2-use-examples-122'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 258-259 (PDF pp. 266-267, g2_p266_printed258.png, g2_p267_printed259.png). Verified まで present tense restriction and 〜方 masu-stem formation with mandatory の case marking.'
    }
]

matrix.extend(l23_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Certified Lesson 23 in source coverage matrix! Total certified rows: {len(matrix)}')
