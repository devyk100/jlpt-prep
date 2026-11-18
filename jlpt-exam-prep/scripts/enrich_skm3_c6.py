import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
BASE_REVIEWED_PATH = ROOT / "content/base-reviewed.json"
CHAPTER_EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"
MATRIX_PATH = ROOT / "audit/source-coverage-matrix.json"
OVERRIDES_PATH = ROOT / "content/reading-overrides.json"

# 1. Update Reading Overrides if needed
overrides = json.loads(OVERRIDES_PATH.read_text(encoding="utf-8"))
needed_overrides = {
    "強豪校": {"reading": "きょうごうこう", "meaning": "powerhouse school / powerhouse sports team"},
    "守秘義務": {"reading": "しゅひぎむ", "meaning": "confidentiality obligation / duty of secrecy"},
    "無駄遣い": {"reading": "むだづかい", "meaning": "wasteful spending / squandering"},
    "放っておいて": {"reading": "ほっておいて", "meaning": "leaving unattended / neglecting"},
    "放っておいては": {"reading": "ほっておいては", "meaning": "if left unattended"}
}
for k, v in needed_overrides.items():
    if k not in overrides:
        overrides[k] = v
OVERRIDES_PATH.write_text(json.dumps(overrides, ensure_ascii=False, indent=2), encoding="utf-8")

# 2. Add Chapter Exercises for SKM N3 Chapter 6
exercises_data = json.loads(CHAPTER_EXERCISES_PATH.read_text(encoding="utf-8"))

c6_exercises = [
    {
        "id": "skm3-c6-q1",
        "chapterId": "skm3-c6",
        "question": "風邪気味なのに無理をして（　）、本格的に寝込んでしまいますよ。",
        "options": [
            "働いては",
            "働いてさえ",
            "働けば",
            "働いても"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 働いては】\n「〜ては」は「〜という事実や状況が続くと、好ましくない悪い結果が予想される」という警告を表します。風邪気味なのに無理して働くと寝込んでしまうというマイナスの結末に最適です。\n\n【選択肢解説】\n1. 働いては (正解): V-ては は悪い結果を引き起こす条件を表す。\n2. 働いてさえ (不正解): 「さえ」には通常「ば」等の条件形（働いてさえいれば）が必要。\n3. 働けば (不正解): 一般的な仮定条件で、好ましくない事態を戒める強い警告ニュアンスがない。\n4. 働いても (不正解): 逆接の譲歩（働いたとしても）になり文脈に合わない。"
    },
    {
        "id": "skm3-c6-q2",
        "chapterId": "skm3-c6",
        "question": "パスポート（　）、海外旅行のホテルにチェックインできます。",
        "options": [
            "さえあれば",
            "があっては",
            "あっても",
            "あればこそ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: さえあれば】\n「名詞＋さえ＋動詞ば形」は「それさえ満たされれば十分である」という必要最低限の条件を表します。「パスポートさえあればチェックインできる」という文脈にぴったりです。\n\n【選択肢解説】\n1. さえあれば (正解): 必要最低限の条件（パスポートさえあれば十分）。\n2. があっては (不正解): 〜ては は悪い結果を導くため、チェックインできるという肯定的事態には使えない。\n3. あっても (不正解): 逆接「あってもチェックインできない」のような文脈になる。\n4. あればこそ (不正解): 理由の強調表現で日常的な条件提示には不自然。"
    },
    {
        "id": "skm3-c6-q3",
        "chapterId": "skm3-c6",
        "question": "（　）遠く離れていても、私たちの友情は永遠に変わりません。",
        "options": [
            "たとえ",
            "もしも",
            "まるで",
            "どうしても"
        ],
        "correctIndex": 0,
        "explanation": "【正解: たとえ】\n「たとえ〜ても」は「ある仮定の状況が存在したとしても、それに関係なく後ろの事態が成り立つ」という不変の事実や強い意志を表します。\n\n【選択肢解説】\n1. たとえ (正解): 「たとえ〜ても」の呼応で強固な不変の友情を誓う。\n2. もしも (不正解): 単純な仮定「もしも〜たら/なら」と呼応し、「〜ても」の逆接譲歩強調には「たとえ」を用いる。\n3. まるで (不正解): 比喩表現（まるで〜のようだ）と呼応する。\n4. どうしても (不正解): 是非とも・何としてもという願望副詞。"
    },
    {
        "id": "skm3-c6-q4",
        "chapterId": "skm3-c6",
        "question": "会議の資料をまだ読んでいない（　）、今すぐ要点をまとめたものを配りますよ。",
        "options": [
            "のなら",
            "のでは",
            "さえすれば",
            "ては"
        ],
        "correctIndex": 0,
        "explanation": "【正解: のなら】\n「〜（の）なら」は相手の状況や発言を受けて、「それならこうしよう」と話者の判断・意志や相手への働きかけを述べる表現です。\n\n【選択肢解説】\n1. のなら (正解): 相手の状況「読んでいない」を前提として「配ります」と意志を表明。\n2. のでは (不正解): マイナスの悪い結果を予測する表現で、話者の親切な提案・意志文には続かない。\n3. さえすれば (不正解): 必要最低限の成立条件。\n4. ては (不正解): 悪い結果を導く表現で、配るという意志には続かない。"
    },
    {
        "id": "skm3-c6-q5",
        "chapterId": "skm3-c6",
        "question": "昨日の天気が（　）、山頂からの絶景が見られたのに、霧で何も見えなかった。",
        "options": [
            "よければ",
            "よくては",
            "よいなら",
            "よいと"
        ],
        "correctIndex": 0,
        "explanation": "【正解: よければ】\n反実仮想（事実と反対の仮定）の「〜ば／たら〜たのに」の構文です。実際には天気が悪くて見えなかった過去の悔恨・残念さを表します。\n\n【選択肢解説】\n1. よければ (正解): い形容詞の仮定形（よければ）＋見られたのに（反実仮想）。\n2. よくては (不正解): 悪い結果を予想する表現で「〜たのに」の後悔文には合わない。\n3. よいなら (不正解): 相手の状況を受けた提案に使うため過去の後悔には使えない。\n4. よいと (不正解): 自然法則・必然の条件節。"
    },
    {
        "id": "skm3-c6-q6",
        "chapterId": "skm3-c6",
        "question": "チームワーク（　）、次の強豪校との試合にも勝てるはずだ。",
        "options": [
            "さえよければ",
            "に反して",
            "に比べて",
            "にしては"
        ],
        "correctIndex": 0,
        "explanation": "【正解: さえよければ】\n「名詞＋さえ＋よければ」で「それさえ良好であれば十分勝てる」という最低限の不可欠な条件を提示しています。\n\n【選択肢解説】\n1. さえよければ (正解): 「名詞＋さえ＋形容詞仮定形」の最低限条件。\n2. に反して (不正解): 予想や規則に逆らうことを表す（予想に反して）。\n3. に比べて (不正解): 比較の基準を表す。\n4. にしては (不正解): 基準に対する意外性を表す（子供にしては）。"
    },
    {
        "id": "skm3-c6-q7",
        "chapterId": "skm3-c6",
        "question": "給料が入ったからといって、そんなに無駄遣いをして（　）、月末に困りますよ。",
        "options": [
            "いては",
            "いたら",
            "いてさえ",
            "いたなら"
        ],
        "correctIndex": 0,
        "explanation": "【正解: いては】\n「動詞て形＋いては」は好ましくない行為を継続していることに対して「それを続けていては困ったことになる」と忠告・警告する典型的な用法です。\n\n【選択肢解説】\n1. いては (正解): 継続する悪習に対する警告。\n2. いたら (不正解): 一般的な仮定で、警告の焦点がぼやける。\n3. いてさえ (不正解): 後ろに「〜ば」が必要。\n4. いたなら (不正解): 相手の状況の確認。"
    },
    {
        "id": "skm3-c6-q8",
        "chapterId": "skm3-c6",
        "question": "電車が遅延（　）、試験に間に合ったものを、遅刻して受けられなかった。",
        "options": [
            "しなかったら",
            "しては",
            "すれば",
            "するなら"
        ],
        "correctIndex": 0,
        "explanation": "【正解: しなかったら】\n反実仮想「〜（な）かったら、…たものを」の文型です。「実際には遅延して間に合わなかったが、もし遅延しなかったなら間に合っていたはずなのに」という強い無念・悔しさを表します。\n\n【選択肢解説】\n1. しなかったら (正解): 事実と反対の否定過去仮定。\n2. しては (不正解): 悪い結果を予想する文で過去の仮想には不適合。\n3. すれば (不正解): 肯定の仮定になり意味が逆。\n4. するなら (不正解): 前提の提示。"
    },
    {
        "id": "skm3-c6-q9",
        "chapterId": "skm3-c6",
        "question": "（　）どんなに親しい友人であっても、守秘義務のある情報は漏らせない。",
        "options": [
            "たとえ",
            "さすが",
            "まさに",
            "いかに"
        ],
        "correctIndex": 0,
        "explanation": "【正解: たとえ】\n「たとえ〜（で）あっても」は「どんな極端な場合を想定しても、結論は揺るがない」という強い原則や決意を表す呼応副詞です。\n\n【選択肢解説】\n1. たとえ (正解): 「たとえ〜であっても」の呼応。\n2. さすが (不正解): 称賛や納得の副詞。\n3. まさに (不正解): まさしく・ちょうどという強調副詞。\n4. いかに (不正解): 程度を尋ねる・強調する副詞で「どんなに」と重複。"
    },
    {
        "id": "skm3-c6-q10",
        "chapterId": "skm3-c6",
        "question": "体調が悪い（　）、今日の残業は断って早く帰りなさい。",
        "options": [
            "のなら",
            "のでは",
            "さえすれば",
            "ては"
        ],
        "correctIndex": 0,
        "explanation": "【正解: のなら】\n「〜（の）なら」は相手の様子や事実を受けて「それならば〜しなさい」と指示・助言・命令を後続節に置くことができます。「〜のでは」や「〜ては」の後ろには指示・命令文は置けません。\n\n【選択肢解説】\n1. のなら (正解): 相手の体調不良を受けて助言・指示する文脈に合致。\n2. のでは (不正解): 後ろに指示・命令文（帰りなさい）を置くことが文法的に禁止されている。\n3. さえすれば (不正解): 最低限条件。\n4. ては (不正解): 後ろに指示・命令文を置くことが禁止されている。"
    },
    {
        "id": "skm3-c6-q11",
        "chapterId": "skm3-c6",
        "question": "薬をきちんと（　）、熱はすぐに下がるでしょう。",
        "options": [
            "飲みさえすれば",
            "飲んでは",
            "飲むのなら",
            "飲んだらでは"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 飲みさえすれば】\n「動詞ます形語幹＋さえすれば」は「その行為を行うことだけで十分だ」という最低限の条件提示です。「薬を飲むことさえすれば熱は下がる」という意味になります。\n\n【選択肢解説】\n1. 飲みさえすれば (正解): 「動詞語幹＋さえすれば」の正しい接続。\n2. 飲んでは (不正解): 「〜ては」は悪い結果を予想するため、熱が下がるという回復には使えない。\n3. 飲むのなら (不正解): 相手の前提条件。\n4. 飲んだらでは (不正解): 文法的に誤った重複接続。"
    },
    {
        "id": "skm3-c6-q12",
        "chapterId": "skm3-c6",
        "question": "あと１年早く申し込んで（　）、オープニング記念割引が適用されたのだが、間に合わなかった。",
        "options": [
            "いれば",
            "いたらでは",
            "いるなら",
            "いては"
        ],
        "correctIndex": 0,
        "explanation": "【正解: いれば】\n反実仮想「動詞て形＋いれば、…たのだが」の形です。「実際には間に合わなかったが、もし申し込んでいたならば割引が効いたのに」という過去の反実仮想を表します。\n\n【選択肢解説】\n1. いれば (正解): 過去の反実仮想（申し込んでいれば〜されたのだが）。\n2. いたらでは (不正解): 存在しない誤った接続。\n3. いるなら (不正解): 現在・未来の前提。\n4. いては (不正解): マイナスの悪い結果を予測する用法。"
    }
]

# Update exercises list
exercises_data = [e for e in exercises_data if e.get("chapterId") != "skm3-c6"]
exercises_data.extend(c6_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(exercises_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with {len(c6_exercises)} exercises for SKM N3 Chapter 6!")

# 3. Enrich base-reviewed.json for Chapter 6 cards
base_reviewed = json.loads(BASE_REVIEWED_PATH.read_text(encoding="utf-8"))

card_enrichments = {
    "skm3-u6-tewa-dewa-negative-consequence": {
        "title": "〜ては / 〜では (Negative Inevitable Consequence)",
        "connection": "動て形 + は | い形くて + は | な形・名 + では | 普通形（な形だ-・名だ-）+ のでは",
        "nuance": "【Shin Kanzen Master N3 p. 32 正式規則】「〜という事実（仮定の状況）から、…という悪い結果が予想される。」Given that (or assuming) condition A holds, an undesirable result B will inevitably occur. 後ろの節（…）はマイナスの意味を持つ表現に限定され、話者の希望・意向を表す文や、相手への働きかけ（指示・依頼・命令・勧誘）の文は絶対に来ない。",
        "keyTakeaway": "Condition A inevitably leads to negative result B. Strictly limited to negative outcomes. Volitions, requests, and commands are strictly banned in clause B.",
        "sentences": [
            {
                "id": "skm3-u6-tewa-dewa-negative-consequence::s-skm3-6-1",
                "japanese": "手術をしないで放っておいては、命にかかわる。",
                "english": "Leaving it unattended without surgery will endanger one's life.",
                "literal": "Surgery without-doing leaving-alone if, life to relates.",
                "tokens": [{"word": "放っておいては", "meaning": "if left untreated", "reading": "ほっておいては", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 verbatim sentence 1: grave consequence endangering life."
            },
            {
                "id": "skm3-u6-tewa-dewa-negative-consequence::s-skm3-6-2",
                "japanese": "無責任な態度をとっていては、信用を失います。",
                "english": "If you maintain such an irresponsible attitude, you will lose everyone's trust.",
                "literal": "Irresponsible attitude taking if, trust lose.",
                "tokens": [{"word": "とっていては", "meaning": "if you keep taking", "reading": "とっていては", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 verbatim sentence 2: cautionary warning against continued irresponsible attitude."
            },
            {
                "id": "skm3-u6-tewa-dewa-negative-consequence::s-skm3-6-3",
                "japanese": "家を建て始めるのがこんなに遅れては、年内に仕上がらない。",
                "english": "With the start of house construction delayed this much, it will not be finished within the year.",
                "literal": "House build start this-much delaying if, within-year not-finish.",
                "tokens": [{"word": "遅れては", "meaning": "if delayed like this", "reading": "おくれては", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 verbatim sentence 3: inevitable scheduling failure due to delay."
            },
            {
                "id": "skm3-u6-tewa-dewa-negative-consequence::s-skm3-6-4",
                "japanese": "毎日こんなに遊んでいては、来月の大学入試に合格できませんよ。",
                "english": "If you spend every day playing around like this, you will never pass next month's university entrance exam.",
                "literal": "Every-day like-this playing if, next-month's exam pass cannot.",
                "tokens": [{"word": "遊んでいては", "meaning": "if you keep playing around", "reading": "あそんでいては", "pos": "Grammar"}],
                "nuanceNote": "Warning against persistent idleness."
            }
        ]
    },
    "skm3-u6-sae-ba": {
        "title": "〜さえ〜ば / 〜さえ〜なら (Sole Sufficient Minimum Prerequisite)",
        "connection": "名 + さえ + 動ば形 / い形ければ / な形なら / 名なら | 動ます形語幹 + さえすれば",
        "nuance": "【Shin Kanzen Master N3 p. 33 正式規則】「〜が実現すれば、…が実現する。「〜（だけ）でいい」という意味で、…が成立するための必要最低限の条件を示す。」If ~ happens or is done, then ... is all that needs to be done. Indicates the single indispensable, minimum condition sufficient for the outcome.",
        "keyTakeaway": "Indicates the minimum prerequisite that guarantees the outcome ('as long as X is met, all else will follow').",
        "sentences": [
            {
                "id": "skm3-u6-sae-ba::s-skm3-6-1",
                "japanese": "太郎は漫画さえあれば、退屈しない。",
                "english": "As long as Taro has manga, he is never bored.",
                "literal": "Taro manga only if-there-is, bored not-become.",
                "tokens": [{"word": "さえあれば", "meaning": "as long as there is", "reading": "さえあれば", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 verbatim sentence 1: single sufficient hobby to prevent boredom."
            },
            {
                "id": "skm3-u6-sae-ba::s-skm3-6-2",
                "japanese": "体さえ丈夫なら、どんな苦労にも耐えられる。",
                "english": "Provided one has a robust, healthy body, one can withstand any hardship.",
                "literal": "Body only if-healthy, any hardship even withstand-can.",
                "tokens": [{"word": "さえ丈夫なら", "meaning": "if only healthy", "reading": "さえじょうぶなら", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 verbatim sentence 2: physical resilience as sole requirement."
            },
            {
                "id": "skm3-u6-sae-ba::s-skm3-6-3",
                "japanese": "一言謝りさえすれば、相手も許してくれるだろう。",
                "english": "If only you offer a word of apology, the other party will surely forgive you.",
                "literal": "One-word apologize only if-do, other-party forgive will.",
                "tokens": [{"word": "謝りさえすれば", "meaning": "if only you apologize", "reading": "あやまりさえすれば", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 verbatim sentence 3: V-stem + さえすれば pattern."
            },
            {
                "id": "skm3-u6-sae-ba::s-skm3-6-4",
                "japanese": "パスポートさえあれば、とりあえず飛行機に乗ることはできる。",
                "english": "As long as you have your passport, you can board the plane for the time being.",
                "literal": "Passport only if-exists, for-now airplane board can.",
                "tokens": [{"word": "さえあれば", "meaning": "if only you have", "reading": "さえあれば", "pos": "Grammar"}],
                "nuanceNote": "Highlighting the indispensable prerequisite."
            }
        ]
    },
    "skm3-u6-tatoe-temo": {
        "title": "たとえ〜ても / たとえ〜でも (Hypothetical Concession: Even Granting X)",
        "connection": "たとえ + 動て形 / い形くて / な形・名 + でも",
        "nuance": "【Shin Kanzen Master N3 p. 33 正式規則】「〜という事実や仮定の状況があっても、関係なく…だ。」Means that even if a certain fact or state exists, something will take place or be done regardless. Frequently paired with the adverb たとえ to emphasize steadfast refusal or unwavering fact.",
        "keyTakeaway": "Even assuming hypothetical obstacle X, outcome Y holds steadfastly regardless.",
        "sentences": [
            {
                "id": "skm3-u6-tatoe-temo::s-skm3-6-1",
                "japanese": "周りのみんなに反対されても、私は歌手になりたい。",
                "english": "Even if everyone around me opposes it, I still want to become a singer.",
                "literal": "Surroundings everyone by opposed-even-if, I singer want-to-become.",
                "tokens": [{"word": "反対されても", "meaning": "even if opposed", "reading": "はんたいされても", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 verbatim sentence 1: personal dream persevering against opposition."
            },
            {
                "id": "skm3-u6-tatoe-temo::s-skm3-6-2",
                "japanese": "たとえ高くても、仕事に必要なものは買わなければならない。",
                "english": "Even if it is expensive, one must purchase things necessary for work.",
                "literal": "Even-if expensive-even-if, work necessary things must-buy.",
                "tokens": [{"word": "たとえ高くても", "meaning": "even if expensive", "reading": "たとえたかくても", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 verbatim sentence 2: inevitable business necessity regardless of cost."
            },
            {
                "id": "skm3-u6-tatoe-temo::s-skm3-6-3",
                "japanese": "たとえ面倒でも、健康診断は毎年受けたほうがいい。",
                "english": "Even if it is a nuisance, you should get a health checkup every year.",
                "literal": "Even-if nuisance-even-if, health-checkup every-year receive better.",
                "tokens": [{"word": "たとえ面倒でも", "meaning": "even if troublesome", "reading": "たとえめんどうでも", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 verbatim sentence 3: prudent medical advice despite inconvenience."
            },
            {
                "id": "skm3-u6-tatoe-temo::s-skm3-6-4",
                "japanese": "たとえどんなに給料が高くても、危険な仕事は引き受けたくない。",
                "english": "Even if the salary were exceptionally high, I would never want to undertake a hazardous job.",
                "literal": "Even-if how-much salary high-even-if, dangerous job undertake not-want.",
                "tokens": [{"word": "たとえ高くても", "meaning": "even if high", "reading": "たとえたかくても", "pos": "Grammar"}],
                "nuanceNote": "Steadfast refusal prioritizing personal safety over money."
            }
        ]
    },
    "added-n3-6-48": {
        "title": "〜なら (Context Premise) & 〜ば・〜たら・〜なら (Counterfactual Past)",
        "connection": "普通形（な形だ-・名だ-）+ (の)なら | 動ば形 / い形ければ / な形なら / 名なら | 普通形過去（〜たら）+ 〜たのに / 〜のだが / 〜ものを",
        "nuance": "【Shin Kanzen Master N3 pp. 32-33 正式規則】\n1.「〜（の）なら」:「〜を受けて、…」〜は相手の発言や様子、…は話者の判断・意志・相手への働きかけ（指示・命令・勧誘など）の文。\n2.「〜ば・〜たら・〜なら（反実仮想）」:「事実と反対の仮定。「〜の場合、…という結果になったはずだが、実際はそうではなかった」と言いたいときに使う。…には「〜たのに・〜のだが・〜ものを」などが来ることが多い。」",
        "keyTakeaway": "Dual structure: (1) 〜（の）なら takes situational context from listener as premise for speaker's judgment/volition/advice; (2) Counterfactual conditional expresses what would have happened if past reality were reversed, typically ending in 〜たのに, 〜のだが, or 〜ものを.",
        "sentences": [
            {
                "id": "added-n3-6-48::s-skm3-6-1",
                "japanese": "この箱、使わないなら、私にください。使いたいです。",
                "english": "If you are not going to use this box, please give it to me; I would like to use it.",
                "literal": "This box, not-use if, to-me please-give. Want-to-use.",
                "tokens": [{"word": "使わないなら", "meaning": "if not using", "reading": "つかわないなら", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 32 verbatim sentence 1: contextual premise followed by polite request."
            },
            {
                "id": "added-n3-6-48::s-skm3-6-2",
                "japanese": "その本、読んだのなら、私に貸してください。",
                "english": "If you have already read that book, please lend it to me.",
                "literal": "That book, read if, to-me please-lend.",
                "tokens": [{"word": "読んだのなら", "meaning": "if you have read", "reading": "よんだのなら", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 32 verbatim sentence 3: 〜のなら taking listener's state as premise."
            },
            {
                "id": "added-n3-6-48::s-skm3-6-3",
                "japanese": "お金と時間があれば、海外旅行に行けたのに。",
                "english": "If only I had money and time, I could have gone traveling abroad (regrettably I had neither).",
                "literal": "Money and time if-there-were, abroad travel could-go though.",
                "tokens": [{"word": "あれば", "meaning": "if there were", "reading": "あれば", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 33 verbatim sentence 1: counterfactual past condition ending in 〜のに."
            },
            {
                "id": "added-n3-6-48::s-skm3-6-4",
                "japanese": "朝寝坊しなかったら、あの飛行機に乗れたはずだ。乗れなかったのが本当に残念だ。",
                "english": "If I had not overslept, I could have caught that flight; not being able to board was truly regrettable.",
                "literal": "Morning-oversleep didn't-do-if, that airplane board-could should-be. Missed truly regrettable.",
                "tokens": [{"word": "しなかったら", "meaning": "if had not done", "reading": "しなかったら", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 33 verbatim sentence 2: counterfactual past condition with 〜たら."
            },
            {
                "id": "added-n3-6-48::s-skm3-6-5",
                "japanese": "ああ、残念だ。学生なら学生割引でチケットが買えたのに…。",
                "english": "Ah, what a pity! If I were a student, I could have bought the ticket with a student discount...",
                "literal": "Ah, regrettable. Student if student-discount ticket could-buy though...",
                "tokens": [{"word": "学生なら", "meaning": "if student", "reading": "がくせいなら", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 33 verbatim sentence 3: counterfactual noun + なら."
            }
        ]
    }
}

for card in base_reviewed:
    cid = card.get("id")
    if cid in card_enrichments:
        card.update(card_enrichments[cid])

BASE_REVIEWED_PATH.write_text(json.dumps(base_reviewed, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Enriched all {len(card_enrichments)} SKM N3 Chapter 6 cards in base-reviewed.json!")

# 4. Update audit/source-coverage-matrix.json
matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))

c6_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 6",
        "exactPrintedPages": "p. 32",
        "exactPdfPages": "p. 55",
        "grammarItem": "〜ては / 〜では (Negative Inevitable Consequence)",
        "instructionalDetails": "Condition A inevitably produces negative outcome B; V-て形 + は / い形くて + は / な形・名 + では / 普通形 + のでは; strict prohibition on speaker volitions, requests, invitations, or commands in clause B.",
        "cardId": "skm3-u6-tewa-dewa-negative-consequence",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u6-tewa-dewa-negative-consequence::s-skm3-6-1",
            "skm3-u6-tewa-dewa-negative-consequence::s-skm3-6-2",
            "skm3-u6-tewa-dewa-negative-consequence::s-skm3-6-3",
            "skm3-u6-tewa-dewa-negative-consequence::s-skm3-6-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 32 (PDF p. 55). Verified Section 2 negative inevitable consequence rules and strict ban on volitional/imperative conclusions."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 6",
        "exactPrintedPages": "p. 33",
        "exactPdfPages": "p. 56",
        "grammarItem": "〜さえ〜ば / 〜さえ〜なら (Sole Sufficient Minimum Prerequisite)",
        "instructionalDetails": "Indicates the single minimum condition that guarantees outcome; Noun + さえ + V-ば/い形ければ/な形なら/名なら or V-ます語幹 + さえすれば; semantics of 'if only this is met, nothing else is required'.",
        "cardId": "skm3-u6-sae-ba",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u6-sae-ba::s-skm3-6-1",
            "skm3-u6-sae-ba::s-skm3-6-2",
            "skm3-u6-sae-ba::s-skm3-6-3",
            "skm3-u6-sae-ba::s-skm3-6-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 33 (PDF p. 56). Verified Section 3 formation with Noun + さえ and V-stem + さえすれば, plus minimum condition semantics."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 6",
        "exactPrintedPages": "p. 33",
        "exactPdfPages": "p. 56",
        "grammarItem": "たとえ〜ても / たとえ〜でも (Hypothetical Concession: Even Granting X)",
        "instructionalDetails": "Hypothetical concession; たとえ + V-ても / い形くて + も / な形・名 + でも; outcome holds steadfastly regardless of hypothetical condition.",
        "cardId": "skm3-u6-tatoe-temo",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u6-tatoe-temo::s-skm3-6-1",
            "skm3-u6-tatoe-temo::s-skm3-6-2",
            "skm3-u6-tatoe-temo::s-skm3-6-3",
            "skm3-u6-tatoe-temo::s-skm3-6-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 33 (PDF p. 56). Verified Section 4 hypothetical concession rules with たとえ."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 6",
        "exactPrintedPages": "pp. 32-33",
        "exactPdfPages": "pp. 55-56",
        "grammarItem": "〜なら (Context Premise) & 〜ば・〜たら・〜なら (Counterfactual Past)",
        "instructionalDetails": "Comprehensive conditional coverage: (1) 〜（の）なら based on listener's context/statements, followed by advice/volition/requests; (2) Counterfactual past conditionals (〜ば/たら + 〜たのに/のだが/ものを) expressing unrealized outcomes contrary to fact.",
        "cardId": "added-n3-6-48",
        "exampleCount": 5,
        "exampleIds": [
            "added-n3-6-48::s-skm3-6-1",
            "added-n3-6-48::s-skm3-6-2",
            "added-n3-6-48::s-skm3-6-3",
            "added-n3-6-48::s-skm3-6-4",
            "added-n3-6-48::s-skm3-6-5"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 32-33 (PDF pp. 55-56). Verified Section 1 context premise rules and Section 5 counterfactual past expressions."
    }
]

# Avoid duplicate cardIds in matrix
existing_card_ids = {e.get("cardId") for e in c6_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(c6_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Chapter 6 in source coverage matrix! Total certified rows: {len(matrix)}")
