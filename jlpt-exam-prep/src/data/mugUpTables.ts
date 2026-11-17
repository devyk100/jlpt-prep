import { MugUpTable } from '../types';

export const MASTER_MUG_UP_TABLES: Record<string, MugUpTable> = {
  teFormMatrix: {
    title: 'The Te-Form (て形) Conjugation Matrix',
    subtitle: 'The foundational gateway for ~ている, ~てから, ~てもいい, ~てはいけない, and ~てしまう.',
    columns: ['Verb Group / Ending', 'Dictionary (辞書形)', 'Te-Form (て形)', 'Past (た形)', 'Mnemonic / Mug-Up Rule'],
    rows: [
      {
        label: 'Group 1: う・つ・る',
        cells: ['買う (kau), 待つ (matsu), 取る (toru)', '買って, 待って, 取って', '買った, 待った, 取った', 'う・つ・る → って / った (Small つ + て)'],
        note: 'Classic rhythm: "u, tsu, ru becomes tte"'
      },
      {
        label: 'Group 1: む・ぶ・ぬ',
        cells: ['飲む (nomu), 遊ぶ (asobu), 死ぬ (shinu)', '飲んで, 遊んで, 死んで', '飲んだ, 遊んだ, 死んだ', 'む・ぶ・ぬ → んで / んだ (Voiced ん + で)'],
        note: 'Voiced consonants always take で, not て.'
      },
      {
        label: 'Group 1: く / ぐ',
        cells: ['書く (kaku), 泳ぐ (oyogu)', '書いて, 泳いで', '書いた, 泳いだ', 'く → いて, ぐ → いで (Drop consonant, add い)'],
        note: 'CRITICAL EXCEPTION: 行く (iku) does NOT become いいて! It becomes 行って (itte) / 行った (itta)!'
      },
      {
        label: 'Group 1: す',
        cells: ['話す (hanasu), 出す (dasu)', '話して, 出して', '話した, 出した', 'す → して / した (Regular change)'],
        note: 'Behaves cleanly like polite shimasu.'
      },
      {
        label: 'Group 2: る (Ichidan)',
        cells: ['食べる (taberu), 見る (miru), 起きる (okiru)', '食べて, 見て, 起きて', '食べた, 見た, 起きた', 'Simply drop る and attach て / た'],
        note: 'Vowel before る is usually e or i (tabe-, mi-).'
      },
      {
        label: 'Group 3: Irregular (変格)',
        cells: ['する (suru), 来る (kuru)', 'して, 来て (きて)', 'した, 来た (きた)', 'Completely irregular, mug up pronunciation of 来 (ki-te, ki-ta)!'],
        note: 'Notice 来る (kuru) changes reading to "ki" in て/た form!'
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
  }
};

