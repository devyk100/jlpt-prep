# -*- coding: utf-8 -*-
"""
Additional discrete grammar points for Shin Kanzen Master N2 Bunpou.
Ensures full coverage of Chapters 1, 2, 3, 5, 6, 8, 10, 12, 14, 17, 18, 19, 20, 21, 22, 24, 25, 26,
and Part 2 Special Functional Constructs (A to G).
"""
from data_full_genki1 import tok, make_sentence, make_quiz

def get_additional_skm_n2():
    return [
        # === CHAPTER 1: とき (TIME & OCCASIONS) ===
        {
            "id": "skm2-c1-tatan-ni",
            "title": "〜たとたん（に） (The Very Instant That / Concurrently Burst Forth)",
            "meaning": "The precise split-second an action finishes, an unexpected, instantaneous event occurs without warning: 'No sooner had... than / The moment that...'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 1: とき (Time & Occasions)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-た形 + とたん（に）",
            "nuance": "UNFORESEEN SURPRISE: Clause Y must be an instantaneous reaction outside the speaker's conscious control. You CANNOT use speaker's planned will or intention in clause Y (❌ 窓を開けたとたん、掃除した).",
            "keyTakeaway": "MUG-UP: V-た + とたんに = 'The instant X happened, unexpected surprise Y broke out!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-1-4",
                    "ドアを開けたとたんに、強烈な冷たい風が部屋の中に吹き込んできた。",
                    "The very instant I opened the door, a fierce freezing blast of wind swept into the room.",
                    "Door opened instant-at, fierce cold wind room-of inside-into blew.",
                    [
                        tok("開けたとたんに", "あけたとたんに", "aketa totan ni", "the very instant I opened", "Grammar")
                    ],
                    "Sudden physical reaction upon opening door."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-1-4",
                    "疲れてベッドに横になった（　　）、あっという間に眠りに落ちてしまった。",
                    "The moment I lay down on the bed from sheer exhaustion, I fell into a deep sleep in an instant.",
                    ["とたん", "最中", "ばかり", "一方"],
                    0,
                    [
                        "Correct! 横になったとたん expresses falling asleep instantaneous upon lying down.",
                        "Incorrect. 横になった最中 is ungrammatical (最中 requires ongoing action: 横になっている最中).",
                        "Incorrect. 横になったばかり denotes recent completion, not instantaneous reaction.",
                        "Incorrect. 横になった一方 is meaningless here."
                    ],
                    "V-た + とたん (Instantaneous reaction)",
                    "Falling asleep the split-second head hits pillow."
                )
            ],
            "tags": ["N2", "SKM Ch 1", "Time", "Instantaneous"]
        },

        # === CHAPTER 2: している (PROGRESS & SHIFTS) ===
        {
            "id": "skm2-c2-tsutsu-aru",
            "title": "〜つつある (Currently in Continuous Transition / Underway)",
            "meaning": "Indicates that an evolutionary process or dynamic transformation is steadily progressing in real time: 'is in the ongoing process of -ing'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 2: している (Progress & Shifts)",
            "streamId": "stream-trends",
            "streamName": "Momentum, Shifts & Inevitable Drift",
            "connection": "V-stem (masu-stem) + つつある",
            "nuance": "MACRO DYNAMIC EVOLUTION: Reserved for systemic, social, economic, or natural shifts (warming, healing, decaying, recovering). NOT used for mundane personal actions like 'ご飯を食べつつある' ❌.",
            "keyTakeaway": "MUG-UP: Verb-stem + つつある = 'Steadily evolving trend underway!'. Formal/written register.",
            "sentences": [
                make_sentence(
                    "s-skm2-2-3",
                    "医療技術の急速な進歩により、かつての難病も克服されつつある。",
                    "Owing to rapid advances in medical technology, formerly intractable illnesses are steadily being overcome.",
                    "Medical technology rapid progress due-to, former intractable-illnesses overcome-being-underway.",
                    [
                        tok("克服されつつある", "こくふくされつつある", "kokufuku saretsutsu aru", "is in the process of being overcome", "Grammar")
                    ],
                    "Formal scientific commentary on healthcare progression."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-2-3",
                    "地球温暖化の影響で、北極の氷が年々解け（　　）。",
                    "Due to the impacts of global warming, the Arctic ice is steadily melting year by year.",
                    ["つつある", "つつあることだ", "つつあるまい", "つつあるべきだ"],
                    0,
                    [
                        "Correct! 解けつつある describes the ongoing gradual environmental transformation.",
                        "Incorrect. つつあることだ is structurally incoherent.",
                        "Incorrect. つつあるまい is ungrammatical.",
                        "Incorrect. つつあるべきだ does not make sense here."
                    ],
                    "V-stem + つつある (Ongoing macro trend)",
                    "Observing continuous polar melting."
                )
            ],
            "tags": ["N2", "SKM Ch 2", "Aspect", "Macro Trend"]
        },

        # === CHAPTER 3: てから (SEQUENCE & INCEPTION) ===
        {
            "id": "skm2-c3-te-hajimete",
            "title": "〜てはじめて (Only After Experiencing X Did Y Truly Dawn Upon Me)",
            "meaning": "Expresses that only after an event occurred or only upon personally experiencing X did one truly recognize, understand, or realize situation Y.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 3: てから (Sequence & Inception)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-て形 + はじめて",
            "nuance": "EPIPHANY THROUGH FIRST EXPERIENCE: 'You don't appreciate health until you get sick': 病気になってはじめて健康のありがたさを知った (Only after falling ill did I appreciate the blessing of health).",
            "keyTakeaway": "MUG-UP: V-て + はじめて = 'Only after X happened did I finally open my eyes to Y!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-3-1",
                    "一人暮らしを始めてはじめて、親が毎日家事をしてくれていたありがたさに気づいた。",
                    "Only after beginning to live alone did I truly realize the immense gratitude I owe my parents for doing chores daily.",
                    "Living-alone started only-after, parents daily chores did gratitude realized.",
                    [
                        tok("始めてはじめて", "はじめてはじめて", "hajimete hajimete", "only after starting", "Grammar")
                    ],
                    "Young adult coming of age realization."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-3-1",
                    "実際に海外で生活し（　　）はじめて、自国の文化の特徴を客観的に見直すことができた。",
                    "Only after actually living abroad was I able to re-examine the characteristics of my own country's culture objectively.",
                    ["て", "たら", "ても", "つつ"],
                    0,
                    [
                        "Correct! 生活してみてはじめて (or 生活してはじめて) forms 'only after living abroad'.",
                        "Incorrect. 生活したらはじめて is ungrammatical.",
                        "Incorrect. 生活してもはじめて is invalid.",
                        "Incorrect. 生活しつつはじめて is grammatically impossible."
                    ],
                    "V-て + はじめて (Epiphany through experience)",
                    "Gaining objective cultural self-awareness through international exposure."
                )
            ],
            "tags": ["N2", "SKM Ch 3", "Sequence", "Realization"]
        },
        {
            "id": "skm2-c3-ue-de",
            "title": "〜上（で） (Upon Thorough Completion of Prerequisite X / In Doing X)",
            "meaning": "Two functions: (1) After completing prerequisite inspection/consultation X, proceed to Y ('After... / Upon...'); (2) In the context/domain of doing X ('When it comes to...').",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 3: てから (Sequence & Inception)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "Prerequisite Sense: V-た形 + 上で | Noun + の上で | Context Sense: V-辞書形 + 上で",
            "nuance": "DELIBERATE PREREQUISITE: Requires deliberate investigation, agreement, or thought: '家族と相談した上で、決断します' (After consulting with family, I will make my decision).",
            "keyTakeaway": "MUG-UP: V-た / Nounの + 上で = 'Only after thorough check X is complete will next action happen!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-3-2",
                    "契約書の内容をよくご確認いただいた上で、こちらにご署名をお願いいたします。",
                    "After having thoroughly verified the contents of the contract, please furnish your signature here.",
                    "Contract-of contents well verify-receive after-upon, here signature please-do.",
                    [
                        tok("ご確認いただいた上で", "ごかくにんいただいたうえで", "gokakunin itadaita ue de", "upon having verified", "Grammar")
                    ],
                    "Formal business contractual execution."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-3-2",
                    "担当者と詳しく話し合っ（　　）上で、今後のスケジュールを決定いたします。",
                    "After discussing the details with the person in charge, we will determine our future schedule.",
                    ["た", "て", "る", "ても"],
                    0,
                    [
                        "Correct! V-た + 上で expresses 'after having held discussions'.",
                        "Incorrect. 話し合って上で is ungrammatical (must be 話し合った上で).",
                        "Incorrect. 話し合う上で means 'in the process of discussing', which clashes with determining future schedule afterward.",
                        "Incorrect. 話し合っても上で is invalid."
                    ],
                    "V-た + 上で (Prerequisite step)",
                    "Strategic scheduling following bilateral discussions."
                )
            ],
            "tags": ["N2", "SKM Ch 3", "Prerequisite", "Sequence"]
        },

        # === CHAPTER 5: だけ (EXCLUSIVITY & LIMITS) ===
        {
            "id": "skm2-c5-nomi-narazu",
            "title": "〜のみならず (Not Only X, but Also Y - Formal & Broad)",
            "meaning": "Formal written equivalent of 〜だけでなく. Asserts that the scope of a phenomenon is not confined to X, but also encompasses Y.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 5: だけ (Exclusivity & Limits)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "Noun + のみならず | 普通形 (な-adj + である, Noun + である) + のみならず",
            "nuance": "BROAD HORIZON: Emphasizes that an impact ripples far beyond the immediate subject: '国内のみならず、全世界で' (Not only domestically, but across the entire globe).",
            "keyTakeaway": "MUG-UP: Noun / Clause + のみならず = 'Not only X, but also Y!'. Formal written prose.",
            "sentences": [
                make_sentence(
                    "s-skm2-5-1",
                    "このアニメは日本国内のみならず、欧米やアジアのファンにも熱狂的に愛されている。",
                    "This anime is passionately loved not only within Japan, but also by fans across Europe, America, and Asia.",
                    "This anime Japan domestic not-only, West and Asia fans-by-also enthusiastically loved-is.",
                    [
                        tok("国内のみならず", "こくないのみならず", "kokunai nominorazu", "not only domestically", "Grammar")
                    ],
                    "Describing global cultural resonance."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-5-1",
                    "彼は英語（　　）ならず、中国語とスペイン語も極めて流暢に操る。",
                    "Not only English, he also commands Chinese and Spanish with extreme fluency.",
                    ["のみ", "だけ", "ばかり", "ほど"],
                    0,
                    [
                        "Correct! 英語のみならず forms the classical 'not only X, but Y as well' collocation.",
                        "Incorrect. 英語だけならず is ungrammatical (must be だけでなく).",
                        "Incorrect. 英語ばかりならず is invalid (must be ばかりでなく).",
                        "Incorrect. 英語ほどならず does not exist."
                    ],
                    "Noun + のみならず (Expansive scope)",
                    "Praising multilingual linguistic proficiency."
                )
            ],
            "tags": ["N2", "SKM Ch 5", "Addition", "Formal Written"]
        },
        {
            "id": "skm2-c5-bakari-ka",
            "title": "〜ばかりか (Not Merely X, but Beyond That Even Y!)",
            "meaning": "Indicates that something does not stop at degree X, but extends unexpectedly to an even more astonishing, serious, or extreme degree Y.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 5: だけ (Exclusivity & Limits)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "普通形 (な-adj + な/である, Noun + である) + ばかりか (often paired with 〜さえ / 〜まで)",
            "nuance": "ESCALATION BEYOND EXPECTATION: Can be positive or negative, but conveys astonishment: '友達ばかりか、家族まで彼を疑った' (Not merely his friends, but even his own family doubted him).",
            "keyTakeaway": "MUG-UP: 普通形 + ばかりか... さえ = 'Not just X, but going so far as extreme Y!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-5-2",
                    "彼は約束の時間に遅刻したばかりか、謝罪の一言さえ口にしなかった。",
                    "He not only showed up late for the promised time, but he didn't even utter a single word of apology.",
                    "He promised-time late-was not-merely, apology single-word even mouth-to not-did.",
                    [
                        tok("遅刻したばかりか", "ちこくしたばかりか", "chikoku shita bakari ka", "not merely late", "Grammar")
                    ],
                    "Indignation at unrepentant bad manners."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-5-2",
                    "彼女は親切に道を教えてくれた（　　）か、目的地まで一緒に案内してくれた。",
                    "Not only did she kindly give me directions, she even guided me all the way to my destination.",
                    ["ばかり", "だけ", "ほど", "くらい"],
                    0,
                    [
                        "Correct! 教えてくれたばかりか expresses unexpected escalation of generosity.",
                        "Incorrect. 教えてくれただけか is a question ('only taught?').",
                        "Incorrect. 教えてくれたほどか is ungrammatical.",
                        "Incorrect. 教えてくれたくらいか does not form this structure."
                    ],
                    "普通形 + ばかりか (Unexpected escalation)",
                    "Recounting remarkable hospitality of a stranger."
                )
            ],
            "tags": ["N2", "SKM Ch 5", "Escalation", "Surprise"]
        },

        # === CHAPTER 6: について・相手にして (TOPICS & TARGETS) ===
        {
            "id": "skm2-c6-ni-kansuru",
            "title": "〜に関して / 〜に関する (Concerning / Pertaining To Formal Matters)",
            "meaning": "Formal, academic equivalent of 〜について. Pertaining to, dealing with, or relating to a broad thematic domain or investigation.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 6: について・相手にして (Topics & Targets)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + に関して / に関しては | Noun + に関する + Noun",
            "nuance": "BROADER INTELLECTUAL REACH: While について touches on the specific topic directly, に関して includes all surrounding contextual ramifications and research data.",
            "keyTakeaway": "MUG-UP: Noun + に関して = Formal 'Concerning / Regarding'. Modifying noun = に関する + Noun.",
            "sentences": [
                make_sentence(
                    "s-skm2-6-1",
                    "AIの倫理的な利用に関する国際シンポジウムが、来月東京で開催される。",
                    "An international symposium concerning the ethical utilization of AI will be held in Tokyo next month.",
                    "AI ethical usage concerning international-symposium, next-month Tokyo-in held-is.",
                    [
                        tok("利用に関する", "りようにかんする", "riyou ni kansuru", "concerning the utilization", "Grammar")
                    ],
                    "High-level academic conference announcement."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-6-1",
                    "環境問題（　　）関する新しい法案が、国会で可決された。",
                    "A new legislative bill concerning environmental issues was passed by the Diet.",
                    ["に", "を", "へ", "で"],
                    0,
                    [
                        "Correct! Noun + に関する is the standard adnominal modifier.",
                        "Incorrect. を関する is ungrammatical.",
                        "Incorrect. へ関する is invalid.",
                        "Incorrect. で関する does not exist."
                    ],
                    "Noun + に関する + Noun (Thematic modifier)",
                    "Legislative enactment on environmental affairs."
                )
            ],
            "tags": ["N2", "SKM Ch 6", "Topic", "Formal Prose"]
        },

        # === CHAPTER 8: 視点 (PERSPECTIVE & GROUNDS) ===
        {
            "id": "skm2-c8-ni-motozuite",
            "title": "〜に基づいて / 〜をもとに (Founded Upon / Grounded on Reliable Data)",
            "meaning": "Indicates the fundamental bedrock, empirical evidence, legal statue, or factual data upon which an action, plan, or creation is constructed.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 8: 視点 (Perspective & Grounds)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + に基づいて / に基づき | Noun + に基づく + Noun",
            "nuance": "LEGAL & SCIENTIFIC FOUNDATION: Used when policies, judgments, or novels are strictly derived from facts or laws: '事実に基づいて映画を作った' (Made a movie based on real facts).",
            "keyTakeaway": "MUG-UP: Noun + に基づいて = 'Grounded strictly upon facts, laws, or data!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-8-1",
                    "最新の科学的知見に基づいて、防災計画の抜本的な見直しが行われた。",
                    "A radical overhaul of the disaster prevention plan was carried out based upon the latest scientific insights.",
                    "Latest scientific insights based-upon, disaster-prevention plan radical overhaul conducted.",
                    [
                        tok("知見に基づいて", "ちけんにもとづいて", "chiken ni motozuite", "based on insights", "Grammar")
                    ],
                    "Policy revisions grounded on rigorous research."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-8-1",
                    "この小説は、歴史的な事実（　　）基づいて執筆された大作である。",
                    "This novel is a monumental work authored based upon historical facts.",
                    ["に", "を", "で", "へ"],
                    0,
                    [
                        "Correct! 事実に基づいて is the established formula for factual foundations.",
                        "Incorrect. 事実を基づいて is ungrammatical.",
                        "Incorrect. 事実で基づいて is invalid.",
                        "Incorrect. 事実へ基づいて is meaningless."
                    ],
                    "Noun + に基づいて (Factual foundation)",
                    "Literary creation based on historical documentation."
                )
            ],
            "tags": ["N2", "SKM Ch 8", "Foundation", "Evidence"]
        },
        {
            "id": "skm2-c8-ni-sotte",
            "title": "〜に沿って / 〜に沿った (In Line With Guidelines / Aligning Faithfully)",
            "meaning": "Indicates taking action along a continuous physical trajectory, or conforming faithfully to a prescribed manual, policy, guideline, or expectation.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 8: 視点 (Perspective & Grounds)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + に沿って / に沿い | Noun + に沿った + Noun",
            "nuance": "FAITHFUL ADHERENCE: Actions must conform seamlessly without deviating: 'マニュアルに沿って作業を進める' (Proceed strictly in accordance with the manual).",
            "keyTakeaway": "MUG-UP: Noun + に沿って = 'In strict alignment with the path/manual/policy!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-8-2",
                    "基本方針に沿って策定された計画に従い、着実に業務を推進してください。",
                    "Please steadily advance operations following the plan formulated in line with our fundamental policy.",
                    "Basic-policy along formulated plan follow, steadily operations advance please.",
                    [
                        tok("方針に沿って", "ほうしんにそって", "houshin ni sotte", "in line with the policy", "Grammar")
                    ],
                    "Managerial directive on operational fidelity."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-8-2",
                    "お客様のご要望（　　）沿った最適なプランをご提案させていただきます。",
                    "We will humbly propose the optimal plan strictly tailored in line with our customer's requests.",
                    ["に", "を", "で", "へ"],
                    0,
                    [
                        "Correct! ご要望に沿った (in line with customer requests) is standard commercial Japanese.",
                        "Incorrect. ご要望を沿った is ungrammatical.",
                        "Incorrect. ご要望で沿った is invalid.",
                        "Incorrect. ご要望へ沿った does not exist."
                    ],
                    "Noun + に沿った + Noun (Faithful alignment)",
                    "Tailoring a customized proposal to client specifications."
                )
            ],
            "tags": ["N2", "SKM Ch 8", "Guideline", "Alignment"]
        },

        # === CHAPTER 10: やる・やらない (ACTION & OMISSION) ===
        {
            "id": "skm2-c10-nuki-de",
            "title": "〜抜きで / 〜抜きにして（は） (Dispensing With / Without the Element Of)",
            "meaning": "Doing an action while omitting, dispensing with, or setting aside a standard accompanying element (formal greetings, alcohol, sugar, or a person's presence).",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 10: やる・やらない (Action & Omission)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + 抜きで / 抜きにして / 抜きには | Noun + 抜きの + Noun",
            "nuance": "CONSCIOUS EXCLUSION: 'お世辞抜きで' (Without flattery / brutally honest), '冗談は抜きにして' (Jokes aside / seriously).",
            "keyTakeaway": "MUG-UP: Noun + 抜きで = 'Without X / Dispensing with X!'. (お世辞抜きで = Flattery aside).",
            "sentences": [
                make_sentence(
                    "s-skm2-10-1",
                    "前置きは抜きにして、早速本日のメインアジェンダに入りましょう。",
                    "Dispensing with preliminary pleasantries, let us dive straight into today's main agenda.",
                    "Preamble dispensing-with, promptly today main-agenda enter let-us.",
                    [
                        tok("前置きは抜きにして", "まえおきはぬきにして", "maeoki wa nuki ni shite", "dispensing with pleasantries", "Grammar")
                    ],
                    "Crisp, efficient chairperson opening a executive meeting."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-10-1",
                    "お世辞（　　）で、あなたの書いた論文は非常に独創的で素晴らしいです。",
                    "Without a single shred of flattery, the thesis you have written is extraordinarily original and splendid.",
                    ["抜き", "切れ", "限り", "きり"],
                    0,
                    [
                        "Correct! お世辞抜きで is the idiomatic phrase for 'without flattery / speaking genuinely'.",
                        "Incorrect. お世辞切れで is ungrammatical.",
                        "Incorrect. お世辞限りで is invalid.",
                        "Incorrect. お世辞きりで does not exist in this sense."
                    ],
                    "Noun + 抜きで (Dispensing with pleasantries)",
                    "Giving sincere academic praise without polite exaggeration."
                )
            ],
            "tags": ["N2", "SKM Ch 10", "Omission", "Directness"]
        },

        # === CHAPTER 12: 最高・最低 (EXTREMES & LIMITS) ===
        {
            "id": "skm2-c12-dokoroka",
            "title": "〜どころか (Far From Being X, on the Contrary Far Worse Y!)",
            "meaning": "Emphatically rejects baseline assertion X, revealing that the true situation is dramatically opposite, vastly worse, or extraordinarily different.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 12: 最高・最低 (Extremes & Limits)",
            "streamId": "stream-contrasts",
            "streamName": "Paradox, Concession & Contrast",
            "connection": "Noun + どころか | 普通形 (な-adj bare/な, Noun bare) + どころか",
            "nuance": "RADICAL REVERSAL: 'Far from getting better, it got worse!': '貯金どころか、借金まで抱えてしまった' (Far from saving money, I ended up saddled with debts!).",
            "keyTakeaway": "MUG-UP: X どころか Y = 'Forget about X! Reality is the extreme polar opposite Y!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-12-1",
                    "喉が痛くて、ご飯を食べるどころか、水を一口飲むことさえできない。",
                    "My throat hurts so severely that far from eating meals, I cannot even swallow a single sip of water.",
                    "Throat hurts, rice eating far-from, water single-sip drink even cannot.",
                    [
                        tok("食べるどころか", "たべるどころか", "taberu dokoroka", "far from eating", "Grammar")
                    ],
                    "Exemplifying acute inflammation preventing basic sustenance."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-12-1",
                    "景気は回復する（　　）か、ますます悪化の一途をたどっている。",
                    "Far from the economy recovering, it is steadily following a continuous path of further deterioration.",
                    ["どころ", "ばかり", "ばかりで", "だけ"],
                    0,
                    [
                        "Correct! 回復するどころか negates recovery to assert continuous deterioration.",
                        "Incorrect. 回復するばかりか means 'not only did it recover, but also...'.",
                        "Incorrect. 回復するばかりでか is ungrammatical.",
                        "Incorrect. 回復するだけか is a question."
                    ],
                    "普通形 + どころか (Radical reversal)",
                    "Bleak economic appraisal debunking false optimism."
                )
            ],
            "tags": ["N2", "SKM Ch 12", "Contrast", "Reversal"]
        },

        # === CHAPTER 14: 比べる (COMPARISON & CONTRAST) ===
        {
            "id": "skm2-c14-ippou-de",
            "title": "〜一方で (While on One Hand X, on the Other Hand Y)",
            "meaning": "Presents two contrasting, parallel, or complementary facets of a single subject or broader situation.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 14: 比べる (Comparison & Contrast)",
            "streamId": "stream-contrasts",
            "streamName": "Paradox, Concession & Contrast",
            "connection": "普通形 (な-adj + な/である, Noun + である) + 一方（で）",
            "nuance": "DUAL PERSPECTIVE: Does not mean one trend replaces another; rather, both coexist simultaneously: '便利になった一方で、プライバシーの懸念も増えた' (While it has become convenient, privacy concerns have also multiplied).",
            "keyTakeaway": "MUG-UP: 普通形 + 一方で = 'Two sides of the same coin! While X is true, Y coexists!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-14-1",
                    "リモートワークは通勤のストレスを減らした一方で、社員間のコミュニケーション不足を生んだ。",
                    "While remote work reduced the stress of commuting, it simultaneously gave rise to a shortage of communication among staff.",
                    "Remote-work commuting stress reduced while, staff-among communication shortage birthed.",
                    [
                        tok("減らした一方で", "へらしたいっぽうで", "herashita ippou de", "while on one hand reducing", "Grammar")
                    ],
                    "Balanced workplace organizational analysis."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-14-1",
                    "観光客が急増して街が潤っている（　　）で、ゴミや騒音の問題が深刻化している。",
                    "While the town is prospering from a boom in tourists, problems with litter and noise pollution are worsening.",
                    ["一方", "ばかり", "反面", "あまり"],
                    0,
                    [
                        "Correct! 潤っている一方で balances economic prosperity against municipal disruptions.",
                        "Incorrect. 潤っているばかりで means 'only prospering' without contrasting dual clauses.",
                        "Incorrect. 潤っている反面で is grammatically awkward (反面 does not take で).",
                        "Incorrect. 潤っているあまりで is ungrammatical."
                    ],
                    "普通形 + 一方で (Dual contrasting facets)",
                    "Assessing municipal trade-offs of mass tourism."
                )
            ],
            "tags": ["N2", "SKM Ch 14", "Contrast", "Dual Facets"]
        },

        # === CHAPTER 17: きっかけ (CATALYSTS & ORIGINS) ===
        {
            "id": "skm2-c17-wo-keiki-ni",
            "title": "〜を契機に / 〜を契機として (Using Catalyst X as a Springboard for Change)",
            "meaning": "Indicates that an unexpected crisis, event, or occurrence served as the historic turning point or springboard that sparked broad reform or personal change.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 17: きっかけ (Catalysts & Origins)",
            "streamId": "stream-causality",
            "streamName": "Origins, Inevitable Cause & Scapegoats",
            "connection": "Noun + を契機に / を契機として / を契機にして",
            "nuance": "POSITIVE TRANSFORMATION FROM EVENT: Unlike きっかけ (which can be trivial), 契機 (けいき) carries gravitas: an event that ignited systemic reform, career pivots, or historical revolutions.",
            "keyTakeaway": "MUG-UP: Noun + を契機に = 'Taking event X as the historical turning point / catalyst for major change!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-17-1",
                    "大病を患ったことを契機に、彼はそれまでの不健康な生活習慣を徹底的に改めた。",
                    "Taking his bout with serious illness as a life-changing catalyst, he thoroughly overhauled his previously unhealthy lifestyle habits.",
                    "Serious-illness suffered that catalyst-as, he previous unhealthy lifestyle thoroughly reformed.",
                    [
                        tok("ことを契機に", "ことをけいきに", "koto o keiki ni", "taking that as a catalyst", "Grammar")
                    ],
                    "Decisive personal health turnaround following a medical scare."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-17-1",
                    "オリンピック開催を（　　）に、都内のバリアフリー化が一気に加速した。",
                    "Taking the hosting of the Olympic Games as a catalyst, barrier-free accessibility across the capital accelerated rapidly.",
                    ["契機", "原因", "目的", "次第"],
                    0,
                    [
                        "Correct! 開催を契機に highlights the Olympic Games as the prime catalyst for citywide architectural accessibility improvements.",
                        "Incorrect. 開催を原因に is unnatural syntax.",
                        "Incorrect. 開催を目的に means 'for the purpose of hosting'.",
                        "Incorrect. 開催を次第に is ungrammatical."
                    ],
                    "Noun + を契機に (Catalyst for transformation)",
                    "Urban transformation catalyzed by an international sporting event."
                )
            ],
            "tags": ["N2", "SKM Ch 17", "Catalyst", "Transformation"]
        },

        # === CHAPTER 18: 原因・理由 (OBJECTIVE CAUSES) ===
        {
            "id": "skm2-c18-dakeni",
            "title": "〜だけに (Precisely Because of Fact X, All the More Y)",
            "meaning": "Indicates that precisely because of a special circumstance, high expectation, or exceptional effort X, the resulting feeling or outcome in Y is all the more magnified.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 18: 原因・理由 (Objective Causes)",
            "streamId": "stream-causality",
            "streamName": "Origins, Inevitable Cause & Scapegoats",
            "connection": "普通形 (な-adj + な/である, Noun + である/bare) + だけに",
            "nuance": "NATURAL AMPLIFICATION: 'Because she practiced so diligently, her disappointment at losing was all the greater': 一生懸命練習しただけに、負けた悔しさは計り知れない.",
            "keyTakeaway": "MUG-UP: 普通形 + だけに = 'Precisely because of X, the sentiment or outcome Y is all the more intense!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-18-1",
                    "半年間寝る間も惜しんで準備しただけに、試験に合格した瞬間の喜びは格別だった。",
                    "Precisely because I had prepared for half a year without even sparing time for sleep, the joy the moment I passed the exam was truly extraordinary.",
                    "Half-year sleeping-time begrudging prepared precisely-because, exam passed moment-of joy extraordinary was.",
                    [
                        tok("準備しただけに", "じゅんびしただけに", "junbi shita dake ni", "precisely because of having prepared", "Grammar")
                    ],
                    "Euphoric sense of accomplishment following grueling dedication."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-18-1",
                    "ずっと楽しみにしていた旅行（　　）に、悪天候で中止になってショックが大きい。",
                    "Precisely because it was a trip I had been looking forward to for so long, the shock of it being cancelled due to bad weather is enormous.",
                    ["だけ", "ばかり", "ほど", "くらい"],
                    0,
                    [
                        "Correct! 旅行だっただけに (or 旅行だけに) amplifies the devastation precisely because anticipation had been so high.",
                        "Incorrect. 旅行ばかりに is ungrammatical.",
                        "Incorrect. 旅行ほどに does not convey this amplified causal disappointment.",
                        "Incorrect. 旅行くらいに does not fit."
                    ],
                    "Noun + だけに (Amplified emotional impact)",
                    "Heartbreaking disappointment magnified by long-held excitement."
                )
            ],
            "tags": ["N2", "SKM Ch 18", "Causality", "Amplification"]
        },
        {
            "id": "skm2-c18-kara-koso",
            "title": "〜からこそ (Precisely Because / For the Very Reason That)",
            "meaning": "Strongly emphasizes the genuine, indispensable reason for an action: 'It is precisely for this reason, and no other, that...'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 18: 原因・理由 (Objective Causes)",
            "streamId": "stream-causality",
            "streamName": "Origins, Inevitable Cause & Scapegoats",
            "connection": "普通形 + からこそ",
            "nuance": "DEFINITIVE JUSTIFICATION: Expresses heartfelt sincerity or tough love: 'あなたの将来を心配しているからこそ、厳しく言うのだ' (It is precisely because I care about your future that I speak harshly).",
            "keyTakeaway": "MUG-UP: 理由 + からこそ = 'Precisely because of this and this alone!'. Reject all other explanations.",
            "sentences": [
                make_sentence(
                    "s-skm2-18-2",
                    "困難な状況にある今だからこそ、チーム全員が団結して支え合う必要がある。",
                    "It is precisely because we find ourselves in difficult circumstances right now that the entire team must unite and support one another.",
                    "Difficult circumstances-in are now precisely-because, team all unite support-each-other need exists.",
                    [
                        tok("今だからこそ", "いまだからこそ", "ima da kara koso", "precisely because it is now", "Grammar")
                    ],
                    "Rallying cry during an organizational crisis."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-18-2",
                    "お互いを深く信頼している（　　）こそ、本音で議論を戦わせることができる。",
                    "It is precisely because we trust each other deeply that we can debate fiercely with raw candor.",
                    ["から", "ので", "ため", "なら"],
                    0,
                    [
                        "Correct! からこそ emphasizes the foundational bond of trust as the sole enabling reason for honest debate.",
                        "Incorrect. のでこそ is ungrammatical.",
                        "Incorrect. ためこそ does not exist.",
                        "Incorrect. ならこそ is archaic."
                    ],
                    "理由 + からこそ (Emphatic singular justification)",
                    "Deep mutual trust enabling productive conflict."
                )
            ],
            "tags": ["N2", "SKM Ch 18", "Causality", "Emphatic Justification"]
        },

        # === CHAPTER 19: 逆接 (CONCESSION & CONTRAST) ===
        {
            "id": "skm2-c19-monono",
            "title": "〜ものの / 〜とはいうものの (Although It Is True That X, Nevertheless Y)",
            "meaning": "Acknowledges a factual reality in clause X, but introduces a contrasting reality, shortfall, or hesitation in clause Y: 'Although... nevertheless / Granted that... yet'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 19: 逆接 (Concession & Contrast)",
            "streamId": "stream-contrasts",
            "streamName": "Paradox, Concession & Contrast",
            "connection": "普通形 (な-adj + な/である, Noun + である) + ものの | Noun / 普通形 + とはいうものの",
            "nuance": "UNMET EXPECTATIONS: What naturally ought to follow from X fails to materialize: '春とはいうものの、まだ風が冷たい' (Although calendar spring has arrived, the wind is still biting cold).",
            "keyTakeaway": "MUG-UP: 事実 + ものの = 'Granted that X is a fact, reality Y falls short!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-19-1",
                    "大学の日本語学科を卒業したものの、ビジネスの現場では思うように話せない。",
                    "Although I graduated from the university's Japanese department, in the actual business arena I cannot speak as fluently as I would like.",
                    "University Japanese-department graduated although, business arena-in as-hoped cannot-speak.",
                    [
                        tok("卒業したものの", "そつぎょうしたものの", "sotsugyou shita mono no", "although I graduated", "Grammar")
                    ],
                    "Humble realization of gap between academic credentials and real-world fluency."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-19-1",
                    "手術は無事に成功した（　　）の、完治するまでにはまだ数ヶ月のリハビリが必要だ。",
                    "Although the surgery succeeded without complications, several months of rehabilitation are still required before full recovery.",
                    ["もの", "こと", "わけ", "ところ"],
                    0,
                    [
                        "Correct! 成功したものの concedes surgical success while presenting the arduous rehab ahead.",
                        "Incorrect. 成功したことの is ungrammatical in this conjunctive position.",
                        "Incorrect. 成功したわけの is invalid.",
                        "Incorrect. 成功したところの is archaic."
                    ],
                    "普通形 + ものの (Realistic concession)",
                    "Tempering surgical relief with realistic rehabilitation horizon."
                )
            ],
            "tags": ["N2", "SKM Ch 19", "Concession", "Reality Check"]
        },

        # === CHAPTER 20: 結果 (OUTCOMES & CONCLUSIONS) ===
        {
            "id": "skm2-c20-ageku-ni",
            "title": "〜あげく（に） (After Endless Agony and Trouble, Disastrous Outcome Y)",
            "meaning": "Indicates that after enduring a prolonged, agonizing struggle, intense dispute, or hesitation, the matter concluded in a thoroughly regrettable, futile, or disastrous result.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 20: 結果 (Outcomes & Conclusions)",
            "streamId": "stream-causality",
            "streamName": "Origins, Inevitable Cause & Scapegoats",
            "connection": "V-た形 + あげく（に） | Noun + のあげく（に）",
            "nuance": "DISASTROUS CONCLUSION: Unlike 末に (which can end positively after effort), あげくに ALWAYS culminates in a negative, exhausted, or disastrous result (quitting, fighting, bankruptcy, failure).",
            "keyTakeaway": "MUG-UP: 長い苦労 + あげくに = 'After all that prolonged suffering, it ended in disaster!'. (Bad outcome only!).",
            "sentences": [
                make_sentence(
                    "s-skm2-20-2",
                    "何時間も激しく口論したあげく、二人は絶交してしまった。",
                    "After arguing fiercely for hours on end, the two of them ended up completely severing their friendship.",
                    "Many-hours fiercely argued after-all, two-people friendship-severed completely.",
                    [
                        tok("口論したあげく", "こうろんしたあげく", "kouron shita ageku", "after endless arguing", "Grammar")
                    ],
                    "Tragic, bitter fallout after prolonged squabbling."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-20-2",
                    "色々と思い悩んだ（　　）に、彼は会社を辞めて実家へ帰る道を選んだ。",
                    "After agonizing endlessly over various options, he ultimately chose the path of resigning from his company and returning to his hometown.",
                    ["あげく", "末", "次第", "おかげ"],
                    0,
                    [
                        "Correct! 思い悩んだあげくに captures prolonged psychological torment culminating in a weary resignation.",
                        "Incorrect. 末に is possible for neutral outcomes, but あげくに specifically highlights agonizing fatigue leading to quitting.",
                        "Incorrect. 次第に means 'gradually'.",
                        "Incorrect. おかげに does not form this structure."
                    ],
                    "V-た + あげくに (Weary negative culmination)",
                    "Exhausted departure after prolonged career angst."
                )
            ],
            "tags": ["N2", "SKM Ch 20", "Culmination", "Regrettable Result"]
        },

        # === CHAPTER 21: 強く言う (EMPHATIC ASSERTION) ===
        {
            "id": "skm2-c21-ni-chigai-nai",
            "title": "〜に違いない / 〜に相違ない (Unshakeable Conviction: There Is No Doubt That)",
            "meaning": "Expresses the speaker's total, unwavering subjective certainty based on convincing circumstantial evidence: 'Must be / Undoubtedly / Without question'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 21: 強く言う (Emphatic Assertion)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "普通形 (な-adj bare/である, Noun bare/である) + に違いない / に相違ない (formal written)",
            "nuance": "UNWAVERING INTUITION / EVIDENCE: '見てごらん、あの笑顔は合格したに違いない' (Look at that smile; she must have passed!). に相違ない is the solemn written legal/journalistic variant.",
            "keyTakeaway": "MUG-UP: 普通形 + に違いない = 'I have zero doubt! It must definitely be so!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-21-2",
                    "夜遅くまで部屋の明かりがついている。山田さんはまだ残業しているに違いない。",
                    "The lights in the office room are on late into the night. Yamada-san must undoubtedly still be working overtime.",
                    "Night late room lights on-are. Yamada-san still overtime-doing must-be.",
                    [
                        tok("残業しているに違いない", "ざんぎょうしているにちがいない", "zangyou shite iru ni chigai nai", "must undoubtedly be working overtime", "Grammar")
                    ],
                    "Firm deduction from observable nighttime lighting."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-21-2",
                    "これほど緻密に作られた偽札は、専門家の手によるものに（　　）。",
                    "Counterfeit bills crafted with this level of meticulous precision must undoubtedly be the work of an expert.",
                    ["相違ない", "限りない", "過言ではない", "他ならない"],
                    0,
                    [
                        "Correct! 専門家の手によるものに相違ない expresses authoritative certainty in formal prose.",
                        "Incorrect. 限りない means 'boundless'.",
                        "Incorrect. 過言ではない means 'it is no exaggeration to say'.",
                        "Incorrect. 他ならない takes からに他ならない (nothing other than because)."
                    ],
                    "Noun + に相違ない (Solemn deductive certainty)",
                    "Forensic investigator concluding counterfeit currency origin."
                )
            ],
            "tags": ["N2", "SKM Ch 21", "Assertion", "Certainty"]
        },

        # === CHAPTER 22: だろうと思う (SPECULATION & PROBABILITY) ===
        {
            "id": "skm2-c22-kane-nai",
            "title": "〜かねない (Dangerous Potential to Trigger Catastrophe)",
            "meaning": "Warns of a severe risk that an ongoing reckless behavior, oversight, or flaw could easily result in a terrible disaster: 'Could well lead to... / Liable to cause...'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 22: だろうと思う (Speculation & Probability)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-stem (masu-stem) + かねない",
            "nuance": "STRICTLY ADVERSE FOREWARNING: Only used for disasters, deaths, accidents, bankruptcies, or leaks: 'スピードの出しすぎは重大な事故を引き起こしかねない' (Excessive speed is liable to trigger a fatal accident).",
            "keyTakeaway": "MUG-UP: Verb-stem + かねない = 'HIGH DANGER! Liable to trigger catastrophe!'. Negative risk only.",
            "sentences": [
                make_sentence(
                    "s-skm2-22-2",
                    "このような杜撰な管理を続けていれば、顧客データの流出を招きかねない。",
                    "If we continue such careless management, we could very well trigger a catastrophic leak of customer data.",
                    "This-kind-of careless management continue-if, customer-data leak invite-could-well.",
                    [
                        tok("招きかねない", "まねきかねない", "manekikanenai", "could well invite disaster", "Grammar")
                    ],
                    "Urgent cybersecurity compliance audit warning."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-22-2",
                    "そんな乱暴な運転をしていたら、いつか人を（　　）かねませんよ。",
                    "If you keep driving recklessly like that, you are liable to run someone over one day.",
                    ["はね", "はねる", "はねた", "はねて"],
                    0,
                    [
                        "Correct! Verb-stem はね + かねません warns of the imminent risk of hitting a pedestrian.",
                        "Incorrect. はねるかねません is ungrammatical (must use masu-stem, not dictionary form).",
                        "Incorrect. はねたかねません is invalid.",
                        "Incorrect. はねてかねません does not exist."
                    ],
                    "V-stem + かねない (Severe adverse hazard)",
                    "Warning a reckless motorist of fatal collision risk."
                )
            ],
            "tags": ["N2", "SKM Ch 22", "Risk", "Adverse Warning"]
        },
        {
            "id": "skm2-c22-kaneru",
            "title": "〜かねる (Psychologically Unable / Politely Refusing on Principle)",
            "meaning": "Indicates that due to ethical, legal, commercial, or emotional constraints, the speaker is completely unable to perform an action: 'Cannot / Am in no position to / Must regretfully decline'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 22: だろうと思う (Speculation & Probability)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-stem (masu-stem) + かねる",
            "nuance": "POLITE BUSINESS REFUSAL: 'いたしかねます' (We regret that we cannot do so). '賛成しかねる' (I find it impossible to agree in good conscience). It is an affirmative form with NEGATIVE meaning!",
            "keyTakeaway": "MUG-UP: Verb-stem + かねる = AFFIRMATIVE FORM with NEGATIVE MEANING! 'I cannot in good conscience do that'.",
            "sentences": [
                make_sentence(
                    "s-skm2-22-3",
                    "お客様の個人的な事情に関しましては、弊社としては関与いたしかねます。",
                    "Concerning personal matters of our customers, our company is regretfully in no position to intervene.",
                    "Customer personal circumstances concerning, our-company-as intervene cannot-regretfully.",
                    [
                        tok("関与いたしかねます", "かんよいたしかねます", "kanyo itashikanemasu", "are regretfully unable to intervene", "Grammar")
                    ],
                    "Formal commercial disclaimer of third-party involvement."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-22-3",
                    "提示された条件はあまりに不公平であり、その契約には同意（　　）ます。",
                    "The proposed conditions are excessively inequitable, and I find it impossible to agree to that contract.",
                    ["しかね", "しかねない", "し得", "しそうにあり"],
                    0,
                    [
                        "Correct! 同意しかねます expresses principled, polite refusal to consent to unfair terms.",
                        "Incorrect. 同意しかねないます is ungrammatical nonsense.",
                        "Incorrect. 同意し得ます means 'can possibly agree' (opposite meaning).",
                        "Incorrect. 同意しそうにあります is invalid."
                    ],
                    "V-stem + かねる (Principled polite refusal)",
                    "Rejecting an exploitative contractual clause."
                )
            ],
            "tags": ["N2", "SKM Ch 22", "Polite Refusal", "Formal"]
        },

        # === CHAPTER 24: 義務・当然 (DUTY & OBLIGATION) ===
        {
            "id": "skm2-c24-koto-da",
            "title": "〜ことだ (Direct Practical Advice: You Should / Best Course Is To)",
            "meaning": "Offers direct, emphatic advice or an admonition to someone facing a dilemma: 'The best thing to do is / You should definitely...'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 24: 義務・当然 (Duty & Obligation)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 / V-ない形 + ことだ",
            "nuance": "SENIOR-TO-JUNIOR ADMONITION: Given by an elder, coach, teacher, or friend who knows the correct solution: '日本語を上達させたければ、毎日声を出して読むことだ' (If you want to master Japanese, the thing to do is read aloud every day). Never use upwards to a boss.",
            "keyTakeaway": "MUG-UP: V-る / V-ない + ことだ = 'Here is the golden rule you should follow!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-24-1",
                    "健康を維持したいなら、暴飲暴食を慎み、規則正しい生活を送ることだ。",
                    "If you wish to maintain your health, the best thing to do is refrain from binge eating and drinking, and lead a regulated lifestyle.",
                    "Health maintain want-if, binge-eating-drinking refrain, regulated life send thing-is.",
                    [
                        tok("送ることだ", "おくることだ", "okuru koto da", "the thing to do is to lead", "Grammar")
                    ],
                    "Sage wellness advice on lifestyle discipline."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-24-1",
                    "試験で実力を発揮したければ、前日は夜更かしをせ（　　）早く休むことだ。",
                    "If you want to perform to your full ability in the exam, you should not stay up late the night before and instead rest early.",
                    ["ずに", "ないで", "ぬで", "ず"],
                    0,
                    [
                        "Correct! 夜更かしをせずに早く休むことだ correctly pairs the negative modifier with the advice pattern ことだ.",
                        "Incorrect. せないで is ungrammatical (must be しないで).",
                        "Incorrect. せぬで is invalid.",
                        "Incorrect. せず早く休むことだ is possible, but せずに is the standard smooth adverbial clause."
                    ],
                    "V-る + ことだ (Practical wisdom advice)",
                    "Pre-exam rest and performance optimization advice."
                )
            ],
            "tags": ["N2", "SKM Ch 24", "Advice", "Admonition"]
        },
        {
            "id": "skm2-c24-zaru-wo-enai",
            "title": "〜ざるを得ない (Inevitably Compelled to Do Against One's Wish)",
            "meaning": "Indicates that despite personal reluctance or aversion, objective circumstances, rules, or harsh realities leave no alternative: 'Cannot help but / Am compelled to / Forced to...'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 24: 義務・当然 (Duty & Obligation)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-ない形 (drop ない) + ざるを得ない (する irregular: せざるを得ない)",
            "nuance": "UNWILLING RESIGNATION: You do not want to do it, but circumstances leave zero escape: 'これだけ証拠が揃っては、罪を認めざるを得ない' (Confronted with this much evidence, one cannot help but confess to the crime).",
            "keyTakeaway": "MUG-UP: V-ない stem + ざるを得ない (する→せざるを得ない) = 'I really don't want to, but I have NO OTHER CHOICE!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-24-2",
                    "台風で全便が欠航となったため、旅行の予定を延期せざるを得なかった。",
                    "Because all flights were cancelled due to the typhoon, we had no choice but to postpone our travel schedule.",
                    "Typhoon-by all-flights cancelled became because, travel-of schedule postpone compelled-was.",
                    [
                        tok("延期せざるを得なかった", "えんきせざるをえなかった", "enki sezaru o enakatta", "had no choice but to postpone", "Grammar")
                    ],
                    "Reluctant acceptance of uncontrollable force majeure."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-24-2",
                    "会社の業績が著しく悪化したため、不採算部門の閉鎖を決断（　　）ざるを得ない。",
                    "Because the company's financial performance deteriorated drastically, management is compelled to decide on closing unprofitable divisions.",
                    ["せ", "し", "さ", "す"],
                    0,
                    [
                        "Correct! する becomes せざるを得ない (irregular suru conjugation).",
                        "Incorrect. しざるを得ない is a classic learner trap (ungrammatical!).",
                        "Incorrect. さざるを得ない does not exist.",
                        "Incorrect. すざるを得ない is invalid."
                    ],
                    "する → せざるを得ない (Compelled reluctant action)",
                    "Executive restructuring compelled by severe losses."
                )
            ],
            "tags": ["N2", "SKM Ch 24", "Compulsion", "No Choice"]
        },

        # === CHAPTER 25: 強く感じる (OVERWHELMING SENSATIONS) ===
        {
            "id": "skm2-c25-te-tamaranai",
            "title": "〜てたまらない / 〜てしかたがない (Intolerably / Irresistibly Overwhelming)",
            "meaning": "An internal psychological emotion, physical sensation, or urge is so powerful that the speaker cannot endure or suppress it: 'Dying to / Unbearably / Cannot help but feel'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 25: 強く感じる (Overwhelming Sensations)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-て形 / い-adj-くて / な-adj-で + たまらない / しょうがない",
            "nuance": "INTOLERABLE INTENSITY: '会いたくてたまらない' (Dying to meet you), '寒くてたまらない' (Unbearably cold), '心配でたまらない' (Worried sick). First-person sensations.",
            "keyTakeaway": "MUG-UP: て-form + たまらない = 'Unbearably intense! I can't hold it back!'. (心配でたまらない = Worried sick).",
            "sentences": [
                make_sentence(
                    "s-skm2-25-3",
                    "一人で海外に留学している娘の安否が、心配でたまらない。",
                    "I am worried sick about the safety and well-being of my daughter studying abroad all on her own.",
                    "Alone overseas studying daughter-of safety, worried-sick intolerably.",
                    [
                        tok("心配でたまらない", "しんぱいでたまらない", "shinpai de tamaranai", "worried sick / unbearably anxious", "Grammar")
                    ],
                    "Parental visceral concern for a distant child."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-25-3",
                    "徹夜でレポートを書き上げて、今は眠くて（　　）。",
                    "Having finished writing the report overnight without sleep, I am dying of sleepiness right now.",
                    ["たまらない", "ならない", "いられない", "やまない"],
                    0,
                    [
                        "Correct! 眠くてたまらない expresses visceral, unbearable physiological fatigue.",
                        "Incorrect. 眠くてならない is unnatural (ならない is for spontaneous mental states like 思えてならない).",
                        "Incorrect. 眠くていられない is ungrammatical.",
                        "Incorrect. 眠くてやまない is invalid."
                    ],
                    "い-adj-くて + たまらない (Unbearable physical state)",
                    "Overwhelming exhaustion after an all-nighter."
                )
            ],
            "tags": ["N2", "SKM Ch 25", "Sensation", "Visceral Intensity"]
        },

        # === CHAPTER 26: 敬語・待遇表現 (POLITE EXPRESSIONS) ===
        {
            "id": "skm2-c26-te-itadaku",
            "title": "〜ていただく / 〜くださる (Benefactive Exchanges in Formal Business Register)",
            "meaning": "Polite business equivalents of favor receipt and bestowment: 〜ていただく (humbly receive an action from an esteemed party); 〜くださる (an esteemed party graciously performs an action for us).",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 26: 敬語・待遇表現 (Polite Expressions)",
            "streamId": "stream-social",
            "streamName": "Social Coordinates, Deference & Humility",
            "connection": "V-て形 + いただく / いただきます | V-て形 + くださる / くださいます",
            "nuance": "BUSINESS PROTOCOL: In professional correspondence: 'ご検討いただけますと幸いです' (We would be honored if you would kindly consider this).",
            "keyTakeaway": "MUG-UP: V-て + いただく = 'We humbly receive your gracious deed'. V-て + くださる = 'You graciously do for us'.",
            "sentences": [
                make_sentence(
                    "s-skm2-26-1",
                    "多忙な時期にもかかわらず、貴重なお時間を割いていただき心より御礼申し上げます。",
                    "Despite it being a hectic period, I express my heartfelt thanks for you generously taking your precious time for us.",
                    "Hectic period despite, precious time sparing-receive-humbly heart-from thanks express.",
                    [
                        tok("割いていただき", "さいていただき", "saite itadaki", "humbly receiving your sparing of time", "Grammar")
                    ],
                    "Formal business correspondence expressing profound appreciation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-26-1",
                    "こちらの企画書につきまして、ご意見を（　　）いただけますでしょうか。",
                    "Concerning this proposal, could we possibly have you share your valuable opinions?",
                    ["お聞かせ", "ご案内", "拝見", "申し上げて"],
                    0,
                    [
                        "Correct! お聞かせいただけますでしょうか politely requests the client to let us hear their thoughts.",
                        "Incorrect. ご案内いただけますでしょうか means 'could you guide us'.",
                        "Incorrect. 拝見 is humble for speaker's own viewing.",
                        "Incorrect. 申し上げていただけますでしょうか is ungrammatical."
                    ],
                    "お + stem + いただく (Deferential client request)",
                    "Soliciting client feedback on a corporate proposal."
                )
            ],
            "tags": ["N2", "SKM Ch 26", "Keigo", "Business Benefactive"]
        },

        # === PART 2: SPECIAL FUNCTIONAL & ARCHAIC FORMS (A TO G) ===
        {
            "id": "skm2-p2-kko-nai",
            "title": "〜っこない (No Way in Hell / Absolutely Out of the Question)",
            "meaning": "Emphatically denies any possibility of an action happening: 'There is absolutely no way / Impossible for someone to...'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Part 2 特殊な形式 A: 〜っこない (Part 2 Form A)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-stem (masu-stem) + っこない",
            "nuance": "CONVERSATIONAL CATEGORICAL REJECTION: Used in passionate speech to dismiss an absurd premise: 'こんな分厚い本、一日で読めっこないよ' (There is no way in hell anyone could read such a thick book in one day!).",
            "keyTakeaway": "MUG-UP: Verb-stem + っこない = 'ZERO CHANCE! Categorically impossible!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-p2-1",
                    "プロの選手相手に、初心者の私たちが勝ちっこないよ。",
                    "There's no way in hell we beginners could ever defeat professional athletes!",
                    "Pro athletes opponent-as, beginner us win-no-way.",
                    [
                        tok("勝ちっこない", "かちっこない", "kachikkonai", "no way we could win", "Grammar")
                    ],
                    "Blunt colloquial dismissal of an unrealistic match outcome."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-p2-1",
                    "地図も持たずに初めての山に入ったら、道に迷い（　　）よ。",
                    "If you enter an unfamiliar mountain without even a map, you are bound to get lost!",
                    ["っこない", "かねない", "きりない", "がちない"],
                    1,
                    [
                        "Incorrect. 迷いっこない would mean 'there is no way you could get lost', which is false.",
                        "Correct! 迷いかねない warns of the very real danger: 'you are liable to get lost'. Note: For っこない, a sentence would be: 道が分かりっこない (No way you could know the path!).",
                        "Incorrect. きりない does not attach to verb stems.",
                        "Incorrect. がちない is invalid."
                    ],
                    "Trap Check: っこない (Zero chance) vs かねない (Danger of happening)",
                    "Distinguishing impossible outcomes from dangerous risks."
                )
            ],
            "tags": ["N2", "SKM Part 2", "Colloquial Impossibility", "Form A"]
        },
        {
            "id": "skm2-p2-mai",
            "title": "〜まい / 〜まいか (Resolute Negative Will / Negative Conjecture)",
            "meaning": "Two functions: (1) Resolute negative intention: 'I am firmly resolved NEVER to do X again'; (2) Negative speculation: 'Surely X will not happen / Is it not so?'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Part 2 特殊な形式 B: 〜まい (Part 2 Form B)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Group 1: V-辞書形 + まい (行くまい) | Group 2: V-stem + まい or 辞書形 + まい (食べまい / 食べるまい) | する: すまい / するまい / せまい | くる: こまい / くるまい",
            "nuance": "STIFF LITERARY NEGATIVE RESOLVE: '二度とあのような過ちは繰り返すまいと誓った' (I vowed never to repeat such a blunder again).",
            "keyTakeaway": "MUG-UP: V-る / V-stem + まい = 'I vow NEVER to do it again!' (Negative will) or 'Surely won't happen'.",
            "sentences": [
                make_sentence(
                    "s-skm2-p2-2",
                    "あんな不愉快な思いをするくらいなら、あの店には二度と行くまい。",
                    "If I have to endure such an unpleasant experience, I vow never to set foot in that shop ever again.",
                    "That unpleasant experience suffer rather-than, that shop-to twice go-never-will.",
                    [
                        tok("行くまい", "いくまい", "ikumai", "vow never to go", "Grammar")
                    ],
                    "Steadfast personal vow after terrible customer service."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-p2-2",
                    "どんな困難があろうとも、途中で決して諦め（　　）と心に誓った。",
                    "No matter what hardships may arise, I swore in my heart never to give up halfway.",
                    ["まい", "ない", "ず", "ぬ"],
                    0,
                    [
                        "Correct! 諦めまいと心に誓った conveys resolute negative determination ('vowed never to give up').",
                        "Incorrect. 諦めないと心に誓った is everyday plain, whereas まい reflects the solemn written resolve of JLPT N2.",
                        "Incorrect. 諦めずと is ungrammatical.",
                        "Incorrect. 諦めぬと is archaic/classical."
                    ],
                    "V-stem + まい (Steadfast negative determination)",
                    "Unshakable vow to persevere through adversity."
                )
            ],
            "tags": ["N2", "SKM Part 2", "Negative Will", "Form B"]
        },
        {
            "id": "skm2-p2-majiki",
            "title": "〜まじき (Utterly Impermissible / Unpardonable for One in Such a Role)",
            "meaning": "Stiff archaic/literary moral prohibition: Indicates that an act is strictly unforgivable and utterly unbecoming of someone in a specific esteemed professional or social position.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Part 2 特殊な形式 D: 〜まじき (Part 2 Form D)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 + まじき + Noun (する irregular: すまじき or するまじき)",
            "nuance": "STRICT ETHICAL PROHIBITION: 'あるまじき行為' (Conduct that should never exist), '許すまじき暴言' (Unpardonable verbal abuse), '教育者にあるまじき態度' (Attitude unbecoming of an educator). Modifies an abstract noun.",
            "keyTakeaway": "MUG-UP: V-る + まじき + Noun = 'Impermissible behavior for that role!'. Example: 医師としてあるまじき行為.",
            "sentences": [
                make_sentence(
                    "s-skm2-p2-3",
                    "患者の秘密を外部に漏らすなど、医師としてあるまじき背信行為だ。",
                    "Leaking a patient's confidential records to outsiders is a treacherous betrayal utterly impermissible for a physician.",
                    "Patient secret outside-to leak like, doctor-as exist-impermissible betrayal is.",
                    [
                        tok("あるまじき背信行為", "あるまじきはいしんこうい", "arumajiki haishinkoui", "impermissible act of betrayal", "Grammar")
                    ],
                    "Stern denunciation of medical malpractice and ethical breach."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-p2-3",
                    "公金を私的に流用するなど、政治家としてある（　　）不正行為である。",
                    "Embezzling public funds for private use is an illicit act utterly unbecoming and impermissible for a politician.",
                    ["まじき", "べき", "はずの", "限りの"],
                    0,
                    [
                        "Correct! あるまじき captures the moral prohibition against corruption in public office.",
                        "Incorrect. あるべき不正行為 is contradictory ('illicit act that ought to exist'!).",
                        "Incorrect. あるはずの不正行為 implies expected corruption.",
                        "Incorrect. ある限りの means 'as much as exists'."
                    ],
                    "V-る + まじき + Noun (Severe ethical violation)",
                    "Condemning political embezzlement."
                )
            ],
            "tags": ["N2", "SKM Part 2", "Archaic Moral Ban", "Form D"]
        },
        {
            "id": "skm2-p2-bekarazu",
            "title": "〜べからず / 〜べからざる (Must Not / Strictly Prohibited on Signs & Decrees)",
            "meaning": "Classical, authoritative prohibition indicating that an action is strictly forbidden: 'Must not / Trespassing prohibited / Do not -'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Part 2 特殊な形式 E: 〜べからず (Part 2 Form E)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 + べからず (sentence end) | V-辞書形 + べからざる + Noun (する irregular: すべからず or するべからず)",
            "nuance": "OFFICIAL PUBLIC SIGNS & MOTTOES: '立ち入るべからず' (Do Not Enter / Trespassers Prohibited), '初心忘るべからず' (One Must Never Forget One's Initial Humility).",
            "keyTakeaway": "MUG-UP: V-る + べからず = Classical public prohibition: 'MUST NOT / STRICTLY FORBIDDEN!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-p2-4",
                    "危険につき、関係者以外この工事現場に立ち入るべからず。",
                    "Due to extreme danger: unauthorized personnel must not enter this construction site under any circumstances.",
                    "Danger due-to, related-personnel besides this construction-site enter must-not.",
                    [
                        tok("立ち入るべからず", "たちいるべからず", "tachiiru bekarazu", "must not enter", "Grammar")
                    ],
                    "Authoritative warning notice posted at a hazardous construction perimeter."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-p2-4",
                    "壁に「ここにゴミを捨てる（　　）」という看板が立てられている。",
                    "A public signboard reading 'Do not dump garbage here' has been erected on the wall.",
                    ["べからず", "まい", "ざるを得ない", "かねない"],
                    0,
                    [
                        "Correct! 捨てるべからず is the classical authoritative sign prohibition against illegal dumping.",
                        "Incorrect. 捨てるまい is speaker's personal intention ('I will not dump').",
                        "Incorrect. 捨てるざるを得ない is ungrammatical.",
                        "Incorrect. 捨てるかねない is grammatically invalid."
                    ],
                    "V-る + べからず (Authoritative public prohibition)",
                    "Official placard prohibiting littering."
                )
            ],
            "tags": ["N2", "SKM Part 2", "Public Prohibition", "Form E"]
        },
        {
            "id": "skm2-p2-kai-ga-aru",
            "title": "〜甲斐があって / 〜甲斐もなく (Worth the Effort vs All in Vain)",
            "meaning": "Evaluates the return on dedicated effort: 甲斐があって indicates that painstaking labor yielded a gratifying reward; 甲斐もなく indicates that despite immense effort, it all proved completely in vain.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Part 2 特殊な形式 F: 〜甲斐 (Part 2 Form F)",
            "streamId": "stream-causality",
            "streamName": "Origins, Inevitable Cause & Scapegoats",
            "connection": "V-た形 / Noun + の + 甲斐があって (かいがあって) | V-た形 / Noun + の + 甲斐もなく",
            "nuance": "FRUITION VS FUTILITY: '苦労した甲斐があった' (It was worth all the hardship; joyful relief). '懸命な治療の甲斐もなく' (Despite all desperate medical treatments, all in vain; heartbreaking grief).",
            "keyTakeaway": "MUG-UP: 甲斐があって = 'Hard effort was fully rewarded!'. 甲斐もなく = 'Heartbreakingly all in vain!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-p2-5",
                    "毎日猛練習を重ねた甲斐があって、ついに全国大会で優勝を勝ち取ることができた。",
                    "It was thoroughly worth having practiced relentlessly every single day, as we finally succeeded in seizing victory at the national tournament.",
                    "Every-day fierce-practice repeated worth-existing, finally national-tournament victory seize could.",
                    [
                        tok("練習を重ねた甲斐があって", "れんしゅうをかさねたかいがあって", "renshuu o kasaneta kai ga atte", "worth having practiced relentlessly", "Grammar")
                    ],
                    "Jubilant athletic triumph crowning grueling preparation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-p2-5",
                    "医師団による懸命な救命活動の甲斐も（　　）、患者は息を引き取った。",
                    "Despite the desperate life-saving efforts by the medical team, tragically all was in vain, and the patient passed away.",
                    ["なく", "あって", "あり", "なしに"],
                    0,
                    [
                        "Correct! 甲斐もなく (all in vain) is required because the tragic death is a heartbreaking failure despite best efforts.",
                        "Incorrect. 甲斐もあって indicates success (contrasting with the patient's passing).",
                        "Incorrect. 甲斐もあり is ungrammatical with tragic results.",
                        "Incorrect. 甲斐もなしに is unidiomatic."
                    ],
                    "Noun + の甲斐もなく (Heartbreaking futility)",
                    "Mourning a patient whose life could not be saved despite heroic efforts."
                )
            ],
            "tags": ["N2", "SKM Part 2", "Effort & Fruition", "Form F"]
        },
        {
            "id": "skm2-p2-wo-oite",
            "title": "〜をおいて（ほかにない） (None Other Than / Unequivocally Unrivaled)",
            "meaning": "Asserts with deep admiration that person or entity X is the single unrivaled, supreme candidate: 'There is nobody other than X / Uniquely qualified'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Part 2 特殊な形式 G: 〜をおいて (Part 2 Form G)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "Noun + をおいて + [ほかにはいない / ほかにない]",
            "nuance": "UNRIVALED SUPREMACY: 'この大役を務められるのは、彼をおいて他にいない' (To handle this monumental role, there is nobody other than him). Always culminates in negative ほかにない / ほかにはいない.",
            "keyTakeaway": "MUG-UP: Noun + をおいて... ほかにない = 'NONE OTHER THAN X! Unrivaled choice!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-p2-6",
                    "この困難な国際紛争を調停できる人物は、百戦錬磨の彼をおいてほかにいない。",
                    "The person capable of mediating this grueling international conflict is none other than him with his battle-tested diplomatic experience.",
                    "This difficult international-conflict mediate can person, battle-tested him setting-aside besides none.",
                    [
                        tok("彼をおいてほかにいない", "かれをおいてほかにいない", "kare o oite hoka ni inai", "none other than him", "Grammar")
                    ],
                    "High tribute to diplomatic crisis leadership."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-p2-6",
                    "次期リーダーとしてチームをまとめられるのは、人望の厚い鈴木さん（　　）おいて他にいない。",
                    "As the next leader capable of uniting the team, there is none other than the deeply trusted Suzuki-san.",
                    ["を", "に", "で", "へ"],
                    0,
                    [
                        "Correct! 鈴木さんをおいて他にいない expresses that Suzuki-san is uniquely qualified.",
                        "Incorrect. 鈴木さんにおして is invalid.",
                        "Incorrect. 鈴木さんでおいて does not exist.",
                        "Incorrect. 鈴木さんへおいて is ungrammatical."
                    ],
                    "Noun + をおいて他にいない (Unrivaled supreme candidate)",
                    "Endorsing a trusted leader for executive captaincy."
                )
            ],
            "tags": ["N2", "SKM Part 2", "Unrivaled Supremacy", "Form G"]
        }
    ]

