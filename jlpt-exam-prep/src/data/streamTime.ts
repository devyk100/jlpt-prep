import { GrammarPoint } from '../types';
import { MASTER_MUG_UP_TABLES } from './mugUpTables';

export const STREAM_TIME_POINTS: GrammarPoint[] = [
  {
    id: 'gp-toki',
    title: '〜時（とき） (When / At the time of)',
    meaning: 'Indicates the time or relative timing of an action. Focuses on whether action A happens before or after action B.',
    level: 'N5',
    streamId: 'stream-time',
    streamName: 'Chronos & Instant Transitions',
    connection: 'V-辞書形 + 時 (Before doing) / V-た + 時 (After doing) / い形 + 時 / な形 + な時 / N + の時',
    nuance: 'The tense of the verb preceding 時 specifies whether that action is completed BEFORE the main action or still in the FUTURE relative to it. Notice: 出かける時 (when going out = not out yet) vs 出かけた時 (when I had gone out = already outside).',
    keyTakeaway: 'MUG-UP: V-dictionary + 時 = Action has NOT happened yet. V-た + 時 = Action is ALREADY completed.',
    table: MASTER_MUG_UP_TABLES.timeSequenceSpectrum,
    sentences: [
      {
        id: 's-toki-1',
        japanese: '日本へ行く時、新しいカメラを買った。',
        english: 'When I was going to Japan, I bought a new camera.',
        literal: 'Japan toward go time, new camera bought.',
        nuanceNote: 'Notice 行く (dictionary form) is used: The camera was bought in his home country BEFORE departing for Japan!',
        trapAlert: 'If you say 行った時、カメラを買った, you bought the camera AFTER arriving in Japan.',
        tokens: [
          { word: '日本', reading: 'にほん', romaji: 'nihon', meaning: 'Japan', pos: 'Noun' },
          { word: 'へ', reading: 'え', romaji: 'e', meaning: 'toward / to', pos: 'Particle' },
          { word: '行く', reading: 'いく', romaji: 'iku', meaning: 'to go', pos: 'Verb (Dic)' },
          { word: '時', reading: 'とき', romaji: 'toki', meaning: 'when / time', pos: 'Grammar' },
          { word: '新しい', reading: 'あたらしい', romaji: 'atarashii', meaning: 'new', pos: 'I-Adj' },
          { word: 'カメラ', reading: 'カメラ', romaji: 'kamera', meaning: 'camera', pos: 'Noun' },
          { word: 'を', reading: 'を', romaji: 'o', meaning: 'direct object marker', pos: 'Particle' },
          { word: '買った', reading: 'かった', romaji: 'katta', meaning: 'bought', pos: 'Verb (Past)' }
        ]
      },
      {
        id: 's-toki-2',
        japanese: '困った時は、いつでも遠慮なく連絡してください。',
        english: 'When you are in trouble, please contact me anytime without hesitation.',
        literal: 'Troubled time-as-for, anytime hesitation-without contact please.',
        nuanceNote: '困った is past/state: the trouble has already occurred when you reach out.',
        tokens: [
          { word: '困った', reading: 'こまった', romaji: 'komatta', meaning: 'troubled / in trouble', pos: 'Verb (Past)' },
          { word: '時は', reading: 'ときは', romaji: 'toki wa', meaning: 'at the time when', pos: 'Grammar' },
          { word: 'いつでも', reading: 'いつでも', romaji: 'itsudemo', meaning: 'anytime', pos: 'Adverb' },
          { word: '遠慮なく', reading: 'えんりょなく', romaji: 'enryonaku', meaning: 'without hesitation / freely', pos: 'Adverb', nuance: 'Frequently used in polite hospitality.' },
          { word: '連絡して', reading: 'れんらくして', romaji: 'renraku shite', meaning: 'contact / get in touch', pos: 'Verb (Te)' },
          { word: 'ください', reading: 'ください', romaji: 'kudasai', meaning: 'please', pos: 'Auxiliary' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-toki-1',
        question: '出張でアメリカへ（　　）時、空港の免税店でお土産を買った。',
        translation: 'When going to America on a business trip, I bought souvenirs at the airport duty-free shop.',
        options: ['行く', '行った', '行かない', '行けば'],
        correctIndex: 0,
        grammarFocus: '〜時 tense sequencing before departure',
        ruleHint: 'The airport duty-free shop is visited BEFORE departing, so dictionary form 行く is required.',
        explanations: [
          {
            text: '行く',
            isCorrect: true,
            reason: 'Correct! The action of buying souvenirs happens before departure to America, so the non-past dictionary form 行く indicates an uncompleted trip.'
          },
          {
            text: '行った',
            isCorrect: false,
            reason: 'Incorrect. 行った時 would mean you had already completed your arrival in America when buying at the initial departure airport.'
          },
          {
            text: '行かない',
            isCorrect: false,
            reason: 'Incorrect. Negative form contradicts the context of taking the business trip.'
          },
          {
            text: '行けば',
            isCorrect: false,
            reason: 'Incorrect. 行けば is a provisional conditional and cannot directly connect to 時.'
          }
        ]
      }
    ],
    nextPointId: 'gp-nagara',
    prevPointId: undefined,
    tags: ['N5', 'Genki L8', 'Time', 'Conjugation']
  },

  {
    id: 'gp-nagara',
    title: '〜ながら (While doing... simultaneous action)',
    meaning: 'Two actions performed simultaneously by the SAME person. Action B is the primary focus; Action A is secondary.',
    level: 'N4',
    streamId: 'stream-time',
    streamName: 'Chronos & Instant Transitions',
    connection: 'V-stem (ます形 without ます) + ながら',
    nuance: 'Crucial requirement: Both actions MUST be performed by the exact same subject! You cannot say "Father drove while mother slept" with ながら. Furthermore, the main verb comes in the SECOND clause.',
    keyTakeaway: 'MUG-UP: V-stem + ながら. Same subject only. The second clause is the MAIN action.',
    sentences: [
      {
        id: 's-nagara-1',
        japanese: '音楽を聴きながら、毎朝漢字を復習しています。',
        english: 'While listening to music, I review kanji every morning.',
        literal: 'Music listening-while, every-morning kanji review am-doing.',
        nuanceNote: 'Kanji review is the main task; music listening is the secondary background action.',
        tokens: [
          { word: '音楽', reading: 'おんがく', romaji: 'ongaku', meaning: 'music', pos: 'Noun' },
          { word: 'を', reading: 'を', romaji: 'o', meaning: 'object marker', pos: 'Particle' },
          { word: '聴きながら', reading: 'ききながら', romaji: 'kikinagara', meaning: 'while listening', pos: 'Grammar', nuance: 'Stem 聴き + ながら' },
          { word: '毎朝', reading: 'まいあさ', romaji: 'maiasa', meaning: 'every morning', pos: 'Noun' },
          { word: '漢字', reading: 'かんじ', romaji: 'kanji', meaning: 'kanji', pos: 'Noun' },
          { word: 'を', reading: 'を', romaji: 'o', meaning: 'object marker', pos: 'Particle' },
          { word: '復習して', reading: 'ふくしゅうして', romaji: 'fukushuu shite', meaning: 'reviewing', pos: 'Verb (Te)' },
          { word: 'います', reading: 'います', romaji: 'imasu', meaning: 'am / ongoing', pos: 'Auxiliary' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-nagara-1',
        question: '彼はいつもコーヒーを（　　）ながら、仕事のメールをチェックしている。',
        translation: 'He is always checking work emails while drinking coffee.',
        options: ['飲み', '飲む', '飲んで', '飲んだ'],
        correctIndex: 0,
        grammarFocus: '〜ながら verb stem connection',
        ruleHint: 'Attach directly to the polite masu-stem (飲みます -> 飲み).',
        explanations: [
          {
            text: '飲み',
            isCorrect: true,
            reason: 'Correct! 飲む stem is 飲み (飲みます without ます), forming 飲みながら.'
          },
          {
            text: '飲む',
            isCorrect: false,
            reason: 'Incorrect. Dictionary form 飲む cannot attach to ながら.'
          },
          {
            text: '飲んで',
            isCorrect: false,
            reason: 'Incorrect. Te-form 飲んで does not take ながら (that would be redundant/ungrammatical).'
          },
          {
            text: '飲んだ',
            isCorrect: false,
            reason: 'Incorrect. Past form 飲んだ cannot connect to ながら.'
          }
        ]
      }
    ],
    nextPointId: 'gp-uchini',
    prevPointId: 'gp-toki',
    tags: ['N4', 'Genki L17', 'Simultaneous']
  },

  {
    id: 'gp-uchini',
    title: '〜うちに (While... / Before condition changes)',
    meaning: '1) Do something while a favorable condition still lasts. 2) While X was going on, natural change Y spontaneously occurred.',
    level: 'N3',
    streamId: 'stream-time',
    streamName: 'Chronos & Instant Transitions',
    connection: 'V-辞書形 / V-ている / V-ない + うちに | い形 + うちに | な形 + な + うちに | N + の + うちに',
    nuance: 'Unlike あいだ (neutral objective time span), うちに carries a subjective urgency: "If I don\'t do it now, the chance will vanish!" (e.g., while the soup is hot, before forgetting). With spontaneous changes, it marks an unnoticed gradual transition (e.g., while listening to lecture, I fell asleep).',
    keyTakeaway: 'MUG-UP: V-ないうちに = "Before [bad condition] happens!" (e.g. 暗くならないうちに = before it gets dark).',
    sentences: [
      {
        id: 's-uchini-1',
        japanese: 'スープが温かいうちに、早く召し上がってください。',
        english: 'Please eat the soup quickly while it is still warm.',
        literal: 'Soup warm while, quickly enjoy-please.',
        nuanceNote: 'Urgency: Once it gets cold, the optimal state is lost.',
        tokens: [
          { word: 'スープ', reading: 'スープ', romaji: 'suupu', meaning: 'soup', pos: 'Noun' },
          { word: 'が', reading: 'が', romaji: 'ga', meaning: 'subject marker', pos: 'Particle' },
          { word: '温かい', reading: 'あたたかい', romaji: 'atatakai', meaning: 'warm', pos: 'I-Adj' },
          { word: 'うちに', reading: 'うちに', romaji: 'uchini', meaning: 'while still', pos: 'Grammar' },
          { word: '早く', reading: 'はやく', romaji: 'hayaku', meaning: 'quickly / early', pos: 'Adverb' },
          { word: '召し上がって', reading: 'めしあがって', romaji: 'meshiagatte', meaning: 'eat / drink (honorific)', pos: 'Keigo Verb' },
          { word: 'ください', reading: 'ください', romaji: 'kudasai', meaning: 'please', pos: 'Auxiliary' }
        ]
      },
      {
        id: 's-uchini-2',
        japanese: '雨が降らないうちに、急いで洗濯物を取り込もう。',
        english: 'Let\'s hurry and bring in the laundry before it starts raining.',
        literal: 'Rain fall-not while, hurrying laundry take-in-volitional.',
        nuanceNote: '降らないうちに literally translates as "while it is not raining", which functionally means "before it starts raining".',
        tokens: [
          { word: '雨', reading: 'あめ', romaji: 'ame', meaning: 'rain', pos: 'Noun' },
          { word: 'が', reading: 'が', romaji: 'ga', meaning: 'subject marker', pos: 'Particle' },
          { word: '降らない', reading: 'ふらない', romaji: 'furanai', meaning: 'does not fall', pos: 'Verb (Neg)' },
          { word: 'うちに', reading: 'うちに', romaji: 'uchini', meaning: 'before / while not', pos: 'Grammar' },
          { word: '急いで', reading: 'いそいで', romaji: 'isoide', meaning: 'hurriedly', pos: 'Adverb' },
          { word: '洗濯物', reading: 'せんたくもの', romaji: 'sentakumono', meaning: 'laundry', pos: 'Noun' },
          { word: 'を', reading: 'を', romaji: 'o', meaning: 'object marker', pos: 'Particle' },
          { word: '取り込もう', reading: 'とりこもう', romaji: 'torikomou', meaning: 'let us bring in', pos: 'Verb (Volitional)' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-uchini-1',
        question: '忘れない（　　）、先生が言った重要事項をメモしておいた。',
        translation: 'Before I forget, I took notes on the important points the teacher mentioned.',
        options: ['うちに', '最中に', '次第', 'つつ'],
        correctIndex: 0,
        grammarFocus: '〜ないうちに (before [undesirable change] happens)',
        ruleHint: 'V-ないうちに is the classic pattern meaning "before X happens".',
        explanations: [
          {
            text: 'うちに',
            isCorrect: true,
            reason: 'Correct! 忘れないうちに means "while I haven\'t forgotten = before I forget". Perfect fit.'
          },
          {
            text: '最中に',
            isCorrect: false,
            reason: 'Incorrect. 最中に means "right in the middle of doing an active process" and cannot connect to negative 忘れない.'
          },
          {
            text: '次第',
            isCorrect: false,
            reason: 'Incorrect. 次第 attaches to verb stems to mean "as soon as (future)", not negative states.'
          },
          {
            text: 'つつ',
            isCorrect: false,
            reason: 'Incorrect. つつ attaches to verb stems for formal simultaneous action ("while doing").'
          }
        ]
      }
    ],
    nextPointId: 'gp-saichuu',
    prevPointId: 'gp-nagara',
    tags: ['N3', 'SKM N3 Ch1', 'Urgency', 'Time']
  },

  {
    id: 'gp-saichuu',
    title: '〜最中に（さいちゅうに） (Right in the middle of... disrupted!)',
    meaning: 'Right in the middle of doing an ongoing action, an unexpected outside event suddenly occurs that interrupts or causes trouble.',
    level: 'N3',
    streamId: 'stream-time',
    streamName: 'Chronos & Instant Transitions',
    connection: 'V-ている + 最中に / N + の最中に',
    nuance: 'Always implies an interruption or nuisance! The second clause MUST describe a sudden, unplanned event (e.g. earthquake struck, phone rang, power went out). You CANNOT use it for intentional planned steps.',
    keyTakeaway: 'MUG-UP: V-ている最中に + [sudden interruption]. Never use with planned volitional actions.',
    sentences: [
      {
        id: 's-saichuu-1',
        japanese: '大切な会議の最中に、スマートフォンの着信音が鳴り響いて焦った。',
        english: 'Right in the middle of an important meeting, my smartphone ringtone rang loudly and I panicked.',
        literal: 'Important meeting\'s midst-in, smartphone ringtone echoed and panicked.',
        nuanceNote: 'Notice the sudden embarrassing disruption (ringtone sounding during a meeting).',
        tokens: [
          { word: '大切な', reading: 'たいせつな', romaji: 'taisetsuna', meaning: 'important', pos: 'Na-Adj' },
          { word: '会議', reading: 'かいぎ', romaji: 'kaigi', meaning: 'meeting / conference', pos: 'Noun' },
          { word: 'の最中に', reading: 'のさいちゅうに', romaji: 'no saichuu ni', meaning: 'right in the middle of', pos: 'Grammar' },
          { word: 'スマートフォン', reading: 'スマートフォン', romaji: 'sumaatofon', meaning: 'smartphone', pos: 'Noun' },
          { word: 'の', reading: 'の', romaji: 'no', meaning: 'possessive', pos: 'Particle' },
          { word: '着信音', reading: 'ちゃくしんおん', romaji: 'chakushin\'on', meaning: 'ringtone', pos: 'Noun' },
          { word: 'が', reading: 'が', romaji: 'ga', meaning: 'subject marker', pos: 'Particle' },
          { word: '鳴り響いて', reading: 'なりひびいて', romaji: 'narihibiite', meaning: 'rang loudly / resonated', pos: 'Verb (Te)' },
          { word: '焦った', reading: 'あせった', romaji: 'asetta', meaning: 'panicked / flustered', pos: 'Verb (Past)' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-saichuu-1',
        question: 'シャワーを（　　）最中に、突然停電になって真っ暗になった。',
        translation: 'Right in the middle of taking a shower, the power suddenly went out and it became pitch dark.',
        options: ['浴びている', '浴びた', '浴びる', '浴びようとする'],
        correctIndex: 0,
        grammarFocus: '〜最中に connection to ongoing action',
        ruleHint: '最中に requires an active continuous action: V-ている.',
        explanations: [
          {
            text: '浴びている',
            isCorrect: true,
            reason: 'Correct! V-ている form represents the ongoing state that gets disrupted by the sudden blackout.'
          },
          {
            text: '浴びた',
            isCorrect: false,
            reason: 'Incorrect. 浴びた is past completed form. You cannot be in the middle of an action that is already finished.'
          },
          {
            text: '浴びる',
            isCorrect: false,
            reason: 'Incorrect. Dictionary form 浴びる cannot attach directly to 最中に.'
          },
          {
            text: '浴びようとする',
            isCorrect: false,
            reason: 'Incorrect. 浴びようとする means "about to take a shower", which doesn\'t match the ongoing action meaning of 最中.'
          }
        ]
      }
    ],
    nextPointId: 'gp-totan',
    prevPointId: 'gp-uchini',
    tags: ['N3', 'SKM N3 Ch1', 'Interruption']
  },

  {
    id: 'gp-totan',
    title: '〜たとたん（に） (The moment that... sudden surprise)',
    meaning: 'The instant action A took place, unexpected event B immediately occurred.',
    level: 'N3',
    streamId: 'stream-time',
    streamName: 'Chronos & Instant Transitions',
    connection: 'V-た + とたん（に）',
    nuance: 'Crucial JLPT rule: Clause B is ALWAYS a surprise or natural reflexive reaction! It CANNOT be a planned, intentional, or volitional command (e.g. you CANNOT say "窓を開けたとたん、掃除してください" ❌).',
    keyTakeaway: 'MUG-UP: V-た + とたんに + [UNEXPECTED event]. Zero speaker volition allowed.',
    sentences: [
      {
        id: 's-totan-1',
        japanese: '立ち上がったとたんに、激しいめまいがして倒れそうになった。',
        english: 'The moment I stood up, I felt severe dizziness and almost collapsed.',
        literal: 'Stood-up moment-at, severe dizziness did and almost-fell became.',
        nuanceNote: 'A classic physiological surprise reaction: instant trigger -> involuntary reaction.',
        tokens: [
          { word: '立ち上がった', reading: 'たちあがった', romaji: 'tachiagatta', meaning: 'stood up', pos: 'Verb (Past)' },
          { word: 'とたんに', reading: 'とたんに', romaji: 'totan ni', meaning: 'the moment that', pos: 'Grammar' },
          { word: '激しい', reading: 'はげしい', romaji: 'hageshii', meaning: 'intense / severe', pos: 'I-Adj' },
          { word: 'めまい', reading: 'めまい', romaji: 'memai', meaning: 'dizziness', pos: 'Noun' },
          { word: 'がして', reading: 'がして', romaji: 'ga shite', meaning: 'felt / occurred', pos: 'Verb (Te)' },
          { word: '倒れそうに', reading: 'たおれそうに', romaji: 'taoresou ni', meaning: 'on the verge of collapsing', pos: 'Adverb' },
          { word: 'なった', reading: 'なった', romaji: 'natta', meaning: 'became', pos: 'Verb (Past)' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-totan-1',
        question: '薬を（　　）とたん、猛烈な眠気に襲われてベッドに倒れ込んだ。',
        translation: 'The moment I took the medicine, I was struck by violent drowsiness and collapsed into bed.',
        options: ['飲んだ', '飲む', '飲んでいる', '飲もうと'],
        correctIndex: 0,
        grammarFocus: '〜たとたん verb form restriction',
        ruleHint: 'とたん strictly requires the past (た) form of the preceding action.',
        explanations: [
          {
            text: '飲んだ',
            isCorrect: true,
            reason: 'Correct! V-た + とたん forms 飲んだとたん ("the moment after I swallowed it").'
          },
          {
            text: '飲む',
            isCorrect: false,
            reason: 'Incorrect. Dictionary form 飲む cannot attach to とたん.'
          },
          {
            text: '飲んでいる',
            isCorrect: false,
            reason: 'Incorrect. Continuous form 飲んでいる cannot attach to とたん (that would be 最中).'
          },
          {
            text: '飲もうと',
            isCorrect: false,
            reason: 'Incorrect. Volitional form 飲もう does not connect to とたん.'
          }
        ]
      }
    ],
    nextPointId: 'gp-kato-omou-to',
    prevPointId: 'gp-saichuu',
    tags: ['N3', 'SKM N3 Ch1', 'Surprise', 'Instant']
  },

  {
    id: 'gp-kato-omou-to',
    title: '〜（か）と思うと / 〜かと思ったら (No sooner had... when suddenly!)',
    meaning: 'No sooner had X happened than event Y immediately followed, presenting a striking or contradictory change.',
    level: 'N2',
    streamId: 'stream-time',
    streamName: 'Chronos & Instant Transitions',
    connection: 'V-た + （か）と思うと / 〜かと思ったら',
    nuance: 'Expresses the speaker\'s astonishment at a rapid transition or contradictory shift. Often describes weather, crying/laughing children, or rapid departures. Cannot describe the speaker\'s own planned deliberate action!',
    keyTakeaway: 'MUG-UP: V-た + かと思うと = "Just when you thought it finished, BAM! Complete opposite/sudden change."',
    sentences: [
      {
        id: 's-kato-1',
        japanese: '赤ちゃんはさっきまで泣いていたかと思うと、もうすやすや眠っている。',
        english: 'Just when I thought the baby was crying until a moment ago, she is already sleeping peacefully.',
        literal: 'Baby until-moment-ago crying-was thought-if, already peacefully sleeping.',
        nuanceNote: 'Contrasting swift change in state: crying -> sound asleep in an instant.',
        tokens: [
          { word: '赤ちゃん', reading: 'あかちゃん', romaji: 'akachan', meaning: 'baby', pos: 'Noun' },
          { word: 'は', reading: 'は', romaji: 'wa', meaning: 'topic marker', pos: 'Particle' },
          { word: 'さっきまで', reading: 'さっきまで', romaji: 'sakki made', meaning: 'until just a moment ago', pos: 'Adverb' },
          { word: '泣いていた', reading: 'ないていた', romaji: 'naite ita', meaning: 'was crying', pos: 'Verb (Past)' },
          { word: 'かと思うと', reading: 'かとおもうと', romaji: 'ka to omou to', meaning: 'no sooner than / just when thought', pos: 'Grammar' },
          { word: 'もう', reading: 'もう', romaji: 'mou', meaning: 'already', pos: 'Adverb' },
          { word: 'すやすや', reading: 'すやすや', romaji: 'suyasuya', meaning: 'peacefully (sleeping)', pos: 'Onomatopoeia' },
          { word: '眠っている', reading: 'ねむっている', romaji: 'nemutte iru', meaning: 'sleeping', pos: 'Verb (Prog)' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-kato-1',
        question: '空が急に暗くなった（　　）、雷とともに大粒の雨が降ってきた。',
        translation: 'No sooner had the sky suddenly darkened than large drops of rain came pouring down with thunder.',
        options: ['かと思うと', '次第', 'ながら', '一方だ'],
        correctIndex: 0,
        grammarFocus: '〜かと思うと sudden rapid weather shift',
        ruleHint: 'Describes rapid, astonishing shifts in nature or other people\'s behavior.',
        explanations: [
          {
            text: 'かと思うと',
            isCorrect: true,
            reason: 'Correct! V-た + かと思うと captures the astonishingly fast transition from darkening sky to downpour.'
          },
          {
            text: '次第',
            isCorrect: false,
            reason: 'Incorrect. 次第 attaches to verb stems to mean "as soon as (business future)", not past weather observations.'
          },
          {
            text: 'ながら',
            isCorrect: false,
            reason: 'Incorrect. ながら requires verb stem and indicates simultaneous actions by the same agent.'
          },
          {
            text: '一方だ',
            isCorrect: false,
            reason: 'Incorrect. 一方だ means "keeps trending in one continuous direction", not an instantaneous occurrence.'
          }
        ]
      }
    ],
    nextPointId: 'gp-kanai-ka',
    prevPointId: 'gp-totan',
    tags: ['N2', 'SKM N2 Ch1', 'Rapid Transition']
  },

  {
    id: 'gp-kanai-ka',
    title: '〜か〜ないかのうちに (On the very verge of... / Barely finished when)',
    meaning: 'Describes an event occurring with virtually ZERO time interval—so fast that you cannot even tell if the first action finished.',
    level: 'N2',
    streamId: 'stream-time',
    streamName: 'Chronos & Instant Transitions',
    connection: 'V-辞書形 / V-た + か + V-ない + かのうちに (The two verbs are the EXACT same verb!)',
    nuance: 'The ultimate Japanese expression for split-second succession. Uses the same verb twice: 終わるか終わらないかのうちに ("in the space between whether it ended or didn\'t end"). Highly literary and dramatic.',
    keyTakeaway: 'MUG-UP: [Verb] + か + [Verb-ない] + かのうちに. Identical verb in affirmative and negative.',
    sentences: [
      {
        id: 's-kanai-1',
        japanese: '授業終了のチャイムが鳴り終わるか終わらないかのうちに、生徒たちは教室を飛び出した。',
        english: 'Hardly had the class chime finished ringing when the students dashed out of the classroom.',
        literal: 'Class finish chime ring-finish or ring-finish-not interval-in, students classroom dashed-out.',
        nuanceNote: 'Notice the extreme immediacy: chime was barely fading and students were already running.',
        tokens: [
          { word: '授業終了', reading: 'じゅぎょうしゅうりょう', romaji: 'jugyou shuuryou', meaning: 'end of class', pos: 'Noun' },
          { word: 'の', reading: 'の', romaji: 'no', meaning: 'possessive', pos: 'Particle' },
          { word: 'チャイム', reading: 'チャイム', romaji: 'chaimu', meaning: 'chime / bell', pos: 'Noun' },
          { word: 'が', reading: 'が', romaji: 'ga', meaning: 'subject marker', pos: 'Particle' },
          { word: '鳴り終わるか終わらないかのうちに', reading: 'なりおわるかおわらないかのうちに', romaji: 'nariowaru ka owaranai ka no uchi ni', meaning: 'hardly had finished ringing when', pos: 'Grammar' },
          { word: '生徒たち', reading: 'せいとたち', romaji: 'seitotachi', meaning: 'students', pos: 'Noun' },
          { word: 'は', reading: 'は', romaji: 'wa', meaning: 'topic marker', pos: 'Particle' },
          { word: '教室', reading: 'きょうしつ', romaji: 'kyoushitsu', meaning: 'classroom', pos: 'Noun' },
          { word: 'を', reading: 'を', romaji: 'o', meaning: 'separation marker', pos: 'Particle' },
          { word: '飛び出した', reading: 'とびだした', romaji: 'tobidashita', meaning: 'dashed out', pos: 'Verb (Past)' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-kanai-1',
        question: '布団に横たわるか（　　）かのうちに、深い眠りに落ちてしまった。',
        translation: 'Hardly had I laid down on the futon when I fell into a deep sleep.',
        options: ['横たわらない', '横たわった', '横たわり', '横たわる'],
        correctIndex: 0,
        grammarFocus: '〜か〜ないかのうちに parallel verb pattern',
        ruleHint: 'The second verb must be the negative form of the same verb (横たわらない).',
        explanations: [
          {
            text: '横たわらない',
            isCorrect: true,
            reason: 'Correct! The formula is V-辞書形 (横たわる) + か + V-ない (横たわらない) + かのうちに.'
          },
          {
            text: '横たわった',
            isCorrect: false,
            reason: 'Incorrect. The second slot requires the negative form, not past affirmative.'
          },
          {
            text: '横たわり',
            isCorrect: false,
            reason: 'Incorrect. Masu-stem cannot be placed in the negative slot.'
          },
          {
            text: '横たわる',
            isCorrect: false,
            reason: 'Incorrect. You cannot duplicate the affirmative form without negative contrast.'
          }
        ]
      }
    ],
    nextPointId: 'gp-shidai',
    prevPointId: 'gp-kato-omou-to',
    tags: ['N2', 'SKM N2 Ch1', 'Split Second', 'Literary']
  },

  {
    id: 'gp-shidai',
    title: '〜次第（しだい） (As soon as... business resolve)',
    meaning: 'As soon as action A is completed or verified in the future, action B will immediately be executed.',
    level: 'N2',
    streamId: 'stream-time',
    streamName: 'Chronos & Instant Transitions',
    connection: 'V-stem (ます形 without ます) + 次第',
    nuance: 'Essential business Japanese! The main clause expresses the speaker\'s intentional future action, commitment, or request. CRITICAL JLPT TRAP: The main clause can NEVER be in the past tense (た)! If it\'s already in the past, use 〜たら or 〜とたん.',
    keyTakeaway: 'MUG-UP: V-stem + 次第 + [FUTURE resolve/request]. Never past tense!',
    sentences: [
      {
        id: 's-shidai-1',
        japanese: '詳しい日程が決まり次第、担当者よりメールにてご連絡いたします。',
        english: 'As soon as the detailed schedule is finalized, our representative will contact you via email.',
        literal: 'Detailed schedule decide-as-soon-as, person-in-charge from email via contact will-do.',
        nuanceNote: 'Polite business commitment regarding a future milestone.',
        tokens: [
          { word: '詳しい', reading: 'くわしい', romaji: 'kuwashii', meaning: 'detailed', pos: 'I-Adj' },
          { word: '日程', reading: 'にってい', romaji: 'nittei', meaning: 'schedule / agenda', pos: 'Noun' },
          { word: 'が', reading: 'が', romaji: 'ga', meaning: 'subject marker', pos: 'Particle' },
          { word: '決まり次第', reading: 'きまりしだい', romaji: 'kimari shidai', meaning: 'as soon as decided', pos: 'Grammar', nuance: 'Stem 決まり + 次第' },
          { word: '担当者', reading: 'たんとうしゃ', romaji: 'tantousha', meaning: 'person in charge', pos: 'Noun' },
          { word: 'より', reading: 'より', romaji: 'yori', meaning: 'from (formal)', pos: 'Particle' },
          { word: 'メールにて', reading: 'メールにて', romaji: 'meeru ni te', meaning: 'via email (business)', pos: 'Particle' },
          { word: 'ご連絡いたします', reading: 'ごれんらくいたします', romaji: 'gorenraku itashimasu', meaning: 'will contact (humble)', pos: 'Keigo Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-shidai-1',
        question: 'パスポートの準備が（　　）次第、旅行会社に書類を提出してください。',
        translation: 'As soon as your passport preparation is complete, please submit the documents to the travel agency.',
        options: ['でき', 'できる', 'できた', 'できている'],
        correctIndex: 0,
        grammarFocus: '〜次第 verb stem connection',
        ruleHint: 'Connects to the masu-stem of the verb (できます -> でき).',
        explanations: [
          {
            text: 'でき',
            isCorrect: true,
            reason: 'Correct! できる stem is でき (できます without ます), forming でき次第.'
          },
          {
            text: 'できる',
            isCorrect: false,
            reason: 'Incorrect. Dictionary form cannot attach directly to 次第 in this time pattern.'
          },
          {
            text: 'できた',
            isCorrect: false,
            reason: 'Incorrect. Past form できた cannot attach to 次第.'
          },
          {
            text: 'できている',
            isCorrect: false,
            reason: 'Incorrect. Progressive form does not attach to 次第.'
          }
        ]
      }
    ],
    nextPointId: undefined,
    prevPointId: 'gp-kanai-ka',
    tags: ['N2', 'SKM N2 Ch3', 'Business', 'Future Commitment']
  }
];

