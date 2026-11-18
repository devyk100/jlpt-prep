import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
BASE_PATH = ROOT / "content/base-reviewed.json"
CHAPTER_EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"
MATRIX_PATH = ROOT / "audit/source-coverage-matrix.json"

# 1. 12 Authentic Exercises for Form Review I
fi_exercises = [
    {
        "id": "skm3-fi-q1",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review I",
        "type": "multiple-choice",
        "context": "Rare frequency: busy CEO rarely takes days off even on weekends.",
        "question": "社長は仕事熱心で、週末でも（　）休むことはない。",
        "translation": "The company president is so devoted to work that he rarely if ever takes a day off, even on weekends.",
        "options": ["めったに", "ぜったいに", "かならず", "たいてい"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-i-67",
        "grammarPointTitle": "後に決まった表現が来る副詞 I (Adverb & Ending Collocations)",
        "explanation": {
            "overall": "「めったに＋否定形（〜ない／〜ことはない）」は、極めて発生頻度が低いこと（滅多に〜ない）を表す厳格な呼応副詞です。",
            "options": [
                {"text": "めったに", "isCorrect": True, "reason": "【正解】めったに…ない（低頻度呼応）。", "trapCategory": ""},
                {"text": "ぜったいに", "isCorrect": False, "reason": "【不正解】絶対否定には「絶対に休まない」が自然であり、休む「ことはない」の頻度語法には「めったに」が最適です。", "trapCategory": "nuance"},
                {"text": "かならず", "isCorrect": False, "reason": "【不正解】肯定呼応副詞であり、否定形と矛盾します。", "trapCategory": "formation"},
                {"text": "たいてい", "isCorrect": False, "reason": "【不正解】「大抵（普段は）」は通常肯定文で用いられます。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which adverb pairs strictly with a negative predicate to express extreme rarity?"
    },
    {
        "id": "skm3-fi-q2",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review I",
        "type": "multiple-choice",
        "context": "Imminent weather event: sky turned pitch black and dark clouds indicate rain any second.",
        "question": "空が急に真っ暗になり、黒い雲から（　）大雨が降り出しそうだ。",
        "translation": "The sky suddenly turned pitch black, and it looks like heavy rain will pour down from the dark clouds at any moment.",
        "options": ["今にも", "いまさら", "いまごろ", "いまでは"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-i-67",
        "grammarPointTitle": "後に決まった表現が来る副詞 I (Adverb & Ending Collocations)",
        "explanation": {
            "overall": "「今にも＋動詞語幹＋そうだ」は、『まさに次の瞬間、直前に行為や変化が起きそうである』という切迫した様態・直前兆候を表す呼応副詞です（過去形や確定事実には接続不可）。",
            "options": [
                {"text": "今にも", "isCorrect": True, "reason": "【正解】今にも…そうだ（直前切迫様態の呼応）。", "trapCategory": ""},
                {"text": "いまさら", "isCorrect": False, "reason": "【不正解】今更（手遅れのニュアンス）となり文脈不一致。", "trapCategory": "meaning"},
                {"text": "いまごろ", "isCorrect": False, "reason": "【不正解】今頃（時期・時間帯の推測）となり合いません。", "trapCategory": "meaning"},
                {"text": "いまでは", "isCorrect": False, "reason": "【不正解】今では（過去との対比）となり直前の兆候を表せません。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What adverb pairs with 〜そうだ to signal an imminent crisis on the verge of happening?"
    },
    {
        "id": "skm3-fi-q3",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review I",
        "type": "multiple-choice",
        "context": "Vivid metaphorical simile: mountain covered in fresh snow looks just like a giant white castle.",
        "question": "新雪に覆われた冬の山は、（　）巨大な白い城のようだ。",
        "translation": "The winter mountain covered in fresh snow looks just like a gigantic white castle.",
        "options": ["まるで", "まさに", "どうしても", "案外"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-i-67",
        "grammarPointTitle": "後に決まった表現が来る副詞 I (Adverb & Ending Collocations)",
        "explanation": {
            "overall": "「まるで＋〜ようだ／みたいだ」は、ある事物の様子を比喩的に『あたかも〜であるかのように見える』と生き生きと形容する定番の比況呼応です。",
            "options": [
                {"text": "まるで", "isCorrect": True, "reason": "【正解】まるで…ようだ（比喩・比況の教科書的完全呼応）。", "trapCategory": ""},
                {"text": "まさに", "isCorrect": False, "reason": "【不正解】「まさに〜そのものだ」と事実を強調する語であり、比喩の「ようだ」には「まるで」が正統。", "trapCategory": "nuance"},
                {"text": "どうしても", "isCorrect": False, "reason": "【不正解】強い願望や不可能性を表す副詞であり不適です。", "trapCategory": "meaning"},
                {"text": "案外", "isCorrect": False, "reason": "【不正解】案外（予想外に）となり比喩を導けません。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which adverb introduces a vivid metaphorical comparison pairing with 〜ようだ?"
    },
    {
        "id": "skm3-fi-q4",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review I",
        "type": "multiple-choice",
        "context": "Resolute ethical pledge: promise made to friends will never be broken under any circumstances.",
        "question": "仲間と交わした大切な約束は、（　）破りません。",
        "translation": "I will never break the precious promise exchanged with my comrades, under any circumstances whatsoever.",
        "options": ["決して", "必ずしも", "まったく", "せいぜい"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-i-67",
        "grammarPointTitle": "後に決まった表現が来る副詞 I (Adverb & Ending Collocations)",
        "explanation": {
            "overall": "「決して＋否定形（〜ない／〜ません）」は、強い誓い・決意をもって『絶対に〜しない』と断固として否定する呼応表現です。",
            "options": [
                {"text": "決して", "isCorrect": True, "reason": "【正解】決して…ない（強い決意・断固たる否定呼応）。", "trapCategory": ""},
                {"text": "必ずしも", "isCorrect": False, "reason": "【不正解】部分否定（必ずしも破らないわけではない）となり、誓いの強さが消滅します。", "trapCategory": "nuance"},
                {"text": "まったく", "isCorrect": False, "reason": "【不正解】程度の完全欠如（まったく分からない）であり、将来の意志的誓いには「決して」が自然。", "trapCategory": "nuance"},
                {"text": "せいぜい", "isCorrect": False, "reason": "【不正解】最大限の見積もり副詞であり不適です。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What adverb pairs with negative verbs to express a resolute, unwavering vow (never ever)?"
    },
    {
        "id": "skm3-fi-q5",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review I",
        "type": "multiple-choice",
        "context": "Gradual continuous progress: as time passed, patient's physical stamina gradually recovered.",
        "question": "リハビリを根気強く続けた結果、体力が（　）回復してきた。",
        "translation": "As a result of patiently continuing rehabilitation, his physical stamina gradually recovered little by little.",
        "options": ["次第に", "一気に", "めったに", "今にも"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-i-67",
        "grammarPointTitle": "後に決まった表現が来る副詞 I (Adverb & Ending Collocations)",
        "explanation": {
            "overall": "「次第に＋変化動詞／〜ていく／〜てくる」は、時間の経過に伴い『少しずつ段階的に事態が推移していく』ことを表す呼応副詞です。",
            "options": [
                {"text": "次第に", "isCorrect": True, "reason": "【正解】次第に…てくる（段階的推移・変化の呼応）。", "trapCategory": ""},
                {"text": "一気に", "isCorrect": False, "reason": "【不正解】一気に（急激に一瞬で）となり、根気強い継続の文脈に反します。", "trapCategory": "nuance"},
                {"text": "めったに", "isCorrect": False, "reason": "【不正解】否定呼応副詞であり肯定文に不適。", "trapCategory": "formation"},
                {"text": "今にも", "isCorrect": False, "reason": "【不正解】今にも…そうだ（直前兆候）専用であり、過去完了の回復には使えません。", "trapCategory": "formation"}
            ]
        },
        "hint": "Which adverb pairs with change verbs to express a gradual, step-by-step progress over time?"
    },
    {
        "id": "skm3-fi-q6",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review I",
        "type": "multiple-choice",
        "context": "Emergency contingency: in the unlikely event of an emergency, please follow staff instructions immediately.",
        "question": "（　）火災や地震が発生した場合は、係員の指示に従って落ち着いて避難してください。",
        "translation": "In the unlikely event that a fire or earthquake should occur, please evacuate calmly following the staff's instructions.",
        "options": ["万一", "たとえ", "どうやら", "せめて"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-i-67",
        "grammarPointTitle": "後に決まった表現が来る副詞 I (Adverb & Ending Collocations)",
        "explanation": {
            "overall": "「万一（万が一）＋〜たら／〜ば／〜場合」は、『滅多にないが、万に一つの確率で危機的事態が起きた際』の危機管理条件文を導く呼応副詞です。",
            "options": [
                {"text": "万一", "isCorrect": True, "reason": "【正解】万一…場合（不測の事態・緊急時の条件文呼応）。", "trapCategory": ""},
                {"text": "たとえ", "isCorrect": False, "reason": "【不正解】譲歩構文「たとえ…ても」と呼応するため、「場合」には合いません。", "trapCategory": "formation"},
                {"text": "どうやら", "isCorrect": False, "reason": "【不正解】推量表現（〜らしい）と呼応するため不適。", "trapCategory": "meaning"},
                {"text": "せめて", "isCorrect": False, "reason": "【不正解】最低限の願望（せめて〜だけでも）であり不適。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What adverb pairs with conditional/emergency clauses meaning 'in the unlikely event of an accident'?"
    },
    {
        "id": "skm3-fi-q7",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review I",
        "type": "multiple-choice",
        "context": "Limiting estimation: distance between houses is short, taking at most 10 minutes on foot.",
        "question": "ここから彼の家までは、（　）歩いて10分くらいのものだ。",
        "translation": "From here to his house, it is at most about a 10-minute walk.",
        "options": ["せいぜい", "もっとも", "どうせ", "とうとう"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-i-67",
        "grammarPointTitle": "後に決まった表現が来る副詞 I (Adverb & Ending Collocations)",
        "explanation": {
            "overall": "「せいぜい＋数量・概数＋だ／くらいだ」は、『どんなに多く見積もってもその程度に過ぎない（精々）』という限定評価を表す呼応副詞です。",
            "options": [
                {"text": "せいぜい", "isCorrect": True, "reason": "【正解】せいぜい…くらいだ（上限見積もり・限定呼応）。", "trapCategory": ""},
                {"text": "もっとも", "isCorrect": False, "reason": "【不正解】最上級または補足説明（尤も）であり、上限見積もりに合いません。", "trapCategory": "meaning"},
                {"text": "どうせ", "isCorrect": False, "reason": "【不正解】投げやりな諦め（どうせ無理だ）となり距離の評価に合いません。", "trapCategory": "nuance"},
                {"text": "とうとう", "isCorrect": False, "reason": "【不正解】最終結果の達成（とうとう完成した）となり不適。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which adverb pairs with numbers or くらい to express 'at most / at best'?"
    },
    {
        "id": "skm3-fi-q8",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review I",
        "type": "multiple-choice",
        "context": "Hypothetical concession: even granting opposition from all relatives, speaker will marry partner.",
        "question": "（　）親族全員に反対されても、私は彼と結婚する決意を変えません。",
        "translation": "Even granting that every single relative opposes it, I will not change my determination to marry him.",
        "options": ["たとえ", "万一", "まるで", "果たして"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-i-67",
        "grammarPointTitle": "後に決まった表現が来る副詞 I (Adverb & Ending Collocations)",
        "explanation": {
            "overall": "「たとえ＋〜ても／でも」は、『極端な事態を仮定して認めたとしても、後件の決意や事実は揺るがない』という仮定譲歩構文を導く代表的呼応副詞です。",
            "options": [
                {"text": "たとえ", "isCorrect": True, "reason": "【正解】たとえ…ても（仮定譲歩の完全呼応）。", "trapCategory": ""},
                {"text": "万一", "isCorrect": False, "reason": "【不正解】「万一…たら」と呼応するため、「ても」には「たとえ」が正解。", "trapCategory": "formation"},
                {"text": "まるで", "isCorrect": False, "reason": "【不正解】比喩呼応副詞（〜ようだ）のため不適。", "trapCategory": "meaning"},
                {"text": "果たして", "isCorrect": False, "reason": "【不正解】疑問呼応副詞（〜だろうか）のため不適。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What adverb specifically introduces an extreme hypothetical concession followed by 〜ても?"
    },
    {
        "id": "skm3-fi-q9",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review I",
        "type": "multiple-choice",
        "context": "Observation-based inference: dark clouds gathering and chilly wind indicate it seems rain will fall soon.",
        "question": "冷たい風が吹き始めた。（　）今夜は雨になりそうだ。",
        "translation": "A chilly wind has begun blowing. Evidently / seemingly, it looks like it will turn to rain tonight.",
        "options": ["どうやら", "どうしても", "めったに", "決して"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-i-67",
        "grammarPointTitle": "後に決まった表現が来る副詞 I (Adverb & Ending Collocations)",
        "explanation": {
            "overall": "「どうやら＋〜そうだ／らしい／ようだ」は、周囲の兆候や間接的根拠から『どうも〜らしい／〜のようだ』と状況を推し量る呼応副詞です。",
            "options": [
                {"text": "どうやら", "isCorrect": True, "reason": "【正解】どうやら…そうだ（兆候に基づく推量呼応）。", "trapCategory": ""},
                {"text": "どうしても", "isCorrect": False, "reason": "【不正解】強い願望や不可能性であり、天候の客観的推量には不適切。", "trapCategory": "nuance"},
                {"text": "めったに", "isCorrect": False, "reason": "【不正解】否定呼応副詞。", "trapCategory": "formation"},
                {"text": "決して", "isCorrect": False, "reason": "【不正解】断固たる否定誓い副詞。", "trapCategory": "meaning"}
            ]
        },
        "hint": "Which adverb pairs with expressions of conjecture (そうだ, らしい, ようだ) based on subtle outward signs?"
    },
    {
        "id": "skm3-fi-q10",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review I",
        "type": "multiple-choice",
        "context": "Rhetorical doubt: will this new untried policy really succeed in reviving the economy?",
        "question": "前例のないこの経済対策で、（　）景気は回復するだろうか。",
        "translation": "With this unprecedented economic measure, will the economy really / truly recover?",
        "options": ["果たして", "まるで", "せいぜい", "必ずしも"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-i-67",
        "grammarPointTitle": "後に決まった表現が来る副詞 I (Adverb & Ending Collocations)",
        "explanation": {
            "overall": "「果たして＋〜だろうか／〜か」は、『本当に〜だろうか、期待通りの結果になるだろうか』という強い疑問や危惧の念を表す疑問呼応副詞です。",
            "options": [
                {"text": "果たして", "isCorrect": True, "reason": "【正解】果たして…だろうか（強い疑問・懐疑の呼応）。", "trapCategory": ""},
                {"text": "まるで", "isCorrect": False, "reason": "【不正解】比喩呼応副詞。", "trapCategory": "meaning"},
                {"text": "せいぜい", "isCorrect": False, "reason": "【不正解】上限見積もり副詞。", "trapCategory": "meaning"},
                {"text": "必ずしも", "isCorrect": False, "reason": "【不正解】部分否定呼応副詞（〜とは限らない）。", "trapCategory": "nuance"}
            ]
        },
        "hint": "What adverb pairs with だろうか to formulate a skeptical question: 'Will it truly happen?'"
    },
    {
        "id": "skm3-fi-q11",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review I",
        "type": "multiple-choice",
        "context": "Partial truth vs universal stereotype: high price does not necessarily guarantee superior durability.",
        "question": "値段が非常に高い商品が、（　）頑丈で長持ちするとは限らない。",
        "translation": "Extremely expensive products are not necessarily durable and long-lasting.",
        "options": ["必ずしも", "決して", "まったく", "めったに"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-i-67",
        "grammarPointTitle": "後に決まった表現が来る副詞 I (Adverb & Ending Collocations)",
        "explanation": {
            "overall": "「必ずしも＋〜とは限らない／〜わけではない」は、『必ずそうであるとは一概に言えない（例外もある）』という部分否定を導く定番呼応です。",
            "options": [
                {"text": "必ずしも", "isCorrect": True, "reason": "【正解】必ずしも…とは限らない（部分否定呼応）。", "trapCategory": ""},
                {"text": "決して", "isCorrect": False, "reason": "【不正解】全否定になり、「高価な物は絶対に頑丈ではない」という不条理な意味になってしまいます。", "trapCategory": "meaning"},
                {"text": "まったく", "isCorrect": False, "reason": "【不正解】完全否定になり文意崩壊。", "trapCategory": "meaning"},
                {"text": "めったに", "isCorrect": False, "reason": "【不正解】頻度副詞であり、性質の普遍性を否定する文脈に合いません。", "trapCategory": "nuance"}
            ]
        },
        "hint": "Which adverb pairs with 〜とは限らない to soften a universal claim (not necessarily)?"
    },
    {
        "id": "skm3-fi-q12",
        "bookId": "skm-n3",
        "chapter": "Part 1 · Form review I",
        "type": "multiple-choice",
        "context": "Utter disbelief / shock: unthinkable that the top straight-A student failed the exam.",
        "question": "学年トップの秀才である彼が、（　）不合格になるとは夢にも思わなかった。",
        "translation": "Never in my wildest dreams did I think that he, the top prodigy of the class, could possibly fail.",
        "options": ["まさか", "どうやら", "せめて", "次第に"],
        "correctIndex": 0,
        "grammarPointId": "added-n3-i-67",
        "grammarPointTitle": "後に決まった表現が来る副詞 I (Adverb & Ending Collocations)",
        "explanation": {
            "overall": "「まさか＋〜とは思わなかった／〜ないだろう」は、『そんな信じられない事態が起こるはずがない』という話者の強い驚愕・信じがたさを表す呼応副詞です。",
            "options": [
                {"text": "まさか", "isCorrect": True, "reason": "【正解】まさか…とは思わなかった（強い驚愕・不信呼応）。", "trapCategory": ""},
                {"text": "どうやら", "isCorrect": False, "reason": "【不正解】推量表現になり驚愕の文脈と不調和。", "trapCategory": "meaning"},
                {"text": "せめて", "isCorrect": False, "reason": "【不正解】最低限の願望であり不適。", "trapCategory": "meaning"},
                {"text": "次第に", "isCorrect": False, "reason": "【不正解】推移副詞であり不適。", "trapCategory": "meaning"}
            ]
        },
        "hint": "What adverb pairs with とは思わなかった to convey stunned disbelief (never in my wildest dreams)?"
    }
]

# Update chapterExercises.json
existing_exs = json.load(open(CHAPTER_EXERCISES_PATH, encoding="utf-8"))
existing_exs = [x for x in existing_exs if x.get("chapter") != "Part 1 · Form review I" and x.get("chapterId") != "skm3-fi"]
existing_exs.extend(fi_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(existing_exs, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with 12 exercises for SKM N3 Form Review I! Total: {len(existing_exs)}")

# 2. Enrich base-reviewed.json
base_cards = json.load(open(BASE_PATH, encoding="utf-8"))

card_enrichments = {
    "added-n3-i-67": {
        "title": "後に決まった表現が来る副詞 I (Adverb & Sentence-Ending Collocations)",
        "meaning": "Mastery of grammatical correlatives (呼応表現) where specific introductory adverbs strictly dictate sentence-final grammatical modalities: negation (めったに/決して〜ない), simile (まるで〜ようだ), imminent aspect (今にも〜そうだ), concession (たとえ〜ても), inference (どうやら〜らしい), doubt (果たして〜だろうか), and exception (必ずしも〜とは限らない).",
        "formation": "①【低頻度】めったに ＋ 否定（〜ない）\n②【切迫様態】今にも ＋ 〜そうだ\n③【比況】まるで ＋ 〜ようだ・みたいだ\n④【断固否定】決して ＋ 否定（〜ない・破らない）\n⑤【段階推移】次第に ＋ 変化動詞・〜ていく／てくる\n⑥【危機仮定】万一（万が一） ＋ 〜たら・ば・なら・場合\n⑦【上限見積】せいぜい ＋ 数量・〜くらいだ\n⑧【仮定譲歩】たとえ ＋ 〜ても・でも\n⑨【兆候推量】どうやら ＋ 〜らしい・ようだ・そうだ\n⑩【懐疑疑問】果たして ＋ 〜だろうか・か\n⑪【部分否定】必ずしも ＋ 〜とは限らない・わけではない\n⑫【驚愕不信】まさか ＋ 〜ないだろう・とは思わなかった",
        "explanation": "【教科書規則と本質的機能 (SKM N3 pp. 92-93)】\n1. 呼応表現の重要性:\n   - 日本語の文法では、文頭・文中の特定の副詞が、文末の述語形式（肯定・否定・様態・推量・比喩・疑問）をあらかじめ強く拘束・決定します。\n2. 各副詞の排他的な文法制約:\n   - 「今にも」は直前の切迫様態（〜そうだ）専用であり、過去形（*今にも雨が降った）には接続できません。\n   - 「めったに」「決して」は否定形としか呼応できません（*めったに休む、*決して守る は非文）。\n   - 「必ずしも」は全否定ではなく部分否定（〜とは限らない、〜わけではない）と排他的に呼応します。\n   - 「たとえ」は譲歩助詞「〜ても／でも」を文末に要求します。",
        "examples": [
            {
                "japanese": "社長は仕事熱心で、週末でもめったに休むことはない。",
                "english": "The company president is so devoted to work that he rarely if ever takes a day off, even on weekends.",
                "nuance": "めったに...ない: Strict collocation denoting extreme rarity."
            },
            {
                "japanese": "空が急に真っ暗になり、黒い雲から今にも大雨が降り出しそうだ。",
                "english": "The sky suddenly turned pitch black, and it looks like heavy rain will pour down from the dark clouds at any moment.",
                "nuance": "今にも...そうだ: Imminent aspect on the verge of precipitating."
            },
            {
                "japanese": "新雪に覆われた冬の山は、まるで巨大な白い城のようだ。",
                "english": "The winter mountain covered in fresh snow looks just like a gigantic white castle.",
                "nuance": "まるで...ようだ: Vivid metaphorical simile."
            },
            {
                "japanese": "前例のないこの経済対策で、果たして景気は回復するだろうか。",
                "english": "With this unprecedented economic measure, will the economy really / truly recover?",
                "nuance": "果たして...だろうか: Skeptical doubt querying actual feasibility."
            },
            {
                "japanese": "値段が非常に高い商品が、必ずしも頑丈で長持ちするとは限らない。",
                "english": "Extremely expensive products are not necessarily durable and long-lasting.",
                "nuance": "必ずしも...とは限らない: Partial negation debunking universality."
            }
        ]
    }
}

for c in base_cards:
    if c["id"] in card_enrichments:
        data = card_enrichments[c["id"]]
        c["title"] = data["title"]
        c["meaning"] = data["meaning"]
        c["formula"] = data["formation"]
        c["explanation"] = data["explanation"]
        c["examples"] = data["examples"]

BASE_PATH.write_text(json.dumps(base_cards, ensure_ascii=False, indent=2), encoding="utf-8")
print("Enriched Form Review I card in base-reviewed.json!")

# 3. Update source-coverage-matrix.json
matrix = json.load(open(MATRIX_PATH, encoding="utf-8"))

fi_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Form review I",
        "exactPrintedPages": "pp. 92-93",
        "exactPdfPages": "pp. 115-116",
        "grammarItem": "後に決まった表現が来る副詞 I (Adverb & Sentence-Ending Collocations)",
        "instructionalDetails": "Comprehensive systematization of modal correlatives (呼応表現): negative triggers (めったに/決して), metaphorical similes (まるで〜ようだ), imminent aspect (今にも〜そうだ), emergency conditionals (万一), upper bound limits (せいぜい), concessive hypothesis (たとえ〜ても), inference (どうやら), skeptical questions (果たして〜だろうか), and partial negation (必ずしも〜とは限らない).",
        "cardId": "added-n3-i-67",
        "exampleCount": 5,
        "exampleIds": [
            "added-n3-i-67::s-skm3-fi-1",
            "added-n3-i-67::s-skm3-fi-2",
            "added-n3-i-67::s-skm3-fi-3",
            "added-n3-i-67::s-skm3-fi-4",
            "added-n3-i-67::s-skm3-fi-5"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 92-93 (PDF pp. 115-116). Verified all 12 correlative modal pairs linking introductory adverbs to governed predicate inflections."
    }
]

existing_card_ids = {e.get("cardId") for e in fi_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(fi_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Form Review I in source coverage matrix! Total certified rows: {len(matrix)}")
