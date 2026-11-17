# -*- coding: utf-8 -*-
"""
Additional discrete grammar points for Shin Kanzen Master N3 Bunpou.
Ensures full coverage of Units 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, and Form Classifications.
"""
from data_full_genki1 import tok, make_sentence, make_quiz

def get_additional_skm_n3():
    return [
        # === UNIT 3: 比較・限定 (COMPARISON & BOUNDARIES) ===
        {
            "id": "skm3-u3-kurai-nara",
            "title": "〜くらいなら / 〜ぐらいなら (Rather Than Suffer X, I Would Prefer Y)",
            "meaning": "If forced to endure an unacceptable condition X, I would far rather do alternative Y (even if Y is also drastic).",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 3: 比較・限定 (Comparison & Boundaries)",
            "streamId": "stream-contrasts",
            "streamName": "Paradox, Concession & Contrast",
            "connection": "V-辞書形 + くらいなら / ぐらいなら",
            "nuance": "UNACCEPTABLE ALTERNATIVE: X is considered so awful that the speaker prefers Y. Example: '満員電車に乗るくらいなら、1時間歩くほうがましだ' (Rather than ride a packed train, I'd rather walk an hour).",
            "keyTakeaway": "MUG-UP: V-る + くらいなら = 'Rather than do X, I'd rather...'. Expresses subjective value choice.",
            "sentences": [
                make_sentence(
                    "s-skm3-3-3",
                    "彼に頭を下げて頼むくらいなら、自分で失敗したほうがまだましだ。",
                    "Rather than bow my head and beg him for help, I would far rather fail on my own.",
                    "Him-to head lower begging rather-than, by-myself failed better is.",
                    [
                        tok("頼むくらいなら", "たのむくらいなら", "tanomu kurai nara", "rather than beg", "Grammar"),
                        tok("頭を下げる", "あたまをさげる", "atama o sageru", "to bow / humble oneself", "Expression")
                    ],
                    "Strong refusal of humiliation in preference of independent struggle."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-3-3",
                    "あんな失礼な人に謝る（　　）なら、仕事を辞めたほうがいい。",
                    "Rather than apologize to such a rude person, I'd rather quit my job.",
                    ["くらい", "ほど", "ばかり", "だけに"],
                    0,
                    [
                        "Correct! 謝るくらいなら expresses 'Rather than apologize, I'd prefer quitting'.",
                        "Incorrect. ほどなら is ungrammatical in this comparative preference structure.",
                        "Incorrect. ばかりなら does not express 'rather than'.",
                        "Incorrect. だけになら is incorrect."
                    ],
                    "V-る + くらいなら (Preferential aversion)",
                    "Rejecting an indignity in favor of another drastic course."
                )
            ],
            "tags": ["N3", "SKM Unit 3", "Comparison", "Preference"]
        },
        {
            "id": "skm3-u3-ni-kagiru",
            "title": "〜に限る (Nothing Beats X / X Is Unequivocally the Best)",
            "meaning": "Expresses the speaker's firm personal conviction that X is the single best, unmatched choice or course of action.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 3: 比較・限定 (Comparison & Boundaries)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "Noun + に限る | V-辞書形 / V-ない形 + に限る",
            "nuance": "SUBJECTIVE SUPREME CHOICE: This is the speaker's personal recommendation, not an objective law: '暑い日は冷たいビールに限る' (On a hot day, nothing beats a cold beer).",
            "keyTakeaway": "MUG-UP: Noun / V-る / V-ない + に限る = 'Nothing beats X!'. Peak personal advice.",
            "sentences": [
                make_sentence(
                    "s-skm3-3-4",
                    "風邪を引いたときは、温かいスープを飲んで早く寝るに限る。",
                    "When you catch a cold, nothing beats drinking hot soup and getting to sleep early.",
                    "Cold caught when, hot soup drink early sleep is-best.",
                    [
                        tok("寝るに限る", "ねるにかぎる", "neru ni kagiru", "nothing beats sleeping", "Grammar")
                    ],
                    "Universal folk wisdom framed as speaker's top recommendation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-3-4",
                    "夏の暑い午後には、冷えたスイカを食べる（　　）。",
                    "On a sweltering summer afternoon, nothing beats eating chilled watermelon.",
                    ["に限る", "にすぎない", "に違いない", "にかかわる"],
                    0,
                    [
                        "Correct! 食べるに限る asserts that chilled watermelon is the supreme summer remedy.",
                        "Incorrect. にすぎない means 'is merely / nothing more than'.",
                        "Incorrect. に違いない expresses certainty ('must surely be').",
                        "Incorrect. にかかわる means 'involves / affects'."
                    ],
                    "V-る + に限る (Supreme choice)",
                    "Declaring the definitive best remedy for summer heat."
                )
            ],
            "tags": ["N3", "SKM Unit 3", "Superlative", "Recommendation"]
        },

        # === UNIT 4: 対比・関係 (CONTRAST & RELATION) ===
        {
            "id": "skm3-u4-ni-taishite",
            "title": "〜に対して (In Contrast To / While X Is..., Y Is...)",
            "meaning": "Juxtaposes two distinct subjects or situations, highlighting their starkly opposite characteristics.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 4: 対比・関係 (Contrast & Relation)",
            "streamId": "stream-contrasts",
            "streamName": "Paradox, Concession & Contrast",
            "connection": "Noun + に対して | 普通形 (な-adj + な/である, Noun + である) + のに対して",
            "nuance": "POLAR OPPOSITES: Compares two separate entities A and B: '兄が社交的なのに対して、弟は内向的だ' (Whereas the older brother is sociable, the younger brother is introverted).",
            "keyTakeaway": "MUG-UP: A のに対して B = 'Whereas A is..., B is the complete opposite!'.",
            "sentences": [
                make_sentence(
                    "s-skm3-4-3",
                    "都市部で人口が急増しているのに対して、地方では過疎化が深刻化している。",
                    "In contrast to urban areas where the population is skyrocketing, depopulation is becoming severe in rural regions.",
                    "Urban-areas-in population rapidly-increasing whereas, rural-regions-in depopulation severe-becoming.",
                    [
                        tok("急増しているのに対して", "きゅうぞうしているのにたいして", "kyuuzou shite iru no ni taishite", "whereas increasing rapidly", "Grammar")
                    ],
                    "Contrasting socioeconomic trends between metropolis and countryside."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-4-3",
                    "昨日は大雨だった（　　）に対して、今日は雲一つない快晴だ。",
                    "In contrast to yesterday which had heavy downpours, today is clear skies without a single cloud.",
                    ["の", "こと", "もの", "わけ"],
                    0,
                    [
                        "Correct! Plain clause + のに対して is required when contrasting entire predicative clauses.",
                        "Incorrect. ことに対して is unidiomatic here.",
                        "Incorrect. ものに対して is ungrammatical.",
                        "Incorrect. わけに対して does not form this comparative pattern."
                    ],
                    "普通形 + のに対して (Contrasting clauses)",
                    "Juxtaposing yesterday's storm with today's clear weather."
                )
            ],
            "tags": ["N3", "SKM Unit 4", "Contrast", "Juxtaposition"]
        },
        {
            "id": "skm3-u4-ni-kurabete",
            "title": "〜に比べて (Compared With / Relative To)",
            "meaning": "Establishes a baseline entity X against which another entity Y is measured and evaluated.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 4: 対比・関係 (Contrast & Relation)",
            "streamId": "stream-contrasts",
            "streamName": "Paradox, Concession & Contrast",
            "connection": "Noun + に比べて / に比べ",
            "nuance": "QUANTITATIVE OR QUALITATIVE BENCHMARK: Unlike に対して (which contrasts polar opposites), に比べて measures differences in scale, price, difficulty, or degree.",
            "keyTakeaway": "MUG-UP: Noun + に比べて = 'Compared to X...'. Standard benchmark.",
            "sentences": [
                make_sentence(
                    "s-skm3-4-4",
                    "今年の夏は、例年に比べて格段に猛暑日が続いている。",
                    "Compared to ordinary years, extremely hot days are continuing at a markedly higher frequency this summer.",
                    "This-year summer, average-years-to compared remarkably heatwave-days continuing.",
                    [
                        tok("例年に比べて", "れいねんにくらべて", "reinen ni kurabete", "compared to average years", "Grammar")
                    ],
                    "Climatic comparison against historical baseline."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-4-4",
                    "以前の古いアパート（　　）比べて、今の部屋はずっと静かで快適だ。",
                    "Compared to my former old apartment, my current room is far quieter and more comfortable.",
                    ["に", "を", "で", "と"],
                    0,
                    [
                        "Correct! Noun + に比べて is the established benchmark comparison pattern.",
                        "Incorrect. を比べて is ungrammatical.",
                        "Incorrect. で比べて is invalid.",
                        "Incorrect. と比べて exists colloquially, but に比べて is the standard JLPT N3 formulation."
                    ],
                    "Noun + に比べて (Comparative benchmark)",
                    "Evaluating residential comfort against former living quarters."
                )
            ],
            "tags": ["N3", "SKM Unit 4", "Comparison", "Benchmark"]
        },

        # === UNIT 5: 原因・理由 (CAUSES & REASONS) ===
        {
            "id": "skm3-u5-okage-sei",
            "title": "〜おかげで vs 〜せいで (Grace of / Due to Fault of)",
            "meaning": "Expresses causal attribution: おかげで attributes a positive outcome to a benefactor; せいで blames an adverse outcome on a scapegoat.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 5: 原因・理由 (Causes & Reasons)",
            "streamId": "stream-causality",
            "streamName": "Origins, Inevitable Cause & Scapegoats",
            "connection": "普通形 (な-adj + な, Noun + の) + おかげで / せいで",
            "nuance": "VALUE POLARITY: おかげで = Gratitude ('Thanks to your guidance, I passed!'). せいで = Blame ('Because of the accident, I was late!'). (Ironical usage also exists: お前のせいで/お前のおかげで).",
            "keyTakeaway": "MUG-UP: おかげで = Good outcome (Blessed). せいで = Bad outcome (Blamed).",
            "sentences": [
                make_sentence(
                    "s-skm3-5-3",
                    "先生が熱心に教えてくださったおかげで、無事に合格できました。",
                    "Thanks to my teacher teaching me so passionately, I was able to pass safely.",
                    "Teacher passionately taught thanks-to, without-trouble could-pass.",
                    [
                        tok("教えてくださったおかげで", "おしえてくださったおかげで", "oshiete kudasatta okage de", "thanks to having taught me", "Grammar")
                    ],
                    "Heartfelt gratitude for mentorship."
                ),
                make_sentence(
                    "s-skm3-5-4",
                    "連日の夜更かしのせいで、朝から頭痛がひどい。",
                    "Because of staying up late night after night, I've had a terrible headache since morning.",
                    "Consecutive-days staying-up-late fault-due-to, morning-from headache severe.",
                    [
                        tok("夜更かしのせいで", "よふかしのせいで", "yofukashi no sei de", "due to staying up late", "Grammar")
                    ],
                    "Attributing bodily distress to personal poor habit."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-5-3",
                    "台風の（　　）で、楽しみにしていた旅行が急遽キャンセルになった。",
                    "Because of the typhoon, the trip I had been eagerly anticipating was cancelled at short notice.",
                    ["せい", "おかげ", "ため", "こと"],
                    0,
                    [
                        "Correct! せいで is required because cancelling an eagerly awaited trip is a negative/regrettable outcome.",
                        "Incorrect. おかげで implies a favorable/happy outcome.",
                        "Incorrect. ためで is ungrammatical (must be 台風のため, without で).",
                        "Incorrect. ことで is not used for blaming disastrous disruptions."
                    ],
                    "Noun + のせいで (Negative causal attribution)",
                    "Blaming an adverse event on severe weather."
                )
            ],
            "tags": ["N3", "SKM Unit 5", "Causality", "Blame & Gratitude"]
        },

        # === UNIT 6: 条件・仮定 (CONDITIONS & HYPOTHESES) ===
        {
            "id": "skm3-u6-sae-ba",
            "title": "〜さえ〜ば (If Only / Provided That Sole Prerequisite Is Met)",
            "meaning": "Specifies that as long as one minimum condition is fulfilled, everything else will be satisfactory or problems will disappear.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 6: 条件・仮定 (Conditions & Hypotheses)",
            "streamId": "stream-conditionals",
            "streamName": "Hypothetical Horizons & Logical Triggers",
            "connection": "Noun + さえ + V-ば / い-adj-ければ / な-adj-なら / Noun + なら | V-stem + さえすれば",
            "nuance": "MINIMAL SUFFICIENT CONDITION: 'If only this single factor exists, nothing else matters': 体さえ健康なら、どんな困難も乗り越えられる (As long as one has health, any obstacle can be surmounted).",
            "keyTakeaway": "MUG-UP: Noun + さえ + Verb-ば = 'If only X, then all is well!'. Focus on the single golden key.",
            "sentences": [
                make_sentence(
                    "s-skm3-6-3",
                    "パスポートさえあれば、とりあえず飛行機に乗ることはできる。",
                    "As long as you have your passport, you can board the plane for the time being.",
                    "Passport only if-exists, for-now airplane board can.",
                    [
                        tok("パスポートさえあれば", "ぱすぽーとさえあれば", "pasupooto sae areba", "if only you have a passport", "Grammar")
                    ],
                    "Highlighting the indispensable prerequisite."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-6-3",
                    "薬を飲み（　　）すれば、すぐに熱は下がりますよ。",
                    "As long as you just take your medicine, your fever will go down promptly.",
                    ["さえ", "こそ", "すら", "ばかり"],
                    0,
                    [
                        "Correct! Verb-stem + さえすれば expresses 'as long as you just do X'.",
                        "Incorrect. こそすれば is ungrammatical.",
                        "Incorrect. すらすれば is invalid.",
                        "Incorrect. ばかりすれば means repeatedly doing nothing else."
                    ],
                    "V-stem + さえすれば (Sole required action)",
                    "Simple clinical instruction: just take the medication."
                )
            ],
            "tags": ["N3", "SKM Unit 6", "Conditionals", "Prerequisite"]
        },
        {
            "id": "skm3-u6-tatoe-temo",
            "title": "たとえ〜ても (Even If / Even Granting That Hypothetical X Occurs)",
            "meaning": "Emphasizes that even in an extreme hypothetical case X, the consequence or speaker's resolute stance in Y remains completely unchanged.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 6: 条件・仮定 (Conditions & Hypotheses)",
            "streamId": "stream-conditionals",
            "streamName": "Hypothetical Horizons & Logical Triggers",
            "connection": "たとえ + V-ても / い-adj-くても / な-adj-でも / Noun + でも",
            "nuance": "UNSHAKEABLE RESOLVE: Even if the most extreme situation materializes, clause Y is unbending: たとえ両親に反対されても、夢を諦めない (Even if my parents oppose, I won't give up).",
            "keyTakeaway": "MUG-UP: たとえ + ても = 'Even if X happens, my resolve Y will NEVER waver!'.",
            "sentences": [
                make_sentence(
                    "s-skm3-6-4",
                    "たとえどんなに給料が高くても、危険な仕事は引き受けたくない。",
                    "Even if the salary were exceptionally high, I would never want to undertake a hazardous job.",
                    "Even-if how-much salary high-even-if, dangerous job undertake not-want.",
                    [
                        tok("たとえ高くても", "たとえたかくても", "tatoe takakutemo", "even if high", "Grammar")
                    ],
                    "Steadfast refusal prioritizing personal safety over money."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-6-4",
                    "（　　）失敗しても、最後まで全力を尽くしたなら悔いはない。",
                    "Even if I fail, as long as I gave it my absolute all until the very end, I will have no regrets.",
                    ["たとえ", "まるで", "決して", "まさか"],
                    0,
                    [
                        "Correct! たとえ pairs with 〜ても to mean 'Even if / Even supposing that'.",
                        "Incorrect. まるで pairs with ようだ ('just like').",
                        "Incorrect. 決して pairs with negative verbs ('never').",
                        "Incorrect. まさか expresses disbelief ('don't tell me...')."
                    ],
                    "たとえ〜ても (Hypothetical concession)",
                    "Acceptance of potential defeat without regret."
                )
            ],
            "tags": ["N3", "SKM Unit 6", "Conditionals", "Concession"]
        },

        # === UNIT 7: 目的・手段 (PURPOSE & MEANS) ===
        {
            "id": "skm3-u7-you-ni-purpose",
            "title": "〜ように (So That / In Order That - Non-Volitional Objective)",
            "meaning": "Expresses an objective or intended state toward which action is directed: 'So that X may become possible / so that X doesn't happen'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 7: 目的・手段 (Purpose & Means)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 (Potential / Intransitive non-volitional) / V-ない + ように",
            "nuance": "VOLITIONAL CONTRAST: ように takes non-volitional verbs (見える、聞こえる、忘れない, potential verbs). In contrast, ために takes conscious volitional actions by the same subject.",
            "keyTakeaway": "MUG-UP: V-ない / V-可能形 + ように = 'So that...'. Example: 忘れないようにメモする (Jot down so as not to forget).",
            "sentences": [
                make_sentence(
                    "s-skm3-7-1",
                    "後ろの席の人にもよく聞こえるように、マイクの音量を上げてください。",
                    "Please turn up the microphone volume so that people in the back seats can hear well too.",
                    "Back-of seats people-to-also well can-hear so-that, mic-of volume please-raise.",
                    [
                        tok("聞こえるように", "きこえるように", "kikoeru you ni", "so that it can be heard", "Grammar")
                    ],
                    "Intransitive potential verb 聞こえる expresses intended auditory perception."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-7-1",
                    "風邪を引か（　　）ように、暖かくして出かけなさい。",
                    "Dress warmly when you go out so that you don't catch a cold.",
                    ["ない", "ず", "ぬ", "なくて"],
                    0,
                    [
                        "Correct! V-ない + ように is the standard pattern for preventative purpose ('so as not to...').",
                        "Incorrect. 引かずように is ungrammatical.",
                        "Incorrect. 引かぬように is archaic/literary.",
                        "Incorrect. 引かなくてように is grammatically invalid."
                    ],
                    "V-ない + ように (Preventative purpose)",
                    "Preventing illness through warm clothing."
                )
            ],
            "tags": ["N3", "SKM Unit 7", "Purpose", "Objective"]
        },
        {
            "id": "skm3-u7-you-ni-suru",
            "title": "〜ようにする (Make an Effort To / Endeavor Habitually)",
            "meaning": "Indicates that the subject makes a conscious, ongoing effort or resolves to build a habit of doing (or not doing) action X.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 7: 目的・手段 (Purpose & Means)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 / V-ない + ようにする / ようにしている",
            "nuance": "CONSCIOUS HABITUAL EFFORT: ようにしている expresses an established personal policy: '毎朝ストレッチをするようにしている' (I make it a point to stretch every morning).",
            "keyTakeaway": "MUG-UP: V-る / V-ない + ようにする = 'Make sure to do / Endeavor to do!'.",
            "sentences": [
                make_sentence(
                    "s-skm3-7-2",
                    "健康のために、夜遅くには甘いものを食べないようにしている。",
                    "For the sake of my health, I make it a strict rule to avoid eating sweets late at night.",
                    "Health-of sake-for, night late sweets eat-not endeavor-am-doing.",
                    [
                        tok("食べないようにしている", "たべないようにしている", "tabenai you ni shite iru", "make a point of not eating", "Grammar")
                    ],
                    "Active self-discipline regarding dietary lifestyle."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-7-2",
                    "約束の時間には絶対に遅れない（　　）してください。",
                    "Please make sure you do not arrive late for the promised time.",
                    ["ように", "ために", "こと", "もの"],
                    0,
                    [
                        "Correct! ようにしてください is the polite formula for urging conscious adherence.",
                        "Incorrect. ためにしてください is ungrammatical.",
                        "Incorrect. ことにしてください means 'please pretend/decide'.",
                        "Incorrect. ものにしてください is invalid."
                    ],
                    "V-ない + ようにする (Urging effort)",
                    "Reminding someone to maintain punctuality."
                )
            ],
            "tags": ["N3", "SKM Unit 7", "Habit", "Effort"]
        },

        # === UNIT 8: 可能・確信 (CERTAINTY & LOGIC) ===
        {
            "id": "skm3-u8-wake-ga-nai",
            "title": "〜わけがない (There Is Absolutely No Way That... / Utter Impossibility)",
            "meaning": "Expresses the speaker's adamant, logical conclusion that something is completely impossible or out of the question.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 8: 可能・確信 (Certainty & Logic)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "普通形 (な-adj + な/である, Noun + の/である) + わけがない / わけはない",
            "nuance": "OBJECTIVE LOGICAL REJECTION: Based on known evidence or common sense, scenario X is mathematically or logically absurd: '彼が犯人のわけがない。その時私と一緒にいたのだから' (There's no way he is the culprit; he was with me).",
            "keyTakeaway": "MUG-UP: 普通形 + わけがない = 'Zero chance! There is no reason or basis for that to be true!'.",
            "sentences": [
                make_sentence(
                    "s-skm3-8-3",
                    "こんなに複雑なプロジェクトを、たった一人で一日で終わらせられるわけがない。",
                    "There is absolutely no way that a project this complex could be finished by a single person in just one day.",
                    "This complex project, just one-person-by one-day-in can-finish no-way.",
                    [
                        tok("終わらせられるわけがない", "おわらせられるわけがない", "owaraserareru wake ga nai", "there's no way it could be finished", "Grammar")
                    ],
                    "Adamant rejection of unrealistic workload expectation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-8-3",
                    "いつも真面目な山田さんが、会社の秘密を漏らす（　　）がありません。",
                    "There is no way that Yamada-san, who is always diligent and upright, would leak company secrets.",
                    ["わけ", "はず", "もの", "こと"],
                    0,
                    [
                        "Correct! わけがありません expresses absolute logical impossibility based on his trustworthy character.",
                        "Incorrect. はずがありません is also possible in speech, but 漏らすわけがありません is the primary syntactic match with がありません.",
                        "Incorrect. ものがありません does not express impossibility.",
                        "Incorrect. ことがありません means 'never happens'."
                    ],
                    "普通形 + わけがない (Logical impossibility)",
                    "Defending a colleague's integrity based on character."
                )
            ],
            "tags": ["N3", "SKM Unit 8", "Modality", "Impossibility"]
        },
        {
            "id": "skm3-u8-wake-dewa-nai",
            "title": "〜わけではない (It Doesn't Mean That... / Partial Negation)",
            "meaning": "Softens an assumption or clarifies that while things might appear so, it is not entirely or universally true: 'Not necessarily / It's not that...'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 8: 可能・確信 (Certainty & Logic)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "普通形 (な-adj + な/である, Noun + の/な/である) + わけではない / わけじゃない",
            "nuance": "AVOIDING ABSOLUTES: Used to prevent misunderstanding: '嫌いなわけではないが、今は食べたくない' (It's not that I dislike it, but I just don't feel like eating right now).",
            "keyTakeaway": "MUG-UP: 普通形 + わけではない = 'Partial denial! Don't jump to conclusions, it's not 100% that way!'.",
            "sentences": [
                make_sentence(
                    "s-skm3-8-4",
                    "日本に住んでいるからといって、誰もが日本語を上手に話せるわけではない。",
                    "Just because someone lives in Japan does not mean that everyone can speak Japanese fluently.",
                    "Japan-in living just-because, everyone Japanese skillfully can-speak not-necessarily.",
                    [
                        tok("話せるわけではない", "はなせるわけではない", "hanaseru wake dewa nai", "does not mean they can speak", "Grammar")
                    ],
                    "Refuting an overly simplistic stereotype."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-8-4",
                    "彼の提案に反対したけれど、彼のことが嫌いな（　　）ではない。",
                    "I opposed his proposal, but it's not that I dislike him as a person.",
                    ["わけ", "はず", "つもり", "せい"],
                    0,
                    [
                        "Correct! 嫌いなわけではない conveys 'it's not that I dislike him' (partial disclaimer).",
                        "Incorrect. 嫌いなはずではない is unnatural.",
                        "Incorrect. 嫌いなつもりではない is unidiomatic here.",
                        "Incorrect. 嫌いなせいではない means 'it's not due to disliking'."
                    ],
                    "な-adj + な + わけではない (Partial denial)",
                    "Separating professional critique from personal sentiment."
                )
            ],
            "tags": ["N3", "SKM Unit 8", "Modality", "Nuance Disclaimer"]
        },
        {
            "id": "skm3-u8-wake-niwa-ikanai",
            "title": "〜わけにはいかない (Cannot Afford To / Morally or Socially Bound Not To)",
            "meaning": "Indicates that even if the speaker wants to do X, social morals, duties, or practical constraints make it utterly impermissible: 'Cannot afford to do / In all conscience I cannot'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 8: 可能・確信 (Certainty & Logic)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 + わけにはいかない (cannot do) | V-ない形 + わけにはいかない (must do / cannot afford not to)",
            "nuance": "INTERNAL CONSCIENCE & SOCIAL CODE: Unlike physical inability (できない), わけにはいかない denotes moral, professional, or situational inhibition: '明日試験だから、ゲームをするわけにはいかない' (Since there's an exam tomorrow, I cannot afford to play games).",
            "keyTakeaway": "MUG-UP: V-る + わけにはいかない = 'Cannot do (conscience/duty forbids)'. V-ない + わけにはいかない = 'MUST do!'.",
            "sentences": [
                make_sentence(
                    "s-skm3-8-5",
                    "大事な会議の当日に、ちょっと熱があるくらいで仕事を休むわけにはいかない。",
                    "On the day of such a crucial meeting, I simply cannot afford to take off work just for a slight fever.",
                    "Crucial meeting day-on, slight fever exists just-by work take-off cannot-afford.",
                    [
                        tok("休むわけにはいかない", "やすむわけにはいかない", "yasumu wake ni wa ikanai", "cannot afford to take off", "Grammar")
                    ],
                    "Sense of professional duty overriding personal discomfort."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-8-5",
                    "友人に秘密にしてくれと頼まれたから、誰にも話す（　　）にはいかない。",
                    "Because my friend pleaded with me to keep it a secret, I cannot in all conscience tell anyone.",
                    ["わけ", "はず", "こと", "もの"],
                    0,
                    [
                        "Correct! 話すわけにはいかない conveys moral obligation not to betray trust.",
                        "Incorrect. 話すはずにはいかない is ungrammatical.",
                        "Incorrect. 話すことにはいかない is invalid.",
                        "Incorrect. 話すものにはいかない does not form this structure."
                    ],
                    "V-る + わけにはいかない (Moral constraint)",
                    "Honor-bound to keep a friend's confidence."
                )
            ],
            "tags": ["N3", "SKM Unit 8", "Modality", "Social Obligation"]
        },

        # === UNIT 9: 感情・評価 (EMOTION & EVALUATION) ===
        {
            "id": "skm3-u9-garu",
            "title": "〜がる / 〜がっている (Third-Person Manifestation of Desires & Sensations)",
            "meaning": "Describes observable behaviors indicating that someone other than the speaker feels an emotion, sensation, or desire.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 9: 感情・評価 (Emotion & Evaluation)",
            "streamId": "stream-social",
            "streamName": "Social Coordinates, Deference & Humility",
            "connection": "い-adj (drop い) + がる / がっている | な-adj (drop な) + がる | V-たい (drop い) + たがる / たがっている",
            "nuance": "THIRD-PERSON BARRIER: In Japanese, you cannot directly peer into another's heart to say '田中さんは痛い' ❌. You must describe observable signs: '痛がっている' (showing signs of pain).",
            "keyTakeaway": "MUG-UP: Third person's internal feeling = Stem + がる / たがる! Never bare 痛い or 行きたい for others.",
            "sentences": [
                make_sentence(
                    "s-skm3-9-1",
                    "弟は注射をひどく怖がって、病院の前で泣き出してしまった。",
                    "My little brother showed tremendous fear of the injection and burst into tears in front of the hospital.",
                    "Little-brother injection terribly feared-showing, hospital front burst-out-crying.",
                    [
                        tok("怖がって", "こわがって", "kowagatte", "showing fear / acting terrified", "Grammar")
                    ],
                    "Describing observable childish reaction to medical procedure."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-9-1",
                    "最近の若者は、海外旅行に行き（　　）なくなったと言われている。",
                    "It is said that young people these days have become less inclined to want to travel abroad.",
                    ["たがら", "たい", "たがり", "たく"],
                    0,
                    [
                        "Correct! 行きたがる becomes 行きたがらなくなった (observable third-person loss of desire).",
                        "Incorrect. 行きたいなくなった is ungrammatical (must be 行きたくなくなった, but that applies to speaker).",
                        "Incorrect. 行きたがりなくなった is invalid.",
                        "Incorrect. 行きたくなくなった reflects 1st-person rather than 3rd-person trend."
                    ],
                    "V-たい → たがらなくなる (3rd person desire trend)",
                    "Sociological observation about modern youth tendencies."
                )
            ],
            "tags": ["N3", "SKM Unit 9", "Psychological", "Third-Person"]
        },
        {
            "id": "skm3-u9-beki-da",
            "title": "〜べきだ / 〜べきではない (Should / Ought To - Moral Duty)",
            "meaning": "States that doing (or not doing) X is an obvious moral duty, ethical obligation, or universal social norm.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 9: 感情・評価 (Emotion & Evaluation)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 + べきだ / べきではない (する irregular: すべきだ or するべきだ)",
            "nuance": "ETHICAL / MORAL OUGHT: Expresses what common sense or civic duty dictates. Not used for strict institutional rules (which use なければならない). Avoid using it directly to superiors.",
            "keyTakeaway": "MUG-UP: V-る + べきだ / するべきだ (or すべきだ) = 'Moral duty / Universal right thing to do!'.",
            "sentences": [
                make_sentence(
                    "s-skm3-9-2",
                    "借りたお金は、どんなに親しい友人であっても期日通りに返す（　　）だ。",
                    "Money that you have borrowed ought to be repaid right on schedule, no matter how close a friend they may be.",
                    "Borrowed money, how-much close friend even-if schedule-according repay ought-to is.",
                    [
                        tok("返すべきだ", "かえすべきだ", "kaesu beki da", "ought to repay", "Grammar")
                    ],
                    "Moral principle governing personal financial integrity."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-9-2",
                    "自分のミスで他人に迷惑をかけたときは、すぐに謝罪（　　）だ。",
                    "When you inconvenience others through your own mistake, you ought to apologize immediately.",
                    ["すべき", "した", "するの", "すれば"],
                    0,
                    [
                        "Correct! 謝罪すべきだ (or 謝罪するべきだ) expresses universal ethical duty.",
                        "Incorrect. 謝罪しただ is ungrammatical.",
                        "Incorrect. 謝罪するのだ is explanatory, not moral prescription.",
                        "Incorrect. 謝罪すればだ is invalid."
                    ],
                    "する → すべきだ (Moral imperative)",
                    "Basic etiquette regarding apologies."
                )
            ],
            "tags": ["N3", "SKM Unit 9", "Duty", "Ethics"]
        },

        # === UNIT 10: 伝聞・推量 (HEARSAY & CONJECTURE) ===
        {
            "id": "skm3-u10-ni-yoru-to",
            "title": "〜によると / 〜によれば (According To Source of Information)",
            "meaning": "Identifies the external source, report, authority, or rumor from which subsequent information or conjecture was obtained.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 10: 伝聞・推量 (Hearsay & Conjecture)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + によると / によれば + [sentence ending in 〜そうだ / 〜ということだ / 〜らしい]",
            "nuance": "MANDATORY HEARSAY PAIRING: The sentence must conclude with an expression of reported speech or conjecture (〜そうだ、〜ということだ、〜らしい). You cannot end with speaker's direct fact or command.",
            "keyTakeaway": "MUG-UP: Noun + によると... 〜そうだ = 'According to source X, I hear that...'.",
            "sentences": [
                make_sentence(
                    "s-skm3-10-1",
                    "天気予報によると、明日の夕方から関東地方全域で大雪になるそうだ。",
                    "According to the weather forecast, heavy snow will reportedly blanket the entire Kanto region starting tomorrow evening.",
                    "Weather forecast according-to, tomorrow evening-from Kanto entire heavy-snow become reportedly.",
                    [
                        tok("天気予報によると", "てんきよほうによると", "tenki yohou ni yoru to", "according to the weather forecast", "Grammar")
                    ],
                    "Formal citation of meteorological bulletin."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-10-1",
                    "今朝の新聞（　　）よると、ガソリン価格が来月から再び値上がりするそうだ。",
                    "According to this morning's newspaper, gasoline prices will reportedly hike again starting next month.",
                    ["に", "で", "を", "へ"],
                    0,
                    [
                        "Correct! Noun + によると is the fixed citation pattern.",
                        "Incorrect. でよると does not exist.",
                        "Incorrect. をよると is ungrammatical.",
                        "Incorrect. へよると is invalid."
                    ],
                    "Noun + によると (Citing sources)",
                    "Reporting economic news from a morning daily."
                )
            ],
            "tags": ["N3", "SKM Unit 10", "Hearsay", "Source Citation"]
        },
        {
            "id": "skm3-u10-rashii",
            "title": "〜らしい (Evidential Hearsay vs Typical Archetype)",
            "meaning": "Two primary senses: (1) Hearsay/conjecture based on external reports ('apparently'); (2) Exemplifying the quintessence of a quality ('truly typical of / behaving like a real...').",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 10: 伝聞・推量 (Hearsay & Conjecture)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Sense 1 (Conjecture): 普通形 (Noun / な-adj bare) + らしい | Sense 2 (Typicality): Noun + らしい",
            "nuance": "ARCHETYPE NUANCE: 男らしい (manly), 男子学生らしい (behaving like a true student), 春らしい (truly spring-like). Unlike っぽい (which implies shallow resemblance), らしい embodies genuine true essence.",
            "keyTakeaway": "MUG-UP: Noun + らしい = 'Embodying the true quintessence of X!'. (春らしい日 = A truly spring-like day).",
            "sentences": [
                make_sentence(
                    "s-skm3-10-2",
                    "桜が咲いてポカポカ暖かくなり、ようやく春らしい季節になった。",
                    "With cherry blossoms blooming and pleasantly warm weather, it has finally become a truly spring-like season.",
                    "Cherry-blossoms bloomed pleasantly warm became, at-last spring-like season became.",
                    [
                        tok("春らしい", "はるらしい", "harurashii", "truly spring-like", "Grammar")
                    ],
                    "Embodying the ideal aesthetic qualities of springtime."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-10-2",
                    "負けて悔しいのは分かるが、プロの選手（　　）最後まで堂々と振る舞うべきだ。",
                    "I understand you are frustrated by the loss, but as a professional athlete you ought to carry yourself with dignity until the end.",
                    ["らしく", "そうに", "みたいで", "がちに"],
                    0,
                    [
                        "Correct! 選手らしく means 'in a manner befitting a true athlete'.",
                        "Incorrect. 選手そうに is ungrammatical.",
                        "Incorrect. 選手みたいで implies superficial resemblance rather than true professional conduct.",
                        "Incorrect. 選手がちに is meaningless."
                    ],
                    "Noun + らしく (Archetypical conduct)",
                    "Demanding professional sportsmanship."
                )
            ],
            "tags": ["N3", "SKM Unit 10", "Conjecture", "Archetype"]
        },

        # === UNIT 11: 意志・計画 (INTENT & REGULATIONS) ===
        {
            "id": "skm3-u11-koto-ni-shite-iru",
            "title": "〜ことにしている (Habitual Personal Rule / Self-Imposed Policy)",
            "meaning": "Indicates a conscious, self-imposed rule or habitual code of conduct that the speaker upholds consistently.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 11: 意志・計画 (Intent & Regulations)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 / V-ない形 + ことにしている",
            "nuance": "PERSONAL RESOLUTION vs EXTERNAL RULE: ことにしている is the speaker's own active personal policy. In contrast, ことになっている denotes external rules, schedules, or societal laws.",
            "keyTakeaway": "MUG-UP: V-る / V-ない + ことにしている = 'My own personal rule/policy!'.",
            "sentences": [
                make_sentence(
                    "s-skm3-11-3",
                    "どんなに忙しくても、毎日必ず30分は読書をすることにしている。",
                    "No matter how busy I am, I make it a strict personal rule to read for at least 30 minutes every day.",
                    "How-much busy even-if, every-day definitely 30-minutes reading do-rule-have.",
                    [
                        tok("読書をすることにしている", "どくしょをすることにしている", "dokusho o suru koto ni shite iru", "make it a rule to read", "Grammar")
                    ],
                    "Disciplined intellectual daily habit."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-11-3",
                    "環境を守るため、買い物にはマイバッグを持参する（　　）にしている。",
                    "To protect the environment, I make it a policy to bring my own shopping bag when buying goods.",
                    ["こと", "もの", "わけ", "ところ"],
                    0,
                    [
                        "Correct! 持参することにしている expresses an intentional self-directed eco-friendly habit.",
                        "Incorrect. ものにしている does not express personal rules.",
                        "Incorrect. わけにしている is ungrammatical.",
                        "Incorrect. ところにしている is invalid."
                    ],
                    "V-る + ことにしている (Personal code)",
                    "Self-directed eco-conscious shopping habit."
                )
            ],
            "tags": ["N3", "SKM Unit 11", "Habit", "Personal Policy"]
        },
        {
            "id": "skm3-u11-tsumori-da",
            "title": "〜つもり (Believing / Acting as If / Contrary to Reality)",
            "meaning": "Expresses that the subject acts with the internal belief or mental mindset of X, regardless of whether external reality or others agree.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 11: 意志・計画 (Intent & Regulations)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-た形 / Noun + の / い-adj / な-adj + な + つもり (Noun modifier)",
            "nuance": "CONVICTION VS REALITY: Can convey a subjective illusion: '自分では若いつもりだが、階段で息が切れる' (I feel young in my own mind, but I get out of breath on stairs). Or reproaching someone: '冗談のつもりだった' (I intended it as a joke).",
            "keyTakeaway": "MUG-UP: V-た / Nounの + つもり = 'In my mind / Believing that I had done so (even if reality differs)'.",
            "sentences": [
                make_sentence(
                    "s-skm3-11-4",
                    "鍵を閉めたつもりだったが、帰宅したらドアが開いていてぞっとした。",
                    "I was under the firm impression that I had locked the door, but returning home I was terrified to find it wide open.",
                    "Key locked impression-had, home-returned door open-being horrified.",
                    [
                        tok("閉めたつもりだった", "しめたつもりだった", "shimeta tsumori datta", "believed I had locked", "Grammar")
                    ],
                    "Chilling discovery of a mistaken assumption."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-11-4",
                    "自分では上手に説明した（　　）だったが、誰にも理解してもらえなかった。",
                    "In my own mind I believed I had explained it clearly, but nobody understood me.",
                    ["つもり", "はず", "わけ", "ところ"],
                    0,
                    [
                        "Correct! 説明したつもりだった reflects internal conviction contradicted by the listeners' bewilderment.",
                        "Incorrect. はずだった means 'was supposed to' (expectation that failed to happen).",
                        "Incorrect. わけだった does not express subjective misconception.",
                        "Incorrect. ところだった means 'was on the verge of'."
                    ],
                    "V-た + つもり (Mistaken subjective impression)",
                    "Discrepancy between speaker's intention and listener's comprehension."
                )
            ],
            "tags": ["N3", "SKM Unit 11", "Mental State", "Subjective Illusion"]
        },

        # === UNIT 12: 敬語・待遇表現 (POLITENESS & RESPECT) ===
        {
            "id": "skm3-u12-keigo-respect",
            "title": "お〜になる / ご〜になる (Honorific Respect - Elevating Others' Actions)",
            "meaning": "Transforms a regular verb into a respectful honorific (尊敬語) to elevate the actions of an esteemed superior, client, or guest.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 12: 敬語・待遇表現 (Politeness & Respect)",
            "streamId": "stream-social",
            "streamName": "Social Coordinates, Deference & Humility",
            "connection": "お + V-stem + になる (wago) | ご + Noun (suru-verb) + になる / なさる (kango)",
            "nuance": "ELEVATING THE OUTGROUP / SUPERIOR: Used only for the actions of others, NEVER for yourself or your in-group family/company members: '社長はもうお帰りになりました' (The president has already departed).",
            "keyTakeaway": "MUG-UP: お + Verb-stem + になる = Elevates others! NEVER use for yourself.",
            "sentences": [
                make_sentence(
                    "s-skm3-12-1",
                    "部長は今朝のニュースをすでにお読みになりましたか。",
                    "Department manager, have you already read this morning's news?",
                    "Department-manager morning news already honorably-read became-question?",
                    [
                        tok("お読みになりましたか", "およみになりましたか", "oyomi ni narimashita ka", "did you honorably read?", "Grammar")
                    ],
                    "Deferential query directed upward toward department head."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-12-1",
                    "先生、こちらの新しい資料をもうご（　　）になりましたか。",
                    "Professor, have you already reviewed this new reference material?",
                    ["覧", "見", "拝見", "見せ"],
                    0,
                    [
                        "Correct! ご覧になる is the honorific form of 見る ('to look/review').",
                        "Incorrect. ご見になる is ungrammatical.",
                        "Incorrect. 拝見 is humble (謙譲語), which you can only say about your own viewing.",
                        "Incorrect. ご見せになる is invalid."
                    ],
                    "ご覧になる (Honorific vision)",
                    "Inquiring politely about a professor's review."
                )
            ],
            "tags": ["N3", "SKM Unit 12", "Keigo", "Respectful Form"]
        },
        {
            "id": "skm3-u12-keigo-humble",
            "title": "お〜する / ご〜する (Humble Deference - Lowering One's Own Actions)",
            "meaning": "Transforms an action performed by the speaker into a humble deferential (謙譲語), lowering oneself to demonstrate respect to the recipient.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "Unit 12: 敬語・待遇表現 (Politeness & Respect)",
            "streamId": "stream-social",
            "streamName": "Social Coordinates, Deference & Humility",
            "connection": "お + V-stem + する / いたす | ご + Noun (suru-verb) + する / いたす",
            "nuance": "LOWERING THE IN-GROUP: Action must direct toward an esteemed person: '重そうなお荷物をお持ちしましょうか' (Shall I hold your heavy luggage?). You CANNOT use it for independent solo actions like '一人でお昼ご飯をお食べする' ❌.",
            "keyTakeaway": "MUG-UP: お + Verb-stem + する = Humbles my own action towards YOU! Never use for solo actions.",
            "sentences": [
                make_sentence(
                    "s-skm3-12-2",
                    "明日の午後に、こちらから改めてお電話いたします。",
                    "I will personally telephone you once again tomorrow afternoon.",
                    "Tomorrow afternoon, from-here again humble-phone will-do.",
                    [
                        tok("お電話いたします", "おでんわいたします", "odenwa itashimasu", "will humbly call you", "Grammar")
                    ],
                    "Polite corporate commitment to follow up by phone."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-12-2",
                    "駅でお待ちしておりますので、到着されましたら（　　）ください。",
                    "I will be waiting for you at the station, so please contact me once you arrive.",
                    ["ご連絡", "お連絡", "ご報告され", "お伝え"],
                    0,
                    [
                        "Correct! ご連絡ください (kango ご + 連絡) is the polite honorific request to a client/guest.",
                        "Incorrect. お連絡 is unidiomatic (kango takes ご).",
                        "Incorrect. ご報告されください is ungrammatical.",
                        "Incorrect. お伝えください means 'please convey this to someone else'."
                    ],
                    "ご + Kango + ください (Polite client request)",
                    "Inviting arrival confirmation."
                )
            ],
            "tags": ["N3", "SKM Unit 12", "Keigo", "Humble Deferential"]
        },

        # === 形式整理: FORM CLASSIFICATIONS ===
        {
            "id": "skm3-fc-tokoro-datta",
            "title": "〜ところだった (Was on the Very Verge Of / Narrowly Escaped)",
            "meaning": "Indicates that an undesirable disaster or drastic event almost occurred, but was averted in the nick of time: 'I almost / was on the verge of...'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "形式整理 C: ところの形式 (Form C: Tokoro)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 + ところだった (often paired with もう少しで, 危うく)",
            "nuance": "NARROW ESCAPE: Almost always paired with adverbs like もう少しで (by a hair's breadth) or 危うく (narrowly): 'もう少しで終電に乗り遅れるところだった' (I almost missed the last train).",
            "keyTakeaway": "MUG-UP: もう少しで + V-る + ところだった = 'Narrow escape! Almost happened but thank goodness it didn't!'.",
            "sentences": [
                make_sentence(
                    "s-skm3-c-1",
                    "足元が滑って、危うく階段から転がり落ちるところだった。",
                    "My footing slipped, and I came within a hair's breadth of tumbling down the stairs.",
                    "Footing slipped, narrowly stairs-from tumble-down verge-was.",
                    [
                        tok("転がり落ちるところだった", "ころがりおちるところだった", "korogariochiru tokoro datta", "was on the verge of tumbling down", "Grammar")
                    ],
                    "Heart-stopping near-miss on a steep staircase."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-c-1",
                    "友達が声をかけてくれなかったら、大事な約束を（　　）ところだった。",
                    "If my friend hadn't called out to remind me, I would have completely forgotten my important appointment.",
                    ["忘れる", "忘れた", "忘れて", "忘れない"],
                    0,
                    [
                        "Correct! 辞書形 忘れる + ところだった expresses an action that was narrowly averted.",
                        "Incorrect. 忘れたところだった is invalid.",
                        "Incorrect. 忘れてところだった is ungrammatical.",
                        "Incorrect. 忘れないところだった conveys the opposite meaning."
                    ],
                    "V-る + ところだった (Averted outcome)",
                    "Saved from an embarrassing oversight by a friend's reminder."
                )
            ],
            "tags": ["N3", "SKM Form C", "Tokoro", "Narrow Escape"]
        },
        {
            "id": "skm3-fj-kimi",
            "title": "〜気味 (Slight Negative Tinge / Feeling Somewhat...)",
            "meaning": "Indicates a subtle, mild onset of an undesirable physical, mental, or situational condition: 'a touch of / feeling slightly...'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "形式整理 J: 意味を広げる形式 (Suffixes & Tendencies)",
            "streamId": "stream-trends",
            "streamName": "Momentum, Shifts & Inevitable Drift",
            "connection": "V-stem + 気味 (ぎみ) | Noun + 気味 (風邪気味, 疲れ気味, 太り気味, 遅れ気味)",
            "nuance": "SLIGHT ONSET: Describes a nascent phase, not fully-blown illness or disaster: 風邪気味 (a slight touch of a cold), 緊張気味 (a bit nervous).",
            "keyTakeaway": "MUG-UP: Stem / Noun + 気味 (ぎみ) = 'A slight touch / mild symptom of negative state'.",
            "sentences": [
                make_sentence(
                    "s-skm3-j-3",
                    "最近残業続きで疲れ気味なので、今週末は家でゆっくり休みたい。",
                    "Because I've been feeling somewhat worn out from consecutive overtime lately, I want to rest peacefully at home this weekend.",
                    "Recently overtime-continuation-due-to fatigue-touch-being, this-weekend home peacefully want-to-rest.",
                    [
                        tok("疲れ気味", "つかれぎみ", "tsukaregimi", "touch of fatigue", "Grammar")
                    ],
                    "Mild exhaustion prompting weekend recuperation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-j-3",
                    "朝から喉が痛くて少し（　　）気味なので、早めに薬を飲んで寝ます。",
                    "My throat has been hurting since morning and I have a touch of a cold, so I will take medicine early and go to sleep.",
                    ["風邪", "病気", "熱", "痛い"],
                    0,
                    [
                        "Correct! 風邪気味 (かぜぎみ) is the classic idiom for having a mild touch of a cold.",
                        "Incorrect. 病気気味 is not standard Japanese.",
                        "Incorrect. 熱気味 is unnatural (one says 微熱がある).",
                        "Incorrect. 痛い気味 is ungrammatical (adjectives do not attach directly to 気味)."
                    ],
                    "Noun + 気味 (Nascent symptom)",
                    "Taking precautionary measures against an impending cold."
                )
            ],
            "tags": ["N3", "SKM Form J", "Suffix", "Mild Symptom"]
        },
        {
            "id": "skm3-fj-gachi",
            "title": "〜がち (Prone To / Habitual Unfortunate Tendency)",
            "meaning": "Indicates a recurring, unwanted tendency to happen frequently or slip into an undesirable state: 'tending to / prone to / easily falling into...'.",
            "level": "N3",
            "book": "Shin Kanzen Master N3",
            "chapter": "形式整理 J: 意味を広げる形式 (Suffixes & Tendencies)",
            "streamId": "stream-trends",
            "streamName": "Momentum, Shifts & Inevitable Drift",
            "connection": "V-stem + がち | Noun + がち (留守がち, 曇りがち, 遠慮がち, 忘れがち)",
            "nuance": "UNFAVORABLE FREQUENCY: Describes a recurring frequency of an undesirable pattern (unlike 気味, which denotes a mild physical symptom). Example: '一人暮らしの人は野菜不足になりがちだ' (People living alone tend to become deficient in vegetables).",
            "keyTakeaway": "MUG-UP: Verb-stem / Noun + がち = 'Prone to slipping into this bad habit/condition!'.",
            "sentences": [
                make_sentence(
                    "s-skm3-j-4",
                    "スマートフォンに夢中になると、ついつい夜更かしをしがちだ。",
                    "When absorbed in one's smartphone, one is terribly prone to inadvertently staying up late.",
                    "Smartphone absorbed become, inadvertently staying-up-late prone-to-do.",
                    [
                        tok("しがちだ", "しがちだ", "shigachi da", "prone to doing", "Grammar")
                    ],
                    "Common behavioral vulnerability in modern life."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm3-j-4",
                    "冬になると寒さのせいで家に閉じこもり（　　）になり、運動不足が心配だ。",
                    "In winter, due to the cold, I tend to stay cooped up indoors, and I worry about lack of exercise.",
                    ["がち", "気味", "っぽい", "だらけ"],
                    0,
                    [
                        "Correct! 閉じこもりがち captures the recurrent seasonal tendency to stay cooped up inside.",
                        "Incorrect. 閉じこもり気味 is less natural for habitual behavior.",
                        "Incorrect. 閉じこもりっぽい is unidiomatic.",
                        "Incorrect. 閉じこもりだらけ is meaningless."
                    ],
                    "V-stem + がち (Frequent behavioral tendency)",
                    "Seasonal sedentary lifestyle concerns."
                )
            ],
            "tags": ["N3", "SKM Form J", "Suffix", "Tendency"]
        }
    ]

