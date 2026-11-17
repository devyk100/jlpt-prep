import { GrammarPoint } from '../types';

export const STREAM_CONTRASTS_POINTS: GrammarPoint[] = [
  {
    id: 'gp-noni-temo',
    title: '〜のに vs 〜ても (Frustration / Expectation Clash vs Pure Concession)',
    meaning: '〜のに: Despite X being true, unexpected result Y occurred (carries emotional complaint, disappointment, or shock). 〜ても: Even if condition X holds true, Y will still be the outcome.',
    level: 'N4',
    streamId: 'stream-contrasts',
    streamName: 'Contrasts, Concessions & Defiance',
    connection: '〜のに: Plain form + のに / な形 + なのに / N + なのに | 〜ても: V-て + も / い形-くても / な形/N + でも',
    nuance: 'Crucial contrast: 〜のに ALWAYS describes a concrete factual past or current reality that clashes with expectations ("I studied hard, yet I failed"). You CANNOT use commands, requests, or intentions with のに (e.g. "雨なのに、傘を持っていきなさい" ❌ is wrong; use 雨でも).',
    keyTakeaway: 'MUG-UP: 〜のに = Emotional complaint/shock about a FACT. Cannot take commands/volition.',
    sentences: [
      {
        id: 's-noni-1',
        japanese: '毎日あんなに一生懸命勉強したのに、試験に受からなかった。',
        english: 'Even though I studied so hard every day, I did not pass the exam.',
        literal: 'Every-day that-much whole-heartedly studied although, exam-to pass-did-not.',
        nuanceNote: 'Deep sense of betrayal of effort and emotional frustration.',
        tokens: [
          { word: '毎日', reading: 'まいにち', romaji: 'mainichi', meaning: 'every day', pos: 'Noun' },
          { word: 'あんなに', reading: 'あんなに', romaji: 'anna ni', meaning: 'to that extent / so much', pos: 'Adverb' },
          { word: '一生懸命', reading: 'いっしょうけんめい', romaji: 'isshoukenmei', meaning: 'wholeheartedly / hard', pos: 'Adverb' },
          { word: '勉強したのに', reading: 'べんきょうしたのに', romaji: 'benkyou shita no ni', meaning: 'even though I studied', pos: 'Grammar' },
          { word: '試験に', reading: 'しけんに', romaji: 'shiken ni', meaning: 'exam', pos: 'Noun' },
          { word: '受からなかった', reading: 'うからなかった', romaji: 'ukaranakatta', meaning: 'did not pass', pos: 'Verb (Past Neg)' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-noni-1',
        question: '熱がまだ三十八度も（　　）のに、彼は無理をして出社しようとした。',
        translation: 'Even though he still had a fever of 38 degrees, he tried to force himself to go to work.',
        options: ['ある', 'あって', 'あった', 'あり'],
        correctIndex: 0,
        grammarFocus: '〜のに non-past state connection with ongoing condition',
        ruleHint: 'Connects to plain form (あるのに marks the existing high fever).',
        explanations: [
          {
            text: 'ある',
            isCorrect: true,
            reason: 'Correct! 熱がある (having a fever right now) + のに accurately contrasts the current fever with his reckless effort.'
          },
          {
            text: 'あって',
            isCorrect: false,
            reason: 'Incorrect. Te-form cannot connect to のに.'
          },
          {
            text: 'あった',
            isCorrect: false,
            reason: 'Incorrect. まだ (still) emphasizes the ongoing condition, so non-past あるのに is natural.'
          },
          {
            text: 'あり',
            isCorrect: false,
            reason: 'Incorrect. Masu-stem cannot connect to のに.'
          }
        ]
      }
    ],
    nextPointId: 'gp-warini-nishiteha',
    prevPointId: undefined,
    tags: ['N4', 'Genki L18', 'Complaint', 'Expectation Clash']
  },

  {
    id: 'gp-warini-nishiteha',
    title: '〜わりに（は） vs 〜にしては (Ratio Assessment vs Strict Criteria Defier)',
    meaning: 'Evaluating results against a standard. わりに: "Considering the cost/age/effort, surprisingly... (proportion ratio)". にしては: "For someone belonging to category X, surprisingly... (concrete standard)".',
    level: 'N3',
    streamId: 'stream-contrasts',
    streamName: 'Contrasts, Concessions & Defiance',
    connection: '〜わりに: Plain form (V / い形 / な形-な / N-の) + わりに | 〜にしては: Plain form (V / い形 / な形 / N) + にしては (NO の/な!)',
    nuance: 'Notice connection: 70歳なのに元気だ → 70歳のわりに(は)元気だ (Ratio) vs 70歳にしては元気だ (Criteria). In にしては, you CANNOT put な or の with nouns (70歳にしては, NOT 70歳のにしては ❌). わりに can be used with generic concept words like 値段, 年齢, 努力.',
    keyTakeaway: 'MUG-UP: Noun + の + わりに(は). Noun (bare) + にしては. Both mean "unexpectedly for that standard".',
    sentences: [
      {
        id: 's-wari-1',
        japanese: 'このレストランの料理は、値段のわりにはボリュームがあって美味しい。',
        english: 'Considering the inexpensive price, this restaurant\'s food has generous portions and tastes great.',
        literal: 'This restaurant\'s food, price\'s considering volume having delicious is.',
        nuanceNote: 'Great cost-performance ratio: low price contrasted with high quality/portion.',
        tokens: [
          { word: 'このレストランの', reading: 'このレストランの', romaji: 'kono resutoran no', meaning: 'this restaurant\'s', pos: 'Noun' },
          { word: '料理は', reading: 'りょうりは', romaji: 'ryouri wa', meaning: 'food / cooking', pos: 'Noun' },
          { word: '値段のわりには', reading: 'ねだんのわりには', romaji: 'nedan no wari ni wa', meaning: 'considering the price', pos: 'Grammar' },
          { word: 'ボリュームが', reading: 'ボリュームが', romaji: 'boryuumu ga', meaning: 'portion size / volume', pos: 'Noun' },
          { word: 'あって', reading: 'あって', romaji: 'atte', meaning: 'having', pos: 'Verb (Te)' },
          { word: '美味しい', reading: 'おいしい', romaji: 'oishii', meaning: 'delicious', pos: 'I-Adj' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-wari-1',
        question: '彼は日本に住んでまだ半年（　　）、日常会話がとてもスムーズだ。',
        translation: 'Even though he has lived in Japan for only half a year, his everyday conversation is remarkably smooth.',
        options: ['にしては', 'のわりに', 'わりに', 'ながら'],
        correctIndex: 0,
        grammarFocus: '〜にしては noun connection without particles',
        ruleHint: 'Connects directly to specific numerical milestone (半年) without の.',
        explanations: [
          {
            text: 'にしては',
            isCorrect: true,
            reason: 'Correct! 半年にしては attaches directly to the specific milestone: "For someone with only half a year, he is remarkably smooth".'
          },
          {
            text: 'のわりに',
            isCorrect: false,
            reason: 'Incorrect. If using わりに with a noun, it would be 半年のわりに, but the prompt has no の before the blank.'
          },
          {
            text: 'わりに',
            isCorrect: false,
            reason: 'Incorrect. Nouns cannot connect directly to わりに without の (needs 半年のわりに).'
          },
          {
            text: 'ながら',
            isCorrect: false,
            reason: 'Incorrect. ながら requires verb stem or formal concession patterns, not bare time spans.'
          }
        ]
      }
    ],
    nextPointId: 'gp-hanmen-ippou',
    prevPointId: 'gp-noni-temo',
    tags: ['N3', 'SKM N3 Ch6', 'Standards', 'Surprise']
  },

  {
    id: 'gp-hanmen-ippou',
    title: '〜反面（はんめん） vs 〜一方（いっぽう）（で） (Opposite Face vs Dual Perspectives)',
    meaning: 'Highlighting two contrasting aspects of the same topic. 反面: "On the flip side (sharp light and dark contrast)". 一方で: "While simultaneously / on the other hand (balanced contrast)".',
    level: 'N3',
    streamId: 'stream-contrasts',
    streamName: 'Contrasts, Concessions & Defiance',
    connection: 'Plain form (V / い形) + 反面 / 一方（で） | な形 + な/である + 反面 / 一方（で） | N + である + 反面 / 一方（で）',
    nuance: '反面 literally means "the opposite surface of a coin": convenient on the surface, but fraught with hidden peril on the other. 一方で can contrast two different trends occurring in parallel (e.g. "Urban populations are rising, while rural populations are shrinking").',
    keyTakeaway: 'MUG-UP: [Plus feature] 反面 [Minus feature]. Two sides of the exact same coin.',
    sentences: [
      {
        id: 's-hanmen-1',
        japanese: '大都市での生活は刺激的で便利な反面、生活費が高くストレスも溜まりやすい。',
        english: 'While life in a big city is stimulating and convenient, on the flip side, the cost of living is high and stress easily accumulates.',
        literal: 'Big-city-in life stimulating and convenient flip-side, living-costs high stress also accumulate-easy.',
        nuanceNote: 'A classic dual-faceted portrait: the glamor of city life contrasted with its steep costs.',
        tokens: [
          { word: '大都市での', reading: 'だいとしでの', romaji: 'daitoshi de no', meaning: 'in the metropolis', pos: 'Noun' },
          { word: '生活は', reading: 'せいかつは', romaji: 'seikatsu wa', meaning: 'life / living', pos: 'Noun' },
          { word: '刺激的で', reading: 'しげきてきで', romaji: 'shigekiteki de', meaning: 'stimulating and', pos: 'Na-Adj' },
          { word: '便利な反面', reading: 'べんりなはんめん', romaji: 'benrina hanmen', meaning: 'convenient on the flip side', pos: 'Grammar' },
          { word: '生活費が', reading: 'せいかつひが', romaji: 'seikatsuhi ga', meaning: 'living expenses', pos: 'Noun' },
          { word: '高く', reading: 'たかく', romaji: 'takaku', meaning: 'high and', pos: 'I-Adj' },
          { word: 'ストレスも', reading: 'ストレスも', romaji: 'sutoresu mo', meaning: 'stress also', pos: 'Noun' },
          { word: '溜まりやすい', reading: 'たまりやすい', romaji: 'tamariyasui', meaning: 'easy to accumulate', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-hanmen-1',
        question: 'リモートワークは通勤の負担がない（　　）、オンとオフの切り替えが難しくなりがちだ。',
        translation: 'While remote work has no commute burden, on the flip side, switching between on and off mode tends to become difficult.',
        options: ['反面', 'あげく', 'ばかりに', '次第'],
        correctIndex: 0,
        grammarFocus: '〜反面 contrasting dual aspects of single reality',
        ruleHint: 'Contrasts the benefit (no commute) with the downside (work-life blur).',
        explanations: [
          {
            text: '反面',
            isCorrect: true,
            reason: 'Correct! 反面 cleanly balances the positive facet (no commute) against the negative flip side.'
          },
          {
            text: 'あげく',
            isCorrect: false,
            reason: 'Incorrect. あげく requires past tense (た) denoting the bitter end of an ordeal.'
          },
          {
            text: 'ばかりに',
            isCorrect: false,
            reason: 'Incorrect. ばかりに means "simply because of one mistake, disaster struck".'
          },
          {
            text: '次第',
            isCorrect: false,
            reason: 'Incorrect. 次第 indicates immediate future execution, not contrast.'
          }
        ]
      }
    ],
    nextPointId: 'gp-monono',
    prevPointId: 'gp-warini-nishiteha',
    tags: ['N3', 'SKM N3 Ch6', 'Dual Facets']
  },

  {
    id: 'gp-monono',
    title: '〜ものの / 〜とはいうものの (Although it is a fact that... still)',
    meaning: 'Conceding that clause A is an undeniable factual reality, but pointing out that clause B fails to develop as one would naturally expect.',
    level: 'N2',
    streamId: 'stream-contrasts',
    streamName: 'Contrasts, Concessions & Defiance',
    connection: 'Plain form (V / い形 / な形-である / N-である) + ものの | な形 + なものの',
    nuance: 'Formal written concession: "It is true that X, but in reality Y." Unlike casual けれど, ものの carries a mature, reflective tone often used in formal writing, reviews, and business retrospectives.',
    keyTakeaway: 'MUG-UP: [Undeniable Fact] + ものの + [Shortcoming / Hesitation].',
    sentences: [
      {
        id: 's-monono-1',
        japanese: '新しいパソコンを購入したものの、機能が多すぎてまだ使いこなせていない。',
        english: 'Although I purchased a new PC, it has too many functions and I haven\'t been able to master it yet.',
        literal: 'New PC purchased although, functions too-many still master-can-not.',
        nuanceNote: 'Acknowledges the purchase as a fact, but laments the struggle to actually master the tool.',
        tokens: [
          { word: '新しい', reading: 'あたらしい', romaji: 'atarashii', meaning: 'new', pos: 'I-Adj' },
          { word: 'パソコンを', reading: 'パソコンを', romaji: 'pasokon o', meaning: 'PC / laptop', pos: 'Noun' },
          { word: '購入したものの', reading: 'こうにゅうしたものの', romaji: 'kounyuu shita mono no', meaning: 'although I purchased', pos: 'Grammar' },
          { word: '機能が', reading: 'きのうが', romaji: 'kinou ga', meaning: 'functions / features', pos: 'Noun' },
          { word: '多すぎて', reading: 'おおすぎて', romaji: 'oosugite', meaning: 'are too numerous', pos: 'Verb (Te)' },
          { word: 'まだ', reading: 'まだ', romaji: 'mada', meaning: 'still / yet', pos: 'Adverb' },
          { word: '使いこなせていない', reading: 'つかいこなせていない', romaji: 'tsukaikonhasete inai', meaning: 'have not mastered using', pos: 'Verb (Prog Neg)' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-monono-1',
        question: '春とは（　　）ものの、朝晩はまだまだ厳しい寒さが続いている。',
        translation: 'Although it is called spring, severe cold still continues in the mornings and evenings.',
        options: ['いう', 'いって', 'いえば', 'いったら'],
        correctIndex: 0,
        grammarFocus: '〜とはいうものの fixed concessive compound',
        ruleHint: 'The set phrase is とはいうものの ("although it is said to be...").',
        explanations: [
          {
            text: 'いう',
            isCorrect: true,
            reason: 'Correct! 「〜とはいうものの」 is the established idiomatic concession pattern meaning "although it is termed X".'
          },
          {
            text: 'いって',
            isCorrect: false,
            reason: 'Incorrect. とはいって cannot take ものの in this way.'
          },
          {
            text: 'いえば',
            isCorrect: false,
            reason: 'Incorrect. といえば means "speaking of which", not concession.'
          },
          {
            text: 'いったら',
            isCorrect: false,
            reason: 'Incorrect. といったら expresses extreme degree (e.g. その美しさといったら).'
          }
        ]
      }
    ],
    nextPointId: 'gp-dokoroka',
    prevPointId: 'gp-hanmen-ippou',
    tags: ['N2', 'SKM N2 Ch14', 'Mature Concession']
  },

  {
    id: 'gp-dokoroka',
    title: '〜どころか / 〜どころではない (Far from X... actually extreme Y!)',
    meaning: '1) 〜どころか: Far from being X, the real situation is completely opposite or dramatically more extreme! 2) 〜どころではない: I am in absolutely NO position / state of mind to even think of doing X.',
    level: 'N2',
    streamId: 'stream-contrasts',
    streamName: 'Contrasts, Concessions & Defiance',
    connection: 'Plain form / N + どころか | V-辞書形 / N + どころではない',
    nuance: 'Massive psychological contrast! "Did you pass? Pass?! Far from passing, I got the lowest score in the class!" (合格どころか、最下位だった). With どころではない, it stresses absolute impossibility due to overwhelm: "Vacation? With this deadline, I can\'t even think of vacation!"',
    keyTakeaway: 'MUG-UP: [A] どころか [予想外の極端なB]! Completely shatters assumption A.',
    sentences: [
      {
        id: 's-dokoroka-1',
        japanese: '貯金が増えるどころか、毎月の赤字で借金が増える一方だ。',
        english: 'Far from savings increasing, with our monthly deficits, our debts just keep growing.',
        literal: 'Savings increase far-from, monthly deficit-by debt increase continuous-trend is.',
        nuanceNote: 'Shatters the optimistic assumption (savings) and reveals the painful reality (growing debt).',
        tokens: [
          { word: '貯金が', reading: 'ちょきんが', romaji: 'chokin ga', meaning: 'savings', pos: 'Noun' },
          { word: '増えるどころか', reading: 'ふえるどころか', romaji: 'fueru dokoro ka', meaning: 'far from increasing', pos: 'Grammar' },
          { word: '毎月の', reading: 'まいつきの', romaji: 'maitsuki no', meaning: 'every month\'s', pos: 'Noun' },
          { word: '赤字で', reading: 'あかじで', romaji: 'akaji de', meaning: 'with deficit', pos: 'Noun' },
          { word: '借金が', reading: 'しゃっきんが', romaji: 'shakkin ga', meaning: 'debt', pos: 'Noun' },
          { word: '増える一方だ', reading: 'ふえるいっぽうだ', romaji: 'fueru ippou da', meaning: 'keeps continuously increasing', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-dokoroka-1',
        question: '来週のプレゼンの準備で徹夜続きで、週末に遊びに行く（　　）。',
        translation: 'Because I\'ve been pulling all-nighters preparing for next week\'s presentation, going out to have fun this weekend is completely out of the question.',
        options: ['どころではない', 'どころか', '反面', 'ものの'],
        correctIndex: 0,
        grammarFocus: '〜どころではない out of the question / overwhelming circumstances',
        ruleHint: 'Overwhelmed by work, making fun leisure totally impossible.',
        explanations: [
          {
            text: 'どころではない',
            isCorrect: true,
            reason: 'Correct! 「〜どころではない」 conveys: "I am in no condition or position to even consider having fun!".'
          },
          {
            text: 'どころか',
            isCorrect: false,
            reason: 'Incorrect. どころか requires a contrasting extreme follow-up clause (e.g. 遊びに行くどころか寝る時間もない).'
          },
          {
            text: '反面',
            isCorrect: false,
            reason: 'Incorrect. 反面 presents a dual balancing aspect, not overwhelming impossibility.'
          },
          {
            text: 'ものの',
            isCorrect: false,
            reason: 'Incorrect. Ungrammatical sentence ending here.'
          }
        ]
      }
    ],
    nextPointId: undefined,
    prevPointId: 'gp-monono',
    tags: ['N2', 'SKM N2 Ch12', 'Extreme Contrast', 'Impossibility']
  }
];

