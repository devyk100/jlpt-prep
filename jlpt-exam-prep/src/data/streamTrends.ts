import type { GrammarPoint } from '../types';

export const STREAM_TRENDS_POINTS: GrammarPoint[] = [
  {
    id: 'gp-ippouda',
    title: '〜一方だ / 〜ばかりだ (Steadily trending in one direction)',
    meaning: 'A change or tendency keeps accelerating continuously in one unbroken direction. 〜ばかりだ almost always indicates a worsening trend; 〜一方だ can be positive or negative.',
    level: 'N3',
    streamId: 'stream-trends',
    streamName: 'Trends, Changes & Proportional Evolution',
    connection: 'V-辞書形 (Change verbs: 増える, 減る, 悪化する, 上がる) + 一方だ / ばかりだ',
    nuance: 'Verbs used with this pattern MUST express continuous change (変化動詞). You cannot say "食べる一方だ" ❌ unless you say "体重が増える一方だ" (weight keeps increasing).',
    keyTakeaway: 'MUG-UP: V-辞書形 (変化動詞) + 一方だ (Continuous trend). ばかりだ = Continuous decline/worsening.',
    sentences: [
      {
        id: 's-ippou-1',
        japanese: '少子高齢化が進み、地方の人口は減少する一方だ。',
        english: 'As the declining birthrate and aging population progress, the population of rural areas keeps steadily decreasing.',
        literal: 'Low-birth-aging progresses, rural-areas\' population decrease one-direction is.',
        nuanceNote: 'Unrelenting demographic trend continuing without sign of stopping.',
        tokens: [
          { word: '少子高齢化', reading: 'しょうしこうれいか', romaji: 'shoushi koureika', meaning: 'declining birthrate and aging population', pos: 'Noun' },
          { word: 'が', reading: 'が', romaji: 'ga', meaning: 'subject marker', pos: 'Particle' },
          { word: '進み', reading: 'すすみ', romaji: 'susumi', meaning: 'progressing', pos: 'Verb (Stem)' },
          { word: '地方の', reading: 'ちほうの', romaji: 'chihou no', meaning: 'rural areas\'', pos: 'Noun' },
          { word: '人口は', reading: 'じんこうは', romaji: 'jinkou wa', meaning: 'population', pos: 'Noun' },
          { word: '減少する一方だ', reading: 'げんしょうするいっぽうだ', romaji: 'genshou suru ippou da', meaning: 'keeps steadily decreasing', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-ippou-1',
        question: '不況の影響で、会社の業績は悪化する（　　）で、社員の不安が募っている。',
        translation: 'Due to the recession, the company\'s business performance just keeps worsening, and employees\' anxieties are mounting.',
        options: ['一方', 'ばかりか', '反面', '次第'],
        correctIndex: 0,
        grammarFocus: '〜一方だ continuous worsening trend',
        ruleHint: 'Connects to change verb 悪化する (to worsen) indicating an accelerating trend.',
        explanations: [
          {
            text: '一方',
            isCorrect: true,
            reason: 'Correct! 「悪化する一方」 indicates that business performance is deteriorating steadily in one continuous direction.'
          },
          {
            text: 'ばかりか',
            isCorrect: false,
            reason: 'Incorrect. ばかりか means "not only X, but also Y" and requires an additive clause.'
          },
          {
            text: '反面',
            isCorrect: false,
            reason: 'Incorrect. 反面 presents a dual balancing facet, not an ongoing trend.'
          },
          {
            text: '次第',
            isCorrect: false,
            reason: 'Incorrect. 次第 requires verb stem to mean "as soon as (business)".'
          }
        ]
      }
    ],
    nextPointId: 'gp-ni-tsurete',
    prevPointId: undefined,
    tags: ['N3', 'SKM N3 Ch2', 'Trends', 'Continuous Change']
  },

  {
    id: 'gp-ni-tsurete',
    title: '〜につれて / 〜にしたがって (As X progresses, Y proportionately changes)',
    meaning: 'In parallel with the progression of change X, change Y occurs naturally and proportionately alongside it.',
    level: 'N2',
    streamId: 'stream-trends',
    streamName: 'Trends, Changes & Proportional Evolution',
    connection: 'V-辞書形 / N (Change noun) + につれて / にしたがって',
    nuance: 'CONTRAST: 〜につれて describes natural, automatic proportional changes (e.g. as temperature rises, ice melts; as you grow older, physical stamina declines). 〜にしたがって can ALSO mean following formal orders/rules (法律にしたがって = according to law).',
    keyTakeaway: 'MUG-UP: [A-変化] につれて [B-比例的変化]. Natural cause-and-effect parallel change.',
    sentences: [
      {
        id: 's-tsurete-1',
        japanese: '年齢を重ねるにつれて、健康の大切さを身に染みて感じるようになった。',
        english: 'As I grow older, I have come to feel the preciousness of good health deep in my bones.',
        literal: 'Age accumulate as-progresses, health\'s importance body-to-permeate feel came-to-be.',
        nuanceNote: 'Natural psychological deepening in direct proportion to aging.',
        tokens: [
          { word: '年齢を', reading: 'ねんれいを', romaji: 'nenrei o', meaning: 'age', pos: 'Noun' },
          { word: '重ねるにつれて', reading: 'かさねるにつれて', romaji: 'kasaneru ni tsurete', meaning: 'as one accumulates (years)', pos: 'Grammar' },
          { word: '健康の', reading: 'けんこうの', romaji: 'kenkou no', meaning: 'health\'s', pos: 'Noun' },
          { word: '大切さを', reading: 'たいせつさを', romaji: 'taisetsusa o', meaning: 'preciousness / importance', pos: 'Noun' },
          { word: '身に染みて', reading: 'みにしみて', romaji: 'mi ni shimite', meaning: 'deeply / to the bone', pos: 'Idiom' },
          { word: '感じるようになった', reading: 'かんじるようになった', romaji: 'kanjiru you ni natta', meaning: 'came to feel', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-tsurete-1',
        question: '台風が（　　）につれて、風雨がますます強まってきた。',
        translation: 'As the typhoon approached, the wind and rain grew stronger and stronger.',
        options: ['近づく', '近づいた', '近づき', '近づいて'],
        correctIndex: 0,
        grammarFocus: '〜につれて verb dictionary form connection',
        ruleHint: 'Connects to dictionary form of change verb (近づく).',
        explanations: [
          {
            text: '近づく',
            isCorrect: true,
            reason: 'Correct! V-辞書形 (近づく) + につれて captures the parallel surge of storm intensity as the typhoon approaches.'
          },
          {
            text: '近づいた',
            isCorrect: false,
            reason: 'Incorrect. Past form cannot connect to につれて.'
          },
          {
            text: '近づき',
            isCorrect: false,
            reason: 'Incorrect. Masu-stem does not connect to につれて.'
          },
          {
            text: '近づいて',
            isCorrect: false,
            reason: 'Incorrect. Te-form cannot connect to につれて.'
          }
        ]
      }
    ],
    nextPointId: 'gp-ni-oujite',
    prevPointId: 'gp-ippouda',
    tags: ['N2', 'SKM N2 Ch9', 'Proportional Change', 'Correlation']
  },

  {
    id: 'gp-ni-oujite',
    title: '〜に応じて（におうじて） (In proportion to / Adapted to)',
    meaning: 'Adjusting, tailoring, or varying action Y flexibly in response to differing conditions, demands, budgets, or abilities X.',
    level: 'N2',
    streamId: 'stream-trends',
    streamName: 'Trends, Changes & Proportional Evolution',
    connection: 'N + に応じて / に応じた + N',
    nuance: 'Customization marker: "Tailored to your budget", "According to skill level", "In response to customer requests". Unlike につれて (passive natural change), に応じて is intentional calibration and bespoke adaptation.',
    keyTakeaway: 'MUG-UP: [基準・要望・能力] + に応じて (e.g. 予算に応じてメニューを決める).',
    sentences: [
      {
        id: 's-oujite-1',
        japanese: '当スクールでは、生徒一人ひとりのレベルに応じて個別の学習計画を作成します。',
        english: 'At our school, we create individual study plans tailored to each individual student\'s level.',
        literal: 'Our school-at, student each-one\'s level in-accordance-with individual study plan create.',
        nuanceNote: 'Personalized customization based on the student\'s proficiency.',
        tokens: [
          { word: '当スクールでは', reading: 'とうスクールでは', romaji: 'tou sukuuru de wa', meaning: 'at our school (formal)', pos: 'Noun' },
          { word: '生徒一人ひとりの', reading: 'せいとひとりひとりの', romaji: 'seito hitorihitori no', meaning: 'each student\'s', pos: 'Noun' },
          { word: 'レベルに応じて', reading: 'レベルにおうじて', romaji: 'reberu ni oujite', meaning: 'tailored to the level', pos: 'Grammar' },
          { word: '個別の', reading: 'こべつの', romaji: 'kobetsu no', meaning: 'individual / personalized', pos: 'Noun' },
          { word: '学習計画を', reading: 'がくしゅうけいかくを', romaji: 'gakushuu keikaku o', meaning: 'study plan', pos: 'Noun' },
          { word: '作成します', reading: 'さくせいします', romaji: 'sakusei shimasu', meaning: 'create / formulate', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-oujite-1',
        question: 'お客様のご予算（　　）、最適なリフォームプランをご提案いたします。',
        translation: 'Tailored to the customer\'s budget, we will propose the most suitable renovation plan.',
        options: ['に応じて', 'をはじめ', 'にわたって', 'に際して'],
        correctIndex: 0,
        grammarFocus: '〜に応じて customized flexibility based on criteria',
        ruleHint: 'Tailoring the renovation proposal to fit the customer\'s financial budget.',
        explanations: [
          {
            text: 'に応じて',
            isCorrect: true,
            reason: 'Correct! ご予算に応じて means "tailored flexibly to match your budget".'
          },
          {
            text: 'をはじめ',
            isCorrect: false,
            reason: 'Incorrect. をはじめ means "starting with representative example".'
          },
          {
            text: 'にわたって',
            isCorrect: false,
            reason: 'Incorrect. にわたって measures time/geographic expanse.'
          },
          {
            text: 'に際して',
            isCorrect: false,
            reason: 'Incorrect. に際して means "on the ceremonial occasion of".'
          }
        ]
      }
    ],
    nextPointId: undefined,
    prevPointId: 'gp-ni-tsurete',
    tags: ['N2', 'SKM N2 Ch9', 'Customization', 'Flexibility']
  }
];

