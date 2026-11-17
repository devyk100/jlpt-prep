import { GrammarPoint } from '../types';
import { MASTER_MUG_UP_TABLES } from './mugUpTables';

export const STREAM_CONDITIONALS_POINTS: GrammarPoint[] = [
  {
    id: 'gp-conditionals-four',
    title: 'The 4 Conditionals Decoded: と vs ば vs たら vs なら',
    meaning: 'Foundational N5/N4 conditionals that test learners continuously through N3 and N2: natural consequence (と), hypothetical requirement (ば), temporal trigger (たら), and contextual advice (なら).',
    level: 'N4',
    streamId: 'stream-conditionals',
    streamName: 'Conditional Horizons & Prerequisites',
    connection: 'V-る + と | V-eば | V-た + ら | N / Plain + なら',
    nuance: 'Pay extreme attention to clause restrictions: 〜と and 〜ば CANNOT have volitional endings (〜てください, 〜ましょう, 〜つもりだ) when the subjects are deliberate actions! If you see "〜てください" at the end of the sentence, 〜たら or 〜なら is almost certainly required.',
    keyTakeaway: 'MUG-UP: 〜てください at the end? Choose たら or なら! Never choose と.',
    table: MASTER_MUG_UP_TABLES.conditionalsMatrix,
    sentences: [
      {
        id: 's-cond-1',
        japanese: 'この交差点を右に曲がると、左手に郵便局が見えます。',
        english: 'When you turn right at this intersection, you will see the post office on your left.',
        literal: 'This intersection right turn-if, left-hand-to post-office is-visible.',
        nuanceNote: 'Natural, automatic spatial consequence: turning the corner mechanically reveals the post office.',
        tokens: [
          { word: 'この', reading: 'この', romaji: 'kono', meaning: 'this', pos: 'Determiner' },
          { word: '交差点', reading: 'こうさてん', romaji: 'kousaten', meaning: 'intersection', pos: 'Noun' },
          { word: 'を', reading: 'を', romaji: 'o', meaning: 'path particle', pos: 'Particle' },
          { word: '右に', reading: 'みぎに', romaji: 'migi ni', meaning: 'to the right', pos: 'Noun' },
          { word: '曲がると', reading: 'まがると', romaji: 'magaru to', meaning: 'when you turn', pos: 'Grammar' },
          { word: '左手に', reading: 'ひだりてに', romaji: 'hidarite ni', meaning: 'on the left hand', pos: 'Noun' },
          { word: '郵便局', reading: 'ゆうびんきょく', romaji: 'yuubinkyoku', meaning: 'post office', pos: 'Noun' },
          { word: 'が', reading: 'が', romaji: 'ga', meaning: 'subject marker', pos: 'Particle' },
          { word: '見えます', reading: 'みえます', romaji: 'miemasu', meaning: 'is visible / can be seen', pos: 'Verb' }
        ]
      },
      {
        id: 's-cond-2',
        japanese: '京都へ行くなら、秋の紅葉の季節が一番おすすめですよ。',
        english: 'If you are going to Kyoto, the autumn foliage season is definitely the best recommendation.',
        literal: 'Kyoto to go if-case, autumn\'s red-leaves season number-one recommendation is.',
        nuanceNote: 'Listener brought up Kyoto; speaker provides expert situational advice with なら.',
        tokens: [
          { word: '京都へ', reading: 'きょうとえ', romaji: 'kyouto e', meaning: 'to Kyoto', pos: 'Noun' },
          { word: '行くなら', reading: 'いくなら', romaji: 'iku nara', meaning: 'if you are going (contextual)', pos: 'Grammar' },
          { word: '秋の', reading: 'あきの', romaji: 'aki no', meaning: 'autumn\'s', pos: 'Noun' },
          { word: '紅葉の', reading: 'こうようの', romaji: 'kouyou no', meaning: 'autumn leaves\'', pos: 'Noun' },
          { word: '季節', reading: 'きせつ', romaji: 'kisetsu', meaning: 'season', pos: 'Noun' },
          { word: 'が', reading: 'が', romaji: 'ga', meaning: 'subject marker', pos: 'Particle' },
          { word: '一番', reading: 'いちばん', romaji: 'ichiban', meaning: 'number one / most', pos: 'Adverb' },
          { word: 'おすすめですよ', reading: 'おすすめですよ', romaji: 'osusume desu yo', meaning: 'is recommendation!', pos: 'Noun' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-cond-1',
        question: '駅に着い（　　）、すぐに私に電話をかけてください。',
        translation: 'When you arrive at the station, please give me a call immediately.',
        options: ['たら', 'てと', 'れば', 'るなら'],
        correctIndex: 0,
        grammarFocus: 'Conditional permission with volitional command clause',
        ruleHint: 'Sentence ends in a request (〜てください), which strictly forbids と.',
        explanations: [
          {
            text: 'たら',
            isCorrect: true,
            reason: 'Correct! 〜たら (着いたら) is the only conditional form here that naturally permits a polite command (〜てください) in the following clause.'
          },
          {
            text: 'てと',
            isCorrect: false,
            reason: 'Incorrect. Ungrammatical connection.'
          },
          {
            text: 'れば',
            isCorrect: false,
            reason: 'Incorrect. 着けば cannot pair with a volitional request when the same person controls the arrival.'
          },
          {
            text: 'るなら',
            isCorrect: false,
            reason: 'Incorrect. 着くなら would mean "If you intend to arrive (before arriving)", but you want them to call AFTER arriving.'
          }
        ]
      }
    ],
    nextPointId: 'gp-sae-ba',
    prevPointId: undefined,
    tags: ['N4', 'Genki L18', 'Conditionals']
  },

  {
    id: 'gp-sae-ba',
    title: '〜さえ〜ば (If only X... then everything is fine)',
    meaning: 'If only one single essential condition X is fulfilled, everything else will naturally resolve and be satisfactory.',
    level: 'N3',
    streamId: 'stream-conditionals',
    streamName: 'Conditional Horizons & Prerequisites',
    connection: 'N + さえ + V-ば / い形-ければ / な形-なら / N-なら | V-stem + さえすれば',
    nuance: 'Expresses minimalism and laser focus: all other concerns are trivial if this one condition is met. Highly frequent in JLPT reading passages (e.g., as long as you have health, as long as you love each other).',
    keyTakeaway: 'MUG-UP: N + さえ + [Conditional ば]. (e.g. 体さえ健康なら / 時間さえあれば).',
    sentences: [
      {
        id: 's-saeba-1',
        japanese: 'どんなに辛い時でも、あなたさえそばにいてくれれば、私は乗り越えられます。',
        english: 'No matter how bitter the times, if only you are by my side, I can overcome anything.',
        literal: 'How-much bitter time even, you-only side-at being-give-if, I overcome can.',
        nuanceNote: 'Your presence alone is the one indispensable prerequisite.',
        tokens: [
          { word: 'どんなに', reading: 'どんなに', romaji: 'donna ni', meaning: 'no matter how', pos: 'Adverb' },
          { word: '辛い', reading: 'つらい', romaji: 'tsurai', meaning: 'bitter / painful', pos: 'I-Adj' },
          { word: '時でも', reading: 'ときでも', romaji: 'toki demo', meaning: 'time even-at', pos: 'Noun' },
          { word: 'あなたさえ', reading: 'あなたさえ', romaji: 'anata sae', meaning: 'you alone / if only you', pos: 'Grammar' },
          { word: 'そばにいてくれれば', reading: 'そばにいてくれれば', romaji: 'soba ni ite kurereba', meaning: 'are by my side (if)', pos: 'Grammar' },
          { word: '私は', reading: 'わたしは', romaji: 'watashi wa', meaning: 'I', pos: 'Pronoun' },
          { word: '乗り越えられます', reading: 'のりこえられます', romaji: 'norikoeraremasu', meaning: 'can overcome (potential)', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-saeba-1',
        question: 'お金（　　）あれば、幸せになれるというわけではない。',
        translation: 'It doesn\'t necessarily mean that you will become happy if only you have money.',
        options: ['さえ', 'こそ', 'ばかり', 'ほど'],
        correctIndex: 0,
        grammarFocus: '〜さえ〜ば minimal prerequisite marker',
        ruleHint: 'Noun + さえ + あれば is the fixed pattern for "if only one has X".',
        explanations: [
          {
            text: 'さえ',
            isCorrect: true,
            reason: 'Correct! お金さえあれば forms "if only one has money", perfectly completing the conditional.'
          },
          {
            text: 'こそ',
            isCorrect: false,
            reason: 'Incorrect. こそ is for strong emphasis ("precisely because X") and doesn\'t form this conditional idiom.'
          },
          {
            text: 'ばかり',
            isCorrect: false,
            reason: 'Incorrect. お金ばかりあれば is ungrammatical.'
          },
          {
            text: 'ほど',
            isCorrect: false,
            reason: 'Incorrect. ほど indicates degree or comparison ("to the extent of").'
          }
        ]
      }
    ],
    nextPointId: 'gp-toshitara',
    prevPointId: 'gp-conditionals-four',
    tags: ['N3', 'SKM N3 Ch7', 'Minimal Condition']
  },

  {
    id: 'gp-toshitara',
    title: '〜としたら / 〜とすれば (Supposing that... / Pure hypothesis)',
    meaning: 'Setting up a hypothetical assumption or scenario: "If we suppose that X were true, then Y would follow."',
    level: 'N3',
    streamId: 'stream-conditionals',
    streamName: 'Conditional Horizons & Prerequisites',
    connection: 'Plain form (V / い形 / な形だ / Nだ) + としたら / とすれば',
    nuance: 'Introduces imaginative, counter-factual, or thought-experiment conditions ("If you won 100 million yen...", "If aliens existed..."). としたら tends to focus on the speaker\'s subjective feelings or actions; とすれば focuses on logical deduction.',
    keyTakeaway: 'MUG-UP: Plain form + としたら = "Suppose for a moment that X were reality..."',
    sentences: [
      {
        id: 's-toshitara-1',
        japanese: 'もし明日地球が滅亡するとしたら、あなたは何を食べたいですか。',
        english: 'Supposing that the earth were to be destroyed tomorrow, what would you want to eat?',
        literal: 'If tomorrow earth perish-if-suppose, you what eat-want?',
        nuanceNote: 'Pure fantasy thought experiment scenario.',
        tokens: [
          { word: 'もし', reading: 'もし', romaji: 'moshi', meaning: 'if (hypothetical marker)', pos: 'Adverb' },
          { word: '明日', reading: 'あした', romaji: 'ashita', meaning: 'tomorrow', pos: 'Noun' },
          { word: '地球が', reading: 'ちきゅうが', romaji: 'chikyuu ga', meaning: 'earth', pos: 'Noun' },
          { word: '滅亡するとしたら', reading: 'めつぼうするとしたら', romaji: 'metsubou suru to shitara', meaning: 'supposing it perishes', pos: 'Grammar' },
          { word: 'あなたは', reading: 'あなたは', romaji: 'anata wa', meaning: 'you', pos: 'Pronoun' },
          { word: '何を', reading: 'なにを', romaji: 'nani o', meaning: 'what', pos: 'Pronoun' },
          { word: '食べたいですか', reading: 'たべたいですか', romaji: 'tabetai desu ka', meaning: 'do you want to eat?', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-toshitara-1',
        question: 'その話が本当だ（　　）、大変な大事件になりますね。',
        translation: 'Supposing that story is true, it would become a massive incident, wouldn\'t it?',
        options: ['とすれば', 'にしたがって', 'につれて', 'とともに'],
        correctIndex: 0,
        grammarFocus: '〜とすれば logical hypothesis deduction',
        ruleHint: 'Marks a logical deduction derived from supposing the premise is true.',
        explanations: [
          {
            text: 'とすれば',
            isCorrect: true,
            reason: 'Correct! Noun + だとすれば sets up the hypothesis: "If that premise holds, then logically Y follows".'
          },
          {
            text: 'にしたがって',
            isCorrect: false,
            reason: 'Incorrect. にしたがって means "as X progresses, Y changes proportionately".'
          },
          {
            text: 'につれて',
            isCorrect: false,
            reason: 'Incorrect. につれて denotes parallel continuous change over time.'
          },
          {
            text: 'とともに',
            isCorrect: false,
            reason: 'Incorrect. とともに means "together with" or "simultaneously as".'
          }
        ]
      }
    ],
    nextPointId: 'gp-mononara',
    prevPointId: 'gp-sae-ba',
    tags: ['N3', 'SKM N3 Ch7', 'Hypothesis']
  },

  {
    id: 'gp-mononara',
    title: '〜ものなら (If by any miracle it were possible / Threatening warning)',
    meaning: '1) If by some near-impossible miracle it could be done, I would love to! 2) If you dare make that one mistake, terrible consequences will follow.',
    level: 'N2',
    streamId: 'stream-conditionals',
    streamName: 'Conditional Horizons & Prerequisites',
    connection: '1) V-可能形 (Potential) + ものなら | 2) V-意向形 / V-る + ものなら',
    nuance: 'With Potential verbs (やり直せるものなら, 帰れるものなら), it conveys heartbreaking longing for something virtually impossible in reality. With non-potential verbs (遅刻しようものなら), it carries a grave warning: "If you dare do X, you will face severe wrath!"',
    keyTakeaway: 'MUG-UP: Potential verb + ものなら = "If only it were remotely possible (alas it is not)".',
    sentences: [
      {
        id: 's-mononara-1',
        japanese: '過去の過ちをやり直せるものなら、人生をもう一度最初からやり直したい。',
        english: 'If by any miracle I could redo my past mistakes, I would want to live my life over again from the beginning.',
        literal: 'Past mistakes redo-can-if-miracle, life once-more beginning from redo want.',
        nuanceNote: 'Deep, poignant longing acknowledging the impossibility of turning back time.',
        tokens: [
          { word: '過去の', reading: 'かこの', romaji: 'kako no', meaning: 'past\'s', pos: 'Noun' },
          { word: '過ちを', reading: 'あやまちを', romaji: 'ayamachi o', meaning: 'mistakes / blunders', pos: 'Noun' },
          { word: 'やり直せるものなら', reading: 'やりなおせるものなら', romaji: 'yarinaoseru mono nara', meaning: 'if by any miracle I could redo', pos: 'Grammar', nuance: 'Potential form やり直せる' },
          { word: '人生を', reading: 'じんせいを', romaji: 'jinsei o', meaning: 'life', pos: 'Noun' },
          { word: 'もう一度', reading: 'もういちど', romaji: 'mou ichido', meaning: 'once more', pos: 'Adverb' },
          { word: '最初から', reading: 'さいしょから', romaji: 'saisho kara', meaning: 'from the start', pos: 'Noun' },
          { word: 'やり直したい', reading: 'やりなおしたい', romaji: 'yarinaoshitai', meaning: 'want to redo', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-mononara-1',
        question: 'あの厳格な部長の前でミスを（　　）ものなら、即座に大目玉を食らうだろう。',
        translation: 'If you dare make a mistake in front of that strict general manager, you\'ll immediately get a furious scolding.',
        options: ['しよう', 'する', 'した', 'して'],
        correctIndex: 0,
        grammarFocus: '〜（よ）うものなら warning conditional',
        ruleHint: 'Connects to volitional form (しよう) for the grave "if you dare" conditional.',
        explanations: [
          {
            text: 'しよう',
            isCorrect: true,
            reason: 'Correct! V-よう (しよう) + ものなら expresses the ominous threat: "If you so much as dare make a mistake..."'
          },
          {
            text: 'する',
            isCorrect: false,
            reason: 'Incorrect. Dictionary form without potential does not create this warning construction.'
          },
          {
            text: 'した',
            isCorrect: false,
            reason: 'Incorrect. Past form した does not connect to ものなら.'
          },
          {
            text: 'して',
            isCorrect: false,
            reason: 'Incorrect. Te-form cannot connect to ものなら.'
          }
        ]
      }
    ],
    nextPointId: 'gp-naikotoniwa',
    prevPointId: 'gp-toshitara',
    tags: ['N2', 'SKM N2 Ch15', 'Miracle Condition', 'Warning']
  },

  {
    id: 'gp-naikotoniwa',
    title: '〜ないことには（〜ない） (Unless X happens... Y is impossible)',
    meaning: 'Unless condition X occurs first, result Y can fundamentally never happen or be determined.',
    level: 'N2',
    streamId: 'stream-conditionals',
    streamName: 'Conditional Horizons & Prerequisites',
    connection: 'V-ない + ことには | い形-くない + ことには | な形-でない + ことには | N-でない + ことには',
    nuance: 'The result clause ALWAYS contains a negative or impossible predicate: 〜ない, 〜できない, 〜わからない. It establishes X as a strict, non-negotiable prerequisite gatekeeper.',
    keyTakeaway: 'MUG-UP: [A-ないことには] + [B-できない / 分からない]. No X, no Y.',
    sentences: [
      {
        id: 's-naikotoniwa-1',
        japanese: '実際に現場の状況を見てみないことには、正確な修理費用は見積もれない。',
        english: 'Unless we actually go and inspect the on-site situation, we cannot estimate the exact repair cost.',
        literal: 'Actually site\'s situation inspect-not unless, accurate repair cost estimate-cannot.',
        nuanceNote: 'Site inspection is an absolute prerequisite before an estimate can be provided.',
        tokens: [
          { word: '実際に', reading: 'じっさいに', romaji: 'jissai ni', meaning: 'actually / in reality', pos: 'Adverb' },
          { word: '現場の', reading: 'げんばの', romaji: 'genba no', meaning: 'on-site / actual spot', pos: 'Noun' },
          { word: '状況を', reading: 'じょうきょうを', romaji: 'joukyou o', meaning: 'situation', pos: 'Noun' },
          { word: '見てみないことには', reading: 'みてみないことには', romaji: 'mite minai koto ni wa', meaning: 'unless we look and see', pos: 'Grammar', nuance: 'Negative of 見てみる + ことには' },
          { word: '正確な', reading: 'せいかくな', romaji: 'seikakuna', meaning: 'accurate / exact', pos: 'Na-Adj' },
          { word: '修理費用は', reading: 'しゅうりひようは', romaji: 'shuuri hiyou wa', meaning: 'repair cost', pos: 'Noun' },
          { word: '見積もれない', reading: 'みつもれない', romaji: 'mitsumorenai', meaning: 'cannot estimate (potential neg)', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-naikotoniwa-1',
        question: '双方の話を直接（　　）ことには、どちらに責任があるか判断できない。',
        translation: 'Unless we listen directly to both sides\' accounts, we cannot judge who bears the responsibility.',
        options: ['聞かない', '聞いた', '聞く', '聞いている'],
        correctIndex: 0,
        grammarFocus: '〜ないことには negative prerequisite connection',
        ruleHint: 'Requires the negative form (聞かない) before ことには.',
        explanations: [
          {
            text: '聞かない',
            isCorrect: true,
            reason: 'Correct! V-ない (聞かない) + ことには forms "unless we listen... we cannot judge".'
          },
          {
            text: '聞いた',
            isCorrect: false,
            reason: 'Incorrect. Past form cannot connect to ことには.'
          },
          {
            text: '聞く',
            isCorrect: false,
            reason: 'Incorrect. Affirmative dictionary form cannot connect here.'
          },
          {
            text: '聞いている',
            isCorrect: false,
            reason: 'Incorrect. Progressive form cannot connect to ことには.'
          }
        ]
      }
    ],
    nextPointId: undefined,
    prevPointId: 'gp-mononara',
    tags: ['N2', 'SKM N2 Ch15', 'Strict Prerequisite']
  }
];

