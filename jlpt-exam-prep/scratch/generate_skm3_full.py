import json

def get_skm3_all_exercises():
    import generate_skm3_part1 as part1
    exercises = part1.get_skm3_exercises() # C1 and C2

    # ==================== SKM N3 PART 1 CHAPTER 3 ====================
    exercises.extend([
        {
            "id": "skm3-c3-ex-1",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 3",
            "type": "multiple-choice",
            "context": "Expressing extreme degree: laughing so hard that tears came out.",
            "question": "お腹が痛くなる（　　）大笑いしました。",
            "translation": "I laughed so hard that my stomach hurt (to the extent that my stomach ached).",
            "options": ["ほど", "ばかり", "とおり", "ついで"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u3-kurai-hodo-extent",
            "grammarPointTitle": "〜くらいだ / 〜ほどだ (Expressing Extreme Degree: To the Extent That)",
            "explanation": {
                "overall": "〜くらいだ / 〜ほどだ expresses an extreme degree by citing an illustrative physical or psychological manifestation ('to the extent that').",
                "options": [
                    {"text": "ほど", "isCorrect": True, "reason": "Correct. Extreme degree: V-dict + ほど / くらい.", "trapCategory": "meaning"},
                    {"text": "ばかり", "isCorrect": False, "reason": "Incorrect. ばかり denotes only/just.", "trapCategory": "meaning"},
                    {"text": "とおり", "isCorrect": False, "reason": "Incorrect. とおり denotes in accordance with.", "trapCategory": "meaning"},
                    {"text": "ついで", "isCorrect": False, "reason": "Incorrect. ついで denotes side task.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which word expresses extreme degree: 'to the point/extent that'?"
        },
        {
            "id": "skm3-c3-ex-2",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 3",
            "type": "multiple-choice",
            "context": "Superlative: 'Nothing in this world is as precious as health'.",
            "question": "健康（　　）大切なものはありません。",
            "translation": "There is nothing as precious as health.",
            "options": ["ほど", "より", "から", "だけ"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u3-kurai-wa-nai",
            "grammarPointTitle": "〜くらい…はない / 〜ほど…はない (Superlative: Nothing Is As... As X)",
            "explanation": {
                "overall": "The superlative construction 'Nothing is as [Adjective] as X' is: Noun + ほど…はない (健康ほど大切なものはない).",
                "options": [
                    {"text": "ほど", "isCorrect": True, "reason": "Correct. Superlative negative comparison: Noun + ほど…はない.", "trapCategory": "formation"},
                    {"text": "より", "isCorrect": False, "reason": "Incorrect. より requires affirmative comparative adjective without はない.", "trapCategory": "formation"},
                    {"text": "から", "isCorrect": False, "reason": "Incorrect. から indicates origin.", "trapCategory": "meaning"},
                    {"text": "だけ", "isCorrect": False, "reason": "Incorrect. だけ means 'only'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What particle combines with 〜はない to express that nothing equals X?"
        },
        {
            "id": "skm3-c3-ex-3",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 3",
            "type": "multiple-choice",
            "context": "Preferring an undesirable alternative over an unbearable one: 'Rather than apologize to him, I'd rather quit the club!'.",
            "question": "あんな奴に謝る（　　）、部活をやめたほうがましだ！",
            "translation": "Rather than apologize to a guy like that, I'd prefer to quit the club!",
            "options": ["くらいなら", "とおりなら", "うちに", "ついでに"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u3-kurai-nara",
            "grammarPointTitle": "〜くらいなら / 〜ぐらいなら (Rather Than Suffer X, I Would Prefer Y)",
            "explanation": {
                "overall": "〜くらいなら means 'rather than suffer condition X (which is intolerable), I would much rather do Y (even if Y is also difficult)'. Paired with ほうがいい / ほうがましだ.",
                "options": [
                    {"text": "くらいなら", "isCorrect": True, "reason": "Correct. 'Rather than suffer X': V-dict + くらいなら.", "trapCategory": "meaning"},
                    {"text": "とおりなら", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"},
                    {"text": "うちに", "isCorrect": False, "reason": "Incorrect. While condition lasts.", "trapCategory": "meaning"},
                    {"text": "ついでに", "isCorrect": False, "reason": "Incorrect. While doing side task.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern expresses 'rather than suffer [intolerable action], I'd prefer...'?"
        },
        {
            "id": "skm3-c3-ex-4",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 3",
            "type": "multiple-choice",
            "context": "Stating the best remedy: 'When you have a cold, sleeping warmly is the best thing to do'.",
            "question": "風邪をひいた時は、温かくして寝る（　　）。",
            "translation": "When you have a cold, sleeping warmly is by far the best choice.",
            "options": ["に限る", "にすぎない", "に違いない", "に決まっている"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u3-ni-kagiru",
            "grammarPointTitle": "〜に限る (Nothing Beats / Best Choice)",
            "explanation": {
                "overall": "〜に限る expresses the speaker's subjective judgment that X is the absolute best, unsurpassed choice ('nothing beats X / X is the best').",
                "options": [
                    {"text": "に限る", "isCorrect": True, "reason": "Correct. Best choice: V-dict / Noun + に限る.", "trapCategory": "meaning"},
                    {"text": "にすぎない", "isCorrect": False, "reason": "Incorrect. にすぎない means 'is nothing more than / merely'.", "trapCategory": "meaning"},
                    {"text": "に違いない", "isCorrect": False, "reason": "Incorrect. に違いない means 'must be / no doubt that'.", "trapCategory": "meaning"},
                    {"text": "に決まっている", "isCorrect": False, "reason": "Incorrect. に決まっている means 'definitely bound to be'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern expresses that something is the absolute best course of action ('nothing beats...')?"
        }
    ])

    # ==================== SKM N3 PART 1 CHAPTER 4 ====================
    exercises.extend([
        {
            "id": "skm3-c4-ex-1",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 4",
            "type": "multiple-choice",
            "context": "Coexisting contradictory aspects: this job is demanding, but on the other hand the salary is high.",
            "question": "この仕事は大変な（　　）、給料は非常に高い。",
            "translation": "This job is tough; on the flip side, the salary is very high.",
            "options": ["反面", "かわりに", "に対して", "について"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u4-hanmen-flipside",
            "grammarPointTitle": "〜反面 (On the Flip Side: Coexisting Contradictory Aspects)",
            "explanation": {
                "overall": "〜反面 highlights two contrasting, opposing facets coexisting simultaneously within the same entity or situation ('on the flip side / on the other hand').",
                "options": [
                    {"text": "反面", "isCorrect": True, "reason": "Correct. Two coexisting opposing qualities: 〜反面.", "trapCategory": "meaning"},
                    {"text": "かわりに", "isCorrect": False, "reason": "Incorrect. かわりに denotes compensation or substitution, not simultaneous contradictory nature.", "trapCategory": "context"},
                    {"text": "に対して", "isCorrect": False, "reason": "Incorrect. に対して contrasts two different distinct entities (A vs B).", "trapCategory": "context"},
                    {"text": "について", "isCorrect": False, "reason": "Incorrect. について means 'about'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern denotes the opposite, contrasting side of the very same thing ('on the flip side')?"
        },
        {
            "id": "skm3-c4-ex-2",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 4",
            "type": "multiple-choice",
            "context": "Compensation / exchange: 'I will teach you English in exchange for you teaching me Japanese'.",
            "question": "日本語を教えてもらう（　　）、英語を教えてあげます。",
            "translation": "In exchange for you teaching me Japanese, I will teach you English.",
            "options": ["かわりに", "反面に", "に対して", "について"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u4-kawari-ni-exchange",
            "grammarPointTitle": "〜かわりに (In Exchange For / Compensation / Instead Of)",
            "explanation": {
                "overall": "〜かわりに denotes reciprocal exchange or compensation: doing action B in return for / instead of action A.",
                "options": [
                    {"text": "かわりに", "isCorrect": True, "reason": "Correct. Reciprocal compensation: V-dict + かわりに.", "trapCategory": "meaning"},
                    {"text": "反面に", "isCorrect": False, "reason": "Incorrect. 反面 does not take に for reciprocal compensation.", "trapCategory": "formation"},
                    {"text": "に対して", "isCorrect": False, "reason": "Incorrect. Contrast, not exchange.", "trapCategory": "meaning"},
                    {"text": "について", "isCorrect": False, "reason": "Incorrect. About/regarding.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which expression means 'in exchange for / in return for'?"
        },
        {
            "id": "skm3-c4-ex-3",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 4",
            "type": "multiple-choice",
            "context": "Contrasting two distinct entities: elder brother is outgoing while younger brother is introverted.",
            "question": "兄が社交的なの（　　）、弟は内向的でおとなしい。",
            "translation": "While the older brother is sociable, in contrast the younger brother is introverted and quiet.",
            "options": ["に対して", "反面", "について", "にとって"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u4-ni-taishite",
            "grammarPointTitle": "〜に対して (In Contrast To / While X Is..., Y Is...)",
            "explanation": {
                "overall": "〜に対して contrasts two distinct subjects or entities showing diametrically opposed traits (兄 vs 弟).",
                "options": [
                    {"text": "に対して", "isCorrect": True, "reason": "Correct. Direct contrast between two entities: 〜に対して.", "trapCategory": "meaning"},
                    {"text": "反面", "isCorrect": False, "reason": "Incorrect. 反面 applies to two traits within the SAME single person or thing.", "trapCategory": "context"},
                    {"text": "について", "isCorrect": False, "reason": "Incorrect. Regarding.", "trapCategory": "meaning"},
                    {"text": "にとって", "isCorrect": False, "reason": "Incorrect. From perspective of.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern explicitly contrasts TWO DIFFERENT people or groups (A vs B)?"
        },
        {
            "id": "skm3-c4-ex-4",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 4",
            "type": "multiple-choice",
            "context": "Relative statistical comparison: 'Compared to last year, prices have risen'.",
            "question": "去年（　　）、今年は物価がかなり上がっている。",
            "translation": "Compared to last year, prices have risen considerably this year.",
            "options": ["に比べて", "に対して", "反面", "にとって"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u4-ni-kurabete",
            "grammarPointTitle": "〜に比べて (Compared With / Relative To)",
            "explanation": {
                "overall": "〜に比べて sets a benchmark of comparison ('compared with / relative to X, Y has [degree difference]').",
                "options": [
                    {"text": "に比べて", "isCorrect": True, "reason": "Correct. Benchmark comparison: Noun + に比べて.", "trapCategory": "meaning"},
                    {"text": "に対して", "isCorrect": False, "reason": "Incorrect. に対して highlights qualitative contrast (e.g. brother vs brother), not numerical benchmark comparison.", "trapCategory": "context"},
                    {"text": "反面", "isCorrect": False, "reason": "Incorrect. On the flip side.", "trapCategory": "meaning"},
                    {"text": "にとって", "isCorrect": False, "reason": "Incorrect. From perspective of.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern means 'compared with [benchmark standard]'?"
        }
    ])

    # ==================== SKM N3 PART 1 CHAPTER 5 ====================
    exercises.extend([
        {
            "id": "skm3-c5-ex-1",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 5",
            "type": "multiple-choice",
            "context": "Objective cause of delay: the train was delayed due to heavy snowfall.",
            "question": "大雪の（　　）、電車が大幅に遅れました。",
            "translation": "Due to heavy snowfall, the train was significantly delayed.",
            "options": ["ため", "おかげ", "せい", "ことから"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u5-tame-ni-causality",
            "grammarPointTitle": "〜ためだ / 〜ために (Objective Cause: Due to / Owing to)",
            "explanation": {
                "overall": "〜ために / 〜ため denotes objective, neutral causality ('due to / owing to'), standard in formal news and announcements.",
                "options": [
                    {"text": "ため", "isCorrect": True, "reason": "Correct. Objective cause: Noun のため / V-short ため.", "trapCategory": "meaning"},
                    {"text": "おかげ", "isCorrect": False, "reason": "Incorrect. おかげ denotes positive gratitude, inappropriate for train delay.", "trapCategory": "meaning"},
                    {"text": "せい", "isCorrect": False, "reason": "Incorrect. せい expresses blame, less formal/neutral than ため in public announcements.", "trapCategory": "context"},
                    {"text": "ことから", "isCorrect": False, "reason": "Incorrect. ことから denotes origin of name or judgment.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which word denotes objective, formal cause: 'due to / owing to'?"
        },
        {
            "id": "skm3-c5-ex-2",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 5",
            "type": "multiple-choice",
            "context": "Origin of a nickname: called 'Fuji' from the fact that its shape resembles Mt. Fuji.",
            "question": "形が富士山に似ている（　　）、「小富士」と呼ばれている。",
            "translation": "From the fact that its shape resembles Mt. Fuji, it is called 'Little Fuji'.",
            "options": ["ことから", "せいで", "おかげで", "ために"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u5-koto-kara-origin",
            "grammarPointTitle": "〜ことから (Origin of Name, Judgment, or Fact: Arising from the Fact That)",
            "explanation": {
                "overall": "〜ことから indicates the reason or origin why something is named, judged, or known as it is ('arising from the fact that / based on the clue that').",
                "options": [
                    {"text": "ことから", "isCorrect": True, "reason": "Correct. Origin of name/appellation: V-short + ことから (と呼ばれている).", "trapCategory": "meaning"},
                    {"text": "せいで", "isCorrect": False, "reason": "Incorrect. Blame for negative outcome.", "trapCategory": "meaning"},
                    {"text": "おかげで", "isCorrect": False, "reason": "Incorrect. Gratitude.", "trapCategory": "meaning"},
                    {"text": "ために", "isCorrect": False, "reason": "Incorrect. Direct physical causality, does not fit naming origin.", "trapCategory": "context"}
                ]
            },
            "hint": "Which pattern connects a characteristic feature to why something is named or called X?"
        },
        {
            "id": "skm3-c5-ex-3",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 5",
            "type": "multiple-choice",
            "context": "Positive outcome with gratitude: passed the exam thanks to the teacher's dedicated guidance.",
            "question": "先生の熱心なご指導の（　　）、合格できました。",
            "translation": "Thanks to the teacher's dedicated guidance, I was able to pass.",
            "options": ["おかげで", "せいで", "ことから", "あまり"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u5-okage-sei",
            "grammarPointTitle": "〜おかげで vs 〜せいで (Grace of / Due to Fault of)",
            "explanation": {
                "overall": "〜おかげで denotes gratitude for a favorable result brought about by someone or something ('thanks to / owing to the grace of').",
                "options": [
                    {"text": "おかげで", "isCorrect": True, "reason": "Correct. Positive gratitude: Noun のおかげで + favorable outcome.", "trapCategory": "meaning"},
                    {"text": "せいで", "isCorrect": False, "reason": "Incorrect. せいで is for blaming a negative outcome.", "trapCategory": "meaning"},
                    {"text": "ことから", "isCorrect": False, "reason": "Incorrect. Origin of name.", "trapCategory": "meaning"},
                    {"text": "あまり", "isCorrect": False, "reason": "Incorrect. Excess of emotion.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which expression means 'thanks to [someone's help]' for a favorable result?"
        },
        {
            "id": "skm3-c5-ex-4",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 5",
            "type": "multiple-choice",
            "context": "Blaming a negative outcome: lost the tennis match because of a lack of sleep.",
            "question": "睡眠不足の（　　）、試合で力を出せなかった。",
            "translation": "Because of / Due to the fault of lack of sleep, I couldn't perform well in the match.",
            "options": ["せいで", "おかげで", "ために", "ことから"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u5-okage-sei",
            "grammarPointTitle": "〜おかげで vs 〜せいで (Grace of / Due to Fault of)",
            "explanation": {
                "overall": "〜せいで attributes blame or responsibility to a cause for an undesirable, negative result ('because of / on account of [fault]').",
                "options": [
                    {"text": "せいで", "isCorrect": True, "reason": "Correct. Negative blame attribution: Noun のせいで + negative outcome.", "trapCategory": "meaning"},
                    {"text": "おかげで", "isCorrect": False, "reason": "Incorrect. おかげで requires a positive/favorable result.", "trapCategory": "meaning"},
                    {"text": "ために", "isCorrect": False, "reason": "Incorrect. ため is neutral, lacking the personal blame/frustration nuance of せいで.", "trapCategory": "context"},
                    {"text": "ことから", "isCorrect": False, "reason": "Incorrect. Origin of name/judgment.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern assigns blame to a factor for a bad or disappointing outcome?"
        }
    ])

    # ==================== SKM N3 PART 1 CHAPTER 6 ====================
    exercises.extend([
        {
            "id": "skm3-c6-ex-1",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 6",
            "type": "multiple-choice",
            "context": "Sole prerequisite: if only we have health, we can overcome anything.",
            "question": "健康（　　）あれ（　　）、何とかなる。",
            "translation": "As long as we have health (provided that sole condition is met), everything will work out.",
            "options": ["さえ・ば", "こそ・ば", "でも・ば", "だけ・ば"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u6-sae-ba",
            "grammarPointTitle": "〜さえ〜ば (If Only / Provided That Sole Prerequisite Is Met)",
            "explanation": {
                "overall": "〜さえ〜ば means 'if only / as long as X is fulfilled, nothing else matters' (健康さえあれば).",
                "options": [
                    {"text": "さえ・ば", "isCorrect": True, "reason": "Correct. Sole prerequisite formula: Noun さえ + Verb-ba (健康さえあれば).", "trapCategory": "formation"},
                    {"text": "こそ・ば", "isCorrect": False, "reason": "Incorrect. こそ denotes emphasis, not prerequisite pairing with ば.", "trapCategory": "formation"},
                    {"text": "でも・ば", "isCorrect": False, "reason": "Incorrect. Ungrammatical mixture.", "trapCategory": "formation"},
                    {"text": "だけ・ば", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the formula for 'if only / as long as [condition is met]'?"
        },
        {
            "id": "skm3-c6-ex-2",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 6",
            "type": "multiple-choice",
            "context": "Strong hypothetical concession: even if everyone opposes it, I will not give up.",
            "question": "たとえ全員に反対され（　　）、私は諦めません。",
            "translation": "Even if I am opposed by everyone, I will not give up.",
            "options": ["ても", "たら", "れば", "と"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u6-tatoe-temo",
            "grammarPointTitle": "たとえ〜ても (Even If / Even Granting That Hypothetical X Occurs)",
            "explanation": {
                "overall": "たとえ…ても means 'even granting that hypothetical X occurs, the outcome in Y remains steadfast' (たとえ〜ても).",
                "options": [
                    {"text": "ても", "isCorrect": True, "reason": "Correct. たとえ pairs with concessive 〜ても (たとえ…ても).", "trapCategory": "formation"},
                    {"text": "たら", "isCorrect": False, "reason": "Incorrect. たとえ standardly requires ても (or たとえ〜でも).", "trapCategory": "formation"},
                    {"text": "れば", "isCorrect": False, "reason": "Incorrect. ば does not pair with たとえ.", "trapCategory": "formation"},
                    {"text": "と", "isCorrect": False, "reason": "Incorrect. と does not pair with たとえ.", "trapCategory": "formation"}
                ]
            },
            "hint": "What concessive ending standardly pairs with the adverb たとえ ('even granting that...')?"
        },
        {
            "id": "skm3-c6-ex-3",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 6",
            "type": "multiple-choice",
            "context": "Negative progressive consequence: if you make such careless mistakes repeatedly, you will lose customer trust.",
            "question": "そんなミスを続け（　　）、信用を失ってしまいますよ。",
            "translation": "If you keep making mistakes like that, you will lose your credibility.",
            "options": ["ては", "たら", "れば", "なら"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u6-tewa-dewa-negative-consequence",
            "grammarPointTitle": "〜ては / 〜では (If Such a Condition Persists, Disaster Will Follow)",
            "explanation": {
                "overall": "〜ては / 〜では indicates that if the currently ongoing or repeated undesirable action continues, an inevitable negative consequence will follow.",
                "options": [
                    {"text": "ては", "isCorrect": True, "reason": "Correct. Condition leading to disaster: V-te + は (続けては).", "trapCategory": "meaning"},
                    {"text": "たら", "isCorrect": False, "reason": "Incorrect. たら is neutral hypothetical, lacking the warning against ongoing persistent error.", "trapCategory": "context"},
                    {"text": "れば", "isCorrect": False, "reason": "Incorrect. Less focused on warning against habit.", "trapCategory": "context"},
                    {"text": "なら", "isCorrect": False, "reason": "Incorrect. Contextual limitation.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern warns that continuing an undesirable action will lead to disaster: 〜ては or 〜たら?"
        }
    ])

    # ==================== SKM N3 PART 1 CHAPTER 8 ====================
    exercises.extend([
        {
            "id": "skm3-c8-ex-1",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 8",
            "type": "multiple-choice",
            "context": "Partial truth: 'Expensive things are not necessarily of good quality'.",
            "question": "値段が高いものが必ずしも良いものだ（　　）。",
            "translation": "Things that are expensive are not necessarily good.",
            "options": ["とは限らない", "わけがない", "はずがない", "に違いない"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u8-to-wa-kagiranai-not-necessarily",
            "grammarPointTitle": "〜とは限らない (Partial Truth: Not Necessarily the Case)",
            "explanation": {
                "overall": "〜とは限らない (frequently paired with 必ずしも) indicates partial negation: 'it is not necessarily the case that X is always true'.",
                "options": [
                    {"text": "とは限らない", "isCorrect": True, "reason": "Correct. Partial negation: (必ずしも)〜とは限らない.", "trapCategory": "meaning"},
                    {"text": "わけがない", "isCorrect": False, "reason": "Incorrect. わけがない means 'there is no way / impossible', clashing with partial truth.", "trapCategory": "meaning"},
                    {"text": "はずがない", "isCorrect": False, "reason": "Incorrect. Cannot possibly be.", "trapCategory": "meaning"},
                    {"text": "に違いない", "isCorrect": False, "reason": "Incorrect. Affirmative certainty ('must be').", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern pairs with 必ずしも to mean 'not necessarily the case'?"
        },
        {
            "id": "skm3-c8-ex-2",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 8",
            "type": "multiple-choice",
            "context": "Absolute impossibility: 'There is no way a three-year-old child could solve this college math problem!'.",
            "question": "三歳の子どもにこんな難しい問題が解ける（　　）。",
            "translation": "There is absolutely no way a three-year-old child could solve such a difficult problem!",
            "options": ["わけがない", "わけではない", "とは限らない", "ものだ"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u8-wake-ga-nai",
            "grammarPointTitle": "〜わけがない (There Is Absolutely No Way That... / Utter Impossibility)",
            "explanation": {
                "overall": "〜わけがない expresses complete, emphatic logical impossibility based on common sense ('there is absolutely no reason or possibility that X could happen').",
                "options": [
                    {"text": "わけがない", "isCorrect": True, "reason": "Correct. Utter impossibility: V-potential + わけがない.", "trapCategory": "meaning"},
                    {"text": "わけではない", "isCorrect": False, "reason": "Incorrect. わけではない is mild partial negation ('it doesn't mean that'), clashing with total impossibility.", "trapCategory": "meaning"},
                    {"text": "とは限らない", "isCorrect": False, "reason": "Incorrect. Not necessarily.", "trapCategory": "meaning"},
                    {"text": "ものだ", "isCorrect": False, "reason": "Incorrect. General truth or nostalgia.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern expresses utter logical impossibility: 'there is no way that...'?"
        },
        {
            "id": "skm3-c8-ex-3",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 8",
            "type": "multiple-choice",
            "context": "Mild partial disclaimer: 'It's not that I hate Japanese food, but raw fish is a bit tough for me'.",
            "question": "日本料理が嫌いな（　　）が、生魚は少し苦手です。",
            "translation": "It doesn't mean that I dislike Japanese food, but raw fish is a bit hard for me.",
            "options": ["わけではない", "わけがない", "はずがない", "にすぎない"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u8-wake-dewa-nai",
            "grammarPointTitle": "〜わけではない (It Doesn't Mean That... / Partial Negation)",
            "explanation": {
                "overall": "〜わけではない (or 〜わけじゃない) softens an absolute statement: 'it does not mean that... / it is not that...'.",
                "options": [
                    {"text": "わけではない", "isCorrect": True, "reason": "Correct. Partial disclaimer/negation: 〜わけではない.", "trapCategory": "meaning"},
                    {"text": "わけがない", "isCorrect": False, "reason": "Incorrect. わけがない expresses utter impossibility ('there is no way I dislike it'), too harsh.", "trapCategory": "meaning"},
                    {"text": "はずがない", "isCorrect": False, "reason": "Incorrect. Cannot be.", "trapCategory": "meaning"},
                    {"text": "にすぎない", "isCorrect": False, "reason": "Incorrect. Merely/only.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern softens a statement to mean 'it's not that / it doesn't mean that'?"
        },
        {
            "id": "skm3-c8-ex-4",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 8",
            "type": "multiple-choice",
            "context": "Double negative litotes: 'If pressed, it's not that I can't eat spicy food'.",
            "question": "辛い料理は、食べられ（　　）が、あまり好きではありません。",
            "translation": "It's not that I can't eat spicy food, but I don't like it very much.",
            "options": ["ないこともない", "わけがない", "はずがない", "ないほうがいい"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u8-nai-koto-wa-nai-litotes",
            "grammarPointTitle": "〜ないことはない / 〜ないこともない (Double Negative Litotes: It's Not That I Can't)",
            "explanation": {
                "overall": "〜ないことはない / 〜ないこともない is a double negative litotes expressing hesitant affirmation ('it's not that I can't / I can do it if required').",
                "options": [
                    {"text": "ないこともない", "isCorrect": True, "reason": "Correct. Double negative litotes: Verb-nai + こともない (食べられないこともない).", "trapCategory": "meaning"},
                    {"text": "わけがない", "isCorrect": False, "reason": "Incorrect. Utter impossibility.", "trapCategory": "meaning"},
                    {"text": "はずがない", "isCorrect": False, "reason": "Incorrect. Cannot be.", "trapCategory": "meaning"},
                    {"text": "ないほうがいい", "isCorrect": False, "reason": "Incorrect. Advice.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which double negative expression means 'it's not that I cannot [do it]'?"
        }
    ])

    # ==================== SKM N3 PART 1 CHAPTER 10 ====================
    exercises.extend([
        {
            "id": "skm3-c10-ex-1",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 10",
            "type": "multiple-choice",
            "context": "Moral obligation: 'One should keep promises made to others'.",
            "question": "人との約束は守る（　　）です。",
            "translation": "One should keep promises made to others. (Moral/ethical duty)",
            "options": ["べき", "はず", "わけ", "ところ"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u9-beki-da",
            "grammarPointTitle": "〜べきだ / 〜べきではない (Should / Ought To - Moral Duty)",
            "explanation": {
                "overall": "〜べきだ expresses universal common-sense, social responsibility, or moral duty ('should / ought to do'). Attached to dictionary verbs (守るべきだ). する becomes すべき or するべき.",
                "options": [
                    {"text": "べき", "isCorrect": True, "reason": "Correct. Moral/ethical obligation: V-dict + べきだ.", "trapCategory": "meaning"},
                    {"text": "はず", "isCorrect": False, "reason": "Incorrect. はず denotes logical expectation based on schedule.", "trapCategory": "meaning"},
                    {"text": "わけ", "isCorrect": False, "reason": "Incorrect. わけ denotes reason or explanation.", "trapCategory": "meaning"},
                    {"text": "ところ", "isCorrect": False, "reason": "Incorrect. Temporal phase.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which auxiliary noun expresses moral or social duty: 'ought to / should'?"
        },
        {
            "id": "skm3-c10-ex-2",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 10",
            "type": "multiple-choice",
            "context": "Citing an external source: 'According to the news, an earthquake occurred'.",
            "question": "ニュースの報道（　　）、今朝地震があったそうです。",
            "translation": "According to the news report, an earthquake occurred this morning.",
            "options": ["によると", "に対して", "にとって", "について"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u10-ni-yoru-to",
            "grammarPointTitle": "〜によると / 〜によれば (According To Source of Information)",
            "explanation": {
                "overall": "〜によると (or 〜によれば) cites an authoritative source of information, always ending with hearsay (〜そうだ / 〜とのことだ).",
                "options": [
                    {"text": "によると", "isCorrect": True, "reason": "Correct. Information source citation: Noun + によると + 〜そうだ.", "trapCategory": "meaning"},
                    {"text": "に対して", "isCorrect": False, "reason": "Incorrect. In contrast to.", "trapCategory": "meaning"},
                    {"text": "にとって", "isCorrect": False, "reason": "Incorrect. From perspective of.", "trapCategory": "meaning"},
                    {"text": "について", "isCorrect": False, "reason": "Incorrect. About/regarding.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern cites an information source: 'according to [source]'?"
        }
    ])

    # ==================== SKM N3 PART 1 CHAPTER 11 ====================
    exercises.extend([
        {
            "id": "skm3-c11-ex-1",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 11",
            "type": "multiple-choice",
            "context": "Action on the verge of inception interrupted: 'Just as I was about to board the train, the doors closed!'.",
            "question": "電車に乗（　　）とした時、ドアが閉まってしまった。",
            "translation": "Just as I was attempting / about to board the train, the doors shut.",
            "options": ["ろう", "り", "る", "った"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u11-you-to-suru-inception",
            "grammarPointTitle": "〜(よ)うとする (On the Very Verge Of / In the Act of Attempting)",
            "explanation": {
                "overall": "Volitional form + とする denotes an action on the very verge of taking place (乗ろうとする時) or an active physical struggle to perform an action.",
                "options": [
                    {"text": "ろう", "isCorrect": True, "reason": "Correct. Volitional inception: 乗る -> 乗ろうとする.", "trapCategory": "formation"},
                    {"text": "り", "isCorrect": False, "reason": "Incorrect. Masu-stem cannot attach とする.", "trapCategory": "formation"},
                    {"text": "る", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach とする.", "trapCategory": "formation"},
                    {"text": "った", "isCorrect": False, "reason": "Incorrect. Ta-form cannot attach とする.", "trapCategory": "formation"}
                ]
            },
            "hint": "What verb form attaches to とする to mean 'on the verge of / attempting to'?"
        },
        {
            "id": "skm3-c11-ex-2",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 11",
            "type": "multiple-choice",
            "context": "Conscious ongoing effort: 'I make an effort to sleep before 11:00 every night'.",
            "question": "毎晩十一時前には寝る（　　）しています。",
            "translation": "I make an effort to go to bed before 11:00 every night.",
            "options": ["ように", "ことに", "ために", "とおりに"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u7-you-ni-suru",
            "grammarPointTitle": "〜ようにする (Make an Effort To / Endeavor Habitually)",
            "explanation": {
                "overall": "〜ようにする denotes making a deliberate, conscious ongoing effort to maintain a good habit or behavior.",
                "options": [
                    {"text": "ように", "isCorrect": True, "reason": "Correct. Conscious endeavor: V-dict + ようにする / ようにしている.", "trapCategory": "meaning"},
                    {"text": "ことに", "isCorrect": False, "reason": "Incorrect. ことにする is a firm resolution/decision, while ようにする emphasizes daily gradual effort.", "trapCategory": "context"},
                    {"text": "ために", "isCorrect": False, "reason": "Incorrect. Purpose/cause.", "trapCategory": "meaning"},
                    {"text": "とおりに", "isCorrect": False, "reason": "Incorrect. In accordance with.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which pattern expresses making a conscious effort to build a habit: 〜ようにする or 〜ことにする?"
        }
    ])

    # ==================== SKM N3 PART 1 CHAPTER 7 ====================
    exercises.extend([
        {
            "id": "skm3-c7-ex-1",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 7",
            "type": "multiple-choice",
            "context": "Formal hearsay / report: 'According to the letter, everyone in the family is doing well'.",
            "question": "手紙によると、ご家族の皆様もお元気だ（　　）。",
            "translation": "According to the letter, everyone in your family is doing well. (Formal hearsay)",
            "options": ["とのことです", "というわけです", "とするはずです", "といいことです"],
            "correctIndex": 0,
            "grammarPointId": "added-n3-7-49",
            "grammarPointTitle": "〜ということだ・〜とのことだ",
            "explanation": {
                "overall": "〜とのことだ / 〜ということだ reports information relayed through formal letters, correspondence, or official channels ('I understand that / reportedly').",
                "options": [
                    {"text": "とのことです", "isCorrect": True, "reason": "Correct. Formal correspondence hearsay: 〜とのことです.", "trapCategory": "formation"},
                    {"text": "というわけです", "isCorrect": False, "reason": "Incorrect. というわけです explains logical deduction.", "trapCategory": "meaning"},
                    {"text": "とするはずです", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"},
                    {"text": "といいことです", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What formal hearsay pattern standardly reports news received via letters or messages?"
        },
        {
            "id": "skm3-c7-ex-2",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 7",
            "type": "multiple-choice",
            "context": "Common consensus / general belief: 'It is said that green tea is good for health'.",
            "question": "緑茶は健康に良い（　　）。",
            "translation": "It is said that green tea is good for health.",
            "options": ["と言われている", "と思っている", "と話されている", "と聞かれている"],
            "correctIndex": 0,
            "grammarPointId": "added-n3-7-50",
            "grammarPointTitle": "〜と言われている",
            "explanation": {
                "overall": "〜と言われている denotes general societal consensus or established popular belief ('it is widely said that...').",
                "options": [
                    {"text": "と言われている", "isCorrect": True, "reason": "Correct. Passive consensus: 〜と言われている.", "trapCategory": "meaning"},
                    {"text": "と思っている", "isCorrect": False, "reason": "Incorrect. Expresses single speaker's ongoing thought.", "trapCategory": "context"},
                    {"text": "と話されている", "isCorrect": False, "reason": "Incorrect. Non-standard for general wisdom.", "trapCategory": "formation"},
                    {"text": "と聞かれている", "isCorrect": False, "reason": "Incorrect. Passive of ask/hear.", "trapCategory": "meaning"}
                ]
            },
            "hint": "What pattern expresses general wisdom: 'it is widely said that...'?"
        }
    ])

    # ==================== SKM N3 PART 1 CHAPTER 9 ====================
    exercises.extend([
        {
            "id": "skm3-c9-ex-1",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 9",
            "type": "multiple-choice",
            "context": "Third-person visible sensation: the child looks cold and is shivering.",
            "question": "子どもが寒（　　）にしています。",
            "translation": "The child is acting cold / showing outward signs of being cold.",
            "options": ["がりそう", "そう", "く", "い"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u9-garu",
            "grammarPointTitle": "〜がる / 〜がっている (Third-Person Manifestation of Desires & Sensations)",
            "explanation": {
                "overall": "〜がる turns an internal sensation or desire adjective (寒い, 痛い, ほしい) into an outwardly observable third-person action (寒がる -> 寒がりそう).",
                "options": [
                    {"text": "がりそう", "isCorrect": True, "reason": "Correct. Outward behavior suffix: 寒がりそうにしている.", "trapCategory": "formation"},
                    {"text": "そう", "isCorrect": False, "reason": "Incorrect. 寒そう describes mere visual appearance, not the continuous outward physical behavior of the child.", "trapCategory": "context"},
                    {"text": "く", "isCorrect": False, "reason": "Incorrect. Adverbial form.", "trapCategory": "formation"},
                    {"text": "い", "isCorrect": False, "reason": "Incorrect. Plain adjective.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which suffix converts an internal adjective into an outwardly displayed third-person behavior?"
        },
        {
            "id": "skm3-c9-ex-2",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 9",
            "type": "multiple-choice",
            "context": "Wanting someone else to do an action: 'I want my parents to understand my dream'.",
            "question": "両親に私の夢を理解し（　　）です。",
            "translation": "I want my parents to understand my dream.",
            "options": ["てもらいたい", "たい", "たがって", "させたい"],
            "correctIndex": 0,
            "grammarPointId": "added-n3-9-53",
            "grammarPointTitle": "〜てもらいたい・〜てほしい",
            "explanation": {
                "overall": "〜てもらいたい (or 〜てほしい) indicates the speaker's desire for another person to perform an action for them (Person に Verb te-form + もらいたい).",
                "options": [
                    {"text": "てもらいたい", "isCorrect": True, "reason": "Correct. Wanting someone to do: Person に V-te + もらいたい.", "trapCategory": "meaning"},
                    {"text": "たい", "isCorrect": False, "reason": "Incorrect. 〜たい expresses wanting to do it oneself.", "trapCategory": "meaning"},
                    {"text": "たがって", "isCorrect": False, "reason": "Incorrect. Third-person desire.", "trapCategory": "meaning"},
                    {"text": "させたい", "isCorrect": False, "reason": "Incorrect. Causative ('make parents understand').", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which expression means 'I want [someone else] to do [action] for me'?"
        }
    ])

    # ==================== SKM N3 PART 1 CHAPTER 12 ====================
    exercises.extend([
        {
            "id": "skm3-c12-ex-1",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 12",
            "type": "multiple-choice",
            "context": "Honorific form for Sino-Japanese verbal nouns: 'The president has already left the office'.",
            "question": "社長はすでに（　　）になりました。",
            "translation": "The company president has already left the office. (Honorific)",
            "options": ["ご退社", "お退社", "退社", "ご退社し"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u12-keigo-respect",
            "grammarPointTitle": "お〜になる / ご〜になる (Honorific Respect - Elevating Others' Actions)",
            "explanation": {
                "overall": "For Sino-Japanese verbal nouns (Suru-verbs), the honorific respect formula is: ご + Noun + になる (ご退社になりました).",
                "options": [
                    {"text": "ご退社", "isCorrect": True, "reason": "Correct. Sino-Japanese honorific formula: ご + Verbal Noun + になる.", "trapCategory": "formation"},
                    {"text": "お退社", "isCorrect": False, "reason": "Incorrect. お prefix is standardly for native Japanese words; Sino-Japanese words take ご.", "trapCategory": "formation"},
                    {"text": "退社", "isCorrect": False, "reason": "Incorrect. Missing honorific prefix ご.", "trapCategory": "formation"},
                    {"text": "ご退社し", "isCorrect": False, "reason": "Incorrect. Redundant verb stem.", "trapCategory": "formation"}
                ]
            },
            "hint": "What honorific prefix do Sino-Japanese words take before になる?"
        },
        {
            "id": "skm3-c12-ex-2",
            "bookId": "skm-n3",
            "chapter": "Part 1 · Chapter 12",
            "type": "multiple-choice",
            "context": "Humble deference for Sino-Japanese verbal nouns: 'I will guide you to the meeting room'.",
            "question": "会議室までご（　　）いたします。",
            "translation": "I will guide you to the conference room. (Humble deference)",
            "options": ["案内", "案内に", "案内になり", "案内させて"],
            "correctIndex": 0,
            "grammarPointId": "skm3-u12-keigo-humble",
            "grammarPointTitle": "お〜する / ご〜する (Humble Deference - Lowering One's Own Actions)",
            "explanation": {
                "overall": "The humble deference formula for Sino-Japanese verbal nouns is: ご + Noun + する / いたす (ご案内いたします).",
                "options": [
                    {"text": "案内", "isCorrect": True, "reason": "Correct. Humble formula: ご + Verbal Noun + いたします: ご案内いたします.", "trapCategory": "formation"},
                    {"text": "案内に", "isCorrect": False, "reason": "Incorrect. に belongs to honorific になる, not humble いたします.", "trapCategory": "formation"},
                    {"text": "案内になり", "isCorrect": False, "reason": "Incorrect. Honorific formula, inappropriate for speaker.", "trapCategory": "context"},
                    {"text": "案内させて", "isCorrect": False, "reason": "Incorrect. Causative insertion error.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the humble formula for Sino-Japanese verbs: ご + [noun] + ___?"
        }
    ])

    return exercises

if __name__ == "__main__":
    ex_list = get_skm3_all_exercises()
    print(f"Generated {len(ex_list)} SKM N3 exercises across Part 1.")
