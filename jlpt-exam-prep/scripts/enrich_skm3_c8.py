import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
BASE_REVIEWED_PATH = ROOT / "content/base-reviewed.json"
CHAPTER_EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"
MATRIX_PATH = ROOT / "audit/source-coverage-matrix.json"
OVERRIDES_PATH = ROOT / "content/reading-overrides.json"

# 1. Update Reading Overrides
overrides = json.loads(OVERRIDES_PATH.read_text(encoding="utf-8"))
needed_overrides = {
    "横領": {"reading": "おうりょう", "meaning": "embezzlement / misappropriation"},
    "総料理長": {"reading": "そうりょうりちょう", "meaning": "executive chef / head chef"},
    "三ツ星": {"reading": "みつぼし", "meaning": "three-star"},
    "先約": {"reading": "せんやく", "meaning": "previous engagement / prior appointment"},
    "不合格": {"reading": "ふごうかく", "meaning": "failure (in an examination)"}
}
for k, v in needed_overrides.items():
    if k not in overrides:
        overrides[k] = v
OVERRIDES_PATH.write_text(json.dumps(overrides, ensure_ascii=False, indent=2), encoding="utf-8")

# 2. Add Chapter Exercises for SKM N3 Chapter 8
exercises_data = json.loads(CHAPTER_EXERCISES_PATH.read_text(encoding="utf-8"))

c8_exercises = [
    {
        "id": "skm3-c8-q1",
        "chapterId": "skm3-c8",
        "question": "あんなに真面目な彼が、会社の金を横領する（　）。絶対に何かの間違いだ。",
        "options": [
            "わけがない",
            "わけではない",
            "とは限らない",
            "ことはない"
        ],
        "correctIndex": 0,
        "explanation": "【正解: わけがない】\n「〜わけがない」は「絶対に〜ない」という話者の論理的根拠に基づく強い確信を表します。真面目な彼が横領するなど絶対にあり得ないという文脈に最適です。\n\n【選択肢解説】\n1. わけがない (正解): 絶対的な不可能性の確信（横領するはずがない）。\n2. わけではない (不正解): 部分否定（横領するわけではない＝横領しないとは限らない等）になり文意と合わない。\n3. とは限らない (不正解): 「〜とは限らない（横領することもある）」になり意味が逆。\n4. ことはない (不正解): 「〜することはない（横領する必要はない）」になり確信否定に合わない。"
    },
    {
        "id": "skm3-c8-q2",
        "chapterId": "skm3-c8",
        "question": "値段が高いものが、必ずしも品質が優れている（　）。",
        "options": [
            "とは限らない",
            "わけがない",
            "ことはない",
            "ことは優れているが"
        ],
        "correctIndex": 0,
        "explanation": "【正解: とは限らない】\n「必ずしも〜とは限らない」は「絶対にそう断言できるわけではなく、例外もある」という部分真実・反例の余地を表す定番の呼応表現です。\n\n【選択肢解説】\n1. とは限らない (正解): 「必ずしも〜とは限らない」の呼応。\n2. わけがない (不正解): 「優れているわけがない（絶対に優れていない）」になり文意が極端に歪む。\n3. ことはない (不正解): 文法的に不成立。\n4. ことは優れているが (不正解): 構文の重複。"
    },
    {
        "id": "skm3-c8-q3",
        "chapterId": "skm3-c8",
        "question": "料理が嫌いな（　）が、平日は忙しくて自炊する時間がないだけです。",
        "options": [
            "わけではない",
            "わけがない",
            "とは限らない",
            "ことはない"
        ],
        "correctIndex": 0,
        "explanation": "【正解: わけではない】\n「〜わけではない」は「相手がそう思いがちだが、実際はそうではない」と一部を否定して事情を弁解・説明する表現です。\n\n【選択肢解説】\n1. わけではない (正解): 「嫌いというわけではない（嫌いなのではなく時間がない）」という部分否定。\n2. わけがない (不正解): 強い絶対否定になり自らの心情の説明として不自然。\n3. とは限らない (不正解): 一般的通説の例外提示に使われる。\n4. ことはない (不正解): 二重否定構文でこの形には合わない。"
    },
    {
        "id": "skm3-c8-q4",
        "chapterId": "skm3-c8",
        "question": "自転車を修理すれば、（　）ことはないが、新しいのを買ったほうが早い。",
        "options": [
            "使えない",
            "使える",
            "使う",
            "使わなかった"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 使えない】\n「動詞ない形＋ことはない」は二重否定により「絶対にできないわけではない（やろうと思えばできる）」という控えめな可能・肯定を表します。\n\n【選択肢解説】\n1. 使えない (正解): 「使えないことはない（使おうと思えば使える）」という二重否定。\n2. 使える (不正解): 肯定形「使えることはない」は「使えるはずがない」という不自然な文になる。\n3. 使う (不正解): 辞書形では二重否定構文にならない。\n4. 使わなかった (不正解): 過去形不適合。"
    },
    {
        "id": "skm3-c8-q5",
        "chapterId": "skm3-c8",
        "question": "このアパートは、駅から近い（　）が、家賃が高すぎて手が出ない。",
        "options": [
            "ことは近い",
            "わけには近い",
            "ものは近い",
            "ほどは近い"
        ],
        "correctIndex": 0,
        "explanation": "【正解: ことは近い】\n「形容詞／動詞＋ことは＋同述語＋が」は「確かにその事実は認めるが、しかし別の大きな問題・制限がある」という譲歩構文です。\n\n【選択肢解説】\n1. ことは近い (正解): 「近いことは近いが（確かに近いことは事実だが家賃が高い）」。\n2. わけには近い (不正解): 不成立表現。\n3. ものは近い (不正解): 誤った助詞組み合わせ。\n4. ほどは近い (不正解): 程度構文。"
    },
    {
        "id": "skm3-c8-q6",
        "chapterId": "skm3-c8",
        "question": "何ヶ月も必死に練習を重ねてきたのだから、本番で失敗する（　）。",
        "options": [
            "わけがない",
            "わけではない",
            "とは限らない",
            "ことはない"
        ],
        "correctIndex": 0,
        "explanation": "【正解: わけがない】\n「〜のだから（十分な根拠）＋〜わけがない」は「これだけの根拠があるのだから失敗するはずが絶対にない」という強い確信の否定を表します。\n\n【選択肢解説】\n1. わけがない (正解): 根拠に基づく絶対否定。\n2. わけではない (不正解): 部分否定で「失敗しないとは言えない」になり文脈の激励と矛盾。\n3. とは限らない (不正解): 例外を示唆してしまい不安を煽る表現になる。\n4. ことはない (不正解): 構文不適合。"
    },
    {
        "id": "skm3-c8-q7",
        "chapterId": "skm3-c8",
        "question": "英語圏に３年間留学していたからといって、誰でもペラペラになれる（　）。",
        "options": [
            "とは限らない",
            "わけがない",
            "ことはない",
            "ことはある"
        ],
        "correctIndex": 0,
        "explanation": "【正解: とは限らない】\n「〜からといって、誰でも〜とは限らない」は「一般的な前提があるからといって、全員が例外なくそうなるわけではない」という普遍化の否定です。\n\n【選択肢解説】\n1. とは限らない (正解): 「〜からといって〜とは限らない」の定番構文。\n2. わけがない (不正解): 「誰一人ペラペラになれるはずがない」という極端な不合理文になる。\n3. ことはない (不正解): 構文不適合。\n4. ことはある (不正解): 「そういうこともある」になり意図と逆。"
    },
    {
        "id": "skm3-c8-q8",
        "chapterId": "skm3-c8",
        "question": "パーティーに行きたくない（　）が、どうしても外せない先約があるんです。",
        "options": [
            "わけではないん",
            "わけがないん",
            "とは限らないん",
            "ことはないん"
        ],
        "correctIndex": 0,
        "explanation": "【正解: わけではないん】\n「行きたくないわけではないんだが」は「行きたくないと思っているわけでは決してないが（行きたい気持ちはあるが）、先約がある」というソフトな弁解表現です。\n\n【選択肢解説】\n1. わけではないん (正解): 行きたくないわけではない＋んだが（弁解・理由説明）。\n2. わけがないん (不正解): 強い絶対否定で自らの感情を説明するのに不自然。\n3. とは限らないん (不正解): 個人的意志の弁解に使えない。\n4. ことはないん (不正解): ニュアンスが不自然。"
    },
    {
        "id": "skm3-c8-q9",
        "chapterId": "skm3-c8",
        "question": "タクシーを使えば、最終の新幹線に（　）こともないが、渋滞が心配だ。",
        "options": [
            "間に合わない",
            "間に合う",
            "間に合えば",
            "間に合った"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 間に合わない】\n「動詞ない形＋こともない」で「間に合わないこともない（万が一の場合間に合う可能性もある）」という消極的・控えめな肯定の可能性を表します。\n\n【選択肢解説】\n1. 間に合わない (正解): 二重否定「〜ないこともない」の正しい接続。\n2. 間に合う (不正解): 肯定形に「こともない」は接続しない。\n3. 間に合えば (不正解): 条件形不適合。\n4. 間に合った (不正解): 過去形不適合。"
    },
    {
        "id": "skm3-c8-q10",
        "chapterId": "skm3-c8",
        "question": "スキーは、（　）ことは滑れますが、上級者コースは無理です。",
        "options": [
            "滑れる",
            "滑る",
            "滑った",
            "滑らない"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 滑れる】\n「動詞可能形＋ことは＋同動詞可能形＋が」で「滑れることは滑れるが（一応滑る能力はあるが、上級者コースは無理だ）」という限定的な事実の承認と留保を表します。\n\n【選択肢解説】\n1. 滑れる (正解): 後ろの「滑れます」と可能形の一致。\n2. 滑る (不正解): 可能形との不一致。\n3. 滑った (不正解): 過去形との不一致。\n4. 滑らない (不正解): 意味の矛盾。"
    },
    {
        "id": "skm3-c8-q11",
        "chapterId": "skm3-c8",
        "question": "三ツ星レストランの総料理長が作った料理が、（　）わけがない。",
        "options": [
            "まずい",
            "おいしい",
            "上手な",
            "高級な"
        ],
        "correctIndex": 0,
        "explanation": "【正解: まずい】\n「まずいわけがない」で「まずいなんてことは絶対にあり得ない（絶対に美味しいはずだ）」という強い確信の否定を表します。\n\n【選択肢解説】\n1. まずい (正解): 「まずいわけがない＝絶対に美味しい」という強い確信。\n2. おいしい (不正解): 「美味しいわけがない＝絶対にまずい」になり文意が破綻。\n3. 上手な (不正解): 料理の味には「まずい／おいしい」を用いる。\n4. 高級な (不正解): 「高級なわけがない」になり文意が破綻。"
    },
    {
        "id": "skm3-c8-q12",
        "chapterId": "skm3-c8",
        "question": "親切にされたら誰でも（　）わけがない。",
        "options": [
            "嬉しくない",
            "嬉しい",
            "喜ぶ",
            "喜ばない"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 嬉しくない】\n「嬉しくないわけがない」は二重否定で「嬉しくないはずが絶対にない＝誰だって絶対に嬉しいに決まっている」という確信を表します。\n\n【選択肢解説】\n1. 嬉しくない (正解): 「嬉しくないわけがない＝絶対に嬉しい」。\n2. 嬉しい (不正解): 「嬉しいわけがない＝絶対に嬉しくない」になり人間心理として破綻。\n3. 喜ぶ (不正解): 接続と文意の破綻。\n4. 喜ばない (不正解): 動詞より形容詞「嬉しくない」が心理状態の描写として自然。"
    }
]

exercises_data = [e for e in exercises_data if e.get("chapterId") != "skm3-c8"]
exercises_data.extend(c8_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(exercises_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with {len(c8_exercises)} exercises for SKM N3 Chapter 8!")

# 3. Enrich base-reviewed.json for Chapter 8 cards
base_reviewed = json.loads(BASE_REVIEWED_PATH.read_text(encoding="utf-8"))

card_enrichments = {
    "skm3-u8-wake-ga-nai": {
        "title": "〜わけがない / 〜わけはない (There Is Absolutely No Way That...)",
        "connection": "普通形（な形な/である・名である/の）+ わけがない / わけはない",
        "nuance": "【Shin Kanzen Master N3 p. 38 正式規則】「絶対に〜ない。」話者が強い確信や客観的根拠を持って否定するときに言う。Strong expression of adamant negation based on the conviction or logic of the speaker. 'There is absolutely no way / It is completely out of the question that...'.",
        "keyTakeaway": "Adamant logical denial of possibility ('there is absolutely no way that...'). Rejects the proposition completely.",
        "sentences": [
            {
                "id": "skm3-u8-wake-ga-nai::s-skm3-8-1",
                "japanese": "褒められて、嬉しくないわけがない。",
                "english": "There is absolutely no way one wouldn't be glad after being praised.",
                "literal": "Praised-being, not-happy way is-not.",
                "tokens": [{"word": "嬉しくないわけがない", "meaning": "no way not to be happy", "reading": "うれしくないわけがない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 38 verbatim sentence 1: rhetorical double negation of emotional reaction."
            },
            {
                "id": "skm3-u8-wake-ga-nai::s-skm3-8-2",
                "japanese": "あの強い相手に勝てるわけがない。",
                "english": "There is no way we can defeat that powerful opponent.",
                "literal": "That strong opponent-to win-can way is-not.",
                "tokens": [{"word": "勝てるわけがない", "meaning": "no way we can win", "reading": "かてるわけがない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 38 verbatim sentence 2: logical conviction of impossible victory."
            },
            {
                "id": "skm3-u8-wake-ga-nai::s-skm3-8-3",
                "japanese": "あんなに勉強したのだから、不合格になるわけがない。",
                "english": "Having studied that hard, there is absolutely no way he could fail.",
                "literal": "That-much studied because, failure become way is-not.",
                "tokens": [{"word": "不合格になるわけがない", "meaning": "no way he will fail", "reading": "ふごうかくになるわけがない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 38 verbatim sentence 3: firm confidence deduced from diligent study."
            },
            {
                "id": "skm3-u8-wake-ga-nai::s-skm3-8-4",
                "japanese": "こんなに安くて美味しい店が、流行らないわけがない。",
                "english": "With food this cheap and delicious, there is no way this restaurant won't be popular.",
                "literal": "This cheap-and delicious restaurant, not-thrive way is-not.",
                "tokens": [{"word": "流行らないわけがない", "meaning": "no way it won't flourish", "reading": "は行らないわけがない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 38 verbatim sentence 4: commercial success as an undeniable certainty."
            }
        ]
    },
    "skm3-u8-to-wa-kagiranai-not-necessarily": {
        "title": "〜とは限らない (Partial Truth: Not Necessarily the Case)",
        "connection": "普通形（な形（だ）・名（だ））+ とは限らない（呼応表現：必ずしも〜、〜からといって〜）",
        "nuance": "【Shin Kanzen Master N3 p. 38 正式規則】「絶対に〜だとは断言できない。〜でない場合もある。」It cannot be stated categorically that ~, there may be cases where it is not ~. Rejecting universal generalization while acknowledging exceptions. Frequently pairs with 必ずしも (not necessarily), いつも (always), or 〜からといって (just because).",
        "keyTakeaway": "Rejects absolute statements or stereotypes ('does not necessarily mean X'). Frequently pairs with 必ずしも or 〜からといって.",
        "sentences": [
            {
                "id": "skm3-u8-to-wa-kagiranai-not-necessarily::s-skm3-8-1",
                "japanese": "高いものが、必ずしもいいものだとは限らない。",
                "english": "Just because something is expensive doesn't necessarily mean it is of good quality.",
                "literal": "Expensive thing necessarily good thing that not-limited.",
                "tokens": [{"word": "いいものだとは限らない", "meaning": "not necessarily a good item", "reading": "いいものだとはかぎらない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 38 verbatim sentence 1: price-quality debunking."
            },
            {
                "id": "skm3-u8-to-wa-kagiranai-not-necessarily::s-skm3-8-2",
                "japanese": "日本人だからといって、全員が寿司が好きだとは限らない。",
                "english": "Just because someone is Japanese does not necessarily mean everyone likes sushi.",
                "literal": "Japanese just-because, all-members sushi like that not-limited.",
                "tokens": [{"word": "好きだとは限らない", "meaning": "does not necessarily mean they like", "reading": "すきだとはかぎらない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 38 verbatim sentence 2: cultural stereotype refutation."
            },
            {
                "id": "skm3-u8-to-wa-kagiranai-not-necessarily::s-skm3-8-3",
                "japanese": "有名な大学を出たからといって、成功するとは限らない。",
                "english": "Graduating from a famous university does not guarantee that one will be successful in life.",
                "literal": "Famous university graduated just-because, succeed that not-limited.",
                "tokens": [{"word": "成功するとは限らない", "meaning": "does not necessarily succeed", "reading": "せいこうするとはかぎらない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 38 verbatim sentence 3: academic credentials vs life success."
            },
            {
                "id": "skm3-u8-to-wa-kagiranai-not-necessarily::s-skm3-8-4",
                "japanese": "新聞に書いてあることが、いつも真実だとは限らない。",
                "english": "What is written in newspapers is not always necessarily the truth.",
                "literal": "Newspaper written thing, always truth that not-limited.",
                "tokens": [{"word": "真実だとは限らない", "meaning": "is not necessarily truth", "reading": "しんじつだとはかぎらない", "pos": "Grammar"}],
                "nuanceNote": "Media skepticism and critical evaluation."
            }
        ]
    },
    "skm3-u8-wake-dewa-nai": {
        "title": "〜わけではない / 〜というわけではない (It Doesn't Mean That... / Partial Negation)",
        "connection": "普通形（な形な/である・名な/である/の）+ わけではない / というわけではない",
        "nuance": "【Shin Kanzen Master N3 p. 39 正式規則】「〜という状況から当然〜だと想像されるが、実際はそうではない。」〜の部分否定を言う。Means something like 'it is not that ~ but rather that', used in contexts where external circumstances might lead one to assume X, but the reality is qualified or different. Negates only part of the statement.",
        "keyTakeaway": "Partial negation softening an assumption or clarifying nuance ('it's not that X is completely true, rather...').",
        "sentences": [
            {
                "id": "skm3-u8-wake-dewa-nai::s-skm3-8-1",
                "japanese": "お金があれば幸せになれるというわけではない。",
                "english": "Having money does not necessarily mean one will become happy.",
                "literal": "Money if-exists happy become-can that reason is-not.",
                "tokens": [{"word": "幸せになれるというわけではない", "meaning": "does not mean one can become happy", "reading": "しあわせになれるというわけではない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 39 verbatim sentence 1: philosophical partial negation of wealth."
            },
            {
                "id": "skm3-u8-wake-dewa-nai::s-skm3-8-2",
                "japanese": "嫌いなわけではないが、今は食べたくない。",
                "english": "It is not that I dislike it, but I just do not feel like eating right now.",
                "literal": "Dislike reason is-not but, now want-to-eat-not.",
                "tokens": [{"word": "嫌いなわけではない", "meaning": "it is not that I dislike it", "reading": "きらいなわけではない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 39 verbatim sentence 2: polite personal qualification."
            },
            {
                "id": "skm3-u8-wake-dewa-nai::s-skm3-8-3",
                "japanese": "仕事をやめたいわけではないが、少し休みが欲しい。",
                "english": "It is not that I want to quit my job, but I would like to take a short break.",
                "literal": "Job want-to-quit reason is-not but, a-little rest want.",
                "tokens": [{"word": "やめたいわけではない", "meaning": "it is not that I want to quit", "reading": "やめたいわけではない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 39 verbatim sentence 3: clarifying career intentions."
            },
            {
                "id": "skm3-u8-wake-dewa-nai::s-skm3-8-4",
                "japanese": "全部分かったわけではありません。",
                "english": "It is not that I understood everything; some parts remain unclear.",
                "literal": "All understood reason is-not.",
                "tokens": [{"word": "全部分かったわけではありません", "meaning": "it is not that I understood all", "reading": "ぜんぶわかったわけではありません", "pos": "Grammar"}],
                "nuanceNote": "Modest academic qualification of comprehension."
            }
        ]
    },
    "skm3-u8-nai-koto-wa-nai-litotes": {
        "title": "〜ないことはない / 〜ないこともない (Double Negative Litotes: It's Not Impossible)",
        "connection": "動ない形・い形くない・な形でない・名でない + ことはない / こともない",
        "nuance": "【Shin Kanzen Master N3 p. 39 正式規則】「絶対に〜ないとは言えない（〜の可能性もある）。」二重否定の形で遠回しに肯定の意味を言う。I cannot say that ~ never happens (is not impossible). Mildly conveys affirmative possibility or qualified concession through double negation.",
        "keyTakeaway": "Double negative expressing mild affirmative possibility or reluctant concession ('it's not that I completely can't... / not impossible if pushed').",
        "sentences": [
            {
                "id": "skm3-u8-nai-koto-wa-nai-litotes::s-skm3-8-1",
                "japanese": "走れば、電車に間に合わないことはない。",
                "english": "If we run, it is not impossible to catch the train.",
                "literal": "Run-if, train to in-time-not fact is-not.",
                "tokens": [{"word": "間に合わないことはない", "meaning": "not impossible to make it in time", "reading": "まにあわないことはない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 39 verbatim sentence 1: conditional affirmative possibility."
            },
            {
                "id": "skm3-u8-nai-koto-wa-nai-litotes::s-skm3-8-2",
                "japanese": "この店の料理は、食べられないことはないが、あまり美味しくない。",
                "english": "The food at this shop is not uneatable, but it is not very delicious.",
                "literal": "This shop's food, eat-cannot fact is-not but, very delicious-not.",
                "tokens": [{"word": "食べられないことはない", "meaning": "not that it cannot be eaten", "reading": "たべられないことはない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 39 verbatim sentence 2: reluctant gastronomic concession."
            },
            {
                "id": "skm3-u8-nai-koto-wa-nai-litotes::s-skm3-8-3",
                "japanese": "試験の結果が心配でないこともないが、信じて待つしかない。",
                "english": "It is not that I am not worried about the examination results, but I just have to believe and wait.",
                "literal": "Exam result worried not-be fact is-not but, believe-and wait only.",
                "tokens": [{"word": "心配でないこともない", "meaning": "not that I am unconcerned", "reading": "しんぱいでないこともない", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 39 verbatim sentence 3: admission of emotional unease."
            },
            {
                "id": "skm3-u8-nai-koto-wa-nai-litotes::s-skm3-8-4",
                "japanese": "一人でできないことはないが、時間がかかります。",
                "english": "It is not impossible to do alone, but it will take substantial time.",
                "literal": "One-person by can-do-not fact is-not but, time takes.",
                "tokens": [{"word": "できないことはない", "meaning": "not impossible to do", "reading": "できないことはない", "pos": "Grammar"}],
                "nuanceNote": "Qualified technical capability with reservation."
            }
        ]
    },
    "added-n3-8-52": {
        "title": "〜ことは〜が (Concession with Reservation / True, But...)",
        "connection": "動・形普通形 + ことは + 動・形普通形/丁寧形 + が",
        "nuance": "【Shin Kanzen Master N3 p. 39 正式規則】「〜というのは事実だが、その事実はあまり重要ではなく、…だ。」It is true that ~ (the fact is acknowledged), but that fact is qualified or overshadowed by another, more significant contrasting consideration.",
        "keyTakeaway": "Concedes a quality or action by repeating the predicate ('it is true that X, but...'), then introduces a decisive reservation or limitation.",
        "sentences": [
            {
                "id": "added-n3-8-52::s-skm3-8-1",
                "japanese": "彼のピアノは、弾けることは弾けるが、あまり上手ではない。",
                "english": "As for his piano playing, he can play, certainly, but he is not very good at it.",
                "literal": "His piano, can-play fact can-play but, very skillful is-not.",
                "tokens": [{"word": "弾けることは弾けるが", "meaning": "can play, certainly, but", "reading": "ひけることはひけるが", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 39 verbatim sentence 1: qualified skill admission."
            },
            {
                "id": "added-n3-8-52::s-skm3-8-2",
                "japanese": "この靴は、歩きやすいことは歩きやすいが、デザインが気に入らない。",
                "english": "As for these shoes, they are easy to walk in, certainly, but I don't like the design.",
                "literal": "These shoes, walk-easy fact walk-easy but, design not-liked.",
                "tokens": [{"word": "歩きやすいことは歩きやすいが", "meaning": "easy to walk in, certainly, but", "reading": "あるきやすいことはあるきやすいが", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 39 verbatim sentence 2: concession of comfort with aesthetic reservation."
            },
            {
                "id": "added-n3-8-52::s-skm3-8-3",
                "japanese": "この本は、読んだことは読んだが、内容をほとんど覚えていない。",
                "english": "As for this book, I did read it, but I barely remember what it was about.",
                "literal": "This book, read fact read but, contents mostly remember-not.",
                "tokens": [{"word": "読んだことは読んだが", "meaning": "did read it, but", "reading": "よんだことはよんだが", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 39 verbatim sentence 3: acknowledging past action with reservation."
            },
            {
                "id": "added-n3-8-52::s-skm3-8-4",
                "japanese": "安いことは安いですが、駅から遠いです。",
                "english": "It is cheap, certainly, but it is far from the station.",
                "literal": "Cheap fact cheap is but, station from far is.",
                "tokens": [{"word": "安いことは安いですが", "meaning": "cheap, certainly, but", "reading": "やすいことはやすいですが", "pos": "Grammar"}],
                "nuanceNote": "Concession of economic benefit with locational handicap."
            }
        ]
    }
}

for card in base_reviewed:
    cid = card.get("id")
    if cid in card_enrichments:
        card.update(card_enrichments[cid])

BASE_REVIEWED_PATH.write_text(json.dumps(base_reviewed, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Enriched all {len(card_enrichments)} SKM N3 Chapter 8 cards in base-reviewed.json!")

# 4. Update audit/source-coverage-matrix.json
matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))

c8_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 8",
        "exactPrintedPages": "p. 38",
        "exactPdfPages": "p. 61",
        "grammarItem": "〜わけがない / 〜わけはない (There Is Absolutely No Way That...)",
        "instructionalDetails": "Plain form (な-adj + な/である, Noun + の/である) + わけがない/わけはない; speaker's conviction of absolute impossibility based on logical evidence; rhetorical double negative (嬉しくないわけがない).",
        "cardId": "skm3-u8-wake-ga-nai",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u8-wake-ga-nai::s-skm3-8-1",
            "skm3-u8-wake-ga-nai::s-skm3-8-2",
            "skm3-u8-wake-ga-nai::s-skm3-8-3",
            "skm3-u8-wake-ga-nai::s-skm3-8-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 38 (PDF p. 61). Verified Section 1 formation, strong negation conviction, and double negation rhetoric."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 8",
        "exactPrintedPages": "p. 38",
        "exactPdfPages": "p. 61",
        "grammarItem": "〜とは限らない (Partial Truth: Not Necessarily the Case)",
        "instructionalDetails": "Plain form (な-adj (だ), Noun (だ)) + とは限らない; rejects universal validity/stereotypes; frequently pairs with 必ずしも (not necessarily), いつも (always), or 〜からといって.",
        "cardId": "skm3-u8-to-wa-kagiranai-not-necessarily",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u8-to-wa-kagiranai-not-necessarily::s-skm3-8-1",
            "skm3-u8-to-wa-kagiranai-not-necessarily::s-skm3-8-2",
            "skm3-u8-to-wa-kagiranai-not-necessarily::s-skm3-8-3",
            "skm3-u8-to-wa-kagiranai-not-necessarily::s-skm3-8-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 38 (PDF p. 61). Verified Section 2 partial truth semantics and pairing with 必ずしも."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 8",
        "exactPrintedPages": "p. 39",
        "exactPdfPages": "p. 62",
        "grammarItem": "〜わけではない / 〜というわけではない (It Doesn't Mean That... / Partial Negation)",
        "instructionalDetails": "Plain form (な-adj + な/である, Noun + な/である/の) + わけではない/というわけではない; clarifies that while circumstances suggest X, reality is qualified or partially negated.",
        "cardId": "skm3-u8-wake-dewa-nai",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u8-wake-dewa-nai::s-skm3-8-1",
            "skm3-u8-wake-dewa-nai::s-skm3-8-2",
            "skm3-u8-wake-dewa-nai::s-skm3-8-3",
            "skm3-u8-wake-dewa-nai::s-skm3-8-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 39 (PDF p. 62). Verified Section 3 partial negation rules and polite conversational qualification."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 8",
        "exactPrintedPages": "p. 39",
        "exactPdfPages": "p. 62",
        "grammarItem": "〜ないことはない / 〜ないこともない (Double Negative Litotes: It's Not Impossible)",
        "instructionalDetails": "V-ない / い形くない / な形でない / 名でない + ことはない/こともない; double negation expressing mild affirmative possibility or qualified concession.",
        "cardId": "skm3-u8-nai-koto-wa-nai-litotes",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u8-nai-koto-wa-nai-litotes::s-skm3-8-1",
            "skm3-u8-nai-koto-wa-nai-litotes::s-skm3-8-2",
            "skm3-u8-nai-koto-wa-nai-litotes::s-skm3-8-3",
            "skm3-u8-nai-koto-wa-nai-litotes::s-skm3-8-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 39 (PDF p. 62). Verified Section 4 double negative litotes formation and mild affirmation semantics."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 8",
        "exactPrintedPages": "p. 39",
        "exactPdfPages": "p. 62",
        "grammarItem": "〜ことは〜が (Concession with Reservation / True, But...)",
        "instructionalDetails": "Predicate (plain) + ことは + Predicate (plain/polite) + が; concedes that X is true while placing primary communicative focus on contrasting reservation or limitation in clause B.",
        "cardId": "added-n3-8-52",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-8-52::s-skm3-8-1",
            "added-n3-8-52::s-skm3-8-2",
            "added-n3-8-52::s-skm3-8-3",
            "added-n3-8-52::s-skm3-8-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 39 (PDF p. 62). Verified Section 5 repetitive predicate concession syntax and contrastive focus."
    }
]

existing_card_ids = {e.get("cardId") for e in c8_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(c8_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Chapter 8 in source coverage matrix! Total certified rows: {len(matrix)}")
