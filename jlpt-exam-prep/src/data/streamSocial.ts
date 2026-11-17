import { GrammarPoint } from '../types';
import { MASTER_MUG_UP_TABLES } from './mugUpTables';

export const STREAM_SOCIAL_POINTS: GrammarPoint[] = [
  {
    id: 'gp-giving-receiving',
    title: 'Giving & Receiving Triad: あげる vs くれる vs もらう (+ て-forms)',
    meaning: 'Tracking favors and social debt. 〜てあげる: I/insider do favor outward. 〜てくれる: Outside person kindly does favor inward to me. 〜てもらう: I humbly receive/benefit from another\'s favor.',
    level: 'N4',
    streamId: 'stream-social',
    streamName: 'Social Transactions, Hierarchy & Favors',
    connection: 'V-て + あげる / くれる / もらう (Humble: 差し上げる, いただく | Honorific: くださる)',
    nuance: 'THE DEFINITIVE JLPT TRAP: The grammatical subject changes completely! In [X が 私に 〜てくれた], X is the subject. In [私 は X に 〜てもらった], "私" is the subject! Notice how using 〜てあげる directly to a teacher or boss sounds arrogant; use 〜て差し上げます or avoid entirely.',
    keyTakeaway: 'MUG-UP: [Giver が 私に くれた] vs [私 は Giver に もらった]. Direction of gratitude!',
    table: MASTER_MUG_UP_TABLES.givingReceivingMatrix,
    sentences: [
      {
        id: 's-give-1',
        japanese: '雨で濡れていた私に、親切な見知らぬ人が傘を貸してくれた。',
        english: 'A kind stranger lent an umbrella to me, who was getting drenched in the rain.',
        literal: 'Rain-by drenched-was me-to, kind stranger umbrella lent-gave.',
        nuanceNote: 'The stranger is the actor/giver; the favor flowed inward to the grateful speaker (私に〜てくれた).',
        tokens: [
          { word: '雨で', reading: 'あめで', romaji: 'ame de', meaning: 'by rain', pos: 'Noun' },
          { word: '濡れていた', reading: 'ぬれていた', romaji: 'nurete ita', meaning: 'was getting drenched', pos: 'Verb' },
          { word: '私に', reading: 'わたしに', romaji: 'watashi ni', meaning: 'to me (recipient)', pos: 'Pronoun' },
          { word: '親切な', reading: 'しんせつな', romaji: 'shinsetsuna', meaning: 'kind', pos: 'Na-Adj' },
          { word: '見知らぬ人が', reading: 'みしらぬひとが', romaji: 'mishiranu hito ga', meaning: 'stranger (giver)', pos: 'Noun' },
          { word: '傘を', reading: 'かさを', romaji: 'kasa o', meaning: 'umbrella', pos: 'Noun' },
          { word: '貸してくれた', reading: 'かしてくれた', romaji: 'kashite kureta', meaning: 'kindly lent to me', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-give-1',
        question: '日本語の文法が分からなかったので、田中先生に（　　）。',
        translation: 'Because I didn\'t understand Japanese grammar, I got Tanaka-sensei to explain it to me.',
        options: ['説明していただいた', '説明してくださった', '説明してあげた', '説明してやった'],
        correctIndex: 0,
        grammarFocus: '〜てもらう / いただく with subject as recipient',
        ruleHint: '田中先生 is marked with particle に, indicating the source from whom the speaker received the favor.',
        explanations: [
          {
            text: '説明していただいた',
            isCorrect: true,
            reason: 'Correct! 「先生に説明していただいた」 (I humbly received an explanation from teacher) correctly matches the particle に marking the teacher.'
          },
          {
            text: '説明してくださった',
            isCorrect: false,
            reason: 'Incorrect. If using くださった, the teacher must be the subject marked by が: 田中先生が説明してくださった.'
          },
          {
            text: '説明してあげた',
            isCorrect: false,
            reason: 'Incorrect. あげた means YOU explained it to the teacher, which is arrogant and contextually upside down.'
          },
          {
            text: '説明してやった',
            isCorrect: false,
            reason: 'Incorrect. やった is condescending, used only for pets or watering plants.'
          }
        ]
      }
    ],
    nextPointId: 'gp-voice-ladder',
    prevPointId: undefined,
    tags: ['N4', 'Genki L14', 'Genki L16', 'Giving and Receiving']
  },

  {
    id: 'gp-voice-ladder',
    title: 'The Voice Transformation Ladder: Passive (受身) → Causative (使役) → Causative-Passive (使役受身)',
    meaning: '1) 受身: Action received / Suffering passive (雨に降られた). 2) 使役: Make or let someone do (子供に野菜を食べさせる). 3) 使役受身: Forced to do against one\'s own will (無理やり酒を飲まされた).',
    level: 'N4',
    streamId: 'stream-social',
    streamName: 'Social Transactions, Hierarchy & Favors',
    connection: '受身: あ-stem + れる / られる | 使役: あ-stem + せる / させる | 使役受身: あ-stem + される (Contracted) / させられる',
    nuance: 'THE SUFFERING PASSIVE (迷惑受身): Japanese uses passive voice when someone suffers from an uncontrollable external event: 電車の中で足を踏まれた (someone stepped on my foot), 泥棒に財布を盗まれた (my wallet was stolen by a thief). In CAUSATIVE-PASSIVE (使役受身), you are forced to endure something: ３時間も立たされた (I was made to stand for 3 whole hours!).',
    keyTakeaway: 'MUG-UP: [あ-stem + される / させられる] = "I was forced to do it against my will!"',
    table: MASTER_MUG_UP_TABLES.voiceMatrix,
    sentences: [
      {
        id: 's-voice-1',
        japanese: '新入社員の歓迎会で、先輩たちに無理やり歌を歌わされた。',
        english: 'At the new employee welcome party, I was forced by the senior staff to sing a song against my will.',
        literal: 'New-employee welcome-party-at, seniors-by by-force song sing-forced-was.',
        nuanceNote: 'Causative-Passive: The speaker had no desire to sing, but social coercion forced them.',
        tokens: [
          { word: '新入社員の', reading: 'しんにゅうしゃいんの', romaji: 'shinnyuu shain no', meaning: 'new employee\'s', pos: 'Noun' },
          { word: '歓迎会で', reading: 'かんげいかいで', romaji: 'kangeikai de', meaning: 'at welcome party', pos: 'Noun' },
          { word: '先輩たちに', reading: 'せんぱいたちに', romaji: 'senpaitachi ni', meaning: 'by the seniors', pos: 'Noun' },
          { word: '無理やり', reading: 'むりやり', romaji: 'muriyari', meaning: 'forcibly / against will', pos: 'Adverb' },
          { word: '歌を', reading: 'うたを', romaji: 'uta o', meaning: 'song', pos: 'Noun' },
          { word: '歌わされた', reading: 'うたわされた', romaji: 'utawasareta', meaning: 'was forced to sing (causative-passive)', pos: 'Grammar', nuance: '歌う (Group 1) -> 歌わされる' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-voice-1',
        question: '子供の頃、母親に毎日２時間もピアノを（　　）、本当に嫌だった。',
        translation: 'When I was a child, I was forced by my mother to practice piano for two hours every day; I truly hated it.',
        options: ['練習させられて', '練習させて', '練習していただいて', '練習されて'],
        correctIndex: 0,
        grammarFocus: '使役受身 causative-passive expressing coercion',
        ruleHint: 'Mother (母親に) forced the child, who felt bitter grievance (嫌だった).',
        explanations: [
          {
            text: '練習させられて',
            isCorrect: true,
            reason: 'Correct! 練習させられる (Causative-Passive) captures being forced to practice against one\'s desire.'
          },
          {
            text: '練習させて',
            isCorrect: false,
            reason: 'Incorrect. 練習させて is active causative ("I made my mother practice"), which is absurd.'
          },
          {
            text: '練習していただいて',
            isCorrect: false,
            reason: 'Incorrect. いただいて implies profound gratitude, directly contradicting "I truly hated it (嫌だった)".'
          },
          {
            text: '練習されて',
            isCorrect: false,
            reason: 'Incorrect. Simple passive doesn\'t convey the sense of being compelled to perform the action.'
          }
        ]
      }
    ],
    nextPointId: 'gp-keigo-core',
    prevPointId: 'gp-giving-receiving',
    tags: ['N4', 'Genki L21', 'Genki L22', 'Passive', 'Causative', 'Causative-Passive']
  },

  {
    id: 'gp-keigo-core',
    title: 'Keigo (敬語) Survival: Sonkeigo (尊敬語) vs Kenjougo (謙譲語)',
    meaning: 'Respectful speech elevating the listener/other person (尊敬語) vs Humble speech lowering yourself and your in-group (謙譲語).',
    level: 'N4',
    streamId: 'stream-social',
    streamName: 'Social Transactions, Hierarchy & Favors',
    connection: '尊敬: いらっしゃる, おっしゃる, 召し上がる, ご覧になる | 謙譲: 参る, 申す, いただく, 拝見する, 致す',
    nuance: 'THE IN-GROUP / OUT-GROUP TEST TRAP: When talking to a client about your own boss, your boss is in your IN-GROUP! Therefore, you must use KENJOUGO (humble) for your own boss: "部長の田中は席を外しております" (NOT いらっしゃいません ❌). Never honor yourself or your own company when speaking to outsiders.',
    keyTakeaway: 'MUG-UP: Other person = 尊敬語 (ご存知、おっしゃる). Speaker / In-Group = 謙譲語 (存じる、申す).',
    table: MASTER_MUG_UP_TABLES.keigoMatrix,
    sentences: [
      {
        id: 's-keigo-1',
        japanese: '昨日お送りいただいた企画書を、先ほど拝見いたしました。',
        english: 'I have just reviewed the proposal document that you kindly sent yesterday.',
        literal: 'Yesterday send-receive proposal, just-now humbly-inspected.',
        nuanceNote: 'Masterful business keigo: いただいた (honors client\'s sending) + 拝見いたしました (humbles speaker\'s reading).',
        tokens: [
          { word: '昨日', reading: 'きのう', romaji: 'kinou', meaning: 'yesterday', pos: 'Noun' },
          { word: 'お送りいただいた', reading: 'おおくりいただいた', romaji: 'o-okuri itadaita', meaning: 'you kindly sent (honorific favor)', pos: 'Keigo Verb' },
          { word: '企画書を', reading: 'きかくしょを', romaji: 'kikakusho o', meaning: 'proposal document', pos: 'Noun' },
          { word: '先ほど', reading: 'さきほど', romaji: 'sakihodo', meaning: 'a short while ago (formal)', pos: 'Adverb' },
          { word: '拝見いたしました', reading: 'はいけんいたしました', romaji: 'haiken itashimashita', meaning: 'humbly reviewed / inspected', pos: 'Keigo Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-keigo-1',
        question: '（電話で）「恐れ入りますが、鈴木社長は（　　）でしょうか。」',
        translation: '(On the phone) "Excuse me, is President Suzuki in at the moment?"',
        options: ['いらっしゃいます', '参られます', 'おられます', '申されます'],
        correctIndex: 0,
        grammarFocus: '尊敬語 honorific inquiry about superior\'s presence',
        ruleHint: 'Asking if the other company\'s president is present requires 尊敬語 (いらっしゃる).',
        explanations: [
          {
            text: 'いらっしゃいます',
            isCorrect: true,
            reason: 'Correct! 「いらっしゃいます」 is the honorific (尊敬語) form of います / 来ます, appropriately elevating the president.'
          },
          {
            text: '参られます',
            isCorrect: false,
            reason: 'Incorrect. 参る is humble (謙譲語) and cannot be used for the other party.'
          },
          {
            text: 'おられます',
            isCorrect: false,
            reason: 'Incorrect. おる is humble and inappropriate for asking about a client/partner president.'
          },
          {
            text: '申されます',
            isCorrect: false,
            reason: 'Incorrect. 申す means "to say (humble)", not "to be present".'
          }
        ]
      }
    ],
    nextPointId: 'gp-tamaranai-naranai',
    prevPointId: 'gp-voice-ladder',
    tags: ['N4', 'Genki L19', 'Keigo', 'Business']
  },

  {
    id: 'gp-tamaranai-naranai',
    title: '〜てたまらない vs 〜てならない (Unbearable Physical Urge vs Spontaneous Deep Emotion)',
    meaning: '1) 〜てたまらない: So overwhelmingly intense I can\'t bear it (physical sensation / direct urge). 2) 〜てならない: Spontaneous, deep emotional or instinctive feeling rising from within.',
    level: 'N3',
    streamId: 'stream-social',
    streamName: 'Social Transactions, Hierarchy & Favors',
    connection: 'V-て / い形-くて / な形-で + たまらない / ならない / しょうがない',
    nuance: 'CONTRAST: 〜てたまらない is visceral and immediate: 喉が渇いてたまらない (I am dying of thirst!), 痛くてたまらない (It hurts unbearably!). 〜てならない is psychological and reflective: 彼の将来が心配でならない (I cannot help feeling profound anxiety about his future).',
    keyTakeaway: 'MUG-UP: たまらない = Visceral / Physical ("Can\'t stand it!"). ならない = Deep spontaneous psychology.',
    sentences: [
      {
        id: 's-tama-1',
        japanese: '長時間のハイキングの後で、冷たいビールが飲みたくてたまらない。',
        english: 'After a long hike, I am dying for an ice-cold beer.',
        literal: 'Long-time hike after, cold beer drink-want unbearably.',
        nuanceNote: 'Overpowering physical thirst and visceral desire.',
        tokens: [
          { word: '長時間の', reading: 'ちょうじかんの', romaji: 'choujikan no', meaning: 'long duration\'s', pos: 'Noun' },
          { word: 'ハイキングの後で', reading: 'ハイキングのあとで', romaji: 'haikingu no ato de', meaning: 'after hiking', pos: 'Noun' },
          { word: '冷たい', reading: 'つめたい', romaji: 'tsumetai', meaning: 'cold (to touch)', pos: 'I-Adj' },
          { word: 'ビールが', reading: 'ビールが', romaji: 'biiru ga', meaning: 'beer', pos: 'Noun' },
          { word: '飲みたくてたまらない', reading: 'のみたくてたまらない', romaji: 'nomitakute tamaranai', meaning: 'dying to drink / unbearable desire', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-tama-1',
        question: '一人暮らしの祖母の健康状態が（　　）ならない。',
        translation: 'I cannot help worrying deeply about the health of my grandmother who lives alone.',
        options: ['心配で', '心配して', '心配な', '心配に'],
        correctIndex: 0,
        grammarFocus: '〜てならない connection with emotional na-adjective',
        ruleHint: 'Connects to な-adj via で: 心配でならない.',
        explanations: [
          {
            text: '心配で',
            isCorrect: true,
            reason: 'Correct! な-adjective (心配) takes で to connect to ならない, forming 心配でならない ("cannot help worrying").'
          },
          {
            text: '心配して',
            isCorrect: false,
            reason: 'Incorrect. While 心配する is a verb, 心配でならない is the standard idiomatic expression for deep spontaneous worry.'
          },
          {
            text: '心配な',
            isCorrect: false,
            reason: 'Incorrect. な cannot connect to ならない.'
          },
          {
            text: '心配に',
            isCorrect: false,
            reason: 'Incorrect. に cannot connect to ならない.'
          }
        ]
      }
    ],
    nextPointId: 'gp-zaruwokenai',
    prevPointId: 'gp-keigo-core',
    tags: ['N3', 'SKM N3 Ch9', 'Emotion', 'Impulse']
  },

  {
    id: 'gp-zaruwokenai',
    title: '〜ざるを得ない（ざるをえない） (Have no choice but to do / Compelled by circumstance)',
    meaning: 'Although one does not want to do it, under the compelling circumstances or undeniable reality, one is forced to / cannot avoid doing it.',
    level: 'N2',
    streamId: 'stream-social',
    streamName: 'Social Transactions, Hierarchy & Favors',
    connection: 'V-ない stem (without ない) + ざるを得ない | EXCEPTION: する → せざるを得ない',
    nuance: 'Heavy reluctance: "Against all personal desire, cold objective reality gives me zero alternative." CRITICAL IRREGULARITY: The verb する does NOT become しざるを得ない! It becomes せざるを得ない (sezaru o enai). Always tested on JLPT N2!',
    keyTakeaway: 'MUG-UP: V-ない + ざるを得ない. する → [せざるを得ない]. Pure reluctant necessity.',
    sentences: [
      {
        id: 's-zaru-1',
        japanese: 'これほど明確な証拠を突きつけられては、自分の非を認めざるを得ない。',
        english: 'Faced with such definitive evidence, I have no choice but to admit my fault.',
        literal: 'This-much clear evidence confronted-being, own mistake admit-cannot-avoid.',
        nuanceNote: 'Overwhelming evidence eliminates any alternative; forced to confess.',
        tokens: [
          { word: 'これほど', reading: 'これほど', romaji: 'kore hodo', meaning: 'to this extent', pos: 'Adverb' },
          { word: '明確な', reading: 'めいかくな', romaji: 'meikakuna', meaning: 'clear / definitive', pos: 'Na-Adj' },
          { word: '証拠を', reading: 'しょうこを', romaji: 'shouko o', meaning: 'evidence', pos: 'Noun' },
          { word: '突きつけられては', reading: 'つきつけられては', romaji: 'tsukitsukerarete wa', meaning: 'being confronted with (passive)', pos: 'Verb' },
          { word: '自分の', reading: 'じぶんの', romaji: 'jibun no', meaning: 'one\'s own', pos: 'Pronoun' },
          { word: '非を', reading: 'ひを', romaji: 'hi o', meaning: 'fault / error', pos: 'Noun' },
          { word: '認めざるを得ない', reading: 'みとめざるをえない', romaji: 'mitomezaru o enai', meaning: 'have no choice but to admit', pos: 'Grammar', nuance: '認める (Group 2) -> 認め + ざるを得ない' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-zaru-1',
        question: '台風が接近しているため、残念ながら明日の野外イベントは中止（　　）。',
        translation: 'Because a typhoon is approaching, regrettably we have no choice but to cancel tomorrow\'s outdoor event.',
        options: ['せざるを得ない', 'しざるを得ない', 'するざるを得ない', 'されざるを得ない'],
        correctIndex: 0,
        grammarFocus: '〜ざるを得ない irregular verb する conjugation',
        ruleHint: 'する irregularly transforms into せざるを得ない.',
        explanations: [
          {
            text: 'せざるを得ない',
            isCorrect: true,
            reason: 'Correct! The irregular verb する strictly conjugates to せざるを得ない.'
          },
          {
            text: 'しざるを得ない',
            isCorrect: false,
            reason: 'Incorrect. しざるを得ない is the classic distractor trap on JLPT N2! Always remember する becomes せ.'
          },
          {
            text: 'するざるを得ない',
            isCorrect: false,
            reason: 'Incorrect. Dictionary form cannot attach to ざるを得ない.'
          },
          {
            text: 'されざるを得ない',
            isCorrect: false,
            reason: 'Incorrect. Ungrammatical mixture.'
          }
        ]
      }
    ],
    nextPointId: undefined,
    prevPointId: 'gp-tamaranai-naranai',
    tags: ['N2', 'SKM N2 Ch24', 'Reluctance', 'Irregular Conjugation']
  }
];

