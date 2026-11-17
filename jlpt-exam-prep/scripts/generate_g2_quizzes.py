# -*- coding: utf-8 -*-
import json

G2_QUIZZES = {
  "added-g2-13-20": {
    "id": "q-added-g2-13-20-1",
    "question": "このケーキは甘くてとても美味し（　　）ですね。",
    "translation": "This cake looks very delicious, doesn't it?",
    "options": ["そう", "らしい", "よう", "みたい"],
    "correctIndex": 0,
    "grammarFocus": "Conjecture 〜そう (Visual Impression)",
    "ruleHint": "い-adjective stem (drop い) + そう; 美味しい becomes 美味しそう.",
    "explanations": [
      {"text": "そう", "isCorrect": True, "reason": "Correct! い-adjective stem (美味し) + そう denotes visual appearance ('looks delicious')."},
      {"text": "らしい", "isCorrect": False, "reason": "Incorrect. らしい attaches to dictionary form (美味しいらしい) and denotes hearsay/typicality."},
      {"text": "よう", "isCorrect": False, "reason": "Incorrect. ように/ようだ requires plain form (美味しいようだ)."},
      {"text": "みたい", "isCorrect": False, "reason": "Incorrect. みたい attaches to plain form (美味しいみたい)."}
    ]
  },
  "added-g2-13-21": {
    "id": "q-added-g2-13-21-1",
    "question": "私は一週間に（　　）プールで泳ぎます。",
    "translation": "I swim at the pool twice a week.",
    "options": ["二回", "二回に", "二回で", "二回を"],
    "correctIndex": 0,
    "grammarFocus": "Frequency per Time Period (〜に〜回)",
    "ruleHint": "Time frame + に + Frequency counter (一週間に二回).",
    "explanations": [
      {"text": "二回", "isCorrect": True, "reason": "Correct! Frequency counter attaches directly following the timeframe: 一週間に二回."},
      {"text": "二回に", "isCorrect": False, "reason": "Incorrect. Frequency counter does not take particle に."},
      {"text": "二回で", "isCorrect": False, "reason": "Incorrect. で specifies total count or cost, not recurrent rate."},
      {"text": "二回を", "isCorrect": False, "reason": "Incorrect. を marks direct objects, not rate of occurrence."}
    ]
  },
  "added-g2-14-22": {
    "id": "q-added-g2-14-22-1",
    "question": "誕生日に母が素敵なセーターを（　　）。",
    "translation": "On my birthday, my mother gave me a lovely sweater.",
    "options": ["くれました", "あげました", "もらいました", "やりました"],
    "correctIndex": 0,
    "grammarFocus": "くれる (Inward Giving to Speaker)",
    "ruleHint": "Someone else gives to the speaker / speaker's in-group takes くれる; speaker gives takes あげる.",
    "explanations": [
      {"text": "くれました", "isCorrect": True, "reason": "Correct! 母 (giver) giving to me (implicit recipient) requires くれました."},
      {"text": "あげました", "isCorrect": False, "reason": "Incorrect. あげる denotes outward giving from the speaker to another."},
      {"text": "もらいました", "isCorrect": False, "reason": "Incorrect. もらう requires the recipient as grammatical subject (私は母にセーターをもらいました)."},
      {"text": "やりました", "isCorrect": False, "reason": "Incorrect. やる is used downward to pets or plants, not from mother to speaker."}
    ]
  },
  "added-g2-14-23": {
    "id": "q-added-g2-14-23-1",
    "question": "財布の中に千円（　　）ありませんから、買い物に行けません。",
    "translation": "Because I only have 1,000 yen in my wallet, I can't go shopping.",
    "options": ["しか", "だけ", "も", "ほど"],
    "correctIndex": 0,
    "grammarFocus": "〜しか…ない (Nothing But / Only with Negative)",
    "ruleHint": "しか is strictly paired with a negative predicate (ありません) to express a lamentable shortage.",
    "explanations": [
      {"text": "しか", "isCorrect": True, "reason": "Correct! しか + negative verb (ありません) means 'only / nothing other than'."},
      {"text": "だけ", "isCorrect": False, "reason": "Incorrect. だけ pairs with affirmative predicates (千円だけあります)."},
      {"text": "も", "isCorrect": False, "reason": "Incorrect. も with negative means 'not even / not at all', clashing with having 1,000 yen."},
      {"text": "ほど", "isCorrect": False, "reason": "Incorrect. ほど denotes general approximation, not exclusive limitation."}
    ]
  },
  "added-g2-15-24": {
    "id": "q-added-g2-15-24-1",
    "question": "旅行へ行く前に、新幹線の切符を（　　）おきました。",
    "translation": "Before going on the trip, I bought the Shinkansen tickets in advance.",
    "options": ["買って", "買う", "買い", "買おう"],
    "correctIndex": 0,
    "grammarFocus": "Preparation in Advance (〜ておく)",
    "ruleHint": "Verb て-form + おく expresses doing an action in advance as preparation.",
    "explanations": [
      {"text": "買って", "isCorrect": True, "reason": "Correct! て-form attaches to おく: 買って + おきました."},
      {"text": "買う", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach to おく."},
      {"text": "買い", "isCorrect": False, "reason": "Incorrect. Stem form cannot attach to おく."},
      {"text": "買おう", "isCorrect": False, "reason": "Incorrect. Volitional form cannot attach to おく."}
    ]
  },
  "added-g2-16-25": {
    "id": "q-added-g2-16-25-1",
    "question": "道が分からなくて困っていたら、親切な人が駅まで（　　）くれました。",
    "translation": "When I was lost and having trouble, a kind person guided me to the station.",
    "options": ["案内して", "案内されて", "案内させ", "案内した"],
    "correctIndex": 0,
    "grammarFocus": "Benefactive Favor (〜てくれる)",
    "ruleHint": "Verb て-form + くれる expresses that another party did a helpful favor for the speaker.",
    "explanations": [
      {"text": "案内して", "isCorrect": True, "reason": "Correct! Verb て-form (案内して) + くれました denotes receiving a kind favor."},
      {"text": "案内されて", "isCorrect": False, "reason": "Incorrect. Passive て-form does not pair with くれる."},
      {"text": "案内させ", "isCorrect": False, "reason": "Incorrect. Causative stem does not attach to くれる."},
      {"text": "案内した", "isCorrect": False, "reason": "Incorrect. Past form cannot precede auxiliary くれる."}
    ]
  },
  "added-g2-16-26": {
    "id": "q-added-g2-16-26-1",
    "question": "すみません、この漢字の読み方を（　　）いただけませんか。",
    "translation": "Excuse me, could you please teach me how to read this kanji?",
    "options": ["教えて", "教える", "教え", "教えられて"],
    "correctIndex": 0,
    "grammarFocus": "Polite Request (〜ていただけませんか)",
    "ruleHint": "Verb て-form + いただけませんか is a very polite request formula.",
    "explanations": [
      {"text": "教えて", "isCorrect": True, "reason": "Correct! Request formula requires verb te-form: 教えていただけませんか."},
      {"text": "教える", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach to いただけませんか."},
      {"text": "教え", "isCorrect": False, "reason": "Incorrect. Masu-stem cannot attach to いただけませんか."},
      {"text": "教えられて", "isCorrect": False, "reason": "Incorrect. Passive form changes the agent of the request."}
    ]
  },
  "added-g2-16-27": {
    "id": "q-added-g2-16-27-1",
    "question": "約束の時間に遅れ（　　）すみませんでした。",
    "translation": "I am very sorry for being late for our appointed time.",
    "options": ["て", "る", "た", "ば"],
    "correctIndex": 0,
    "grammarFocus": "Apology for an action (〜てすみません)",
    "ruleHint": "Verb て-form + すみません expresses an apology for having done an action.",
    "explanations": [
      {"text": "て", "isCorrect": True, "reason": "Correct! 遅れて + すみませんでした apologizes for the action of being late."},
      {"text": "る", "isCorrect": False, "reason": "Incorrect. Dictionary form (遅れる) cannot attach directly to すみません."},
      {"text": "た", "isCorrect": False, "reason": "Incorrect. Past form cannot attach directly to すみません."},
      {"text": "ば", "isCorrect": False, "reason": "Incorrect. Conditional ば cannot attach to an apology."}
    ]
  },
  "added-g2-17-28": {
    "id": "q-added-g2-17-28-1",
    "question": "外は風が強くて、今にも雨が降り出す（　　）ですね。",
    "translation": "The wind outside is strong, and it looks like it will start raining at any moment.",
    "options": ["みたい", "らしい", "そう", "はず"],
    "correctIndex": 0,
    "grammarFocus": "Colloquial Resemblance / Inference 〜みたいだ",
    "ruleHint": "Verb plain form + みたいだ denotes immediate observational inference ('looks like / seems like').",
    "explanations": [
      {"text": "みたい", "isCorrect": True, "reason": "Correct! 降り出す + みたい attaches directly to plain form to denote observational inference."},
      {"text": "らしい", "isCorrect": False, "reason": "Incorrect. らしい denotes hearsay or typicality from external evidence."},
      {"text": "そう", "isCorrect": False, "reason": "Incorrect. そう requires stem (降り出しそう), not dictionary form 降り出す."},
      {"text": "はず", "isCorrect": False, "reason": "Incorrect. はず denotes logical expectation ('is supposed to'), clashing with sensory visual inference."}
    ]
  },
  "added-g2-17-29": {
    "id": "q-added-g2-17-29-1",
    "question": "食事を（　　）前に、必ず手を洗いましょう。",
    "translation": "Let's be sure to wash our hands before eating.",
    "options": ["する", "した", "している", "して"],
    "correctIndex": 0,
    "grammarFocus": "Temporal Sequence: Verb 辞書形 + 前に",
    "ruleHint": "〜前に is ALWAYS preceded by the non-past dictionary form, even for past events.",
    "explanations": [
      {"text": "する", "isCorrect": True, "reason": "Correct! 〜前に strictly requires non-past dictionary form: 食事をする前に."},
      {"text": "した", "isCorrect": False, "reason": "Incorrect. Past form た cannot precede 前に (common learner error)."},
      {"text": "している", "isCorrect": False, "reason": "Incorrect. Continuous 〜ている cannot precede 前に."},
      {"text": "して", "isCorrect": False, "reason": "Incorrect. Te-form cannot precede 前に."}
    ]
  },
  "added-g2-18-30": {
    "id": "q-added-g2-18-30-1",
    "question": "大切な書類を電車の中に忘れ（　　）しまいました。",
    "translation": "I regrettably left the important document behind on the train.",
    "options": ["て", "た", "る", "ない"],
    "correctIndex": 0,
    "grammarFocus": "Regrettable Completion (〜てしまう)",
    "ruleHint": "Verb て-form + しまう expresses unintentional action accompanied by regret or chagrin.",
    "explanations": [
      {"text": "て", "isCorrect": True, "reason": "Correct! 忘れて + しまいました expresses regretful accidental completion."},
      {"text": "た", "isCorrect": False, "reason": "Incorrect. Ta-form cannot attach to しまう."},
      {"text": "る", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach to しまう."},
      {"text": "ない", "isCorrect": False, "reason": "Incorrect. Negative form cannot attach to しまう."}
    ]
  },
  "added-g2-18-31": {
    "id": "q-added-g2-18-31-1",
    "question": "音楽を（　　）ながら、部屋の掃除をしました。",
    "translation": "I cleaned the room while listening to music.",
    "options": ["聞き", "聞いて", "聞く", "聞いた"],
    "correctIndex": 0,
    "grammarFocus": "Simultaneous Actions (Verb stem + ながら)",
    "ruleHint": "Verb ます-stem + ながら indicates performing a secondary action while focusing on the main action.",
    "explanations": [
      {"text": "聞き", "isCorrect": True, "reason": "Correct! Verb masu-stem (聞き) + ながら denotes simultaneous action."},
      {"text": "聞いて", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach to ながら."},
      {"text": "聞く", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach to ながら."},
      {"text": "聞いた", "isCorrect": False, "reason": "Incorrect. Ta-form cannot attach to ながら."}
    ]
  },
  "added-g2-19-32": {
    "id": "q-added-g2-19-32-1",
    "question": "忙しい時に手伝って（　　）どうもありがとうございました。",
    "translation": "Thank you very much for helping me out when I was busy.",
    "options": ["くれて", "あげて", "もらって", "やって"],
    "correctIndex": 0,
    "grammarFocus": "Gratitude for an Inward Favor (〜てくれてありがとう)",
    "ruleHint": "〜てくれてありがとう expresses gratitude for an action someone performed for you.",
    "explanations": [
      {"text": "くれて", "isCorrect": True, "reason": "Correct! 〜てくれてありがとう thanks the other person for their kind favor toward the speaker."},
      {"text": "あげて", "isCorrect": False, "reason": "Incorrect. 〜てあげてありがとう would imply thanking someone for letting the speaker do a favor."},
      {"text": "もらって", "isCorrect": False, "reason": "Incorrect. もらって requires different subject construction."},
      {"text": "やって", "isCorrect": False, "reason": "Incorrect. やる is downward/condescending."}
    ]
  },
  "added-g2-19-33": {
    "id": "q-added-g2-19-33-1",
    "question": "彼は毎日一生懸命練習していますから、明日の試合に（　　）はずです。",
    "translation": "Because he practices diligently every day, he is expected to win tomorrow's match.",
    "options": ["勝つ", "勝ち", "勝って", "勝とう"],
    "correctIndex": 0,
    "grammarFocus": "Objective Expectation 〜はずだ (Plain form)",
    "ruleHint": "Verb plain form + はずだ expresses strong logical confidence based on clear evidence.",
    "explanations": [
      {"text": "勝つ", "isCorrect": True, "reason": "Correct! Dictionary form (勝つ) + はずです denotes confident expectation."},
      {"text": "勝ち", "isCorrect": False, "reason": "Incorrect. Masu-stem cannot attach to はず."},
      {"text": "勝って", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach to はず."},
      {"text": "勝とう", "isCorrect": False, "reason": "Incorrect. Volitional form cannot attach to はず."}
    ]
  },
  "added-g2-20-34": {
    "id": "q-added-g2-20-34-1",
    "question": "明日、十時に社長のお宅へ（　　）。",
    "translation": "Tomorrow at ten, I will humbly visit the company president's residence.",
    "options": ["伺います（うかがいます）", "いらっしゃいます", "参ります（まいります）", "おっしゃいます"],
    "correctIndex": 0,
    "grammarFocus": "Humble Visiting Verb 伺う (うかがう)",
    "ruleHint": "Visiting/asking someone of superior status uses humble 伺う; 参る is simply humble 'go/come'.",
    "explanations": [
      {"text": "伺います（うかがいます）", "isCorrect": True, "reason": "Correct! 伺う is the humble verb specifically for visiting someone of higher status."},
      {"text": "いらっしゃいます", "isCorrect": False, "reason": "Incorrect. いらっしゃる is honorific (尊敬語) for the other person's actions, never the speaker's."},
      {"text": "参ります（まいります）", "isCorrect": False, "reason": "Incorrect. 参る means 'go/come' neutrally; visiting someone's home takes 伺う."},
      {"text": "おっしゃいます", "isCorrect": False, "reason": "Incorrect. おっしゃる is honorific for 'to say'."}
    ]
  },
  "added-g2-20-35": {
    "id": "q-added-g2-20-35-1",
    "question": "昨晩は歯を（　　）ないで寝てしまいました。",
    "translation": "Last night I regrettably fell asleep without brushing my teeth.",
    "options": ["磨か（みがか）", "磨き（みがき）", "磨く（みがく）", "磨いた（みがいた）"],
    "correctIndex": 0,
    "grammarFocus": "Doing without doing X (Verb ない-stem + ないで)",
    "ruleHint": "Verb negative plain base + ないで indicates performing an action without doing another.",
    "explanations": [
      {"text": "磨か（みがか）", "isCorrect": True, "reason": "Correct! Group 1 verb 磨く conjugates to negative base 磨か + ないで."},
      {"text": "磨き（みがき）", "isCorrect": False, "reason": "Incorrect. Masu-stem cannot attach to ないで."},
      {"text": "磨く（みがく）", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach to ないで."},
      {"text": "磨いた（みがいた）", "isCorrect": False, "reason": "Incorrect. Past form cannot attach to ないで."}
    ]
  },
  "added-g2-20-36": {
    "id": "q-added-g2-20-36-1",
    "question": "会議が何時に始まる（　　）、知っていますか。",
    "translation": "Do you know what time the meeting will start?",
    "options": ["か", "かどうか", "の", "と"],
    "correctIndex": 0,
    "grammarFocus": "Embedded Question with Question Word (〜か)",
    "ruleHint": "Embedded clauses with question words (何時, どこ, だれ) take 〜か; clauses without take 〜かどうか.",
    "explanations": [
      {"text": "か", "isCorrect": True, "reason": "Correct! Because 何時に is an interrogative question word, the clause closes with か."},
      {"text": "かどうか", "isCorrect": False, "reason": "Incorrect. かどうか is used for yes/no questions without question words ('whether or not')."},
      {"text": "の", "isCorrect": False, "reason": "Incorrect. の nominalizes the sentence but does not form an embedded interrogative."},
      {"text": "と", "isCorrect": False, "reason": "Incorrect. と marks direct quotation rather than an embedded inquiry."}
    ]
  },
  "added-g2-20-37": {
    "id": "q-added-g2-20-37-1",
    "question": "この字は薄くてとても（　　）にくいです。",
    "translation": "This lettering is faint and very difficult to read.",
    "options": ["読み", "読む", "読んで", "読んだ"],
    "correctIndex": 0,
    "grammarFocus": "Difficulty Suffix 〜にくい (Verb stem + にくい)",
    "ruleHint": "Verb ます-stem + やすい (easy to do) / にくい (hard to do).",
    "explanations": [
      {"text": "読み", "isCorrect": True, "reason": "Correct! Verb masu-stem (読み) + にくい expresses physical or practical difficulty."},
      {"text": "読む", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach to にくい."},
      {"text": "読んで", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach to にくい."},
      {"text": "読んだ", "isCorrect": False, "reason": "Incorrect. Ta-form cannot attach to にくい."}
    ]
  },
  "added-g2-21-38": {
    "id": "q-added-g2-21-38-1",
    "question": "満員電車の中で、見知らぬ人に足を（　　）痛かったです。",
    "translation": "On the crowded train, someone stepped on my foot, and it was painful.",
    "options": ["踏まれて（ふまれて）", "踏んで（ふんで）", "踏ませて（ふませて）", "踏み（ふみ）"],
    "correctIndex": 0,
    "grammarFocus": "Adversity / Suffering Passive (被害受身)",
    "ruleHint": "Suffering passive: Victim は Culprit に Belonging を Verb-受身形.",
    "explanations": [
      {"text": "踏まれて（ふまれて）", "isCorrect": True, "reason": "Correct! Adversity passive: 見知らぬ人に足を踏まれる = having one's foot stepped on."},
      {"text": "踏んで（ふんで）", "isCorrect": False, "reason": "Incorrect. Active voice implies the speaker stepped on someone else's foot."},
      {"text": "踏ませて（ふませて）", "isCorrect": False, "reason": "Incorrect. Causative implies making someone step on the foot."},
      {"text": "踏み（ふみ）", "isCorrect": False, "reason": "Incorrect. Masu-stem does not convey passive adversity."}
    ]
  },
  "added-g2-21-39": {
    "id": "q-added-g2-21-39-1",
    "question": "部屋が暗いから、もっと（　　）してください。",
    "translation": "The room is dark, so please make it brighter.",
    "options": ["明るく", "明るい", "明るさに", "明るいで"],
    "correctIndex": 0,
    "grammarFocus": "Adjective + する (Deliberate Change: Make X)",
    "ruleHint": "い-adjective (drop い) + くする denotes intentionally changing a state: 明るくする.",
    "explanations": [
      {"text": "明るく", "isCorrect": True, "reason": "Correct! い-adjective takes く before する: 明るくする (to make bright)."},
      {"text": "明るい", "isCorrect": False, "reason": "Incorrect. Bare adjective cannot attach to する."},
      {"text": "明るさに", "isCorrect": False, "reason": "Incorrect. 明るさ is a noun ('brightness') and does not form this comparative adjustment."},
      {"text": "明るいで", "isCorrect": False, "reason": "Incorrect. い-adjectives do not conjugate with で."}
    ]
  },
  "added-g2-22-40": {
    "id": "q-added-g2-22-40-1",
    "question": "母は毎日弟に野菜を（　　）。",
    "translation": "Mother makes my younger brother eat vegetables every day.",
    "options": ["食べさせます", "食べられます", "食べさせられます", "食べてもらいます"],
    "correctIndex": 0,
    "grammarFocus": "Causative Form 使役形 (Make someone do)",
    "ruleHint": "Transitive causative: Director は Actor に Object を Verb-Causative (食べさせる).",
    "explanations": [
      {"text": "食べさせます", "isCorrect": True, "reason": "Correct! Group 2 verb 食べる becomes causative 食べさせる: makes him eat."},
      {"text": "食べられます", "isCorrect": False, "reason": "Incorrect. 食べられます is passive or potential ('can eat')."},
      {"text": "食べさせられます", "isCorrect": False, "reason": "Incorrect. 食べさせられます is causative-passive ('is forced to eat')."},
      {"text": "食べてもらいます", "isCorrect": False, "reason": "Incorrect. 食べてもらう implies receiving a favor, which does not fit parental disciplinary direction."}
    ]
  },
  "added-g2-22-41": {
    "id": "q-added-g2-22-41-1",
    "question": "もう遅い時間だから、早く（　　）なさい。",
    "translation": "It is already late, so hurry up and go to sleep.",
    "options": ["寝（ね）", "寝る（ねる）", "寝て（ねて）", "寝た（ねた）"],
    "correctIndex": 0,
    "grammarFocus": "Firm Parental Command 〜なさい",
    "ruleHint": "Verb ます-stem + なさい gives firm, authoritative direction (parents to children, teachers to students).",
    "explanations": [
      {"text": "寝（ね）", "isCorrect": True, "reason": "Correct! Group 2 verb 寝る takes masu-stem 寝 + なさい: 寝なさい."},
      {"text": "寝る（ねる）", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach to なさい."},
      {"text": "寝て（ねて）", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach to なさい."},
      {"text": "寝た（ねた）", "isCorrect": False, "reason": "Incorrect. Ta-form cannot attach to なさい."}
    ]
  },
  "added-g2-22-42": {
    "id": "q-added-g2-22-42-1",
    "question": "あの雲はまるで白い羊の（　　）ですね。",
    "translation": "That cloud looks just like a white sheep, doesn't it?",
    "options": ["ようだ", "ようで", "そう", "らしい"],
    "correctIndex": 0,
    "grammarFocus": "Simile / Metaphor: Noun + のようだ (Like)",
    "ruleHint": "Noun + のようだ expresses figurative resemblance ('just like N').",
    "explanations": [
      {"text": "ようだ", "isCorrect": True, "reason": "Correct! Noun + のようだ denotes figurative resemblance: 白い羊のようだ."},
      {"text": "ようで", "isCorrect": False, "reason": "Incorrect. ようで is linking te-form, but sentence ends here with ね."},
      {"text": "そう", "isCorrect": False, "reason": "Incorrect. そう cannot attach after Noun + の."},
      {"text": "らしい", "isCorrect": False, "reason": "Incorrect. Noun + らしい denotes typicality ('acts like a true sheep'), not metaphorical simile."}
    ]
  },
  "added-g2-23-43": {
    "id": "q-added-g2-23-43-1",
    "question": "子供のころ、嫌いなピーマンを無理やり（　　）。",
    "translation": "When I was a child, I was forced to eat bell peppers against my will.",
    "options": ["食べさせられました", "食べさせました", "食べられました", "食べてあげました"],
    "correctIndex": 0,
    "grammarFocus": "Causative-Passive 使役受身 (Forced to do)",
    "ruleHint": "Causative-passive expresses being compelled by someone else to perform an undesirable action.",
    "explanations": [
      {"text": "食べさせられました", "isCorrect": True, "reason": "Correct! Group 2 causative-passive 食べさせられる conveys being forced to eat."},
      {"text": "食べさせました", "isCorrect": False, "reason": "Incorrect. 食べさせました is active causative (I made someone else eat)."},
      {"text": "食べられました", "isCorrect": False, "reason": "Incorrect. 食べられました is simple passive or potential."},
      {"text": "食べてあげました", "isCorrect": False, "reason": "Incorrect. 食べてあげました means I ate it as a favor to them."}
    ]
  },
  "added-g2-23-44": {
    "id": "q-added-g2-23-44-1",
    "question": "健康のために、毎晩十時前には寝る（　　）にしています。",
    "translation": "For my health, I make it a personal rule to go to bed before ten every night.",
    "options": ["こと", "もの", "わけ", "ところ"],
    "correctIndex": 0,
    "grammarFocus": "Maintained Personal Habit (〜ことにしている)",
    "ruleHint": "Verb 辞書形 / ない形 + ことにしている expresses a conscious, self-determined habit or discipline.",
    "explanations": [
      {"text": "こと", "isCorrect": True, "reason": "Correct! 〜ことにしている denotes an ongoing self-imposed personal rule."},
      {"text": "もの", "isCorrect": False, "reason": "Incorrect. 〜ものにしている is ungrammatical."},
      {"text": "わけ", "isCorrect": False, "reason": "Incorrect. 〜わけにしている is ungrammatical."},
      {"text": "ところ", "isCorrect": False, "reason": "Incorrect. 〜ところにしている is ungrammatical."}
    ]
  },
  "added-g2-23-45": {
    "id": "q-added-g2-23-45-1",
    "question": "レポートは明日の午後五時（　　）提出してください。",
    "translation": "Please submit your report by 5:00 PM tomorrow.",
    "options": ["までに", "まで", "から", "で"],
    "correctIndex": 0,
    "grammarFocus": "Deadline: 〜までに (By the time)",
    "ruleHint": "〜まで indicates continuous action lasting until a point; 〜までに marks a deadline by which a single action must finish.",
    "explanations": [
      {"text": "までに", "isCorrect": True, "reason": "Correct! 〜までに marks a one-time deadline for completion: 五時までに提出する."},
      {"text": "まで", "isCorrect": False, "reason": "Incorrect. 〜まで requires continuous action (五時まで待つ), not one-off instantaneous actions like 提出する."},
      {"text": "から", "isCorrect": False, "reason": "Incorrect. から means 'starting from'."},
      {"text": "で", "isCorrect": False, "reason": "Incorrect. で marks duration/means, not a strict clock deadline."}
    ]
  }
}

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

updated = 0
for p in points:
    if p['id'] in G2_QUIZZES and len(p.get('quiz', [])) == 0:
        p['quiz'] = [G2_QUIZZES[p['id']]]
        updated += 1

with open("jlpt-exam-prep/src/data/studyPoints.json", "w", encoding="utf-8") as f:
    json.dump(points, f, ensure_ascii=False, indent=2)

print(f"Added quizzes to {updated} Genki II cards!")
