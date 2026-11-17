import json

def get_skm2_exercises():
    exercises = []

    # ==================== SKM N2 PART 1 CHAPTER 1 ====================
    exercises.extend([
        {
            "id": "skm2-c1-ex-1",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 1",
            "type": "multiple-choice",
            "context": "Formal commencement of a high-stakes ceremony: upon opening the new museum.",
            "question": "新美術館の開館に（　　）、記念式典が盛大に行われた。",
            "translation": "Upon the occasion of opening the new art museum, a commemorative ceremony was held on a grand scale.",
            "options": ["際して", "つれて", "応じて", "そって"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c1-ni-saishite",
            "grammarPointTitle": "〜に際して / 〜にあたって (Upon the Occasion Of / At the Inception Of)",
            "explanation": {
                "overall": "〜に際して denotes a momentous, non-routine, formal occasion or event ('upon the occasion of / at the inception of').",
                "options": [
                    {"text": "際して", "isCorrect": True, "reason": "Correct. Formal occasion inception: Noun + に際して.", "trapCategory": "meaning"},
                    {"text": "つれて", "isCorrect": False, "reason": "Incorrect. につれて denotes proportional evolution, not a special ceremonial occasion.", "trapCategory": "meaning"},
                    {"text": "応じて", "isCorrect": False, "reason": "Incorrect. に応じて means commensurate with / in response to.", "trapCategory": "meaning"},
                    {"text": "そって", "isCorrect": False, "reason": "Incorrect. に沿って means along / in line with guidelines.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which formal pattern expresses 'upon the momentous occasion of [event]'?"
        },
        {
            "id": "skm2-c1-ex-2",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 1",
            "type": "multiple-choice",
            "context": "Sudden unexpected transition: the moment the baby fell asleep, the doorbell rang.",
            "question": "赤ちゃんがやっと眠った（　　）と思ったら、チャイムが鳴って起きてしまった。",
            "translation": "Just as I thought the baby had finally fallen asleep, the doorbell rang and woke him up.",
            "options": ["か", "に", "と", "を"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c1-ka-to-omou-to",
            "grammarPointTitle": "〜（か）と思うと / 〜（か）と思ったら (Just as I Thought X, Y Suddenly Burst Forth)",
            "explanation": {
                "overall": "〜（か）と思ったら / 〜（か）と思うと expresses that the instant the speaker registered event X, an immediate sudden event Y burst forth in sharp contrast.",
                "options": [
                    {"text": "か", "isCorrect": True, "reason": "Correct. Immediate surprise transition formula: 〜（か）と思ったら.", "trapCategory": "formation"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. Ungrammatical before と思ったら.", "trapCategory": "formation"},
                    {"text": "と", "isCorrect": False, "reason": "Incorrect. Redundant particle.", "trapCategory": "formation"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What particle precedes と思ったら in this sudden contrast pattern?"
        },
        {
            "id": "skm2-c1-ex-3",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 1",
            "type": "multiple-choice",
            "context": "Virtually simultaneous occurrence: before the chime had even finished ringing, students rushed out.",
            "question": "終業のチャイムが鳴るか鳴ら（　　）のうちに、生徒たちは教室を飛び出した。",
            "translation": "Almost before the end-of-class chime had finished ringing, the students rushed out of the classroom.",
            "options": ["ないか", "なくて", "ず", "ないで"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c1-kanai-ka-no-uchini",
            "grammarPointTitle": "〜か〜ないかのうちに (On the Very Verge Of / Before Even Finishing)",
            "explanation": {
                "overall": "The pattern for two virtually simultaneous events is: Verb-dict + か + Verb-nai + かのうちに (鳴るか鳴らないかのうちに).",
                "options": [
                    {"text": "ないか", "isCorrect": True, "reason": "Correct. Formula: V-dict か V-nai かのうちに (鳴るか鳴らないかのうちに).", "trapCategory": "formation"},
                    {"text": "なくて", "isCorrect": False, "reason": "Incorrect. Te-form cannot form this simultaneous pattern.", "trapCategory": "formation"},
                    {"text": "ず", "isCorrect": False, "reason": "Incorrect. Archaic negative.", "trapCategory": "formation"},
                    {"text": "ないで", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the formula: V-dict か V-nai ___ のうちに?"
        }
    ])

    # ==================== SKM N2 PART 1 CHAPTER 2 ====================
    exercises.extend([
        {
            "id": "skm2-c2-ex-1",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 2",
            "type": "multiple-choice",
            "context": "Continual unidirectional deterioration: due to lack of exercise, physical stamina just keeps declining.",
            "question": "運動不足で、体力が衰える（　　）だ。",
            "translation": "Due to lack of exercise, my physical strength just keeps declining in one direction.",
            "options": ["一方", "最中", "つつ", "とおり"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c2-ippou-da-bakari-da",
            "grammarPointTitle": "〜ばかりだ / 〜一方だ (Continual Single-Directional Trend: Keep On -ing)",
            "explanation": {
                "overall": "〜一方だ (or 〜ばかりだ) attaches to dictionary change verbs to express a persistent single-directional trend, especially toward an undesirable state ('keeps on declining').",
                "options": [
                    {"text": "一方", "isCorrect": True, "reason": "Correct. Unidirectional trend: V-dict + 一方だ.", "trapCategory": "meaning"},
                    {"text": "最中", "isCorrect": False, "reason": "Incorrect. 最中 denotes peak of dynamic action, not long-term trend.", "trapCategory": "meaning"},
                    {"text": "つつ", "isCorrect": False, "reason": "Incorrect. つつ requires auxiliary ある (つつある).", "trapCategory": "formation"},
                    {"text": "とおり", "isCorrect": False, "reason": "Incorrect. In accordance with.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which noun expresses a continuous single-directional trend ('keeps on... in one direction')?"
        },
        {
            "id": "skm2-c2-ex-2",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 2",
            "type": "multiple-choice",
            "context": "Process underway in transition: the medical condition is gradually improving.",
            "question": "新しい薬の効果で、病状は回復し（　　）ある。",
            "translation": "Thanks to the effects of the new medicine, the condition is currently in the process of recovering.",
            "options": ["つつ", "ながら", "一方", "ばかり"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c2-tsutsu-aru",
            "grammarPointTitle": "〜つつある (Currently in Continuous Transition / Underway)",
            "explanation": {
                "overall": "〜つつある attaches to verb stems to denote a gradual transition or transformation currently in progress ('underway / in the process of -ing').",
                "options": [
                    {"text": "つつ", "isCorrect": True, "reason": "Correct. Formal transition underway: V-stem + つつある.", "trapCategory": "formation"},
                    {"text": "ながら", "isCorrect": False, "reason": "Incorrect. ながら cannot attach to ある to mean 'underway'.", "trapCategory": "formation"},
                    {"text": "一方", "isCorrect": False, "reason": "Incorrect. 一方 attaches to dictionary form + だ (回復する一方だ).", "trapCategory": "formation"},
                    {"text": "ばかり", "isCorrect": False, "reason": "Incorrect. ばかり attaches to dictionary form + だ.", "trapCategory": "formation"}
                ]
            },
            "hint": "What suffix attaches to a verb stem with ある to express a formal process underway?"
        }
    ])

    # ==================== SKM N2 PART 1 CHAPTER 7 ====================
    exercises.extend([
        {
            "id": "skm2-c7-ex-1",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 7",
            "type": "multiple-choice",
            "context": "Centering around a heated controversy: fierce debates over tax reform.",
            "question": "税制改革を（　　）、国会で激しい議論が交わされた。",
            "translation": "Heated arguments were exchanged in the Diet centering around tax system reform.",
            "options": ["めぐって", "こたえて", "通して", "通じて"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c7-wo-megutte",
            "grammarPointTitle": "〜をめぐって / 〜をめぐる (Centering Around a Dispute, Controversy, or Conflict)",
            "explanation": {
                "overall": "〜をめぐって denotes an issue or focal point around which multiple opposing parties contest, debate, or disagree ('centering around a dispute / concerning').",
                "options": [
                    {"text": "めぐって", "isCorrect": True, "reason": "Correct. Focal point of controversy/debate: Noun + をめぐって.", "trapCategory": "meaning"},
                    {"text": "こたえて", "isCorrect": False, "reason": "Incorrect. にこたえて means in response to demands/expectations.", "trapCategory": "meaning"},
                    {"text": "通して", "isCorrect": False, "reason": "Incorrect. を通して means throughout or through the medium of.", "trapCategory": "meaning"},
                    {"text": "通じて", "isCorrect": False, "reason": "Incorrect. Through the medium of.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which expression means 'centering around [a dispute or controversy]'?"
        },
        {
            "id": "skm2-c7-ex-2",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 7",
            "type": "multiple-choice",
            "context": "Responding to requests / expectations: held an encore performance in response to fan demand.",
            "question": "ファンの熱狂的なアンコールに（　　）、もう一曲演奏した。",
            "translation": "In response to the enthusiastic encores of the fans, they performed one more song.",
            "options": ["こたえて", "めぐって", "反して", "沿って"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c7-ni-kotaete",
            "grammarPointTitle": "〜にこたえて / 〜にこたえる (In Response to Expectations, Requests, or Demands)",
            "explanation": {
                "overall": "〜にこたえて denotes acting in a way that fulfills, satisfies, or meets requests, cheers, or expectations ('in response to / meeting expectations').",
                "options": [
                    {"text": "こたえて", "isCorrect": True, "reason": "Correct. Fulfilling expectations/requests: Noun + にこたえて.", "trapCategory": "meaning"},
                    {"text": "めぐって", "isCorrect": False, "reason": "Incorrect. をめぐって is for disputes/controversies.", "trapCategory": "meaning"},
                    {"text": "反して", "isCorrect": False, "reason": "Incorrect. に反して means against / contrary to expectations.", "trapCategory": "meaning"},
                    {"text": "沿って", "isCorrect": False, "reason": "Incorrect. に沿って means along guidelines.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern means 'in response to [demands / cheers / expectations]'?"
        }
    ])

    # ==================== SKM N2 PART 1 CHAPTER 15 ====================
    exercises.extend([
        {
            "id": "skm2-c15-ex-1",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 15",
            "type": "multiple-choice",
            "context": "Miraculous hypothetical condition: 'If by any remote miracle I could return to my youth, I would study harder'.",
            "question": "若返ることができる（　　）、もう一度青春をやり直したい。",
            "translation": "If by any miraculous chance it were possible to become young again, I would want to redo my youth.",
            "options": ["ものなら", "ことには", "あまり", "契機に"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c15-mono-nara",
            "grammarPointTitle": "〜ものなら (If by Any Miraculous Chance It Were Possible)",
            "explanation": {
                "overall": "Potential verb + ものなら expresses a hypothetical wish for something recognized as virtually impossible or miraculous ('if by any remote miracle it were possible').",
                "options": [
                    {"text": "ものなら", "isCorrect": True, "reason": "Correct. Miraculous hypothetical wish: V-potential + ものなら.", "trapCategory": "meaning"},
                    {"text": "ことには", "isCorrect": False, "reason": "Incorrect. 〜ないことには requires negative prerequisite.", "trapCategory": "formation"},
                    {"text": "あまり", "isCorrect": False, "reason": "Incorrect. Excessive degree.", "trapCategory": "meaning"},
                    {"text": "契機に", "isCorrect": False, "reason": "Incorrect. Catalyst springboard.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What conditional attaches to a potential verb to express an impossible wish ('if by any miracle I could')?"
        },
        {
            "id": "skm2-c15-ex-2",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 15",
            "type": "multiple-choice",
            "context": "Negative prerequisite: unless we hear from both sides, we cannot judge.",
            "question": "両者の意見を聞か（　　）、判断は下せません。",
            "translation": "Unless we listen to the opinions of both parties, we cannot make a judgment.",
            "options": ["ないことには", "ないものなら", "ないあまり", "ない契機に"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c15-nai-koto-niwa",
            "grammarPointTitle": "〜ないことには（〜ない） (Unless Condition X Occurs, Y Is Utterly Impossible)",
            "explanation": {
                "overall": "〜ないことには（〜ない） denotes an indispensable prerequisite: 'Unless X occurs, Y cannot possibly happen / is impossible'.",
                "options": [
                    {"text": "ないことには", "isCorrect": True, "reason": "Correct. Absolute prerequisite: V-nai + ことには + negative conclusion.", "trapCategory": "formation"},
                    {"text": "ないものなら", "isCorrect": False, "reason": "Incorrect. ものなら does not form standard prerequisite with negative verbs.", "trapCategory": "formation"},
                    {"text": "ないあまり", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"},
                    {"text": "ない契機に", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What pattern means 'unless [prerequisite condition] occurs, [Y is impossible]'?"
        }
    ])

    # ==================== SKM N2 PART 1 CHAPTER 18 ====================
    exercises.extend([
        {
            "id": "skm2-c18-ex-1",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 18",
            "type": "multiple-choice",
            "context": "Psychological inability / formal polite refusal: cannot accept this confidential request on ethical grounds.",
            "question": "そのご要望にはお応えいたし（　　）。申し訳ございません。",
            "translation": "I am afraid I cannot comply with that request. I am terribly sorry. (Polite refusal on principle)",
            "options": ["かねます", "かねません", "がたいです", "得ません"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c22-kaneru",
            "grammarPointTitle": "〜かねる (Psychologically Unable / Politely Refusing on Principle)",
            "explanation": {
                "overall": "〜かねる (Verb stem + かねる / かねます) expresses a polite, formal refusal based on professional duty, role restrictions, or psychological difficulty ('cannot do / find it difficult to comply').",
                "options": [
                    {"text": "かねます", "isCorrect": True, "reason": "Correct. Polite principled refusal: V-stem + かねます.", "trapCategory": "meaning"},
                    {"text": "かねません", "isCorrect": False, "reason": "Incorrect. 〜かねない / 〜かねません expresses dangerous possibility ('might cause catastrophe'), opposite meaning!", "trapCategory": "meaning"},
                    {"text": "がたいです", "isCorrect": False, "reason": "Incorrect. 〜がたい denotes emotional difficulty (信じがたい), not polite service refusal.", "trapCategory": "context"},
                    {"text": "得ません", "isCorrect": False, "reason": "Incorrect. 〜得ない denotes logical impossibility.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Be careful: which one is the formal refusal 'I cannot comply' (〜かねる vs 〜かねない)?"
        },
        {
            "id": "skm2-c18-ex-2",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 18",
            "type": "multiple-choice",
            "context": "Dangerous potential risk: if you drive recklessly like that, you might cause a serious accident.",
            "question": "そんな乱暴な運転をしていたら、大事故を起こし（　　）よ。",
            "translation": "If you drive recklessly like that, you could very well cause a major accident!",
            "options": ["かねない", "かねる", "がたい", "得ない"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c22-kane-nai",
            "grammarPointTitle": "〜かねない (Dangerous Potential to Trigger Catastrophe)",
            "explanation": {
                "overall": "〜かねない (Verb stem + かねない) warns that an undesirable, catastrophic outcome could very easily happen if conditions continue ('might trigger / has dangerous potential to').",
                "options": [
                    {"text": "かねない", "isCorrect": True, "reason": "Correct. Dangerous catastrophe risk: V-stem + かねない.", "trapCategory": "meaning"},
                    {"text": "かねる", "isCorrect": False, "reason": "Incorrect. 〜かねる is polite inability to do, clashing with causing an accident.", "trapCategory": "meaning"},
                    {"text": "がたい", "isCorrect": False, "reason": "Incorrect. 〜がたい means hard to do emotionally.", "trapCategory": "meaning"},
                    {"text": "得ない", "isCorrect": False, "reason": "Incorrect. 〜得ない means logically impossible, opposite of warning.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern warns of a dangerous negative risk: 〜かねない or 〜かねる?"
        }
    ])

    # ==================== SKM N2 PART 1 CHAPTER 25 ====================
    exercises.extend([
        {
            "id": "skm2-c25-ex-1",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 25",
            "type": "multiple-choice",
            "context": "Irresistible psychological urge: couldn't help laughing at the funny story.",
            "question": "あまりのおかしさに、笑わずには（　　）かった。",
            "translation": "Because it was so funny, I couldn't help laughing / was unable to suppress a laugh.",
            "options": ["いられな", "おけな", "すま", "おわらな"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c25-zu-niwa-irarenai",
            "grammarPointTitle": "〜ずにいられない / 〜ないではいられない (Cannot Help But Do / Irresistible Urge)",
            "explanation": {
                "overall": "〜ずにいられない (or 〜ないではいられない) expresses an irresistible psychological or emotional impulse that cannot be suppressed ('cannot help but do').",
                "options": [
                    {"text": "いられな", "isCorrect": True, "reason": "Correct. Irresistible urge formula: 〜ずにはいられない / 〜ずにいられなかった.", "trapCategory": "formation"},
                    {"text": "おけな", "isCorrect": False, "reason": "Incorrect. 〜ずにおく is not the impulse pattern.", "trapCategory": "formation"},
                    {"text": "すま", "isCorrect": False, "reason": "Incorrect. 〜ずにはすまない means 'cannot get by without doing' (social duty).", "trapCategory": "meaning"},
                    {"text": "おわらな", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the formula for 'cannot help but [laugh/cry]': 〜ずには___?"
        },
        {
            "id": "skm2-c25-ex-2",
            "bookId": "skm-n2",
            "chapter": "Part 1 · Chapter 25",
            "type": "multiple-choice",
            "context": "Inevitable duty / no choice but to do: forced by economic hardship to sell the family land.",
            "question": "借金を返すために、先祖代々の土地を売ら（　　）を得なかった。",
            "translation": "In order to pay off the debt, I was inevitably compelled to sell the ancestral land.",
            "options": ["ざる", "ない", "ず", "なくて"],
            "correctIndex": 0,
            "grammarPointId": "skm2-c24-zaru-wo-enai",
            "grammarPointTitle": "〜ざるを得ない (Inevitably Compelled to Do Against One's Wish)",
            "explanation": {
                "overall": "〜ざるを得ない indicates having no other choice under circumstances but to perform an action against one's true personal wish (Verb nai-stem + ざるを得ない. する becomes せざるを得ない).",
                "options": [
                    {"text": "ざる", "isCorrect": True, "reason": "Correct. Inevitably compelled formula: V-nai stem + ざるを得ない.", "trapCategory": "formation"},
                    {"text": "ない", "isCorrect": False, "reason": "Incorrect. *ないを得ない is ungrammatical.", "trapCategory": "formation"},
                    {"text": "ず", "isCorrect": False, "reason": "Incorrect. *ずを得ない is ungrammatical.", "trapCategory": "formation"},
                    {"text": "なくて", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What archaic negative particle forms the compelling pattern: V-nai stem + ___ を得ない?"
        }
    ])

    # ==================== SKM N2 PART 3 CHAPTER 10 ====================
    exercises.extend([
        {
            "id": "skm2-p3-10-ex-1",
            "bookId": "skm-n2",
            "chapter": "Part 3 · Chapter 10",
            "type": "multiple-choice",
            "context": "Connector for adding an even stronger point: this apartment is close to the station, and what's more, the rent is cheap.",
            "question": "駅から近く、環境も良い。（　　）、家賃も驚くほど安い。",
            "translation": "It is close to the station and the environment is pleasant. What's more / On top of that, the rent is surprisingly cheap.",
            "options": ["そのうえ", "それに対して", "あるいは", "だが"],
            "correctIndex": 0,
            "grammarPointId": "added-n2-p3-10-150",
            "grammarPointTitle": "文章：接続表現",
            "explanation": {
                "overall": "そのうえ (or しかも、さらに、そればかりか) is a cumulative additive connector meaning 'what is more / in addition / on top of that', adding a reinforcing positive or negative attribute.",
                "options": [
                    {"text": "そのうえ", "isCorrect": True, "reason": "Correct. Cumulative addition connector: そのうえ ('what is more / furthermore').", "trapCategory": "meaning"},
                    {"text": "それに対して", "isCorrect": False, "reason": "Incorrect. それに対して denotes contrast (in contrast to that).", "trapCategory": "meaning"},
                    {"text": "あるいは", "isCorrect": False, "reason": "Incorrect. あるいは denotes disjunction (or).", "trapCategory": "meaning"},
                    {"text": "だが", "isCorrect": False, "reason": "Incorrect. だが denotes opposition (however), clashing with reinforcing cheap rent.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which connector introduces an additional reinforcing positive factor ('on top of that / furthermore')?"
        },
        {
            "id": "skm2-p3-10-ex-2",
            "bookId": "skm-n2",
            "chapter": "Part 3 · Chapter 10",
            "type": "multiple-choice",
            "context": "Connector contrasting two sides: urban populations increase, while rural populations decline.",
            "question": "大都市では人口が増加している。（　　）、地方では過疎化が進んでいる。",
            "translation": "In large cities, the population is increasing. In contrast / On the other hand, depopulation is advancing in rural areas.",
            "options": ["一方", "さらに", "そのうえ", "したがって"],
            "correctIndex": 0,
            "grammarPointId": "added-n2-p3-10-150",
            "grammarPointTitle": "文章：接続表現",
            "explanation": {
                "overall": "一方 (or それに対して) connects two sentences by presenting a contrast between two distinct situations or viewpoints ('on the other hand / in contrast').",
                "options": [
                    {"text": "一方", "isCorrect": True, "reason": "Correct. Contrastive connector between two situations: 一方 / それに対して.", "trapCategory": "meaning"},
                    {"text": "さらに", "isCorrect": False, "reason": "Incorrect. さらに is addition ('furthermore'), clashing with rural depopulation contrast.", "trapCategory": "meaning"},
                    {"text": "そのうえ", "isCorrect": False, "reason": "Incorrect. そのうえ is addition.", "trapCategory": "meaning"},
                    {"text": "したがって", "isCorrect": False, "reason": "Incorrect. したがって is logical consequence ('therefore').", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which connector presents an opposing contrast between two situations ('on the other hand')?"
        }
    ])

    return exercises

if __name__ == "__main__":
    ex_list = get_skm2_exercises()
    print(f"Generated {len(ex_list)} SKM N2 exercises.")
