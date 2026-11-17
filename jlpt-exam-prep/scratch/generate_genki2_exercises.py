import json

def get_genki2_exercises():
    exercises = []

    # ==================== LESSON 13 ====================
    exercises.extend([
        {
            "id": "g2-l13-ex-1",
            "bookId": "genki-2",
            "chapter": "Lesson 13",
            "type": "multiple-choice",
            "context": "Stating ability: Ken can read Japanese kanji.",
            "question": "けんさんは漢字を（　　）。",
            "translation": "Ken can read kanji.",
            "options": ["読めます", "読まれます", "読みられます", "読めるです"],
            "correctIndex": 0,
            "grammarPointId": "g2-l13-potential",
            "grammarPointTitle": "可能形 (Potential Verbs: Ability & Possibility)",
            "explanation": {
                "overall": "U-verb potential formation: change final -u vowel to -e and add -ru / -masu (読む -> 読める -> 読めます).",
                "options": [
                    {"text": "読めます", "isCorrect": True, "reason": "Correct. U-verb potential: mu -> me + masu.", "trapCategory": "formation"},
                    {"text": "読まれます", "isCorrect": False, "reason": "Incorrect. Passive/honorific form, not potential.", "trapCategory": "formation"},
                    {"text": "読みられます", "isCorrect": False, "reason": "Incorrect. Irregular overgeneralization of Ru-verb potential.", "trapCategory": "formation"},
                    {"text": "読めるです", "isCorrect": False, "reason": "Incorrect. Plain potential verb cannot take です directly.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the potential form of the U-verb 読む?"
        },
        {
            "id": "g2-l13-ex-2",
            "bookId": "genki-2",
            "chapter": "Lesson 13",
            "type": "multiple-choice",
            "context": "Potential verb particle choice: I can speak Japanese.",
            "question": "私は日本語（　　）話せます。",
            "translation": "I can speak Japanese.",
            "options": ["が", "に", "で", "へ"],
            "correctIndex": 0,
            "grammarPointId": "g2-l13-potential",
            "grammarPointTitle": "可能形 (Potential Verbs: Ability & Possibility)",
            "explanation": {
                "overall": "With potential verbs, the direct object particle を is standardly replaced by が in textbook Japanese (日本語が話せます).",
                "options": [
                    {"text": "が", "isCorrect": True, "reason": "Correct. Standard textbook potential object particle is が.", "trapCategory": "formation"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. に does not mark the target ability of potential verbs.", "trapCategory": "meaning"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で marks instrument/means, not the target ability.", "trapCategory": "meaning"},
                    {"text": "へ", "isCorrect": False, "reason": "Incorrect. へ marks direction of movement.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle standardly marks the object of a potential verb in Genki II?"
        },
        {
            "id": "g2-l13-ex-3",
            "bookId": "genki-2",
            "chapter": "Lesson 13",
            "type": "multiple-choice",
            "context": "Listing multiple reasons for liking a coffee shop: coffee is delicious AND the atmosphere is quiet.",
            "question": "コーヒーも美味しい（　　）、静かだ（　　）、この店が好きです。",
            "translation": "The coffee is delicious, and it is quiet, so I like this shop.",
            "options": ["し・し", "から・から", "ので・ので", "て・て"],
            "correctIndex": 0,
            "grammarPointId": "g2-l13-shi-reasons",
            "grammarPointTitle": "〜し、〜し (Listing Multiple Parallel Reasons)",
            "explanation": {
                "overall": "The connective 〜し lists multiple coordinate reasons leading to a conclusion: Reason 1 し、Reason 2 し、[Result].",
                "options": [
                    {"text": "し・し", "isCorrect": True, "reason": "Correct. Multiple parallel reason linker: 〜し、〜し.", "trapCategory": "formation"},
                    {"text": "から・から", "isCorrect": False, "reason": "Incorrect. Repeating から consecutively is unnatural in standard Japanese.", "trapCategory": "formation"},
                    {"text": "ので・ので", "isCorrect": False, "reason": "Incorrect. Repeating ので consecutively in coordinate clauses is ungrammatical.", "trapCategory": "formation"},
                    {"text": "て・て", "isCorrect": False, "reason": "Incorrect. Te-forms link sequential states, not emphatic cumulative reasons.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle is used to list multiple parallel reasons leading to a decision?"
        },
        {
            "id": "g2-l13-ex-4",
            "bookId": "genki-2",
            "chapter": "Lesson 13",
            "type": "multiple-choice",
            "context": "Trying out an action to test the experience: trying on a sweater at a clothing store.",
            "question": "このセーターを着（　　）もいいですか。",
            "translation": "May I try on this sweater?",
            "options": ["てみて", "てあり", "ておき", "てい"],
            "correctIndex": 0,
            "grammarPointId": "g2-l13-te-miru",
            "grammarPointTitle": "〜てみる (Trying Out an Action: Doing Something to See What Happens)",
            "explanation": {
                "overall": "〜てみる means doing something tentatively to test or see what happens. '着てみる' means 'try wearing / try on'. Combined with permission: 着てみてもいいですか.",
                "options": [
                    {"text": "てみて", "isCorrect": True, "reason": "Correct. Te-form of 〜てみる before もいいですか: 着てみてもいいですか.", "trapCategory": "formation"},
                    {"text": "てあり", "isCorrect": False, "reason": "Incorrect. 〜てある is transitive preparation, not trial.", "trapCategory": "meaning"},
                    {"text": "ておき", "isCorrect": False, "reason": "Incorrect. 〜ておく is preparation in advance.", "trapCategory": "meaning"},
                    {"text": "てい", "isCorrect": False, "reason": "Incorrect. 〜ている is progressive/resultant state.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which auxiliary verb expresses doing an action to see what it is like ('try doing')?"
        },
        {
            "id": "g2-l13-ex-5",
            "bookId": "genki-2",
            "chapter": "Lesson 13",
            "type": "multiple-choice",
            "context": "Contextual limitation with なら: 'If it is hiragana, I can read it (though kanji is impossible)'.",
            "question": "ひらがな（　　）読めますが、漢字はまだ読めません。",
            "translation": "If it is hiragana, I can read it (as for hiragana), but I can't read kanji yet.",
            "options": ["なら", "たら", "ば", "と"],
            "correctIndex": 0,
            "grammarPointId": "g2-l13-nara-conditional",
            "grammarPointTitle": "なら (Contextual Limitation Conditional: If It's X / As For X)",
            "explanation": {
                "overall": "なら provides contextual limitation ('if it's X / as for X, within that boundary'). Often implies a contrast with other possibilities.",
                "options": [
                    {"text": "なら", "isCorrect": True, "reason": "Correct. Contextual limitation conditional: Noun + なら.", "trapCategory": "context"},
                    {"text": "たら", "isCorrect": False, "reason": "Incorrect. Noun + だったら expresses past hypothetical condition, not topical domain restriction.", "trapCategory": "formation"},
                    {"text": "ば", "isCorrect": False, "reason": "Incorrect. Nouns do not attach ば directly without であれば.", "trapCategory": "formation"},
                    {"text": "と", "isCorrect": False, "reason": "Incorrect. と indicates natural consequence, not contextual limitation.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which conditional particle sets a contextual limitation: 'if it is [Noun]'?"
        },
        {
            "id": "g2-l13-ex-6",
            "bookId": "genki-2",
            "chapter": "Lesson 13",
            "type": "multiple-choice",
            "context": "Judging appearance from visual evidence: looking at dark clouds and judging rain is imminent.",
            "question": "空が暗いです。雨が降り（　　）ですね。",
            "translation": "The sky is dark. It looks like it will rain, doesn't it?",
            "options": ["そう", "らしい", "よう", "みたい"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-13-20",
            "grammarPointTitle": "〜そうです：様子",
            "explanation": {
                "overall": "Appearance 〜そうです ('looks like / on the verge of') attaches to the verb stem (降る -> 降り -> 降りそうです).",
                "options": [
                    {"text": "そう", "isCorrect": True, "reason": "Correct. Verb stem + そうです: 降りそうです ('looks like it will rain').", "trapCategory": "formation"},
                    {"text": "らしい", "isCorrect": False, "reason": "Incorrect. らしい takes dictionary form (降るらしい) and means hearsay/conjecture.", "trapCategory": "formation"},
                    {"text": "よう", "isCorrect": False, "reason": "Incorrect. よう requires dictionary form and な/に.", "trapCategory": "formation"},
                    {"text": "みたい", "isCorrect": False, "reason": "Incorrect. みたい requires dictionary form (降るみたい).", "trapCategory": "formation"}
                ]
            },
            "hint": "What appearance suffix attaches directly to the verb stem to mean 'looks like / on the verge of'?"
        },
        {
            "id": "g2-l13-ex-7",
            "bookId": "genki-2",
            "chapter": "Lesson 13",
            "type": "multiple-choice",
            "context": "Visual appearance of delicious food: looking at a fresh cake.",
            "question": "このケーキはとても美味し（　　）です。",
            "translation": "This cake looks delicious.",
            "options": ["そう", "いそう", "かったそう", "くそう"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-13-20",
            "grammarPointTitle": "〜そうです：様子",
            "explanation": {
                "overall": "For い-adjectives, drop final い before appearance そうです: 美味しい -> 美味し + そうです (美味しそうです).",
                "options": [
                    {"text": "そう", "isCorrect": True, "reason": "Correct. い-adjective stem (drop -i) + そうです.", "trapCategory": "formation"},
                    {"text": "いそう", "isCorrect": False, "reason": "Incorrect. Retaining -i is hearsay (美味しいそうです = 'I hear it is delicious'), not visual appearance.", "trapCategory": "meaning"},
                    {"text": "かったそう", "isCorrect": False, "reason": "Incorrect. Past hearsay, not present appearance.", "trapCategory": "formation"},
                    {"text": "くそう", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "Do you drop or keep the final い of an adjective when expressing visual appearance ('looks delicious')?"
        },
        {
            "id": "g2-l13-ex-8",
            "bookId": "genki-2",
            "chapter": "Lesson 13",
            "type": "multiple-choice",
            "context": "Irregular appearance formation for いい (good): looking at a nice design.",
            "question": "そのアイデアはとても（　　）ですね。",
            "translation": "That idea looks / sounds very good, doesn't it?",
            "options": ["よさそう", "いいそう", "よそう", "いくそう"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-13-20",
            "grammarPointTitle": "〜そうです：様子",
            "explanation": {
                "overall": "Famous irregular rule: the appearance form of いい is よさそう (NOT *いいそう or *よそう).",
                "options": [
                    {"text": "よさそう", "isCorrect": True, "reason": "Correct. Irregular appearance of いい is よさそう.", "trapCategory": "formation"},
                    {"text": "いいそう", "isCorrect": False, "reason": "Incorrect. いいそう is hearsay ('I hear it is good').", "trapCategory": "meaning"},
                    {"text": "よそう", "isCorrect": False, "reason": "Incorrect. Missing inserted さ.", "trapCategory": "formation"},
                    {"text": "いくそう", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the irregular appearance form of the adjective いい?"
        },
        {
            "id": "g2-l13-ex-9",
            "bookId": "genki-2",
            "chapter": "Lesson 13",
            "type": "multiple-choice",
            "context": "Stating frequency per period: brushing teeth three times in one day.",
            "question": "一日に（　　）歯を磨きます。",
            "translation": "I brush my teeth three times a day.",
            "options": ["三回", "三度で", "三回に", "三回を"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-13-21",
            "grammarPointTitle": "期間に回数",
            "explanation": {
                "overall": "The frequency formula is: [Period] に [Quantity/Times] (e.g. 一日に三回). The frequency count stands adverbially without extra particles.",
                "options": [
                    {"text": "三回", "isCorrect": True, "reason": "Correct. Formula: [Period] に [Count]: 一日に三回.", "trapCategory": "formation"},
                    {"text": "三度で", "isCorrect": False, "reason": "Incorrect. Extra で is ungrammatical.", "trapCategory": "formation"},
                    {"text": "三回に", "isCorrect": False, "reason": "Incorrect. に belongs after the time frame, not the counter.", "trapCategory": "formation"},
                    {"text": "三回を", "isCorrect": False, "reason": "Incorrect. Counter is not a direct object.", "trapCategory": "formation"}
                ]
            },
            "hint": "How do you state frequency of an action within a given time period?"
        },
        {
            "id": "g2-l13-ex-10",
            "bookId": "genki-2",
            "chapter": "Lesson 13",
            "type": "multiple-choice",
            "context": "Irregular verb potential: する (to do) and くる (to come).",
            "question": "あしたのパーティーに（　　）か。",
            "translation": "Can you come to tomorrow's party?",
            "options": ["こられます", "これます", "きられます", "きれます"],
            "correctIndex": 0,
            "grammarPointId": "g2-l13-potential",
            "grammarPointTitle": "可能形 (Potential Verbs: Ability & Possibility)",
            "explanation": {
                "overall": "The potential form of くる is こられる (polite こられます).",
                "options": [
                    {"text": "こられます", "isCorrect": True, "reason": "Correct. Potential form of くる is こられる / こられます.", "trapCategory": "formation"},
                    {"text": "これます", "isCorrect": False, "reason": "Incorrect. Colloquial ra-nuki form; standard textbook Genki II form is こられます.", "trapCategory": "formation"},
                    {"text": "きられます", "isCorrect": False, "reason": "Incorrect. Stem vowel must be ko-, not ki-.", "trapCategory": "formation"},
                    {"text": "きれます", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What is the standard potential form of the irregular verb くる?"
        }
    ])

    # ==================== LESSON 14 ====================
    exercises.extend([
        {
            "id": "g2-l14-ex-1",
            "bookId": "genki-2",
            "chapter": "Lesson 14",
            "type": "multiple-choice",
            "context": "Expressing desire for an object: I want a new smartphone.",
            "question": "新しいスマホ（　　）ほしいです。",
            "translation": "I want a new smartphone.",
            "options": ["が", "を", "に", "で"],
            "correctIndex": 0,
            "grammarPointId": "g2-l14-hoshii",
            "grammarPointTitle": "ほしい (Expressing Desire for an Object: Want Something)",
            "explanation": {
                "overall": "ほしい is an い-adjective meaning 'desirable / wanted'. The desired object is marked with particle が (Noun が ほしいです).",
                "options": [
                    {"text": "が", "isCorrect": True, "reason": "Correct. Object of ほしい takes particle が.", "trapCategory": "formation"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. ほしい is an adjective, not a transitive verb; を is unnatural in standard grammar.", "trapCategory": "formation"},
                    {"text": "に", "isCorrect": False, "reason": "Incorrect. に does not mark the desired object.", "trapCategory": "meaning"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で does not mark the desired object.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle marks the desired item with the adjective ほしい?"
        },
        {
            "id": "g2-l14-ex-2",
            "bookId": "genki-2",
            "chapter": "Lesson 14",
            "type": "multiple-choice",
            "context": "Describing third-person desire for an object: Ken wants a new car.",
            "question": "けんさんは新しい車を（　　）。",
            "translation": "Ken wants a new car. (Describing third-person desire)",
            "options": ["ほしがっています", "ほしいです", "ほしがるでした", "ほしかったです"],
            "correctIndex": 0,
            "grammarPointId": "g2-l14-hoshii",
            "grammarPointTitle": "ほしい (Expressing Desire for an Object: Want Something)",
            "explanation": {
                "overall": "ほしいです is restricted to the speaker's own desires. For third persons, Japanese uses ほしがっている (and the particle shifts from が to を).",
                "options": [
                    {"text": "ほしがっています", "isCorrect": True, "reason": "Correct. Third-person desire for objects: [Object] を ほしがっている.", "trapCategory": "context"},
                    {"text": "ほしいです", "isCorrect": False, "reason": "Incorrect. Cannot directly state third person's internal psychological desire with ほしいです.", "trapCategory": "context"},
                    {"text": "ほしがるでした", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"},
                    {"text": "ほしかったです", "isCorrect": False, "reason": "Incorrect. First-person past desire, not third-person current desire.", "trapCategory": "meaning"}
                ]
            },
            "hint": "How do you express a third person's desire for an object?"
        },
        {
            "id": "g2-l14-ex-3",
            "bookId": "genki-2",
            "chapter": "Lesson 14",
            "type": "multiple-choice",
            "context": "Expressing epistemic possibility: Mary might be at the library right now.",
            "question": "メアリーさんは今、図書館にいる（　　）。",
            "translation": "Mary might be at the library right now.",
            "options": ["かもしれません", "でしょう", "はずです", "そうです"],
            "correctIndex": 0,
            "grammarPointId": "g2-l14-kamoshirenai",
            "grammarPointTitle": "〜かもしれない / 〜かもしんない (Epistemic Possibility: Might / May)",
            "explanation": {
                "overall": "〜かもしれない expresses possibility ('might / may', ~50% or lower likelihood). Attaches to short forms.",
                "options": [
                    {"text": "かもしれません", "isCorrect": True, "reason": "Correct. Epistemic possibility: V-short + かもしれません.", "trapCategory": "meaning"},
                    {"text": "でしょう", "isCorrect": False, "reason": "Incorrect. でしょう expresses probable certainty (~70-80%), stronger than might.", "trapCategory": "meaning"},
                    {"text": "はずです", "isCorrect": False, "reason": "Incorrect. はずです expresses expectation based on grounds, not uncertain possibility.", "trapCategory": "meaning"},
                    {"text": "そうです", "isCorrect": False, "reason": "Incorrect. Hearsay or appearance.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which expression denotes epistemic possibility ('might / may')?"
        },
        {
            "id": "g2-l14-ex-4",
            "bookId": "genki-2",
            "chapter": "Lesson 14",
            "type": "multiple-choice",
            "context": "Formation of 〜かもしれない with a noun predicate: 'He might be a student'.",
            "question": "田中さんは学生（　　）かもしれません。",
            "translation": "Mr. Tanaka might be a student.",
            "options": ["（接続語なし）", "だ", "な", "である"],
            "correctIndex": 0,
            "grammarPointId": "g2-l14-kamoshirenai",
            "grammarPointTitle": "〜かもしれない / 〜かもしんない (Epistemic Possibility: Might / May)",
            "explanation": {
                "overall": "Important rule: nouns and な-adjectives attach directly to かもしれない WITHOUT だ (学生かもしれません, NOT *学生だかもしれません).",
                "options": [
                    {"text": "（接続語なし）", "isCorrect": True, "reason": "Correct. Nouns attach directly to かもしれません dropping だ.", "trapCategory": "formation"},
                    {"text": "だ", "isCorrect": False, "reason": "Incorrect. Major learner trap: do NOT keep だ before かもしれません.", "trapCategory": "formation"},
                    {"text": "な", "isCorrect": False, "reason": "Incorrect. な is not used before かもしれません.", "trapCategory": "formation"},
                    {"text": "である", "isCorrect": False, "reason": "Incorrect. Stiff literary form.", "trapCategory": "context"}
                ]
            },
            "hint": "Do nouns keep or drop だ before かもしれません?"
        },
        {
            "id": "g2-l14-ex-5",
            "bookId": "genki-2",
            "chapter": "Lesson 14",
            "type": "multiple-choice",
            "context": "Offering casual suggestion to a troubled friend: 'Why don't you talk to the teacher?'.",
            "question": "先生に相談し（　　）どうですか。",
            "translation": "Why don't you consult with the teacher?",
            "options": ["たら", "ては", "れば", "なら"],
            "correctIndex": 0,
            "grammarPointId": "g2-l14-tara-dou-desu-ka",
            "grammarPointTitle": "〜たらどうですか (Casual Advice / Suggestion: Why Don't You?)",
            "explanation": {
                "overall": "The pattern for suggesting or giving advice is: Verb ta-form + らどうですか (〜たらどうですか).",
                "options": [
                    {"text": "たら", "isCorrect": True, "reason": "Correct. Advice formula: V-ta + らどうですか.", "trapCategory": "formation"},
                    {"text": "ては", "isCorrect": False, "reason": "Incorrect. 〜てはどうですか is more formal/written, Genki II standard spoken pattern is 〜たらどうですか.", "trapCategory": "formation"},
                    {"text": "れば", "isCorrect": False, "reason": "Incorrect. 〜ればどうですか is ungrammatical.", "trapCategory": "formation"},
                    {"text": "なら", "isCorrect": False, "reason": "Incorrect. Ungrammatical.", "trapCategory": "formation"}
                ]
            },
            "hint": "What conditional form is used in the advice pattern 'Why don't you...?'"
        },
        {
            "id": "g2-l14-ex-6",
            "bookId": "genki-2",
            "chapter": "Lesson 14",
            "type": "multiple-choice",
            "context": "Giving a birthday present to a friend: I gave a book to Mary.",
            "question": "私はメアリーさんに本を（　　）。",
            "translation": "I gave a book to Mary.",
            "options": ["あげました", "くれました", "もらいました", "いただきまし"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-14-22",
            "grammarPointTitle": "あげる・くれる・もらう",
            "explanation": {
                "overall": "When the speaker gives something to an outside person, the verb is あげる (私 は Recipient に Item を あげる).",
                "options": [
                    {"text": "あげました", "isCorrect": True, "reason": "Correct. Speaker gives to another: あげました.", "trapCategory": "meaning"},
                    {"text": "くれました", "isCorrect": False, "reason": "Incorrect. くれる is used when someone gives TO the speaker, not when speaker gives.", "trapCategory": "meaning"},
                    {"text": "もらいました", "isCorrect": False, "reason": "Incorrect. もらう means 'received from'.", "trapCategory": "meaning"},
                    {"text": "いただきまし", "isCorrect": False, "reason": "Incorrect. Humble receiving verb, incorrect actor direction.", "trapCategory": "formation"}
                ]
            },
            "hint": "Which verb is used when YOU give something to another person?"
        },
        {
            "id": "g2-l14-ex-7",
            "bookId": "genki-2",
            "chapter": "Lesson 14",
            "type": "multiple-choice",
            "context": "Ken gave flowers to me on my birthday.",
            "question": "けんさんは私に花を（　　）。",
            "translation": "Ken gave flowers to me.",
            "options": ["くれました", "あげました", "もらいました", "やりました"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-14-22",
            "grammarPointTitle": "あげる・くれる・もらう",
            "explanation": {
                "overall": "When someone gives something inward to the speaker (or in-group), the verb is strictly くれる (Giver は 私に Item を くれる).",
                "options": [
                    {"text": "くれました", "isCorrect": True, "reason": "Correct. Someone gives to speaker: くれました.", "trapCategory": "meaning"},
                    {"text": "あげました", "isCorrect": False, "reason": "Incorrect. Major giving-receiving error: other person cannot 'あげる' to speaker.", "trapCategory": "meaning"},
                    {"text": "もらいました", "isCorrect": False, "reason": "Incorrect. もらう requires receiver as subject (私はけんさんにもらいました).", "trapCategory": "formation"},
                    {"text": "やりました", "isCorrect": False, "reason": "Incorrect. やる is used for animals, plants, or subordinates, inappropriate here.", "trapCategory": "context"}
                ]
            },
            "hint": "Which verb is used when someone gives something TO YOU?"
        },
        {
            "id": "g2-l14-ex-8",
            "bookId": "genki-2",
            "chapter": "Lesson 14",
            "type": "multiple-choice",
            "context": "Emphasizing a surprisingly large quantity: Mary ate as many as ten apples!",
            "question": "メアリーさんはリンゴを十個（　　）食べました。",
            "translation": "Mary ate as many as ten apples!",
            "options": ["も", "しか", "だけ", "ほど"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-14-23",
            "grammarPointTitle": "数量＋も・しか〜ない",
            "explanation": {
                "overall": "Quantity + も expresses that the number is surprisingly large ('as many as X'). Attached to affirmative verbs.",
                "options": [
                    {"text": "も", "isCorrect": True, "reason": "Correct. Quantity + も = 'as many as X' (surprise at large quantity).", "trapCategory": "meaning"},
                    {"text": "しか", "isCorrect": False, "reason": "Incorrect. しか requires a negative verb (しか食べませんでした).", "trapCategory": "formation"},
                    {"text": "だけ", "isCorrect": False, "reason": "Incorrect. だけ simply means 'only' without emphatic surprise.", "trapCategory": "meaning"},
                    {"text": "ほど", "isCorrect": False, "reason": "Incorrect. ほど means 'approximately'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle attaches to a number with an affirmative verb to mean 'as many as'?"
        },
        {
            "id": "g2-l14-ex-9",
            "bookId": "genki-2",
            "chapter": "Lesson 14",
            "type": "multiple-choice",
            "context": "Emphasizing scarcity with しか: having only one hundred yen.",
            "question": "財布に百円（　　）ありません。",
            "translation": "I have only 100 yen in my wallet (nothing more than 100 yen).",
            "options": ["しか", "だけ", "も", "でも"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-14-23",
            "grammarPointTitle": "数量＋も・しか〜ない",
            "explanation": {
                "overall": "しか strictly requires a negative verb (〜しか…ない) and conveys that the quantity is insufficient or only that little.",
                "options": [
                    {"text": "しか", "isCorrect": True, "reason": "Correct. しか + negative verb = 'only / no more than'.", "trapCategory": "formation"},
                    {"text": "だけ", "isCorrect": False, "reason": "Incorrect. だけ pairs with affirmative verbs (百円だけあります).", "trapCategory": "formation"},
                    {"text": "も", "isCorrect": False, "reason": "Incorrect. も emphasizes largeness, clashing with 100 yen scarcity.", "trapCategory": "meaning"},
                    {"text": "でも", "isCorrect": False, "reason": "Incorrect. でも means 'even / or something'.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle pairs strictly with a negative verb to mean 'only / no more than'?"
        },
        {
            "id": "g2-l14-ex-10",
            "bookId": "genki-2",
            "chapter": "Lesson 14",
            "type": "multiple-choice",
            "context": "Receiving a gift: I received a souvenir from Professor Tanaka.",
            "question": "私は田中先生（　　）お土産をいただきました。",
            "translation": "I humbly received a souvenir from Professor Tanaka.",
            "options": ["に", "を", "で", "へ"],
            "correctIndex": 0,
            "grammarPointId": "added-g2-14-22",
            "grammarPointTitle": "あげる・くれる・もらう",
            "explanation": {
                "overall": "With もらう / いただく, the source from whom you received is marked with particle に (or から).",
                "options": [
                    {"text": "に", "isCorrect": True, "reason": "Correct. Giver in receiving structure takes に (or から).", "trapCategory": "formation"},
                    {"text": "を", "isCorrect": False, "reason": "Incorrect. を marks the gift received (お土産を), not the giver.", "trapCategory": "formation"},
                    {"text": "で", "isCorrect": False, "reason": "Incorrect. で does not mark the giver.", "trapCategory": "meaning"},
                    {"text": "へ", "isCorrect": False, "reason": "Incorrect. へ marks direction of movement.", "trapCategory": "meaning"}
                ]
            },
            "hint": "Which particle marks the person from whom you receive a gift in もらう/いただく sentences?"
        }
    ])

    return exercises

if __name__ == "__main__":
    ex_list = get_genki2_exercises()
    print(f"Generated {len(ex_list)} exercises across Genki II Lessons 13 and 14.")
    
    with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
        existing = json.load(f)
    
    # Filter out any existing L13-L14
    kept = [x for x in existing if not (x.get('bookId') == 'genki-2' and x.get('chapter') in ['Lesson 13', 'Lesson 14'])]
    combined = kept + ex_list
    
    with open('c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    
    print(f"Saved {len(combined)} exercises to c:/JLPT/jlpt-exam-prep/src/data/chapterExercises.json")
