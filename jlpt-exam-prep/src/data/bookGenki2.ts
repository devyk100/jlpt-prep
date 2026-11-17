import type { GrammarPoint } from '../types';

export const BOOK_GENKI2_POINTS: GrammarPoint[] = [
  {
    "id": "g2-l13-potential",
    "title": "可能形 (Potential Verbs: Ability & Possibility)",
    "meaning": "Expresses that an agent has the ability to do an action or that circumstances permit it.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 13: Looking for a Part-time Job",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "Ru-verbs: 食べる→食べられる | U-verbs: 書く→書ける, 飲む→飲める | Irregular: する→できる, くる→こられる",
    "nuance": "PARTICLE FLIP: The direct object particle を frequently shifts to が (日本語を話す → 日本語が話せる).",
    "keyTakeaway": "MUG-UP: U-verbs: change final -u to -e + る (行く→行ける). Object を often becomes が!",
    "sentences": [
      {
        "id": "s-g2-13-1",
        "japanese": "漢字が難しくて、新聞がすらすら読めません。",
        "english": "The kanji are difficult, so I cannot read the newspaper smoothly.",
        "literal": "Kanji difficult-being, newspaper smoothly read-cannot.",
        "tokens": [
          {
            "word": "読めません",
            "meaning": "cannot read (potential neg)",
            "reading": "よめません",
            "romaji": "yomemasen",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "読む potential negative: 読める → 読めません."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-13-1",
        "question": "刺身は新鮮ですが、どうしても生魚が（　　）。",
        "translation": "The sashimi is fresh, but I just cannot eat raw fish.",
        "options": [
          "食べられません",
          "食べません",
          "食べさせません",
          "食べてもらえません"
        ],
        "correctIndex": 0,
        "grammarFocus": "可能形 potential negative",
        "ruleHint": "Inability to consume raw fish.",
        "explanations": [
          {
            "text": "食べられません",
            "isCorrect": true,
            "reason": "Correct! 食べる potential negative is 食べられない / 食べられません."
          },
          {
            "text": "食べません",
            "isCorrect": false,
            "reason": "Incorrect. 食べません is a simple will decision ('I will not eat')."
          },
          {
            "text": "食べさせません",
            "isCorrect": false,
            "reason": "Incorrect. 食べさせません is causative ('I will not let someone eat')."
          },
          {
            "text": "食べてもらえません",
            "isCorrect": false,
            "reason": "Incorrect. 食べてもらえません means cannot get someone to eat."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L13",
      "Potential",
      "Ability"
    ]
  },
  {
    "id": "g2-l13-shi-reasons",
    "title": "〜し、〜し (Listing Multiple Parallel Reasons)",
    "meaning": "Lists two or more complementary reasons leading up to a conclusion or emotion ('Not only... but also...').",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 13: Looking for a Part-time Job",
    "streamId": "stream-causality",
    "streamName": "Causal Chains & Regret",
    "connection": "Plain form + し (Noun/な-adj non-past affirmative takes だ: 綺麗だし, 休みだし)",
    "nuance": "CUMULATIVE FACTORS: Unlike から which gives one direct explanation, 〜し accumulates multiple contributing factors.",
    "keyTakeaway": "MUG-UP: Connects to plain forms. Remember: Noun / な-adj non-past takes だ + し (親切だし).",
    "sentences": [
      {
        "id": "s-g2-13-2",
        "japanese": "物価も安いし、治安もいいし、この街に住んでよかったです。",
        "english": "Prices are cheap and public safety is great, so I am really glad I live in this town.",
        "literal": "Prices-also cheap-and, safety-also good-and, this town-in living glad-was.",
        "tokens": [
          {
            "word": "物価も安いし",
            "meaning": "prices are cheap and",
            "reading": "ぶっかもやすいし",
            "romaji": "bukka mo yasui shi",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Two positive factors combined using 〜し."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-13-2",
        "question": "このアパートは家賃も安いし、駅からも（　　）し、とても便利です。",
        "translation": "This apartment has cheap rent and is close to the station, so it is very convenient.",
        "options": [
          "近い",
          "近くだ",
          "近くに",
          "近いで"
        ],
        "correctIndex": 0,
        "grammarFocus": "い-adjective connection to 〜し",
        "ruleHint": "Listing attributes with parallel reason marker し.",
        "explanations": [
          {
            "text": "近い",
            "isCorrect": true,
            "reason": "Correct! 近い is an い-adjective, connecting directly to し (近いし)."
          },
          {
            "text": "近くだ",
            "isCorrect": false,
            "reason": "Incorrect. 近い is an い-adjective and never takes だ."
          },
          {
            "text": "近くに",
            "isCorrect": false,
            "reason": "Incorrect. 近くに is an adverbial form."
          },
          {
            "text": "近いで",
            "isCorrect": false,
            "reason": "Incorrect. 近いで is ungrammatical."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L13",
      "Reasons",
      "Conjunction"
    ]
  },
  {
    "id": "g2-l13-te-miru",
    "title": "〜てみる (Trying Out an Action: Doing Something to See What Happens)",
    "meaning": "Performs an experimental action to test the waters or see what the outcome will be: 'try doing / give it a try'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 13: Looking for a Part-time Job",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-て + みる (Conjugates as a Ru-verb: 〜てみます, 〜てみたい)",
    "nuance": "TESTING THE WATERS: Literally uses the verb 見る (to see): 'do and see'. 履いてみる (try shoes on), 食べてみる (taste it), 行ってみる (go and check).",
    "keyTakeaway": "MUG-UP: V-て + みる = Give it a try to see the result! (やってみよう = Let's give it a shot!).",
    "sentences": [
      {
        "id": "s-g2-13-3",
        "japanese": "日本の納豆はまだ食べたことがないので、一口食べてみます。",
        "english": "Since I have never eaten Japanese natto yet, I will try taking a bite to see what it's like.",
        "literal": "Japan's natto yet eaten experience have-not since, one-bite eat-and-see.",
        "tokens": [
          {
            "word": "食べてみます",
            "meaning": "will try eating",
            "reading": "たべてみます",
            "romaji": "tabete mimasu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Experimental culinary trial."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-13-3",
        "question": "この服、サイズが合うかどうか一度（　　）みてもいいですか。",
        "translation": "May I try this clothing on once to see if the size fits?",
        "options": [
          "着て",
          "着る",
          "着",
          "着た"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-て + みる (Try doing)",
        "ruleHint": "Trying on clothes in a store.",
        "explanations": [
          {
            "text": "着て",
            "isCorrect": true,
            "reason": "Correct! 着る is a Ru-verb: te-form 着て + みてもいいですか (着てみてもいいですか)."
          },
          {
            "text": "着る",
            "isCorrect": false,
            "reason": "Incorrect. 着る is dictionary form."
          },
          {
            "text": "着",
            "isCorrect": false,
            "reason": "Incorrect. 着 is bare stem."
          },
          {
            "text": "着た",
            "isCorrect": false,
            "reason": "Incorrect. 着た is past form."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L13",
      "Trial",
      "Te-Form"
    ]
  },
  {
    "id": "g2-l13-nara-conditional",
    "title": "なら (Contextual Limitation Conditional: If It's X / As For X)",
    "meaning": "Singles out a specific topic from context: 'If we're talking about X, then... / As for X (though other things might not be)'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 13: Looking for a Part-time Job",
    "streamId": "stream-conditionals",
    "streamName": "Conditional Logic & Inevitability",
    "connection": "Noun + なら (Attaches directly without だ!) | Plain form + なら",
    "nuance": "CONTRASTIVE CONTEXT: Often carries an implicit contrast: 'ひらがななら読めます' (If it's hiragana I can read it—implying kanji is impossible).",
    "keyTakeaway": "MUG-UP: Noun + なら = 'If it's X you're talking about...'. Replaces topic は.",
    "sentences": [
      {
        "id": "s-g2-13-4",
        "japanese": "英語なら話せますが、フランス語は全く話せません。",
        "english": "If it's English, I can speak it, but I cannot speak French at all.",
        "literal": "English if-talking-about speak-can but, French at-all speak-cannot.",
        "tokens": [
          {
            "word": "英語なら",
            "meaning": "if it's English",
            "reading": "えいごなら",
            "romaji": "eigo nara",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Selective linguistic competence."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-13-4",
        "question": "「明日京都に行くんですが。」「京都（　　）、金閣寺がおすすめですよ。」",
        "translation": "'I'm going to Kyoto tomorrow.' 'If it's Kyoto, Kinkaku-ji is highly recommended!'",
        "options": [
          "なら",
          "たら",
          "ば",
          "と"
        ],
        "correctIndex": 0,
        "grammarFocus": "Contextual conditional なら",
        "ruleHint": "Offering a recommendation based on the listener's plan.",
        "explanations": [
          {
            "text": "なら",
            "isCorrect": true,
            "reason": "Correct! なら picks up the conversational topic mentioned by the partner."
          },
          {
            "text": "たら",
            "isCorrect": false,
            "reason": "Incorrect. たら is temporal sequence ('if/when Kyoto happens')."
          },
          {
            "text": "ば",
            "isCorrect": false,
            "reason": "Incorrect. ば requires a predicate (verb/adjective)."
          },
          {
            "text": "と",
            "isCorrect": false,
            "reason": "Incorrect. と is natural inevitable consequence."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L13",
      "Conditionals",
      "Limitation"
    ]
  },
  {
    "id": "g2-l14-hoshii",
    "title": "ほしい (Expressing Desire for an Object: Want Something)",
    "meaning": "Expresses first-person desire to possess a concrete object or commodity: [Item] が ほしい ('I want [Item]').",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 14: Valentine's Day",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "[Item] が ほしいです (Conjugates 100% as an い-adjective: ほしくない, ほしかった)",
    "nuance": "HOSHII VS TAI: たい is for ACTIONS ('I want to BUY a car' = 車を買いたい). ほしい is for NOUN OBJECTS ('I want a car' = 車がほしい). Target takes が!",
    "keyTakeaway": "MUG-UP: [Noun] が ほしい! Never use を with ほしい. (Action desire = 〜たい).",
    "sentences": [
      {
        "id": "s-g2-14-1",
        "japanese": "今度の誕生日に、新しいノートパソコンがほしいです。",
        "english": "For my upcoming birthday, I want a new laptop computer.",
        "literal": "This-time's birthday-on, new laptop want is.",
        "tokens": [
          {
            "word": "ノートパソコンが",
            "meaning": "laptop",
            "reading": "ノートパソコンが",
            "romaji": "nootopasokon ga",
            "pos": "Noun+Particle"
          },
          {
            "word": "ほしいです",
            "meaning": "want",
            "reading": "ほしいです",
            "romaji": "hoshii desu",
            "pos": "Adjective"
          }
        ],
        "nuanceNote": "Desire for material item marked with が."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-14-1",
        "question": "今は何も（　　）くないです。ただゆっくり休みたいです。",
        "translation": "Right now I don't want anything. I just want to rest leisurely.",
        "options": [
          "ほし",
          "ほしい",
          "ほしく",
          "ほしな"
        ],
        "correctIndex": 0,
        "grammarFocus": "Negative of ほしい (ほしくない)",
        "ruleHint": "Expressing absence of material desire.",
        "explanations": [
          {
            "text": "ほし",
            "isCorrect": true,
            "reason": "Correct! ほしい drops い + くない = ほしくない (Nothing wanted)."
          },
          {
            "text": "ほしい",
            "isCorrect": false,
            "reason": "Incorrect. ほしいくない retains the extra い."
          },
          {
            "text": "ほしく",
            "isCorrect": false,
            "reason": "Incorrect. ほしく is already adverbial; adding another くない is invalid."
          },
          {
            "text": "ほしな",
            "isCorrect": false,
            "reason": "Incorrect. ほしな is ungrammatical."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L14",
      "Desire",
      "Possession"
    ]
  },
  {
    "id": "g2-l14-kamoshirenai",
    "title": "〜かもしれない / 〜かもしんない (Epistemic Possibility: Might / May)",
    "meaning": "States that something is possible without guaranteeing it: 'might / may be X' (roughly 50% or less certainty).",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 14: Valentine's Day",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "Plain form + かもしれません | Noun / な-adj attach directly without だ!",
    "nuance": "NO だ BEFORE KAMOSHれない: Just like でしょう, nouns and な-adjectives drop だ: 雨かもしれない (NOT 雨だかもしれない ❌), 暇かもしれない.",
    "keyTakeaway": "MUG-UP: Attach directly without だ! (風邪かもしれない = Might have caught a cold).",
    "sentences": [
      {
        "id": "s-g2-14-2",
        "japanese": "午後から天気が崩れて、雨が降るかもしれません。",
        "english": "The weather may deteriorate from the afternoon, and it might rain.",
        "literal": "Afternoon-from weather deteriorate, rain fall might.",
        "tokens": [
          {
            "word": "降るかもしれません",
            "meaning": "might fall",
            "reading": "ふるかもしれません",
            "romaji": "furu kamoshiremasen",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Epistemic possibility of rain."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-14-2",
        "question": "山田さんはまだ来ませんね。道に（　　）のかもしれません。",
        "translation": "Yamada-san hasn't arrived yet, has he? He might have gotten lost on the way.",
        "options": [
          "迷った",
          "迷う",
          "迷って",
          "迷い"
        ],
        "correctIndex": 0,
        "grammarFocus": "Past conjecture with 〜かもしれない",
        "ruleHint": "Speculating on reasons for someone being late.",
        "explanations": [
          {
            "text": "迷った",
            "isCorrect": true,
            "reason": "Correct! Past plain form 迷った + のかもしれません ('might have gotten lost')."
          },
          {
            "text": "迷う",
            "isCorrect": false,
            "reason": "Incorrect. 迷う is non-past ('will get lost')."
          },
          {
            "text": "迷って",
            "isCorrect": false,
            "reason": "Incorrect. 迷って is te-form."
          },
          {
            "text": "迷い",
            "isCorrect": false,
            "reason": "Incorrect. 迷い is masu-stem."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L14",
      "Possibility",
      "Modality"
    ]
  },
  {
    "id": "g2-l14-tara-dou-desu-ka",
    "title": "〜たらどうですか (Casual Advice / Suggestion: Why Don't You?)",
    "meaning": "Offers a suggestion or recommendation to the listener: 'Why don't you try X? / How about doing X?'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 14: Valentine's Day",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "V-た + らどうですか",
    "nuance": "CRITICAL SOCIAL CAUTION: This phrase can sound patronizing or critical if said to superiors ('Why don't you do your job?'). Use only with peers, friends, or juniors.",
    "keyTakeaway": "MUG-UP: V-た + らどうですか = Friendly suggestion ('Why don't you...?'). Avoid with superiors!",
    "sentences": [
      {
        "id": "s-g2-14-3",
        "japanese": "頭が痛いなら、無理をしないで薬を飲んで寝たらどうですか。",
        "english": "If you have a headache, why don't you stop overworking, take medicine, and sleep?",
        "literal": "Head hurts if, overwork do-not medicine take slept-if how is?",
        "tokens": [
          {
            "word": "寝たらどうですか",
            "meaning": "why don't you sleep?",
            "reading": "ねたらどうですか",
            "romaji": "netara dou desu ka",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Sympathetic peer recommendation."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-14-3",
        "question": "分からない単語があるなら、辞書で（　　）たらどうですか。",
        "translation": "If there are vocabulary words you don't understand, why don't you look them up in a dictionary?",
        "options": [
          "調べ",
          "調べる",
          "調べて",
          "調べた"
        ],
        "correctIndex": 0,
        "grammarFocus": "Advice formula 〜たらどうですか",
        "ruleHint": "Suggesting dictionary lookup.",
        "explanations": [
          {
            "text": "調べ",
            "isCorrect": true,
            "reason": "Correct! 調べる (Ru-verb) past form is 調べた + らどうですか (調べたらどうですか)."
          },
          {
            "text": "調べる",
            "isCorrect": false,
            "reason": "Incorrect. 調べる is dictionary form."
          },
          {
            "text": "調べて",
            "isCorrect": false,
            "reason": "Incorrect. 調べて is te-form."
          },
          {
            "text": "調べた",
            "isCorrect": false,
            "reason": "Incorrect. 調べた already contains た, so adding たら produces '調べたらたら'."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L14",
      "Advice",
      "Suggestions"
    ]
  },
  {
    "id": "g2-l15-volitional-form",
    "title": "意向形 (The Volitional Form: Casual Let's Do / Self-Resolve)",
    "meaning": "The casual plain equivalent of 〜ましょう: 'Let's do X!' In monologue, expresses personal determination: 'I shall do X!'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 15: A Trip to Nagano",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "Ru-verbs: drop る + よう (食べよう) | U-verbs: change final -u to -ou (行こう, 飲もう) | する→しよう, くる→こよう",
    "nuance": "CASUAL COMPANION: In peer conversation, '行こう!' replaces '行きましょう!'. In internal monologue, 'よし、頑張ろう!' expresses resolve.",
    "keyTakeaway": "MUG-UP: Ru-verbs = drop る + よう. U-verbs = change final -u to long -ou (書く→書こう).",
    "sentences": [
      {
        "id": "s-g2-15-1",
        "japanese": "今日は天気がいいから、海までドライブに行こう！",
        "english": "The weather is great today, so let's go for a drive to the beach!",
        "literal": "Today weather good since, beach-to drive-to let's-go!",
        "tokens": [
          {
            "word": "行こう",
            "meaning": "let's go (volitional)",
            "reading": "いこう",
            "romaji": "ikou",
            "pos": "Verb"
          }
        ],
        "nuanceNote": "Casual peer invitation."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-15-1",
        "question": "疲れたから、あそこのカフェで少し（　　）よう。",
        "translation": "Since we're tired, let's rest for a bit at that cafe over there.",
        "options": [
          "休も",
          "休もう",
          "休み",
          "休ま"
        ],
        "correctIndex": 1,
        "grammarFocus": "U-verb volitional form 休もう",
        "ruleHint": "Casual proposal to rest.",
        "explanations": [
          {
            "text": "休も",
            "isCorrect": false,
            "reason": "Incorrect. 休も lacks the long vowel う."
          },
          {
            "text": "休もう",
            "isCorrect": true,
            "reason": "Correct! 休む (U-verb) becomes 休もう in volitional form."
          },
          {
            "text": "休み",
            "isCorrect": false,
            "reason": "Incorrect. 休み is masu-stem."
          },
          {
            "text": "休ま",
            "isCorrect": false,
            "reason": "Incorrect. 休ま is negative stem."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L15",
      "Volitional",
      "Verbs"
    ]
  },
  {
    "id": "g2-l15-volitional-to-omotte-iru",
    "title": "意向形 + と思っている (Firm Ongoing Determination: Intending To)",
    "meaning": "Expresses an ongoing, settled determination that the speaker has been contemplating over time: 'I have been planning/intending to do X'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 15: A Trip to Nagano",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "V-意向形 + と思っています (Ongoing firm intent) / と思います (Decision made on the spot)",
    "nuance": "SPONTANEOUS VS PONDERED: と思う = decided right now on the spot. と思っている = has been decided for some time and remains an ongoing intention.",
    "keyTakeaway": "MUG-UP: V-よう + と思っている = A settled plan I have been thinking about for a while.",
    "sentences": [
      {
        "id": "s-g2-15-2",
        "japanese": "来年から日本企業で働こうと思っています。",
        "english": "I am planning on working at a Japanese firm starting next year.",
        "literal": "Next-year-from Japanese firm-at work-shall quote thinking-am.",
        "tokens": [
          {
            "word": "働こうと思っています",
            "meaning": "am intending to work",
            "reading": "はたらこうとおもっています",
            "romaji": "hatarakou to omotte imasu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Ongoing career resolution."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-15-2",
        "question": "夏休みに富士山に（　　）と思っています。",
        "translation": "I am intending to climb Mt. Fuji during summer vacation.",
        "options": [
          "登ろう",
          "登る",
          "登り",
          "登った"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-意向形 + と思っている",
        "ruleHint": "Ongoing vacation intent.",
        "explanations": [
          {
            "text": "登ろう",
            "isCorrect": true,
            "reason": "Correct! 登る volitional is 登ろう + と思っています."
          },
          {
            "text": "登る",
            "isCorrect": false,
            "reason": "Incorrect. 登る is dictionary form (takes つもり, not volitional と思う)."
          },
          {
            "text": "登り",
            "isCorrect": false,
            "reason": "Incorrect. 登り is masu-stem."
          },
          {
            "text": "登った",
            "isCorrect": false,
            "reason": "Incorrect. 登った is past form."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L15",
      "Intention",
      "Volitional"
    ]
  },
  {
    "id": "g2-l15-relative-clauses",
    "title": "連体修飾節 (Relative Clauses / Qualifying Nouns with Sentences)",
    "meaning": "Embedding an entire sentence before a noun to modify it without any relative pronoun ('The book that I bought yesterday').",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 15: A Trip to Nagano",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "Plain sentence + Noun (Subordinate subject marked with が, NEVER は!)",
    "nuance": "NO RELATIVE PRONOUN: Japanese uses NO 'who', 'which', or 'that'. The modifying sentence simply directly precedes the head noun. Crucially, the subject inside the relative clause takes が!",
    "keyTakeaway": "MUG-UP: [Plain clause] + [Noun]. Inside the clause, use が for the subject (母が作った料理 = Food that mother made).",
    "sentences": [
      {
        "id": "s-g2-15-3",
        "japanese": "これは私が昨日デパートで買ったセーターです。",
        "english": "This is the sweater that I bought at the department store yesterday.",
        "literal": "This topic I-subject yesterday department-store-at bought sweater is.",
        "tokens": [
          {
            "word": "私が昨日デパートで買った",
            "meaning": "that I bought at department store yesterday",
            "reading": "わたしがきょうデパートでかった",
            "romaji": "watashi ga kinou depaato de katta",
            "pos": "Clause"
          },
          {
            "word": "セーター",
            "meaning": "sweater",
            "reading": "セーター",
            "romaji": "seetaa",
            "pos": "Noun"
          }
        ],
        "nuanceNote": "Direct noun qualification without pronouns."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-15-3",
        "question": "あそこに立って（　　）人は、私の高校の英語の先生です。",
        "translation": "The person standing over there is my high school English teacher.",
        "options": [
          "いる",
          "います",
          "いたの",
          "いまして"
        ],
        "correctIndex": 0,
        "grammarFocus": "Relative clause noun modification with plain form",
        "ruleHint": "Modifying person with ongoing action.",
        "explanations": [
          {
            "text": "いる",
            "isCorrect": true,
            "reason": "Correct! Plain form いる modifies the head noun 人 (立っている人)."
          },
          {
            "text": "います",
            "isCorrect": false,
            "reason": "Incorrect. Polite form います cannot modify a noun directly."
          },
          {
            "text": "いたの",
            "isCorrect": false,
            "reason": "Incorrect. いたの人は has unnecessary nominalizer の."
          },
          {
            "text": "いまして",
            "isCorrect": false,
            "reason": "Incorrect. いまして is te-form."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L15",
      "Relative Clauses",
      "Syntax"
    ]
  },
  {
    "id": "g2-l16-to-ii-hoping",
    "title": "〜といい (Hoping for Favorable Outcomes: I Hope That...)",
    "meaning": "Expresses hope or wish that a favorable condition will happen: 〜といいね (Hoping for listener's sake) vs 〜といいんですが (Hoping for speaker's own sake).",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 16: Lost and Found",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "Plain non-past verb + といいですね / といいんですが",
    "nuance": "FOR OTHER VS FOR SELF: When wishing good fortune for the other person, say '〜といいですね' (I hope it goes well for you!). When wishing for yourself, soften with '〜といいんですが' (I hope I pass...).",
    "keyTakeaway": "MUG-UP: V-plain + といいね (Wishing for others). V-plain + といいんですが (Wishing for self).",
    "sentences": [
      {
        "id": "s-g2-16-1",
        "japanese": "明日の試合、晴れるといいですね。「ええ、本当に。」",
        "english": "I hope it will be sunny for tomorrow's match, don't you? 'Yes, truly.'",
        "literal": "Tomorrow's match, clear-up if good is right? Yes, really.",
        "tokens": [
          {
            "word": "晴れるといいですね",
            "meaning": "I hope it clears up",
            "reading": "はれるといいですね",
            "romaji": "hareru to ii desu ne",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Expressing mutual hope for good weather."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-16-1",
        "question": "来週の採用試験に無事合格できる（　　）いいんですが。",
        "translation": "I really hope I can pass next week's employment exam safely.",
        "options": [
          "と",
          "ば",
          "たら",
          "なら"
        ],
        "correctIndex": 0,
        "grammarFocus": "Hoping formula 〜といい",
        "ruleHint": "Hoping to pass employment exam.",
        "explanations": [
          {
            "text": "と",
            "isCorrect": true,
            "reason": "Correct! できるといいんですが is the standard formula for expressing personal hopes."
          },
          {
            "text": "ば",
            "isCorrect": false,
            "reason": "Incorrect. できるば is an invalid conjugation (must be できれば)."
          },
          {
            "text": "たら",
            "isCorrect": false,
            "reason": "Incorrect. できたらいいんですが is colloquial, but と is the canonical textbook pattern."
          },
          {
            "text": "なら",
            "isCorrect": false,
            "reason": "Incorrect. できるならいい requires a different contextual nuance."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L16",
      "Hopes",
      "Modality"
    ]
  },
  {
    "id": "g2-l16-toki-tense",
    "title": "〜時（とき）の時制 (Tense Nuances in 'When' Clauses: V-る時 vs V-た時)",
    "meaning": "Tense distinctions before とき: V-る時 (Action NOT yet completed before main verb) vs V-た時 (Action ALREADY completed before main verb).",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 16: Lost and Found",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-辞書形 + 時 (Prior/During) | V-た + 時 (After completion)",
    "nuance": "CRITICAL TENSE PUZZLE: '日本に行く時カメラを買った' = Bought camera BEFORE arriving in Japan. '日本に行った時カメラを買った' = Bought camera AFTER arriving in Japan!",
    "keyTakeaway": "MUG-UP: V-る時 = Before you do it. V-た時 = After you have finished doing it!",
    "sentences": [
      {
        "id": "s-g2-16-2",
        "japanese": "出かける時、鍵をかけるのを忘れました。",
        "english": "When I was heading out, I forgot to lock the door.",
        "literal": "Head-out when, lock apply forgot.",
        "tokens": [
          {
            "word": "出かける時",
            "meaning": "when heading out",
            "reading": "でかけるとき",
            "romaji": "dekakeru toki",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Action was in progress/prior to completing the departure."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-16-2",
        "question": "日本へ（　　）時、空港の免税店でお土産を買いました。",
        "translation": "When I went to Japan (prior to boarding/reaching Japan), I bought souvenirs at the airport duty-free shop.",
        "options": [
          "行く",
          "行った",
          "行っている",
          "行かない"
        ],
        "correctIndex": 0,
        "grammarFocus": "Tense before とき (V-る時 prior action)",
        "ruleHint": "Action performed before arrival at destination.",
        "explanations": [
          {
            "text": "行く",
            "isCorrect": true,
            "reason": "Correct! Buying souvenirs at the departure duty-free shop happens BEFORE reaching Japan, requiring 行く時."
          },
          {
            "text": "行った",
            "isCorrect": false,
            "reason": "Incorrect. 行った時 would mean after already having arrived in Japan."
          },
          {
            "text": "行っている",
            "isCorrect": false,
            "reason": "Incorrect. 行っている時 is awkward here."
          },
          {
            "text": "行かない",
            "isCorrect": false,
            "reason": "Incorrect. 行かない is negative."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L16",
      "Time",
      "Aspect"
    ]
  },
  {
    "id": "g2-l17-hearsay-sou-desu",
    "title": "〜そうです (Hearsay / Quoting Reports: I Heard That / Reportedly)",
    "meaning": "Relays information obtained from external news, reports, or rumors without personal verification: 'I heard that... / Reportedly'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 17: Grumble and Gossip",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "Plain form + そうです (Noun / な-adj non-past takes だ: 暇だそうです, 雨だそうです)",
    "nuance": "CRUCIAL DIFFERENCE FROM CONJECTURE: Appearance: drop い (おいしそう = looks tasty). Hearsay: KEEP い and keep だ (おいしいそうです = I heard it's tasty; 暇だそうです = I heard he's free).",
    "keyTakeaway": "MUG-UP: Hearsay attaches to 100% UNCHANGED plain form (including だ for nouns/na-adj)! Drop nothing!",
    "sentences": [
      {
        "id": "s-g2-17-1",
        "japanese": "ニュースによると、明日は関東地方で雪が降るそうです。",
        "english": "According to the news, I heard that it will snow in the Kanto region tomorrow.",
        "literal": "News according-to, tomorrow Kanto-region snow fall reportedly.",
        "tokens": [
          {
            "word": "雪が降るそうです",
            "meaning": "I heard it will snow",
            "reading": "ゆきがふるそうです",
            "romaji": "yuki ga furu sou desu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Relaying journalistic weather forecast."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-17-1",
        "question": "田中さんの話では、新しい先生はとても（　　）そうです。",
        "translation": "According to Tanaka-san, I heard that the new teacher is very kind.",
        "options": [
          "親切だ",
          "親切",
          "親切な",
          "親切に"
        ],
        "correctIndex": 0,
        "grammarFocus": "Hearsay 〜そうです with な-adjective",
        "ruleHint": "Reporting secondhand rumor about teacher's personality.",
        "explanations": [
          {
            "text": "親切だ",
            "isCorrect": true,
            "reason": "Correct! Hearsay requires plain affirmative copula だ for な-adjectives: 親切だそうです."
          },
          {
            "text": "親切",
            "isCorrect": false,
            "reason": "Incorrect. 親切 without だ creates appearance/conjecture ('looks kind')."
          },
          {
            "text": "親切な",
            "isCorrect": false,
            "reason": "Incorrect. 親切な is noun-modifying form."
          },
          {
            "text": "親切に",
            "isCorrect": false,
            "reason": "Incorrect. 親切に is adverbial."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L17",
      "Hearsay",
      "Modality"
    ]
  },
  {
    "id": "g2-l17-tara-conditional",
    "title": "〜たら (Specific & Temporal Conditional: If / When / Once Done)",
    "meaning": "Universal conditional: 1) Hypothetical condition ('If X happens, then Y'). 2) Temporal certainty in future ('When / Once X finishes, Y will happen').",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 17: Grumble and Gossip",
    "streamId": "stream-conditionals",
    "streamName": "Conditional Logic & Inevitability",
    "connection": "V-た + ら | い-adj かった + ら | な-adj / Noun だった + ら",
    "nuance": "MOST VERSATILE CONDITIONAL: Unlike と (which forbids commands) or ば (which restricts volitions), 〜たら allows commands, invitations, requests, and future decisions in clause B!",
    "keyTakeaway": "MUG-UP: Formed by adding ら to past た-form! Allows commands and requests in clause B.",
    "sentences": [
      {
        "id": "s-g2-17-2",
        "japanese": "家に帰ったら、すぐに手を洗ってうがいをしましょう。",
        "english": "Once you return home, let's wash our hands and gargle right away.",
        "literal": "Home return-once, immediately hands wash gargle let's-do.",
        "tokens": [
          {
            "word": "帰ったら",
            "meaning": "once you return",
            "reading": "かえったら",
            "romaji": "kaettara",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Temporal sequential conditional triggering action."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-17-2",
        "question": "東京駅に（　　）ら、私に電話をかけてください。",
        "translation": "Once you arrive at Tokyo Station, please call me.",
        "options": [
          "着いた",
          "着く",
          "着き",
          "着いて"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-たら conditional connection",
        "ruleHint": "Instruction to call upon arrival.",
        "explanations": [
          {
            "text": "着いた",
            "isCorrect": true,
            "reason": "Correct! 着く past is 着いた + ら = 着いたら ('once you arrive')."
          },
          {
            "text": "着く",
            "isCorrect": false,
            "reason": "Incorrect. 着く is dictionary form."
          },
          {
            "text": "着き",
            "isCorrect": false,
            "reason": "Incorrect. 着き is masu-stem."
          },
          {
            "text": "着いて",
            "isCorrect": false,
            "reason": "Incorrect. 着いて is te-form."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L17",
      "Conditionals",
      "Sequence"
    ]
  },
  {
    "id": "g2-l17-nakute-mo-ii",
    "title": "〜なくてもいいです (Lack of Obligation: You Do Not Have To)",
    "meaning": "States that an action is unnecessary: 'You do not have to do X / It is fine even if you don't do X'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 17: Grumble and Gossip",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "V-ない (drop い) + くてもいいです",
    "nuance": "LITERAL MEANING: Even if you do not do X, it is fine. Releases the listener from social or official obligation.",
    "keyTakeaway": "MUG-UP: V-ない (drop い) + くてもいいです = You don't have to do it!",
    "sentences": [
      {
        "id": "s-g2-17-3",
        "japanese": "明日は祝日ですから、朝早く起きなくてもいいですよ。",
        "english": "Since tomorrow is a national holiday, you do not have to wake up early.",
        "literal": "Tomorrow national-holiday is since, morning early wake-not-even-if good is.",
        "tokens": [
          {
            "word": "起きなくてもいいですよ",
            "meaning": "you don't have to wake up",
            "reading": "おきなくてもいいですよ",
            "romaji": "okinakute mo ii desu yo",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Releasing listener from waking up early."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-17-3",
        "question": "パスポートのコピーは提出し（　　）くてもいいです。",
        "translation": "You do not have to submit a copy of your passport.",
        "options": [
          "なか",
          "ない",
          "なくて",
          "なかった"
        ],
        "correctIndex": 0,
        "grammarFocus": "〜なくてもいい lack of obligation",
        "ruleHint": "Noting non-essential document requirement.",
        "explanations": [
          {
            "text": "なか",
            "isCorrect": true,
            "reason": "Correct! 提出しない drops い to become なか + くてもいいです."
          },
          {
            "text": "ない",
            "isCorrect": false,
            "reason": "Incorrect. ないくても is ungrammatical (must change い to く)."
          },
          {
            "text": "なくて",
            "isCorrect": false,
            "reason": "Incorrect. なくて already has て."
          },
          {
            "text": "なかった",
            "isCorrect": false,
            "reason": "Incorrect. なかった is past form."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L17",
      "Permission",
      "Lack of Obligation"
    ]
  },
  {
    "id": "g2-l18-transitive-intransitive",
    "title": "自動詞 vs 他動詞 (Intransitive vs Transitive Verb Pairs)",
    "meaning": "Pairs of verbs distinguishing self-occurring natural phenomena (自動詞: marked with が) from deliberate actions on an object (他動詞: marked with を).",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 18: John's Part-Time Job",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "Entity が 自動詞 (開く, 閉まる, つく, 消える) | Agent が Object を 他動詞 (開ける, 閉める, つける, 消す)",
    "nuance": "AGENCY TRAP: ドアが開いた = The door opened (spontaneously/naturally). ドアを開けた = Someone intentionally opened the door. Crucial for advanced JLPT parsing!",
    "keyTakeaway": "MUG-UP: 自動詞 takes が (自発・自然). 他動詞 takes を (Human action). (窓が開く vs 窓を開ける).",
    "sentences": [
      {
        "id": "s-g2-18-1",
        "japanese": "風でドアが閉まりました。寒かったので、私がドアを閉めました。",
        "english": "The door closed in the wind. Because it was cold, I deliberately closed the door.",
        "literal": "Wind-by door closed (intrans). Cold was since, I door closed (trans).",
        "tokens": [
          {
            "word": "ドアが閉まりました",
            "meaning": "door closed (intransitive)",
            "reading": "ドアがしまりました",
            "romaji": "doa ga shimarimashita",
            "pos": "Grammar"
          },
          {
            "word": "ドアを閉めました",
            "meaning": "closed door (transitive)",
            "reading": "ドアをしめました",
            "romaji": "doa o shimemashita",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Side-by-side contrast of intransitive vs transitive pairs."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-18-1",
        "question": "部屋が暗いですね。電気を（　　）ましょう。",
        "translation": "The room is dark, isn't it? Let's turn on the lights.",
        "options": [
          "つけ",
          "つき",
          "消し",
          "消え"
        ],
        "correctIndex": 0,
        "grammarFocus": "Transitive verb つける with direct object を",
        "ruleHint": "Deliberately turning on the lights.",
        "explanations": [
          {
            "text": "つけ",
            "isCorrect": true,
            "reason": "Correct! Direct object marker を requires transitive verb つける (stem つけ + ましょう)."
          },
          {
            "text": "つき",
            "isCorrect": false,
            "reason": "Incorrect. つく is intransitive (電気がつく)."
          },
          {
            "text": "消し",
            "isCorrect": false,
            "reason": "Incorrect. 消す means turn off."
          },
          {
            "text": "消え",
            "isCorrect": false,
            "reason": "Incorrect. 消える is intransitive turn off."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L18",
      "Transitivity",
      "Verbs"
    ]
  },
  {
    "id": "g2-l18-to-natural-consequence",
    "title": "〜と (Natural Consequence & Inevitable Conditional: When / If)",
    "meaning": "States an inevitable natural consequence, physical law, or habitual fact: 'Whenever X happens, Y automatically occurs'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 18: John's Part-Time Job",
    "streamId": "stream-conditionals",
    "streamName": "Conditional Logic & Inevitability",
    "connection": "V-辞書形 / V-ない + と",
    "nuance": "STRICT PROHIBITION ON WILL: Clause B CANNOT be a human request, command, suggestion, or permission (e.g., '春になると花見に行きましょう' ❌ is ungrammatical; must use たら). B must be an automatic physical/natural fact.",
    "keyTakeaway": "MUG-UP: V-る + と = Inevitable automatic trigger! Clause B CANNOT be a command or invitation!",
    "sentences": [
      {
        "id": "s-g2-18-2",
        "japanese": "このボタンを押すと、お釣りが出ます。",
        "english": "When you press this button, the change automatically comes out.",
        "literal": "This button press-when, change comes-out.",
        "tokens": [
          {
            "word": "押すと",
            "meaning": "when you press it",
            "reading": "おすと",
            "romaji": "osu to",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Automatic mechanical consequence."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-18-2",
        "question": "あの交差点を右に（　　）と、左手に大きな郵便局が見えます。",
        "translation": "When you turn right at that intersection, you will see a large post office on your left.",
        "options": [
          "曲がる",
          "曲がった",
          "曲がって",
          "曲がり"
        ],
        "correctIndex": 0,
        "grammarFocus": "Route guidance conditional 〜と",
        "ruleHint": "Automatic visual consequence upon turning.",
        "explanations": [
          {
            "text": "曲がる",
            "isCorrect": true,
            "reason": "Correct! Plain non-past 曲がる connects directly to と for automatic route guidance."
          },
          {
            "text": "曲がった",
            "isCorrect": false,
            "reason": "Incorrect. Past 曲がった cannot connect to と for future directions."
          },
          {
            "text": "曲がって",
            "isCorrect": false,
            "reason": "Incorrect. 曲がって is te-form."
          },
          {
            "text": "曲がり",
            "isCorrect": false,
            "reason": "Incorrect. 曲がり is masu-stem."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L18",
      "Conditionals",
      "Natural Law"
    ]
  },
  {
    "id": "g2-l18-ba-yokatta",
    "title": "〜ばよかった (Retrospective Regret: I Should Have Done)",
    "meaning": "Expresses retrospective regret or remorse over an unfulfilled action: 'I should have done X (but unfortunately I didn't)'. Negative: 'I shouldn't have done X'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 18: John's Part-Time Job",
    "streamId": "stream-causality",
    "streamName": "Causal Chains & Regret",
    "connection": "V-ば + よかった (Affirmative regret: should have) | V-なければ + よかった (Negative regret: shouldn't have)",
    "nuance": "MISSED OPPORTUNITY: Communicates a sigh of self-reproach. '傘を持ってくればよかった' implies it is pouring now and I am drenched.",
    "keyTakeaway": "MUG-UP: V-ば + よかった = 'Ah, I should have done it!'. Negative: V-なければよかった.",
    "sentences": [
      {
        "id": "s-g2-18-3",
        "japanese": "昨夜もっと早く寝ればよかった。今日は一日中頭がぼーっとしています。",
        "english": "I should have gone to bed earlier last night. Today my head is in a daze all day long.",
        "literal": "Last-night more early slept-if was-good. Today all-day head dazed-is.",
        "tokens": [
          {
            "word": "寝ればよかった",
            "meaning": "should have slept",
            "reading": "ねればよかった",
            "romaji": "nereba yokatta",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Remorse over late night."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-18-3",
        "question": "こんなに雨が降るなら、傘を持って（　　）ばよかった。",
        "translation": "If it was going to rain this much, I should have brought an umbrella.",
        "options": [
          "くれ",
          "くる",
          "こ",
          "きた"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-ばよかった retrospective regret",
        "ruleHint": "Regretting forgetting an umbrella in the rain.",
        "explanations": [
          {
            "text": "くれ",
            "isCorrect": true,
            "reason": "Correct! 持ってくる conditional is 持ってくれば + よかった (should have brought)."
          },
          {
            "text": "くる",
            "isCorrect": false,
            "reason": "Incorrect. くる is dictionary form."
          },
          {
            "text": "こ",
            "isCorrect": false,
            "reason": "Incorrect. こ is negative stem."
          },
          {
            "text": "きた",
            "isCorrect": false,
            "reason": "Incorrect. きた is past form."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L18",
      "Regret",
      "Causality"
    ]
  },
  {
    "id": "g2-l19-sonkeigo-verbs",
    "title": "尊敬語 (Honorific Speech: Special Verbs & Regular Formulas)",
    "meaning": "Elevates the actions, states, and possessions of the respected subject (professors, clients, superiors).",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 19: Meeting the Boss",
    "streamId": "stream-social",
    "streamName": "Social Hierarchy, Benefaction & Modesty",
    "connection": "Special verbs: いらっしゃる (行く/来る/いる), おっしゃる (言う), なさる (する), 召し上がる (食べる/飲む), ご覧になる (見る), ご存じだ (知っている) | Regular formula: お + V-stem + になる",
    "nuance": "NEVER USE ON SELF: 尊敬語 elevates the OTHER person. Using it for your own actions is a catastrophic error in Japanese etiquette.",
    "keyTakeaway": "MUG-UP: 尊敬語 (Sonkeigo) is STRICTLY for superiors' actions! Never use for yourself!",
    "sentences": [
      {
        "id": "s-g2-19-1",
        "japanese": "先生は昨日の学会で、非常に興味深い研究成果をおっしゃいました。",
        "english": "The professor stated highly intriguing research findings at yesterday's academic conference.",
        "literal": "Professor yesterday's conference-at, intriguing findings honorably-said.",
        "tokens": [
          {
            "word": "おっしゃいました",
            "meaning": "honorably said (sonkeigo)",
            "reading": "おっしゃいました",
            "romaji": "osshaimashita",
            "pos": "Verb"
          }
        ],
        "nuanceNote": "Elevating professor's speech act via おっしゃる."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-19-1",
        "question": "社長はもうお昼ご飯を（　　）ましたか。",
        "translation": "Has the company president already eaten lunch?",
        "options": [
          "召し上がり",
          "いただき",
          "参り",
          "拝見し"
        ],
        "correctIndex": 0,
        "grammarFocus": "Special honorific verb 召し上がる",
        "ruleHint": "Elevating the president's lunch action.",
        "explanations": [
          {
            "text": "召し上がり",
            "isCorrect": true,
            "reason": "Correct! 召し上がる is the special honorific (尊敬語) verb for 食べる/飲む."
          },
          {
            "text": "いただき",
            "isCorrect": false,
            "reason": "Incorrect. いただく is humble (謙譲語) for oneself eating."
          },
          {
            "text": "参り",
            "isCorrect": false,
            "reason": "Incorrect. 参る is humble for going/coming."
          },
          {
            "text": "拝見し",
            "isCorrect": false,
            "reason": "Incorrect. 拝見する is humble for looking."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L19",
      "Keigo",
      "Honorific"
    ]
  },
  {
    "id": "g2-l19-o-kudasai",
    "title": "お + V-stem + ください (Polite Honorific Request: Please Graciously Do)",
    "meaning": "A graceful, courteous request formula for superiors or customers: 'Please graciously do X' (much more polite than 〜てください).",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 19: Meeting the Boss",
    "streamId": "stream-social",
    "streamName": "Social Hierarchy, Benefaction & Modesty",
    "connection": "お + V-stem + ください (Group 3 する verbs: ご + Noun + ください: ご注意ください)",
    "nuance": "CUSTOMER SERVICE REGISTER: Ubiquitous in stores, public transit, and professional offices: お座りください (Please be seated), お入りください (Please come in), ご覧ください (Please take a look).",
    "keyTakeaway": "MUG-UP: お + [Masu-stem] + ください (Native verbs) / ご + [Noun] + ください (Sino-Japanese).",
    "sentences": [
      {
        "id": "s-g2-19-2",
        "japanese": "足元が滑りやすくなっておりますので、十分にお気をつけください。",
        "english": "Because the footing has become slippery, please take great care.",
        "literal": "Footing slippery become since, sufficiently take-care please.",
        "tokens": [
          {
            "word": "お気をつけください",
            "meaning": "please take care",
            "reading": "おきをつけください",
            "romaji": "o-ki o tsukete kudasai",
            "pos": "Expression"
          }
        ],
        "nuanceNote": "Polite safety announcement."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-19-2",
        "question": "どうぞこちらのお席にお（　　）ください。",
        "translation": "Please graciously have a seat here in this chair.",
        "options": [
          "掛け",
          "掛ける",
          "掛けて",
          "掛けた"
        ],
        "correctIndex": 0,
        "grammarFocus": "Honorific request formula お + stem + ください",
        "ruleHint": "Inviting someone to sit down.",
        "explanations": [
          {
            "text": "掛け",
            "isCorrect": true,
            "reason": "Correct! 腰を掛ける stem is 掛け: お掛けください (Please have a seat)."
          },
          {
            "text": "掛ける",
            "isCorrect": false,
            "reason": "Incorrect. 掛ける is dictionary form."
          },
          {
            "text": "掛けて",
            "isCorrect": false,
            "reason": "Incorrect. 掛けて is te-form."
          },
          {
            "text": "掛けた",
            "isCorrect": false,
            "reason": "Incorrect. 掛けた is past form."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L19",
      "Requests",
      "Keigo"
    ]
  },
  {
    "id": "g2-l21-te-aru",
    "title": "〜てある (Transitive Verb Resultant State: Deliberately Prepared)",
    "meaning": "Describes a continuous state that resulted from someone having deliberately performed an action beforehand for a purpose: 'has been done and remains so'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 21: Which Style of House?",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "Transitive Verb-て + ある (Object is marked with が: 窓が開けてある)",
    "nuance": "DELIBERATE HUMAN PURPOSE: Contrast with 〜ている! '窓が開いている' = The window is open (mere state). '窓が開けてある' = Someone purposely opened the window for ventilation and left it open!",
    "keyTakeaway": "MUG-UP: Transitive verb-て + ある = Purposely prepared beforehand. Object particle flips to が!",
    "sentences": [
      {
        "id": "s-g2-21-1",
        "japanese": "会議室の黒板に、今日の議題が書いてあります。",
        "english": "On the blackboard in the conference room, today's agenda has been written.",
        "literal": "Conference-room blackboard-on, today's agenda written-remains.",
        "tokens": [
          {
            "word": "書いてあります",
            "meaning": "has been written and remains so",
            "reading": "かいてあります",
            "romaji": "kaite arimasu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Deliberately posted agenda."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-21-1",
        "question": "パーティーのために、壁に綺麗な花が（　　）あります。",
        "translation": "For the party, beautiful flowers have been deliberately hung on the wall.",
        "options": [
          "飾って",
          "飾る",
          "飾り",
          "飾られ"
        ],
        "correctIndex": 0,
        "grammarFocus": "Transitive resultant state 〜てある",
        "ruleHint": "Decorations intentionally hung for an upcoming party.",
        "explanations": [
          {
            "text": "飾って",
            "isCorrect": true,
            "reason": "Correct! 飾る (to decorate) connects via te-form 飾って + あります."
          },
          {
            "text": "飾る",
            "isCorrect": false,
            "reason": "Incorrect. 飾る is dictionary form."
          },
          {
            "text": "飾り",
            "isCorrect": false,
            "reason": "Incorrect. 飾り is masu-stem."
          },
          {
            "text": "飾られ",
            "isCorrect": false,
            "reason": "Incorrect. 飾られ is passive stem."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L21",
      "Resultant State",
      "Preparation"
    ]
  },
  {
    "id": "g2-l21-aida-vs-aidani",
    "title": "〜間に vs 〜間 (During a Moment vs Throughout the Entire Duration)",
    "meaning": "〜間に (A short, discrete action occurs AT SOME MOMENT during interval X). 〜間 (A continuous state persists THROUGHOUT THE ENTIRETY of interval X).",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 21: Which Style of House?",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-ている / Noun + の + 間に (Momentary point) vs 間 (Continuous entirety)",
    "nuance": "CRITICAL PARTICLE DISCRIMINATOR: '留守の[間]、犬が寝ていた' = The dog slept the ENTIRE time I was gone. '留守の[間に]、泥棒が入った' = A thief broke in AT A MOMENT during my absence.",
    "keyTakeaway": "MUG-UP: 〜間 = 100% of the time interval. 〜間に = A single moment during the window!",
    "sentences": [
      {
        "id": "s-g2-21-2",
        "japanese": "子供が昼寝をしている間に、急いで晩ご飯の支度を済ませた。",
        "english": "While the child was taking a nap, I quickly completed the dinner preparations.",
        "literal": "Child nap doing was while-in, quickly dinner prep completed.",
        "tokens": [
          {
            "word": "している間に",
            "meaning": "during the time that...",
            "reading": "しているあいだに",
            "romaji": "shite iru aida ni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Action finished at a moment within the child's nap window."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-21-2",
        "question": "日本に留学している（　　）、一度富士山に登ってみたいです。",
        "translation": "While I am studying abroad in Japan, I want to try climbing Mt. Fuji once.",
        "options": [
          "間に",
          "間",
          "うちに",
          "最中に"
        ],
        "correctIndex": 0,
        "grammarFocus": "〜間に (Momentary action within time frame)",
        "ruleHint": "Climbing Mt. Fuji during study abroad stay.",
        "explanations": [
          {
            "text": "間に",
            "isCorrect": true,
            "reason": "Correct! Climbing Mt. Fuji is a discrete, one-time momentary event during the stay, requiring 間に."
          },
          {
            "text": "間",
            "isCorrect": false,
            "reason": "Incorrect. 間 would imply climbing Mt. Fuji continuously for the entire years of study abroad!"
          },
          {
            "text": "うちに",
            "isCorrect": false,
            "reason": "Incorrect. うちに emphasizes urgency before leaving, but 間に is the canonical duration contrast."
          },
          {
            "text": "最中に",
            "isCorrect": false,
            "reason": "Incorrect. 最中に implies right in the thick of a physical activity."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L21",
      "Time",
      "Duration"
    ]
  },
  {
    "id": "g2-l22-ba-conditional",
    "title": "〜ば (The Hypothetical Conditional: If)",
    "meaning": "States a logical or hypothetical condition: 'If X condition is met, then Y occurs'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 22: Education in Japan",
    "streamId": "stream-conditionals",
    "streamName": "Conditional Logic & Inevitability",
    "connection": "Verbs: change final -u to -e + ば (書く→書けば, 食べる→食べれば) | い-adj: drop い + ければ | な-adj / Noun: なら (ば)",
    "nuance": "THE VOLITIONAL PROHIBITION TRAP: If clause A is an action verb (not state), clause B CANNOT be a human request, volition, or command! You cannot say '車を買えば、海に行きましょう' ❌ (Must use たら).",
    "keyTakeaway": "MUG-UP: All verbs: final -u changes to -e + ば! (話す→話せば, 待つ→待てば).",
    "sentences": [
      {
        "id": "s-g2-22-1",
        "japanese": "分からない言葉があれば、いつでも私に聞いてください。",
        "english": "If there are words you don't understand, please ask me anytime.",
        "literal": "Understand-not words have-if, anytime me-to ask please.",
        "tokens": [
          {
            "word": "あれば",
            "meaning": "if there is (stative verb)",
            "reading": "あれば",
            "romaji": "areba",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "ある is a stative verb, so requests in clause B are permitted."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-22-1",
        "question": "毎日練習を（　　）ば、誰でもピアノが上手に弾けるようになりますよ。",
        "translation": "If you practice every day, anyone will become able to play the piano skillfully.",
        "options": [
          "すれ",
          "する",
          "した",
          "して"
        ],
        "correctIndex": 0,
        "grammarFocus": "Verb conditional form 〜ば of する (すれば)",
        "ruleHint": "Practice leading to musical proficiency.",
        "explanations": [
          {
            "text": "すれ",
            "isCorrect": true,
            "reason": "Correct! する irregular conditional is すれば."
          },
          {
            "text": "する",
            "isCorrect": false,
            "reason": "Incorrect. する is dictionary form."
          },
          {
            "text": "した",
            "isCorrect": false,
            "reason": "Incorrect. した is past form."
          },
          {
            "text": "して",
            "isCorrect": false,
            "reason": "Incorrect. して is te-form."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L22",
      "Conditionals",
      "Conjugation"
    ]
  },
  {
    "id": "g2-l22-noni-frustration",
    "title": "〜のに (Frustrated Concession: Even Though / In Spite Of)",
    "meaning": "States that contrary to natural, logical expectation, the reality turned out disappointing or perplexing: 'even though / in spite of the fact that'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 22: Education in Japan",
    "streamId": "stream-contrasts",
    "streamName": "Contrasts, Concessions & Paradoxes",
    "connection": "Plain form + のに (Noun / な-adj non-past affirmative takes な: 好きなのに, 暇なのに)",
    "nuance": "EMOTIONAL INDIGNATION: Unlike が or けれども which are neutral contrasts, のに carries emotional coloring: frustration, indignation, bewilderment, or grievance.",
    "keyTakeaway": "MUG-UP: Connects like んです: Noun / な-adj + な + のに! Carries frustration / disappointment.",
    "sentences": [
      {
        "id": "s-g2-22-2",
        "japanese": "一生懸命勉強したのに、試験で目標の点数が取れませんでした。",
        "english": "Even though I studied with all my might, I couldn't get my target score on the exam.",
        "literal": "Utmost-effort studied even-though, exam-in target score take-could-not.",
        "tokens": [
          {
            "word": "勉強したのに",
            "meaning": "even though I studied",
            "reading": "べんきょうしたのに",
            "romaji": "benkyou shita noni",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Frustrated disappointment at unrewarded hard effort."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-22-2",
        "question": "薬を飲んだ（　　）、頭痛が一向によくなりません。",
        "translation": "Even though I took medicine, my headache is not improving at all.",
        "options": [
          "のに",
          "ので",
          "から",
          "なら"
        ],
        "correctIndex": 0,
        "grammarFocus": "Concessive emotional linker 〜のに",
        "ruleHint": "Frustration that headache persists.",
        "explanations": [
          {
            "text": "のに",
            "isCorrect": true,
            "reason": "Correct! のに conveys grievance that medicine failed to work as expected."
          },
          {
            "text": "ので",
            "isCorrect": false,
            "reason": "Incorrect. ので indicates objective cause ('because I took medicine')."
          },
          {
            "text": "から",
            "isCorrect": false,
            "reason": "Incorrect. から indicates subjective cause."
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
      "N4",
      "Genki L22",
      "Concession",
      "Frustration"
    ]
  },
  {
    "id": "g2-l23-temo-even-if",
    "title": "〜ても / 〜でも (Concessive Conditional: Even If / Even Though)",
    "meaning": "States that even under extreme or hypothetical condition X, result Y does not change: 'Even if X happens, Y'.",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 23: Good-bye",
    "streamId": "stream-conditionals",
    "streamName": "Conditional Logic & Inevitability",
    "connection": "V-て + も | い-adj くて + も | な-adj / Noun + でも",
    "nuance": "OPPOSITE OF TARA: たら means 'if it happens, I will do Y'. ても means 'even if it happens, I STILL will do Y regardless' (雨が降っても行く = Even if it rains, I'm going).",
    "keyTakeaway": "MUG-UP: Formed by adding も to te-form! Verbs/い-adj = 〜ても. Nouns/な-adj = 〜でも.",
    "sentences": [
      {
        "id": "s-g2-23-1",
        "japanese": "どんなに困難でも、私は最後まで諦めません。",
        "english": "No matter how difficult it may be, I will not give up until the very end.",
        "literal": "No-matter-how difficult even-if, I last-until give-up-not.",
        "tokens": [
          {
            "word": "困難でも",
            "meaning": "even if difficult",
            "reading": "こんなんでも",
            "romaji": "konnan de mo",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Unshakable resolve despite hardship."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-23-1",
        "question": "いくら（　　）も、答えがどうしても思い出せない。",
        "translation": "No matter how much I think, I just cannot recall the answer.",
        "options": [
          "考えて",
          "考える",
          "考えた",
          "考え"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-て + も concessive conditional",
        "ruleHint": "Persistent mental block despite hard thinking.",
        "explanations": [
          {
            "text": "考えて",
            "isCorrect": true,
            "reason": "Correct! 考える te-form 考えて + も forms 考えても ('even if I think')."
          },
          {
            "text": "考える",
            "isCorrect": false,
            "reason": "Incorrect. 考える is dictionary form."
          },
          {
            "text": "考えた",
            "isCorrect": false,
            "reason": "Incorrect. 考えた is past form."
          },
          {
            "text": "考え",
            "isCorrect": false,
            "reason": "Incorrect. 考え is masu-stem."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L23",
      "Concession",
      "Conditionals"
    ]
  },
  {
    "id": "g2-l23-koto-ni-suru-naru",
    "title": "〜ことにする vs 〜ことになる (Personal Decision vs Outside Emergence)",
    "meaning": "〜ことにする (The speaker personally decides to do X). 〜ことになる (It has been determined by external rules, organizations, or circumstances that X will happen).",
    "level": "N4",
    "book": "Genki II",
    "chapter": "Lesson 23: Good-bye",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "V-辞書形 / V-ない + ことにする / ことになる",
    "nuance": "DECISION VS SOCIAL CONSENSUS: '会社を辞めることにした' = I personally chose to quit. '会社を辞めることになった' = Due to layoffs, restructuring, or external consensus, I am leaving (polite Japanese deflection).",
    "keyTakeaway": "MUG-UP: ことにする = MY active decision. ことになる = OUTSIDE circumstance / official rule.",
    "sentences": [
      {
        "id": "s-g2-23-2",
        "japanese": "健康のために、毎日野菜をたくさん食べることにしました。",
        "english": "For my health, I decided to eat lots of vegetables every day.",
        "literal": "Health-for, every-day vegetables lots eat-decision made.",
        "tokens": [
          {
            "word": "食べることにしました",
            "meaning": "decided to eat",
            "reading": "たべることにしました",
            "romaji": "taberu koto ni shimashita",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Voluntary personal lifestyle decision."
      }
    ],
    "quiz": [
      {
        "id": "q-g2-23-2",
        "question": "来月から大阪の支店へ転勤する（　　）になりました。",
        "translation": "It has been arranged that I will transfer to the Osaka branch from next month.",
        "options": [
          "こと",
          "もの",
          "わけ",
          "はず"
        ],
        "correctIndex": 0,
        "grammarFocus": "External emergence 〜ことになる",
        "ruleHint": "Reporting official corporate reassignment.",
        "explanations": [
          {
            "text": "こと",
            "isCorrect": true,
            "reason": "Correct! Official company job transfer is an outside organizational decision: 〜ことになった."
          },
          {
            "text": "もの",
            "isCorrect": false,
            "reason": "Incorrect. ものになった is nonsensical."
          },
          {
            "text": "わけ",
            "isCorrect": false,
            "reason": "Incorrect. わけになった does not exist."
          },
          {
            "text": "はず",
            "isCorrect": false,
            "reason": "Incorrect. はずになった is ungrammatical."
          }
        ]
      }
    ],
    "tags": [
      "N4",
      "Genki L23",
      "Decision",
      "Modality"
    ]
  }
];
