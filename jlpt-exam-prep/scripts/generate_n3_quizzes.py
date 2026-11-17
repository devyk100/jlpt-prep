# -*- coding: utf-8 -*-
import json

N3_QUIZZES = {
  "added-n3-4-46": {
    "id": "q-added-n3-4-46-1",
    "question": "あの人は学者（　　）、むしろ優れた実業家と言ったほうがふさわしい。",
    "translation": "Rather than calling that person a scholar, it's more appropriate to say he is an accomplished businessman.",
    "options": ["というより", "一方で", "反面", "わりに"],
    "correctIndex": 0,
    "grammarFocus": "〜というより (Rather than X, more like Y)",
    "ruleHint": "X というより Y expresses that Y is a more accurate description than X.",
    "explanations": [
      {"text": "というより", "isCorrect": True, "reason": "Correct! 〜というより reframes the description: rather than a scholar, an entrepreneur."},
      {"text": "一方で", "isCorrect": False, "reason": "Incorrect. 一方で contrasts two existing co-present realities, rather than choosing a more fitting label."},
      {"text": "反面", "isCorrect": False, "reason": "Incorrect. 反面 contrasts two sides of the same entity."},
      {"text": "わりに", "isCorrect": False, "reason": "Incorrect. わりに expresses disproportionate expectation ('considering that')."}
    ]
  },
  "added-n3-5-47": {
    "id": "q-added-n3-5-47-1",
    "question": "先日の記録的な台風（　　）、多くの鉄道路線が終日運休となった。",
    "translation": "Due to the record-breaking typhoon the other day, many train lines were suspended all day.",
    "options": ["によって", "にとって", "について", "に対して"],
    "correctIndex": 0,
    "grammarFocus": "〜によって (Formal Cause / Reason)",
    "ruleHint": "Noun + によって specifies an external formal cause or natural agent.",
    "explanations": [
      {"text": "によって", "isCorrect": True, "reason": "Correct! 台風によって marks the natural cause leading to train suspension."},
      {"text": "にとって", "isCorrect": False, "reason": "Incorrect. にとって marks evaluative standpoint ('from the perspective of')."},
      {"text": "について", "isCorrect": False, "reason": "Incorrect. について introduces a topic of discussion/study ('about')."},
      {"text": "に対して", "isCorrect": False, "reason": "Incorrect. に対して marks a target of action or sharp contrast."}
    ]
  },
  "added-n3-6-48": {
    "id": "q-added-n3-6-48-1",
    "question": "東京へ行く（　　）、新幹線を利用するのが一番便利ですよ。",
    "translation": "If you are going to Tokyo, taking the Shinkansen is the most convenient.",
    "options": ["なら", "たら", "ば", "と"],
    "correctIndex": 0,
    "grammarFocus": "Contextual Advice Conditional 〜なら",
    "ruleHint": "Verb 辞書形 + なら takes up the listener's topic/plan to give advice; action in main clause happens BEFORE destination.",
    "explanations": [
      {"text": "なら", "isCorrect": True, "reason": "Correct! 〜なら acts on the premise of going to Tokyo to offer advice prior to departure."},
      {"text": "たら", "isCorrect": False, "reason": "Incorrect. 行ったら would imply advice to be performed after already arriving in Tokyo."},
      {"text": "ば", "isCorrect": False, "reason": "Incorrect. 行けば is a provisional conditional that sounds unnatural for travel route advice."},
      {"text": "と", "isCorrect": False, "reason": "Incorrect. と cannot pair with subjective advice (一番便利ですよ)."}
    ]
  },
  "added-n3-7-49": {
    "id": "q-added-n3-7-49-1",
    "question": "天気予報による（　　）、明日は午後から激しい雷雨になるということだ。",
    "translation": "According to the weather forecast, there will be severe thunderstorms starting tomorrow afternoon.",
    "options": ["と", "なら", "ば", "たら"],
    "correctIndex": 0,
    "grammarFocus": "Hearsay Source: 〜によると…ということだ",
    "ruleHint": "〜によると is the canonical formula paired with 〜ということだ / 〜とのことだ.",
    "explanations": [
      {"text": "と", "isCorrect": True, "reason": "Correct! 〜によると sets up the formal information source culminating in ということだ."},
      {"text": "なら", "isCorrect": False, "reason": "Incorrect. によるなら is ungrammatical."},
      {"text": "ば", "isCorrect": False, "reason": "Incorrect. によれば is possible, but によるば is ungrammatical."},
      {"text": "たら", "isCorrect": False, "reason": "Incorrect. によったら is colloquial/nonstandard."}
    ]
  },
  "added-n3-7-50": {
    "id": "q-added-n3-7-50-1",
    "question": "納豆は古くから健康に良い（　　）いる。",
    "translation": "Natto has been said to be good for one's health since ancient times.",
    "options": ["と言われて", "と言って", "と思って", "と聞いて"],
    "correctIndex": 0,
    "grammarFocus": "General Belief / Consensual Hearsay (〜と言われている)",
    "ruleHint": "〜と言われている expresses widespread, long-standing public consensus ('it is said that...').",
    "explanations": [
      {"text": "と言われて", "isCorrect": True, "reason": "Correct! 〜と言われている reports established general social knowledge."},
      {"text": "と言って", "isCorrect": False, "reason": "Incorrect. と言って indicates a specific person speaking."},
      {"text": "と思って", "isCorrect": False, "reason": "Incorrect. と思っている indicates ongoing personal thought."},
      {"text": "と聞いて", "isCorrect": False, "reason": "Incorrect. と聞いている reports information the speaker personally heard."}
    ]
  },
  "added-n3-7-51": {
    "id": "q-added-n3-7-51-1",
    "question": "来週、新しい留学生が来る（　　）聞いたよ。",
    "translation": "I heard that a new exchange student is coming next week.",
    "options": ["って", "とは", "では", "すら"],
    "correctIndex": 0,
    "grammarFocus": "Casual Quotative / Hearsay 〜って",
    "ruleHint": "Casual conversation replaces quotative と with って.",
    "explanations": [
      {"text": "って", "isCorrect": True, "reason": "Correct! って is the casual quotative particle replacing と: 来るって聞いたよ."},
      {"text": "とは", "isCorrect": False, "reason": "Incorrect. とは indicates contrastive definition, not casual quotation."},
      {"text": "では", "isCorrect": False, "reason": "Incorrect. では does not function as a quotative linker."},
      {"text": "すら", "isCorrect": False, "reason": "Incorrect. すら means 'even' (emphatic particle)."}
    ]
  },
  "added-n3-8-52": {
    "id": "q-added-n3-8-52-1",
    "question": "ピアノを弾くこと（　　）弾けますが、人前で演奏できるほど上手ではありません。",
    "translation": "I can play the piano, to be sure, but not well enough to perform in front of people.",
    "options": ["は", "も", "が", "を"],
    "correctIndex": 0,
    "grammarFocus": "Concession Formula: 〜ことは〜が",
    "ruleHint": "Verb-辞書形 + ことは + Verb-ます形 + が concedes a fact while qualifying it in the following clause.",
    "explanations": [
      {"text": "は", "isCorrect": True, "reason": "Correct! 〜ことは〜が is the fixed concession formula ('it is true that X, but...')."},
      {"text": "も", "isCorrect": False, "reason": "Incorrect. ことも does not form this contrastive concession pattern."},
      {"text": "が", "isCorrect": False, "reason": "Incorrect. ことが is subject marker, clashing with the paired structure."},
      {"text": "を", "isCorrect": False, "reason": "Incorrect. ことを is object marker."}
    ]
  },
  "added-n3-9-53": {
    "id": "q-added-n3-9-53-1",
    "question": "この仕事はとても重要ですから、君にぜひ引き受けて（　　）。",
    "translation": "Because this job is very important, I really want you to take it on.",
    "options": ["もらいたい", "あげたい", "やりたい", "いただきたいです"],
    "correctIndex": 0,
    "grammarFocus": "Desire for Another's Action: 〜てもらいたい / 〜てほしい",
    "ruleHint": "Verb て-form + もらいたい / ほしい expresses the speaker's personal desire for the other person to do something.",
    "explanations": [
      {"text": "もらいたい", "isCorrect": True, "reason": "Correct! 君に...引き受けてもらいたい expresses the speaker's earnest wish for the listener's action."},
      {"text": "あげたい", "isCorrect": False, "reason": "Incorrect. てあげたい means the speaker wants to do a favor for the listener."},
      {"text": "やりたい", "isCorrect": False, "reason": "Incorrect. てやりたい is downward favor."},
      {"text": "いただきたいです", "isCorrect": False, "reason": "Incorrect. いただきたい is possible, but 君に matches the standard register of もらいたい."}
    ]
  },
  "added-n3-9-54": {
    "id": "q-added-n3-9-54-1",
    "question": "本日の研究発表会で、私の論文について説明（　　）いただきたいと存じます。",
    "translation": "At today's symposium, I would like to be permitted to explain my research paper.",
    "options": ["させて", "されて", "して", "されさせて"],
    "correctIndex": 0,
    "grammarFocus": "Humble Permission Request (〜させていただきたい)",
    "ruleHint": "Causative stem (させて) + いただく politely asks for permission to carry out one's own action.",
    "explanations": [
      {"text": "させて", "isCorrect": True, "reason": "Correct! 説明させていただきたい politely requests permission to present one's own work."},
      {"text": "されて", "isCorrect": False, "reason": "Incorrect. Passive (されて) would mean asking the listener to be explained."},
      {"text": "して", "isCorrect": False, "reason": "Incorrect. していただきたい asks the listener to do the explanation."},
      {"text": "されさせて", "isCorrect": False, "reason": "Incorrect. Ungrammatical double-passive construction."}
    ]
  },
  "added-n3-9-55": {
    "id": "q-added-n3-9-55-1",
    "question": "明日の遠足は、どうか雨が降らなければ（　　）のですが。",
    "translation": "I really hope that it doesn't rain for tomorrow's excursion.",
    "options": ["いい", "ましだ", "だめだ", "いけない"],
    "correctIndex": 0,
    "grammarFocus": "Hoping for a favorable outcome (〜ばいい / 〜たらいい)",
    "ruleHint": "Conditional (降らなければ) + いいのに / いいのですが expresses a heartfelt hope for an outcome.",
    "explanations": [
      {"text": "いい", "isCorrect": True, "reason": "Correct! 〜ばいいのですが is the canonical formula for wishing a desired condition will hold."},
      {"text": "ましだ", "isCorrect": False, "reason": "Incorrect. ましだ means 'better than nothing / relatively preferable'."},
      {"text": "だめだ", "isCorrect": False, "reason": "Incorrect. だめだ means 'it is no good', reversing the desired wish."},
      {"text": "いけない", "isCorrect": False, "reason": "Incorrect. 〜なければいけない expresses obligation ('must do')."}
    ]
  },
  "added-n3-10-56": {
    "id": "q-added-n3-10-56-1",
    "question": "試験中は、机の上に筆記用具以外置いては（　　）。",
    "translation": "During the exam, you must not place anything on your desk other than writing utensils.",
    "options": ["ならない", "いけないことだ", "だめなはずだ", "しかない"],
    "correctIndex": 0,
    "grammarFocus": "Formal Written Prohibition (〜てはならない)",
    "ruleHint": "〜てはならない is the formal written equivalent of 〜てはいけません, used in official regulations.",
    "explanations": [
      {"text": "ならない", "isCorrect": True, "reason": "Correct! 〜てはならない is the standard formal prohibition used on exam instructions and regulations."},
      {"text": "いけないことだ", "isCorrect": False, "reason": "Incorrect. Clunky phrasing that doesn't form the rule expression."},
      {"text": "だめなはずだ", "isCorrect": False, "reason": "Incorrect. Expresses speculative expectation rather than an authoritative rule."},
      {"text": "しかない", "isCorrect": False, "reason": "Incorrect. 〜しかない means 'have no choice but to'."}
    ]
  },
  "added-n3-10-57": {
    "id": "q-added-n3-10-57-1",
    "question": "一人で悩んでいないで、一度先生に相談してみ（　　）どうですか。",
    "translation": "Instead of brooding alone, why don't you try consulting your teacher?",
    "options": ["たら", "れば", "ると", "なら"],
    "correctIndex": 0,
    "grammarFocus": "Suggestion / Gentle Advice: 〜たらどうか / 〜たらどうですか",
    "ruleHint": "Verb た-form + らどうですか offers gentle practical advice or suggestion.",
    "explanations": [
      {"text": "たら", "isCorrect": True, "reason": "Correct! 〜てみたらどうですか is the canonical formula for proposing an action."},
      {"text": "れば", "isCorrect": False, "reason": "Incorrect. みればどうですか is ungrammatical."},
      {"text": "ると", "isCorrect": False, "reason": "Incorrect. みるとどうですか is ungrammatical."},
      {"text": "なら", "isCorrect": False, "reason": "Incorrect. みるならどうですか is ungrammatical."}
    ]
  },
  "added-n3-12-58": {
    "id": "q-added-n3-12-58-1",
    "question": "私は来週月曜日に、先生の研究室へ（　　）。",
    "translation": "Next Monday, I will humbly visit your office, Professor.",
    "options": ["伺います（うかがいます）", "いらっしゃいます", "ご覧になります", "おっしゃいます"],
    "correctIndex": 0,
    "grammarFocus": "Humble Visiting Verb 伺う (Kenjougo I)",
    "ruleHint": "Visiting a superior uses humble 伺う (never honorific いらっしゃる).",
    "explanations": [
      {"text": "伺います（うかがいます）", "isCorrect": True, "reason": "Correct! 伺う is the humble verb for the speaker visiting someone of higher status."},
      {"text": "いらっしゃいます", "isCorrect": False, "reason": "Incorrect. いらっしゃる is honorific for the teacher's actions, never the speaker's."},
      {"text": "ご覧になります", "isCorrect": False, "reason": "Incorrect. ご覧になる is honorific for 'to see/look'."},
      {"text": "おっしゃいます", "isCorrect": False, "reason": "Incorrect. おっしゃる is honorific for 'to say'."}
    ]
  },
  "added-n3-a-59": {
    "id": "q-added-n3-a-59-1",
    "question": "彼は忙しすぎて、昼ご飯を食べる時間（　　）ないそうだ。",
    "translation": "He is so busy that he reportedly doesn't even have time to eat lunch.",
    "options": ["さえ", "ばかり", "ほど", "だけ"],
    "correctIndex": 0,
    "grammarFocus": "Emphatic Particle 〜さえ (Even X)",
    "ruleHint": "〜さえ marks an extreme baseline example to imply everything else is obvious.",
    "explanations": [
      {"text": "さえ", "isCorrect": True, "reason": "Correct! 時間さえない emphasizes that even the most fundamental necessity is lacking."},
      {"text": "ばかり", "isCorrect": False, "reason": "Incorrect. ばかりない is ungrammatical."},
      {"text": "ほど", "isCorrect": False, "reason": "Incorrect. ほどない would require a comparative predicate."},
      {"text": "だけ", "isCorrect": False, "reason": "Incorrect. だけない means 'only doesn't have', lacking the emphatic force of さえ."}
    ]
  },
  "added-n3-b-60": {
    "id": "q-added-n3-b-60-1",
    "question": "日本の伝統文化（　　）もっと詳しく調べるために、図書館へ行った。",
    "translation": "In order to investigate Japanese traditional culture in greater detail, I went to the library.",
    "options": ["について", "に対して", "にとって", "として"],
    "correctIndex": 0,
    "grammarFocus": "〜について (Topic / Theme of Inquiry)",
    "ruleHint": "Noun + について introduces the central subject of research, thinking, or speech (調べる, 書く, 話す).",
    "explanations": [
      {"text": "について", "isCorrect": True, "reason": "Correct! 調べる takes 〜について to mark the topic of investigation."},
      {"text": "に対して", "isCorrect": False, "reason": "Incorrect. に対して marks a target of attitude or contrast between two parties."},
      {"text": "にとって", "isCorrect": False, "reason": "Incorrect. にとって marks subjective evaluator ('from the perspective of')."},
      {"text": "として", "isCorrect": False, "reason": "Incorrect. として marks role or qualification ('in the capacity of')."}
    ]
  },
  "added-n3-c-61": {
    "id": "q-added-n3-c-61-1",
    "question": "隣の部屋で誰かがピアノを弾いている（　　）が聞こえます。",
    "translation": "I can hear someone playing the piano in the next room.",
    "options": ["の", "こと", "もの", "わけ"],
    "correctIndex": 0,
    "grammarFocus": "Sensory Nominalizer の (Direct Perception)",
    "ruleHint": "Verbs of direct sensory perception (聞こえる, 見る, 感じる) strictly require nominalizer の.",
    "explanations": [
      {"text": "の", "isCorrect": True, "reason": "Correct! Sensory perception (聞こえる) strictly requires nominalizer の for an unfolding concrete event."},
      {"text": "こと", "isCorrect": False, "reason": "Incorrect. こと nominalizes abstract concepts, but direct physical perception requires の."},
      {"text": "もの", "isCorrect": False, "reason": "Incorrect. もの refers to tangible objects or general truths."},
      {"text": "わけ", "isCorrect": False, "reason": "Incorrect. わけ means 'reason / logical explanation'."}
    ]
  },
  "added-n3-d-62": {
    "id": "q-added-n3-d-62-1",
    "question": "風邪をひかない（　　）、毎日手洗いとうがいを徹底しています。",
    "translation": "In order not to catch a cold, I thoroughly wash my hands and gargle every day.",
    "options": ["ように", "ために", "ようにして", "とおりに"],
    "correctIndex": 0,
    "grammarFocus": "Negative Purpose: V-ない + ように (So as not to)",
    "ruleHint": "Negative purpose ('so that X does not happen') takes Verb ない-form + ように (never ために).",
    "explanations": [
      {"text": "ように", "isCorrect": True, "reason": "Correct! Non-volitional/negative purpose strictly takes ように: ひかないように."},
      {"text": "ために", "isCorrect": False, "reason": "Incorrect. ために requires volitional control and cannot attach to negative potential/states."},
      {"text": "ようにして", "isCorrect": False, "reason": "Incorrect. ようにして means 'making an effort to', clashing with the subordinate purpose clause."},
      {"text": "とおりに", "isCorrect": False, "reason": "Incorrect. とおりに means 'in accordance with / just as'."}
    ]
  },
  "added-n3-e-63": {
    "id": "q-added-n3-e-63-1",
    "question": "大事な会議の直前だから、今ここで仕事を投げ出すわけには（　　）。",
    "translation": "Because it's right before an important meeting, there is no way I can abandon my work now.",
    "options": ["いかない", "ない", "ある", "しない"],
    "correctIndex": 0,
    "grammarFocus": "Moral / Social Prohibition (〜わけにはいかない)",
    "ruleHint": "Verb 辞書形 + わけにはいかない expresses that one cannot do X due to social/moral responsibility.",
    "explanations": [
      {"text": "いかない", "isCorrect": True, "reason": "Correct! わけにはいかない denotes strong social/moral impossibility despite physical ability."},
      {"text": "ない", "isCorrect": False, "reason": "Incorrect. わけにはない is ungrammatical."},
      {"text": "ある", "isCorrect": False, "reason": "Incorrect. わけにはある is ungrammatical."},
      {"text": "しない", "isCorrect": False, "reason": "Incorrect. わけにはしない is ungrammatical."}
    ]
  },
  "added-n3-f-64": {
    "id": "q-added-n3-f-64-1",
    "question": "弟は部屋でゲームを（　　）ばかりいて、少しも勉強しようとしない。",
    "translation": "My younger brother does nothing but play games in his room, not trying to study at all.",
    "options": ["して", "する", "した", "し"],
    "correctIndex": 0,
    "grammarFocus": "Repetitive Habitual Indulgence: 〜てばかりいる",
    "ruleHint": "Verb て-form + ばかりいる expresses repeatedly doing only one action with critical/disapproving nuance.",
    "explanations": [
      {"text": "して", "isCorrect": True, "reason": "Correct! て-form attaches to ばかりいる: ゲームをしてばかりいる."},
      {"text": "する", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach to ばかりいる."},
      {"text": "した", "isCorrect": False, "reason": "Incorrect. したばかり means 'just recently completed', not habitual action."},
      {"text": "し", "isCorrect": False, "reason": "Incorrect. Masu-stem cannot attach to ばかりいる."}
    ]
  },
  "added-n3-g-65": {
    "id": "q-added-n3-g-65-1",
    "question": "来月から会社の規則で、週に二日は在宅勤務をする（　　）になりました。",
    "translation": "Starting next month, due to company regulations, it has been decided that we will work from home two days a week.",
    "options": ["こと", "もの", "わけ", "ところ"],
    "correctIndex": 0,
    "grammarFocus": "External Decision / Organizational Policy (〜ことになる)",
    "ruleHint": "Verb 辞書形 + ことになる expresses decisions made by institutional rules, consensus, or external authority.",
    "explanations": [
      {"text": "こと", "isCorrect": True, "reason": "Correct! 〜ことになる denotes an institutional decision beyond single individual volition."},
      {"text": "もの", "isCorrect": False, "reason": "Incorrect. 〜ものになる is ungrammatical for rules."},
      {"text": "わけ", "isCorrect": False, "reason": "Incorrect. 〜わけになる is ungrammatical."},
      {"text": "ところ", "isCorrect": False, "reason": "Incorrect. 〜ところになる is ungrammatical."}
    ]
  },
  "added-n3-h-66": {
    "id": "q-added-n3-h-66-1",
    "question": "外国語は、勉強す（　　）勉強するほど上達する。",
    "translation": "The more you study a foreign language, the more proficient you become.",
    "options": ["れば", "ると", "るなら", "ったら"],
    "correctIndex": 0,
    "grammarFocus": "Proportional Increase: 〜ば〜ほど",
    "ruleHint": "Verb-ば + Verb-辞書形 + ほど expresses proportional advancement ('the more X, the more Y').",
    "explanations": [
      {"text": "れば", "isCorrect": True, "reason": "Correct! すれば勉強するほど is the canonical proportional formula."},
      {"text": "ると", "isCorrect": False, "reason": "Incorrect. すると...ほど does not form the proportional correlative."},
      {"text": "るなら", "isCorrect": False, "reason": "Incorrect. するなら...ほど is ungrammatical."},
      {"text": "ったら", "isCorrect": False, "reason": "Incorrect. したら...ほど is colloquial/nonstandard."}
    ]
  },
  "added-n3-i-67": {
    "id": "q-added-n3-i-67-1",
    "question": "あんなに真面目な彼が、嘘をつくなど（　　）信じられない。",
    "translation": "I absolutely cannot believe that someone as earnest as him would tell a lie.",
    "options": ["まったく", "必ずしも", "たぶん", "どうやら"],
    "correctIndex": 0,
    "grammarFocus": "Collocation: まったく + Negative (Not at all / Absolutely cannot)",
    "ruleHint": "まったく pairs with negative predicates to express total negation or absolute disbelief.",
    "explanations": [
      {"text": "まったく", "isCorrect": True, "reason": "Correct! まったく信じられない expresses total negation ('completely impossible to believe')."},
      {"text": "必ずしも", "isCorrect": False, "reason": "Incorrect. 必ずしも pairs with partial negation 〜とは限らない ('not necessarily')."},
      {"text": "たぶん", "isCorrect": False, "reason": "Incorrect. たぶん pairs with conjecture (だろう/でしょう)."},
      {"text": "どうやら", "isCorrect": False, "reason": "Incorrect. どうやら pairs with observational inference (ようだ/らしい)."}
    ]
  },
  "added-n3-j-68": {
    "id": "q-added-n3-j-68-1",
    "question": "最近仕事が忙しくて、少し風邪（　　）なので早めに寝ます。",
    "translation": "Work has been busy lately, and I have a slight touch of a cold, so I'll go to sleep early.",
    "options": ["気味（ぎみ）", "がち", "っぽい", "だらけ"],
    "correctIndex": 0,
    "grammarFocus": "Slight Internal Symptom: Noun + 気味 (ぎみ)",
    "ruleHint": "〜気味 expresses a mild emerging physical or psychological symptom (風邪気味, 疲れ気味).",
    "explanations": [
      {"text": "気味（ぎみ）", "isCorrect": True, "reason": "Correct! 風邪気味 indicates a slight emerging touch of a cold."},
      {"text": "がち", "isCorrect": False, "reason": "Incorrect. がち indicates a frequent unfortunate habit over time (留守がち)."},
      {"text": "っぽい", "isCorrect": False, "reason": "Incorrect. っぽい indicates external childish or cheapened appearance (子供っぽい)."},
      {"text": "だらけ", "isCorrect": False, "reason": "Incorrect. だらけ indicates complete surface mess (泥だらけ, 間違いだらけ)."}
    ]
  },
  "added-n3-j-115": {
    "id": "q-added-n3-j-115-1",
    "question": "机の上に、読み（　　）の本がそのまま置かれている。",
    "translation": "On the desk, an unfinished book that was in the middle of being read is left as is.",
    "options": ["かけ", "通し", "づらい", "きり"],
    "correctIndex": 0,
    "grammarFocus": "Incomplete Action in Progress: Verb stem + かけ",
    "ruleHint": "Verb ます-stem + かけ denotes an action started but left suspended before completion.",
    "explanations": [
      {"text": "かけ", "isCorrect": True, "reason": "Correct! 読みかけの本 means a book someone started reading but has not finished."},
      {"text": "通し", "isCorrect": False, "reason": "Incorrect. 読み通す means reading all the way through to completion."},
      {"text": "づらい", "isCorrect": False, "reason": "Incorrect. 読みづらい means difficult to read."},
      {"text": "きり", "isCorrect": False, "reason": "Incorrect. 読みきり is used for standalone complete short stories."}
    ]
  },
  "added-n3-p2-1-124": {
    "id": "q-added-n3-p2-1-124-1",
    "question": "部長は明日十時からの会議に出席できない（　　）言っていました。",
    "translation": "The department manager was saying that he cannot attend tomorrow's meeting from 10:00.",
    "options": ["と", "を", "に", "で"],
    "correctIndex": 0,
    "grammarFocus": "Sentence Quotation Particle と",
    "ruleHint": "Quoted speech clauses close with particle と preceding 言う, 伝える, 書いてある.",
    "explanations": [
      {"text": "と", "isCorrect": True, "reason": "Correct! Quotative particle と links the quoted clause to 言っていました."},
      {"text": "を", "isCorrect": False, "reason": "Incorrect. を cannot link a clausal quotation."},
      {"text": "に", "isCorrect": False, "reason": "Incorrect. に cannot quote a clausal statement."},
      {"text": "で", "isCorrect": False, "reason": "Incorrect. で cannot quote speech."}
    ]
  },
  "added-n3-p2-2-125": {
    "id": "q-added-n3-p2-2-125-1",
    "question": "私が日本で初めて（　　）料理は、京都の伝統的な懐石料理でした。",
    "translation": "The food that I ate for the first time in Japan was traditional Kyoto kaiseki cuisine.",
    "options": ["食べた", "食べます", "食べて", "食べる"],
    "correctIndex": 0,
    "grammarFocus": "Noun Modification with Completed Past Event (た形 + Noun)",
    "ruleHint": "A completed past event modifying a noun takes plain past た-form in the relative clause.",
    "explanations": [
      {"text": "食べた", "isCorrect": True, "reason": "Correct! Completed past experience modifying 料理: 初めて食べた料理."},
      {"text": "食べます", "isCorrect": False, "reason": "Incorrect. Polite forms cannot modify nouns within relative clauses."},
      {"text": "食べて", "isCorrect": False, "reason": "Incorrect. Te-form cannot directly modify a noun."},
      {"text": "食べる", "isCorrect": False, "reason": "Incorrect. Non-past 食べる clashes with the past event '懐石料理でした'."}
    ]
  },
  "added-n3-p2-3-126": {
    "id": "q-added-n3-p2-3-126-1",
    "question": "地震や津波（　　）自然災害に対する日頃の備えが欠かせない。",
    "translation": "Daily preparation against natural disasters such as earthquakes and tsunamis is indispensable.",
    "options": ["といった", "といって", "というと", "といえば"],
    "correctIndex": 0,
    "grammarFocus": "Exemplifying Noun Modifiers: 〜といった + Noun",
    "ruleHint": "A や B + といった + Category Noun lists representative examples to modify a summarizing noun.",
    "explanations": [
      {"text": "といった", "isCorrect": True, "reason": "Correct! 〜といった links representative examples (地震や津波) to the summary category 自然災害."},
      {"text": "といって", "isCorrect": False, "reason": "Incorrect. といって links predicates, not attributive noun modification."},
      {"text": "というと", "isCorrect": False, "reason": "Incorrect. というと prompts a topic association ('speaking of...')."},
      {"text": "といえば", "isCorrect": False, "reason": "Incorrect. といえば also prompts topic association."}
    ]
  },
  "added-n3-p2-4-127": {
    "id": "q-added-n3-p2-4-127-1",
    "question": "努力すれば必ず成功するとは（　　）。運や環境も影響するからだ。",
    "translation": "It is not necessarily true that one will always succeed if one makes an effort. Luck and environment also play a role.",
    "options": ["限らない", "違いない", "ほかならない", "すぎない"],
    "correctIndex": 0,
    "grammarFocus": "Partial Negation: 〜とは限らない (Not necessarily)",
    "ruleHint": "〜とは限らない denies that a condition is universally absolute ('not always so').",
    "explanations": [
      {"text": "限らない", "isCorrect": True, "reason": "Correct! 〜とは限らない expresses partial negation ('does not guarantee 100% success')."},
      {"text": "違いない", "isCorrect": False, "reason": "Incorrect. 〜に違いない expresses strong positive conviction ('without doubt')."},
      {"text": "ほかならない", "isCorrect": False, "reason": "Incorrect. 〜にほかならない means 'is nothing other than'."},
      {"text": "すぎない", "isCorrect": False, "reason": "Incorrect. 〜にすぎない means 'is merely / no more than'."}
    ]
  },
  "added-n3-p3-1-131": {
    "id": "q-added-n3-p3-1-131-1",
    "question": "いくら一生懸命頼まれた（　　）、不正な行為に加担することはできない。",
    "translation": "No matter how earnestly I am pleaded with, I cannot participate in an illegal act.",
    "options": ["としても", "とすれば", "とすると", "となると"],
    "correctIndex": 0,
    "grammarFocus": "Discourse Correlative: いくら〜としても / ても",
    "ruleHint": "いくら correlates with conditional concessive forms (ても / としても) to mean 'no matter how much'.",
    "explanations": [
      {"text": "としても", "isCorrect": True, "reason": "Correct! いくら correlates strictly with concessive としても ('even granting that...')."},
      {"text": "とすれば", "isCorrect": False, "reason": "Incorrect. とすれば is a hypothetical conditional ('if we assume')."},
      {"text": "とすると", "isCorrect": False, "reason": "Incorrect. とすると introduces a natural deduction."},
      {"text": "となると", "isCorrect": False, "reason": "Incorrect. となると indicates a topic scenario ('if it comes to that')."}
    ]
  },
  "added-n3-p3-2-132": {
    "id": "q-added-n3-p3-2-132-1",
    "question": "父は昔から毎朝近所の公園を散歩（　　）。今でも元気だ。",
    "translation": "My father has been taking walks in the neighborhood park every morning for a long time. He is still vigorous even now.",
    "options": ["している", "した", "する", "していた"],
    "correctIndex": 0,
    "grammarFocus": "Ongoing Customary Action (〜ている)",
    "ruleHint": "A habitual action continuing from the past into the present is expressed with 〜ている.",
    "explanations": [
      {"text": "している", "isCorrect": True, "reason": "Correct! 昔から...今でも reflects a continuous ongoing habit: 散歩している."},
      {"text": "した", "isCorrect": False, "reason": "Incorrect. 散歩した would describe a completed one-time past event."},
      {"text": "する", "isCorrect": False, "reason": "Incorrect. Bare 散歩する does not convey the historical continuous habit."},
      {"text": "していた", "isCorrect": False, "reason": "Incorrect. 散歩していた implies the habit has now ceased, clashing with '今でも元気だ'."}
    ]
  },
  "added-n3-p3-3-133": {
    "id": "q-added-n3-p3-3-133-1",
    "question": "強風のせいで、庭の古い門が突然（　　）。",
    "translation": "Due to the strong wind, the old garden gate suddenly opened.",
    "options": ["開いた（あいた）", "開けた（あけた）", "開かせた（あかせた）", "開けられた（あけられた）"],
    "correctIndex": 0,
    "grammarFocus": "Intransitive Phenomenon: が + 開く (あく)",
    "ruleHint": "Inanimate subject with が moving spontaneously uses intransitive 開く; intentional human action uses を + 開ける.",
    "explanations": [
      {"text": "開いた（あいた）", "isCorrect": True, "reason": "Correct! The gate (門が) spontaneously opened on its own in the wind: 開いた (intransitive)."},
      {"text": "開けた（あけた）", "isCorrect": False, "reason": "Incorrect. 開ける is transitive and requires a human agent with particle を."},
      {"text": "開かせた（あかせた）", "isCorrect": False, "reason": "Incorrect. Causative form requires a commanding director."},
      {"text": "開けられた（あけられた）", "isCorrect": False, "reason": "Incorrect. Passive implies an external person opened it."}
    ]
  },
  "added-n3-p3-4-134": {
    "id": "q-added-n3-p3-4-134-1",
    "question": "夕方になって、空がだんだん暗く（　　）。",
    "translation": "As evening arrived, the sky gradually became dark.",
    "options": ["なってきた", "なっていった", "なりそうだ", "なるはずだ"],
    "correctIndex": 0,
    "grammarFocus": "Temporal Trajectory: 〜てくる (Developing toward Present)",
    "ruleHint": "A gradual change emerging toward the speaker's present vantage point uses 〜てくる (なってきた).",
    "explanations": [
      {"text": "なってきた", "isCorrect": True, "reason": "Correct! An unfolding change reaching the present moment is marked with 〜てきた."},
      {"text": "なっていった", "isCorrect": False, "reason": "Incorrect. 〜ていった marks changes moving away from the vantage point into the future/distance."},
      {"text": "なりそうだ", "isCorrect": False, "reason": "Incorrect. なりそうだ describes future expectation, clashing with the completed fact in progress."},
      {"text": "なるはずだ", "isCorrect": False, "reason": "Incorrect. なるはずだ is a logical expectation."}
    ]
  },
  "added-n3-p3-5-135": {
    "id": "q-added-n3-p3-5-135-1",
    "question": "先生に難しい質問を（　　）、うまく答えられなかった。",
    "translation": "I was asked a difficult question by the teacher, and couldn't answer well.",
    "options": ["聞かれて", "聞いて", "聞かせて", "聞かさせて"],
    "correctIndex": 0,
    "grammarFocus": "Direct Passive: 先生に + 聞かれる",
    "ruleHint": "Passive voice: Agent に + Verb-受身形 (先生に質問を聞かれて / されて).",
    "explanations": [
      {"text": "聞かれて", "isCorrect": True, "reason": "Correct! Passive form 聞かれて indicates receiving the inquiry from the teacher (先生に)."},
      {"text": "聞いて", "isCorrect": False, "reason": "Incorrect. Active 聞いて would mean the speaker asked the teacher."},
      {"text": "聞かせて", "isCorrect": False, "reason": "Incorrect. 聞かせて is causative (let someone hear)."},
      {"text": "聞かさせて", "isCorrect": False, "reason": "Incorrect. Ungrammatical form."}
    ]
  },
  "added-n3-p3-6-136": {
    "id": "q-added-n3-p3-6-136-1",
    "question": "重い荷物を持って階段を上っていたら、後ろから来た親切な人が（　　）。",
    "translation": "When I was climbing the stairs carrying heavy luggage, a kind person who came from behind carried it for me.",
    "options": ["持ってくれた", "持ってあげた", "持ってもらった", "持ってやった"],
    "correctIndex": 0,
    "grammarFocus": "Benefactive Viewpoint: Person が + 〜てくれる",
    "ruleHint": "When the other person is the grammatical subject (親切な人が), their favor to me takes 〜てくれる.",
    "explanations": [
      {"text": "持ってくれた", "isCorrect": True, "reason": "Correct! 親切な人が (subject) + 持ってくれた marks their favor directed toward me."},
      {"text": "持ってあげた", "isCorrect": False, "reason": "Incorrect. 持ってあげた means the speaker did a favor for them."},
      {"text": "持ってもらった", "isCorrect": False, "reason": "Incorrect. 持ってもらった requires the speaker as subject (私は親切な人に持ってもらった)."},
      {"text": "持ってやった", "isCorrect": False, "reason": "Incorrect. やる is downward/condescending."}
    ]
  },
  "added-n3-p3-7-137": {
    "id": "q-added-n3-p3-7-137-1",
    "question": "昨日、山田さんから電話があった。（　　）時、彼はとても元気そうだった。",
    "translation": "Yesterday, there was a phone call from Yamada-san. At that time, he sounded very cheerful.",
    "options": ["その", "あの", "この", "どの"],
    "correctIndex": 0,
    "grammarFocus": "Discourse Anaphora: その (Referring to Mentioned Entity)",
    "ruleHint": "In discourse, an entity or occasion just introduced in the immediate preceding sentence is referred to with その.",
    "explanations": [
      {"text": "その", "isCorrect": True, "reason": "Correct! その時 refers back anaphorically to the phone call just mentioned."},
      {"text": "あの", "isCorrect": False, "reason": "Incorrect. あの implies shared mutual psychological distance/nostalgia."},
      {"text": "この", "isCorrect": False, "reason": "Incorrect. この implies current ongoing situation."},
      {"text": "どの", "isCorrect": False, "reason": "Incorrect. どの is an interrogative ('which')."}
    ]
  },
  "added-n3-p3-8-138": {
    "id": "q-added-n3-p3-8-138-1",
    "question": "昔々、ある所に心優しいおじいさん（　　）住んでいました。",
    "translation": "Once upon a time, in a certain place, there lived a kind-hearted old man.",
    "options": ["が", "は", "も", "に"],
    "correctIndex": 0,
    "grammarFocus": "Discourse Introduction: New Participant Marked with が",
    "ruleHint": "In narratives, a newly introduced subject in a story takes が; once established, it becomes topic は.",
    "explanations": [
      {"text": "が", "isCorrect": True, "reason": "Correct! Introducing a brand-new entity into narrative discourse strictly takes particle が."},
      {"text": "は", "isCorrect": False, "reason": "Incorrect. は marks known, shared topics; newly introduced characters take が."},
      {"text": "も", "isCorrect": False, "reason": "Incorrect. も implies an additional character ('also')."},
      {"text": "に", "isCorrect": False, "reason": "Incorrect. に cannot mark the grammatical subject of the narrative."}
    ]
  },
  "added-n3-p3-9-139": {
    "id": "q-added-n3-p3-9-139-1",
    "question": "この計画には多額の費用がかかる。（　　）、将来の利益を考えれば実行すべきだ。",
    "translation": "This project incurs great expenses. However, considering future profits, it should be carried out.",
    "options": ["しかし", "しかも", "したがって", "たとえば"],
    "correctIndex": 0,
    "grammarFocus": "Discourse Adversative Connector しかし",
    "ruleHint": "しかし introduces a decisive contrary counter-argument to the preceding clause.",
    "explanations": [
      {"text": "しかし", "isCorrect": True, "reason": "Correct! しかし contrasts the expense against the overriding imperative to execute."},
      {"text": "しかも", "isCorrect": False, "reason": "Incorrect. しかも adds an additional corroborating point ('moreover')."},
      {"text": "したがって", "isCorrect": False, "reason": "Incorrect. したがって introduces a logical consequence ('therefore')."},
      {"text": "たとえば", "isCorrect": False, "reason": "Incorrect. たとえば introduces an illustrative example ('for example')."}
    ]
  },
  "added-n3-p3-10-140": {
    "id": "q-added-n3-p3-10-140-1",
    "question": "論文を書く際は、文末を「〜である」「〜だ」で（　　）一貫させなければならない。",
    "translation": "When writing an academic paper, sentence endings must be unified consistently with 'dearu' or 'da'.",
    "options": ["統一して（とういつして）", "省略して", "繰り返して", "反対にして"],
    "correctIndex": 0,
    "grammarFocus": "Style Consistency (文体の統一: である vs です/ます)",
    "ruleHint": "Academic and essay discourse demands strict stylistic consistency throughout the passage.",
    "explanations": [
      {"text": "統一して（とういつして）", "isCorrect": True, "reason": "Correct! 文体を統一する is the canonical rule of Japanese essay and academic writing."},
      {"text": "省略して", "isCorrect": False, "reason": "Incorrect. 省略する means omitting words."},
      {"text": "繰り返して", "isCorrect": False, "reason": "Incorrect. 繰り返す means repeating."},
      {"text": "反対にして", "isCorrect": False, "reason": "Incorrect. 反対にする means inverting."}
    ]
  }
}

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

updated = 0
for p in points:
    if p['id'] in N3_QUIZZES and len(p.get('quiz', [])) == 0:
        p['quiz'] = [N3_QUIZZES[p['id']]]
        updated += 1

with open("jlpt-exam-prep/src/data/studyPoints.json", "w", encoding="utf-8") as f:
    json.dump(points, f, ensure_ascii=False, indent=2)

print(f"Added quizzes to {updated} Shin Kanzen Master N3 cards!")
