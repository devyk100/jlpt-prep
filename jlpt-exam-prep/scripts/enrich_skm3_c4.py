import json

# 1. Update chapterExercises.json for SKM N3 Chapter 4 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

new_questions = [
    {
        'id': 'skm3-c4-ex-5',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 4',
        'type': 'multiple-choice',
        'context': 'Characterizing a warm mentor: Explaining that rather than a strict teacher, she feels more like an approachable friend.',
        'question': 'あの先生は厳しい指導者（　　）、まるで何でも話せる友達のようです。',
        'translation': 'Rather than a strict instructor, that teacher is more like a friend you can talk to about anything.',
        'options': [
            'というより',
            'に反して',
            'について',
            'に比べて'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-n3-4-46',
        'grammarPointTitle': '〜一方で・〜というより',
        'explanation': {
            'overall': '〜というより means "rather than say X, it is more accurate to describe it as Y" (指導者というより、友達のようだ: more like a friend than an instructor).',
            'options': [
                {
                    'text': 'というより',
                    'isCorrect': True,
                    'reason': 'Correct. Noun + というより indicates that characterization Y is more appropriate than X.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'に反して',
                    'isCorrect': False,
                    'reason': 'Incorrect. に反して means "contrary to expectations/rules", not a stylistic rephrasing.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'について',
                    'isCorrect': False,
                    'reason': 'Incorrect. について means "regarding / about", not a comparative re-evaluation.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'に比べて',
                    'isCorrect': False,
                    'reason': 'Incorrect. に比べて compares two distinct objects, whereas というより reframes a single person.',
                    'trapCategory': 'nuance'
                }
            ]
        },
        'hint': 'Which phrase means "rather than call it X, it is more like Y"?'
    },
    {
        'id': 'skm3-c4-ex-6',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 4',
        'type': 'multiple-choice',
        'context': 'Economic commentary on dual realities: Noting that while officials declare the economy is recovering, public anxiety is rising.',
        'question': '政府は景気が回復していると発表する（　　）、国民の将来への不安は高まっている。',
        'translation': 'While the government announces that the economy is recovering, on the other hand, public anxiety about the future is increasing.',
        'options': [
            '一方で',
            'とおりに',
            'たびに',
            'ついでに'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-n3-4-46',
        'grammarPointTitle': '〜一方で・〜というより',
        'explanation': {
            'overall': 'Verb (plain form) + 一方で expresses that two contrasting trends or opposing realities coexist concurrently ("while on the one hand A, at the same time on the other hand B").',
            'options': [
                {
                    'text': '一方で',
                    'isCorrect': True,
                    'reason': 'Correct. Plain form + 一方で presents dual concurrent opposing developments.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'とおりに',
                    'isCorrect': False,
                    'reason': 'Incorrect. とおりに indicates accordance/conformity, contradicting the opposing anxiety.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'たびに',
                    'isCorrect': False,
                    'reason': 'Incorrect. たびに indicates repeated recurrence, not dual simultaneous trends.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'ついでに',
                    'isCorrect': False,
                    'reason': 'Incorrect. ついでに indicates side errands, not contradictory social phenomena.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which conjunction means "while on the one hand..., at the same time on the other hand..."?'
    },
    {
        'id': 'skm3-c4-ex-7',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 4',
        'type': 'multiple-choice',
        'context': 'Evaluating solitary lifestyle: Admitting that living alone is wonderfully carefree, but on the flip side, can feel lonely.',
        'question': '一人暮らしは誰にも気兼ねなく生活できて気楽な（　　）、ふとした瞬間に寂しさを感じることもある。',
        'translation': 'Living alone is carefree with no need to worry about anyone, but on the flip side, there are moments when you feel lonely.',
        'options': [
            '反面',
            'わりに',
            'ために',
            'せいで'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u4-hanmen-flipside',
        'grammarPointTitle': '〜反面 (On the Flip Side: Coexisting Contradictory Aspects)',
        'explanation': {
            'overall': 'な-adjective + な + 反面 expresses two coexisting, opposite sides (pros and cons) of the very same situation or entity ("on the flip side / on the other hand").',
            'options': [
                {
                    'text': '反面',
                    'isCorrect': True,
                    'reason': 'Correct. な-adjective + な + 反面 captures the coexisting light and dark sides of living alone.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'わりに',
                    'isCorrect': False,
                    'reason': 'Incorrect. わりに indicates unexpected contrast with a baseline standard ("considering..."), not dual merits/demerits.',
                    'trapCategory': 'nuance'
                },
                {
                    'text': 'ために',
                    'isCorrect': False,
                    'reason': 'Incorrect. ために indicates cause or purpose, not contradictory aspects.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'せいで',
                    'isCorrect': False,
                    'reason': 'Incorrect. せいで attributes blame for a negative result, not balanced coexistence.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which noun connects with [な-adjective + な] to present the coexisting "flip side" of a situation?'
    },
    {
        'id': 'skm3-c4-ex-8',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 4',
        'type': 'multiple-choice',
        'context': 'Corporate proxy attendance: Explaining that you attended the shareholders meeting as a proxy in place of your sick manager.',
        'question': '急な病気で倒れた部長の（　　）、課長である私が代理で株主総会に出席した。',
        'translation': 'In place of the department manager who collapsed from sudden illness, I attended the shareholders meeting as proxy.',
        'options': [
            'かわりに',
            'とおりに',
            '反面に',
            'ついでに'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u4-kawari-ni-exchange',
        'grammarPointTitle': '〜かわりに (In Exchange For / Compensation / Instead Of)',
        'explanation': {
            'overall': 'Noun + の + かわりに expresses substitution: "in place of / acting as a proxy for X".',
            'options': [
                {
                    'text': 'かわりに',
                    'isCorrect': True,
                    'reason': 'Correct. Noun + のかわりに indicates proxy substitution ("in place of the manager").',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'とおりに',
                    'isCorrect': False,
                    'reason': 'Incorrect. のとおりに means "in accordance with", not substitution.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '反面に',
                    'isCorrect': False,
                    'reason': 'Incorrect. 反面 does not take に to mean proxy substitution.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'ついでに',
                    'isCorrect': False,
                    'reason': 'Incorrect. ついでに indicates an incidental side errand, not official proxy substitution.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which word connects with [Noun + の] to mean "in place of / as a substitute for"?'
    },
    {
        'id': 'skm3-c4-ex-9',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 4',
        'type': 'multiple-choice',
        'context': 'Demographic contrast: Highlighting that while urban metropolitan areas see population growth, rural areas suffer depopulation.',
        'question': '大都市圏で若者の人口が増加しているの（　　）、地方の農村では深刻な過疎化が進んでいる。',
        'translation': 'While the youth population is increasing in metropolitan areas, in contrast, severe depopulation is worsening in rural farming villages.',
        'options': [
            'に対して',
            'に関して',
            'にとって',
            'によって'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u4-ni-taishite',
        'grammarPointTitle': '〜に対して (In Contrast To / While X Is..., Y Is...)',
        'explanation': {
            'overall': 'Clause A + のに対して + Clause B clearly contrasts two distinct entities or opposing factual realities: "in contrast to / whereas".',
            'options': [
                {
                    'text': 'に対して',
                    'isCorrect': True,
                    'reason': 'Correct. のに対して contrasts the urban population influx against rural depopulation.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'に関して',
                    'isCorrect': False,
                    'reason': 'Incorrect. に関して means "regarding / concerning", not contrasting two entities.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'にとって',
                    'isCorrect': False,
                    'reason': 'Incorrect. にとって means "from the perspective of", not contrast.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'によって',
                    'isCorrect': False,
                    'reason': 'Incorrect. によって indicates method, cause, or variation ("by / depending on").',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which compound particle after の clearly contrasts two opposing situations ("whereas / in contrast to")?'
    },
    {
        'id': 'skm3-c4-ex-10',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 4',
        'type': 'multiple-choice',
        'context': 'Product comparison: Observing that compared to the older model, the new model is much lighter.',
        'question': '新しく発売されたスマートフォンは、旧型（　　）重さが半分以下になっている。',
        'translation': 'Compared to the older model, the newly released smartphone has its weight reduced to less than half.',
        'options': [
            'に比べて',
            'に反して',
            'において',
            'にとって'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u4-ni-kurabete',
        'grammarPointTitle': '〜に比べて (Compared With / Relative To)',
        'explanation': {
            'overall': 'Noun + に比べて (or に比べると) compares two items and evaluates their difference in degree or quality: "compared with / relative to".',
            'options': [
                {
                    'text': 'に比べて',
                    'isCorrect': True,
                    'reason': 'Correct. Noun + に比べて compares the new phone to the old phone\'s weight.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'に反して',
                    'isCorrect': False,
                    'reason': 'Incorrect. に反して means "contrary to", not a comparative benchmark.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'において',
                    'isCorrect': False,
                    'reason': 'Incorrect. において indicates domain or location ("in / at").',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'にとって',
                    'isCorrect': False,
                    'reason': 'Incorrect. にとって indicates personal standpoint ("for").',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which expression attaches to a noun to mean "compared with / relative to"?'
    },
    {
        'id': 'skm3-c4-ex-11',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 4',
        'type': 'multiple-choice',
        'context': 'Precise sensation description: Remarking that today\'s mountain breeze is more refreshing than truly cold.',
        'question': '山頂の風は、冷たい（　　）むしろ心地よく涼しいくらいだ。',
        'translation': 'The mountain peak breeze is pleasant and cool rather than actually cold.',
        'options': [
            'というより',
            '反面に',
            'わりに',
            'かわりに'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-n3-4-46',
        'grammarPointTitle': '〜一方で・〜というより',
        'explanation': {
            'overall': 'Plain form + というより (often paired with むしろ) means "rather than [adjective], it is more accurate to say...": 冷たいというよりむしろ涼しい (cool rather than cold).',
            'options': [
                {
                    'text': 'というより',
                    'isCorrect': True,
                    'reason': 'Correct. というより むしろ indicates an improved nuance description ("cool rather than cold").',
                    'trapCategory': 'formation'
                },
                {
                    'text': '反面に',
                    'isCorrect': False,
                    'reason': 'Incorrect. 反面 does not pair with むしろ to re-evaluate sensation descriptions.',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'わりに',
                    'isCorrect': False,
                    'reason': 'Incorrect. わりに expresses unexpected contrast with expectation, not nuance correction.',
                    'trapCategory': 'nuance'
                },
                {
                    'text': 'かわりに',
                    'isCorrect': False,
                    'reason': 'Incorrect. かわりに expresses trade-off or compensation, not nuance rephrasing.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which phrase pairs with むしろ to say "more like [nuance] rather than [word]"?'
    },
    {
        'id': 'skm3-c4-ex-12',
        'bookId': 'skm-n3',
        'chapter': 'Part 1 · Chapter 4',
        'type': 'multiple-choice',
        'context': 'Apartment trade-off: Explaining that while the apartment is quite far from the nearest station, in return the rent is remarkably cheap.',
        'question': 'このアパートは最寄り駅から遠い（　　）、部屋が広くて家賃もとても安い。',
        'translation': 'While this apartment is far from the nearest station, in return, the rooms are spacious and the rent is very cheap.',
        'options': [
            'かわりに',
            'うちに',
            'とおりに',
            'たびに'
        ],
        'correctIndex': 0,
        'grammarPointId': 'skm3-u4-kawari-ni-exchange',
        'grammarPointTitle': '〜かわりに (In Exchange For / Compensation / Instead Of)',
        'explanation': {
            'overall': 'Adjective + かわりに expresses a balanced trade-off or compensation: "on the one hand disadvantage A, but in return / compensation for it, advantage B".',
            'options': [
                {
                    'text': 'かわりに',
                    'isCorrect': True,
                    'reason': 'Correct. い-adjective + かわりに expresses compensating trade-off (far station vs cheap rent).',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'うちに',
                    'isCorrect': False,
                    'reason': 'Incorrect. うちに indicates temporal window, not trade-off balance.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'とおりに',
                    'isCorrect': False,
                    'reason': 'Incorrect. とおりに indicates accordance/conformity.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'たびに',
                    'isCorrect': False,
                    'reason': 'Incorrect. たびに indicates repeated recurrence.',
                    'trapCategory': 'meaning'
                }
            ]
        },
        'hint': 'Which conjunction means "in return for / as compensation for [disadvantage A]"?'
    }
]

existing_ids = {e['id'] for e in exercises}
for q in new_questions:
    if q['id'] not in existing_ids:
        exercises.append(q)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for SKM N3 Chapter 4!')

# 2. Enrich base-reviewed.json for Chapter 4 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. skm3-u4-hanmen-flipside
c = card_map.get('skm3-u4-hanmen-flipside')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 4'
    c['nuance'] = (
        '〜反面 expresses the coexistence of two contrasting, contradictory sides (positive and negative) within the VERY SAME entity, situation, or phenomenon: "on the flip side / on the other hand". '
        'FORMATION (Printed p. 24): '
        '・Plain form (+ な/である for な-adj, + である for Noun) + 反面. '
        '・都会の生活は便利な反面、ストレスも多い (Urban life is convenient, but on the flip side, stress is high). '
        '・薬は病気を治す反面、副作用があることもある (Medicine cures illness, but on the flip side, can have side effects). '
        '・一人暮らしは気楽な反面、寂しさを感じることもある (Living alone is carefree, but on the flip side, can feel lonely). '
        'CORE CONSTRAINT: '
        'Subject in both halves must refer to the SAME object/situation, highlighting its internal dual nature.'
    )
    c['keyTakeaway'] = '〜反面: Coexisting opposite aspects (merits vs demerits) of the SAME entity ("on the flip side"). Formations: Verb/い-adj plain + 反面; な-adj + な/である反面; Noun + である反面.'
    c['connection'] = 'Plain form (+ な/である for な-adj, + である for Noun) + 反面'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 4, Section 2, printed p. 24 (PDF p. 47).'

# 2. skm3-u4-kawari-ni-exchange
c = card_map.get('skm3-u4-kawari-ni-exchange')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 4'
    c['nuance'] = (
        '〜かわりに expresses trade-off compensation or proxy substitution: '
        'FORMATION (Printed p. 25): '
        '・Plain form (+ な for な-adj, + の for Noun) + かわりに. '
        '(1) Trade-off / Balanced Compensation (p. 25): '
        '・"On the one hand A, but in return / compensation for it, equivalent B holds." '
        '・この仕事は大変なかわりに、給料が非常に高い (This job is grueling, but in return, the pay is very high). '
        '・駅から遠いかわりに、家賃がとても安い (Far from the station, but in return, rent is cheap). '
        '(2) Mutual Exchange: '
        '・日本語を教えてもらうかわりに、英語を教えてあげる (In return for learning Japanese, I will teach you English). '
        '(3) Proxy Substitution (Instead of): '
        '・病気の部長のかわりに、私が会議に出席した (In place of the sick manager, I attended the meeting).'
    )
    c['keyTakeaway'] = '〜かわりに: (1) Trade-off / compensation ("disadvantage A, but in return, compensating advantage B"); (2) Exchange of favors; (3) Proxy substitution ("in place of / instead of"). Noun takes の.'
    c['connection'] = 'Plain form (+ な for な-adj, + の for Noun) + かわりに'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 4, Section 4, printed p. 25 (PDF p. 48).'

# 3. skm3-u4-ni-taishite
c = card_map.get('skm3-u4-ni-taishite')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 4'
    c['nuance'] = (
        '〜に対して / 〜のに対して clearly contrasts two different, separate entities or actions: "unlike ~, ... / in contrast to ~, whereas ...". '
        'FORMATION (Printed p. 24): '
        '・Noun + に対して (兄に対して弟は: in contrast to older brother, younger brother is...). '
        '・Clause (plain form + な/である for な-adj, + な/である/の for Noun) + のに対して (都市部で人口が増加しているのに対して、地方では過疎化が進んでいる: Whereas urban population grows, rural population declines). '
        '・兄が活発なのに対して、弟はおとなしい (Whereas older brother is lively, younger brother is quiet). '
        'DISTINCTION FROM 反面: '
        '反面 contrasts dual aspects of the SAME entity; 〜に対して contrasts TWO DISTINCT subjects/entities.'
    )
    c['keyTakeaway'] = '〜に対して / 〜のに対して: Contrasts TWO DIFFERENT entities/subjects ("whereas X is..., in contrast Y is..."). Contrasts with 反面 which examines internal duality of a single entity.'
    c['connection'] = 'Noun + に対して | Clause (plain form + の) + に対して'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 4, Section 1, printed p. 24 (PDF p. 47).'

# 4. skm3-u4-ni-kurabete
c = card_map.get('skm3-u4-ni-kurabete')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 4'
    c['nuance'] = (
        '〜に比べて / 〜に比べると uses Noun as a comparative benchmark to evaluate a difference in degree or quality: "compared with / relative to". '
        'FORMATION (Printed pp. 24-25): '
        '・Noun + に比べて / Noun + に比べると. '
        '・去年に比べて、今年は物価がかなり上がっている (Compared to last year, prices have risen significantly this year). '
        '・兄に比べて弟の方が背が高い (Compared to the older brother, the younger brother is taller). '
        '・以前に比べると、町がずいぶん静かになった (Compared to before, the town has become much quieter). '
        'FOCUS: '
        'Focuses on comparative degree measurement against a baseline standard.'
    )
    c['keyTakeaway'] = 'Noun + に比べて / に比べると: "compared with / relative to Noun". Uses Noun as a baseline benchmark to measure a difference in degree or quality.'
    c['connection'] = 'Noun + に比べて / に比べると'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 4, Supplementary Section, printed pp. 24-25 (PDF pp. 47-48).'

# 5. added-n3-4-46 (~一方で・〜というより)
c = card_map.get('added-n3-4-46')
if c:
    c['book'] = 'Shin Kanzen Master N3'
    c['chapter'] = 'Part 1 · Chapter 4'
    c['nuance'] = (
        'This card covers two high-frequency comparative discourse expressions: '
        '(1) 〜一方で (On One Hand... On the Other Hand, p. 24): '
        '・Plain form (+ な/である for な-adj, + である for Noun) + 一方(で). '
        '・Presents two opposing sides, dual simultaneous tendencies, or concurrent contrasting phenomena ("while at the same time on the other hand"): '
        '・政府は景気回復を発表する一方で、国民の不安は高まっている (While the government announces economic recovery, on the other hand, public anxiety is rising). '
        '・会議で自分の意見をはっきり言う一方で、他人の意見も尊重する (Speaks his mind, while at the same time respecting others). '
        '(2) 〜というより (Rather Than Say X, It\'s More Like Y, p. 25): '
        '・Word / Plain form + というより (often accompanied by むしろ). '
        '・Indicates that expression Y is more accurate, appropriate, or fitting than expression X: '
        '・あの人は指導者というより、友達のようだ (More like a friend than an instructor). '
        '・冷たいというよりむしろ涼しい (Cool rather than cold). '
        '・美人というより可愛い (Cute rather than beautiful).'
    )
    c['keyTakeaway'] = '〜一方で: Dual concurrent opposing trends ("while A, at the same time B"). 〜というより: Nuance correction ("rather than call it X, it is more like Y"). Often paired with むしろ.'
    c['connection'] = 'Plain form + 一方で | Word / Plain form + というより (むしろ)'
    c['sourceReference'] = 'Shin Kanzen Master N3 Bunpou, Part 1, Chapter 4, Section 3 & Section 5, printed pp. 24-25 (PDF pp. 47-48).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 5 SKM N3 Chapter 4 cards in base-reviewed.json!')

# 3. Add 5 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing SKM N3 Chapter 4 rows if any (including the older supplementary one)
matrix = [r for r in matrix if not (
    r.get('sourceBook') == 'Shin Kanzen Master N3' and (
        r.get('sourceSection') == 'Part 1 · Chapter 4' or 
        r.get('cardId') in ['skm3-u4-hanmen-flipside', 'skm3-u4-kawari-ni-exchange', 'skm3-u4-ni-taishite', 'skm3-u4-ni-kurabete', 'added-n3-4-46']
    )
)]

skm3_c4_entries = [
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 4',
        'exactPrintedPages': 'p. 24',
        'exactPdfPages': 'p. 47',
        'grammarItem': '〜反面 (On the Flip Side: Coexisting Contradictory Aspects)',
        'instructionalDetails': 'Coexistence of contradictory sides (pros/cons) within the same entity/situation; Plain form (+ な/である for な-adj, + である for Noun) + 反面; core constraint: both halves must describe the same subject/situation.',
        'cardId': 'skm3-u4-hanmen-flipside',
        'exampleCount': 4,
        'exampleIds': ['skm3-u4-hanmen-flipside::s-skm3-4-1', 'skm3-u4-hanmen-flipside::n3-use-examples-43', 'skm3-u4-hanmen-flipside::n3-use-examples-44', 'skm3-u4-hanmen-flipside::n3-use-examples-45'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 24 (PDF p. 47, skm3_pdf_47.png). Verified Section 2 formation, dual aspect coexistence semantics, and same-entity constraint.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 4',
        'exactPrintedPages': 'p. 25',
        'exactPdfPages': 'p. 48',
        'grammarItem': '〜かわりに (In Exchange For / Compensation / Instead Of)',
        'instructionalDetails': 'Three functions: (1) trade-off compensation ("disadvantage A, but in return advantage B"), (2) exchange of favors, (3) proxy substitution ("in place of"); Plain form (+ な for な-adj, + の for Noun) + かわりに.',
        'cardId': 'skm3-u4-kawari-ni-exchange',
        'exampleCount': 4,
        'exampleIds': ['skm3-u4-kawari-ni-exchange::s-skm3-4-2', 'skm3-u4-kawari-ni-exchange::n3-use-examples-46', 'skm3-u4-kawari-ni-exchange::n3-use-examples-47', 'skm3-u4-kawari-ni-exchange::n3-use-examples-48'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 25 (PDF p. 48, skm3_pdf_48.png). Verified Section 4 formation rules, trade-off compensation semantics, and proxy substitution mechanics.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 4',
        'exactPrintedPages': 'p. 24',
        'exactPdfPages': 'p. 47',
        'grammarItem': '〜に対して (In Contrast To / While X Is..., Y Is...)',
        'instructionalDetails': 'Contrasts two different entities or opposing factual realities; Noun + に対して / Clause (plain form + の) + に対して; contrast with 反面 (two entities vs single entity duality).',
        'cardId': 'skm3-u4-ni-taishite',
        'exampleCount': 4,
        'exampleIds': ['skm3-u4-ni-taishite::s-skm3-4-3', 'skm3-u4-ni-taishite::n3-use-examples-49', 'skm3-u4-ni-taishite::n3-use-examples-50', 'skm3-u4-ni-taishite::n3-use-examples-51'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 24 (PDF p. 47, skm3_pdf_47.png). Verified Section 1 contrast mechanics and syntactic connection with noun and nominalized clauses.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 4',
        'exactPrintedPages': 'pp. 24-25',
        'exactPdfPages': 'pp. 47-48',
        'grammarItem': '〜に比べて (Compared With / Relative To)',
        'instructionalDetails': 'Noun + に比べて / に比べると; uses noun as comparative baseline standard to evaluate a difference in degree or quality; comparative degree measurement.',
        'cardId': 'skm3-u4-ni-kurabete',
        'exampleCount': 4,
        'exampleIds': ['skm3-u4-ni-kurabete::s-skm3-4-4', 'skm3-u4-ni-kurabete::n3-use-examples-52', 'skm3-u4-ni-kurabete::n3-use-examples-53', 'skm3-u4-ni-kurabete::n3-use-examples-54'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 24-25 (PDF pp. 47-48, skm3_pdf_47.png, skm3_pdf_48.png). Verified comparative degree evaluation and noun attachment rules.'
    },
    {
        'sourceBook': 'Shin Kanzen Master N3',
        'sourceSection': 'Part 1 · Chapter 4',
        'exactPrintedPages': 'pp. 24-25',
        'exactPdfPages': 'pp. 47-48',
        'grammarItem': '〜一方で・〜というより (Dual Perspectives & Nuance Rephrasing)',
        'instructionalDetails': '〜一方で presents dual concurrent opposing phenomena ("while A, at the same time B"); 〜というより indicates nuance correction ("rather than X, it is more like Y; often paired with むしろ).',
        'cardId': 'added-n3-4-46',
        'exampleCount': 4,
        'exampleIds': ['added-n3-4-46-example', 'added-n3-4-46::n3-use-examples-55', 'added-n3-4-46::n3-use-examples-56', 'added-n3-4-46::n3-use-examples-57'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 24-25 (PDF pp. 47-48, skm3_pdf_47.png, skm3_pdf_48.png). Verified Section 3 一方で dual trend semantics and Section 5 というより nuance correction rules.'
    }
]

matrix.extend(skm3_c4_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Certified SKM N3 Chapter 4 in source coverage matrix! Total certified rows: {len(matrix)}')
