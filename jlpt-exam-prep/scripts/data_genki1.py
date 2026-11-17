# -*- coding: utf-8 -*-
"""
Genki I (3rd Edition) - Complete Canonical N5 Grammar Syllabus (Lessons 1 to 12)
Fully annotated with lexical tokens, literal glosses, nuance notes, and 4-way quiz explanations.
"""

def tok(word, reading=None, romaji=None, meaning="", pos=None):
    d = {"word": word, "meaning": meaning}
    if reading: d["reading"] = reading
    if romaji: d["romaji"] = romaji
    if pos: d["pos"] = pos
    return d

def make_sentence(sid, ja, en, literal, tokens, nuanceNote=None, trapAlert=None):
    d = {
        "id": sid,
        "japanese": ja,
        "english": en,
        "literal": literal,
        "tokens": tokens
    }
    if nuanceNote:
        d["nuanceNote"] = nuanceNote
    if trapAlert:
        d["trapAlert"] = trapAlert
    return d

def make_quiz(qid, q, trans, opts, correct_idx, explanations, focus, hint):
    return {
        "id": qid,
        "question": q,
        "translation": trans,
        "options": opts,
        "correctIndex": correct_idx,
        "grammarFocus": focus,
        "ruleHint": hint,
        "explanations": [
            {
                "text": opts[i],
                "isCorrect": (i == correct_idx),
                "reason": explanations[i]
            }
            for i in range(len(opts))
        ]
    }

def get_genki1_points():
    pts = [
        # 1. Lesson 1: X は Y です
        {
            "id": "gp-genki1-wa-desu",
            "title": "X は Y です (X is Y / Topic & Copula)",
            "meaning": "X is Y. Establishes X as the contextual topic with は and equates it to predicate Y with です.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 1: New Friends",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun1 + は + Noun2 / Adjective + です",
            "nuance": "The topic particle は (pronounced 'wa') presents the background context or focus of conversation ('as for X...'). です serves as the polite non-past copula ('is / am / are').",
            "keyTakeaway": "MUG-UP: は marks the topic ('as for X'). Pronounced 'wa', written as は.",
            "sentences": [
                make_sentence(
                    "s-g1-1-1",
                    "私はカリフォルニア大学の留学生です。",
                    "I am an international student at the University of California.",
                    "I topic UC's international-student am.",
                    [
                        tok("私", "わたし", "watashi", "I / me", "Pronoun"),
                        tok("は", "わ", "wa", "topic marker", "Particle"),
                        tok("留学生", "りゅうがくせい", "ryuugakusei", "international student", "Noun"),
                        tok("です", "です", "desu", "am / is (polite copula)", "Copula")
                    ],
                    "Standard polite self-introduction formula."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-1-1",
                    "田中さん（　　）日本人です。",
                    "Tanaka-san is Japanese.",
                    ["は", "を", "に", "へ"],
                    0,
                    [
                        "Correct! は marks Tanaka-san as the topic being identified as Japanese.",
                        "Incorrect. を marks direct objects of action verbs, not copula topics.",
                        "Incorrect. に indicates direction, time, or location of existence.",
                        "Incorrect. へ indicates direction of movement."
                    ],
                    "Topic marker は",
                    "Marks Tanaka-san as the topic of the sentence."
                )
            ],
            "tags": ["N5", "Genki L1", "Copula", "Topic"]
        },

        # 2. Lesson 1: Noun の Noun
        {
            "id": "gp-genki1-no-possessive",
            "title": "Noun1 の Noun2 (Possession, Affiliation & Attribute)",
            "meaning": "Links two nouns where Noun1 qualifies, possesses, or describes Noun2 ('Noun1's Noun2' or 'Noun2 of Noun1').",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 1: New Friends",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun1 + の + Noun2",
            "nuance": "Noun modifier order in Japanese is strictly modifier first: 日本の車 (Japanese car), 私の本 (my book), 大学の先生 (university professor).",
            "keyTakeaway": "MUG-UP: In Japanese, the modifier ALWAYS precedes の. [Modifier] の [Main Noun].",
            "sentences": [
                make_sentence(
                    "s-g1-1-2",
                    "これはメアリーさんの日本語の教科書です。",
                    "This is Mary's Japanese language textbook.",
                    "This topic Mary's Japanese-language's textbook is.",
                    [
                        tok("これ", "これ", "kore", "this", "Pronoun"),
                        tok("は", "わ", "wa", "topic marker", "Particle"),
                        tok("メアリーさん", "メアリーさん", "mearii-san", "Mary", "Noun"),
                        tok("の", "の", "no", "possessive particle", "Particle"),
                        tok("日本語", "にほんご", "nihongo", "Japanese language", "Noun"),
                        tok("教科書", "きょうかしょ", "kyoukasho", "textbook", "Noun"),
                        tok("です", "です", "desu", "is", "Copula")
                    ],
                    "Notice chained possessives: Mary's -> Japanese's -> textbook."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-1-2",
                    "それは（　　）傘ですか。「スミスさんのです。」",
                    "Whose umbrella is that? 'It is Smith-san's.'",
                    ["だれの", "どれの", "どこの", "なんの"],
                    0,
                    [
                        "Correct! だれの means 'whose' (who + possessive の).",
                        "Incorrect. どれ means 'which one of 3+', not who.",
                        "Incorrect. どこ means 'where', asking about place.",
                        "Incorrect. なん means 'what', asking about object category."
                    ],
                    "Interrogative だれの (whose)",
                    "Asking for the owner of the umbrella."
                )
            ],
            "tags": ["N5", "Genki L1", "Particle の", "Possession"]
        },

        # 3. Lesson 2: これ / それ / あれ / どれ (Ko-So-A-Do System)
        {
            "id": "gp-genki1-ko-so-a-do",
            "title": "これ・それ・あれ・どれ (The Ko-So-A-Do Demonstrative System)",
            "meaning": "Spatial and psychological demonstratives: これ (near speaker), それ (near listener), あれ (distant from both), どれ (which one).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 2: Shopping",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "これ / それ / あれ / どれ (Standalone Pronouns) | この / その / あの / どの + Noun",
            "nuance": "CRITICAL DISTINCTION: これ stand alone as pronouns. この MUST be followed immediately by a noun (この本, NOT このは ❌).",
            "keyTakeaway": "MUG-UP: こ (close to me), そ (close to you), あ (over there), ど (which?).",
            "sentences": [
                make_sentence(
                    "s-g1-2-1",
                    "あの時計はいくらですか。「あれは五千円です。」",
                    "How much is that watch over there? 'That one over there is 5,000 yen.'",
                    "That watch-over-there topic how-much is? That-over-there topic 5000-yen is.",
                    [
                        tok("あの", "あの", "ano", "that (over there)", "Pre-noun"),
                        tok("時計", "とけい", "tokei", "watch / clock", "Noun"),
                        tok("は", "わ", "wa", "topic marker", "Particle"),
                        tok("いくら", "いくら", "ikura", "how much", "Interrogative"),
                        tok("あれ", "あれ", "are", "that one over there", "Pronoun")
                    ],
                    "あの requires the noun 時計; あれ stands independently."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-2-1",
                    "すみません、（　　）辞書を見せてください。",
                    "Excuse me, please show me that dictionary near you.",
                    ["その", "それ", "そこ", "そんな"],
                    0,
                    [
                        "Correct! その directly precedes the noun 辞書 to point to an item near the listener.",
                        "Incorrect. それ is an independent pronoun and cannot directly modify 辞書 without の.",
                        "Incorrect. そこ means 'that place near you'.",
                        "Incorrect. そんな means 'that kind of'."
                    ],
                    "Ko-So-A-Do noun modifier その",
                    "Modifying 辞書 near the listener."
                )
            ],
            "tags": ["N5", "Genki L2", "Ko-So-A-Do", "Demonstratives"]
        },

        # 4. Lesson 3: 動詞の３分類 (The Three Verb Classes)
        {
            "id": "gp-genki1-verb-groups",
            "title": "動詞の３分類 (The Three Verb Groups: Ru, U, & Irregular)",
            "meaning": "Japanese verbs are strictly classified into Ru-verbs (一段), U-verbs (五段), and Irregular verbs (する, くる).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 3: Making a Date",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "Ru-verbs: drop る + ます | U-verbs: change final -u to -i + ます | する→します, くる→きます",
            "nuance": "THE RU-VERB ILLUSION: Not all verbs ending in -る are Ru-verbs! Verbs like 帰る (かえる - to return), 走る (はしる - to run), and 入る (はいる - to enter) look like Ru-verbs but are strictly U-verbs (帰ります, 走ります, 入ります).",
            "keyTakeaway": "MUG-UP: If it doesn't end in -eru or -iru, it's 100% a U-verb. If it ends in -eru/-iru, beware sneaky U-verbs (帰る, 入る, 走る)!",
            "sentences": [
                make_sentence(
                    "s-g1-3-1",
                    "毎朝七時に起きて、学校へ行きます。",
                    "Every morning I wake up at 7 o'clock and go to school.",
                    "Every-morning 7-at waking-up, school-to go.",
                    [
                        tok("毎朝", "まいあさ", "maiasa", "every morning", "Noun"),
                        tok("七時", "しちじ", "shichiji", "7 o'clock", "Noun"),
                        tok("起きて", "おきて", "okite", "wake up (Ru-verb te-form)", "Verb"),
                        tok("行きます", "いきます", "ikimasu", "go (U-verb masu-form)", "Verb")
                    ],
                    "起きる is a Ru-verb (起きる→起きます); 行く is a U-verb (行く→行きます)."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-3-1",
                    "私は毎日六時にうちへ（　　）。",
                    "I return home at 6 o'clock every day.",
                    ["帰ります", "帰れます", "帰します", "帰りられます"],
                    0,
                    [
                        "Correct! 帰る (かえる) is an irregular U-verb: る changes to り + ます (帰ります).",
                        "Incorrect. 帰れます is the potential form ('can return').",
                        "Incorrect. 帰す (かえす) means 'to let someone return / return an item'.",
                        "Incorrect. 帰りられます is an ungrammatical hybrid."
                    ],
                    "U-verb conjugation of 帰る",
                    "Conjugating 帰る into polite non-past."
                )
            ],
            "tags": ["N5", "Genki L3", "Verbs", "Conjugation"]
        },

        # 5. Lesson 3: 格助詞 を・で・に・へ (Core Particles)
        {
            "id": "gp-genki1-core-particles",
            "title": "格助詞 を・で・に・へ (Object, Location of Action, Goal & Time)",
            "meaning": "Defines semantic roles: を (direct object), で (location of activity / tool), に (destination, specific time, indirect object), へ (direction of motion).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 3: Making a Date",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + を (Object) / で (Action place) / に (Target/Time) / へ (Heading)",
            "nuance": "で vs に TRAP: で marks where an EVENT or ACTION happens (図書館で勉強する - study at the library). に marks where something EXISTS (図書館に本がある) or a movement destination (図書館に行く).",
            "keyTakeaway": "MUG-UP: で = Doing an action at a spot. に = Being at a spot or heading into it.",
            "sentences": [
                make_sentence(
                    "s-g1-3-2",
                    "昨日の午後、図書館で友達と日本語を勉強しました。",
                    "Yesterday afternoon, I studied Japanese with my friend at the library.",
                    "Yesterday's afternoon, library-at friend-with Japanese studied.",
                    [
                        tok("図書館で", "としょかんで", "toshokan de", "at the library", "Noun+Particle"),
                        tok("日本語を", "にほんごを", "nihongo o", "Japanese (object)", "Noun+Particle"),
                        tok("勉強しました", "べんきょうしました", "benkyou shimashita", "studied", "Verb")
                    ],
                    "Action勉強 happens at the library, so it takes で."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-3-2",
                    "土曜日にデパート（　　）靴を買いました。",
                    "On Saturday, I bought shoes at the department store.",
                    ["で", "に", "へ", "を"],
                    0,
                    [
                        "Correct! 買う is an active event, so the location of action requires で.",
                        "Incorrect. に marks existence or destination, not where buying takes place.",
                        "Incorrect. へ marks direction of movement.",
                        "Incorrect. を marks the direct object (靴を)."
                    ],
                    "Location of action particle で",
                    "Buying shoes is an action conducted inside the department store."
                )
            ],
            "tags": ["N5", "Genki L3", "Particles", "Case Markers"]
        },

        # 6. Lesson 4: Existence X があります vs X がいます
        {
            "id": "gp-genki1-arimasu-imasu",
            "title": "〜があります vs 〜がいます (Inanimate vs Animate Existence)",
            "meaning": "Existence verbs: あります (inanimate objects, plants, events) vs います (living, moving beings: humans, animals).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 4: The First Date",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Place に Entity が あります / います",
            "nuance": "Robots and plants: In standard modern Japanese, plants use あります (木があります) because they do not locomote. Pets and humans use います (犬がいます).",
            "keyTakeaway": "MUG-UP: Can it walk or breathe? Use います. Inanimate or plant? Use あります.",
            "sentences": [
                make_sentence(
                    "s-g1-4-1",
                    "机の上に教科書とノートがあります。庭に猫がいます。",
                    "There are textbooks and notebooks on the desk. There is a cat in the yard.",
                    "Desk-on textbooks and notebooks exist. Yard-in cat exists.",
                    [
                        tok("机", "つくえ", "tsukue", "desk", "Noun"),
                        tok("上", "うえ", "ue", "top / above", "Noun"),
                        tok("あります", "あります", "arimasu", "exists (inanimate)", "Verb"),
                        tok("猫", "ねこ", "neko", "cat", "Noun"),
                        tok("います", "います", "imasu", "exists (animate)", "Verb")
                    ],
                    "Inanimate books take あります; living cat takes います."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-4-1",
                    "教室の中にスミス先生が（　　）。",
                    "Professor Smith is inside the classroom.",
                    ["います", "あります", "します", "なります"],
                    0,
                    [
                        "Correct! A teacher is a human being, requiring the animate existence verb います.",
                        "Incorrect. あります is strictly for inanimate objects and plants.",
                        "Incorrect. します means 'to do'.",
                        "Incorrect. なります means 'to become'."
                    ],
                    "Animate existence verb います",
                    "Selecting the existence verb for a human being."
                )
            ],
            "tags": ["N5", "Genki L4", "Existence", "Verbs"]
        },

        # 7. Lesson 5: い形容詞 vs な形容詞 (Adjective Conjugations)
        {
            "id": "gp-genki1-adjectives",
            "title": "い形容詞 vs な形容詞 (True Adjectives vs Adjectival Nouns)",
            "meaning": "The two classes of Japanese adjectives and their past/negative inflections: い-adjectives change suffix; な-adjectives use copula.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 5: A Trip to Okinawa",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "い-adj: 高い→高くない→高かった→高くなかった | な-adj: 静か(な)→静かじゃない→静かだった→静かじゃなかった",
            "nuance": "THE II/YOI EXCEPTION: いい (good) NEVER conjugates as いかった or いくない! Its base root is よい: よくない, よかった, よくなかった.",
            "keyTakeaway": "MUG-UP: いい → よくない, よかった, よくなかった! Never say いかった ❌.",
            "sentences": [
                make_sentence(
                    "s-g1-5-1",
                    "昨日の映画はとても面白かったですが、チケットはあまり安くなかったです。",
                    "Yesterday's movie was very interesting, but the tickets were not very cheap.",
                    "Yesterday's movie topic very interesting-past but, ticket topic not-very cheap-past-neg was.",
                    [
                        tok("面白かった", "おもしろかった", "omoshirokatta", "was interesting", "Adjective"),
                        tok("安くなかったです", "やすくなかったです", "yasukunakatta desu", "was not cheap", "Adjective")
                    ],
                    "面白い past affirmative = 面白かった; 安い past negative = 安くなかったです."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-5-1",
                    "先週のテストはあまり（　　）です。",
                    "Last week's test was not very good.",
                    ["よくなかった", "いくなかった", "いいじゃなかった", "よいでした"],
                    0,
                    [
                        "Correct! いい must conjugate through its root よい, becoming よくなかった.",
                        "Incorrect. いくなかった is an invalid false conjugation.",
                        "Incorrect. いいじゃなかった incorrectly applies な-adjective copula to an い-adjective.",
                        "Incorrect. よいでした is ungrammatical; past must be in the adjective itself (よかった)."
                    ],
                    "Past negative of いい (よい)",
                    "Conjugating いい into the past negative."
                )
            ],
            "tags": ["N5", "Genki L5", "Adjectives", "Conjugation"]
        },

        # 8. Lesson 6: て形 (The Te-Form & Polite Requests)
        {
            "id": "gp-genki1-te-form",
            "title": "て形 (The Te-Form: Connection, Requests & Prohibition)",
            "meaning": "The primary connective form of Japanese verbs: used for polite requests (〜てください), permission (〜てもいい), prohibition (〜てはいけない), and sequence.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 6: A Day in Robert's Life",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "う・つ・る→って | む・ぶ・ぬ→んで | く→いて (行く→行って!) | ぐ→いで | す→して | 一段(る)→て",
            "nuance": "CRITICAL EXCEPTION: 行く は「いいて」にならず、「行って」と促音便になります。",
            "keyTakeaway": "MUG-UP: V-て + ください = Please do. Prohibited: V-て + はいけません = Must not.",
            "sentences": [
                make_sentence(
                    "s-g1-6-1",
                    "すみませんが、窓を開けてください。",
                    "Excuse me, but please open the window.",
                    "Excuse-me but, window open please.",
                    [
                        tok("すみませんが", "すみませんが", "sumimasen ga", "excuse me but", "Expression"),
                        tok("窓を", "まどを", "mado o", "window", "Noun"),
                        tok("開けてください", "あけてください", "akete kudasai", "please open", "Grammar")
                    ],
                    "開ける is a Ru-verb: drop る + てください."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-6-1",
                    "ここで写真を（　　）はいけません。撮影禁止です。",
                    "You must not take photos here. Photography is prohibited.",
                    ["撮って", "撮る", "撮り", "撮った"],
                    0,
                    [
                        "Correct! 撮る (U-verb ending in る) conjugates to 撮って + はいけません for prohibition.",
                        "Incorrect. Dictionary form cannot connect to はいけません.",
                        "Incorrect. Masu-stem cannot connect to はいけません.",
                        "Incorrect. Past form cannot connect to はいけません."
                    ],
                    "〜てはいけません prohibition",
                    "Connecting a verb to the prohibition formula."
                )
            ],
            "tags": ["N5", "Genki L6", "Te-Form", "Prohibition"]
        },

        # 9. Lesson 7: 〜ている (Ongoing Action vs Resultant State)
        {
            "id": "gp-genki1-te-iru",
            "title": "〜ている (Actions in Progress vs Resulting Continuous States)",
            "meaning": "1) Ongoing action occurring right now (eating, studying). 2) Continuous state resulting from a past change (married, living, knowing).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 7: Family Picture",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-て + いる / います",
            "nuance": "THE INSTANT VERB TRAP: For puncture verbs like 結婚する (to marry), 知る (to find out), and 住む (to take up residence), 〜ている indicates the RESULTING STATE! 結婚している means 'is currently married', NOT 'is walking down the aisle right now'.",
            "keyTakeaway": "MUG-UP: 知っている = I know. Negative exception: 知りません (NOT 知っていません ❌)!",
            "sentences": [
                make_sentence(
                    "s-g1-7-1",
                    "姉は東京のIT企業に勤めています。",
                    "My older sister is employed at an IT company in Tokyo.",
                    "Older-sister Tokyo IT-company-at employed-state-is.",
                    [
                        tok("姉は", "あねは", "ane wa", "my older sister", "Noun"),
                        tok("東京の", "とうきょうの", "toukyou no", "Tokyo's", "Noun"),
                        tok("勤めています", "つとめています", "tsutomete imasu", "is employed", "Grammar")
                    ],
                    "勤めている indicates ongoing occupational employment state."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-7-1",
                    "田中さんの電話番号を（　　）か。「いいえ、知りません。」",
                    "Do you know Tanaka-san's phone number? 'No, I don't know.'",
                    ["知っています", "知ります", "知覚します", "知ってある"],
                    0,
                    [
                        "Correct! State of possessing information requires 知っています.",
                        "Incorrect. 知ります means 'I will find out in the future'.",
                        "Incorrect. 知覚します means sensory perception in technical terms.",
                        "Incorrect. 〜てある is only for deliberate actions on objects."
                    ],
                    "〜ている for state of knowledge",
                    "Possession of knowledge requires the continuous state form."
                )
            ],
            "tags": ["N5", "Genki L7", "Continuous State", "Verbs"]
        },

        # 10. Lesson 8: 普通形 (Short / Informal Forms) & 〜と思う
        {
            "id": "gp-genki1-short-forms-to-omou",
            "title": "普通形 + と思う / と言っていた (Short Forms, Thoughts & Quotations)",
            "meaning": "Plain/short forms (辞書形, ない形, た形, なかった形) are required before quotative particles: 〜と思う (I think that...) and 〜と言う (They said that...).",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 8: Barbecue",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Plain sentence + と思います / と言っていました (Noun/な-adj non-past takes だ: 暇だと思う)",
            "nuance": "DA-DROP TRAP: In polite speech you say 暇です, but before と it MUST be 暇だ (だ cannot be dropped in affirmative non-past for nouns/na-adjectives).",
            "keyTakeaway": "MUG-UP: Inside quotes with と, use short forms! Noun/な-adj present affirmative requires だ (学生だと思う).",
            "sentences": [
                make_sentence(
                    "s-g1-8-1",
                    "明日は雨が降ると思います。",
                    "I think that it will rain tomorrow.",
                    "Tomorrow topic rain will-fall quote think.",
                    [
                        tok("明日", "あした", "ashita", "tomorrow", "Noun"),
                        tok("雨が降る", "あめがふる", "ame ga furu", "rain falls (plain)", "Verb"),
                        tok("と思います", "とおもいます", "to omoimasu", "I think that", "Grammar")
                    ],
                    "Short dictionary form 降る directly precedes quotative と思います."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-8-1",
                    "山田さんは「明日は（　　）」と言っていました。",
                    "Yamada-san said, 'I am free tomorrow.'",
                    ["暇だ", "暇です", "暇な", "暇に"],
                    0,
                    [
                        "Correct! な-adjectives in plain non-past affirmative require だ before と (暇だと言っていた).",
                        "Incorrect. 暇です is polite style; quotes typically take plain forms in indirect speech.",
                        "Incorrect. 暇な is the noun-modifying form, not a predicate.",
                        "Incorrect. 暇に is an adverbial form."
                    ],
                    "Plain form before quotative と",
                    "Connecting a な-adjective in plain form to と言う."
                )
            ],
            "tags": ["N5", "Genki L8", "Short Forms", "Quotations"]
        },

        # 11. Lesson 10: Comparison A と B とどちらのほうが〜ですか
        {
            "id": "gp-genki1-comparisons",
            "title": "A と B とどちらのほうが〜ですか (Binary & Superlative Comparisons)",
            "meaning": "Comparing two items: 'Between A and B, which is more [adj]?' Response: 'A のほうが [adj] です'. Superlative: '[Group] の中で A が一番 [adj] です'.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 10: Winter Vacations Approaching",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "A と B と どちら / どっち のほうが [Adj] ですか | [Category] の中で A が一番 [Adj] です",
            "nuance": "Question word selection: For 2 choices, always use どちら (or casual どっち). For 3 or more choices, use question words like だれ, どこ, なに + が一番.",
            "keyTakeaway": "MUG-UP: 2 items = どちらのほうが. 3+ items = [Group] の中で [Item] が一番.",
            "sentences": [
                make_sentence(
                    "s-g1-10-1",
                    "肉と魚とどちらのほうが好きですか。「魚のほうが好きです。」",
                    "Which do you like better, meat or fish? 'I like fish better.'",
                    "Meat and fish which side like is? Fish side like is.",
                    [
                        tok("どちらのほうが", "どちらのほうが", "dochira no hou ga", "which one (comparative)", "Expression"),
                        tok("魚のほうが", "さかなのほうが", "sakana no hou ga", "fish (side)", "Expression"),
                        tok("好きです", "すきです", "suki desu", "like (polite)", "Adjective")
                    ],
                    "Binary choice answered with 〜のほうが."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-10-1",
                    "季節の（　　）春が一番好きです。",
                    "Among all the seasons, I like spring the best.",
                    ["中で", "間で", "上で", "先で"],
                    0,
                    [
                        "Correct! Group superlative takes 〜の中で ('among / out of').",
                        "Incorrect. 間で means between two physical points or during a time interval.",
                        "Incorrect. 上で means 'on top of' or 'upon doing'.",
                        "Incorrect. 先で means 'ahead / at the destination'."
                    ],
                    "Superlative formula 〜の中で",
                    "Expressing the superlative domain of comparison."
                )
            ],
            "tags": ["N5", "Genki L10", "Comparison", "Superlative"]
        },

        # 12. Lesson 11: 〜たり〜たりする
        {
            "id": "gp-genki1-tari-tari",
            "title": "〜たり〜たりする (Listing Non-Exhaustive Representative Actions)",
            "meaning": "Lists representative activities or states: 'Doing things like A and B (among others)'.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 11: After-Vacation Plans",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-た + り + V-た + りする (Tense is carried ONLY by the final する!)",
            "nuance": "NON-EXHAUSTIVE vs SEQUENTIAL: 〜て、〜て lists actions strictly chronologically in total. 〜たり〜たり implies you did A and B, plus other unnamed activities.",
            "keyTakeaway": "MUG-UP: Formed by adding り to plain past た-form! Tense is determined exclusively by the final する/しました.",
            "sentences": [
                make_sentence(
                    "s-g1-11-1",
                    "週末は買い物をしたり、映画を見たりしました。",
                    "Over the weekend, I did things like shopping and watching a movie.",
                    "Weekend topic shopping did-and, movie watched-and did.",
                    [
                        tok("買い物をしたり", "かいものをしたり", "kaimono o shitari", "did shopping and", "Grammar"),
                        tok("見たりしました", "みたりしました", "mitari shimashita", "watched and did (past)", "Grammar")
                    ],
                    "Listing two representative weekend pastimes."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-11-1",
                    "休みの日は本を（　　）散歩をしたりします。",
                    "On my days off, I do things like read books and take walks.",
                    ["読んだり", "読んで", "読むたり", "読みたり"],
                    0,
                    [
                        "Correct! 読む past is 読んだ, which takes り to form 読んだり.",
                        "Incorrect. 読んで is standard te-form, which cannot pair with たりする.",
                        "Incorrect. 読むたり is an incorrect conjugation (must attach to た-form).",
                        "Incorrect. 読みたり attaches incorrectly to the masu-stem."
                    ],
                    "〜たり conjugation from past form",
                    "Forming the representative action listing."
                )
            ],
            "tags": ["N5", "Genki L11", "Representative Actions", "Verbs"]
        },

        # 13. Lesson 12: 〜んです / 〜のだ (The Explanatory Mode)
        {
            "id": "gp-genki1-ndesu",
            "title": "〜んです / 〜のだ (The Explanatory Mode: Seeking & Giving Context)",
            "meaning": "Provides background explanation, clarifies reasons, asks for clarification, or invites empathy: 'The thing is... / You see...'",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 12: Feeling Sick",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "Plain form + んです | な-adj / Noun + な + んです (Note the required な!)",
            "nuance": "Emotional rapport marker: Without んです, '頭が痛いです' is a dry medical observation. With '頭が痛いんです', it communicates: 'The reason I look distressed is that I have a headache; please understand my situation.'",
            "keyTakeaway": "MUG-UP: Noun / な-adj + [なんです] (NOT だんです ❌!).",
            "sentences": [
                make_sentence(
                    "s-g1-12-1",
                    "どうして遅刻したのですか。「目覚まし時計が鳴らなかったんです。」",
                    "Why were you late? 'The thing is, my alarm clock didn't ring.'",
                    "Why late-did? Alarm clock rang-not-explanatory.",
                    [
                        tok("どうして", "どうして", "doushite", "why", "Adverb"),
                        tok("遅刻したのですか", "ちこくしたのですか", "chikoku shita no desu ka", "did you arrive late?", "Verb+Grammar"),
                        tok("鳴らなかったんです", "ならなかったんです", "naranakattan desu", "didn't ring (explanatory)", "Grammar")
                    ],
                    "Explanatory んです provides the empathetic reason for the mishap."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-12-1",
                    "明日は大事な試験で（　　）んです。今夜は遊びに行けません。",
                    "The thing is, I am busy with an important exam tomorrow. I cannot go out tonight.",
                    ["忙しい", "忙しだ", "忙しく", "忙しな"],
                    0,
                    [
                        "Correct! Plain form 忙しい connects directly to んです.",
                        "Incorrect. い-adjectives never take だ.",
                        "Incorrect. Adverbial form cannot attach to んです.",
                        "Incorrect. な is only for な-adjectives and nouns."
                    ],
                    "い-adjective connection to んです",
                    "Connecting an い-adjective to the explanatory mode."
                )
            ],
            "tags": ["N5", "Genki L12", "Explanatory", "Reason"]
        },

        # 14. Lesson 12: 〜ほうがいいです (Giving Advice)
        {
            "id": "gp-genki1-hou-ga-ii",
            "title": "〜ほうがいいです (Giving Concrete Advice: Had Better / Should)",
            "meaning": "Provides strong personal advice or recommendations: affirmative uses past た-form; negative uses plain negative ない-form.",
            "level": "N5",
            "book": "Genki I",
            "chapter": "Lesson 12: Feeling Sick",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-た + ほうがいい (Affirmative: Had better do) | V-ない + ほうがいい (Negative: Had better not do)",
            "nuance": "TENSE ASYMMETRY TRAP: Affirmative advice requires PAST た-form (病院に行ったほうがいい, NOT 行くほうがいい)! But negative advice requires PRESENT ない-form (無理をしないほうがいい).",
            "keyTakeaway": "MUG-UP: Affirmative advice = た-form (行ったほうがいい). Negative advice = ない-form (行かないほうがいい).",
            "sentences": [
                make_sentence(
                    "s-g1-12-2",
                    "熱があるなら、今日は早く家に帰って寝たほうがいいですよ。",
                    "If you have a fever, you had better go home early and sleep today.",
                    "Fever have if, today early home return slept-side good is.",
                    [
                        tok("熱があるなら", "ねつがあるなら", "netsu ga aru nara", "if you have a fever", "Grammar"),
                        tok("寝たほうがいいですよ", "ねたほうがいいですよ", "neta hou ga ii desu yo", "you had better sleep", "Grammar")
                    ],
                    "Affirmative recommendation uses past form 寝た."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-g1-12-2",
                    "風邪をひいているなら、冷たい水を（　　）ほうがいいです。",
                    "If you have caught a cold, you had better not drink cold water.",
                    ["飲まない", "飲まなかった", "飲んだ", "飲む"],
                    0,
                    [
                        "Correct! Negative advice requires plain present negative: 飲まないほうがいい.",
                        "Incorrect. 飲まなかった is past negative, which is ungrammatical before ほうがいい.",
                        "Incorrect. 飲んだ is affirmative advice ('you should drink').",
                        "Incorrect. 飲む violates standard native advice grammar."
                    ],
                    "Negative advice with ないほうがいい",
                    "Recommending abstention from an action."
                )
            ],
            "tags": ["N5", "Genki L12", "Advice", "Modality"]
        }
    ]
    return pts

if __name__ == '__main__':
    points = get_genki1_points()
    print(f"Genki I generated {len(points)} grammar points.")
