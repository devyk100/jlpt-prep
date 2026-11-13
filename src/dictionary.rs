use std::collections::HashMap;

#[derive(Debug, Clone)]
pub struct KanjiInfo {
    pub character: char,
    pub onyomi: &'static str,
    #[allow(dead_code)]
    pub kunyomi: &'static str,
    pub meaning: &'static str,
}

#[derive(Debug, Clone)]
pub struct WordInfo {
    #[allow(dead_code)]
    pub surface: &'static str,
    pub reading: &'static str,
    pub meaning: &'static str,
    #[allow(dead_code)]
    pub part_of_speech: &'static str,
}

#[derive(Debug, Clone)]
pub struct GrammarNote {
    pub pattern: &'static str,
    pub meaning: &'static str,
    pub explanation: &'static str,
}

pub struct LocalDictionary {
    pub kanji_map: HashMap<char, KanjiInfo>,
    pub word_map: HashMap<&'static str, WordInfo>,
    pub grammar_rules: Vec<GrammarNote>,
}

impl LocalDictionary {
    pub fn new() -> Self {
        let mut kd = HashMap::new();
        let mut wd = HashMap::new();

        // 1. Core Immersion Kanji Database (Persona, JRPGs, Anime, Daily)
        let kanji_data: &[(char, &str, &str, &str)] = &[
            // Persona & JRPG staples
            ('悪', "アク, オ", "わる・い", "bad, evil, wrong"),
            ('魔', "マ", "", "demon, evil spirit, magic"),
            ('心', "シン", "こころ", "heart, mind, spirit"),
            ('怪', "カイ, ケ", "あや・しい", "suspicious, mystery, phantom"),
            ('盗', "トウ", "ぬす・む", "steal, rob, thief"),
            ('団', "ダン, トン", "", "group, association, team"),
            ('仮', "カ, ケ", "かり", "temporary, mask, hypothetical"),
            ('面', "メン, ベン", "おも, つら", "mask, face, surface"),
            ('命', "メイ, ミョウ", "いのち", "life, fate, destiny"),
            ('運', "ウン", "はこ・ぶ", "carry, luck, destiny"),
            ('世', "セイ, セ", "よ", "world, generation, society"),
            ('界', "カイ", "", "world, boundary, sphere"),
            ('自', "ジ, シ", "みずか・ら", "oneself, self"),
            ('由', "ユ, ユウ", "よし", "reason, freedom, origin"),
            ('選', "セン", "えら・ぶ", "choose, select, elect"),
            ('択', "タク", "", "choose, pick, select"),
            ('力', "リョク, リキ", "ちから", "power, strength, ability"),
            ('魂', "コン", "たましい", "soul, spirit"),
            ('戦', "セン", "たたか・う, いくさ", "war, fight, battle"),
            ('闘', "トウ", "たたか・う", "fight, battle, struggle"),
            ('勝', "ショウ", "か・つ", "win, victory, excel"),
            ('敗', "ハイ", "やぶ・れる", "failure, defeat, loss"),
            ('友', "ユウ", "とも", "friend, companion"),
            ('仲', "チュウ", "なか", "relationship, comrade, middle"),
            ('間', "カン, ケン", "あいだ, ま", "interval, space, between"),
            ('絆', "ハン", "きずな", "bonds, emotional ties"),
            ('信', "シン", "", "trust, faith, believe, message"),
            ('頼', "ライ", "たの・む, たよ・る", "trust, rely on, request"),
            ('真', "シン", "ま, まこと", "truth, reality, genuine"),
            ('実', "ジツ, シツ", "み, みの・る", "truth, reality, fruit"),
            ('偽', "ギ", "いつわ・る, にせ", "false, fake, deceive"),
            ('嘘', "キョ", "うそ", "lie, falsehood"),
            ('情', "ジョウ, セイ", "なさ・け", "feelings, emotion, circumstances"),
            ('報', "ホウ", "むく・いる", "report, news, reward"),
            ('考', "コウ", "かんが・える", "think, consider"),
            ('思', "シ", "おも・う", "think, recall, thought"),
            ('知', "チ", "し・る", "know, understand"),
            ('見', "ケン", "み・る", "see, look, view"),
            ('聞', "ブン, モン", "き・く", "hear, ask, listen"),
            ('言', "ゲン, ゴン", "い・う, こと", "say, word, speech"),
            ('話', "ワ", "はな・す, はなし", "talk, speak, story"),
            ('行', "コウ, ギョウ", "い・く, おこな・う", "go, act, carry out"),
            ('来', "ライ", "く・る, きた・る", "come, arrive, future"),
            ('帰', "キ", "かえ・る", "return, go home"),
            ('出', "シュツ, スイ", "で・る, だ・す", "exit, go out, produce"),
            ('入', "ニュウ", "はい・る, い・れる", "enter, insert"),
            ('食', "ショク, ジキ", "た・べる, く・う", "eat, food"),
            ('飲', "イン", "の・む", "drink"),
            ('死', "シ", "し・ぬ", "death, die"),
            ('生', "セイ, ショウ", "い・きる, う・まれる", "life, birth, live"),
            ('殺', "サツ, サイ", "ころ・す", "kill, murder"),
            ('助', "ジョ", "たす・ける", "help, rescue, assist"),
            ('救', "キュウ", "すく・う", "save, rescue, salvage"),
            ('守', "シュ, ス", "まも・る", "protect, guard, defend"),
            ('攻', "コウ", "せ・める", "attack, offense"),
            ('防', "ボウ", "ふせ・ぐ", "defend, prevent, ward off"),
            ('撃', "ゲキ", "う・つ", "strike, hit, attack"),
            ('敵', "テキ", "かたき", "enemy, foe, rival"),
            ('味', "ミ", "あじ", "flavor, taste, ally (味方)"),
            ('方', "ホウ", "かた", "direction, person, method"),
            ('時', "ジ", "とき", "time, hour"),
            ('今', "コン, キン", "いま", "now, present"),
            ('日', "ニチ, ジツ", "ひ, か", "day, sun, Japan"),
            ('月', "ゲツ, ガツ", "つき", "month, moon"),
            ('年', "ネン", "とし", "year"),
            ('夜', "ヤ", "よ, よる", "night, evening"),
            ('朝', "チョウ", "あさ", "morning"),
            ('前', "ゼン", "まえ", "before, front, ahead"),
            ('後', "ゴ, コウ", "のち, うし・ろ, あと", "behind, after, later"),
            ('何', "カ", "なに, なん", "what, which"),
            ('誰', "", "だれ", "who, someone"),
            ('僕', "ボク", "", "I, me (masculine), servant"),
            ('俺', "", "おれ", "I, me (informal masculine)"),
            ('私', "シ", "わたし, わたくし", "I, me, private"),
            ('君', "クン", "きみ", "you, ruler, boy"),
            ('彼', "ヒ", "かれ, かの", "he, that"),
            ('女', "ジョ, ニョ", "おんな, め", "woman, female"),
            ('男', "ダン, ナン", "おとこ", "man, male"),
            ('人', "ジン, ニン", "ひと", "person, human"),
            ('子', "シ, ス", "こ", "child, offspring"),
            ('親', "シン", "おや, した・しい", "parent, intimacy, close"),
            ('手', "シュ", "て", "hand, arm, method"),
            ('目', "モク, ボク", "め", "eye, look, insight"),
            ('口', "コウ, ク", "くち", "mouth, opening"),
            ('気', "キ, ケ", "", "spirit, mind, mood, air"),
            ('持', "ジ", "も・つ", "hold, possess, have"),
            ('待', "タイ", "ま・つ", "wait, depend on"),
            ('分', "ブン, フン, ブ", "わ・かる, わ・ける", "part, minute, understand"),
            ('合', "ゴウ, ガッ", "あ・う, あ・わせる", "fit, join, match, meet"),
            ('会', "カイ, エ", "あ・う", "meet, party, society"),
            ('話', "ワ", "はな・す", "talk, story"),
            ('困', "コン", "こま・る", "quandary, distressed, troubled"),
            ('難', "ナン", "むずか・しい", "difficult, trouble, hardship"),
            ('易', "エキ, イ", "やさ・しい", "easy, exchange, divination"),
            ('変', "ヘン", "か・わる, か・える", "strange, change, unusual"),
            ('同', "ドウ", "おな・じ", "same, equal, agree"),
            ('違', "イ", "ちが・う, ちが・える", "differ, vary, mistake"),
            ('要', "ヨウ", "い・る, かなめ", "need, vital, essential"),
            ('必', "ヒツ", "かなら・ず", "invariably, certain, inevitable"),
            ('断', "ダン", "ことわ・る, た・つ", "refuse, sever, resolve"),
            ('決', "ケツ", "き・める, き・まる", "decide, determine, agree"),
            ('定', "テイ, ジョウ", "さだ・める", "determine, fix, establish"),
            ('約', "ヤク", "", "promise, approximate"),
            ('束', "ソク", "たば", "bundle, tie, control (約束)"),
            ('道', "ドウ, トウ", "みち", "road, path, way, teachings"),
            ('歩', "ホ, ブ", "ある・く, あゆ・む", "walk, step"),
            ('走', "ソウ", "はし・る", "run, rush"),
            ('飛', "ヒ", "と・ぶ", "fly, jump"),
            ('落', "ラク", "お・ちる, お・とす", "fall, drop"),
            ('終', "シュウ", "お・わる", "end, finish"),
            ('始', "シ", "はじ・まる", "begin, start"),
            ('開', "カイ", "ひら・く, あ・ける", "open, unfold"),
            ('閉', "ヘイ", "と・じる, し・める", "close, shut"),
            ('止', "シ", "と・まる, と・める", "stop, halt"),
            ('動', "ドウ", "うご・く", "move, motion, change"),
            ('静', "セイ, ジョウ", "しず・か", "quiet, peaceful"),
            ('光', "コウ", "ひかり", "light, ray"),
            ('闇', "アン", "やみ", "darkness, gloom"),
            ('影', "エイ", "かげ", "shadow, silhouette"),
            ('夢', "ム", "ゆめ", "dream, vision"),
            ('幻', "ゲン", "まぼろし", "phantom, illusion, vision"),
            ('願', "ガン", "ねが・う", "request, wish, pray"),
            ('望', "ボウ, モウ", "のぞ・む", "hope, desire, ambition"),
            ('解', "カイ, ゲ", "と・く, わか・る", "untie, solve, explain"),
            ('覚', "カク", "おぼ・える, さ・める", "remember, awake, perceive"),
            ('忘', "ボウ", "わす・れる", "forget"),
            ('愛', "アイ", "", "love, affection, favorite"),
            ('恋', "レン", "こい, こい・しい", "romance, in love, yearning"),
            ('怖', "フ", "こわ・い", "scary, frightening, fear"),
            ('恐', "キョウ", "おそ・れる", "fear, dread, awe"),
            ('怒', "ド", "いか・る, おこ・る", "angry, rage"),
            ('悲', "ヒ", "かな・しい", "sad, grieve, sorrow"),
            ('喜', "キ", "よろこ・ぶ", "rejoice, take pleasure in"),
            ('楽', "ラク, ガク", "たの・しい", "music, comfort, fun, ease"),
            ('苦', "ク", "くる・しい, にが・い", "pain, bitter, suffering"),
            ('痛', "ツウ", "いた・い", "pain, hurt, bruise"),
            ('傷', "ショウ", "きず, いた・む", "wound, hurt, injury"),
            ('癒', "ユ", "い・やす", "heal, cure, soothe"),
            ('強', "キョウ, ゴウ", "つよ・い", "strong, forceful"),
            ('弱', "ジャク", "よわ・い", "weak, frail"),
            ('高', "コウ", "たか・い", "tall, high, expensive"),
            ('低', "テイ", "ひく・い", "low, short, humble"),
            ('深', "シン", "ふか・い", "deep, profound"),
            ('浅', "セン", "あさ・い", "shallow, superficial"),
            ('重', "ジュウ, チョウ", "おも・い, かさ・なる", "heavy, important, duplicate"),
            ('軽', "ケイ", "かる・い", "light, minor, frivolous"),
        ];

        for &(ch, on, kun, mean) in kanji_data {
            kd.insert(
                ch,
                KanjiInfo {
                    character: ch,
                    onyomi: on,
                    kunyomi: kun,
                    meaning: mean,
                },
            );
        }

        // 2. High-Frequency Immersion Vocabulary
        let words: &[(&str, &str, &str, &str)] = &[
            ("怪盗団", "かいとうだん", "Phantom Thieves", "noun"),
            ("怪盗", "かいとう", "phantom thief, gentleman burglar", "noun"),
            ("仮面", "かめん", "mask, persona", "noun"),
            ("悪魔", "あくま", "demon, devil", "noun"),
            ("ペルソナ", "ペルソナ", "Persona, personality mask", "noun"),
            ("仲間", "なかま", "companion, comrade, ally", "noun"),
            ("絆", "きずな", "bonds, emotional ties", "noun"),
            ("運命", "うんめい", "destiny, fate", "noun"),
            ("世界", "せかい", "world, universe", "noun"),
            ("自由", "じゆう", "freedom, liberty", "noun"),
            ("真実", "しんじつ", "truth, reality", "noun"),
            ("嘘", "うそ", "lie, falsehood", "noun"),
            ("選択", "せんたく", "choice, selection", "noun"),
            ("決断", "けつだん", "decision, resolution", "noun"),
            ("約束", "やくそく", "promise, agreement", "noun"),
            ("時間", "じかん", "time, hours", "noun"),
            ("気持ち", "きもち", "feeling, mood, sensation", "noun"),
            ("心", "こころ", "heart, mind, spirit", "noun"),
            ("力", "ちから", "power, strength, ability", "noun"),
            ("情報", "じょうほう", "information, intel", "noun"),
            ("処理", "しょり", "processing, disposal, treatment", "noun"),
            ("言われても", "いわれても", "even if told / even if you say that", "expression"),
            ("困る", "こまる", "to be troubled, at a loss, perplexed", "verb"),
            ("困った", "こまった", "troubled, in a fix, Oh dear", "expression"),
            ("何", "なに", "what", "pronoun"),
            ("誰", "だれ", "who", "pronoun"),
            ("どこ", "どこ", "where", "pronoun"),
            ("いつ", "いつ", "when", "pronoun"),
            ("どうして", "どうして", "why, how come", "adverb"),
            ("なぜ", "なぜ", "why, for what reason", "adverb"),
            ("本当", "ほんとう", "truth, really, truly", "noun/adverb"),
            ("大丈夫", "だいじょうぶ", "all right, okay, safe", "na-adjective"),
            ("無理", "むり", "impossible, unreasonable, straining", "na-adjective"),
            ("簡単", "かんたん", "simple, easy", "na-adjective"),
            ("危険", "きけん", "danger, hazard, perilous", "na-adjective"),
            ("秘密", "ひみつ", "secret, mystery", "noun"),
            ("覚悟", "かくご", "resolution, readiness, preparedness", "noun/suru"),
            ("諦める", "あきらめる", "to give up, abandon hope", "verb"),
            ("信じる", "しんじる", "to believe, trust in", "verb"),
            ("戦う", "たたかう", "to fight, battle, struggle", "verb"),
            ("助ける", "たすける", "to help, rescue, assist", "verb"),
            ("守る", "まもる", "to protect, defend, obey", "verb"),
            ("行く", "いく", "to go, proceed", "verb"),
            ("来る", "くる", "to come, approach", "verb"),
            ("帰る", "かえる", "to go back, return home", "verb"),
            ("言う", "いう", "to say, utter, tell", "verb"),
            ("話す", "はなす", "to speak, converse", "verb"),
            ("見る", "みる", "to see, look, watch", "verb"),
            ("聞く", "きく", "to hear, listen, ask", "verb"),
            ("知る", "しる", "to know, understand", "verb"),
            ("分かる", "わかる", "to understand, comprehend", "verb"),
            ("思う", "おもう", "to think, feel, consider", "verb"),
            ("考える", "かんがえる", "to contemplate, reflect, plan", "verb"),
            ("待つ", "まつ", "to wait, await", "verb"),
            ("持つ", "もつ", "to hold, possess, carry", "verb"),
        ];

        for &(surf, read, mean, pos) in words {
            wd.insert(
                surf,
                WordInfo {
                    surface: surf,
                    reading: read,
                    meaning: mean,
                    part_of_speech: pos,
                },
            );
        }

        // 3. Common Grammar Patterns & Conversational Endings
        let grammar_rules = vec![
            GrammarNote {
                pattern: "〜ても / 〜でも",
                meaning: "Even if / Even though",
                explanation: "Connects a condition: 'even if [verb/adj] happens, [result]'. Formed with te-form + も.",
            },
            GrammarNote {
                pattern: "〜んだけど / 〜ですが",
                meaning: "It's just that... / but...",
                explanation: "Combines explanatory のだ/んだ with softening conjunction けど/が. Very common in natural dialogue.",
            },
            GrammarNote {
                pattern: "〜ちゃう / 〜じゃう",
                meaning: "End up doing / Completely done (casual)",
                explanation: "Casual contraction of 〜てしまう. Expresses unintended action, regret, or complete finality.",
            },
            GrammarNote {
                pattern: "〜とく / 〜ておく",
                meaning: "Do in advance / Leave as is",
                explanation: "Contraction of 〜ておく. Doing something now in preparation for later.",
            },
            GrammarNote {
                pattern: "〜受身 (れる / られる)",
                meaning: "Passive voice (is done by someone)",
                explanation: "Indicates the subject is acted upon by an external agent. In Japanese, often conveys suffering/inconvenience.",
            },
            GrammarNote {
                pattern: "〜使役 (せる / させる)",
                meaning: "Causative (make/let someone do)",
                explanation: "Indicates causing or permitting another person to perform an action.",
            },
            GrammarNote {
                pattern: "〜ば / 〜たら / 〜なら",
                meaning: "Conditional (If / When)",
                explanation: "Standard conditional forms describing hypothesis or subsequent events.",
            },
            GrammarNote {
                pattern: "〜わけがない / 〜はずがない",
                meaning: "There's no way that / Impossible",
                explanation: "Strong denial of possibility based on logic or evidence.",
            },
            GrammarNote {
                pattern: "〜かもしれない / 〜かも",
                meaning: "Might / Perhaps / Maybe",
                explanation: "Expresses conjecture or possibility (~50%). Very frequent in casual conversation.",
            },
        ];

        Self {
            kanji_map: kd,
            word_map: wd,
            grammar_rules,
        }
    }

    pub fn lookup_kanji(&self, ch: char) -> Option<&KanjiInfo> {
        self.kanji_map.get(&ch)
    }

    pub fn lookup_word(&self, word: &str) -> Option<&WordInfo> {
        self.word_map.get(word)
    }

    pub fn detect_grammar(&self, text: &str) -> Vec<GrammarNote> {
        let mut found = Vec::new();

        if text.contains("ても") || text.contains("でも") {
            found.push(self.grammar_rules[0].clone());
        }
        if text.contains("んだけど") || text.contains("んだが") || text.contains("んですが") {
            found.push(self.grammar_rules[1].clone());
        }
        if text.contains("ちゃう") || text.contains("ちゃった") || text.contains("じゃう") {
            found.push(self.grammar_rules[2].clone());
        }
        if text.contains("とく") || text.contains("といた") || text.contains("ておく") {
            found.push(self.grammar_rules[3].clone());
        }
        if text.contains("れる") || text.contains("られる") || text.contains("われた") || text.contains("された") {
            found.push(self.grammar_rules[4].clone());
        }
        if text.contains("せる") || text.contains("させる") {
            found.push(self.grammar_rules[5].clone());
        }
        if text.contains("たら") || text.contains("なら") || text.ends_with('ば') {
            found.push(self.grammar_rules[6].clone());
        }
        if text.contains("わけが") || text.contains("はずが") {
            found.push(self.grammar_rules[7].clone());
        }
        if text.contains("かも") || text.contains("かもしれない") {
            found.push(self.grammar_rules[8].clone());
        }

        found
    }
}

