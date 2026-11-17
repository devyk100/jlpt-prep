import { GrammarPoint } from '../types';

export const STREAM_LIMITS_POINTS: GrammarPoint[] = [
  {
    id: 'gp-dake-shika',
    title: '〜だけ vs 〜しか〜ない (Neutral Only vs Insufficiency Only)',
    meaning: 'Limiting quantity or scope. だけ is neutral ("just that amount"). しか〜ない expresses strong subjective dissatisfaction or insufficiency ("only that little bit!").',
    level: 'N5',
    streamId: 'stream-limits',
    streamName: 'Boundaries, Exclusivity & Scope',
    connection: 'Noun / Quantifier + だけ (Affirmative or Negative) | Noun / Quantifier + しか + NEGATIVE VERB (〜ない)',
    nuance: 'Notice: しか MUST always end with a negative verb! "千円しかあります" is completely ungrammatical in Japanese ❌. It must be "千円しかありません" (I have only a mere 1,000 yen). With particles: だけに, だけを, but にしか, でしか (しか takes the outer position).',
    keyTakeaway: 'MUG-UP: [しか] ALWAYS demands [NEGATIVE VERB] (〜ない). Always conveys "not enough".',
    sentences: [
      {
        id: 's-dake-1',
        japanese: '財布の中に小銭が百円しか残っていない。',
        english: 'There is only a mere 100 yen in small change left in my wallet.',
        literal: 'Wallet inside small-change 100-yen only remaining-is-not.',
        nuanceNote: 'Speaker laments having almost no money left (strong sense of insufficiency).',
        tokens: [
          { word: '財布の', reading: 'さいふの', romaji: 'saifu no', meaning: 'wallet\'s', pos: 'Noun' },
          { word: '中に', reading: 'なかに', romaji: 'naka ni', meaning: 'inside', pos: 'Noun' },
          { word: '小銭が', reading: 'こぜにが', romaji: 'kozeni ga', meaning: 'small change / coins', pos: 'Noun' },
          { word: '百円しか', reading: 'ひゃくえんしか', romaji: 'hyaku-en shika', meaning: 'only 100 yen (with scarcity)', pos: 'Grammar' },
          { word: '残っていない', reading: 'のこっていない', romaji: 'nokotte inai', meaning: 'is not remaining', pos: 'Verb (Neg)' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-dake-1',
        question: '昨夜は忙しくて、睡眠時間が三時間（　　）取れなかった。',
        translation: 'Because I was so busy last night, I could only get a mere 3 hours of sleep.',
        options: ['しか', 'だけ', 'ばかり', 'ほど'],
        correctIndex: 0,
        grammarFocus: '〜しか〜ない negative agreement',
        ruleHint: 'Pairs with the negative potential verb 取れなかった expressing insufficient sleep.',
        explanations: [
          {
            text: 'しか',
            isCorrect: true,
            reason: 'Correct! しか + 取れなかった forms "could only get a mere 3 hours", stressing scarcity.'
          },
          {
            text: 'だけ',
            isCorrect: false,
            reason: 'Incorrect. If using だけ, it would be 三時間だけ取れた (neutral affirmative). With 取れなかった, it sounds awkward.'
          },
          {
            text: 'ばかり',
            isCorrect: false,
            reason: 'Incorrect. 三時間ばかり取れなかった is ungrammatical.'
          },
          {
            text: 'ほど',
            isCorrect: false,
            reason: 'Incorrect. ほど doesn\'t carry the restrictive "only a mere" emphasis of しか.'
          }
        ]
      }
    ],
    nextPointId: 'gp-wo-hajime',
    prevPointId: undefined,
    tags: ['N5', 'Genki L14', 'Limits']
  },

  {
    id: 'gp-wo-hajime',
    title: '〜をはじめ（として） (Starting with... primary representative)',
    meaning: 'Singling out the most prominent, representative example from a group, followed by many other similar items: "Starting with X, as well as many others."',
    level: 'N3',
    streamId: 'stream-limits',
    streamName: 'Boundaries, Exclusivity & Scope',
    connection: 'N + をはじめ / をはじめとして / をはじめとする + N',
    nuance: 'Formal and informative. Used when presenting an impressive lineup, delegation, or category where X is the flagship example (e.g. "Starting with the Prime Minister, many dignitaries attended").',
    keyTakeaway: 'MUG-UP: [Flagship Noun] + をはじめ(として) + [全体・多くの人々].',
    sentences: [
      {
        id: 's-hajime-1',
        japanese: '富士山をはじめ、日本には世界的に有名な観光名所が数多く存在している。',
        english: 'Starting with Mt. Fuji, numerous world-famous tourist attractions exist in Japan.',
        literal: 'Mt. Fuji starting-with, Japan-in globally famous tourist-spots many exist.',
        nuanceNote: 'Mt. Fuji represents the premier icon among Japan\'s numerous famous attractions.',
        tokens: [
          { word: '富士山', reading: 'ふじさん', romaji: 'fujisan', meaning: 'Mt. Fuji', pos: 'Noun' },
          { word: 'をはじめ', reading: 'をはじめ', romaji: 'o hajime', meaning: 'starting with (representative)', pos: 'Grammar' },
          { word: '日本には', reading: 'にほんには', romaji: 'nihon ni wa', meaning: 'in Japan', pos: 'Noun' },
          { word: '世界的に', reading: 'せかいてきに', romaji: 'sekaiteki ni', meaning: 'globally / worldwide', pos: 'Adverb' },
          { word: '有名な', reading: 'ゆうめいな', romaji: 'yuumeina', meaning: 'famous', pos: 'Na-Adj' },
          { word: '観光名所が', reading: 'かんこうめいしょが', romaji: 'kankou meisho ga', meaning: 'tourist attractions', pos: 'Noun' },
          { word: '数多く', reading: 'かずおおく', romaji: 'kazuooku', meaning: 'in great numbers', pos: 'Adverb' },
          { word: '存在している', reading: 'そんざいしている', romaji: 'sonzai shite iru', meaning: 'exist', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-hajime-1',
        question: '校長先生（　　）、教職員の皆様には心より感謝申し上げます。',
        translation: 'Starting with the Principal, I extend my heartfelt gratitude to all the faculty and staff.',
        options: ['をはじめ', 'を通じて', 'にわたって', 'に限って'],
        correctIndex: 0,
        grammarFocus: '〜をはじめ representative leader introduction',
        ruleHint: 'Singles out the school principal as the primary representative of the faculty group.',
        explanations: [
          {
            text: 'をはじめ',
            isCorrect: true,
            reason: 'Correct! 校長先生をはじめ highlights the principal as the flagship leader of the entire teaching staff.'
          },
          {
            text: 'を通じて',
            isCorrect: false,
            reason: 'Incorrect. を通じて means "throughout a whole period" or "via a medium".'
          },
          {
            text: 'にわたって',
            isCorrect: false,
            reason: 'Incorrect. にわたって denotes continuous span across time or geographical space.'
          },
          {
            text: 'に限って',
            isCorrect: false,
            reason: 'Incorrect. に限って means "of all unfortunate days" or "specifically only X".'
          }
        ]
      }
    ],
    nextPointId: 'gp-ni-watatte',
    prevPointId: 'gp-dake-shika',
    tags: ['N3', 'SKM N3 Ch4', 'Representative']
  },

  {
    id: 'gp-ni-watatte',
    title: '〜にわたって / 〜にわたり (Spanning across time or space)',
    meaning: 'An action, state, or phenomenon extends continuously across an entire expansive span of time, area, or scope.',
    level: 'N3',
    streamId: 'stream-limits',
    streamName: 'Boundaries, Exclusivity & Scope',
    connection: 'N (Time duration / Geographical expanse / Number of times) + にわたって / にわたり / にわたる + N',
    nuance: 'Signifies breadth, grand scale, and extensive duration (e.g., across 10 years, across the whole country, across 5 rounds of negotiations). It elevates the sense of scale compared to simple 間.',
    keyTakeaway: 'MUG-UP: [大規模な時間・場所・回数] + にわたって (e.g. 10年間にわたる研究).',
    sentences: [
      {
        id: 's-watatte-1',
        japanese: '３日間にわたる激しい議論の末に、ついに合意に達した。',
        english: 'After fierce debates spanning three full days, an agreement was finally reached.',
        literal: '3-days-span fierce debates end-at, finally agreement reached.',
        nuanceNote: 'Emphasizes the intense, exhausting continuous duration of three whole days.',
        tokens: [
          { word: '３日間にわたる', reading: 'みっかかんにわたる', romaji: 'mikkakan ni wataru', meaning: 'spanning across 3 days', pos: 'Grammar' },
          { word: '激しい', reading: 'はげしい', romaji: 'hageshii', meaning: 'intense / fierce', pos: 'I-Adj' },
          { word: '議論の末に', reading: 'ぎろんのすえに', romaji: 'giron no sue ni', meaning: 'after debates (resolution)', pos: 'Grammar' },
          { word: 'ついに', reading: 'ついに', romaji: 'tsuini', meaning: 'at last / finally', pos: 'Adverb' },
          { word: '合意に', reading: 'ごういに', romaji: 'goui ni', meaning: 'agreement', pos: 'Noun' },
          { word: '達した', reading: 'たっした', romaji: 'tasshita', meaning: 'reached', pos: 'Verb (Past)' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-watatte-1',
        question: '台風の影響で、関東全域（　　）停電が発生した。',
        translation: 'Due to the impact of the typhoon, power outages occurred spanning the entire Kanto region.',
        options: ['にわたって', 'をはじめ', 'にとって', 'をめぐって'],
        correctIndex: 0,
        grammarFocus: '〜にわたって geographical expanse',
        ruleHint: 'Describes a phenomenon covering a vast geographic area (関東全域).',
        explanations: [
          {
            text: 'にわたって',
            isCorrect: true,
            reason: 'Correct! 関東全域にわたって captures the vast geographic expanse over which blackouts occurred.'
          },
          {
            text: 'をはじめ',
            isCorrect: false,
            reason: 'Incorrect. をはじめ requires a single representative member, not an entire region.'
          },
          {
            text: 'にとって',
            isCorrect: false,
            reason: 'Incorrect. にとって means "from the perspective of".'
          },
          {
            text: 'をめぐって',
            isCorrect: false,
            reason: 'Incorrect. をめぐって means "controversy surrounding a disputed issue".'
          }
        ]
      }
    ],
    nextPointId: 'gp-wo-tsuujite',
    prevPointId: 'gp-wo-hajime',
    tags: ['N3', 'SKM N3 Ch4', 'Expanse', 'Span']
  },

  {
    id: 'gp-wo-tsuujite',
    title: '〜を通じて / 〜を通して (Throughout period / Via medium)',
    meaning: '1) Continuously throughout an entire uninterrupted period. 2) Doing or achieving something by means of / through an intermediary or medium.',
    level: 'N3',
    streamId: 'stream-limits',
    streamName: 'Boundaries, Exclusivity & Scope',
    connection: 'N + を通じて / を通して (つうじて / とおして)',
    nuance: 'Dual meaning: 1) Time: 四季を通じて (throughout the 4 seasons / all year round). 2) Medium: 友人を通じて知り合った (we got to know each other through a mutual friend). Note: Direct physical tools like pen/scissors take で, not を通じて.',
    keyTakeaway: 'MUG-UP: 1) 一年を通じて = All year round. 2) インターネットを通じて = Via the internet.',
    sentences: [
      {
        id: 's-tsuujite-1',
        japanese: 'この地域は温暖で、一年を通じて様々なフルーツが栽培されている。',
        english: 'This region has a mild climate, and various fruits are cultivated throughout the entire year.',
        literal: 'This region mild being, one-year throughout various fruits cultivated are.',
        nuanceNote: 'Unbroken continuum throughout the full calendar year.',
        tokens: [
          { word: 'この地域は', reading: 'このちいきは', romaji: 'kono chiiki wa', meaning: 'this region', pos: 'Noun' },
          { word: '温暖で', reading: 'おんだんで', romaji: 'ondan de', meaning: 'mild / warm', pos: 'Na-Adj' },
          { word: '一年を通じて', reading: 'いちねんをつうじて', romaji: 'ichinen o tsuujite', meaning: 'throughout the whole year', pos: 'Grammar' },
          { word: '様々な', reading: 'さまざまな', romaji: 'samazamana', meaning: 'various', pos: 'Na-Adj' },
          { word: 'フルーツが', reading: 'フルーツが', romaji: 'furuutsu ga', meaning: 'fruits', pos: 'Noun' },
          { word: '栽培されている', reading: 'さいばいされている', romaji: 'saibai sarete iru', meaning: 'are cultivated', pos: 'Verb (Passive)' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-tsuujite-1',
        question: 'ボランティア活動（　　）、多くの素晴らしい仲間と出会うことができた。',
        translation: 'Through volunteer activities, I was able to meet many wonderful companions.',
        options: ['を通じて', 'にわたって', 'にかけて', 'に際して'],
        correctIndex: 0,
        grammarFocus: '〜を通じて intermediary medium',
        ruleHint: 'Volunteer activities served as the medium through which new friends were met.',
        explanations: [
          {
            text: 'を通じて',
            isCorrect: true,
            reason: 'Correct! ボランティア活動を通じて means "by way of / through the experience of volunteer work".'
          },
          {
            text: 'にわたって',
            isCorrect: false,
            reason: 'Incorrect. にわたって measures numerical duration/expanse, not a qualitative medium.'
          },
          {
            text: 'にかけて',
            isCorrect: false,
            reason: 'Incorrect. にかけて requires starting and ending bounds (AからBにかけて).'
          },
          {
            text: 'に際して',
            isCorrect: false,
            reason: 'Incorrect. に際して means "on the ceremonial occasion of".'
          }
        ]
      }
    ],
    nextPointId: 'gp-ni-kagiri',
    prevPointId: 'gp-ni-watatte',
    tags: ['N3', 'SKM N3 Ch4', 'Medium', 'Duration']
  },

  {
    id: 'gp-ni-kagiri',
    title: '〜に限り（にかぎり） (Strictly limited to... exclusive privilege)',
    meaning: 'An exceptional privilege, special deal, or strict rule that applies ONLY and exclusively to this specific group or timeframe.',
    level: 'N2',
    streamId: 'stream-limits',
    streamName: 'Boundaries, Exclusivity & Scope',
    connection: 'N + に限り / に限る',
    nuance: 'Formal announcements, ticketing rules, promotions, and regulations: "Only on weekends", "Only for first-time visitors". It firmly draws an unbendable line excluding all others.',
    keyTakeaway: 'MUG-UP: [資格・特定対象] + に限り (e.g. 本日ご来店のお客様に限り割引).',
    sentences: [
      {
        id: 's-nikagiri-1',
        japanese: '本日ご来店いただいたお客様に限り、全商品を２０％オフでご提供いたします。',
        english: 'Strictly limited to customers visiting our store today, we offer 20% off all products.',
        literal: 'Today store-visit received customers strictly-to-limited, all-products 20%-off at provide will.',
        nuanceNote: 'Special commercial privilege with strict temporal boundary.',
        tokens: [
          { word: '本日', reading: 'ほんじつ', romaji: 'honjitsu', meaning: 'today (formal)', pos: 'Noun' },
          { word: 'ご来店いただいた', reading: 'ごらいてんいただいた', romaji: 'goraiten itadaita', meaning: 'visited store (keigo)', pos: 'Keigo Verb' },
          { word: 'お客様に限り', reading: 'おきゃくさまにかぎり', romaji: 'okyakusama ni kagiri', meaning: 'strictly limited to customers', pos: 'Grammar' },
          { word: '全商品を', reading: 'ぜんしょうひんを', romaji: 'zen-shouhin o', meaning: 'all products', pos: 'Noun' },
          { word: '２０％オフで', reading: 'にじゅっぱーせんとオフで', romaji: 'nijuppaasento ofu de', meaning: 'at 20% off', pos: 'Noun' },
          { word: 'ご提供いたします', reading: 'ごていきょういたします', romaji: 'goteikyou itashimasu', meaning: 'will offer (humble)', pos: 'Keigo Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-nikagiri-1',
        question: 'このクーポン券は、平日のランチタイム（　　）ご利用いただけます。',
        translation: 'This coupon ticket can be used strictly during weekday lunchtimes only.',
        options: ['に限り', 'に限って', 'をはじめ', 'をめぐって'],
        correctIndex: 0,
        grammarFocus: '〜に限り exclusive promotional qualification',
        ruleHint: 'Official qualification restriction for coupon redemption.',
        explanations: [
          {
            text: 'に限り',
            isCorrect: true,
            reason: 'Correct! に限り marks the strict exclusive terms of the coupon validity.'
          },
          {
            text: 'に限って',
            isCorrect: false,
            reason: 'Incorrect. に限って expresses subjective misfortune ("of all days!") or selective trust, not official rules.'
          },
          {
            text: 'をはじめ',
            isCorrect: false,
            reason: 'Incorrect. をはじめ means "starting with representative example".'
          },
          {
            text: 'をめぐって',
            isCorrect: false,
            reason: 'Incorrect. をめぐって indicates dispute/debate surrounding an issue.'
          }
        ]
      }
    ],
    nextPointId: 'gp-ni-kagitte',
    prevPointId: 'gp-wo-tsuujite',
    tags: ['N2', 'SKM N2 Ch5', 'Strict Exclusivity']
  },

  {
    id: 'gp-ni-kagitte',
    title: '〜に限って（にかぎって） (Of all unlucky days! / Selective trust)',
    meaning: '1) Of all days/times, something inconvenient or unfortunate happens specifically on this occasion (Murphy\'s Law!). 2) Because I know X, that person of all people would never do such a thing.',
    level: 'N2',
    streamId: 'stream-limits',
    streamName: 'Boundaries, Exclusivity & Scope',
    connection: 'N + に限って',
    nuance: 'CONTRAST WITH 〜に限り: に限り is dry, official and neutral (rules, discounts). In contrast, に限って is intensely emotional! 傘を持っていない日に限って、雨が降る ("Of all days, it rains specifically on the day I forgot my umbrella!").',
    keyTakeaway: 'MUG-UP: [Bad timing Noun] + に限って + [Unhappy coincidence] (Murphy\'s Law).',
    sentences: [
      {
        id: 's-nikagitte-1',
        japanese: '傘を持ってこなかった日に限って、突然の大雨に見舞われる。',
        english: 'Of all days, it suddenly pours heavily on the exact day I didn\'t bring an umbrella.',
        literal: 'Umbrella brought-not day strictly-on, sudden heavy-rain struck-by.',
        nuanceNote: 'The universal frustration of Murphy\'s Law in daily life.',
        tokens: [
          { word: '傘を', reading: 'かさを', romaji: 'kasa o', meaning: 'umbrella', pos: 'Noun' },
          { word: '持ってこなかった', reading: 'もってこなかった', romaji: 'motte konakatta', meaning: 'did not bring', pos: 'Verb (Past Neg)' },
          { word: '日に限って', reading: 'ひにかぎって', romaji: 'hi ni kagitte', meaning: 'of all days / specifically on the day', pos: 'Grammar' },
          { word: '突然の', reading: 'とつぜんの', romaji: 'totsuzen no', meaning: 'sudden', pos: 'Noun' },
          { word: '大雨に', reading: 'おおあめに', romaji: 'ooame ni', meaning: 'heavy rain', pos: 'Noun' },
          { word: '見舞われる', reading: 'みまわれる', romaji: 'mimawareru', meaning: 'be struck by (suffering passive)', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-nikagitte-1',
        question: '急いでいる時（　　）、前の車がやたらと遅くてイライラする。',
        translation: 'Of all times, specifically when I am in a hurry, the car in front is dreadfully slow and irritates me.',
        options: ['に限って', 'に限り', 'に反して', 'を通じて'],
        correctIndex: 0,
        grammarFocus: '〜に限って Murphy\'s Law frustration',
        ruleHint: 'Expresses exasperation at unlucky irony when in a hurry.',
        explanations: [
          {
            text: 'に限って',
            isCorrect: true,
            reason: 'Correct! 急いでいる時に限って perfectly captures the ironic, irritating bad timing.'
          },
          {
            text: 'に限り',
            isCorrect: false,
            reason: 'Incorrect. に限り is for objective rule eligibility (discounts, admission), not subjective frustration.'
          },
          {
            text: 'に反して',
            isCorrect: false,
            reason: 'Incorrect. に反して means "contrary to expectations/wishes".'
          },
          {
            text: 'を通じて',
            isCorrect: false,
            reason: 'Incorrect. を通じて means "throughout or via".'
          }
        ]
      }
    ],
    nextPointId: 'gp-bakarika',
    prevPointId: 'gp-ni-kagiri',
    tags: ['N2', 'SKM N2 Ch5', 'Irony', 'Frustration']
  },

  {
    id: 'gp-bakarika',
    title: '〜ばかりか / 〜のみならず (Not only X... but even Y!)',
    meaning: 'Not only does state X apply, but something even further, unexpected, or more extreme Y is also the case.',
    level: 'N2',
    streamId: 'stream-limits',
    streamName: 'Boundaries, Exclusivity & Scope',
    connection: 'Plain form (V / い形 / な形-な / N-である) + ばかりか | のみならず',
    nuance: 'Escalation marker: Clause B adds something beyond the baseline expectation (often with も or さえ). Nuance distinction: 〜ばかりか often emphasizes surprise or grievance, while 〜のみならず is formal/written Japanese suitable for essays and academic speeches.',
    keyTakeaway: 'MUG-UP: [A] ばかりか / のみならず [B も / さえ]. Escalating addition.',
    sentences: [
      {
        id: 's-bakarika-1',
        japanese: '彼は日本語ばかりか、中国語や英語もネイティブ並みに流暢に話すことができる。',
        english: 'He can speak not only Japanese, but also Chinese and English as fluently as a native.',
        literal: 'He Japanese not-only, Chinese and English also native-level fluently speak can.',
        nuanceNote: 'Japanese was already impressive; adding two more languages escalates the admiration.',
        tokens: [
          { word: '彼は', reading: 'かれは', romaji: 'kare wa', meaning: 'he', pos: 'Pronoun' },
          { word: '日本語ばかりか', reading: 'にほんごばかりか', romaji: 'nihongo bakari ka', meaning: 'not only Japanese', pos: 'Grammar' },
          { word: '中国語や', reading: 'ちゅうごくごや', romaji: 'chuugokugo ya', meaning: 'Chinese and', pos: 'Noun' },
          { word: '英語も', reading: 'えいごも', romaji: 'eigo mo', meaning: 'English also', pos: 'Noun' },
          { word: 'ネイティブ並みに', reading: 'ネイティブなみに', romaji: 'neiteibu nami ni', meaning: 'at native level', pos: 'Adverb' },
          { word: '流暢に', reading: 'りゅうちょうに', romaji: 'ryuuchou ni', meaning: 'fluently', pos: 'Adverb' },
          { word: '話すことができる', reading: 'はなすことができる', romaji: 'hanasu koto ga dekiru', meaning: 'can speak', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-bakarika-1',
        question: '今回の不祥事は会社の信用を失墜させた（　　）、巨額の損害賠償問題にまで発展した。',
        translation: 'This recent scandal not only caused the company to lose its credibility, but escalated into a massive damages issue.',
        options: ['ばかりか', 'わりに', '反面', 'あげく'],
        correctIndex: 0,
        grammarFocus: '〜ばかりか escalating consequence addition',
        ruleHint: 'Pairs with 〜にまで発展した (escalated even to...) denoting additive severity.',
        explanations: [
          {
            text: 'ばかりか',
            isCorrect: true,
            reason: 'Correct! V-た (失墜させた) + ばかりか sets up the escalation: "not only X, but even went so far as Y".'
          },
          {
            text: 'わりに',
            isCorrect: false,
            reason: 'Incorrect. わりに means "considering the ratio/standard" and doesn\'t express additive escalation.'
          },
          {
            text: '反面',
            isCorrect: false,
            reason: 'Incorrect. 反面 presents a balancing opposite facet (e.g. convenient, but dangerous).'
          },
          {
            text: 'あげく',
            isCorrect: false,
            reason: 'Incorrect. Ungrammatical here; doesn\'t form the "not only X, but even Y" pair with にまで.'
          }
        ]
      }
    ],
    nextPointId: undefined,
    prevPointId: 'gp-ni-kagitte',
    tags: ['N2', 'SKM N2 Ch6', 'Escalation', 'Not Only']
  }
];

