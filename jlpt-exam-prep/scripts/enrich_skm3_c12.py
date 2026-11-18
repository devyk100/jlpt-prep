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
    "応接室": {"reading": "おうせつしつ", "meaning": "reception room / parlor"},
    "突き当たり": {"reading": "つきあたり", "meaning": "end of the corridor / dead end"},
    "社外": {"reading": "しゃがい", "meaning": "outside the company / external clients"},
    "美化語": {"reading": "びかご", "meaning": "beautified speech / refined language"}
}
for k, v in needed_overrides.items():
    if k not in overrides:
        overrides[k] = v
OVERRIDES_PATH.write_text(json.dumps(overrides, ensure_ascii=False, indent=2), encoding="utf-8")

# 2. Add Chapter Exercises for SKM N3 Chapter 12
exercises_data = json.loads(CHAPTER_EXERCISES_PATH.read_text(encoding="utf-8"))

c12_exercises = [
    {
        "id": "skm3-c12-q1",
        "chapterId": "skm3-c12",
        "question": "社長、先ほどA社の田中社長がロビーに（　）。応接室へご案内しますか。",
        "options": [
            "お見えになりました",
            "参りました",
            "伺いました",
            "申されました"
        ],
        "correctIndex": 0,
        "explanation": "【正解: お見えになりました】\n「お見えになる」は「来る・到着する」の尊敬語です。大切なお客様である取引先社長の到着を高めて述べるのに最適です。\n\n【選択肢解説】\n1. お見えになりました (正解): 来るの尊敬語（お見えになる）。\n2. 参りました (不正解): 謙譲語II（丁重語）で自分側の動作を下げる表現であり、お客様に使えない。\n3. 伺いました (不正解): 謙譲語Iで自分が相手を訪問する動作。\n4. 申されました (不正解): 二重敬語かつ動詞の混乱。"
    },
    {
        "id": "skm3-c12-q2",
        "chapterId": "skm3-c12",
        "question": "先生、その重そうなお荷物は私がお（　）しましょうか。",
        "options": [
            "持ち",
            "持たれ",
            "持ちになり",
            "持っていただき"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 持ち】\n「お＋動詞ます形語幹＋する」は謙譲語Iで、自分が目上の人に対して行う行為をへりくだって敬意を表す公式です（お持ちしましょうか）。\n\n【選択肢解説】\n1. 持ち (正解): お＋持ち＋する（謙譲語I）。\n2. 持たれ (不正解): 受身または尊敬語で自分が荷物を持つ文脈に合わない。\n3. 持ちになり (不正解): お〜になる（尊敬語）を自分の動作に使うと重大な非礼。\n4. 持っていただき (不正解): 先生に持ってもらうことになり不適切。"
    },
    {
        "id": "skm3-c12-q3",
        "chapterId": "skm3-c12",
        "question": "はじめまして。私、山田太郎と（　）。本日はよろしくお願い申し上げます。",
        "options": [
            "申します",
            "おっしゃいます",
            "申し上げます",
            "伺います"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 申します】\n「申す」は「言う」の謙譲語II（丁重語）で、聞き手に対して改まって自分の名前を名乗る定番の表現です（〜と申します）。\n\n【選択肢解説】\n1. 申します (正解): 自己紹介における標準的な丁重語（〜と申します）。\n2. おっしゃいます (不正解): 尊敬語であり、自分の名乗りに使うと自己を賛美する非礼になる。\n3. 申し上げます (不正解): 謙譲語Iで「お礼・お詫びを申し上げる」のように相手へ届ける行為に使う。\n4. 伺います (不正解): 訪問・聞くの謙譲語。"
    },
    {
        "id": "skm3-c12-q4",
        "chapterId": "skm3-c12",
        "question": "先生、お昼ご飯はもう（　）か。よろしければご一緒しませんか。",
        "options": [
            "召し上がりました",
            "いただきました",
            "ご飯しました",
            "お食べになりました"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 召し上がりました】\n「食べる・飲む」の特別な尊敬語動詞は「召し上がる」です。目上の先生の食事を敬意を込めて尋ねる表現です。\n\n【選択肢解説】\n1. 召し上がりました (正解): 「食べる・飲む」の特別尊敬語。\n2. いただきました (不正解): 「食べる・飲む」の謙譲語で、自分の動作に使う。\n3. ご飯しました (不正解): くだけた俗語。\n4. お食べになりました (不正解): 一般規則形だが特別語「召し上がる」が最優先される。"
    },
    {
        "id": "skm3-c12-q5",
        "chapterId": "skm3-c12",
        "question": "明日の午後３時に、御社の本社オフィスへ（　）と存じます。",
        "options": [
            "伺いたい",
            "いらっしゃりたい",
            "おいでになりたい",
            "参上されたい"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 伺いたい】\n「伺う」は「行く・訪問する」の謙譲語Iで、相手の場所へ自分が向かうことをへりくだって敬意を表します（伺いたいと存じます）。\n\n【選択肢解説】\n1. 伺いたい (正解): 相手先を訪問する謙譲語I。\n2. いらっしゃりたい (不正解): 尊敬語を自分の動作に使えない。\n3. おいでになりたい (不正解): 尊敬語を自分の動作に使えない。\n4. 参上されたい (不正解): 不自然な受身尊敬の混同。"
    },
    {
        "id": "skm3-c12-q6",
        "chapterId": "skm3-c12",
        "question": "（社外からの電話対応）「あいにく社長はただいま席を（　）。」",
        "options": [
            "外しております",
            "外していらっしゃいます",
            "外されます",
            "外すそうです"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 外しております】\n内外（ウチとソト）の敬語原則では、社外の顧客に対して自社の人間（社長であっても）の動作を述べる際は、尊敬語を使わず謙譲語II（外しております）を用います。\n\n【選択肢解説】\n1. 外しております (正解): 自社上司の動作を社外に伝える正しい謙譲語表現。\n2. 外していらっしゃいます (不正解): 自社上司に尊敬語を使ってしまいウチ・ソトの規則違反。\n3. 外されます (不正解): 自社上司への尊敬語で誤り。\n4. 外すそうです (不正解): 伝聞口調でビジネス電話対応に不適切。"
    },
    {
        "id": "skm3-c12-q7",
        "chapterId": "skm3-c12",
        "question": "こちらの最新カタログをどうぞ（　）ください。",
        "options": [
            "ご覧",
            "拝見",
            "お見せ",
            "見られ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: ご覧】\n「見る」の特別尊敬語は「ご覧になる」で、「どうぞご覧ください」は相手に見ていただく丁寧な依頼表現です。\n\n【選択肢解説】\n1. ご覧 (正解): 「ご覧ください（見てくださいの尊敬語）」。\n2. 拝見 (不正解): 自分が読む・見る謙譲語（拝見します）。相手に「拝見してください」と言うのは重大な非礼。\n3. お見せ (不正解): 「見せてください」の意になりカタログを見せろという奇妙な文になる。\n4. 見られ (不正解): 接続不適合。"
    },
    {
        "id": "skm3-c12-q8",
        "chapterId": "skm3-c12",
        "question": "昨日送っていただいた提案書、早速（　）ました。素晴らしい内容です。",
        "options": [
            "拝見し",
            "ご覧になり",
            "見られ",
            "拝謁し"
        ],
        "correctIndex": 0,
        "explanation": "【正解: 拝見し】\n相手が作成・送付してくれた書類を自分が読む・見る動作には、謙譲語Iの「拝見する（拝見しました）」を用います。\n\n【選択肢解説】\n1. 拝見し (正解): 「見る」の謙譲語I（拝見しました）。\n2. ご覧になり (不正解): 尊敬語を自分の動作に使ってはいけない。\n3. 見られ (不正解): 敬語が不十分。\n4. 拝謁し (不正解): 天皇や国王に謁見する極度の古典語でビジネスに不適合。"
    },
    {
        "id": "skm3-c12-q9",
        "chapterId": "skm3-c12",
        "question": "ただいま倉庫に十分な在庫が（　）。明日発送可能です。",
        "options": [
            "ございます",
            "いらっしゃいます",
            "おられます",
            "存じます"
        ],
        "correctIndex": 0,
        "explanation": "【正解: ございます】\n無生物である「在庫がある」を丁寧に述べるには「ある」の丁寧語「ございます」を用います。\n\n【選択肢解説】\n1. ございます (正解): 「ある」の丁寧語。\n2. いらっしゃいます (不正解): 有情物（目上の人）の存在を表す尊敬語。\n3. おられます (不正解): 有情物（人）の存在を表す。\n4. 存じます (不正解): 「思う・知る」の謙譲語。"
    },
    {
        "id": "skm3-c12-q10",
        "chapterId": "skm3-c12",
        "question": "先生は明日の午後、研究室に（　）でしょうか。",
        "options": [
            "いらっしゃる",
            "おる",
            "参る",
            "伺う"
        ],
        "correctIndex": 0,
        "explanation": "【正解: いらっしゃる】\n目上の先生が「居る（いる）」ことを敬意を込めて尋ねるには、「いる」の特別尊敬語動詞「いらっしゃる」を用います。\n\n【選択肢解説】\n1. いらっしゃる (正解): 「いる」の特別尊敬語。\n2. おる (不正解): 謙譲語IIで自分の存在を下げる表現。\n3. 参る (不正解): 行く・来るの謙譲語。\n4. 伺う (不正解): 訪問するの謙譲語。"
    },
    {
        "id": "skm3-c12-q11",
        "chapterId": "skm3-c12",
        "question": "大切な荷物ですので、明日の朝一番に私が直接（　）します。",
        "options": [
            "お届け",
            "お届けに成り",
            "届けていただき",
            "届けられ"
        ],
        "correctIndex": 0,
        "explanation": "【正解: お届け】\n「お＋動詞ます形語幹＋する（お届けします）」は、相手に荷物を届ける自分の行為をへりくだって敬意を示す謙譲語Iです。\n\n【選択肢解説】\n1. お届け (正解): 「お届けします（謙譲語I）」。\n2. お届けに成り (不正解): 尊敬語を自分の動作に使えない。\n3. 届けていただき (不正解): 相手に届けてもらう依頼になる。\n4. 届けられ (不正解): 受身・可能。"
    },
    {
        "id": "skm3-c12-q12",
        "chapterId": "skm3-c12",
        "question": "お手洗いは廊下を右に曲がった突き当たりに（　）。",
        "options": [
            "ございます",
            "おられます",
            "いらっしゃいます",
            "存じ上げます"
        ],
        "correctIndex": 0,
        "explanation": "【正解: ございます】\n場所や施設の存在を丁寧に案内する際、「ある」の改まった丁寧語「ございます」を用います。\n\n【選択肢解説】\n1. ございます (正解): 「ある」の丁寧語案内。\n2. おられます (不正解): 人の存在。\n3. いらっしゃいます (不正解): 目上の人の存在。\n4. 存じ上げます (不正解): 人を知っているの謙譲語。"
    }
]

exercises_data = [e for e in exercises_data if e.get("chapterId") != "skm3-c12"]
exercises_data.extend(c12_exercises)
CHAPTER_EXERCISES_PATH.write_text(json.dumps(exercises_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated chapterExercises.json with {len(c12_exercises)} exercises for SKM N3 Chapter 12!")

# 3. Enrich base-reviewed.json for Chapter 12 cards
base_reviewed = json.loads(BASE_REVIEWED_PATH.read_text(encoding="utf-8"))

card_enrichments = {
    "skm3-u12-keigo-respect": {
        "title": "尊敬語: お〜になる / ご〜になる / 特別動詞 (Respectful Language - Elevating Others)",
        "connection": "お + 動ます形語幹 + になる (和語) | ご + 名詞 + になる / なさる (漢語) | お + 動ます形語幹 + ください | 特別動詞（いらっしゃる, おっしゃる, 召し上がる, ご覧になる, ご存知だ, なさる, くださる）",
        "nuance": "【Shin Kanzen Master N3 p. 52 正式規則】目上の人（顧客・上司・先生・取引先等）の行為を高めて敬意を表す表現。話し手自身の行為には絶対に使えない。\n・特別動詞（行く/来る/いる→いらっしゃる、言う→おっしゃる、食べる/飲む→召し上がる、見る→ご覧になる、する→なさる、くれる→くださる）\n・一般動詞規則形: お + ます語幹 + になる（お読みになる、お帰りになる）/ ご + 漢語名詞 + になる（ご出席になる、ご卒業なさる）\n・受身形（〜れる/られる）による尊敬（話される、来られる）",
        "keyTakeaway": "Elevates the actions of respected superiors and clients. Never used for oneself. Prioritize special irregular verbs (召し上がる, いらっしゃる) over regular formulas (お〜になる).",
        "sentences": [
            {
                "id": "skm3-u12-keigo-respect::s-skm3-12-1",
                "japanese": "何年に大学をご卒業なさったのですか。",
                "english": "In what year did you graduate from university?",
                "literal": "What year university graduated honorably-did question?",
                "tokens": [{"word": "ご卒業なさった", "meaning": "honorably graduated", "reading": "ごそつぎょうなさった", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 52 verbatim sentence 2: ご + noun + なさる honorific."
            },
            {
                "id": "skm3-u12-keigo-respect::s-skm3-12-2",
                "japanese": "明日の研究会にはご出席になりますか。",
                "english": "Will you be attending tomorrow's study group meeting?",
                "literal": "Tomorrow's study-group attendance become question?",
                "tokens": [{"word": "ご出席になりますか", "meaning": "will you attend?", "reading": "ごしゅっせきになりますか", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 52 verbatim sentence 3: ご + noun + になる honorific."
            },
            {
                "id": "skm3-u12-keigo-respect::s-skm3-12-3",
                "japanese": "今晩、先生のお宅にいらっしゃいますか。",
                "english": "Will you be at your home this evening, Professor?",
                "literal": "This-evening Professor's home-at are question?",
                "tokens": [{"word": "いらっしゃいますか", "meaning": "will you be there?", "reading": "いらっしゃいますか", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 52 verbatim sentence 5: special verb いらっしゃる for presence."
            },
            {
                "id": "skm3-u12-keigo-respect::s-skm3-12-4",
                "japanese": "会長が新しい研究についてお話しくださいます。",
                "english": "The association president will kindly speak to us about the new research.",
                "literal": "President new research about kindly-speak will-give.",
                "tokens": [{"word": "お話しくださいます", "meaning": "will kindly speak", "reading": "おはなしくざさいます", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 52 verbatim sentence 4: respectful benefactive with くださる."
            }
        ]
    },
    "skm3-u12-keigo-humble": {
        "title": "謙譲語I: お〜する / ご〜する / 特別動詞 (Humble Language 1 - Recipient Directed)",
        "connection": "お + 動ます形語幹 + する / いたす (和語) | ご + 名詞 + する / いたす (漢語) | 特別動詞（伺う, 申す/申し上げる, 拝見する, お目にかかる, 存じ上げる, いただく, 差し上げる）",
        "nuance": "【Shin Kanzen Master N3 pp. 52-53 正式規則】目上の人に関係のある、自分の行為をへりくだって言う表現。行為の受け手（相手・先生・顧客）を高めるために、自分側の動作を下げる。\n・特別動詞: 行く/来る/聞く/訪ねる→伺う、言う→申し上げる、見る→拝見する、会う→お目にかかる、あげる→差し上げる、もらう→いただく\n・一般動詞規則形: お + ます語幹 + する/いたす（お持ちする、お送りする）/ ご + 漢語名詞 + する/いたす（ご案内する、ご報告いたす）",
        "keyTakeaway": "Lowers speaker's action directed at an esteemed recipient ('humbly do for you / defer to recipient'). Distinguish from Kenjougo II (which lowers action toward listener without a recipient).",
        "sentences": [
            {
                "id": "skm3-u12-keigo-humble::s-skm3-12-1",
                "japanese": "先生の本をお借りしてよろしいでしょうか。",
                "english": "May I please borrow your book, Professor?",
                "literal": "Professor's book humbly-borrow good question?",
                "tokens": [{"word": "お借りして", "meaning": "humbly borrow", "reading": "おかりして", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 53 verbatim sentence 1: お + stem + する humble borrowing."
            },
            {
                "id": "skm3-u12-keigo-humble::s-skm3-12-2",
                "japanese": "会場まで私がご案内いたします。",
                "english": "I will personally guide you to the venue.",
                "literal": "Venue until I humbly-guide will-do.",
                "tokens": [{"word": "ご案内いたします", "meaning": "will humbly guide you", "reading": "ごあんないいたします", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 53 verbatim sentence 2: ご + noun + いたす humble guiding."
            },
            {
                "id": "skm3-u12-keigo-humble::s-skm3-12-3",
                "japanese": "完成品を先生にお見せしました。",
                "english": "I showed the finished product to my professor.",
                "literal": "Finished-product Professor-to humbly-showed did.",
                "tokens": [{"word": "お見せしました", "meaning": "humbly showed", "reading": "おみせしました", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 53 verbatim sentence 3: showing an item to an esteemed recipient."
            },
            {
                "id": "skm3-u12-keigo-humble::s-skm3-12-4",
                "japanese": "明日3時に先生のお宅へ伺います。",
                "english": "I will visit your home at 3:00 tomorrow, Professor.",
                "literal": "Tomorrow 3-o'clock Professor's home to humbly-visit.",
                "tokens": [{"word": "伺います", "meaning": "will humbly visit", "reading": "うかがいます", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 53 verbatim sentence 4: special verb 伺う for visiting a superior."
            }
        ]
    },
    "added-n3-12-58": {
        "title": "謙譲語II（丁重語）・丁寧語 (Humble Language 2 & Polite Forms)",
        "connection": "特別動詞（参る, おる, 申す, いたす, ござる） | 丁寧語（です, ます, ございます）",
        "nuance": "【Shin Kanzen Master N3 p. 53 正式規則】\n1.「謙譲語II（丁重語）」: 聞き手に対して自分の行為そのものを改まって丁寧に言う表現。行為の向かう相手（客体）が存在しなくても、聞き手に対する配慮として使える（東京に住んでおります、明日参ります、田中と申します、準備ができております）。社外の人に対して社内の人間の動作を述べるときにも必須（ウチ・ソトの敬語）。\n2.「丁寧語」: 話し相手との上下関係に関係なく、言葉遣いを丁寧に整える形式（です・ます・ございます）。",
        "keyTakeaway": "Listener-oriented modest speech (Teichougo / Kenjougo II): 参る, おる, 申す, いたす, ござる. Essential for business etiquette and Uchi/Soto distinctions.",
        "sentences": [
            {
                "id": "added-n3-12-58::s-skm3-12-1",
                "japanese": "明日3時に参ります。",
                "english": "I will come/go at 3:00 tomorrow.",
                "literal": "Tomorrow 3-o'clock-at humbly-go/come.",
                "tokens": [{"word": "参ります", "meaning": "will humbly come/go", "reading": "まいります", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 53 verbatim sentence 1: special verb 参る for movement."
            },
            {
                "id": "added-n3-12-58::s-skm3-12-2",
                "japanese": "夜は家におります。",
                "english": "I will be at home in the evening.",
                "literal": "Night home-at humbly-stay.",
                "tokens": [{"word": "おります", "meaning": "will humbly be there", "reading": "おります", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 53 verbatim sentence 2: special verb おる for modest presence."
            },
            {
                "id": "added-n3-12-58::s-skm3-12-3",
                "japanese": "私は山田と申します。",
                "english": "My name is Yamada.",
                "literal": "I Yamada as humbly-call.",
                "tokens": [{"word": "申します", "meaning": "am humbly called", "reading": "もうします", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 53 verbatim sentence 3: special verb 申す for stating name."
            },
            {
                "id": "added-n3-12-58::s-skm3-12-4",
                "japanese": "受付は一階にございます。",
                "english": "The reception desk is on the first floor.",
                "literal": "Reception 1st-floor-at politely-exists.",
                "tokens": [{"word": "ございます", "meaning": "politely exists", "reading": "ございます", "pos": "Grammar"}],
                "nuanceNote": "SKM N3 p. 53 verbatim sentence 4: polite existence verb ございます."
            }
        ]
    }
}

for card in base_reviewed:
    cid = card.get("id")
    if cid in card_enrichments:
        card.update(card_enrichments[cid])

BASE_REVIEWED_PATH.write_text(json.dumps(base_reviewed, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Enriched all {len(card_enrichments)} SKM N3 Chapter 12 cards in base-reviewed.json!")

# 4. Update audit/source-coverage-matrix.json
matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))

c12_matrix_entries = [
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 12",
        "exactPrintedPages": "p. 52",
        "exactPdfPages": "p. 75",
        "grammarItem": "尊敬語: お〜になる / ご〜になる / 特別動詞 (Respectful Language - Elevating Others)",
        "instructionalDetails": "Elevates actions of superiors/guests; special irregular verbs (いらっしゃる, おっしゃる, 召し上がる, ご覧になる, ご存知だ, なさる, くださる); regular formula お+V-stem+になる, ご+Noun+になる, passive respectful forms.",
        "cardId": "skm3-u12-keigo-respect",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u12-keigo-respect::s-skm3-12-1",
            "skm3-u12-keigo-respect::s-skm3-12-2",
            "skm3-u12-keigo-respect::s-skm3-12-3",
            "skm3-u12-keigo-respect::s-skm3-12-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 52 (PDF p. 75). Verified Section 1 special honorific verbs, regular formulas, and ban on self-elevation."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 12",
        "exactPrintedPages": "pp. 52-53",
        "exactPdfPages": "pp. 75-76",
        "grammarItem": "謙譲語I: お〜する / ご〜する / 特別動詞 (Humble Language 1 - Recipient Directed)",
        "instructionalDetails": "Lowers speaker's actions relative to esteemed recipient; special verbs (伺う, 申し上げる, 拝見する, お目にかかる, 存じ上げる, いただく, 差し上げる); regular formula お+V-stem+する/いたす, ご+Noun+する/いたす.",
        "cardId": "skm3-u12-keigo-humble",
        "exampleCount": 4,
        "exampleIds": [
            "skm3-u12-keigo-humble::s-skm3-12-1",
            "skm3-u12-keigo-humble::s-skm3-12-2",
            "skm3-u12-keigo-humble::s-skm3-12-3",
            "skm3-u12-keigo-humble::s-skm3-12-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed pp. 52-53 (PDF pp. 75-76). Verified Section 2 recipient-directed deference, special humble forms, and regular formulas."
    },
    {
        "sourceBook": "Shin Kanzen Master N3",
        "sourceSection": "Part 1 · Chapter 12",
        "exactPrintedPages": "p. 53",
        "exactPdfPages": "p. 76",
        "grammarItem": "謙譲語II（丁重語）・丁寧語 (Humble Language 2 & Polite Forms)",
        "instructionalDetails": "Listener-directed modest speech (参る, おる, 申す, いたす, ござる) and polite forms (です, ます, ございます); essential for business phone etiquette and Uchi/Soto distinctions.",
        "cardId": "added-n3-12-58",
        "exampleCount": 4,
        "exampleIds": [
            "added-n3-12-58::s-skm3-12-1",
            "added-n3-12-58::s-skm3-12-2",
            "added-n3-12-58::s-skm3-12-3",
            "added-n3-12-58::s-skm3-12-4"
        ],
        "missingWork": "",
        "status": "checked",
        "evidence": "Visual inspection of printed p. 53 (PDF p. 76). Verified Section 3 Teichougo listener-oriented forms and Section 4 polite existentials."
    }
]

existing_card_ids = {e.get("cardId") for e in c12_matrix_entries}
matrix = [m for m in matrix if m.get("cardId") not in existing_card_ids]
matrix.extend(c12_matrix_entries)
MATRIX_PATH.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Certified SKM N3 Chapter 12 in source coverage matrix! Total certified rows: {len(matrix)}")
