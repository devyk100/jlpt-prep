import type { GrammarPoint } from '../types';

export const BOOK_SKM_N2_POINTS: GrammarPoint[] = [
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
      {
        "id": "s-skm2-1-1",
        "japanese": "新会社の設立にあたって、出資者と関係各位に心より感謝の意を表します。",
        "english": "Upon the establishment of our new company, I express my heartfelt gratitude to the investors and all parties concerned.",
        "literal": "New-company establishment upon, investors and related-parties-to heart-from gratitude express.",
        "tokens": [
          {
            "word": "新会社の設立にあたって",
            "meaning": "upon founding the new company",
            "reading": "しんがいしゃのせつりつにあたって",
            "romaji": "shin-gaisha no setsuritsu ni atatte",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Solemn inaugural corporate speech."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-1-1",
        "question": "留学（　　）あたって、現地での生活費や保険について詳しく調べた。",
        "translation": "Prior to studying abroad, I thoroughly researched living expenses and health insurance in the destination country.",
        "options": [
          "に",
          "を",
          "へ",
          "で"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + にあたって milestone preparation",
        "ruleHint": "Preparations prior to studying abroad.",
        "explanations": [
          {
            "text": "に",
            "isCorrect": true,
            "reason": "Correct! 留学にあたって expresses careful preparatory measures for a major life event."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. 留学をあたって is an invalid particle combination."
          },
          {
            "text": "へ",
            "isCorrect": false,
            "reason": "Incorrect. 留学へあたって is ungrammatical."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. 留学であたって does not exist."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 1",
      "Milestone",
      "Formal"
    ]
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
      {
        "id": "s-skm2-1-2",
        "japanese": "空が急に暗くなったかと思うと、激しい雷雨が降り出した。",
        "english": "No sooner had the sky suddenly turned dark than a violent thunderstorm began pouring down.",
        "literal": "Sky suddenly dark-became thought-when, violent thunderstorm began-falling.",
        "tokens": [
          {
            "word": "暗くなったかと思うと",
            "meaning": "just as it turned dark",
            "reading": "くらくなったかとおもうと",
            "romaji": "kuraku natta ka to omou to",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Jarring meteorological onset."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-1-2",
        "question": "赤ちゃんは今泣いていた（　　）思うと、もうすやすや眠っている。",
        "translation": "Just when I thought the baby was crying right now, he is already sleeping peacefully.",
        "options": [
          "かと",
          "なと",
          "にと",
          "へと"
        ],
        "correctIndex": 0,
        "grammarFocus": "〜かと思うと sudden transition",
        "ruleHint": "Rapid shift from crying to sleep.",
        "explanations": [
          {
            "text": "かと",
            "isCorrect": true,
            "reason": "Correct! 泣いていたかと思うと expresses lightning-fast reversal of baby's state."
          },
          {
            "text": "なと",
            "isCorrect": false,
            "reason": "Incorrect. なと is ungrammatical."
          },
          {
            "text": "にと",
            "isCorrect": false,
            "reason": "Incorrect. にと is invalid."
          },
          {
            "text": "へと",
            "isCorrect": false,
            "reason": "Incorrect. へと indicates directional transformation."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 1",
      "Sudden Change",
      "Time"
    ]
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
      {
        "id": "s-skm2-1-3",
        "japanese": "授業終了のチャイムが鳴るか鳴らないかのうちに、生徒たちは教室を飛び出していった。",
        "english": "No sooner had the end-of-class chime begun ringing than the students dashed out of the classroom.",
        "literal": "Class-end chime ring or ring-not within, students classroom dashed-out.",
        "tokens": [
          {
            "word": "鳴るか鳴らないかのうちに",
            "meaning": "scarcely before it finished ringing",
            "reading": "なるかならないかのうちに",
            "romaji": "naru ka naranai ka no uchi ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Instantaneous burst of action at the bell."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-1-3",
        "question": "布団に横に（　　）か横にならないかのうちに、深い眠りに落ちてしまった。",
        "translation": "No sooner had I lain down on the futon than I fell into a deep sleep.",
        "options": [
          "なる",
          "なって",
          "なり",
          "なら"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-るか〜ないかのうちに simultaneous timing",
        "ruleHint": "Falling asleep the instant head hits bed.",
        "explanations": [
          {
            "text": "なる",
            "isCorrect": true,
            "reason": "Correct! 辞書形 横になるか + 横にならないかのうちに is the canonical pair."
          },
          {
            "text": "なって",
            "isCorrect": false,
            "reason": "Incorrect. なって is te-form."
          },
          {
            "text": "なり",
            "isCorrect": false,
            "reason": "Incorrect. なり is masu-stem."
          },
          {
            "text": "なら",
            "isCorrect": false,
            "reason": "Incorrect. なら is conditional."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 1",
      "Simultaneous",
      "Time"
    ]
  },
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
      {
        "id": "s-skm2-2-1",
        "japanese": "重要なプレゼンテーションを行っている最中に、停電でプロジェクターが消えてしまった。",
        "english": "Right in the middle of delivering an important presentation, the projector shut off due to a power outage.",
        "literal": "Important presentation conducting middle-in, blackout-by projector vanished-regrettably.",
        "tokens": [
          {
            "word": "行っている最中に",
            "meaning": "right in the middle of conducting",
            "reading": "おこなっているさいちゅうに",
            "romaji": "okonatte iru saichuu ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Severe external disruption during presentation."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-2-1",
        "question": "食事の（　　）に激しい地震が発生し、食器棚から皿が落ちて割れた。",
        "translation": "Right in the middle of the meal, a violent earthquake struck, and plates fell from the cupboard and shattered.",
        "options": [
          "最中",
          "間",
          "うち",
          "次第"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + の + 最中に disruptive interruption",
        "ruleHint": "Earthquake striking mid-meal.",
        "explanations": [
          {
            "text": "最中",
            "isCorrect": true,
            "reason": "Correct! 食事の最中に captures the sudden, violent intrusion during the activity."
          },
          {
            "text": "間",
            "isCorrect": false,
            "reason": "Incorrect. 間 lacks the specific dramatic climax of disruption."
          },
          {
            "text": "うち",
            "isCorrect": false,
            "reason": "Incorrect. うち requires different nuance."
          },
          {
            "text": "次第",
            "isCorrect": false,
            "reason": "Incorrect. 次第 means as soon as."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 2",
      "Interruption",
      "Progress"
    ]
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
      {
        "id": "s-skm2-2-2",
        "japanese": "少子高齢化が進み、地方都市の人口は減少する一方だ。",
        "english": "With birth rates declining and population aging, the populations of regional cities keep on dwindling relentlessly.",
        "literal": "Declining-birth aging advance, regional-city population decrease one-direction-is.",
        "tokens": [
          {
            "word": "減少する一方だ",
            "meaning": "keeps on steadily decreasing",
            "reading": "げんしょうするいっぽうだ",
            "romaji": "genshou suru ippou da",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Relentless demographic decline."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-2-2",
        "question": "不景気の影響で、会社の業績は悪化する（　　）だ。",
        "translation": "Under the impact of the recession, company performance is only worsening further and further.",
        "options": [
          "ばかり",
          "ところ",
          "わけ",
          "こと"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-る + ばかりだ continual deterioration",
        "ruleHint": "Worsening business performance.",
        "explanations": [
          {
            "text": "ばかり",
            "isCorrect": true,
            "reason": "Correct! 悪化するばかりだ expresses continuous negative downward spiral."
          },
          {
            "text": "ところ",
            "isCorrect": false,
            "reason": "Incorrect. ところだ indicates temporal phase."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. わけだ indicates logical consequence."
          },
          {
            "text": "こと",
            "isCorrect": false,
            "reason": "Incorrect. ことだ indicates advice or exclamation."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 2",
      "Trends",
      "Deterioration"
    ]
  },
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
      {
        "id": "s-skm2-4-1",
        "japanese": "富士山をはじめ、日本には四季折々の美しい景観が数多く存在する。",
        "english": "Starting with Mt. Fuji, there exist numerous breathtaking landscapes reflecting the four seasons in Japan.",
        "literal": "Mt-Fuji starting-with, Japan-in four-seasons beautiful landscapes many exist.",
        "tokens": [
          {
            "word": "富士山をはじめ",
            "meaning": "starting with Mt. Fuji",
            "reading": "ふじさんをはじめ",
            "romaji": "fujisan o hajime",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Flagship natural landmark leading into nationwide landscapes."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-4-1",
        "question": "社長（　　）社員全員が一丸となって、新事業の成功に取り組んだ。",
        "translation": "Starting with the company president, all employees united as one and tackled the success of the new business.",
        "options": [
          "をはじめ",
          "をめぐって",
          "をもとに",
          "にそって"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + をはじめ representative leader",
        "ruleHint": "Leadership leading organizational unity.",
        "explanations": [
          {
            "text": "をはじめ",
            "isCorrect": true,
            "reason": "Correct! 社長をはじめ marks the president as the leading representative of the entire company."
          },
          {
            "text": "をめぐって",
            "isCorrect": false,
            "reason": "Incorrect. をめぐって means concerning a dispute."
          },
          {
            "text": "をもとに",
            "isCorrect": false,
            "reason": "Incorrect. をもとに means based on data/material."
          },
          {
            "text": "にそって",
            "isCorrect": false,
            "reason": "Incorrect. にそって means conforming to rules."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 4",
      "Scope",
      "Representative"
    ]
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
      {
        "id": "s-skm2-4-2",
        "japanese": "彼の態度は、挨拶の言葉遣いからして社会人としてなっていない。",
        "english": "His attitude, judging even from his very choice of words in greetings, is completely unacceptable as a working adult.",
        "literal": "His attitude, greeting's word-choice from-even working-adult-as unacceptable.",
        "tokens": [
          {
            "word": "言葉遣いからして",
            "meaning": "judging even from his phrasing",
            "reading": "ことばづかいからして",
            "romaji": "kotobadzukai kara shite",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Basic flaw indicating systemic unprofessionalism."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-4-2",
        "question": "この店の料理は、盛り付けの美しさ（　　）して一流の気品が漂っている。",
        "translation": "This restaurant's cuisine, judging even from the sheer beauty of its presentation, radiates first-class elegance.",
        "options": [
          "から",
          "まで",
          "より",
          "ほど"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + からして indicative clue",
        "ruleHint": "Visual presentation as proof of culinary excellence.",
        "explanations": [
          {
            "text": "から",
            "isCorrect": true,
            "reason": "Correct! 〜からして singles out presentation as an immediate indicative proof of top quality."
          },
          {
            "text": "まで",
            "isCorrect": false,
            "reason": "Incorrect. までして indicates extreme drastic measure ('even going so far as to...')."
          },
          {
            "text": "より",
            "isCorrect": false,
            "reason": "Incorrect. よりして is ungrammatical."
          },
          {
            "text": "ほど",
            "isCorrect": false,
            "reason": "Incorrect. ほどして is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 4",
      "Clue",
      "Appraisal"
    ]
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
      {
        "id": "s-skm2-4-3",
        "japanese": "台風の影響で、この地域は三日間にわたって停電が続いた。",
        "english": "Under the influence of the typhoon, power outages persisted across this region spanning three full days.",
        "literal": "Typhoon influence-by, this region 3-days-spanning blackout continued.",
        "tokens": [
          {
            "word": "三日間にわたって",
            "meaning": "spanning across three full days",
            "reading": "みっかかんにわたって",
            "romaji": "mikkakan ni watatte",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Extensive temporal blackout span."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-4-3",
        "question": "高速道路は事故のため、十キロ（　　）わたって渋滞している。",
        "translation": "Due to an accident, the expressway is congested spanning across ten kilometers.",
        "options": [
          "に",
          "を",
          "へ",
          "で"
        ],
        "correctIndex": 0,
        "grammarFocus": "Spatial span 〜にわたって",
        "ruleHint": "Ten-kilometer expressway gridlock.",
        "explanations": [
          {
            "text": "に",
            "isCorrect": true,
            "reason": "Correct! 十キロにわたって indicates the continuous 10km spatial span of the traffic jam."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. をわたって is ungrammatical with this construction."
          },
          {
            "text": "へ",
            "isCorrect": false,
            "reason": "Incorrect. へわたって does not exist."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. でわたって is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 4",
      "Scale",
      "Span"
    ]
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
      {
        "id": "s-skm2-4-4",
        "japanese": "私が調べた限りでは、この地域に同業他社の店舗はまだ存在しません。",
        "english": "As far as my investigation reaches, no competitor stores exist in this region yet.",
        "literal": "I investigated extent-in, this region competitor stores yet exist-not.",
        "tokens": [
          {
            "word": "調べた限りでは",
            "meaning": "as far as I have researched",
            "reading": "しらべたかぎりでは",
            "romaji": "shirabeta kagiri de wa",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Scoping market research claim."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-4-4",
        "question": "警察の発表（　　）限りでは、今回の事件で怪我人は出ていないようだ。",
        "translation": "As far as the police announcement indicates, no injuries appear to have occurred in this incident.",
        "options": [
          "の",
          "に",
          "を",
          "と"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + の + 限りでは information scope",
        "ruleHint": "Restricting statement to official police statement.",
        "explanations": [
          {
            "text": "の",
            "isCorrect": true,
            "reason": "Correct! Noun 発表 connects via の to 限りでは (発表の限りでは)."
          },
          {
            "text": "に",
            "isCorrect": false,
            "reason": "Incorrect. に限り means strictly limited to."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. を is direct object marker."
          },
          {
            "text": "と",
            "isCorrect": false,
            "reason": "Incorrect. と connects clauses."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 4",
      "Information Scope",
      "Limits"
    ]
  },
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
      {
        "id": "s-skm2-7-1",
        "japanese": "莫大な遺産の相続をめぐって、親族の間で激しい裁判闘争が続いている。",
        "english": "Centering around the inheritance of a vast fortune, a fierce legal battle continues among relatives.",
        "literal": "Vast estate inheritance over, relatives-between fierce court-battle continuing.",
        "tokens": [
          {
            "word": "相続をめぐって",
            "meaning": "over the inheritance",
            "reading": "そうぞくをめぐって",
            "romaji": "souzoku o megutte",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Legal dispute centered on disputed wealth."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-7-1",
        "question": "新空港の建設予定地を（　　）て、住民と行政の間で激しい議論が交わされた。",
        "translation": "Over the planned construction site of the new airport, fierce debates were exchanged between residents and the government.",
        "options": [
          "めぐっ",
          "もとづい",
          "こたえ",
          "つうじ"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + をめぐって contentious controversy",
        "ruleHint": "Government-citizen conflict over airport site.",
        "explanations": [
          {
            "text": "めぐっ",
            "isCorrect": true,
            "reason": "Correct! 予定地をめぐって captures the contentious conflict between citizens and government."
          },
          {
            "text": "もとづい",
            "isCorrect": false,
            "reason": "Incorrect. もとづいて means based on evidence."
          },
          {
            "text": "こたえ",
            "isCorrect": false,
            "reason": "Incorrect. こたえて means responding to expectations."
          },
          {
            "text": "つうじ",
            "isCorrect": false,
            "reason": "Incorrect. つうじて means through the medium of."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 7",
      "Dispute",
      "Controversy"
    ]
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
      {
        "id": "s-skm2-7-2",
        "japanese": "お客様からの熱いご要望にこたえて、人気商品の再販売を決定いたしました。",
        "english": "In response to passionate requests from our customers, we have decided to resume sales of our popular item.",
        "literal": "Customers passionate requests in-response-to, popular-item re-sale decided.",
        "tokens": [
          {
            "word": "ご要望にこたえて",
            "meaning": "in response to requests",
            "reading": "ごようぼうにこたえて",
            "romaji": "goyoubou ni kotaete",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Corporate commercial response to customer feedback."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-7-2",
        "question": "ファンの温かい応援に（　　）て、選手は見事な逆転勝利を収めた。",
        "translation": "In response to the warm cheers of the fans, the athlete achieved a spectacular comeback victory.",
        "options": [
          "こたえ",
          "そっ",
          "めぐっ",
          "たいし"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + にこたえて responsive action",
        "ruleHint": "Athlete motivated by fan support.",
        "explanations": [
          {
            "text": "こたえ",
            "isCorrect": true,
            "reason": "Correct! 応援にこたえて expresses rising to the occasion driven by fan support."
          },
          {
            "text": "そっ",
            "isCorrect": false,
            "reason": "Incorrect. そって means following along rules."
          },
          {
            "text": "めぐっ",
            "isCorrect": false,
            "reason": "Incorrect. めぐって means over a dispute."
          },
          {
            "text": "たいし",
            "isCorrect": false,
            "reason": "Incorrect. たいして means toward an object or in contrast."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 7",
      "Expectations",
      "Response"
    ]
  },
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
      {
        "id": "s-skm2-9-1",
        "japanese": "台風が北上して近づくにつれて、風と雨が次第に激しくなってきた。",
        "english": "As the typhoon moved north and approached, the wind and rain gradually became violent.",
        "literal": "Typhoon northward-moving approach as, wind and rain gradually violent became.",
        "tokens": [
          {
            "word": "近づくにつれて",
            "meaning": "as it drew closer",
            "reading": "ちかづくにつれて",
            "romaji": "chikadzuku ni tsurete",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Simultaneous escalation of storm intensity with geographical proximity."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-9-1",
        "question": "日本での生活が長く（　　）につれて、日本の文化を深く理解できるようになった。",
        "translation": "As my life in Japan became longer, I became able to deeply understand Japanese culture.",
        "options": [
          "なる",
          "なって",
          "なり",
          "なった"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-る + につれて proportional evolution",
        "ruleHint": "Cultural understanding deepening over time.",
        "explanations": [
          {
            "text": "なる",
            "isCorrect": true,
            "reason": "Correct! Plain dictionary form 長くなる connects directly to につれて."
          },
          {
            "text": "なって",
            "isCorrect": false,
            "reason": "Incorrect. なって is te-form."
          },
          {
            "text": "なり",
            "isCorrect": false,
            "reason": "Incorrect. なり is masu-stem."
          },
          {
            "text": "なった",
            "isCorrect": false,
            "reason": "Incorrect. なった is past form."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 9",
      "Proportion",
      "Trends"
    ]
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
      {
        "id": "s-skm2-9-2",
        "japanese": "お客様のご予算に応じて、最適な旅行プランをカスタマイズいたします。",
        "english": "We will customize the optimal travel plan scaled strictly to your budget.",
        "literal": "Customer budget commensurate-with, optimal travel plan customize.",
        "tokens": [
          {
            "word": "ご予算に応じて",
            "meaning": "commensurate with your budget",
            "reading": "ごよさんにおうじて",
            "romaji": "goyosan ni oujite",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Commercial customization tailored to client spending power."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-9-2",
        "question": "子供の成長段階に（　　）本を選ぶことが、読書好きに育てる秘訣だ。",
        "translation": "Selecting books customized appropriately to a child's developmental stage is the secret to raising an avid reader.",
        "options": [
          "応じた",
          "対した",
          "沿った",
          "向けた"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + に応じた + Noun customized scaling",
        "ruleHint": "Calibrating literature to developmental age.",
        "explanations": [
          {
            "text": "応じた",
            "isCorrect": true,
            "reason": "Correct! 成長段階に応じた本 describes books calibrated to the child's developmental maturity."
          },
          {
            "text": "対した",
            "isCorrect": false,
            "reason": "Incorrect. 対した is ungrammatical before a noun without に."
          },
          {
            "text": "沿った",
            "isCorrect": false,
            "reason": "Incorrect. 沿った implies following strict blueprints."
          },
          {
            "text": "向けた",
            "isCorrect": false,
            "reason": "Incorrect. 向けた is unidiomatic here."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 9",
      "Tailoring",
      "Scaling"
    ]
  },
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
      {
        "id": "s-skm2-11-1",
        "japanese": "明日のマラソン大会は、雨天決行です。天候にかかわらず予定通り行われます。",
        "english": "Tomorrow's marathon will proceed rain or shine. It will be held as scheduled regardless of the weather.",
        "literal": "Tomorrow marathon rain-or-shine. Weather regardless as-scheduled held.",
        "tokens": [
          {
            "word": "天候にかかわらず",
            "meaning": "regardless of the weather",
            "reading": "てんこうにかかわらず",
            "romaji": "tenkou ni kakawarazu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Public athletic announcement dismissing weather variations."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-11-1",
        "question": "経験の有無（　　）かかわらず、どなたでも意欲のある方を歓迎します。",
        "translation": "Regardless of whether you have experience or not, anyone with motivation is welcome.",
        "options": [
          "に",
          "を",
          "へ",
          "で"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + にかかわらず (Regardless of binary)",
        "ruleHint": "Job advertisement welcoming all experience levels.",
        "explanations": [
          {
            "text": "に",
            "isCorrect": true,
            "reason": "Correct! 有無にかかわらず (regardless of presence or absence) is the standard recruitment formula."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. を is direct object marker."
          },
          {
            "text": "へ",
            "isCorrect": false,
            "reason": "Incorrect. へ is directional."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. で is locational/means."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 11",
      "Disregard",
      "Binary Choice"
    ]
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
      {
        "id": "s-skm2-11-2",
        "japanese": "デザインの良し悪しはともかくとして、この靴はとても軽くて歩きやすい。",
        "english": "Leaving aside whether the design is good or bad, these shoes are very lightweight and comfortable to walk in.",
        "literal": "Design quality aside-leaving, these shoes very light walk-easy.",
        "tokens": [
          {
            "word": "良し悪しはともかくとして",
            "meaning": "leaving aside whether good or bad",
            "reading": "よしあしはともかくとして",
            "romaji": "yoshiashi wa tomokaku to shite",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Bracketing aesthetic debate to praise functional comfort."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-11-2",
        "question": "合格できるか（　　）はともかく、全力を尽くして受験しよう。",
        "translation": "Setting aside whether I can pass or not for now, let's exert my utmost effort on the exam.",
        "options": [
          "どう",
          "どうか",
          "なに",
          "いつ"
        ],
        "correctIndex": 1,
        "grammarFocus": "〜かどうかはともかく bracketing uncertainty",
        "ruleHint": "Bracketing outcome to focus on full exertion.",
        "explanations": [
          {
            "text": "どう",
            "isCorrect": false,
            "reason": "Correct! Embedded binary 是否: 合格できるかどうかはともかく (Whether I can pass or not aside)."
          },
          {
            "text": "どうか",
            "isCorrect": true,
            "reason": "Incorrect. どう lacks the binary か interrogative."
          },
          {
            "text": "なに",
            "isCorrect": false,
            "reason": "Incorrect. なに means what."
          },
          {
            "text": "いつ",
            "isCorrect": false,
            "reason": "Incorrect. いつ means when."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 11",
      "Bracketing",
      "Topic Framing"
    ]
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
      {
        "id": "s-skm2-11-3",
        "japanese": "世間話はさておき、今日の会議のメインテーマである新規事業計画について話し合いましょう。",
        "english": "Putting small talk aside for the moment, let's discuss today's main meeting theme: the new business plan.",
        "literal": "Small-talk aside-putting, today's meeting main theme new-business discuss let's.",
        "tokens": [
          {
            "word": "世間話はさておき",
            "meaning": "setting aside small talk",
            "reading": "せけんばなしはさておき",
            "romaji": "sekenbanashi wa sateoki",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Pivoting formal agenda from casual pleasantries to agenda."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-11-3",
        "question": "冗談（　　）さておき、次のプロジェクトの締め切りはいつですか。",
        "translation": "Jokes aside, when is the deadline for the next project?",
        "options": [
          "は",
          "を",
          "に",
          "が"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + はさておき agenda pivot",
        "ruleHint": "Transitioning from humor to serious work deadline.",
        "explanations": [
          {
            "text": "は",
            "isCorrect": true,
            "reason": "Correct! 冗談はさておき is the classic idiom for 'all joking aside'."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. を is ungrammatical with this construction."
          },
          {
            "text": "に",
            "isCorrect": false,
            "reason": "Incorrect. に is invalid."
          },
          {
            "text": "が",
            "isCorrect": false,
            "reason": "Incorrect. が does not form this topic pivot."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 11",
      "Priority Shift",
      "Conversation"
    ]
  },
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
      {
        "id": "s-skm2-13-1",
        "japanese": "数学の難問を解くことにかけては、学年で彼の右に出る者はいない。",
        "english": "When it comes to solving difficult mathematics problems, there is nobody in the entire grade who can surpass him.",
        "literal": "Math difficult-problems solve domain-in, grade-in his right-side exceed person none.",
        "tokens": [
          {
            "word": "解くことにかけては",
            "meaning": "when it comes to solving",
            "reading": "とくことにかけては",
            "romaji": "toku koto ni kakete wa",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Supreme academic domain superiority."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-13-1",
        "question": "パソコンの修理（　　）かけては、社内で田中さんの知識が一番豊富です。",
        "translation": "When it comes to computer repair, Tanaka-san's knowledge is the most extensive in the company.",
        "options": [
          "に",
          "を",
          "へ",
          "で"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + にかけては specialized expertise",
        "ruleHint": "Unmatched technical competence in IT repair.",
        "explanations": [
          {
            "text": "に",
            "isCorrect": true,
            "reason": "Correct! 修理にかけては specifies the specialized domain where Tanaka-san excels supreme."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. をかけて means risking one's life (命をかけて)."
          },
          {
            "text": "へ",
            "isCorrect": false,
            "reason": "Incorrect. へ is directional."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. で is locational."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 13",
      "Specialty",
      "Expertise"
    ]
  },
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
      {
        "id": "s-skm2-15-1",
        "japanese": "過去に戻れるものなら、あの日に戻って人生をやり直したい。",
        "english": "If by any miraculous chance I could return to the past, I would want to return to that day and redo my life.",
        "literal": "Past return-can if-miracle, that day return life redo want.",
        "tokens": [
          {
            "word": "戻れるものなら",
            "meaning": "if by any miracle I could return",
            "reading": "もどれるものなら",
            "romaji": "modoreru mono nara",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Yearning for impossible temporal regression."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-15-1",
        "question": "病気の子供の痛みを代わって（　　）ものなら、代わってあげたい。",
        "translation": "If by any miracle I could take on my sick child's pain in their place, I would take it on for them.",
        "options": [
          "やれる",
          "やる",
          "やった",
          "やり"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-可能形 + ものなら desperate impossible wish",
        "ruleHint": "Parental love yearning to absorb child's suffering.",
        "explanations": [
          {
            "text": "やれる",
            "isCorrect": true,
            "reason": "Correct! Potential form やれる + ものなら expresses a parent's desperate, impossible wish."
          },
          {
            "text": "やる",
            "isCorrect": false,
            "reason": "Incorrect. やる is dictionary form without potential ability."
          },
          {
            "text": "やった",
            "isCorrect": false,
            "reason": "Incorrect. やった is past form."
          },
          {
            "text": "やり",
            "isCorrect": false,
            "reason": "Incorrect. やり is masu-stem."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 15",
      "Impossible Wish",
      "Conditionals"
    ]
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
      {
        "id": "s-skm2-15-2",
        "japanese": "全員の意見を聞いてみないことには、どちらの案を採用すべきか決められない。",
        "english": "Unless we listen to everyone's opinions first, we cannot decide which proposal ought to be adopted.",
        "literal": "Everyone's opinions listen-try-not unless, which proposal adopt ought decide-cannot.",
        "tokens": [
          {
            "word": "聞いてみないことには",
            "meaning": "unless we try listening",
            "reading": "きいてみないことには",
            "romaji": "kiite minai koto ni wa",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Democratic consensus prerequisite."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-15-2",
        "question": "本人に直接会って（　　）ことには、採用するかどうか判断できません。",
        "translation": "Unless we meet the applicant in person directly, we cannot judge whether to hire them.",
        "options": [
          "話さない",
          "話す",
          "話して",
          "話した"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-ない + ことには bottleneck condition",
        "ruleHint": "Refusing hiring verdict without personal interview.",
        "explanations": [
          {
            "text": "話さない",
            "isCorrect": true,
            "reason": "Correct! 話さない + ことには sets up the mandatory interview bottleneck."
          },
          {
            "text": "話す",
            "isCorrect": false,
            "reason": "Incorrect. 話す is affirmative."
          },
          {
            "text": "話して",
            "isCorrect": false,
            "reason": "Incorrect. 話して is te-form."
          },
          {
            "text": "話した",
            "isCorrect": false,
            "reason": "Incorrect. 話した is past form."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 15",
      "Bottleneck",
      "Prerequisite"
    ]
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
      {
        "id": "s-skm2-15-3",
        "japanese": "国民の深い理解と協力を抜きにしては、この困難な改革を成し遂げることはできない。",
        "english": "Without the deep understanding and cooperation of the citizens, accomplishing this arduous reform is impossible.",
        "literal": "Citizens' deep understanding cooperation without, this difficult reform achieve cannot.",
        "tokens": [
          {
            "word": "協力を抜きにしては",
            "meaning": "without the cooperation of",
            "reading": "きょうりょくをぬきにしては",
            "romaji": "kyouryoku o nuki ni shite wa",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Statesman's acknowledgment of civic dependency."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-15-3",
        "question": "ボランティアの皆様の献身的な活動（　　）抜きにしては、大会の成功はあり得ませんでした。",
        "translation": "Without the dedicated activities of all our volunteers, the success of this tournament would have been impossible.",
        "options": [
          "を",
          "に",
          "へ",
          "で"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + を抜きにしては irreplaceable contribution",
        "ruleHint": "Tribute to volunteer tournament staff.",
        "explanations": [
          {
            "text": "を",
            "isCorrect": true,
            "reason": "Correct! 活動を抜きにしては marks volunteer contribution as an irreplaceable prerequisite."
          },
          {
            "text": "に",
            "isCorrect": false,
            "reason": "Incorrect. に抜きにしては is ungrammatical."
          },
          {
            "text": "へ",
            "isCorrect": false,
            "reason": "Incorrect. へ is invalid."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. で is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 15",
      "Irreplaceable",
      "Tribute"
    ]
  },
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
      {
        "id": "s-skm2-16-1",
        "japanese": "合格通知を受け取った母は、嬉しさのあまり大声を上げて泣き崩れてしまった。",
        "english": "Receiving the acceptance notice, my mother, overcome by intense joy, cried out loud and broke down in tears.",
        "literal": "Acceptance-notice received mother, joy's excess loud-voice raised broke-down.",
        "tokens": [
          {
            "word": "嬉しさのあまり",
            "meaning": "in excess of intense joy",
            "reading": "うれしさのあまり",
            "romaji": "uresisa no amari",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Overwhelming joy culminating in weeping."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-16-1",
        "question": "大勢の観客の前でスピーチをする（　　）の緊張に、頭が真っ白になってしまった。",
        "translation": "From the sheer excess of nervous tension speaking before a huge audience, my mind went completely blank.",
        "options": [
          "あまり",
          "ばかり",
          "ほど",
          "わけ"
        ],
        "correctIndex": 0,
        "grammarFocus": "あまりの + Noun + に emotional paralysis",
        "ruleHint": "Mind blanking under extreme stage fright.",
        "explanations": [
          {
            "text": "あまり",
            "isCorrect": true,
            "reason": "Correct! あまりの緊張に (from excessive tension) describes cognitive paralysis under stress."
          },
          {
            "text": "ばかり",
            "isCorrect": false,
            "reason": "Incorrect. ばかり indicates only / just."
          },
          {
            "text": "ほど",
            "isCorrect": false,
            "reason": "Incorrect. ほど indicates degree comparison."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. わけ indicates logical reason."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 16",
      "Emotion",
      "Excess"
    ]
  },
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
      {
        "id": "s-skm2-20-1",
        "japanese": "何ヶ月にも及ぶ厳しい交渉の末に、両国は歴史的な平和条約に調印した。",
        "english": "At the end of grueling negotiations spanning many months, both nations finally signed a historic peace treaty.",
        "literal": "Many-months spanning tough negotiations end-at, both-nations historic peace treaty signed.",
        "tokens": [
          {
            "word": "交渉の末に",
            "meaning": "at the conclusion of negotiations",
            "reading": "こうしょうのすえに",
            "romaji": "koushou no sue ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Diplomatic breakthrough achieved after protracted talks."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-20-1",
        "question": "家族と何度も真剣に話し合っ（　　）末に、故郷へ戻って起業することを決断した。",
        "translation": "At the end of discussing seriously with my family many times, I decisively chose to return home and start a business.",
        "options": [
          "た",
          "て",
          "る",
          "ない"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-た + 末に culmination of deliberation",
        "ruleHint": "Career decision made after family discussions.",
        "explanations": [
          {
            "text": "た",
            "isCorrect": true,
            "reason": "Correct! 話し合った (past form) + 末に marks the culmination of deliberation."
          },
          {
            "text": "て",
            "isCorrect": false,
            "reason": "Incorrect. て is te-form."
          },
          {
            "text": "る",
            "isCorrect": false,
            "reason": "Incorrect. る is dictionary form."
          },
          {
            "text": "ない",
            "isCorrect": false,
            "reason": "Incorrect. ない is negative form."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 20",
      "Resolution",
      "Outcome"
    ]
  },
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
      {
        "id": "s-skm2-21-1",
        "japanese": "こんな大雪の日に山へ登るなんて、危険に決まっている。今すぐ中止しなさい。",
        "english": "Climbing a mountain on a day with such heavy snow is bound to be dangerous. Call it off right now.",
        "literal": "Such heavy-snow day mountain-to climb dangerous bound-to-be. Immediately cancel.",
        "tokens": [
          {
            "word": "危険に決まっている",
            "meaning": "is bound to be dangerous",
            "reading": "きけんにきまっている",
            "romaji": "kiken ni kimatte iru",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Indignant safety common sense."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-21-1",
        "question": "あんなに毎日努力している彼が、試合に（　　）に決まっている。",
        "translation": "He who puts in such effort every day is bound to win the match.",
        "options": [
          "勝つ",
          "勝って",
          "勝ち",
          "勝ったの"
        ],
        "correctIndex": 0,
        "grammarFocus": "Plain form + に決まっている conviction",
        "ruleHint": "Unshakable faith in a teammate's victory.",
        "explanations": [
          {
            "text": "勝つ",
            "isCorrect": true,
            "reason": "Correct! Plain dictionary form 勝つ connects directly to に決まっている."
          },
          {
            "text": "勝って",
            "isCorrect": false,
            "reason": "Incorrect. 勝って is te-form."
          },
          {
            "text": "勝ち",
            "isCorrect": false,
            "reason": "Incorrect. 勝ち is masu-stem."
          },
          {
            "text": "勝ったの",
            "isCorrect": false,
            "reason": "Incorrect. 勝ったの has redundant nominalizer."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 21",
      "Certainty",
      "Conviction"
    ]
  },
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
      {
        "id": "s-skm2-22-1",
        "japanese": "この火山は活動が活発化しており、近い将来に大規模な噴火を起こす恐れがある。",
        "english": "This volcano's activity is intensifying, and there is a grave fear that it may trigger a large-scale eruption in the near future.",
        "literal": "This volcano activity intensifying, near-future large-scale eruption cause danger has.",
        "tokens": [
          {
            "word": "噴火を起こす恐れがある",
            "meaning": "there is a grave risk of an eruption",
            "reading": "ふんかをおこすおそれがある",
            "romaji": "funka o okosu osore ga aru",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Volcanological geological alert."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-22-1",
        "question": "適切な治療を受けないと、病状がさらに悪化する（　　）があります。",
        "translation": "Unless you receive appropriate treatment, there is a risk that your condition will deteriorate further.",
        "options": [
          "恐れ",
          "はず",
          "わけ",
          "こと"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-る + 恐れがある risk warning",
        "ruleHint": "Medical warning of condition deterioration.",
        "explanations": [
          {
            "text": "恐れ",
            "isCorrect": true,
            "reason": "Correct! 悪化する恐れがある is the standard medical warning formula for risk of deterioration."
          },
          {
            "text": "はず",
            "isCorrect": false,
            "reason": "Incorrect. はず means logical expectation."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. わけ means logical cause."
          },
          {
            "text": "こと",
            "isCorrect": false,
            "reason": "Incorrect. こと means general fact."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 22",
      "Risk",
      "Warning"
    ]
  },
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
      {
        "id": "s-skm2-23-1",
        "japanese": "若い頃は、夜を徹して友達と語り明かしたものだ。",
        "english": "Back when I was young, I used to often talk the night away with my friends.",
        "literal": "Young time, night through friend-with talk-spend used-to.",
        "tokens": [
          {
            "word": "語り明かしたものだ",
            "meaning": "used to talk the night away (fond nostalgia)",
            "reading": "かたりあかしたものだ",
            "romaji": "katariakashita mono da",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Nostalgic reminiscence of youth."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-23-1",
        "question": "月日の経つのは本当に早い（　　）ですね。もう一年が終わってしまいます。",
        "translation": "Time truly flies so fast, doesn't it? Another whole year is coming to an end already.",
        "options": [
          "もの",
          "こと",
          "わけ",
          "はず"
        ],
        "correctIndex": 0,
        "grammarFocus": "Adjective + ものだ philosophical reflection",
        "ruleHint": "Reflecting on the swift passage of time.",
        "explanations": [
          {
            "text": "もの",
            "isCorrect": true,
            "reason": "Correct! 早いものですね is the canonical philosophical exclamation on the swift passage of time."
          },
          {
            "text": "こと",
            "isCorrect": false,
            "reason": "Incorrect. 早いことですね is awkward."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. 早いわけですね means 'so that is why it is early'."
          },
          {
            "text": "はず",
            "isCorrect": false,
            "reason": "Incorrect. 早いはずですね means 'it ought to be early'."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 23",
      "Nostalgia",
      "Human Nature"
    ]
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
      {
        "id": "s-skm2-23-2",
        "japanese": "雨は降らないかもしれないが、念のため折り畳み傘を持って行くに越したことはない。",
        "english": "It might not rain, but just in case, nothing beats taking a folding umbrella with you.",
        "literal": "Rain fall-not might but, just-in-case folding-umbrella bring-go best-is.",
        "tokens": [
          {
            "word": "持って行くに越したことはない",
            "meaning": "nothing beats bringing it along",
            "reading": "もっていくにこしたことはない",
            "romaji": "motte iku ni koshita koto wa nai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Prudent advice to pack an umbrella just in case."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-23-2",
        "question": "病気の予防のためには、手洗いうがいを徹底するに（　　）ことはない。",
        "translation": "For disease prevention, nothing surpasses thorough hand-washing and gargling.",
        "options": [
          "越した",
          "限った",
          "至った",
          "及んだ"
        ],
        "correctIndex": 0,
        "grammarFocus": "〜に越したことはない prudent wisdom",
        "ruleHint": "Hand-washing as best preventive measure.",
        "explanations": [
          {
            "text": "越した",
            "isCorrect": true,
            "reason": "Correct! 徹底するに越したことはない is the idiomatic expression for prudent prevention."
          },
          {
            "text": "限った",
            "isCorrect": false,
            "reason": "Incorrect. 限ったことはない does not exist."
          },
          {
            "text": "至った",
            "isCorrect": false,
            "reason": "Incorrect. 至ったことはない is ungrammatical."
          },
          {
            "text": "及んだ",
            "isCorrect": false,
            "reason": "Incorrect. 及んだことはない is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 23",
      "Prudence",
      "Wisdom"
    ]
  },
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
      {
        "id": "s-skm2-25-1",
        "japanese": "試験まであと一週間しかないのだから、遊んではいられない。",
        "english": "Since there is only one week left until the exam, I cannot afford to be playing around.",
        "literal": "Exam-until only 1-week have-not since, playing-around afford-cannot.",
        "tokens": [
          {
            "word": "遊んではいられない",
            "meaning": "cannot afford to play around",
            "reading": "あそんではいられない",
            "romaji": "asonde wa irarenai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Urgent study pressure eliminating leisure."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-25-1",
        "question": "こんな重大な危機に直面して、ただ黙って（　　）はいられない。",
        "translation": "Facing such a critical crisis, I cannot afford to just keep silent and do nothing.",
        "options": [
          "見て",
          "見",
          "見る",
          "見た"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-て + はいられない urgent compulsion",
        "ruleHint": "Compelled to speak up during a crisis.",
        "explanations": [
          {
            "text": "見て",
            "isCorrect": true,
            "reason": "Correct! 黙って見ている (silently watching) becomes 黙って見てはいられない ('cannot just look on')."
          },
          {
            "text": "見",
            "isCorrect": false,
            "reason": "Incorrect. 見はいられない is ungrammatical without て."
          },
          {
            "text": "見る",
            "isCorrect": false,
            "reason": "Incorrect. 見るはいられない is invalid."
          },
          {
            "text": "見た",
            "isCorrect": false,
            "reason": "Incorrect. 見た is past form."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 25",
      "Urgency",
      "Call to Action"
    ]
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
      {
        "id": "s-skm2-25-2",
        "japanese": "あまりの理不尽な対応に、一言抗議せずにはいられなかった。",
        "english": "Confronted with such an overly unreasonable response, I couldn't help but voice a word of protest.",
        "literal": "Overly unreasonable response-to, one-word protest without could-not-stay.",
        "tokens": [
          {
            "word": "抗議せずにはいられなかった",
            "meaning": "couldn't help but protest",
            "reading": "こうぎせずにはいられなかった",
            "romaji": "kougi sezu ni wa irarenakatta",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Irrepressible moral protest against injustice."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-25-2",
        "question": "悲しい結末の映画を見て、涙を（　　）ずにはいられなかった。",
        "translation": "Watching the movie with its tragic ending, I couldn't help but shed tears.",
        "options": [
          "流さ",
          "流し",
          "流す",
          "流せ"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-ず + にはいられない irresistible emotional impulse",
        "ruleHint": "Uncontrollable tears at movie ending.",
        "explanations": [
          {
            "text": "流さ",
            "isCorrect": true,
            "reason": "Correct! 流す negative stem 流さ + ずにいられない forms 流さずにはいられなかった ('couldn't help shedding tears')."
          },
          {
            "text": "流し",
            "isCorrect": false,
            "reason": "Incorrect. 流し is masu-stem."
          },
          {
            "text": "流す",
            "isCorrect": false,
            "reason": "Incorrect. 流す is dictionary form."
          },
          {
            "text": "流せ",
            "isCorrect": false,
            "reason": "Incorrect. 流せ is imperative/potential stem."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 25",
      "Impulse",
      "Emotion"
    ]
  },
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
      {
        "id": "s-skm2-1-4",
        "japanese": "ドアを開けたとたんに、強烈な冷たい風が部屋の中に吹き込んできた。",
        "english": "The very instant I opened the door, a fierce freezing blast of wind swept into the room.",
        "literal": "Door opened instant-at, fierce cold wind room-of inside-into blew.",
        "tokens": [
          {
            "word": "開けたとたんに",
            "meaning": "the very instant I opened",
            "reading": "あけたとたんに",
            "romaji": "aketa totan ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Sudden physical reaction upon opening door."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-1-4",
        "question": "疲れてベッドに横になった（　　）、あっという間に眠りに落ちてしまった。",
        "translation": "The moment I lay down on the bed from sheer exhaustion, I fell into a deep sleep in an instant.",
        "options": [
          "とたん",
          "最中",
          "ばかり",
          "一方"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-た + とたん (Instantaneous reaction)",
        "ruleHint": "Falling asleep the split-second head hits pillow.",
        "explanations": [
          {
            "text": "とたん",
            "isCorrect": true,
            "reason": "Correct! 横になったとたん expresses falling asleep instantaneous upon lying down."
          },
          {
            "text": "最中",
            "isCorrect": false,
            "reason": "Incorrect. 横になった最中 is ungrammatical (最中 requires ongoing action: 横になっている最中)."
          },
          {
            "text": "ばかり",
            "isCorrect": false,
            "reason": "Incorrect. 横になったばかり denotes recent completion, not instantaneous reaction."
          },
          {
            "text": "一方",
            "isCorrect": false,
            "reason": "Incorrect. 横になった一方 is meaningless here."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 1",
      "Time",
      "Instantaneous"
    ]
  },
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
      {
        "id": "s-skm2-2-3",
        "japanese": "医療技術の急速な進歩により、かつての難病も克服されつつある。",
        "english": "Owing to rapid advances in medical technology, formerly intractable illnesses are steadily being overcome.",
        "literal": "Medical technology rapid progress due-to, former intractable-illnesses overcome-being-underway.",
        "tokens": [
          {
            "word": "克服されつつある",
            "meaning": "is in the process of being overcome",
            "reading": "こくふくされつつある",
            "romaji": "kokufuku saretsutsu aru",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Formal scientific commentary on healthcare progression."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-2-3",
        "question": "地球温暖化の影響で、北極の氷が年々解け（　　）。",
        "translation": "Due to the impacts of global warming, the Arctic ice is steadily melting year by year.",
        "options": [
          "つつある",
          "つつあることだ",
          "つつあるまい",
          "つつあるべきだ"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-stem + つつある (Ongoing macro trend)",
        "ruleHint": "Observing continuous polar melting.",
        "explanations": [
          {
            "text": "つつある",
            "isCorrect": true,
            "reason": "Correct! 解けつつある describes the ongoing gradual environmental transformation."
          },
          {
            "text": "つつあることだ",
            "isCorrect": false,
            "reason": "Incorrect. つつあることだ is structurally incoherent."
          },
          {
            "text": "つつあるまい",
            "isCorrect": false,
            "reason": "Incorrect. つつあるまい is ungrammatical."
          },
          {
            "text": "つつあるべきだ",
            "isCorrect": false,
            "reason": "Incorrect. つつあるべきだ does not make sense here."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 2",
      "Aspect",
      "Macro Trend"
    ]
  },
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
      {
        "id": "s-skm2-3-1",
        "japanese": "一人暮らしを始めてはじめて、親が毎日家事をしてくれていたありがたさに気づいた。",
        "english": "Only after beginning to live alone did I truly realize the immense gratitude I owe my parents for doing chores daily.",
        "literal": "Living-alone started only-after, parents daily chores did gratitude realized.",
        "tokens": [
          {
            "word": "始めてはじめて",
            "meaning": "only after starting",
            "reading": "はじめてはじめて",
            "romaji": "hajimete hajimete",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Young adult coming of age realization."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-3-1",
        "question": "実際に海外で生活し（　　）はじめて、自国の文化の特徴を客観的に見直すことができた。",
        "translation": "Only after actually living abroad was I able to re-examine the characteristics of my own country's culture objectively.",
        "options": [
          "て",
          "たら",
          "ても",
          "つつ"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-て + はじめて (Epiphany through experience)",
        "ruleHint": "Gaining objective cultural self-awareness through international exposure.",
        "explanations": [
          {
            "text": "て",
            "isCorrect": true,
            "reason": "Correct! 生活してみてはじめて (or 生活してはじめて) forms 'only after living abroad'."
          },
          {
            "text": "たら",
            "isCorrect": false,
            "reason": "Incorrect. 生活したらはじめて is ungrammatical."
          },
          {
            "text": "ても",
            "isCorrect": false,
            "reason": "Incorrect. 生活してもはじめて is invalid."
          },
          {
            "text": "つつ",
            "isCorrect": false,
            "reason": "Incorrect. 生活しつつはじめて is grammatically impossible."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 3",
      "Sequence",
      "Realization"
    ]
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
      {
        "id": "s-skm2-3-2",
        "japanese": "契約書の内容をよくご確認いただいた上で、こちらにご署名をお願いいたします。",
        "english": "After having thoroughly verified the contents of the contract, please furnish your signature here.",
        "literal": "Contract-of contents well verify-receive after-upon, here signature please-do.",
        "tokens": [
          {
            "word": "ご確認いただいた上で",
            "meaning": "upon having verified",
            "reading": "ごかくにんいただいたうえで",
            "romaji": "gokakunin itadaita ue de",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Formal business contractual execution."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-3-2",
        "question": "担当者と詳しく話し合っ（　　）上で、今後のスケジュールを決定いたします。",
        "translation": "After discussing the details with the person in charge, we will determine our future schedule.",
        "options": [
          "た",
          "て",
          "る",
          "ても"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-た + 上で (Prerequisite step)",
        "ruleHint": "Strategic scheduling following bilateral discussions.",
        "explanations": [
          {
            "text": "た",
            "isCorrect": true,
            "reason": "Correct! V-た + 上で expresses 'after having held discussions'."
          },
          {
            "text": "て",
            "isCorrect": false,
            "reason": "Incorrect. 話し合って上で is ungrammatical (must be 話し合った上で)."
          },
          {
            "text": "る",
            "isCorrect": false,
            "reason": "Incorrect. 話し合う上で means 'in the process of discussing', which clashes with determining future schedule afterward."
          },
          {
            "text": "ても",
            "isCorrect": false,
            "reason": "Incorrect. 話し合っても上で is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 3",
      "Prerequisite",
      "Sequence"
    ]
  },
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
      {
        "id": "s-skm2-5-1",
        "japanese": "このアニメは日本国内のみならず、欧米やアジアのファンにも熱狂的に愛されている。",
        "english": "This anime is passionately loved not only within Japan, but also by fans across Europe, America, and Asia.",
        "literal": "This anime Japan domestic not-only, West and Asia fans-by-also enthusiastically loved-is.",
        "tokens": [
          {
            "word": "国内のみならず",
            "meaning": "not only domestically",
            "reading": "こくないのみならず",
            "romaji": "kokunai nominorazu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Describing global cultural resonance."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-5-1",
        "question": "彼は英語（　　）ならず、中国語とスペイン語も極めて流暢に操る。",
        "translation": "Not only English, he also commands Chinese and Spanish with extreme fluency.",
        "options": [
          "のみ",
          "だけ",
          "ばかり",
          "ほど"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + のみならず (Expansive scope)",
        "ruleHint": "Praising multilingual linguistic proficiency.",
        "explanations": [
          {
            "text": "のみ",
            "isCorrect": true,
            "reason": "Correct! 英語のみならず forms the classical 'not only X, but Y as well' collocation."
          },
          {
            "text": "だけ",
            "isCorrect": false,
            "reason": "Incorrect. 英語だけならず is ungrammatical (must be だけでなく)."
          },
          {
            "text": "ばかり",
            "isCorrect": false,
            "reason": "Incorrect. 英語ばかりならず is invalid (must be ばかりでなく)."
          },
          {
            "text": "ほど",
            "isCorrect": false,
            "reason": "Incorrect. 英語ほどならず does not exist."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 5",
      "Addition",
      "Formal Written"
    ]
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
      {
        "id": "s-skm2-5-2",
        "japanese": "彼は約束の時間に遅刻したばかりか、謝罪の一言さえ口にしなかった。",
        "english": "He not only showed up late for the promised time, but he didn't even utter a single word of apology.",
        "literal": "He promised-time late-was not-merely, apology single-word even mouth-to not-did.",
        "tokens": [
          {
            "word": "遅刻したばかりか",
            "meaning": "not merely late",
            "reading": "ちこくしたばかりか",
            "romaji": "chikoku shita bakari ka",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Indignation at unrepentant bad manners."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-5-2",
        "question": "彼女は親切に道を教えてくれた（　　）か、目的地まで一緒に案内してくれた。",
        "translation": "Not only did she kindly give me directions, she even guided me all the way to my destination.",
        "options": [
          "ばかり",
          "だけ",
          "ほど",
          "くらい"
        ],
        "correctIndex": 0,
        "grammarFocus": "普通形 + ばかりか (Unexpected escalation)",
        "ruleHint": "Recounting remarkable hospitality of a stranger.",
        "explanations": [
          {
            "text": "ばかり",
            "isCorrect": true,
            "reason": "Correct! 教えてくれたばかりか expresses unexpected escalation of generosity."
          },
          {
            "text": "だけ",
            "isCorrect": false,
            "reason": "Incorrect. 教えてくれただけか is a question ('only taught?')."
          },
          {
            "text": "ほど",
            "isCorrect": false,
            "reason": "Incorrect. 教えてくれたほどか is ungrammatical."
          },
          {
            "text": "くらい",
            "isCorrect": false,
            "reason": "Incorrect. 教えてくれたくらいか does not form this structure."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 5",
      "Escalation",
      "Surprise"
    ]
  },
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
      {
        "id": "s-skm2-6-1",
        "japanese": "AIの倫理的な利用に関する国際シンポジウムが、来月東京で開催される。",
        "english": "An international symposium concerning the ethical utilization of AI will be held in Tokyo next month.",
        "literal": "AI ethical usage concerning international-symposium, next-month Tokyo-in held-is.",
        "tokens": [
          {
            "word": "利用に関する",
            "meaning": "concerning the utilization",
            "reading": "りようにかんする",
            "romaji": "riyou ni kansuru",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "High-level academic conference announcement."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-6-1",
        "question": "環境問題（　　）関する新しい法案が、国会で可決された。",
        "translation": "A new legislative bill concerning environmental issues was passed by the Diet.",
        "options": [
          "に",
          "を",
          "へ",
          "で"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + に関する + Noun (Thematic modifier)",
        "ruleHint": "Legislative enactment on environmental affairs.",
        "explanations": [
          {
            "text": "に",
            "isCorrect": true,
            "reason": "Correct! Noun + に関する is the standard adnominal modifier."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. を関する is ungrammatical."
          },
          {
            "text": "へ",
            "isCorrect": false,
            "reason": "Incorrect. へ関する is invalid."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. で関する does not exist."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 6",
      "Topic",
      "Formal Prose"
    ]
  },
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
      {
        "id": "s-skm2-8-1",
        "japanese": "最新の科学的知見に基づいて、防災計画の抜本的な見直しが行われた。",
        "english": "A radical overhaul of the disaster prevention plan was carried out based upon the latest scientific insights.",
        "literal": "Latest scientific insights based-upon, disaster-prevention plan radical overhaul conducted.",
        "tokens": [
          {
            "word": "知見に基づいて",
            "meaning": "based on insights",
            "reading": "ちけんにもとづいて",
            "romaji": "chiken ni motozuite",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Policy revisions grounded on rigorous research."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-8-1",
        "question": "この小説は、歴史的な事実（　　）基づいて執筆された大作である。",
        "translation": "This novel is a monumental work authored based upon historical facts.",
        "options": [
          "に",
          "を",
          "で",
          "へ"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + に基づいて (Factual foundation)",
        "ruleHint": "Literary creation based on historical documentation.",
        "explanations": [
          {
            "text": "に",
            "isCorrect": true,
            "reason": "Correct! 事実に基づいて is the established formula for factual foundations."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. 事実を基づいて is ungrammatical."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. 事実で基づいて is invalid."
          },
          {
            "text": "へ",
            "isCorrect": false,
            "reason": "Incorrect. 事実へ基づいて is meaningless."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 8",
      "Foundation",
      "Evidence"
    ]
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
      {
        "id": "s-skm2-8-2",
        "japanese": "基本方針に沿って策定された計画に従い、着実に業務を推進してください。",
        "english": "Please steadily advance operations following the plan formulated in line with our fundamental policy.",
        "literal": "Basic-policy along formulated plan follow, steadily operations advance please.",
        "tokens": [
          {
            "word": "方針に沿って",
            "meaning": "in line with the policy",
            "reading": "ほうしんにそって",
            "romaji": "houshin ni sotte",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Managerial directive on operational fidelity."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-8-2",
        "question": "お客様のご要望（　　）沿った最適なプランをご提案させていただきます。",
        "translation": "We will humbly propose the optimal plan strictly tailored in line with our customer's requests.",
        "options": [
          "に",
          "を",
          "で",
          "へ"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + に沿った + Noun (Faithful alignment)",
        "ruleHint": "Tailoring a customized proposal to client specifications.",
        "explanations": [
          {
            "text": "に",
            "isCorrect": true,
            "reason": "Correct! ご要望に沿った (in line with customer requests) is standard commercial Japanese."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. ご要望を沿った is ungrammatical."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. ご要望で沿った is invalid."
          },
          {
            "text": "へ",
            "isCorrect": false,
            "reason": "Incorrect. ご要望へ沿った does not exist."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 8",
      "Guideline",
      "Alignment"
    ]
  },
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
      {
        "id": "s-skm2-10-1",
        "japanese": "前置きは抜きにして、早速本日のメインアジェンダに入りましょう。",
        "english": "Dispensing with preliminary pleasantries, let us dive straight into today's main agenda.",
        "literal": "Preamble dispensing-with, promptly today main-agenda enter let-us.",
        "tokens": [
          {
            "word": "前置きは抜きにして",
            "meaning": "dispensing with pleasantries",
            "reading": "まえおきはぬきにして",
            "romaji": "maeoki wa nuki ni shite",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Crisp, efficient chairperson opening a executive meeting."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-10-1",
        "question": "お世辞（　　）で、あなたの書いた論文は非常に独創的で素晴らしいです。",
        "translation": "Without a single shred of flattery, the thesis you have written is extraordinarily original and splendid.",
        "options": [
          "抜き",
          "切れ",
          "限り",
          "きり"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + 抜きで (Dispensing with pleasantries)",
        "ruleHint": "Giving sincere academic praise without polite exaggeration.",
        "explanations": [
          {
            "text": "抜き",
            "isCorrect": true,
            "reason": "Correct! お世辞抜きで is the idiomatic phrase for 'without flattery / speaking genuinely'."
          },
          {
            "text": "切れ",
            "isCorrect": false,
            "reason": "Incorrect. お世辞切れで is ungrammatical."
          },
          {
            "text": "限り",
            "isCorrect": false,
            "reason": "Incorrect. お世辞限りで is invalid."
          },
          {
            "text": "きり",
            "isCorrect": false,
            "reason": "Incorrect. お世辞きりで does not exist in this sense."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 10",
      "Omission",
      "Directness"
    ]
  },
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
      {
        "id": "s-skm2-12-1",
        "japanese": "喉が痛くて、ご飯を食べるどころか、水を一口飲むことさえできない。",
        "english": "My throat hurts so severely that far from eating meals, I cannot even swallow a single sip of water.",
        "literal": "Throat hurts, rice eating far-from, water single-sip drink even cannot.",
        "tokens": [
          {
            "word": "食べるどころか",
            "meaning": "far from eating",
            "reading": "たべるどころか",
            "romaji": "taberu dokoroka",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Exemplifying acute inflammation preventing basic sustenance."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-12-1",
        "question": "景気は回復する（　　）か、ますます悪化の一途をたどっている。",
        "translation": "Far from the economy recovering, it is steadily following a continuous path of further deterioration.",
        "options": [
          "どころ",
          "ばかり",
          "ばかりで",
          "だけ"
        ],
        "correctIndex": 0,
        "grammarFocus": "普通形 + どころか (Radical reversal)",
        "ruleHint": "Bleak economic appraisal debunking false optimism.",
        "explanations": [
          {
            "text": "どころ",
            "isCorrect": true,
            "reason": "Correct! 回復するどころか negates recovery to assert continuous deterioration."
          },
          {
            "text": "ばかり",
            "isCorrect": false,
            "reason": "Incorrect. 回復するばかりか means 'not only did it recover, but also...'."
          },
          {
            "text": "ばかりで",
            "isCorrect": false,
            "reason": "Incorrect. 回復するばかりでか is ungrammatical."
          },
          {
            "text": "だけ",
            "isCorrect": false,
            "reason": "Incorrect. 回復するだけか is a question."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 12",
      "Contrast",
      "Reversal"
    ]
  },
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
      {
        "id": "s-skm2-14-1",
        "japanese": "リモートワークは通勤のストレスを減らした一方で、社員間のコミュニケーション不足を生んだ。",
        "english": "While remote work reduced the stress of commuting, it simultaneously gave rise to a shortage of communication among staff.",
        "literal": "Remote-work commuting stress reduced while, staff-among communication shortage birthed.",
        "tokens": [
          {
            "word": "減らした一方で",
            "meaning": "while on one hand reducing",
            "reading": "へらしたいっぽうで",
            "romaji": "herashita ippou de",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Balanced workplace organizational analysis."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-14-1",
        "question": "観光客が急増して街が潤っている（　　）で、ゴミや騒音の問題が深刻化している。",
        "translation": "While the town is prospering from a boom in tourists, problems with litter and noise pollution are worsening.",
        "options": [
          "一方",
          "ばかり",
          "反面",
          "あまり"
        ],
        "correctIndex": 0,
        "grammarFocus": "普通形 + 一方で (Dual contrasting facets)",
        "ruleHint": "Assessing municipal trade-offs of mass tourism.",
        "explanations": [
          {
            "text": "一方",
            "isCorrect": true,
            "reason": "Correct! 潤っている一方で balances economic prosperity against municipal disruptions."
          },
          {
            "text": "ばかり",
            "isCorrect": false,
            "reason": "Incorrect. 潤っているばかりで means 'only prospering' without contrasting dual clauses."
          },
          {
            "text": "反面",
            "isCorrect": false,
            "reason": "Incorrect. 潤っている反面で is grammatically awkward (反面 does not take で)."
          },
          {
            "text": "あまり",
            "isCorrect": false,
            "reason": "Incorrect. 潤っているあまりで is ungrammatical."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 14",
      "Contrast",
      "Dual Facets"
    ]
  },
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
      {
        "id": "s-skm2-17-1",
        "japanese": "大病を患ったことを契機に、彼はそれまでの不健康な生活習慣を徹底的に改めた。",
        "english": "Taking his bout with serious illness as a life-changing catalyst, he thoroughly overhauled his previously unhealthy lifestyle habits.",
        "literal": "Serious-illness suffered that catalyst-as, he previous unhealthy lifestyle thoroughly reformed.",
        "tokens": [
          {
            "word": "ことを契機に",
            "meaning": "taking that as a catalyst",
            "reading": "ことをけいきに",
            "romaji": "koto o keiki ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Decisive personal health turnaround following a medical scare."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-17-1",
        "question": "オリンピック開催を（　　）に、都内のバリアフリー化が一気に加速した。",
        "translation": "Taking the hosting of the Olympic Games as a catalyst, barrier-free accessibility across the capital accelerated rapidly.",
        "options": [
          "契機",
          "原因",
          "目的",
          "次第"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + を契機に (Catalyst for transformation)",
        "ruleHint": "Urban transformation catalyzed by an international sporting event.",
        "explanations": [
          {
            "text": "契機",
            "isCorrect": true,
            "reason": "Correct! 開催を契機に highlights the Olympic Games as the prime catalyst for citywide architectural accessibility improvements."
          },
          {
            "text": "原因",
            "isCorrect": false,
            "reason": "Incorrect. 開催を原因に is unnatural syntax."
          },
          {
            "text": "目的",
            "isCorrect": false,
            "reason": "Incorrect. 開催を目的に means 'for the purpose of hosting'."
          },
          {
            "text": "次第",
            "isCorrect": false,
            "reason": "Incorrect. 開催を次第に is ungrammatical."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 17",
      "Catalyst",
      "Transformation"
    ]
  },
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
      {
        "id": "s-skm2-18-1",
        "japanese": "半年間寝る間も惜しんで準備しただけに、試験に合格した瞬間の喜びは格別だった。",
        "english": "Precisely because I had prepared for half a year without even sparing time for sleep, the joy the moment I passed the exam was truly extraordinary.",
        "literal": "Half-year sleeping-time begrudging prepared precisely-because, exam passed moment-of joy extraordinary was.",
        "tokens": [
          {
            "word": "準備しただけに",
            "meaning": "precisely because of having prepared",
            "reading": "じゅんびしただけに",
            "romaji": "junbi shita dake ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Euphoric sense of accomplishment following grueling dedication."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-18-1",
        "question": "ずっと楽しみにしていた旅行（　　）に、悪天候で中止になってショックが大きい。",
        "translation": "Precisely because it was a trip I had been looking forward to for so long, the shock of it being cancelled due to bad weather is enormous.",
        "options": [
          "だけ",
          "ばかり",
          "ほど",
          "くらい"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + だけに (Amplified emotional impact)",
        "ruleHint": "Heartbreaking disappointment magnified by long-held excitement.",
        "explanations": [
          {
            "text": "だけ",
            "isCorrect": true,
            "reason": "Correct! 旅行だっただけに (or 旅行だけに) amplifies the devastation precisely because anticipation had been so high."
          },
          {
            "text": "ばかり",
            "isCorrect": false,
            "reason": "Incorrect. 旅行ばかりに is ungrammatical."
          },
          {
            "text": "ほど",
            "isCorrect": false,
            "reason": "Incorrect. 旅行ほどに does not convey this amplified causal disappointment."
          },
          {
            "text": "くらい",
            "isCorrect": false,
            "reason": "Incorrect. 旅行くらいに does not fit."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 18",
      "Causality",
      "Amplification"
    ]
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
      {
        "id": "s-skm2-18-2",
        "japanese": "困難な状況にある今だからこそ、チーム全員が団結して支え合う必要がある。",
        "english": "It is precisely because we find ourselves in difficult circumstances right now that the entire team must unite and support one another.",
        "literal": "Difficult circumstances-in are now precisely-because, team all unite support-each-other need exists.",
        "tokens": [
          {
            "word": "今だからこそ",
            "meaning": "precisely because it is now",
            "reading": "いまだからこそ",
            "romaji": "ima da kara koso",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Rallying cry during an organizational crisis."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-18-2",
        "question": "お互いを深く信頼している（　　）こそ、本音で議論を戦わせることができる。",
        "translation": "It is precisely because we trust each other deeply that we can debate fiercely with raw candor.",
        "options": [
          "から",
          "ので",
          "ため",
          "なら"
        ],
        "correctIndex": 0,
        "grammarFocus": "理由 + からこそ (Emphatic singular justification)",
        "ruleHint": "Deep mutual trust enabling productive conflict.",
        "explanations": [
          {
            "text": "から",
            "isCorrect": true,
            "reason": "Correct! からこそ emphasizes the foundational bond of trust as the sole enabling reason for honest debate."
          },
          {
            "text": "ので",
            "isCorrect": false,
            "reason": "Incorrect. のでこそ is ungrammatical."
          },
          {
            "text": "ため",
            "isCorrect": false,
            "reason": "Incorrect. ためこそ does not exist."
          },
          {
            "text": "なら",
            "isCorrect": false,
            "reason": "Incorrect. ならこそ is archaic."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 18",
      "Causality",
      "Emphatic Justification"
    ]
  },
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
      {
        "id": "s-skm2-19-1",
        "japanese": "大学の日本語学科を卒業したものの、ビジネスの現場では思うように話せない。",
        "english": "Although I graduated from the university's Japanese department, in the actual business arena I cannot speak as fluently as I would like.",
        "literal": "University Japanese-department graduated although, business arena-in as-hoped cannot-speak.",
        "tokens": [
          {
            "word": "卒業したものの",
            "meaning": "although I graduated",
            "reading": "そつぎょうしたものの",
            "romaji": "sotsugyou shita mono no",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Humble realization of gap between academic credentials and real-world fluency."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-19-1",
        "question": "手術は無事に成功した（　　）の、完治するまでにはまだ数ヶ月のリハビリが必要だ。",
        "translation": "Although the surgery succeeded without complications, several months of rehabilitation are still required before full recovery.",
        "options": [
          "もの",
          "こと",
          "わけ",
          "ところ"
        ],
        "correctIndex": 0,
        "grammarFocus": "普通形 + ものの (Realistic concession)",
        "ruleHint": "Tempering surgical relief with realistic rehabilitation horizon.",
        "explanations": [
          {
            "text": "もの",
            "isCorrect": true,
            "reason": "Correct! 成功したものの concedes surgical success while presenting the arduous rehab ahead."
          },
          {
            "text": "こと",
            "isCorrect": false,
            "reason": "Incorrect. 成功したことの is ungrammatical in this conjunctive position."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. 成功したわけの is invalid."
          },
          {
            "text": "ところ",
            "isCorrect": false,
            "reason": "Incorrect. 成功したところの is archaic."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 19",
      "Concession",
      "Reality Check"
    ]
  },
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
      {
        "id": "s-skm2-20-2",
        "japanese": "何時間も激しく口論したあげく、二人は絶交してしまった。",
        "english": "After arguing fiercely for hours on end, the two of them ended up completely severing their friendship.",
        "literal": "Many-hours fiercely argued after-all, two-people friendship-severed completely.",
        "tokens": [
          {
            "word": "口論したあげく",
            "meaning": "after endless arguing",
            "reading": "こうろんしたあげく",
            "romaji": "kouron shita ageku",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Tragic, bitter fallout after prolonged squabbling."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-20-2",
        "question": "色々と思い悩んだ（　　）に、彼は会社を辞めて実家へ帰る道を選んだ。",
        "translation": "After agonizing endlessly over various options, he ultimately chose the path of resigning from his company and returning to his hometown.",
        "options": [
          "あげく",
          "末",
          "次第",
          "おかげ"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-た + あげくに (Weary negative culmination)",
        "ruleHint": "Exhausted departure after prolonged career angst.",
        "explanations": [
          {
            "text": "あげく",
            "isCorrect": true,
            "reason": "Correct! 思い悩んだあげくに captures prolonged psychological torment culminating in a weary resignation."
          },
          {
            "text": "末",
            "isCorrect": false,
            "reason": "Incorrect. 末に is possible for neutral outcomes, but あげくに specifically highlights agonizing fatigue leading to quitting."
          },
          {
            "text": "次第",
            "isCorrect": false,
            "reason": "Incorrect. 次第に means 'gradually'."
          },
          {
            "text": "おかげ",
            "isCorrect": false,
            "reason": "Incorrect. おかげに does not form this structure."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 20",
      "Culmination",
      "Regrettable Result"
    ]
  },
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
      {
        "id": "s-skm2-21-2",
        "japanese": "夜遅くまで部屋の明かりがついている。山田さんはまだ残業しているに違いない。",
        "english": "The lights in the office room are on late into the night. Yamada-san must undoubtedly still be working overtime.",
        "literal": "Night late room lights on-are. Yamada-san still overtime-doing must-be.",
        "tokens": [
          {
            "word": "残業しているに違いない",
            "meaning": "must undoubtedly be working overtime",
            "reading": "ざんぎょうしているにちがいない",
            "romaji": "zangyou shite iru ni chigai nai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Firm deduction from observable nighttime lighting."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-21-2",
        "question": "これほど緻密に作られた偽札は、専門家の手によるものに（　　）。",
        "translation": "Counterfeit bills crafted with this level of meticulous precision must undoubtedly be the work of an expert.",
        "options": [
          "相違ない",
          "限りない",
          "過言ではない",
          "他ならない"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + に相違ない (Solemn deductive certainty)",
        "ruleHint": "Forensic investigator concluding counterfeit currency origin.",
        "explanations": [
          {
            "text": "相違ない",
            "isCorrect": true,
            "reason": "Correct! 専門家の手によるものに相違ない expresses authoritative certainty in formal prose."
          },
          {
            "text": "限りない",
            "isCorrect": false,
            "reason": "Incorrect. 限りない means 'boundless'."
          },
          {
            "text": "過言ではない",
            "isCorrect": false,
            "reason": "Incorrect. 過言ではない means 'it is no exaggeration to say'."
          },
          {
            "text": "他ならない",
            "isCorrect": false,
            "reason": "Incorrect. 他ならない takes からに他ならない (nothing other than because)."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 21",
      "Assertion",
      "Certainty"
    ]
  },
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
      {
        "id": "s-skm2-22-2",
        "japanese": "このような杜撰な管理を続けていれば、顧客データの流出を招きかねない。",
        "english": "If we continue such careless management, we could very well trigger a catastrophic leak of customer data.",
        "literal": "This-kind-of careless management continue-if, customer-data leak invite-could-well.",
        "tokens": [
          {
            "word": "招きかねない",
            "meaning": "could well invite disaster",
            "reading": "まねきかねない",
            "romaji": "manekikanenai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Urgent cybersecurity compliance audit warning."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-22-2",
        "question": "そんな乱暴な運転をしていたら、いつか人を（　　）かねませんよ。",
        "translation": "If you keep driving recklessly like that, you are liable to run someone over one day.",
        "options": [
          "はね",
          "はねる",
          "はねた",
          "はねて"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-stem + かねない (Severe adverse hazard)",
        "ruleHint": "Warning a reckless motorist of fatal collision risk.",
        "explanations": [
          {
            "text": "はね",
            "isCorrect": true,
            "reason": "Correct! Verb-stem はね + かねません warns of the imminent risk of hitting a pedestrian."
          },
          {
            "text": "はねる",
            "isCorrect": false,
            "reason": "Incorrect. はねるかねません is ungrammatical (must use masu-stem, not dictionary form)."
          },
          {
            "text": "はねた",
            "isCorrect": false,
            "reason": "Incorrect. はねたかねません is invalid."
          },
          {
            "text": "はねて",
            "isCorrect": false,
            "reason": "Incorrect. はねてかねません does not exist."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 22",
      "Risk",
      "Adverse Warning"
    ]
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
      {
        "id": "s-skm2-22-3",
        "japanese": "お客様の個人的な事情に関しましては、弊社としては関与いたしかねます。",
        "english": "Concerning personal matters of our customers, our company is regretfully in no position to intervene.",
        "literal": "Customer personal circumstances concerning, our-company-as intervene cannot-regretfully.",
        "tokens": [
          {
            "word": "関与いたしかねます",
            "meaning": "are regretfully unable to intervene",
            "reading": "かんよいたしかねます",
            "romaji": "kanyo itashikanemasu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Formal commercial disclaimer of third-party involvement."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-22-3",
        "question": "提示された条件はあまりに不公平であり、その契約には同意（　　）ます。",
        "translation": "The proposed conditions are excessively inequitable, and I find it impossible to agree to that contract.",
        "options": [
          "しかね",
          "しかねない",
          "し得",
          "しそうにあり"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-stem + かねる (Principled polite refusal)",
        "ruleHint": "Rejecting an exploitative contractual clause.",
        "explanations": [
          {
            "text": "しかね",
            "isCorrect": true,
            "reason": "Correct! 同意しかねます expresses principled, polite refusal to consent to unfair terms."
          },
          {
            "text": "しかねない",
            "isCorrect": false,
            "reason": "Incorrect. 同意しかねないます is ungrammatical nonsense."
          },
          {
            "text": "し得",
            "isCorrect": false,
            "reason": "Incorrect. 同意し得ます means 'can possibly agree' (opposite meaning)."
          },
          {
            "text": "しそうにあり",
            "isCorrect": false,
            "reason": "Incorrect. 同意しそうにあります is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 22",
      "Polite Refusal",
      "Formal"
    ]
  },
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
      {
        "id": "s-skm2-24-1",
        "japanese": "健康を維持したいなら、暴飲暴食を慎み、規則正しい生活を送ることだ。",
        "english": "If you wish to maintain your health, the best thing to do is refrain from binge eating and drinking, and lead a regulated lifestyle.",
        "literal": "Health maintain want-if, binge-eating-drinking refrain, regulated life send thing-is.",
        "tokens": [
          {
            "word": "送ることだ",
            "meaning": "the thing to do is to lead",
            "reading": "おくることだ",
            "romaji": "okuru koto da",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Sage wellness advice on lifestyle discipline."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-24-1",
        "question": "試験で実力を発揮したければ、前日は夜更かしをせ（　　）早く休むことだ。",
        "translation": "If you want to perform to your full ability in the exam, you should not stay up late the night before and instead rest early.",
        "options": [
          "ずに",
          "ないで",
          "ぬで",
          "ず"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-る + ことだ (Practical wisdom advice)",
        "ruleHint": "Pre-exam rest and performance optimization advice.",
        "explanations": [
          {
            "text": "ずに",
            "isCorrect": true,
            "reason": "Correct! 夜更かしをせずに早く休むことだ correctly pairs the negative modifier with the advice pattern ことだ."
          },
          {
            "text": "ないで",
            "isCorrect": false,
            "reason": "Incorrect. せないで is ungrammatical (must be しないで)."
          },
          {
            "text": "ぬで",
            "isCorrect": false,
            "reason": "Incorrect. せぬで is invalid."
          },
          {
            "text": "ず",
            "isCorrect": false,
            "reason": "Incorrect. せず早く休むことだ is possible, but せずに is the standard smooth adverbial clause."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 24",
      "Advice",
      "Admonition"
    ]
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
      {
        "id": "s-skm2-24-2",
        "japanese": "台風で全便が欠航となったため、旅行の予定を延期せざるを得なかった。",
        "english": "Because all flights were cancelled due to the typhoon, we had no choice but to postpone our travel schedule.",
        "literal": "Typhoon-by all-flights cancelled became because, travel-of schedule postpone compelled-was.",
        "tokens": [
          {
            "word": "延期せざるを得なかった",
            "meaning": "had no choice but to postpone",
            "reading": "えんきせざるをえなかった",
            "romaji": "enki sezaru o enakatta",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Reluctant acceptance of uncontrollable force majeure."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-24-2",
        "question": "会社の業績が著しく悪化したため、不採算部門の閉鎖を決断（　　）ざるを得ない。",
        "translation": "Because the company's financial performance deteriorated drastically, management is compelled to decide on closing unprofitable divisions.",
        "options": [
          "せ",
          "し",
          "さ",
          "す"
        ],
        "correctIndex": 0,
        "grammarFocus": "する → せざるを得ない (Compelled reluctant action)",
        "ruleHint": "Executive restructuring compelled by severe losses.",
        "explanations": [
          {
            "text": "せ",
            "isCorrect": true,
            "reason": "Correct! する becomes せざるを得ない (irregular suru conjugation)."
          },
          {
            "text": "し",
            "isCorrect": false,
            "reason": "Incorrect. しざるを得ない is a classic learner trap (ungrammatical!)."
          },
          {
            "text": "さ",
            "isCorrect": false,
            "reason": "Incorrect. さざるを得ない does not exist."
          },
          {
            "text": "す",
            "isCorrect": false,
            "reason": "Incorrect. すざるを得ない is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 24",
      "Compulsion",
      "No Choice"
    ]
  },
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
      {
        "id": "s-skm2-25-3",
        "japanese": "一人で海外に留学している娘の安否が、心配でたまらない。",
        "english": "I am worried sick about the safety and well-being of my daughter studying abroad all on her own.",
        "literal": "Alone overseas studying daughter-of safety, worried-sick intolerably.",
        "tokens": [
          {
            "word": "心配でたまらない",
            "meaning": "worried sick / unbearably anxious",
            "reading": "しんぱいでたまらない",
            "romaji": "shinpai de tamaranai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Parental visceral concern for a distant child."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-25-3",
        "question": "徹夜でレポートを書き上げて、今は眠くて（　　）。",
        "translation": "Having finished writing the report overnight without sleep, I am dying of sleepiness right now.",
        "options": [
          "たまらない",
          "ならない",
          "いられない",
          "やまない"
        ],
        "correctIndex": 0,
        "grammarFocus": "い-adj-くて + たまらない (Unbearable physical state)",
        "ruleHint": "Overwhelming exhaustion after an all-nighter.",
        "explanations": [
          {
            "text": "たまらない",
            "isCorrect": true,
            "reason": "Correct! 眠くてたまらない expresses visceral, unbearable physiological fatigue."
          },
          {
            "text": "ならない",
            "isCorrect": false,
            "reason": "Incorrect. 眠くてならない is unnatural (ならない is for spontaneous mental states like 思えてならない)."
          },
          {
            "text": "いられない",
            "isCorrect": false,
            "reason": "Incorrect. 眠くていられない is ungrammatical."
          },
          {
            "text": "やまない",
            "isCorrect": false,
            "reason": "Incorrect. 眠くてやまない is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 25",
      "Sensation",
      "Visceral Intensity"
    ]
  },
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
      {
        "id": "s-skm2-26-1",
        "japanese": "多忙な時期にもかかわらず、貴重なお時間を割いていただき心より御礼申し上げます。",
        "english": "Despite it being a hectic period, I express my heartfelt thanks for you generously taking your precious time for us.",
        "literal": "Hectic period despite, precious time sparing-receive-humbly heart-from thanks express.",
        "tokens": [
          {
            "word": "割いていただき",
            "meaning": "humbly receiving your sparing of time",
            "reading": "さいていただき",
            "romaji": "saite itadaki",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Formal business correspondence expressing profound appreciation."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-26-1",
        "question": "こちらの企画書につきまして、ご意見を（　　）いただけますでしょうか。",
        "translation": "Concerning this proposal, could we possibly have you share your valuable opinions?",
        "options": [
          "お聞かせ",
          "ご案内",
          "拝見",
          "申し上げて"
        ],
        "correctIndex": 0,
        "grammarFocus": "お + stem + いただく (Deferential client request)",
        "ruleHint": "Soliciting client feedback on a corporate proposal.",
        "explanations": [
          {
            "text": "お聞かせ",
            "isCorrect": true,
            "reason": "Correct! お聞かせいただけますでしょうか politely requests the client to let us hear their thoughts."
          },
          {
            "text": "ご案内",
            "isCorrect": false,
            "reason": "Incorrect. ご案内いただけますでしょうか means 'could you guide us'."
          },
          {
            "text": "拝見",
            "isCorrect": false,
            "reason": "Incorrect. 拝見 is humble for speaker's own viewing."
          },
          {
            "text": "申し上げて",
            "isCorrect": false,
            "reason": "Incorrect. 申し上げていただけますでしょうか is ungrammatical."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Ch 26",
      "Keigo",
      "Business Benefactive"
    ]
  },
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
      {
        "id": "s-skm2-p2-1",
        "japanese": "プロの選手相手に、初心者の私たちが勝ちっこないよ。",
        "english": "There's no way in hell we beginners could ever defeat professional athletes!",
        "literal": "Pro athletes opponent-as, beginner us win-no-way.",
        "tokens": [
          {
            "word": "勝ちっこない",
            "meaning": "no way we could win",
            "reading": "かちっこない",
            "romaji": "kachikkonai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Blunt colloquial dismissal of an unrealistic match outcome."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-p2-1",
        "question": "地図も持たずに初めての山に入ったら、道に迷い（　　）よ。",
        "translation": "If you enter an unfamiliar mountain without even a map, you are bound to get lost!",
        "options": [
          "っこない",
          "かねない",
          "きりない",
          "がちない"
        ],
        "correctIndex": 1,
        "grammarFocus": "Trap Check: っこない (Zero chance) vs かねない (Danger of happening)",
        "ruleHint": "Distinguishing impossible outcomes from dangerous risks.",
        "explanations": [
          {
            "text": "っこない",
            "isCorrect": false,
            "reason": "Incorrect. 迷いっこない would mean 'there is no way you could get lost', which is false."
          },
          {
            "text": "かねない",
            "isCorrect": true,
            "reason": "Correct! 迷いかねない warns of the very real danger: 'you are liable to get lost'. Note: For っこない, a sentence would be: 道が分かりっこない (No way you could know the path!)."
          },
          {
            "text": "きりない",
            "isCorrect": false,
            "reason": "Incorrect. きりない does not attach to verb stems."
          },
          {
            "text": "がちない",
            "isCorrect": false,
            "reason": "Incorrect. がちない is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Part 2",
      "Colloquial Impossibility",
      "Form A"
    ]
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
      {
        "id": "s-skm2-p2-2",
        "japanese": "あんな不愉快な思いをするくらいなら、あの店には二度と行くまい。",
        "english": "If I have to endure such an unpleasant experience, I vow never to set foot in that shop ever again.",
        "literal": "That unpleasant experience suffer rather-than, that shop-to twice go-never-will.",
        "tokens": [
          {
            "word": "行くまい",
            "meaning": "vow never to go",
            "reading": "いくまい",
            "romaji": "ikumai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Steadfast personal vow after terrible customer service."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-p2-2",
        "question": "どんな困難があろうとも、途中で決して諦め（　　）と心に誓った。",
        "translation": "No matter what hardships may arise, I swore in my heart never to give up halfway.",
        "options": [
          "まい",
          "ない",
          "ず",
          "ぬ"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-stem + まい (Steadfast negative determination)",
        "ruleHint": "Unshakable vow to persevere through adversity.",
        "explanations": [
          {
            "text": "まい",
            "isCorrect": true,
            "reason": "Correct! 諦めまいと心に誓った conveys resolute negative determination ('vowed never to give up')."
          },
          {
            "text": "ない",
            "isCorrect": false,
            "reason": "Incorrect. 諦めないと心に誓った is everyday plain, whereas まい reflects the solemn written resolve of JLPT N2."
          },
          {
            "text": "ず",
            "isCorrect": false,
            "reason": "Incorrect. 諦めずと is ungrammatical."
          },
          {
            "text": "ぬ",
            "isCorrect": false,
            "reason": "Incorrect. 諦めぬと is archaic/classical."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Part 2",
      "Negative Will",
      "Form B"
    ]
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
      {
        "id": "s-skm2-p2-3",
        "japanese": "患者の秘密を外部に漏らすなど、医師としてあるまじき背信行為だ。",
        "english": "Leaking a patient's confidential records to outsiders is a treacherous betrayal utterly impermissible for a physician.",
        "literal": "Patient secret outside-to leak like, doctor-as exist-impermissible betrayal is.",
        "tokens": [
          {
            "word": "あるまじき背信行為",
            "meaning": "impermissible act of betrayal",
            "reading": "あるまじきはいしんこうい",
            "romaji": "arumajiki haishinkoui",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Stern denunciation of medical malpractice and ethical breach."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-p2-3",
        "question": "公金を私的に流用するなど、政治家としてある（　　）不正行為である。",
        "translation": "Embezzling public funds for private use is an illicit act utterly unbecoming and impermissible for a politician.",
        "options": [
          "まじき",
          "べき",
          "はずの",
          "限りの"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-る + まじき + Noun (Severe ethical violation)",
        "ruleHint": "Condemning political embezzlement.",
        "explanations": [
          {
            "text": "まじき",
            "isCorrect": true,
            "reason": "Correct! あるまじき captures the moral prohibition against corruption in public office."
          },
          {
            "text": "べき",
            "isCorrect": false,
            "reason": "Incorrect. あるべき不正行為 is contradictory ('illicit act that ought to exist'!)."
          },
          {
            "text": "はずの",
            "isCorrect": false,
            "reason": "Incorrect. あるはずの不正行為 implies expected corruption."
          },
          {
            "text": "限りの",
            "isCorrect": false,
            "reason": "Incorrect. ある限りの means 'as much as exists'."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Part 2",
      "Archaic Moral Ban",
      "Form D"
    ]
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
      {
        "id": "s-skm2-p2-4",
        "japanese": "危険につき、関係者以外この工事現場に立ち入るべからず。",
        "english": "Due to extreme danger: unauthorized personnel must not enter this construction site under any circumstances.",
        "literal": "Danger due-to, related-personnel besides this construction-site enter must-not.",
        "tokens": [
          {
            "word": "立ち入るべからず",
            "meaning": "must not enter",
            "reading": "たちいるべからず",
            "romaji": "tachiiru bekarazu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Authoritative warning notice posted at a hazardous construction perimeter."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-p2-4",
        "question": "壁に「ここにゴミを捨てる（　　）」という看板が立てられている。",
        "translation": "A public signboard reading 'Do not dump garbage here' has been erected on the wall.",
        "options": [
          "べからず",
          "まい",
          "ざるを得ない",
          "かねない"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-る + べからず (Authoritative public prohibition)",
        "ruleHint": "Official placard prohibiting littering.",
        "explanations": [
          {
            "text": "べからず",
            "isCorrect": true,
            "reason": "Correct! 捨てるべからず is the classical authoritative sign prohibition against illegal dumping."
          },
          {
            "text": "まい",
            "isCorrect": false,
            "reason": "Incorrect. 捨てるまい is speaker's personal intention ('I will not dump')."
          },
          {
            "text": "ざるを得ない",
            "isCorrect": false,
            "reason": "Incorrect. 捨てるざるを得ない is ungrammatical."
          },
          {
            "text": "かねない",
            "isCorrect": false,
            "reason": "Incorrect. 捨てるかねない is grammatically invalid."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Part 2",
      "Public Prohibition",
      "Form E"
    ]
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
      {
        "id": "s-skm2-p2-5",
        "japanese": "毎日猛練習を重ねた甲斐があって、ついに全国大会で優勝を勝ち取ることができた。",
        "english": "It was thoroughly worth having practiced relentlessly every single day, as we finally succeeded in seizing victory at the national tournament.",
        "literal": "Every-day fierce-practice repeated worth-existing, finally national-tournament victory seize could.",
        "tokens": [
          {
            "word": "練習を重ねた甲斐があって",
            "meaning": "worth having practiced relentlessly",
            "reading": "れんしゅうをかさねたかいがあって",
            "romaji": "renshuu o kasaneta kai ga atte",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Jubilant athletic triumph crowning grueling preparation."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-p2-5",
        "question": "医師団による懸命な救命活動の甲斐も（　　）、患者は息を引き取った。",
        "translation": "Despite the desperate life-saving efforts by the medical team, tragically all was in vain, and the patient passed away.",
        "options": [
          "なく",
          "あって",
          "あり",
          "なしに"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + の甲斐もなく (Heartbreaking futility)",
        "ruleHint": "Mourning a patient whose life could not be saved despite heroic efforts.",
        "explanations": [
          {
            "text": "なく",
            "isCorrect": true,
            "reason": "Correct! 甲斐もなく (all in vain) is required because the tragic death is a heartbreaking failure despite best efforts."
          },
          {
            "text": "あって",
            "isCorrect": false,
            "reason": "Incorrect. 甲斐もあって indicates success (contrasting with the patient's passing)."
          },
          {
            "text": "あり",
            "isCorrect": false,
            "reason": "Incorrect. 甲斐もあり is ungrammatical with tragic results."
          },
          {
            "text": "なしに",
            "isCorrect": false,
            "reason": "Incorrect. 甲斐もなしに is unidiomatic."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Part 2",
      "Effort & Fruition",
      "Form F"
    ]
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
      {
        "id": "s-skm2-p2-6",
        "japanese": "この困難な国際紛争を調停できる人物は、百戦錬磨の彼をおいてほかにいない。",
        "english": "The person capable of mediating this grueling international conflict is none other than him with his battle-tested diplomatic experience.",
        "literal": "This difficult international-conflict mediate can person, battle-tested him setting-aside besides none.",
        "tokens": [
          {
            "word": "彼をおいてほかにいない",
            "meaning": "none other than him",
            "reading": "かれをおいてほかにいない",
            "romaji": "kare o oite hoka ni inai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "High tribute to diplomatic crisis leadership."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-p2-6",
        "question": "次期リーダーとしてチームをまとめられるのは、人望の厚い鈴木さん（　　）おいて他にいない。",
        "translation": "As the next leader capable of uniting the team, there is none other than the deeply trusted Suzuki-san.",
        "options": [
          "を",
          "に",
          "で",
          "へ"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + をおいて他にいない (Unrivaled supreme candidate)",
        "ruleHint": "Endorsing a trusted leader for executive captaincy.",
        "explanations": [
          {
            "text": "を",
            "isCorrect": true,
            "reason": "Correct! 鈴木さんをおいて他にいない expresses that Suzuki-san is uniquely qualified."
          },
          {
            "text": "に",
            "isCorrect": false,
            "reason": "Incorrect. 鈴木さんにおして is invalid."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. 鈴木さんでおいて does not exist."
          },
          {
            "text": "へ",
            "isCorrect": false,
            "reason": "Incorrect. 鈴木さんへおいて is ungrammatical."
          }
        ]
      }
    ],
    "tags": [
      "N2",
      "SKM Part 2",
      "Unrivaled Supremacy",
      "Form G"
    ]
  }
];
