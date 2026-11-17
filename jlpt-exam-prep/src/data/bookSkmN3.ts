import type { GrammarPoint } from '../types';

export const BOOK_SKM_N3_POINTS: GrammarPoint[] = [
  {
    "id": "skm3-u1-uchini-while",
    "title": "〜うちに (While State Lasts / Before Opportunity Slips)",
    "meaning": "While a favorable situation or continuous condition persists, take action before the window of opportunity closes.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 1: 時・進行 (Time & Progress)",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-辞書形 / V-ている / V-ない + うちに | い-adj + うちに | な-adj + な + うちに | Noun + の + うちに",
    "nuance": "TIME SENSITIVITY: If you don't act now, it will become impossible later: スープが熱いうちに (before it gets cold), 日本にいるうちに (before leaving Japan).",
    "keyTakeaway": "MUG-UP: V-ない + うちに = 'Before it becomes...' (暗くならないうちに = Before it gets dark).",
    "sentences": [
      {
        "id": "s-skm3-1-1",
        "japanese": "温かいうちに、どうぞ召し上がってください。",
        "english": "Please go ahead and enjoy the food while it is still warm.",
        "literal": "Warm while, please eat.",
        "tokens": [
          {
            "word": "温かいうちに",
            "meaning": "while it is warm",
            "reading": "あたたかいうちに",
            "romaji": "atatakai uchi ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "い-adjective connects directly to うちに."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-1-1",
        "question": "雨が（　　）うちに、急いで洗濯物を取り込みましょう。",
        "translation": "Let's hurry and bring in the laundry before it starts raining.",
        "options": [
          "降らない",
          "降った",
          "降る",
          "降らなくて"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-ない + うちに (Before...)",
        "ruleHint": "Taking action before laundry gets wet.",
        "explanations": [
          {
            "text": "降らない",
            "isCorrect": true,
            "reason": "Correct! 降らないうちに means 'before it rains / while it is not raining'."
          },
          {
            "text": "降った",
            "isCorrect": false,
            "reason": "Incorrect. 降ったうちに is invalid (past tense cannot combine with うちに)."
          },
          {
            "text": "降る",
            "isCorrect": false,
            "reason": "Incorrect. 降るうちに implies while it is actively raining."
          },
          {
            "text": "降らなくて",
            "isCorrect": false,
            "reason": "Incorrect. 降らなくて cannot directly attach to うちに."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 1",
      "Time Limit",
      "Opportunity"
    ]
  },
  {
    "id": "skm3-u1-uchini-change",
    "title": "〜うちに (Unnoticed Natural Evolution: While Doing X, Y Emerged)",
    "meaning": "While continuing action X over time, an uncalculated natural change or realization Y developed unnoticed.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 1: 時・進行 (Time & Progress)",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-ている / V-辞書形 + うちに",
    "nuance": "NO CONSCIOUS INTENT: Clause B is NOT a planned decision; it is a spontaneous change that crept up silently (e.g. while reading I fell asleep; as we talked we grew fond of each other).",
    "keyTakeaway": "MUG-UP: V-ている + うちに = Inadvertently happened without realizing it!",
    "sentences": [
      {
        "id": "s-skm3-1-2",
        "japanese": "本を読んでいるうちに、いつの間にか眠ってしまった。",
        "english": "While I was reading a book, before I knew it, I fell fast asleep.",
        "literal": "Book reading was while, unnoticed slept-ended-up.",
        "tokens": [
          {
            "word": "読んでいるうちに",
            "meaning": "while reading",
            "reading": "よんでいるうちに",
            "romaji": "yonde iru uchi ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Spontaneous transition into sleep."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-1-2",
        "question": "何度も練習を重ねて（　　）うちに、自然と上手に話せるようになった。",
        "translation": "While repeating practice over and over, I naturally became able to speak skillfully.",
        "options": [
          "いる",
          "ある",
          "おく",
          "みる"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-ている + うちに gradual evolution",
        "ruleHint": "Fluency developing naturally over practice.",
        "explanations": [
          {
            "text": "いる",
            "isCorrect": true,
            "reason": "Correct! 重ねているうちに marks the gradual, unforced emergence of fluency over continuous practice."
          },
          {
            "text": "ある",
            "isCorrect": false,
            "reason": "Incorrect. ある is for resultant state of inanimate objects."
          },
          {
            "text": "おく",
            "isCorrect": false,
            "reason": "Incorrect. おく is advance preparation."
          },
          {
            "text": "みる",
            "isCorrect": false,
            "reason": "Incorrect. みる is trial action."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 1",
      "Natural Change",
      "Evolution"
    ]
  },
  {
    "id": "skm3-u1-aida-vs-aidani",
    "title": "〜間 vs 〜間に (Continuous Duration vs Momentary Action)",
    "meaning": "〜間 (Action in B continues through 100% of duration A). 〜間に (Discrete action in B happens at some specific point during interval A).",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 1: 時・進行 (Time & Progress)",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-ている / Noun + の + 間 (Throughout) vs 間に (Single point)",
    "nuance": "DURATION VS POINT: '夏休みの間、毎日泳いだ' (Swam every day the whole vacation). '夏休みの間に、免許を取った' (Acquired license at a moment during vacation).",
    "keyTakeaway": "MUG-UP: 間 = Whole time. 間に = At a moment within the interval.",
    "sentences": [
      {
        "id": "s-skm3-1-3",
        "japanese": "両親が旅行している間、ずっと一人で留守番をしていた。",
        "english": "Throughout the entire time my parents were traveling, I looked after the house alone.",
        "literal": "Parents traveling while, throughout alone home-tending did.",
        "tokens": [
          {
            "word": "旅行している間",
            "meaning": "throughout the entire time they traveled",
            "reading": "りょこうしているあいだ",
            "romaji": "ryokou shite iru aida",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Continuous house-sitting for the entire vacation interval."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-1-3",
        "question": "お風呂に入っている（　　）、宅急便の配達員がベルを鳴らした。",
        "translation": "While I was taking a bath, the courier delivery person rang the doorbell.",
        "options": [
          "間に",
          "間",
          "うちに",
          "最中に"
        ],
        "correctIndex": 0,
        "grammarFocus": "〜間に (Momentary event during interval)",
        "ruleHint": "Doorbell ringing during bath.",
        "explanations": [
          {
            "text": "間に",
            "isCorrect": true,
            "reason": "Correct! Ringing the doorbell was a momentary event occurring at a point in the bath window, requiring 間に."
          },
          {
            "text": "間",
            "isCorrect": false,
            "reason": "Incorrect. 間 would mean the courier rang the bell non-stop for the entire 30 minutes of the bath!"
          },
          {
            "text": "うちに",
            "isCorrect": false,
            "reason": "Incorrect. うちに implies urgency to avoid a negative change."
          },
          {
            "text": "最中に",
            "isCorrect": false,
            "reason": "Incorrect. 最中に emphasizes physical interruption, but 間に is the standard temporal boundary contrast."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 1",
      "Duration",
      "Time Boundaries"
    ]
  },
  {
    "id": "skm3-u1-te-kara-denaito",
    "title": "〜てからでないと / 〜てからでなければ (Not Until / Only After Prerequisite Is Done)",
    "meaning": "Action Y is completely impossible until prerequisite action X has been thoroughly fulfilled: 'Unless you do X first, Y cannot be done'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 1: 時・進行 (Time & Progress)",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-て + からでないと / からでなければ + Negative / Impossible Predicate",
    "nuance": "MANDATORY NEGATIVE CONCEQUENCE: Clause B ALWAYS expresses inability, refusal, or impossibility (できません, 決められません, 分かりません).",
    "keyTakeaway": "MUG-UP: V-て + からでないと + [Negative] = Cannot do Y until X is completed first!",
    "sentences": [
      {
        "id": "s-skm3-1-4",
        "japanese": "上司と相談してからでないと、この場でお返事はできません。",
        "english": "Unless I consult with my supervisor first, I cannot give you an answer on the spot.",
        "literal": "Supervisor-with consult-after-only, this place-at reply cannot.",
        "tokens": [
          {
            "word": "相談してからでないと",
            "meaning": "not until consulting",
            "reading": "そうだんしてからでないと",
            "romaji": "soudan shite kara de nai to",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Business prerequisite for answer."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-1-4",
        "question": "詳しい契約内容を（　　）からでないと、サインすることはできません。",
        "translation": "Unless I read the detailed contract terms first, I cannot sign it.",
        "options": [
          "読んで",
          "読む",
          "読んだ",
          "読まない"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-て + からでないと prerequisite",
        "ruleHint": "Refusing signature before review.",
        "explanations": [
          {
            "text": "読んで",
            "isCorrect": true,
            "reason": "Correct! 読む connects via te-form 読んで + からでないと."
          },
          {
            "text": "読む",
            "isCorrect": false,
            "reason": "Incorrect. 読む is dictionary form."
          },
          {
            "text": "読んだ",
            "isCorrect": false,
            "reason": "Incorrect. 読んだ is past form."
          },
          {
            "text": "読まない",
            "isCorrect": false,
            "reason": "Incorrect. 読まない is negative form."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 1",
      "Prerequisite",
      "Time"
    ]
  },
  {
    "id": "skm3-u1-tokoro-da-phases",
    "title": "〜ところだ (Temporal Phase: Imminent, In the Midst, or Just Finished)",
    "meaning": "Pinpoints the exact temporal boundary: 1) Just about to start (辞書形). 2) In the thick of doing (ている). 3) Just completed moments ago (た形).",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 1: 時・進行 (Time & Progress)",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-辞書形 + ところだ (Inception) | V-ている + ところだ (Midst) | V-た + ところだ (Conclusion)",
    "nuance": "PHASE CLUES: '今から出かけるところだ' (I'm putting on my shoes). '今調べているところだ' (Browsing right now). '今帰ったところだ' (Just stepped through the door).",
    "keyTakeaway": "MUG-UP: V-るところ (About to) -> V-ているところ (Right now) -> V-たところ (Just finished right now!).",
    "sentences": [
      {
        "id": "s-skm3-1-5",
        "japanese": "今から家を出るところですから、三十分後には着くと思います。",
        "english": "I am just about to leave the house right now, so I think I'll arrive in about 30 minutes.",
        "literal": "Now house leave-about-to, 30-mins-after arrive think.",
        "tokens": [
          {
            "word": "出るところですから",
            "meaning": "just about to leave, so",
            "reading": "でるところですから",
            "romaji": "deru tokoro desu kara",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "V-辞書形 + ところ indicates imminent departure."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-1-5",
        "question": "ちょうど今、昼ご飯を食べ（　　）ところだから、お腹がいっぱいです。",
        "translation": "I just finished eating lunch right now, so I am completely full.",
        "options": [
          "終わった",
          "終わる",
          "終わっている",
          "終われ"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-た + ところだ (Just finished)",
        "ruleHint": "Explaining fullness after immediate completion.",
        "explanations": [
          {
            "text": "終わった",
            "isCorrect": true,
            "reason": "Correct! V-た + ところだ indicates an action that concluded moments ago."
          },
          {
            "text": "終わる",
            "isCorrect": false,
            "reason": "Incorrect. 終わるところ implies about to finish."
          },
          {
            "text": "終わっている",
            "isCorrect": false,
            "reason": "Incorrect. 終わっているところ is awkward with ところ."
          },
          {
            "text": "終われ",
            "isCorrect": false,
            "reason": "Incorrect. 終われ is imperative."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 1",
      "Aspect",
      "Temporal Phase"
    ]
  },
  {
    "id": "skm3-u2-toori-ni-accordance",
    "title": "〜とおりに / 〜どおりに (Just As / In Exact Accordance With)",
    "meaning": "Executing an action in faithful, exact alignment with instructions, drawings, thoughts, or maps ('Just as planned / Exactly as told').",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "V-辞書形 / V-た + とおりに | Noun + の + とおりに | Noun + どおりに (Voiced sound without の!)",
    "nuance": "VOICING RULE (連濁): Noun + の + とおりに OR Noun + どおりに (voiced without の): 予定どおり (as scheduled), 期待どおり (as hoped).",
    "keyTakeaway": "MUG-UP: Noun + の + とおりに OR Noun + どおりに (voiced!). V-る / V-た + とおりに.",
    "sentences": [
      {
        "id": "s-skm3-2-1",
        "japanese": "先生が指示したとおりに実験を行ったら、予想どおりの結果が出た。",
        "english": "When we conducted the experiment exactly as the teacher instructed, results came out just as expected.",
        "literal": "Teacher instructed as-exact experiment conducted-when, expectation-as results came-out.",
        "tokens": [
          {
            "word": "指示したとおりに",
            "meaning": "just as instructed",
            "reading": "しじしたとおりに",
            "romaji": "shiji shita toori ni",
            "pos": "Grammar"
          },
          {
            "word": "予想どおりの",
            "meaning": "just as predicted",
            "reading": "よそうどおりの",
            "romaji": "yosou doori no",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Verbal とおりに and nominal どおり."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-2-1",
        "question": "事態は我々の当初の計画（　　）に進展しており、何の問題もありません。",
        "translation": "The situation is progressing exactly according to our original plan, and there are no problems whatsoever.",
        "options": [
          "どおり",
          "とおり",
          "ばかり",
          "ほど"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + どおり (Voiced without の)",
        "ruleHint": "Faithful progress according to plan.",
        "explanations": [
          {
            "text": "どおり",
            "isCorrect": true,
            "reason": "Correct! Noun 計画 combines directly as 計画どおり (voiced without の)."
          },
          {
            "text": "とおり",
            "isCorrect": false,
            "reason": "Incorrect. とおり directly after noun requires の (計画のとおり)."
          },
          {
            "text": "ばかり",
            "isCorrect": false,
            "reason": "Incorrect. ばかり means only / just."
          },
          {
            "text": "ほど",
            "isCorrect": false,
            "reason": "Incorrect. ほど means extent or proportion."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 2",
      "Accordance",
      "Adherence"
    ]
  },
  {
    "id": "skm3-u2-ni-yotte-variation",
    "title": "〜によって / 〜によっては (Depending on / According to Differences)",
    "meaning": "Indicates diversity, variety, or contingency: 'Depending on X, things differ / In some cases of X...'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "Noun + によって (異なる, 違う, さまざまだ) | Noun + によっては (Certain specific outcomes)",
    "nuance": "によって VS によっては: によって introduces general variety (国によって習慣が違う = Customs differ by country). によっては singles out an extreme or specific contingency (日によっては氷点下になる = On some days it drops below freezing).",
    "keyTakeaway": "MUG-UP: Noun + によって = Depending on X, things vary. によっては = In some specific cases of X.",
    "sentences": [
      {
        "id": "s-skm3-2-2",
        "japanese": "文化や宗教によって、タブーとされる食べ物は大きく異なる。",
        "english": "Depending on culture and religion, foods considered taboo differ significantly.",
        "literal": "Culture or religion depending-on, taboo considered food greatly differs.",
        "tokens": [
          {
            "word": "宗教によって",
            "meaning": "depending on religion",
            "reading": "しゅうきょうによって",
            "romaji": "shuukyou ni yotte",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Societal variations across cultural groups."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-2-2",
        "question": "この薬は通常安全ですが、体質（　　）は軽いアレルギー反応が出ることがあります。",
        "translation": "This medicine is usually safe, but depending on the individual constitution, mild allergic reactions may occur in some cases.",
        "options": [
          "によっては",
          "によって",
          "について",
          "にとって"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + によっては (Contingent outcome)",
        "ruleHint": "Specific adverse reactions in certain cases.",
        "explanations": [
          {
            "text": "によっては",
            "isCorrect": true,
            "reason": "Correct! 体質によっては singles out the specific subset of constitutions prone to reaction."
          },
          {
            "text": "によって",
            "isCorrect": false,
            "reason": "Incorrect. によって is general variation, whereas sentence describes an occasional specific outcome."
          },
          {
            "text": "について",
            "isCorrect": false,
            "reason": "Incorrect. について means 'concerning / regarding'."
          },
          {
            "text": "にとって",
            "isCorrect": false,
            "reason": "Incorrect. にとって means 'from the perspective of'."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 2",
      "Variation",
      "Contingency"
    ]
  },
  {
    "id": "skm3-u2-tabini-repetition",
    "title": "〜たびに (Every Single Time / Invariable Recurrence)",
    "meaning": "Whenever condition X occurs, emotional or behavioral response Y invariably accompanies it: 'Every single time without exception'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-辞書形 + たびに | Noun + の + たびに",
    "nuance": "EMOTIONAL RECURRENCE: Used when the speaker notices a recurring pattern or emotional reaction. Cannot be used for everyday routine sequences without feeling (e.g. 'every day when I wake up').",
    "keyTakeaway": "MUG-UP: V-る / Noun + の + たびに = Every time without exception! (会うたびに = Every time we meet).",
    "sentences": [
      {
        "id": "s-skm3-2-3",
        "japanese": "このアルバムを見るたびに、楽しかった学生時代を懐かしく思い出す。",
        "english": "Every time I look at this photo album, I fondly recall my happy student days.",
        "literal": "This album look every-time, fun student-era fondly recall.",
        "tokens": [
          {
            "word": "見るたびに",
            "meaning": "every time I look",
            "reading": "みるたびに",
            "romaji": "miru tabi ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Emotional trigger whenever looking at photos."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-2-3",
        "question": "父は出張の（　　）、家族にその土地の名産品を買ってきてくれる。",
        "translation": "Every time my father goes on a business trip, he buys local specialty goods for the family.",
        "options": [
          "たびに",
          "うちに",
          "ついでに",
          "最中に"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + の + たびに",
        "ruleHint": "Recurrent occurrence on every business trip.",
        "explanations": [
          {
            "text": "たびに",
            "isCorrect": true,
            "reason": "Correct! 出張のたびに expresses invariable recurrence on every business trip."
          },
          {
            "text": "うちに",
            "isCorrect": false,
            "reason": "Incorrect. うちに means while or before opportunity slips."
          },
          {
            "text": "ついでに",
            "isCorrect": false,
            "reason": "Incorrect. ついでに means taking advantage of an errand to perform another side chore."
          },
          {
            "text": "最中に",
            "isCorrect": false,
            "reason": "Incorrect. 最中に means right in the middle of a continuous event."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 2",
      "Repetition",
      "Recurrence"
    ]
  },
  {
    "id": "skm3-u2-ba-hodo-proportion",
    "title": "(〜ば)〜ほど (Proportional Correlation: The More... The More...)",
    "meaning": "As the scale or intensity of condition A increases, consequence B escalates in direct proportion: 'The more X, the more Y'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
    "streamId": "stream-trends",
    "streamName": "Trends, Changes & Proportional Evolution",
    "connection": "V-ば + V-辞書形 + ほど | い-adj ければ + い-adj + ほど | な-adj なら + な-adj な + ほど | Noun + であればあるほど",
    "nuance": "ELLIPSIS ALLOWED: The first conditional part (〜ば) is often dropped in speech: 考えるほど分からなくなる (The more I think, the less I understand).",
    "keyTakeaway": "MUG-UP: [ば-form] + [Dictionary form] + ほど = The more X, the more Y.",
    "sentences": [
      {
        "id": "s-skm3-2-4",
        "japanese": "外国語は使えば使うほど、上手に話せるようになります。",
        "english": "The more you use a foreign language, the more fluently you become able to speak it.",
        "literal": "Foreign-language use-if use-extent, skillfully speak able become.",
        "tokens": [
          {
            "word": "使えば使うほど",
            "meaning": "the more you use it",
            "reading": "つかえばつかうほど",
            "romaji": "tsukaeba tsukau hodo",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Proportional correlation between usage and fluency."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-2-4",
        "question": "荷物は（　　）ほど、旅行は身軽で快適になる。",
        "translation": "The less luggage you have, the lighter and more comfortable your trip becomes.",
        "options": [
          "少なければ少ない",
          "少ないなら少ない",
          "少なくて少ない",
          "少ないと少ない"
        ],
        "correctIndex": 0,
        "grammarFocus": "い-adjective (〜ければ)〜ほど",
        "ruleHint": "Proportional scale of luggage to comfort.",
        "explanations": [
          {
            "text": "少なければ少ない",
            "isCorrect": true,
            "reason": "Correct! い-adjective proportional formula: 少なければ + 少ない + ほど."
          },
          {
            "text": "少ないなら少ない",
            "isCorrect": false,
            "reason": "Incorrect. 少ないなら少ない does not combine in standard correlative pair."
          },
          {
            "text": "少なくて少ない",
            "isCorrect": false,
            "reason": "Incorrect. て-form cannot form this correlative formula."
          },
          {
            "text": "少ないと少ない",
            "isCorrect": false,
            "reason": "Incorrect. と does not match the ほど correlative construction."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 2",
      "Proportion",
      "Correlation"
    ]
  },
  {
    "id": "skm3-u2-tsuide-ni-opportunity",
    "title": "〜ついでに (While at It / Seizing Opportunity for a Side Task)",
    "meaning": "While executing primary task A, seizing the convenient opportunity to perform secondary side task B: 'While you're at it / On the way'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 2: 対象・関連 (Relation & Repetition)",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-辞書形 / V-た + ついでに | Noun + の + ついでに",
    "nuance": "PRIMARY VS INCIDENTAL: Task A is the planned main excursion. Task B is a minor incidental chore piggybacked on A.",
    "keyTakeaway": "MUG-UP: V-る / V-た / Noun + の + ついでに = Convenient 2-for-1 side action!",
    "sentences": [
      {
        "id": "s-skm3-2-5",
        "japanese": "郵便局へ切手を買いに行くついでに、コンビニで公共料金を支払ってきた。",
        "english": "While heading to the post office to buy stamps, I stopped by the convenience store and paid utility bills.",
        "literal": "Post-office stamps buy go while-at-it, convenience-store utility-bills paid.",
        "tokens": [
          {
            "word": "行くついでに",
            "meaning": "while going",
            "reading": "いくついでに",
            "romaji": "iku tsuide ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Side errand during post office trip."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-2-5",
        "question": "散歩の（　　）、ポストにこの手紙を投函してきてくれませんか。",
        "translation": "While you're out taking a walk, would you mind dropping this letter into the mailbox for me?",
        "options": [
          "ついでに",
          "たびに",
          "うちに",
          "最中に"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + の + ついでに (Incidental side-task)",
        "ruleHint": "Piggybacking a chore onto a walk.",
        "explanations": [
          {
            "text": "ついでに",
            "isCorrect": true,
            "reason": "Correct! 散歩のついでに means conveniently posting the letter while already out on a walk."
          },
          {
            "text": "たびに",
            "isCorrect": false,
            "reason": "Incorrect. たびに means every single time you walk."
          },
          {
            "text": "うちに",
            "isCorrect": false,
            "reason": "Incorrect. うちに means before the walk ends."
          },
          {
            "text": "最中に",
            "isCorrect": false,
            "reason": "Incorrect. 最中に means in the middle of walking."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 2",
      "Convenience",
      "Time"
    ]
  },
  {
    "id": "skm3-u3-kurai-hodo-extent",
    "title": "〜くらいだ / 〜ほどだ (Expressing Extreme Degree: To the Extent That)",
    "meaning": "Vividly illustrates high intensity or emotional degree by comparing it to an exaggerated metaphorical state: 'so [adj] that... / to the extent that...'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 3: 比較・限定 (Comparison & Boundaries)",
    "streamId": "stream-limits",
    "streamName": "Boundaries, Extremes & Scope",
    "connection": "V-辞書形 / V-ない + くらいだ / ほどだ | Noun + くらい / ほど",
    "nuance": "METAPHORICAL EXAGGERATION: 'お腹が痛くて、涙が出るほどだった' (My stomach hurt so badly that tears were practically coming out). ほど is slightly more formal/elevated than くらい.",
    "keyTakeaway": "MUG-UP: V-る + くらい / ほど = Metaphorical intensity ('so much that...').",
    "sentences": [
      {
        "id": "s-skm3-3-1",
        "japanese": "昨日の富士山頂からの日の出は、息をのむほど美しかった。",
        "english": "Yesterday's sunrise from the summit of Mt. Fuji was breathtakingly beautiful to the point of gasping.",
        "literal": "Yesterday's Mt-Fuji summit sunrise, breath swallow extent beautiful-was.",
        "tokens": [
          {
            "word": "息をのむほど",
            "meaning": "to the extent of taking one's breath away",
            "reading": "いきをのむほど",
            "romaji": "iki o nomu hodo",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Breathtaking beauty on mountain summit."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-3-1",
        "question": "昨夜はあまりに仕事が忙しくて、猫の手も借りたい（　　）だった。",
        "translation": "Last night work was so overwhelmingly busy that I was in a state where I'd welcome even a cat's paw to help.",
        "options": [
          "くらい",
          "ばかり",
          "ところ",
          "わけ"
        ],
        "correctIndex": 0,
        "grammarFocus": "〜くらいだ (Extreme metaphorical degree)",
        "ruleHint": "Desperate busyness.",
        "explanations": [
          {
            "text": "くらい",
            "isCorrect": true,
            "reason": "Correct! 猫の手も借りたいくらいだ is the idiomatic expression for extreme desperation for help."
          },
          {
            "text": "ばかり",
            "isCorrect": false,
            "reason": "Incorrect. ばかり means only / just."
          },
          {
            "text": "ところ",
            "isCorrect": false,
            "reason": "Incorrect. ところ means temporal phase."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. わけ means logical reason."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 3",
      "Degree",
      "Metaphor"
    ]
  },
  {
    "id": "skm3-u3-kurai-wa-nai",
    "title": "〜くらい…はない / 〜ほど…はない (Superlative: Nothing Is As... As X)",
    "meaning": "Subjective superlative declaring that entity X is unsurpassed in quality Y: 'Nothing is as [adjective] as X / There is nobody quite as [adjective] as X'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 3: 比較・限定 (Comparison & Boundaries)",
    "streamId": "stream-contrasts",
    "streamName": "Contrasts, Concessions & Paradoxes",
    "connection": "Noun + くらい / ほど + [Noun] はない (Negative predicate at the end!)",
    "nuance": "SPEAKER'S HEARTFELT RATING: Expresses the speaker's emotional conviction that X stands supreme (e.g. 'Nothing feels better than a hot bath in winter').",
    "keyTakeaway": "MUG-UP: [Entity] ほど [Adjective] ものはない = There is NOTHING in the world as great as X!",
    "sentences": [
      {
        "id": "s-skm3-3-2",
        "japanese": "仕事で大汗をかいた後の一杯の冷たい水ほど、美味しいものはない。",
        "english": "There is nothing quite as delicious as a glass of cold water after sweating heavily at work.",
        "literal": "Work-at big-sweat shed after one-glass cold water extent, delicious thing none.",
        "tokens": [
          {
            "word": "冷たい水ほど",
            "meaning": "nothing as... as cold water",
            "reading": "つめたいみずほど",
            "romaji": "tsumetai mizu hodo",
            "pos": "Grammar"
          },
          {
            "word": "美味しいものはない",
            "meaning": "there is nothing as delicious",
            "reading": "おいしいものはない",
            "romaji": "oishii mono wa nai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Superlative personal evaluation of cold water."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-3-2",
        "question": "私にとって、家族と一緒に過ごす時間（　　）大切なものはありません。",
        "translation": "For me, there is nothing as precious as the time I spend together with my family.",
        "options": [
          "ほど",
          "ばかり",
          "きり",
          "とおり"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + ほど…はない (Unsurpassed superlative)",
        "ruleHint": "Declaring family time as the supreme treasure.",
        "explanations": [
          {
            "text": "ほど",
            "isCorrect": true,
            "reason": "Correct! 〜ほど [大切なもの] はない establishes the superlative evaluation."
          },
          {
            "text": "ばかり",
            "isCorrect": false,
            "reason": "Incorrect. ばかり means only / just."
          },
          {
            "text": "きり",
            "isCorrect": false,
            "reason": "Incorrect. きり means only / limit."
          },
          {
            "text": "とおり",
            "isCorrect": false,
            "reason": "Incorrect. とおり means in accordance with."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 3",
      "Superlative",
      "Evaluation"
    ]
  },
  {
    "id": "skm3-u4-hanmen-flipside",
    "title": "〜反面 (On the Flip Side: Coexisting Contradictory Aspects)",
    "meaning": "Presents two opposing, contradictory qualities coexisting simultaneously within the exact same person, product, or phenomenon: 'Convenient, but on the flip side, expensive'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 4: 対比・関係 (Contrast & Relation)",
    "streamId": "stream-contrasts",
    "streamName": "Contrasts, Concessions & Paradoxes",
    "connection": "Plain form + 反面 (な-adj takes な/である, Noun takes である)",
    "nuance": "SAME ENTITY PARADOX: Unlike 対して which contrasts two separate people (兄 vs 弟), 反面 examines the two contradictory faces of ONE single subject.",
    "keyTakeaway": "MUG-UP: Two opposing sides of the SAME subject! な-adj takes な + 反面 / である反面.",
    "sentences": [
      {
        "id": "s-skm3-4-1",
        "japanese": "都会の生活は刺激的で便利な反面、人との温かい触れ合いが少ない。",
        "english": "While urban living is stimulating and convenient, on the flip side, warm human connections are few.",
        "literal": "Urban living stimulating convenient flip-side, people-with warm connection few.",
        "tokens": [
          {
            "word": "便利な反面",
            "meaning": "convenient, but on the flip side",
            "reading": "べんりなはんめん",
            "romaji": "benri na hanmen",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Balancing urban convenience against social alienation."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-4-1",
        "question": "一人暮らしは自由で気楽な（　　）、病気の時は非常に心細い。",
        "translation": "While living alone is free and carefree, on the flip side, when you are sick you feel terribly lonely.",
        "options": [
          "反面",
          "ついでに",
          "とたんに",
          "かぎりに"
        ],
        "correctIndex": 0,
        "grammarFocus": "な-adj + な + 反面 two sides of same coin",
        "ruleHint": "Contrasting freedom and vulnerability.",
        "explanations": [
          {
            "text": "反面",
            "isCorrect": true,
            "reason": "Correct! 気楽な反面 contrasts the freedom against the loneliness of the same living situation."
          },
          {
            "text": "ついでに",
            "isCorrect": false,
            "reason": "Incorrect. ついでに means side task."
          },
          {
            "text": "とたんに",
            "isCorrect": false,
            "reason": "Incorrect. とたんに means instant surprise trigger."
          },
          {
            "text": "かぎりに",
            "isCorrect": false,
            "reason": "Incorrect. かぎりに is ungrammatical here."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 4",
      "Flip Side",
      "Contrast"
    ]
  },
  {
    "id": "skm3-u4-kawari-ni-exchange",
    "title": "〜かわりに (In Exchange For / Compensation / Instead Of)",
    "meaning": "1) In exchange for doing or accepting X, compensating with Y ('I'll teach you English in exchange for Japanese lessons'). 2) Instead of regular X, doing alternate Y.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 4: 対比・関係 (Contrast & Relation)",
    "streamId": "stream-contrasts",
    "streamName": "Contrasts, Concessions & Paradoxes",
    "connection": "V-辞書形 + かわりに | Noun + の + かわりに",
    "nuance": "RECIPROCAL EXCHANGE: Clause A balances Clause B like a financial or social trade-off. Can also mean substitution: '休みの日に働いたかわりに、月曜日に休む' (Compensatory day off).",
    "keyTakeaway": "MUG-UP: V-る / Noun + の + かわりに = In exchange for / In place of!",
    "sentences": [
      {
        "id": "s-skm3-4-2",
        "japanese": "英語を教えてもらうかわりに、彼女に美味しい手料理をご馳走した。",
        "english": "In exchange for having her teach me English, I treated her to delicious home cooking.",
        "literal": "English taught-get in-exchange, her-to delicious home-cooking treated.",
        "tokens": [
          {
            "word": "教えてもらうかわりに",
            "meaning": "in exchange for being taught",
            "reading": "おしえてもらうかわりに",
            "romaji": "oshiete morau kawari ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Reciprocal favor trade."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-4-2",
        "question": "この仕事は残業が多くて大変な（　　）に、給料は非常に高い。",
        "translation": "In exchange for this job having lots of overtime and being tough, the salary is exceptionally high.",
        "options": [
          "かわり",
          "ついで",
          "とおり",
          "あまり"
        ],
        "correctIndex": 0,
        "grammarFocus": "〜かわりに reciprocal trade-off",
        "ruleHint": "High salary compensating for tough overtime.",
        "explanations": [
          {
            "text": "かわり",
            "isCorrect": true,
            "reason": "Correct! 大変なかわりに balances tough working conditions with high financial compensation."
          },
          {
            "text": "ついで",
            "isCorrect": false,
            "reason": "Incorrect. ついで means taking opportunity for side errand."
          },
          {
            "text": "とおり",
            "isCorrect": false,
            "reason": "Incorrect. とおり means in accordance with."
          },
          {
            "text": "あまり",
            "isCorrect": false,
            "reason": "Incorrect. あまり means overcome by emotion."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 4",
      "Exchange",
      "Compensation"
    ]
  },
  {
    "id": "skm3-u5-tame-ni-causality",
    "title": "〜ためだ / 〜ために (Objective Cause: Due to / Owing to)",
    "meaning": "Formal written and broadcast expression stating an objective cause or reason: 'Due to X, consequence Y resulted'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 5: 原因・理由 (Causes & Reasons)",
    "streamId": "stream-causality",
    "streamName": "Causal Chains & Regret",
    "connection": "Plain form + ため（に） (な-adj takes な, Noun takes の: 大雪のために)",
    "nuance": "OBJECTIVE & NO PERSONAL INTENT IN B: Clause B cannot be a human command, request, or intention (e.g. '雨のため、傘を持って行きなさい' ❌ is ungrammatical; must use から). ため is for factual reporting.",
    "keyTakeaway": "MUG-UP: Noun + の + ために = Factual cause ('due to'). No commands or requests in clause B!",
    "sentences": [
      {
        "id": "s-skm3-5-1",
        "japanese": "強風と大雨のため、全便の飛行機が見合わせとなっております。",
        "english": "Due to strong winds and heavy rain, all flights are currently suspended.",
        "literal": "Strong-wind and heavy-rain due-to, all-flights airplane suspended become.",
        "tokens": [
          {
            "word": "大雨のため",
            "meaning": "due to heavy rain",
            "reading": "おおあめのため",
            "romaji": "ooame no tame",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Formal public transportation announcement."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-5-1",
        "question": "道路工事の（　　）、この先は全面通行止めになっております。",
        "translation": "Due to road construction, this road ahead is completely closed to traffic.",
        "options": [
          "ため",
          "せい",
          "わけ",
          "こと"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + の + ため (Formal objective cause)",
        "ruleHint": "Road closure announcement.",
        "explanations": [
          {
            "text": "ため",
            "isCorrect": true,
            "reason": "Correct! 道路工事のため is the standard formal administrative announcement register."
          },
          {
            "text": "せい",
            "isCorrect": false,
            "reason": "Incorrect. せい is colloquial emotional blame."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. わけ means logical reason."
          },
          {
            "text": "こと",
            "isCorrect": false,
            "reason": "Incorrect. こと indicates nominalization."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 5",
      "Cause",
      "Formal"
    ]
  },
  {
    "id": "skm3-u5-koto-kara-origin",
    "title": "〜ことから (Origin of Name, Judgment, or Fact: Arising from the Fact That)",
    "meaning": "Points to the historical origin, observable characteristic, or evidential cue that led to a name, reputation, or deduction: 'Named so / Inferred because of X'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 5: 原因・理由 (Causes & Reasons)",
    "streamId": "stream-causality",
    "streamName": "Causal Chains & Regret",
    "connection": "Plain form + ことから (な-adj takes な/である, Noun takes である)",
    "nuance": "NAME ORIGIN & EVIDENTIAL CLUE: Ubiquitous when explaining why places or plants are named: '形が星に似ていることから、星草と呼ばれている' (Called star grass because its shape resembles a star).",
    "keyTakeaway": "MUG-UP: [Observable Fact] ことから [Name / Deductive Conclusion]! Origin story marker.",
    "sentences": [
      {
        "id": "s-skm3-5-2",
        "japanese": "道が濡れていることから、昨夜雨が降ったことが分かる。",
        "english": "From the fact that the roads are wet, we can deduce that it rained last night.",
        "literal": "Roads wet-are fact-from, last-night rain fell fact understand.",
        "tokens": [
          {
            "word": "濡れていることから",
            "meaning": "from the fact that they are wet",
            "reading": "ぬれていることから",
            "romaji": "nurete iru koto kara",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Physical evidence serving as deductive basis."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-5-2",
        "question": "富士山が美しく見える（　　）から、この坂は富士見坂と名付けられた。",
        "translation": "From the fact that Mt. Fuji can be seen beautifully, this slope was named Fujimi-zaka.",
        "options": [
          "こと",
          "もの",
          "わけ",
          "ところ"
        ],
        "correctIndex": 0,
        "grammarFocus": "Clause + ことから (Origin of name)",
        "ruleHint": "Naming origin of Fujimi Slope.",
        "explanations": [
          {
            "text": "こと",
            "isCorrect": true,
            "reason": "Correct! 〜ことから expresses the historical origin of naming a geographical landmark."
          },
          {
            "text": "もの",
            "isCorrect": false,
            "reason": "Incorrect. ものから is ungrammatical here."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. わけから does not exist."
          },
          {
            "text": "ところ",
            "isCorrect": false,
            "reason": "Incorrect. ところから indicates starting location or circumstantial clue, but ことから is the canonical origin pattern."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 5",
      "Origin",
      "Deduction"
    ]
  },
  {
    "id": "skm3-u6-no-dakara-reality",
    "title": "〜のだから / 〜んだから (Since It Is an Acknowledged Reality)",
    "meaning": "Since situation X is an undisputed fact known to all parties, consequence Y naturally follows: 'Since it's a fact that X, of course Y!'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 6: 条件・仮定 (Conditions & Hypotheses)",
    "streamId": "stream-causality",
    "streamName": "Causal Chains & Regret",
    "connection": "Plain form + のだから / んだから (な-adj / Noun takes な: 好きなのだから, 子供なのだから)",
    "nuance": "SHARED COMMON GROUND: You don't use のだから to announce new surprising information; you appeal to a shared premise to give advice, reproof, or encouragement.",
    "keyTakeaway": "MUG-UP: [Obvious Shared Fact] なのだから [Natural mandate or encouragement]!",
    "sentences": [
      {
        "id": "s-skm3-6-1",
        "japanese": "まだ子供なのだから、失敗してもくよくよ悩む必要はありません。",
        "english": "Since you are still a child, there is no need to brood over your mistakes.",
        "literal": "Still child is-since, fail even worry necessity is-not.",
        "tokens": [
          {
            "word": "子供なのだから",
            "meaning": "since you are a child",
            "reading": "こどもなのだから",
            "romaji": "kodomo na no da kara",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Appealing to youth as a compassionate ground for reassurance."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-6-1",
        "question": "自分で決めたこと（　　）だから、最後まで諦めずにやり通しなさい。",
        "translation": "Since this is something you decided for yourself, carry it through to the end without giving up.",
        "options": [
          "なん",
          "だん",
          "のん",
          "いん"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + なのだから / なんだから shared premise",
        "ruleHint": "Mandating responsibility for personal choice.",
        "explanations": [
          {
            "text": "なん",
            "isCorrect": true,
            "reason": "Correct! Noun こと connects via なん to だから (ことなんだから / ことなのだから)."
          },
          {
            "text": "だん",
            "isCorrect": false,
            "reason": "Incorrect. だんだから is ungrammatical."
          },
          {
            "text": "のん",
            "isCorrect": false,
            "reason": "Incorrect. のんだから is nonsensical."
          },
          {
            "text": "いん",
            "isCorrect": false,
            "reason": "Incorrect. いんだから is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 6",
      "Common Ground",
      "Causality"
    ]
  },
  {
    "id": "skm3-u6-tewa-dewa-negative-consequence",
    "title": "〜ては / 〜では (If Such a Condition Persists, Disaster Will Follow)",
    "meaning": "Considers condition X as a severe obstacle: 'If X happens / If you keep doing X, bad result Y is inevitable'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 6: 条件・仮定 (Conditions & Hypotheses)",
    "streamId": "stream-conditionals",
    "streamName": "Conditional Logic & Inevitability",
    "connection": "V-て + は | い-adj くて + は | な-adj / Noun + では",
    "nuance": "NEGATIVE FOREBODING: Clause B ALWAYS describes a bad consequence, trouble, or failure: 'こんなにミスが多くては困る' (If you make this many errors, we're in trouble).",
    "keyTakeaway": "MUG-UP: V-ては / では + [Disaster / Complaint] = 'If this keeps happening, we're doomed!'.",
    "sentences": [
      {
        "id": "s-skm3-6-2",
        "japanese": "毎日こんなに遊んでいては、来月の大学入試に合格できませんよ。",
        "english": "If you spend every day playing around like this, you will never pass next month's university entrance exam.",
        "literal": "Every-day like-this playing if, next-month's exam pass cannot.",
        "tokens": [
          {
            "word": "遊んでいては",
            "meaning": "if you keep playing around",
            "reading": "あそんでいては",
            "romaji": "asonde ite wa",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Warning against persistent idleness."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-6-2",
        "question": "締め切りが明日（　　）、今夜は徹夜するしかありません。",
        "translation": "If the deadline is tomorrow, we have no choice but to pull an all-nighter tonight.",
        "options": [
          "では",
          "ては",
          "なら",
          "たら"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + では negative consequence conditional",
        "ruleHint": "Foreboding deadline emergency.",
        "explanations": [
          {
            "text": "では",
            "isCorrect": true,
            "reason": "Correct! Noun 明日 connects via では (明日では = If it's already tomorrow, we're in trouble)."
          },
          {
            "text": "ては",
            "isCorrect": false,
            "reason": "Incorrect. ては is for verbs and い-adjectives, not nouns."
          },
          {
            "text": "なら",
            "isCorrect": false,
            "reason": "Incorrect. なら is general conditional without the warning foreboding of では."
          },
          {
            "text": "たら",
            "isCorrect": false,
            "reason": "Incorrect. たら is temporal sequence."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 6",
      "Negative Condition",
      "Foreboding"
    ]
  },
  {
    "id": "skm3-u8-to-wa-kagiranai-not-necessarily",
    "title": "〜とは限らない (Partial Truth: Not Necessarily the Case)",
    "meaning": "Denies the absolute validity of a generalization: 'It does not necessarily mean that X is always true in every single case'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 8: 可能・確信 (Certainty & Logic)",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "Plain form + とは限らない (Frequently pairs with adverbs: 必ずしも, いつも, だれもが)",
    "nuance": "DEBUNKING ASSUMPTIONS: '高いものが必ずしも良いとは限らない' (Expensive things are not necessarily good). Softens rigid dogmas.",
    "keyTakeaway": "MUG-UP: 必ずしも [Plain form] とは限らない = Not always necessarily true!",
    "sentences": [
      {
        "id": "s-skm3-8-1",
        "japanese": "有名大学を卒業したからといって、仕事ができるとは限りません。",
        "english": "Just because someone graduated from a famous university, it does not necessarily mean they are competent at work.",
        "literal": "Famous university graduated just-because, work able is-not-necessarily.",
        "tokens": [
          {
            "word": "できるとは限りません",
            "meaning": "not necessarily competent",
            "reading": "できるとはかぎりません",
            "romaji": "dekiru to wa kagirimasen",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Debunking academic credentials as sole proof of competence."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-8-1",
        "question": "値段が高い服が、必ずしも長持ちする（　　）とは限らない。",
        "translation": "High-priced clothing does not necessarily last long in every case.",
        "options": [
          "の",
          "こと",
          "もの",
          "わけ"
        ],
        "correctIndex": 0,
        "grammarFocus": "〜とは限らない partial negation",
        "ruleHint": "Rejecting the assumption that price equals longevity.",
        "explanations": [
          {
            "text": "の",
            "isCorrect": true,
            "reason": "Correct! Plain predicate connects directly: 長持ちするとは限らない (or するものとは限らない)."
          },
          {
            "text": "こと",
            "isCorrect": false,
            "reason": "Incorrect. こと requires additional syntax."
          },
          {
            "text": "もの",
            "isCorrect": false,
            "reason": "Incorrect. わけ requires connection rules."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. の can be omitted; direct connection is canonical."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 8",
      "Certainty",
      "Partial Negation"
    ]
  },
  {
    "id": "skm3-u8-nai-koto-wa-nai-litotes",
    "title": "〜ないことはない / 〜ないこともない (Double Negative Litotes: It's Not That I Can't)",
    "meaning": "Double negative expressing reluctant admission or modest possibility: 'It's not that I completely can't do it... / If pushed, I could possibly manage'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 8: 可能・確信 (Certainty & Logic)",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "V-ない + ことはない | い-adj くない + ことはない | な-adj / Noun でない + ことはない",
    "nuance": "RELUCTANT HESITATION: You don't want to boast 'I can do it easily'. You say '走れば間に合わないことはない' (If I run, it's not that I couldn't make it).",
    "keyTakeaway": "MUG-UP: [Negative] + ことはない = Double negative! 'It is not impossible for me to do X'.",
    "sentences": [
      {
        "id": "s-skm3-8-2",
        "japanese": "納豆はあまり好きではありませんが、食べられないことはありません。",
        "english": "I don't like natto very much, but it's not that I can't eat it if offered.",
        "literal": "Natto not-very like-not but, eat-cannot fact-is-not.",
        "tokens": [
          {
            "word": "食べられないことはありません",
            "meaning": "it is not that I cannot eat it",
            "reading": "たべられないことはありません",
            "romaji": "taberarenai koto wa arimasen",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Reluctant dietary concession."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-8-2",
        "question": "どうしてもとおっしゃるなら、手伝わ（　　）こともありませんが。",
        "translation": "If you insist that it must be done, it's not that I couldn't help you out...",
        "options": [
          "ない",
          "ず",
          "ぬ",
          "なくて"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-ない + こともない double negative",
        "ruleHint": "Hesitant offer of assistance under insistence.",
        "explanations": [
          {
            "text": "ない",
            "isCorrect": true,
            "reason": "Correct! 手伝う negative is 手伝わない + こともありません (It's not that I can't help)."
          },
          {
            "text": "ず",
            "isCorrect": false,
            "reason": "Incorrect. 手伝わず cannot pair with こともない."
          },
          {
            "text": "ぬ",
            "isCorrect": false,
            "reason": "Incorrect. 手伝わぬ is archaic."
          },
          {
            "text": "なくて",
            "isCorrect": false,
            "reason": "Incorrect. 手伝わなくて is te-form."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 8",
      "Litotes",
      "Modesty"
    ]
  },
  {
    "id": "skm3-u11-you-to-suru-inception",
    "title": "〜(よ)うとする (On the Very Verge Of / In the Act of Attempting)",
    "meaning": "1) Inception: Right at the exact moment of about to execute an action. 2) Effort: Actively attempting or striving to achieve X.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 11: 意志・計画 (Intent & Regulations)",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-意向形 + とする (Past: とした / としていた) | Negative: としない (Refuses to do)",
    "nuance": "VERGE OF INTERRUPTION: '家を出ようとした時、電話が鳴った' (Just as I was about to walk out the door, phone rang). Negative 〜ようとしない indicates stubborn refusal ('He refuses to apologize').",
    "keyTakeaway": "MUG-UP: V-よう + とする = Just about to do X! Negative: V-ようとしない = Stubbornly refuses to do!",
    "sentences": [
      {
        "id": "s-skm3-11-1",
        "japanese": "電車に乗ろうとした瞬間、ドアが目の前で閉まってしまった。",
        "english": "The instant I attempted to board the train, the doors shut right in front of my eyes.",
        "literal": "Train board-attempted instant, doors eyes-front-at closed-regrettably.",
        "tokens": [
          {
            "word": "乗ろうとした瞬間",
            "meaning": "the moment I attempted to board",
            "reading": "のろうとしたしゅんかん",
            "romaji": "norou to shita shunkan",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Interrupted boarding action."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-11-1",
        "question": "うちの犬は、お風呂に（　　）とすると、必死で逃げ出そうとする。",
        "translation": "Whenever I attempt to put my dog in the bath, he desperately tries to flee.",
        "options": [
          "入れよう",
          "入れる",
          "入れ",
          "入れた"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-意向形 + とする (Attempting action)",
        "ruleHint": "Attempting to bathe resistant pet.",
        "explanations": [
          {
            "text": "入れよう",
            "isCorrect": true,
            "reason": "Correct! 入れる volitional is 入れよう + とする (Attempting to put into bath)."
          },
          {
            "text": "入れる",
            "isCorrect": false,
            "reason": "Incorrect. 入れる is dictionary form."
          },
          {
            "text": "入れ",
            "isCorrect": false,
            "reason": "Incorrect. 入れ is masu-stem."
          },
          {
            "text": "入れた",
            "isCorrect": false,
            "reason": "Incorrect. 入れた is past form."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 11",
      "Attempt",
      "Inception"
    ]
  },
  {
    "id": "skm3-u11-koto-ni-natte-iru",
    "title": "〜ことになっている (Customary Rule, Schedule, or Standing Regulation)",
    "meaning": "Indicates a pre-established rule, institutional regulation, law, or standing appointment that governs behavior: 'It is a rule that / It is scheduled that'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "Unit 11: 意志・計画 (Intent & Regulations)",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "V-辞書形 / V-ない + ことになっている",
    "nuance": "EXTERNAL REGULATION: This is NOT a personal whim. It represents external school rules, legal bylaws, or schedules: '教室では日本語で話すことになっている' (It is the standing classroom rule).",
    "keyTakeaway": "MUG-UP: V-る / V-ない + ことになっている = It is an established societal/organizational rule!",
    "sentences": [
      {
        "id": "s-skm3-11-2",
        "japanese": "法律により、二十歳未満の飲酒と喫煙は禁止されることになっています。",
        "english": "By law, drinking and smoking under twenty years of age is strictly prohibited.",
        "literal": "Law-by, 20-under drinking smoking prohibited become-is.",
        "tokens": [
          {
            "word": "ことになっています",
            "meaning": "is the standing legal regulation",
            "reading": "ことになっています",
            "romaji": "koto ni natte imasu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Standing statutory legal requirement."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-11-2",
        "question": "この寮では、夜十一時以降は静かに（　　）ことになっている。",
        "translation": "In this dormitory, it is a standing rule to remain quiet after 11:00 PM.",
        "options": [
          "する",
          "して",
          "した",
          "し"
        ],
        "correctIndex": 0,
        "grammarFocus": "Standing rule formula 〜ことになっている",
        "ruleHint": "Dormitory curfew rule.",
        "explanations": [
          {
            "text": "する",
            "isCorrect": true,
            "reason": "Correct! V-辞書形 静かにする connects to ことになっている."
          },
          {
            "text": "して",
            "isCorrect": false,
            "reason": "Incorrect. して is te-form."
          },
          {
            "text": "した",
            "isCorrect": false,
            "reason": "Incorrect. した is past form."
          },
          {
            "text": "し",
            "isCorrect": false,
            "reason": "Incorrect. し is bare stem."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 11",
      "Rules",
      "Regulations"
    ]
  },
  {
    "id": "skm3-fj-ppoi-personality",
    "title": "〜っぽい (Prone to Negative Behavior / Resembling Quality: -ish / -y)",
    "meaning": "1) Tendency toward a personality flaw (怒りっぽい = quick-tempered, 忘れっぽい = forgetful). 2) Displaying obvious childlike or cheap qualities (子供っぽい, 安っぽい).",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "形式整理 J: 意味を広げる形式 (Suffixes & Tendencies)",
    "streamId": "stream-trends",
    "streamName": "Trends, Changes & Proportional Evolution",
    "connection": "V-stem + っぽい | Noun + っぽい | い-adj (drop い) + っぽい (Conjugates as an い-adjective: っぽくない)",
    "nuance": "CRITICAL DIFFERENCE FROM RASHII: らしい indicates genuine authentic nature (男らしい = Manly, worthy of a man). っぽい indicates superficial resemblance or flaw (男っぽい = Tomboyish; 子供っぽい = Childish/Immature).",
    "keyTakeaway": "MUG-UP: Suffix 〜っぽい = -ish, -like, prone to temper/lapse! Acts as an い-adj.",
    "sentences": [
      {
        "id": "s-skm3-j-1",
        "japanese": "彼は些細なことで怒りっぽい性格なので、みんな話しかけにくそうにしている。",
        "english": "Because he has a quick-tempered personality who gets angry over trivial matters, everyone seems hesitant to talk to him.",
        "literal": "He trivial-things-over angry-prone personality since, everyone speak-hard looking-is.",
        "tokens": [
          {
            "word": "怒りっぽい性格",
            "meaning": "quick-tempered personality",
            "reading": "おこりっぽいせいかく",
            "romaji": "okorippoi seikaku",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "怒る (stem 怒り) + っぽい describes chronic short temper."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-j-1",
        "question": "いい歳をした大人が、そんな（　　）っぽい嘘をつくのは恥ずかしいですよ。",
        "translation": "It is shameful for a grown adult to tell such a childish lie.",
        "options": [
          "子供",
          "大人",
          "先生",
          "若者"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + っぽい (Superficial resemblance / immaturity)",
        "ruleHint": "Reproaching childish deception in an adult.",
        "explanations": [
          {
            "text": "子供",
            "isCorrect": true,
            "reason": "Correct! 子供っぽい means 'childish / immature'."
          },
          {
            "text": "大人",
            "isCorrect": false,
            "reason": "Incorrect. 大人っぽい means mature-looking."
          },
          {
            "text": "先生",
            "isCorrect": false,
            "reason": "Incorrect. 先生っぽい means teacher-like."
          },
          {
            "text": "若者",
            "isCorrect": false,
            "reason": "Incorrect. 若者っぽい means youth-like."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Form J",
      "Suffix",
      "Personality"
    ]
  },
  {
    "id": "skm3-fj-darake-flaws",
    "title": "〜だらけ (Covered in Mess, Flaws, or Filth: Riddled With / Full Of)",
    "meaning": "Covered entirely with an undesirable substance or riddled with flaws: 'covered in mud, full of errors, riddled with debts'.",
    "level": "N3",
    "book": "Shin Kanzen Master N3",
    "chapter": "形式整理 J: 意味を広げる形式 (Suffixes & Tendencies)",
    "streamId": "stream-limits",
    "streamName": "Boundaries, Extremes & Scope",
    "connection": "Noun + だらけ (泥だらけ, 間違いだらけ, ゴミだらけ, 借金だらけ)",
    "nuance": "STRICTLY NEGATIVE / DISGUST: You CANNOT use だらけ for desirable things (you cannot say '宝石だらけ' ❌ or 'お金だらけ' ❌ unless complaining of clutter). It is for filth, mess, or errors.",
    "keyTakeaway": "MUG-UP: Noun + だらけ = Covered in an undesirable MESS! (泥だらけ = Covered in mud).",
    "sentences": [
      {
        "id": "s-skm3-j-2",
        "japanese": "急いで書いた彼のレポートは、誤字や文法の間違いだらけだった。",
        "english": "His report, which was written in a rush, was riddled with typos and grammatical errors.",
        "literal": "Hurriedly wrote his report, typos grammar mistakes-riddled was.",
        "tokens": [
          {
            "word": "間違いだらけだった",
            "meaning": "was riddled with mistakes",
            "reading": "まちがいだらけだった",
            "romaji": "machigaidarake datta",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Negative appraisal of messy draft."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-j-2",
        "question": "雨の中サッカーをして、ユニフォームが（　　）だらけになってしまった。",
        "translation": "We played soccer in the rain, and my uniform ended up completely covered in mud.",
        "options": [
          "泥",
          "雨",
          "水",
          "土"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + だらけ (Covered in mess)",
        "ruleHint": "Mud-splattered sports uniform.",
        "explanations": [
          {
            "text": "泥",
            "isCorrect": true,
            "reason": "Correct! 泥だらけ is the canonical idiom for covered all over in mud."
          },
          {
            "text": "雨",
            "isCorrect": false,
            "reason": "Incorrect. 雨だらけ is unnatural (must be びしょ濡れ)."
          },
          {
            "text": "水",
            "isCorrect": false,
            "reason": "Incorrect. 水だらけ is unidiomatic."
          },
          {
            "text": "土",
            "isCorrect": false,
            "reason": "Incorrect. 土だらけ is less natural than 泥 after rain."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Form J",
      "Suffix",
      "Mess"
    ]
  },
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
      {
        "id": "s-skm3-3-3",
        "japanese": "彼に頭を下げて頼むくらいなら、自分で失敗したほうがまだましだ。",
        "english": "Rather than bow my head and beg him for help, I would far rather fail on my own.",
        "literal": "Him-to head lower begging rather-than, by-myself failed better is.",
        "tokens": [
          {
            "word": "頼むくらいなら",
            "meaning": "rather than beg",
            "reading": "たのむくらいなら",
            "romaji": "tanomu kurai nara",
            "pos": "Grammar"
          },
          {
            "word": "頭を下げる",
            "meaning": "to bow / humble oneself",
            "reading": "あたまをさげる",
            "romaji": "atama o sageru",
            "pos": "Expression"
          }
        ],
        "nuanceNote": "Strong refusal of humiliation in preference of independent struggle."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-3-3",
        "question": "あんな失礼な人に謝る（　　）なら、仕事を辞めたほうがいい。",
        "translation": "Rather than apologize to such a rude person, I'd rather quit my job.",
        "options": [
          "くらい",
          "ほど",
          "ばかり",
          "だけに"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-る + くらいなら (Preferential aversion)",
        "ruleHint": "Rejecting an indignity in favor of another drastic course.",
        "explanations": [
          {
            "text": "くらい",
            "isCorrect": true,
            "reason": "Correct! 謝るくらいなら expresses 'Rather than apologize, I'd prefer quitting'."
          },
          {
            "text": "ほど",
            "isCorrect": false,
            "reason": "Incorrect. ほどなら is ungrammatical in this comparative preference structure."
          },
          {
            "text": "ばかり",
            "isCorrect": false,
            "reason": "Incorrect. ばかりなら does not express 'rather than'."
          },
          {
            "text": "だけに",
            "isCorrect": false,
            "reason": "Incorrect. だけになら is incorrect."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 3",
      "Comparison",
      "Preference"
    ]
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
      {
        "id": "s-skm3-3-4",
        "japanese": "風邪を引いたときは、温かいスープを飲んで早く寝るに限る。",
        "english": "When you catch a cold, nothing beats drinking hot soup and getting to sleep early.",
        "literal": "Cold caught when, hot soup drink early sleep is-best.",
        "tokens": [
          {
            "word": "寝るに限る",
            "meaning": "nothing beats sleeping",
            "reading": "ねるにかぎる",
            "romaji": "neru ni kagiru",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Universal folk wisdom framed as speaker's top recommendation."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-3-4",
        "question": "夏の暑い午後には、冷えたスイカを食べる（　　）。",
        "translation": "On a sweltering summer afternoon, nothing beats eating chilled watermelon.",
        "options": [
          "に限る",
          "にすぎない",
          "に違いない",
          "にかかわる"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-る + に限る (Supreme choice)",
        "ruleHint": "Declaring the definitive best remedy for summer heat.",
        "explanations": [
          {
            "text": "に限る",
            "isCorrect": true,
            "reason": "Correct! 食べるに限る asserts that chilled watermelon is the supreme summer remedy."
          },
          {
            "text": "にすぎない",
            "isCorrect": false,
            "reason": "Incorrect. にすぎない means 'is merely / nothing more than'."
          },
          {
            "text": "に違いない",
            "isCorrect": false,
            "reason": "Incorrect. に違いない expresses certainty ('must surely be')."
          },
          {
            "text": "にかかわる",
            "isCorrect": false,
            "reason": "Incorrect. にかかわる means 'involves / affects'."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 3",
      "Superlative",
      "Recommendation"
    ]
  },
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
      {
        "id": "s-skm3-4-3",
        "japanese": "都市部で人口が急増しているのに対して、地方では過疎化が深刻化している。",
        "english": "In contrast to urban areas where the population is skyrocketing, depopulation is becoming severe in rural regions.",
        "literal": "Urban-areas-in population rapidly-increasing whereas, rural-regions-in depopulation severe-becoming.",
        "tokens": [
          {
            "word": "急増しているのに対して",
            "meaning": "whereas increasing rapidly",
            "reading": "きゅうぞうしているのにたいして",
            "romaji": "kyuuzou shite iru no ni taishite",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Contrasting socioeconomic trends between metropolis and countryside."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-4-3",
        "question": "昨日は大雨だった（　　）に対して、今日は雲一つない快晴だ。",
        "translation": "In contrast to yesterday which had heavy downpours, today is clear skies without a single cloud.",
        "options": [
          "の",
          "こと",
          "もの",
          "わけ"
        ],
        "correctIndex": 0,
        "grammarFocus": "普通形 + のに対して (Contrasting clauses)",
        "ruleHint": "Juxtaposing yesterday's storm with today's clear weather.",
        "explanations": [
          {
            "text": "の",
            "isCorrect": true,
            "reason": "Correct! Plain clause + のに対して is required when contrasting entire predicative clauses."
          },
          {
            "text": "こと",
            "isCorrect": false,
            "reason": "Incorrect. ことに対して is unidiomatic here."
          },
          {
            "text": "もの",
            "isCorrect": false,
            "reason": "Incorrect. ものに対して is ungrammatical."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. わけに対して does not form this comparative pattern."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 4",
      "Contrast",
      "Juxtaposition"
    ]
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
      {
        "id": "s-skm3-4-4",
        "japanese": "今年の夏は、例年に比べて格段に猛暑日が続いている。",
        "english": "Compared to ordinary years, extremely hot days are continuing at a markedly higher frequency this summer.",
        "literal": "This-year summer, average-years-to compared remarkably heatwave-days continuing.",
        "tokens": [
          {
            "word": "例年に比べて",
            "meaning": "compared to average years",
            "reading": "れいねんにくらべて",
            "romaji": "reinen ni kurabete",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Climatic comparison against historical baseline."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-4-4",
        "question": "以前の古いアパート（　　）比べて、今の部屋はずっと静かで快適だ。",
        "translation": "Compared to my former old apartment, my current room is far quieter and more comfortable.",
        "options": [
          "に",
          "を",
          "で",
          "と"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + に比べて (Comparative benchmark)",
        "ruleHint": "Evaluating residential comfort against former living quarters.",
        "explanations": [
          {
            "text": "に",
            "isCorrect": true,
            "reason": "Correct! Noun + に比べて is the established benchmark comparison pattern."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. を比べて is ungrammatical."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. で比べて is invalid."
          },
          {
            "text": "と",
            "isCorrect": false,
            "reason": "Incorrect. と比べて exists colloquially, but に比べて is the standard JLPT N3 formulation."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 4",
      "Comparison",
      "Benchmark"
    ]
  },
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
      {
        "id": "s-skm3-5-3",
        "japanese": "先生が熱心に教えてくださったおかげで、無事に合格できました。",
        "english": "Thanks to my teacher teaching me so passionately, I was able to pass safely.",
        "literal": "Teacher passionately taught thanks-to, without-trouble could-pass.",
        "tokens": [
          {
            "word": "教えてくださったおかげで",
            "meaning": "thanks to having taught me",
            "reading": "おしえてくださったおかげで",
            "romaji": "oshiete kudasatta okage de",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Heartfelt gratitude for mentorship."
      },
      {
        "id": "s-skm3-5-4",
        "japanese": "連日の夜更かしのせいで、朝から頭痛がひどい。",
        "english": "Because of staying up late night after night, I've had a terrible headache since morning.",
        "literal": "Consecutive-days staying-up-late fault-due-to, morning-from headache severe.",
        "tokens": [
          {
            "word": "夜更かしのせいで",
            "meaning": "due to staying up late",
            "reading": "よふかしのせいで",
            "romaji": "yofukashi no sei de",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Attributing bodily distress to personal poor habit."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-5-3",
        "question": "台風の（　　）で、楽しみにしていた旅行が急遽キャンセルになった。",
        "translation": "Because of the typhoon, the trip I had been eagerly anticipating was cancelled at short notice.",
        "options": [
          "せい",
          "おかげ",
          "ため",
          "こと"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + のせいで (Negative causal attribution)",
        "ruleHint": "Blaming an adverse event on severe weather.",
        "explanations": [
          {
            "text": "せい",
            "isCorrect": true,
            "reason": "Correct! せいで is required because cancelling an eagerly awaited trip is a negative/regrettable outcome."
          },
          {
            "text": "おかげ",
            "isCorrect": false,
            "reason": "Incorrect. おかげで implies a favorable/happy outcome."
          },
          {
            "text": "ため",
            "isCorrect": false,
            "reason": "Incorrect. ためで is ungrammatical (must be 台風のため, without で)."
          },
          {
            "text": "こと",
            "isCorrect": false,
            "reason": "Incorrect. ことで is not used for blaming disastrous disruptions."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 5",
      "Causality",
      "Blame & Gratitude"
    ]
  },
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
      {
        "id": "s-skm3-6-3",
        "japanese": "パスポートさえあれば、とりあえず飛行機に乗ることはできる。",
        "english": "As long as you have your passport, you can board the plane for the time being.",
        "literal": "Passport only if-exists, for-now airplane board can.",
        "tokens": [
          {
            "word": "パスポートさえあれば",
            "meaning": "if only you have a passport",
            "reading": "ぱすぽーとさえあれば",
            "romaji": "pasupooto sae areba",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Highlighting the indispensable prerequisite."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-6-3",
        "question": "薬を飲み（　　）すれば、すぐに熱は下がりますよ。",
        "translation": "As long as you just take your medicine, your fever will go down promptly.",
        "options": [
          "さえ",
          "こそ",
          "すら",
          "ばかり"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-stem + さえすれば (Sole required action)",
        "ruleHint": "Simple clinical instruction: just take the medication.",
        "explanations": [
          {
            "text": "さえ",
            "isCorrect": true,
            "reason": "Correct! Verb-stem + さえすれば expresses 'as long as you just do X'."
          },
          {
            "text": "こそ",
            "isCorrect": false,
            "reason": "Incorrect. こそすれば is ungrammatical."
          },
          {
            "text": "すら",
            "isCorrect": false,
            "reason": "Incorrect. すらすれば is invalid."
          },
          {
            "text": "ばかり",
            "isCorrect": false,
            "reason": "Incorrect. ばかりすれば means repeatedly doing nothing else."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 6",
      "Conditionals",
      "Prerequisite"
    ]
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
      {
        "id": "s-skm3-6-4",
        "japanese": "たとえどんなに給料が高くても、危険な仕事は引き受けたくない。",
        "english": "Even if the salary were exceptionally high, I would never want to undertake a hazardous job.",
        "literal": "Even-if how-much salary high-even-if, dangerous job undertake not-want.",
        "tokens": [
          {
            "word": "たとえ高くても",
            "meaning": "even if high",
            "reading": "たとえたかくても",
            "romaji": "tatoe takakutemo",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Steadfast refusal prioritizing personal safety over money."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-6-4",
        "question": "（　　）失敗しても、最後まで全力を尽くしたなら悔いはない。",
        "translation": "Even if I fail, as long as I gave it my absolute all until the very end, I will have no regrets.",
        "options": [
          "たとえ",
          "まるで",
          "決して",
          "まさか"
        ],
        "correctIndex": 0,
        "grammarFocus": "たとえ〜ても (Hypothetical concession)",
        "ruleHint": "Acceptance of potential defeat without regret.",
        "explanations": [
          {
            "text": "たとえ",
            "isCorrect": true,
            "reason": "Correct! たとえ pairs with 〜ても to mean 'Even if / Even supposing that'."
          },
          {
            "text": "まるで",
            "isCorrect": false,
            "reason": "Incorrect. まるで pairs with ようだ ('just like')."
          },
          {
            "text": "決して",
            "isCorrect": false,
            "reason": "Incorrect. 決して pairs with negative verbs ('never')."
          },
          {
            "text": "まさか",
            "isCorrect": false,
            "reason": "Incorrect. まさか expresses disbelief ('don't tell me...')."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 6",
      "Conditionals",
      "Concession"
    ]
  },
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
      {
        "id": "s-skm3-7-1",
        "japanese": "後ろの席の人にもよく聞こえるように、マイクの音量を上げてください。",
        "english": "Please turn up the microphone volume so that people in the back seats can hear well too.",
        "literal": "Back-of seats people-to-also well can-hear so-that, mic-of volume please-raise.",
        "tokens": [
          {
            "word": "聞こえるように",
            "meaning": "so that it can be heard",
            "reading": "きこえるように",
            "romaji": "kikoeru you ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Intransitive potential verb 聞こえる expresses intended auditory perception."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-7-1",
        "question": "風邪を引か（　　）ように、暖かくして出かけなさい。",
        "translation": "Dress warmly when you go out so that you don't catch a cold.",
        "options": [
          "ない",
          "ず",
          "ぬ",
          "なくて"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-ない + ように (Preventative purpose)",
        "ruleHint": "Preventing illness through warm clothing.",
        "explanations": [
          {
            "text": "ない",
            "isCorrect": true,
            "reason": "Correct! V-ない + ように is the standard pattern for preventative purpose ('so as not to...')."
          },
          {
            "text": "ず",
            "isCorrect": false,
            "reason": "Incorrect. 引かずように is ungrammatical."
          },
          {
            "text": "ぬ",
            "isCorrect": false,
            "reason": "Incorrect. 引かぬように is archaic/literary."
          },
          {
            "text": "なくて",
            "isCorrect": false,
            "reason": "Incorrect. 引かなくてように is grammatically invalid."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 7",
      "Purpose",
      "Objective"
    ]
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
      {
        "id": "s-skm3-7-2",
        "japanese": "健康のために、夜遅くには甘いものを食べないようにしている。",
        "english": "For the sake of my health, I make it a strict rule to avoid eating sweets late at night.",
        "literal": "Health-of sake-for, night late sweets eat-not endeavor-am-doing.",
        "tokens": [
          {
            "word": "食べないようにしている",
            "meaning": "make a point of not eating",
            "reading": "たべないようにしている",
            "romaji": "tabenai you ni shite iru",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Active self-discipline regarding dietary lifestyle."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-7-2",
        "question": "約束の時間には絶対に遅れない（　　）してください。",
        "translation": "Please make sure you do not arrive late for the promised time.",
        "options": [
          "ように",
          "ために",
          "こと",
          "もの"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-ない + ようにする (Urging effort)",
        "ruleHint": "Reminding someone to maintain punctuality.",
        "explanations": [
          {
            "text": "ように",
            "isCorrect": true,
            "reason": "Correct! ようにしてください is the polite formula for urging conscious adherence."
          },
          {
            "text": "ために",
            "isCorrect": false,
            "reason": "Incorrect. ためにしてください is ungrammatical."
          },
          {
            "text": "こと",
            "isCorrect": false,
            "reason": "Incorrect. ことにしてください means 'please pretend/decide'."
          },
          {
            "text": "もの",
            "isCorrect": false,
            "reason": "Incorrect. ものにしてください is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 7",
      "Habit",
      "Effort"
    ]
  },
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
      {
        "id": "s-skm3-8-3",
        "japanese": "こんなに複雑なプロジェクトを、たった一人で一日で終わらせられるわけがない。",
        "english": "There is absolutely no way that a project this complex could be finished by a single person in just one day.",
        "literal": "This complex project, just one-person-by one-day-in can-finish no-way.",
        "tokens": [
          {
            "word": "終わらせられるわけがない",
            "meaning": "there's no way it could be finished",
            "reading": "おわらせられるわけがない",
            "romaji": "owaraserareru wake ga nai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Adamant rejection of unrealistic workload expectation."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-8-3",
        "question": "いつも真面目な山田さんが、会社の秘密を漏らす（　　）がありません。",
        "translation": "There is no way that Yamada-san, who is always diligent and upright, would leak company secrets.",
        "options": [
          "わけ",
          "はず",
          "もの",
          "こと"
        ],
        "correctIndex": 0,
        "grammarFocus": "普通形 + わけがない (Logical impossibility)",
        "ruleHint": "Defending a colleague's integrity based on character.",
        "explanations": [
          {
            "text": "わけ",
            "isCorrect": true,
            "reason": "Correct! わけがありません expresses absolute logical impossibility based on his trustworthy character."
          },
          {
            "text": "はず",
            "isCorrect": false,
            "reason": "Incorrect. はずがありません is also possible in speech, but 漏らすわけがありません is the primary syntactic match with がありません."
          },
          {
            "text": "もの",
            "isCorrect": false,
            "reason": "Incorrect. ものがありません does not express impossibility."
          },
          {
            "text": "こと",
            "isCorrect": false,
            "reason": "Incorrect. ことがありません means 'never happens'."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 8",
      "Modality",
      "Impossibility"
    ]
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
      {
        "id": "s-skm3-8-4",
        "japanese": "日本に住んでいるからといって、誰もが日本語を上手に話せるわけではない。",
        "english": "Just because someone lives in Japan does not mean that everyone can speak Japanese fluently.",
        "literal": "Japan-in living just-because, everyone Japanese skillfully can-speak not-necessarily.",
        "tokens": [
          {
            "word": "話せるわけではない",
            "meaning": "does not mean they can speak",
            "reading": "はなせるわけではない",
            "romaji": "hanaseru wake dewa nai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Refuting an overly simplistic stereotype."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-8-4",
        "question": "彼の提案に反対したけれど、彼のことが嫌いな（　　）ではない。",
        "translation": "I opposed his proposal, but it's not that I dislike him as a person.",
        "options": [
          "わけ",
          "はず",
          "つもり",
          "せい"
        ],
        "correctIndex": 0,
        "grammarFocus": "な-adj + な + わけではない (Partial denial)",
        "ruleHint": "Separating professional critique from personal sentiment.",
        "explanations": [
          {
            "text": "わけ",
            "isCorrect": true,
            "reason": "Correct! 嫌いなわけではない conveys 'it's not that I dislike him' (partial disclaimer)."
          },
          {
            "text": "はず",
            "isCorrect": false,
            "reason": "Incorrect. 嫌いなはずではない is unnatural."
          },
          {
            "text": "つもり",
            "isCorrect": false,
            "reason": "Incorrect. 嫌いなつもりではない is unidiomatic here."
          },
          {
            "text": "せい",
            "isCorrect": false,
            "reason": "Incorrect. 嫌いなせいではない means 'it's not due to disliking'."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 8",
      "Modality",
      "Nuance Disclaimer"
    ]
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
      {
        "id": "s-skm3-8-5",
        "japanese": "大事な会議の当日に、ちょっと熱があるくらいで仕事を休むわけにはいかない。",
        "english": "On the day of such a crucial meeting, I simply cannot afford to take off work just for a slight fever.",
        "literal": "Crucial meeting day-on, slight fever exists just-by work take-off cannot-afford.",
        "tokens": [
          {
            "word": "休むわけにはいかない",
            "meaning": "cannot afford to take off",
            "reading": "やすむわけにはいかない",
            "romaji": "yasumu wake ni wa ikanai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Sense of professional duty overriding personal discomfort."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-8-5",
        "question": "友人に秘密にしてくれと頼まれたから、誰にも話す（　　）にはいかない。",
        "translation": "Because my friend pleaded with me to keep it a secret, I cannot in all conscience tell anyone.",
        "options": [
          "わけ",
          "はず",
          "こと",
          "もの"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-る + わけにはいかない (Moral constraint)",
        "ruleHint": "Honor-bound to keep a friend's confidence.",
        "explanations": [
          {
            "text": "わけ",
            "isCorrect": true,
            "reason": "Correct! 話すわけにはいかない conveys moral obligation not to betray trust."
          },
          {
            "text": "はず",
            "isCorrect": false,
            "reason": "Incorrect. 話すはずにはいかない is ungrammatical."
          },
          {
            "text": "こと",
            "isCorrect": false,
            "reason": "Incorrect. 話すことにはいかない is invalid."
          },
          {
            "text": "もの",
            "isCorrect": false,
            "reason": "Incorrect. 話すものにはいかない does not form this structure."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 8",
      "Modality",
      "Social Obligation"
    ]
  },
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
      {
        "id": "s-skm3-9-1",
        "japanese": "弟は注射をひどく怖がって、病院の前で泣き出してしまった。",
        "english": "My little brother showed tremendous fear of the injection and burst into tears in front of the hospital.",
        "literal": "Little-brother injection terribly feared-showing, hospital front burst-out-crying.",
        "tokens": [
          {
            "word": "怖がって",
            "meaning": "showing fear / acting terrified",
            "reading": "こわがって",
            "romaji": "kowagatte",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Describing observable childish reaction to medical procedure."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-9-1",
        "question": "最近の若者は、海外旅行に行き（　　）なくなったと言われている。",
        "translation": "It is said that young people these days have become less inclined to want to travel abroad.",
        "options": [
          "たがら",
          "たい",
          "たがり",
          "たく"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-たい → たがらなくなる (3rd person desire trend)",
        "ruleHint": "Sociological observation about modern youth tendencies.",
        "explanations": [
          {
            "text": "たがら",
            "isCorrect": true,
            "reason": "Correct! 行きたがる becomes 行きたがらなくなった (observable third-person loss of desire)."
          },
          {
            "text": "たい",
            "isCorrect": false,
            "reason": "Incorrect. 行きたいなくなった is ungrammatical (must be 行きたくなくなった, but that applies to speaker)."
          },
          {
            "text": "たがり",
            "isCorrect": false,
            "reason": "Incorrect. 行きたがりなくなった is invalid."
          },
          {
            "text": "たく",
            "isCorrect": false,
            "reason": "Incorrect. 行きたくなくなった reflects 1st-person rather than 3rd-person trend."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 9",
      "Psychological",
      "Third-Person"
    ]
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
      {
        "id": "s-skm3-9-2",
        "japanese": "借りたお金は、どんなに親しい友人であっても期日通りに返す（　　）だ。",
        "english": "Money that you have borrowed ought to be repaid right on schedule, no matter how close a friend they may be.",
        "literal": "Borrowed money, how-much close friend even-if schedule-according repay ought-to is.",
        "tokens": [
          {
            "word": "返すべきだ",
            "meaning": "ought to repay",
            "reading": "かえすべきだ",
            "romaji": "kaesu beki da",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Moral principle governing personal financial integrity."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-9-2",
        "question": "自分のミスで他人に迷惑をかけたときは、すぐに謝罪（　　）だ。",
        "translation": "When you inconvenience others through your own mistake, you ought to apologize immediately.",
        "options": [
          "すべき",
          "した",
          "するの",
          "すれば"
        ],
        "correctIndex": 0,
        "grammarFocus": "する → すべきだ (Moral imperative)",
        "ruleHint": "Basic etiquette regarding apologies.",
        "explanations": [
          {
            "text": "すべき",
            "isCorrect": true,
            "reason": "Correct! 謝罪すべきだ (or 謝罪するべきだ) expresses universal ethical duty."
          },
          {
            "text": "した",
            "isCorrect": false,
            "reason": "Incorrect. 謝罪しただ is ungrammatical."
          },
          {
            "text": "するの",
            "isCorrect": false,
            "reason": "Incorrect. 謝罪するのだ is explanatory, not moral prescription."
          },
          {
            "text": "すれば",
            "isCorrect": false,
            "reason": "Incorrect. 謝罪すればだ is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 9",
      "Duty",
      "Ethics"
    ]
  },
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
      {
        "id": "s-skm3-10-1",
        "japanese": "天気予報によると、明日の夕方から関東地方全域で大雪になるそうだ。",
        "english": "According to the weather forecast, heavy snow will reportedly blanket the entire Kanto region starting tomorrow evening.",
        "literal": "Weather forecast according-to, tomorrow evening-from Kanto entire heavy-snow become reportedly.",
        "tokens": [
          {
            "word": "天気予報によると",
            "meaning": "according to the weather forecast",
            "reading": "てんきよほうによると",
            "romaji": "tenki yohou ni yoru to",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Formal citation of meteorological bulletin."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-10-1",
        "question": "今朝の新聞（　　）よると、ガソリン価格が来月から再び値上がりするそうだ。",
        "translation": "According to this morning's newspaper, gasoline prices will reportedly hike again starting next month.",
        "options": [
          "に",
          "で",
          "を",
          "へ"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + によると (Citing sources)",
        "ruleHint": "Reporting economic news from a morning daily.",
        "explanations": [
          {
            "text": "に",
            "isCorrect": true,
            "reason": "Correct! Noun + によると is the fixed citation pattern."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. でよると does not exist."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. をよると is ungrammatical."
          },
          {
            "text": "へ",
            "isCorrect": false,
            "reason": "Incorrect. へよると is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 10",
      "Hearsay",
      "Source Citation"
    ]
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
      {
        "id": "s-skm3-10-2",
        "japanese": "桜が咲いてポカポカ暖かくなり、ようやく春らしい季節になった。",
        "english": "With cherry blossoms blooming and pleasantly warm weather, it has finally become a truly spring-like season.",
        "literal": "Cherry-blossoms bloomed pleasantly warm became, at-last spring-like season became.",
        "tokens": [
          {
            "word": "春らしい",
            "meaning": "truly spring-like",
            "reading": "はるらしい",
            "romaji": "harurashii",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Embodying the ideal aesthetic qualities of springtime."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-10-2",
        "question": "負けて悔しいのは分かるが、プロの選手（　　）最後まで堂々と振る舞うべきだ。",
        "translation": "I understand you are frustrated by the loss, but as a professional athlete you ought to carry yourself with dignity until the end.",
        "options": [
          "らしく",
          "そうに",
          "みたいで",
          "がちに"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + らしく (Archetypical conduct)",
        "ruleHint": "Demanding professional sportsmanship.",
        "explanations": [
          {
            "text": "らしく",
            "isCorrect": true,
            "reason": "Correct! 選手らしく means 'in a manner befitting a true athlete'."
          },
          {
            "text": "そうに",
            "isCorrect": false,
            "reason": "Incorrect. 選手そうに is ungrammatical."
          },
          {
            "text": "みたいで",
            "isCorrect": false,
            "reason": "Incorrect. 選手みたいで implies superficial resemblance rather than true professional conduct."
          },
          {
            "text": "がちに",
            "isCorrect": false,
            "reason": "Incorrect. 選手がちに is meaningless."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 10",
      "Conjecture",
      "Archetype"
    ]
  },
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
      {
        "id": "s-skm3-11-3",
        "japanese": "どんなに忙しくても、毎日必ず30分は読書をすることにしている。",
        "english": "No matter how busy I am, I make it a strict personal rule to read for at least 30 minutes every day.",
        "literal": "How-much busy even-if, every-day definitely 30-minutes reading do-rule-have.",
        "tokens": [
          {
            "word": "読書をすることにしている",
            "meaning": "make it a rule to read",
            "reading": "どくしょをすることにしている",
            "romaji": "dokusho o suru koto ni shite iru",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Disciplined intellectual daily habit."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-11-3",
        "question": "環境を守るため、買い物にはマイバッグを持参する（　　）にしている。",
        "translation": "To protect the environment, I make it a policy to bring my own shopping bag when buying goods.",
        "options": [
          "こと",
          "もの",
          "わけ",
          "ところ"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-る + ことにしている (Personal code)",
        "ruleHint": "Self-directed eco-conscious shopping habit.",
        "explanations": [
          {
            "text": "こと",
            "isCorrect": true,
            "reason": "Correct! 持参することにしている expresses an intentional self-directed eco-friendly habit."
          },
          {
            "text": "もの",
            "isCorrect": false,
            "reason": "Incorrect. ものにしている does not express personal rules."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. わけにしている is ungrammatical."
          },
          {
            "text": "ところ",
            "isCorrect": false,
            "reason": "Incorrect. ところにしている is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 11",
      "Habit",
      "Personal Policy"
    ]
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
      {
        "id": "s-skm3-11-4",
        "japanese": "鍵を閉めたつもりだったが、帰宅したらドアが開いていてぞっとした。",
        "english": "I was under the firm impression that I had locked the door, but returning home I was terrified to find it wide open.",
        "literal": "Key locked impression-had, home-returned door open-being horrified.",
        "tokens": [
          {
            "word": "閉めたつもりだった",
            "meaning": "believed I had locked",
            "reading": "しめたつもりだった",
            "romaji": "shimeta tsumori datta",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Chilling discovery of a mistaken assumption."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-11-4",
        "question": "自分では上手に説明した（　　）だったが、誰にも理解してもらえなかった。",
        "translation": "In my own mind I believed I had explained it clearly, but nobody understood me.",
        "options": [
          "つもり",
          "はず",
          "わけ",
          "ところ"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-た + つもり (Mistaken subjective impression)",
        "ruleHint": "Discrepancy between speaker's intention and listener's comprehension.",
        "explanations": [
          {
            "text": "つもり",
            "isCorrect": true,
            "reason": "Correct! 説明したつもりだった reflects internal conviction contradicted by the listeners' bewilderment."
          },
          {
            "text": "はず",
            "isCorrect": false,
            "reason": "Incorrect. はずだった means 'was supposed to' (expectation that failed to happen)."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. わけだった does not express subjective misconception."
          },
          {
            "text": "ところ",
            "isCorrect": false,
            "reason": "Incorrect. ところだった means 'was on the verge of'."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 11",
      "Mental State",
      "Subjective Illusion"
    ]
  },
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
      {
        "id": "s-skm3-12-1",
        "japanese": "部長は今朝のニュースをすでにお読みになりましたか。",
        "english": "Department manager, have you already read this morning's news?",
        "literal": "Department-manager morning news already honorably-read became-question?",
        "tokens": [
          {
            "word": "お読みになりましたか",
            "meaning": "did you honorably read?",
            "reading": "およみになりましたか",
            "romaji": "oyomi ni narimashita ka",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Deferential query directed upward toward department head."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-12-1",
        "question": "先生、こちらの新しい資料をもうご（　　）になりましたか。",
        "translation": "Professor, have you already reviewed this new reference material?",
        "options": [
          "覧",
          "見",
          "拝見",
          "見せ"
        ],
        "correctIndex": 0,
        "grammarFocus": "ご覧になる (Honorific vision)",
        "ruleHint": "Inquiring politely about a professor's review.",
        "explanations": [
          {
            "text": "覧",
            "isCorrect": true,
            "reason": "Correct! ご覧になる is the honorific form of 見る ('to look/review')."
          },
          {
            "text": "見",
            "isCorrect": false,
            "reason": "Incorrect. ご見になる is ungrammatical."
          },
          {
            "text": "拝見",
            "isCorrect": false,
            "reason": "Incorrect. 拝見 is humble (謙譲語), which you can only say about your own viewing."
          },
          {
            "text": "見せ",
            "isCorrect": false,
            "reason": "Incorrect. ご見せになる is invalid."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 12",
      "Keigo",
      "Respectful Form"
    ]
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
      {
        "id": "s-skm3-12-2",
        "japanese": "明日の午後に、こちらから改めてお電話いたします。",
        "english": "I will personally telephone you once again tomorrow afternoon.",
        "literal": "Tomorrow afternoon, from-here again humble-phone will-do.",
        "tokens": [
          {
            "word": "お電話いたします",
            "meaning": "will humbly call you",
            "reading": "おでんわいたします",
            "romaji": "odenwa itashimasu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Polite corporate commitment to follow up by phone."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-12-2",
        "question": "駅でお待ちしておりますので、到着されましたら（　　）ください。",
        "translation": "I will be waiting for you at the station, so please contact me once you arrive.",
        "options": [
          "ご連絡",
          "お連絡",
          "ご報告され",
          "お伝え"
        ],
        "correctIndex": 0,
        "grammarFocus": "ご + Kango + ください (Polite client request)",
        "ruleHint": "Inviting arrival confirmation.",
        "explanations": [
          {
            "text": "ご連絡",
            "isCorrect": true,
            "reason": "Correct! ご連絡ください (kango ご + 連絡) is the polite honorific request to a client/guest."
          },
          {
            "text": "お連絡",
            "isCorrect": false,
            "reason": "Incorrect. お連絡 is unidiomatic (kango takes ご)."
          },
          {
            "text": "ご報告され",
            "isCorrect": false,
            "reason": "Incorrect. ご報告されください is ungrammatical."
          },
          {
            "text": "お伝え",
            "isCorrect": false,
            "reason": "Incorrect. お伝えください means 'please convey this to someone else'."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Unit 12",
      "Keigo",
      "Humble Deferential"
    ]
  },
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
      {
        "id": "s-skm3-c-1",
        "japanese": "足元が滑って、危うく階段から転がり落ちるところだった。",
        "english": "My footing slipped, and I came within a hair's breadth of tumbling down the stairs.",
        "literal": "Footing slipped, narrowly stairs-from tumble-down verge-was.",
        "tokens": [
          {
            "word": "転がり落ちるところだった",
            "meaning": "was on the verge of tumbling down",
            "reading": "ころがりおちるところだった",
            "romaji": "korogariochiru tokoro datta",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Heart-stopping near-miss on a steep staircase."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-c-1",
        "question": "友達が声をかけてくれなかったら、大事な約束を（　　）ところだった。",
        "translation": "If my friend hadn't called out to remind me, I would have completely forgotten my important appointment.",
        "options": [
          "忘れる",
          "忘れた",
          "忘れて",
          "忘れない"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-る + ところだった (Averted outcome)",
        "ruleHint": "Saved from an embarrassing oversight by a friend's reminder.",
        "explanations": [
          {
            "text": "忘れる",
            "isCorrect": true,
            "reason": "Correct! 辞書形 忘れる + ところだった expresses an action that was narrowly averted."
          },
          {
            "text": "忘れた",
            "isCorrect": false,
            "reason": "Incorrect. 忘れたところだった is invalid."
          },
          {
            "text": "忘れて",
            "isCorrect": false,
            "reason": "Incorrect. 忘れてところだった is ungrammatical."
          },
          {
            "text": "忘れない",
            "isCorrect": false,
            "reason": "Incorrect. 忘れないところだった conveys the opposite meaning."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Form C",
      "Tokoro",
      "Narrow Escape"
    ]
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
      {
        "id": "s-skm3-j-3",
        "japanese": "最近残業続きで疲れ気味なので、今週末は家でゆっくり休みたい。",
        "english": "Because I've been feeling somewhat worn out from consecutive overtime lately, I want to rest peacefully at home this weekend.",
        "literal": "Recently overtime-continuation-due-to fatigue-touch-being, this-weekend home peacefully want-to-rest.",
        "tokens": [
          {
            "word": "疲れ気味",
            "meaning": "touch of fatigue",
            "reading": "つかれぎみ",
            "romaji": "tsukaregimi",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Mild exhaustion prompting weekend recuperation."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-j-3",
        "question": "朝から喉が痛くて少し（　　）気味なので、早めに薬を飲んで寝ます。",
        "translation": "My throat has been hurting since morning and I have a touch of a cold, so I will take medicine early and go to sleep.",
        "options": [
          "風邪",
          "病気",
          "熱",
          "痛い"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + 気味 (Nascent symptom)",
        "ruleHint": "Taking precautionary measures against an impending cold.",
        "explanations": [
          {
            "text": "風邪",
            "isCorrect": true,
            "reason": "Correct! 風邪気味 (かぜぎみ) is the classic idiom for having a mild touch of a cold."
          },
          {
            "text": "病気",
            "isCorrect": false,
            "reason": "Incorrect. 病気気味 is not standard Japanese."
          },
          {
            "text": "熱",
            "isCorrect": false,
            "reason": "Incorrect. 熱気味 is unnatural (one says 微熱がある)."
          },
          {
            "text": "痛い",
            "isCorrect": false,
            "reason": "Incorrect. 痛い気味 is ungrammatical (adjectives do not attach directly to 気味)."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Form J",
      "Suffix",
      "Mild Symptom"
    ]
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
      {
        "id": "s-skm3-j-4",
        "japanese": "スマートフォンに夢中になると、ついつい夜更かしをしがちだ。",
        "english": "When absorbed in one's smartphone, one is terribly prone to inadvertently staying up late.",
        "literal": "Smartphone absorbed become, inadvertently staying-up-late prone-to-do.",
        "tokens": [
          {
            "word": "しがちだ",
            "meaning": "prone to doing",
            "reading": "しがちだ",
            "romaji": "shigachi da",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Common behavioral vulnerability in modern life."
      }
    ],
    "quiz": [
      {
        "id": "q-skm3-j-4",
        "question": "冬になると寒さのせいで家に閉じこもり（　　）になり、運動不足が心配だ。",
        "translation": "In winter, due to the cold, I tend to stay cooped up indoors, and I worry about lack of exercise.",
        "options": [
          "がち",
          "気味",
          "っぽい",
          "だらけ"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-stem + がち (Frequent behavioral tendency)",
        "ruleHint": "Seasonal sedentary lifestyle concerns.",
        "explanations": [
          {
            "text": "がち",
            "isCorrect": true,
            "reason": "Correct! 閉じこもりがち captures the recurrent seasonal tendency to stay cooped up inside."
          },
          {
            "text": "気味",
            "isCorrect": false,
            "reason": "Incorrect. 閉じこもり気味 is less natural for habitual behavior."
          },
          {
            "text": "っぽい",
            "isCorrect": false,
            "reason": "Incorrect. 閉じこもりっぽい is unidiomatic."
          },
          {
            "text": "だらけ",
            "isCorrect": false,
            "reason": "Incorrect. 閉じこもりだらけ is meaningless."
          }
        ]
      }
    ],
    "tags": [
      "N3",
      "SKM Form J",
      "Suffix",
      "Tendency"
    ]
  }
];
