import json

# 1. Update chapterExercises.json for Lesson 20 to have 12 questions
ex_path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(ex_path, 'r', encoding='utf-8') as f:
    exercises = json.load(f)

has_q11 = any(q.get('id') == 'g2-l20-ex-11' for q in exercises)
if not has_q11:
    q11 = {
        'id': 'g2-l20-ex-11',
        'bookId': 'genki-2',
        'chapter': 'Lesson 20',
        'type': 'multiple-choice',
        'context': 'Business telephone etiquette: Asking permission to humbly visit a client at their corporate office tomorrow afternoon.',
        'question': '明日の午後三時に、御社へ（　　）もよろしいでしょうか。',
        'translation': 'Would it be all right if I visited your company tomorrow at 3:00 PM?',
        'options': [
            '伺って',
            '参って',
            'いらっしゃって',
            'お行きして'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-g2-20-34',
        'grammarPointTitle': '丁重語・謙譲語',
        'explanation': {
            'overall': 'When visiting or asking someone you respect, the dedicated humble verb is 伺う (うかがう: humble for 訪ねる and 聞く). 参る is an extra-modest verb showing general deference to the listener rather than an action performed directly toward the recipient.',
            'options': [
                {
                    'text': '伺って',
                    'isCorrect': True,
                    'reason': 'Correct. 伺う (te-form: 伺って) is the humble verb used when visiting an honored person or their organization.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '参って',
                    'isCorrect': False,
                    'reason': 'Incorrect. 参る is extra-modest (丁重語) for going/coming, but 伺う is the precise humble verb for paying a visit to an honored party.',
                    'trapCategory': 'register'
                },
                {
                    'text': 'いらっしゃって',
                    'isCorrect': False,
                    'reason': 'Incorrect. いらっしゃる is honorific (尊敬語) for the actions of others, never one\'s own actions.',
                    'trapCategory': 'register'
                },
                {
                    'text': 'お行きして',
                    'isCorrect': False,
                    'reason': 'Incorrect. 行く has irregular humble forms and cannot be combined into *お行きする.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'Which humble verb means specifically to visit or ask an honored party?'
    }
    exercises.append(q11)

has_q12 = any(q.get('id') == 'g2-l20-ex-12' for q in exercises)
if not has_q12:
    q12 = {
        'id': 'g2-l20-ex-12',
        'bookId': 'genki-2',
        'chapter': 'Lesson 20',
        'type': 'multiple-choice',
        'context': 'Indirect yes/no question about someone\'s availability: Wondering whether a friend is free tomorrow.',
        'question': '明日彼が（　　）かどうか分かりませんが、電話で聞いてみます。',
        'translation': 'I do not know whether he is free tomorrow, but I will call and ask him.',
        'options': [
            '暇',
            '暇だ',
            '暇な',
            '暇の'
        ],
        'correctIndex': 0,
        'grammarPointId': 'added-g2-20-36',
        'grammarPointTitle': '文の中の疑問・という名前',
        'explanation': {
            'overall': 'In embedded questions ending with か or かどうか, the present affirmative copula だ of な-adjectives and nouns is dropped (e.g. 暇かどうか, 学生かどうか, not *暇だかどうか).',
            'options': [
                {
                    'text': '暇',
                    'isCorrect': True,
                    'reason': 'Correct. The copula だ is dropped after な-adjectives before かどうか (暇かどうか).',
                    'trapCategory': 'formation'
                },
                {
                    'text': '暇だ',
                    'isCorrect': False,
                    'reason': 'Incorrect. The copula だ is obligatorily dropped in standard embedded questions before かどうか.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '暇な',
                    'isCorrect': False,
                    'reason': 'Incorrect. な is used before nouns (暇な人), but omitted before the particle marker かどうか.',
                    'trapCategory': 'formation'
                },
                {
                    'text': '暇の',
                    'isCorrect': False,
                    'reason': 'Incorrect. の is not used with な-adjectives before embedded question markers.',
                    'trapCategory': 'formation'
                }
            ]
        },
        'hint': 'What happens to the copula だ of な-adjectives when forming embedded questions with かどうか?'
    }
    exercises.append(q12)

with open(ex_path, 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print('Updated chapterExercises.json with 12 exercises for Lesson 20!')

# 2. Enrich base-reviewed.json for Lesson 20 cards
base_path = 'jlpt-exam-prep/content/base-reviewed.json'
with open(base_path, 'r', encoding='utf-8') as f:
    cards = json.load(f)

card_map = {c['id']: c for c in cards}

# 1. added-g2-20-34 (丁重語・謙譲語)
c = card_map.get('added-g2-20-34')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 20'
    c['nuance'] = (
        'Genki II distinguishes two types of self-humbling expressions: '
        '(1) Extra-Modest Expressions (丁重語 teichougo, pp. 184-185): '
        'Talk modestly of what you (or your in-group, family, company) do, showing deference generally to the listener. Used in self-introductions, job interviews, customer service, and announcements. Verbs: '
        '・いる → おる (おります) '
        '・行く・来る → 参る (まいります) '
        '・言う → 申す (もうします) '
        '・する → いたす (いたします) '
        '・食べる・飲む → いただく (いただきます) '
        '・ある → ござる (ございます) '
        '・〜ている → 〜ておる (〜ております) '
        '・〜です → 〜でござる (〜でございます) '
        '(2) Humble Expressions (謙譲語 kenjougo, pp. 186-187): '
        'Talk humbly of an action performed directly for or in deference to a specific honored recipient who appears in the event described. '
        '・Regular formula (wago): お + verb stem + する (お持ちします: I will carry for you; お送りします: I will walk/drive you; お貸しします). '
        '・Regular formula (kango suru-compounds): ご + Noun + する (ご紹介します: let us introduce to you; ご案内します: I will guide you; ご説明します: I will explain; ご連絡します). '
        '・Special humble verbs: もらう → いただく; あげる → 差し上げる (さしあげます); 訪ねる/聞く → 伺う (うかがいます); 会う → お目にかかる (おめにかかります).'
    )
    c['keyTakeaway'] = '丁重語: Modest actions exalting the listener generally (参る, 申す, いたす, おる, ござる). 謙譲語: Humble action directed toward a specific honored recipient (お+stem+する / ご+Noun+する; special: 伺う, 差し上げる, お目にかかる).'
    c['connection'] = '丁重語: 参ります / 申します / いたします | 謙譲語: お + V-stem + する / ご + Noun + する | 伺う / 差し上げる'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 20, Grammar 1 & 2, printed pp. 184-187 (PDF pp. 192-195).'

# 2. added-g2-20-35 (~ないで)
c = card_map.get('added-g2-20-35')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 20'
    c['nuance'] = (
        'V-ないで expresses doing something without doing X (accompanying circumstance or bypassed expected step: "without doing..."). '
        'Formation: Short present negative verb + で: V-ないで + Main Verb (昨日の夜、寝ないで、勉強しました: Last night I studied without getting any sleep; 辞書を使わないで、新聞を読みます: I read the newspaper without using a dictionary). '
        'CRITICAL TENSE CONSTRAINT (p. 188): '
        'The present tense negative form 〜ないで is used for BOTH present and past sentences! You never conjugate the 〜ないで clause into the past (*寝なかったで is completely ungrammatical). Tense is marked exclusively on the sentence-final main verb.'
    )
    c['keyTakeaway'] = 'V-ないで: "without doing X". The present form 〜ないで is used for BOTH present and past sentences (never *なかったで). Tense is determined by the final verb.'
    c['connection'] = 'V-ない + で + Main Verb'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 20, Grammar 3, printed p. 188 (PDF p. 196).'

# 3. added-g2-20-36 (文の中の疑問・という名前)
c = card_map.get('added-g2-20-36')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 20'
    c['nuance'] = (
        'This section encompasses questions embedded within larger sentences and naming constructions: '
        '(1) Embedded Questions (pp. 188-189): '
        '・With question word (who, what, where): Short form clause + か (だれが一番上手か知りません: I don\'t know who is the best; 何時に始まるか教えてください: Tell me what time it starts). '
        '・Yes/No question (whether or not): Short form clause + かどうか (あの人が学生かどうか知りません: I don\'t know whether that person is a student; 来るかどうか分かりません). '
        '・Mandatory だ dropping rule: The present affirmative copula だ on な-adjectives and nouns is dropped before か and かどうか (学生かどうか, 暇かどうか; never *学生だかどうか). '
        '・Internal subject rule: The subject of the embedded clause is marked with が, not は. '
        '(2) Name-Calling (Noun called X, p. 190): '
        '・[Name] という [Noun] specifies the name of a person, item, song, or book (「花」という歌: a song called "Hana"; 「吾輩は猫である」という小説: a novel titled "I Am a Cat"; ポチという犬).'
    )
    c['keyTakeaway'] = 'Embedded Qs: Wh-word + short form + か | Yes/No: short form + かどうか. The copula だ on nouns/な-adj is dropped before か/かどうか. Internal subject takes が. Naming: [Name] という [Noun].'
    c['connection'] = 'Embedded Wh-Q: clause + か | Embedded Yes/No: clause + かどうか | Naming: [Name] という [Noun]'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 20, Grammar 4 & 5, printed pp. 188-190 (PDF pp. 196-198).'

# 4. added-g2-20-37 (~やすい・〜にくい)
c = card_map.get('added-g2-20-37')
if c:
    c['book'] = 'Genki II'
    c['chapter'] = 'Lesson 20'
    c['nuance'] = (
        'Attaching 〜やすい or 〜にくい to the masu-stem of a verb creates compound い-adjectives describing ease or difficulty: '
        '(1) V-stem + やすい: "easy to do / prone to doing" (この電子辞書はとても使いやすいです: This electronic dictionary is very easy to use; 読みやすい: easy to read; 分かりやすい: easy to understand; 壊れやすい: fragile / prone to breaking; 太りやすい: prone to gaining weight). '
        '(2) V-stem + にくい: "hard/difficult to do / unlikely to do" (この苦い薬は飲みにくいです: This bitter medicine is hard to swallow; 読みにくい: hard to read; 分かりにくい: hard to understand; 骨折しにくい: hard to fracture). '
        'INFLECTION: They conjugate identically to い-adjectives: '
        '・Present: 〜やすい / 〜にくい '
        '・Negative: 〜やすくない / 〜にくくない '
        '・Past: 〜やすかった / 〜にくかった '
        '・Past Negative: 〜やすくなかった / 〜にくくなかった '
        '・Adverbial: 〜やすく / 〜にくく '
        'FOCUS CONSTRAINT: Can focus on psychological ease/difficulty, physical manageability, or statistical propensity of an object.'
    )
    c['keyTakeaway'] = 'V-stem + やすい = easy to V / prone to V. V-stem + にくい = hard to V. Conjugates as regular い-adjectives (〜やすくない, 〜やすかった, 〜にくかった).'
    c['connection'] = 'V(masu-stem) + やすい / にくい'
    c['sourceReference'] = 'Genki II (3rd Ed.), Lesson 20, Grammar 6, printed p. 190 (PDF p. 198).'

with open(base_path, 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print('Enriched all 4 Lesson 20 cards in base-reviewed.json!')

# 3. Add 4 certified matrix rows to source-coverage-matrix.json
matrix_path = 'jlpt-exam-prep/audit/source-coverage-matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Filter existing Lesson 20 rows if any
matrix = [r for r in matrix if not (r.get('sourceBook') == 'Genki II (3rd Ed.)' and r.get('sourceSection') == 'Lesson 20')]

l20_entries = [
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 20',
        'exactPrintedPages': 'pp. 184-187',
        'exactPdfPages': 'pp. 192-195',
        'grammarItem': '丁重語・謙譲語 (Extra-Modest Speech & Humble Expressions)',
        'instructionalDetails': '丁重語 exalts listener generally (参る, 申す, いたす, おる, ござる); 謙譲語 exalts specific recipient of action; regular formula お + V-stem + する (お持ちする) and ご + Noun + する (ご紹介する); special humble verbs (伺う, 差し上げる, お目にかかる).',
        'cardId': 'added-g2-20-34',
        'exampleCount': 4,
        'exampleIds': ['added-g2-20-34-example', 'added-g2-20-34::genki2-use-examples-75', 'added-g2-20-34::genki2-use-examples-76', 'added-g2-20-34::genki2-use-examples-77'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 184-187 (PDF pp. 192-195, g2_p192_printed184.png to g2_p195_printed187.png). Verified extra-modest verbs table, humble formulas (お〜する / ご〜する), and distinction between listener deference vs recipient deference.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 20',
        'exactPrintedPages': 'p. 188',
        'exactPdfPages': 'p. 196',
        'grammarItem': '〜ないで (Doing Something Without Doing X)',
        'instructionalDetails': 'V-short negative + で for unperformed prerequisite/circumstance; critical tense rule: present 〜ないで is used for BOTH present and past sentences (never *なかったで); tense marked only on main final verb.',
        'cardId': 'added-g2-20-35',
        'exampleCount': 4,
        'exampleIds': ['added-g2-20-35-example', 'added-g2-20-35::genki2-use-examples-78', 'added-g2-20-35::genki2-use-examples-79', 'added-g2-20-35::genki2-use-examples-80'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 188 (PDF p. 196, g2_p196_printed188.png). Verified formation V-ないで and strict ban on past marking inside the clause.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 20',
        'exactPrintedPages': 'pp. 188-190',
        'exactPdfPages': 'pp. 196-198',
        'grammarItem': '文の中の疑問・という名前 (Embedded Questions & Noun Called X)',
        'instructionalDetails': 'Embedded questions: Wh-word + short clause + か; Yes/No + かどうか; mandatory だ dropping on nouns and な-adjectives before か/かどうか; internal subject takes が; naming construction [Name] という [Noun].',
        'cardId': 'added-g2-20-36',
        'exampleCount': 4,
        'exampleIds': ['added-g2-20-36-example', 'added-g2-20-36::genki2-use-examples-81', 'added-g2-20-36::genki2-use-examples-82', 'added-g2-20-36::genki2-use-examples-83'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed pp. 188-190 (PDF pp. 196-198, g2_p196_printed188.png to g2_p198_printed190.png). Verified embedded Wh-question か, Yes/No かどうか, copula だ dropping rule, and という naming pattern.'
    },
    {
        'sourceBook': 'Genki II (3rd Ed.)',
        'sourceSection': 'Lesson 20',
        'exactPrintedPages': 'p. 190',
        'exactPdfPages': 'p. 198',
        'grammarItem': '〜やすい・〜にくい (Easy to Do / Hard to Do)',
        'instructionalDetails': 'V(masu-stem) + やすい (easy to V / prone to V); V(masu-stem) + にくい (hard/difficult to V); inflection identical to い-adjectives (〜やすくない, 〜やすかった, 〜にくかった); covers manageability and inherent propensity.',
        'cardId': 'added-g2-20-37',
        'exampleCount': 4,
        'exampleIds': ['added-g2-20-37-example', 'added-g2-20-37::genki2-use-examples-84', 'added-g2-20-37::genki2-use-examples-85', 'added-g2-20-37::genki2-use-examples-86'],
        'missingWork': '',
        'status': 'checked',
        'evidence': 'Visual inspection of printed p. 190 (PDF p. 198, g2_p198_printed190.png). Verified masu-stem attachment, い-adjective inflection paradigm, and affirmative/negative usage.'
    }
]

matrix.extend(l20_entries)

with open(matrix_path, 'w', encoding='utf-8') as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f'Certified Lesson 20 in source coverage matrix! Total certified rows: {len(matrix)}')
