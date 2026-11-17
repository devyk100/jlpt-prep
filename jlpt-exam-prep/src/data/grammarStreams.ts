import type { StreamCategory } from '../types';

export const STREAM_CATEGORIES: StreamCategory[] = [
  {
    id: 'stream-time',
    title: 'Chronos & Instant Transitions',
    japaneseTitle: '時・継起・瞬間の推移',
    description: 'From simple time markers (~とき, ~ながら) to split-second disruptions (~最中に, ~うちに) and immediate sequence (~たとたん, ~か〜ないかのうちに, ~次第).',
    iconName: 'Clock',
    grammarIds: ['gp-toki', 'gp-nagara', 'gp-uchini', 'gp-saichuu', 'gp-totan', 'gp-kato-omou-to', 'gp-kanai-ka', 'gp-shidai']
  },
  {
    id: 'stream-causality',
    title: 'Causal Chains & Regret',
    japaneseTitle: '原因・理由・言い訳・結末',
    description: 'From direct causes (~から, ~ので) to positive/negative blame (~おかげで, ~せいで), personal excuses (~ものだから), and harsh outcomes (~あまり, ~あげく).',
    iconName: 'GitCommit',
    grammarIds: ['gp-kara-node', 'gp-te-shimau', 'gp-okage-sei', 'gp-bakarini', 'gp-monodakara', 'gp-karaniwa', 'gp-amari', 'gp-ageku']
  },
  {
    id: 'stream-conditionals',
    title: 'Conditional Horizons & Prerequisites',
    japaneseTitle: '条件・仮定・前提条件',
    description: 'Master the classic trap of と vs ば vs たら vs なら, progressing into prerequisite emphasis (~さえ〜ば), hypothetical suppositions (~としたら), and strict prerequisites (~ないことには, ~ものなら).',
    iconName: 'GitFork',
    grammarIds: ['gp-conditionals-four', 'gp-sae-ba', 'gp-toshitara', 'gp-mononara', 'gp-naikotoniwa']
  },
  {
    id: 'stream-limits',
    title: 'Boundaries, Exclusivity & Scope',
    japaneseTitle: '限定・範囲・付加の極限',
    description: 'From elementary limits (~だけ, ~しか〜ない) to span markers (~をはじめ, ~にわたって, ~を通じて) and tight restrictions (~に限り, ~に限って, ~ばかりか).',
    iconName: 'Maximize2',
    grammarIds: ['gp-dake-shika', 'gp-wo-hajime', 'gp-ni-watatte', 'gp-wo-tsuujite', 'gp-ni-kagiri', 'gp-ni-kagitte', 'gp-bakarika']
  },
  {
    id: 'stream-contrasts',
    title: 'Contrasts, Concessions & Defiance',
    japaneseTitle: '逆接・対比・予想の裏切り',
    description: 'From ~のに and ~ても to expectation-defiers (~わりに, ~にしては), balanced facets (~反面, ~一方), and extreme contrasts (~ものの, ~どころか).',
    iconName: 'Repeat',
    grammarIds: ['gp-noni-temo', 'gp-warini-nishiteha', 'gp-hanmen-ippou', 'gp-monono', 'gp-dokoroka']
  },
  {
    id: 'stream-modality',
    title: 'Epistemic Certainty, Conviction & Duty',
    japaneseTitle: '推量・確信・否定・義務',
    description: 'From ~かもしれない and ~はずだ to logical deductions (~わけだ, ~わけがない, ~わけではない), absolute certainty (~に違いない, ~にほかならない), and impossibility (~っこない, ~かねない).',
    iconName: 'Compass',
    grammarIds: ['gp-hazuda-kamoshirenai', 'gp-wake-trio', 'gp-ni-chigainai', 'gp-ni-hokaranaranai', 'gp-kkonai-kanenai']
  },
  {
    id: 'stream-social',
    title: 'Social Transactions, Hierarchy & Favors',
    japaneseTitle: '授受・受身使役・敬語・衝動',
    description: 'Giving and receiving favors (~てあげる, ~てくれる, ~てもらう), the voice transformation ladder (受身, 使役, 使役受身), keigo survival, and uncontrollable inner urges (~てたまらない, ~ざるを得ない).',
    iconName: 'Users',
    grammarIds: ['gp-giving-receiving', 'gp-voice-ladder', 'gp-keigo-core', 'gp-tamaranai-naranai', 'gp-zaruwokenai']
  },
  {
    id: 'stream-trends',
    title: 'Trends, Changes & Proportional Evolution',
    japaneseTitle: '変化・傾向・相関の進展',
    description: 'From steady trends (~一方だ, ~ばかりだ) to proportional parallel evolution (~につれて, ~にしたがって) and customized flexibility (~に応じて).',
    iconName: 'TrendingUp',
    grammarIds: ['gp-ippouda', 'gp-ni-tsurete', 'gp-ni-oujite']
  },
  {
    id: 'stream-topics',
    title: 'Topic Framing, Criteria & Disregard',
    japaneseTitle: '話題提示・基準・無関係',
    description: 'Astounding degrees (~といったら), barrier-breaking inclusivity (~を問わず), prioritizing pragmatic focus (~はともかく), source materials (~をもとに, ~に基づいて), and subjective value (~に対して, ~にとって).',
    iconName: 'HelpCircle',
    grammarIds: ['gp-to-ittara', 'gp-wo-towazu', 'gp-ha-tomokaku', 'gp-motoni-motozuite', 'gp-ni-taishite']
  }
];
