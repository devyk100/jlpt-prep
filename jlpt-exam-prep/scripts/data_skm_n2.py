# -*- coding: utf-8 -*-
"""
Shin Kanzen Master N2 Bunpou - Complete Canonical Syllabus (Chapters 1 to 26)
Fully annotated with lexical tokens, literal glosses, nuance notes, and 4-way quiz explanations.
"""
from data_genki1 import tok, make_sentence, make_quiz

def get_skm_n2_points():
    pts = [
        # Ch 1: 〜際（に）
        {
            "id": "gp-skm2-sai-ni",
            "title": "〜際（に） (Formal Occasion: At the Time of / When)",
            "meaning": "Formal equivalent of とき (when), used in business, announcements, and manuals: 'On the occasion of / When doing X'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 1: とき (Time & Occasions)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 / V-た + 際（に） | Noun + の + 際（に）",
            "nuance": "REGISTER WARNING: Too formal for everyday casual speech. Reserved for notices, legal terms, and courteous announcements.",
            "keyTakeaway": "MUG-UP: 際（に） = Formal business とき. Frequently found in public warnings: 非常の際は.",
            "sentences": [
                make_sentence(
                    "s-skm2-1-1",
                    "パスポートを更新する際には、戸籍謄本と写真が必要になります。",
                    "When renewing your passport, a certified family register transcript and a photograph are required.",
                    "Passport renew occasion-at, family-register transcript and photo necessary become.",
                    [
                        tok("更新する際には", "こうしんするさいには", "koushin suru sai ni wa", "at the time of renewing", "Grammar")
                    ],
                    "Formal procedural guideline."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-1-1",
                    "エレベーターをご利用の（　　）は、足元に十分ご注意ください。",
                    "When using the elevator, please pay careful attention to your step.",
                    ["際", "度", "上", "末"],
                    0,
                    [
                        "Correct! ご利用の際（は） is formal polite public announcement register.",
                        "Incorrect. ご利用の度は ungrammatical.",
                        "Incorrect. ご利用の上は means 'after having used / upon using'.",
                        "Incorrect. ご利用の末 is ungrammatical."
                    ],
                    "Noun + の + 際 (Formal occasion)",
                    "Polite elevator caution announcement."
                )
            ],
            "tags": ["N2", "SKM Ch 1", "Formal", "Time"]
        },

        # Ch 1: 〜たとたん（に）
        {
            "id": "gp-skm2-totan-ni",
            "title": "〜たとたん（に） (The Instant That / No Sooner Than)",
            "meaning": "The moment action A occurs, an unexpected, instantaneous event B takes place ('The instant I opened the door, the cat bolted out').",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 1: とき (Time & Occasions)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-た + とたん（に）",
            "nuance": "NO SPEAKER WILL IN B: Clause B CANNOT be the speaker's deliberate command, request, or conscious intention!",
            "keyTakeaway": "MUG-UP: V-た + とたん(に). Clause B is ALWAYS an unexpected accident or automatic surprise!",
            "sentences": [
                make_sentence(
                    "s-skm2-1-2",
                    "一口食べた途端に、強烈な辛さが口いっぱいに広がった。",
                    "The instant I took a single bite, intense spiciness spread all throughout my mouth.",
                    "One-bite ate instant-at, intense spiciness mouth-full spread.",
                    [
                        tok("食べた途端に", "たべたとたんに", "tabeta totan ni", "the instant I took a bite", "Grammar")
                    ],
                    "Instant reflexive sensation triggered by taking a bite."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-1-2",
                    "窓を開けた（　　）、突風が吹き込んできて書類が散らばった。",
                    "The instant I opened the window, a gust of wind blew in and scattered my documents.",
                    ["とたんに", "うちに", "ついでに", "かわりに"],
                    0,
                    [
                        "Correct! 開けたとたんに marks the instantaneous surprise trigger of the wind gust.",
                        "Incorrect. 開けたうちに is ungrammatical.",
                        "Incorrect. ついでに implies taking advantage of an errand to perform another conscious task.",
                        "Incorrect. かわりに means 'instead of'."
                    ],
                    "V-た + とたんに instant trigger",
                    "Uncontrolled physical accident happening immediately upon opening."
                )
            ],
            "tags": ["N2", "SKM Ch 1", "Instant", "Accident"]
        },

        # Ch 2: 〜つつある
        {
            "id": "gp-skm2-tsutsu-aru",
            "title": "〜つつある (Ongoing Dynamic Shift: In the Process Of)",
            "meaning": "An ongoing gradual change or continuous trend is actively unfolding right now ('Is steadily undergoing transition').",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 2: している (Progress & Shifts)",
            "streamId": "stream-trends",
            "streamName": "Trends, Changes & Proportional Evolution",
            "connection": "V-stem (ます形 without ます) + つつある",
            "nuance": "CHANGE VERBS ONLY: Connects almost exclusively to verbs of change, evolution, recovery, or decline.",
            "keyTakeaway": "MUG-UP: V-stem + つつある = Formal written trend in progress ('is in the process of changing').",
            "sentences": [
                make_sentence(
                    "s-skm2-2-1",
                    "景気はどん底を脱し、各種経済指標も緩やかに回復しつつあります。",
                    "The economy has escaped its rock bottom, and various economic indicators are gradually in the process of recovering.",
                    "Economy bottom escaped, various indicators-also gently recovering-process-in are.",
                    [
                        tok("回復しつつあります", "かいふくしつつあります", "kaifuku shitsutsu arimasu", "is in the process of recovering", "Grammar")
                    ],
                    "Formal written economic reporting of gradual upward trend."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-2-1",
                    "伝統的な職人技を受け継ぐ若者が減り、古くからの技術が失われ（　　）。",
                    "Young people inheriting traditional artisanal skills are dwindling, and ancient techniques are in the process of being lost.",
                    ["つつある", "きっている", "おわっている", "だしている"],
                    0,
                    [
                        "Correct! 失われ (stem of passive 失われる) + つつある depicts a gradual ongoing loss.",
                        "Incorrect. きっている implies fully completed to exhaustion.",
                        "Incorrect. おわっている means already finished.",
                        "Incorrect. だしている indicates sudden outburst of spontaneous action."
                    ],
                    "V-stem + つつある gradual shift",
                    "Depicting a continuous ongoing socio-cultural decline."
                )
            ],
            "tags": ["N2", "SKM Ch 2", "Trends", "Evolution"]
        },

        # Ch 3: 〜てはじめて
        {
            "id": "gp-skm2-te-hajimete",
            "title": "〜てはじめて (Only After Experiencing X Did Y Dawn)",
            "meaning": "Only after experiencing X or being placed in situation X did the speaker truly realize, appreciate, or become able to do Y.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 3: あとで (Aftermath & Epiphany)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-て + はじめて",
            "nuance": "PSYCHOLOGICAL EPIPHANY: Clause B describes a newfound appreciation or realization that was previously taken for granted.",
            "keyTakeaway": "MUG-UP: V-て + はじめて = 'Not until / Only after doing X did I realize Y!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-3-1",
                    "重い病気を患ってはじめて、健康で暮らせることのありがたさを痛感した。",
                    "Only after suffering a severe illness did I acutely realize how precious it is to live in good health.",
                    "Severe illness suffered-after, health-with live preciousness acutely-felt.",
                    [
                        tok("患ってはじめて", "わずらってはじめて", "wazuratte hajimete", "only after suffering", "Grammar")
                    ],
                    "Profound epiphany triggered only after experiencing adversity."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-3-1",
                    "親元を離れて一人暮らしをし（　　）はじめて、親の苦労が身にしみて分かった。",
                    "Only after moving away from my parents and living alone did I truly grasp my parents' struggles.",
                    ["て", "た", "る", "ない"],
                    0,
                    [
                        "Correct! して (te-form of する) + はじめて expresses realization after experience.",
                        "Incorrect. Past た cannot connect to はじめて in this grammar.",
                        "Incorrect. Dictionary form cannot connect to はじめて.",
                        "Incorrect. Negative ない cannot connect here."
                    ],
                    "V-て + はじめて realization",
                    "Realization triggered after living independently."
                )
            ],
            "tags": ["N2", "SKM Ch 3", "Epiphany", "Realization"]
        },

        # Ch 3: 〜上（で）
        {
            "id": "gp-skm2-ue-de",
            "title": "〜上（で） (Upon Doing X First / In Terms Of)",
            "meaning": "1) After completing step A as a necessary preparatory foundation, proceeding to execute step B ('Only upon reviewing the contract will I decide'). 2) In the domain of / In terms of ('曆の上では').",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 3: あとで (Aftermath & Epiphany)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-た + 上で (After doing) | Noun + の + 上で | V-辞書形 + 上で (In doing)",
            "nuance": "CONSCIOUS DELIBERATION: Clause A is a deliberate prerequisite (thinking, reading, consulting) undertaken before making a formal judgment or decision.",
            "keyTakeaway": "MUG-UP: V-た + 上で = 'After doing A first, then B'. Noun + の上で.",
            "sentences": [
                make_sentence(
                    "s-skm2-3-2",
                    "家族とよく話し合った上で、留学するかどうか最終決定を下します。",
                    "Only after thoroughly discussing with my family will I make the final decision on whether to study abroad.",
                    "Family-with well discussed upon, study-abroad whether final-decision make.",
                    [
                        tok("話し合った上で", "はなしあったうえで", "hanashiatta ue de", "upon discussing thoroughly", "Grammar")
                    ],
                    "Thorough prerequisite discussion before rendering decision."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-3-2",
                    "実物をご確認いただいた（　　）で、ご購入を決めていただけます。",
                    "You may decide on your purchase only upon checking the actual item in person.",
                    ["上", "末", "間", "際"],
                    0,
                    [
                        "Correct! いただいた上で expresses proceeding to purchase only after physically inspecting.",
                        "Incorrect. いただいた末 means after long struggle/friction.",
                        "Incorrect. いただいた間 means during.",
                        "Incorrect. いただいた際 means at the time of."
                    ],
                    "V-た + 上で prerequisite",
                    "Careful inspection before business transaction."
                )
            ],
            "tags": ["N2", "SKM Ch 3", "Sequence", "Prerequisite"]
        },

        # Ch 3: 〜次第
        {
            "id": "gp-skm2-shidai",
            "title": "〜次第 (As Soon As / Immediate Sequential Execution)",
            "meaning": "Formal business expression: As soon as event A finishes, immediately execute action B without any delay ('As soon as the results arrive, I will notify you').",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 3: あとで (Aftermath & Epiphany)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-stem (ます形 without ます) + 次第",
            "nuance": "IMMEDIATE BUSINESS PROMISE: Clause B is ALWAYS the speaker's conscious promise, request, or intention (すぐ〜します, ご連絡ください).",
            "keyTakeaway": "MUG-UP: V-stem + 次第 = Formal 'As soon as X is done, I will do Y!'. Connects to masu-stem.",
            "sentences": [
                make_sentence(
                    "s-skm2-3-3",
                    "詳しい日程が決まり次第、メールにてご連絡申し上げます。",
                    "As soon as the detailed schedule is finalized, I will humbly contact you via email.",
                    "Detailed schedule decide-as-soon-as, email via humble-contact.",
                    [
                        tok("決まり次第", "きまりしだい", "kimari shidai", "as soon as it is decided", "Grammar")
                    ],
                    "Polite corporate promise of prompt communication."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-3-3",
                    "成田空港に到着（　　）、すぐに家族へ無事の電話を入れたいと思います。",
                    "As soon as I arrive at Narita Airport, I would like to call my family immediately to let them know I arrived safely.",
                    ["し次第", "した次第", "する次第", "して次第"],
                    0,
                    [
                        "Correct! 到着する stem is 到着し + 次第 (到着し次第).",
                        "Incorrect. 到着した次第 is ungrammatical before a future intentional verb.",
                        "Incorrect. Dictionary form cannot connect to 次第 for 'as soon as'.",
                        "Incorrect. Te-form cannot connect to 次第."
                    ],
                    "V-stem + 次第 prompt sequence",
                    "Immediate phone call following international arrival."
                )
            ],
            "tags": ["N2", "SKM Ch 3", "Promptness", "Business"]
        },

        # Ch 5: 〜に限って
        {
            "id": "gp-skm2-ni-kagitte",
            "title": "〜に限って (Perverse Timing / Murphy's Law / Unwavering Trust)",
            "meaning": "1) Murphy's law: Of all times/days, it perversely happens on this specific day! 2) Unwavering faith: 'Of all people, that person would NEVER do such a thing'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 5: だけ (Limits & Exceptions)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "Noun + に限って",
            "nuance": "MURPHY'S LAW VS TRUST: Irony or unshakable defense.",
            "keyTakeaway": "MUG-UP: に限って = 'Of all days / Of all people!'. Irony or unshakable defense.",
            "sentences": [
                make_sentence(
                    "s-skm2-5-1",
                    "滅多に遅刻しない彼に限って、こんな大事な契約の日に限って寝坊するなんて。",
                    "Of all people, he who rarely arrives late—and of all days, on the day of such an important contract—to oversleep!",
                    "Rarely late-not him of-all-people, important contract day of-all-days oversleeping shocking.",
                    [
                        tok("彼に限って", "かれにかぎって", "kare ni kagitte", "he of all people", "Grammar"),
                        tok("日に限って", "ひにかぎって", "hi ni kagitte", "of all days", "Grammar")
                    ],
                    "Double irony of person and timing."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-5-1",
                    "忙しくて時間が全くない時に（　　）、面倒なトラブルが次々と舞い込んでくる。",
                    "Of all times, precisely when I am busy and have no time at all, troublesome issues come pouring in one after another.",
                    ["限って", "沿って", "おいて", "即して"],
                    0,
                    [
                        "Correct! 時に限って captures Murphy's law: trouble arrives precisely at the worst possible time.",
                        "Incorrect. 時に沿って is nonsensical.",
                        "Incorrect. 時において means 'at the time of', neutral without irony.",
                        "Incorrect. 時に即して means adapting strictly to standards."
                    ],
                    "Noun + に限って Murphy's law timing",
                    "Perverse adverse timing of troubles."
                )
            ],
            "tags": ["N2", "SKM Ch 5", "Irony", "Timing"]
        },

        # Ch 5: 〜のみならず
        {
            "id": "gp-skm2-nominarazu",
            "title": "〜のみならず (Formal Addition: Not Only X, But Also Y)",
            "meaning": "Formal written and rhetorical equivalent of だけでなく: 'Not only A, but what is more, B as well'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 5: だけ (Limits & Exceptions)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "Plain form + のみならず | Noun + のみならず (Noun connects directly without である!)",
            "nuance": "WRITTEN / ORATORICAL GRAVITAS: Often used in essays, journalistic reporting, and speeches to highlight an expanding scope of impact.",
            "keyTakeaway": "MUG-UP: のみならず = Formal written だけでなく. Nouns connect directly (日本のみならず).",
            "sentences": [
                make_sentence(
                    "s-skm2-5-2",
                    "地球温暖化は日本国内のみならず、世界各国の生態系に深刻な打撃を与えている。",
                    "Global warming is delivering severe blows not only within Japan, but also to ecosystems in nations across the entire world.",
                    "Global-warming Japan inside not-only, world each-country ecosystem severe blow giving.",
                    [
                        tok("日本国内のみならず", "にほんこくないのみならず", "nihon kokunai nominarazu", "not only within Japan, but also", "Grammar")
                    ],
                    "Expanding geographic scope of environmental degradation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-5-2",
                    "このアニメは子供（　　）ならず、大人の世代の間でも絶大な人気を誇っている。",
                    "This anime boasts tremendous popularity not only among children, but also among the adult generation.",
                    ["のみ", "ばかり", "きり", "だけ"],
                    0,
                    [
                        "Correct! のみならず forms the canonical formal additive expression.",
                        "Incorrect. ばかりならず is archaic and unidiomatic in modern standard JLPT.",
                        "Incorrect. きりならず does not exist.",
                        "Incorrect. だけならず is ungrammatical (must be だけでなく)."
                    ],
                    "Noun + のみならず formal addition",
                    "Cross-generational popularity of anime."
                )
            ],
            "tags": ["N2", "SKM Ch 5", "Addition", "Formal"]
        },

        # Ch 8: 〜に沿って
        {
            "id": "gp-skm2-ni-sotte",
            "title": "〜に沿って / 〜に沿った (Conforming Strictly to Rules, Plans, or Lines)",
            "meaning": "Following along a physical route (river, coastline) or strictly adhering to an abstract policy, rule, manual, or expectation without deviation.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 8: を基準にして (Criteria & Adherence)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + に沿って (Adverbial) | Noun + に沿った + Noun (Attributive)",
            "nuance": "CONFORMITY: Moving along a pre-existing path or blueprint.",
            "keyTakeaway": "MUG-UP: Noun + に沿って = Along the line / In compliance with the guidelines! Modifying a noun: に沿った + Noun.",
            "sentences": [
                make_sentence(
                    "s-skm2-8-1",
                    "政府が策定した基本方針に沿って、各地方自治体は具体的な防災計画を策定した。",
                    "In strict alignment with the basic policy drafted by the national government, each local municipality formulated a concrete disaster prevention plan.",
                    "Government drafted basic-policy conforming-to, each local-municipality disaster-plan formulated.",
                    [
                        tok("基本方針に沿って", "きほんほうしんにそって", "kihon houshin ni sotte", "conforming to the basic policy", "Grammar")
                    ],
                    "Administrative compliance with government directives."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-8-1",
                    "お客様のご要望に（　　）プランをご提案させていただきます。",
                    "We would like to propose a customized plan in strict alignment with your requests.",
                    ["沿った", "対した", "向けた", "即した"],
                    0,
                    [
                        "Correct! ご要望に沿ったプラン describes a proposal customized strictly to match the client's guidelines.",
                        "Incorrect. ご要望に対した is ungrammatical.",
                        "Incorrect. ご要望に向けた is unidiomatic here.",
                        "Incorrect. 即した requires realistic conditions."
                    ],
                    "Noun + に沿った + Noun",
                    "Aligning a business plan with customer specifications."
                )
            ],
            "tags": ["N2", "SKM Ch 8", "Criteria", "Compliance"]
        },

        # Ch 11: 〜を問わず
        {
            "id": "gp-skm2-wo-towazu",
            "title": "〜を問わず (Irrespective of / Regardless of / Open to All)",
            "meaning": "Condition X makes zero difference and imposes no restriction whatsoever: 'Regardless of age, gender, nationality, or experience'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 11: 関係なく・無視して (Disregard & Inclusivity)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + を問わず (Frequently pairs with opposite extremes: 昼夜を問わず, 年齢・性別を問わず)",
            "nuance": "PUBLIC OPENNESS: Ubiquitous in recruitment advertisements and public facility notices.",
            "keyTakeaway": "MUG-UP: Noun + を問わず = 'Does not question X' (Question = 問う). Pairs with polar opposites.",
            "sentences": [
                make_sentence(
                    "s-skm2-11-1",
                    "このボランティア活動は、国籍や年齢を問わず、どなたでも自由に参加できます。",
                    "This volunteer activity is open to anyone to join freely, regardless of nationality or age.",
                    "This volunteer activity, nationality or age questioning-not, anyone freely participate can.",
                    [
                        tok("年齢を問わず", "ねんれいをとわず", "nenrei o towazu", "regardless of age", "Grammar")
                    ],
                    "Universal invitation eliminating age barriers."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-11-1",
                    "救急病院の集中治療室では、昼夜を（　　）懸命な救命活動が続けられている。",
                    "In the intensive care unit of the emergency hospital, tireless life-saving efforts continue night and day, regardless of the hour.",
                    ["問わず", "限らず", "兼ねず", "応ぜず"],
                    0,
                    [
                        "Correct! 昼夜を問わず is the canonical idiom for 'day and night without interruption / around the clock'.",
                        "Incorrect. 昼夜に限らず is awkward with を.",
                        "Incorrect. 兼ねず means cannot combine.",
                        "Incorrect. 応ぜず means not responding."
                    ],
                    "Noun + を問わず around the clock",
                    "Continuous medical dedication irrespective of day or night."
                )
            ],
            "tags": ["N2", "SKM Ch 11", "Disregard", "Universal"]
        },

        # Ch 12: 〜どころか
        {
            "id": "gp-skm2-dokoroka",
            "title": "〜どころか (Far From It / Anything But / On the Contrary)",
            "meaning": "Strongly refutes condition A and replaces it with an even more extreme or opposite reality B: 'Far from X, the real truth is Y!'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 12: 強く否定する (Strong Negation)",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "Noun / Plain form + どころか",
            "nuance": "STARK POLAR OPPOSITE: Exceeds ordinary negation. Not only did expected thing A fail to occur, but something in the exact opposite direction occurred.",
            "keyTakeaway": "MUG-UP: A どころか B = 'Far from A, actually B!'. Exposes an unexpected gap.",
            "sentences": [
                make_sentence(
                    "s-skm2-12-1",
                    "ボーナスをもらえるどころか、業績悪化で給料を二割もカットされてしまった。",
                    "Far from receiving a bonus, my salary was actually cut by twenty percent due to deteriorating company performance.",
                    "Bonus receive far-from, business-performance decline-by salary 20-percent cut-was.",
                    [
                        tok("もらえるどころか", "もらえるどころか", "moraeru dokoroka", "far from receiving it", "Grammar")
                    ],
                    "Extreme adverse contrast between expected bonus and brutal pay cut."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-12-1",
                    "病気は良くなる（　　）、日を追うごとに悪化する一方だ。",
                    "Far from getting better, the illness is only steadily worsening with each passing day.",
                    ["どころか", "ばかりか", "ものなら", "わけには"],
                    0,
                    [
                        "Correct! 良くなるどころか expresses that rather than improving, condition is deteriorating.",
                        "Incorrect. ばかりか implies additive ('not only improves, but also...'), which makes no sense with worsening.",
                        "Incorrect. ものなら is a hypothetical 'if by miracle'.",
                        "Incorrect. わけには is part of わけにはいかない."
                    ],
                    "Plain verb + どころか polar refutation",
                    "Refuting recovery and affirming deterioration."
                )
            ],
            "tags": ["N2", "SKM Ch 12", "Refutation", "Contrast"]
        },

        # Ch 14: 〜ものの
        {
            "id": "gp-skm2-monono",
            "title": "〜ものの / 〜とはいうものの (Although / Conceding Fact A with But B)",
            "meaning": "Acknowledges and concedes that fact A is undeniably true, but clause B contradicts the normal expectation arising from A ('Although I bought it, I haven't used it once').",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 14: けれど (Concession & Contrast)",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "Plain form + ものの (な-adj takes な/である, Noun takes である: 不便であるものの)",
            "nuance": "WRITTEN CONCESSIVE REGISTER: Highly natural in formal writing and reflective adult speech.",
            "keyTakeaway": "MUG-UP: [Admitted Fact] ものの [Underwhelming Reality]. Noun/な-adj takes であるものの.",
            "sentences": [
                make_sentence(
                    "s-skm2-14-1",
                    "高価な最新のパソコンを購入したものの、使いこなせずに宝の持ち腐れになっている。",
                    "Although I purchased an expensive high-end computer, I haven't been able to master it, and it has become a wasted treasure.",
                    "Expensive latest PC bought although, master-without treasure's waste become-is.",
                    [
                        tok("購入したものの", "こうにゅうしたものの", "kounyuu shita mono no", "although I purchased it", "Grammar")
                    ],
                    "Conceding the purchase, followed by underwhelming usage."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-14-1",
                    "大学の入学試験に合格した（　　）、将来の進路についてまだ不安が残っている。",
                    "Although I passed the university entrance exam, anxieties about my future path still linger.",
                    ["ものの", "ばかりに", "おかげで", "せいで"],
                    0,
                    [
                        "Correct! 合格したものの concedes the success while noting persistent anxiety.",
                        "Incorrect. ばかりに means 'solely because of that, a disaster happened' (negative blame).",
                        "Incorrect. おかげで expresses gratitude for a positive result.",
                        "Incorrect. せいで attributes blame."
                    ],
                    "〜ものの concession",
                    "Conceding success while acknowledging residual worry."
                )
            ],
            "tags": ["N2", "SKM Ch 14", "Concession", "Contrast"]
        },

        # Ch 14: 〜からといって
        {
            "id": "gp-skm2-kara-to-itte",
            "title": "〜からといって (Just Because X, It Doesn't Follow That Y)",
            "meaning": "Rejects the invalid assumption that condition A automatically justifies or guarantees result B ('Just because someone is wealthy, it doesn't mean they are happy').",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 14: けれど (Concession & Contrast)",
            "streamId": "stream-contrasts",
            "streamName": "Contrasts, Concessions & Paradoxes",
            "connection": "Plain form + からといって + Negative Conclusion (〜とは限らない, 〜わけではない)",
            "nuance": "PREVENTS GENERALIZATION: Frequently pairs with partial negations: とは限らない, わけではない, してはいけない.",
            "keyTakeaway": "MUG-UP: [Premise] からといって + [Negative/Warning] = Just because X, that's no excuse for Y!",
            "sentences": [
                make_sentence(
                    "s-skm2-14-2",
                    "日本に何年も住んでいるからといって、誰もが日本語を流暢に話せるわけではない。",
                    "Just because someone has lived in Japan for many years, it does not necessarily follow that everyone can speak Japanese fluently.",
                    "Japan-in many-years living just-because, everyone Japanese fluently speak able reason-is-not.",
                    [
                        tok("住んでいるからといって", "すんでいるからといって", "sunde iru kara to itte", "just because they live there", "Grammar")
                    ],
                    "Debunking the automatic assumption that living abroad equals fluency."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-14-2",
                    "いくら忙しいからと（　　）、挨拶もしないで立ち去るのは失礼だ。",
                    "No matter how busy you are, just because you are in a rush, leaving without greeting is extremely rude.",
                    ["いって", "みて", "して", "なって"],
                    0,
                    [
                        "Correct! からといって rejects being busy as a valid justification for rude behavior.",
                        "Incorrect. からとみて is ungrammatical here.",
                        "Incorrect. からとして is ungrammatical.",
                        "Incorrect. からとなって is nonsensical."
                    ],
                    "〜からといって invalid justification",
                    "Rejecting busyness as an excuse for bad manners."
                )
            ],
            "tags": ["N2", "SKM Ch 14", "Excuse", "Concession"]
        },

        # Ch 17: 〜からには / 〜以上は
        {
            "id": "gp-skm2-kara-niwa",
            "title": "〜からには / 〜以上は (Now That / Since It Has Come to This, Duty Compels)",
            "meaning": "Now that situation X is an established reality or commitment, the speaker feels an absolute moral resolve or duty to follow through with Y.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 17: だから―理由 (Cause & Resolution)",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "Plain form + からには / 以上は (Noun/な-adj takes である: 代表である以上は)",
            "nuance": "NO RETREAT: The bridge behind has been burned. Clause B conveys powerful resolve, duty, or mandate (〜つもりだ, 〜なければならない, 〜べきだ).",
            "keyTakeaway": "MUG-UP: [Established Fact] からには [Firm Determination / Absolute Duty]! Point of no return.",
            "sentences": [
                make_sentence(
                    "s-skm2-17-1",
                    "チームのリーダーを引き受けたからには、最後まで全力を尽くして責任を果たす覚悟です。",
                    "Now that I have accepted the position of team leader, I am fully prepared to do my utmost and fulfill my responsibility until the very end.",
                    "Team leader accepted now-that, last-until all-power exhaust responsibility fulfill resolve-is.",
                    [
                        tok("引き受けたからには", "ひきうけたからには", "hikiuketa kara ni wa", "now that I accepted it", "Grammar")
                    ],
                    "High sense of personal leadership duty."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-17-1",
                    "一度自分でやると約束した（　　）は、途中で投げ出してはいけない。",
                    "Now that you promised to do it yourself, you must not throw in the towel midway.",
                    ["からに", "うえに", "ために", "わりに"],
                    0,
                    [
                        "Correct! 約束したからには (or 以上は) establishes that the promise binds one to finish.",
                        "Incorrect. うえに means 'in addition to / on top of'.",
                        "Incorrect. ために means in order to / due to.",
                        "Incorrect. わりに means unexpectedly considering."
                    ],
                    "V-た + からには firm commitment",
                    "Moral duty to fulfill a voluntary pledge."
                )
            ],
            "tags": ["N2", "SKM Ch 17", "Resolve", "Duty"]
        },

        # Ch 18: 〜がたい
        {
            "id": "gp-skm2-gatai",
            "title": "〜がたい (Psychologically Unfathomable / Hard to Accept or Do)",
            "meaning": "Emotionally or mentally impossible/extremely difficult to do (believe, forgive, understand): 'Virtually impossible for my heart/mind to accept'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 18: 困難・不能 (Inability & Struggle)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "V-stem (ます形 without ます) + がたい",
            "nuance": "PSYCHOLOGICAL NOT PHYSICAL: Pairs almost exclusively with cognitive verbs: 信じる, 許す, 想像する, 理解する.",
            "keyTakeaway": "MUG-UP: V-stem + がたい = Mentally/emotionally unfathomable! Fixed collocations: 信じがたい, 許しがたい, 得がたい.",
            "sentences": [
                make_sentence(
                    "s-skm2-18-1",
                    "長年信頼していた同僚に裏切られたことは、私にとって到底信じがたい事実だった。",
                    "Being betrayed by a colleague I had trusted for years was a fact that was utterly unfathomable for me to believe.",
                    "Many-years trusted colleague-by betrayed fact topic, me-for utterly believe-hard fact was.",
                    [
                        tok("信じがたい事実", "しんじがたいじじつ", "shinjigatai jijitsu", "unfathomable fact / hard to believe", "Grammar")
                    ],
                    "Emotional disbelief in a betrayal."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-18-1",
                    "あの温厚なスミス先生が激怒したなんて、私には想像（　　）光景です。",
                    "That gentle Professor Smith flew into a rage is a scene that is hard for me to even imagine.",
                    ["しがたい", "しかねる", "しようがない", "し得ない"],
                    0,
                    [
                        "Correct! 想像しがたい is the natural collocation for something psychologically unimaginable.",
                        "Incorrect. しかねる is for polite professional refusal (致しかねます).",
                        "Incorrect. しようがない means lacking any physical method/means to execute.",
                        "Incorrect. し得ない means technically/logically impossible in physics/law."
                    ],
                    "Cognitive verb stem + がたい",
                    "Psychologically unfathomable behavior from a calm teacher."
                )
            ],
            "tags": ["N2", "SKM Ch 18", "Psychological Inability", "Difficulty"]
        },

        # Ch 18: 〜かねる
        {
            "id": "gp-skm2-kaneru",
            "title": "〜かねる (Polite Business Refusal: Regretfully Cannot Do)",
            "meaning": "Polite professional formula used by service personnel or business representatives to decline requests: 'I am regretfully in no position to do so'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 18: 困難・不能 (Inability & Struggle)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "V-stem (ます形 without ます) + かねる (Past/Polite: かねます)",
            "nuance": "DIPLOMATIC SOFT REFUSAL: Saying 'できません' is blunt and offensive in Japanese business. Saying 'いたしかねます' or 'お引き受けしかねます' conveys that internal company rules or circumstances prevent compliance.",
            "keyTakeaway": "MUG-UP: V-stem + かねます = The golden polite Japanese business refusal ('I regretfully cannot').",
            "sentences": [
                make_sentence(
                    "s-skm2-18-2",
                    "お客様の個人的なご事情とはいえ、会社の規定により返金には応じかねます。",
                    "Even understanding your personal circumstances, in accordance with company policy we regretfully cannot accommodate a refund.",
                    "Customer personal circumstances although, company rule-by refund accommodate-cannot.",
                    [
                        tok("応じかねます", "おうじかねます", "ouji kanemasu", "regretfully cannot accommodate", "Grammar")
                    ],
                    "Polite corporate boundary setting."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-18-2",
                    "個人情報の保護に関するお問い合わせのため、私の一存ではお答え（　　）。",
                    "Because this inquiry concerns privacy protection, I am in no position to answer on my own personal authority.",
                    ["しかねます", "しがたいです", "しようがありません", "し得ません"],
                    0,
                    [
                        "Correct! お答えしかねます is the courteous, polite business refusal pattern.",
                        "Incorrect. お答えしがたい implies personal emotional resistance, not official company stance.",
                        "Incorrect. お答えしようがありません is colloquial and lacks polite diplomatic polish.",
                        "Incorrect. お答えし得ません is technical logical impossibility."
                    ],
                    "V-stem + かねます polite refusal",
                    "Diplomatic refusal based on privacy regulations."
                )
            ],
            "tags": ["N2", "SKM Ch 18", "Polite Refusal", "Business"]
        },

        # Ch 20: 〜ずじまい（だ）
        {
            "id": "gp-skm2-zujimai",
            "title": "〜ずじまい（だ） (Ended Up Never Doing / Regrettable Inaction)",
            "meaning": "Despite intending or hoping to do X, time or circumstance ran out and one ended up never doing it, leaving a sense of lingering regret.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 20: 結果 (Outcomes & Conclusions)",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "V-ない form without ない + ずじまいだ (する irregular: せずじまいだ)",
            "nuance": "OPPORTUNITY EXPIRED: The window of opportunity has permanently closed.",
            "keyTakeaway": "MUG-UP: V-ず + じまい(だ) = 'Never ended up doing it!'. する becomes せずじまい.",
            "sentences": [
                make_sentence(
                    "s-skm2-20-1",
                    "日本に留学中、富士山に登ろうと計画していたが、結局登らずじまいで帰国してしまった。",
                    "While studying abroad in Japan, I had planned to climb Mt. Fuji, but in the end I returned home without ever having climbed it.",
                    "Japan study-abroad during, Mt-Fuji climb planned but, in-end climb-without-ended returning-ended.",
                    [
                        tok("登らずじまいで", "のぼらずじまいで", "noborazu jimai de", "ended up never climbing it", "Grammar")
                    ],
                    "Lost opportunity during stay in Japan."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-20-1",
                    "せっかく買った名作小説だが、仕事が忙しくて読ま（　　）じまいで本棚に眠っている。",
                    "Despite having gone out of my way to buy this masterpiece novel, I was so busy with work that it ended up unread on my bookshelf.",
                    ["ず", "ない", "ぬ", "ずに"],
                    0,
                    [
                        "Correct! 読む negative stem 読ま + ずじまい forms 読まずじまい ('ended up never reading').",
                        "Incorrect. 読まないじまい is ungrammatical.",
                        "Incorrect. 読まぬじまい is incorrect archaic syntax.",
                        "Incorrect. 読まずにじまい has an extra に."
                    ],
                    "V-ず + じまい lost opportunity",
                    "Book bought with high hopes that ended up unread."
                )
            ],
            "tags": ["N2", "SKM Ch 20", "Regret", "Inaction"]
        },

        # Ch 20: 〜あげく
        {
            "id": "gp-skm2-ageku",
            "title": "〜あげく (After a Long Grueling Ordeal, Bad Outcome Resulted)",
            "meaning": "After enduring a protracted period of deliberation, worry, or struggle A, a disappointing or disastrous conclusion B resulted ('In the end / After all that hassle').",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 20: 結果 (Outcomes & Conclusions)",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "V-た + あげく (に) | Noun + の + あげく (に)",
            "nuance": "NEGATIVE FATIGUE: Clause B is virtually always undesirable, disastrous, or exhausting (e.g., arguing for 3 hours only to break up, wandering around only to find the store closed).",
            "keyTakeaway": "MUG-UP: V-た + あげく = 'After all that prolonged suffering, a BAD result occurred!'. Contrast with 末に (which can be good).",
            "sentences": [
                make_sentence(
                    "s-skm2-20-2",
                    "何時間も激しい口論を続けたあげく、二人は仲直りできずに別れてしまった。",
                    "After arguing fiercely for hours on end, the two failed to reconcile and ended up breaking up.",
                    "Many-hours fierce quarrel continued ordeal-after, two reconcile cannot broke-up.",
                    [
                        tok("続けたあげく", "つづけたあげく", "tsudzuketa ageku", "after continuing for so long, the sad result was", "Grammar")
                    ],
                    "Exhausting ordeal resulting in total breakup."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-20-2",
                    "散々悩んだ（　　）に、誤った選択をしてしまって後悔している。",
                    "After agonizing terribly over it, I ended up making the wrong choice and deeply regret it.",
                    ["あげく", "とたん", "ついで", "あまり"],
                    0,
                    [
                        "Correct! 散々悩んだあげくに expresses prolonged agony culminating in a bad decision.",
                        "Incorrect. とたん marks instantaneous physical surprise, not prolonged agony.",
                        "Incorrect. ついで means taking advantage of a side opportunity.",
                        "Incorrect. あまり requires an emotional noun or direct state without 散々悩んだ."
                    ],
                    "V-た + あげくに bad outcome",
                    "Prolonged agonizing leading to an unfortunate decision."
                )
            ],
            "tags": ["N2", "SKM Ch 20", "Bad Result", "Ordeal"]
        },

        # Ch 21: 〜にほかならない
        {
            "id": "gp-skm2-ni-hokaranaranai",
            "title": "〜にほかならない (Is Nothing Other Than / Purely and Simply)",
            "meaning": "States emphatically that X is the one and only true reason, cause, or identity of something: 'It is none other than X / It is nothing less than X'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 21: 強く言う (Emphatic Assertion)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Noun / Plain form + からにほかならない (Because of nothing other than) | Noun + にほかならない",
            "nuance": "RHETORICAL CONVICTION: The speaker completely sweeps away all alternate explanations, asserting with absolute philosophical certainty that X is the core truth.",
            "keyTakeaway": "MUG-UP: [Reason] からにほかならない = 'It is solely and exclusively because of X!'. Written style.",
            "sentences": [
                make_sentence(
                    "s-skm2-21-1",
                    "今回のプロジェクトが大成功を収めたのは、チーム全員が団結して努力した結果にほかならない。",
                    "That this project achieved great success is nothing other than the result of the entire team uniting and exerting their utmost efforts.",
                    "This-time project great-success achieved fact, team everyone united effort result none-other-than.",
                    [
                        tok("結果にほかならない", "けっかにほかならない", "kekka ni hokaranaranai", "is nothing other than the result", "Grammar")
                    ],
                    "Emphatic credit attributed purely to team synergy."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-21-1",
                    "彼が厳しい言葉をかけたのは、君の成長を心から期待しているからに（　　）。",
                    "That he spoke harsh words to you is because of nothing other than his sincere hope for your personal growth.",
                    ["ほかならない", "違いない", "すぎない", "相違ない"],
                    0,
                    [
                        "Correct! からにほかならない asserts that genuine goodwill was the sole motivation.",
                        "Incorrect. からに違いない is ungrammatical (must be 期待しているに違いない without からに).",
                        "Incorrect. からにすぎない means 'merely because', minimizing rather than strongly justifying.",
                        "Incorrect. からに相違ない is ungrammatical."
                    ],
                    "〜からにほかならない emphatic core reason",
                    "Asserting that tough love was the sole true motive."
                )
            ],
            "tags": ["N2", "SKM Ch 21", "Assertion", "Core Truth"]
        },

        # Ch 25: 〜てたまらない / 〜てならない
        {
            "id": "gp-skm2-tamaranai-naranai",
            "title": "〜てたまらない vs 〜てならない (Unbearable Physical Urge vs Involuntary Spontaneous Emotion)",
            "meaning": "Expresses overwhelming sensations: 〜てたまらない (Unbearably acute sensory urge: 'Dying to/So itchy I can't bear it'). 〜てならない (Spontaneous internal feeling that naturally wells up from within).",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 25: 強く感じる (Overwhelming Sensations)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-て / い-adj くて / な-adj で + たまらない / ならない",
            "nuance": "CRITICAL DIFFERENCE: たまらない is for intense physical desires. ならない is for deep psychological intuitions and worries.",
            "keyTakeaway": "MUG-UP: たまらない = Unbearably acute (Sensory/Desire). ならない = Naturally wells up from within (Spontaneous emotion/Intuition).",
            "sentences": [
                make_sentence(
                    "s-skm2-25-1",
                    "一人で異国の地に暮らしていると、家族の声が無性に聞きたくてたまらなくなる時がある。",
                    "When living alone in a foreign land, there are times when I become unbearably longing to hear my family's voices.",
                    "Alone foreign land-in living-when, family's voice intensely hear-want unbearable become times have.",
                    [
                        tok("聞きたくてたまらなくなる", "ききたくてたまらなくなる", "kikitakute tamaranaku naru", "become unbearably longing to hear", "Grammar")
                    ],
                    "Acute emotional homesickness."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-25-1",
                    "遠方の被災地で孤立している人々の安否が、心配で（　　）。",
                    "I cannot help but feel deeply, uncontrollably worried about the safety of the people isolated in the distant disaster zone.",
                    ["ならない", "いられない", "きらない", "すぎない"],
                    0,
                    [
                        "Correct! 心配でならない is the standard literary expression for spontaneous, deep psychological worry.",
                        "Incorrect. 心配でいられない is ungrammatical (must be 〜てはいられない).",
                        "Incorrect. 心配できらない is ungrammatical.",
                        "Incorrect. 心配にすぎない means 'merely worried' (minimizing)."
                    ],
                    "Spontaneous psychological welling 〜てならない",
                    "Deep worry arising spontaneously for disaster victims."
                )
            ],
            "tags": ["N2", "SKM Ch 25", "Emotion", "Compulsion"]
        }
    ]
    return pts

if __name__ == '__main__':
    points = get_skm_n2_points()
    print(f"SKM N2 generated {len(points)} grammar points.")
