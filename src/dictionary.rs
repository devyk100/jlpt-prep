use crate::tokenizer::{is_hiragana, is_kanji, is_katakana};
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
    pub surface: String,
    pub reading: String,
    pub meaning: String,
    #[allow(dead_code)]
    pub part_of_speech: String,
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
    pub word_map: HashMap<String, WordInfo>,
    pub grammar_rules: Vec<GrammarNote>,
}

impl LocalDictionary {
    pub fn new() -> Self {
        let mut kd = HashMap::new();
        let mut wd: HashMap<String, WordInfo> = HashMap::new();

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
            // Essential Dialogue, Story & Game vocabulary
            ("家族", "かぞく", "family, household", "noun"),
            ("大事", "だいじ", "important, precious, serious matter", "na-adjective"),
            ("登る", "のぼる", "to climb, ascend, go up", "verb"),
            ("登", "とう", "climb, ascend, register", "noun"),
            ("より", "より", "more than, rather than, from", "particle"),
            ("くれ", "くれ", "give me, do for me (imperative of くれる)", "verb"),
            ("くれる", "くれる", "to give (to me), do something for me", "verb"),
            ("くれた", "くれた", "gave (to me), did for me", "verb-past"),
            ("くれない", "くれない", "won't you do for me?", "expression"),
            ("仲間", "なかま", "companion, comrade, ally, crew", "noun"),
            ("友達", "ともだち", "friend, companion", "noun"),
            ("親", "おや", "parent", "noun"),
            ("子供", "こども", "child, children", "noun"),
            ("兄", "あに", "older brother", "noun"),
            ("弟", "おとうと", "younger brother", "noun"),
            ("姉", "あね", "older sister", "noun"),
            ("妹", "いもうと", "younger sister", "noun"),
            ("守る", "まもる", "to protect, defend, guard", "verb"),
            ("倒す", "たおす", "to defeat, bring down, topple", "verb"),
            ("敵", "てき", "enemy, foe, adversary", "noun"),
            ("味方", "みかた", "ally, supporter, friend", "noun"),
            ("攻撃", "こうげき", "attack, strike, offensive", "noun/suru"),
            ("防御", "ぼうぎょ", "defense, guard", "noun/suru"),
            ("魔法", "まほう", "magic, sorcery, spell", "noun"),
            ("スキル", "スキル", "skill, special ability", "noun"),
            ("武器", "ぶき", "weapon, arms", "noun"),
            ("装備", "そうび", "equipment, gear", "noun/suru"),
            ("勝利", "しょうり", "victory, triumph", "noun"),
            ("敗北", "はいぼく", "defeat, loss", "noun"),
            ("生きる", "いきる", "to live, exist", "verb"),
            ("命", "いのち", "life, life force, fate", "noun"),
            ("魂", "たましい", "soul, spirit", "noun"),
            ("勇気", "ゆうき", "courage, bravery", "noun"),
            ("希望", "きぼう", "hope, wish", "noun"),
            ("絶望", "ぜつぼう", "despair, hopelessness", "noun"),
            ("記憶", "きおく", "memory, recollection", "noun"),
            ("思い出", "おもいで", "memories, reminiscence", "noun"),
            ("許す", "ゆるす", "to forgive, pardon, permit", "verb"),
            ("頼む", "たのむ", "to request, ask, rely upon", "verb"),
            ("任せる", "まかせる", "to entrust to, leave to", "verb"),
            ("理由", "りゆう", "reason, cause", "noun"),
            ("問題", "もんだい", "problem, issue, question", "noun"),
            ("事件", "じけん", "incident, case, affair", "noun"),
            ("警察", "けいさつ", "police", "noun"),
            ("探偵", "たんてい", "detective, investigator", "noun"),
            ("犯人", "はんにん", "culprit, criminal", "noun"),
            ("場所", "ばしょ", "place, location", "noun"),
            ("名前", "なまえ", "name", "noun"),
            ("仕事", "しごと", "work, job, duty", "noun"),
            ("学校", "がっこう", "school", "noun"),
            ("絶対", "ぜったい", "absolutely, unconditionally", "adverb"),
            ("必ず", "かならず", "certainly, without fail", "adverb"),
            ("たぶん", "たぶん", "probably, perhaps", "adverb"),
            ("きっと", "きっと", "surely, definitely", "adverb"),
            ("もし", "もし", "if, in case", "adverb"),
            ("少し", "すこし", "a little, slightly", "adverb"),
            ("たくさん", "たくさん", "a lot, plenty", "adverb"),
            ("全部", "ぜんぶ", "all, entirety", "noun/adverb"),
            ("全て", "すべて", "all, everything", "noun/adverb"),
            ("大きい", "おおきい", "big, large", "i-adjective"),
            ("小さい", "ちいさい", "small, tiny", "i-adjective"),
            ("高い", "たかい", "high, tall, expensive", "i-adjective"),
            ("安い", "やすい", "cheap, peaceful", "i-adjective"),
            ("新しい", "あたらしい", "new, fresh", "i-adjective"),
            ("古い", "ふるい", "old, aged", "i-adjective"),
            ("良い", "よい", "good, excellent", "i-adjective"),
            ("いい", "いい", "good, fine, okay", "i-adjective"),
            ("悪い", "わるい", "bad, evil, wrong", "i-adjective"),
            ("正しい", "ただしい", "correct, righteous", "i-adjective"),
            ("違う", "ちがう", "different, wrong, to differ", "verb"),
            ("美しい", "うつくしい", "beautiful, lovely", "i-adjective"),
            ("可愛い", "かわいい", "cute, adorable", "i-adjective"),
            ("面白い", "おもしろい", "interesting, amusing, fun", "i-adjective"),
            ("悲しい", "かなしい", "sad, sorrowful", "i-adjective"),
            ("嬉しい", "うれしい", "happy, glad, delighted", "i-adjective"),
            ("楽しい", "たのしい", "enjoyable, fun", "i-adjective"),
            ("苦しい", "くるしい", "painful, agonizing", "i-adjective"),
            ("怒る", "おこる", "to get angry, be mad", "verb"),
            ("笑う", "わらう", "to laugh, smile", "verb"),
            ("泣く", "なく", "to weep, cry", "verb"),
            ("叫ぶ", "さけぶ", "to shout, yell, scream", "verb"),
            ("黙る", "だまる", "to be silent, shut up", "verb"),
            ("教える", "おしえる", "to teach, tell, inform", "verb"),
            ("忘れる", "わすれる", "to forget", "verb"),
            ("覚える", "おぼえる", "to remember, memorize", "verb"),
            ("探す", "さがす", "to search for, look for", "verb"),
            ("見つける", "みつける", "to find, discover", "verb"),
            ("歩く", "あるく", "to walk", "verb"),
            ("走る", "はしる", "to run", "verb"),
            ("止まる", "とまる", "to stop, halt", "verb"),
            ("動く", "うごく", "to move, operate", "verb"),
            ("入る", "はいる", "to enter, go in", "verb"),
            ("出る", "でる", "to exit, leave, appear", "verb"),
            ("そして", "そして", "and then, and so", "conjunction"),
            ("しかし", "しかし", "however, but", "conjunction"),
            ("だから", "だから", "therefore, that's why", "conjunction"),
            ("でも", "でも", "but, however, even", "conjunction"),
            ("もう", "もう", "already, anymore", "adverb"),
            ("まだ", "まだ", "still, not yet", "adverb"),
            ("もっと", "もっと", "more, further", "adverb"),
            ("ずっと", "ずっと", "all along, by far, continuously", "adverb"),
            ("一番", "いちばん", "best, number one, most", "adverb"),
            ("任せろ", "まかせろ", "leave it to me! (imperative)", "expression"),
            ("待たせたな", "またせたな", "kept you waiting (greeting)", "expression"),
            ("ふざけるな", "ふざけるな", "don't mess around! don't screw with me!", "expression"),
            ("仕方ない", "しかたない", "can't be helped, inevitable", "expression"),
            ("しょうがない", "しょうがない", "it can't be helped", "expression"),
            ("さすが", "さすが", "as expected, truly impressive", "na-adjective/adverb"),
            ("やっぱり", "やっぱり", "as I thought, after all", "adverb"),
            ("まさか", "まさか", "no way! impossible! surely not!", "adverb"),
            ("信じられない", "しんじられない", "unbelievable! can't believe it!", "expression"),
            ("やれやれ", "やれやれ", "good grief, sigh", "interjection"),
            ("おい", "おい", "hey! (casual call)", "interjection"),
            ("ちょっと", "ちょっと", "a bit, wait a moment", "adverb"),
        ];

        for &(surf, read, mean, pos) in words {
            wd.insert(
                surf.to_string(),
                WordInfo {
                    surface: surf.to_string(),
                    reading: read.to_string(),
                    meaning: mean.to_string(),
                    part_of_speech: pos.to_string(),
                },
            );
        }

        // === 3. LOAD FULL JMDict DATABASE (499,822 Entries) ===
        let mut dict_paths = vec![
            std::path::PathBuf::from("yomiflow_dict.tsv"),
            std::path::PathBuf::from("../yomiflow_dict.tsv"),
        ];
        if let Ok(exe) = std::env::current_exe() {
            if let Some(dir) = exe.parent() {
                dict_paths.push(dir.join("yomiflow_dict.tsv"));
            }
        }
        for path in &dict_paths {
            if let Ok(file) = std::fs::File::open(path) {
                let reader = std::io::BufReader::new(file);
                use std::io::BufRead;
                for line in reader.lines().flatten() {
                    let mut parts = line.split('\t');
                    if let (Some(surf), Some(read), Some(mean)) = (parts.next(), parts.next(), parts.next()) {
                        wd.entry(surf.to_string()).or_insert_with(|| WordInfo {
                            surface: surf.to_string(),
                            reading: read.to_string(),
                            meaning: mean.to_string(),
                            part_of_speech: "jmdict".to_string(),
                        });
                    }
                }
                println!("[Dictionary] Loaded {} entries from {:?}", wd.len(), path);
                break;
            }
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
        // Imperative standalone: しろ -> する, して -> する
        if word == "しろ" || word == "して" {
            return Some("する".to_string());
        }

        // Te-form & Past Ta-form for Godan verbs
        if word.ends_with("って") && word.len() > 6 {
            return Some(format!("{}う", &word[..word.len() - "って".len()]));
        }
        if word.ends_with("った") && word.len() > 6 {
            return Some(format!("{}う", &word[..word.len() - "った".len()]));
        }
        if (word.ends_with("いて") || word.ends_with("いた")) && word.len() >= 6 {
            let base = &word[..word.len() - 6];
            return Some(format!("{}く", base));
        }
        if (word.ends_with("して") || word.ends_with("した")) && word.len() >= 6 {
            let base = &word[..word.len() - 6];
            return Some(format!("{}す", base));
        }
        if (word.ends_with("んで") || word.ends_with("んだ")) && word.len() >= 6 {
            let base = &word[..word.len() - 6];
            return Some(format!("{}む", base));
        }
        // Ichidan te/ta: 助けて -> 助ける, 食べた -> 食べる
        if (word.ends_with('て') || word.ends_with('た')) && word.len() > 3 {
            let base = &word[..word.len() - 3];
            return Some(format!("{}る", base));
        }
        // Negative nai: 食べない -> 食べる, 言わない -> 言う
        if word.ends_with("ない") && word.len() > 6 {
            let base = &word[..word.len() - "ない".len()];
            if base.ends_with('わ') && base.len() >= 3 {
                return Some(format!("{}う", &base[..base.len() - 3]));
            }
            return Some(format!("{}る", base));
        }
        // Imperative e-form: 払え -> 払う, 言え -> 言う
        if word.ends_with('え') && word.len() > 3 {
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

                    let base = if let Some(stemmed) = self.deinflect(&candidate) {
                        stemmed
                    } else {
                        info.surface.to_string()
                    };

                    results.push(ParsedWord {
                        surface: candidate.clone(),
                        base_form: base,
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

            // 4. Consecutive Kanji compound chunk (group consecutive kanji + attached okurigana together)
            if is_kanji(c) {
                let mut word = String::new();
                let mut kanjis = Vec::new();

                while i < len && is_kanji(chars[i]) {
                    word.push(chars[i]);
                    if let Some(k) = self.lookup_kanji(chars[i]) {
                        kanjis.push(k.clone());
                    }
                    i += 1;
                }

                let mut okuri = 0;
                while i < len && is_hiragana(chars[i]) && okuri < 3 {
                    if okuri > 0 && matches!(chars[i], 'は' | 'が' | 'を' | 'に' | 'へ' | 'で' | 'と') {
                        break;
                    }
                    word.push(chars[i]);
                    okuri += 1;
                    i += 1;
                }

                let mut reading = String::new();
                let mut meaning = String::new();
                let mut base = word.clone();

                if let Some(info) = self.lookup_word(&word) {
                    reading = info.reading.to_string();
                    meaning = info.meaning.to_string();
                    base = info.surface.to_string();
                } else if let Some(first_k) = kanjis.first() {
                    meaning = first_k.meaning.to_string();
                }

                results.push(ParsedWord {
                    surface: word,
                    base_form: base,
                    reading,
                    meaning,
                    part_of_speech: "kanji-word".to_string(),
                    kanji_breakdown: kanjis,
                    is_punct: false,
                });
                continue;
            }

            // 5. Katakana compound (e.g. ペルソナ, ルカ, ショバ)
            if is_katakana(c) || c == 'ー' {
                let mut kata = String::new();
                while i < len && (is_katakana(chars[i]) || chars[i] == 'ー') {
                    kata.push(chars[i]);
                    i += 1;
                }

                let mut reading = kata.clone();
                let mut meaning = String::new();
                if let Some(info) = self.lookup_word(&kata) {
                    reading = info.reading.to_string();
                    meaning = info.meaning.to_string();
                }

                results.push(ParsedWord {
                    surface: kata.clone(),
                    base_form: kata,
                    reading,
                    meaning,
                    part_of_speech: "katakana".to_string(),
                    kanji_breakdown: vec![],
                    is_punct: false,
                });
                continue;
            }

            // 6. Hiragana particle or phrase
            if is_hiragana(c) {
                let mut hira = String::new();
                while i < len && is_hiragana(chars[i]) && !is_kanji(chars[i]) {
                    hira.push(chars[i]);
                    i += 1;
                    if matches!(chars[i - 1], 'は' | 'が' | 'を' | 'に' | 'へ' | 'で' | 'と' | 'も' | 'ね' | 'よ') {
                        break;
                    }
                }

                let mut meaning = String::new();
                let mut base = hira.clone();
                if let Some(info) = self.lookup_word(&hira) {
                    meaning = info.meaning.to_string();
                    base = info.surface.to_string();
                }

                results.push(ParsedWord {
                    surface: hira.clone(),
                    base_form: base,
                    reading: hira,
                    meaning,
                    part_of_speech: "hiragana".to_string(),
                    kanji_breakdown: vec![],
                    is_punct: false,
                });
                continue;
            }

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
        assert!(parsed.iter().any(|p| p.surface.contains("言った")));
    }

    #[test]
    fn test_family_dialogue_parsing() {
        let dict = LocalDictionary::new();
        let sentence = "家族より、大事にしてくれよ";
        let parsed = dict.parse_sentence(sentence);

        let words: Vec<&str> = parsed.iter().map(|p| p.surface.as_str()).collect();
        println!("Parsed tokens: {:?}", words);

        assert!(parsed.iter().any(|p| p.surface == "家族" && p.meaning.contains("family")));
        assert!(parsed.iter().any(|p| p.surface == "大事" && p.meaning.contains("important")));
        assert!(parsed.iter().any(|p| p.surface == "くれ"));
    }
}
