import type { GrammarPoint } from '../types';

export const STREAM_TOPICS_POINTS: GrammarPoint[] = [
  {
    id: 'gp-to-ittara',
    title: '〜といったら / 〜といえば (When talking about... astounding degree!)',
    meaning: '1) 〜といったら: When it comes to the astonishing degree of X, words can hardly describe it! 2) 〜といえば: Speaking of topic X, something associated immediately comes to mind.',
    level: 'N2',
    streamId: 'stream-topics',
    streamName: 'Topic Framing, Criteria & Disregard',
    connection: 'N + といったら / といえば',
    nuance: 'Astonishment marker! With といったら, it brings up an extreme quality and emphasizes how staggering, breathtaking, or awful it was: 富士山の山頂から見た日の出の美しさといったら、言葉にできないほどだった ("As for the beauty of that sunrise, it was beyond words!").',
    keyTakeaway: 'MUG-UP: [極端な感情的名詞] + といったら + [言葉にできないほどの驚き].',
    sentences: [
      {
        id: 's-toittara-1',
        japanese: '真夏の満員電車の息苦しさといったら、本当に耐えられないほどだった。',
        english: 'As for the suffocating stuffiness of the packed commuter train in midsummer, it was truly unbearable.',
        literal: 'Midsummer packed-train\'s stuffiness talking-of, truly endure-cannot extent was.',
        nuanceNote: 'Evokes visceral horror and staggering discomfort.',
        tokens: [
          { word: '真夏の', reading: 'まなつの', romaji: 'manatsu no', meaning: 'midsummer\'s', pos: 'Noun' },
          { word: '満員電車の', reading: 'まんいんでんしゃの', romaji: 'man\'in densha no', meaning: 'packed train\'s', pos: 'Noun' },
          { word: '息苦しさといったら', reading: 'いきぐるしさといったら', romaji: 'ikigurushisa to ittara', meaning: 'talking of the stuffiness', pos: 'Grammar' },
          { word: '本当に', reading: 'ほんとうに', romaji: 'hontou ni', meaning: 'truly', pos: 'Adverb' },
          { word: '耐えられないほど', reading: 'たえられないほど', romaji: 'taerarenai hodo', meaning: 'to the extent of unbearable', pos: 'Grammar' },
          { word: 'だった', reading: 'だった', romaji: 'datta', meaning: 'was', pos: 'Copula' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-toittara-1',
        question: '初めて満点のテストを見た時の母の喜び（　　）、家中を飛び跳ねていた。',
        translation: 'As for my mother\'s joy when seeing my perfect test score for the first time, she was literally jumping around the house.',
        options: ['といったら', 'を通じて', 'にわたって', 'にあたって'],
        correctIndex: 0,
        grammarFocus: '〜といったら astounding emotional degree',
        ruleHint: 'Highlights the mother\'s overflowing, astonishing joy.',
        explanations: [
          {
            text: 'といったら',
            isCorrect: true,
            reason: 'Correct! 「母の喜びといったら」 brings up her joy and stresses its astounding, animated intensity.'
          },
          {
            text: 'を通じて',
            isCorrect: false,
            reason: 'Incorrect. を通じて means "throughout or via".'
          },
          {
            text: 'にわたって',
            isCorrect: false,
            reason: 'Incorrect. にわたって measures numerical duration/expanse.'
          },
          {
            text: 'にあたって',
            isCorrect: false,
            reason: 'Incorrect. にあたって means "on the threshold of a momentous event".'
          }
        ]
      }
    ],
    nextPointId: 'gp-wo-towazu',
    prevPointId: undefined,
    tags: ['N2', 'SKM N2 Ch13', 'Astonishing Degree', 'Topic']
  },

  {
    id: 'gp-wo-towazu',
    title: '〜を問わず（をとわず） (Regardless of... / Open to all)',
    meaning: 'Without being limited or restricted by conditions X (such as age, gender, nationality, experience, or weather).',
    level: 'N2',
    streamId: 'stream-topics',
    streamName: 'Topic Framing, Criteria & Disregard',
    connection: 'N (Contrasting pair or broad category: 年齢, 性別, 国籍, 昼夜, 経験) + を問わず',
    nuance: 'Official, welcoming, or inclusive announcements: "Recruiting participants regardless of age or gender" (年齢や性別を問わず募集). It explicitly removes discriminatory or selective barriers.',
    keyTakeaway: 'MUG-UP: [対立概念・広範な属性] + を問わず (e.g. 昼夜を問わず, 経験を問わず).',
    sentences: [
      {
        id: 's-towazu-1',
        japanese: 'このボランティア活動は、年齢や国籍を問わず、どなたでも自由にご参加いただけます。',
        english: 'Anyone is welcome to freely participate in this volunteer activity, regardless of age or nationality.',
        literal: 'This volunteer activity, age and nationality ask-not, whoever freely participate-can.',
        nuanceNote: 'Warm, universal inclusivity eliminating all demographic barriers.',
        tokens: [
          { word: 'この', reading: 'この', romaji: 'kono', meaning: 'this', pos: 'Determiner' },
          { word: 'ボランティア活動は', reading: 'ボランティアかつどうは', romaji: 'borantia katsudou wa', meaning: 'volunteer activity', pos: 'Noun' },
          { word: '年齢や', reading: 'ねんれいや', romaji: 'nenrei ya', meaning: 'age and', pos: 'Noun' },
          { word: '国籍を問わず', reading: 'こくせきをとわず', romaji: 'kokuseki o towazu', meaning: 'regardless of nationality', pos: 'Grammar' },
          { word: 'どなたでも', reading: 'どなたでも', romaji: 'donata demo', meaning: 'anyone (polite)', pos: 'Pronoun' },
          { word: '自由に', reading: 'じゆうに', romaji: 'jiyuu ni', meaning: 'freely', pos: 'Adverb' },
          { word: 'ご参加いただけます', reading: 'ごさんかいただけます', romaji: 'gosanka itadakemasu', meaning: 'can participate (keigo)', pos: 'Keigo Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-towazu-1',
        question: '救急救命センターのスタッフは、昼夜を（　　）患者の治療に全力を尽くしている。',
        translation: 'The staff of the emergency medical center devote all their efforts to treating patients regardless of day or night.',
        options: ['問わず', '限って', 'めぐって', '沿って'],
        correctIndex: 0,
        grammarFocus: '〜を問わず paired opposites disregard',
        ruleHint: 'Connects to paired opposites (昼夜 = day and night) meaning "day or night alike".',
        explanations: [
          {
            text: '問わず',
            isCorrect: true,
            reason: 'Correct! 「昼夜を問わず」 is the established idiom meaning "day and night alike / around the clock".'
          },
          {
            text: '限って',
            isCorrect: false,
            reason: 'Incorrect. に限って means "specifically only / of all days".'
          },
          {
            text: 'めぐって',
            isCorrect: false,
            reason: 'Incorrect. をめぐって means "dispute surrounding an issue".'
          },
          {
            text: '沿って',
            isCorrect: false,
            reason: 'Incorrect. に沿って means "in accordance with a guideline".'
          }
        ]
      }
    ],
    nextPointId: 'gp-ha-tomokaku',
    prevPointId: 'gp-to-ittara',
    tags: ['N2', 'SKM N2 Ch11', 'Inclusivity', 'Disregard']
  },

  {
    id: 'gp-ha-tomokaku',
    title: '〜はともかく（として） (Setting aside X for now... what really matters is Y)',
    meaning: 'While issue X is valid or questionable, let us set it aside for now, because the core priority is factor Y.',
    level: 'N2',
    streamId: 'stream-topics',
    streamName: 'Topic Framing, Criteria & Disregard',
    connection: 'N + はともかく / はともかくとして',
    nuance: 'Priority filter: "Look, whether the design is pretty or not is beside the point for now; what matters is whether it actually works!" (デザインはともかく、使いやすさが一番だ). Pragmatic and prioritizing.',
    keyTakeaway: 'MUG-UP: [A] はともかく [Bが重要 / 優先]. Puts A on hold to focus on B.',
    sentences: [
      {
        id: 's-tomokaku-1',
        japanese: '味はともかくとして、この定食は値段が安くてボリュームが満点だ。',
        english: 'Taste aside for the moment, this set meal is inexpensive and very filling.',
        literal: 'Taste setting-aside, this set-meal price cheap volume full is.',
        nuanceNote: 'Pragmatic assessment: not winning any culinary awards, but unbeatable value.',
        tokens: [
          { word: '味はともかくとして', reading: 'あじはともかくとして', romaji: 'aji wa tomokaku to shite', meaning: 'taste aside for now', pos: 'Grammar' },
          { word: 'この', reading: 'この', romaji: 'kono', meaning: 'this', pos: 'Determiner' },
          { word: '定食は', reading: 'ていしょくは', romaji: 'teishoku wa', meaning: 'set meal', pos: 'Noun' },
          { word: '値段が', reading: 'ねだんが', romaji: 'nedan ga', meaning: 'price', pos: 'Noun' },
          { word: '安くて', reading: 'やすくて', romaji: 'yasukute', meaning: 'cheap and', pos: 'I-Adj' },
          { word: 'ボリュームが', reading: 'ボリュームが', romaji: 'boryuumu ga', meaning: 'portion volume', pos: 'Noun' },
          { word: '満点だ', reading: 'まんてんだ', romaji: 'manten da', meaning: 'perfect score / full marks', pos: 'Na-Adj' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-tomokaku-1',
        question: '結果（　　）、全力を出し切って戦った選手たちの健闘を称えたい。',
        translation: 'Setting aside the outcome for now, I want to praise the valiant fighting of the athletes who gave it their all.',
        options: ['はともかく', 'をはじめ', 'にわたって', 'のもとに'],
        correctIndex: 0,
        grammarFocus: '〜はともかく setting aside secondary result to praise effort',
        ruleHint: 'Sets aside whether they won or lost to focus on praising their heroic effort.',
        explanations: [
          {
            text: 'はともかく',
            isCorrect: true,
            reason: 'Correct! 「結果はともかく」 sets aside the final score to applaud their unwavering dedication.'
          },
          {
            text: 'をはじめ',
            isCorrect: false,
            reason: 'Incorrect. をはじめ means "starting with representative example".'
          },
          {
            text: 'にわたって',
            isCorrect: false,
            reason: 'Incorrect. にわたって measures time/spatial expanse.'
          },
          {
            text: 'のもとに',
            isCorrect: false,
            reason: 'Incorrect. のもとに means "under the supervision/guidance of".'
          }
        ]
      }
    ],
    nextPointId: 'gp-motoni-motozuite',
    prevPointId: 'gp-wo-towazu',
    tags: ['N2', 'SKM N2 Ch11', 'Priority', 'Setting Aside']
  },

  {
    id: 'gp-motoni-motozuite',
    title: '〜をもとに vs 〜に基づいて (Creative Material vs Statutory / Fact Basis)',
    meaning: '〜をもとに: Using raw materials, real stories, or data as creative inspiration to build something new. 〜に基づいて: Strictly adhering to formal laws, data, principles, or regulations as statutory foundation.',
    level: 'N3',
    streamId: 'stream-topics',
    streamName: 'Topic Framing, Criteria & Disregard',
    connection: 'N + をもとに / をもとにして | N + に基づいて / に基づく + N',
    nuance: 'CONTRAST: If a novelist writes a book inspired by a true event, use をもとに (実話をもとにした小説). If a judge passes a verdict based on the constitution, use に基づいて (法律に基づいて判決を下す). に基づいて demands strict fidelity to rules and hard facts.',
    keyTakeaway: 'MUG-UP: もとに = Creative base / raw material. 基づいて = Legal, factual, rigorous foundation.',
    sentences: [
      {
        id: 's-moto-1',
        japanese: 'この映画は、実際に起きた歴史的事件をもとにして制作された。',
        english: 'This movie was produced based upon a historical event that actually occurred.',
        literal: 'This movie, actually occurred historical event based-upon produced was.',
        nuanceNote: 'Creative adaptation taking a real historical occurrence as source material.',
        tokens: [
          { word: 'この映画は', reading: 'このえいがは', romaji: 'kono eiga wa', meaning: 'this movie', pos: 'Noun' },
          { word: '実際に', reading: 'じっさいに', romaji: 'jissai ni', meaning: 'actually', pos: 'Adverb' },
          { word: '起きた', reading: 'おきた', romaji: 'okita', meaning: 'occurred', pos: 'Verb (Past)' },
          { word: '歴史的事件を', reading: 'れきしてきじけんを', romaji: 'rekishiteki jiken o', meaning: 'historical incident', pos: 'Noun' },
          { word: 'もとにして', reading: 'もとにして', romaji: 'moto ni shite', meaning: 'based upon (creative material)', pos: 'Grammar' },
          { word: '制作された', reading: 'せいさくされた', romaji: 'seisaku sareta', meaning: 'was produced', pos: 'Verb (Passive)' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-moto-1',
        question: '最新の調査データ（　　）、今後のマーケティング戦略を慎重に策定した。',
        translation: 'Based strictly upon the latest survey data, we formulated our future marketing strategy with care.',
        options: ['に基づいて', 'をはじめ', 'をめぐって', 'に際して'],
        correctIndex: 0,
        grammarFocus: '〜に基づいて rigorous factual data foundation',
        ruleHint: 'Business strategy formulated upon analytical data requires に基づいて.',
        explanations: [
          {
            text: 'に基づいて',
            isCorrect: true,
            reason: 'Correct! 「最新の調査データに基づいて」 represents a rigorous, empirical foundation for decision-making.'
          },
          {
            text: 'をはじめ',
            isCorrect: false,
            reason: 'Incorrect. をはじめ introduces a representative example.'
          },
          {
            text: 'をめぐって',
            isCorrect: false,
            reason: 'Incorrect. をめぐって indicates dispute/conflict surrounding an issue.'
          },
          {
            text: 'に際して',
            isCorrect: false,
            reason: 'Incorrect. に際して means "on the ceremonial occasion of".'
          }
        ]
      }
    ],
    nextPointId: 'gp-ni-taishite',
    prevPointId: 'gp-ha-tomokaku',
    tags: ['N3', 'SKM N3 Ch3', 'SKM N2 Ch8', 'Bases', 'Rules']
  },

  {
    id: 'gp-ni-taishite',
    title: '〜に対して vs 〜にとって (Target / Contrast vs Personal Perspective)',
    meaning: '〜に対して: 1) Toward person/target (attitude/action). 2) In stark contrast to A, B is... 〜にとって: From the subjective perspective / standard of evaluating value for person X ("For me, this is important").',
    level: 'N3',
    streamId: 'stream-topics',
    streamName: 'Topic Framing, Criteria & Disregard',
    connection: 'N + に対して / に対する + N | N + にとって / にとっての + N',
    nuance: 'THE CLASSIC JLPT N3/N2 CONFUSION: Notice the direction! にとって evaluates psychological value or impact on the person ("To a child, play is education"). に対して directs an action or emotion outward toward an external target ("Be polite towards customers: お客様に対して丁寧にしなさい").',
    keyTakeaway: 'MUG-UP: にとって = "In my eyes / For me" (Value judgment). に対して = "Aimed toward target" OR "In contrast to".',
    sentences: [
      {
        id: 's-tai-1',
        japanese: '活発で外遊びが好きな兄に対して、弟は家の中で読書をするのが好きだ。',
        english: 'In contrast to the older brother who is active and loves playing outdoors, the younger brother loves reading books inside.',
        literal: 'Active and outdoors-play liking older-brother in-contrast-to, younger-brother house inside reading like.',
        nuanceNote: 'Direct, balanced contrast between two opposite personalities.',
        tokens: [
          { word: '活発で', reading: 'かっぱつで', romaji: 'kappatsu de', meaning: 'active / lively and', pos: 'Na-Adj' },
          { word: '外遊びが', reading: 'そとあそびが', romaji: 'sotoasobi ga', meaning: 'playing outdoors', pos: 'Noun' },
          { word: '好きな', reading: 'すきな', romaji: 'sukina', meaning: 'liked', pos: 'Na-Adj' },
          { word: '兄に対して', reading: 'あににたいして', romaji: 'ani ni taishite', meaning: 'in contrast to the older brother', pos: 'Grammar' },
          { word: '弟は', reading: 'おとうとは', romaji: 'otouto wa', meaning: 'younger brother', pos: 'Noun' },
          { word: '家の中で', reading: 'いえのなかで', romaji: 'ie no naka de', meaning: 'inside the house', pos: 'Noun' },
          { word: '読書をするのが', reading: 'どくしょをするのが', romaji: 'dokusho o suru no ga', meaning: 'reading books', pos: 'Noun' },
          { word: '好きだ', reading: 'すきだ', romaji: 'suki da', meaning: 'likes', pos: 'Na-Adj' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-tai-1',
        question: '外国語を習得することは、私（　　）世界への視野を広げる最高の冒険だ。',
        translation: 'Acquiring a foreign language is, for me, the ultimate adventure that expands my perspective on the world.',
        options: ['にとって', 'に対して', 'を通じて', 'にわたって'],
        correctIndex: 0,
        grammarFocus: '〜にとって subjective value evaluation',
        ruleHint: 'Expresses the speaker\'s personal subjective standard of value (私にとって...最高の冒険だ).',
        explanations: [
          {
            text: 'にとって',
            isCorrect: true,
            reason: 'Correct! 「私にとって」 expresses "from my perspective / in my eyes, it is the greatest adventure".'
          },
          {
            text: 'に対して',
            isCorrect: false,
            reason: 'Incorrect. に対して means "directed toward someone" or "in stark contrast to", which does not evaluate personal meaning.'
          },
          {
            text: 'を通じて',
            isCorrect: false,
            reason: 'Incorrect. を通じて means "through or via a medium".'
          },
          {
            text: 'にわたって',
            isCorrect: false,
            reason: 'Incorrect. にわたって measures time or spatial expanse.'
          }
        ]
      }
    ],
    nextPointId: undefined,
    prevPointId: 'gp-motoni-motozuite',
    tags: ['N3', 'SKM N3 Ch3', 'Perspective', 'Contrast']
  }
];

