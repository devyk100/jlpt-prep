import type { GrammarPoint } from '../types';
import { MASTER_MUG_UP_TABLES } from './mugUpTables';

export const STREAM_GENKI_POINTS: GrammarPoint[] = [
  {
    id: 'genki1-wa-desu',
    title: 'X は Y です (X is Y / Topic & Copula)',
    meaning: 'X is Y. Establishes X as the conversational topic with は and equates it to predicate Y with です.',
    level: 'N5',
    book: 'Genki I',
    chapter: 'Lesson 1: New Friends',
    streamId: 'stream-topics',
    streamName: 'Topic Framing, Criteria & Disregard',
    connection: 'Noun1 + は + Noun2 / Adjective + です',
    nuance: 'The topic particle は (pronounced "wa") presents the background framework or subject of interest ("speaking of X..."). です acts as the polite non-past copula.',
    keyTakeaway: 'MUG-UP: は marks the topic ("as for X"). Pronounced "wa", written as は.',
    sentences: [
      {
        id: 's-g1-1-1',
        japanese: '私はカリフォルニア大学の留学生です。',
        english: 'I am an international student at the University of California.',
        literal: 'I topic UC\'s international-student am.',
        nuanceNote: 'Standard polite self-introduction formula.',
        tokens: [
          { word: '私', reading: 'わたし', romaji: 'watashi', meaning: 'I / me', pos: 'Pronoun' },
          { word: 'は', reading: 'わ', romaji: 'wa', meaning: 'topic marker', pos: 'Particle' },
          { word: '留学生', reading: 'りゅうがくせい', romaji: 'ryuugakusei', meaning: 'international student', pos: 'Noun' },
          { word: 'です', reading: 'です', romaji: 'desu', meaning: 'am / is (polite copula)', pos: 'Copula' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-g1-1-1',
        question: '田中さん（　　）日本人です。',
        translation: 'Tanaka-san is Japanese.',
        options: ['は', 'を', 'に', 'へ'],
        correctIndex: 0,
        grammarFocus: 'Topic marker は',
        ruleHint: 'Marks Tanaka-san as the topic of the sentence.',
        explanations: [
          { text: 'は', isCorrect: true, reason: 'Correct! は marks Tanaka-san as the topic being identified as Japanese.' },
          { text: 'を', isCorrect: false, reason: 'Incorrect. を marks direct objects of action verbs, not copula topics.' },
          { text: 'に', isCorrect: false, reason: 'Incorrect. に indicates direction, time, or location of existence.' },
          { text: 'へ', isCorrect: false, reason: 'Incorrect. へ indicates direction of movement.' }
        ]
      }
    ],
    tags: ['N5', 'Genki L1', 'Copula', 'Topic']
  },

  {
    id: 'genki1-verb-groups',
    title: '動詞の３分類 (The Three Verb Groups: Ru, U, & Irregular)',
    meaning: 'Japanese verbs are strictly classified into Ru-verbs (一段), U-verbs (五段), and Irregular verbs (する, くる).',
    level: 'N5',
    book: 'Genki I',
    chapter: 'Lesson 3: Making a Date',
    streamId: 'stream-trends',
    streamName: 'Trends, Changes & Proportional Evolution',
    connection: 'Ru-verbs: stem + ます | U-verbs: u-vowel changes to i-vowel + ます | Irregular: する→します, くる→きます',
    nuance: 'Not every verb ending in る is a Ru-verb! Verbs like 帰る (かえる - to return) and 知る (しる - to know) end in る but are 五段 U-verbs (帰ります, 知ります).',
    keyTakeaway: 'MUG-UP: Ru-verbs drop る. U-verbs change final u to i (行く→行きます, 飲む→飲みます).',
    sentences: [
      {
        id: 's-g1-3-1',
        japanese: '毎晩図書館で日本語を勉強します。',
        english: 'I study Japanese in the library every night.',
        literal: 'Every-night library-at Japanese study-do.',
        nuanceNote: '勉強する is an irregular compound verb (勉強します).',
        tokens: [
          { word: '毎晩', reading: 'まいばん', romaji: 'maiban', meaning: 'every night', pos: 'Noun' },
          { word: '図書館', reading: 'としょかん', romaji: 'toshokan', meaning: 'library', pos: 'Noun' },
          { word: 'で', reading: 'で', romaji: 'de', meaning: 'at (action location)', pos: 'Particle' },
          { word: '日本語', reading: 'にほんご', romaji: 'nihongo', meaning: 'Japanese language', pos: 'Noun' },
          { word: 'を', reading: 'を', romaji: 'o', meaning: 'object marker', pos: 'Particle' },
          { word: '勉強します', reading: 'べんきょうします', romaji: 'benkyou shimasu', meaning: 'study (polite)', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-g1-3-1',
        question: '明日友達と映画を（　　）ます。',
        translation: 'I will watch a movie with a friend tomorrow.',
        options: ['見', '見る', '見て', '見ら'],
        correctIndex: 0,
        grammarFocus: 'Ru-verb stem connection to ます',
        ruleHint: '見る is an Ichidan Ru-verb: drop る to form stem 見 + ます.',
        explanations: [
          { text: '見', isCorrect: true, reason: 'Correct! 見る drops る to form 見ます.' },
          { text: '見る', isCorrect: false, reason: 'Incorrect. Cannot retain dictionary る before ます.' },
          { text: '見て', isCorrect: false, reason: 'Incorrect. Te-form cannot attach directly to ます.' },
          { text: '見ら', isCorrect: false, reason: 'Incorrect. 見ら is part of passive/potential, not polite stem.' }
        ]
      }
    ],
    tags: ['N5', 'Genki L3', 'Verbs', 'Conjugation']
  },

  {
    id: 'genki1-te-form',
    title: 'て形 (The Te-Form & Polite Requests 〜てください)',
    meaning: 'The fundamental connective form of Japanese verbs, used for requests (〜てください), permission (〜てもいい), prohibition (〜てはいけない), and sequence.',
    level: 'N5',
    book: 'Genki I',
    chapter: 'Lesson 6: A Day in Robert\'s Life',
    streamId: 'stream-time',
    streamName: 'Chronos & Instant Transitions',
    connection: 'う・つ・る→って | む・ぶ・ぬ→んで | く→いて (行く→行って!) | ぐ→いで | す→して | る(一段)→て',
    nuance: 'CRITICAL EXCEPTION: 行く は「いいて」にならず、「行って」と促音便になります。',
    keyTakeaway: 'MUG-UP: V-て + ください = Please do. Prohibited: V-て + はいけません = Must not.',
    table: MASTER_MUG_UP_TABLES.teFormMatrix,
    sentences: [
      {
        id: 's-g1-6-1',
        japanese: 'すみませんが、窓を開けてください。',
        english: 'Excuse me, but please open the window.',
        literal: 'Excuse-me but, window open please.',
        nuanceNote: '開ける is Ru-verb: stem 開け + て + ください.',
        tokens: [
          { word: '窓', reading: 'まど', romaji: 'mado', meaning: 'window', pos: 'Noun' },
          { word: 'を', reading: 'を', romaji: 'o', meaning: 'object marker', pos: 'Particle' },
          { word: '開けてください', reading: 'あけてください', romaji: 'akete kudasai', meaning: 'please open', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-g1-6-1',
        question: 'ここで写真を（　　）はいけません。撮影禁止です。',
        translation: 'You must not take photos here. Photography is prohibited.',
        options: ['撮って', '撮る', '撮り', '撮った'],
        correctIndex: 0,
        grammarFocus: '〜てはいけません prohibition',
        ruleHint: 'Connects to te-form: 撮る (Group 1 る) -> 撮って.',
        explanations: [
          { text: '撮って', isCorrect: true, reason: 'Correct! 撮る conjugates to 撮って + はいけません for strict prohibition.' },
          { text: '撮る', isCorrect: false, reason: 'Incorrect. Dictionary form cannot connect to はいけません.' },
          { text: '撮り', isCorrect: false, reason: 'Incorrect. Masu-stem cannot connect to はいけません.' },
          { text: '撮った', isCorrect: false, reason: 'Incorrect. Past form cannot connect to はいけません.' }
        ]
      }
    ],
    tags: ['N5', 'Genki L6', 'Te-Form', 'Prohibition']
  },

  {
    id: 'genki1-te-iru',
    title: '〜ている (Actions in Progress vs Resulting Continuous States)',
    meaning: '1) Ongoing action occurring right now (eating, studying). 2) Continuous state resulting from a past change (married, living, knowing).',
    level: 'N5',
    book: 'Genki I',
    chapter: 'Lesson 7: Family Picture',
    streamId: 'stream-time',
    streamName: 'Chronos & Instant Transitions',
    connection: 'V-て + いる / います',
    nuance: 'THE INSTANT VERB TRAP: For puncture verbs like 結婚する (to marry), 知る (to find out), and 住む (to take up residence), 〜ている indicates the RESULTING STATE! 結婚している means "is currently married", NOT "is walking down the aisle right now".',
    keyTakeaway: 'MUG-UP: 知っている = I know. Negative exception: 知りません (NOT 知っていません ❌)!',
    sentences: [
      {
        id: 's-g1-7-1',
        japanese: '姉は東京のIT企業に勤めています。',
        english: 'My older sister is employed at an IT company in Tokyo.',
        literal: 'Older-sister Tokyo IT-company-at employed-state-is.',
        nuanceNote: '勤めている indicates ongoing occupational employment state.',
        tokens: [
          { word: '姉', reading: 'あね', romaji: 'ane', meaning: 'my older sister', pos: 'Noun' },
          { word: 'は', reading: 'わ', romaji: 'wa', meaning: 'topic marker', pos: 'Particle' },
          { word: '東京', reading: 'とうきょう', romaji: 'toukyou', meaning: 'Tokyo', pos: 'Noun' },
          { word: '勤めています', reading: 'つとめています', romaji: 'tsutomete imasu', meaning: 'is employed', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-g1-7-1',
        question: '田中さんの電話番号を（　　）か。「いいえ、知りません。」',
        translation: 'Do you know Tanaka-san\'s phone number? "No, I don\'t know."',
        options: ['知っています', '知ります', '知覚します', '知ってある'],
        correctIndex: 0,
        grammarFocus: '〜ている for state of knowledge',
        ruleHint: 'Knowing a fact is expressed with the state 〜ています.',
        explanations: [
          { text: '知っています', isCorrect: true, reason: 'Correct! State of possessing information requires 知っています.' },
          { text: '知ります', isCorrect: false, reason: 'Incorrect. 知ります means "I will find out in the future".' },
          { text: '知覚します', isCorrect: false, reason: 'Incorrect. Unnatural technical jargon.' },
          { text: '知ってある', isCorrect: false, reason: 'Incorrect. 〜てある is only for deliberate actions on objects.' }
        ]
      }
    ],
    tags: ['N5', 'Genki L7', 'Continuous State']
  },

  {
    id: 'genki1-ndesu',
    title: '〜んです / 〜のだ (The Explanatory Mode)',
    meaning: 'Provides background explanation, clarifies reasons, asks for clarification, or invites empathy: "The thing is... / You see..."',
    level: 'N5',
    book: 'Genki I',
    chapter: 'Lesson 12: Feeling Sick',
    streamId: 'stream-causality',
    streamName: 'Causal Chains & Regret',
    connection: 'Plain form + んです | な-adj / Noun + な + んです (Note the な!)',
    nuance: 'Emotional rapport marker: Without んです, "頭が痛いです" is a dry medical observation. With "頭が痛いんです", it communicates: "The reason I look distressed is that I have a headache; please understand my situation."',
    keyTakeaway: 'MUG-UP: Noun / な-adj + [なんです] (NOT だんです ❌!).',
    sentences: [
      {
        id: 's-g1-12-1',
        japanese: 'どうして遅刻したのですか。「目覚まし時計が鳴らなかったんです。」',
        english: 'Why were you late? "The thing is, my alarm clock didn\'t ring."',
        literal: 'Why late-did? Alarm clock rang-not-explanatory.',
        nuanceNote: 'Explanatory んです provides the empathetic reason for the mishap.',
        tokens: [
          { word: 'どうして', reading: 'どうして', romaji: 'doushite', meaning: 'why', pos: 'Adverb' },
          { word: '遅刻した', reading: 'ちこくした', romaji: 'chikoku shita', meaning: 'was late', pos: 'Verb (Past)' },
          { word: '目覚まし時計', reading: 'めざましどけい', romaji: 'mezamashidokei', meaning: 'alarm clock', pos: 'Noun' },
          { word: '鳴らなかったんです', reading: 'ならなかったんです', romaji: 'naranakattan desu', meaning: 'did not ring (explanatory)', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-g1-12-1',
        question: '明日は大事な試験で（　　）んです。今夜は遊びに行けません。',
        translation: 'The thing is, I have a major exam tomorrow. I cannot go out to play tonight.',
        options: ['忙しい', '忙しだ', '忙しく', '忙しな'],
        correctIndex: 0,
        grammarFocus: 'い-adjective connection to んです',
        ruleHint: 'い-adjectives connect directly without adding anything: 忙しいんです.',
        explanations: [
          { text: '忙しい', isCorrect: true, reason: 'Correct! Plain form 忙しい connects directly to んです.' },
          { text: '忙しだ', isCorrect: false, reason: 'Incorrect. い-adjectives never take だ.' },
          { text: '忙しく', isCorrect: false, reason: 'Incorrect. Adverbial form cannot attach to んです.' },
          { text: '忙しな', isCorrect: false, reason: 'Incorrect. な is only for な-adjectives and nouns.' }
        ]
      }
    ],
    tags: ['N5', 'Genki L12', 'Explanatory', 'Reason']
  },

  {
    id: 'genki2-kanoukei',
    title: '可能形 (Potential Verbs: Ability & Possibility)',
    meaning: 'Expresses that one can do something or that something is possible. Ru-verbs: drop る + られる | U-verbs: u-sound changes to e-sound + る.',
    level: 'N4',
    book: 'Genki II',
    chapter: 'Lesson 13: Looking for a Part-time Job',
    streamId: 'stream-modality',
    streamName: 'Epistemic Certainty, Conviction & Duty',
    connection: 'Ru-verbs: 食べる→食べられる | U-verbs: 行く→行ける, 飲む→飲める, 話す→話せる | Irregular: する→できる, くる→こられる',
    nuance: 'PARTICLE SHIFT TRAP: When a transitive verb converts to potential form, the direct object particle を frequently shifts to が! 日本語を話す → 日本語が話せる (I can speak Japanese).',
    keyTakeaway: 'MUG-UP: U-verbs: u -> e + る (書く→書ける). The object particle を often becomes が!',
    sentences: [
      {
        id: 's-g2-13-1',
        japanese: '漢字が難しくて、新聞をすらすら読むことができません（読めません）。',
        english: 'The kanji are difficult, so I cannot read the newspaper smoothly.',
        literal: 'Kanji difficult-being, newspaper smoothly read cannot.',
        nuanceNote: '読む (U-verb) becomes 読める in potential form (読めません).',
        tokens: [
          { word: '漢字', reading: 'かんじ', romaji: 'kanji', meaning: 'kanji', pos: 'Noun' },
          { word: '新聞', reading: 'しんぶん', romaji: 'shinbun', meaning: 'newspaper', pos: 'Noun' },
          { word: '読めません', reading: 'よめません', romaji: 'yomemasen', meaning: 'cannot read (potential neg)', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-g2-13-1',
        question: '刺身は新鮮ですが、どうしても生魚が（　　）。',
        translation: 'The sashimi is fresh, but I just cannot eat raw fish.',
        options: ['食べられません', '食べません', '食べさせません', '食べてもらえません'],
        correctIndex: 0,
        grammarFocus: '可能形 potential negative',
        ruleHint: 'Eating raw fish is impossible due to personal inability (食べられない).',
        explanations: [
          { text: '食べられません', isCorrect: true, reason: 'Correct! 食べる potential negative is 食べられない / 食べられません.' },
          { text: '食べません', isCorrect: false, reason: 'Incorrect. 食べません is a simple will decision ("I will not eat"), not ability.' },
          { text: '食べさせません', isCorrect: false, reason: 'Incorrect. Causative ("I will not let someone eat").' },
          { text: '食べてもらえません', isCorrect: false, reason: 'Incorrect. Favors pattern ("Cannot get someone to eat").' }
        ]
      }
    ],
    tags: ['N4', 'Genki L13', 'Potential', 'Ability']
  },

  {
    id: 'genki2-te-oku',
    title: '〜ておく / 〜とく (Doing in Advance / Preparatory Action)',
    meaning: 'Performing an action in advance to prepare for future convenience or leaving a state as is for later.',
    level: 'N4',
    book: 'Genki II',
    chapter: 'Lesson 15: A Trip to Nagano',
    streamId: 'stream-time',
    streamName: 'Chronos & Instant Transitions',
    connection: 'V-て + おく (Casual spoken contraction: 〜ておく → 〜とく / 〜でおく → 〜どく)',
    nuance: 'Forward-looking mindset: "I\'ll buy tickets beforehand so we don\'t wait in line" (切符を買っておく). In casual speech, 買っておく becomes 買っとく, 飲んでおく becomes 飲んどく.',
    keyTakeaway: 'MUG-UP: V-て + おく = Action done in advance for future convenience. Contracted: 〜とく.',
    sentences: [
      {
        id: 's-g2-15-1',
        japanese: 'パーティーの前に、部屋を綺麗に掃除しておきます。',
        english: 'Before the party, I will clean up the room nicely in advance.',
        literal: 'Party\'s before, room cleanly clean-up in-advance.',
        nuanceNote: 'Preparatory action executed specifically for the upcoming party.',
        tokens: [
          { word: 'パーティーの前に', reading: 'パーティーのまえに', romaji: 'paatii no mae ni', meaning: 'before the party', pos: 'Noun' },
          { word: '部屋を', reading: 'へやを', romaji: 'heya o', meaning: 'room', pos: 'Noun' },
          { word: '掃除しておきます', reading: 'そうじしておきます', romaji: 'souji shite okimasu', meaning: 'will clean in advance', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-g2-15-1',
        question: '明日から旅行なので、ホテルの予約を（　　）おきました。',
        translation: 'Since I\'m traveling from tomorrow, I made hotel reservations in advance.',
        options: ['して', 'する', 'した', 'し'],
        correctIndex: 0,
        grammarFocus: '〜ておく te-form connection',
        ruleHint: 'Connects to te-form (して).',
        explanations: [
          { text: 'して', isCorrect: true, reason: 'Correct! する becomes して, forming しておきました ("reserved in advance").' },
          { text: 'する', isCorrect: false, reason: 'Incorrect. Dictionary form cannot connect to おく.' },
          { text: 'した', isCorrect: false, reason: 'Incorrect. Past form cannot connect to おく.' },
          { text: 'し', isCorrect: false, reason: 'Incorrect. Masu-stem cannot connect to おく.' }
        ]
      }
    ],
    tags: ['N4', 'Genki L15', 'Advance Action', 'Preparation']
  },

  {
    id: 'genki2-yasui-nikui',
    title: '〜やすい vs 〜にくい (Easy to Do vs Difficult to Do)',
    meaning: 'Evaluates psychological or physical ease/difficulty of an action: 〜やすい (easy to do / prone to), 〜にくい (hard to do / resistant to).',
    level: 'N4',
    book: 'Genki II',
    chapter: 'Lesson 20: Mary Goes Shopping',
    streamId: 'stream-trends',
    streamName: 'Trends, Changes & Proportional Evolution',
    connection: 'V-stem (ます形 without ます) + やすい / にくい (Conjugate as い-adjectives: 〜やすくない, 〜やすかった)',
    nuance: 'Once attached to the verb stem, the compound behaves 100% like a normal い-adjective! Also used for tendencies: このグラスは割れやすい (this glass breaks easily).',
    keyTakeaway: 'MUG-UP: V-stem + やすい (Easy) / にくい (Hard). Functions grammatically as an い-adjective.',
    sentences: [
      {
        id: 's-g2-20-1',
        japanese: 'このペンは握りやすくて、長時間の筆記でも手が疲れません。',
        english: 'This pen is easy to grip, so my hand doesn\'t tire even during long periods of writing.',
        literal: 'This pen grip-easy and, long-time writing even hand tire-not.',
        nuanceNote: 'Physical ergonomic ease (握る stem 握り + やすくて).',
        tokens: [
          { word: 'このペンは', reading: 'このペンは', romaji: 'kono pen wa', meaning: 'this pen', pos: 'Noun' },
          { word: '握りやすくて', reading: 'にぎりやすくて', romaji: 'nigiriyasukute', meaning: 'is easy to grip and', pos: 'Grammar' },
          { word: '手が', reading: 'てが', romaji: 'te ga', meaning: 'hand', pos: 'Noun' },
          { word: '疲れません', reading: 'つかれません', romaji: 'tsukaremasen', meaning: 'does not get tired', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-g2-20-1',
        question: 'この本は字が大きくて、子供にもとても（　　）やすい。',
        translation: 'This book has large print, so it is very easy to read even for children.',
        options: ['読み', '読む', '読ん', '読ま'],
        correctIndex: 0,
        grammarFocus: '〜やすい verb stem connection',
        ruleHint: 'Connects to masu-stem (読みます -> 読み).',
        explanations: [
          { text: '読み', isCorrect: true, reason: 'Correct! 読む stem is 読み, forming 読みやすい ("easy to read").' },
          { text: '読む', isCorrect: false, reason: 'Incorrect. Dictionary form cannot attach to やすい.' },
          { text: '読ん', isCorrect: false, reason: 'Incorrect. Te-stem cannot attach to やすい.' },
          { text: '読ま', isCorrect: false, reason: 'Incorrect. Negative stem cannot attach to やすい.' }
        ]
      }
    ],
    tags: ['N4', 'Genki L20', 'Ease', 'Adjective']
  }
];

