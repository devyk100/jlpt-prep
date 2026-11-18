import json

NEW_EXERCISES = [
    {
        "id": "skm2-c20-ex-shidai",
        "bookId": "skm-n2",
        "chapter": "Part 1 · Chapter 20",
        "type": "multiple-choice",
        "context": "医療現場での医師からの説明文",
        "question": "明日の精密検査の（　）、緊急手術を実施するかどうかを判断することになります。",
        "translation": "Depending on the results of tomorrow's detailed examination, we will judge whether or not to perform emergency surgery.",
        "options": [
            "結果次第では",
            "結果最中に",
            "結果きりで",
            "結果ずじまいで"
        ],
        "correctIndex": 0,
        "grammarPointId": "skm2-c20-shidai-de-wa",
        "grammarPointTitle": "〜次第では / 〜次第だ (Contingency: Depending on Circumstances)",
        "explanation": {
            "overall": "「名詞＋次第では」は『名詞の条件・状況によって、ある重大な結果や判断が左右される（〜によっては）』という条件随伴・偶発的可能性を表します。検査結果という条件に応じて手術の要否という判断が変わる文脈に完全に合致します。",
            "options": [
                {
                    "text": "結果次第では",
                    "isCorrect": True,
                    "reason": "「結果次第では」は『検査の結果によって、手術をするかどうかが決まる』という条件随伴を表し、後続の「判断することになります」に自然に結びつきます。"
                },
                {
                    "text": "結果最中に",
                    "isCorrect": False,
                    "reason": "「最中に」は動作や事態が最高潮に進行している瞬間（〜しているまさにその時）を表す表現であり、検査の結果という静的な条件判断の基準を表すことはできません。"
                },
                {
                    "text": "結果きりで",
                    "isCorrect": False,
                    "reason": "「〜きり」は『〜したまま後続の事態が継続している・〜だけ』を表す限定・継続表現であり、検査結果に依存して判断を下すという文脈には適しません。"
                },
                {
                    "text": "結果ずじまいで",
                    "isCorrect": False,
                    "reason": "「〜ずじまい」は『〜しないまま終わってしまった』という遺憾な未完了を表す表現であり、これからの判断基準を提示する文脈では文法的に破綻します。"
                }
            ]
        },
        "hint": "名詞に接続し、「〜の条件や結果によって決まる」という意味を表す表現を選びましょう。",
        "provenance": "original",
        "sourceEvidence": "Original diagnostic exercise authored to test contingency syntax (名詞＋次第では) patterned after Shin Kanzen Master N2 Chapter 20."
    },
    {
        "id": "skm2-c15-ex-kuse",
        "bookId": "skm-n2",
        "chapter": "Part 1 · Chapter 15",
        "type": "multiple-choice",
        "context": "同僚についての不満を述べる会話",
        "question": "彼は自分では何一つ仕事を（　）、いつも他人のミスの揚げ足ばかり取っている。",
        "translation": "Even though he doesn't do a single bit of work himself, he's always nitpicking others' mistakes.",
        "options": [
            "しないくせに",
            "しないものの",
            "しないことには",
            "しないばかりか"
        ],
        "correctIndex": 0,
        "grammarPointId": "skm2-c15-kuse-ni",
        "grammarPointTitle": "〜くせに (Critical Concession: Despite Being X, Blameworthy Y)",
        "explanation": {
            "overall": "「普通形＋くせに」は、主語が同一人物で、その立場や現状に反する不都合・非難すべき行為を行っていることに対して、話し手が強い不満・非難・軽蔑の感情を込めて述べる逆接表現です。自分は仕事をしないのに他人の批判ばかりするという非難の文脈に最も自然に合致します。",
            "options": [
                {
                    "text": "しないくせに",
                    "isCorrect": True,
                    "reason": "「しないくせに」は『自分では仕事をしないという立場に反して、不当にも他人の批判をする』という強い非難・不満を表し、文脈の批判的トーンに完璧に適合します。"
                },
                {
                    "text": "しないものの",
                    "isCorrect": False,
                    "reason": "「〜ものの」は客観的・確定的な事実を前置きとして認める文語的逆接であり、話し手の主観的な強い非難や軽蔑のニュアンスを含みません。"
                },
                {
                    "text": "しないことには",
                    "isCorrect": False,
                    "reason": "「〜ないことには（〜ない）」は『〜しなければ、…できない』という必須前提条件を表す表現であり、ここでは逆接の非難を述べる文脈であるため不適当です。"
                },
                {
                    "text": "しないばかりか",
                    "isCorrect": False,
                    "reason": "「〜ばかりか」は『〜だけでなく、さらにそれ以上のことも…』という累加を表す表現であり、前後の対立的な矛盾・非難の関係を正しく表せません。"
                }
            ]
        },
        "hint": "主語に対する不満や非難の気持ちを込めて「〜という立場・事実があるのに」と逆接でつなぐ表現を選びましょう。",
        "provenance": "original",
        "sourceEvidence": "Original diagnostic exercise authored to test critical concession (くせに) patterned after Shin Kanzen Master N2 Chapter 15."
    },
    {
        "id": "skm2-c17-ex-koto",
        "bookId": "skm-n2",
        "chapter": "Part 1 · Chapter 17",
        "type": "multiple-choice",
        "context": "地名の由来を説明する地理の解説文",
        "question": "この島は上空から見ると鳥が翼を広げた形に（　）、「鳥島」と名付けられたと言われている。",
        "translation": "Because this island resembles the shape of a bird spreading its wings when viewed from the sky, it is said to have been named 'Torishima'.",
        "options": [
            "似ていることから",
            "似ているものだから",
            "似ているからといって",
            "似ているだけに"
        ],
        "correctIndex": 0,
        "grammarPointId": "skm2-c17-koto-kara",
        "grammarPointTitle": "〜ことから (Origin & Grounds: Arising from the Fact That)",
        "explanation": {
            "overall": "「普通形＋ことから」は、名付けの由来、判断の客観的根拠、またはある事実が判明したきっかけを客観的に説明する表現です。「〜と名付けられた」「〜と呼ばれている」「〜ことが分かる」などの述語と典型的に呼応します。",
            "options": [
                {
                    "text": "似ていることから",
                    "isCorrect": True,
                    "reason": "「似ていることから」は『鳥の形に似ているという客観的な事実を根拠・由来として名付けられた』という命名の由来を自然に表し、「名付けられた」と正確に呼応します。"
                },
                {
                    "text": "似ているものだから",
                    "isCorrect": False,
                    "reason": "「〜ものだから」は個人的な言い訳や不可抗力の事情を話し言葉で説明する表現であり、地名の客観的な由来を解説する文体には適しません。"
                },
                {
                    "text": "似ているからといって",
                    "isCorrect": False,
                    "reason": "「〜からといって」は『〜という理由があるからといって（必ずしも…とは言えない）』という部分否定や制約を導く表現であり、命名の事実を述べる文脈に合いません。"
                },
                {
                    "text": "似ているだけに",
                    "isCorrect": False,
                    "reason": "「〜だけに」は『〜という理由があるから、なおさら・いっそう…だ』という比例的強調を表す表現であり、命名の由来の因果関係を示す表現としては不自然です。"
                }
            ]
        },
        "hint": "地名の由来や命名の理由を客観的に説明し、「〜と名付けられた」と呼応する表現を選びましょう。",
        "provenance": "original",
        "sourceEvidence": "Original diagnostic exercise authored to test causal origin syntax (ことから) patterned after Shin Kanzen Master N2 Chapter 17."
    },
    {
        "id": "skm2-c17-ex-wake",
        "bookId": "skm-n2",
        "chapter": "Part 1 · Chapter 17",
        "type": "multiple-choice",
        "context": "語学学習に関する現実的なアドバイス",
        "question": "海外に長期間住んでいれば、誰もが自然に外国語が流暢に話せるようになる（　）。",
        "translation": "Living abroad for a long time does not necessarily mean that anyone will naturally become fluent in a foreign language.",
        "options": [
            "というわけではない",
            "わけにはいかない",
            "どころではない",
            "に相違ない"
        ],
        "correctIndex": 0,
        "grammarPointId": "skm2-c17-wake-de-wa-nai",
        "grammarPointTitle": "〜わけではない / 〜というわけではない (Partial Negation: Not Necessarily So)",
        "explanation": {
            "overall": "「普通形＋というわけではない／わけではない」は、『一見そう思われがちだが、必ずしも全員・すべてがそうであるとは限らない』という部分否定を表します。「海外に住めば誰でも話せるようになる」という短絡的な一般論を否定する文脈に正確に適合します。",
            "options": [
                {
                    "text": "というわけではない",
                    "isCorrect": True,
                    "reason": "「というわけではない」は『海外に住んでいれば誰もが自然に話せるようになる、というわけではない（例外や個人の努力が必要だ）』という部分否定を自然に成立させます。"
                },
                {
                    "text": "わけにはいかない",
                    "isCorrect": False,
                    "reason": "「〜わけにはいかない」は社会的義務や心理的抵抗によって『〜するわけにはいかない（行動できない）』ことを表す表現であり、一般的な事実の可否の判断には使えません。"
                },
                {
                    "text": "どころではない",
                    "isCorrect": False,
                    "reason": "「〜どころではない」は『状況が切迫していて、とても〜できる状態ではない』という極度の困難を表す表現であり、部分否定の文脈には適合しません。"
                },
                {
                    "text": "に相違ない",
                    "isCorrect": False,
                    "reason": "「〜に相違ない」は『絶対に〜に違いない』という強い確信・断定を表す表現であり、一般的な思い込みを否定する文意とは正反対になってしまいます。"
                }
            ]
        },
        "hint": "「一般的にはそう思われがちだが、必ずしもそうとは言えない」という部分否定の表現を選びましょう。",
        "provenance": "original",
        "sourceEvidence": "Original diagnostic exercise authored to test partial negation syntax (というわけではない) patterned after Shin Kanzen Master N2 Chapter 17."
    },
    {
        "id": "skm2-c14-ex-hanmen",
        "bookId": "skm-n2",
        "chapter": "Part 1 · Chapter 14",
        "type": "multiple-choice",
        "context": "最新のAI技術の導入に関する論説文",
        "question": "人工知能の導入は業務効率を劇的に向上させる（　）、雇用の喪失という深刻な課題ももたらしている。",
        "translation": "While the introduction of artificial intelligence dramatically improves operational efficiency, on the flip side, it also brings the serious challenge of job losses.",
        "options": [
            "反面",
            "わりに",
            "反して",
            "末に"
        ],
        "correctIndex": 0,
        "grammarPointId": "skm2-c14-hanmen",
        "grammarPointTitle": "〜反面 (On the Flip Side: Coexisting Duality in the Same Entity)",
        "explanation": {
            "overall": "「普通形＋反面」は、同一の事象や対象（ここではAIの導入）が持つ、互いに相反する二つの側面（メリットである効率向上と、デメリットである雇用喪失）を対比させて並べる表現です。",
            "options": [
                {
                    "text": "反面",
                    "isCorrect": True,
                    "reason": "「反面」は『AI導入という同一の事象について、効率向上という利点がある一方で、雇用喪失という課題も同時に存在する』という両面性を鮮やかに表現します。"
                },
                {
                    "text": "わりに",
                    "isCorrect": False,
                    "reason": "「〜わりに」は基準から予想される事態と実際の結果のズレ（値段のわりに美味しい等）を表す表現であり、同一事象の相反する両面を対置する文脈には適しません。"
                },
                {
                    "text": "反して",
                    "isCorrect": False,
                    "reason": "「〜に反して」の形で『予想や規則に逆らって』を表す表現であり、「動詞辞書形＋反して」という直接接続は非文です。"
                },
                {
                    "text": "末に",
                    "isCorrect": False,
                    "reason": "「〜末に」は『長い苦労や議論の最後に、最終的な結果が出た』という時間的推移・結果を表す表現であり、二面性の対比には使えません。"
                }
            ]
        },
        "hint": "同一の対象が持つ「良い面がある一方で、悪い面もある」という両面性を表す接続を選びましょう。",
        "provenance": "original",
        "sourceEvidence": "Original diagnostic exercise authored to test coexisting duality syntax (反面) patterned after Shin Kanzen Master N2 Chapter 14."
    }
]

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    exercises = json.load(f)

existing_eids = {e["id"] for e in exercises}
added = 0
for ex in NEW_EXERCISES:
    if ex["id"] not in existing_eids:
        exercises.append(ex)
        added += 1
    else:
        for i, e in enumerate(exercises):
            if e["id"] == ex["id"]:
                exercises[i] = ex

with open("jlpt-exam-prep/src/data/chapterExercises.json", "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print(f"Added/updated {len(NEW_EXERCISES)} dedicated diagnostic exercises in chapterExercises.json (new: {added})")
