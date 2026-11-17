import { GrammarPoint } from '../types';

export const STREAM_CAUSALITY_POINTS: GrammarPoint[] = [
  {
    id: 'gp-kara-node',
    title: '〜から vs 〜ので (Subjective Reason vs Objective Cause)',
    meaning: 'Explaining why something happened. から is subjective, emotional, or gives commands; ので is polite, objective, and softens requests.',
    level: 'N5',
    streamId: 'stream-causality',
    streamName: 'Causal Chains & Regret',
    connection: '〜から: Plain/Polite form + から | 〜ので: Verb/い形 plain + ので / な形 + なので / N + なので',
    nuance: 'Notice: If you give a direct command or invitation (〜てください, 〜ましょう), you MUST use から (危ないから、触らないで). Using ので with strong commands can feel stiff or contradictory because ので sounds like an objective circumstance beyond speaker control.',
    keyTakeaway: 'MUG-UP: な-adj / Noun + なので (NOT だので ❌). Use から for commands and suggestions.',
    sentences: [
      {
        id: 's-kara-1',
        japanese: '危ないですから、黄色い線の内側にお下がりください。',
        english: 'Because it is dangerous, please step back behind the yellow line.',
        literal: 'Dangerous is because, yellow line\'s inside-to step-back please.',
        nuanceNote: 'Polite station announcement with direct request/instruction to passengers.',
        tokens: [
          { word: '危ない', reading: 'あぶない', romaji: 'abunai', meaning: 'dangerous', pos: 'I-Adj' },
          { word: 'ですから', reading: 'ですから', romaji: 'desu kara', meaning: 'because it is', pos: 'Grammar' },
          { word: '黄色い', reading: 'きいろい', romaji: 'kiiroi', meaning: 'yellow', pos: 'I-Adj' },
          { word: '線', reading: 'せん', romaji: 'sen', meaning: 'line', pos: 'Noun' },
          { word: 'の', reading: 'の', romaji: 'no', meaning: 'possessive', pos: 'Particle' },
          { word: '内側', reading: 'うちがわ', romaji: 'uchigawa', meaning: 'inside', pos: 'Noun' },
          { word: 'に', reading: 'に', romaji: 'ni', meaning: 'target/direction', pos: 'Particle' },
          { word: 'お下がりください', reading: 'おさがりください', romaji: 'osagari kudasai', meaning: 'please step back (keigo)', pos: 'Keigo Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-kara-1',
        question: '明日は大事な試験が（　　）から、今夜は早く寝ようと思う。',
        translation: 'Because I have an important exam tomorrow, I think I will go to bed early tonight.',
        options: ['ある', 'あって', 'あり', 'あろう'],
        correctIndex: 0,
        grammarFocus: '〜から plain form connection',
        ruleHint: 'Connects to standard plain/polite predicative forms.',
        explanations: [
          {
            text: 'ある',
            isCorrect: true,
            reason: 'Correct! Plain non-past ある connects cleanly to から.'
          },
          {
            text: 'あって',
            isCorrect: false,
            reason: 'Incorrect. Te-form cannot connect directly to から.'
          },
          {
            text: 'あり',
            isCorrect: false,
            reason: 'Incorrect. Stem form あり is ungrammatical before から.'
          },
          {
            text: 'あろう',
            isCorrect: false,
            reason: 'Incorrect. Volitional form cannot be used as the factual condition here.'
          }
        ]
      }
    ],
    nextPointId: 'gp-te-shimau',
    prevPointId: undefined,
    tags: ['N5', 'Genki L9', 'Reason']
  },

  {
    id: 'gp-te-shimau',
    title: '〜てしまう / 〜ちゃう (Irreversible Completion & Regret)',
    meaning: '1) Completely finished doing something to the end. 2) Done by accident or mistake with deep regret ("Oh no, I did it!").',
    level: 'N4',
    streamId: 'stream-causality',
    streamName: 'Causal Chains & Regret',
    connection: 'V-て + しまう (Spoken contractions: 〜てしまう → 〜ちゃう / 〜でしまう → 〜じゃう)',
    nuance: 'Crucial dual nature: Sometimes it means proud complete accomplishment (本を全部読んでしまった = I read the whole book!), but overwhelmingly on JLPT tests it signifies unintentional mistake and regret (財布を落としてしまった = I lost my wallet, alas).',
    keyTakeaway: 'MUG-UP: V-てしまう = Complete finish OR irreversible regret. Contracted: 忘れちゃった!',
    sentences: [
      {
        id: 's-teshimau-1',
        japanese: '電車の網棚に大切な書類の入ったバッグを忘れてしまった。',
        english: 'I accidentally left my bag with important documents on the train\'s luggage rack.',
        literal: 'Train luggage-rack on important documents entered bag forgot-regretfully.',
        nuanceNote: 'Deep remorse and frustration over an irreversible blunder.',
        tokens: [
          { word: '電車', reading: 'でんしゃ', romaji: 'densha', meaning: 'train', pos: 'Noun' },
          { word: 'の', reading: 'の', romaji: 'no', meaning: 'possessive', pos: 'Particle' },
          { word: '網棚', reading: 'あみだな', romaji: 'amidana', meaning: 'overhead luggage rack', pos: 'Noun' },
          { word: 'に', reading: 'に', romaji: 'ni', meaning: 'location marker', pos: 'Particle' },
          { word: '大切な', reading: 'たいせつな', romaji: 'taisetsuna', meaning: 'important', pos: 'Na-Adj' },
          { word: '書類', reading: 'しょるい', romaji: 'shorui', meaning: 'documents / papers', pos: 'Noun' },
          { word: 'の', reading: 'の', romaji: 'no', meaning: 'subject in relative clause', pos: 'Particle' },
          { word: '入った', reading: 'はいった', romaji: 'haitta', meaning: 'contained / entered', pos: 'Verb (Past)' },
          { word: 'バッグ', reading: 'バッグ', romaji: 'baggu', meaning: 'bag', pos: 'Noun' },
          { word: 'を', reading: 'を', romaji: 'o', meaning: 'object marker', pos: 'Particle' },
          { word: '忘れてしまった', reading: 'わすれてしまった', romaji: 'wasurete shimatta', meaning: 'left behind / forgot regretfully', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-teshimau-1',
        question: '急いでいたので、違う色の靴下を（　　）しまった。',
        translation: 'Because I was in a hurry, I ended up putting on different-colored socks by mistake.',
        options: ['履いて', '履く', '履き', '履いた'],
        correctIndex: 0,
        grammarFocus: '〜てしまう te-form connection',
        ruleHint: 'Connects to the te-form (履いて).',
        explanations: [
          {
            text: '履いて',
            isCorrect: true,
            reason: 'Correct! 履く (to wear shoes/socks) becomes 履いて in te-form, forming 履いてしまった.'
          },
          {
            text: '履く',
            isCorrect: false,
            reason: 'Incorrect. Dictionary form cannot connect to しまう.'
          },
          {
            text: '履き',
            isCorrect: false,
            reason: 'Incorrect. Masu-stem 履き does not connect to しまう.'
          },
          {
            text: '履いた',
            isCorrect: false,
            reason: 'Incorrect. Past form 履いた cannot precede しまう.'
          }
        ]
      }
    ],
    nextPointId: 'gp-okage-sei',
    prevPointId: 'gp-kara-node',
    tags: ['N4', 'Genki L18', 'Regret']
  },

  {
    id: 'gp-okage-sei',
    title: '〜おかげで vs 〜せいで (Gratitude vs Blame)',
    meaning: '〜おかげで: Thanks to X, a good outcome Y resulted. 〜せいで: Because of X (blaming X), a terrible outcome Y resulted.',
    level: 'N3',
    streamId: 'stream-causality',
    streamName: 'Causal Chains & Regret',
    connection: 'Plain form (V / い形) + おかげで / せいで | な形 + な + おかげで / せいで | N + の + おかげで / せいで',
    nuance: 'Irony note: Sometimes おかげで is used sarcastically ("Thanks to your terrible driving, we are lost"), but on the JLPT, treat おかげで as POSITIVE and せいで as NEGATIVE BLAME! You can also end a sentence with 〜せいだ / 〜おかげだ.',
    keyTakeaway: 'MUG-UP: おかげで = Gratitude (Positive). せいで = Blame (Negative). Noun + の + おかげ/せい.',
    sentences: [
      {
        id: 's-okage-1',
        japanese: '先生の熱心なご指導のおかげで、無事に合格することができました。',
        english: 'Thanks to the teacher\'s enthusiastic guidance, I was able to pass safely.',
        literal: 'Teacher\'s enthusiastic guidance\'s thanks-to, safely pass doing was-able-to.',
        nuanceNote: 'Expresses genuine gratitude towards a benefactor.',
        tokens: [
          { word: '先生', reading: 'せんせい', romaji: 'sensei', meaning: 'teacher', pos: 'Noun' },
          { word: 'の', reading: 'の', romaji: 'no', meaning: 'possessive', pos: 'Particle' },
          { word: '熱心な', reading: 'ねっしんな', romaji: 'nesshinna', meaning: 'enthusiastic / earnest', pos: 'Na-Adj' },
          { word: 'ご指導', reading: 'ごしどう', romaji: 'goshidou', meaning: 'guidance (honorific)', pos: 'Noun' },
          { word: 'のおかげで', reading: 'のおかげで', romaji: 'no okage de', meaning: 'thanks to', pos: 'Grammar' },
          { word: '無事に', reading: 'ぶじに', romaji: 'buji ni', meaning: 'safely / without trouble', pos: 'Adverb' },
          { word: '合格することができました', reading: 'ごうかくすることができました', romaji: 'goukaku suru koto ga dekimashita', meaning: 'was able to pass', pos: 'Verb' }
        ]
      },
      {
        id: 's-sei-1',
        japanese: '台風のせいで、楽しみにしていた週末の花火大会が中止になってしまった。',
        english: 'Because of the typhoon, the weekend fireworks festival I was looking forward to got cancelled.',
        literal: 'Typhoon\'s fault-because, looking-forward-was weekend fireworks festival cancellation became-regretfully.',
        nuanceNote: 'Blaming the typhoon for ruining anticipated plans.',
        tokens: [
          { word: '台風', reading: 'たいふう', romaji: 'taifuu', meaning: 'typhoon', pos: 'Noun' },
          { word: 'のせいで', reading: 'のせいで', romaji: 'no sei de', meaning: 'because of (blame)', pos: 'Grammar' },
          { word: '楽しみにしていた', reading: 'たのしみにしていた', romaji: 'tanoshimi ni shite ita', meaning: 'was looking forward to', pos: 'Verb (Past)' },
          { word: '週末', reading: 'しゅうまつ', romaji: 'shuumatsu', meaning: 'weekend', pos: 'Noun' },
          { word: 'の', reading: 'の', romaji: 'no', meaning: 'possessive', pos: 'Particle' },
          { word: '花火大会', reading: 'はなびたいかい', romaji: 'hanabi taikai', meaning: 'fireworks festival', pos: 'Noun' },
          { word: 'が', reading: 'が', romaji: 'ga', meaning: 'subject marker', pos: 'Particle' },
          { word: '中止になってしまった', reading: 'ちゅうしになってしまった', romaji: 'chuushi ni natte shimatta', meaning: 'ended up cancelled', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-okage-1',
        question: '隣の部屋の騒音の（　　）、昨夜は一睡もできなかった。',
        translation: 'Because of the noise from the next room, I couldn\'t sleep a wink last night.',
        options: ['せいで', 'おかげで', 'ために', 'ばかりに'],
        correctIndex: 0,
        grammarFocus: '〜せいで negative blame attribution',
        ruleHint: 'Insomnia is an unpleasant outcome, so blame (せいで) is required.',
        explanations: [
          {
            text: 'せいで',
            isCorrect: true,
            reason: 'Correct! Not being able to sleep is a terrible outcome blamed entirely on the noise.'
          },
          {
            text: 'おかげで',
            isCorrect: false,
            reason: 'Incorrect. おかげで requires a positive/beneficial result.'
          },
          {
            text: 'ために',
            isCorrect: false,
            reason: 'Incorrect. While ために indicates cause, Noun connects as 騒音のために, and せいで conveys personal grievance far more naturally here.'
          },
          {
            text: 'ばかりに',
            isCorrect: false,
            reason: 'Incorrect. ばかりに connects directly to verbs or clauses (〜たばかりに) to mean "simply because of one slight mistake", not Noun のばかりに.'
          }
        ]
      }
    ],
    nextPointId: 'gp-bakarini',
    prevPointId: 'gp-te-shimau',
    tags: ['N3', 'SKM N3 Ch5', 'Gratitude', 'Blame']
  },

  {
    id: 'gp-bakarini',
    title: '〜ばかりに (Simply because of... a catastrophic outcome)',
    meaning: 'Simply because of that one single thing / trivial action, an unexpectedly terrible, disastrous result happened.',
    level: 'N3',
    streamId: 'stream-causality',
    streamName: 'Causal Chains & Regret',
    connection: 'V-た / い形 / な形-な / N-である + ばかりに',
    nuance: 'Expresses deep bite-your-tongue regret and frustration: "If only I hadn\'t done that one little thing, this catastrophe wouldn\'t have occurred!" The result clause is ALWAYS negative, tragic, or disadvantageous.',
    keyTakeaway: 'MUG-UP: V-た + ばかりに + [DISASTROUS OUTCOME]. Pure remorse.',
    sentences: [
      {
        id: 's-bakarini-1',
        japanese: '嘘をついたばかりに、親友からの信頼を完全に失ってしまった。',
        english: 'Simply because I told a lie, I completely lost the trust of my best friend.',
        literal: 'Lie told simply-because, best-friend from trust completely lost-regretfully.',
        nuanceNote: 'One lie (trivial action) spiraled into complete loss of friendship (disaster).',
        tokens: [
          { word: '嘘', reading: 'うそ', romaji: 'uso', meaning: 'lie', pos: 'Noun' },
          { word: 'を', reading: 'を', romaji: 'o', meaning: 'object marker', pos: 'Particle' },
          { word: 'ついた', reading: 'ついた', romaji: 'tsuita', meaning: 'told (a lie)', pos: 'Verb (Past)' },
          { word: 'ばかりに', reading: 'ばかりに', romaji: 'bakari ni', meaning: 'simply because of', pos: 'Grammar' },
          { word: '親友', reading: 'しんゆう', romaji: 'shin\'yuu', meaning: 'best friend', pos: 'Noun' },
          { word: 'からの', reading: 'からの', romaji: 'kara no', meaning: 'from', pos: 'Particle' },
          { word: '信頼', reading: 'しんらい', romaji: 'shinrai', meaning: 'trust / confidence', pos: 'Noun' },
          { word: 'を', reading: 'を', romaji: 'o', meaning: 'object marker', pos: 'Particle' },
          { word: '完全に', reading: 'かんぜんに', romaji: 'kanzen ni', meaning: 'completely', pos: 'Adverb' },
          { word: '失ってしまった', reading: 'うしなってしまった', romaji: 'ushinatte shimatta', meaning: 'lost regretfully', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-bakarini-1',
        question: '道を一本（　　）ばかりに、飛行機の出発時刻に間に合わなかった。',
        translation: 'Simply because I took one wrong turn, I failed to make the flight\'s departure time.',
        options: ['間違えた', '間違える', '間違えて', '間違えそう'],
        correctIndex: 0,
        grammarFocus: '〜ばかりに past tense connection',
        ruleHint: 'Connects to past form (間違えた) to mark the single fateful past mistake.',
        explanations: [
          {
            text: '間違えた',
            isCorrect: true,
            reason: 'Correct! V-た (間違えた) + ばかりに highlights the single mistake that triggered missing the plane.'
          },
          {
            text: '間違える',
            isCorrect: false,
            reason: 'Incorrect. Non-past dictionary form is rare and does not fit a past missed flight.'
          },
          {
            text: '間違えて',
            isCorrect: false,
            reason: 'Incorrect. Te-form cannot attach directly to ばかりに.'
          },
          {
            text: '間違えそう',
            isCorrect: false,
            reason: 'Incorrect. 〜そう (looks like) does not connect to ばかりに.'
          }
        ]
      }
    ],
    nextPointId: 'gp-monodakara',
    prevPointId: 'gp-okage-sei',
    tags: ['N3', 'SKM N3 Ch5', 'Disaster', 'Regret']
  },

  {
    id: 'gp-monodakara',
    title: '〜ものだから / 〜もので (Social Excuse / "It couldn\'t be helped")',
    meaning: 'Giving a personal explanation or mild excuse to justify why you were late, couldn\'t attend, or failed to do something.',
    level: 'N3',
    streamId: 'stream-causality',
    streamName: 'Causal Chains & Regret',
    connection: 'Plain form + ものだから / もので | な形 + な + ものだから | N + な + ものだから',
    nuance: 'Subtle psychology: It appeals to the listener\'s empathy! "The circumstances were such that any reasonable person would have done the same." In casual conversation, contracted to 〜もんだから or simply 〜もん (childish/informal excuse).',
    keyTakeaway: 'MUG-UP: [Circumstance] + なものだから = "Please forgive me, it was unavoidable circumstances!"',
    sentences: [
      {
        id: 's-monodakara-1',
        japanese: '途中で事故渋滞に巻き込まれたものだから、集合時間に遅れてしまいました。',
        english: 'Because I got caught in an accident traffic jam on the way, I unfortunately ended up late for the meeting time.',
        literal: 'On-the-way accident congestion in wrapped-was because, gathering time to was-late.',
        nuanceNote: 'Polite, empathetic excuse explaining an unavoidable delay.',
        tokens: [
          { word: '途中で', reading: 'とちゅうで', romaji: 'tochuu de', meaning: 'on the way', pos: 'Noun' },
          { word: '事故渋滞', reading: 'じこじゅうたい', romaji: 'jiko juutai', meaning: 'accident traffic jam', pos: 'Noun' },
          { word: 'に', reading: 'に', romaji: 'ni', meaning: 'target/source', pos: 'Particle' },
          { word: '巻き込まれた', reading: 'まきこまれた', romaji: 'makikomareta', meaning: 'got wrapped/caught up in', pos: 'Verb (Passive)' },
          { word: 'ものだから', reading: 'ものだから', romaji: 'mono dakara', meaning: 'because (social excuse)', pos: 'Grammar' },
          { word: '集合時間', reading: 'しゅうごうじかん', romaji: 'shuugou jikan', meaning: 'meeting / assembly time', pos: 'Noun' },
          { word: 'に', reading: 'に', romaji: 'ni', meaning: 'time marker', pos: 'Particle' },
          { word: '遅れてしまいました', reading: 'おくれてしまいました', romaji: 'okurete shimaimashita', meaning: 'regretfully ended up late', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-monodakara-1',
        question: 'あまりに（　　）ものだから、ついダイエット中なのにケーキを食べてしまった。',
        translation: 'Because it looked so utterly delicious, I ended up eating cake even though I was in the middle of a diet.',
        options: ['美味しそうだった', '美味しい', '美味しそうだ', '美味しかった'],
        correctIndex: 0,
        grammarFocus: '〜ものだから justification for temptation',
        ruleHint: 'Looking delicious (past appearance) triggered the lapse in diet.',
        explanations: [
          {
            text: '美味しそうだった',
            isCorrect: true,
            reason: 'Correct! "Because it looked so delicious" explains the uncontrollable urge to eat the cake.'
          },
          {
            text: '美味しい',
            isCorrect: false,
            reason: 'Incorrect. You hadn\'t tasted it yet; it was the visual appeal (そう) that tempted you.'
          },
          {
            text: '美味しそうだ',
            isCorrect: false,
            reason: 'Incorrect. Needs past tense or proper connective な before もの.'
          },
          {
            text: '美味しかった',
            isCorrect: false,
            reason: 'Incorrect. Focusing on past taste fails to explain the initial temptation.'
          }
        ]
      }
    ],
    nextPointId: 'gp-karaniwa',
    prevPointId: 'gp-bakarini',
    tags: ['N3', 'SKM N3 Ch5', 'Excuse', 'Social']
  },

  {
    id: 'gp-karaniwa',
    title: '〜からには / 〜以上（は） (Now that... I must naturally / Resolute commitment)',
    meaning: 'Now that situation X has become reality, it is only natural, proper, and obligatory that course Y must follow.',
    level: 'N3',
    streamId: 'stream-causality',
    streamName: 'Causal Chains & Regret',
    connection: 'Plain form (V / い形 / な形である / Nである) + からには / 以上（は）',
    nuance: 'Strong moral conviction and determination! The second clause almost ALWAYS ends in volition, necessity, or command: 〜つもりだ, 〜べきだ, 〜なければならない, or 〜てください. Never used for passive accidental results.',
    keyTakeaway: 'MUG-UP: 〜からには + [強い意志・義務・覚悟] (つもリだ、べきだ、〜てみせる).',
    sentences: [
      {
        id: 's-karaniwa-1',
        japanese: 'JLPT N2を受験すると決めたからには、最後まで諦めずに全力で勉強するつもりだ。',
        english: 'Now that I have decided to take the JLPT N2, I intend to study with all my might until the very end without giving up.',
        literal: 'JLPT N2 take-exam that decided now-that, last until not-giving-up full-power study intend.',
        nuanceNote: 'Unwavering resolve and personal accountability following a commitment.',
        tokens: [
          { word: 'JLPT N2', reading: 'エヌに', romaji: 'en-ni', meaning: 'JLPT N2', pos: 'Noun' },
          { word: 'を', reading: 'を', romaji: 'o', meaning: 'object marker', pos: 'Particle' },
          { word: '受験すると', reading: 'じゅけんすると', romaji: 'juken suru to', meaning: 'to take exam (quote)', pos: 'Verb' },
          { word: '決めたからには', reading: 'きめたからには', romaji: 'kimeta kara ni wa', meaning: 'now that decided', pos: 'Grammar' },
          { word: '最後まで', reading: 'さいごまで', romaji: 'saigo made', meaning: 'until the end', pos: 'Adverb' },
          { word: '諦めずに', reading: 'あきらめずに', romaji: 'akiramezu ni', meaning: 'without giving up', pos: 'Adverb' },
          { word: '全力で', reading: 'ぜんりょくで', romaji: 'zenryoku de', meaning: 'with all one\'s power', pos: 'Adverb' },
          { word: '勉強するつもりだ', reading: 'べんきょうするつもりだ', romaji: 'benkyou suru tsumori da', meaning: 'intend to study', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-karaniwa-1',
        question: '一度引き受けた（　　）、どんなに困難でも責任を持ってやり遂げるべきだ。',
        translation: 'Now that you have accepted the task, no matter how difficult it is, you ought to see it through with responsibility.',
        options: ['からには', 'あまり', 'あげく', '末に'],
        correctIndex: 0,
        grammarFocus: '〜からには moral duty and resolve',
        ruleHint: 'Pairs with べきだ (ought to) expressing moral accountability.',
        explanations: [
          {
            text: 'からには',
            isCorrect: true,
            reason: 'Correct! "Now that you took on the job, you must finish it" is the signature meaning of からには.'
          },
          {
            text: 'あまり',
            isCorrect: false,
            reason: 'Incorrect. あまり means "due to excessive emotion/stress, an abnormal result occurred".'
          },
          {
            text: 'あげく',
            isCorrect: false,
            reason: 'Incorrect. あげく means "after a long struggle, ended up with a bad result".'
          },
          {
            text: '末に',
            isCorrect: false,
            reason: 'Incorrect. 末に means "after a long process, a decision was reached", without the moral command tone.'
          }
        ]
      }
    ],
    nextPointId: 'gp-amari',
    prevPointId: 'gp-monodakara',
    tags: ['N3', 'SKM N3 Ch5', 'Resolve', 'Duty']
  },

  {
    id: 'gp-amari',
    title: '〜あまり (Excessive emotion leading to abnormal outcome)',
    meaning: 'Because an emotion, stress, or excitement was so overwhelming and extreme, an abnormal, unusual, or out-of-control result occurred.',
    level: 'N2',
    streamId: 'stream-causality',
    streamName: 'Causal Chains & Regret',
    connection: 'V-辞書形 / V-た + あまり | N + の + あまり',
    nuance: 'The trigger MUST be an intense psychological state (喜び, 緊張, 怒り, 心配, 悲哀). The outcome is something the subject couldn\'t prevent—such as fainting, bursting into tears, or making a shocking blunder.',
    keyTakeaway: 'MUG-UP: [強い感情的名詞] + のあまり + [異常な結果] (e.g. 緊張のあまり声が出なかった).',
    sentences: [
      {
        id: 's-amari-1',
        japanese: '面接の際、極度の緊張のあまり、用意していた自己紹介の言葉が全部飛んでしまった。',
        english: 'During the interview, out of extreme nervousness, the self-introduction words I had prepared completely vanished from my mind.',
        literal: 'Interview occasion-at, extreme nervousness\'s excess-at, prepared self-intro words all flew-regretfully.',
        nuanceNote: 'Paralyzing stress causing mind to go completely blank.',
        tokens: [
          { word: '面接の際', reading: 'めんせつのさい', romaji: 'mensetsu no sai', meaning: 'on the occasion of interview', pos: 'Grammar' },
          { word: '極度の', reading: 'きょくどの', romaji: 'kyokudo no', meaning: 'extreme degree of', pos: 'Noun' },
          { word: '緊張のあまり', reading: 'きんちょうのあまり', romaji: 'kinchou no amari', meaning: 'out of extreme nervousness', pos: 'Grammar' },
          { word: '用意していた', reading: 'よういしていた', romaji: 'youi shite ita', meaning: 'had prepared', pos: 'Verb (Past)' },
          { word: '自己紹介', reading: 'じこしょうかい', romaji: 'jikoshoukai', meaning: 'self-introduction', pos: 'Noun' },
          { word: 'の言葉が', reading: 'のことばが', romaji: 'no kotoba ga', meaning: 'words of', pos: 'Noun' },
          { word: '全部', reading: 'ぜんぶ', romaji: 'zenbu', meaning: 'all', pos: 'Adverb' },
          { word: '飛んでしまった', reading: 'とんでしまった', romaji: 'tonde shimatta', meaning: 'vanished / flew away', pos: 'Verb' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-amari-1',
        question: '母は私の合格通知を見て、嬉しさの（　　）大声を上げて泣き崩れた。',
        translation: 'Seeing my acceptance letter, my mother broke down in tears and shouted out of sheer joy.',
        options: ['あまり', 'おかげで', 'せいで', '次第'],
        correctIndex: 0,
        grammarFocus: '〜あまり emotional overload outcome',
        ruleHint: 'Noun (嬉しさ) + の + あまり signifies overflowing joy inducing tears.',
        explanations: [
          {
            text: 'あまり',
            isCorrect: true,
            reason: 'Correct! 嬉しさのあまり expresses joy so intense that it caused her to cry uncontrollably.'
          },
          {
            text: 'おかげで',
            isCorrect: false,
            reason: 'Incorrect. おかげで explains logical gratitude, not an involuntary psychological reflex.'
          },
          {
            text: 'せいで',
            isCorrect: false,
            reason: 'Incorrect. せいで implies blame for a bad thing, but acceptance is a wonderful event.'
          },
          {
            text: '次第',
            isCorrect: false,
            reason: 'Incorrect. 次第 means "as soon as (business)" and cannot connect to an emotion noun in this way.'
          }
        ]
      }
    ],
    nextPointId: 'gp-ageku',
    prevPointId: 'gp-karaniwa',
    tags: ['N2', 'SKM N2 Ch17', 'Emotion Overload']
  },

  {
    id: 'gp-ageku',
    title: '〜あげく / 〜あげくに (After prolonged ordeal... ended up with a bad result)',
    meaning: 'After undergoing a prolonged process of agonizing, arguing, or struggling, the final outcome was unfortunately bad or wasted effort.',
    level: 'N2',
    streamId: 'stream-causality',
    streamName: 'Causal Chains & Regret',
    connection: 'V-た + あげく / N + の + あげく',
    nuance: 'CONTRAST WITH 〜末に (すえに): 〜末に can end in either a good or bad major decision (e.g. 苦労の末に成功した). But 〜あげく ALMOST ALWAYS ends in disappointment, exhaustion, or a terrible outcome (e.g. argued for 3 hours, ended up breaking up).',
    keyTakeaway: 'MUG-UP: V-たあげく = Long hassle -> Disappointing/bad result. 末に = Long struggle -> Final resolution (good or bad).',
    sentences: [
      {
        id: 's-ageku-1',
        japanese: '何時間も迷いに迷ったあげく、結局何も買わずに店を出てしまった。',
        english: 'After hesitating and agonizing for hours, in the end I left the store without buying anything.',
        literal: 'Many-hours agonizing-agonized end-in, eventually nothing buying-without store exited-regretfully.',
        nuanceNote: 'Huge expenditure of time and mental energy with zero fruit to show for it.',
        tokens: [
          { word: '何時間も', reading: 'なんじかんも', romaji: 'nanjikan mo', meaning: 'for many hours', pos: 'Adverb' },
          { word: '迷いに迷った', reading: 'まよいにまよった', romaji: 'mayoi ni mayotta', meaning: 'agonized and hesitated endlessly', pos: 'Verb (Past)' },
          { word: 'あげく', reading: 'あげく', romaji: 'ageku', meaning: 'after all that (negative)', pos: 'Grammar' },
          { word: '結局', reading: 'けっきょく', romaji: 'kekkyoku', meaning: 'in the end / after all', pos: 'Adverb' },
          { word: '何も', reading: 'なにも', romaji: 'nanimo', meaning: 'nothing', pos: 'Adverb' },
          { word: '買わずに', reading: 'かわずに', romaji: 'kawazu ni', meaning: 'without buying', pos: 'Adverb' },
          { word: '店を', reading: 'みせを', romaji: 'mise o', meaning: 'store', pos: 'Noun' },
          { word: '出てしまった', reading: 'でてしまった', romaji: 'dete shimatta', meaning: 'ended up leaving', pos: 'Grammar' }
        ]
      }
    ],
    quiz: [
      {
        id: 'q-ageku-1',
        question: '夫婦で散々（　　）あげく、結局離婚することになってしまった。',
        translation: 'After arguing endlessly as husband and wife, in the end they unfortunately ended up getting divorced.',
        options: ['口論した', '口論する', '口論して', '口論しようと'],
        correctIndex: 0,
        grammarFocus: '〜あげく past tense connection',
        ruleHint: 'Connects to the past (た) form of the exhausting struggle.',
        explanations: [
          {
            text: '口論した',
            isCorrect: true,
            reason: 'Correct! V-た (口論した) + あげく accurately highlights the prolonged arguing that concluded in divorce.'
          },
          {
            text: '口論する',
            isCorrect: false,
            reason: 'Incorrect. Dictionary form cannot connect to あげく when describing a completed history.'
          },
          {
            text: '口論して',
            isCorrect: false,
            reason: 'Incorrect. Te-form cannot connect to あげく.'
          },
          {
            text: '口論しようと',
            isCorrect: false,
            reason: 'Incorrect. Volitional form does not fit.'
          }
        ]
      }
    ],
    nextPointId: undefined,
    prevPointId: 'gp-amari',
    tags: ['N2', 'SKM N2 Ch20', 'Futile Ordeal', 'Disappointment']
  }
];

