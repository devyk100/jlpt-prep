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
    "古文書": {"reading": "こもんじょ", "meaning": "ancient document / historic archives"},
    "腸内環境": {"reading": "ちょうないかんきょう", "meaning": "intestinal environment / gut flora"},
    "発酵食品": {"reading": "はっこうしょくひん", "meaning": "fermented food products"},
    "深海": {"reading": "しんかい", "meaning": "deep sea / ocean depths"},
    "龍": {"reading": "りゅう", "meaning": "dragon"}
}
for k, v in needed_overrides.items():
    if k not in overrides:
        overrides[k] = v
OVERRIDES_PATH.write_text(json.dumps(overrides, ensure_ascii=False, indent=2), encoding="utf-8")

# 2. Add Chapter Exercises for SKM N3 Chapter 7
exercises_data = json.loads(CHAPTER_EXERCISES_PATH.read_text(encoding="utf-8"))

c7_exercises = [
    {
        "id": "skm3-c7-q1",
        "chapterId": "skm3-c7",
        "question": "市の広報紙によると、来月からゴミの分別方法が新しくなる（　）。",
        "options": [
            "とのことだ",
            "と言われている",
            "とか",
            "って"
        ],
        "correctIndex": 0,
        "explanation": "【正解: とのことだ】\n「情報源（〜によると）＋普通形＋とのことだ／ということだ」は、入手した情報を公的・正確に伝えるフォーマルな伝聞表現です。市の広報紙からの連絡を伝える文脈に最も適しています。\n\n【選択肢解説】\n1. とのことだ (正解): 公式な情報伝達に適した伝聞文末。\n2. と言われている (不正解): 世間の一般的な評価・風説を表す表現で、行政広報からの正確な告知には不自然。\n3. とか (不正解): 未確認の噂話のような曖昧なニュアンスがあり、公的通知には不適切。\n4. って (不正解): くだけた日常会話専用の口語表現。"
    },
    {
        "id": "skm3-c7-q2",
        "chapterId": "skm3-c7",
        "question": "納豆や味噌などの発酵食品は、腸内環境を整えて健康に良い（　）。",
        "options": [
            "と言われている",
            "とのことだ",
            "って",
            "とかで"
        ],
        "correctIndex": 0,
        "explanation": "【正解: と言われている】\n「普通形＋と言われている」は「世間の人々や専門家の間で一般的にそう言われている」という社会的共通認識・通説を述べる表現です。\n\n【選択肢解説】\n1. と言われている (正解): 「健康に良いと広く知られている」という通説表現。\n2. とのことだ (不正解): 特定の個人やニュースからの伝言を伝える表現。\n3. って (不正解): くだけた口語体。\n4. とかで (不正解): 未確認の曖昧な理由づけ。"
    },
    {
        "id": "skm3-c7-q3",
        "chapterId": "skm3-c7",
        "question": "田中さん「ねえ、駅前の新しいカフェ、もうオープンした（　）？」",
        "options": [
            "んだって",
            "とのことだ",
            "と言われている",
            "という"
        ],
        "correctIndex": 0,
        "explanation": "【正解: んだって】\n親しい間柄での日常会話では、伝聞の「〜そうだ」のくだけた口語形「〜って／んだって」が自然に使われます。\n\n【選択肢解説】\n1. んだって (正解): 親しい友人同士の会話における伝聞の確認。\n2. とのことだ (不正解): 堅苦しい書き言葉・報告表現で友人間の会話に不向き。\n3. と言われている (不正解): 社会的通説を表すため、個別の店舗オープンには合わない。\n4. という (不正解): 格式張った書き言葉・歴史的記述。"
    },
    {
        "id": "skm3-c7-q4",
        "chapterId": "skm3-c7",
        "question": "古文書の記録によると、この寺は平安時代の初めに建てられた（　）。",
        "options": [
            "という",
            "って",
            "とか",
            "と言って"
        ],
        "correctIndex": 0,
        "explanation": "【正解: という】\n「普通形＋という」は、歴史的な記録や伝承などを客観的に伝える、格式の高い書き言葉の伝聞表現です。\n\n【選択肢解説】\n1. という (正解): 歴史的記録や伝承を伝える硬い書き言葉。\n2. って (不正解): くだけた口語体で歴史記述に不適切。\n3. とか (不正解): 信憑性の低い噂話のニュアンス。\n4. と言って (不正解): 引用の動詞連用形で文末を完結できない。"
    },
    {
        "id": "skm3-c7-q5",
        "chapterId": "skm3-c7",
        "question": "隣のクラスの高橋君、来月家族でアメリカへ引っ越す（　）。本当かな。",
        "options": [
            "とか",
            "とのことだ",
            "と言われている",
            "という"
        ],
        "correctIndex": 0,
        "explanation": "【正解: とか】\n「普通形＋とか」は「〜と聞いたが、確かな情報ではない」という未確認の噂を伝える表現で、「本当かな」と疑問を抱く文脈に最適です。\n\n【選択肢解説】\n1. とか (正解): 未確認の噂話を伝える用法（〜とか、本当かな）。\n2. とのことだ (不正解): 確実な伝言・告知を伝える文脈に使う。\n3. と言われている (不正解): 一般的通説。\n4. という (不正解): 硬い書き言葉。"
    },
    {
        "id": "skm3-c7-q6",
        "chapterId": "skm3-c7",
        "question": "受付の女性「部長からの伝言です。本日の打ち合わせは15時から（　）。」",
        "options": [
            "とのことです",
            "とかです",
            "と言われています",
            "ってです"
        ],
        "correctIndex": 0,
        "explanation": "【正解: とのことです】\n個人の発言や伝言を丁寧に伝える場合、「〜とのことです」を用います。\n\n【選択肢解説】\n1. とのことです (正解): 個人の伝言を改まって伝える定型表現。\n2. とかです (不正解): 噂話のように聞こえ、業務の伝言として失礼かつ不適切。\n3. と言われています (不正解): 社会的通説。\n4. ってです (不正解): 口語の「って」と丁寧語「です」の不自然な接続。"
    },
    {
        "id": "skm3-c7-q7",
        "chapterId": "skm3-c7",
        "question": "今シーズンのプロ野球では、強力な投手陣を誇るAチームが優勝する（　）。",
        "options": [
            "と言われている",
            "とのことだ",
            "とか",
            "って"
        ],
        "correctIndex": 0,
        "explanation": "【正解: と言われている】\n多くの専門家や世論が一致してそう見込んでいるという世間の評判・予想を述べるには「〜と言われている」を用います。\n\n【選択肢解説】\n1. と言われている (正解): 衆目の一致する評価・下馬評を伝える。\n2. とのことだ (不正解): 個別の伝言の伝達。\n3. とか (不正解): 根拠の薄い噂話。\n4. って (不正解): くだけた口語。"
    },
    {
        "id": "skm3-c7-q8",
        "chapterId": "skm3-c7",
        "question": "山田君、さっき職員室で先生が「すぐ来い」って（　）。",
        "options": [
            "言ってたよ",
            "とのことだ",
            "と言われている",
            "ということだった"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 言ってたよ】\n「引用内容＋って言ってたよ」は親しい友人への口頭伝達における定番フレーズです。\n\n【選択肢解説】\n1. 言ってたよ (正解): 友人への日常会話での自然な伝言。\n2. とのことだ (不正解): 文末が硬すぎて同級生同士の会話として不自然。\n3. と言われている (不正解): 通説表現。\n4. ということだった (不正解): 客観的公的報告の過去形。"
    },
    {
        "id": "skm3-c7-q9",
        "chapterId": "skm3-c7",
        "question": "今朝の科学ニュースによると、深海で新種の生物が発見された（　）。",
        "options": [
            "ということだ",
            "って",
            "とか",
            "と言われている"
        ],
        "correctIndex": 0,
        "explanation": "【正解: ということだ】\nニュース報道や学術的な伝聞を客観的に報告する場合、「〜ということだ」が極めて自然です。\n\n【選択肢解説】\n1. ということだ (正解): 報道・客観的事実の伝達。\n2. って (不正解): 口語的すぎてニュース報告に合わない。\n3. とか (不正解): 未確認の噂に聞こえる。\n4. と言われている (不正解): 世間の評判・通説であり、新発見の事実報告にはそぐわない。"
    },
    {
        "id": "skm3-c7-q10",
        "chapterId": "skm3-c7",
        "question": "村の古い言い伝えでは、あの山には昔、巨大な龍が住んでいた（　）。",
        "options": [
            "という",
            "って",
            "とのことだ",
            "とか"
        ],
        "correctIndex": 0,
        "explanation": "【正解: という】\n古い伝説・言い伝え・文献記録などをフォーマルに語る文脈では、「〜という」が伝統的な書き言葉として用いられます。\n\n【選択肢解説】\n1. という (正解): 伝説や伝承を語る格調高い文末。\n2. って (不正解): くだけた口語。\n3. とのことだ (不正解): 現代のメッセージ伝達。\n4. とか (不正解): 現代の軽い噂話。"
    },
    {
        "id": "skm3-c7-q11",
        "chapterId": "skm3-c7",
        "question": "同僚の話では、来期から新しい評価制度が導入される（　）で、みんな不安がっている。",
        "options": [
            "とか",
            "とのこと",
            "と言われている",
            "って"
        ],
        "correctIndex": 0,
        "explanation": "【正解: とか】\n「〜とかで」は「〜という話を聞いて」という未確認の噂を理由・背景として後続節につなげる慣用表現です。\n\n【選択肢解説】\n1. とか (正解): 「〜とかで」の形で噂を理由として提示。\n2. とのこと (不正解): 「とのこと」に直接「で」を接続して理由節にする用法は一般的でない。\n3. と言われている (不正解): 通説であり、「〜と言われているで」という接続は誤り。\n4. って (不正解): 「ってで」という接続は存在しない。"
    },
    {
        "id": "skm3-c7-q12",
        "chapterId": "skm3-c7",
        "question": "（手紙の文面）ご長男が大学に無事合格なさった（　）、心よりお祝い申し上げます。",
        "options": [
            "とのこと",
            "って",
            "とか",
            "と言われている"
        ],
        "correctIndex": 0,
        "explanation": "【正解: とのこと】\n手紙や改まった挨拶状で人づてに聞いた慶事を述べる際、「〜とのこと、心よりお祝い申し上げます」という書簡慣用表現を用います。\n\n【選択肢解説】\n1. とのこと (正解): 書簡で間接的に聞いた知らせを受けて祝意を表す定番表現。\n2. って (不正解): 手紙で使うのは極めて失礼。\n3. とか (不正解): 噂話扱いになり祝いの手紙として非礼。\n4. と言われている (不正解): 個人的慶事を通説扱いするのは不自然。"
    }
]

# Update exercises
exercises_data = [e for e in exercises_data if e.get("chapterId") != "skm3-c7"]
exercises_data.extend(c7_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(exercises_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with {len(c7_exercises)} exercises for SKM N3 Chapter 7!")

# 3. Enrich base-reviewed.json for Chapter 7 cards
base_reviewed = json.loads(BASE_REVIEWED_PATH.read_text(encoding="utf-8"))

card_enrichments = {
    "added-n3-7-49": {
        "title": "〜ということだ・〜とのことだ (Formal Transmission of Reported Speech)",
        "connection": "普通形 + ということだ / とのことだ（情報源を示す表現：〜によると・〜によれば・〜では）",
        "nuance": "【Shin Kanzen Master N3 p. 36 正式規則】「（〜によると）、…ということだ・とのことだ。」得た情報を第三者に伝える言い方。「〜そうだ」よりも改まった、少し硬い表現。情報源を示すときは「〜によると・〜によれば・〜では」などの表現を前に置く。言った人が個人の場合は「〜とのことだ」を使うことが多く、手紙やビジネス文書・メールでも頻出する。",
        "keyTakeaway": "Formal transmission of heard information/notices. Slightly stiffer than 〜そうだ. Often paired with 〜によると/によれば. When relaying a personal message, 〜とのことだ is standard.",
        "sentences": [
            {
                "id": "added-n3-7-49::s-skm3-7-1",
                "japanese": "市の知らせによると、この道路工事は来年まで続くということだ。",
                "english": "According to the city notice, this road construction is scheduled to continue until next year.",
                "literal": "City's notice according-to, this road construction next-year until continue that is said.",
                "tokens": [{"word": "続くということだ", "meaning": "is said to continue", "reading": "つづくということだ", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 36 verbatim sentence 1: municipal announcement relay."
            },
            {
                "id": "added-n3-7-49::s-skm3-7-2",
                "japanese": "店の人の話によれば、この地方の米は甘くてとてもおいしいとのことだ。",
                "english": "According to the shop clerk, the rice from this region is sweet and exceptionally delicious.",
                "literal": "Shop's person talk according-to, this region's rice sweet-and delicious that is said.",
                "tokens": [{"word": "おいしいとのことだ", "meaning": "is reported to be delicious", "reading": "おいしいとのことだ", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 36 verbatim sentence 2: personal information relay with 〜とのことだ."
            },
            {
                "id": "added-n3-7-49::s-skm3-7-3",
                "japanese": "長期出張でそちらへ伺う予定とのこと、大変楽しみにいたしております。",
                "english": "I hear that you plan to visit us on an extended business trip; we are looking forward to it very much.",
                "literal": "Long-term trip by there visit plan that heard, very looking-forward doing.",
                "tokens": [{"word": "予定とのこと", "meaning": "reported to be the plan", "reading": "よていとのこと", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 36 verbatim sentence 3: formal epistolary/letter usage."
            },
            {
                "id": "added-n3-7-49::s-skm3-7-4",
                "japanese": "連絡によると、会議は延期されたとのことです。",
                "english": "According to the message, the meeting has been postponed.",
                "literal": "Message according-to, meeting postponed that is said.",
                "tokens": [{"word": "延期されたとのことです", "meaning": "reported to have been postponed", "reading": "えんきされたとのことです", "pos": "Grammar"}],
                "nuanceNote": "Official business postponement notice."
            }
        ]
    },
    "added-n3-7-50": {
        "title": "〜と言われている (Received Opinion / Widespread Public Belief)",
        "connection": "普通形 + と言われている",
        "nuance": "【Shin Kanzen Master N3 p. 36 正式規則】「〜と、世間の人々が言っている。」Indicates received opinion or general consensus held by society, experts, or the general public. Does not require citing a specific individual or formal source, as the claim is recognized as widespread belief.",
        "keyTakeaway": "Expresses general social consensus ('it is said that / people generally believe that'). Focuses on widespread opinion rather than a single speaker's words.",
        "sentences": [
            {
                "id": "added-n3-7-50::s-skm3-7-1",
                "japanese": "今年は黒い服が流行すると言われている。",
                "english": "It is said that black clothing will be in fashion this year.",
                "literal": "This-year black clothing fashion-do that is-said.",
                "tokens": [{"word": "流行すると言われている", "meaning": "is said to become popular", "reading": "りゅうこうするといわれている", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 36 verbatim sentence 1: widespread fashion forecast."
            },
            {
                "id": "added-n3-7-50::s-skm3-7-2",
                "japanese": "納豆は体にいいと言われている。",
                "english": "Natto is generally believed to be good for one's health.",
                "literal": "Natto body-to good that is-said.",
                "tokens": [{"word": "いいと言われている", "meaning": "is said to be good", "reading": "いいといわれている", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 36 verbatim sentence 2: widespread nutritional consensus."
            },
            {
                "id": "added-n3-7-50::s-skm3-7-3",
                "japanese": "今度の大会では中川選手が優勝すると言われている。",
                "english": "It is widely predicted that Nakagawa will win the championship in the upcoming tournament.",
                "literal": "This-time's tournament Nakagawa competitor win that is-said.",
                "tokens": [{"word": "優勝すると言われている", "meaning": "is tipped to win", "reading": "ゆうしょうするといわれている", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 36 verbatim sentence 3: public sports consensus."
            },
            {
                "id": "added-n3-7-50::s-skm3-7-4",
                "japanese": "この町は住みやすいと言われています。",
                "english": "This town is said to be very pleasant to live in.",
                "literal": "This town live-easy that is-said.",
                "tokens": [{"word": "住みやすいと言われています", "meaning": "is said to be easy to live in", "reading": "すみやすいといわれています", "pos": "Grammar"}],
                "nuanceNote": "General reputation of a residential community."
            }
        ]
    },
    "added-n3-7-51": {
        "title": "〜とか・〜って・〜という (Hearsay Spectrum: Casual Gossip to Written Lore)",
        "connection": "普通形 + とか（未確認の伝聞） | 普通形 + って（くだけた口語伝聞） | 普通形 + という（硬い書き言葉伝聞）",
        "nuance": "【Shin Kanzen Master N3 p. 37 正式規則】\n1.「〜とか」:「〜と聞いた。」未確認の伝聞。自分が得た情報がまだ確実でない場合に使う。\n2.「〜って」:「〜と言っている・〜と聞いた。」「〜そうだ」のくだけた口頭表現。後ろの動詞（言っている、聞いた等）は省略されることが多い。\n3.「〜という」:「〜そうだ。」の少し硬い書き言葉。歴史的伝承や客観的報道・文献で使われる。",
        "keyTakeaway": "Tripartite stylistic spectrum: 〜とか (unverified rumor/hearsay); 〜って (casual spoken shortcut omitting reporting verb); 〜という (formal written reporting for history and lore).",
        "sentences": [
            {
                "id": "added-n3-7-51::s-skm3-7-1",
                "japanese": "来月、新しい美術館ができるとか。一度行ってみたい。",
                "english": "I hear that a new art museum is opening next month; I would like to visit it once.",
                "literal": "Next-month new art-museum can-do rumor. Once want-to-go.",
                "tokens": [{"word": "できるとか", "meaning": "heard that it will be built", "reading": "できるとか", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 37 verbatim sentence 1: unverified pleasant rumor."
            },
            {
                "id": "added-n3-7-51::s-skm3-7-2",
                "japanese": "佐藤さんの奥さん、料理の先生なんだって。",
                "english": "I heard that Sato's wife is a cooking instructor.",
                "literal": "Sato's wife cooking teacher that is heard.",
                "tokens": [{"word": "先生なんだって", "meaning": "heard that she is a teacher", "reading": "せんせいなんだって", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 37 verbatim sentence 2: casual spoken hearsay."
            },
            {
                "id": "added-n3-7-51::s-skm3-7-3",
                "japanese": "この城の周りは、昔、一面の野原だったという。",
                "english": "It is recorded that the area around this castle was once an expanse of open fields.",
                "literal": "This castle's surrounding, old-days, one-surface plain was that is-said.",
                "tokens": [{"word": "野原だったという", "meaning": "is said to have been open fields", "reading": "のはらだったという", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 37 verbatim sentence 3: formal written historical record."
            },
            {
                "id": "added-n3-7-51::s-skm3-7-4",
                "japanese": "豆腐は1300年前に中国から日本へ伝わったという。",
                "english": "It is said that tofu was introduced to Japan from China 1,300 years ago.",
                "literal": "Tofu 1300-years-ago China from Japan to introduced that is-said.",
                "tokens": [{"word": "伝わったという", "meaning": "is said to have been transmitted", "reading": "つたわったという", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 37 verbatim sentence 5: historical origin transmission."
            }
        ]
    }
}

for card in base_reviewed:
    cid = card.get("id")
    if cid in card_enrichments:
        card.update(card_enrichments[cid])

BASE_REVIEWED_PATH.write_text(json.dumps(base_reviewed, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Enriched all {len(card_enrichments)} SKM N3 Chapter 7 cards in base-reviewed.json!")

# 4. Update audit/source-coverage-matrix.json
matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))

c7_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 7",
        "exactPrintedPages": "p. 36",
        "exactPdfPages": "p. 59",
        "grammarItem": "〜ということだ・〜とのことだ (Formal Transmission of Reported Speech)",
        "instructionalDetails": "Plain form + ということだ / とのことだ; slightly formal reporting register; source indicated by 〜によると/によれば; 〜とのことだ preferred when relaying personal messages, letters, or direct spoken statements.",
        "cardId": "added-n3-7-49",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-7-49::s-skm3-7-1",
            "added-n3-7-49::s-skm3-7-2",
            "added-n3-7-49::s-skm3-7-3",
            "added-n3-7-49::s-skm3-7-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 36 (PDF p. 59). Verified Section 1 formation with 〜によると and personal relay function of 〜とのことだ."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 7",
        "exactPrintedPages": "p. 36",
        "exactPdfPages": "p. 59",
        "grammarItem": "〜と言われている (Received Opinion / Widespread Public Belief)",
        "instructionalDetails": "Plain form + と言われている; indicates widespread received opinion / societal consensus; no specific individual speaker needed as subject.",
        "cardId": "added-n3-7-50",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-7-50::s-skm3-7-1",
            "added-n3-7-50::s-skm3-7-2",
            "added-n3-7-50::s-skm3-7-3",
            "added-n3-7-50::s-skm3-7-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 36 (PDF p. 59). Verified Section 2 public consensus semantics and example sentences."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 7",
        "exactPrintedPages": "p. 37",
        "exactPdfPages": "p. 60",
        "grammarItem": "〜とか・〜って・〜という (Hearsay Spectrum: Casual Gossip to Written Lore)",
        "instructionalDetails": "Three distinct registers of hearsay: (1) 〜とか for unconfirmed rumors; (2) 〜って as casual conversational shortcut; (3) 〜という as formal written/historical report.",
        "cardId": "added-n3-7-51",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-7-51::s-skm3-7-1",
            "added-n3-7-51::s-skm3-7-2",
            "added-n3-7-51::s-skm3-7-3",
            "added-n3-7-51::s-skm3-7-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 37 (PDF p. 60). Verified Sections 3, 4, 5 stylistic spectrum and omission of reporting verbs in casual って."
    }
]

existing_card_ids = {e.get("cardId") for e in c7_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(c7_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Chapter 7 in source coverage matrix! Total certified rows: {len(matrix)}")
