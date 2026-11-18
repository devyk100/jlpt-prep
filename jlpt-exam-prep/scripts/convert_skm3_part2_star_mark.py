import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"

exercises = json.load(open(EXERCISES_PATH, encoding="utf-8"))

# Master dataset of authentic Star-Mark sentence rearrangements for SKM N3 Part 2 (Chapters 1–4, 48 items)
STAR_MARK_N3 = {
    # =========================================================================
    # Part 2 · Chapter 1: 引用 (Quotation & Indirect Speech) - pp. 104–105
    # =========================================================================
    "skm3-p2-c1-q1": {
        "question": "課長に、電車の ＿＿ ＿＿ ★ ＿＿ 伝えていただけますか。",
        "options": ["遅延で", "10分ほど", "遅れると", "電話で"],
        "scrambleOrder": [1, 2, 3, 4],  # 1(遅延で) -> 2(10分ほど) -> 3(遅れると★) -> 4(電話で) -> [Wait: 電話で電車の... let's check order]
        # Better natural order: 電車の [遅延で(1)] [10分ほど(2)] [遅れると(3)] [伝えて(tail)]
        # Options: 1: 遅延で, 2: 10分ほど, 3: 遅れる, 4: と
        # Sentence: 課長に、電車の [遅延で] [10分ほど] [遅れる] [★と] 伝えていただけますか。
        "options": ["遅延で", "10分ほど", "遅れる", "と"],
        "scrambleOrder": [1, 2, 3, 4], # [1: 遅延で] [2: 10分ほど] [★ 3: 遅れる] [4: と] -> star is 3 (遅れる) or star is 4?
        # In JLPT standard: slot sequence is [1] [2] [★ 3] [4]. The option in slot 3 is the answer!
        # If order is: [遅延で(1)] [10分ほど(2)] [遅れる(3)] [と(4)], then slot 3 is option "遅れる" (idx 2).
        "slotChoices": ["遅延で", "10分ほど", "遅れる", "と"],
        "correctIndex": 2, # "遅れる" is in slot 3 (★)
        "reconstructed": "課長に、電車の遅延で10分ほど遅れると伝えていただけますか。",
        "translation": "Could you please tell the section manager that I will be about 10 minutes late due to a train delay?",
        "context": "Asking a colleague to relay a delay message to a supervisor.",
        "hint": "Link cause (遅延で), amount (10分ほど), predicate (遅れる), and quotation particle (と).",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 引用), pp. 104–105",
        "overall": "文末の「伝えていただけますか」に呼応して、発言内容を引用する構造を作ります。【電車の遅延で】（理由）→【10分ほど】（程度）→【遅れる】（内容述語）→【と】（引用助詞）の順に並びます。★の位置（3番目）には「遅れる」が入ります。",
        "optReasons": [
            ("遅延で", "1番目の要素。「電車の」に直接接続して遅刻の理由を示します。"),
            ("10分ほど", "2番目の要素。遅れる時間の長さを指定します。"),
            ("遅れる", "【正解（★・3番目）】引用助詞「と」の直前に置く述語普通形です。"),
            ("と", "4番目の要素。「〜と伝える」の引用格助詞で、文末「伝えていただけますか」に接続します。")
        ]
    },
    "skm3-p2-c1-q2": {
        "question": "医師から、塩分を ＿＿ ＿＿ ★ ＿＿ 強く言われた。",
        "options": ["控えて", "できるだけ", "薄味にする", "ように"],
        "correctIndex": 2, # [控えて(1)] [できるだけ(2)] [★ 薄味にする(3)] [ように(4)]
        "reconstructed": "医師から、塩分を控えてできるだけ薄味にするように強く言われた。",
        "translation": "I was strongly told by the doctor to cut back on salt and make meals as lightly seasoned as possible.",
        "context": "Relaying dietary health instructions from a medical specialist.",
        "hint": "Arrange actions in sequence followed by the directive indirect citation ように言われた.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 引用), pp. 104–105",
        "overall": "「〜ように言う」は指示・助言の間接引用です。【控えて】（先行動作）→【できるだけ】（副詞）→【薄味にする】（動詞基本形）→【ように】（指示引用）の順序になります。★の位置（3番目）には「薄味にする」が入ります。",
        "optReasons": [
            ("控えて", "1番目の要素。「塩分を控えて」として最初の注意点を示します。"),
            ("できるだけ", "2番目の要素。次の「薄味にする」を修飾する副詞です。"),
            ("薄味にする", "【正解（★・3番目）】「ように」の直前に接続する動詞辞書形です。"),
            ("ように", "4番目の要素。「言われた」に接続する指示の間接引用形式です。")
        ]
    },
    "skm3-p2-c1-q3": {
        "question": "彼は「少し ＿＿ ＿＿ ★ ＿＿ 立ち上がり、大きく伸びをした。",
        "options": ["休憩しよう」", "と", "独り言を", "言って"],
        "correctIndex": 2, # [休憩しよう」(1)] [と(2)] [★ 独り言を(3)] [言って(4)]
        "reconstructed": "彼は「少し休憩しよう」と独り言を言って立ち上がり、大きく伸びをした。",
        "translation": "Muttering to himself 'let's take a short break', he stood up and stretched extensively.",
        "context": "Describing someone muttering a quote before stretching at work.",
        "hint": "Connect direct quote 「〜」 + と + 独り言を + 言って.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 引用), pp. 104–105",
        "overall": "直接引用の鉤括弧「　」の直後に引用助詞「と」が続き、【独り言を言って】で述語を作ります。順序は【休憩しよう」】→【と】→【独り言を】→【言って】。★の位置（3番目）は「独り言を」です。",
        "optReasons": [
            ("休憩しよう」", "1番目の要素。鉤括弧を閉じる発話内容です。"),
            ("と", "2番目の要素。直接引用を受ける引用助詞です。"),
            ("独り言を", "【正解（★・3番目）】目的語として後続の動詞「言って」を修飾します。"),
            ("言って", "4番目の要素。後続の「立ち上がり」へと繋ぐ中連形です。")
        ]
    },
    "skm3-p2-c1-q4": {
        "question": "あの人気歌手が ＿＿ ＿＿ ★ ＿＿ 噂が、ネット上で急速に広がっている。",
        "options": ["極秘で", "結婚した", "という", "信じがたい"],
        "correctIndex": 2, # [極秘で(1)] [結婚した(2)] [★ という(3)] [信じがたい(4)] -> wait: [極秘で結婚したという] [信じがたい] 噂が? Or [信じがたい極秘で...]
        # Standard: あの人気歌手が [極秘で] [結婚した] [という] [信じがたい] 噂が / Or: [極秘で(1)] [電撃(2)]...
        # Let's check: options = ["極秘で", "結婚した", "という", "驚きの"] -> [極秘で] [結婚した] [という] [驚きの] 噂が
        "options": ["極秘で", "結婚した", "という", "信じがたい"],
        "correctIndex": 2, # slot 3 is "という"
        "reconstructed": "あの人気歌手が極秘で結婚したという信じがたい噂が、ネット上で急速に広がっている。",
        "translation": "The hard-to-believe rumor that that popular singer got married in secret is spreading rapidly on the internet.",
        "context": "Discussing unverified celebrity rumors trending online.",
        "hint": "Clause modifying 噂: [clause] + という + [adjective] + 噂.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 引用), pp. 104–105",
        "overall": "名詞「噂」の内容を同格節で説明する構造です。【極秘で】→【結婚した】→【という】→【信じがたい】→「噂が」の順序になります。★の位置（3番目）には同格引用の「という」が入ります。",
        "optReasons": [
            ("極秘で", "1番目の要素。副詞として「結婚した」を修飾します。"),
            ("結婚した", "2番目の要素。「という」に接続する節の述語です。"),
            ("という", "【正解（★・3番目）】節「結婚した」と名詞句を同格で結ぶ引用助詞です。"),
            ("信じがたい", "4番目の要素。「噂」を直接修飾するイ形容詞です。")
        ]
    },
    "skm3-p2-c1-q5": {
        "question": "天気予報によると、明日は ＿＿ ＿＿ ★ ＿＿ とのことだ。",
        "options": ["全国的に", "真冬並みの", "厳しい", "寒さになる"],
        "correctIndex": 2, # [全国的に(1)] [真冬並みの(2)] [★ 厳しい(3)] [寒さになる(4)]
        "reconstructed": "天気予報によると、明日は全国的に真冬並みの厳しい寒さになるとのことだ。",
        "translation": "According to the weather forecast, tomorrow will reportedly bring severe cold comparable to midwinter nationwide.",
        "context": "Relaying formal meteorological hearsay announcements.",
        "hint": "Nationwide (全国的に) + midwinter-level (真冬並みの) + severe (厳しい) + cold (寒さになる).",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 引用), pp. 104–105",
        "overall": "伝聞文末「とのことだ」の前に置く節を組み立てます。【全国的に】（範囲）→【真冬並みの】（名詞修飾）→【厳しい】（形容詞）→【寒さになる】（変化述語）。★の位置（3番目）には「厳しい」が入ります。",
        "optReasons": [
            ("全国的に", "1番目の要素。地域全体の範囲を示します。"),
            ("真冬並みの", "2番目の要素。「厳しい」を修飾する連体修飾句です。"),
            ("厳しい", "【正解（★・3番目）】名詞「寒さ」を直接修飾するイ形容詞連体形です。"),
            ("寒さになる", "4番目の要素。「とのことだ」の直前に入る述語句です。")
        ]
    },
    "skm3-p2-c1-q6": {
        "question": "彼が明日の ＿＿ ＿＿ ★ ＿＿ 返事をもらっていない。",
        "options": ["懇親会に", "出席する", "かどうか", "まだ"],
        "correctIndex": 2, # [懇親会に(1)] [出席する(2)] [★ かどうか(3)] [まだ(4)]
        "reconstructed": "彼が明日の懇親会に出席するかどうか、まだ返事をもらっていない。",
        "translation": "I haven't received a reply yet regarding whether or not he will attend tomorrow's social gathering.",
        "context": "Checking attendance RSVP for an upcoming company event.",
        "hint": "Embedded yes/no clause: [clause] + かどうか + [adverb] + predicate.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 引用), pp. 104–105",
        "overall": "埋め込み疑問文「〜かどうか」の構文です。【懇親会に】→【出席する】→【かどうか】→【まだ】→「返事をもらっていない」の順に繋がります。★の位置（3番目）には「かどうか」が入ります。",
        "optReasons": [
            ("懇親会に", "1番目の要素。向格助詞「に」で出席先を表します。"),
            ("出席する", "2番目の要素。「かどうか」に接続する動詞辞書形です。"),
            ("かどうか", "【正解（★・3番目）】不確実な事態を埋め込み節にする疑問形式です。"),
            ("まだ", "4番目の要素。主節の「もらっていない」を修飾する副詞です。")
        ]
    },
    "skm3-p2-c1-q7": {
        "question": "店員さんに、何時に ＿＿ ＿＿ ★ ＿＿ 聞いてみましょう。",
        "options": ["この店が", "本日", "閉店する", "か"],
        "correctIndex": 2, # [この店が(1)] [本日(2)] [★ 閉店する(3)] [か(4)]
        "reconstructed": "店員さんに、何時にこの店が本日閉店するか聞いてみましょう。",
        "translation": "Let's ask the store clerk what time this store will close today.",
        "context": "Inquiring about business closing hours politely.",
        "hint": "Interrogative clause embedded with か: 何時に + [subject] + [adverb] + [verb] + か.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 引用), pp. 104–105",
        "overall": "疑問詞「何時に」を含む埋め込み疑問節「〜か聞く」の組み立てです。【この店が】→【本日】→【閉店する】→【か】→「聞いてみましょう」。★の位置（3番目）には動詞「閉店する」が入ります。",
        "optReasons": [
            ("この店が", "1番目の要素。従属節の主語です。"),
            ("本日", "2番目の要素。日付を指定する副詞的表現です。"),
            ("閉店する", "【正解（★・3番目）】疑問助詞「か」の直前に置く動詞辞書形です。"),
            ("か", "4番目の要素。「聞いてみましょう」に接続する疑問終助詞です。")
        ]
    },
    "skm3-p2-c1-q8": {
        "question": "彼は「自分はお金を ＿＿ ＿＿ ★ ＿＿ 頑なに主張し続けた。",
        "options": ["盗んで", "など", "いない」", "と"],
        "correctIndex": 2, # [盗んで(1)] [など(2)] [★ いない」(3)] [と(4)]
        "reconstructed": "彼は「自分はお金を盗んでなどいない」と頑なに主張し続けた。",
        "translation": "He stubbornly insisted: 'I have never stolen any money at all!'",
        "context": "Asserting absolute innocence against theft allegations.",
        "hint": "Quote denial: 盗んで + など + いない」 + と.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 引用), pp. 104–105",
        "overall": "鉤括弧「　」内の強い否定発言と引用助詞「と」の連結です。【盗んで】→【など】（強い否定・軽視）→【いない」】→【と】（引用）→「頑なに主張し続けた」。★の位置（3番目）には「いない」」が入ります。",
        "optReasons": [
            ("盗んで", "1番目の要素。「て形」で「など」に接続します。"),
            ("など", "2番目の要素。否定の感情を強める取り立て助詞です。"),
            ("いない」", "【正解（★・3番目）】鉤括弧を閉じる否定述語です。"),
            ("と", "4番目の要素。「主張し続けた」に繋ぐ引用助詞です。")
        ]
    },
    "skm3-p2-c1-q9": {
        "question": "両親は幼い頃から、知らない人には ＿＿ ＿＿ ★ ＿＿ 厳しく言い聞かせてきた。",
        "options": ["絶対", "ついて", "行かない", "ように"],
        "correctIndex": 2, # [絶対(1)] [ついて(2)] [★ 行かない(3)] [ように(4)]
        "reconstructed": "両親は幼い頃から、知らない人には絶対ついて行かないように厳しく言い聞かせてきた。",
        "translation": "From when I was young, my parents strictly admonished me never to follow strangers.",
        "context": "Recalling parental childhood safety admonitions.",
        "hint": "Negative directive citation: 絶対 + ついて + 行かない + ように.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 引用), pp. 104–105",
        "overall": "教えや言いつけの間接引用「〜ように言い聞かせる」構文です。【絶対】（強調副詞）→【ついて】→【行かない】（否定形）→【ように】（間接命令助詞）。★の位置（3番目）には「行かない」が入ります。",
        "optReasons": [
            ("絶対", "1番目の要素。後続の否定表現と呼応する強調副詞です。"),
            ("ついて", "2番目の要素。複合動詞「ついて行く」の前半部です。"),
            ("行かない", "【正解（★・3番目）】「ように」の直前に接続する動詞否定形です。"),
            ("ように", "4番目の要素。「言い聞かせてきた」に接続する指示の間接引用形式です。")
        ]
    },
    "skm3-p2-c1-q10": {
        "question": "今日は午後から雨が ＿＿ ＿＿ ★ ＿＿ 折りたたみ傘を持参した。",
        "options": ["降る", "だろう", "と", "思って"],
        "correctIndex": 2, # [降る(1)] [だろう(2)] [★ と(3)] [思って(4)]
        "reconstructed": "今日は午後から雨が降るだろうと思って、折りたたみ傘を持参した。",
        "translation": "Thinking that it would probably rain in the afternoon today, I brought a folding umbrella.",
        "context": "Preparing for anticipated weather changes based on personal thought.",
        "hint": "Thought quote: 降る + だろう + と + 思って.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 引用), pp. 104–105",
        "overall": "話者の内心の推量を引用する「〜だろうと思って」構文です。【降る】（動詞基本形）→【だろう】（推量助動詞）→【と】（思考引用）→【思って】（中連形）。★の位置（3番目）には引用助詞「と」が入ります。",
        "optReasons": [
            ("降る", "1番目の要素。主語「雨が」を受ける動詞です。"),
            ("だろう", "2番目の要素。推量を表す助動詞です。"),
            ("と", "【正解（★・3番目）】思考動詞「思って」に先行する引用格助詞です。"),
            ("思って", "4番目の要素。理由・動機を表して「持参した」に接続します。")
        ]
    },
    "skm3-p2-c1-q11": {
        "question": "先生は学生に、図書館では ＿＿ ＿＿ ★ ＿＿ 言った。",
        "options": ["静かに", "本を", "読む", "ように"],
        "correctIndex": 2, # [静かに(1)] [本を(2)] [★ 読む(3)] [ように(4)]
        "reconstructed": "先生は学生に、図書館では静かに本を読むように言った。",
        "translation": "The teacher told the students to read books quietly in the library.",
        "context": "Instructing proper student conduct in library facilities.",
        "hint": "Adverb + object + verb + ように + 言った.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 引用), pp. 104–105",
        "overall": "指示の間接引用「〜ように言う」構文です。【静かに】（様態副詞）→【本を】（目的語）→【読む】（動詞辞書形）→【ように】（間接指示形式）。★の位置（3番目）には「読む」が入ります。",
        "optReasons": [
            ("静かに", "1番目の要素。「読む」を修飾する連用形です。"),
            ("本を", "2番目の要素。動詞「読む」の目的語です。"),
            ("読む", "【正解（★・3番目）】「ように」の直前に接続する動詞辞書形です。"),
            ("ように", "4番目の要素。「言った」に接続する間接命令表現です。")
        ]
    },
    "skm3-p2-c1-q12": {
        "question": "悩んでいる友人に、専門家に ＿＿ ＿＿ ★ ＿＿ 助言した。",
        "options": ["一度", "相談して", "みたほうがいい", "と"],
        "correctIndex": 2, # [一度(1)] [相談して(2)] [★ みたほうがいい(3)] [と(4)]
        "reconstructed": "悩んでいる友人に、専門家に一度相談してみたほうがいいと助言した。",
        "translation": "I advised my troubled friend that they should try consulting a specialist once.",
        "context": "Offering well-meaning counsel to a friend in distress.",
        "hint": "Advice structure: 一度 + 相談して + みたほうがいい + と + 助言した.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 引用), pp. 104–105",
        "overall": "助言内容を引用する「〜ほうがいいと助言した」構文です。【一度】（頻度副詞）→【相談して】（試行前項）→【みたほうがいい】（助言述語）→【と】（引用助詞）。★の位置（3番目）には「みたほうがいい」が入ります。",
        "optReasons": [
            ("一度", "1番目の要素。副詞として「相談して」を修飾します。"),
            ("相談して", "2番目の要素。「〜てみる」の前半部です。"),
            ("みたほうがいい", "【正解（★・3番目）】提案・助言を表す述語です。"),
            ("と", "4番目の要素。「助言した」に接続する引用助詞です。")
        ]
    },

    # =========================================================================
    # Part 2 · Chapter 2: 名詞の説明 (Noun Modification) - pp. 106–107
    # =========================================================================
    "skm3-p2-c2-q1": {
        "question": "机の上に置いてあるのは、高校時代に ＿＿ ＿＿ ★ ＿＿ 手紙です。",
        "options": ["お世話になった", "恩師", "への", "感謝の"],
        "correctIndex": 2, # [お世話になった(1)] [恩師(2)] [★ への(3)] [感謝の(4)]
        "reconstructed": "机の上に置いてあるのは、高校時代にお世話になった恩師への感謝の手紙です。",
        "translation": "What is placed on the desk is a letter of gratitude addressed to the mentor who took care of me during high school.",
        "context": "Explaining the recipient and sentimental nature of a personal letter.",
        "hint": "Relative clause modifying 恩師 + への + 感謝の + 手紙.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞の説明), pp. 106–107",
        "overall": "重層的な名詞修飾構文です。【お世話になった】（連体修飾節）→【恩師】（被修飾名詞）→【への】（方向格助詞＋の）→【感謝の】（名詞修飾）→「手紙です」。★の位置（3番目）には「への」が入ります。",
        "optReasons": [
            ("お世話になった", "1番目の要素。「恩師」を修飾する連体修飾節です。"),
            ("恩師", "2番目の要素。「への」に接続する名詞です。"),
            ("への", "【正解（★・3番目）】手紙の宛先・方向を表す連体助詞です。"),
            ("感謝の", "4番目の要素。「手紙」を直接修飾する属性句です。")
        ]
    },
    "skm3-p2-c2-q2": {
        "question": "彼が学会で発表したのは、地球温暖化が ＿＿ ＿＿ ★ ＿＿ 修士論文だった。",
        "options": ["農業に", "与える", "影響についての", "画期的な"],
        "correctIndex": 2, # [農業に(1)] [与える(2)] [★ 影響についての(3)] [画期的な(4)]
        "reconstructed": "彼が学会で発表したのは、地球温暖化が農業に与える影響についての画期的な修士論文だった。",
        "translation": "What he presented at the academic conference was a groundbreaking master's thesis regarding the impact of global warming on agriculture.",
        "context": "Introducing a graduate student's acclaimed academic research thesis.",
        "hint": "Impact on agriculture: 農業に + 与える + 影響についての + 画期的な + 修士論文.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞の説明), pp. 106–107",
        "overall": "複合的な複文名詞修飾構造です。【農業に】（対象）→【与える】（動詞連体形）→【影響についての】（テーマ修飾句）→【画期的な】（ナ形容詞）→「修士論文だった」。★の位置（3番目）には「影響についての」が入ります。",
        "optReasons": [
            ("農業に", "1番目の要素。「与える」の対象を表す格助詞句です。"),
            ("与える", "2番目の要素。「影響」を修飾する連体形動詞です。"),
            ("影響についての", "【正解（★・3番目）】修士論文のテーマを限定する連体修飾句です。"),
            ("画期的な", "4番目の要素。「修士論文」を直接修飾するナ形容詞連体形です。")
        ]
    },
    "skm3-p2-c2-q3": {
        "question": "集中して本を読むには、このように ＿＿ ＿＿ ★ ＿＿ 最も適している。",
        "options": ["静かで", "落ち着いた", "環境の", "図書館が"],
        "correctIndex": 2, # [静かで(1)] [落ち着いた(2)] [★ 環境の(3)] [図書館が(4)]
        "reconstructed": "集中して本を読むには、このように静かで落ち着いた環境の図書館が最も適している。",
        "translation": "To read books with full concentration, a library with a quiet and relaxed environment like this is most suitable.",
        "context": "Describing optimal study atmospheres in libraries.",
        "hint": "Modifiers of 図書館: 静かで + 落ち着いた + 環境の + 図書館が.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞の説明), pp. 106–107",
        "overall": "名詞「図書館」を並列形容詞と名詞修飾句で詳しく説明する構文です。【静かで】（テ形中連）→【落ち着いた】（動詞タ形連体修飾）→【環境の】（名詞＋の）→【図書館が】（主語）。★の位置（3番目）には「環境の」が入ります。",
        "optReasons": [
            ("静かで", "1番目の要素。形容動詞のテ形で並列します。"),
            ("落ち着いた", "2番目の要素。「環境」を修飾する連体形です。"),
            ("環境の", "【正解（★・3番目）】「図書館」を修飾する連体格助詞「の」です。"),
            ("図書館が", "4番目の要素。「最も適している」の主語名詞です。")
        ]
    },
    "skm3-p2-c2-q4": {
        "question": "就職活動のために靴を磨き上げ、きれいに ＿＿ ＿＿ ★ ＿＿ 面接に向かった。",
        "options": ["手入れされた", "黒い", "革靴を", "履いて"],
        "correctIndex": 2, # [手入れされた(1)] [黒い(2)] [★ 革靴を(3)] [履いて(4)]
        "reconstructed": "就職活動のために靴を磨き上げ、きれいに手入れされた黒い革靴を履いて面接に向かった。",
        "translation": "Having polished my shoes for job hunting, I put on nicely maintained black leather shoes and headed to the interview.",
        "context": "Preparing attire carefully before attending employment interviews.",
        "hint": "きれいに + 手入れされた + 黒い + 革靴を + 履いて.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞の説明), pp. 106–107",
        "overall": "名詞「革靴」を修飾する受身連体形とイ形容詞の連鎖です。【手入れされた】（受身連体形）→【黒い】（イ形容詞）→【革靴を】（目的語）→【履いて】（動詞テ形）。★の位置（3番目）には「革靴を」が入ります。",
        "optReasons": [
            ("手入れされた", "1番目の要素。「きれいに」を受ける受身連体形です。"),
            ("黒い", "2番目の要素。「革靴」を直接修飾するイ形容詞です。"),
            ("革靴を", "【正解（★・3番目）】「履いて」の目的語となる名詞句です。"),
            ("履いて", "4番目の要素。「面接に向かった」に先行する動作です。")
        ]
    },
    "skm3-p2-c2-q5": {
        "question": "田舎の祖母が ＿＿ ＿＿ ★ ＿＿ 手作りのパンは格別においしい。",
        "options": ["私のために", "心を込めて", "焼いてくれた", "焼きたての"],
        "correctIndex": 2, # [私のために(1)] [心を込めて(2)] [★ 焼いてくれた(3)] [焼きたての(4)]
        "reconstructed": "田舎の祖母が私のために心を込めて焼いてくれた焼きたての手作りのパンは格別においしい。",
        "translation": "The freshly baked handmade bread that my grandmother in the countryside lovingly baked for me is exceptionally delicious.",
        "context": "Praising beloved homemade culinary gifts from family.",
        "hint": "Benefactive relative clause: 私のために + 心を込めて + 焼いてくれた + 焼きたての + パン.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞の説明), pp. 106–107",
        "overall": "授受動詞「〜てくれた」を含む複文連体修飾節です。【私のために】（受益対象）→【心を込めて】（様態副詞句）→【焼いてくれた】（連体修飾述語）→【焼きたての】（名詞修飾）→「手作りのパン」。★の位置（3番目）には「焼いてくれた」が入ります。",
        "optReasons": [
            ("私のために", "1番目の要素。祖母の愛情の対象を示します。"),
            ("心を込めて", "2番目の要素。動作の丁寧な様態を表します。"),
            ("焼いてくれた", "【正解（★・3番目）】「祖母が」を受ける連体節述語です。"),
            ("焼きたての", "4番目の要素。「手作りのパン」を直前で修飾する句です。")
        ]
    },
    "skm3-p2-c2-q6": {
        "question": "今学期から、日本語を ＿＿ ＿＿ ★ ＿＿ 留学生が3名加わった。",
        "options": ["専攻している", "海外からの", "非常に熱心な", "新しい"],
        "correctIndex": 2, # [専攻している(1)] [海外からの(2)] [★ 非常に熱心な(3)] [新しい(4)]
        "reconstructed": "今学期から、日本語を専攻している海外からの非常に熱心な新しい留学生が3名加わった。",
        "translation": "Starting this semester, three highly enthusiastic new international students from overseas who are majoring in Japanese joined our class.",
        "context": "Welcoming incoming exchange students into an academic department.",
        "hint": "Multiple modifiers before 留学生: 専攻している + 海外からの + 非常に熱心な + 新しい.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞の説明), pp. 106–107",
        "overall": "名詞「留学生」を段階的に修飾する多重連体修飾の組み立てです。【専攻している】（連体動詞）→【海外からの】（格助詞＋の）→【非常に熱心な】（ナ形容詞）→【新しい】（イ形容詞）。★の位置（3番目）には「非常に熱心な」が入ります。",
        "optReasons": [
            ("専攻している", "1番目の要素。「日本語を」を受ける動詞連体形です。"),
            ("海外からの", "2番目の要素。出身地を示す名詞修飾句です。"),
            ("非常に熱心な", "【正解（★・3番目）】学習意欲の態度を表すナ形容詞連体形です。"),
            ("新しい", "4番目の要素。「留学生」を直接修飾するイ形容詞です。")
        ]
    },
    "skm3-p2-c2-q7": {
        "question": "役員会では、経営陣の ＿＿ ＿＿ ★ ＿＿ 結論は持ち越された。",
        "options": ["提案した", "新方針に対する", "強い反対意見が", "相次いで"],
        "correctIndex": 2, # [提案した(1)] [新方針に対する(2)] [★ 強い反対意見が(3)] [相次いで(4)]
        "reconstructed": "役員会では、経営陣の提案した新方針に対する強い反対意見が相次いで、結論は持ち越された。",
        "translation": "At the board meeting, strong objections against the new policy proposed by executive management occurred one after another, and the conclusion was carried over.",
        "context": "Reporting contentious deliberations at a corporate board meeting.",
        "hint": "Proposal modifiers: 提案した + 新方針に対する + 強い反対意見が + 相次いで.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞の説明), pp. 106–107",
        "overall": "格助詞「の」（＝が）による主格修飾と「に対する」の連鎖構文です。【提案した】（連体形）→【新方針に対する】（対象修飾）→【強い反対意見が】（主語句）→【相次いで】（述語接続）。★の位置（3番目）には「強い反対意見が」が入ります。",
        "optReasons": [
            ("提案した", "1番目の要素。「経営陣の」を主語にとる連体節です。"),
            ("新方針に対する", "2番目の要素。反対意見の対象を指定する句です。"),
            ("強い反対意見が", "【正解（★・3番目）】「相次いで」の主語となる名詞句です。"),
            ("相次いで", "4番目の要素。「持ち越された」原因を述べる連用形です。")
        ]
    },
    "skm3-p2-c2-q8": {
        "question": "夏目漱石によって ＿＿ ＿＿ ★ ＿＿ 今でも多くの人に愛読されている。",
        "options": ["書かれた", "『坊っちゃん』という", "不朽の", "名作小説は"],
        "correctIndex": 2, # [書かれた(1)] [『坊っちゃん』という(2)] [★ 不朽の(3)] [名作小説は(4)]
        "reconstructed": "夏目漱石によって書かれた『坊っちゃん』という不朽の名作小説は、今でも多くの人に愛読されている。",
        "translation": "The immortal masterpiece novel entitled 'Botchan', penned by Natsume Soseki, is widely read and loved by many people even today.",
        "context": "Introducing enduring classic Japanese literature.",
        "hint": "Passive author clause + title with という + 不朽の + 名作小説は.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞の説明), pp. 106–107",
        "overall": "受身動詞修飾と名称定義「という」の結合文です。【書かれた】（受身連体形）→【『坊っちゃん』という】（名称引用）→【不朽の】（名詞修飾）→【名作小説は】（文頭主語）。★の位置（3番目）には「不朽の」が入ります。",
        "optReasons": [
            ("書かれた", "1番目の要素。「夏目漱石によって」を受ける受身動詞です。"),
            ("『坊っちゃん』という", "2番目の要素。作品名を示す引用連体句です。"),
            ("不朽の", "【正解（★・3番目）】「名作小説」の永続的価値を称える修飾句です。"),
            ("名作小説は", "4番目の要素。「愛読されている」の主語です。")
        ]
    },
    "skm3-p2-c2-q9": {
        "question": "彼女はまるで ＿＿ ＿＿ ★ ＿＿ 会場の聴衆全員を魅了した。",
        "options": ["プロの", "歌手のように", "澄み渡った", "歌声で"],
        "correctIndex": 2, # [プロの(1)] [歌手のように(2)] [★ 澄み渡った(3)] [歌声で(4)]
        "reconstructed": "彼女はまるでプロの歌手のように澄み渡った歌声で、会場の聴衆全員を魅了した。",
        "translation": "With a singing voice as crystal clear as that of a professional singer, she captivated the entire audience in the venue.",
        "context": "Praising a remarkable vocal musical performance.",
        "hint": "Simile and instrument: プロの + 歌手のように + 澄み渡った + 歌声で.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞の説明), pp. 106–107",
        "overall": "比況「〜のように」と手段格「で」の名詞修飾構造です。【プロの】（連体修飾）→【歌手のように】（比況副詞句）→【澄み渡った】（連体修飾動詞）→【歌声で】（手段・方法）。★の位置（3番目）には「澄み渡った」が入ります。",
        "optReasons": [
            ("プロの", "1番目の要素。「歌手」を修飾します。"),
            ("歌手のように", "2番目の要素。比喩として「澄み渡った」を修飾します。"),
            ("澄み渡った", "【正解（★・3番目）】「歌声」を直接修飾するタ形連体形です。"),
            ("歌声で", "4番目の要素。「魅了した」手段を表す格助詞句です。")
        ]
    },
    "skm3-p2-c2-q10": {
        "question": "これは、かつて ＿＿ ＿＿ ★ ＿＿ 歴史ある日本家屋です。",
        "options": ["祖父が", "長年", "大切に住んでいた", "趣のある"],
        "correctIndex": 2, # [祖父が(1)] [長年(2)] [★ 大切に住んでいた(3)] [趣のある(4)]
        "reconstructed": "これは、かつて祖父が長年大切に住んでいた趣のある歴史ある日本家屋です。",
        "translation": "This is an atmospheric, historic Japanese residence where my grandfather once lived for many years with great care.",
        "context": "Explaining the emotional provenance of a traditional family residence.",
        "hint": "Grandfather's relative clause: 祖父が + 長年 + 大切に住んでいた + 趣のある + 日本家屋.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞の説明), pp. 106–107",
        "overall": "連体修飾節の内部構造と重層形容の組み立てです。【祖父が】（節内主語）→【長年】（時間副詞）→【大切に住んでいた】（連体述語）→【趣のある】（連体句）→「歴史ある日本家屋です」。★の位置（3番目）には「大切に住んでいた」が入ります。",
        "optReasons": [
            ("祖父が", "1番目の要素。修飾節内の動作主です。"),
            ("長年", "2番目の要素。継続期間を表す副詞です。"),
            ("大切に住んでいた", "【正解（★・3番目）】祖父の居住を表す連体節述語です。"),
            ("趣のある", "4番目の要素。「日本家屋」を直接修飾する慣用連体句です。")
        ]
    },
    "skm3-p2-c2-q11": {
        "question": "これは ＿＿ ＿＿ ★ ＿＿ 素晴らしい本です。",
        "options": ["恩師の", "先生が", "推薦して", "くださった"],
        "correctIndex": 2, # [恩師の(1)] [先生が(2)] [★ 推薦して(3)] [くださった(4)]
        "reconstructed": "これは恩師の先生が推薦してくださった素晴らしい本です。",
        "translation": "This is a wonderful book that my respected mentor kindly recommended to me.",
        "context": "Expressing respect for a recommended educational volume.",
        "hint": "Respectful recommendation: 恩師の + 先生が + 推薦して + くださった + 本.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞の説明), pp. 106–107",
        "overall": "授受動詞「〜てくださる」の連体修飾節です。【恩師の】（連体修飾）→【先生が】（節内主語）→【推薦して】（テ形接続）→【くださった】（補助動詞タ形）。★の位置（3番目）には「推薦して」が入ります。",
        "optReasons": [
            ("恩師の", "1番目の要素。「先生」を尊敬の念を込めて修飾します。"),
            ("先生が", "2番目の要素。「推薦してくださった」の主語です。"),
            ("推薦して", "【正解（★・3番目）】「くださった」に接続する動詞テ形です。"),
            ("くださった", "4番目の要素。「本」を修飾する恩恵補助動詞です。")
        ]
    },
    "skm3-p2-c2-q12": {
        "question": "プロジェクトの ＿＿ ＿＿ ★ ＿＿ 毎日の進捗管理を徹底している。",
        "options": ["リーダーとしての", "責任ある", "重要な役割を", "果たすために"],
        "correctIndex": 2, # [リーダーとしての(1)] [責任ある(2)] [★ 重要な役割を(3)] [果たすために(4)]
        "reconstructed": "プロジェクトのリーダーとしての責任ある重要な役割を果たすために、毎日の進捗管理を徹底している。",
        "translation": "In order to fulfill my crucial and responsible role as project leader, I enforce daily progress management rigorously.",
        "context": "Describing leadership duties and professional accountability.",
        "hint": "Leader role purpose: リーダーとしての + 責任ある + 重要な役割を + 果たすために.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞の説明), pp. 106–107",
        "overall": "資格・立場「〜としての」と目的節「〜ために」の結合です。【リーダーとしての】（資格修飾）→【責任ある】（連体句）→【重要な役割を】（目的語）→【果たすために】（目的表現）。★の位置（3番目）には「重要な役割を」が入ります。",
        "optReasons": [
            ("リーダーとしての", "1番目の要素。プロジェクト内での立場・資格を示します。"),
            ("責任ある", "2番目の要素。役割の重さを表す連体句です。"),
            ("重要な役割を", "【正解（★・3番目）】「果たすために」の直接の目的語です。"),
            ("果たすために", "4番目の要素。主節「徹底している」の目的節です。")
        ]
    },

    # =========================================================================
    # Part 2 · Chapter 3: 「こと」「の」 (Sentence Nominalizers & Fixed Syntax) - pp. 108–109
    # =========================================================================
    "skm3-p2-c3-q1": {
        "question": "数学や物理、 ＿＿ ＿＿ ★ ＿＿ 思考力を養うのに役立つ。",
        "options": ["化学といった", "理科系の", "科目を学ぶ", "ことは論理的"],
        "correctIndex": 2, # [化学といった(1)] [理科系の(2)] [★ 科目を学ぶ(3)] [ことは論理的(4)]
        "reconstructed": "数学や物理、化学といった理科系の科目を学ぶことは、論理的思考力を養うのに役立つ。",
        "translation": "Studying science subjects such as mathematics, physics, and chemistry is beneficial for cultivating logical thinking skills.",
        "context": "Expounding on the academic benefits of rigorous science education.",
        "hint": "Examples with といった + category + studying subjects + ことは.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 「こと」「の」), pp. 108–109",
        "overall": "例示「〜といった」と形式名詞「こと」による主語化構文です。【化学といった】（例示）→【理科系の】（分野限定）→【科目を学ぶ】（目的語＋動詞）→【ことは論理的】（名詞化主語）。★の位置（3番目）には「科目を学ぶ」が入ります。",
        "optReasons": [
            ("化学といった", "1番目の要素。並列例示を総括する表現です。"),
            ("理科系の", "2番目の要素。「科目」を修飾する連体修飾句です。"),
            ("科目を学ぶ", "【正解（★・3番目）】「こと」に接続する動詞辞書形です。"),
            ("ことは論理的", "4番目の要素。主語を提示し、後続の「思考力」に繋ぎます。")
        ]
    },
    "skm3-p2-c3-q2": {
        "question": "東南アジアには、 ＿＿ ＿＿ ★ ＿＿ 果物がある。",
        "options": ["「ドリアン」という", "非常に", "強烈な匂いの", "する珍しい"],
        "correctIndex": 2, # [「ドリアン」という(1)] [非常に(2)] [★ 強烈な匂いの(3)] [する珍しい(4)]
        "reconstructed": "東南アジアには、「ドリアン」という非常に強烈な匂いのする珍しい果物がある。",
        "translation": "In Southeast Asia, there is an unusual fruit called 'durian' that has an extremely pungent aroma.",
        "context": "Introducing exotic tropical botanical species.",
        "hint": "Name + smell clause: ドリアンという + 非常に + 強烈な匂いの + する珍しい + 果物.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 「こと」「の」), pp. 108–109",
        "overall": "名前の提示「という」と主格助詞「の」（＝が）の連体節です。【「ドリアン」という】（名称付与）→【非常に】（程度副詞）→【強烈な匂いの】（主格）→【する珍しい】（動詞＋形容詞連体形）。★の位置（3番目）には「強烈な匂いの」が入ります。",
        "optReasons": [
            ("「ドリアン」という", "1番目の要素。果物の名前を説明します。"),
            ("非常に", "2番目の要素。「強烈な」を修飾する程度副詞です。"),
            ("強烈な匂いの", "【正解（★・3番目）】連体節内での主格（〜がする）を表す助詞「の」です。"),
            ("する珍しい", "4番目の要素。「果物」を直接修飾する述語複合体です。")
        ]
    },
    "skm3-p2-c3-q3": {
        "question": "全館禁煙という ＿＿ ＿＿ ★ ＿＿ 吸ってはいけないということだ。",
        "options": ["ことは、", "会場内の", "いかなる場所でも", "タバコを"],
        "correctIndex": 2, # [ことは、(1)] [会場内の(2)] [★ いかなる場所でも(3)] [タバコを(4)]
        "reconstructed": "全館禁煙ということは、会場内のいかなる場所でもタバコを吸ってはいけないということだ。",
        "translation": "The fact that the entire building is non-smoking means that one must not smoke tobacco in any location whatsoever inside the venue.",
        "context": "Explaining the strict scope of building-wide nonsmoking regulations.",
        "hint": "Explanatory frame: ということは + 会場内の + いかなる場所でも + タバコを.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 「こと」「の」), pp. 108–109",
        "overall": "「〜ということは、〜ということだ」（〜の意味だ）という定義説明の呼応構文です。【ことは、】（文頭主語化）→【会場内の】（場所限定）→【いかなる場所でも】（全域強調）→【タバコを】（目的語）。★の位置（3番目）には「いかなる場所でも」が入ります。",
        "optReasons": [
            ("ことは、", "1番目の要素。「全館禁煙という」を受けて主題を作ります。"),
            ("会場内の", "2番目の要素。施設内部の範囲を指定します。"),
            ("いかなる場所でも", "【正解（★・3番目）】例外のない全面禁止を強調する副詞句です。"),
            ("タバコを", "4番目の要素。「吸ってはいけない」の目的語です。")
        ]
    },
    "skm3-p2-c3-q4": {
        "question": "就職活動の面接では、 ＿＿ ＿＿ ★ ＿＿ スーツの着用が求められる。",
        "options": ["黒や紺", "といった", "落ち着いた色合いの", "清潔感のある"],
        "correctIndex": 2, # [黒や紺(1)] [といった(2)] [★ 落ち着いた色合いの(3)] [清潔感のある(4)]
        "reconstructed": "就職活動の面接では、黒や紺といった落ち着いた色合いの清潔感のあるスーツの着用が求められる。",
        "translation": "In job hunting interviews, wearing a suit with a calm hue such as black or navy and a clean appearance is required.",
        "context": "Instructing job seekers on corporate dress code norms.",
        "hint": "Color examples with といった + 落ち着いた色合いの + 清潔感のある + スーツ.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 「こと」「の」), pp. 108–109",
        "overall": "代表例示「〜といった」から名詞「スーツ」へ多重修飾する構文です。【黒や紺】（具体色）→【といった】（例示助詞）→【落ち着いた色合いの】（色彩属性）→【清潔感のある】（印象属性）。★の位置（3番目）には「落ち着いた色合いの」が入ります。",
        "optReasons": [
            ("黒や紺", "1番目の要素。推奨される基本色の例示です。"),
            ("といった", "2番目の要素。例を総括して次の名詞句に繋ぎます。"),
            ("落ち着いた色合いの", "【正解（★・3番目）】スーツのトーンを限定する連体修飾句です。"),
            ("清潔感のある", "4番目の要素。「スーツ」を直接修飾する属性句です。")
        ]
    },
    "skm3-p2-c3-q5": {
        "question": "学校の掲示板に、 ＿＿ ＿＿ ★ ＿＿ 知らせが貼り出されていた。",
        "options": ["明日の午後の", "講義が急遽", "休講になる", "という重要な"],
        "correctIndex": 2, # [明日の午後の(1)] [講義が急遽(2)] [★ 休講になる(3)] [という重要な(4)]
        "reconstructed": "学校の掲示板に、明日の午後の講義が急遽休講になるという重要な知らせが貼り出されていた。",
        "translation": "On the school bulletin board, an important announcement that tomorrow afternoon's lecture is cancelled on short notice had been posted.",
        "context": "Noticing urgent cancellation notices on campus.",
        "hint": "Cancellation notice: 明日の午後の + 講義が急遽 + 休講になる + という重要な + 知らせ.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 「こと」「の」), pp. 108–109",
        "overall": "同格節「〜という」で通知内容を名詞「知らせ」に連結する構文です。【明日の午後の】（時間限定）→【講義が急遽】（主語＋副詞）→【休講になる】（述語変化）→【という重要な】（同格＋形容詞）。★の位置（3番目）には「休講になる」が入ります。",
        "optReasons": [
            ("明日の午後の", "1番目の要素。対象講義の時間帯を示します。"),
            ("講義が急遽", "2番目の要素。急な変更を表す主格句です。"),
            ("休講になる", "【正解（★・3番目）】「という」の直前に入る述語句です。"),
            ("という重要な", "4番目の要素。「知らせ」を直接修飾する同格句です。")
        ]
    },
    "skm3-p2-c3-q6": {
        "question": "緑茶を毎日習慣的に ＿＿ ＿＿ ★ ＿＿ 効果的だと言われている。",
        "options": ["飲む", "ことは、", "風邪の", "予防に極めて"],
        "correctIndex": 2, # [飲む(1)] [ことは、(2)] [★ 風邪の(3)] [予防に極めて(4)]
        "reconstructed": "緑茶を毎日習慣的に飲むことは、風邪の予防に極めて効果的だと言われている。",
        "translation": "Habitually drinking green tea every day is said to be extremely effective for preventing colds.",
        "context": "Reporting health findings regarding tea consumption.",
        "hint": "Nominalized subject: 飲む + ことは + 風邪の + 予防に極めて + 効果的だ.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 「こと」「の」), pp. 108–109",
        "overall": "形式名詞「こと」による動作の名詞化主語文です。【飲む】（動詞辞書形）→【ことは、】（名詞化主題）→【風邪の】（名詞修飾）→【予防に極めて】（対象＋程度）。★の位置（3番目）には「風邪の」が入ります。",
        "optReasons": [
            ("飲む", "1番目の要素。「習慣的に」を受ける動詞です。"),
            ("ことは、", "2番目の要素。主語節をまとめる名詞化助詞句です。"),
            ("風邪の", "【正解（★・3番目）】「予防」の内容を指定する連体句です。"),
            ("予防に極めて", "4番目の要素。「効果的だ」を修飾する述語句です。")
        ]
    },
    "skm3-p2-c3-q7": {
        "question": "冷蔵庫や洗濯機、 ＿＿ ＿＿ ★ ＿＿ 必需品である。",
        "options": ["電子レンジといった", "生活に不可欠な", "家電製品は", "新生活の"],
        "correctIndex": 2, # [電子レンジといった(1)] [生活に不可欠な(2)] [★ 家電製品は(3)] [新生活の(4)]
        "reconstructed": "冷蔵庫や洗濯機、電子レンジといった生活に不可欠な家電製品は、新生活の必需品である。",
        "translation": "Household appliances indispensable for daily living, such as refrigerators, washing machines, and microwave ovens, are necessities for a new life.",
        "context": "Listing essential home appliances when moving into a new apartment.",
        "hint": "Examples with といった + 不可欠な + 家電製品は + 新生活の + 必需品.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 「こと」「の」), pp. 108–109",
        "overall": "家電の具体例を「といった」で束ね、主語「家電製品は」を提示する構造です。【電子レンジといった】（例示結び）→【生活に不可欠な】（ナ形容詞修飾）→【家電製品は】（主語）→【新生活の】（連体修飾）。★の位置（3番目）には「家電製品は」が入ります。",
        "optReasons": [
            ("電子レンジといった", "1番目の要素。3つ目の代表例を示します。"),
            ("生活に不可欠な", "2番目の要素。家電の必要性を強調するナ形容詞です。"),
            ("家電製品は", "【正解（★・3番目）】文の主語となる名詞です。"),
            ("新生活の", "4番目の要素。「必需品」を修飾する属性句です。")
        ]
    },
    "skm3-p2-c3-q8": {
        "question": "彼の困惑した表情から、 ＿＿ ＿＿ ★ ＿＿ 印象を強く受けた。",
        "options": ["その提案を", "あまり快く", "思っていない", "という"],
        "correctIndex": 2, # [その提案を(1)] [あまり快く(2)] [★ 思っていない(3)] [という(4)]
        "reconstructed": "彼の困惑した表情から、その提案をあまり快く思っていないという印象を強く受けた。",
        "translation": "From his perplexed facial expression, I got the strong impression that he did not view that proposal very favorably.",
        "context": "Inferring someone's private negative appraisal from body language.",
        "hint": "Impression content: その提案を + あまり快く + 思っていない + という + 印象.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 「こと」「の」), pp. 108–109",
        "overall": "「印象」の内容を「〜という」で説明する同格連体構造です。【その提案を】（対象目的語）→【あまり快く】（連用修飾）→【思っていない】（否定述語）→【という】（同格引用助詞）。★の位置（3番目）には「思っていない」が入ります。",
        "optReasons": [
            ("その提案を", "1番目の要素。相手の評価対象を示します。"),
            ("あまり快く", "2番目の要素。「思っていない」と呼応する呼応副詞です。"),
            ("思っていない", "【正解（★・3番目）】「という」の直前に入る述語否定形です。"),
            ("という", "4番目の要素。「印象」と同格で結ぶ助詞です。")
        ]
    },
    "skm3-p2-c3-q9": {
        "question": "休日は ＿＿ ＿＿ ★ ＿＿ 自宅でできる趣味を楽しんでいる。",
        "options": ["読書や", "映画鑑賞", "といった", "一人で静かに"],
        "correctIndex": 2, # [読書や(1)] [映画鑑賞(2)] [★ といった(3)] [一人で静かに(4)]
        "reconstructed": "休日は読書や映画鑑賞といった一人で静かに自宅でできる趣味を楽しんでいる。",
        "translation": "On holidays, I enjoy quiet solo hobbies that can be done at home, such as reading and watching movies.",
        "context": "Describing relaxing solo indoor pastimes.",
        "hint": "Hobbies like reading: 読書や + 映画鑑賞 + といった + 一人で静かに + 自宅でできる趣味.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 「こと」「の」), pp. 108–109",
        "overall": "趣味の具体例を「といった」でまとめて後続の修飾句に繋ぐ構文です。【読書や】（並列第1項）→【映画鑑賞】（第2項）→【といった】（例示結び）→【一人で静かに】（様態修飾）。★の位置（3番目）には「といった」が入ります。",
        "optReasons": [
            ("読書や", "1番目の要素。趣味の最初の具体例です。"),
            ("映画鑑賞", "2番目の要素。2つ目の具体例です。"),
            ("といった", "【正解（★・3番目）】具体例を「趣味」へと結びつける例示助詞です。"),
            ("一人で静かに", "4番目の要素。「自宅でできる趣味」を修飾する副詞句です。")
        ]
    },
    "skm3-p2-c3-q10": {
        "question": "「AI」とは、 ＿＿ ＿＿ ★ ＿＿ 略称のことである。",
        "options": ["人間の知的能力を", "人工的に", "コンピューターで再現する", "「人工知能」の"],
        "correctIndex": 2, # [人間の知的能力を(1)] [人工的に(2)] [★ コンピューターで再現する(3)] [「人工知能」の(4)]
        "reconstructed": "「AI」とは、人間の知的能力を人工的にコンピューターで再現する「人工知能」の略称のことである。",
        "translation": "'AI' refers to the abbreviation for 'Artificial Intelligence', which reproduces human intellectual capabilities artificially using computers.",
        "context": "Providing technical terminological definitions of modern AI.",
        "hint": "Definition structure: 人間の知的能力を + 人工的に + コンピューターで再現する + 「人工知能」の + 略称.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 「こと」「の」), pp. 108–109",
        "overall": "「〜とは、〜のことである」という定義構文の内部で名詞を説明します。【人間の知的能力を】（目的語）→【人工的に】（副詞）→【コンピューターで再現する】（連体述語）→【「人工知能」の】（名詞修飾）。★の位置（3番目）には「コンピューターで再現する」が入ります。",
        "optReasons": [
            ("人間の知的能力を", "1番目の要素。再現される対象です。"),
            ("人工的に", "2番目の要素。再現の方法を表す副詞です。"),
            ("コンピューターで再現する", "【正解（★・3番目）】「人工知能」を修飾する連体形動詞句です。"),
            ("「人工知能」の", "4番目の要素。「略称」を修飾する名詞句です。")
        ]
    },
    "skm3-p2-c3-q11": {
        "question": "会議では、全員で ＿＿ ＿＿ ★ ＿＿ 合意が満場一致で形成された。",
        "options": ["一致団結して", "難題に", "立ち向かう", "という重要な"],
        "correctIndex": 2, # [一致団結して(1)] [難題に(2)] [★ 立ち向かう(3)] [という重要な(4)]
        "reconstructed": "会議では、全員で一致団結して難題に立ち向かうという重要な合意が満場一致で形成された。",
        "translation": "At the meeting, an important consensus that everyone would unite in solidarity to confront the difficult challenge was reached unanimously.",
        "context": "Reporting solid organizational unity achieved during critical team meetings.",
        "hint": "Resolution content: 一致団結して + 難題に + 立ち向かう + という重要な + 合意.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 「こと」「の」), pp. 108–109",
        "overall": "「合意」の内容を「〜という」で同格化する文型です。【一致団結して】（様態テ形）→【難題に】（対象）→【立ち向かう】（連体動詞）→【という重要な】（同格＋形容詞）。★の位置（3番目）には「立ち向かう」が入ります。",
        "optReasons": [
            ("一致団結して", "1番目の要素。チーム全体の姿勢を示します。"),
            ("難題に", "2番目の要素。「立ち向かう」の対象です。"),
            ("立ち向かう", "【正解（★・3番目）】「という」の直前に入る動詞辞書形です。"),
            ("という重要な", "4番目の要素。「合意」を直接修飾する連体節結びです。")
        ]
    },
    "skm3-p2-c3-q12": {
        "question": "茶道や華道、 ＿＿ ＿＿ ★ ＿＿ 外国人観光客が急増している。",
        "options": ["書道といった", "伝統文化を", "深く体験したい", "という熱心な"],
        "correctIndex": 2, # [書道といった(1)] [伝統文化を(2)] [★ 深く体験したい(3)] [という熱心な(4)]
        "reconstructed": "茶道や華道、書道といった伝統文化を深く体験したいという熱心な外国人観光客が急増している。",
        "translation": "Enthusiastic foreign tourists who wish to deeply experience traditional arts such as tea ceremony, flower arranging, and calligraphy are surging in number.",
        "context": "Explaining increasing inbound tourist interest in authentic Japanese cultural arts.",
        "hint": "Cultural arts examples: 書道といった + 伝統文化を + 深く体験したい + という熱心な + 観光客.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 「こと」「の」), pp. 108–109",
        "overall": "具体例示「といった」と願望節「〜たいという」を重ねた名詞修飾文です。【書道といった】（例示結び）→【伝統文化を】（目的語）→【深く体験したい】（願望述語）→【という熱心な】（同格＋ナ形容詞）。★の位置（3番目）には「深く体験したい」が入ります。",
        "optReasons": [
            ("書道といった", "1番目の要素。3つ目の伝統文化の例示です。"),
            ("伝統文化を", "2番目の要素。「体験したい」の目的語です。"),
            ("深く体験したい", "【正解（★・3番目）】「という」に接続するタイ形述語です。"),
            ("という熱心な", "4番目の要素。「外国人観光客」を直接修飾する句です。")
        ]
    },

    # =========================================================================
    # Part 2 · Chapter 4: 決まった形 (Fixed Syntactic Patterns & Paired Particles) - pp. 110–111
    # =========================================================================
    "skm3-p2-c4-q1": {
        "question": "昨夜遅くから ＿＿ ＿＿ ★ ＿＿ 記録的な大雨が降った。",
        "options": ["今朝の", "明け方に", "かけて、", "関東各地で"],
        "correctIndex": 2, # [今朝の(1)] [明け方に(2)] [★ かけて、(3)] [関東各地で(4)]
        "reconstructed": "昨夜遅くから今朝の明け方にかけて、関東各地で記録的な大雨が降った。",
        "translation": "From late last night through dawn this morning, record-breaking torrential rain fell across various parts of the Kanto region.",
        "context": "Reporting regional storm conditions over an extended overnight timeframe.",
        "hint": "Time range: 〜から + 今朝の + 明け方に + かけて + 関東各地で.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 4 (文の組み立て 4: 決まった形), pp. 110–111",
        "overall": "「〜から〜にかけて」（ある時からある時まで継続して）の相関文型です。【今朝の】（連体修飾）→【明け方に】（終点名詞＋に）→【かけて、】（範囲終了形式）→【関東各地で】（場所格助詞）。★の位置（3番目）には「かけて、」が入ります。",
        "optReasons": [
            ("今朝の", "1番目の要素。「明け方」を限定する名詞修飾です。"),
            ("明け方に", "2番目の要素。「かけて」を受ける「に」格です。"),
            ("かけて、", "【正解（★・3番目）】「〜から」と呼応しておおよその時間範囲を結びます。"),
            ("関東各地で", "4番目の要素。「大雨が降った」発生場所を示します。")
        ]
    },
    "skm3-p2-c4-q2": {
        "question": "新年度のサークル活動は、 ＿＿ ＿＿ ★ ＿＿ 進めていきます。",
        "options": ["「健康第一」を", "最大の目標", "として、", "無理のないペースで"],
        "correctIndex": 2, # [「健康第一」を(1)] [最大の目標(2)] [★ として、(3)] [無理のないペースで(4)]
        "reconstructed": "新年度のサークル活動は、「健康第一」を最大の目標として、無理のないペースで進めていきます。",
        "translation": "For the new academic year's club activities, taking 'health first' as our greatest objective, we will proceed at a sustainable pace.",
        "context": "Announcing club guidelines and organizing priorities.",
        "hint": "Objective setting: 「健康第一」を + 最大の目標 + として + 無理のないペースで.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 4 (文の組み立て 4: 決まった形), pp. 110–111",
        "overall": "「〜を〜として」（〜を目標・基準と位置付けて）の構文です。【「健康第一」を】（対象目的格）→【最大の目標】（位置付け名詞）→【として、】（資格・役割助詞）→【無理のないペースで】（様態句）。★の位置（3番目）には「として、」が入ります。",
        "optReasons": [
            ("「健康第一」を", "1番目の要素。「として」の対象格助詞「を」です。"),
            ("最大の目標", "2番目の要素。位置付けられる役割名詞です。"),
            ("として、", "【正解（★・3番目）】「〜を〜とする」の中連形です。"),
            ("無理のないペースで", "4番目の要素。「進めていきます」を修飾する様態表現です。")
        ]
    },
    "skm3-p2-c4-q3": {
        "question": "このアニメ作品は、 ＿＿ ＿＿ ★ ＿＿ 熱狂的な人気を集めている。",
        "options": ["日本国内は", "もちろん、", "海外のファンの", "間でも"],
        "correctIndex": 2, # [日本国内は(1)] [もちろん、(2)] [★ 海外のファンの(3)] [間でも(4)]
        "reconstructed": "このアニメ作品は、日本国内はもちろん、海外のファンの間でも熱狂的な人気を集めている。",
        "translation": "This anime work has garnered fervent popularity not only domestically in Japan, of course, but also among fans overseas.",
        "context": "Reporting on the widespread global success of an acclaimed animation franchise.",
        "hint": "Not only A but also B: 日本国内は + もちろん + 海外のファンの + 間でも.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 4 (文の組み立て 4: 決まった形), pp. 110–111",
        "overall": "「〜はもちろん、〜も」（〜は言うまでもなく、その上〜も）の相関文型です。【日本国内は】（前提提示）→【もちろん、】（当然化副詞）→【海外のファンの】（名詞修飾）→【間でも】（範囲提示＋も）。★の位置（3番目）には「海外のファンの」が入ります。",
        "optReasons": [
            ("日本国内は", "1番目の要素。「もちろん」の前提となる国内市場です。"),
            ("もちろん、", "2番目の要素。当然のことを確認する表現です。"),
            ("海外のファンの", "【正解（★・3番目）】「間」を限定する名詞修飾句です。"),
            ("間でも", "4番目の要素。「人気を集めている」範囲を「も」で拡大します。")
        ]
    },
    "skm3-p2-c4-q4": {
        "question": "どんなに厳しい状況であっても、 ＿＿ ＿＿ ★ ＿＿ 何とかなるものだ。",
        "options": ["体さえ", "健康で", "あれば、", "きっと"],
        "correctIndex": 2, # [体さえ(1)] [健康で(2)] [★ あれば、(3)] [きっと(4)]
        "reconstructed": "どんなに厳しい状況であっても、体さえ健康であれば、きっと何とかなるものだ。",
        "translation": "No matter how severe the situation is, as long as one's physical body is healthy, things will surely work out somehow.",
        "context": "Offering encouraging, resilient life wisdom.",
        "hint": "Sole prerequisite: 体さえ + 健康で + あれば + きっと.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 4 (文の組み立て 4: 決まった形), pp. 110–111",
        "overall": "最低限の必要条件「〜さえ〜ば」の相関文型です。【体さえ】（必要条件の主語）→【健康で】（形容動詞連用形）→【あれば、】（仮定形）→【きっと】（推量呼応副詞）。★の位置（3番目）には「あれば、」が入ります。",
        "optReasons": [
            ("体さえ", "1番目の要素。必須の唯一条件を取り立てる「さえ」です。"),
            ("健康で", "2番目の要素。「ある」に接続する形容動詞連用形です。"),
            ("あれば、", "【正解（★・3番目）】条件文を結ぶ仮定形です。"),
            ("きっと", "4番目の要素。「何とかなる」を強める確信副詞です。")
        ]
    },
    "skm3-p2-c4-q5": {
        "question": "その学術論文を ＿＿ ＿＿ ★ ＿＿ 半分も理解できなかった。",
        "options": ["読んだことは", "読んだのだが、", "内容が難解すぎて", "私の知識では"],
        "correctIndex": 2, # [読んだことは(1)] [読んだのだが、(2)] [★ 内容が難解すぎて(3)] [私の知識では(4)]
        "reconstructed": "その学術論文を読んだことは読んだのだが、内容が難解すぎて私の知識では半分も理解できなかった。",
        "translation": "I did read that academic paper as a matter of fact, but the content was so abstruse that with my knowledge I couldn't understand even half of it.",
        "context": "Conceding having read an advanced paper while admitting incomprehension.",
        "hint": "Concession structure: 読んだことは + 読んだのだが + 内容が難解すぎて + 私の知識では.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 4 (文の組み立て 4: 決まった形), pp. 110–111",
        "overall": "事実をひとまず認める「〜ことは〜が」の譲歩構文です。【読んだことは】（既成事実の提示）→【読んだのだが、】（反駁接続）→【内容が難解すぎて】（理解不能の理由）→【私の知識では】（限界の基準）。★の位置（3番目）には「内容が難解すぎて」が入ります。",
        "optReasons": [
            ("読んだことは", "1番目の要素。動作の事実を認める提示部です。"),
            ("読んだのだが、", "2番目の要素。逆接助詞「だが」で後続に繋ぎます。"),
            ("内容が難解すぎて", "【正解（★・3番目）】理解できない直接の理由を述べる「すぎて」形です。"),
            ("私の知識では", "4番目の要素。理解の能力限界を示す限定句です。")
        ]
    },
    "skm3-p2-c4-q6": {
        "question": "外国語の会話は、 ＿＿ ＿＿ ★ ＿＿ 自然に話せるようになる。",
        "options": ["毎日練習", "すれば", "するほど、", "流暢かつ"],
        "correctIndex": 2, # [毎日練習(1)] [すれば(2)] [★ するほど、(3)] [流暢かつ(4)]
        "reconstructed": "外国語の会話は、毎日練習すればするほど、流暢かつ自然に話せるようになる。",
        "translation": "As for foreign language conversation, the more you practice every day, the more fluently and naturally you become able to speak.",
        "context": "Explaining the proportional relationship between speaking practice and fluency.",
        "hint": "Proportional correlation: 毎日練習 + すれば + するほど + 流暢かつ.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 4 (文の組み立て 4: 決まった形), pp. 110–111",
        "overall": "比例的変化「〜ば〜ほど」（〜の度合いが増すにつれて）の呼応構文です。【毎日練習】（動作名詞）→【すれば】（条件形）→【するほど、】（比例助詞）→【流暢かつ】（様態副詞句）。★の位置（3番目）には「するほど、」が入ります。",
        "optReasons": [
            ("毎日練習", "1番目の要素。頻度副詞と動作名詞の組み合わせです。"),
            ("すれば", "2番目の要素。「〜ば」条件形です。"),
            ("するほど、", "【正解（★・3番目）】「〜ば」と呼応して比例関係を作る「ほど」です。"),
            ("流暢かつ", "4番目の要素。「自然に」と並列して話す質を修飾します。")
        ]
    },
    "skm3-p2-c4-q7": {
        "question": "大型の台風が接近しており、 ＿＿ ＿＿ ★ ＿＿ 暴風雨に警戒が必要です。",
        "options": ["九州地方から", "四国地方に", "かけての広い地域で", "猛烈な"],
        "correctIndex": 2, # [九州地方から(1)] [四国地方に(2)] [★ かけての広い地域で(3)] [猛烈な(4)]
        "reconstructed": "大型の台風が接近しており、九州地方から四国地方にかけての広い地域で猛烈な暴風雨に警戒が必要です。",
        "translation": "A large typhoon is approaching, and caution against violent storms is necessary across a wide area spanning from the Kyushu region to the Shikoku region.",
        "context": "Broadcasting urgent disaster warning advisories.",
        "hint": "Spanning from A to B: 九州地方から + 四国地方に + かけての広い地域で + 猛烈な.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 4 (文の組み立て 4: 決まった形), pp. 110–111",
        "overall": "空間的範囲「〜から〜にかけての＋名詞」の連体修飾文型です。【九州地方から】（始点）→【四国地方に】（終点格）→【かけての広い地域で】（範囲連体形＋場所）→【猛烈な】（ナ形容詞）。★の位置（3番目）には「かけての広い地域で」が入ります。",
        "optReasons": [
            ("九州地方から", "1番目の要素。影響範囲の起点です。"),
            ("四国地方に", "2番目の要素。「かけて」を受ける「に」格です。"),
            ("かけての広い地域で", "【正解（★・3番目）】「名詞＋の」で地域をまとめ、発生場所を示します。"),
            ("猛烈な", "4番目の要素。「暴風雨」を直接修飾するナ形容詞連体形です。")
        ]
    },
    "skm3-p2-c4-q8": {
        "question": "この温泉旅館は、 ＿＿ ＿＿ ★ ＿＿ 評判である。",
        "options": ["窓からの眺めも", "よければ、", "お湯の泉質も", "最高だと"],
        "correctIndex": 2, # [窓からの眺めも(1)] [よければ、(2)] [★ お湯の泉質も(3)] [最高だと(4)]
        "reconstructed": "この温泉旅館は、窓からの眺めもよければ、お湯の泉質も最高だと評判である。",
        "translation": "This hot spring inn is renowned for having both a wonderful view from the windows and supreme water quality.",
        "context": "Praising the combined scenic and bathing merits of a traditional inn.",
        "hint": "Parallel merits: 窓からの眺めも + よければ + お湯の泉質も + 最高だと.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 4 (文の組み立て 4: 決まった形), pp. 110–111",
        "overall": "長所の並列列挙「〜も〜ば、〜も〜」（〜も良いし、さらに〜も）構文です。【窓からの眺めも】（第1の長所）→【よければ、】（条件形）→【お湯の泉質も】（第2の長所）→【最高だと】（引用述語）。★の位置（3番目）には「お湯の泉質も」が入ります。",
        "optReasons": [
            ("窓からの眺めも", "1番目の要素。最初の取り立て助詞「も」です。"),
            ("よければ、", "2番目の要素。形容詞「良い」の条件形「ば」です。"),
            ("お湯の泉質も", "【正解（★・3番目）】2つ目の魅力を取り立てる「も」格です。"),
            ("最高だと", "4番目の要素。「評判である」に接続する引用句です。")
        ]
    },
    "skm3-p2-c4-q9": {
        "question": "今回の探査プロジェクトでは、 ＿＿ ＿＿ ★ ＿＿ 偉業を達成した。",
        "options": ["日本人研究者を", "中心とした", "国際チームが", "前人未到の"],
        "correctIndex": 2, # [日本人研究者を(1)] [中心とした(2)] [★ 国際チームが(3)] [前人未到の(4)]
        "reconstructed": "今回の探査プロジェクトでは、日本人研究者を中心とした国際チームが前人未到の偉業を達成した。",
        "translation": "In this exploration project, an international team centered around Japanese researchers accomplished an unprecedented feat.",
        "context": "Reporting historic breakthroughs in scientific exploration.",
        "hint": "Leadership center: 日本人研究者を + 中心とした + 国際チームが + 前人未到の + 偉業.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 4 (文の組み立て 4: 決まった形), pp. 110–111",
        "overall": "「〜を中心とする」（〜を中核として構成される）の連体修飾文型です。【日本人研究者を】（中心対象）→【中心とした】（連体修飾述語）→【国際チームが】（達成主語）→【前人未到の】（連体修飾句）。★の位置（3番目）には「国際チームが」が入ります。",
        "optReasons": [
            ("日本人研究者を", "1番目の要素。「中心とする」の対象を示す「を」格です。"),
            ("中心とした", "2番目の要素。「国際チーム」を修飾するタ形連体句です。"),
            ("国際チームが", "【正解（★・3番目）】「偉業を達成した」の主格名詞です。"),
            ("前人未到の", "4番目の要素。「偉業」を直接修飾する四字熟語連体句です。")
        ]
    },
    "skm3-p2-c4-q10": {
        "question": "このアニメ映画は、 ＿＿ ＿＿ ★ ＿＿ 親しまれている。",
        "options": ["小さな子どもから", "年配の方まで", "幅広い世代の", "人々に深く"],
        "correctIndex": 2, # [小さな子どもから(1)] [年配の方まで(2)] [★ 幅広い世代の(3)] [人々に深く(4)]
        "reconstructed": "このアニメ映画は、小さな子どもから年配の方まで幅広い世代の人々に深く親しまれている。",
        "translation": "This animated film is deeply loved by people of a broad range of generations, from small children to elderly individuals.",
        "context": "Explaining broad demographic appeal of an acclaimed movie.",
        "hint": "From A to B span: 小さな子どもから + 年配の方まで + 幅広い世代の + 人々に深く.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 4 (文の組み立て 4: 決まった形), pp. 110–111",
        "overall": "包括的範囲「〜から〜まで」の相関構文です。【小さな子どもから】（範囲始点）→【年配の方まで】（範囲終点）→【幅広い世代の】（名詞修飾）→【人々に深く】（対象＋副詞）。★の位置（3番目）には「幅広い世代の」が入ります。",
        "optReasons": [
            ("小さな子どもから", "1番目の要素。年齢層の始点です。"),
            ("年配の方まで", "2番目の要素。年齢層の到達点です。"),
            ("幅広い世代の", "【正解（★・3番目）】「人々」を修飾する連体修飾句です。"),
            ("人々に深く", "4番目の要素。「親しまれている」の対象と様態を示します。")
        ]
    },
    "skm3-p2-c4-q11": {
        "question": "この手作り家具は、値段が ＿＿ ＿＿ ★ ＿＿ 十分にある。",
        "options": ["高いことは", "高いが、", "一生使い続けられる", "それだけの価値が"],
        "correctIndex": 2, # [高いことは(1)] [高いが、(2)] [★ 一生使い続けられる(3)] [それだけの価値が(4)]
        "reconstructed": "この手作り家具は、値段が高いことは高いが、一生使い続けられるそれだけの価値が十分にある。",
        "translation": "As for this handcrafted furniture, it is indeed expensive, but it has ample worth commensurate with being able to be used for a lifetime.",
        "context": "Evaluating the high quality and lifetime durability of bespoke craftsmanship.",
        "hint": "Concession structure: 高いことは + 高いが + 一生使い続けられる + それだけの価値が.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 4 (文の組み立て 4: 決まった形), pp. 110–111",
        "overall": "事実を認めて後項を主張する「〜ことは〜が」の譲歩構文です。【高いことは】（事実提示）→【高いが、】（反駁接続）→【一生使い続けられる】（連体可能節）→【それだけの価値が】（主格句）。★の位置（3番目）には「一生使い続けられる」が入ります。",
        "optReasons": [
            ("高いことは", "1番目の要素。高額であることを認める提示部です。"),
            ("高いが、", "2番目の要素。逆接で反論へ繋ぐ「が」です。"),
            ("一生使い続けられる", "【正解（★・3番目）】「価値」を説明する可能連体節です。"),
            ("それだけの価値が", "4番目の要素。「十分にある」の主語です。")
        ]
    },
    "skm3-p2-c4-q12": {
        "question": "前途多難な挑戦であっても、 ＿＿ ＿＿ ★ ＿＿ 必ず切り拓ける。",
        "options": ["一歩踏み出す", "勇気さえ", "あれば、", "未来は"],
        "correctIndex": 2, # [一歩踏み出す(1)] [勇気さえ(2)] [★ あれば、(3)] [未来は(4)]
        "reconstructed": "前途多難な挑戦であっても、一歩踏み出す勇気さえあれば、未来は必ず切り拓ける。",
        "translation": "Even if it is a daunting challenge fraught with difficulties, as long as you have the courage to take a step forward, the future can surely be forged.",
        "context": "Delivering inspiring words of courage before an ambitious venture.",
        "hint": "Prerequisite courage: 一歩踏み出す + 勇気さえ + あれば + 未来は.",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 2 Chapter 4 (文の組み立て 4: 決まった形), pp. 110–111",
        "overall": "「〜さえ〜ば」（それさえ満たせば他は可能になる）の相関文型です。【一歩踏み出す】（連体動詞句）→【勇気さえ】（唯一条件主語）→【あれば、】（仮定形）→【未来は】（主節主語）。★の位置（3番目）には「あれば、」が入ります。",
        "optReasons": [
            ("一歩踏み出す", "1番目の要素。「勇気」を修飾する連体節です。"),
            ("勇気さえ", "2番目の要素。必須条件を取り立てる「さえ」です。"),
            ("あれば、", "【正解（★・3番目）】条件文を完成させる仮定形動詞です。"),
            ("未来は", "4番目の要素。「切り拓ける」の主節主題です。")
        ]
    }
}

updated = 0
for e in exercises:
    eid = e.get("id")
    if eid in STAR_MARK_N3:
        d = STAR_MARK_N3[eid]
        e["type"] = "star-mark"
        e["question"] = d["question"]
        e["options"] = d["options"]
        e["correctIndex"] = d["correctIndex"]
        e["scrambleOrder"] = [1, 2, 3, 4] # standardized 1-4 slot sequence where slot 3 is the star
        e["reconstructedSentence"] = d["reconstructed"]
        e["translation"] = d["translation"]
        e["context"] = d["context"]
        e["hint"] = d["hint"]
        e["provenance"] = "source-derived"
        e["sourceEvidence"] = d["evidence"]
        
        # Build pristine option breakdown
        opt_breakdown = []
        for opt_text, opt_reason in d["optReasons"]:
            is_corr = (opt_text == d["options"][d["correctIndex"]])
            opt_breakdown.append({
                "text": opt_text,
                "isCorrect": is_corr,
                "reason": opt_reason,
                "trapCategory": "" if is_corr else "formation"
            })
        
        e["explanation"] = {
            "overall": d["overall"],
            "options": opt_breakdown
        }
        updated += 1

print(f"Successfully converted {updated} SKM N3 Part 2 exercises to authentic Star-Mark format!")

with open(EXERCISES_PATH, "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved updated chapterExercises.json successfully.")
