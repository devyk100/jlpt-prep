# -*- coding: utf-8 -*-
import json

G1_QUIZZES = {
  "added-g1-2-1": {
    "id": "q-added-g1-2-1-1",
    "question": "A:「これは（　　）傘ですか。」 B:「田中さんの傘ですよ。」",
    "translation": "A: 'Whose umbrella is this?' B: 'It's Tanaka's umbrella, you know.'",
    "options": ["だれの", "どれの", "どこの", "だれ"],
    "correctIndex": 0,
    "grammarFocus": "だれの (Whose) + よ",
    "ruleHint": "だれの + Noun asks about ownership/possession.",
    "explanations": [
      {"text": "だれの", "isCorrect": True, "reason": "Correct! だれの modifies 傘 to ask 'whose umbrella'."},
      {"text": "どれの", "isCorrect": False, "reason": "Incorrect. どれ means 'which one' (among three or more) and does not ask for personal ownership."},
      {"text": "どこの", "isCorrect": False, "reason": "Incorrect. どこの asks for place, country of origin, or company."},
      {"text": "だれ", "isCorrect": False, "reason": "Incorrect. だれ lacks particle の needed to modify the following noun 傘."}
    ]
  },
  "added-g1-3-2": {
    "id": "q-added-g1-3-2-1",
    "question": "私は毎晩、図書館（　　）日本語を勉強します。",
    "translation": "I study Japanese at the library every night.",
    "options": ["で", "に", "を", "へ"],
    "correctIndex": 0,
    "grammarFocus": "Particle で (Location of Action)",
    "ruleHint": "Place + で marks the location where an active event takes place.",
    "explanations": [
      {"text": "で", "isCorrect": True, "reason": "Correct! で marks 図書館 as the place where the dynamic action of studying occurs."},
      {"text": "に", "isCorrect": False, "reason": "Incorrect. に marks static location of existence (with います/あります) or destination of movement."},
      {"text": "を", "isCorrect": False, "reason": "Incorrect. を marks direct objects (already used in 日本語を)."},
      {"text": "へ", "isCorrect": False, "reason": "Incorrect. へ marks direction of travel towards a destination."}
    ]
  },
  "added-g1-3-3": {
    "id": "q-added-g1-3-3-1",
    "question": "毎朝七時（　　）起きますが、日曜日はあまり早く起きません。",
    "translation": "I get up at seven every morning, but on Sundays I don't get up very early.",
    "options": ["に", "で", "を", "へ"],
    "correctIndex": 0,
    "grammarFocus": "Time particle に + あまり + Negative",
    "ruleHint": "Specific numerical clock times take に; relative times like 毎朝 do not.",
    "explanations": [
      {"text": "に", "isCorrect": True, "reason": "Correct! Specific point in time (七時) takes particle に."},
      {"text": "で", "isCorrect": False, "reason": "Incorrect. で marks means or action location, not clock time."},
      {"text": "を", "isCorrect": False, "reason": "Incorrect. を marks direct objects."},
      {"text": "へ", "isCorrect": False, "reason": "Incorrect. へ marks direction of movement."}
    ]
  },
  "added-g1-4-4": {
    "id": "q-added-g1-4-4-1",
    "question": "あそこに大きい木が（　　）、木の下に可愛い猫が（　　）。",
    "translation": "Over there is a big tree, and under the tree is a cute cat.",
    "options": ["あります／います", "います／あります", "あります／あります", "います／います"],
    "correctIndex": 0,
    "grammarFocus": "あります (Inanimate) vs います (Animate)",
    "ruleHint": "Inanimate objects (木, 机) take あります; living people and animals (猫, 学生) take います.",
    "explanations": [
      {"text": "あります／います", "isCorrect": True, "reason": "Correct! 木 is an inanimate plant (あります) and 猫 is a living animal (います)."},
      {"text": "います／あります", "isCorrect": False, "reason": "Incorrect. Inverts animate and inanimate verbs of existence."},
      {"text": "あります／あります", "isCorrect": False, "reason": "Incorrect. Animate living animals like 猫 require います."},
      {"text": "います／います", "isCorrect": False, "reason": "Incorrect. Inanimate objects like 木 require あります."}
    ]
  },
  "added-g1-4-5": {
    "id": "q-added-g1-4-5-1",
    "question": "昨日は図書館で友達と（　　）日本語を勉強しました。",
    "translation": "Yesterday I studied Japanese with a friend for three hours at the library.",
    "options": ["三時間", "三時間に", "三時間の", "三時間で"],
    "correctIndex": 0,
    "grammarFocus": "Duration of time (No に)",
    "ruleHint": "Time spans/durations (三時間, 二日間) function adverbially and do NOT take particle に.",
    "explanations": [
      {"text": "三時間", "isCorrect": True, "reason": "Correct! Duration counters attach directly without particle に."},
      {"text": "三時間に", "isCorrect": False, "reason": "Incorrect. に marks point in time (三時に), never duration of time."},
      {"text": "三時間の", "isCorrect": False, "reason": "Incorrect. の requires a following noun to modify."},
      {"text": "三時間で", "isCorrect": False, "reason": "Incorrect. で specifies a time limit for completion, not simple duration spent."}
    ]
  },
  "added-g1-5-6": {
    "id": "q-added-g1-5-6-1",
    "question": "昨日の試験は全然（　　）でした。",
    "translation": "Yesterday's exam was not difficult at all.",
    "options": ["難しくなかった", "難しくない", "難しかった", "難しいじゃなかった"],
    "correctIndex": 0,
    "grammarFocus": "い-Adjective Past Negative (〜くなかった)",
    "ruleHint": "い-adjectives form past negative with 〜くなかった (drop い + くなかった).",
    "explanations": [
      {"text": "難しくなかった", "isCorrect": True, "reason": "Correct! 難しい becomes 難しくなかった in the past negative, pairing with 昨日の and 全然."},
      {"text": "難しくない", "isCorrect": False, "reason": "Incorrect. 難しくない is present/non-past tense, clashing with 昨日の."},
      {"text": "難しかった", "isCorrect": False, "reason": "Incorrect. 難しかった is affirmative, clashing with 全然 which requires negative."},
      {"text": "難しいじゃなかった", "isCorrect": False, "reason": "Incorrect. い-adjectives never conjugate with じゃなかった (that is for な-adjectives and nouns)."}
    ]
  },
  "added-g1-5-7": {
    "id": "q-added-g1-5-7-1",
    "question": "郵便局で綺麗な切手を（　　）買いました。",
    "translation": "I bought five beautiful stamps at the post office.",
    "options": ["五枚", "五台", "五本", "五匹"],
    "correctIndex": 0,
    "grammarFocus": "Flat object counter 〜枚 (まい)",
    "ruleHint": "Flat, thin objects like stamps (切手), paper (紙), and shirts (シャツ) are counted with 〜枚.",
    "explanations": [
      {"text": "五枚", "isCorrect": True, "reason": "Correct! Stamps (切手) are thin flat items counted with 〜枚 (ごまい)."},
      {"text": "五台", "isCorrect": False, "reason": "Incorrect. 〜台 (だい) counts machines, computers, and vehicles."},
      {"text": "五本", "isCorrect": False, "reason": "Incorrect. 〜本 (ほん) counts long cylindrical items like pens and bottles."},
      {"text": "五匹", "isCorrect": False, "reason": "Incorrect. 〜匹 (ひき) counts small animals."}
    ]
  },
  "added-g1-6-8": {
    "id": "q-added-g1-6-8-1",
    "question": "図書館の中では大きな声で（　　）はいけません。",
    "translation": "You must not speak in a loud voice inside the library.",
    "options": ["話して", "話す", "話し", "話した"],
    "correctIndex": 0,
    "grammarFocus": "Prohibition 〜てはいけません",
    "ruleHint": "Verb て-form + はいけません expresses strict prohibition ('must not do').",
    "explanations": [
      {"text": "話して", "isCorrect": True, "reason": "Correct! Prohibition attaches to verb te-form: 話して + はいけません."},
      {"text": "話す", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach directly to はいけません."},
      {"text": "話し", "isCorrect": False, "reason": "Incorrect. Masu-stem cannot attach directly to はいけません."},
      {"text": "話した", "isCorrect": False, "reason": "Incorrect. Ta-form cannot attach to はいけません."}
    ]
  },
  "added-g1-7-9": {
    "id": "q-added-g1-7-9-1",
    "question": "姉は三年前に結婚して、今は東京に（　　）。",
    "translation": "My older sister got married three years ago, and now lives in Tokyo.",
    "options": ["住んでいます", "住みます", "住んであります", "住み始めます"],
    "correctIndex": 0,
    "grammarFocus": "〜ている (Resultant State of Living)",
    "ruleHint": "住む is a verb of instantaneous change; residing in a place is expressed as 住んでいる.",
    "explanations": [
      {"text": "住んでいます", "isCorrect": True, "reason": "Correct! Residence is a continuous state resulting from moving: 住んでいます."},
      {"text": "住みます", "isCorrect": False, "reason": "Incorrect. 住みます denotes future intention to live, not current residence."},
      {"text": "住んであります", "isCorrect": False, "reason": "Incorrect. 〜てある is used with transitive verbs for deliberate preparations."},
      {"text": "住み始めます", "isCorrect": False, "reason": "Incorrect. 住み始めます denotes initiating residence in the future."}
    ]
  },
  "added-g1-7-10": {
    "id": "q-added-g1-7-10-1",
    "question": "昨日のパーティーには留学生が（　　）来ました。",
    "translation": "Four international students came to yesterday's party.",
    "options": ["四人（よにん）", "四人（よんにん）", "四人（しにん）", "四つ（よっつ）"],
    "correctIndex": 0,
    "grammarFocus": "People Counter 四人 (よにん)",
    "ruleHint": "Four people is uniquely pronounced よにん (never よんにん or しにん).",
    "explanations": [
      {"text": "四人（よにん）", "isCorrect": True, "reason": "Correct! Four people is pronounced with phonological reduction as よにん."},
      {"text": "四人（よんにん）", "isCorrect": False, "reason": "Incorrect. よんにん is an erroneous phonological pronunciation."},
      {"text": "四人（しにん）", "isCorrect": False, "reason": "Incorrect. しにん sounds like 'dead person' (死人) and is strictly avoided."},
      {"text": "四つ（よっつ）", "isCorrect": False, "reason": "Incorrect. よっつ counts inanimate objects, never people."}
    ]
  },
  "added-g1-8-11": {
    "id": "q-added-g1-8-11-1",
    "question": "明日は雨が（　　）と思います。",
    "translation": "I think it will rain tomorrow.",
    "options": ["降る", "降ります", "降って", "降り"],
    "correctIndex": 0,
    "grammarFocus": "Quotation / Belief with 〜と思う (Plain form)",
    "ruleHint": "〜と思う quotes a thought in plain (short) form: Verb 辞書形 / た形 / ない形 + と思う.",
    "explanations": [
      {"text": "降る", "isCorrect": True, "reason": "Correct! 〜と思う takes short/plain forms (降る + と思います)."},
      {"text": "降ります", "isCorrect": False, "reason": "Incorrect. Polite forms like 降ります do not precede と思います in standard speech."},
      {"text": "降って", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach directly to と思います."},
      {"text": "降り", "isCorrect": False, "reason": "Incorrect. Stem form cannot attach directly to と思います."}
    ]
  },
  "added-g1-8-12": {
    "id": "q-added-g1-8-12-1",
    "question": "お腹が痛かったので、今朝は（　　）食べませんでした。",
    "translation": "Because my stomach hurt, I didn't eat anything this morning.",
    "options": ["何も", "何か", "何が", "何を"],
    "correctIndex": 0,
    "grammarFocus": "何も + Negative (Nothing / Not anything)",
    "ruleHint": "何か takes affirmative sentences ('something'); 何も takes negative predicates ('not anything').",
    "explanations": [
      {"text": "何も", "isCorrect": True, "reason": "Correct! 何も pairs with negative verbs (食べませんでした) to mean 'nothing at all'."},
      {"text": "何か", "isCorrect": False, "reason": "Incorrect. 何か means 'something' and pairs with affirmative predicates."},
      {"text": "何が", "isCorrect": False, "reason": "Incorrect. 何が is a question word subject marker ('what is...')."},
      {"text": "何を", "isCorrect": False, "reason": "Incorrect. 何を asks 'what did you eat?' in question sentences."}
    ]
  },
  "added-g1-9-13": {
    "id": "q-added-g1-9-13-1",
    "question": "あそこで眼鏡を（　　）人は、私の日本語の先生です。",
    "translation": "The person wearing glasses over there is my Japanese teacher.",
    "options": ["かけている", "かけます", "かけた", "かけて"],
    "correctIndex": 0,
    "grammarFocus": "Noun Modification with Relative Clause (〜ている人)",
    "ruleHint": "Relative clauses modify nouns using plain forms; state of wearing accessories uses 〜ている.",
    "explanations": [
      {"text": "かけている", "isCorrect": True, "reason": "Correct! Wearing glasses is a continuous state modifying 人: かけている人."},
      {"text": "かけます", "isCorrect": False, "reason": "Incorrect. Polite forms (ます) cannot modify a noun in a relative clause."},
      {"text": "かけた", "isCorrect": False, "reason": "Incorrect. かけた人 denotes having put on in the past rather than the ongoing state visible over there."},
      {"text": "かけて", "isCorrect": False, "reason": "Incorrect. Te-form cannot directly modify a noun."}
    ]
  },
  "added-g1-10-14": {
    "id": "q-added-g1-10-14-1",
    "question": "季節の中で、春と秋とどちらの（　　）好きですか。",
    "translation": "Between spring and autumn, which one do you like better?",
    "options": ["ほうが", "より", "から", "ほど"],
    "correctIndex": 0,
    "grammarFocus": "Comparison: A と B とどちらのほうが〜か",
    "ruleHint": "When comparing two alternatives, どちらのほうが asks 'which side is more...'.",
    "explanations": [
      {"text": "ほうが", "isCorrect": True, "reason": "Correct! どちらのほうが is the fixed comparative formula for choosing between two items."},
      {"text": "より", "isCorrect": False, "reason": "Incorrect. より marks the baseline of comparison ('than'), not the selected side."},
      {"text": "から", "isCorrect": False, "reason": "Incorrect. から means 'from' or 'because'."},
      {"text": "ほど", "isCorrect": False, "reason": "Incorrect. ほど is used in negative comparison ('not as much as')."}
    ]
  },
  "added-g1-10-15": {
    "id": "q-added-g1-10-15-1",
    "question": "A:「どれが田中さんのペンですか。」 B:「あの黒い（　　）です。」",
    "translation": "A: 'Which one is Tanaka-san's pen?' B: 'It's that black one.'",
    "options": ["の", "こと", "もの", "方"],
    "correctIndex": 0,
    "grammarFocus": "Noun-substitute pronoun の (The one)",
    "ruleHint": "Adjective + の replaces a previously mentioned concrete noun (黒いペン → 黒いの).",
    "explanations": [
      {"text": "の", "isCorrect": True, "reason": "Correct! の acts as the pronoun 'one' replacing the noun ペン: 黒いのです."},
      {"text": "こと", "isCorrect": False, "reason": "Incorrect. こと refers to abstract concepts or matters, never physical items like pens."},
      {"text": "もの", "isCorrect": False, "reason": "Incorrect. 黒いもの is unnecessarily general/formal when referring to an identified pen."},
      {"text": "方", "isCorrect": False, "reason": "Incorrect. 方 means 'direction' or 'person' (polite)."}
    ]
  },
  "added-g1-10-16": {
    "id": "q-added-g1-10-16-1",
    "question": "先週末は疲れていたので、（　　）出かけませんでした。",
    "translation": "Because I was tired last weekend, I didn't go anywhere.",
    "options": ["どこにも", "どこかに", "どこかへ", "どこでも"],
    "correctIndex": 0,
    "grammarFocus": "どこにも + Negative (Not anywhere)",
    "ruleHint": "どこか means 'somewhere'; どこにも / どこへも pairs with negative verbs to mean 'nowhere'.",
    "explanations": [
      {"text": "どこにも", "isCorrect": True, "reason": "Correct! どこにも pairs with negative verbs (出かけませんでした) to mean 'nowhere at all'."},
      {"text": "どこかに", "isCorrect": False, "reason": "Incorrect. どこかに means 'to somewhere' and pairs with affirmative actions."},
      {"text": "どこかへ", "isCorrect": False, "reason": "Incorrect. どこかへ also pairs with affirmative predicates."},
      {"text": "どこでも", "isCorrect": False, "reason": "Incorrect. どこでも means 'anywhere / everywhere' and takes affirmative verbs."}
    ]
  },
  "added-g1-11-17": {
    "id": "q-added-g1-11-17-1",
    "question": "休みの日は、部屋を掃除し（　　）、洗濯し（　　）しました。",
    "translation": "On my days off, I did things like cleaning my room and doing laundry.",
    "options": ["たり／たり", "て／て", "し／し", "ながら／ながら"],
    "correctIndex": 0,
    "grammarFocus": "Listing representative activities (〜たり〜たりする)",
    "ruleHint": "Verb た-form + り + Verb た-form + り + する lists representative non-exhaustive actions.",
    "explanations": [
      {"text": "たり／たり", "isCorrect": True, "reason": "Correct! 掃除したり、洗濯したりしました lists non-exhaustive weekend activities."},
      {"text": "て／て", "isCorrect": False, "reason": "Incorrect. て-form lists chronological sequential actions in full, not representative examples."},
      {"text": "し／し", "isCorrect": False, "reason": "Incorrect. 〜し〜し lists reasons or predicates in plain form."},
      {"text": "ながら／ながら", "isCorrect": False, "reason": "Incorrect. 〜ながら indicates simultaneous actions conducted at the exact same moment."}
    ]
  },
  "added-g1-12-18": {
    "id": "q-added-g1-12-18-1",
    "question": "A:「顔色が悪いですね。どうしたんですか。」 B:「頭がとても痛い（　　）。」",
    "translation": "A: 'You look pale. What's the matter?' B: 'It's that I have a very bad headache.'",
    "options": ["んです", "のですか", "からだ", "わけだ"],
    "correctIndex": 0,
    "grammarFocus": "Explanatory 〜んです (Providing rationale)",
    "ruleHint": "〜んです provides an explanation or reason for an observed situation or state.",
    "explanations": [
      {"text": "んです", "isCorrect": True, "reason": "Correct! 痛いんです directly answers どうしたんですか with an explanatory statement."},
      {"text": "のですか", "isCorrect": False, "reason": "Incorrect. のですか is a question form, but B is providing an answer."},
      {"text": "からだ", "isCorrect": False, "reason": "Incorrect. からだ is plain causal assertion without the communicative engagement of んです."},
      {"text": "わけだ", "isCorrect": False, "reason": "Incorrect. わけだ means 'so that's why' (drawing a logical conclusion)."}
    ]
  },
  "added-g1-12-19": {
    "id": "q-added-g1-12-19-1",
    "question": "熱が高いですから、今日は無理をしない（　　）いいですよ。",
    "translation": "Since your fever is high, it's better not to overdo it today.",
    "options": ["ほうが", "より", "ほど", "ように"],
    "correctIndex": 0,
    "grammarFocus": "Negative Advice: 〜ないほうがいい",
    "ruleHint": "Giving advice: V-た + ほうがいい (should do) / V-ない + ほうがいい (should not do).",
    "explanations": [
      {"text": "ほうが", "isCorrect": True, "reason": "Correct! V-ない + ほうがいい advises against an action: 無理をしないほうがいい."},
      {"text": "より", "isCorrect": False, "reason": "Incorrect. より marks comparison ('than'), not advice."},
      {"text": "ほど", "isCorrect": False, "reason": "Incorrect. ほど indicates degree or extent."},
      {"text": "ように", "isCorrect": False, "reason": "Incorrect. ように denotes purpose or indirect request, not direct advice."}
    ]
  }
}

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

updated = 0
for p in points:
    if p['id'] in G1_QUIZZES and len(p.get('quiz', [])) == 0:
        p['quiz'] = [G1_QUIZZES[p['id']]]
        updated += 1

with open("jlpt-exam-prep/src/data/studyPoints.json", "w", encoding="utf-8") as f:
    json.dump(points, f, ensure_ascii=False, indent=2)

print(f"Added quizzes to {updated} Genki I cards!")
