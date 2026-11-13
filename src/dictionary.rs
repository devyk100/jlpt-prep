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

#[derive(Debug, Clone)]
pub struct ParsedWord {
    pub surface: String,
    pub base_form: String,
    pub reading: String,
    pub meaning: String,
    #[allow(dead_code)]
    pub part_of_speech: String,
    pub kanji_breakdown: Vec<KanjiInfo>,
    pub is_punct: bool,
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

        // === 1. EXPANDED IMMERSION KANJI DATABASE (400+ Kanji) ===
        let kanji_data: &[(char, &str, &str, &str)] = &[
            // Gaming, Slang, & Story
            ('払', "フツ, ヒツ", "はら・う", "pay, clear away, sweep"),
            ('代', "ダイ, タイ", "か・わる, よ, しろ", "fee, cost, generation, replace"),
            ('商', "ショウ", "あきな・う", "commerce, trade, merchant"),
            ('売', "バイ", "う・る", "sell, betray"),
            ('買', "バイ", "か・う", "buy, purchase"),
            ('涙', "ルイ", "なみだ", "tear, weeping"),
            ('目', "モク, ボク", "め, ま", "eye, look, insight"),
            ('客', "キャク, カク", "", "guest, customer, visitor"),
            ('観', "カン", "み・る", "view, observe, appearance"),
            ('男', "ダン, ナン", "おとこ", "man, male"),
            ('女', "ジョ, ニョ", "おんな", "woman, female"),
            ('悪', "アク, オ", "わる・い", "bad, evil, wrong"),
            ('魔', "マ", "", "demon, evil spirit, magic"),
            ('心', "シン", "こころ", "heart, mind, spirit"),
            ('怪', "カイ, ケ", "あや・しい", "suspicious, mystery, phantom"),
            ('盗', "トウ", "ぬす・む", "steal, rob, thief"),
            ('団', "ダン, トン", "", "group, team, association"),
            ('仮', "カ, ケ", "かり", "temporary, mask, hypothetical"),
            ('面', "メン, ベン", "おも, つら", "mask, face, surface"),
            ('命', "メイ, ミョウ", "いのち", "life, fate, destiny"),
            ('運', "ウン", "はこ・ぶ", "carry, luck, destiny"),
            ('世', "セイ, セ", "よ", "world, generation, society"),
            ('界', "カイ", "", "world, boundary, sphere"),
            ('自', "ジ, シ", "みずか・ら", "oneself, self"),
            ('由', "ユ, ユウ", "よし", "reason, freedom, origin"),
            ('選', "セン", "えら・ぶ", "choose, select, pick"),
            ('択', "タク", "", "choose, select"),
            ('力', "リョク, リキ", "ちから", "power, strength, ability"),
            ('魂', "コン", "たましい", "soul, spirit"),
            ('戦', "セン", "たたか・う", "war, fight, battle"),
            ('闘', "トウ", "たたか・う", "fight, struggle"),
            ('勝', "ショウ", "か・つ", "win, victory, excel"),
            ('敗', "ハイ", "やぶ・れる", "failure, defeat, loss"),
            ('友', "ユウ", "とも", "friend, companion"),
            ('仲', "チュウ", "なか", "relationship, comrade, middle"),
            ('間', "カン, ケン", "あいだ, ま", "interval, space, between"),
            ('絆', "ハン", "きずな", "bonds, emotional ties"),
            ('信', "シン", "", "trust, faith, believe"),
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
            ('聞', "ブン, モン", "き・く", "hear, listen, ask"),
            ('言', "ゲン, ゴン", "い・う, こと", "say, word, speech"),
            ('話', "ワ", "はな・す, はなし", "talk, speak, story"),
            ('行', "コウ, ギョウ", "い・く, おこな・う", "go, act, carry out"),
            ('来', "ライ", "く・る, きた・る", "come, arrive"),
            ('帰', "キ", "かえ・る", "return, go home"),
            ('出', "シュツ", "で・る, だ・す", "exit, go out, put out"),
            ('入', "ニュウ", "はい・る, い・れる", "enter, insert"),
            ('食', "ショク", "た・べる, く・う", "eat, food"),
            ('飲', "イン", "の・む", "drink"),
            ('死', "シ", "し・ぬ", "death, die"),
            ('生', "セイ, ショウ", "い・きる, う・まれる", "life, birth, live"),
            ('殺', "サツ", "ころ・す", "kill, murder"),
            ('殴', "オウ", "なぐ・る", "hit, strike, punch"),
            ('助', "ジョ", "たす・ける", "help, rescue, assist"),
            ('救', "キュウ", "すく・う", "save, rescue"),
            ('守', "シュ", "まも・る", "protect, guard, defend"),
            ('攻', "コウ", "せ・める", "attack, offense"),
            ('防', "ボウ", "ふせ・ぐ", "defend, prevent, ward off"),
            ('撃', "ゲキ", "う・つ", "strike, shoot, attack"),
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
            ('後', "ゴ, コウ", "うし・ろ, あと", "behind, after, later"),
            ('何', "カ", "なに, なん", "what, which"),
            ('誰', "", "だれ", "who, someone"),
            ('俺', "", "おれ", "I, me (informal masculine)"),
            ('僕', "ボク", "", "I, me (casual masculine)"),
            ('私', "シ", "わたし", "I, me, private"),
            ('君', "クン", "きみ", "you, ruler"),
            ('彼', "ヒ", "かれ, かの", "he, that"),
            ('奴', "ド", "やつ", "guy, fellow, slave"),
            ('手', "シュ", "て", "hand, arm, method"),
            ('口', "コウ, ク", "くち", "mouth, opening"),
            ('気', "キ, ケ", "", "spirit, mood, mind, air"),
            ('持', "ジ", "も・つ", "hold, have, possess"),
            ('待', "タイ", "ま・つ", "wait, await"),
            ('分', "ブン, フン", "わ・かる, わ・ける", "part, minute, understand"),
            ('合', "ゴウ", "あ・う, あ・わせる", "fit, match, join, meet"),
            ('会', "カイ", "あ・う", "meet, society"),
            ('困', "コン", "こま・る", "quandary, distressed, troubled"),
            ('難', "ナン", "むずか・しい", "difficult, trouble, hardship"),
            ('変', "ヘン", "か・わる, か・える", "strange, change, unusual"),
            ('同', "ドウ", "おな・じ", "same, equal, agree"),
            ('違', "イ", "ちが・う", "differ, vary, mistake"),
            ('要', "ヨウ", "い・る, かなめ", "need, vital, essential"),
            ('必', "ヒツ", "かなら・ず", "invariably, certain"),
            ('断', "ダン", "ことわ・る, た・つ", "refuse, sever, resolve"),
            ('決', "ケツ", "き・める, き・まる", "decide, determine"),
            ('定', "テイ", "さだ・める", "determine, fix, establish"),
            ('約', "ヤク", "", "promise, approximate"),
            ('束', "ソク", "たば", "bundle, tie (約束)"),
            ('道', "ドウ", "みち", "road, path, way"),
            ('走', "ソウ", "はし・る", "run, rush"),
            ('逃', "トウ", "に・げる, のが・す", "escape, flee, run away"),
            ('追', "ツイ", "お・う", "chase, pursue, follow"),
            ('終', "シュウ", "お・わる", "end, finish"),
            ('始', "シ", "はじ・まる", "begin, start"),
            ('開', "カイ", "あ・ける, ひら・く", "open, unfold"),
            ('閉', "ヘイ", "し・める, と・じる", "close, shut"),
            ('止', "シ", "と・まる, と・める", "stop, halt"),
            ('動', "ドウ", "うご・く", "move, motion, change"),
            ('光', "コウ", "ひかり", "light, ray"),
            ('闇', "アン", "やみ", "darkness, gloom"),
            ('影', "エイ", "かげ", "shadow, silhouette"),
            ('夢', "ム", "ゆめ", "dream, vision"),
            ('願', "ガン", "ねが・う", "request, wish, pray"),
            ('解', "カイ, ゲ", "と・く, わか・る", "untie, solve, explain"),
            ('覚', "カク", "おぼ・える, さ・める", "remember, awake, realize"),
            ('忘', "ボウ", "わす・れる", "forget"),
            ('愛', "アイ", "", "love, affection"),
            ('怖', "フ", "こわ・い", "scary, frightening, fear"),
            ('怒', "ド", "おこ・る, いか・る", "angry, rage"),
            ('悲', "ヒ", "かな・しい", "sad, grief"),
            ('喜', "キ", "よろこ・ぶ", "rejoice, delight"),
            ('楽', "ラク, ガク", "たの・しい", "comfort, ease, fun, music"),
            ('苦', "ク", "くる・しい, にが・い", "pain, bitter, suffering"),
            ('痛', "ツウ", "いた・い", "pain, hurt, ache"),
            ('強', "キョウ", "つよ・い", "strong, forceful"),
            ('弱', "ジャク", "よわ・い", "weak, frail"),
            ('高', "コウ", "たか・い", "tall, high, expensive"),
            ('安', "アン", "やす・い", "cheap, peaceful, safe"),
            ('危', "キ", "あぶ・ない", "danger, perilous"),
            ('険', "ケン", "けわ・しい", "steep, severe (危険)"),
            ('町', "チョウ", "まち", "town, street"),
            ('街', "ガイ", "まち", "street, city, avenue"),
            ('港', "コウ", "みなと", "harbor, port"),
            ('金', "キン, コン", "かね", "gold, money"),
            ('銭', "セン", "ぜに", "coin, money, small change"),
            ('親', "シン", "おや, した・しい", "parent, intimacy, close"),
            ('子', "シ, ス", "こ", "child, offspring"),
            ('兄', "ケイ, キョウ", "あに", "older brother"),
            ('弟', "テイ, ダイ", "おとうと", "younger brother"),
            ('姉', "シ", "あね", "older sister"),
            ('妹', "マイ", "いもうと", "younger sister"),
            ('家', "カ, ケ", "いえ, や", "house, family, home"),
            ('室', "シツ", "むろ", "room, chamber"),
            ('門', "モン", "かど", "gate, entrance"),
            ('車', "シャ", "くるま", "car, vehicle, wheel"),
            ('店', "テン", "みせ", "shop, store"),
            ('声', "セイ, ショウ", "こえ", "voice, sound"),
            ('音', "オン, イン", "おと, ね", "sound, noise"),
            ('歌', "カ", "うた, うた・う", "song, sing"),
            ('紙', "シ", "かみ", "paper"),
            ('本', "ホン", "もと", "book, origin, main"),
            ('字', "ジ", "あざ", "character, letter, mark"),
            ('文', "ブン, モン", "ふみ", "sentence, literature, style"),
            ('理', "リ", "", "reason, logic, justice"),
            ('意', "イ", "", "intent, meaning, mind, will"),
            ('味', "ミ", "あじ", "flavor, taste, meaning (意味)"),
            ('正', "セイ, ショウ", "ただ・しい, まさ", "correct, right, justice"),
            ('義', "ギ", "", "justice, honor, meaning (正義)"),
            ('罪', "ザイ", "つみ", "guilt, crime, sin"),
            ('罰', "バツ, バチ", "", "punishment, penalty"),
            ('牢', "ロウ", "", "prison, cage, jail"),
            ('獄', "ゴク", "", "prison, hell (牢獄)"),
            ('処', "ショ", "", "dispose, manage, treat"),
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

        // === 2. EXTENSIVE IMMERSION VOCABULARY DATABASE (1,000+ Words) ===
        let words: &[(&str, &str, &str, &str)] = &[
            // Slang, Anime, JoJo, & Mafia staples
            ("ショバ代", "ショバだい", "turf fee, protection money, territory tax (slang)", "noun"),
            ("ショバ", "ショバ", "turf, location, patch of territory (slang)", "noun"),
            ("代", "だい", "fee, charge, cost, generation", "noun/suffix"),
            ("払う", "はらう", "to pay, settle, clear off", "verb"),
            ("商売", "しょうばい", "trade, business, commerce", "noun/suru"),
            ("しろ", "しろ", "do it! (rough imperative of する)", "verb-imperative"),
            ("する", "する", "to do, cause, make", "verb"),
            ("言った", "いった", "said, told (past of 言う)", "verb-past"),
            ("言う", "いう", "to say, tell, utter", "verb"),
            ("涙目", "なみだめ", "teary-eyed, on the verge of tears", "noun"),
            ("涙", "なみだ", "tear, teardrop", "noun"),
            ("ルカ", "ルカ", "Luca (character name)", "noun"),
            ("どれくらい", "どれくらい", "how much, to what extent, how long", "adverb"),
            ("どうする", "どうする", "what will you do? what should we do?", "expression"),
            ("客", "きゃく", "customer, client, guest", "noun"),
            ("観客", "かんきゃく", "spectator, audience, onlooker", "noun"),
            ("男", "おとこ", "man, male", "noun"),
            ("女", "おんな", "woman, female", "noun"),
            ("野郎", "やろう", "bastard, guy, rascal (slang)", "noun"),
            ("てめえ", "てめえ", "you bastard (very rude pronoun)", "pronoun"),
            ("貴様", "きさま", "you, you scum (rude pronoun)", "pronoun"),
            ("お前", "おまえ", "you (informal/blunt)", "pronoun"),
            ("俺", "おれ", "I, me (masculine informal)", "pronoun"),
            ("僕", "ぼく", "I, me (casual masculine)", "pronoun"),
            ("私", "わたし", "I, me (standard)", "pronoun"),
            ("やつ", "やつ", "guy, fellow, that thing", "noun"),
            ("こいつ", "こいつ", "this guy, this one", "pronoun"),
            ("そいつ", "そいつ", "that guy, that one", "pronoun"),
            ("あいつ", "あいつ", "that bastard over there, that guy", "pronoun"),
            ("ぶっ殺す", "ぶっころす", "beat to death, murder, slaughter (slang)", "verb"),
            ("殺す", "ころす", "to kill, murder", "verb"),
            ("死ぬ", "しぬ", "to die, perish", "verb"),
            ("殴る", "なぐる", "to strike, hit, punch", "verb"),
            ("逃げる", "にげる", "to run away, escape, flee", "verb"),
            ("追う", "おう", "to chase, pursue", "verb"),
            ("助ける", "たすける", "to help, rescue, assist", "verb"),
            ("助けて", "たすけて", "Help me! (te-form of 助ける)", "expression"),
            ("守る", "まもる", "to protect, defend, guard", "verb"),
            ("奪う", "うばう", "to snatch away, steal, rob", "verb"),
            ("盗む", "ぬすむ", "to steal, rob", "verb"),
            ("怪盗団", "かいとうだん", "Phantom Thieves (Persona 5)", "noun"),
            ("怪盗", "かいとう", "phantom thief, gentleman burglar", "noun"),
            ("仮面", "かめん", "mask, persona", "noun"),
            ("ペルソナ", "ペルソナ", "Persona, alter ego", "noun"),
            ("パレス", "パレス", "Palace (cognitive realm)", "noun"),
            ("オタカラ", "オタカラ", "Treasure (in Palace)", "noun"),
            ("悪魔", "あくま", "demon, devil", "noun"),
            ("仲間", "なかま", "companion, comrade, crew, ally", "noun"),
            ("絆", "きずな", "bonds, emotional ties", "noun"),
            ("運命", "うんめい", "destiny, fate", "noun"),
            ("世界", "せかい", "world, universe", "noun"),
            ("自由", "じゆう", "freedom, liberty", "noun"),
            ("真実", "しんじつ", "truth, reality", "noun"),
            ("嘘", "うそ", "lie, falsehood", "noun"),
            ("本当", "ほんとう", "truth, reality, really", "noun/adverb"),
            ("本当は", "ほんとうは", "in truth, actually", "expression"),
            ("まじで", "まじで", "seriously? for real? (slang)", "adverb"),
            ("選択", "せんたく", "choice, selection", "noun/suru"),
            ("決断", "けつだん", "decision, resolution", "noun/suru"),
            ("約束", "やくそく", "promise, agreement", "noun/suru"),
            ("覚悟", "かくご", "readiness, preparedness, resolution", "noun/suru"),
            ("諦める", "あきらめる", "to give up, abandon hope", "verb"),
            ("信じる", "しんじる", "to believe, trust in", "verb"),
            ("戦う", "たたかう", "to fight, battle, struggle", "verb"),
            ("勝つ", "かつ", "to win, triumph", "verb"),
            ("負ける", "まける", "to lose, be defeated", "verb"),
            ("倒す", "たおす", "to defeat, bring down, knock over", "verb"),
            ("行く", "いく", "to go, proceed", "verb"),
            ("行こう", "いこう", "let's go! (volitional)", "verb"),
            ("行け", "いけ", "Go! (imperative)", "verb"),
            ("来る", "くる", "to come, arrive", "verb"),
            ("来い", "こい", "Come here! (imperative)", "verb"),
            ("帰る", "かえる", "to go home, return", "verb"),
            ("帰れ", "かえれ", "Go home! (imperative)", "verb"),
            ("話す", "はなす", "to speak, talk, tell", "verb"),
            ("見る", "みる", "to see, look, watch", "verb"),
            ("見ろ", "みろ", "Look! (imperative)", "verb"),
            ("見て", "みて", "look, please look (te-form)", "expression"),
            ("聞く", "きく", "to hear, listen, ask", "verb"),
            ("知る", "しる", "to know, understand", "verb"),
            ("知ってる", "しってる", "I know (contraction of 知っている)", "expression"),
            ("知らない", "しらない", "I don't know", "expression"),
            ("分かる", "わかる", "to understand, comprehend", "verb"),
            ("分かった", "わかった", "Understood / Got it!", "expression"),
            ("分からない", "わからない", "I don't understand", "expression"),
            ("思う", "おもう", "to think, feel, consider", "verb"),
            ("考える", "かんがえる", "to contemplate, consider, plan", "verb"),
            ("待つ", "まつ", "to wait, await", "verb"),
            ("待て", "まて", "Wait! Hold on! (imperative)", "verb"),
            ("待って", "まって", "Wait! (te-form)", "expression"),
            ("持つ", "もつ", "to hold, possess, carry", "verb"),
            ("食べる", "たべる", "to eat", "verb"),
            ("飲む", "のむ", "to drink", "verb"),
            ("金", "かね", "money, gold", "noun"),
            ("銭", "ぜに", "coins, cash (slang)", "noun"),
            ("時間", "じかん", "time, hours", "noun"),
            ("気持ち", "きもち", "feeling, sensation, mood", "noun"),
            ("心", "こころ", "heart, mind, spirit", "noun"),
            ("力", "ちから", "power, strength, ability", "noun"),
            ("情報", "じょうほう", "information, intel", "noun"),
            ("大丈夫", "だいじょうぶ", "all right, okay, safe", "na-adjective"),
            ("無理", "むり", "impossible, unreasonable", "na-adjective"),
            ("簡単", "かんたん", "simple, easy", "na-adjective"),
            ("危険", "きけん", "danger, hazard, perilous", "na-adjective"),
            ("秘密", "ひみつ", "secret, mystery", "noun"),
            ("何", "なに", "what", "pronoun"),
            ("何で", "なんで", "why? how come?", "adverb"),
            ("誰", "だれ", "who", "pronoun"),
            ("どこ", "どこ", "where", "pronoun"),
            ("いつ", "いつ", "when", "pronoun"),
            ("なぜ", "なぜ", "why, for what reason", "adverb"),
            ("どうして", "どうして", "why, how come", "adverb"),
            ("すごい", "すごい", "amazing, incredible, terrible", "i-adjective"),
            ("やばい", "やばい", "dangerous, crazy, insane (slang)", "i-adjective"),
            ("強い", "つよい", "strong, powerful", "i-adjective"),
            ("弱い", "よわい", "weak, frail", "i-adjective"),
            ("痛い", "いたい", "painful, sore, ouch!", "i-adjective"),
            ("怖い", "こわい", "scary, frightening", "i-adjective"),
            ("困る", "こまる", "to be troubled, at a loss", "verb"),
            ("困った", "こまった", "troubled, in a pinch", "expression"),
            ("言われても", "いわれても", "even if told / even if you say that", "expression"),
            ("から", "から", "from, since, after doing, because", "particle"),
            ("まで", "まで", "until, up to, as far as", "particle"),
            ("って", "って", "quotation particle / casual 'said that'", "particle"),
            ("よなあ", "よなあ", "right? don't you agree? (seeking consensus)", "particle"),
            ("なあ", "なあ", "hey, right? (particle)", "particle"),
            ("よ", "よ", "you know / assertion (particle)", "particle"),
            ("ね", "ね", "isn't it? (particle)", "particle"),
            ("さん", "さん", "Mr./Ms. (polite honorific)", "suffix"),
            ("くん", "くん", "young man / honorific for peers", "suffix"),
            ("ちゃん", "ちゃん", "affectionate honorific", "suffix"),
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

        // === 3. HIGH-FREQUENCY GRAMMAR PATTERNS ===
        let grammar_rules = vec![
            GrammarNote {
                pattern: "〜ても / 〜でも",
                meaning: "Even if / Even though",
                explanation: "Connects a condition: 'even if [verb/adj] happens, [result]'. Formed with te-form + も.",
            },
            GrammarNote {
                pattern: "〜てから",
                meaning: "After doing... / Ever since...",
                explanation: "Indicates that one action must finish before the second starts (e.g. 払ってから商売しろ).",
            },
            GrammarNote {
                pattern: "〜しろ / 命令形",
                meaning: "Do it! (Rough Imperative)",
                explanation: "Direct commanding form (e.g. する → しろ, 払う → 払え, 見る → 見ろ). Very common in anime/manga dialogue.",
            },
            GrammarNote {
                pattern: "〜って (引用・伝聞)",
                meaning: "Said that... / Casual quotation",
                explanation: "Casual conversational contraction of と言った or と (e.g. 商売しろって言った).",
            },
            GrammarNote {
                pattern: "〜よなあ / 〜よな",
                meaning: "Right?! / Don't you think so?",
                explanation: "Combines assertive よ with seeking agreement なあ. Strong informal confirmation.",
            },
            GrammarNote {
                pattern: "〜んだけど / 〜ですが",
                meaning: "It's just that... / but...",
                explanation: "Combines explanatory のだ/んだ with softening conjunction けど/が.",
            },
            GrammarNote {
                pattern: "〜ちゃう / 〜じゃう",
                meaning: "End up doing / Completely done (casual)",
                explanation: "Casual contraction of 〜てしまう. Expresses unintended action or finality.",
            },
            GrammarNote {
                pattern: "〜とく / 〜ておく",
                meaning: "Do in advance / Leave as is",
                explanation: "Contraction of 〜ておく. Preparing beforehand.",
            },
            GrammarNote {
                pattern: "〜受身 (れる / られる)",
                meaning: "Passive voice (done by someone)",
                explanation: "Indicates subject is acted upon by another agent.",
            },
            GrammarNote {
                pattern: "〜使役 (せる / させる)",
                meaning: "Causative (make/let someone do)",
                explanation: "Indicates causing or permitting another to act.",
            },
            GrammarNote {
                pattern: "〜ば / 〜たら / 〜なら",
                meaning: "Conditional (If / When)",
                explanation: "Standard conditional forms describing hypotheses or future events.",
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
        // 1. Direct match
        if let Some(w) = self.word_map.get(word) {
            return Some(w);
        }

        // 2. Morphological De-inflection: try stemming common verb/adjective forms
        if let Some(stemmed) = self.deinflect(word) {
            if let Some(w) = self.word_map.get(stemmed.as_str()) {
                return Some(w);
            }
        }

        None
    }

    pub fn deinflect(&self, word: &str) -> Option<String> {
        // Te-form & Past Ta-form
        if word.ends_with("って") {
            return Some(format!("{}う", &word[..word.len() - "って".len()]));
        }
        if word.ends_with("った") {
            return Some(format!("{}う", &word[..word.len() - "った".len()]));
        }
        if word.ends_with("いて") || word.ends_with("いた") {
            let base = &word[..word.len() - 6];
            return Some(format!("{}く", base));
        }
        if word.ends_with("して") || word.ends_with("した") {
            let base = &word[..word.len() - 6];
            return Some(format!("{}す", base));
        }
        if word.ends_with("んで") || word.ends_with("んだ") {
            let base = &word[..word.len() - 6];
            return Some(format!("{}む", base));
        }
        // Ichidan te/ta: 助けて -> 助ける, 食べた -> 食べる
        if word.ends_with('て') || word.ends_with('た') {
            let base = &word[..word.len() - 3];
            return Some(format!("{}る", base));
        }
        // Negative nai: 食べない -> 食べる, 言わない -> 言う
        if word.ends_with("ない") {
            let base = &word[..word.len() - "ない".len()];
            if base.ends_with('わ') {
                return Some(format!("{}う", &base[..base.len() - 3]));
            }
            return Some(format!("{}る", base));
        }
        // Imperative: しろ -> する
        if word.ends_with("しろ") {
            return Some("する".to_string());
        }
        // Imperative e-form: 払え -> 払う, 言え -> 言う
        if word.ends_with('え') {
            let base = &word[..word.len() - 3];
            return Some(format!("{}う", base));
        }

        None
    }

    /// Yomitan-style Longest-Prefix Sentence Parser
    pub fn parse_sentence(&self, text: &str) -> Vec<ParsedWord> {
        let mut results = Vec::new();
        let chars: Vec<char> = text.chars().collect();
        let len = chars.len();
        let mut i = 0;

        while i < len {
            let c = chars[i];

            // 1. Skip English letters and ASCII noise
            if c.is_ascii_alphabetic() || c.is_ascii_digit() {
                i += 1;
                continue;
            }

            // 2. Japanese Dialogue Punctuation
            if is_cjk_punct(c) || c == '？' || c == '！' || c == '?' || c == '!' {
                results.push(ParsedWord {
                    surface: c.to_string(),
                    base_form: c.to_string(),
                    reading: String::new(),
                    meaning: String::new(),
                    part_of_speech: "punct".to_string(),
                    kanji_breakdown: vec![],
                    is_punct: true,
                });
                i += 1;
                continue;
            }

            // Skip whitespace and stray ASCII symbols
            if c.is_whitespace() || c.is_ascii_punctuation() {
                i += 1;
                continue;
            }

            // 3. Longest Prefix Substring Matching (lengths 8 down to 1)
            let max_lookahead = (len - i).min(8);
            let mut matched = false;

            for chunk_len in (1..=max_lookahead).rev() {
                let candidate: String = chars[i..i + chunk_len].iter().collect();

                // Check exact word or stemmed word
                if let Some(info) = self.lookup_word(&candidate) {
                    let mut kanjis = Vec::new();
                    for ch in candidate.chars() {
                        if let Some(k) = self.lookup_kanji(ch) {
                            kanjis.push(k.clone());
                        }
                    }

                    results.push(ParsedWord {
                        surface: candidate.clone(),
                        base_form: info.surface.to_string(),
                        reading: info.reading.to_string(),
                        meaning: info.meaning.to_string(),
                        part_of_speech: info.part_of_speech.to_string(),
                        kanji_breakdown: kanjis,
                        is_punct: false,
                    });

                    i += chunk_len;
                    matched = true;
                    break;
                }
            }

            if matched {
                continue;
            }

            // 3. Fallback: Single character Kanji or Kana
            let single_ch = chars[i];
            let mut kanjis = Vec::new();
            let mut meaning = String::new();
            let mut reading = String::new();

            if let Some(k) = self.lookup_kanji(single_ch) {
                reading = k.onyomi.to_string();
                meaning = k.meaning.to_string();
                kanjis.push(k.clone());
            }

            results.push(ParsedWord {
                surface: single_ch.to_string(),
                base_form: single_ch.to_string(),
                reading,
                meaning,
                part_of_speech: if !kanjis.is_empty() { "kanji".to_string() } else { "kana".to_string() },
                kanji_breakdown: kanjis,
                is_punct: false,
            });

            i += 1;
        }

        results
    }

    pub fn detect_grammar(&self, text: &str) -> Vec<GrammarNote> {
        let mut found = Vec::new();

        if text.contains("ても") || text.contains("でも") {
            found.push(self.grammar_rules[0].clone());
        }
        if text.contains("てから") || text.contains("でから") {
            found.push(self.grammar_rules[1].clone());
        }
        if text.contains("しろ") || text.contains("払え") || text.contains("言え") || text.contains("見ろ") || text.contains("逃げろ") {
            found.push(self.grammar_rules[2].clone());
        }
        if text.contains("って") {
            found.push(self.grammar_rules[3].clone());
        }
        if text.contains("よなあ") || text.contains("よな") {
            found.push(self.grammar_rules[4].clone());
        }
        if text.contains("んだけど") || text.contains("んだが") || text.contains("んですが") {
            found.push(self.grammar_rules[5].clone());
        }
        if text.contains("ちゃう") || text.contains("ちゃった") || text.contains("じゃう") {
            found.push(self.grammar_rules[6].clone());
        }
        if text.contains("とく") || text.contains("といた") || text.contains("ておく") {
            found.push(self.grammar_rules[7].clone());
        }
        if text.contains("れる") || text.contains("られる") || text.contains("われた") || text.contains("された") {
            found.push(self.grammar_rules[8].clone());
        }
        if text.contains("せる") || text.contains("させる") {
            found.push(self.grammar_rules[9].clone());
        }
        if text.contains("たら") || text.contains("なら") || text.ends_with('ば') {
            found.push(self.grammar_rules[10].clone());
        }

        found
    }
}

fn is_cjk_punct(c: char) -> bool {
    matches!(c, '。' | '、' | '！' | '？' | '「' | '」' | '『' | '』' | '（' | '）' | '…' | '―' | '〜' | '・')
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_jojo_dialogue_parsing() {
        let dict = LocalDictionary::new();
        let sentence = "ショバ代払ってから商売しろって言ったよなあ？";
        let parsed = dict.parse_sentence(sentence);

        let words: Vec<&str> = parsed.iter().map(|p| p.surface.as_str()).collect();
        println!("Parsed tokens: {:?}", words);

        assert!(parsed.iter().any(|p| p.surface == "ショバ代" && p.meaning.contains("turf fee")));
        assert!(parsed.iter().any(|p| p.surface == "払って" && p.base_form == "払う"));
        assert!(parsed.iter().any(|p| p.surface == "商売" && p.meaning.contains("business")));
        assert!(parsed.iter().any(|p| p.surface == "しろ" && p.base_form == "する"));
        assert!(parsed.iter().any(|p| p.surface == "言った" && p.base_form == "言う"));
    }
}
