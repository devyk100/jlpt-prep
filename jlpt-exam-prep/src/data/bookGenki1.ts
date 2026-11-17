import type { GrammarPoint } from '../types';

export const BOOK_GENKI1_POINTS: GrammarPoint[] = [
  {
    "id": "g1-l1-wa-desu",
    "title": "X は Y です (X is Y / Topic & Copula)",
    "meaning": "X is Y. Establishes X as the contextual topic with は and equates it to predicate Y with です.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 1: New Friends",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "Noun1 + は + Noun2 / Adjective + です",
    "nuance": "The topic particle は (pronounced 'wa') presents the background context ('as for X...'). です serves as polite non-past copula.",
    "keyTakeaway": "MUG-UP: は marks the topic. Pronounced 'wa', written as は.",
    "sentences": [
      {
        "id": "s-g1-1-1",
        "japanese": "私はアリゾナ大学の学生です。",
        "english": "I am a student at the University of Arizona.",
        "literal": "I topic University-of-Arizona's student am.",
        "tokens": [
          {
            "word": "私",
            "meaning": "I / me",
            "reading": "わたし",
            "romaji": "watashi",
            "pos": "Pronoun"
          },
          {
            "word": "は",
            "meaning": "topic marker",
            "reading": "わ",
            "romaji": "wa",
            "pos": "Particle"
          },
          {
            "word": "学生",
            "meaning": "student",
            "reading": "がくせい",
            "romaji": "gakusei",
            "pos": "Noun"
          },
          {
            "word": "です",
            "meaning": "am / is",
            "reading": "です",
            "romaji": "desu",
            "pos": "Copula"
          }
        ],
        "nuanceNote": "Standard polite self-identification."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-1-1",
        "question": "スミスさん（　　）イギリス人です。",
        "translation": "Smith-san is British.",
        "options": [
          "は",
          "を",
          "に",
          "へ"
        ],
        "correctIndex": 0,
        "grammarFocus": "Topic particle は",
        "ruleHint": "Marks Smith-san as the conversational topic.",
        "explanations": [
          {
            "text": "は",
            "isCorrect": true,
            "reason": "Correct! は marks Smith-san as the topic being identified as British."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. を marks direct objects of action verbs."
          },
          {
            "text": "に",
            "isCorrect": false,
            "reason": "Incorrect. に marks destination, time, or location of existence."
          },
          {
            "text": "へ",
            "isCorrect": false,
            "reason": "Incorrect. へ marks direction of movement."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L1",
      "Topic",
      "Copula"
    ]
  },
  {
    "id": "g1-l1-question-ka",
    "title": "質問の「か」 (Question Sentence Marker 〜ですか)",
    "meaning": "Turns any declarative sentence into a question simply by appending か at the end, without inverting word order.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 1: New Friends",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "Sentence + か (Rising intonation)",
    "nuance": "NO QUESTION MARK NEEDED: In traditional Japanese, particle か serves as the question mark itself. Question word goes right where the answer belongs.",
    "keyTakeaway": "MUG-UP: Append か to the end of a sentence to make it a polite question. No word inversion!",
    "sentences": [
      {
        "id": "s-g1-1-2",
        "japanese": "専攻は何ですか。「日本語です。」",
        "english": "What is your major? 'It is Japanese.'",
        "literal": "Major topic what is question? Japanese is.",
        "tokens": [
          {
            "word": "専攻",
            "meaning": "major",
            "reading": "せんこう",
            "romaji": "senkou",
            "pos": "Noun"
          },
          {
            "word": "何",
            "meaning": "what",
            "reading": "なん",
            "romaji": "nan",
            "pos": "Interrogative"
          },
          {
            "word": "ですか",
            "meaning": "is it?",
            "reading": "ですか",
            "romaji": "desu ka",
            "pos": "Copula+Particle"
          }
        ],
        "nuanceNote": "Interrogative 何 directly takes ですか."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-1-2",
        "question": "今何時（　　）。「午後二時です。」",
        "translation": "What time is it now? 'It is 2:00 PM.'",
        "options": [
          "ですか",
          "でした",
          "でして",
          "ですね"
        ],
        "correctIndex": 0,
        "grammarFocus": "Question particle か",
        "ruleHint": "Inquiring about current time.",
        "explanations": [
          {
            "text": "ですか",
            "isCorrect": true,
            "reason": "Correct! ですか forms a standard polite question asking the time."
          },
          {
            "text": "でした",
            "isCorrect": false,
            "reason": "Incorrect. でした is past tense ('was it?')."
          },
          {
            "text": "でして",
            "isCorrect": false,
            "reason": "Incorrect. でして is te-form of copula."
          },
          {
            "text": "ですね",
            "isCorrect": false,
            "reason": "Incorrect. ですね seeks confirmation ('isn't it?'), not an open inquiry."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L1",
      "Questions",
      "Particle か"
    ]
  },
  {
    "id": "g1-l1-noun-no-noun",
    "title": "Noun1 の Noun2 (Noun Modification, Possession & Affiliation)",
    "meaning": "Particle の connects two nouns where Noun1 modifies, describes, or possesses Noun2 ('Noun1's Noun2' or 'Noun2 of Noun1').",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 1: New Friends",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "Noun1 (Modifier/Owner) + の + Noun2 (Main item)",
    "nuance": "MODIFIER FIRST: Japanese strictly places the modifier before の: 日本の大学 (Japanese university), 私の友達 (my friend).",
    "keyTakeaway": "MUG-UP: [Owner/Category] の [Item]. The main noun is ALWAYS at the end!",
    "sentences": [
      {
        "id": "s-g1-1-3",
        "japanese": "たけしさんはさくら大学の学生です。",
        "english": "Takeshi-san is a student of Sakura University.",
        "literal": "Takeshi topic Sakura-University's student is.",
        "tokens": [
          {
            "word": "さくら大学の",
            "meaning": "Sakura University's",
            "reading": "さくらだいがくの",
            "romaji": "sakura daigaku no",
            "pos": "Noun+Particle"
          },
          {
            "word": "学生",
            "meaning": "student",
            "reading": "がくせい",
            "romaji": "gakusei",
            "pos": "Noun"
          }
        ],
        "nuanceNote": "Affiliation: Sakura University modifies student."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-1-3",
        "question": "これは私の母（　　）写真です。",
        "translation": "This is a photo of my mother.",
        "options": [
          "の",
          "に",
          "を",
          "と"
        ],
        "correctIndex": 0,
        "grammarFocus": "Possessive / Attribute particle の",
        "ruleHint": "Mother qualifies the photo.",
        "explanations": [
          {
            "text": "の",
            "isCorrect": true,
            "reason": "Correct! の connects the subject of the photo (母) to the photo itself (写真)."
          },
          {
            "text": "に",
            "isCorrect": false,
            "reason": "Incorrect. に marks indirect objects, destinations, or specific time."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. を marks direct objects of action verbs."
          },
          {
            "text": "と",
            "isCorrect": false,
            "reason": "Incorrect. と means 'and' or 'with'."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L1",
      "Particle の",
      "Possession"
    ]
  },
  {
    "id": "g1-l1-time-and-age",
    "title": "時間と年齢 (Telling Time with 〜時・〜分 and Age with 〜歳)",
    "meaning": "Formulas for hours (〜時 / じ), minutes (〜分 / ふん・ぷん), and age (〜歳 / さい) including critical phonological irregularities.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 1: New Friends",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "Number + 時 (Hour) | Number + 分 (Minutes) | Number + 歳 (Age)",
    "nuance": "IRREGULARITY ALERT: 4 o'clock is よじ (NOT よんじ ❌)! 7 o'clock is しちじ (NOT ななじ). 9 o'clock is くじ (NOT きゅうじ). Age 1 is いっさい; age 20 is はたち (二十歳)!",
    "keyTakeaway": "MUG-UP: 4:00 = よじ! 7:00 = しちじ! 9:00 = くじ! Age 20 = はたち!",
    "sentences": [
      {
        "id": "s-g1-1-4",
        "japanese": "今、午前九時半です。私は十九歳です。",
        "english": "Right now, it is 9:30 AM. I am nineteen years old.",
        "literal": "Now AM 9-hour-half is. I 19-years-old am.",
        "tokens": [
          {
            "word": "午前",
            "meaning": "AM / morning",
            "reading": "ごぜん",
            "romaji": "gozen",
            "pos": "Noun"
          },
          {
            "word": "九時半",
            "meaning": "9:30",
            "reading": "くじはん",
            "romaji": "kuji han",
            "pos": "Noun"
          },
          {
            "word": "十九歳",
            "meaning": "19 years old",
            "reading": "じゅうきゅうさい",
            "romaji": "juukyuu sai",
            "pos": "Noun"
          }
        ],
        "nuanceNote": "九時 is read くじ; 半 means half past."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-1-4",
        "question": "会議は午後（　　）から始まります。",
        "translation": "The meeting starts from 4:00 PM.",
        "options": [
          "四時（よじ）",
          "四時（よんじ）",
          "四時（しじ）",
          "四時（ななじ）"
        ],
        "correctIndex": 0,
        "grammarFocus": "Irregular hour reading 四時 (よじ)",
        "ruleHint": "Reading 4 o'clock correctly.",
        "explanations": [
          {
            "text": "四時（よじ）",
            "isCorrect": true,
            "reason": "Correct! 4 o'clock is strictly read as よじ (yoji)."
          },
          {
            "text": "四時（よんじ）",
            "isCorrect": false,
            "reason": "Incorrect. よんじ is a common learner error but does not exist in standard Japanese."
          },
          {
            "text": "四時（しじ）",
            "isCorrect": false,
            "reason": "Incorrect. しじ is avoided due to phonetic clash with death (死)."
          },
          {
            "text": "四時（ななじ）",
            "isCorrect": false,
            "reason": "Incorrect. ななじ is 7, not 4."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L1",
      "Time",
      "Numbers"
    ]
  },
  {
    "id": "g1-l2-kore-sore-are-dore",
    "title": "これ・それ・あれ・どれ (Thing Demonstrative Pronouns)",
    "meaning": "Standalone pronouns indicating physical things relative to speaker and listener: これ (near speaker), それ (near listener), あれ (far from both), どれ (which one).",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 2: Shopping",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "これ / それ / あれ / どれ + は / が / を (Standalone Pronouns)",
    "nuance": "STANDALONE RULE: これ/それ/あれ/どれ stand alone as independent nouns. They CANNOT directly modify a noun (you cannot say 'これ本' ❌; that requires 'この本').",
    "keyTakeaway": "MUG-UP: これ/それ/あれ/どれ stand ALONE. こ (me), そ (you), あ (far away), ど (which?).",
    "sentences": [
      {
        "id": "s-g1-2-1",
        "japanese": "これは日本のペンです。あれはアメリカのペンです。",
        "english": "This is a Japanese pen. That one over there is an American pen.",
        "literal": "This topic Japan's pen is. That-over-there America's pen is.",
        "tokens": [
          {
            "word": "これ",
            "meaning": "this (near me)",
            "reading": "これ",
            "romaji": "kore",
            "pos": "Pronoun"
          },
          {
            "word": "あれ",
            "meaning": "that (over there)",
            "reading": "あれ",
            "romaji": "are",
            "pos": "Pronoun"
          }
        ],
        "nuanceNote": "Spatial contrast between proximal and distal items."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-2-1",
        "question": "（　　）は誰の傘ですか。「それですか。私のです。」",
        "translation": "Whose umbrella is that near you? 'That one? It is mine.'",
        "options": [
          "それ",
          "ここ",
          "その",
          "そこ"
        ],
        "correctIndex": 0,
        "grammarFocus": "Demonstrative pronoun それ",
        "ruleHint": "Pointing to an item near the conversation partner.",
        "explanations": [
          {
            "text": "それ",
            "isCorrect": true,
            "reason": "Correct! それ refers to an object near the listener."
          },
          {
            "text": "ここ",
            "isCorrect": false,
            "reason": "Incorrect. ここ means 'this place'."
          },
          {
            "text": "その",
            "isCorrect": false,
            "reason": "Incorrect. その must directly precede a noun (その傘)."
          },
          {
            "text": "そこ",
            "isCorrect": false,
            "reason": "Incorrect. そこ means 'that place near you'."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L2",
      "Demonstratives",
      "Pronouns"
    ]
  },
  {
    "id": "g1-l2-kono-sono-ano-dono",
    "title": "この・その・あの・どの + Noun (Pre-Noun Demonstrative Modifiers)",
    "meaning": "Demonstrative determiners that must immediately precede and specify a noun: この (this N), その (that N near you), あの (that N over there), どの (which N).",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 2: Shopping",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "この / その / あの / どの + Noun",
    "nuance": "MUST HAVE A NOUN: Unlike これ which is an independent noun, この CANNOT stand by itself. Saying 'このは私の' ❌ is ungrammatical; must be 'この時計は私の'.",
    "keyTakeaway": "MUG-UP: この・その・あの・どの MUST be glued to a following Noun!",
    "sentences": [
      {
        "id": "s-g1-2-2",
        "japanese": "あの時計はいくらですか。「三千円です。」",
        "english": "How much is that watch over there? 'It is 3,000 yen.'",
        "literal": "That watch-over-there how-much is? 3000-yen is.",
        "tokens": [
          {
            "word": "あの",
            "meaning": "that (over there)",
            "reading": "あの",
            "romaji": "ano",
            "pos": "Pre-noun"
          },
          {
            "word": "時計",
            "meaning": "watch / clock",
            "reading": "とけい",
            "romaji": "tokei",
            "pos": "Noun"
          }
        ],
        "nuanceNote": "あの directly modifies noun 時計."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-2-2",
        "question": "すみません、（　　）辞書を見せてください。",
        "translation": "Excuse me, please show me that dictionary near you.",
        "options": [
          "その",
          "それ",
          "そんな",
          "そこに"
        ],
        "correctIndex": 0,
        "grammarFocus": "Pre-noun determiner その",
        "ruleHint": "Modifying the noun 辞書.",
        "explanations": [
          {
            "text": "その",
            "isCorrect": true,
            "reason": "Correct! その directly modifies the noun 辞書."
          },
          {
            "text": "それ",
            "isCorrect": false,
            "reason": "Incorrect. それ is a standalone pronoun and cannot directly attach to 辞書 without の."
          },
          {
            "text": "そんな",
            "isCorrect": false,
            "reason": "Incorrect. そんな means 'that kind of'."
          },
          {
            "text": "そこに",
            "isCorrect": false,
            "reason": "Incorrect. そこに is a locational postposition."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L2",
      "Demonstratives",
      "Pre-nouns"
    ]
  },
  {
    "id": "g1-l2-koko-soko-asoko-doko",
    "title": "ここ・そこ・あそこ・どこ (Place Demonstrative Pronouns)",
    "meaning": "Demonstrative locational nouns indicating places: ここ (here), そこ (there near you), あそこ (over there), どこ (where).",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 2: Shopping",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "ここ / そこ / あそこ / どこ + は / に / で",
    "nuance": "PHONETIC IRREGULARITY: Notice the pattern: こ, そ, but あそこ (NOT あこ ❌)! Interrogative is どこ.",
    "keyTakeaway": "MUG-UP: Note the irregularity: ここ, そこ, あそこ (with -そ- in the middle!), どこ.",
    "sentences": [
      {
        "id": "s-g1-2-3",
        "japanese": "図書館はどこですか。「あそこです。」",
        "english": "Where is the library? 'It is over there.'",
        "literal": "Library topic where is? Over-there is.",
        "tokens": [
          {
            "word": "図書館",
            "meaning": "library",
            "reading": "としょかん",
            "romaji": "toshokan",
            "pos": "Noun"
          },
          {
            "word": "どこ",
            "meaning": "where",
            "reading": "どこ",
            "romaji": "doko",
            "pos": "Interrogative"
          },
          {
            "word": "あそこ",
            "meaning": "over there",
            "reading": "あそこ",
            "romaji": "asoko",
            "pos": "Pronoun"
          }
        ],
        "nuanceNote": "Inquiring place with どこ; answering with distant place あそこ."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-2-3",
        "question": "お手洗いは（　　）ですか。「あちらのエレベーターの隣です。」",
        "translation": "Where is the restroom? 'It is next to the elevator over there.'",
        "options": [
          "どこ",
          "どれ",
          "だれ",
          "どう"
        ],
        "correctIndex": 0,
        "grammarFocus": "Locational interrogative どこ",
        "ruleHint": "Inquiring about location of facilities.",
        "explanations": [
          {
            "text": "どこ",
            "isCorrect": true,
            "reason": "Correct! どこ is the place interrogative meaning 'where'."
          },
          {
            "text": "どれ",
            "isCorrect": false,
            "reason": "Incorrect. どれ means 'which item among 3+'."
          },
          {
            "text": "だれ",
            "isCorrect": false,
            "reason": "Incorrect. だれ means 'who'."
          },
          {
            "text": "どう",
            "isCorrect": false,
            "reason": "Incorrect. どう means 'how'."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L2",
      "Location",
      "Demonstratives"
    ]
  },
  {
    "id": "g1-l2-mo-particle",
    "title": "助詞「も」 (Inclusive Particle 'Also / Too')",
    "meaning": "Indicates inclusion: equates the predicate for a new topic to that of a previously mentioned entity ('X is also Y').",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 2: Shopping",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "Noun + も (Directly replaces は, が, or を!)",
    "nuance": "PARTICLE ABSORPTION: Particle も directly absorbs and replaces topic particle は and object particle を. You NEVER say 'はも' ❌ or 'をも' ❌!",
    "keyTakeaway": "MUG-UP: も replaces は and を completely! (私[は]学生です → 田中さん[も]学生です).",
    "sentences": [
      {
        "id": "s-g1-2-4",
        "japanese": "メアリーさんはアメリカ人です。ロバートさんもアメリカ人です。",
        "english": "Mary is an American. Robert is also an American.",
        "literal": "Mary topic American is. Robert also American is.",
        "tokens": [
          {
            "word": "ロバートさん",
            "meaning": "Robert",
            "reading": "ロバートさん",
            "romaji": "robaato-san",
            "pos": "Noun"
          },
          {
            "word": "も",
            "meaning": "also / too",
            "reading": "も",
            "romaji": "mo",
            "pos": "Particle"
          },
          {
            "word": "アメリカ人",
            "meaning": "American",
            "reading": "アメリカじん",
            "romaji": "amerika-jin",
            "pos": "Noun"
          }
        ],
        "nuanceNote": "も replaces は to establish shared national identity."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-2-4",
        "question": "私もその本（　　）読みました。とても面白かったです。",
        "translation": "I also read that book too.",
        "options": [
          "を",
          "も",
          "に",
          "で"
        ],
        "correctIndex": 1,
        "grammarFocus": "Particle も replacing direct object",
        "ruleHint": "Inclusive object marking.",
        "explanations": [
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. を is standard object marker without 'also'."
          },
          {
            "text": "も",
            "isCorrect": true,
            "reason": "Correct! も replaces を to express 'that book also'."
          },
          {
            "text": "に",
            "isCorrect": false,
            "reason": "Incorrect. に indicates direction/time."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. で indicates location/means."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L2",
      "Particle も",
      "Inclusion"
    ]
  },
  {
    "id": "g1-l2-janai-desu",
    "title": "じゃないです / じゃありません (Negative Copula: Is Not)",
    "meaning": "Polite non-past negative form of copula です: 'is not / am not / are not'.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 2: Shopping",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "Noun / な-adj + じゃないです (Conversational) / じゃありません (Formal)",
    "nuance": "REGISTER DIFFERENCE: じゃないです is standard polite spoken Japanese. じゃありません is slightly more formal. ではありません is conservative written/speech style.",
    "keyTakeaway": "MUG-UP: Negative of です is じゃないです (or じゃありません). Connects to nouns and な-adjectives.",
    "sentences": [
      {
        "id": "s-g1-2-5",
        "japanese": "山田さんは留学生じゃありません。先生です。",
        "english": "Yamada-san is not an international student. He is a teacher.",
        "literal": "Yamada topic international-student is-not. Teacher is.",
        "tokens": [
          {
            "word": "留学生",
            "meaning": "international student",
            "reading": "りゅうがくせい",
            "romaji": "ryuugakusei",
            "pos": "Noun"
          },
          {
            "word": "じゃありません",
            "meaning": "is not (polite neg)",
            "reading": "じゃありません",
            "romaji": "ja arimasen",
            "pos": "Copula"
          }
        ],
        "nuanceNote": "Polite denial of category followed by affirmative correction."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-2-5",
        "question": "私は一年生（　　）。三年生です。",
        "translation": "I am not a first-year student. I am a third-year student.",
        "options": [
          "じゃありません",
          "ありません",
          "ないでした",
          "でした"
        ],
        "correctIndex": 0,
        "grammarFocus": "Negative copula じゃありません",
        "ruleHint": "Negating noun identity.",
        "explanations": [
          {
            "text": "じゃありません",
            "isCorrect": true,
            "reason": "Correct! じゃありません (or じゃないです) is the polite negative copula for nouns."
          },
          {
            "text": "ありません",
            "isCorrect": false,
            "reason": "Incorrect. ありません is for inanimate existence (there isn't), not noun identity."
          },
          {
            "text": "ないでした",
            "isCorrect": false,
            "reason": "Incorrect. ないでした is ungrammatical."
          },
          {
            "text": "でした",
            "isCorrect": false,
            "reason": "Incorrect. でした is past affirmative ('was')."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L2",
      "Negation",
      "Copula"
    ]
  },
  {
    "id": "g1-l3-masu-form",
    "title": "〜ます / 〜ません (Polite Non-Past Affirmative & Negative)",
    "meaning": "The standard polite verbal ending for present habitual actions and future actions: 〜ます (affirmative) and 〜ません (negative).",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 3: Making a Date",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "Verb stem (ます-stem) + ます / ません",
    "nuance": "NON-PAST INCLUDES FUTURE: Japanese has only two grammatical tenses: past and non-past. 食べます means 'I eat (habitually)' OR 'I will eat (future)'.",
    "keyTakeaway": "MUG-UP: V-stem + ます = Present habit OR future plan. Negative = 〜ません.",
    "sentences": [
      {
        "id": "s-g1-3-1",
        "japanese": "私は毎朝コーヒーを飲みますが、お茶は飲みません。",
        "english": "I drink coffee every morning, but I do not drink tea.",
        "literal": "I every-morning coffee drink but, tea drink-not.",
        "tokens": [
          {
            "word": "飲みます",
            "meaning": "drink (polite)",
            "reading": "のみます",
            "romaji": "nomimasu",
            "pos": "Verb"
          },
          {
            "word": "飲みません",
            "meaning": "do not drink (polite neg)",
            "reading": "のみません",
            "romaji": "nomimasen",
            "pos": "Verb"
          }
        ],
        "nuanceNote": "Habitual affirmative and negative actions."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-3-1",
        "question": "明日は日曜日ですから、仕事へ（　　）。",
        "translation": "Since tomorrow is Sunday, I will not go to work.",
        "options": [
          "行きません",
          "行きます",
          "行きました",
          "行かないでした"
        ],
        "correctIndex": 0,
        "grammarFocus": "Polite non-past negative 〜ません",
        "ruleHint": "Future negation based on Sunday.",
        "explanations": [
          {
            "text": "行きません",
            "isCorrect": true,
            "reason": "Correct! 行きません is the polite non-past negative ('will not go')."
          },
          {
            "text": "行きます",
            "isCorrect": false,
            "reason": "Incorrect. 行きます is affirmative ('will go'), which contradicts Sunday."
          },
          {
            "text": "行きました",
            "isCorrect": false,
            "reason": "Incorrect. 行きました is past tense ('went')."
          },
          {
            "text": "行かないでした",
            "isCorrect": false,
            "reason": "Incorrect. 行かないでした is ungrammatical."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L3",
      "Verbs",
      "Polite Form"
    ]
  },
  {
    "id": "g1-l3-masenka-invitation",
    "title": "〜ませんか (Polite Invitation: Won't You? / Would You Like To?)",
    "meaning": "Invites the listener to do an activity together politely: 'Won't you...? / Would you like to...?'",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 3: Making a Date",
    "streamId": "stream-social",
    "streamName": "Social Hierarchy, Benefaction & Modesty",
    "connection": "V-stem (ます-stem) + ませんか",
    "nuance": "RESPECTFUL INVITATION: Asking negatively gives the listener psychological space to decline without awkwardness. Saying '映画に行きますか' is an informational check; '映画に行きませんか' is a warm date invitation.",
    "keyTakeaway": "MUG-UP: V-stem + ませんか = The golden Japanese polite invitation! (一緒に食べませんか = Won't you eat with me?).",
    "sentences": [
      {
        "id": "s-g1-3-2",
        "japanese": "今度の週末、一緒に美術館へ行きませんか。「ええ、ぜひ！」",
        "english": "Won't you go to the art museum together this coming weekend? 'Yes, by all means!'",
        "literal": "This-time's weekend, together art-museum go-won't-you? Yes, definitely!",
        "tokens": [
          {
            "word": "行きませんか",
            "meaning": "won't you go? (invitation)",
            "reading": "いきませんか",
            "romaji": "ikimasen ka",
            "pos": "Verb+Grammar"
          },
          {
            "word": "ぜひ",
            "meaning": "by all means / definitely",
            "reading": "ぜひ",
            "romaji": "zehi",
            "pos": "Adverb"
          }
        ],
        "nuanceNote": "Warm invitation paired with enthusiastic agreement."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-3-2",
        "question": "少し疲れましたね。喫茶店でお茶を（　　）ませんか。",
        "translation": "We've gotten a bit tired, haven't we? Won't you drink some tea at a cafe?",
        "options": [
          "飲み",
          "飲む",
          "飲んで",
          "飲ま"
        ],
        "correctIndex": 0,
        "grammarFocus": "Polite invitation 〜ませんか with verb stem",
        "ruleHint": "Proposing a cafe rest.",
        "explanations": [
          {
            "text": "飲み",
            "isCorrect": true,
            "reason": "Correct! 飲む stem is 飲み, connecting to ませんか (飲みませんか)."
          },
          {
            "text": "飲む",
            "isCorrect": false,
            "reason": "Incorrect. 飲む is dictionary form; cannot connect to ませんか."
          },
          {
            "text": "飲んで",
            "isCorrect": false,
            "reason": "Incorrect. 飲んで is te-form."
          },
          {
            "text": "飲ま",
            "isCorrect": false,
            "reason": "Incorrect. 飲ま is negative stem."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L3",
      "Invitation",
      "Social"
    ]
  },
  {
    "id": "g1-l4-past-forms-deshita",
    "title": "〜ました・〜ませんでした・〜でした (Polite Past Tense of Verbs & Copula)",
    "meaning": "Past tense for verbs (〜ました / 〜ませんでした) and noun/adjectival predicates (〜でした / 〜じゃありませんでした).",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 4: The First Date",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "Verb stem + ました / ませんでした | Noun / な-adj + でした / じゃありませんでした",
    "nuance": "COPULA PAST NEGATIVE: In polite conversation, you can say either じゃありませんでした or じゃないでした / じゃなかったです.",
    "keyTakeaway": "MUG-UP: Verb past = ました. Verb past negative = ませんでした. Noun past = でした.",
    "sentences": [
      {
        "id": "s-g1-4-1",
        "japanese": "昨日は雨でした。私はどこへも行きませんでした。",
        "english": "Yesterday was rainy. I did not go anywhere.",
        "literal": "Yesterday rain was. I anywhere go-past-neg.",
        "tokens": [
          {
            "word": "雨でした",
            "meaning": "was rain",
            "reading": "あめでした",
            "romaji": "ame deshita",
            "pos": "Noun+Copula"
          },
          {
            "word": "行きませんでした",
            "meaning": "did not go",
            "reading": "いきませんでした",
            "romaji": "ikimasen deshita",
            "pos": "Verb"
          }
        ],
        "nuanceNote": "Past state of weather and past negation of activity."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-4-1",
        "question": "昨夜は十二時まで日本語を（　　）。とても眠かったです。",
        "translation": "Last night I studied Japanese until 12 o'clock. I was very sleepy.",
        "options": [
          "勉強しました",
          "勉強します",
          "勉強でした",
          "勉強しでした"
        ],
        "correctIndex": 0,
        "grammarFocus": "Verb past tense 〜ました",
        "ruleHint": "Completed past study action.",
        "explanations": [
          {
            "text": "勉強しました",
            "isCorrect": true,
            "reason": "Correct! 勉強する past form is 勉強しました."
          },
          {
            "text": "勉強します",
            "isCorrect": false,
            "reason": "Incorrect. 勉強します is present/future non-past."
          },
          {
            "text": "勉強でした",
            "isCorrect": false,
            "reason": "Incorrect. 勉強でした uses copula past without verb inflection."
          },
          {
            "text": "勉強しでした",
            "isCorrect": false,
            "reason": "Incorrect. 勉強しでした is ungrammatical hybrid."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L4",
      "Past Tense",
      "Verbs"
    ]
  },
  {
    "id": "g1-l4-location-words",
    "title": "位置の名詞 (Spatial Postpositions: 上・下・前・後ろ・中・隣・近く・間)",
    "meaning": "Spatial relational nouns indicating position relative to a reference point: X の [上/下/前/後ろ/中/隣/間] に.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 4: The First Date",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "Reference Noun + の + [上 / 下 / 前 / 後ろ / 中 / 隣 / 近く / 間] + に",
    "nuance": "TONARI VS CHIKAKU: 隣 (となり) is strictly adjacent of the same category (next to). 近く (ちかく) is in the general vicinity. 間 (あいだ) requires two bounds (A と B の間).",
    "keyTakeaway": "MUG-UP: [Object] の [Position] に. (机の[上]に = On top of the desk).",
    "sentences": [
      {
        "id": "s-g1-4-2",
        "japanese": "猫が机の下で寝ています。銀行は郵便局と本屋の間にあります。",
        "english": "A cat is sleeping under the desk. The bank is between the post office and bookstore.",
        "literal": "Cat desk-under sleeping-is. Bank post-office and bookstore's between exists.",
        "tokens": [
          {
            "word": "机の下で",
            "meaning": "under the desk",
            "reading": "つくえのしたで",
            "romaji": "tsukue no shita de",
            "pos": "Noun+Postposition"
          },
          {
            "word": "間にあります",
            "meaning": "exists between",
            "reading": "あいだにあります",
            "romaji": "aida ni arimasu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Relational location followed by action/existence verbs."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-4-2",
        "question": "私の部屋の鍵は、カバンの（　　）にあります。",
        "translation": "My room key is inside my bag.",
        "options": [
          "中",
          "上",
          "前",
          "間"
        ],
        "correctIndex": 0,
        "grammarFocus": "Spatial noun 中 (inside)",
        "ruleHint": "Location of keys inside the bag.",
        "explanations": [
          {
            "text": "中",
            "isCorrect": true,
            "reason": "Correct! 中 (なか) means 'inside'."
          },
          {
            "text": "上",
            "isCorrect": false,
            "reason": "Incorrect. 上 means 'on top of'."
          },
          {
            "text": "前",
            "isCorrect": false,
            "reason": "Incorrect. 前 means 'in front of'."
          },
          {
            "text": "間",
            "isCorrect": false,
            "reason": "Incorrect. 間 means 'between two entities'."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L4",
      "Spatial",
      "Positions"
    ]
  },
  {
    "id": "g1-l5-suki-kirai",
    "title": "好き（な） / 嫌い（な） (Expressing Likes and Dislikes with が)",
    "meaning": "Expresses fondness (好き) or aversion (嫌い): marked with particle が on the object of emotion, NOT を!",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 5: A Trip to Okinawa",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "[Person] は [Item] が 好きです / 嫌いです (Adjectival predicates)",
    "nuance": "PARTICLE TRAP: In English 'like' is a transitive verb (I like X). In Japanese, 好き is a な-adjective (X is pleasing to me), so the item takes particle が (NOT を ❌)!",
    "keyTakeaway": "MUG-UP: [Noun] が 好きです / 嫌いです! Never use を with 好き/嫌い!",
    "sentences": [
      {
        "id": "s-g1-5-1",
        "japanese": "私は辛い食べ物が大好きですが、甘いお菓子はあまり好きじゃありません。",
        "english": "I love spicy food, but I don't like sweet snacks very much.",
        "literal": "I spicy food like-very but, sweet snacks not-very like-not.",
        "tokens": [
          {
            "word": "食べ物が",
            "meaning": "food (target)",
            "reading": "たべものが",
            "romaji": "tabemono ga",
            "pos": "Noun+Particle"
          },
          {
            "word": "大好きですが",
            "meaning": "love it, but",
            "reading": "だいすきですが",
            "romaji": "daisuki desu ga",
            "pos": "Adjective"
          }
        ],
        "nuanceNote": "Target of affection marked with が."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-5-1",
        "question": "ロバートさんは日本の歴史（　　）とても好きです。",
        "translation": "Robert-san likes Japanese history very much.",
        "options": [
          "が",
          "を",
          "に",
          "で"
        ],
        "correctIndex": 0,
        "grammarFocus": "Object marker が with 好き",
        "ruleHint": "Marking the target of fondness.",
        "explanations": [
          {
            "text": "が",
            "isCorrect": true,
            "reason": "Correct! Target of 好き requires particle が."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. を is an English calque trap; 好き is an adjective, not a transitive verb."
          },
          {
            "text": "に",
            "isCorrect": false,
            "reason": "Incorrect. に indicates direction/time."
          },
          {
            "text": "で",
            "isCorrect": false,
            "reason": "Incorrect. で indicates location/means."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L5",
      "Preferences",
      "Particle が"
    ]
  },
  {
    "id": "g1-l5-mashou-ka",
    "title": "〜ましょう / 〜ましょうか (Volitional Suggestion: Let's / Shall We?)",
    "meaning": "Proposes action enthusiastically: 〜ましょう ('Let's do it!') or offers assistance/mutual decision: 〜ましょうか ('Shall we do it? / Shall I help?').",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 5: A Trip to Okinawa",
    "streamId": "stream-social",
    "streamName": "Social Hierarchy, Benefaction & Modesty",
    "connection": "V-stem (ます-stem) + ましょう / ましょうか",
    "nuance": "TWO USES OF 〜ましょうか: 1) Suggesting mutual action ('Shall we take a break?'). 2) Offering personal assistance ('Shall I carry your bag?').",
    "keyTakeaway": "MUG-UP: V-stem + ましょう = Let's do it! V-stem + ましょうか = Shall we? / Shall I help?",
    "sentences": [
      {
        "id": "s-g1-5-2",
        "japanese": "荷物が重そうですね。手伝いましょうか。「ありがとうございます！」",
        "english": "Your luggage looks heavy. Shall I help you? 'Thank you so much!'",
        "literal": "Luggage heavy-looks. Shall-I-help? Thank-you!",
        "tokens": [
          {
            "word": "手伝いましょうか",
            "meaning": "shall I help?",
            "reading": "てつだいましょうか",
            "romaji": "tetsudaimashou ka",
            "pos": "Verb+Grammar"
          }
        ],
        "nuanceNote": "Offering courteous assistance to someone in need."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-5-2",
        "question": "雨が止みましたね。公園を少し（　　）ましょう。",
        "translation": "The rain has stopped, hasn't it? Let's take a walk in the park for a bit.",
        "options": [
          "散歩し",
          "散歩する",
          "散歩して",
          "散歩した"
        ],
        "correctIndex": 0,
        "grammarFocus": "Suggestion 〜ましょう with verb stem",
        "ruleHint": "Proposing a walk together.",
        "explanations": [
          {
            "text": "散歩し",
            "isCorrect": true,
            "reason": "Correct! 散歩する stem is 散歩し + ましょう (散歩しましょう = Let's take a walk)."
          },
          {
            "text": "散歩する",
            "isCorrect": false,
            "reason": "Incorrect. 散歩する is dictionary form."
          },
          {
            "text": "散歩して",
            "isCorrect": false,
            "reason": "Incorrect. 散歩して is te-form."
          },
          {
            "text": "散歩した",
            "isCorrect": false,
            "reason": "Incorrect. 散歩した is past form."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L5",
      "Volitional",
      "Suggestions"
    ]
  },
  {
    "id": "g1-l6-te-kudasai",
    "title": "〜てください (Polite Request: Please Do)",
    "meaning": "Politely instructs or requests the listener to perform an action for instruction, guidance, or courtesy: 'Please do X'.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 6: A Day in Robert's Life",
    "streamId": "stream-social",
    "streamName": "Social Hierarchy, Benefaction & Modesty",
    "connection": "V-て + ください",
    "nuance": "REGISTER WARNING: Because ください carries an underlying mild command tone ('do this for me'), saying it to high superiors (professors, boss, clients) can sound overly direct. Use 〜ていただけませんか instead.",
    "keyTakeaway": "MUG-UP: V-て + ください = Please do X. Connects strictly to te-form!",
    "sentences": [
      {
        "id": "s-g1-6-1",
        "japanese": "教科書の三十五ページを開けてください。",
        "english": "Please open your textbook to page 35.",
        "literal": "Textbook's 35-page open please.",
        "tokens": [
          {
            "word": "開けてください",
            "meaning": "please open",
            "reading": "あけてください",
            "romaji": "akete kudasai",
            "pos": "Verb+Grammar"
          }
        ],
        "nuanceNote": "Standard classroom instructional request."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-6-1",
        "question": "ここにあなたのお名前と電話番号を（　　）ください。",
        "translation": "Please write your name and phone number here.",
        "options": [
          "書いて",
          "書く",
          "書き",
          "書いた"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-て + ください polite request",
        "ruleHint": "Requesting writing information.",
        "explanations": [
          {
            "text": "書いて",
            "isCorrect": true,
            "reason": "Correct! 書く connects via te-form 書いて + ください."
          },
          {
            "text": "書く",
            "isCorrect": false,
            "reason": "Incorrect. 書く is dictionary form."
          },
          {
            "text": "書き",
            "isCorrect": false,
            "reason": "Incorrect. 書き is masu-stem."
          },
          {
            "text": "書いた",
            "isCorrect": false,
            "reason": "Incorrect. 書いた is past form."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L6",
      "Requests",
      "Te-Form"
    ]
  },
  {
    "id": "g1-l6-te-mo-ii",
    "title": "〜てもいいですか (Asking for & Granting Permission: May I?)",
    "meaning": "Asking for permission: 'May I do X?' (〜てもいいですか). Granting permission: 'You may do X' (〜てもいいです).",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 6: A Day in Robert's Life",
    "streamId": "stream-social",
    "streamName": "Social Hierarchy, Benefaction & Modesty",
    "connection": "V-て + もいいですか / もいいです",
    "nuance": "LITERAL MEANING: 〜ても (even if I do) + いい (it is good). 'Even if I open the window, is it fine?'",
    "keyTakeaway": "MUG-UP: V-て + もいいですか = May I do this? Granting: V-て + もいいですよ.",
    "sentences": [
      {
        "id": "s-g1-6-2",
        "japanese": "部屋が少し暑いですね。窓を開けてもいいですか。「ええ、どうぞ。」",
        "english": "The room is a bit hot, isn't it? May I open the window? 'Yes, please go ahead.'",
        "literal": "Room slightly hot is. Window open-even-if good is question? Yes, please.",
        "tokens": [
          {
            "word": "開けてもいいですか",
            "meaning": "may I open it?",
            "reading": "あけてもいいですか",
            "romaji": "akete mo ii desu ka",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Courteous permission query before altering shared environment."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-6-2",
        "question": "このペンを少しの間、（　　）てもいいですか。",
        "translation": "May I borrow this pen for a brief moment?",
        "options": [
          "借り",
          "借る",
          "借りて",
          "借りた"
        ],
        "correctIndex": 0,
        "grammarFocus": "Permission formula 〜てもいいですか",
        "ruleHint": "Borrowing an item politely.",
        "explanations": [
          {
            "text": "借り",
            "isCorrect": true,
            "reason": "Correct! 借りる is a Ru-verb: stem 借り + てもいいですか (借りてもいいですか)."
          },
          {
            "text": "借る",
            "isCorrect": false,
            "reason": "Incorrect. 借る is an archaic form."
          },
          {
            "text": "借りて",
            "isCorrect": false,
            "reason": "Incorrect. 借りて already has て; adding another てもいい creates '借りてても'."
          },
          {
            "text": "借りた",
            "isCorrect": false,
            "reason": "Incorrect. 借りた is past form."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L6",
      "Permission",
      "Te-Form"
    ]
  },
  {
    "id": "g1-l6-kara-reason",
    "title": "〜から (Stating Reasons / Because - Clause Linker)",
    "meaning": "States a subjective explanation or cause: 'Because of X, Y happens' or 'Y happens because of X'.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 6: A Day in Robert's Life",
    "streamId": "stream-causality",
    "streamName": "Causal Chains & Regret",
    "connection": "Sentence 1 (Reason) + から、 Sentence 2 (Conclusion)",
    "nuance": "SUBJECTIVE CONVICTION: から represents the speaker's personal logic and subjective view. It can be paired directly with commands, requests, and volitions (雨が降っているから、傘を持って行きなさい).",
    "keyTakeaway": "MUG-UP: [Reason] から、[Result]. Unlike English, the reason comes FIRST!",
    "sentences": [
      {
        "id": "s-g1-6-3",
        "japanese": "今日は大事なテストがありますから、早く寝ます。",
        "english": "Because I have an important test today, I will go to bed early.",
        "literal": "Today important test have because, early sleep.",
        "tokens": [
          {
            "word": "ありますから",
            "meaning": "because I have",
            "reading": "ありますから",
            "romaji": "arimasu kara",
            "pos": "Verb+Particle"
          },
          {
            "word": "早く寝ます",
            "meaning": "will sleep early",
            "reading": "はやくねます",
            "romaji": "hayaku nemasu",
            "pos": "Adverb+Verb"
          }
        ],
        "nuanceNote": "Reason precedes the resulting decision."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-6-3",
        "question": "明日は朝早く起きます（　　）、今夜はテレビを見ません。",
        "translation": "Because I will wake up early tomorrow morning, I won't watch television tonight.",
        "options": [
          "から",
          "まで",
          "より",
          "ほど"
        ],
        "correctIndex": 0,
        "grammarFocus": "Causal clause linker から",
        "ruleHint": "Explaining the reason for an early night.",
        "explanations": [
          {
            "text": "から",
            "isCorrect": true,
            "reason": "Correct! から links the reason for abstaining from TV."
          },
          {
            "text": "まで",
            "isCorrect": false,
            "reason": "Incorrect. まで means 'until'."
          },
          {
            "text": "より",
            "isCorrect": false,
            "reason": "Incorrect. より indicates comparison."
          },
          {
            "text": "ほど",
            "isCorrect": false,
            "reason": "Incorrect. ほど indicates degree or proportion."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L6",
      "Causality",
      "Reason"
    ]
  },
  {
    "id": "g1-l7-describing-people",
    "title": "身体の描写 (Describing People's Physical Attributes: 目が大きいです)",
    "meaning": "Formula for describing a person's physical features: [Person] は [Body Part] が [Adjective] です ('As for X, their eyes are big').",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 7: Family Picture",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "[Person] は + [Body Part] が + [Adjective] です",
    "nuance": "AVOID NOUN OF NOUN FOR BODY PARTS: In English we say 'Mary's hair is long'. In Japanese, 'メアリーさんの髪は長いです' sounds stiff; native syntax frames the person as topic: 'メアリーさんは髪が長いです'.",
    "keyTakeaway": "MUG-UP: [Person] は [Body part] が [Adjective]! (トムさんは背が高い = Tom is tall).",
    "sentences": [
      {
        "id": "s-g1-7-1",
        "japanese": "私の妹は目が大きくて、髪が長いです。",
        "english": "My younger sister has big eyes and long hair.",
        "literal": "My younger-sister eyes big-and, hair long-is.",
        "tokens": [
          {
            "word": "妹は",
            "meaning": "younger sister",
            "reading": "いもうとは",
            "romaji": "imouto wa",
            "pos": "Noun+Particle"
          },
          {
            "word": "目が大きくて",
            "meaning": "eyes are big and",
            "reading": "めがおおきくて",
            "romaji": "me ga ookikute",
            "pos": "Grammar"
          },
          {
            "word": "髪が長いです",
            "meaning": "hair is long",
            "reading": "かみがながいです",
            "romaji": "kami ga nagai desu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Natural Japanese body description framing."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-7-1",
        "question": "田中さんはとても背（　　）高いです。",
        "translation": "Tanaka-san is very tall.",
        "options": [
          "が",
          "は",
          "を",
          "に"
        ],
        "correctIndex": 0,
        "grammarFocus": "Physical attribute marker が (背が高い)",
        "ruleHint": "Describing height with が.",
        "explanations": [
          {
            "text": "が",
            "isCorrect": true,
            "reason": "Correct! Body attribute takes particle が (背が高い)."
          },
          {
            "text": "は",
            "isCorrect": false,
            "reason": "Incorrect. は is already used for Tanaka-san as topic."
          },
          {
            "text": "を",
            "isCorrect": false,
            "reason": "Incorrect. を is direct object marker."
          },
          {
            "text": "に",
            "isCorrect": false,
            "reason": "Incorrect. に indicates destination/time."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L7",
      "Description",
      "Attributes"
    ]
  },
  {
    "id": "g1-l7-adj-te-forms",
    "title": "形容詞・名詞の「て形」 (Connecting Adjectives & Nouns: 〜くて / 〜で)",
    "meaning": "Links multiple qualities or attributes: い-adjectives change final い to くて; な-adjectives and nouns take で.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 7: Family Picture",
    "streamId": "stream-contrasts",
    "streamName": "Contrasts, Concessions & Paradoxes",
    "connection": "い-adj (drop い) + くて | な-adj stem + で | Noun + で",
    "nuance": "THE II/YOI TE-FORM: いい (good) drops its irregular root and conjugates as よくて (NOT いくて ❌)! な-adjectives take で, exactly like nouns.",
    "keyTakeaway": "MUG-UP: い-adj = 〜くて (いい→よくて). な-adj / Noun = 〜で.",
    "sentences": [
      {
        "id": "s-g1-7-2",
        "japanese": "この部屋は広くて明るくて、とても静かです。",
        "english": "This room is spacious, bright, and very quiet.",
        "literal": "This room spacious-and bright-and, very quiet-is.",
        "tokens": [
          {
            "word": "広くて",
            "meaning": "spacious and",
            "reading": "ひろくて",
            "romaji": "hirokute",
            "pos": "Adjective"
          },
          {
            "word": "明るくて",
            "meaning": "bright and",
            "reading": "あかるくて",
            "romaji": "akarukute",
            "pos": "Adjective"
          },
          {
            "word": "静かです",
            "meaning": "is quiet",
            "reading": "しずかです",
            "romaji": "shizuka desu",
            "pos": "Adjective"
          }
        ],
        "nuanceNote": "Chaining two い-adjectives via くて into a terminal な-adjective."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-7-2",
        "question": "あのカフェはコーヒーが（　　）、値段も安いです。",
        "translation": "That cafe's coffee is delicious, and the price is also cheap.",
        "options": [
          "おいしくて",
          "おいしいで",
          "おいしくで",
          "おいしいくて"
        ],
        "correctIndex": 0,
        "grammarFocus": "い-adjective te-form 〜くて",
        "ruleHint": "Connecting two positive attributes.",
        "explanations": [
          {
            "text": "おいしくて",
            "isCorrect": true,
            "reason": "Correct! おいしい drops い + くて = おいしくて."
          },
          {
            "text": "おいしいで",
            "isCorrect": false,
            "reason": "Incorrect. おいしいで incorrectly applies noun/na-adj で to an い-adj."
          },
          {
            "text": "おいしくで",
            "isCorrect": false,
            "reason": "Incorrect. おいしくで is ungrammatical."
          },
          {
            "text": "おいしいくて",
            "isCorrect": false,
            "reason": "Incorrect. おいしいくて fails to drop the initial い."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L7",
      "Adjectives",
      "Te-Form"
    ]
  },
  {
    "id": "g1-l7-purpose-ni-iku",
    "title": "V-stem + に行く / に来る (Purpose of Movement: Going to Do)",
    "meaning": "Expresses the specific purpose of movement: going (行く), coming (来る), or returning (帰る) in order to perform an action.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 7: Family Picture",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-stem (ます-stem) + に + 行く / 来る / 帰る | Activity Noun + に + 行く",
    "nuance": "VERB STEM BEFORE に: Drop ます and append に directly: 食べます → 食べに行く, 買いに行きます. If using an activity noun (買い物, 散歩), attach に directly: 買い物に行く.",
    "keyTakeaway": "MUG-UP: [Masu-stem] に行く = Going to DO X. Purpose particle is STRICTLY に!",
    "sentences": [
      {
        "id": "s-g1-7-3",
        "japanese": "デパートへ友達の誕生日プレゼントを買いに行きました。",
        "english": "I went to the department store to buy a birthday present for my friend.",
        "literal": "Department-store friend's birthday present buy-in-order-to went.",
        "tokens": [
          {
            "word": "買いに行きました",
            "meaning": "went to buy",
            "reading": "かいにいきました",
            "romaji": "kai ni ikimashita",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "買う (stem 買い) + に行きました."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-7-3",
        "question": "週末は図書館へ本を（　　）に行きます。",
        "translation": "On weekends I go to the library to return books.",
        "options": [
          "返し",
          "返す",
          "返して",
          "返した"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-stem + に行く purpose of movement",
        "ruleHint": "Going to return library books.",
        "explanations": [
          {
            "text": "返し",
            "isCorrect": true,
            "reason": "Correct! 返す (to return an item) stem is 返し + に行きます."
          },
          {
            "text": "返す",
            "isCorrect": false,
            "reason": "Incorrect. 返す is dictionary form."
          },
          {
            "text": "返して",
            "isCorrect": false,
            "reason": "Incorrect. 返して is te-form."
          },
          {
            "text": "返した",
            "isCorrect": false,
            "reason": "Incorrect. 返した is past form."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L7",
      "Movement",
      "Purpose"
    ]
  },
  {
    "id": "g1-l8-nai-de-kudasai",
    "title": "〜ないでください (Negative Request: Please Do Not)",
    "meaning": "Politely requests or instructs someone to refrain from an action: 'Please do not do X'.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 8: Barbecue",
    "streamId": "stream-social",
    "streamName": "Social Hierarchy, Benefaction & Modesty",
    "connection": "V-ない + でください",
    "nuance": "NEGATIVE POLITE REQUEST: Formed from the plain negative ない-form + でください. Very common on signs, exams, and courteous instructions (忘れないでください).",
    "keyTakeaway": "MUG-UP: V-ない + でください = Please don't do X! (Drop nothing from ない).",
    "sentences": [
      {
        "id": "s-g1-8-1",
        "japanese": "図書館の中では大声で話さないでください。",
        "english": "Please do not speak in a loud voice inside the library.",
        "literal": "Library inside loud-voice-in speak-not-please.",
        "tokens": [
          {
            "word": "話さないでください",
            "meaning": "please do not speak",
            "reading": "はなさないでください",
            "romaji": "hanasanaide kudasai",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "話す negative 話さない + でください."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-8-1",
        "question": "まだテスト中ですから、教室から（　　）ないでください。",
        "translation": "Since the test is still ongoing, please do not leave the classroom.",
        "options": [
          "出",
          "出る",
          "出て",
          "出な"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-ない + でください negative request",
        "ruleHint": "Requesting students remain in room.",
        "explanations": [
          {
            "text": "出",
            "isCorrect": true,
            "reason": "Correct! 出る (Ru-verb) negative is 出ない + でください (出ないでください)."
          },
          {
            "text": "出る",
            "isCorrect": false,
            "reason": "Incorrect. 出るない is false conjugation."
          },
          {
            "text": "出て",
            "isCorrect": false,
            "reason": "Incorrect. 出て is te-form."
          },
          {
            "text": "出な",
            "isCorrect": false,
            "reason": "Incorrect. 出な is ungrammatical."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L8",
      "Requests",
      "Negation"
    ]
  },
  {
    "id": "g1-l8-nominalizer-no",
    "title": "動詞の「の」名詞化 (Nominalizing Verbs with の: のが好き / 上手 / 下手)",
    "meaning": "Turns an action verb into a noun phrase using の, enabling evaluations of preference or skill: V-plain + のが好き / 上手 / 下手.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 8: Barbecue",
    "streamId": "stream-topics",
    "streamName": "Topic Framing, Criteria & Disregard",
    "connection": "V-辞書形 + のが [好き / 嫌い / 上手 / 下手 / 得意 / 苦手] です",
    "nuance": "NOMINALIZATION REQUIREMENT: In Japanese you cannot attach が directly to a verb ('食べるが好き' ❌). You must nominalize it with の ('食べるのが好き').",
    "keyTakeaway": "MUG-UP: [Verb-Dictionary] + のが + 好き / 上手 / 下手! The particle の acts as 'the act of'.",
    "sentences": [
      {
        "id": "s-g1-8-2",
        "japanese": "私はギターを弾くのが大好きですが、歌を歌うのはあまり上手ではありません。",
        "english": "I love playing the guitar, but I am not very good at singing songs.",
        "literal": "I guitar play-nominalizer like-very but, songs sing-nominalizer not-very good is-not.",
        "tokens": [
          {
            "word": "弾くのが大好き",
            "meaning": "love playing",
            "reading": "ひくのがだいすき",
            "romaji": "hiku no ga daisuki",
            "pos": "Grammar"
          },
          {
            "word": "歌うのは",
            "meaning": "as for singing",
            "reading": "うたうのは",
            "romaji": "utau no wa",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Nominalizing musical instruments and singing."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-8-2",
        "question": "母は料理を（　　）のがとても上手です。",
        "translation": "My mother is very good at cooking meals.",
        "options": [
          "作る",
          "作って",
          "作り",
          "作った"
        ],
        "correctIndex": 0,
        "grammarFocus": "Nominalization V-辞書形 + の",
        "ruleHint": "Skill appraisal in cooking.",
        "explanations": [
          {
            "text": "作る",
            "isCorrect": true,
            "reason": "Correct! V-辞書形 作る connects to nominalizer の (作るのが上手)."
          },
          {
            "text": "作って",
            "isCorrect": false,
            "reason": "Incorrect. 作って is te-form."
          },
          {
            "text": "作り",
            "isCorrect": false,
            "reason": "Incorrect. 作り is masu-stem."
          },
          {
            "text": "作った",
            "isCorrect": false,
            "reason": "Incorrect. 作った is past form."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L8",
      "Nominalization",
      "Skills"
    ]
  },
  {
    "id": "g1-l9-mou-mada",
    "title": "もう〜ました vs まだ〜ていません (Already Done vs Have Not Yet Done)",
    "meaning": "もう〜ました (Action has already been completed). まだ〜ていません (Action has not yet taken place; still in uncompleted state).",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 9: Kabuki",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "もう + V-ました | まだ + V-ていません (NOT まだ〜ませんでした ❌!)",
    "nuance": "CRITICAL NEGATIVE TRAP: To say 'I haven't eaten yet', you CANNOT say 'まだ食べませんでした' ❌! Past negative implies you never intended to eat. You must say 'まだ食べていません' (still in state of not having eaten).",
    "keyTakeaway": "MUG-UP: Haven't done yet = まだ + [Te-form] + いません! Never use past negative with まだ!",
    "sentences": [
      {
        "id": "s-g1-9-1",
        "japanese": "宿題はもう終わりましたか。「いいえ、まだ終わっていません。」",
        "english": "Have you finished your homework already? 'No, I have not finished it yet.'",
        "literal": "Homework already finished? No, still finished-state-not.",
        "tokens": [
          {
            "word": "もう終わりましたか",
            "meaning": "already finished?",
            "reading": "もうおわりましたか",
            "romaji": "mou owarimashita ka",
            "pos": "Grammar"
          },
          {
            "word": "まだ終わっていません",
            "meaning": "have not finished yet",
            "reading": "まだおわっていません",
            "romaji": "mada owatte imasen",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Canonical pairing of もう with past vs まだ with progressive negative."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-9-1",
        "question": "昼ご飯はもう食べましたか。「いいえ、まだ（　　）。」",
        "translation": "Did you eat lunch already? 'No, I haven't eaten yet.'",
        "options": [
          "食べていません",
          "食べませんでした",
          "食べません",
          "食べないでした"
        ],
        "correctIndex": 0,
        "grammarFocus": "まだ + V-ていません (Not yet)",
        "ruleHint": "Replying that lunch hasn't occurred yet.",
        "explanations": [
          {
            "text": "食べていません",
            "isCorrect": true,
            "reason": "Correct! まだ takes progressive negative 食べていません ('have not eaten yet')."
          },
          {
            "text": "食べませんでした",
            "isCorrect": false,
            "reason": "Incorrect. 食べませんでした means you didn't eat at all in the past, rather than not yet."
          },
          {
            "text": "食べません",
            "isCorrect": false,
            "reason": "Incorrect. 食べません is present habitual refusal."
          },
          {
            "text": "食べないでした",
            "isCorrect": false,
            "reason": "Incorrect. 食べないでした is ungrammatical."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L9",
      "Aspect",
      "Time"
    ]
  },
  {
    "id": "g1-l10-tsumori",
    "title": "〜つもりだ / つもりです (Stated Personal Intention: Plan To)",
    "meaning": "States a conscious, determined personal intention or plan: 'I intend to / I plan to do X'.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 10: Winter Vacations Approaching",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "V-辞書形 + つもりです (Affirmative plan) | V-ない + つもりです / つもりはありません (Negative plan)",
    "nuance": "FIRST/SECOND PERSON ONLY: In polite conversation, つもり states your own plans. Attributing つもり directly to superiors can sound rude because it presumes to know their internal mental intent.",
    "keyTakeaway": "MUG-UP: V-る + つもりです = I intend to do X. Negative: V-ない + つもりです.",
    "sentences": [
      {
        "id": "s-g1-10-1",
        "japanese": "大学を卒業したら、日本の大学院に進学するつもりです。",
        "english": "Upon graduating from college, I intend to advance to graduate school in Japan.",
        "literal": "College graduate-when, Japan's grad-school advance intend.",
        "tokens": [
          {
            "word": "進学するつもりです",
            "meaning": "intend to advance to higher education",
            "reading": "しんがくするつもりです",
            "romaji": "shingaku suru tsumori desu",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Stating personal academic career intent."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-10-1",
        "question": "今年の夏休みは、どこへも旅行に（　　）つもりです。家で勉強します。",
        "translation": "This summer vacation, I intend not to travel anywhere. I will study at home.",
        "options": [
          "行かない",
          "行く",
          "行かないで",
          "行った"
        ],
        "correctIndex": 0,
        "grammarFocus": "Negative intention V-ない + つもりだ",
        "ruleHint": "Intending to stay home.",
        "explanations": [
          {
            "text": "行かない",
            "isCorrect": true,
            "reason": "Correct! Negative intention connects via ない-form: 行かないつもりです."
          },
          {
            "text": "行く",
            "isCorrect": false,
            "reason": "Incorrect. 行く indicates affirmative intent to travel."
          },
          {
            "text": "行かないで",
            "isCorrect": false,
            "reason": "Incorrect. 行かないで is te-form."
          },
          {
            "text": "行った",
            "isCorrect": false,
            "reason": "Incorrect. 行った is past form."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L10",
      "Intention",
      "Plans"
    ]
  },
  {
    "id": "g1-l10-adj-naru",
    "title": "形容詞 + なる (Expressing Change of State: To Become)",
    "meaning": "Describes a natural or progressive change of state: 'to become [adjective]' (growing warm, becoming quiet, turning into an adult).",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 10: Winter Vacations Approaching",
    "streamId": "stream-trends",
    "streamName": "Trends, Changes & Proportional Evolution",
    "connection": "い-adj (drop い) + くなる | な-adj stem + になる | Noun + になる",
    "nuance": "ADVERBIAL INFLECTION: い-adjectives change final い to く before なる (暖かくなる). な-adjectives and nouns take に before なる (静かになる, 先生になる).",
    "keyTakeaway": "MUG-UP: い-adj = 〜くなる (暑くなる). な-adj / Noun = 〜になる (元気になる, 医者になる).",
    "sentences": [
      {
        "id": "s-g1-10-2",
        "japanese": "春になって、だんだん暖かくなってきましたね。",
        "english": "Spring has arrived, and it has gradually become warm, hasn't it?",
        "literal": "Spring become, gradually warm became-came.",
        "tokens": [
          {
            "word": "春になって",
            "meaning": "became spring and",
            "reading": "はるになって",
            "romaji": "haru ni natte",
            "pos": "Grammar"
          },
          {
            "word": "暖かくなってきました",
            "meaning": "has become warm",
            "reading": "あたたかくなってきました",
            "romaji": "atatakaku natte kimashita",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Noun + になる and い-adj + くなる."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-10-2",
        "question": "薬を飲んだら、痛みがだいぶ（　　）なりました。",
        "translation": "After taking the medicine, the pain became considerably better.",
        "options": [
          "よく",
          "いいに",
          "よくに",
          "いいく"
        ],
        "correctIndex": 0,
        "grammarFocus": "Change of state with いい (よくなる)",
        "ruleHint": "Pain improving after medicine.",
        "explanations": [
          {
            "text": "よく",
            "isCorrect": true,
            "reason": "Correct! いい changes through root よい to become adverbial よく + なりました."
          },
          {
            "text": "いいに",
            "isCorrect": false,
            "reason": "Incorrect. いいに is ungrammatical; い-adjectives take く."
          },
          {
            "text": "よくに",
            "isCorrect": false,
            "reason": "Incorrect. よくに is double adverbial marking."
          },
          {
            "text": "いいく",
            "isCorrect": false,
            "reason": "Incorrect. いいく is invalid root conjugation."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L10",
      "Change of State",
      "Trends"
    ]
  },
  {
    "id": "g1-l11-tai-desire",
    "title": "〜たい / 〜たくない (Expressing Desire to Do: Want to Do)",
    "meaning": "Expresses first-person desire to perform an action: 'I want to do X'. Negative: 'I do not want to do X' (〜たくない).",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 11: After-Vacation Plans",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "V-stem (ます-stem) + たい (Conjugates 100% as an い-adjective: 〜たくない, 〜たかった)",
    "nuance": "PARTICLE FLEXIBILITY: The direct object of the verb can be marked with EITHER を or が! 水を飲みたい is acceptable, but 水が飲みたい highlights the desired object more prominently.",
    "keyTakeaway": "MUG-UP: V-stem + たい = Want to do! Conjugates as an い-adj. Direct object particle を often becomes が.",
    "sentences": [
      {
        "id": "s-g1-11-1",
        "japanese": "日本へ行って、本場のラーメンが食べたいです。",
        "english": "I want to go to Japan and eat authentic ramen.",
        "literal": "Japan-to go, authentic ramen eat-want is.",
        "tokens": [
          {
            "word": "食べたいです",
            "meaning": "want to eat",
            "reading": "たべたいです",
            "romaji": "tabetai desu",
            "pos": "Verb+Grammar"
          }
        ],
        "nuanceNote": "Desire to eat authentic ramen."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-11-1",
        "question": "今日はとても疲れたので、何も（　　）たくないです。",
        "translation": "Because I am so tired today, I do not want to do anything.",
        "options": [
          "し",
          "する",
          "して",
          "した"
        ],
        "correctIndex": 0,
        "grammarFocus": "Negative desire 〜たくない with verb stem",
        "ruleHint": "Desire to do nothing after tiring day.",
        "explanations": [
          {
            "text": "し",
            "isCorrect": true,
            "reason": "Correct! する stem is し + たくない (したくない = do not want to do)."
          },
          {
            "text": "する",
            "isCorrect": false,
            "reason": "Incorrect. する is dictionary form."
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
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L11",
      "Desire",
      "Modality"
    ]
  },
  {
    "id": "g1-l11-koto-ga-aru",
    "title": "〜ことがある (Past Experiential Aspect: Have Ever Done)",
    "meaning": "Expresses that one has had the lifetime historical experience of doing an action: 'Have had the experience of / Have ever done X'.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 11: After-Vacation Plans",
    "streamId": "stream-time",
    "streamName": "Chronos & Instant Transitions",
    "connection": "V-た + ことがある / あります (Negative: ありません / ない)",
    "nuance": "LIFETIME HISTORICAL ASPECT: Strictly connects to past た-form! Cannot be used for immediate recent routine events (e.g., 'I ate toast this morning' ❌). It refers to lifetime resume experiences.",
    "keyTakeaway": "MUG-UP: V-た + ことがある = I have had the lifetime experience of doing X!",
    "sentences": [
      {
        "id": "s-g1-11-2",
        "japanese": "富士山に登ったことがありますか。「ええ、一度あります。」",
        "english": "Have you ever climbed Mt. Fuji? 'Yes, once.'",
        "literal": "Mt-Fuji climbed experience have question? Yes, once have.",
        "tokens": [
          {
            "word": "登ったことがありますか",
            "meaning": "have you ever climbed?",
            "reading": "のぼったことがありますか",
            "romaji": "nobotta koto ga arimasu ka",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Lifetime experiential inquiry."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-11-2",
        "question": "歌舞伎を（　　）ことがありますか。「いいえ、一度もありません。」",
        "translation": "Have you ever seen Kabuki? 'No, not once.'",
        "options": [
          "見た",
          "見る",
          "見て",
          "見"
        ],
        "correctIndex": 0,
        "grammarFocus": "V-た + ことがある lifetime experience",
        "ruleHint": "Inquiring about Kabuki viewing experience.",
        "explanations": [
          {
            "text": "見た",
            "isCorrect": true,
            "reason": "Correct! Experiential aspect requires past form 見た + ことがある."
          },
          {
            "text": "見る",
            "isCorrect": false,
            "reason": "Incorrect. 見ることがある means 'there are times when I see' (occasional habit), not past experience."
          },
          {
            "text": "見て",
            "isCorrect": false,
            "reason": "Incorrect. 見て is te-form."
          },
          {
            "text": "見",
            "isCorrect": false,
            "reason": "Incorrect. 見 is masu-stem."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L11",
      "Experience",
      "Aspect"
    ]
  },
  {
    "id": "g1-l11-sugiru",
    "title": "〜すぎる (Excessiveness: Too Much / Overdoing)",
    "meaning": "Indicates exceeding a proper, healthy, or desirable threshold: 'too [adj]' or 'doing [verb] too much'.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 11: After-Vacation Plans",
    "streamId": "stream-limits",
    "streamName": "Boundaries, Extremes & Scope",
    "connection": "V-stem + すぎる | い-adj (drop い) + すぎる | な-adj stem + すぎる (Conjugates as Ru-verb)",
    "nuance": "UNFAVORABLE THRESHOLD: Sugiru carries an overwhelmingly negative implication (e.g., this is too spicy to eat, I drank too much and got sick).",
    "keyTakeaway": "MUG-UP: Drop final い, drop ます, drop な, and append すぎる! Conjugates as a Ru-verb (すぎます, すぎた).",
    "sentences": [
      {
        "id": "s-g1-11-3",
        "japanese": "昨夜はお酒を飲みすぎて、今朝はひどい二日酔いです。",
        "english": "Last night I drank too much alcohol, and this morning I have a terrible hangover.",
        "literal": "Last-night alcohol drink-excessively, this-morning terrible hangover is.",
        "tokens": [
          {
            "word": "飲みすぎて",
            "meaning": "drank too much and",
            "reading": "のみすぎて",
            "romaji": "nomisugite",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Excessive drinking resulting in hangover."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-11-3",
        "question": "この問題は難し（　　）て、私には全く分かりません。",
        "translation": "This problem is too difficult, so I don't understand it at all.",
        "options": [
          "すぎ",
          "そう",
          "やすく",
          "がち"
        ],
        "correctIndex": 0,
        "grammarFocus": "い-adjective + すぎる excessiveness",
        "ruleHint": "Overly difficult problem.",
        "explanations": [
          {
            "text": "すぎ",
            "isCorrect": true,
            "reason": "Correct! 難しい drops い + すぎて forms 難しすぎて ('too difficult')."
          },
          {
            "text": "そう",
            "isCorrect": false,
            "reason": "Incorrect. そう indicates appearance (難しそう)."
          },
          {
            "text": "やすく",
            "isCorrect": false,
            "reason": "Incorrect. やすく indicates ease (難しやすく is nonsense)."
          },
          {
            "text": "がち",
            "isCorrect": false,
            "reason": "Incorrect. がち indicates negative tendency."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L11",
      "Excess",
      "Thresholds"
    ]
  },
  {
    "id": "g1-l12-node-objective-reason",
    "title": "〜ので (Objective Reason / Natural Causality: Since / Because)",
    "meaning": "Presents an objective, natural, or polite reason: 'Since / Because X, naturally Y'.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 12: Feeling Sick",
    "streamId": "stream-causality",
    "streamName": "Causal Chains & Regret",
    "connection": "Plain form + ので | な-adj / Noun + な + ので (Notice the required な!)",
    "nuance": "POLITE & NATURAL: Unlike から which sounds subjective and assertive, ので presents the reason as an objective circumstance beyond the speaker's personal whim. Far more polite in business requests.",
    "keyTakeaway": "MUG-UP: Noun / な-adj + な + ので (雨なので, 暇なので). More polite and objective than から.",
    "sentences": [
      {
        "id": "s-g1-12-1",
        "japanese": "明日は朝早く出発するので、今夜は準備をして早く寝ます。",
        "english": "Since I will depart early tomorrow morning, I will prepare tonight and go to bed early.",
        "literal": "Tomorrow morning early depart since, tonight prepare early sleep.",
        "tokens": [
          {
            "word": "出発するので",
            "meaning": "since I will depart",
            "reading": "しゅっぱつするので",
            "romaji": "shuppatsu suru node",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Objective factual circumstance motivating early rest."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-12-1",
        "question": "明日は（　　）なので、一日中家でのんびり過ごします。",
        "translation": "Since tomorrow is a holiday, I will spend the entire day relaxing at home.",
        "options": [
          "休み",
          "休みの",
          "休みだ",
          "休みに"
        ],
        "correctIndex": 0,
        "grammarFocus": "Noun + な + ので objective causality",
        "ruleHint": "Connecting a noun to causal marker ので.",
        "explanations": [
          {
            "text": "休み",
            "isCorrect": true,
            "reason": "Correct! Noun 休み connects via な to ので (休みなので)."
          },
          {
            "text": "休みの",
            "isCorrect": false,
            "reason": "Incorrect. 休みの is an invalid connector to ので."
          },
          {
            "text": "休みだ",
            "isCorrect": false,
            "reason": "Incorrect. 休みだ cannot attach to ので (must be なので, NOT だので ❌)."
          },
          {
            "text": "休みに",
            "isCorrect": false,
            "reason": "Incorrect. 休みに is adverbial."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L12",
      "Causality",
      "Polite Reason"
    ]
  },
  {
    "id": "g1-l12-nakereba-ikemasen",
    "title": "〜なければいけません / なきゃいけません (Obligation: Must Do / Have to Do)",
    "meaning": "Expresses an unavoidable obligation or necessity: 'Must do / Have to do X'. Spoken contraction: 〜なきゃいけません / なきゃ.",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 12: Feeling Sick",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "V-ない (drop い) + ければいけません / ければなりません",
    "nuance": "DOUBLE NEGATIVE LOGIC: Literally 'If I do not do X, it cannot go on'. Spoken casual forms contract heavily: なければ → なきゃ, 食べなきゃ.",
    "keyTakeaway": "MUG-UP: Drop final い from ない-form, add ければいけません! Casual: 〜なきゃ.",
    "sentences": [
      {
        "id": "s-g1-12-2",
        "japanese": "明日の朝九時までに、レポートを提出しなければいけません。",
        "english": "I must submit the report by 9:00 AM tomorrow morning.",
        "literal": "Tomorrow morning 9-by report submit must.",
        "tokens": [
          {
            "word": "提出しなければいけません",
            "meaning": "must submit",
            "reading": "ていしゅつしなければいけません",
            "romaji": "teishutsu shinakereba ikemasen",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Strict academic obligation."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-12-2",
        "question": "熱が高いですから、今日は病院へ（　　）ければいけませんよ。",
        "translation": "Since your fever is high, you must go to the hospital today.",
        "options": [
          "行かな",
          "行く",
          "行って",
          "行き"
        ],
        "correctIndex": 0,
        "grammarFocus": "Obligation formula 〜なければいけません",
        "ruleHint": "Medical necessity to visit hospital.",
        "explanations": [
          {
            "text": "行かな",
            "isCorrect": true,
            "reason": "Correct! 行く negative stem is 行かな + ければいけません."
          },
          {
            "text": "行く",
            "isCorrect": false,
            "reason": "Incorrect. 行く is dictionary form."
          },
          {
            "text": "行って",
            "isCorrect": false,
            "reason": "Incorrect. 行って is te-form."
          },
          {
            "text": "行き",
            "isCorrect": false,
            "reason": "Incorrect. 行き is masu-stem."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L12",
      "Obligation",
      "Necessity"
    ]
  },
  {
    "id": "g1-l12-deshou-darou",
    "title": "〜でしょう / 〜だろう (Conjecture & Probability: Probably)",
    "meaning": "Expresses conjecture or probability without absolute certainty: 'Probably / It will likely be X'. Also used with rising tone to seek agreement ('Right?').",
    "level": "N5",
    "book": "Genki I",
    "chapter": "Lesson 12: Feeling Sick",
    "streamId": "stream-modality",
    "streamName": "Epistemic Certainty, Conviction & Duty",
    "connection": "Plain form + でしょう (Polite) / だろう (Plain) [Noun & な-adj attach directly without だ!]",
    "nuance": "NO だ BEFORE DESHOU: For nouns and な-adjectives, drop だ completely: 暇でしょう (NOT 暇だでしょう ❌), 雨でしょう (NOT 雨だでしょう ❌).",
    "keyTakeaway": "MUG-UP: Attach directly without だ! (雨でしょう = It will probably rain).",
    "sentences": [
      {
        "id": "s-g1-12-3",
        "japanese": "天気予報によると、明日は午後から雨が降るでしょう。",
        "english": "According to the weather forecast, it will probably rain from the afternoon tomorrow.",
        "literal": "Weather-forecast according-to, tomorrow afternoon-from rain fall probably.",
        "tokens": [
          {
            "word": "降るでしょう",
            "meaning": "will probably fall",
            "reading": "ふるでしょう",
            "romaji": "furu deshou",
            "pos": "Grammar"
          }
        ],
        "nuanceNote": "Meteorological conjecture."
      }
    ],
    "quiz": [
      {
        "id": "q-g1-12-3",
        "question": "田中さんは毎日一生懸命勉強していますから、きっと試験に（　　）でしょう。",
        "translation": "Since Tanaka-san studies hard every day, he will surely pass the exam.",
        "options": [
          "合格する",
          "合格して",
          "合格し",
          "合格したの"
        ],
        "correctIndex": 0,
        "grammarFocus": "Conjecture 〜でしょう with plain verb",
        "ruleHint": "Predicting exam success based on diligence.",
        "explanations": [
          {
            "text": "合格する",
            "isCorrect": true,
            "reason": "Correct! Plain dictionary form 合格する connects directly to でしょう."
          },
          {
            "text": "合格して",
            "isCorrect": false,
            "reason": "Incorrect. 合格して is te-form."
          },
          {
            "text": "合格し",
            "isCorrect": false,
            "reason": "Incorrect. 合格し is masu-stem."
          },
          {
            "text": "合格したの",
            "isCorrect": false,
            "reason": "Incorrect. 合格したの has unnecessary nominalizer の."
          }
        ]
      }
    ],
    "tags": [
      "N5",
      "Genki L12",
      "Conjecture",
      "Probability"
    ]
  }
];
