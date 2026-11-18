import json

# 1. Update chapterExercises.json for Lesson 13 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

has_q11 = any(q.get('id') == 'g2-l13-ex-11' for q in exercises)
if not has_q11:
    q11 = {
        'id': 'g2-l13-ex-11',
        'bookId': 'genki-2',
        'chapter': 'Lesson 13',
        'type': 'multiple-choice',
        'context': 'Listing reasons: Praising Professor Yamashita for being kind and having good explanations.',
        'question': '山下先生は教えるのが上手（　　）、親切（　　）、大好きな先生です。',
        'translation': 'Professor Yamashita is good at teaching and is kind, so I love him.',
        'options': [
            'だし・だし',
            'し・し',
            'な・な',
            'ので・ので'
        ],
        'correctIndex': 0,
        'grammarPointId': 'g2-l13-shi-reasons',
        'grammarPointTitle': '〜し、〜し (Listing Multiple Parallel Reasons)',
        'explanation': {
            'overall': 'When listing reasons with 〜し after a な-adjective or noun in the present tense affirmative, mandatory だ must be inserted: な-adj + だし (上手だし、親切だし).',
            'options': [
                {
                    'text': 'だし・だし',
                    'isCorrect': True,
                    'reason': 'Correct. な-adjectives in present affirmative must take だ before し (上手だし, 親切だし).',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'し・し',
                    'isCorrect': False,
                    'reason': 'Incorrect. Attaching し directly to な-adjective stems without だ (*上手し) is strictly ungrammatical.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'な・な',
                    'isCorrect': False,
                    'reason': 'Incorrect. な connects to nouns, not clauses listing reasons.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'ので・ので',
                    'isCorrect': False,
                    'reason': 'Incorrect. ので is not repeated in parallel lists like し.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'What copula form must precede し when attaching to な-adjectives in the present affirmative?'
    }
    exercises.append(q11)

has_q12 = any(q.get('id') == 'g2-l13-ex-12' for q in exercises)
if not has_q12:
    q12 = {
        'id': 'g2-l13-ex-12',
        'bookId': 'genki-2',
        'chapter': 'Lesson 13',
        'type': 'multiple-choice',
        'context': 'Direct visual observation: Looking at a flower in full bloom and commenting that it is pretty.',
        'question': '庭の花を見て、「わあ、（　　）ね」と言いました。',
        'translation': 'Looking at the flowers in the garden, I said, "Wow, they are pretty!"',
        'options': [
            'きれいだ',
            'きれいそう',
            'きれくそう',
            'きれいだそう'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-g2-13-20',
        'grammarPointTitle': '〜そうです：様子 (Look like / Seem - Conjectural Appearance)',
        'explanation': {
            'overall': 'Genki II Lesson 13 explicitly notes: 〜そうです is used when we lack conclusive evidence. For adjectives where visual evidence is self-evident (such as きれい: pretty/clean, or かわいい: cute), you cannot use そうです (*きれいそうです is wrong). You say きれいですね.',
            'options': [
                {
                    'text': 'きれいだ',
                    'isCorrect': True,
                    'reason': 'Correct. Direct visual perception uses the base adjective (きれいですね), not conjectural そうです.',
                    'trapCategory': 'context'
                },
                {
                    'text': 'きれいそう',
                    'isCorrect': False,
                    'reason': 'Incorrect. Explicit textbook constraint: *きれいそうです is prohibited because visual beauty is immediately self-evident.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'きれくそう',
                    'isCorrect': False,
                    'reason': 'Incorrect. Ungrammatical formation (きれい is a な-adjective).',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'きれいだそう',
                    'isCorrect': False,
                    'reason': 'Incorrect. だそうです is hearsay (reported speech), not first-hand visual perception.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Can you use conjectural 〜そうです with adjectives like きれい whose quality is directly self-evident to sight?'
    }
    exercises.append(q12)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for Lesson 13!')

# 2. Enrich base-reviewed.json for Lesson 13 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. g2-l13-potential
c = card_map.get('g2-l13-potential')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 13'
    c['nuance'] = (
        'Potential verbs express that an agent has the ability to do an action ("can do"), or that circumstances permit it ("is possible"). '
        'Conjugation rules: '
        '(1) Ru-verbs: drop -ru and add -rareru (見る → 見られる, 食べる → 食べられる). Spoken casual allows "ra-less" forms (見れる, 食べれる), though school grammar flags them (Footnote 1). '
        '(2) U-verbs: drop -u and add -eru (行く → 行ける, 泳ぐ → 泳げる, 話す → 話せる, 待つ → 待てる, 飲む → 飲める, 買う → 買える). '
        '(3) Irregular verbs: 来る (くる) → こられる (ra-less: これる); する → できる. '
        'Potential verbs themselves conjugate as regular Ru-verbs (話せる、話せない、話せます、話せません、話せた、話せて). '
        'PARTICLE ALTERNATION: Verbs that take direct object を can take EITHER を OR が when converted to the potential (漢字を読む → 漢字が読める OR 漢字を読める). '
        'Special case: できる takes が almost exclusively (仕事ができる). All particles other than を (に, で, へ, etc.) remain unchanged (山に登れる).'
    )
    c['keyTakeaway'] = 'Ru-verbs: -rareru (見られる). U-verbs: -eru (行ける, 読める). くる→こられる, する→できる. Direct object を can switch to が (漢字が読める). Other particles do not change.'
    c['connection'] = 'Ru: V-stem + られる | U: V (u->e) + る | くる→こられる | する→できる'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 13, Grammar 1, printed pp. 26-28 (PDF pp. 34-36).'

# 2. g2-l13-shi-reasons
c = card_map.get('g2-l13-shi-reasons')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 13'
    c['nuance'] = (
        'Used to mention two or more parallel reasons leading up to a situation or conclusion: (reason 1) し、(reason 2) し、(situation). '
        'Predicate form: Usually follows predicates in the short form (面白いし、物価が安いし). In polite speech, can follow long forms (好きですし). '
        'Single し: When only one し clause is cited, it implies that it is not the only reason for the situation. '
        'MANDATORY だ RULE: For な-adjectives and Nouns in the present tense affirmative, mandatory だ must precede し (親切だし, 学生だし! NEVER *親切し or *学生し). '
        'い-adjectives take し directly (面白いし).'
    )
    c['keyTakeaway'] = 'Listing reasons: [Reason 1]し、[Reason 2]し、[Situation]. Short form predicate. MANDATORY: な-adj and Nouns take だし (親切だし, 学生だし; never bare stem + し).'
    c['connection'] = 'Short form + し | な-adj / Noun + だし'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 13, Grammar 2, printed pp. 28-29 (PDF pp. 36-37).'

# 3. added-g2-13-20 (~そうです: 様子)
c = card_map.get('added-g2-13-20')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 13'
    c['nuance'] = (
        'Add そうです to adjective bases to state a conjectural impression based on visual/intuitive appearance ("it looks like / seems [property]"). '
        'Conjugation rules: '
        '(1) い-adjectives: drop final い + そうです (おいしい → おいしそうです, 寒そう). '
        'CRITICAL EXCEPTION: The adjective いい changes to よさそう (NOT *いそう ❌). '
        '(2) な-adjectives: drop な + そうです (元気[な] → 元気そうです, 暇そう). '
        '(3) Negative appearance: い-adj negative ない changes to なさそう (よくなさそう, 面白くなさそう), or negate the ending (おいしそうじゃないです). '
        '(4) Verbs: verb stem + そうです (雨が降りそうです: it looks like it will rain). '
        'CRITICAL VISUAL CONSTRAINT: 〜そうです is used when we lack conclusive evidence (e.g. before tasting food). '
        'For adjectives where visual evidence is already self-evident to the eyes, such as きれい (pretty/clean) or かわいい (cute), you CANNOT use そうです: *きれいそうです is strictly prohibited. Say きれいですね.'
    )
    c['keyTakeaway'] = 'い-adj (drop い) + そうです (おいしそう). EXCEPTION: いい→よさそう. な-adj (drop な) + そうです (元気そう). Verbs: stem + そうです (降りそう). BAN on self-evident visual words (*きれいそう is wrong).'
    c['connection'] = 'い-adj (drop い) + そうです | いい → よさそうです | な-adj stem + そうです | V-stem + そうです'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 13, Grammar 3, printed pp. 29-30 (PDF pp. 37-38).'

# 4. g2-l13-te-miru
c = card_map.get('g2-l13-te-miru')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 13'
    c['nuance'] = (
        'The te-form of a verb plus the helping auxiliary みる expresses "doing something tentatively" or "trying something out to see what happens" (testing the waters when outcome is uncertain). '
        'Formation: V-て + みる (e.g. 食べてみる, 書いてみる, 行ってみる, 着てみる). '
        'Conjugation: みる conjugates as a regular Ru-verb (〜てみます、〜てみた、〜てみてください). '
        'ORTHOGRAPHY RULE: Unlike the main lexical verb 見る (to look/see), the auxiliary 〜てみる is ALWAYS written in hiragana.'
    )
    c['keyTakeaway'] = 'V-て + みる (try doing to see outcome). みる conjugates as Ru-verb. Orthography: Always write auxiliary 〜てみる in hiragana (never *〜て見る).'
    c['connection'] = 'V-て形 + みる / みます / みて / みた'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 13, Grammar 4, printed p. 30 (PDF p. 38).'

# 5. g2-l13-nara-conditional
c = card_map.get('g2-l13-nara-conditional')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 13'
    c['nuance'] = (
        'X (noun) なら Y (predicate) introduces a conditional context where predicate Y applies specifically to X and is not more generally valid. '
        'Semantic core: Contrast and Limitation. '
        'It singles out an item from the conversational context and introduces a positive statement about that specific item while contrasting it with other alternatives (e.g. チリなら行きましたが、ブラジルは行ったことがありません: If it\'s Chile, yes; but Brazil, no; ひらがななら読めます: If it\'s in hiragana, I can read it). '
        'PARTICLE RULE (Footnote 6): Particles は, が, を never appear before なら (they are dropped). Particles like に, で, から may optionally be retained (チリになら).'
    )
    c['keyTakeaway'] = 'Noun + なら (contextual limitation: If it is X / As for X). Singles out an item with contrastive positive applicability. Particles は/が/を are dropped before なら.'
    c['connection'] = 'Noun + なら | Noun + [に/で/から] + なら'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 13, Grammar 5, printed p. 31 (PDF p. 39).'

# 6. added-g2-13-21 (期間に回数)
c = card_map.get('added-g2-13-21')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 13'
    c['nuance'] = (
        'Framework for expressing the frequency of events or duration of activities over a period of time: (period) に (frequency / duration). '
        'Examples: 一週間に三回 (three times a week), 一日に三時間 (three hours a day), 一か月に三日か四日 (three or four days a month). '
        'Question pattern: (period) に何回 [V] ますか (e.g. 一週間に何回髪を洗いますか: How many times a week do you wash your hair?).'
    )
    c['keyTakeaway'] = '(period) に (frequency / duration) = [frequency] per [period] (e.g. 一週間に三回: 3 times a week; 一日に一時間: 1 hour a day).'
    c['connection'] = '(Period) に (Frequency: 〜回) | (Period) に (Duration: 〜時間)'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 13, Grammar 6, printed pp. 31-32 (PDF pp. 39-40).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 6 Lesson 13 cards in base-reviewed.json!')

# 3. Add 6 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing Lesson 13 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Genki II (3rd Ed.)' and r.get('sourceSection') == 'Lesson 13')]

l13_entries = [
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 13',
        'exactPrintedPages': 'pp. 26-28',
        'exactPdfPages': 'pp. 34-36',
        'grammarItem': '可能形 (Potential Verbs: Ability & Possibility)',
        'instructionalDetails': 'Ru-verbs: -rareru (見られる, 食べられる; spoken ra-less -reru); U-verbs: -eru (行ける, 読める, 泳げる); irregulars: くる→こられる, する→できる; potential verbs conjugate as Ru-verbs; direct object を standardly switches to が (漢字が読める); できる takes が; other particles (に, で, へ) remain unchanged.',
        'cardId': 'g2-l13-potential',
        'exampleCount': 3,
        'exampleIds': ['g2-l13-potential::s-g2-13-1', 'g2-l13-potential::genki2-use-examples-1', 'g2-l13-potential::genki2-use-examples-2'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 26-28 (PDF pp. 34-36, p34_printed26.png, p35_printed27.png, p36_printed28.png). Verified potential conjugation paradigm, ra-less note, and を -> が particle alternation.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 13',
        'exactPrintedPages': 'pp. 28-29',
        'exactPdfPages': 'pp. 36-37',
        'grammarItem': '〜し、〜し (Listing Multiple Parallel Reasons)',
        'instructionalDetails': '[Reason 1]し、[Reason 2]し、[Situation] for multiple parallel reasons; short form predicates; polite long forms allowed; single し implies additional unstated reasons; MANDATORY だ insertion for な-adjectives and nouns in present affirmative (親切だし, 学生だし; ban on bare stem *親切し).',
        'cardId': 'g2-l13-shi-reasons',
        'exampleCount': 3,
        'exampleIds': ['g2-l13-shi-reasons::s-g2-13-2', 'g2-l13-shi-reasons::genki2-use-examples-3', 'g2-l13-shi-reasons::genki2-use-examples-4'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 28-29 (PDF pp. 36-37, p36_printed28.png, p37_printed29.png). Verified multiple reason coordination and mandatory だ insertion for な-adjectives and nouns.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 13',
        'exactPrintedPages': 'pp. 29-30',
        'exactPdfPages': 'pp. 37-38',
        'grammarItem': '〜そうです：様子 (Look like / Seem - Conjectural Appearance)',
        'instructionalDetails': 'Adjective stem + そうです for conjectural appearance based on impressions; い-adj (drop い) + そうです; irregular いい→よさそう (ban on *いそう); な-adj (drop な) + そうです; negative なさそう / 〜そうじゃないです; verb stem + そうです; CRITICAL RESTRICTION against self-evident visual words (*きれいそう and *かわいいそう are prohibited; say きれいですね).',
        'cardId': 'added-g2-13-20',
        'exampleCount': 7,
        'exampleIds': [
            'added-g2-13-20-example',
            'added-g2-13-20::genki2-use-examples-9',
            'added-g2-13-20::genki2-use-examples-10',
            'added-g2-13-20::genki2-use-examples-11',
            'added-g2-13-20::merged-genki2-kanoukei::s-g2-13-1',
            'added-g2-13-20::merged-genki2-kanoukei::supp-use-examples-22',
            'added-g2-13-20::merged-genki2-kanoukei::supp-use-examples-23'
        ],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 29-30 (PDF pp. 37-38, p37_printed29.png, p38_printed30.png). Verified adjective stem attachments, いい→よさそう irregular, and explicit prohibition on visually self-evident adjectives like きれい.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 13',
        'exactPrintedPages': 'p. 30',
        'exactPdfPages': 'p. 38',
        'grammarItem': '〜てみる (Trying Out an Action: Doing Something to See)',
        'instructionalDetails': 'V-て + みる for doing something tentatively or testing the waters with unknown outcome; regular Ru-verb conjugation; ORTHOGRAPHY RULE: auxiliary 〜てみる is always written in hiragana (distinguishing from lexical 見る).',
        'cardId': 'g2-l13-te-miru',
        'exampleCount': 3,
        'exampleIds': ['g2-l13-te-miru::s-g2-13-3', 'g2-l13-te-miru::genki2-use-examples-5', 'g2-l13-te-miru::genki2-use-examples-6'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 30 (PDF p. 38, p38_printed30.png). Verified tentative experimental aspect, Ru-verb inflection, and hiragana-only orthography rule.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 13',
        'exactPrintedPages': 'p. 31',
        'exactPdfPages': 'p. 39',
        'grammarItem': 'なら (Contextual Limitation Conditional: If It\'s X / As For X)',
        'instructionalDetails': 'Noun + なら singles out an item from context with contrast and limitation (チリなら行きましたが、ブラジルは行ったことがありません); affirmative/positive assertion on the singled-out item; particle rule (Footnote 6): は, が, を are dropped before なら; に, で, から may be retained.',
        'cardId': 'g2-l13-nara-conditional',
        'exampleCount': 3,
        'exampleIds': ['g2-l13-nara-conditional::s-g2-13-4', 'g2-l13-nara-conditional::genki2-use-examples-7', 'g2-l13-nara-conditional::genki2-use-examples-8'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 31 (PDF p. 39, p39_printed31.png). Verified contrastive limitation semantics, positive context restriction, and particle dropping behavior.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 13',
        'exactPrintedPages': 'pp. 31-32',
        'exactPdfPages': 'pp. 39-40',
        'grammarItem': '期間に回数 (Frequency over a Period: 〜に〜回)',
        'instructionalDetails': '(period) に (frequency / duration) framework (一週間に三回: three times a week; 一日に三時間: three hours a day); question pattern with (period) に何回 [V] ますか.',
        'cardId': 'added-g2-13-21',
        'exampleCount': 3,
        'exampleIds': ['added-g2-13-21-example', 'added-g2-13-21::genki2-use-examples-12', 'added-g2-13-21::genki2-use-examples-13'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 31-32 (PDF pp. 39-40, p39_printed31.png, p40_printed32.png). Verified period framework and frequency counters.'
    }
]

matrix.extend(l13_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Successfully updated matrix! Total rows now: {len(matrix)}')
