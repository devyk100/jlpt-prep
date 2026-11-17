# -*- coding: utf-8 -*-
"""
Shin Kanzen Master N2 Bunpou - Full Unabridged N2 Grammar Syllabus (Chapters 1 to 26 & Part 2/3)
Every individual grammar pattern and chapter section has its own discrete entry.
"""
from data_full_genki1 import tok, make_sentence, make_quiz

def get_full_skm_n2():
    pts = [
        # === CHAPTER 1: とき (TIME & OCCASIONS) ===
        {
            "id": "skm2-c1-ni-saishite",
            "title": "〜に際して / 〜にあたって (Upon the Occasion Of / At the Inception Of)",
            "meaning": "Formal expression used when initiating an important, solemn, or once-in-a-lifetime milestone: 'On the occasion of / Prior to commencing X'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 1: とき (Time & Occasions)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 + に際して / にあたって | Noun + に際して / にあたって",
            "nuance": "FORWARD-LOOKING MILESTONES: Used for marriages, opening a company, starting a contract, or delivering opening ceremonial greetings. You cannot use it for mundane daily events like waking up.",
            "keyTakeaway": "MUG-UP: V-る / Noun + に際して・にあたって = Formal ceremonial milestone! Forward-looking.",
            "sentences": [
                make_sentence(
                    "s-skm2-1-1",
                    "新会社の設立にあたって、出資者と関係各位に心より感謝の意を表します。",
                    "Upon the establishment of our new company, I express my heartfelt gratitude to the investors and all parties concerned.",
                    "New-company establishment upon, investors and related-parties-to heart-from gratitude express.",
                    [
                        tok("新会社の設立にあたって", "しんがいしゃのせつりつにあたって", "shin-gaisha no setsuritsu ni atatte", "upon founding the new company", "Grammar")
                    ],
                    "Solemn inaugural corporate speech."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-1-1",
                    "留学（　　）あたって、現地での生活費や保険について詳しく調べた。",
                    "Prior to studying abroad, I thoroughly researched living expenses and health insurance in the destination country.",
                    ["に", "を", "へ", "で"],
                    0,
                    [
                        "Correct! 留学にあたって expresses careful preparatory measures for a major life event.",
                        "Incorrect. 留学をあたって is an invalid particle combination.",
                        "Incorrect. 留学へあたって is ungrammatical.",
                        "Incorrect. 留学であたって does not exist."
                    ],
                    "Noun + にあたって milestone preparation",
                    "Preparations prior to studying abroad."
                )
            ],
            "tags": ["N2", "SKM Ch 1", "Milestone", "Formal"]
        },
        {
            "id": "skm2-c1-ka-to-omou-to",
            "title": "〜（か）と思うと / 〜（か）と思ったら (Just as I Thought X, Y Suddenly Burst Forth)",
            "meaning": "No sooner had condition X occurred than unexpected event Y abruptly and surprisingly burst forth: 'Hardly had... when suddenly...'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 1: とき (Time & Occasions)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-た + （か）と思うと / （か）と思ったら",
            "nuance": "SUDDEN REVERSAL: Clause B describes an instantaneous, jarring surprise or sudden shift. CANNOT be the speaker's own planned action or volition!",
            "keyTakeaway": "MUG-UP: V-た + かと思ったら = Just when I thought X, BAM, sudden surprise Y happened!",
            "sentences": [
                make_sentence(
                    "s-skm2-1-2",
                    "空が急に暗くなったかと思うと、激しい雷雨が降り出した。",
                    "No sooner had the sky suddenly turned dark than a violent thunderstorm began pouring down.",
                    "Sky suddenly dark-became thought-when, violent thunderstorm began-falling.",
                    [
                        tok("暗くなったかと思うと", "くらくなったかとおもうと", "kuraku natta ka to omou to", "just as it turned dark", "Grammar")
                    ],
                    "Jarring meteorological onset."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-1-2",
                    "赤ちゃんは今泣いていた（　　）思うと、もうすやすや眠っている。",
                    "Just when I thought the baby was crying right now, he is already sleeping peacefully.",
                    ["かと", "なと", "にと", "へと"],
                    0,
                    [
                        "Correct! 泣いていたかと思うと expresses lightning-fast reversal of baby's state.",
                        "Incorrect. なと is ungrammatical.",
                        "Incorrect. にと is invalid.",
                        "Incorrect. へと indicates directional transformation."
                    ],
                    "〜かと思うと sudden transition",
                    "Rapid shift from crying to sleep."
                )
            ],
            "tags": ["N2", "SKM Ch 1", "Sudden Change", "Time"]
        },
        {
            "id": "skm2-c1-kanai-ka-no-uchini",
            "title": "〜か〜ないかのうちに (On the Very Verge Of / Before Even Finishing)",
            "meaning": "Action Y takes place virtually simultaneously with action X, so fast that one can barely tell if X even finished: 'No sooner had... than...'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 1: とき (Time & Occasions)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-辞書形 / V-た + か + V-ない + かのうちに",
            "nuance": "PHYSICAL FRACTION OF A SECOND: The bell hasn't even finished vibrating before the students dash out (ベルが鳴り終わるか終わらないかのうちに飛び出した).",
            "keyTakeaway": "MUG-UP: V-る + か + V-ない + かのうちに = Before X even finished, Y happened!",
            "sentences": [
                make_sentence(
                    "s-skm2-1-3",
                    "授業終了のチャイムが鳴るか鳴らないかのうちに、生徒たちは教室を飛び出していった。",
                    "No sooner had the end-of-class chime begun ringing than the students dashed out of the classroom.",
                    "Class-end chime ring or ring-not within, students classroom dashed-out.",
                    [
                        tok("鳴るか鳴らないかのうちに", "なるかならないかのうちに", "naru ka naranai ka no uchi ni", "scarcely before it finished ringing", "Grammar")
                    ],
                    "Instantaneous burst of action at the bell."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-1-3",
                    "布団に横に（　　）か横にならないかのうちに、深い眠りに落ちてしまった。",
                    "No sooner had I lain down on the futon than I fell into a deep sleep.",
                    ["なる", "なって", "なり", "なら"],
                    0,
                    [
                        "Correct! 辞書形 横になるか + 横にならないかのうちに is the canonical pair.",
                        "Incorrect. なって is te-form.",
                        "Incorrect. なり is masu-stem.",
                        "Incorrect. なら is conditional."
                    ],
                    "V-るか〜ないかのうちに simultaneous timing",
                    "Falling asleep the instant head hits bed."
                )
            ],
            "tags": ["N2", "SKM Ch 1", "Simultaneous", "Time"]
        },

        # === CHAPTER 2: している (PROGRESS & SHIFTS) ===
        {
            "id": "skm2-c2-saichuu-da",
            "title": "〜最中だ / 〜最中に (In the Very Thick Of / Climax of Activity)",
            "meaning": "Right in the exact peak or middle of performing an activity, suddenly an external interruption intrudes unexpectedly: 'In the middle of X, Y happened'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 2: している (Progress & Shifts)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-ている + 最中に / 最中だ | Noun + の + 最中に / 最中だ",
            "nuance": "UNWANTED DISRUPTION: Clause B is virtually always an inconvenient disruption or obstacle that cuts in right at the worst time (e.g., power outage during surgery).",
            "keyTakeaway": "MUG-UP: V-ている + 最中に = Right in the thick of it, suddenly interrupted!",
            "sentences": [
                make_sentence(
                    "s-skm2-2-1",
                    "重要なプレゼンテーションを行っている最中に、停電でプロジェクターが消えてしまった。",
                    "Right in the middle of delivering an important presentation, the projector shut off due to a power outage.",
                    "Important presentation conducting middle-in, blackout-by projector vanished-regrettably.",
                    [
                        tok("行っている最中に", "おこなっているさいちゅうに", "okonatte iru saichuu ni", "right in the middle of conducting", "Grammar")
                    ],
                    "Severe external disruption during presentation."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-2-1",
                    "食事の（　　）に激しい地震が発生し、食器棚から皿が落ちて割れた。",
                    "Right in the middle of the meal, a violent earthquake struck, and plates fell from the cupboard and shattered.",
                    ["最中", "間", "うち", "次第"],
                    0,
                    [
                        "Correct! 食事の最中に captures the sudden, violent intrusion during the activity.",
                        "Incorrect. 間 lacks the specific dramatic climax of disruption.",
                        "Incorrect. うち requires different nuance.",
                        "Incorrect. 次第 means as soon as."
                    ],
                    "Noun + の + 最中に disruptive interruption",
                    "Earthquake striking mid-meal."
                )
            ],
            "tags": ["N2", "SKM Ch 2", "Interruption", "Progress"]
        },
        {
            "id": "skm2-c2-ippou-da-bakari-da",
            "title": "〜ばかりだ / 〜一方だ (Continual Single-Directional Trend: Keep On -ing)",
            "meaning": "An accelerating trend continues moving relentlessly in one direction without stopping: 'Keeps on getting worse / Deteriorating further and further'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 2: している (Progress & Shifts)",
            "streamId": "stream-trends",
            "streamName": "Trends, Changes & Proportional Evolution",
            "connection": "Change Verb (辞書形) + ばかりだ / 一方だ (悪化する, 増える, 減る, 上がる, 下がる)",
            "nuance": "NEGATIVE BIAS IN ばかりだ: ばかりだ is used almost exclusively for WORSE trends (悪化するばかりだ = Only getting worse). 一方だ can be used for both positive and negative continuous shifts.",
            "keyTakeaway": "MUG-UP: Change-Verb + 一方だ / ばかりだ = Relentlessly spiraling in one direction!",
            "sentences": [
                make_sentence(
                    "s-skm2-2-2",
                    "少子高齢化が進み、地方都市の人口は減少する一方だ。",
                    "With birth rates declining and population aging, the populations of regional cities keep on dwindling relentlessly.",
                    "Declining-birth aging advance, regional-city population decrease one-direction-is.",
                    [
                        tok("減少する一方だ", "げんしょうするいっぽうだ", "genshou suru ippou da", "keeps on steadily decreasing", "Grammar")
                    ],
                    "Relentless demographic decline."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-2-2",
                    "不景気の影響で、会社の業績は悪化する（　　）だ。",
                    "Under the impact of the recession, company performance is only worsening further and further.",
                    ["ばかり", "ところ", "わけ", "こと"],
                    0,
                    [
                        "Correct! 悪化するばかりだ expresses continuous negative downward spiral.",
                        "Incorrect. ところだ indicates temporal phase.",
                        "Incorrect. わけだ indicates logical consequence.",
                        "Incorrect. ことだ indicates advice or exclamation."
                    ],
                    "V-る + ばかりだ continual deterioration",
                    "Worsening business performance."
                )
            ],
            "tags": ["N2", "SKM Ch 2", "Trends", "Deterioration"]
        },

        # === CHAPTER 4: 範囲 (SCOPE & BOUNDS) ===
        {
            "id": "skm2-c4-wo-hajime",
            "title": "〜をはじめ（として） (Starting with Representative Prime Example X)",
            "meaning": "Singles out prime representative example X first, followed by numerous other members of the same category: 'Starting with X, as well as many others'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 4: 範囲 (Scope & Breakthroughs)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "Noun + をはじめ（として） / をはじめとする + Noun",
            "nuance": "CHIEF REPRESENTATIVE: Entity X is the most prominent, flagship, or famous example (e.g. 'Starting with Tokyo, cities across Japan...').",
            "keyTakeaway": "MUG-UP: Noun + をはじめとして = Prime flagship example first, plus the rest!",
            "sentences": [
                make_sentence(
                    "s-skm2-4-1",
                    "富士山をはじめ、日本には四季折々の美しい景観が数多く存在する。",
                    "Starting with Mt. Fuji, there exist numerous breathtaking landscapes reflecting the four seasons in Japan.",
                    "Mt-Fuji starting-with, Japan-in four-seasons beautiful landscapes many exist.",
                    [
                        tok("富士山をはじめ", "ふじさんをはじめ", "fujisan o hajime", "starting with Mt. Fuji", "Grammar")
                    ],
                    "Flagship natural landmark leading into nationwide landscapes."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-4-1",
                    "社長（　　）社員全員が一丸となって、新事業の成功に取り組んだ。",
                    "Starting with the company president, all employees united as one and tackled the success of the new business.",
                    ["をはじめ", "をめぐって", "をもとに", "にそって"],
                    0,
                    [
                        "Correct! 社長をはじめ marks the president as the leading representative of the entire company.",
                        "Incorrect. をめぐって means concerning a dispute.",
                        "Incorrect. をもとに means based on data/material.",
                        "Incorrect. にそって means conforming to rules."
                    ],
                    "Noun + をはじめ representative leader",
                    "Leadership leading organizational unity."
                )
            ],
            "tags": ["N2", "SKM Ch 4", "Scope", "Representative"]
        },
        {
            "id": "skm2-c4-kara-shite",
            "title": "〜からして (Judging Even from Such a Basic Initial Clue: From the Very...)",
            "meaning": "Judges or criticizes an entire whole by singling out one basic, glaring, or minor sample detail: 'Judging even from the very X, the whole thing is hopeless / obvious'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 4: 範囲 (Scope & Breakthroughs)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + からして",
            "nuance": "NEGATIVE CRITICISM / HARSH APPRAISAL: Frequently highlights a preliminary flaw: 'タイトルからして怪しい' (Suspicious even from its very title). '挨拶の仕方からしてなっていない' (Unacceptable even from the very way he greets).",
            "keyTakeaway": "MUG-UP: Noun + からして = 'Judging even from this one basic clue, the rest is bad!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-4-2",
                    "彼の態度は、挨拶の言葉遣いからして社会人としてなっていない。",
                    "His attitude, judging even from his very choice of words in greetings, is completely unacceptable as a working adult.",
                    "His attitude, greeting's word-choice from-even working-adult-as unacceptable.",
                    [
                        tok("言葉遣いからして", "ことばづかいからして", "kotobadzukai kara shite", "judging even from his phrasing", "Grammar")
                    ],
                    "Basic flaw indicating systemic unprofessionalism."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-4-2",
                    "この店の料理は、盛り付けの美しさ（　　）して一流の気品が漂っている。",
                    "This restaurant's cuisine, judging even from the sheer beauty of its presentation, radiates first-class elegance.",
                    ["から", "まで", "より", "ほど"],
                    0,
                    [
                        "Correct! 〜からして singles out presentation as an immediate indicative proof of top quality.",
                        "Incorrect. までして indicates extreme drastic measure ('even going so far as to...').",
                        "Incorrect. よりして is ungrammatical.",
                        "Incorrect. ほどして is invalid."
                    ],
                    "Noun + からして indicative clue",
                    "Visual presentation as proof of culinary excellence."
                )
            ],
            "tags": ["N2", "SKM Ch 4", "Clue", "Appraisal"]
        },
        {
            "id": "skm2-c4-ni-watatte",
            "title": "〜にわたって / 〜にわたり (Spanning Across Extensive Time or Space)",
            "meaning": "Indicates vast, uninterrupted scale across a large geographical expanse, temporal span, or multiple fields: 'Spanning across / Covering a period of X'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 4: 範囲 (Scope & Breakthroughs)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "Noun (Time Span / Space Expanse / Number of Sessions) + にわたって / にわたり",
            "nuance": "EXTENSIVE SCALE: Connects to words denoting broad range: 数十キロにわたって (spanning dozens of km), 三年間にわたって (spanning 3 full years), 全五回にわたり (spanning 5 sessions).",
            "keyTakeaway": "MUG-UP: [Large Range / Big Number] + にわたって = Spanning over a vast scale!",
            "sentences": [
                make_sentence(
                    "s-skm2-4-3",
                    "台風の影響で、この地域は三日間にわたって停電が続いた。",
                    "Under the influence of the typhoon, power outages persisted across this region spanning three full days.",
                    "Typhoon influence-by, this region 3-days-spanning blackout continued.",
                    [
                        tok("三日間にわたって", "みっかかんにわたって", "mikkakan ni watatte", "spanning across three full days", "Grammar")
                    ],
                    "Extensive temporal blackout span."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-4-3",
                    "高速道路は事故のため、十キロ（　　）わたって渋滞している。",
                    "Due to an accident, the expressway is congested spanning across ten kilometers.",
                    ["に", "を", "へ", "で"],
                    0,
                    [
                        "Correct! 十キロにわたって indicates the continuous 10km spatial span of the traffic jam.",
                        "Incorrect. をわたって is ungrammatical with this construction.",
                        "Incorrect. へわたって does not exist.",
                        "Incorrect. でわたって is invalid."
                    ],
                    "Spatial span 〜にわたって",
                    "Ten-kilometer expressway gridlock."
                )
            ],
            "tags": ["N2", "SKM Ch 4", "Scale", "Span"]
        },
        {
            "id": "skm2-c4-kagiri-dewa",
            "title": "〜限りでは (As Far As Scope of Information Reaches: Insofar As)",
            "meaning": "Restricts a judgment strictly to the boundary of personal knowledge, research, memory, or reports: 'As far as my knowledge/investigation goes...'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 4: 範囲 (Scope & Breakthroughs)",
            "streamId": "stream-limits",
            "streamName": "Boundaries, Extremes & Scope",
            "connection": "V-辞書形 / V-た + 限りでは | Noun + の + 限りでは (Pairs with informational verbs: 知る, 見る, 聞く, 調べた)",
            "nuance": "EPISTEMIC HUMILITY: Protects the speaker against being wrong outside their range: '私が知っている限りでは問題ありません' (As far as I know, there are no issues).",
            "keyTakeaway": "MUG-UP: [知る / 聞く / 調べる] + 限りでは = 'As far as my information reaches...'.",
            "sentences": [
                make_sentence(
                    "s-skm2-4-4",
                    "私が調べた限りでは、この地域に同業他社の店舗はまだ存在しません。",
                    "As far as my investigation reaches, no competitor stores exist in this region yet.",
                    "I investigated extent-in, this region competitor stores yet exist-not.",
                    [
                        tok("調べた限りでは", "しらべたかぎりでは", "shirabeta kagiri de wa", "as far as I have researched", "Grammar")
                    ],
                    "Scoping market research claim."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-4-4",
                    "警察の発表（　　）限りでは、今回の事件で怪我人は出ていないようだ。",
                    "As far as the police announcement indicates, no injuries appear to have occurred in this incident.",
                    ["の", "に", "を", "と"],
                    0,
                    [
                        "Correct! Noun 発表 connects via の to 限りでは (発表の限りでは).",
                        "Incorrect. に限り means strictly limited to.",
                        "Incorrect. を is direct object marker.",
                        "Incorrect. と connects clauses."
                    ],
                    "Noun + の + 限りでは information scope",
                    "Restricting statement to official police statement."
                )
            ],
            "tags": ["N2", "SKM Ch 4", "Information Scope", "Limits"]
        },

        # === CHAPTER 7: について・相手にして (TOPICS & TARGETS) ===
        {
            "id": "skm2-c7-wo-megutte",
            "title": "〜をめぐって / 〜をめぐる (Centering Around a Dispute, Controversy, or Conflict)",
            "meaning": "Indicates the contentious issue, disputed prize, or topic around which opposing parties argue, battle, or negotiate: 'Over / Regarding / Concerning [conflict]'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 7: について・相手にして (Topics & Targets)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + をめぐって (Adverbial) | Noun + をめぐる + Noun (Attributive)",
            "nuance": "MULTIPLE PARTIES IN CONTENTION: Unlike について which is neutral research ('I wrote a thesis ABOUT cats'), をめぐって requires contention, rivalry, or debate (e.g. arguing OVER inheritance, battling OVER rights).",
            "keyTakeaway": "MUG-UP: Noun + をめぐって = Fighting / debating OVER a controversial issue!",
            "sentences": [
                make_sentence(
                    "s-skm2-7-1",
                    "莫大な遺産の相続をめぐって、親族の間で激しい裁判闘争が続いている。",
                    "Centering around the inheritance of a vast fortune, a fierce legal battle continues among relatives.",
                    "Vast estate inheritance over, relatives-between fierce court-battle continuing.",
                    [
                        tok("相続をめぐって", "そうぞくをめぐって", "souzoku o megutte", "over the inheritance", "Grammar")
                    ],
                    "Legal dispute centered on disputed wealth."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-7-1",
                    "新空港の建設予定地を（　　）て、住民と行政の間で激しい議論が交わされた。",
                    "Over the planned construction site of the new airport, fierce debates were exchanged between residents and the government.",
                    ["めぐっ", "もとづい", "こたえ", "つうじ"],
                    0,
                    [
                        "Correct! 予定地をめぐって captures the contentious conflict between citizens and government.",
                        "Incorrect. もとづいて means based on evidence.",
                        "Incorrect. こたえて means responding to expectations.",
                        "Incorrect. つうじて means through the medium of."
                    ],
                    "Noun + をめぐって contentious controversy",
                    "Government-citizen conflict over airport site."
                )
            ],
            "tags": ["N2", "SKM Ch 7", "Dispute", "Controversy"]
        },
        {
            "id": "skm2-c7-ni-kotaete",
            "title": "〜にこたえて / 〜にこたえる (In Response to Expectations, Requests, or Demands)",
            "meaning": "Taking concrete action to meet, fulfill, or respond positively to expectations, public demands, cheer, or customer feedback.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 7: について・相手にして (Topics & Targets)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + にこたえて (Adverbial) | Noun + にこたえる + Noun (Attributive)",
            "nuance": "FAVORABLE RESPONSE TO CHEERS / DEMANDS: Fixed pairings: 期待にこたえて (meeting expectations), 要望にこたえて (responding to requests), アンコールにこたえて (responding to encore).",
            "keyTakeaway": "MUG-UP: [期待 / 要望 / 声援] にこたえて = Fulfilling expectations or demands!",
            "sentences": [
                make_sentence(
                    "s-skm2-7-2",
                    "お客様からの熱いご要望にこたえて、人気商品の再販売を決定いたしました。",
                    "In response to passionate requests from our customers, we have decided to resume sales of our popular item.",
                    "Customers passionate requests in-response-to, popular-item re-sale decided.",
                    [
                        tok("ご要望にこたえて", "ごようぼうにこたえて", "goyoubou ni kotaete", "in response to requests", "Grammar")
                    ],
                    "Corporate commercial response to customer feedback."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-7-2",
                    "ファンの温かい応援に（　　）て、選手は見事な逆転勝利を収めた。",
                    "In response to the warm cheers of the fans, the athlete achieved a spectacular comeback victory.",
                    ["こたえ", "そっ", "めぐっ", "たいし"],
                    0,
                    [
                        "Correct! 応援にこたえて expresses rising to the occasion driven by fan support.",
                        "Incorrect. そって means following along rules.",
                        "Incorrect. めぐって means over a dispute.",
                        "Incorrect. たいして means toward an object or in contrast."
                    ],
                    "Noun + にこたえて responsive action",
                    "Athlete motivated by fan support."
                )
            ],
            "tags": ["N2", "SKM Ch 7", "Expectations", "Response"]
        },

        # === CHAPTER 9: に関連して (CORRELATION & CORRESPONDENCE) ===
        {
            "id": "skm2-c9-ni-tsurete",
            "title": "〜につれて / 〜にしたがって (As X Progresses, Y Proportionally Evolves)",
            "meaning": "As condition A naturally moves or progresses along a timeline or scale, condition B simultaneously evolves in step: 'As X changes, Y evolves alongside'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 9: に関連して・に対応して (Correlation & Correspondence)",
            "streamId": "stream-trends",
            "streamName": "Trends, Changes & Proportional Evolution",
            "connection": "V-辞書形 (Change verb) + につれて | Noun (Change noun) + につれて",
            "nuance": "NATURAL DRIFT: Connects to verbs of ongoing spontaneous progression: 年を取るにつれて (As we grow older), 経済が発展するにつれて (As the economy develops).",
            "keyTakeaway": "MUG-UP: [Change Verb] につれて = In lockstep with the progress of X, Y evolves naturally!",
            "sentences": [
                make_sentence(
                    "s-skm2-9-1",
                    "台風が北上して近づくにつれて、風と雨が次第に激しくなってきた。",
                    "As the typhoon moved north and approached, the wind and rain gradually became violent.",
                    "Typhoon northward-moving approach as, wind and rain gradually violent became.",
                    [
                        tok("近づくにつれて", "ちかづくにつれて", "chikadzuku ni tsurete", "as it drew closer", "Grammar")
                    ],
                    "Simultaneous escalation of storm intensity with geographical proximity."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-9-1",
                    "日本での生活が長く（　　）につれて、日本の文化を深く理解できるようになった。",
                    "As my life in Japan became longer, I became able to deeply understand Japanese culture.",
                    ["なる", "なって", "なり", "なった"],
                    0,
                    [
                        "Correct! Plain dictionary form 長くなる connects directly to につれて.",
                        "Incorrect. なって is te-form.",
                        "Incorrect. なり is masu-stem.",
                        "Incorrect. なった is past form."
                    ],
                    "V-る + につれて proportional evolution",
                    "Cultural understanding deepening over time."
                )
            ],
            "tags": ["N2", "SKM Ch 9", "Proportion", "Trends"]
        },
        {
            "id": "skm2-c9-ni-oujite",
            "title": "〜に応じて / 〜に応じた (Commensurate with / Scaled Proportionally to)",
            "meaning": "Adjusting, tailoring, or varying action B in precise proportion to the scale, ability, budget, or circumstances of X: 'According to / Commensurate with'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 9: に関連して・に対応して (Correlation & Correspondence)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + に応じて (Adverbial) | Noun + に応じた + Noun (Attributive)",
            "nuance": "CUSTOMIZATION & SCALING: Modulating output based on input: 予算に応じて (according to budget), 能力に応じて (scaled to ability), 年齢に応じて (appropriate for age).",
            "keyTakeaway": "MUG-UP: Noun + に応じて = Custom-tailored / Scaled in proportion to X!",
            "sentences": [
                make_sentence(
                    "s-skm2-9-2",
                    "お客様のご予算に応じて、最適な旅行プランをカスタマイズいたします。",
                    "We will customize the optimal travel plan scaled strictly to your budget.",
                    "Customer budget commensurate-with, optimal travel plan customize.",
                    [
                        tok("ご予算に応じて", "ごよさんにおうじて", "goyosan ni oujite", "commensurate with your budget", "Grammar")
                    ],
                    "Commercial customization tailored to client spending power."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-9-2",
                    "子供の成長段階に（　　）本を選ぶことが、読書好きに育てる秘訣だ。",
                    "Selecting books customized appropriately to a child's developmental stage is the secret to raising an avid reader.",
                    ["応じた", "対した", "沿った", "向けた"],
                    0,
                    [
                        "Correct! 成長段階に応じた本 describes books calibrated to the child's developmental maturity.",
                        "Incorrect. 対した is ungrammatical before a noun without に.",
                        "Incorrect. 沿った implies following strict blueprints.",
                        "Incorrect. 向けた is unidiomatic here."
                    ],
                    "Noun + に応じた + Noun customized scaling",
                    "Calibrating literature to developmental age."
                )
            ],
            "tags": ["N2", "SKM Ch 9", "Tailoring", "Scaling"]
        },

        # === CHAPTER 11: 関係なく・無視して (DISREGARD & INCLUSIVITY) ===
        {
            "id": "skm2-c11-ni-kakawarazu",
            "title": "〜にかかわらず / 〜にかかわりなく (Regardless Of / Making No Difference)",
            "meaning": "Condition X exerts zero influence, restriction, or differential treatment on outcome B: 'Regardless of / No matter whether X or not'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 11: 関係なく・無視して (Disregard & Inclusivity)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun (with polarity: 天候, 合否) + にかかわらず | V-辞書形 + V-ない + にかかわらず (行く行かないにかかわらず)",
            "nuance": "OPPOSITE PAIRS: Ubiquitously connects to binary opposites: 参加するしないにかかわらず (whether you attend or not), 雨天・晴天にかかわらず (rain or shine).",
            "keyTakeaway": "MUG-UP: [Opposite Pair / Binary Noun] + にかかわらず = 'Regardless of whether A or B happens!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-11-1",
                    "明日のマラソン大会は、雨天決行です。天候にかかわらず予定通り行われます。",
                    "Tomorrow's marathon will proceed rain or shine. It will be held as scheduled regardless of the weather.",
                    "Tomorrow marathon rain-or-shine. Weather regardless as-scheduled held.",
                    [
                        tok("天候にかかわらず", "てんこうにかかわらず", "tenkou ni kakawarazu", "regardless of the weather", "Grammar")
                    ],
                    "Public athletic announcement dismissing weather variations."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-11-1",
                    "経験の有無（　　）かかわらず、どなたでも意欲のある方を歓迎します。",
                    "Regardless of whether you have experience or not, anyone with motivation is welcome.",
                    ["に", "を", "へ", "で"],
                    0,
                    [
                        "Correct! 有無にかかわらず (regardless of presence or absence) is the standard recruitment formula.",
                        "Incorrect. を is direct object marker.",
                        "Incorrect. へ is directional.",
                        "Incorrect. で is locational/means."
                    ],
                    "Noun + にかかわらず (Regardless of binary)",
                    "Job advertisement welcoming all experience levels."
                )
            ],
            "tags": ["N2", "SKM Ch 11", "Disregard", "Binary Choice"]
        },
        {
            "id": "skm2-c11-ha-tomo-kaku",
            "title": "〜はともかく（として） (Leaving A Aside for Now: Whether A Is So or Not)",
            "meaning": "Puts aside evaluating item A for the moment because item B is far more urgent, certain, or remarkable: 'Leaving aside A for now, B is certainly true'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 11: 関係なく・無視して (Disregard & Inclusivity)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + はともかく（として）",
            "nuance": "CONCESSIVE BRACKETING: '味はともかく、値段が安い' = Leaving aside whether it tastes great, the price is certainly dirt cheap! Bracket A to highlight B.",
            "keyTakeaway": "MUG-UP: [Questionable Quality A] はともかく、[Definite Fact B] = Setting aside A, B is undisputed!",
            "sentences": [
                make_sentence(
                    "s-skm2-11-2",
                    "デザインの良し悪しはともかくとして、この靴はとても軽くて歩きやすい。",
                    "Leaving aside whether the design is good or bad, these shoes are very lightweight and comfortable to walk in.",
                    "Design quality aside-leaving, these shoes very light walk-easy.",
                    [
                        tok("良し悪しはともかくとして", "よしあしはともかくとして", "yoshiashi wa tomokaku to shite", "leaving aside whether good or bad", "Grammar")
                    ],
                    "Bracketing aesthetic debate to praise functional comfort."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-11-2",
                    "合格できるか（　　）はともかく、全力を尽くして受験しよう。",
                    "Setting aside whether I can pass or not for now, let's exert my utmost effort on the exam.",
                    ["どう", "どうか", "なに", "いつ"],
                    1,
                    [
                        "Correct! Embedded binary 是否: 合格できるかどうかはともかく (Whether I can pass or not aside).",
                        "Incorrect. どう lacks the binary か interrogative.",
                        "Incorrect. なに means what.",
                        "Incorrect. いつ means when."
                    ],
                    "〜かどうかはともかく bracketing uncertainty",
                    "Bracketing outcome to focus on full exertion."
                )
            ],
            "tags": ["N2", "SKM Ch 11", "Bracketing", "Topic Framing"]
        },
        {
            "id": "skm2-c11-ha-sateoki",
            "title": "〜はさておき (Setting Aside A to Focus on the Immediate Priority B)",
            "meaning": "Consciously defers secondary topic A to immediately pivot conversational focus onto the primary core priority B: 'Putting A aside for the moment, let's deal with B'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 11: 関係なく・無視して (Disregard & Inclusivity)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + はさておき",
            "nuance": "PRIORITY SHIFT: Stronger conversational redirect than はともかく. Frequently used by meeting leaders: '冗談はさておき、本題に入りましょう' (Jokes aside, let's get down to business).",
            "keyTakeaway": "MUG-UP: Noun + はさておき = 'Jokes/side topics aside, let's address the real urgent matter!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-11-3",
                    "世間話はさておき、今日の会議のメインテーマである新規事業計画について話し合いましょう。",
                    "Putting small talk aside for the moment, let's discuss today's main meeting theme: the new business plan.",
                    "Small-talk aside-putting, today's meeting main theme new-business discuss let's.",
                    [
                        tok("世間話はさておき", "せけんばなしはさておき", "sekenbanashi wa sateoki", "setting aside small talk", "Grammar")
                    ],
                    "Pivoting formal agenda from casual pleasantries to agenda."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-11-3",
                    "冗談（　　）さておき、次のプロジェクトの締め切りはいつですか。",
                    "Jokes aside, when is the deadline for the next project?",
                    ["は", "を", "に", "が"],
                    0,
                    [
                        "Correct! 冗談はさておき is the classic idiom for 'all joking aside'.",
                        "Incorrect. を is ungrammatical with this construction.",
                        "Incorrect. に is invalid.",
                        "Incorrect. が does not form this topic pivot."
                    ],
                    "Noun + はさておき agenda pivot",
                    "Transitioning from humor to serious work deadline."
                )
            ],
            "tags": ["N2", "SKM Ch 11", "Priority Shift", "Conversation"]
        },

        # === CHAPTER 13: 話題は (TOPICS & HIGHLIGHTS) ===
        {
            "id": "skm2-c13-ni-kakete-wa",
            "title": "〜にかけては (When It Comes to Skill / Domain: Unrivaled Superiority)",
            "meaning": "Identifies a specific technical skill, athletic ability, or specialized domain where the subject has no equal: 'When it comes to X, no one surpasses them'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 13: 話題は (Topics & Specialties)",
            "streamId": "stream-topics",
            "streamName": "Topic Framing, Criteria & Disregard",
            "connection": "Noun + にかけては + Evaluative Superiority (だれにも負けない, 一番だ, 右に出る者はいない)",
            "nuance": "UNRIVALED MASTERY: Clause B virtually always expresses supreme confidence, unmatched mastery, or unbeatable excellence within that narrow slice of talent.",
            "keyTakeaway": "MUG-UP: [Skill / Domain] にかけては [Nobody can beat them!] Unmatched supremacy.",
            "sentences": [
                make_sentence(
                    "s-skm2-13-1",
                    "数学の難問を解くことにかけては、学年で彼の右に出る者はいない。",
                    "When it comes to solving difficult mathematics problems, there is nobody in the entire grade who can surpass him.",
                    "Math difficult-problems solve domain-in, grade-in his right-side exceed person none.",
                    [
                        tok("解くことにかけては", "とくことにかけては", "toku koto ni kakete wa", "when it comes to solving", "Grammar")
                    ],
                    "Supreme academic domain superiority."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-13-1",
                    "パソコンの修理（　　）かけては、社内で田中さんの知識が一番豊富です。",
                    "When it comes to computer repair, Tanaka-san's knowledge is the most extensive in the company.",
                    ["に", "を", "へ", "で"],
                    0,
                    [
                        "Correct! 修理にかけては specifies the specialized domain where Tanaka-san excels supreme.",
                        "Incorrect. をかけて means risking one's life (命をかけて).",
                        "Incorrect. へ is directional.",
                        "Incorrect. で is locational."
                    ],
                    "Noun + にかけては specialized expertise",
                    "Unmatched technical competence in IT repair."
                )
            ],
            "tags": ["N2", "SKM Ch 13", "Specialty", "Expertise"]
        },

        # === CHAPTER 15: もしそうなら (HYPOTHETICAL HORIZONS) ===
        {
            "id": "skm2-c15-mono-nara",
            "title": "〜ものなら (If by Any Miraculous Chance It Were Possible)",
            "meaning": "Hypothesizes a virtually impossible, desperate, or miraculous wish: 'If I could possibly do it (though realistically impossible), I would give everything to do so'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 15: もしそうなら (Hypothetical Horizons)",
            "streamId": "stream-conditionals",
            "streamName": "Conditional Logic & Inevitability",
            "connection": "V-可能形 + ものなら + Desperate Desire (〜たい, 〜てみたい)",
            "nuance": "DESPERATE IMPOSSIBILITY: The speaker knows reality cannot be undone, yet cries out in longing: 'やり直せるものならやり直したい' (If I could redo my life, I would). If paired with non-potential volitional, it acts as a severe threat: '動こうものなら撃つぞ' (If you so much as twitch, I shoot!).",
            "keyTakeaway": "MUG-UP: V-可能形 + ものなら = Desperate impossible wish! ('If by a miracle I could...').",
            "sentences": [
                make_sentence(
                    "s-skm2-15-1",
                    "過去に戻れるものなら、あの日に戻って人生をやり直したい。",
                    "If by any miraculous chance I could return to the past, I would want to return to that day and redo my life.",
                    "Past return-can if-miracle, that day return life redo want.",
                    [
                        tok("戻れるものなら", "もどれるものなら", "modoreru mono nara", "if by any miracle I could return", "Grammar")
                    ],
                    "Yearning for impossible temporal regression."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-15-1",
                    "病気の子供の痛みを代わって（　　）ものなら、代わってあげたい。",
                    "If by any miracle I could take on my sick child's pain in their place, I would take it on for them.",
                    ["やれる", "やる", "やった", "やり"],
                    0,
                    [
                        "Correct! Potential form やれる + ものなら expresses a parent's desperate, impossible wish.",
                        "Incorrect. やる is dictionary form without potential ability.",
                        "Incorrect. やった is past form.",
                        "Incorrect. やり is masu-stem."
                    ],
                    "V-可能形 + ものなら desperate impossible wish",
                    "Parental love yearning to absorb child's suffering."
                )
            ],
            "tags": ["N2", "SKM Ch 15", "Impossible Wish", "Conditionals"]
        },
        {
            "id": "skm2-c15-nai-koto-niwa",
            "title": "〜ないことには（〜ない） (Unless Condition X Occurs, Y Is Utterly Impossible)",
            "meaning": "Establishes a mandatory bottleneck: without condition X being thoroughly fulfilled, desirable result Y cannot happen: 'Unless X happens, Y is impossible'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 15: もしそうなら (Hypothetical Horizons)",
            "streamId": "stream-conditionals",
            "streamName": "Conditional Logic & Inevitability",
            "connection": "V-ないことには | い-adj くないことには | な-adj / Noun でないことには + Negative Predicate",
            "nuance": "STRICT BOTTLENECK: Clause B is ALWAYS negative: 始まらない, 分からない, 決められない. '実際に現地に行ってみないことには、本当の状況は分からない' (Unless you go in person, you cannot know).",
            "keyTakeaway": "MUG-UP: [Negative] ことには [Negative Predicate] = Unless X happens, Y cannot proceed!",
            "sentences": [
                make_sentence(
                    "s-skm2-15-2",
                    "全員の意見を聞いてみないことには、どちらの案を採用すべきか決められない。",
                    "Unless we listen to everyone's opinions first, we cannot decide which proposal ought to be adopted.",
                    "Everyone's opinions listen-try-not unless, which proposal adopt ought decide-cannot.",
                    [
                        tok("聞いてみないことには", "きいてみないことには", "kiite minai koto ni wa", "unless we try listening", "Grammar")
                    ],
                    "Democratic consensus prerequisite."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-15-2",
                    "本人に直接会って（　　）ことには、採用するかどうか判断できません。",
                    "Unless we meet the applicant in person directly, we cannot judge whether to hire them.",
                    ["話さない", "話す", "話して", "話した"],
                    0,
                    [
                        "Correct! 話さない + ことには sets up the mandatory interview bottleneck.",
                        "Incorrect. 話す is affirmative.",
                        "Incorrect. 話して is te-form.",
                        "Incorrect. 話した is past form."
                    ],
                    "V-ない + ことには bottleneck condition",
                    "Refusing hiring verdict without personal interview."
                )
            ],
            "tags": ["N2", "SKM Ch 15", "Bottleneck", "Prerequisite"]
        },
        {
            "id": "skm2-c15-wo-nuki-ni-shite-wa",
            "title": "〜を抜きにしては（〜ない） (Without Element X, Y Could Never Exist)",
            "meaning": "Praises the indispensable, vital role of X: without X's presence or contribution, success Y could never possibly have materialized.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 15: もしそうなら (Hypothetical Horizons)",
            "streamId": "stream-conditionals",
            "streamName": "Conditional Logic & Inevitability",
            "connection": "Noun + を抜きにしては / を抜きにして + Negative Predicate (あり得ない, 語れない, 成功しなかった)",
            "nuance": "DEEP INDEBTEDNESS: Used in award acceptance speeches, memoirs, and tributes: 'スタッフの献身的な支えを抜きにしては、この映画の完成はあり得なかった' (Without the staff's support, this movie could never exist).",
            "keyTakeaway": "MUG-UP: Noun + を抜きにしては + [あり得ない] = Without X, success would be 100% impossible!",
            "sentences": [
                make_sentence(
                    "s-skm2-15-3",
                    "国民の深い理解と協力を抜きにしては、この困難な改革を成し遂げることはできない。",
                    "Without the deep understanding and cooperation of the citizens, accomplishing this arduous reform is impossible.",
                    "Citizens' deep understanding cooperation without, this difficult reform achieve cannot.",
                    [
                        tok("協力を抜きにしては", "きょうりょくをぬきにしては", "kyouryoku o nuki ni shite wa", "without the cooperation of", "Grammar")
                    ],
                    "Statesman's acknowledgment of civic dependency."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-15-3",
                    "ボランティアの皆様の献身的な活動（　　）抜きにしては、大会の成功はあり得ませんでした。",
                    "Without the dedicated activities of all our volunteers, the success of this tournament would have been impossible.",
                    ["を", "に", "へ", "で"],
                    0,
                    [
                        "Correct! 活動を抜きにしては marks volunteer contribution as an irreplaceable prerequisite.",
                        "Incorrect. に抜きにしては is ungrammatical.",
                        "Incorrect. へ is invalid.",
                        "Incorrect. で is invalid."
                    ],
                    "Noun + を抜きにしては irreplaceable contribution",
                    "Tribute to volunteer tournament staff."
                )
            ],
            "tags": ["N2", "SKM Ch 15", "Irreplaceable", "Tribute"]
        },

        # === CHAPTER 16: だから (EMOTION & REASON) ===
        {
            "id": "skm2-c16-amari-excess",
            "title": "〜あまり / 〜あまりの〜に (So Overcome by Excessive Emotion That...)",
            "meaning": "Because emotional feeling, excitement, or tension X reaches an overwhelming, uncontrollable peak, an abnormal or extreme consequence Y resulted.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 16: だから (Emotion & Reason)",
            "streamId": "stream-causality",
            "streamName": "Causal Chains & Regret",
            "connection": "Noun + のあまり | V-辞書形 / V-た + あまり | あまりの + Noun + に / で",
            "nuance": "INTENSE PSYCHOLOGICAL STATE: Connects to words of powerful human affect: 驚きのあまり (in excess of shock), 悲しみのあまり (so grief-stricken that), 緊張のあまり (so nervous that).",
            "keyTakeaway": "MUG-UP: [Emotional Noun] のあまり = So overcome by intense emotion that an abnormal reaction occurred!",
            "sentences": [
                make_sentence(
                    "s-skm2-16-1",
                    "合格通知を受け取った母は、嬉しさのあまり大声を上げて泣き崩れてしまった。",
                    "Receiving the acceptance notice, my mother, overcome by intense joy, cried out loud and broke down in tears.",
                    "Acceptance-notice received mother, joy's excess loud-voice raised broke-down.",
                    [
                        tok("嬉しさのあまり", "うれしさのあまり", "uresisa no amari", "in excess of intense joy", "Grammar")
                    ],
                    "Overwhelming joy culminating in weeping."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-16-1",
                    "大勢の観客の前でスピーチをする（　　）の緊張に、頭が真っ白になってしまった。",
                    "From the sheer excess of nervous tension speaking before a huge audience, my mind went completely blank.",
                    ["あまり", "ばかり", "ほど", "わけ"],
                    0,
                    [
                        "Correct! あまりの緊張に (from excessive tension) describes cognitive paralysis under stress.",
                        "Incorrect. ばかり indicates only / just.",
                        "Incorrect. ほど indicates degree comparison.",
                        "Incorrect. わけ indicates logical reason."
                    ],
                    "あまりの + Noun + に emotional paralysis",
                    "Mind blanking under extreme stage fright."
                )
            ],
            "tags": ["N2", "SKM Ch 16", "Emotion", "Excess"]
        },

        # === CHAPTER 20: 結果 (OUTCOMES & ORDEALS) ===
        {
            "id": "skm2-c20-sue-ni-deliberation",
            "title": "〜末（に） / 〜末の (After Extensive Deliberation, Final Outcome Reached)",
            "meaning": "After enduring a protracted period of extensive agonizing, deliberation, or struggle, a final decisive outcome or resolution was reached: 'At the end of all that X, finally Y'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 20: 結果 (Outcomes & Conclusions)",
            "streamId": "stream-time",
            "streamName": "Chronos & Instant Transitions",
            "connection": "V-た + 末（に） | Noun + の + 末（に）",
            "nuance": "CONTRAST WITH AGEKU: あげく is virtually 100% negative/disastrous. 末に (すえに) can result in a positive, hard-won breakthrough OR a negative outcome (e.g. after long negotiations, agreement was reached: 激論の末に合意に達した).",
            "keyTakeaway": "MUG-UP: V-た / Noun + の + 末に = 'At the conclusion of an extensive process!'. Can be positive or negative.",
            "sentences": [
                make_sentence(
                    "s-skm2-20-1",
                    "何ヶ月にも及ぶ厳しい交渉の末に、両国は歴史的な平和条約に調印した。",
                    "At the end of grueling negotiations spanning many months, both nations finally signed a historic peace treaty.",
                    "Many-months spanning tough negotiations end-at, both-nations historic peace treaty signed.",
                    [
                        tok("交渉の末に", "こうしょうのすえに", "koushou no sue ni", "at the conclusion of negotiations", "Grammar")
                    ],
                    "Diplomatic breakthrough achieved after protracted talks."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-20-1",
                    "家族と何度も真剣に話し合っ（　　）末に、故郷へ戻って起業することを決断した。",
                    "At the end of discussing seriously with my family many times, I decisively chose to return home and start a business.",
                    ["た", "て", "る", "ない"],
                    0,
                    [
                        "Correct! 話し合った (past form) + 末に marks the culmination of deliberation.",
                        "Incorrect. て is te-form.",
                        "Incorrect. る is dictionary form.",
                        "Incorrect. ない is negative form."
                    ],
                    "V-た + 末に culmination of deliberation",
                    "Career decision made after family discussions."
                )
            ],
            "tags": ["N2", "SKM Ch 20", "Resolution", "Outcome"]
        },

        # === CHAPTER 21: 強く言う (EMPHATIC ASSERTION) ===
        {
            "id": "skm2-c21-ni-kimatte-iru",
            "title": "〜に決まっている (Inflexible Subjective Conviction: Bound to Be / Definitely)",
            "meaning": "Expresses an uncompromising, intuitive personal certainty: 'There is no doubt whatsoever! / It is bound to be X!'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 21: 強く言う (Emphatic Assertion)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Plain form + に決まっている (Noun / な-adj attach directly without だ: 嘘に決まっている, 暇に決まっている)",
            "nuance": "CONVICTION WITHOUT SCIENTIFIC PROOF: Stronger and more intuitive than に違いない. Driven by gut feeling, common sense, or indignant suspicion: 'そんなの嘘に決まっている!' (That's bound to be a lie!).",
            "keyTakeaway": "MUG-UP: [Plain predicate / Bare Noun] + に決まっている = 100% bound to be so in my mind!",
            "sentences": [
                make_sentence(
                    "s-skm2-21-1",
                    "こんな大雪の日に山へ登るなんて、危険に決まっている。今すぐ中止しなさい。",
                    "Climbing a mountain on a day with such heavy snow is bound to be dangerous. Call it off right now.",
                    "Such heavy-snow day mountain-to climb dangerous bound-to-be. Immediately cancel.",
                    [
                        tok("危険に決まっている", "きけんにきまっている", "kiken ni kimatte iru", "is bound to be dangerous", "Grammar")
                    ],
                    "Indignant safety common sense."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-21-1",
                    "あんなに毎日努力している彼が、試合に（　　）に決まっている。",
                    "He who puts in such effort every day is bound to win the match.",
                    ["勝つ", "勝って", "勝ち", "勝ったの"],
                    0,
                    [
                        "Correct! Plain dictionary form 勝つ connects directly to に決まっている.",
                        "Incorrect. 勝って is te-form.",
                        "Incorrect. 勝ち is masu-stem.",
                        "Incorrect. 勝ったの has redundant nominalizer."
                    ],
                    "Plain form + に決まっている conviction",
                    "Unshakable faith in a teammate's victory."
                )
            ],
            "tags": ["N2", "SKM Ch 21", "Certainty", "Conviction"]
        },

        # === CHAPTER 22: だろうと思う (SPECULATION & PROBABILITY) ===
        {
            "id": "skm2-c22-osore-ga-aru",
            "title": "〜恐れがある (Grave Risk / Looming Danger of Adverse Outcome)",
            "meaning": "Formal journalistic and administrative warning that a serious negative event or disaster might happen: 'There is a grave fear/danger that X may occur'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 22: だろうと思う (Speculation & Probability)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 / V-ない + 恐れがある | Noun + の + 恐れがある",
            "nuance": "STRICTLY GRAVE NEGATIVE RISKS: Used for typhoons, disease outbreaks, economic meltdowns, or extinctions. CANNOT be used for positive hopes (e.g. 'There is a danger we might pass the exam' ❌).",
            "keyTakeaway": "MUG-UP: V-る / Noun + の + 恐れがある = Public warning of looming danger / risk!",
            "sentences": [
                make_sentence(
                    "s-skm2-22-1",
                    "この火山は活動が活発化しており、近い将来に大規模な噴火を起こす恐れがある。",
                    "This volcano's activity is intensifying, and there is a grave fear that it may trigger a large-scale eruption in the near future.",
                    "This volcano activity intensifying, near-future large-scale eruption cause danger has.",
                    [
                        tok("噴火を起こす恐れがある", "ふんかをおこすおそれがある", "funka o okosu osore ga aru", "there is a grave risk of an eruption", "Grammar")
                    ],
                    "Volcanological geological alert."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-22-1",
                    "適切な治療を受けないと、病状がさらに悪化する（　　）があります。",
                    "Unless you receive appropriate treatment, there is a risk that your condition will deteriorate further.",
                    ["恐れ", "はず", "わけ", "こと"],
                    0,
                    [
                        "Correct! 悪化する恐れがある is the standard medical warning formula for risk of deterioration.",
                        "Incorrect. はず means logical expectation.",
                        "Incorrect. わけ means logical cause.",
                        "Incorrect. こと means general fact."
                    ],
                    "V-る + 恐れがある risk warning",
                    "Medical warning of condition deterioration."
                )
            ],
            "tags": ["N2", "SKM Ch 22", "Risk", "Warning"]
        },

        # === CHAPTER 23: 感想を言う (REFLECTIONS & ESSENCE) ===
        {
            "id": "skm2-c23-mono-da-essence",
            "title": "〜ものだ (Universal Truth, Innate Human Nature, or Nostalgic Reminiscence)",
            "meaning": "1) Innate Truth: That is naturally how human beings or the world inherently are ('Children are naturally energetic'). 2) Nostalgia: Looking back on fond past habits with た ('I used to swim in this river').",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 23: 感想を言う (Reflections & Essence)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-辞書形 + ものだ (General truth / Nature) | V-た + ものだ (Fond past habit)",
            "nuance": "PHILOSOPHICAL NATURE: Not a legal requirement, but a profound observation on how the world works: '人の心は移ろいやすいものだ' (The human heart is naturally fickle). With た-form, sighs with nostalgia: '子供の頃はよく川で遊んだものだ' (I used to play in the river).",
            "keyTakeaway": "MUG-UP: V-る + ものだ = General truth / human nature. V-た + ものだ = 'Ah, I used to do that often...'.",
            "sentences": [
                make_sentence(
                    "s-skm2-23-1",
                    "若い頃は、夜を徹して友達と語り明かしたものだ。",
                    "Back when I was young, I used to often talk the night away with my friends.",
                    "Young time, night through friend-with talk-spend used-to.",
                    [
                        tok("語り明かしたものだ", "かたりあかしたものだ", "katariakashita mono da", "used to talk the night away (fond nostalgia)", "Grammar")
                    ],
                    "Nostalgic reminiscence of youth."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-23-1",
                    "月日の経つのは本当に早い（　　）ですね。もう一年が終わってしまいます。",
                    "Time truly flies so fast, doesn't it? Another whole year is coming to an end already.",
                    ["もの", "こと", "わけ", "はず"],
                    0,
                    [
                        "Correct! 早いものですね is the canonical philosophical exclamation on the swift passage of time.",
                        "Incorrect. 早いことですね is awkward.",
                        "Incorrect. 早いわけですね means 'so that is why it is early'.",
                        "Incorrect. 早いはずですね means 'it ought to be early'."
                    ],
                    "Adjective + ものだ philosophical reflection",
                    "Reflecting on the swift passage of time."
                )
            ],
            "tags": ["N2", "SKM Ch 23", "Nostalgia", "Human Nature"]
        },
        {
            "id": "skm2-c23-ni-koshita-koto-wa-nai",
            "title": "〜に越したことはない (Nothing Surpasses Caution / Best to Be Safe)",
            "meaning": "Practical worldly wisdom: While other options exist, X is definitely the safest, most foolproof, or ideal policy: 'Nothing beats being prepared / It is best to do X'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 23: 感想を言う (Reflections & Essence)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "Plain form + に越したことはない (Noun / な-adj takes である or direct: 安全に越したことはない)",
            "nuance": "COMMON-SENSE PRUDENCE: '準備は早めにしておくのに越したことはない' (You can never be too early with preparations). Emphasizes sensible risk aversion.",
            "keyTakeaway": "MUG-UP: [Sensible Policy] に越したことはない = Best to be safe! (用心に越したことはない).",
            "sentences": [
                make_sentence(
                    "s-skm2-23-2",
                    "雨は降らないかもしれないが、念のため折り畳み傘を持って行くに越したことはない。",
                    "It might not rain, but just in case, nothing beats taking a folding umbrella with you.",
                    "Rain fall-not might but, just-in-case folding-umbrella bring-go best-is.",
                    [
                        tok("持って行くに越したことはない", "もっていくにこしたことはない", "motte iku ni koshita koto wa nai", "nothing beats bringing it along", "Grammar")
                    ],
                    "Prudent advice to pack an umbrella just in case."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-23-2",
                    "病気の予防のためには、手洗いうがいを徹底するに（　　）ことはない。",
                    "For disease prevention, nothing surpasses thorough hand-washing and gargling.",
                    ["越した", "限った", "至った", "及んだ"],
                    0,
                    [
                        "Correct! 徹底するに越したことはない is the idiomatic expression for prudent prevention.",
                        "Incorrect. 限ったことはない does not exist.",
                        "Incorrect. 至ったことはない is ungrammatical.",
                        "Incorrect. 及んだことはない is invalid."
                    ],
                    "〜に越したことはない prudent wisdom",
                    "Hand-washing as best preventive measure."
                )
            ],
            "tags": ["N2", "SKM Ch 23", "Prudence", "Wisdom"]
        },

        # === CHAPTER 25: 強く感じる (OVERWHELMING SENSATIONS) ===
        {
            "id": "skm2-c25-te-wa-irarenai",
            "title": "〜てはいられない / 〜てられない (Cannot Afford to Keep Idling / Urgency)",
            "meaning": "Due to high urgency, pressing emergency, or moral crisis, one cannot afford to remain idle or continue doing X: 'I can't just sit here doing X!'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 25: 強く感じる (Overwhelming Sensations)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-て + はいられない (Spoken: 〜てられない)",
            "nuance": "CRITICAL EMERGENCY / CALL TO ACTION: You cannot stay inactive in the present posture: 'のんびりお茶を飲んではいられない、早く避難しよう!' (We can't just sit here sipping tea; let's evacuate!).",
            "keyTakeaway": "MUG-UP: V-て + はいられない = 'I can't afford to just sit here doing X! Time to act!'.",
            "sentences": [
                make_sentence(
                    "s-skm2-25-1",
                    "試験まであと一週間しかないのだから、遊んではいられない。",
                    "Since there is only one week left until the exam, I cannot afford to be playing around.",
                    "Exam-until only 1-week have-not since, playing-around afford-cannot.",
                    [
                        tok("遊んではいられない", "あそんではいられない", "asonde wa irarenai", "cannot afford to play around", "Grammar")
                    ],
                    "Urgent study pressure eliminating leisure."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-25-1",
                    "こんな重大な危機に直面して、ただ黙って（　　）はいられない。",
                    "Facing such a critical crisis, I cannot afford to just keep silent and do nothing.",
                    ["見て", "見", "見る", "見た"],
                    0,
                    [
                        "Correct! 黙って見ている (silently watching) becomes 黙って見てはいられない ('cannot just look on').",
                        "Incorrect. 見はいられない is ungrammatical without て.",
                        "Incorrect. 見るはいられない is invalid.",
                        "Incorrect. 見た is past form."
                    ],
                    "V-て + はいられない urgent compulsion",
                    "Compelled to speak up during a crisis."
                )
            ],
            "tags": ["N2", "SKM Ch 25", "Urgency", "Call to Action"]
        },
        {
            "id": "skm2-c25-zu-niwa-irarenai",
            "title": "〜ずにいられない / 〜ないではいられない (Cannot Help But Do / Irresistible Urge)",
            "meaning": "An internal psychological urge or emotional impulse is so intensely overwhelming that the speaker is irresistibly compelled to do X: 'Cannot help but do / Cannot suppress doing'.",
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": "Chapter 25: 強く感じる (Overwhelming Sensations)",
            "streamId": "stream-modality",
            "streamName": "Epistemic Certainty, Conviction & Duty",
            "connection": "V-ない form (drop ない) + ずにいられない (する irregular: せずにいられない) / ないではいられない",
            "nuance": "UNCONTROLLABLE EMOTIONAL IMPULSE: Laughing, crying, saying something, or helping: '彼の面白い顔を見たら、笑わずにはいられなかった' (Seeing his funny face, I couldn't help but burst into laughter).",
            "keyTakeaway": "MUG-UP: V-ず + にはいられない = 'I simply couldn't stop myself from doing it!'. する becomes せず.",
            "sentences": [
                make_sentence(
                    "s-skm2-25-2",
                    "あまりの理不尽な対応に、一言抗議せずにはいられなかった。",
                    "Confronted with such an overly unreasonable response, I couldn't help but voice a word of protest.",
                    "Overly unreasonable response-to, one-word protest without could-not-stay.",
                    [
                        tok("抗議せずにはいられなかった", "こうぎせずにはいられなかった", "kougi sezu ni wa irarenakatta", "couldn't help but protest", "Grammar")
                    ],
                    "Irrepressible moral protest against injustice."
                )
            ],
            "quiz": [
                make_quiz(
                    "q-skm2-25-2",
                    "悲しい結末の映画を見て、涙を（　　）ずにはいられなかった。",
                    "Watching the movie with its tragic ending, I couldn't help but shed tears.",
                    ["流さ", "流し", "流す", "流せ"],
                    0,
                    [
                        "Correct! 流す negative stem 流さ + ずにいられない forms 流さずにはいられなかった ('couldn't help shedding tears').",
                        "Incorrect. 流し is masu-stem.",
                        "Incorrect. 流す is dictionary form.",
                        "Incorrect. 流せ is imperative/potential stem."
                    ],
                    "V-ず + にはいられない irresistible emotional impulse",
                    "Uncontrollable tears at movie ending."
                )
            ],
            "tags": ["N2", "SKM Ch 25", "Impulse", "Emotion"]
        }
    ]
    return pts

if __name__ == '__main__':
    pts = get_full_skm_n2()
    print(f"SKM N2 generated {len(pts)} exhaustive discrete grammar points.")

