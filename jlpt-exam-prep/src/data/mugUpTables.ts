import { MugUpTable } from '../types';

export const MASTER_MUG_UP_TABLES: Record<string, MugUpTable> = {
  teFormMatrix: {
    title: 'The Te-Form (て形) Conjugation Matrix',
    subtitle: 'The foundational gateway for ~ている, ~てから, ~てもいい, ~てはいけない, and ~てしまう.',
    columns: ['Verb Group / Ending', 'Dictionary (辞書形)', 'Te-Form (て形)', 'Past (た形)', 'Mnemonic / Mug-Up Rule'],
    rows: [
      {
        label: 'Group 1: う・つ・る',
        cells: ['買う, 待つ, 取る', '買って, 待って, 取って', '買った, 待った, 取った', 'う・つ・る → って / った (促音便: 小さい「っ」+ て)'],
        note: 'Classic rhythm: "u, tsu, ru" becomes "tte"'
      },
      {
        label: 'Group 1: む・ぶ・ぬ',
        cells: ['飲む, 遊ぶ, 死ぬ', '飲んで, 遊んで, 死んで', '飲んだ, 遊んだ, 死んだ', 'む・ぶ・ぬ → んで / んだ (撥音便: 濁音の「で」)'],
        note: 'Voiced consonants always take で, not て.'
      },
      {
        label: 'Group 1: く / ぐ',
        cells: ['書く, 泳ぐ', '書いて, 泳いで', '書いた, 泳いだ', 'く → いて, ぐ → いで (イ音便: い + て/で)'],
        note: 'CRITICAL EXCEPTION: 行く は「いいて」にならず、「行って・行った」と促音便になります。'
      },
      {
        label: 'Group 1: す',
        cells: ['話す, 出す', '話して, 出して', '話した, 出した', 'す → して / した'],
        note: 'Behaves cleanly like polite shimasu.'
      },
      {
        label: 'Group 2: る (一段動詞)',
        cells: ['食べる, 見る, 起きる', '食べて, 見て, 起きて', '食べた, 見た, 起きた', 'る を取って「て・た」を付ける'],
        note: 'Vowel before る is usually e or i (たべ・み).'
      },
      {
        label: 'Group 3: Irregular (変格動詞)',
        cells: ['する, 来る', 'して, 来て', 'した, 来た', '不規則活用: 来る は「来て（きて）・来た（きた）」と読みが変化します。'],
        note: 'Notice 来る changes reading to 「き」 in て/た form: 来て（きて）, 来た（きた）.'
      }
    ]
  },

  conditionalsMatrix: {
    title: 'The 4 Great Conditionals Decoded: と vs ば vs たら vs なら',
    subtitle: 'The #1 JLPT trap point across N4, N3, and N2. Never confuse them again.',
    columns: ['Conditional Form', 'Core Psychological Nuance', 'Volition / Command in Result Clause?', 'Past Tense (た) in Result Clause?', 'Golden Test Trap Alert'],
    rows: [
      {
        label: '〜と (Natural / Mechanic)',
        cells: [
          'Natural law, physics, mechanical trigger: "Once X happens, Y automatically follows."',
          'Normally excludes requests and intentions in the result of a hypothetical condition.',
          'YES ✅ (Discovered a new surprise: 窓を開けると、雪が降っていた)',
          'For a request triggered by a future event, use a suitable たら construction. Distinguish conditional と from quotation と.'
        ],
        note: 'Example: ボタンを押すと、切符が出る (Press button -> ticket dispenses).'
      },
      {
        label: '〜ば (Provisional Hypothetical)',
        cells: [
          'Logical requirement: "Provided that X is met, Y is true."',
          'RESTRICTED ⚠️ (Only if verb is non-action / state like ある, or subjects differ)',
          'Not the usual form for a one-off past discovery; habitual past results are possible.',
          'TRAP: "薬を飲めば、熱が下がった" is WRONG. Use 飲んだら.'
        ],
        note: 'Classic saying: 安ければ買う (If it is cheap, I will buy it).'
      },
      {
        label: '〜たら (Chronological Trigger)',
        cells: [
          '"Once X is completed, THEN Y happens." The most versatile conditional.',
          'YES ✅ (Freely allows requests, intentions, invitations: 〜てください, 〜ましょう)',
          'YES ✅ (Indicates sequential discovery in the past: 家に帰ったら、手紙があった)',
          'SAFE HARBOR: When in doubt on volitional clauses or conversational requests, たら is king.'
        ],
        note: 'Connection: Past short form (た) + ら.'
      },
      {
        label: '〜なら (Contextual Topic / Advice)',
        cells: [
          '"If that is the case you are talking about..." Topic conditional based on listener input.',
          'YES ✅ (Excellent for advice, recommendations: 〜がいいですよ)',
          'Not a chronological after-marker; it can refer to a past premise.',
          'TRAP: Time inversion! In "日本へ行くなら、カメラを買ったほうがいい", you buy the camera BEFORE going!'
        ],
        note: 'Noun / Plain form + なら (no だ).'
      }
    ]
  },

  givingReceivingMatrix: {
    title: 'Giving & Receiving Triad (授受動詞): あげる vs くれる vs もらう',
    subtitle: 'Tracks social perspective, insider/outsider psychology, and debt of gratitude.',
    columns: ['Verb Pattern', 'Grammatical Subject', 'Direction of Action / Favor', 'Polite / Humble Counterpart', 'JLPT Trap & Mental Model'],
    rows: [
      {
        label: 'X は Y に あげる / 〜てあげる',
        cells: [
          'X (Giver / "I" or insider)',
          'From Speaker/Insider OUTWARD to Receiver',
          '差し上げる (さしあげる - Humble toward higher status)',
          'CAUTION: Doing a favor directly to a superior with 〜てあげます can sound condescending. Avoid!'
        ],
        note: 'Subject = Giver. Particle に = Receiver.'
      },
      {
        label: 'X が 私に くれる / 〜てくれる',
        cells: [
          'X (Giver / Outside party)',
          'From Outside party INWARD to Speaker / My In-Group',
          'くださる (Honorific - Superior gave to me)',
          'The giver is the subject. The recipient is understood from the speaker or empathy viewpoint, typically the speaker or their in-group.'
        ],
        note: '先生が私に本をくださった (Teacher gave me a book).'
      },
      {
        label: '私 は X に/から もらう / 〜てもらう',
        cells: [
          '私 (Receiver / Beneficiary as Subject)',
          'The subject receives from the giver; the subject need not be the speaker.',
          'いただく (Humble - I humbly received from superior)',
          'The receiver is the subject (often presented as a は-topic). The giver takes に; から is possible for receiving objects, but not freely interchangeable with に in てもらう.'
        ],
        note: '田中さんに手伝ってもらった (I got Tanaka-san to help me).'
      }
    ]
  },

  voiceMatrix: {
    title: 'The Voice Transformation Matrix: Active → Passive → Causative → Causative-Passive',
    subtitle: 'From direct acts to being victimized (迷惑受身) to being coerced (使役受身).',
    columns: ['Voice Type', 'Grammatical Meaning', 'Group 1 (五段) Formula', 'Group 2 (一段) Formula', 'Irregular (する・くる)'],
    rows: [
      {
        label: '受身 (Passive)',
        cells: [
          'Action received. Includes Suffering Passive (迷惑受身) where speaker is inconvenienced.',
          'あ-stem + れる (書く → 書かれる, 踏む → 踏まれる)',
          'Stem + られる (食べる → 食べられる, 褒める → 褒められる)',
          'する → される / くる → こられる'
        ],
        note: 'Suffering Passive: 雨に降られた (I was rained on / inconvenienced by rain).'
      },
      {
        label: '使役 (Causative)',
        cells: [
          'Make / Let someone do something. Expresses authority, permission, or triggering emotion.',
          'あ-stem + せる (行く → 行かせる, 読む → 読ませる)',
          'Stem + させる (食べる → 食べさせる)',
          'する → させる / くる → こさせる'
        ],
        note: 'Polite request: 帰らせてください (Please let me go home).'
      },
      {
        label: '使役受身 (Causative-Passive)',
        cells: [
          'Forced to do against one\'s personal desire ("I was made to..."). Highly frequent in JLPT!',
          'あ-stem + される (Contracted: 待たされる, 飲まされる, 書かされる) or せられる',
          'Stem + させられる (食べさせられる)',
          'する → させられる / くる → こさせられる'
        ],
        note: 'Exception: Verbs ending in す (話す) cannot contract to される! Must be 話させられる.'
      }
    ]
  },

  keigoMatrix: {
    title: 'Keigo (敬語) Survival Matrix: Sonkeigo vs Kenjougo',
    subtitle: 'Elevating the listener/superior (尊敬語) vs humbling yourself/in-group (謙譲語).',
    columns: ['Normal Verb', '尊敬語 (Honorific - Other person\'s action)', '謙譲語 (Humble - My own action)', 'Formula Pattern'],
    rows: [
      {
        label: '行く / 来る / いる',
        cells: ['いらっしゃる / おいでになる', '参る (まいる) / おる (いる)', 'Other: お+V-stem+になる | Me: お+V-stem+する'],
        note: '社長はいらっしゃいますか (Is the company president in?)'
      },
      {
        label: '言う (To say)',
        cells: ['おっしゃる', '申す (もうす) / 申し上げる', 'Other says: おっしゃる | I say: 申します'],
        note: '田中と申します (My name is Tanaka - humble).'
      },
      {
        label: '食べる / 飲む',
        cells: ['召し上がる (めしあがる)', 'いただく', 'Other eats: 召し上がる | I eat: いただきます'],
        note: 'どうぞ召し上がってください (Please enjoy the food).'
      },
      {
        label: '見る (To look/see)',
        cells: ['ご覧になる (ごらんになる)', '拝見する (はいけんする)', 'Other looks: ご覧になる | I inspect: 拝見する'],
        note: '資料を拝見しました (I reviewed the documents).'
      },
      {
        label: '知っている (To know)',
        cells: ['ご存知だ (ごぞんじだ)', '存じている (ぞんじている) / 存じ上げている', 'Other knows: ご存知 | I know: 存じております'],
        note: 'Never say "私はご存知です" ❌! That is honoring yourself!'
      },
      {
        label: 'する (To do)',
        cells: ['なさる', '致す (いたす)', 'Other does: なさる | I do: いたします'],
        note: 'よろしくお願いいたします (Humble request).'
      }
    ]
  },

  timeSequenceSpectrum: {
    title: 'Time & Instant Sequence Spectrum (時・継起のグラデーション)',
    subtitle: 'How Japanese grammar sharpens from general timing to split-second interruption.',
    columns: ['Grammar Point', 'JLPT Level', 'Time Window / Immediacy', 'Speaker Control / Volition', 'Defining Nuance & Trap'],
    rows: [
      {
        label: '〜最中に (さいちゅうに)',
        cells: ['N3', 'Right in the middle of active ongoing action', 'Emphasizes being in the middle of an activity', 'Often followed by an interruption, but neither surprise nor a negative outcome is required.'],
        note: 'Conjugation: V-ている + 最中に / N の最中に'
      },
      {
        label: '〜うちに',
        cells: ['N3', 'Within limited window before condition changes', 'Natural change or spontaneous urge ⚠️', 'Do it while hot / Before you forget (冷めないうちに / 忘れないうちに).'],
        note: 'Conjugation: V dictionary/ない/ている, い-adjective, な-adjectiveな or Nの + うちに'
      },
      {
        label: '〜たとたん（に）',
        cells: ['N3', 'The exact split-second after X finishes', 'Immediate surprise, NO speaker volition ❌', 'Clause B is a sudden surprise event (立ち上がったとたん、めまいがした).'],
        note: 'Conjugation: V-た + とたん（に）'
      },
      {
        label: '〜かと思うと / 〜かと思ったら',
        cells: ['N2', 'Right when you thought X had occurred', 'Sharp unexpected contrast / sudden change ❌', 'Cannot describe speaker\'s deliberate action (空が暗くなったかと思うと、雨が降ってきた).'],
        note: 'Conjugation: V-た + かと思うと'
      },
      {
        label: '〜か〜ないかのうちに',
        cells: ['N2', 'Literally on the border of completion', 'Simultaneous / instantaneous sequence', 'Almost no time gap: ベルが鳴り終わるか終わらないかのうちに.'],
        note: 'Conjugation: V-辞書形 / V-た + か + V-ない + かのうちに'
      },
      {
        label: '〜次第 (しだい)',
        cells: ['N2', 'Immediate trigger for planned next step', 'HIGH speaker volition & business resolve ✅', 'Used for future events: 決まり次第、ご連絡いたします.'],
        note: 'Conjugation: V-stem + 次第 (NO past tense in main clause!)'
      }
    ]
  },
genki1TimeAndAgeMatrix: {
    title: 'Genki I: Time (時・分) & Age (歳) Reading Matrix',
    subtitle: 'The foundational number transformations and phonetic traps in Lesson 1.',
    columns: ['Category / Unit', 'Standard Pattern', 'Irregular / Phonetic Trap Items', 'Question Form & Mnemonic'],
    rows: [
      {
        label: 'Hours (〜時: じ)',
        cells: [
          '1時(いちじ), 2時(にじ), 3時(さんじ), 5時(ごじ), 6時(ろくじ), 8時(はちじ), 10時(じゅうじ), 11時(じゅういちじ), 12時(じゅうにじ)',
          '⚠️ 4時 = よじ (NOT よんじ/しじ), 7時 = しちじ (sometimes ななじ), 9時 = くじ (NOT きゅうじ)',
          '何時 (なんじ)? Example: 今、何時ですか。(What time is it now?)'
        ],
        note: 'Trap alert: 4:00, 7:00, 9:00 have unique readings that JLPT tests frequently.'
      },
      {
        label: 'Minutes (〜分: ふん/ぷん)',
        cells: [
          'Unvoiced ふん: 2分(にふん), 5分(ごふん), 7分(ななふん), 9分(きゅうふん)',
          'Geminate / Voiced ぷん: 1分(いっぷん), 3分(さんぷん), 4分(よんぷん), 6分(ろっぷん), 8分(はっぷん/はちふん), 10分(じゅっぷん/じっぷん)',
          '何分 (なんぷん)? Half past = 半 (はん): 1時半 (1:30)'
        ],
        note: 'Mnemonic: 1, 3, 4, 6, 8, 10 は半濁音の「ぷん」になります。'
      },
      {
        label: 'Age (〜歳: さい)',
        cells: [
          '2歳(にさい), 3歳(さんさい), 4歳(よんさい), 5歳(ごさい), 6歳(ろくさい), 7歳(ななさい), 9歳(きゅうさい)',
          '⚠️ 1歳 = いっさい, 8歳 = はっさい, 10歳 = じゅっさい (じっさい), 20歳 = はたち (二十歳)',
          '何歳 (なんさい)? Polite: おいくつですか。'
        ],
        note: '20歳 は「はたち（二十歳）」と読み、後ろに「さい」は付きません。'
      },
      {
        label: 'Telephone & School Year',
        cells: [
          '学年: 1年生(いちねんせい), 2年生(にねんせい), 3年生(さんねんせい), 4年生(よねんせい ⚠️)',
          'Telephone hyphens are read as の: 090-1234-5678 (ぜろきゅうぜろ の いちにさんよん の...)',
          '何年生 (なんねんせい)? / 電話番号は何番 (なんばん)?'
        ],
        note: '4th year student is よねんせい (NOT よんねんせい).'
      }
    ]
  },

  genki1VerbGroupsMatrix: {
    title: 'Genki I: The Three Verb Groups & Polite Conjugation Matrix',
    subtitle: 'Ru-verbs (一段), U-verbs (五段), and Irregular verbs (変格) in Lesson 3.',
    columns: ['Verb Group', 'Dictionary Ending Rule', 'Stem Formation Formula', 'Present Polite Affirmative & Negative', 'Crucial Trap Verbs (The "Fake Ru" Verbs)'],
    rows: [
      {
        label: 'Group 2: Ru-Verbs (一段動詞)',
        cells: [
          'Ends in る preceded by an /i/ or /e/ sound (e.g. 食べる, 見る, 起きる: 直前が「い段」または「え段」)',
          'Simply DROP る to obtain the stem (食べ-, 見-, 起き-)',
          '食べます / 食べません, 見ます / 見ません',
          'Regular behavior: stems are stable across all conjugations.'
        ],
        note: 'Drop る, add ます/ません.'
      },
      {
        label: 'Group 1: U-Verbs (五段動詞)',
        cells: [
          'Ends in any basic -u syllable: う, つ, る, む, ぶ, ぬ, く, ぐ, す',
          'Shift the final -u sound to the corresponding -i sound (u→i, tsu→chi, ru→ri, ku→ki, mu→mi, su→shi)',
          '行く → 行きます / 行きません, 飲む → 飲みます, 話す → 話します, 待つ → 待ちます',
          '⚠️ LOOKS LIKE RU BUT IS AN U-VERB: 帰る（かえります）, 入る（はいります）, 知る（しります）, 走る（はしります）!'
        ],
        note: 'Golden Rule: If a verb ends in -aru, -oru, -uru, it is ALWAYS an U-verb. If it ends in -iru or -eru, check if it is one of the classic Godan exceptions like 帰る.'
      },
      {
        label: 'Group 3: Irregular Verbs (不規則動詞)',
        cells: [
          'Only TWO verbs in the entire Japanese language: する (to do) and 来る (くる, to come)',
          'Stems undergo complete vowel mutation: する → し-, くる → き-',
          'します / しません, 来ます (きます) / 来ません (きません)',
          'Compound suru-verbs follow this pattern: 勉強する → 勉強します, 案内する → 案内します'
        ],
        note: '来（く）る は活用によって「来（き）ます」と読みが変化します。'
      }
    ]
  },

  genki1AdjectivesMatrix: {
    title: 'Genki I: Adjective Conjugation Matrix (Lesson 5)',
    subtitle: 'い-adjectives vs な-adjectives across Present, Past, Affirmative, and Negative.',
    columns: ['Adjective Class', 'Present Affirmative', 'Present Negative', 'Past Affirmative', 'Past Negative', 'Noun Modification'],
    rows: [
      {
        label: 'い-Adjectives (True Adjectives)',
        cells: [
          '高いです',
          '高くないです / 高くありません (Drop い → くない)',
          '高かったです (Drop い → かった)',
          '高くなかったです / 高くありませんでした (Drop い → くなかった)',
          'Direct attachment: 高い本 (An expensive book)'
        ],
        note: '⚠️ THE IRREGULAR "GOOD": いい は「良い（よい）」から変化します。否定: よくないです, 過去: よかったです, 過去否定: よくなかったです。「いくない」は誤り ❌!'
      },
      {
        label: 'な-Adjectives (Adjectival Nouns)',
        cells: [
          '静かです',
          '静かじゃないです / 静かではありません',
          '静かでした',
          '静かじゃなかったです / 静かではありませんでした',
          'Requires な before noun: 静かな町 (A quiet town)'
        ],
        note: '⚠️ LOOKS LIKE い BUT IS A な-ADJECTIVE: きれい (pretty/clean), 嫌い (きらい, disliked), 有名 (ゆうめい, famous). They take な: きれいな町, 有名な人!'
      }
    ]
  },

  genki1ShortFormsMatrix: {
    title: 'Genki I: Plain / Short Forms (普通形) Master Matrix (Lessons 8 & 9)',
    subtitle: 'The essential informal register for ~と思う, ~と言っていた, and casual conversation.',
    columns: ['Predicate Type', 'Present Affirmative', 'Present Negative', 'Past Affirmative', 'Past Negative'],
    rows: [
      {
        label: 'Verbs (動詞)',
        cells: [
          '辞書形 (Dictionary): 食べる / 行く',
          'ない形 (Nai-form): 食べない / 行かない (Note: ある → ない)',
          'た形 (Ta-form): 食べた / 行った',
          'なかった形: 食べなかった / 行かなかった'
        ],
        note: 'Conjugates like the Te-form (て → た, で → だ).'
      },
      {
        label: 'い-Adjectives',
        cells: [
          'Drop です: かわいい / 高い',
          'Drop です: かわいくない / 高くない',
          'Drop です: かわいかった / 高かった',
          'Drop です: かわいくなかった / 高くなかった'
        ],
        note: 'Plain form of い-adjectives simply drops です!'
      },
      {
        label: 'な-Adjectives & Nouns',
        cells: [
          'だ (Attach だ): 静かだ / 学生だ',
          'じゃない: 静かじゃない / 学生じゃない',
          'だった: 静かだった / 学生だった',
          'じゃなかった: 静かじゃなかった / 学生じゃなかった'
        ],
        note: 'CRITICAL TRAP: In affirmative present, です becomes だ! (e.g. 日本人だと思う).'
      }
    ]
  },

  genki2PotentialMatrix: {
    title: 'Genki II: Potential Verbs (可能形) Matrix (Lesson 13)',
    subtitle: 'Expressing ability and situational possibility ("can do").',
    columns: ['Verb Group', 'Dictionary Form', 'Potential Form (可能形)', 'Particle Transformation Rule', 'Crucial Trap Alerts'],
    rows: [
      {
        label: 'Group 2: Ru-Verbs',
        cells: [
          '食べる, 見る, 起きる',
          '食べられる, 見られる, 起きられる (Drop る, attach られる)',
          'Direct object particle を shifts to が: 漢字が読める, 日本語が話せる',
          'Colloquial "ra-nuki" (ら抜き): 食べれる, 見れる (frequent in spoken Japanese, but avoid on formal JLPT!)'
        ],
        note: 'Identical form to passive; context disambiguates.'
      },
      {
        label: 'Group 1: U-Verbs',
        cells: [
          '行く, 飲む, 話す, 待つ, 泳ぐ',
          '行ける, 飲める, 話せる, 待てる, 泳げる (Shift final -u sound to -e sound and add る)',
          'All potential verbs conjugate as Group 2 (Ichidan) verbs once transformed: 話せる → 話せます / 話せない',
          'Do NOT add られる to U-verbs! 行く becomes 行ける, NOT 行かられる ❌!'
        ],
        note: 'Clean shift: -u → -eru.'
      },
      {
        label: 'Group 3: Irregular',
        cells: [
          'する (to do), 来る (くる, to come)',
          'する → できる, 来る → こられる (来られる)',
          'Particle shift: 運転ができる (Can drive), 日本語ができる (Can speak Japanese)',
          'Note the reading of 来 changes to "ko": こられる (NOT ちられる ❌).'
        ],
        note: 'する completely transforms into the independent potential verb できる.'
      }
    ]
  },

  genki2VolitionalMatrix: {
    title: 'Genki II: Volitional Form (意向形 / 意志形) Matrix (Lesson 15)',
    subtitle: 'Casual "Let\'s do" (~ましょう) and ongoing personal intentions (~と思っています).',
    columns: ['Verb Group', 'Dictionary Form', 'Volitional Form (意向形)', 'Key Syntactic Constructions'],
    rows: [
      {
        label: 'Group 2: Ru-Verbs',
        cells: [
          '食べる, 見る, 起きる',
          '食べよう, 見よう, 起きよう (Drop る, attach よう)',
          '1. Casual invitation: 一緒に行こう (Let\'s go together!)'
        ],
        note: 'Casual equivalent of 〜ましょう.'
      },
      {
        label: 'Group 1: U-Verbs',
        cells: [
          '行く, 飲む, 話す, 買う, 待つ',
          '行こう, 飲もう, 話そう, 買おう, 待とう (Shift final -u to -o sound and elongate with う)',
          '2. On-the-spot decision: 〜ようと思う (I think I will...)'
        ],
        note: 'Elongated vowel sound: ikou, nomou, hanasou.'
      },
      {
        label: 'Group 3: Irregular',
        cells: [
          'する, 来る (くる)',
          'しよう, 来よう (こよう)',
          '3. Ongoing firm resolve: 〜ようと思っている (I have been intending to...)'
        ],
        note: 'Pronounced ko-you.'
      }
    ]
  },

  genki2TransitiveIntransitiveMatrix: {
    title: 'Genki II: Transitive vs Intransitive (他動詞 vs 自動詞) Pairs (Lesson 18)',
    subtitle: 'Human deliberate action with を vs Spontaneous state change with が + 〜ている.',
    columns: ['Verb Meaning', '他動詞 (Transitive: Subject + を + V)', '自動詞 (Intransitive: Subject + が + V)', 'Resulting State: 自動詞 + 〜ている'],
    rows: [
      {
        label: 'Open (To open)',
        cells: ['窓を開ける (Open the window)', '窓が開く (The window opens)', '窓が開いている (The window is open)'],
        note: 'Transitive takes を; Intransitive takes が.'
      },
      {
        label: 'Close (To close)',
        cells: ['ドアを閉める (Close the door)', 'ドアが閉まる (The door closes)', 'ドアが閉まっている (The door is closed)'],
        note: 'Intransitive -aru ending indicates state change.'
      },
      {
        label: 'Turn on / Light up',
        cells: ['電気をつける (Turn on light)', '電気がつく (Light turns on)', '電気がついている (Light is on)'],
        note: 'State: It is currently illuminated.'
      },
      {
        label: 'Turn off / Extinguish',
        cells: ['電気を消す (Turn off light)', '電気が消える (Light goes out)', '電気が消えている (Light is off)'],
        note: '消す (transitive, -su) vs 消える (intransitive, -eru).'
      },
      {
        label: 'Drop / Fall',
        cells: ['財布を落とす (Drop wallet)', '財布が落ちる (Wallet drops/falls)', '財布が落ちている (A wallet is lying dropped)'],
        note: '落とす is human action; 落ちる is spontaneous event.'
      },
      {
        label: 'Put in / Enter',
        cells: ['本をかばんに入れる (Put book in bag)', '部屋に入る (Enter room)', 'かばんに本が入っている (A book is inside the bag)'],
        note: '「入る（はいる）」は一段動詞の形ですが、五段（う動詞）活用です。'
      },
      {
        label: 'Take out / Come out',
        cells: ['ペンを出す (Take out pen)', '月が出る (Moon comes out)', '手紙が出ている (Letter has been sent out)'],
        note: '出す (transitive) vs 出る (intransitive).'
      },
      {
        label: 'Break / Break down',
        cells: ['時計を壊す (Break a clock)', '時計が壊れる (Clock breaks)', '時計が壊れている (Clock is broken)'],
        note: '壊れている describes existing condition of brokenness.'
      },
      {
        label: 'Soil / Get dirty',
        cells: ['服を汚す (Soil one\'s clothes)', '服が汚れる (Clothes get dirty)', '服が汚れている (Clothes are stained/dirty)'],
        note: 'Intransitive state marker.'
      }
    ]
  },

  skmN2ConnectorsMatrix: {
    title: 'SKM N2: The 9 Discourse Connector Categories (pp. 186–187)',
    subtitle: 'Sentence-initial discourse markers systematically distinguished by rhetorical function.',
    columns: ['Discourse Function', 'Key Connectors', 'Defining Nuance & Usage Distinction', 'Illustrative Example Context'],
    rows: [
      {
        label: '1. Adding Points (累加・付加)',
        cells: [
          'しかも, そのうえ, さらに, そればかりか, そればかりでなく',
          'しかも: adds surprising/escalating extra detail. そのうえ: "on top of that". さらに: step-by-step progressive increment. そればかりか: "not merely that, but even..."',
          'この料理は美味しく、しかも値段が手頃だ。'
        ],
        note: 'Escalation beyond prior statement.'
      },
      {
        label: '2. Contrast & Comparison (対比)',
        cells: [
          'それに対して, 一方(で)',
          'それに対して: sharp directional contrast between two distinct entities. 一方: balancing two parallel facts or sides of the same entity.',
          '兄は社交的だ。それに対して、弟は物静かな性格だ。'
        ],
        note: 'A vs B juxtaposition.'
      },
      {
        label: '3. Alternatives & Choices (選択)',
        cells: [
          'あるいは, それとも',
          'あるいは: formal/written alternative ("or alternatively"). それとも: conversational question alternative ("A? Or is it B?").',
          '郵送、あるいはメールで提出してください。'
        ],
        note: 'それとも is restricted to interrogative choices.'
      },
      {
        label: '4. Consequence & Action (結末・行動)',
        cells: [
          'そのため, したがって, そこで, すると, このように, こうして',
          'そのため: objective causal result. したがって: logical conclusion ("therefore"). そこで: motivated deliberate action taken in response. すると: instantaneous discovery/mechanical result.',
          '雨が降り出した。そこで、近くの喫茶店に入った。'
        ],
        note: 'Trap: そこで requires speaker\'s deliberate volition; すると excludes personal intention!'
      },
      {
        label: '5. Rationale & Background (理由・説明)',
        cells: [
          'なぜなら(ば), というのは',
          'なぜなら(ば): formal retrospective reason ("the reason why is..."). というのは: explanatory elaboration of context.',
          '昨夜は欠席しました。というのは、急な発熱があったからです。'
        ],
        note: 'Often concludes with 〜からだ / 〜ためだ.'
      },
      {
        label: '6. Adversative & Persistence (逆接・譲歩)',
        cells: [
          'だが, ところが, それなのに, それでも',
          'だが: standard formal but. ところが: unexpected, surprising twist. それなのに: indignant frustration against expectation. それでも: persistence despite counterweight.',
          '必死に頼み込んだ。それでも、彼は承諾しなかった。'
        ],
        note: 'ところが cannot introduce speaker\'s volitional request.'
      },
      {
        label: '7. Restatement & Analogy (換言・要約)',
        cells: [
          'つまり, 要するに, すなわち, いわば',
          'つまり: summarizing meaning ("in short"). 要するに: distilling to core essence. すなわち: formal exact equivalence ("namely"). いわば: figurative metaphor ("so to speak").',
          '彼は私の恩人、いわば人生の師匠だ。'
        ],
        note: 'いわば requires a metaphorical comparison.'
      },
      {
        label: '8. Qualification & Provisos (補足・条件)',
        cells: [
          'ただし, もっとも, なお',
          'ただし: strict conditions, provisos, or exceptions to the preceding rule. もっとも: natural partial concession or reservation. なお: neutral supplementary admin detail.',
          '入場は無料です。ただし、事前登録が必要です。'
        ],
        note: 'ただし is standard for legal and contract terms.'
      },
      {
        label: '9. Topic Shift & Transition (転換)',
        cells: [
          'さて, ところで',
          'さて: closes previous topic and smoothly advances forward to main business ("now then"). ところで: abrupt complete change of subject ("by the way").',
          '雑談はここまでにして、さて、本題に入りましょう。'
        ],
        note: 'Do not confuse discourse ところで with temporal 〜たところで!'
      }
    ]
  },

  skmN2ClassicalRemnantsMatrix: {
    title: 'SKM N2: Classical Remnants & Archaic Literary Forms (p. 126)',
    subtitle: 'Classical grammar surviving in formal written Japanese and idioms.',
    columns: ['Classical Family', 'Literary Form & Conjugation', 'Modern Equivalent', 'Core Meaning & Contextual Usage'],
    rows: [
      {
        label: 'Classical Negation: ず / ざる',
        cells: [
          'V-未然形 + ず (せず) / ざる + N',
          '〜ないで / 〜ない (修飾: 〜ないN)',
          'ず: adverbial negative ("without doing"). ざる: noun-attributive negative ("that does not..."). Examples: 絶えず (constantly), 意図せざる結果 (unintended consequence), 知らざる一面 (unknown side).'
        ],
        note: 'Special: する becomes せず (adverbial) / せざる (attributive).'
      },
      {
        label: 'Classical Obligation: べし / べく',
        cells: [
          'V-辞書形 + べし / べき / べく',
          '〜なければならない / 〜する目的で',
          'べし: natural solemn duty or inevitable consequence. べき: moral obligation ("ought to"). べく: formal in-order-to purpose marker (成功すべく努力する).'
        ],
        note: 'Common phrase: あるべからざる (that should never exist).'
      },
      {
        label: 'Classical Negative Conjecture: まい',
        cells: [
          'V-辞書形 (一段: 辞書/未然) + まい',
          '〜ないだろう / 絶対〜しない',
          '1. Negative conjecture: "surely will not" (今夜は雨が降るまい). 2. Strong negative resolve: "will never do again" (二度と行くまい). 3. Rhetorical: ではあるまいか (is it not perhaps...?).'
        ],
        note: 'Group 2 / Irregular: するまい/すまい, くるまい/こまい.'
      },
      {
        label: 'Classical Simultaneous & Progress: つつ',
        cells: [
          'V-stem + つつ / つつある',
          '〜ながら / 〜ている (進行中)',
          '1. つつ: concurrent contrastive action ("while knowing full well...": 悪いと知りつつ). 2. つつある: ongoing progressive change ("is steadily in the process of...": 事態は悪化しつつある).'
        ],
        note: 'つつある only pairs with verbs of continuous change (発展, 増加, 回復).'
      },
      {
        label: 'Classical Imperative: よ / せよ',
        cells: [
          'V-未然/連用 + せよ / れよ',
          '〜しなさい / 〜しろ',
          'Written imperative used in exam instructions, technical documents, and public slogans. Examples: 次の問に答えよ (Answer the following question), 行動せよ (Take action).'
        ],
        note: 'する becomes せよ; 来る becomes 来い (こい) / 来たれ.'
      }
    ]
  },

  skmN3CompoundParticlesMatrix: {
    title: "SKM N3: Core Compound Particles Matrix (p. 62)",
    subtitle: "について vs に対して vs にとって vs として vs において",
    columns: ["Compound Particle", "Grammatical Function & Nuance", "Typical Predicates / Collocations", "Key Restrictions & Comparison"],
    rows: [
      {
        label: "〜について (Topic / Theme)",
        cells: ["名詞 + について (修飾: 〜についてのN)", "Regarding / about: introduces the central topic of thought, speech, or inquiry.", "日本の文化について研究する / 将来の進路について話し合う", "Followed by verbs of inquiry/expression: 調べる, 書く, 話す, 考える. Cannot replace に対して when pointing to an opposing party."],
        note: "Formal equivalent is 〜に関（かん）して."
      },
      {
        label: "〜に対して (Target / Contrast)",
        cells: ["名詞 + に対して (修飾: 〜に対するN)", "1. Toward / facing an external target. 2. In sharp contrast between two different subjects.", "お客様に対して丁寧な言葉遣いをする / 兄が活発なのに対して、弟は物静かだ", "Distinguish from 反面: 反面 contrasts two aspects of the SAME subject; に対して contrasts TWO DISTINCT subjects."],
        note: "When expressing an attitude toward people, に対して is mandatory."
      },
      {
        label: "〜にとって (Evaluative Standpoint)",
        cells: ["名詞 + にとって (修飾: 〜にとってのN)", "From the standpoint / in the eyes of: establishes the subjective evaluator.", "私にとって家族が一番大切だ / 留学生にとって漢字の習得は高い壁だ", "Predicate MUST express subjective evaluation (大切だ, 難しい, 深刻だ). NEVER expresses personal physical action (❌ 私にとって本を買う)."],
        note: "Evaluates value or difficulty from that party's stance."
      },
      {
        label: "〜として (Role / Capacity)",
        cells: ["名詞 + として (修飾: 〜としてのN)", "In the role, capacity, official status, or recognized qualification of.", "留学生として日本に来ました / 彼は会社の代表として会議に出席した", "Noun before として must represent an official title, category, function, or status."],
        note: "Indicates functioning within that recognized status."
      },
      {
        label: "〜において (Formal Domain / Setting)",
        cells: ["名詞 + において (修飾: 〜におけるN)", "In / at / within: specifies the formal setting, field, era, or domain.", "現代社会において情報技術は不可欠だ / 開会式は第一ホールにおいて行われる", "Formal written equivalent of で; heavily used in news, academic writing, and official announcements."],
        note: "Formal locus marker for occasions and fields."
      }
    ]
  },

  skmN3NominalizersMatrix: {
    title: "SKM N3: Nominalizers Triad Matrix: こと vs の vs もの (p. 66)",
    subtitle: "Distinguishing abstract truth, sensory perception, and tangible/natural reality.",
    columns: ["Nominalizer", "Core Linguistic Nuance", "Exclusive Grammatical Environments", "Classic Golden Rules"],
    rows: [
      {
        label: "こと (Abstract Truth / Definition)",
        cells: ["動詞普通形 + こと / 名詞 + であること", "Conceptualization, abstract facts, rules, and definition statements.", "私の趣味は音楽を聴くことです / パソコンを使うことができる", "Mandatory in fixed patterns: 〜ことができる, 〜ことにする / なる, 〜ことがある. Mandatory in definitional sentences (X は Y ことです)."],
        note: "Use こと when treating an action as an abstract concept."
      },
      {
        label: "の (Direct Sensory Perception)",
        cells: ["動詞普通形 + の", "Immediate concrete action happening right in front of the speaker's senses.", "子供たちが走っているのを見た / 隣の部屋で誰かが歌っているのが聞こえる", "Mandatory with sensory verbs (見る, 聞こえる, 感じる) and physical intervention verbs (手伝う, 待つ, 止める). Mandatory in cleft sentences (〜のは〜だ)."],
        note: "Sensory perception of unfolding events always takes の."
      },
      {
        label: "もの (Tangible Reality / Natural Essence)",
        cells: ["普通形 + もの (な-adj な / 名詞な)", "Concrete physical objects, universal human nature, or innate natural truth.", "冷たいものが飲みたい / 人間は誰でも失敗するものだ", "〜ものだ expresses universal general truth ('It is human nature to...'). 〜ものではない expresses strong moral warning ('You should never...')."],
        note: "もの refers to real substances or general inherent truths."
      }
    ]
  },

  skmN3WakeQuadrupletsMatrix: {
    title: "SKM N3: The 4 わけ Quadruplets Decoded (p. 74)",
    subtitle: "Logical inevitability vs total impossibility vs partial denial vs moral barrier.",
    columns: ["Pattern", "Meaning & Psychological State", "Formula & Negation Type", "JLPT Test Trap Alert"],
    rows: [
      {
        label: "〜わけだ (Logical Conclusion)",
        cells: ["Naturally so / No wonder: a conclusion that follows as the obvious logical result.", "普通形 (な-adj な, N である) + わけだ", "今日は気温が38度もある。暑いわけだ。", "Connects observed facts into an understandable explanation ('That explains why!')."],
        note: "Confirms why a situation is naturally understandable."
      },
      {
        label: "〜わけがない (Absolute Impossibility)",
        cells: ["There is no way on earth that...: absolute objective impossibility based on evidence.", "普通形 + わけがない (= はずがない)", "彼がそんな酷い嘘をつくわけがない。", "Emphatic certainty that something cannot possibly be true."],
        note: "Strong denial of possibility based on reason."
      },
      {
        label: "〜わけではない (Partial Negation)",
        cells: ["It does not necessarily mean that... / I don't mean to say that...", "普通形 + わけではない", "日本料理が嫌いなわけではないが、納豆は苦手だ。", "Softens a statement by denying total black-and-white interpretation."],
        note: "Partial negation; does not reject the entire premise."
      },
      {
        label: "〜わけにはいかない (Moral / Social Barrier)",
        cells: ["Cannot bring oneself to do / Cannot afford to do because of duty, conscience, or society.", "動詞辞書形 + わけにはいかない (二重否定: 動詞ない形 + わけにはいかない = Must do)", "大事な会議があるから、熱があっても休むわけにはいかない。", "Physical ability exists, but social/moral constraints prevent the action."],
        note: "Conscience or social duty forbids the action."
      }
    ]
  },

  skmN3BakariSpectrumMatrix: {
    title: "SKM N3: The 〜ばかり Functional Spectrum (p. 80)",
    subtitle: "From exclusive concentration to critical indulgence to recency to unidirectional change.",
    columns: ["Structure", "Core Function & Meaning", "Emotional Tone", "Distinct Contrast Item"],
    rows: [
      {
        label: "N + ばかり (Exclusive Concentration)",
        cells: ["Nothing but N / Only N: focused entirely on one item to the exclusion of others.", "肉ばかり食べないで、野菜も食べなさい。", "Critical observation of one-sidedness.", "Contrast with だけ: だけ is neutral limitation; ばかり implies excessive saturation."],
        note: "Often carries a tone of mild criticism regarding imbalance."
      },
      {
        label: "V-て + ばかりいる (Habitual Indulgence)",
        cells: ["Does nothing but V all the time: habitual repetition of unproductive activity.", "弟は勉強もしないで、ゲームをしてばかりいる。", "Annoyance or disapproval from the speaker.", "Always expresses critical reproach regarding repeated behavior."],
        note: "Indicates continuous repetition with speaker criticism."
      },
      {
        label: "V-た + ばかりだ (Subjective Recency)",
        cells: ["Just finished doing: feels subjectively immediate to the speaker.", "先月日本に来たばかりなので、まだ地理がよく分かりません。", "Subjective feeling of recency, even if weeks have passed.", "Contrast with 〜たところだ: たところだ is literal immediate temporal phase (minutes ago)."],
        note: "Speaker treats the completed action as very fresh."
      },
      {
        label: "V-辞書形 + ばかりだ (Unidirectional Trend)",
        cells: ["Continues steadily to worsen/progress, or everything is prepared and ready to V.", "不況のせいで、会社の業績は悪化するばかりだ。", "Passive acknowledgment of unfolding momentum.", "Only pairs with verbs of continuous change (上がる, 下がる, 悪化する)."],
        note: "Describes an ongoing change moving steadily in one direction."
      },
      {
        label: "〜ばかりか / ばかりでなく (Escalating Addition)",
        cells: ["Not only A, but on top of that B as well: escalating surprise or severity.", "彼は漢字ばかりか、ひらがなさえ読めない。", "Strong emphatic addition.", "Clause B introduces something even more surprising or severe."],
        note: "Formal equivalent of 〜だけでなく."
      }
    ]
  },

  skmN3SuruNaruDecisionGrid: {
    title: "SKM N3: The Decision & Custom Grid: する vs なる (p. 84)",
    subtitle: "Personal volition vs external outcome vs maintained habit vs institutional regulation.",
    columns: ["Expression", "Deciding Agent", "Temporality & Aspect", "Real-World Communication Context"],
    rows: [
      {
        label: "〜ことにする (Personal Decision)",
        cells: ["Personal volition / deliberate conscious choice made by the speaker.", "One-off new resolution.", "健康のために、今日からお酒をやめることにした。", "Announcing a personal decision."],
        note: "Reflects the speaker's own will."
      },
      {
        label: "〜ことになる (External Outcome)",
        cells: ["External circumstances, collective decision, or objective outcome without individual focus.", "Settled outcome / development.", "来月、大阪の本社へ転勤することになりました。", "Polite reporting of business/life developments where personal agency is restrained."],
        note: "Presents an arrangement as a settled situation."
      },
      {
        label: "〜ことにしている (Maintained Habit)",
        cells: ["Personal self-discipline / self-imposed standing policy.", "Ongoing maintained routine.", "どんなに忙しくても、毎日30分は本を読むことにしている。", "Describing personal health, lifestyle, or study discipline."],
        note: "Speaker's own persistent rule."
      },
      {
        label: "〜ことになっている (Standing Regulation)",
        cells: ["Standing law, institutional regulation, societal rule, or fixed schedule.", "Established system / rule.", "法律により、二十歳未満の飲酒は禁止されていることになっている。", "Explaining societal laws, school rules, and official schedules."],
        note: "Societal or institutional standing rule."
      }
    ]
  },

  skmN3AdverbCollocationsMatrix: {
    title: "SKM N3: Adverb & Sentence-Ending Collocations (呼応表現) (p. 92)",
    subtitle: "The golden pair triggers that determine the grammatical ending before reading the sentence.",
    columns: ["Trigger Adverb", "Required Ending Form", "Semantic Category", "JLPT Trap Example"],
    rows: [
      {
        label: "決して (けっして)",
        cells: ["〜ない / 否定形", "Resolute total refusal: 'Never, under any circumstance'.", "約束は決して破りません。", "Trap: Pairs strictly with negative predicates."],
        note: "Strong determination never to do."
      },
      {
        label: "まったく",
        cells: ["〜ない / 否定形", "Complete absence: 'Not in the slightest / Not at all'.", "彼の説明は難しくて、まったく分からなかった。", "Can also mean 'truly/completely' in affirmative with surprise (まったく驚いた)."],
        note: "Emphasizes complete lack or total state."
      },
      {
        label: "必ずしも (かならずしも)",
        cells: ["〜わけではない / 〜とは限らない", "Partial exception: 'Not necessarily true in every case'.", "有名大学を卒業した人が、必ずしも優秀だとは限らない。", "Trap: Almost always resolves in 〜とは限らない or 〜わけではない."],
        note: "Denies absolute universality."
      },
      {
        label: "まるで",
        cells: ["〜ようだ / 〜みたいだ", "Vivid figurative simile: 'Just as if / Exactly like'.", "あの雲はまるで白い城のようだ。", "Trap: Signals a metaphorical comparison."],
        note: "Introduces a vivid simile."
      },
      {
        label: "たとえ",
        cells: ["〜ても / 〜でも", "Extreme hypothetical concession: 'Even if / No matter if'.", "たとえ親に反対されても、自分の夢を諦めない。", "Trap: Pairs with 〜ても to concede an extreme situation."],
        note: "Concessive hypothesis marker."
      },
      {
        label: "どうしても",
        cells: ["〜たい / 〜てしまう / 否定形", "Inescapable yearning or unavoidable impossibility: 'By all means / Simply cannot'.", "どうしても日本で働きたい。 / どうしても鍵が見つからない。", "Expresses powerful internal urge or insurmountable barrier."],
        note: "Pairs with strong volition or impossibility."
      },
      {
        label: "まさか",
        cells: ["〜ないだろう / 〜とは思わなかった", "Utter disbelief: 'It couldn't possibly be... / Never in my wildest dreams'.", "まさか彼が試験に落ちるとは思わなかった。", "Trap: Expresses shock that an unthinkable event occurred."],
        note: "Signals incredulity or surprise."
      }
    ]
  },

  skmN3SuffixMatrix: {
    title: "SKM N3: Suffix Transformation Matrix: っぽい vs だらけ vs 気味 vs がち (p. 96)",
    subtitle: "Resemblance vs surface saturation vs physical tinge vs unfortunate habit.",
    columns: ["Suffix", "Attachment Base", "Nuance & Emotional Valence", "Signature High-Yield Examples"],
    rows: [
      {
        label: "〜っぽい (Resemblance / Cheapened Quality)",
        cells: ["名詞 / 動詞ます語幹 / い形容詞語幹", "Resembling a quality, often with a childish, negative, or cheapened tone: '-ish, -like'.", "子供っぽい (childish), 怒りっぽい (quick-tempered), 安っぽい (cheap-looking), 白っぽい (whitish)", "Cannot be used for dignified praise (use 〜らしい instead)."],
        note: "Negative or informal resemblance."
      },
      {
        label: "〜だらけ (Surface Saturation)",
        cells: ["名詞 (always negative or messy entities)", "Completely covered, riddled with, or full of undesirable things across an entire surface.", "間違いだらけ (riddled with errors), 泥だらけ (covered in mud), 借金だらけ (deep in debt)", "Exclusive to negative, dirty, or flawed conditions."],
        note: "Physical or metaphorical mess across the whole surface."
      },
      {
        label: "〜気味 (ぎみ) (Slight Negative Tinge)",
        cells: ["名詞 / 動詞ます語幹", "A slight, emerging physical, mental, or bodily symptom: 'A touch of..., feeling somewhat...'.", "風邪気味 (a touch of a cold), 疲れ気味 (somewhat tired), 緊張気味 (a bit nervous)", "Describes an incipient, mild physical or psychological feeling."],
        note: "Slight internal feeling or symptom."
      },
      {
        label: "〜がち (Unfortunate Tendency)",
        cells: ["名詞 / 動詞ます語幹", "Unfortunate recurrent tendency or habit: 'Prone to doing..., frequently happens'.", "病気がち (frequently falling ill), 遠慮しがち (tending to hold back), 留守にしがち (often away)", "Describes a persistent negative pattern over time."],
        note: "Frequent regrettable occurrence."
      }
    ]
  },

  skmN3TeKuruTeIkuMatrix: {
    title: "SKM N3: Spatiotemporal Direction Matrix: てくる vs ていく (p. 124)",
    subtitle: "Spatial vectors, temporal evolution, and psychological emergence.",
    columns: ["Dimension", "〜てくる (Approaching / Emerging)", "〜ていく (Departing / Continuing)", "Visual Mental Model"],
    rows: [
      {
        label: "Physical Space (空間的移動)",
        cells: ["Moving toward the speaker's current physical location.", "Moving away from the speaker into distance.", "黒い雲がこちらへ近づいてきた (Clouds approached us) vs 飛行機が遠くへ飛んでいった (Plane flew away).", "Speaker is the spatial anchor point (原点)."],
        note: "Spatial vector toward vs away from speaker."
      },
      {
        label: "Time Dimension (時間的推移)",
        cells: ["Development from the past up to the present moment.", "Progression from the present moment onward into the future.", "日本で三年勉強してきた (Have studied up to now) vs これからも努力を続けていく (Will continue onward into future).", "Present moment is the pivot point."],
        note: "Historical accumulation up to now vs future trajectory."
      },
      {
        label: "Physiological / Emergence (生起・変化)",
        cells: ["Spontaneous internal sensation emerging into conscious perception.", "Fading away, disappearing, or settling into extinction.", "寒くなってきた / お腹が空いてきた (Felt cold / hunger emerge) vs 音が消えていった (Sound faded away).", "Perception emerging inward vs dissolving outward."],
        note: "Internal emergence vs outward dissolution."
      }
    ]
  },

  skmN2InceptionOccasionMatrix: {
    title: "SKM N2: Inception & Turning Point Matrix (p. 122)",
    subtitle: "に際して vs にあたって vs に先立って vs を契機に / を機に",
    columns: ["Grammar Pattern", "Formality & Register", "Core Meaning & Timing", "Prerequisite Conditions"],
    rows: [
      {
        label: "〜に際して (Momentous Occasion)",
        cells: ["Formal written / public announcements.", "On the occasion of / When embarking upon: used for special, momentous, non-routine events.", "動詞辞書形 / 名詞 + に際して", "新しいプロジェクトの開始に際して、チーム全員に注意事項が伝えられた。"],
        note: "Formal announcement for special occasions."
      },
      {
        label: "〜にあたって (Forward-Looking Juncture)",
        cells: ["Formal speeches, ceremonies, welcoming addresses.", "At this crucial juncture of starting / As we embark upon: forward-looking positive resolve.", "動詞辞書形 / 名詞 + にあたって", "新生活を始めるにあたって、目標を明確に定めた。"],
        note: "Clause B always contains positive resolve, preparation, or greetings."
      },
      {
        label: "〜に先立って (Preparatory Action)",
        cells: ["Formal business, research, public events.", "In advance of / Prior to embarking on: Action A is a prerequisite step carried out before B.", "名詞 / 動詞辞書形 + に先立って (修飾: 〜に先立つN)", "映画の一般公開に先立って、関係者向けの特別試写会が行われた。"],
        note: "Deliberate prerequisite step prior to main event."
      },
      {
        label: "〜を契機に / 〜を機に (Catalyst for Transformation)",
        cells: ["Written narrative, expository analysis, historical reflection.", "Triggered by / Taking X as the decisive catalyst for permanent transformation.", "名詞 + を契機に / を機に", "大病を患ったことを契機に、健康的な生活習慣を徹底するようになった。"],
        note: "X serves as a historic milestone initiating lasting change."
      }
    ]
  },

  skmN2EvidentialPerspectiveMatrix: {
    title: "SKM N2: Evidential Evaluation from Nouns Matrix (p. 124)",
    subtitle: "からすると vs から見ると vs からいえば vs からして",
    columns: ["Pattern", "Basis of Judgment", "Speaker's Angle of Vision", "Typical Evaluative Outcomes"],
    rows: [
      {
        label: "〜からすると / からすれば",
        cells: ["Inferred from outward signs, symptoms, or standing in someone else's shoes.", "Judging by the evidence ('Judging by the footsteps, father is home') or from someone's feelings.", "足音からすると、父が帰ってきたようだ。 / 親からすれば、子供は何歳になっても心配だ。", "Forms deductions from sensory clues or empathetic perspective."],
        note: "Evaluation based on clues or someone's perspective."
      },
      {
        label: "〜から見ると / から見れば",
        cells: ["Evaluating external appearance, architectural design, or external third-party viewpoint.", "Viewed from the perspective of an external observer.", "外国人旅行者から見ると、日本の治安の良さは驚嘆に値するだろう。", "Used when evaluating how something appears to an observer."],
        note: "Third-party observation angle."
      },
      {
        label: "〜からいえば / からいって",
        cells: ["Evaluating from one specific isolated dimension (quality, cost, skill, legal terms).", "Speaking strictly in terms of dimension X...", "味からいえば文句なしの名店だが、値段からいえば庶民的とは言えない。", "Limits evaluation strictly to the specified criterion."],
        note: "Speaking strictly from one specific criterion."
      },
      {
        label: "〜からして",
        cells: ["Singling out one prominent representative clue to prove the whole condition is true.", "Judging even from this one single extreme detail, you can easily tell the rest...", "あの店は看板からして怪しい。 / タイトルからして難解そうな論文だ。", "Picks one extreme sample to deduce the nature of the whole entity."],
        note: "One prominent clue indicates the whole nature."
      }
    ]
  },

  skmN2KotoMatrix: {
    title: "SKM N2: The Advanced こと Constructions Matrix (p. 128)",
    subtitle: "ことなく vs ことに(は) vs ことは〜が vs ということだ",
    columns: ["Construction", "Linguistic Meaning & Function", "Connection Formula", "Register & Emotional Nuance"],
    rows: [
      {
        label: "〜ことなく (Formal Continuous Negative)",
        cells: ["Formal written negative: 'Without doing X even once / Without ceasing'.", "動詞辞書形 + ことなく", "彼は困難に直面しても、一度も弱音を吐くことなく前進を続けた。", "High formal equivalent of 〜ないで; elevated literary and essay register."],
        note: "Formal without doing even once."
      },
      {
        label: "〜ことに(は) (Speaker's Emotional Preamble)",
        cells: ["Speaker's emotional preamble: 'To my great emotion / What is remarkable is that...'.", "感情形容詞 / 動詞た形 + ことに", "嬉しいことに、全員が無事に試験に合格した。 / 残念なことに、旅行は雨で中止になった。", "Fronts the speaker's emotional reaction before stating the factual event."],
        note: "Emotional preamble before reporting facts."
      },
      {
        label: "〜ことは〜が (Concessive Qualification)",
        cells: ["Concessive qualification: 'It is true that X, but nevertheless Y'.", "動詞辞書形 + ことは + 同動詞 + が / 形容詞 + ことは + 形容詞 + が", "読めることは読めるが、専門用語が多すぎて意味は分からない。", "Concedes truth of point A before introducing reservations in B."],
        note: "Concedes the first point before qualifying."
      },
      {
        label: "〜ということだ / 〜とのことだ (Authoritative Hearsay)",
        cells: ["Official hearsay quotation ('Reportedly / According to statements'), or summarizing explanation.", "普通形 + ということだ / とのことだ", "気象庁の発表によると、台風は今夜上陸する見込みだとのことだ。", "Frequently paired with information sources (〜によると, 〜の話では)."],
        note: "High formal hearsay reporting."
      }
    ]
  },

  skmN2DoubleNegativesMatrix: {
    title: "SKM N2: Double Negatives & Compelled Action Matrix (p. 146)",
    subtitle: "ないではいられない vs ずにはいられない vs なくはない vs ないわけにはいかない",
    columns: ["Double Negative Formula", "Psychological Drive / Motivation", "Degree of Negation", "Nuance Trap Alert"],
    rows: [
      {
        label: "〜ないではいられない / 〜ずにはいられない",
        cells: ["Irrepressible emotional urge: cannot help but feel / compelled to do by internal urge.", "動詞ない形 + ではいられない / 動詞未然形 + ずにはいられない (する → せずにはいられない)", "悲惨な事故のニュースを聞いて、涙を流さずにはいられなかった。", "Driven by uncontrollable spontaneous emotion from inside."],
        note: "Internal irrepressible urge."
      },
      {
        label: "〜ないわけにはいかない",
        cells: ["Mandatory social responsibility or ethical duty: cannot afford not to do.", "動詞ない形 + わけにはいかない", "恩師に頼まれた以上、この仕事を引き受けないわけにはいかない。", "Driven by external duty, social conscience, or obligation."],
        note: "External moral/social obligation."
      },
      {
        label: "〜なくはない / 〜なくもない",
        cells: ["Cautious double negative understatement: 'It is not entirely impossible that...'.", "動詞ない形 + くはない / 形容詞く + はない", "相手の言い分も理解できなくはないが、全面的に賛同はできない。", "Understatement used to soften disagreement or show reluctant admission."],
        note: "Reluctant admission or softened understatement."
      },
      {
        label: "〜ないものでもない",
        cells: ["Tentative willingness under hypothetical conditions: 'Not entirely out of the question'.", "動詞ない形 + ものでもない", "今すぐ条件を見直していただけるなら、交渉に応じないものでもない。", "Modest theoretical possibility under suitable terms."],
        note: "Hesitant potential concession."
      }
    ]
  },

  skmN2SentenceFinalConstraintsMatrix: {
    title: "SKM N2: Sentence-Ending Constraints & Epistemic Stance Matrix (p. 136)",
    subtitle: "Moral obligation vs strong negative resolve vs conviction vs speaker evaluation.",
    columns: ["Ending Expression", "Core Epistemic Function", "Grammatical & Person Restrictions", "Signature JLPT Example"],
    rows: [
      {
        label: "〜べきだ / べきではない",
        cells: ["General moral duty or common-sense obligation ('Ought to do / Should not do').", "動詞辞書形 + べき (する → すべき / するべき)", "人から親切にされたら、感謝の気持ちを伝えるべきだ。", "Expresses universal social ethics, NOT arbitrary personal orders to a superior."],
        note: "Universal moral obligation."
      },
      {
        label: "〜まい (Negative Resolve / Conjecture)",
        cells: ["1. Strong negative resolve ('Will never do again') 2. Negative conjecture ('Surely will not').", "動詞辞書形 (一段: 辞書/未然) + まい (する → するまい/すまい)", "二度とあのような愚かな過ちは繰り返すまいと誓った。", "First-person for resolve; third-person takes 〜まいと思っている."],
        note: "Resolute refusal or negative conjecture."
      },
      {
        label: "〜に相違ない (にそういない)",
        cells: ["High certainty conviction based on authoritative evidence ('There is no doubt that...').", "普通形 (な-adj である, 名詞である) + に相違ない", "確固たる証拠が見つかった以上、犯人は彼であることに相違ない。", "Formal written equivalent of に違いない; based on logical deduction."],
        note: "Authoritative conviction based on evidence."
      },
      {
        label: "〜にすぎない",
        cells: ["Limiting minimization ('Merely / Nothing more than / Just').", "普通形 / 名詞 + にすぎない", "私は会社の方針に従って業務を遂行したにすぎません。", "Speaker deliberately downsizes the status, scale, or praise of X."],
        note: "Downsizes importance or scale."
      },
      {
        label: "〜にほかならない",
        cells: ["Definitive sole reason or essence ('Nothing other than / Precisely because').", "名詞 + にほかならない", "彼が難関試験に合格できたのは、日々の地道な努力の結果にほかならない。", "Eliminates all other alternative causes; identifies the absolute core truth."],
        note: "Asserts the singular core reason."
      },
      {
        label: "〜かねない vs 〜かねる",
        cells: ["かねない: Negative danger ('Could happen / Risk of...'). かねる: Polite refusal ('Unable to do').", "動詞ます語幹 + かねない / かねる", "過度の過労は重大な病気を引き起こしかねない。 / そのご依頼には応じかねます。", "かねない warns of dangerous consequences; かねる is formal customer-facing refusal."],
        note: "Danger warning vs polite refusal."
      }
    ]
  }
};
