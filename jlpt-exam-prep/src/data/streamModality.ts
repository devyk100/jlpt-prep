import { GrammarPoint } from '../types';

export const STREAM_MODALITY_POINTS: GrammarPoint[] = [
  {
    id: 'gp-hazuda-kamoshirenai',
    title: '〜はずだ vs 〜かもしれない (Logical Expectation vs Unverified Possibility)',
    meaning: '〜はずだ: It should be so / I expect it based on solid evidence or calculation. 〜かもしれない: It might be so (unverified possibility ranging from 10% to 50%).',
    level: 'N4',
    streamId: 'stream-modality',
    streamName: 'Epistemic Certainty, Conviction & Duty',
    connection: '〜はずだ: Plain form (V / い形) + はずだ / な形 + なはずだ / N + のはずだ | 〜かもしれない: Plain form (without だ) + かもしれない',
    nuance: 'Notice connection: With nouns, はず demands の (田中さんの職務のはずだ), whereas かもしれない attaches bare to nouns without だ (雨かもしれない, NOT 雨だかもしれない ❌). Furthermore, 〜はずがない means "there is no logical way that... (complete disbelief)".',
    keyTakeaway: 'MUG-UP: Noun + [のはずだ]. Noun (bare) + [かもしれない] (no だ!).',
    sentences: [
      {
        id: 's-hazu-1',
        japanese: '彼は日本に５年間も留学していたのだから、日本語がペラペラなはずだ。',
        english: 'Since he studied abroad in Japan for as long as five years, he should be fluent in Japanese.',
        literal: 'He Japan-in 5-years studied because, Japanese fluent-should-be.',
        nuanceNote: 'Solid deduction based on the logical premise of a 5-year stay in Japan.',
        tokens: [
          { word: '彼は', reading: 'かれは', romaji: 'kare wa', meaning: 'he', pos: 'Pronoun' },
          { word: '日本に', reading: 'にほんに', romaji: 'nihon ni', meaning: 'in Japan', pos: 'Noun' },
          { word: '５年間も', reading: 'ごねんかんも', romaji: 'gonenkan mo', meaning: 'as long as 5 years', pos: 'Noun' },
          { word: '留学していたのだから', reading: 'りゅうがくしていたのだから', romaji: 'ryuugaku shite ita no da kara', meaning: 'because he studied abroad', pos: 'Grammar' },
          { word: '日本語が', reading: 'にほんごが', romaji: 'nihongo ga', meaning: 'Japanese language', pos: 'Noun' },
          { word: 'ペラペラなはずだ', reading: 'ペラペラなはずだ', romaji: 'perapera na hazu da', meaning: 'should be fluent', pos: 'Grammar', nuance: 'Na-adj + なはずだ' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-hazu-1',
        question: '今日は日曜日だから、市役所は休み（　　）だ。',
        translation: 'Because today is Sunday, the city hall should be closed.',
        options: ['のはず', 'はず', 'なはず', 'であるはず'],
        correctIndex: 0,
        grammarFocus: '〜はずだ noun connection with の',
        ruleHint: 'Noun (休み) connects to はず via particle の.',
        explanations: [
          {
            text: 'のはず',
            isCorrect: true,
            reason: 'Correct! Noun + の + はず forms 休みのはずだ ("should be closed").'
          },
          {
            text: 'はず',
            isCorrect: false,
            reason: 'Incorrect. Nouns cannot connect directly to はず without の.'
          },
          {
            text: 'なはず',
            isCorrect: false,
            reason: 'Incorrect. な is for な-adjectives, but 休み is a noun.'
          },
          {
            text: 'であるはず',
            isCorrect: false,
            reason: 'Incorrect. While grammatically possible in hyper-formal writing, のはず is the natural standard Japanese pattern.'
          }
        ]
      }
    ],
    nextPointId: 'gp-wake-trio',
    prevPointId: undefined,
    tags: ['N4', 'Genki L14', 'Expectation', 'Possibility']
  },

  {
    id: 'gp-wake-trio',
    title: 'The "Wake" Trio: わけだ vs わけがない vs わけではない',
    meaning: '1) 〜わけだ: Naturally so / That explains why! 2) 〜わけがない: There is absolutely NO WAY (logical impossibility)! 3) 〜わけではない: It doesn\'t necessarily mean that (partial negation).',
    level: 'N3',
    streamId: 'stream-modality',
    streamName: 'Epistemic Certainty, Conviction & Duty',
    connection: 'Plain form (V / い形 / な形-な / N-の/な) + わけだ / わけがない / わけではない',
    nuance: 'The ultimate Japanese logic pillar! わけ signifies the internal reason/logic of the universe. わけだ = "The puzzle pieces fit, now I understand why it\'s cold!" わけがない = "Such a thing defies all reason and reality!" わけではない = "Don\'t jump to conclusions; it\'s not that I hate it, I\'m just full."',
    keyTakeaway: 'MUG-UP: わけだ (That explains it!), わけがない (Impossible!), わけではない (Not necessarily so!).',
    sentences: [
      {
        id: 's-wake-1',
        japanese: 'エアコンが故障しているのか。部屋がこんなに蒸し暑いわけだ。',
        english: 'So the air conditioner is broken? That explains why the room is so sweltering hot!',
        literal: 'Air-conditioner broken is? Room this-much humid-hot natural-reason is.',
        nuanceNote: 'Aha-moment realization: discovering the broken AC explains the sweltering heat.',
        tokens: [
          { word: 'エアコンが', reading: 'エアコンが', romaji: 'eakon ga', meaning: 'air conditioner', pos: 'Noun' },
          { word: '故障しているのか', reading: 'こしょうしているのか', romaji: 'koshou shite iru no ka', meaning: 'is broken?', pos: 'Verb' },
          { word: '部屋が', reading: 'へやが', romaji: 'heya ga', meaning: 'room', pos: 'Noun' },
          { word: 'こんなに', reading: 'こんなに', romaji: 'konna ni', meaning: 'this much / so', pos: 'Adverb' },
          { word: '蒸し暑いわけだ', reading: 'むしあついわけだ', romaji: 'mushiatsui wake da', meaning: 'naturally so / explains why it is hot', pos: 'Grammar' }
        ]
      },
      {
        id: 's-wake-2',
        japanese: '日本食が嫌いなわけではないが、納豆だけはどうしても苦手だ。',
        english: 'It isn\'t that I dislike Japanese food, but natto is the one thing I just can\'t stomach.',
        literal: 'Japanese-food dislike not-necessarily, natto only by-all-means weak-at is.',
        nuanceNote: 'Partial negation: softening the statement to prevent misunderstanding.',
        tokens: [
          { word: '日本食が', reading: 'にほんしょくが', romaji: 'nihonshoku ga', meaning: 'Japanese food', pos: 'Noun' },
          { word: '嫌いなわけではないが', reading: 'きらいなわけではないが', romaji: 'kiraina wake de wa nai ga', meaning: 'it does not mean I dislike, but', pos: 'Grammar', nuance: 'Na-adj + なわけではない' },
          { word: '納豆だけは', reading: 'なっとうだけは', romaji: 'nattou dake wa', meaning: 'natto specifically', pos: 'Noun' },
          { word: 'どうしても', reading: 'どうしても', romaji: 'doushitemo', meaning: 'no matter what / by all means', pos: 'Adverb' },
          { word: '苦手だ', reading: 'にがてだ', romaji: 'nigate da', meaning: 'bad with / dislike', pos: 'Na-Adj' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-wake-1',
        question: 'あんなに誠実な彼が、仲間のお金を盗む（　　）。絶対に誤解だ。',
        translation: 'There is absolutely no way that a man as sincere as him would steal his companions\' money. It is definitely a misunderstanding.',
        options: ['わけがない', 'わけだ', 'わけではない', 'ものだ'],
        correctIndex: 0,
        grammarFocus: '〜わけがない absolute logical impossibility',
        ruleHint: 'Pairs with 絶対に誤解だ expressing total conviction that he couldn\'t have done it.',
        explanations: [
          {
            text: 'わけがない',
            isCorrect: true,
            reason: 'Correct! 「〜わけがない」 asserts complete logical impossibility: "there is no way he would steal!".'
          },
          {
            text: 'わけだ',
            isCorrect: false,
            reason: 'Incorrect. わけだ would mean "that explains why he stole", directly contradicting his sincere reputation.'
          },
          {
            text: 'わけではない',
            isCorrect: false,
            reason: 'Incorrect. わけではない means "it doesn\'t necessarily mean...", which is too weak and contradicts "definitely a misunderstanding".'
          },
          {
            text: 'ものだ',
            isCorrect: false,
            reason: 'Incorrect. ものだ expresses general truths, nostalgias, or social norms.'
          }
        ]
      }
    ],
    nextPointId: 'gp-ni-chigainai',
    prevPointId: 'gp-hazuda-kamoshirenai',
    tags: ['N3', 'SKM N3 Ch10', 'Logic', 'Negation']
  },

  {
    id: 'gp-ni-chigainai',
    title: '〜に違いない（にちがいない） (Must be / Strong subjective certainty)',
    meaning: 'The speaker feels overwhelmingly certain that something is true, based on intuitive conviction or compelling circumstantial evidence.',
    level: 'N3',
    streamId: 'stream-modality',
    streamName: 'Epistemic Certainty, Conviction & Duty',
    connection: 'Plain form (V / い形 / な形 / N) + に違いない (NO だ with な-adj or Nouns!)',
    nuance: 'CONTRAST WITH はずだ: はずだ is based on external objective calculations or promises (train timetable, contracts). に違いない is the speaker\'s intense subjective conviction ("Looking at his pale face, he MUST be sick!"). In casual speech, contracted to 〜に違いない / 〜に決まっている.',
    keyTakeaway: 'MUG-UP: Noun / な-adj (bare) + に違いない. "There is zero doubt in my mind!"',
    sentences: [
      {
        id: 's-chigai-1',
        japanese: '現場に彼の手袋が落ちていたのなら、犯人は彼に違いない。',
        english: 'If his glove was left dropped at the crime scene, the culprit must be him without a doubt.',
        literal: 'Scene-at his glove fallen-was if, culprit he must-be.',
        nuanceNote: 'Strong, unshakeable deduction from damning physical evidence.',
        tokens: [
          { word: '現場に', reading: 'げんばに', romaji: 'genba ni', meaning: 'at the scene', pos: 'Noun' },
          { word: '彼の手袋が', reading: 'かれのてぶくろが', romaji: 'kare no tebukuro ga', meaning: 'his glove', pos: 'Noun' },
          { word: '落ちていたのなら', reading: 'おちていたのなら', romaji: 'ochite ita no nara', meaning: 'if it was dropped', pos: 'Grammar' },
          { word: '犯人は', reading: 'はんにんは', romaji: 'hannin wa', meaning: 'culprit / perpetrator', pos: 'Noun' },
          { word: '彼に違いない', reading: 'かれにちがいない', romaji: 'kare ni chigainai', meaning: 'must be him without a doubt', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-chigai-1',
        question: '朝から何も口にしていないのだから、彼は今とても（　　）に違いない。',
        translation: 'Since he hasn\'t eaten a single bite since morning, he must be extremely hungry right now without a doubt.',
        options: ['お腹が空いている', 'お腹が空くだろう', 'お腹が空いたこと', 'お腹が空かない'],
        correctIndex: 0,
        grammarFocus: '〜に違いない connection with current continuous state',
        ruleHint: 'Connects directly to the state of being currently hungry.',
        explanations: [
          {
            text: 'お腹が空いている',
            isCorrect: true,
            reason: 'Correct! V-ている form (お腹が空いている) + に違いない conveys "he must be hungry right now".'
          },
          {
            text: 'お腹が空くだろう',
            isCorrect: false,
            reason: 'Incorrect. だろう cannot be nested inside に違いない.'
          },
          {
            text: 'お腹が空いたこと',
            isCorrect: false,
            reason: 'Incorrect. Adding こと is redundant and ungrammatical here.'
          },
          {
            text: 'お腹が空かない',
            isCorrect: false,
            reason: 'Incorrect. Negative form contradicts having eaten nothing all day.'
          }
        ]
      }
    ],
    nextPointId: 'gp-ni-hokaranaranai',
    prevPointId: 'gp-wake-trio',
    tags: ['N3', 'SKM N3 Ch10', 'Certainty']
  },

  {
    id: 'gp-ni-hokaranaranai',
    title: '〜にほかならない (Is nothing other than... / Absolutely none other than)',
    meaning: 'Strongly and authoritatively declaring that X is the sole, definitive cause or essence of something: "It is nothing other than X."',
    level: 'N2',
    streamId: 'stream-modality',
    streamName: 'Epistemic Certainty, Conviction & Duty',
    connection: 'N + にほかならない | から + にほかならない (Because of none other than...)',
    nuance: 'Formal, assertive, and philosophical. Frequently appears in conclusion paragraphs of JLPT N2/N1 essays and editorial speeches: "This victory is due to nothing other than our team\'s unflagging efforts" (チームの努力の賜物にほかならない).',
    keyTakeaway: 'MUG-UP: [Noun / 理由] + にほかならない = "It is definitively X and nothing else!"',
    sentences: [
      {
        id: 's-hoka-1',
        japanese: '彼が今回の難関プロジェクトを成功させることができたのは、日頃の弛まぬ努力の結果にほかならない。',
        english: 'That he was able to make this formidable project a success is nothing other than the result of his constant daily efforts.',
        literal: 'He formidable project succeed-cause able-was that-which, daily unflagging effort result nothing-other-than.',
        nuanceNote: 'Categorical attribution of success solely to steadfast diligence.',
        tokens: [
          { word: '彼が', reading: 'かれが', romaji: 'kare ga', meaning: 'he', pos: 'Pronoun' },
          { word: '今回の', reading: 'こんかいの', romaji: 'konkai no', meaning: 'this time\'s', pos: 'Noun' },
          { word: '難関プロジェクトを', reading: 'なんかんプロジェクトを', romaji: 'nankan purojekuto o', meaning: 'formidable project', pos: 'Noun' },
          { word: '成功させることができたのは', reading: 'せいこうさせることができたのは', romaji: 'seikou saseru koto ga dekita no wa', meaning: 'being able to make succeed', pos: 'Grammar' },
          { word: '日頃の', reading: 'ひごろの', romaji: 'higoro no', meaning: 'daily / everyday', pos: 'Noun' },
          { word: '弛まぬ努力の', reading: 'たゆまぬどりょくの', romaji: 'tayumanu doryoku no', meaning: 'unflagging effort\'s', pos: 'Noun' },
          { word: '結果にほかならない', reading: 'けっかにほかならない', romaji: 'kekka ni hokaranaranai', meaning: 'is nothing other than the result', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-hoka-1',
        question: '親が子供に対して厳しく叱るのは、将来を真剣に心配している（　　）にほかならない。',
        translation: 'That parents scold their children strictly is out of nothing other than serious concern for their future.',
        options: ['から', 'ので', 'ため', 'あげく'],
        correctIndex: 0,
        grammarFocus: '〜からにほかならない reason attribution pattern',
        ruleHint: 'Pairs with the reason clause (心配しているから) + にほかならない.',
        explanations: [
          {
            text: 'から',
            isCorrect: true,
            reason: 'Correct! 「〜からにほかならない」 is the standard formula declaring "it is precisely because of X and nothing else".'
          },
          {
            text: 'ので',
            isCorrect: false,
            reason: 'Incorrect. ので cannot pair directly with にほかならない.'
          },
          {
            text: 'ため',
            isCorrect: false,
            reason: 'Incorrect. Would require ためである or ためにほかならない without duplicate phrasing.'
          },
          {
            text: 'あげく',
            isCorrect: false,
            reason: 'Incorrect. あげく denotes the bitter end of an ordeal.'
          }
        ]
      }
    ],
    nextPointId: 'gp-kkonai-kanenai',
    prevPointId: 'gp-ni-chigainai',
    tags: ['N2', 'SKM N2 Ch21', 'Definitive Truth', 'Formal']
  },

  {
    id: 'gp-kkonai-kanenai',
    title: '〜っこない vs 〜かねない vs 〜かねる (Impossibility vs Danger vs Polite Hesitation)',
    meaning: '1) 〜っこない: No way in hell / absolutely impossible (spoken conviction). 2) 〜かねない: Might result in something terrible (grave danger). 3) 〜かねる: Hesitate / cannot bring myself to do (formal polite refusal).',
    level: 'N2',
    streamId: 'stream-modality',
    streamName: 'Epistemic Certainty, Conviction & Duty',
    connection: 'All attach to V-stem (ます形 without ます)! V-stem + っこない / かねない / かねる',
    nuance: 'THE TRIPLE JLPT N2 TRAP: Notice that 〜かねない ends in ない (negative appearance), but means POSITIVE DANGER ("it might very well happen!"). 〜かねる ends affirmative, but means CANNOT ("I am unable to accept"). 〜っこない is forceful conversational rejection ("I could never run a marathon!").',
    keyTakeaway: 'MUG-UP: かねない = "Bad thing MIGHT happen!" かねる = "Politely cannot do." っこない = "No chance!"',
    sentences: [
      {
        id: 's-kane-1',
        japanese: 'こんな大雨の中でスピードを出しすぎると、大事故を起こしかねない。',
        english: 'If you speed in this heavy rain, you might very well cause a major accident.',
        literal: 'This heavy-rain inside speed excess-produce-if, major-accident cause-danger-exists.',
        nuanceNote: 'Warning about a severe, dangerous risk that could easily manifest.',
        tokens: [
          { word: 'こんな', reading: 'こんな', romaji: 'konna', meaning: 'such / this kind of', pos: 'Determiner' },
          { word: '大雨の中で', reading: 'おおあめのなかで', romaji: 'ooame no naka de', meaning: 'in this heavy rain', pos: 'Noun' },
          { word: 'スピードを', reading: 'スピードを', romaji: 'supiido o', meaning: 'speed', pos: 'Noun' },
          { word: '出しすぎると', reading: 'だしすぎると', romaji: 'dashi sugiru to', meaning: 'if you exceed / produce too much', pos: 'Verb' },
          { word: '大事故を', reading: 'だいじこを', romaji: 'daijiko o', meaning: 'major accident', pos: 'Noun' },
          { word: '起こしかねない', reading: 'おこしかねない', romaji: 'okoshikanenai', meaning: 'might very well cause (danger)', pos: 'Grammar', nuance: 'Stem 起こし + かねない' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-kane-1',
        question: '申し訳ございませんが、個人情報に関わるお問い合わせにはお答えいたし（　　）。',
        translation: 'We are terribly sorry, but we cannot answer inquiries involving personal information.',
        options: ['かねます', 'かねないです', 'っこないです', 'すぎます'],
        correctIndex: 0,
        grammarFocus: '〜かねる polite business refusal',
        ruleHint: 'Polite refusal in customer service attaches to stem: いたしかねます (we cannot do).',
        explanations: [
          {
            text: 'かねます',
            isCorrect: true,
            reason: 'Correct! 「いたしかねます」 is the quintessential business Japanese phrase politely refusing an impossible request.'
          },
          {
            text: 'かねないです',
            isCorrect: false,
            reason: 'Incorrect. かねない means "there is a dangerous risk that we will answer", which is completely backwards.'
          },
          {
            text: 'っこないです',
            isCorrect: false,
            reason: 'Incorrect. っこない is casual/colloquial and highly rude in formal customer service.'
          },
          {
            text: 'すぎます',
            isCorrect: false,
            reason: 'Incorrect. すぎます means "doing excessively".'
          }
        ]
      }
    ],
    nextPointId: undefined,
    prevPointId: 'gp-ni-hokaranaranai',
    tags: ['N2', 'SKM N2 Ch18', 'Risk', 'Polite Refusal', 'Spoken']
  }
];

