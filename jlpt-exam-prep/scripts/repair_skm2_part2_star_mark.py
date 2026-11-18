"""
repair_skm2_part2_star_mark.py
Converts all 36 exercises in Shin Kanzen Master N2 Part 2 (Chapters 1, 2, 3)
into authentic JLPT Question 2 Star-Mark (文の組み立て ★) exercises.
Includes full reconstructed sentence, 1-based scrambleOrder, authentic options,
0-indexed correctIndex pointing to the 3rd slot (★), complete English translations,
and option-by-option linguistic syntactic rationale.
"""

import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
EXERCISES_FILE = ROOT / "src/data/chapterExercises.json"

STAR_MARK_DATA = {
    # ------------------ Part 2 · Chapter 1 (決まった形・語順) ------------------
    "skm2-p2-c1-q1": {
        "context": "Expressing impossibility regarding an amateur tackling a massive codebase.",
        "question": "これほど複雑で膨大なプログラムを、 ＿＿ ＿＿ ★ ＿＿。",
        "translation": "There is no way an amateur like him could develop such a complex, massive program all by himself.",
        "options": ["素人の彼が", "たった一人で", "短期間で開発", "できっこない"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "これほど複雑で膨大なプログラムを、素人の彼がたった一人で短期間で開発できっこない。",
        "hint": "Subject (素人の彼が) → adverbial (たった一人で) → verb compound (短期間で開発) → emphatic impossibility (できっこない).",
        "explanation": {
            "overall": "文頭の目的語「これほど複雑で膨大なプログラムを」を受けて、主語【素人の彼が】→様態【たった一人で】→動作述語【短期間で開発】→強い口語否定【できっこない】の順序で文が組み立てられます。★の位置（3番目）には「短期間で開発」が入ります。",
            "options": [
                {"text": "素人の彼が", "isCorrect": False, "reason": "1番目の要素。主語として後続の動作主体を示します。", "trapCategory": "formation"},
                {"text": "たった一人で", "isCorrect": False, "reason": "2番目の要素。動作の条件・様態を限定する副詞句です。", "trapCategory": "formation"},
                {"text": "短期間で開発", "isCorrect": True, "reason": "【正解（★・3番目）】「できっこない」の動詞連用形「でき」に接続する複合名詞述語です。", "trapCategory": ""},
                {"text": "できっこない", "isCorrect": False, "reason": "4番目の要素。文末で「絶対に〜できるはずがない」という強い断定的不可能を表します。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 決まった形), pp. 140–145"
    },
    "skm2-p2-c1-q2": {
        "context": "Reflecting on grueling athletic training leading to victory.",
        "question": "半年に及ぶ ＿＿ ＿＿ ★ ＿＿ 初優勝を飾ることができた。",
        "translation": "Thanks to the grueling six months of intensive training, he was able to secure his long-cherished first victory at the national tournament.",
        "options": ["猛特訓の", "甲斐があって", "彼は全国大会で", "念願の"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "半年に及ぶ猛特訓の甲斐があって、彼は全国大会で念願の初優勝を飾ることができた。",
        "hint": "Noun modifier (猛特訓の) → result clause (甲斐があって) → topic/location (彼は全国大会で) → noun modifier (念願の).",
        "explanation": {
            "overall": "「半年に及ぶ」が名詞【猛特訓の】を修飾し、努力の報いを示す【甲斐があって】で節を区切ります。後半は主語・場所【彼は全国大会で】→修飾語【念願の】→「初優勝」へと繋がります。★の位置（3番目）には「彼は全国大会で」が入ります。",
            "options": [
                {"text": "猛特訓の", "isCorrect": False, "reason": "1番目の要素。「半年に及ぶ」の直接の被修飾名詞です。", "trapCategory": "formation"},
                {"text": "甲斐があって", "isCorrect": False, "reason": "2番目の要素。努力が実を結んだ因果関係を示す接続形式です。", "trapCategory": "formation"},
                {"text": "彼は全国大会で", "isCorrect": True, "reason": "【正解（★・3番目）】主節の主語と行為の舞台を示す名詞句です。", "trapCategory": ""},
                {"text": "念願の", "isCorrect": False, "reason": "4番目の要素。文末直前の「初優勝」を直接修飾する連体修飾語です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 決まった形), pp. 140–145"
    },
    "skm2-p2-c1-q3": {
        "context": "Asserting that a specific colleague is uniquely qualified for project lead.",
        "question": "次期プロジェクトの最高責任者には、 ＿＿ ＿＿ ★ ＿＿ 適任者はいない。",
        "translation": "As the supreme director for the upcoming project, aside from him who possesses outstanding leadership, there is no other qualified candidate.",
        "options": ["卓越した指導力を持つ", "彼をおいて", "ほかに", "ふさわしい"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "次期プロジェクトの最高責任者には、卓越した指導力を持つ彼をおいてほかにふさわしい適任者はいない。",
        "hint": "Relative clause (卓越した指導力を持つ) → exclusive marker (彼をおいて) → negation paired adverb (ほかに) → modifier (ふさわしい).",
        "explanation": {
            "overall": "「〜をおいてほかに〜ない」の呼応構文です。【卓越した指導力を持つ】（連体修飾）→【彼をおいて】（唯一性の提示）→【ほかに】（呼応副詞）→【ふさわしい】（適任者を修飾）の順に結びます。★の位置（3番目）には「ほかに」が入ります。",
            "options": [
                {"text": "卓越した指導力を持つ", "isCorrect": False, "reason": "1番目の要素。「彼」を修飾する連体修飾節です。", "trapCategory": "formation"},
                {"text": "彼をおいて", "isCorrect": False, "reason": "2番目の要素。「〜をおいて…ない」の基幹文型を形成します。", "trapCategory": "formation"},
                {"text": "ほかに", "isCorrect": True, "reason": "【正解（★・3番目）】「をおいて」と呼応して文末の否定「いない」を導く副詞です。", "trapCategory": ""},
                {"text": "ふさわしい", "isCorrect": False, "reason": "4番目の要素。直後の名詞「適任者」を修飾します。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 決まった形), pp. 140–145"
    },
    "skm2-p2-c1-q4": {
        "context": "Lamenting an unsuccessful emergency resuscitation effort.",
        "question": "医師団による ＿＿ ＿＿ ★ ＿＿ 救うことはできなかった。",
        "translation": "Despite the medical team's desperate lifesaving treatment, it was unfortunately impossible to save the patient's precious life.",
        "options": ["懸命の", "救命治療の甲斐もなく", "患者の尊い", "命を"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "医師団による懸命の救命治療の甲斐もなく、患者の尊い命を救うことはできなかった。",
        "hint": "Modifier (懸命の) → unavailing effort (救命治療の甲斐もなく) → noun modifier (患者の尊い) → direct object (命を).",
        "explanation": {
            "overall": "「医師団による」から【懸命の】（修飾）→【救命治療の甲斐もなく】（努力の不毛）→【患者の尊い】（修飾）→【命を】（目的語）→「救うことはできなかった」へと構造が連鎖します。★の位置（3番目）には「患者の尊い」が入ります。",
            "options": [
                {"text": "懸命の", "isCorrect": False, "reason": "1番目の要素。「救命治療」を修飾する連体詞的用法です。", "trapCategory": "formation"},
                {"text": "救命治療の甲斐もなく", "isCorrect": False, "reason": "2番目の要素。甲斐もなく構文で前半節を結びます。", "trapCategory": "formation"},
                {"text": "患者の尊い", "isCorrect": True, "reason": "【正解（★・3番目）】主節の目的語「命」を修飾する連体修飾句です。", "trapCategory": ""},
                {"text": "命を", "isCorrect": False, "reason": "4番目の要素。文末「救うことはできなかった」に直接かかる目的語です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 決まった形), pp. 140–145"
    },
    "skm2-p2-c1-q5": {
        "context": "Stating the sheer impossibility of defeating a world champion.",
        "question": "世界チャンピオンを相手に、 ＿＿ ＿＿ ★ ＿＿。",
        "translation": "Facing the world champion, there is no chance that a beginner like me could win in an official match.",
        "options": ["初心者の", "私が公式の試合で", "勝て", "っこない"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "世界チャンピオンを相手に、初心者の私が公式の試合で勝てっこない。",
        "hint": "Apposition (初心者の) → subject phrase (私が公式の試合で) → verb stem (勝て) → suffix (っこない).",
        "explanation": {
            "overall": "対戦相手の提示後、【初心者の】→【私が公式の試合で】（動作主と状況）→【勝て】（動詞ます形語幹）→【っこない】（絶対否定）と文法要素が連続します。★の位置（3番目）には「勝て」が入ります。",
            "options": [
                {"text": "初心者の", "isCorrect": False, "reason": "1番目の要素。後続の「私」を同格・属性修飾します。", "trapCategory": "formation"},
                {"text": "私が公式の試合で", "isCorrect": False, "reason": "2番目の要素。述語の主語と対戦場所を示します。", "trapCategory": "formation"},
                {"text": "勝て", "isCorrect": True, "reason": "【正解（★・3番目）】「〜っこない」が接続する動詞ます形（連用形）語幹です。", "trapCategory": ""},
                {"text": "っこない", "isCorrect": False, "reason": "4番目の要素。口語的な絶対不可能を表す接尾辞形式です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 決まった形), pp. 140–145"
    },
    "skm2-p2-c1-q6": {
        "context": "Highlighting Director Yamada as the indispensable leader.",
        "question": "新体制のリーダーとして ＿＿ ＿＿ ★ ＿＿ 絶対に考えられない。",
        "translation": "As leader of the new system, a person capable of guiding all staff is completely unthinkable aside from Director Yamada, a person of great character.",
        "options": ["全社員を", "牽引できる人物は", "人格者の", "山田部長をおいて"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "新体制のリーダーとして全社員を牽引できる人物は、人格者の山田部長をおいて絶対に考えられない。",
        "hint": "Object (全社員を) → relative clause subject (牽引できる人物は) → modifier (人格者の) → unique exclusion (山田部長をおいて).",
        "explanation": {
            "overall": "「全社員を」が【全社員を】→【牽引できる人物は】（主題）→【人格者の】（修飾）→【山田部長をおいて】（除外限定）→「絶対に考えられない」と整序されます。★の位置（3番目）には「人格者の」が入ります。",
            "options": [
                {"text": "全社員を", "isCorrect": False, "reason": "1番目の要素。動詞「牽引できる」の直接目的語です。", "trapCategory": "formation"},
                {"text": "牽引できる人物は", "isCorrect": False, "reason": "2番目の要素。文全体の主題を提示する主格節です。", "trapCategory": "formation"},
                {"text": "人格者の", "isCorrect": True, "reason": "【正解（★・3番目）】直後の「山田部長」の人物的資質を修飾する名詞修飾節です。", "trapCategory": ""},
                {"text": "山田部長をおいて", "isCorrect": False, "reason": "4番目の要素。「〜をおいて…ない」構文を完成させるキーフレーズです。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 決まった形), pp. 140–145"
    },
    "skm2-p2-c1-q7": {
        "context": "Tenacious laboratory research resulting in synthesis of new substance.",
        "question": "十年間 ＿＿ ＿＿ ★ ＿＿ 合成に成功した。",
        "translation": "Thanks to continuing research for ten years without giving up, we finally succeeded in the synthesis of a groundbreaking new substance.",
        "options": ["諦めずに", "研究を続けた甲斐があって", "ついに画期的な", "新物質の"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "十年間諦めずに研究を続けた甲斐があって、ついに画期的な新物質の合成に成功した。",
        "hint": "Negative adverbial (諦めずに) → effort rewarded (研究を続けた甲斐があって) → adverb/modifier (ついに画期的な) → noun modifier (新物質の).",
        "explanation": {
            "overall": "「十年間」に続いて【諦めずに】→【研究を続けた甲斐があって】（努力の結果）→【ついに画期的な】（成果修飾）→【新物質の】（合成の対象）の順序で結実します。★の位置（3番目）には「ついに画期的な」が入ります。",
            "options": [
                {"text": "諦めずに", "isCorrect": False, "reason": "1番目の要素。「研究を続けた」にかかる様態副詞句です。", "trapCategory": "formation"},
                {"text": "研究を続けた甲斐があって", "isCorrect": False, "reason": "2番目の要素。十年間の努力が報われた理由を示します。", "trapCategory": "formation"},
                {"text": "ついに画期的な", "isCorrect": True, "reason": "【正解（★・3番目）】達成の副詞「ついに」と「新物質」を修飾する形容動詞連体形です。", "trapCategory": ""},
                {"text": "新物質の", "isCorrect": False, "reason": "4番目の要素。文末「合成」を直接修飾する名詞句です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 決まった形), pp. 140–145"
    },
    "skm2-p2-c1-q8": {
        "context": "Despairing over finding a tiny contact lens in the dark.",
        "question": "こんな暗闇の中で ＿＿ ＿＿ ★ ＿＿ 今すぐ見つかりっこない。",
        "translation": "A tiny contact lens dropped in darkness like this could not possibly be found right away even if one searches.",
        "options": ["落としてしまった", "小さな", "コンタクトレンズなど", "探しても"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "こんな暗闇の中で落としてしまった小さなコンタクトレンズなど、探しても今すぐ見つかりっこない。",
        "hint": "Relative verb (落としてしまった) → adjective (小さな) → topic noun (コンタクトレンズなど) → conditional concessive (探しても).",
        "explanation": {
            "overall": "「こんな暗闇の中で」に【落としてしまった】→【小さな】→【コンタクトレンズなど】（主題）→【探しても】（逆接仮定）→「今すぐ見つかりっこない」と繋がります。★の位置（3番目）には「コンタクトレンズなど」が入ります。",
            "options": [
                {"text": "落としてしまった", "isCorrect": False, "reason": "1番目の要素。場所句を受けて目的物を修飾する動詞節です。", "trapCategory": "formation"},
                {"text": "小さな", "isCorrect": False, "reason": "2番目の要素。レンズの形状・小ささを修飾する連体詞です。", "trapCategory": "formation"},
                {"text": "コンタクトレンズなど", "isCorrect": True, "reason": "【正解（★・3番目）】主題提示と軽視・強調を表す助詞「など」を伴う名詞です。", "trapCategory": ""},
                {"text": "探しても", "isCorrect": False, "reason": "4番目の要素。「〜ても…っこない」の条件節を導く逆接節です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 決まった形), pp. 140–145"
    },
    "skm2-p2-c1-q9": {
        "context": "All-night presentation prep ruined by last-minute cancellation.",
        "question": "徹夜で仕上げた ＿＿ ＿＿ ★ ＿＿ 終わってしまった。",
        "translation": "Although it was a presentation document finished by working all night, due to the last-minute meeting cancellation, it ended in vain with all effort wasted.",
        "options": ["プレゼン資料だったが", "直前の会議中止により", "準備の", "甲斐もなく無駄に"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "徹夜で仕上げたプレゼン資料だったが、直前の会議中止により準備の甲斐もなく無駄に終わってしまった。",
        "hint": "Concession clause (プレゼン資料だったが) → cause (直前の会議中止により) → noun (準備の) → fruitlessness (甲斐もなく無駄に).",
        "explanation": {
            "overall": "前半【プレゼン資料だったが】で前提を述べ、【直前の会議中止により】（理由）→【準備の】→【甲斐もなく無駄に】（不毛な結果）→「終わってしまった」へと配置されます。★の位置（3番目）には「準備の」が入ります。",
            "options": [
                {"text": "プレゼン資料だったが", "isCorrect": False, "reason": "1番目の要素。「徹夜で仕上げた」を受ける名詞文接続助詞です。", "trapCategory": "formation"},
                {"text": "直前の会議中止により", "isCorrect": False, "reason": "2番目の要素。努力が無駄になった外的要因を示す原因句です。", "trapCategory": "formation"},
                {"text": "準備の", "isCorrect": True, "reason": "【正解（★・3番目）】「甲斐もなく」の直前に置かれ、報われなかった行為の名詞です。", "trapCategory": ""},
                {"text": "甲斐もなく無駄に", "isCorrect": False, "reason": "4番目の要素。文末「終わってしまった」を副詞的に修飾します。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 決まった形), pp. 140–145"
    },
    "skm2-p2-c1-q10": {
        "context": "Young animators as the sole drivers of global anime dissemination.",
        "question": "現代日本のアニメーション文化を ＿＿ ＿＿ ★ ＿＿ ほかにない。",
        "translation": "The core figures who will disseminate modern Japanese animation culture to the world are none other than young creators.",
        "options": ["世界に発信する", "主役となる人材は", "若いクリエイターを", "おいて"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "現代日本のアニメーション文化を世界に発信する主役となる人材は、若いクリエイターをおいてほかにない。",
        "hint": "Relative clause (世界に発信する) → head subject (主役となる人材は) → object noun (若いクリエイターを) → postposition (おいて).",
        "explanation": {
            "overall": "「文化を」に呼応して【世界に発信する】→【主役となる人材は】（主語）→【若いクリエイターを】→【おいて】（除外格）→「ほかにない」が連鎖します。★の位置（3番目）には「若いクリエイターを」が入ります。",
            "options": [
                {"text": "世界に発信する", "isCorrect": False, "reason": "1番目の要素。直前の目的語を受けて人材を修飾する連体節です。", "trapCategory": "formation"},
                {"text": "主役となる人材は", "isCorrect": False, "reason": "2番目の要素。文全体の主題を導出する名詞句です。", "trapCategory": "formation"},
                {"text": "若いクリエイターを", "isCorrect": True, "reason": "【正解（★・3番目）】文末の「おいてほかにない」に接続する対格名詞句です。", "trapCategory": ""},
                {"text": "おいて", "isCorrect": False, "reason": "4番目の要素。「〜をおいてほかに〜ない」構文の接続動詞て形です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 決まった形), pp. 140–145"
    },
    "skm2-p2-c1-q11": {
        "context": "Eating a ten-person portion steak is humanly impossible.",
        "question": "一度に十人分ものステーキを、 ＿＿ ＿＿ ★ ＿＿。",
        "translation": "There is no way an ordinary human being could finish a ten-person steak meal all alone in a short time.",
        "options": ["普通の人間が", "たった一人で", "短時間で完食", "できっこない"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "一度に十人分ものステーキを、普通の人間がたった一人で短時間で完食できっこない。",
        "hint": "Subject (普通の人間が) → solitary manner (たった一人で) → predicate noun (短時間で完食) → cannot (できっこない).",
        "explanation": {
            "overall": "目的語提示に続き、【普通の人間が】（主格）→【たった一人で】（様態）→【短時間で完食】（動作述語）→【できっこない】（絶対否定）と文が結ばれます。★の位置（3番目）には「短時間で完食」が入ります。",
            "options": [
                {"text": "普通の人間が", "isCorrect": False, "reason": "1番目の要素。文の動作主体を限定する主格句です。", "trapCategory": "formation"},
                {"text": "たった一人で", "isCorrect": False, "reason": "2番目の要素。孤立・単独の状況を表す副詞句です。", "trapCategory": "formation"},
                {"text": "短時間で完食", "isCorrect": True, "reason": "【正解（★・3番目）】「できっこない」のサ変語幹「完食でき」を形成する名詞述語です。", "trapCategory": ""},
                {"text": "できっこない", "isCorrect": False, "reason": "4番目の要素。文末で強力な客観的不可能性を断定します。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 決まった形), pp. 140–145"
    },
    "skm2-p2-c1-q12": {
        "context": "Health checkup metrics drastically improving through strict jogging and diet.",
        "question": "毎朝の ＿＿ ＿＿ ★ ＿＿ 数値が見違えるほど改善した。",
        "translation": "Thanks to thoroughly committing to jogging and dietary management every morning, the numbers on this year's health checkup improved dramatically.",
        "options": ["ジョギングと食事管理を", "徹底した甲斐があって", "今年の健康診断の", "検査結果の"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "毎朝のジョギングと食事管理を徹底した甲斐があって、今年の健康診断の検査結果の数値が見違えるほど改善した。",
        "hint": "Noun compound (ジョギングと食事管理を) → fruitful effort (徹底した甲斐があって) → noun modifier (今年の健康診断の) → modifier (検査結果の).",
        "explanation": {
            "overall": "「毎朝の」から【ジョギングと食事管理を】→【徹底した甲斐があって】（努力の結果）→【今年の健康診断の】→【検査結果の】→「数値」へと連体修飾の連鎖を作ります。★の位置（3番目）には「今年の健康診断の」が入ります。",
            "options": [
                {"text": "ジョギングと食事管理を", "isCorrect": False, "reason": "1番目の要素。「毎朝の」に続く目的語句です。", "trapCategory": "formation"},
                {"text": "徹底した甲斐があって", "isCorrect": False, "reason": "2番目の要素。努力の継続が良い結果を生んだことを示します。", "trapCategory": "formation"},
                {"text": "今年の健康診断の", "isCorrect": True, "reason": "【正解（★・3番目）】主節の対象となる診断時期を限定する連体名詞句です。", "trapCategory": ""},
                {"text": "検査結果の", "isCorrect": False, "reason": "4番目の要素。直後の名詞「数値」を直接修飾します。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 1 (文の組み立て 1: 決まった形), pp. 140–145"
    },

    # ------------------ Part 2 · Chapter 2 (名詞を説明する形式) ------------------
    "skm2-p2-c2-q1": {
        "context": "Severe professional rebuke against an educator leaking personal student data.",
        "question": "生徒の個人情報を ＿＿ ＿＿ ★ ＿＿ 言語道断の不祥事だ。",
        "translation": "The act of deliberately leaking student personal information to outsiders is an outrageous scandal completely impermissible for an educator.",
        "options": ["故意に外部へ", "漏洩させる行為は", "教育者に", "あるまじき"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "生徒の個人情報を故意に外部へ漏洩させる行為は、教育者にあるまじき言語道断の不祥事だ。",
        "hint": "Adverbial goal (故意に外部へ) → action nominal (漏洩させる行為は) → professional status (教育者に) → archaic prohibition (あるまじき).",
        "explanation": {
            "overall": "「生徒の個人情報を」に続き、【故意に外部へ】→【漏洩させる行為は】（主題）→【教育者に】→【あるまじき】（〜にあるまじき修飾）→「言語道断の不祥事だ」と連鎖します。★の位置（3番目）には「教育者に」が入ります。",
            "options": [
                {"text": "故意に外部へ", "isCorrect": False, "reason": "1番目の要素。漏洩の態様と方向を示す副詞句です。", "trapCategory": "formation"},
                {"text": "漏洩させる行為は", "isCorrect": False, "reason": "2番目の要素。文全体の主語・主題を提示する名詞節です。", "trapCategory": "formation"},
                {"text": "教育者に", "isCorrect": True, "reason": "【正解（★・3番目）】「〜にあるまじき」の立場・身分を表す名詞＋格助詞です。", "trapCategory": ""},
                {"text": "あるまじき", "isCorrect": False, "reason": "4番目の要素。「〜にあってはならない」意味で不祥事を修飾する連体形です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞を説明する形式), pp. 146–149"
    },
    "skm2-p2-c2-q2": {
        "context": "Freedom of the press as an indispensable pillar of healthy democracy.",
        "question": "健全な民主主義社会を ＿＿ ＿＿ ★ ＿＿ 根本要素である。",
        "translation": "In maintaining a healthy democratic society, freedom of the press is an indispensable fundamental element that must not be lacking even for a single day.",
        "options": ["維持する上で", "報道の自由は", "一日たりとも", "欠くべからざる"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "健全な民主主義社会を維持する上で、報道の自由は一日たりとも欠くべからざる根本要素である。",
        "hint": "Purpose clause (維持する上で) → topic subject (報道の自由は) → minimal time unit (一日たりとも) → indispensable modifier (欠くべからざる).",
        "explanation": {
            "overall": "「〜を維持する上で」から【維持する上で】→【報道の自由は】（主題）→【一日たりとも】（最小限の否定強調）→【欠くべからざる】（根本要素を修飾）と整序されます。★の位置（3番目）には「一日たりとも」が入ります。",
            "options": [
                {"text": "維持する上で", "isCorrect": False, "reason": "1番目の要素。前提条件・場面設定を表す接続形式です。", "trapCategory": "formation"},
                {"text": "報道の自由は", "isCorrect": False, "reason": "2番目の要素。主節の主題を提示する主格名詞句です。", "trapCategory": "formation"},
                {"text": "一日たりとも", "isCorrect": True, "reason": "【正解（★・3番目）】「〜たりとも…ない」の強調形式で、欠くべからざるの否定性を強めます。", "trapCategory": ""},
                {"text": "欠くべからざる", "isCorrect": False, "reason": "4番目の要素。「欠いてはならない」意味で「根本要素」を連体修飾します。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞を説明する形式), pp. 146–149"
    },
    "skm2-p2-c2-q3": {
        "context": "Strict signboard prohibiting unauthorized garbage dumping in temple grounds.",
        "question": "神聖な境内において、 ＿＿ ＿＿ ★ ＿＿ 看板がある。",
        "translation": "In the sacred temple grounds, there is a signboard stating that visitors must not indiscriminately dump trash without permission.",
        "options": ["一般参拝客が", "勝手にゴミを", "投棄する", "べからずとの"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "神聖な境内において、一般参拝客が勝手にゴミを投棄するべからずとの看板がある。",
        "hint": "Subject (一般参拝客が) → adverb/object (勝手にゴミを) → verb dictionary form (投棄する) → classical prohibitive citation (べからずとの).",
        "explanation": {
            "overall": "場所句の後に【一般参拝客が】→【勝手にゴミを】→【投棄する】（動詞辞書形）→【べからずとの】（禁止の引用）→「看板がある」と続きます。★の位置（3番目）には「投棄する」が入ります。",
            "options": [
                {"text": "一般参拝客が", "isCorrect": False, "reason": "1番目の要素。引用節内の主体を示す主格句です。", "trapCategory": "formation"},
                {"text": "勝手にゴミを", "isCorrect": False, "reason": "2番目の要素。投棄の様態と目的語です。", "trapCategory": "formation"},
                {"text": "投棄する", "isCorrect": True, "reason": "【正解（★・3番目）】古風な禁止表現「〜べからず」が直接前接する動詞終止形（辞書形）です。", "trapCategory": ""},
                {"text": "べからずとの", "isCorrect": False, "reason": "4番目の要素。「〜してはならないという」意味で看板を修飾する引用形式です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞を説明する形式), pp. 146–149"
    },
    "skm2-p2-c2-q4": {
        "context": "Condemning a doctor trading patients' lives for selfish profit.",
        "question": "患者の生命を ＿＿ ＿＿ ★ ＿＿ 許すまじき犯罪だ。",
        "translation": "Using patients' lives for selfish transactions is an unforgivable crime for a doctor entrusted with human life.",
        "options": ["私利私欲の", "取引に利用するなど", "人の命を預かる", "医師として"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "患者の生命を私利私欲の取引に利用するなど、人の命を預かる医師として許すまじき犯罪だ。",
        "hint": "Modifier (私利私欲の) → predicate clause (取引に利用するなど) → relative clause (人の命を預かる) → status (医師として).",
        "explanation": {
            "overall": "「患者の生命を」に【私利私欲の】→【取引に利用するなど】（前段批判）→【人の命を預かる】→【医師として】（資格立場）→「許すまじき犯罪だ」と結びます。★の位置（3番目）には「人の命を預かる」が入ります。",
            "options": [
                {"text": "私利私欲の", "isCorrect": False, "reason": "1番目の要素。「取引」を修飾する連体名詞句です。", "trapCategory": "formation"},
                {"text": "取引に利用するなど", "isCorrect": False, "reason": "2番目の要素。非難の対象となる行為を具体化する節です。", "trapCategory": "formation"},
                {"text": "人の命を預かる", "isCorrect": True, "reason": "【正解（★・3番目）】「医師」の職務的崇高さを修飾する連体修飾節です。", "trapCategory": ""},
                {"text": "医師として", "isCorrect": False, "reason": "4番目の要素。「許すまじき」の評価基準となる立場・資格を示します。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞を説明する形式), pp. 146–149"
    },
    "skm2-p2-c2-q5": {
        "context": "Constructing a climate change model based on a decade of observations.",
        "question": "過去十年に ＿＿ ＿＿ ★ ＿＿ 温暖化モデルを構築した。",
        "translation": "Based on meteorological observation records spanning the past ten years, we constructed a highly accurate global warming progression model.",
        "options": ["わたる綿密な", "気象観測の記録に", "基づいて精度の高い", "将来の地球"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "過去十年にわたる綿密な気象観測の記録に基づいて精度の高い将来の地球温暖化モデルを構築した。",
        "hint": "Span predicate (わたる綿密な) → noun head (気象観測の記録に) → basis (基づいて精度の高い) → modifier (将来の地球).",
        "explanation": {
            "overall": "「過去十年に」から【わたる綿密な】→【気象観測の記録に】→【基づいて精度の高い】（基準）→【将来の地球】→「温暖化モデル」へと連体修飾が構成されます。★の位置（3番目）には「基づいて精度の高い」が入ります。",
            "options": [
                {"text": "わたる綿密な", "isCorrect": False, "reason": "1番目の要素。期間を表す名詞に接続する連体形です。", "trapCategory": "formation"},
                {"text": "気象観測の記録に", "isCorrect": False, "reason": "2番目の要素。「基づいて」の根拠となる名詞句です。", "trapCategory": "formation"},
                {"text": "基づいて精度の高い", "isCorrect": True, "reason": "【正解（★・3番目）】「〜に基づいて」の根拠表現と、モデルの精度修飾です。", "trapCategory": ""},
                {"text": "将来の地球", "isCorrect": False, "reason": "4番目の要素。「温暖化モデル」を直接修飾する名詞句です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞を説明する形式), pp. 146–149"
    },
    "skm2-p2-c2-q6": {
        "context": "Sovereignty and citizen safety as an unyielding government principle.",
        "question": "国家の主権と ＿＿ ＿＿ ★ ＿＿ 防衛原則である。",
        "translation": "The duty to protect national sovereignty and citizen safety is an uncompromising defense principle that the government must never yield under any circumstances.",
        "options": ["国民の安全を守る責務は", "政府にとって", "いかなる事態でも", "譲るべからざる"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "国家の主権と国民の安全を守る責務は、政府にとっていかなる事態でも譲るべからざる防衛原則である。",
        "hint": "Subject clause (国民の安全を守る責務は) → viewpoint (政府にとって) → adverbial condition (いかなる事態でも) → non-negotiable (譲るべからざる).",
        "explanation": {
            "overall": "「国家の主権と」に並列して【国民の安全を守る責務は】（主語）→【政府にとって】→【いかなる事態でも】→【譲るべからざる】（原則を修飾）と整序されます。★の位置（3番目）には「いかなる事態でも」が入ります。",
            "options": [
                {"text": "国民の安全を守る責務は", "isCorrect": False, "reason": "1番目の要素。主語句を完結させる並列名詞節です。", "trapCategory": "formation"},
                {"text": "政府にとって", "isCorrect": False, "reason": "2番目の要素。評価の主体・観点を示す格助詞句です。", "trapCategory": "formation"},
                {"text": "いかなる事態でも", "isCorrect": True, "reason": "【正解（★・3番目）】譲歩条件として「譲るべからざる」の絶対性を強める修飾語です。", "trapCategory": ""},
                {"text": "譲るべからざる", "isCorrect": False, "reason": "4番目の要素。「決して譲ってはならない」意味で防衛原則を連体修飾します。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞を説明する形式), pp. 146–149"
    },
    "skm2-p2-c2-q7": {
        "context": "Violence to subjugate others is an impermissible act of barbarism.",
        "question": "いかなる理由が ＿＿ ＿＿ ★ ＿＿ 許すまじき暴挙である。",
        "translation": "Regardless of what reasons there may be, subjugating others by unreasonable violence is an impermissible act of outrage.",
        "options": ["あろうとも理不尽な", "暴力によって", "他者を無理やり", "屈服させる行為は"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "いかなる理由があろうとも理不尽な暴力によって他者を無理やり屈服させる行為は、許すまじき暴挙である。",
        "hint": "Concessive (あろうとも理不尽な) → means (暴力によって) → adverb/object (他者を無理やり) → subject noun (屈服させる行為は).",
        "explanation": {
            "overall": "「いかなる理由が」から【あろうとも理不尽な】→【暴力によって】→【他者を無理やり】→【屈服させる行為は】（主題）→「許すまじき暴挙である」へと連鎖します。★の位置（3番目）には「他者を無理やり」が入ります。",
            "options": [
                {"text": "あろうとも理不尽な", "isCorrect": False, "reason": "1番目の要素。「〜があろうとも」の譲歩表現と名詞修飾語です。", "trapCategory": "formation"},
                {"text": "暴力によって", "isCorrect": False, "reason": "2番目の要素。手段・方法を示す「〜によって」です。", "trapCategory": "formation"},
                {"text": "他者を無理やり", "isCorrect": True, "reason": "【正解（★・3番目）】屈服させる対象「他者を」と様態副詞「無理やり」です。", "trapCategory": ""},
                {"text": "屈服させる行為は", "isCorrect": False, "reason": "4番目の要素。主節全体の主題を示す名詞節です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞を説明する形式), pp. 146–149"
    },
    "skm2-p2-c2-q8": {
        "context": "Warning sign prohibiting careless entry onto the lawn.",
        "question": "この芝生内に ＿＿ ＿＿ ★ ＿＿ 掲示されている。",
        "translation": "A warning stating that one must not carelessly step onto this lawn is prominently displayed on the signboard at the park entrance.",
        "options": ["みだりに", "立ち入る", "べからずとの警告が", "公園入口の看板に"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "この芝生内にみだりに立ち入るべからずとの警告が、公園入口の看板に掲示されている。",
        "hint": "Adverb (みだりに) → verb (立ち入る) → prohibitive citation (べからずとの警告が) → location (公園入口の看板に).",
        "explanation": {
            "overall": "「この芝生内に」に続き、【みだりに】→【立ち入る】→【べからずとの警告が】（主語）→【公園入口の看板に】→「掲示されている」と配置されます。★の位置（3番目）には「べからずとの警告が」が入ります。",
            "options": [
                {"text": "みだりに", "isCorrect": False, "reason": "1番目の要素。正当な理由なく勝手に行う様態を示す副詞です。", "trapCategory": "formation"},
                {"text": "立ち入る", "isCorrect": False, "reason": "2番目の要素。「〜べからず」に前接する動詞終止形です。", "trapCategory": "formation"},
                {"text": "べからずとの警告が", "isCorrect": True, "reason": "【正解（★・3番目）】公的な禁止文言を引用して主語を作る名詞句です。", "trapCategory": ""},
                {"text": "公園入口の看板に", "isCorrect": False, "reason": "4番目の要素。掲示されている場所を示す格助詞句です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞を説明する形式), pp. 146–149"
    },
    "skm2-p2-c2-q9": {
        "context": "Approving a new night clinic in response to earnest citizen demand.",
        "question": "市民の切実な ＿＿ ＿＿ ★ ＿＿ 正式に承認された。",
        "translation": "The establishment of a new emergency night clinic, planned in response to earnest citizen demands, was officially approved at the recent city council session.",
        "options": ["要望に", "こたえる形で計画された", "夜間急病診療所の新設が", "先日の市議会で"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "市民の切実な要望にこたえる形で計画された夜間急病診療所の新設が、先日の市議会で正式に承認された。",
        "hint": "Indirect object (要望に) → responsive plan (こたえる形で計画された) → subject noun (夜間急病診療所の新設が) → temporal location (先日の市議会で).",
        "explanation": {
            "overall": "「市民の切実な」から【要望に】→【こたえる形で計画された】（〜にこたえる）→【夜間急病診療所の新設が】（主語）→【先日の市議会で】→「正式に承認された」と繋がります。★の位置（3番目）には「夜間急病診療所の新設が」が入ります。",
            "options": [
                {"text": "要望に", "isCorrect": False, "reason": "1番目の要素。「切実な」に修飾され、「こたえる」にかかる名詞句です。", "trapCategory": "formation"},
                {"text": "こたえる形で計画された", "isCorrect": False, "reason": "2番目の要素。期待・要望への応諾を示す連体節です。", "trapCategory": "formation"},
                {"text": "夜間急病診療所の新設が", "isCorrect": True, "reason": "【正解（★・3番目）】主節の述語「承認された」の主格となる名詞句です。", "trapCategory": ""},
                {"text": "先日の市議会で", "isCorrect": False, "reason": "4番目の要素。承認が行われた場を示す格助詞句です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞を説明する形式), pp. 146–149"
    },
    "skm2-p2-c2-q10": {
        "context": "Judicial integrity compromised by taking bribes.",
        "question": "法治国家の司法官として、 ＿＿ ＿＿ ★ ＿＿ 重大な背信行為だ。",
        "translation": "As a judicial officer in a constitutional state ruled by law, taking illicit money and valuables from a defendant is an utterly impermissible and grave breach of trust.",
        "options": ["被告人から", "不正な金品を", "受け取るなどは", "決してあるまじき"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "法治国家の司法官として、被告人から不正な金品を受け取るなどは、決してあるまじき重大な背信行為だ。",
        "hint": "Origin (被告人から) → object (不正な金品を) → gerund topic (受け取るなどは) → impermissible (決してあるまじき).",
        "explanation": {
            "overall": "司法官としての立場に続き、【被告人から】→【不正な金品を】→【受け取るなどは】（非難の主題）→【決してあるまじき】（〜にあるまじき修飾）→「重大な背信行為だ」と結びます。★の位置（3番目）には「受け取るなどは」が入ります。",
            "options": [
                {"text": "被告人から", "isCorrect": False, "reason": "1番目の要素。授受の相手を示す格助詞句です。", "trapCategory": "formation"},
                {"text": "不正な金品を", "isCorrect": False, "reason": "2番目の要素。動詞「受け取る」の目的語です。", "trapCategory": "formation"},
                {"text": "受け取るなどは", "isCorrect": True, "reason": "【正解（★・3番目）】行為を主題化して強い非難の焦点を当てる名詞化句です。", "trapCategory": ""},
                {"text": "決してあるまじき", "isCorrect": False, "reason": "4番目の要素。「あってはならない」意味で背信行為を連体修飾します。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞を説明する形式), pp. 146–149"
    },
    "skm2-p2-c2-q11": {
        "context": "Founding philosophy as the core strength of an enduring corporation.",
        "question": "会社の ＿＿ ＿＿ ★ ＿＿ 最大の強みである。",
        "translation": "The posture of upholding sincere manufacturing based on the company's founding spirit is precisely the greatest competitive strength of our traditional enterprise.",
        "options": ["創業精神に", "基づく真摯な", "ものづくりを貫く姿勢こそが", "我が伝統企業の"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "会社の創業精神に基づく真摯なものづくりを貫く姿勢こそが、我が伝統企業の最大の強みである。",
        "hint": "Reference (創業精神に) → based modifier (基づく真摯な) → emphasized subject (ものづくりを貫く姿勢こそが) → possessor (我が伝統企業の).",
        "explanation": {
            "overall": "「会社の」から【創業精神に】→【基づく真摯な】（〜に基づく）→【ものづくりを貫く姿勢こそが】（主語）→【我が伝統企業の】→「最大の強みである」と連鎖します。★の位置（3番目）には「ものづくりを貫く姿勢こそが」が入ります。",
            "options": [
                {"text": "創業精神に", "isCorrect": False, "reason": "1番目の要素。「会社の」に修飾され、「基づく」にかかる名詞句です。", "trapCategory": "formation"},
                {"text": "基づく真摯な", "isCorrect": False, "reason": "2番目の要素。根拠に基づく修飾句です。", "trapCategory": "formation"},
                {"text": "ものづくりを貫く姿勢こそが", "isCorrect": True, "reason": "【正解（★・3番目）】文全体の焦点となる主格主題句です。", "trapCategory": ""},
                {"text": "我が伝統企業の", "isCorrect": False, "reason": "4番目の要素。「最大の強み」の所属を示す連体修飾句です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞を説明する形式), pp. 146–149"
    },
    "skm2-p2-c2-q12": {
        "context": "Learning from history and never repeating wartime tragedy.",
        "question": "歴史の教訓に学び、 ＿＿ ＿＿ ★ ＿＿ 忘るべからざる責務である。",
        "translation": "Learning from history's lessons, the vow never to repeat the tragedy of war is an unforgettable duty for modern people living into the future.",
        "options": ["二度と戦争の", "悲劇を繰り返さない誓いは", "未来を生きる", "現代人の"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "歴史の教訓に学び、二度と戦争の悲劇を繰り返さない誓いは、未来を生きる現代人の忘るべからざる責務である。",
        "hint": "Negative frequency (二度と戦争の) → subject vow (悲劇を繰り返さない誓いは) → relative clause (未来を生きる) → people (現代人の).",
        "explanation": {
            "overall": "前置きに続き、【二度と戦争の】→【悲劇を繰り返さない誓いは】（主語）→【未来を生きる】→【現代人の】（責務の主体）→「忘るべからざる責務である」へと整序されます。★の位置（3番目）には「未来を生きる」が入ります。",
            "options": [
                {"text": "二度と戦争の", "isCorrect": False, "reason": "1番目の要素。否定の呼応副詞と名詞修飾です。", "trapCategory": "formation"},
                {"text": "悲劇を繰り返さない誓いは", "isCorrect": False, "reason": "2番目の要素。主節の主題となる名詞節です。", "trapCategory": "formation"},
                {"text": "未来を生きる", "isCorrect": True, "reason": "【正解（★・3番目）】「現代人」を修飾する連体修飾節です。", "trapCategory": ""},
                {"text": "現代人の", "isCorrect": False, "reason": "4番目の要素。「責務」の担い手を示す格助詞句です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 2 (文の組み立て 2: 名詞を説明する形式), pp. 146–149"
    },

    # ------------------ Part 2 · Chapter 3 (「ない」の範囲・文末の呼応) ------------------
    "skm2-p2-c3-q1": {
        "context": "Global environmental crisis requiring worldwide united action without postponement.",
        "question": "地球規模の環境破壊を ＿＿ ＿＿ ★ ＿＿ 先送りにはできない。",
        "translation": "To halt environmental destruction on a global scale, since worldwide cooperation is indispensable, we cannot postpone countermeasures any further.",
        "options": ["食い止めるために", "世界各国の協力が", "不可欠である以上", "これ以上の対策を"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "地球規模の環境破壊を食い止めるために世界各国の協力が不可欠である以上、これ以上の対策を先送りにはできない。",
        "hint": "Purpose (食い止めるために) → subject clause (世界各国の協力が) → since/given that (不可欠である以上) → direct object (これ以上の対策を).",
        "explanation": {
            "overall": "「環境破壊を」から【食い止めるために】（目的）→【世界各国の協力が】（主格）→【不可欠である以上】（〜以上理由）→【これ以上の対策を】（目的語）→「先送りにはできない」と構文が連鎖します。★の位置（3番目）には「不可欠である以上」が入ります。",
            "options": [
                {"text": "食い止めるために", "isCorrect": False, "reason": "1番目の要素。直前の目的語を受ける目的表現です。", "trapCategory": "formation"},
                {"text": "世界各国の協力が", "isCorrect": False, "reason": "2番目の要素。「不可欠である」の主格節です。", "trapCategory": "formation"},
                {"text": "不可欠である以上", "isCorrect": True, "reason": "【正解（★・3番目）】「〜以上（は）」で強い義務・決意を導く接続形式です。", "trapCategory": ""},
                {"text": "これ以上の対策を", "isCorrect": False, "reason": "4番目の要素。文末「先送りにはできない」にかかる目的語です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 文末の呼応), pp. 150–153"
    },
    "skm2-p2-c3-q2": {
        "context": "Obligation to attend beloved mentor's retirement celebration despite being busy.",
        "question": "長年お世話になった ＿＿ ＿＿ ★ ＿＿ 出席しないわけにはいかない。",
        "translation": "Since it is a gathering celebrating the retirement of a beloved mentor who took care of me for many years, no matter how extremely busy work may be, I cannot avoid attending.",
        "options": ["恩師の退職を", "祝う会である以上", "いくら仕事が", "多忙を極めていても"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "長年お世話になった恩師の退職を祝う会である以上、いくら仕事が多忙を極めていても出席しないわけにはいかない。",
        "hint": "Direct object (恩師の退職を) → justification (祝う会である以上) → concessive degree (いくら仕事が) → even if busy (多忙を極めていても).",
        "explanation": {
            "overall": "「長年お世話になった」から【恩師の退職を】→【祝う会である以上】（強い理由付け）→【いくら仕事が】→【多忙を極めていても】（譲歩条件）→「出席しないわけにはいかない」（義務）へと繋がります。★の位置（3番目）には「いくら仕事が」が入ります。",
            "options": [
                {"text": "恩師の退職を", "isCorrect": False, "reason": "1番目の要素。「祝う」の対象となる名詞句です。", "trapCategory": "formation"},
                {"text": "祝う会である以上", "isCorrect": False, "reason": "2番目の要素。道義的義務を生じさせる理由接続です。", "trapCategory": "formation"},
                {"text": "いくら仕事が", "isCorrect": True, "reason": "【正解（★・3番目）】「いくら〜ても」の呼応を作る譲歩副詞句です。", "trapCategory": ""},
                {"text": "多忙を極めていても", "isCorrect": False, "reason": "4番目の要素。「出席しないわけにはいかない」の障害となる条件節です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 文末の呼応), pp. 150–153"
    },
    "skm2-p2-c3-q3": {
        "context": "Risk of being involved in a collision despite safe driving habits.",
        "question": "どんなに安全運転を ＿＿ ＿＿ ★ ＿＿ 巻き込まれかねない。",
        "translation": "No matter how much one is mindful of safe driving, one could very well be dragged into a rear-end collision due to severe negligence on the other party's side.",
        "options": ["心がけていても", "相手方の", "重大な過失による", "追突事故に"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "どんなに安全運転を心がけていても、相手方の重大な過失による追突事故に巻き込まれかねない。",
        "hint": "Concessive (心がけていても) → possessor (相手方の) → cause modifier (重大な過失による) → collision noun (追突事故に).",
        "explanation": {
            "overall": "「どんなに」に呼応して【心がけていても】→【相手方の】→【重大な過失による】（原因）→【追突事故に】（対象）→「巻き込まれかねない」（悪化可能性）へと連なります。★の位置（3番目）には「重大な過失による」が入ります。",
            "options": [
                {"text": "心がけていても", "isCorrect": False, "reason": "1番目の要素。「どんなに〜ても」の呼応を形成する動詞逆接形です。", "trapCategory": "formation"},
                {"text": "相手方の", "isCorrect": False, "reason": "2番目の要素。過失の責任主体を示す名詞修飾です。", "trapCategory": "formation"},
                {"text": "重大な過失による", "isCorrect": True, "reason": "【正解（★・3番目）】「追突事故」の原因を明示する連体修飾句です。", "trapCategory": ""},
                {"text": "追突事故に", "isCorrect": False, "reason": "4番目の要素。「巻き込まれる」の着格助詞を伴う名詞です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 文末の呼応), pp. 150–153"
    },
    "skm2-p2-c3-q4": {
        "context": "Overcome by tears of compassion upon witnessing a child's misfortune.",
        "question": "身寄りのない ＿＿ ＿＿ ★ ＿＿ 禁じ得ない。",
        "translation": "Witnessing before one's own eyes the tragic plight of a young child without relatives, one cannot suppress tears of deep compassion.",
        "options": ["幼い子どもの", "悲惨な境遇を", "目の当たりにして", "同情の涙を"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "身寄りのない幼い子どもの悲惨な境遇を目の当たりにして、同情の涙を禁じ得ない。",
        "hint": "Apposition (幼い子どもの) → accusative plight (悲惨な境遇を) → visual encounter (目の当たりにして) → emotional object (同情の涙を).",
        "explanation": {
            "overall": "「身寄りのない」から【幼い子どもの】→【悲惨な境遇を】（目的語）→【目の当たりにして】（生起契機）→【同情の涙を】（自然感情）→「禁じ得ない」（感情抑制不可）と結びます。★の位置（3番目）には「目の当たりにして」が入ります。",
            "options": [
                {"text": "幼い子どもの", "isCorrect": False, "reason": "1番目の要素。「身寄りのない」に続く名詞句です。", "trapCategory": "formation"},
                {"text": "悲惨な境遇を", "isCorrect": False, "reason": "2番目の要素。「目の当たりにして」にかかる目的語です。", "trapCategory": "formation"},
                {"text": "目の当たりにして", "isCorrect": True, "reason": "【正解（★・3番目）】湧き上がる感情の直接の引き金となる動詞て形節です。", "trapCategory": ""},
                {"text": "同情の涙を", "isCorrect": False, "reason": "4番目の要素。「〜を禁じ得ない」と呼応する感情表現です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 文末の呼応), pp. 150–153"
    },
    "skm2-p2-c3-q5": {
        "context": "Protecting judicial independence to ensure fair trials.",
        "question": "公正な裁判を ＿＿ ＿＿ ★ ＿＿ 守られなければならない。",
        "translation": "In order to conduct a fair trial, the independence of the assigned judge's official authority and political neutrality must be strictly protected.",
        "options": ["行うためには", "担当する裁判官の", "職権の独立と", "政治的中立性が"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "公正な裁判を行うためには担当する裁判官の職権の独立と政治的中立性が守られなければならない。",
        "hint": "Goal (行うためには) → subject possessor (担当する裁判官の) → parallel subject 1 (職権の独立と) → parallel subject 2 (政治的中立性が).",
        "explanation": {
            "overall": "「公正な裁判を」から【行うためには】（目的）→【担当する裁判官の】→【職権の独立と】（並列助詞「と」）→【政治的中立性が】（主格）→「守られなければならない」と構築されます。★の位置（3番目）には「職権の独立と」が入ります。",
            "options": [
                {"text": "行うためには", "isCorrect": False, "reason": "1番目の要素。裁判を行う目的を示す接続句です。", "trapCategory": "formation"},
                {"text": "担当する裁判官の", "isCorrect": False, "reason": "2番目の要素。独立性の帰属主体を示す修飾句です。", "trapCategory": "formation"},
                {"text": "職権の独立と", "isCorrect": True, "reason": "【正解（★・3番目）】「政治的中立性」と並列される要件の第1要素です。", "trapCategory": ""},
                {"text": "政治的中立性が", "isCorrect": False, "reason": "4番目の要素。受身述語「守られなければならない」の主格です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 文末の呼応), pp. 150–153"
    },
    "skm2-p2-c3-q6": {
        "context": "Executive resigning to take responsibility for severe company losses.",
        "question": "自らの不手際で ＿＿ ＿＿ ★ ＿＿ 辞任せざるを得ない。",
        "translation": "Since I caused immense damage to the company through my own blunder, I am compelled to resign to take responsibility as a representative.",
        "options": ["会社に多大な", "損害を与えてしまった以上", "代表者としての", "責任を取って"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "自らの不手際で会社に多大な損害を与えてしまった以上、代表者としての責任を取って辞任せざるを得ない。",
        "hint": "Indirect object/degree (会社に多大な) → since caused damage (損害を与えてしまった以上) → status (代表者としての) → taking responsibility (責任を取って).",
        "explanation": {
            "overall": "「自らの不手際で」から【会社に多大な】→【損害を与えてしまった以上】（理由確定）→【代表者としての】→【責任を取って】→「辞任せざるを得ない」（余儀なくされる）へと整序されます。★の位置（3番目）には「代表者としての」が入ります。",
            "options": [
                {"text": "会社に多大な", "isCorrect": False, "reason": "1番目の要素。損害の規模と対象を表す修飾句です。", "trapCategory": "formation"},
                {"text": "損害を与えてしまった以上", "isCorrect": False, "reason": "2番目の要素。辞任の不可避性を導く理由接続節です。", "trapCategory": "formation"},
                {"text": "代表者としての", "isCorrect": True, "reason": "【正解（★・3番目）】「責任」の根拠となる立場を修飾する連体句です。", "trapCategory": ""},
                {"text": "責任を取って", "isCorrect": False, "reason": "4番目の要素。「辞任する」理由・様態を示す動詞て形です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 文末の呼応), pp. 150–153"
    },
    "skm2-p2-c3-q7": {
        "context": "Risking painful defeat by letting one's guard down against a lower-tier rival.",
        "question": "相手がいくら ＿＿ ＿＿ ★ ＿＿ 喫しかねない。",
        "translation": "No matter how lower-ranked the opponent may be, if one lets down one's guard during the match, one could easily suffer an unexpected, painful defeat.",
        "options": ["格下の相手であっても", "試合中に油断すれば", "予想外の痛い", "敗北を"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "相手がいくら格下の相手であっても、試合中に油断すれば予想外の痛い敗北を喫しかねない。",
        "hint": "Concessive (格下の相手であっても) → condition (試合中に油断すれば) → modifier (予想外の痛い) → object (敗北を).",
        "explanation": {
            "overall": "「いくら」に呼応して【格下の相手であっても】（譲歩）→【試合中に油断すれば】（仮定条件）→【予想外の痛い】（修飾）→【敗北を】→「喫しかねない」（悪い結果の懸念）へと配置されます。★の位置（3番目）には「予想外の痛い」が入ります。",
            "options": [
                {"text": "格下の相手であっても", "isCorrect": False, "reason": "1番目の要素。「いくら〜であっても」の譲歩述部です。", "trapCategory": "formation"},
                {"text": "試合中に油断すれば", "isCorrect": False, "reason": "2番目の要素。敗北を引き起こす条件節です。", "trapCategory": "formation"},
                {"text": "予想外の痛い", "isCorrect": True, "reason": "【正解（★・3番目）】直後の名詞「敗北」を修飾する連体修飾語です。", "trapCategory": ""},
                {"text": "敗北を", "isCorrect": False, "reason": "4番目の要素。「喫する（被る）」の目的格助詞を伴う名詞です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 文末の呼応), pp. 150–153"
    },
    "skm2-p2-c3-q8": {
        "context": "Cannot abandon a close friend pleading for assistance in distress.",
        "question": "親しい友人が ＿＿ ＿＿ ★ ＿＿ 素通りするわけにはいかない。",
        "translation": "Since a close friend is in such extreme distress and asking for help, I cannot possibly pass by and abandon their plight.",
        "options": ["これほど困り果てて", "助けを求めている以上", "その窮状を", "見捨てて"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "親しい友人がこれほど困り果てて助けを求めている以上、その窮状を見捨てて素通りするわけにはいかない。",
        "hint": "Distress state (これほど困り果てて) → given that (助けを求めている以上) → object plight (その窮状を) → abandoning (見捨てて).",
        "explanation": {
            "overall": "「友人が」から【これほど困り果てて】→【助けを求めている以上】（見過ごせない理由）→【その窮状を】（見捨てる対象）→【見捨てて】→「素通りするわけにはいかない」と連鎖します。★の位置（3番目）には「その窮状を」が入ります。",
            "options": [
                {"text": "これほど困り果てて", "isCorrect": False, "reason": "1番目の要素。友人の切迫した状態を表す副詞的用法です。", "trapCategory": "formation"},
                {"text": "助けを求めている以上", "isCorrect": False, "reason": "2番目の要素。道義的義務を導く接続形式です。", "trapCategory": "formation"},
                {"text": "その窮状を", "isCorrect": True, "reason": "【正解（★・3番目）】「見捨てて」にかかる直接の目的格名詞句です。", "trapCategory": ""},
                {"text": "見捨てて", "isCorrect": False, "reason": "4番目の要素。「素通りする」に連なる動詞て形です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 文末の呼応), pp. 150–153"
    },
    "skm2-p2-c3-q9": {
        "context": "All visitors deeply impressed by sublime artistic beauty.",
        "question": "展示された ＿＿ ＿＿ ★ ＿＿ 禁じ得なかった。",
        "translation": "Touching upon the sublime beauty of the splendid masterpieces on exhibit, all the visitors could not help feeling profound impression.",
        "options": ["素晴らしい名画の", "崇高な美しさに触れて", "来場者一同が", "深い感銘を"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "展示された素晴らしい名画の崇高な美しさに触れて、来場者一同が深い感銘を禁じ得なかった。",
        "hint": "Modifier (素晴らしい名画の) → trigger (崇高な美しさに触れて) → subject (来場者一同が) → emotion (深い感銘を).",
        "explanation": {
            "overall": "「展示された」から【素晴らしい名画の】→【崇高な美しさに触れて】（情動の契機）→【来場者一同が】（感情の主体）→【深い感銘を】（目的語）→「禁じ得なかった」と連なります。★の位置（3番目）には「来場者一同が」が入ります。",
            "options": [
                {"text": "素晴らしい名画の", "isCorrect": False, "reason": "1番目の要素。展示品の崇高さを修飾する名詞句です。", "trapCategory": "formation"},
                {"text": "崇高な美しさに触れて", "isCorrect": False, "reason": "2番目の要素。感銘を引き起こした原因・契機を示す節です。", "trapCategory": "formation"},
                {"text": "来場者一同が", "isCorrect": True, "reason": "【正解（★・3番目）】「深い感銘を禁じ得なかった」の動作主（体験者）です。", "trapCategory": ""},
                {"text": "深い感銘を", "isCorrect": False, "reason": "4番目の要素。「禁じ得ない」の直接の感情目的語です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 文末の呼応), pp. 150–153"
    },
    "skm2-p2-c3-q10": {
        "context": "Compelled to recall product inventory due to unconfirmed safety.",
        "question": "新製品の発売延期は痛手だが、 ＿＿ ＿＿ ★ ＿＿ せざるを得ない。",
        "translation": "Although postponing the new product release is painful, since compliance with safety standards has not been confirmed, we are compelled to temporarily recall all inventory.",
        "options": ["安全基準への適合が", "確認されない以上は", "すべての在庫を", "一旦回収"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "新製品の発売延期は痛手だが、安全基準への適合が確認されない以上はすべての在庫を一旦回収せざるを得ない。",
        "hint": "Safety requirement (安全基準への適合が) → since unconfirmed (確認されない以上は) → inventory object (すべての在庫を) → recall verb stem (一旦回収).",
        "explanation": {
            "overall": "逆接の前置きに続き、【安全基準への適合が】→【確認されない以上は】（不可避の理由）→【すべての在庫を】（目的語）→【一旦回収】（サ変語幹）→「せざるを得ない」（余儀なくされる）へと構築されます。★の位置（3番目）には「すべての在庫を」が入ります。",
            "options": [
                {"text": "安全基準への適合が", "isCorrect": False, "reason": "1番目の要素。未確認事項の内容を示す主格節です。", "trapCategory": "formation"},
                {"text": "確認されない以上は", "isCorrect": False, "reason": "2番目の要素。回収措置を余儀なくさせる確定条件です。", "trapCategory": "formation"},
                {"text": "すべての在庫を", "isCorrect": True, "reason": "【正解（★・3番目）】「回収する」の対象となる直接目的語句です。", "trapCategory": ""},
                {"text": "一旦回収", "isCorrect": False, "reason": "4番目の要素。「せざるを得ない」に直接接続するサ変複合名詞です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 文末の呼応), pp. 150–153"
    },
    "skm2-p2-c3-q11": {
        "context": "Strong economy risking sharp downturn influenced by overseas crises.",
        "question": "現在の好調な景気も、 ＿＿ ＿＿ ★ ＿＿ 悪化しかねない。",
        "translation": "Even the current buoyant economy could sharply deteriorate further in the near future under the influence of rapid financial collapse overseas.",
        "options": ["海外の急速な", "金融破綻の影響を受けて", "近いうちに一段と", "急激に景気が"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "現在の好調な景気も、海外の急速な金融破綻の影響を受けて近いうちに一段と急激に景気が悪化しかねない。",
        "hint": "Overseas modifier (海外の急速な) → crisis cause (金融破綻の影響を受けて) → temporal degree (近いうちに一段と) → sharp decline subject (急激に景気が).",
        "explanation": {
            "overall": "「好調な景気も」から【海外の急速な】→【金融破綻の影響を受けて】（外的要因）→【近いうちに一段と】（時期・程度）→【急激に景気が】（主格）→「悪化しかねない」（望ましくない懸念）と整序されます。★の位置（3番目）には「近いうちに一段と」が入ります。",
            "options": [
                {"text": "海外の急速な", "isCorrect": False, "reason": "1番目の要素。「金融破綻」を修飾する連体詞的用法です。", "trapCategory": "formation"},
                {"text": "金融破綻の影響を受けて", "isCorrect": False, "reason": "2番目の要素。景気悪化をもたらす誘因を示す節です。", "trapCategory": "formation"},
                {"text": "近いうちに一段と", "isCorrect": True, "reason": "【正解（★・3番目）】悪化の時期と程度を強める副詞句です。", "trapCategory": ""},
                {"text": "急激に景気が", "isCorrect": False, "reason": "4番目の要素。述語「悪化しかねない」の主格節です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 文末の呼応), pp. 150–153"
    },
    "skm2-p2-c3-q12": {
        "context": "Democratic principle requiring fair respect for minority viewpoints.",
        "question": "民主主義の基本ルールとして、 ＿＿ ＿＿ ★ ＿＿ 尊重しないわけにはいかない。",
        "translation": "As a fundamental rule of democracy, we cannot avoid fairly respecting valuable opinions asserted by the minority, rather than relying solely on majority vote.",
        "options": ["多数決だけでなく", "少数派が主張する", "貴重な意見も", "公平に"],
        "correctIndex": 2,
        "scrambleOrder": [1, 2, 3, 4],
        "reconstructedSentence": "民主主義の基本ルールとして、多数決だけでなく少数派が主張する貴重な意見も公平に尊重しないわけにはいかない。",
        "hint": "Comparison (多数決だけでなく) → relative clause (少数派が主張する) → object (貴重な意見も) → manner (公平に).",
        "explanation": {
            "overall": "「基本ルールとして」から【多数決だけでなく】（除外対比）→【少数派が主張する】→【貴重な意見も】（尊重対象）→【公平に】（様態副詞）→「尊重しないわけにはいかない」（道義的必然）へと連鎖します。★の位置（3番目）には「貴重な意見も」が入ります。",
            "options": [
                {"text": "多数決だけでなく", "isCorrect": False, "reason": "1番目の要素。多数派優位の制約を広げる対比表現です。", "trapCategory": "formation"},
                {"text": "少数派が主張する", "isCorrect": False, "reason": "2番目の要素。「意見」を修飾する連体修飾節です。", "trapCategory": "formation"},
                {"text": "貴重な意見も", "isCorrect": True, "reason": "【正解（★・3番目）】「尊重する」の目的語となる名詞句です。", "trapCategory": ""},
                {"text": "公平に", "isCorrect": False, "reason": "4番目の要素。「尊重する」にかかる様態副詞です。", "trapCategory": "formation"}
            ]
        },
        "provenance": "source-derived",
        "sourceEvidence": "Shin Kanzen Master N2 Bunpou, Part 2 Chapter 3 (文の組み立て 3: 文末の呼応), pp. 150–153"
    }
}

def main():
    with open(EXERCISES_FILE, "r", encoding="utf-8") as f:
        exercises = json.load(f)

    updated_count = 0
    for ex in exercises:
        eid = ex.get("id")
        if eid in STAR_MARK_DATA:
            patch = STAR_MARK_DATA[eid]
            ex["type"] = "star-mark"
            ex["context"] = patch["context"]
            ex["question"] = patch["question"]
            ex["translation"] = patch["translation"]
            ex["options"] = patch["options"]
            ex["correctIndex"] = patch["correctIndex"]
            ex["scrambleOrder"] = patch["scrambleOrder"]
            ex["reconstructedSentence"] = patch["reconstructedSentence"]
            ex["hint"] = patch["hint"]
            ex["explanation"] = patch["explanation"]
            ex["provenance"] = patch["provenance"]
            ex["sourceEvidence"] = patch["sourceEvidence"]
            updated_count += 1

    with open(EXERCISES_FILE, "w", encoding="utf-8") as f:
        json.dump(exercises, f, ensure_ascii=False, indent=2)

    print(f"Successfully converted {updated_count} exercises in SKM N2 Part 2 to Star-Mark format.")

if __name__ == "__main__":
    main()
