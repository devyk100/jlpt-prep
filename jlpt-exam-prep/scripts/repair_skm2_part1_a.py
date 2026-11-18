import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"

exercises = json.load(open(EXERCISES_PATH, encoding="utf-8"))

# Master repair mapping for SKM N2 Part 1 Chapters 1–12 (144 items)
# Each item has: trans, ctx, opt_reasons, evid
REPAIRS_1_12 = {
    # --- Chapter 1: 時・時の関係 - 1 (〜とき・〜の直後) pp. 18–21 ---
    "skm2-p1-c1-q1": {
        "trans": "Prior to commencing the construction of the new factory, an explanatory briefing for neighborhood residents was held.",
        "ctx": "Community engagement prior to major industrial construction.",
        "opt_reasons": {
            "たとたん": "直後の偶発的現象を表す表現であり、意図的な事前準備の文脈に合いません。",
            "かと思うと": "先行事態の直後に予想外の急変が起きる対比であり、計画的説明会の開催に不適です。",
            "うちに": "時間的制限内の行動を表しますが、事業開始直前の公式準備には「にあたって」が最適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 1, Practice Drills, pp. 18–21"
    },
    "skm2-p1-c1-q2": {
        "trans": "On the momentous occasion of the Olympic opening ceremony, the athlete delegations of nations worldwide conducted their entrance parade.",
        "ctx": "Ceremonial procedures at global sporting spectacles.",
        "opt_reasons": {
            "次第": "事態完了後の即時意志行動（〜し次第）を表し、大行事の冒頭という機会を表せません。",
            "末に": "長時間の苦難の末の結末を表すため、開会式の入場行進に合いません。",
            "あげく": "散々〜した挙げ句の悪い結果を表すマイナス表現で、祝賀行事に極めて不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 1, Practice Drills, pp. 18–21"
    },
    "skm2-p1-c1-q3": {
        "trans": "When enrolling in overseas travel insurance, I verified every single contractual clause with utmost care.",
        "ctx": "Reviewing insurance legal documentation upon policy enrollment.",
        "opt_reasons": {
            "とたん": "直後に起きた突発的事態を表し、契約手続きを行う改まった「時」を表せません。",
            "最中": "動作の真最中を表すため、「加入する（未完了）」という手続きの機会指定に合いません。",
            "一方": "並行推移や対比を表す表現であり、契約行為の時点指定として機能しません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 1, Practice Drills, pp. 18–21"
    },
    "skm2-p1-c1-q4": {
        "trans": "The moment I opened the door, a cold gust of wind blew in and scattered the paperwork.",
        "ctx": "Sudden environmental interruption scattering paperwork.",
        "opt_reasons": {
            "にあたって": "重大事業の開始直前の準備・心構えを表すため、冷風が吹き込んだ偶発突発事態に合いません。",
            "に際して": "公式・格式張った機会を表す硬い表現であり、日常の突発的風の侵入に不適です。",
            "次第": "意志的な行動への移行を表すため、風で書類が散らばった無意志現象に接続できません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 1, Practice Drills, pp. 18–21"
    },
    "skm2-p1-c1-q5": {
        "trans": "No sooner had the baby finally stopped crying than it began wailing loudly all over again.",
        "ctx": "Observing sudden emotional reversals in infant crying.",
        "opt_reasons": {
            "にあたって": "事業やイベントの開始に際する配慮を表すため、赤ちゃんの泣き出しに合いません。",
            "上で": "先行手続きを踏まえた行動を表すため、直後の急変・再発を表せません。",
            "て以来": "過去の時点から現在まで同じ状態が続く表現であり、即座の急変に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 1, Practice Drills, pp. 18–21"
    },
    "skm2-p1-c1-q6": {
        "trans": "Hardly had the starting pistol sounded before the athletes dashed out all at once aiming for the finish line.",
        "ctx": "Athletes bursting off starting blocks at the signal.",
        "opt_reasons": {
            "にあたって": "事前準備を表すため、合図直後の瞬間的な猛ダッシュに合いません。",
            "際に": "一般的な時を表す改まった表現であり、極限の僅差で飛び出した臨場感が出ません。",
            "最中に": "ピストルが鳴り響いている真最中ではなく、鳴り終わりとほぼ同時のダッシュです。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 1, Practice Drills, pp. 18–21"
    },
    "skm2-p1-c1-q7": {
        "trans": "The exam bell had scarcely stopped ringing when the examinees flipped their question sheets over simultaneously.",
        "ctx": "Immediate test-taking reactions upon the exam start bell.",
        "opt_reasons": {
            "に際して": "格式張った行事の機会を表すため、ベル直後の物理的動作の瞬間描写に合いません。",
            "とたん": "直前の動作と後続の突発事象を結びますが、鳴り終わるかどうかの極限には「〜か〜ないかのうちに」が最適です。",
            "うちに": "時間の幅を表すため、ベル停止と同時の一斉反転動作に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 1, Practice Drills, pp. 18–21"
    },
    "skm2-p1-c1-q8": {
        "trans": "Just when I thought I was watching the sunset in the western sky, the entire surroundings turned pitch dark in the blink of an eye.",
        "ctx": "Marveling at the sudden rapidity of twilight turning into night.",
        "opt_reasons": {
            "にあたって": "計画的な行動の準備を表すため、日没後の急激な暗転現象に合いません。",
            "に際して": "改まった公式の機会指定であり、自然現象の急変に対する驚きを表せません。",
            "上で": "先行行為に基づく判断を表すため、あっという間に暗くなった自然変化に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 1, Practice Drills, pp. 18–21"
    },
    "skm2-p1-c1-q9": {
        "trans": "In conjunction with the unveiling of the new product, the head of development gave a detailed presentation regarding revolutionary new features.",
        "ctx": "Corporate launch presentation delivered by R&D executives.",
        "opt_reasons": {
            "とたんに": "予期せぬ突発現象を表すため、予定された公式プレゼンテーションの実施に合いません。",
            "かと思うと": "急激な事態の反転を表すため、新商品発表の晴れの舞台の導入に不適です。",
            "うちに": "状態変化の前の時間幅を表すため、公式発表の機会そのものを指定できません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 1, Practice Drills, pp. 18–21"
    },
    "skm2-p1-c1-q10": {
        "trans": "The instant he saw my face, an expression as if he wanted to say something surfaced and he averted his eyes.",
        "ctx": "Observing sudden emotional nonverbal cues upon meeting someone.",
        "opt_reasons": {
            "に際して": "公的・格式張った機会を表すため、個人の瞬時の表情変化・視線回避に合いません。",
            "にあたって": "事前準備を表すため、顔を見た瞬間に起きた心理的リアクションに不適です。",
            "次第": "意志的な後続行動を導くため、無意識に視線を逸らした自然現象に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 1, Practice Drills, pp. 18–21"
    },
    "skm2-p1-c1-q11": {
        "trans": "Upon utilizing this service, we ask for your agreement to our terms of service beforehand.",
        "ctx": "Formal customer service guidance outlining prerequisite terms.",
        "opt_reasons": {
            "とたんに": "直後の突発事態を表すため、サービス利用の前提条件の提示に合いません。",
            "かと思ったら": "急変に対する主観的驚きを表すため、公的な利用案内に不適切です。",
            "最中に": "利用している動作の真最中を表すため、事前の同意を求める文脈と矛盾します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 1, Practice Drills, pp. 18–21"
    },
    "skm2-p1-c1-q12": {
        "trans": "No sooner had lightning flashed in the sky than a tremendous roar of thunder boomed along with ground tremors.",
        "ctx": "Immediate explosive thunderclap following a lightning strike.",
        "opt_reasons": {
            "にあたって": "準備行為を表すため、稲妻直後の雷鳴という自然の猛威に合いません。",
            "に際して": "改まった行事の機会指定であり、突発的な天候現象に不適切です。",
            "て以来": "過去の時点から現在までの継続を表すため、瞬時の雷鳴発生に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 1, Practice Drills, pp. 18–21"
    },

    # --- Chapter 2: 時・時の関係 - 2 (〜進行中・変化の過程) pp. 22–25 ---
    "skm2-p1-c2-q1": {
        "trans": "Right in the middle of an important job interview, my smartphone suddenly began ringing at full volume, causing huge fluster.",
        "ctx": "Embarrassing electronic interruption during a critical interview.",
        "opt_reasons": {
            "うちに": "時間的猶予内の行動を表すため、面接の最中に突然邪魔が入る文脈に合いません。",
            "つつ": "二つの動作の同時進行を表すため、突然の着信という突発事故に不適です。",
            "一方": "客観的な推移や対比を表すため、電話の割り込みに不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 2, Practice Drills, pp. 22–25"
    },
    "skm2-p1-c2-q2": {
        "trans": "While the hot soup has not cooled down yet, please go ahead and enjoy it without hesitation.",
        "ctx": "Hospitality encouraging guests to dine before dishes turn cold.",
        "opt_reasons": {
            "最中に": "動作の真最中を表すため、「冷めない」という状態継続に接続できません。",
            "ばかりに": "〜したことだけが原因で悪い結果になったことを表すため、食事の勧めに反します。",
            "つつも": "逆接譲歩を表すため、温かい間に食べてほしいという肯定的な勧めに合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 2, Practice Drills, pp. 22–25"
    },
    "skm2-p1-c2-q3": {
        "trans": "While practicing the same musical piece repeatedly, I became able to play it without even looking at the sheet music.",
        "ctx": "Unconscious natural skill acquisition through dedicated practice.",
        "opt_reasons": {
            "最中に": "練習の瞬間的な中断を表す語感になり、練習を重ねる中で生じた能力変化に合いません。",
            "ばかりで": "限定や不満を表すため、暗譜で弾けるようになった成長変化に不適です。",
            "一方だ": "一方向への変化の進行を表す文末表現であり、副詞節の接続形式になりません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 2, Practice Drills, pp. 22–25"
    },
    "skm2-p1-c2-q4": {
        "trans": "Under the influence of the economic downturn, the number of bankruptcies among small and medium enterprises is steadily on the rise.",
        "ctx": "Reporting relentless economic deterioration and business failures.",
        "opt_reasons": {
            "最中": "動作の真最中を表す名詞であり、継続的な増加傾向を表す文末述語になりません。",
            "うち": "時間的範囲を表す形式名詞であり、「増える一方だ」という一途な推移を示せません。",
            "つつ": "動詞連用形に接続する複文接続助詞であり、文末述語「〜一方だ」に代替できません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 2, Practice Drills, pp. 22–25"
    },
    "skm2-p1-c2-q5": {
        "trans": "Due to the prolonged heatwave, the reservoir's water storage level is only decreasing further, raising concerns over impacts on resident livelihoods.",
        "ctx": "Depleted water reserves during severe summer droughts.",
        "opt_reasons": {
            "最中": "進行中の瞬間を表すため、悪化の一途をたどる水位低下の傾向に合いません。",
            "うち": "時間幅を表す名詞であり、「減るばかりだ」というマイナス進行を表せません。",
            "つつ": "中連接続助詞であり、文末の推移述語として使えません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 2, Practice Drills, pp. 22–25"
    },
    "skm2-p1-c2-q6": {
        "trans": "From the eastern horizon, the sun heralding the dawn of a new era is steadily in the process of rising.",
        "ctx": "Poetic portrayal of sunrise signifying new historical eras.",
        "opt_reasons": {
            "ばかりだ": "マイナス方向への進行を表すことが多く、希望に満ちた夜明けの上昇に不適です。",
            "一方だ": "客観的な量的増減の加速を表すため、太陽が昇る着実な推移描写に合いません。",
            "うちだ": "時間的制限を表す名詞であり、動詞連用形に直接結んで文末を作れません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 2, Practice Drills, pp. 22–25"
    },
    "skm2-p1-c2-q7": {
        "trans": "The sun is right on the verge of sinking beyond the western mountain ridge at this very moment.",
        "ctx": "The precise instant right before twilight sunset completes.",
        "opt_reasons": {
            "ある": "「沈もうとある」という日本語表現は文法的に破綻しています。",
            "ばかりだ": "進行中の悪化傾向を表す表現であり、沈む直前の極限状態を示せません。",
            "一方だ": "一方的な変化の進行を表す表現であり、意志形「〜（よ）うとしている」と結合しません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 2, Practice Drills, pp. 22–25"
    },
    "skm2-p1-c2-q8": {
        "trans": "Even while being fully aware that it is bad for my body, I succumbed to the temptation of late-night ramen and sweet carbonated soda.",
        "ctx": "Confessing dietary lapses despite knowing health consequences.",
        "opt_reasons": {
            "うちに": "時間的猶予内の行動を表すため、「知っている」という意識と矛盾する行動の逆接になりません。",
            "最中に": "動作の真最中を表すため、心理的葛藤を抱えながらの行動に合いません。",
            "一方": "対比を表しますが、「体に毒だと知りつつも」という自覚と行動の齟齬を表せません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 2, Practice Drills, pp. 22–25"
    },
    "skm2-p1-c2-q9": {
        "trans": "Holding anxiety about their future in their hearts, young people are struggling earnestly to move forward believing in hope.",
        "ctx": "Navigating youthful uncertainties while maintaining forward momentum.",
        "opt_reasons": {
            "最中に": "突発的な妨害を表す語感になり、長期間にわたる並行した心理状態の保持に合いません。",
            "うちに": "時間幅内の変化を表すため、不安を抱きながら前進する付帯状態に不適です。",
            "一方": "対比を表す表現であり、二つの動作・心理の同時維持を表せません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 2, Practice Drills, pp. 22–25"
    },
    "skm2-p1-c2-q10": {
        "trans": "My grandfather's medical condition is only deteriorating further, despite earnest treatment by the physicians.",
        "ctx": "Lamenting unabated medical decline despite therapeutic interventions.",
        "opt_reasons": {
            "最中": "動作進行中を表すため、病状の悪化の一途をたどる客観的推移に合いません。",
            "うち": "時間幅を表す名詞であり、悪化傾向を表す文末構文になりません。",
            "つつ": "動詞連用形接続であり、「悪化する」辞書形に直接接続できません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 2, Practice Drills, pp. 22–25"
    },
    "skm2-p1-c2-q11": {
        "trans": "Right in the middle of exchanging heated discussions at the conference, the interior room lights suddenly extinguished and went dark.",
        "ctx": "Power outage disrupting intensive deliberations.",
        "opt_reasons": {
            "うちに": "状態が保たれている間の行動を表すため、議論の真っ最中の突然の消灯に合いません。",
            "ばかりに": "〜したことだけが原因でという恨み節になり、消灯の突発性に合いません。",
            "一方": "推移を表す表現であり、議論のクライマックスへの割り込みに不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 2, Practice Drills, pp. 22–25"
    },
    "skm2-p1-c2-q12": {
        "trans": "Cherry blossom buds are swelling day by day, steadily approaching full bloom with the arrival of spring.",
        "ctx": "Observing botanical transitions toward springtime blossom peaks.",
        "opt_reasons": {
            "ばかりだ": "マイナス方向の悪化を表すことが多く、美しい満開の進行に不自然です。",
            "一方だ": "歯止めの効かない増減推移を表すため、自然界の優美な開花プロセスに合いません。",
            "最中だ": "すでに満開になっている真最中を表すため、「満開を迎えつつある（直前の進行）」とズレます。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 2, Practice Drills, pp. 22–25"
    },

    # --- Chapter 3: 時・時の関係 - 3 (〜前後の関係・契機) pp. 26–29 ---
    "skm2-p1-c3-q1": {
        "trans": "Only after experiencing living alone in a foreign land did I deeply appreciate my parents' kindness and love from the bottom of my heart.",
        "ctx": "Attaining deep filial appreciation through independent living.",
        "opt_reasons": {
            "した上で": "事前手続きを完了させた後の計画的行動を表すため、身をもって初めて気づく認識の契機に合いません。",
            "次第": "完了直後の即時意志行動を表すため、親のありがたみの実感という内面変化に不適です。",
            "してからでないと": "否定・不可能の帰結と呼応するため、肯定的な気づきの述語に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 3, Practice Drills, pp. 26–29"
    },
    "skm2-p1-c3-q2": {
        "trans": "After holding thorough discussions with all internal company stakeholders, I wish to make the final executive management decision.",
        "ctx": "Executive decision-making based on prior comprehensive consultations.",
        "opt_reasons": {
            "重ねてはじめて": "初めて気づくという認識の契機になり、計画的な経営判断の下達に合いません。",
            "重ね次第": "完了直後の機械的即時行動になり、慎重な検討を経た重い経営判断に不自然です。",
            "重ねてこのかた": "その時以来ずっとという意味になり、これからの判断下達に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 3, Practice Drills, pp. 26–29"
    },
    "skm2-p1-c3-q3": {
        "trans": "As soon as I arrive on site, I will report the situation to the headquarters emergency response room immediately.",
        "ctx": "Promising immediate field status updates upon arrival.",
        "opt_reasons": {
            "てはじめて": "経験による新しい認識の獲得を表すため、到着直後の業務連絡に合いません。",
            "て以来": "過去の時点から現在までの継続を表すため、未来の到着時の報告に不適です。",
            "てからでないと": "否定条件を表すため、肯定的な報告の即時約束に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 3, Practice Drills, pp. 26–29"
    },
    "skm2-p1-c3-q4": {
        "trans": "Ever since graduating from university, I have not set foot on my hometown soil even once, and nostalgic scenes of my alma mater come to mind.",
        "ctx": "Reflecting on prolonged absence from one's hometown since graduation.",
        "opt_reasons": {
            "してはじめて": "卒業したことで初めて気づいた認識を表す表現になり、その後の長年の不在に合いません。",
            "した上で": "卒業を事前条件として次の行動に移る表現になり、長期間の継続状態に不適です。",
            "して次第": "文法的に破綻した接続であり存在しません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 3, Practice Drills, pp. 26–29"
    },
    "skm2-p1-c3-q5": {
        "trans": "Ever since my surgery ten years ago, I have been exceptionally attentive to my physical condition and maintained healthy daily habits.",
        "ctx": "Sustained health vigilance following medical procedures.",
        "opt_reasons": {
            "上で": "手続き・判断の前提を表すため、10年間の生活習慣の継続に合いません。",
            "次第": "直後の即時行動を表すため、10年にわたる継続状態の叙述に不適です。",
            "からでないと": "必要条件を表す表現であり、手術以来ずっと健康を保っている事実に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 3, Practice Drills, pp. 26–29"
    },
    "skm2-p1-c3-q6": {
        "trans": "Unless you obtain formal authorization from your supervisor first, exchanging confidential contracts on your own is strictly forbidden.",
        "ctx": "Emphasizing supervisory sign-off prerequisites before signing contracts.",
        "opt_reasons": {
            "得てはじめて": "承認を得て初めて気づくという意味になり、禁止規定の文脈に合いません。",
            "得た上で": "承認を得た上で交わす肯定的な順序を表し、後続の「絶対に許されない」という否定禁止に呼応しません。",
            "得て以来": "承認を得てからずっとという意味になり、契約前の手続き警告に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 3, Practice Drills, pp. 26–29"
    },
    "skm2-p1-c3-q7": {
        "trans": "Unless we complete the prior safety inspections first, resuming operations of the large amusement attractions is impossible.",
        "ctx": "Safety protocol compliance before restarting theme park rides.",
        "opt_reasons": {
            "させてはじめて": "点検させて初めて〜が分かったという意味になり、運航再開の不可能性に合いません。",
            "させ次第": "点検完了後に即座に再開する肯定文になり、「再開できない」という否定文と矛盾します。",
            "させて以来": "点検させてから今までという意味になり、事前点検の前提条件に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 3, Practice Drills, pp. 26–29"
    },
    "skm2-p1-c3-q8": {
        "trans": "As soon as the itinerary details are finalized, we will deliver the written invitations to all participants via postal mail.",
        "ctx": "Logistical timeline for sending finalized travel invitations.",
        "opt_reasons": {
            "てはじめて": "決定を契機として初めて認識した意味になり、案内の送付約束に合いません。",
            "て以来": "決定してからずっとという意味になり、これからの送付予定に不適切です。",
            "てからでないと": "否定条件文（〜ない）を要求するため、肯定的な発送予定に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 3, Practice Drills, pp. 26–29"
    },
    "skm2-p1-c3-q9": {
        "trans": "Only after entering real society and experiencing fierce competition was I painfully made aware of my own immaturity and lack of study.",
        "ctx": "Awakening to personal shortcomings through real-world competition.",
        "opt_reasons": {
            "経験した上で": "競争を経験した上で次の行動をとる表現になり、痛感させられた心理的自覚に合いません。",
            "経験次第": "競争を経験し次第すぐに行動するという意味になり、内省的痛感に不適です。",
            "経験してこのかた": "経験してから現在までずっとという意味になり、自覚が生じた契機の瞬間に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 3, Practice Drills, pp. 26–29"
    },
    "skm2-p1-c3-q10": {
        "trans": "Confirming the contract contents meticulously with legal counsel before executing signature and seal is the iron rule of business.",
        "ctx": "Legal review precedence prior to executing corporate agreements.",
        "opt_reasons": {
            "してはじめて": "確認して初めて気づくという意味になり、ビジネスの鉄則としての段取りに合いません。",
            "し次第": "確認が終わったら直ちに署名するというスピード重視になり、慎重な手続きの完了を前提とする語感に合いません。",
            "して以来": "確認してからずっとという意味になり、順序規定に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 3, Practice Drills, pp. 26–29"
    },
    "skm2-p1-c3-q11": {
        "trans": "Ever since that tragic accident, I have made it a personal rule to avoid driving a car alone at night.",
        "ctx": "Adopting driving cautions following a traumatic past vehicular accident.",
        "opt_reasons": {
            "上で": "事故を前提条件とする意味になり、悲惨な事故の契機以降の継続状態に合いません。",
            "次第": "事故の直後にという意味になり、長年の運転回避習慣の叙述に不適です。",
            "からでなければ": "否定条件句であり、事故以来ずっと続いている日常方針の記述に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 3, Practice Drills, pp. 26–29"
    },
    "skm2-p1-c3-q12": {
        "trans": "If you enter the ocean without performing adequate warm-up exercises first, there is a serious risk of inducing heart failure or muscle cramps.",
        "ctx": "Warm-up imperatives to avoid aquatic physical hazards.",
        "opt_reasons": {
            "してはじめて": "準備運動をして初めて海に入ると危険という意味になり、論理が完全に破綻します。",
            "した上で": "準備運動をした上で入ると危険という意味になり、警告の意図と真逆になります。",
            "して次第": "文法的に誤った接続形式であり存在しません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 3, Practice Drills, pp. 26–29"
    },

    # --- Chapter 4: 範囲・限界・開始点・終了点 pp. 30–33 ---
    "skm2-p1-c4-q1": {
        "trans": "In major metropolitan areas starting with Tokyo and Osaka, resolving the acute childcare waiting list issue has become an urgent priority.",
        "ctx": "Metropolitan social challenges in urban child care.",
        "opt_reasons": {
            "を限りに": "期限の終了（〜を最後に）を表すため、代表例を挙げて全体を提示する文脈に合いません。",
            "を皮切りに": "ある行動をきっかけに同種の行動が次々起きることを表し、都市の例示に不適です。",
            "にいたるまで": "極端な範囲の到達点を表すため、「東京や大阪などの大都市」という代表例示に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 4, Practice Drills, pp. 30–33"
    },
    "skm2-p1-c4-q2": {
        "trans": "His plan, judging from the fundraising methods right from the outset, is exceedingly unrealistic, and the possibility of realization is nonexistent.",
        "ctx": "Critiquing an unviable business plan starting with initial capital flaws.",
        "opt_reasons": {
            "を通して": "期間や手段を表すため、最初の着眼点から判断して全体を否定する「からして」に合いません。",
            "にかけて": "おおよその範囲を表すため、資金調達という最初の欠陥の指摘に不適です。",
            "にわたって": "期間や場所の広がりを表すため、判断の根拠となる手掛かりの提示に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 4, Practice Drills, pp. 30–33"
    },
    "skm2-p1-c4-q3": {
        "trans": "Over an extensive period spanning three years, researchers conducted meticulous field surveys across tropical rainforests.",
        "ctx": "Multiphase longitudinal scientific surveys in rainforests.",
        "opt_reasons": {
            "を通じて": "「3年にわたって」は期間の広大さ・継続を強調し、「を通じて」よりも規模の大きさに合致します。",
            "を皮切りに": "連続的行動の端緒を表すため、3年間という継続期間そのものに接続できません。",
            "をもって": "手段や厳密な期限の区切りを表すため、調査期間の広がりを表せません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 4, Practice Drills, pp. 30–33"
    },
    "skm2-p1-c4-q4": {
        "trans": "Kicking off with the Tokyo performance, the rock band will conduct a nationwide tour across 20 cities throughout Japan.",
        "ctx": "Rock band tour itinerary starting with headline Tokyo dates.",
        "opt_reasons": {
            "をはじめとして": "代表例を挙げる表現であり、ツアーの最初の公演を合図に連続公演を展開する勢いが出ません。",
            "を限りに": "終了期限を表すため、ツアーの開幕となる東京公演に矛盾します。",
            "にいたるまで": "最終的な到達点を表すため、最初のスタート地点の提示に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 4, Practice Drills, pp. 30–33"
    },
    "skm2-p1-c4-q5": {
        "trans": "With today's broadcast as the very last, this long-running television drama spanning 30 years will conclude its historic broadcast run.",
        "ctx": "Series finale announcement for a legendary broadcast drama.",
        "opt_reasons": {
            "を皮切りに": "開始・端緒を表すため、30年の歴史に幕を下ろす最終回に真逆の意味になります。",
            "をはじめ": "代表例の提示であり、今日で完全に終了するという期限設定に合いません。",
            "を通じて": "全期間を通じてという意味になり、「本日の放送をもって終了」という区切りを示せません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 4, Practice Drills, pp. 30–33"
    },
    "skm2-p1-c4-q6": {
        "trans": "From clothes and interior decor all the way down to smartphone wallpapers, her room is meticulously unified in pink.",
        "ctx": "Extensive aesthetic consistency unified down to minor details.",
        "opt_reasons": {
            "をはじめ": "代表例の提示であり、壁紙という些細な極限にまで及んでいる徹底性を表せません。",
            "を皮切りに": "行動の連鎖の開始を表すため、持ち物の色彩統一の範囲に合いません。",
            "にわたって": "期間や空間の広がりを表す助詞であり、極端な例「壁紙」に直接結べません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 4, Practice Drills, pp. 30–33"
    },
    "skm2-p1-c4-q7": {
        "trans": "Through mutual exchanges in sports and cultural arts, deep bonds of friendship were fostered between the two nations.",
        "ctx": "Cross-cultural friendship fostered via exchange channels.",
        "opt_reasons": {
            "を限りに": "期限の終了を表すため、親善を育む媒介・手段に合いません。",
            "からして": "手掛かりによる否定的推論を表すため、交流を通じた親善の促進に不適です。",
            "にいたるまで": "範囲の極端な限界を表すため、友好関係を築く手段・経路に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 4, Practice Drills, pp. 30–33"
    },
    "skm2-p1-c4-q8": {
        "trans": "His dedicated enthusiasm can be clearly perceived even just from the exceptional quality of his submitted paperwork.",
        "ctx": "Evaluating dedication evident from application craftsmanship.",
        "opt_reasons": {
            "をはじめ": "代表例の並列であり、書類の質という一つの手掛かりから人柄を見抜く文脈に合いません。",
            "を皮切りに": "連続動作の開始を表すため、熱意の推論根拠に不適です。",
            "を限りに": "期限終了を表すため、書類の完成度から推し量る文脈に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 4, Practice Drills, pp. 30–33"
    },
    "skm2-p1-c4-q9": {
        "trans": "Across a vast area extending over 50 kilometers, the typhoon caused devastating landslides and flood damage.",
        "ctx": "Wide-area typhoon destruction across extended terrain.",
        "opt_reasons": {
            "からして": "推論の手掛かりを表すため、50キロという広大な空間的広がりの叙述に合いません。",
            "をはじめ": "代表例の提示であり、連続した地理的距離の幅に不適です。",
            "を限りに": "期限の打ち切りを表すため、台風被害の空間的規模に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 4, Practice Drills, pp. 30–33"
    },
    "skm2-p1-c4-q10": {
        "trans": "Starting with the mayor, municipal officials and local citizen volunteers gathered together to undertake river cleaning activities.",
        "ctx": "Civic river restoration headed by municipal leaders.",
        "opt_reasons": {
            "を皮切りに": "連続したイベントの口火を切る表現であり、参加人物の代表例示に合いません。",
            "を限りに": "終了期限を表すため、市長をはじめとする市民の参加に矛盾します。",
            "にいたるまで": "市長を極端な隅の例とするのは失礼であり、リーダーとして代表例示する文脈に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 4, Practice Drills, pp. 30–33"
    },
    "skm2-p1-c4-q11": {
        "trans": "As of the conclusion of today's reception desk hours, application acceptance for this fiscal year's subsidies will close.",
        "ctx": "Formal administrative deadline closure announcement.",
        "opt_reasons": {
            "を皮切りに": "開始を表すため、申請受付を締め切る終了宣言に真逆の意味になります。",
            "をはじめ": "代表例の提示であり、受付時間を明確に区切る期限に合いません。",
            "を通して": "期間全体の媒介を表すため、本日をもって終了するという厳密な区切りに不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 4, Practice Drills, pp. 30–33"
    },
    "skm2-p1-c4-q12": {
        "trans": "Over 20 years, he has persisted single-mindedly with his research into traditional pottery techniques.",
        "ctx": "Lifelong artisan devotion to traditional ceramics.",
        "opt_reasons": {
            "を皮切りに": "最初の一撃を表すため、20年間という長い歳月の継続に合いません。",
            "からして": "推論の手掛かりを表すため、研究年月の広がりを表せません。",
            "を限りに": "引退・終了を表すため、現在も続く研究の年月に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 4, Practice Drills, pp. 30–33"
    },

    # --- Chapter 5: 限定・非限定・付加 pp. 34–37 ---
    "skm2-p1-c5-q1": {
        "trans": "Today's special discount campaign applies exclusively to the first 100 members who have completed registration.",
        "ctx": "Promotional qualification restricted to first registered members.",
        "opt_reasons": {
            "ばかりに": "〜したことだけが原因で悪い結果になったことを表すため、特典の限定適用に合いません。",
            "のみならず": "〜だけでなく他にもという非限定を表すため、「先着100名様のみ」という厳格な限定に矛盾します。",
            "だけでなく": "非限定の付加を表すため、人数枠を絞るキャンペーンの条件に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 5, Practice Drills, pp. 34–37"
    },
    "skm2-p1-c5-q2": {
        "trans": "Of all people him, who rarely oversleeps normally, the alarm clock failed to ring on the very day of the crucial exam.",
        "ctx": "Unfortunate Murphy's law timing on critical exam morning.",
        "opt_reasons": {
            "に限り": "一般的な特別優遇・制限の規定を表すため、不運な偶然に対する皮肉な感情に合いません。",
            "ばかりか": "付加累加を表すため、「大事な日に限って」という運の悪さの強調に不適です。",
            "どころか": "正反対の極端な事態を導くため、普段寝坊しない彼という人物の取り立てに合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 5, Practice Drills, pp. 34–37"
    },
    "skm2-p1-c5-q3": {
        "trans": "As long as you preserve a passionate curiosity, humans can continue learning new knowledge at any age.",
        "ctx": "Lifelong learning capabilities provided curiosity persists.",
        "opt_reasons": {
            "ばかりに": "恨み・後悔の理由を表すため、生涯学習の前提条件に合いません。",
            "のみならず": "非限定を表すため、「好奇心を持ち続ける限り」という継続条件に不適です。",
            "に限り": "特定の対象の選別を表すため、状態が続く間という時間的・論理的条件に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 5, Practice Drills, pp. 34–37"
    },
    "skm2-p1-c5-q4": {
        "trans": "As far as my personal investigations are concerned, no documents corresponding to this historical incident were found.",
        "ctx": "Academic research parameters delimiting evidential absence.",
        "opt_reasons": {
            "に限って": "不運な巡り合わせや特別な信頼を表すため、調査範囲の限定に合いません。",
            "ばかりか": "累加を表すため、「自分が調べた範囲では」という判断枠の限定に不適です。",
            "のみならず": "「〜だけでなく」という意味になり、調査範囲を区切る表現になりません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 5, Practice Drills, pp. 34–37"
    },
    "skm2-p1-c5-q5": {
        "trans": "That honest company president of all people would never commit such fraud; there must be some deep background reason.",
        "ctx": "Expressing unshakeable trust in an honorable executive's integrity.",
        "opt_reasons": {
            "に限り": "規則的優遇を表すため、特定人物の人柄に対する強い信用に合いません。",
            "ばかりに": "悪い結果の原因を表すため、不正を絶対にしないという確信に不適です。",
            "どころか": "対比・反論を表すため、信じる対象の取り立てに合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 5, Practice Drills, pp. 34–37"
    },
    "skm2-p1-c5-q6": {
        "trans": "This admission pass is valid exclusively for the purchaser on the day of issuance.",
        "ctx": "Strict non-transferable admission ticket regulations.",
        "opt_reasons": {
            "に限って": "皮肉な巡り合わせや信頼を表すため、規約における公式の限定規定に合いません。",
            "ばかりに": "後悔の原因を表す表現であり、入場券の有効規約に不適切です。",
            "のみならず": "「〜だけでなく」になり、購入者本人以外への譲渡を許すことになり規約と矛盾します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 5, Practice Drills, pp. 34–37"
    },
    "skm2-p1-c5-q7": {
        "trans": "Just because I blurted out a single careless remark, I ended up inviting my friend's intense anger.",
        "ctx": "Regretting disproportionate consequences caused by a careless comment.",
        "opt_reasons": {
            "に限り": "肯定的限定や優遇を表すため、失言のせいで怒りを買った後悔に合いません。",
            "のみならず": "「〜だけでなく」になり、一言言ったことだけが原因という限定性に反します。",
            "どころか": "反駁の否定になり、失言が引き金となった因果関係を表せません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 5, Practice Drills, pp. 34–37"
    },
    "skm2-p1-c5-q8": {
        "trans": "As long as the company rules do not permit side businesses, one must avoid secretly taking secondary jobs without permission.",
        "ctx": "Workplace compliance regarding unauthorized secondary employment.",
        "opt_reasons": {
            "ばかりに": "後悔の理由を表すため、就業規則が認めない状態が続く間の義務に合いません。",
            "に限って": "不運な例外を表すため、規則が禁じている前提条件に不適です。",
            "のみならず": "非限定の付加を表すため、規則で縛られている前提に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 5, Practice Drills, pp. 34–37"
    },
    "skm2-p1-c5-q9": {
        "trans": "As far as the eye can see, golden fields of wheat spread across toward the horizon.",
        "ctx": "Panoramic pastoral description of endless wheat fields.",
        "opt_reasons": {
            "に限って": "特定の不運や信頼を表すため、視覚の及ぶ範囲全体の描写に合いません。",
            "ばかりに": "原因を表すため、見渡す限りの壮大な景観描写に不適です。",
            "のみならず": "非限定付加であり、「見渡す限り」という視野の物理的限界設定に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 5, Practice Drills, pp. 34–37"
    },
    "skm2-p1-c5-q10": {
        "trans": "On days when I leave without carrying an umbrella of all days, it always rains unexpectedly.",
        "ctx": "Classic irony of unexpected downpours on umbrella-less days.",
        "opt_reasons": {
            "に限り": "公式の制限を表すため、日常の運の悪さに対する皮肉な感情に合いません。",
            "ばかりに": "後悔の原因を表すため、「傘を持たない日に限って」という日時の取り立てに不適です。",
            "のみならず": "「〜だけでなく」になり、雨が降る日の皮肉な特定に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 5, Practice Drills, pp. 34–37"
    },
    "skm2-p1-c5-q11": {
        "trans": "Simply because of wanting to see that popular idol group in person, I traveled all the way to an arena in a neighboring prefecture.",
        "ctx": "Fandom devotion driving long-distance concert travel.",
        "opt_reasons": {
            "に限り": "特別規則の限定を表すため、個人的な一途な動機付けに合いません。",
            "のみならず": "「〜だけでなく」になり、「ただ会いたい一心で」という純粋な動機に反します。",
            "に限って": "不運な偶然を表すため、自発的な情熱による遠征行動に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 5, Practice Drills, pp. 34–37"
    },
    "skm2-p1-c5-q12": {
        "trans": "As far as the meteorological agency's announcements indicate, the possibility of the typhoon making direct landfall tomorrow is low.",
        "ctx": "Weather forecast assessment regarding typhoon trajectory.",
        "opt_reasons": {
            "に限って": "特定の例外を表すため、発表情報の範囲に基づく判断に合いません。",
            "ばかりに": "悪い結果の原因を表すため、客観的な予報データによる推論に不適です。",
            "のみならず": "非限定付加であり、予報発表の範囲内という限定に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 5, Practice Drills, pp. 34–37"
    },

    # --- Chapter 6: 関連・関係・対応 pp. 40–41 ---
    "skm2-p1-c6-q1": {
        "trans": "This environmental protection project is gathering attention not only within Japan, but also from young people across Asian nations.",
        "ctx": "Broad regional youth engagement in eco-initiatives.",
        "opt_reasons": {
            "に限り": "排他的限定を表すため、「アジア各国の若者からも」という拡大に矛盾します。",
            "どころか": "反駁の対比を表すため、「国内だけでなく海外からも」という付加に合いません。",
            "ばかりに": "悪い結果の原因を表すため、国際的な注目を集める発展的文脈に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 40–41"
    },
    "skm2-p1-c6-q2": {
        "trans": "That politician not only broke his promises, but shoved all responsibility for his own misgovernment onto his subordinates.",
        "ctx": "Denouncing political malfeasance and subordinate scapegoating.",
        "opt_reasons": {
            "に限り": "特別優遇を表すため、悪行が重なる政治家の批判に合いません。",
            "のみならず": "客観的な付加を表しますが、前項の悪行に輪をかけてひどい後項を糾弾するには「ばかりか」が最適です。",
            "どころか": "正反対の事態を導くため、両方の悪行を重ねて非難する文脈に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 40–41"
    },
    "skm2-p1-c6-q3": {
        "trans": "This restaurant's dishes are not merely exceptionally delicious, but their nutritional balance is outstanding as well.",
        "ctx": "Praising combined gastronomic excellence and nutritional value.",
        "opt_reasons": {
            "に限り": "排他的限定を表すため、「栄養バランスも抜群」という長所の追加に矛盾します。",
            "ばかりに": "後悔の原因を表すため、レストランの美点を称賛する文脈に合いません。",
            "どころか": "反駁否定を表すため、美味しさと栄養の両立に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 40–41"
    },
    "skm2-p1-c6-q4": {
        "trans": "Severe earthquakes not only directly destroy buildings, but also trigger devastating tsunami secondary disasters.",
        "ctx": "Seismic disaster hazards compounding secondary tsunamis.",
        "opt_reasons": {
            "に限り": "排他的限定を表すため、二次災害を併発する大震災の脅威に合いません。",
            "ばかりに": "後悔の理由を表すため、自然災害の客観的な複合被害の記述に不適です。",
            "どころか": "正反対の対比を導くため、倒壊と津波の両方が発生する事実に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 40–41"
    },
    "skm2-p1-c6-q5": {
        "trans": "He arrived an hour late without contacting us beforehand, and furthermore didn't offer a single word of apology.",
        "ctx": "Disapproval of uncommunicative tardiness compounded by lack of remorse.",
        "opt_reasons": {
            "に限り": "特別優遇を表すため、不誠実な態度を重ねる遅刻者に合いません。",
            "のみならず": "客観的事実の並列になり、無礼な振る舞いに憤慨して非難する語気が出ません。",
            "どころか": "「〜どころか謝らなかった」だと遅刻しなかったような錯覚を生み、文脈が崩壊します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 40–41"
    },
    "skm2-p1-c6-q6": {
        "trans": "Global environmental issues require urgent countermeasures not only by developed nations, but by the international community as a whole.",
        "ctx": "Universal international accountability for climate action.",
        "opt_reasons": {
            "に限り": "先進国だけに限定することになり、地球規模の包括的連携と真っ向から衝突します。",
            "ばかりに": "後悔の原因を表すため、国際社会全体の協調義務に合いません。",
            "どころか": "先進国の対策を否定する語感になり、国際的共同責任の推進に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 40–41"
    },
    "skm2-p1-c6-q7": {
        "trans": "The internet not only made information searches convenient, but fundamentally transformed interpersonal communication.",
        "ctx": "Digital revolution transforming daily communicative sociology.",
        "opt_reasons": {
            "に限り": "限定を表すため、情報検索の利便性と通信変革の両面を肯定する文脈に合いません。",
            "ばかりに": "悪い結果の原因を表すため、文明的発展の肯定的評価に不適です。",
            "どころか": "利便性を否定するニュアンスが生じ、二大恩恵の共存に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 40–41"
    },
    "skm2-p1-c6-q8": {
        "trans": "He not only did not hand in his assignment on the deadline, but also falsely claimed to the teacher that he had lost it.",
        "ctx": "Reprimanding student non-submission compounded by dishonesty.",
        "opt_reasons": {
            "に限り": "優遇を表すため、嘘を重ねる不誠実な生徒の叱責に合いません。",
            "のみならず": "中立的な事実並立になり、課題未提出の上に嘘までついた悪質さの糾弾に不十分です。",
            "どころか": "「〜どころか嘘をついた」だと提出したことになり、文意が破綻します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 40–41"
    },
    "skm2-p1-c6-q9": {
        "trans": "This software not only features intuitive, easy-to-use operability, but also excels in high security performance.",
        "ctx": "Software marketing showcasing intuitive UX and enterprise security.",
        "opt_reasons": {
            "に限り": "排他的限定を表すため、操作性と安全性の二大強みの両立に矛盾します。",
            "ばかりに": "後悔の原因を表すため、製品の優秀なスペックアピールに合いません。",
            "どころか": "操作性を否定する対比になり、製品の優位性に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 40–41"
    },
    "skm2-p1-c6-q10": {
        "trans": "The typhoon not only brought severe downpours, but violent gales toppled street trees in succession.",
        "ctx": "Severe typhoon damage combining flooding and gale-force windfalls.",
        "opt_reasons": {
            "に限り": "限定を表すため、暴風と豪雨の重複被害の記述に合いません。",
            "どころか": "大雨を否定することになり、風水害の両立に矛盾します。",
            "ばかりに": "個人の後悔を表すため、客観的な気象災害の被害拡大描写に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 40–41"
    },
    "skm2-p1-c6-q11": {
        "trans": "He is not merely intelligent and quick-witted, but also remarkably thoughtful and considerate toward others.",
        "ctx": "Praising intellectual agility combined with deep empathy.",
        "opt_reasons": {
            "に限り": "限定を表すため、知性と優しさの両面を兼ね備える人物称賛に合いません。",
            "ばかりに": "悪い結果の原因を表すため、美点を称える文脈に不適切です。",
            "どころか": "知性を否定するニュアンスが生じるため、二つの長所の兼備に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 40–41"
    },
    "skm2-p1-c6-q12": {
        "trans": "Smoking not only harms the health of smokers themselves, but exerts grave negative health impacts on surrounding people.",
        "ctx": "Public health warnings on second-hand passive smoking hazards.",
        "opt_reasons": {
            "に限り": "喫煙者だけに限定してしまい、受動喫煙の周囲への被害拡大警告に矛盾します。",
            "ばかりに": "後悔を表すため、公衆衛生の客観的警告に合いません。",
            "どころか": "喫煙者自身の健康被害を否定することになり、医学的事実に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 40–41"
    },

    # --- Chapter 7: 無関係・無視・除外 pp. 42–45 ---
    "skm2-p1-c7-q1": {
        "trans": "Surrounding the issue of inheritance succession, a fierce courtroom struggle spanning many years has been ongoing among relatives.",
        "ctx": "Inheritance disputes causing long-standing intra-family litigation.",
        "opt_reasons": {
            "にこたえて": "要望や期待に応えることを表すため、遺産をめぐる激しい親族間の対立・争いに合いません。",
            "に基づいて": "法的根拠やデータに基づくことを表すため、争乱の中心テーマとなる「をめぐって」に不適です。",
            "を問わず": "条件を不問に付す表現であり、争いの対立軸となる対象提示に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 42–45"
    },
    "skm2-p1-c7-q2": {
        "trans": "In response to the passionate cheers of the fans, the athlete endured the pain of his injury and achieved a magnificent comeback victory.",
        "ctx": "Athlete rallying past injuries inspired by crowd support.",
        "opt_reasons": {
            "をめぐって": "争いや議論の対象を表すため、ファンの温かい声援に応える感謝の行動に合いません。",
            "に基づいて": "理論的根拠を表すため、感情的声援に奮起するスポーツの美談に不適です。",
            "を問わず": "条件の無関係を表すため、ファンの声援に報いる逆転劇の動機付けに合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 42–45"
    },
    "skm2-p1-c7-q3": {
        "trans": "Regarding the relocation plan of the capital city functions, lively debates were unfolded from diverse angles among scholars.",
        "ctx": "Multidisciplinary academic debates on capital decentralization.",
        "opt_reasons": {
            "にこたえて": "要請に応えることを表すため、賛否両論が分かれる政策論争の争点提示に合いません。",
            "を問わず": "無条件を表すため、議論の核心テーマ「移転計画をめぐって」に不適です。",
            "に反して": "予想の裏切りを表すため、テーマを巡る活発な意見交換に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 42–45"
    },
    "skm2-p1-c7-q4": {
        "trans": "In response to urgent customer demands, the company decided to develop and launch a low-priced model promptly.",
        "ctx": "Agile product development responding to consumer demand.",
        "opt_reasons": {
            "をめぐって": "争乱や論争を表すため、顧客の切実な要望に応えて新製品を作る前向きな経営判断に合いません。",
            "に基づいて": "事実データや規則に基づくことを表し、顧客の要望・期待に「応える」ニュアンスが出ません。",
            "を問わず": "条件不問を表すため、要望に応じる因果関係に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 42–45"
    },
    "skm2-p1-c7-q5": {
        "trans": "Surrounding ownership of the newly discovered historical ancient document, disputes erupted among regional research institutes.",
        "ctx": "Jurisdictional controversies over discovered historical artifacts.",
        "opt_reasons": {
            "にこたえて": "期待に応じる表現であり、古文書の所有権を争う対立関係に合いません。",
            "に基づいて": "根拠を表すため、取り合いの対象となる論争テーマに不適です。",
            "を問わず": "不問を表すため、所有権をめぐる激しい対立に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 42–45"
    },
    "skm2-p1-c7-q6": {
        "trans": "In response to the warm applause of the audience, the pianist appeared on stage once more and played an encore piece.",
        "ctx": "Concert encore performance in response to enthusiastic applause.",
        "opt_reasons": {
            "をめぐって": "争いや対立を表すため、聴衆の温かいアンコール拍手に応じる演奏に合いません。",
            "に基づいて": "データや規則に基づくことを表すため、聴衆の熱狂に応える芸術的応答に不適です。",
            "を問わず": "無関係を表すため、拍手に応えた演奏の動機付けに反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 42–45"
    },
    "skm2-p1-c7-q7": {
        "trans": "Surrounding policy for amending the constitution, severe confrontations between ruling and opposition parties continue in the Diet.",
        "ctx": "Partisan legislative standoff regarding constitutional revision.",
        "opt_reasons": {
            "にこたえて": "要望に応じる肯定的な行動を表すため、与野党の激しい政治的対立に合いません。",
            "に基づいて": "根拠を表すため、争点となるテーマの提示「憲法改正案をめぐって」に不適です。",
            "を問わず": "不問を表すため、政治的抗争の対立軸提示に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 42–45"
    },
    "skm2-p1-c7-q8": {
        "trans": "In response to the enthusiastic requests of attendees, the instructor conducted a special Q&A session.",
        "ctx": "Academic seminar extending into audience Q&A sessions.",
        "opt_reasons": {
            "をめぐって": "争乱を表すため、受講者の真剣な要請に応じる親切な特別セッションに合いません。",
            "に基づいて": "客観的規則に基づくことを表し、受講者の熱い要望に「応える」文脈に不適です。",
            "を問わず": "条件不問を表すため、要望に応答する因果関係になりません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 42–45"
    },
    "skm2-p1-c7-q9": {
        "trans": "Surrounding introduction of the new evaluation system, repeated discussions were held between management and labor unions.",
        "ctx": "Labor-management negotiations regarding new appraisal frameworks.",
        "opt_reasons": {
            "にこたえて": "要求に応える一方的受諾を表すため、労使が互いに議論を重ねるテーマ提示に合いません。",
            "に基づいて": "データに基づくことを表すため、対立する新制度導入の争点提示に不適です。",
            "を問わず": "不問を表すため、交渉テーマの指定に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 42–45"
    },
    "skm2-p1-c7-q10": {
        "trans": "In response to high social expectations, the startup company achieved the goal of going public in its third year.",
        "ctx": "Startup enterprise delivering on market expectations by IPO.",
        "opt_reasons": {
            "をめぐって": "争いや対立を表すため、社会の期待に応えて上場を成し遂げた成功物語に合いません。",
            "に基づいて": "規則に基づくことを表すため、社会の期待に「応えて」飛躍した文意に不適です。",
            "を問わず": "不問を表すため、期待に報いる動機付けになりません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 42–45"
    },
    "skm2-p1-c7-q11": {
        "trans": "Surrounding development rights of the offshore wind power facility, negotiations between local fishermen and energy enterprises are underway.",
        "ctx": "Offshore wind energy leasing talks with maritime fishing unions.",
        "opt_reasons": {
            "にこたえて": "要望に応じることを表すため、利権をめぐる慎重な利害交渉に合いません。",
            "に基づいて": "規則の準拠を表すため、交渉の核心テーマとなる対象提示に不適です。",
            "を問わず": "条件不問を表すため、交渉事案の特定に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 42–45"
    },
    "skm2-p1-c7-q12": {
        "trans": "In response to local citizens' safety concerns, the municipal government decided to install streetlights and security cameras along school routes.",
        "ctx": "Municipal safety improvements along elementary school commuting paths.",
        "opt_reasons": {
            "をめぐって": "対立・闘争を表すため、住民の不安の声に応えて安全対策を講じる善政に合いません。",
            "に基づいて": "客観的基準を表すため、住民の声に耳を傾けて「応える」行政判断に不適です。",
            "を問わず": "不問を表すため、市民の不安に応答する因果関係になりません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 42–45"
    },

    # --- Chapter 8: 基準・根拠 pp. 46–49 ---
    "skm2-p1-c8-q1": {
        "trans": "Based upon the latest scientific experimental data, the therapeutic efficacy of the new anticancer drug was proven objectively.",
        "ctx": "Clinical validation of oncological pharmaceuticals based on data.",
        "opt_reasons": {
            "に反して": "予想の裏切りを表すため、確固たる実験データに「基づいて」証明された科学的成果に合いません。",
            "をもとに": "創作や着想のヒントを表すことが多く、厳密な科学的・客観的立証の根拠には「に基づいて」が最適です。",
            "にそって": "方針やルールに従うことを表すため、データから論理的結論を導く根拠に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 46–49"
    },
    "skm2-p1-c8-q2": {
        "trans": "This historical novel was written drawing inspiration based on the author's own turbulent youth experiences.",
        "ctx": "Literary novels adapted from biographical youth experiences.",
        "opt_reasons": {
            "に基づいて": "法規や客観的データに立脚する硬い表現であり、芸術作品・小説の創作素材には「をもとに（して）」が自然です。",
            "に反して": "事前の予想と反対であることを表すため、自らの体験を材料とした執筆に合いません。",
            "にそって": "マニュアルに従うことを表すため、人生体験を素材に生かした創作に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 46–49"
    },
    "skm2-p1-c8-q3": {
        "trans": "Strictly in accordance with company emergency response guidelines, safety evacuation drills were conducted swiftly.",
        "ctx": "Conducting emergency evacuation drills aligned with corporate protocol.",
        "opt_reasons": {
            "をもとに": "創作素材を表すため、マニュアルや規則の流れに合致させて進める「にそって」に合いません。",
            "に反して": "規則違反を表すことになり、迅速かつ適切に訓練を行った肯定文脈と矛盾します。",
            "をめぐって": "利権争いを表すため、規定に忠実に従った防災訓練に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 46–49"
    },
    "skm2-p1-c8-q4": {
        "trans": "Defying the market analysts' pre-match forecasts, the underdog team achieved a stunning upset victory.",
        "ctx": "Sports underdogs defying analytical predictions to triumph.",
        "opt_reasons": {
            "に基づいて": "予想通りの結果になったことを表すため、「大方の予想を裏切って」勝った劇的勝利に矛盾します。",
            "をもとに": "素材を表すため、事前の予測に反して番狂わせが起きた文脈に合いません。",
            "にそって": "予想の流れに従うことを表すため、波乱の逆転劇に真逆の意味になります。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 46–49"
    },
    "skm2-p1-c8-q5": {
        "trans": "Based upon strict standards established by national law, construction permits for nuclear power facilities are scrutinized.",
        "ctx": "Statutory regulatory compliance in nuclear facility permitting.",
        "opt_reasons": {
            "をもとに": "自由な創作の材料を表すため、国家の厳格な法的審査基準への準拠に合いません。",
            "に反して": "基準違反を表すことになり、厳正に審査を行う手続きの趣旨に反します。",
            "にこたえて": "心情的要望に応えることを表すため、法的許可基準の厳正な適用に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 46–49"
    },
    "skm2-p1-c8-q6": {
        "trans": "Taking the folklore traditions passed down in the local region as raw material, the anime script was crafted.",
        "ctx": "Anime storytelling adapted from traditional regional folklore lore.",
        "opt_reasons": {
            "に基づいて": "法規やデータへの厳密な準拠を表すため、伝承をヒントに創作を膨らませた脚本作りに不自然です。",
            "に反して": "伝承を否定することを表すため、民間伝承を素材として生かしたアニメ制作に合いません。",
            "にそって": "業務規則に従うことを表すため、自由な芸術的シナリオ執筆に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 46–49"
    },
    "skm2-p1-c8-q7": {
        "trans": "In accordance with the established curriculum plan, the university lectures progressed steadily through the semester.",
        "ctx": "Curricular progression adhering to university instructional plans.",
        "opt_reasons": {
            "をもとに": "創作材料を表すため、シラバスの計画の流れに忠実に沿って進む講義に合いません。",
            "に反して": "計画倒れを表すことになり、順調に講義が進んだ肯定文脈と矛盾します。",
            "をめぐって": "争いを表すため、講義計画の着実な履行に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 46–49"
    },
    "skm2-p1-c8-q8": {
        "trans": "Contrary to the weather forecast that predicted sunny skies, rain started pouring down from midday.",
        "ctx": "Unexpected midday downpours contrary to sunny forecasts.",
        "opt_reasons": {
            "に基づいて": "予報通りの天候になったことを表すため、晴れの予報が外れて雨が降った事実に矛盾します。",
            "をもとに": "素材を表すため、予報の予想が覆された天候変化に合いません。",
            "にそって": "予報通り進行したことを表すため、雨に裏切られた文意と真逆になります。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 46–49"
    },
    "skm2-p1-c8-q9": {
        "trans": "Based upon strict objective evaluation data from third-party certification organizations, the product was awarded the prize.",
        "ctx": "Awards attributed on objective third-party audit metrics.",
        "opt_reasons": {
            "をもとに": "着想のヒントを表すため、第三者機関の公的データに基づく厳正な表彰に不適です。",
            "に反して": "評価データに背くことを表すため、正当な受賞の趣旨に反します。",
            "にそって": "マニュアル準拠を表すため、評価データという根拠から導かれた表彰に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 46–49"
    },
    "skm2-p1-c8-q10": {
        "trans": "Taking the true story of an abandoned dog that moved the nation as its base, this tear-jerking film was produced.",
        "ctx": "Cinematic adaptations inspired by celebrated animal rescue stories.",
        "opt_reasons": {
            "に基づいて": "法規や論理的データの引用を表すため、感動の実話を題材とした映画製作には「をもとに」が自然です。",
            "に反して": "実話に背くことを表すため、実話を原案とする感動映画に合いません。",
            "にそって": "手順の遵守を表すため、ドラマの題材素材の指定に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 46–49"
    },
    "skm2-p1-c8-q11": {
        "trans": "In accordance with corporate environmental conservation guidelines, energy-saving measures across the entire factory were implemented.",
        "ctx": "Industrial energy efficiency adhering to environmental protocols.",
        "opt_reasons": {
            "をもとに": "創作素材を表すため、企業方針・ガイドラインの線に沿った施策の遂行に合いません。",
            "に反して": "方針違反を表すことになり、環境対策を徹底した文脈と矛盾します。",
            "をめぐって": "方針をめぐる争いを表すため、決定済みガイドラインの実践に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 46–49"
    },
    "skm2-p1-c8-q12": {
        "trans": "Contrary to surrounding expectations that he would certainly win the championship, he suffered an unexpected defeat in the first round.",
        "ctx": "Tournament favorite suffering unexpected first-round elimination.",
        "opt_reasons": {
            "に基づいて": "期待通りの勝利を表すため、初戦敗退という期待の裏切りに矛盾します。",
            "をもとに": "素材を表すため、周囲の期待に反した不本意な敗北に合いません。",
            "にそって": "期待通りの展開を表すため、初戦敗退のショックと真逆の意味になります。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 46–49"
    },

    # --- Chapter 9: 比較・対比・割合 pp. 50–53 ---
    "skm2-p1-c9-q1": {
        "trans": "As we drew closer to the mountain summit, the temperature plummeted sharply and fierce winds began to howl.",
        "ctx": "Climatic shifts proportional to higher mountain altitude.",
        "opt_reasons": {
            "にともなって": "事態の発生に伴う付随現象を表しますが、空間的・連続的な移行に伴う自然現象の変化には「につれて」が最適です。",
            "とともに": "二つの事態が同時に生じることを表しますが、移動の進行に応じた連続的温度変化には「につれて」が最も自然です。",
            "に従って": "規則への服従の語感を帯びることがあり、標高の上昇に伴う自然界の推移には「につれて」が第一選択です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 50–53"
    },
    "skm2-p1-c9-q2": {
        "trans": "In step with the progress of economic recovery, corporate job offer ratios have also steadily begun to rise.",
        "ctx": "Employment market improvements correlating with macro recovery.",
        "opt_reasons": {
            "にともなって": "偶発的な付随変化を表すため、景気回復の歩調に並行して進む求人倍率の上昇には「にしたがって」が最適です。",
            "につれて": "主に自然で無自覚な推移に用いられ、社会経済指標の客観的相関関係には「にしたがって」がより適合します。",
            "とともに": "単純な同時発生を表すため、景気動向と雇用改善の論理的な相関性に「にしたがって」が優れます。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 50–53"
    },
    "skm2-p1-c9-q3": {
        "trans": "Along with the advancement of the information society, security countermeasures against cybercrime are becoming increasingly important.",
        "ctx": "Cybersecurity priority escalating alongside digitization.",
        "opt_reasons": {
            "につれて": "自然現象の漸進的変化に多く、情報社会の発展という時代の大きな転換と重要性の共存には「とともに」が最適です。",
            "にしたがって": "規則への順応の語感があり、時代の進化に伴う課題の出現には「とともに」がより重厚です。",
            "にともなって": "具体的な個別事象の付随に多く、大局的な時代の到来には「とともに」が最も格調高いです。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 50–53"
    },
    "skm2-p1-c9-q4": {
        "trans": "Accompanying the retirement of the factory facilities, major reorganization of internal personnel was carried out.",
        "ctx": "Personnel restructuring accompanying industrial plant shutdowns.",
        "opt_reasons": {
            "につれて": "連続的で漸進的な変化を表すため、工場の閉鎖・引退という一回性の決定に伴う人事再編には「にともなって」が最適です。",
            "にしたがって": "歩調を合わせた比例変化を表すため、事業撤退に伴う組織改革に合いません。",
            "とともに": "「〜と同時に」の意味になりますが、重大事象に伴う派生措置には「にともなって」が最適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 50–53"
    },
    "skm2-p1-c9-q5": {
        "trans": "As time passed by, the acute sadness of that bereavement gradually softened into a calm memory.",
        "ctx": "Grief softening progressively over the passage of time.",
        "opt_reasons": {
            "にともなって": "事象の付随を表すため、時間の自然な経過に伴う心理的癒やしには「につれて」が最適です。",
            "にしたがって": "指示に従う語感があり、年月の経過による自然な心の変化に合いません。",
            "とともに": "一回性の同時生起を表すため、時間の流れに伴う漸進的な感情の軟化には「につれて」が適合します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 50–53"
    },
    "skm2-p1-c9-q6": {
        "trans": "In step with age progression, physical strength naturally declines, so conscious exercise habits become necessary.",
        "ctx": "Physical maintenance requirements escalating alongside aging.",
        "opt_reasons": {
            "にともなって": "特定事象の付随を表すため、加齢という不可逆の規則的プロセスには「にしたがって」が最適です。",
            "とともに": "加齢と同時に起きる一過性の事象ではないため、漸進的相関には「にしたがって」が適合します。",
            "につれて": "自然現象にも使えますが、年齢という目盛りに準拠した変化には「にしたがって」が極めて自然です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 50–53"
    },
    "skm2-p1-c9-q7": {
        "trans": "Along with welcoming the New Year, I newly renewed my determination toward achieving my career goals.",
        "ctx": "New Year renewal of personal career determinations.",
        "opt_reasons": {
            "につれて": "徐々に進む漸進的変化を表すため、新年を迎えた節目の一回性の決意表明に合いません。",
            "にしたがって": "比例変化を表すため、新年の訪れという瞬間の訪れに不適です。",
            "にともなって": "事業や事件の付随を表すため、おめでたい新年の挨拶・決意に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 50–53"
    },
    "skm2-p1-c9-q8": {
        "trans": "Accompanying the massive earthquake, fires broke out in various locations and city gas supplies were shut off.",
        "ctx": "Utility shutdowns and fires directly triggered by seismic disaster.",
        "opt_reasons": {
            "につれて": "ゆっくり進む変化を表すため、地震直後に発生した二次災害の付随に合いません。",
            "にしたがって": "歩調を合わせた比例変化を表すため、突発的災害の連鎖に不適です。",
            "とともに": "共存を表しますが、地震という原因から生じた直接の派生被害には「にともなって」が最も的確です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 50–53"
    },
    "skm2-p1-c9-q9": {
        "trans": "As the typhoon approached the coast, the waves grew toweringly high and strong gale warnings were issued.",
        "ctx": "Wave swells escalating as a typhoon closes in.",
        "opt_reasons": {
            "にともなって": "制度や事故の派生を表すため、台風の接近という自然界の移動推移には「につれて」が最適です。",
            "にしたがって": "規則への順応を表す語感があり、波が高くなる物理現象に不自然です。",
            "とともに": "一瞬の同時生起になり、接近の度合いに応じて波が高くなる比例関係が出ません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 50–53"
    },
    "skm2-p1-c9-q10": {
        "trans": "In step with increasing experience in society, one becomes capable of making decisions with a broader perspective.",
        "ctx": "Professional decision maturity expanding in step with experience.",
        "opt_reasons": {
            "にともなって": "個別事件の付随を表すため、経験の蓄積に伴う視野の成熟には「にしたがって」が最適です。",
            "とともに": "一回性の共起になり、長年の経験値に応じた判断力の向上という比例関係に合いません。",
            "につれて": "自然現象の推移に多く、社会的成熟の道程には「にしたがって」がより格式的です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 50–53"
    },
    "skm2-p1-c9-q11": {
        "trans": "Along with global economic integration, interdependence among nations has deepened more than ever before.",
        "ctx": "Macroeconomic globalization heightening mutual cross-border reliance.",
        "opt_reasons": {
            "につれて": "身近な自然現象の変化に多く、グローバル経済の一体化という歴史的大転換には「とともに」が最も適します。",
            "にしたがって": "指示への服従を連想させ、相互依存の深まりという共存的発展に不自然です。",
            "にともなって": "具体的なトラブルや措置の付随を表すことが多く、大局的変革に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 50–53"
    },
    "skm2-p1-c9-q12": {
        "trans": "Accompanying the revision of the law, procedures at administrative counters underwent major simplifications.",
        "ctx": "Administrative deregulation accompanying legislative amendments.",
        "opt_reasons": {
            "につれて": "徐々に起きる推移を表すため、法改正に伴う窓口手続きの一斉変更に合いません。",
            "にしたがって": "比例変化を表すため、法改正の施行に伴う制度変更に不適です。",
            "とともに": "同時生起を表しますが、法改正という原因から派生した業務変更には「にともなって」が最適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 50–53"
    },

    # --- Chapter 10: 立場・視点・評価基準 pp. 54–57 ---
    "skm2-p1-c10-q1": {
        "trans": "Joking aside, this is an acute emergency involving genuine peril to life unless we evacuate right now.",
        "ctx": "Urgent life-safety warning demanding immediate seriousness.",
        "opt_reasons": {
            "抜きにしては": "後件に「〜できない」という仮定否定を要求するため、「冗談抜きで避難しろ」という直接命令・断定文に合いません。",
            "を問わず": "条件不問を表すため、「冗談を排除して真面目に」という態度の切り替えに不適です。",
            "をこめて": "感情を込めることを表すため、「冗談をやめて」という排除の意図と真逆になります。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 54–57"
    },
    "skm2-p1-c10-q2": {
        "trans": "Without his immense contributions over many years, the success of this research project could never be spoken of.",
        "ctx": "Honoring an indispensable researcher whose contributions ensured project success.",
        "opt_reasons": {
            "抜きで": "副詞的に「〜なしで行動する」意味になり、「〜がなければ成功はあり得ない」という条件否定の呼応（抜きにしては〜語れない）になりません。",
            "を問わず": "条件不問を表すため、成功の不可欠な要因を称える文脈に合いません。",
            "を通して": "期間や手段を表すため、彼の貢献を前提とする仮定否定文に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 54–57"
    },
    "skm2-p1-c10-q3": {
        "trans": "From the perspective of foreign language learners, the three writing systems of Japanese—hiragana, katakana, and kanji—are tremendously challenging.",
        "ctx": "Analyzing Japanese orthographic difficulty from a learner standpoint.",
        "opt_reasons": {
            "をもとに": "創作素材を表すため、学習者の立場からの主観的評価・判断の提示に合いません。",
            "を抜きにして": "排除を表すため、評価の基準となる学習者の立場指定に不適です。",
            "に基づいて": "客観的規則を表すため、「〜の立場から見ると困難だ」という視点提示に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 54–57"
    },
    "skm2-p1-c10-q4": {
        "trans": "Let us abandon formal social flatteries and engage in a frank exchange of opinions today.",
        "ctx": "Inviting uninhibited, candid dialogue without formalities.",
        "opt_reasons": {
            "抜きにしては": "後件に仮定否定（〜できない）を要求するため、「本音で語り合おう」という勧誘文に接続できません。",
            "を問わず": "条件不問を表すため、お世辞を排除する文脈に合いません。",
            "を込めて": "感情を注入することを表すため、お世辞を抜きにする意図と矛盾します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 54–57"
    },
    "skm2-p1-c10-q5": {
        "trans": "Without the warm encouragement and guidance of my teacher, passing the certification exam would have been impossible for me.",
        "ctx": "Attributing certification success to a mentor's indispensable guidance.",
        "opt_reasons": {
            "抜きで": "手段の省略を表すため、「指導がなければ合格できなかった」という反実仮想の条件否定文には「抜きにしては」が必須です。",
            "を通して": "手段を表す肯定文になり、「合格はあり得なかった」という否定文と矛盾します。",
            "を問わず": "不問を表すため、恩師の指導の決定的な重みを語る文脈に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 54–57"
    },
    "skm2-p1-c10-q6": {
        "trans": "From the perspective of environmental conservation, developing technologies to reduce plastic waste is a global imperative.",
        "ctx": "Evaluating plastic waste reduction through an eco-preservation lens.",
        "opt_reasons": {
            "を抜きにして": "排除を表すため、議論の立脚点となる「環境保護の視点」の提示に合いません。",
            "をもとに": "創作素材を表すため、技術開発の評価視点の提示に不適です。",
            "に反して": "背くことを表すため、環境保護の見地に立った肯定的な開発要請に矛盾します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 54–57"
    },
    "skm2-p1-c10-q7": {
        "trans": "Leaving aside personal feelings, let us evaluate the matter purely objectively based on facts.",
        "ctx": "Setting personal emotions aside for objective appraisal.",
        "opt_reasons": {
            "抜きにしては": "仮定否定文を要求するため、「客観的に評価しよう」という肯定提案文に接続できません。",
            "を込めて": "感情を込めることになり、私情を排して客観視する趣旨と正反対になります。",
            "を問わず": "条件不問を表すため、私情を脇に置く態度の切り替えに合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 54–57"
    },
    "skm2-p1-c10-q8": {
        "trans": "Without the devoted support of local volunteers, managing this marathon tournament would not be viable.",
        "ctx": "Acknowledging volunteers as indispensable to race operations.",
        "opt_reasons": {
            "抜きで": "手段の省略になり、「支えがなければ成り立たない」という条件否定の呼応（抜きにしては〜成り立たない）になりません。",
            "を通して": "手段を表す肯定文になり、否定結末に呼応しません。",
            "に沿って": "マニュアル準拠を表すため、ボランティアの存在自体の不可欠性に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 54–57"
    },
    "skm2-p1-c10-q9": {
        "trans": "From the viewpoint of children's healthy development, excessively restricting outdoor play is not desirable.",
        "ctx": "Pediatric developmental lens on outdoor play freedom.",
        "opt_reasons": {
            "を抜きにして": "排除を表すため、判断の立脚点となる子どもの成長の観点提示に合いません。",
            "をもとに": "素材を表すため、教育的見地からの健全な判断提示に不適です。",
            "に反して": "背くことを表すため、子どもの健全な発育の視点そのものの指定に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 54–57"
    },
    "skm2-p1-c10-q10": {
        "trans": "Putting preliminary excuses aside, please report the core facts of the accident immediately.",
        "ctx": "Demanding direct incident reporting without preliminary pretexts.",
        "opt_reasons": {
            "抜きにしては": "後件に仮定否定（〜できない）を要求するため、「すぐに報告しなさい」という命令文に接続できません。",
            "を込めて": "言い訳を込めて報告することになり、不条理で非論理的になります。",
            "を問わず": "条件不問を表すため、言い訳を排除する指示に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 54–57"
    },
    "skm2-p1-c10-q11": {
        "trans": "Without rigorous quality control, high trust in our brand could never have been established.",
        "ctx": "Brand trust contingent on uncompromising quality control.",
        "opt_reasons": {
            "抜きで": "手段の省略になり、「徹底した管理がなければ信頼は築けなかった」という条件否定の呼応になりません。",
            "を通して": "肯定的な手段を表すため、「信頼は築けなかった」という否定文と衝突します。",
            "に沿って": "手順遵守を表すため、品質管理の不可欠性の強調に「抜きにしては」が最適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 54–57"
    },
    "skm2-p1-c10-q12": {
        "trans": "From the standpoint of financial soundness, this major debt-financed investment involves immense risk.",
        "ctx": "Corporate fiscal risk assessment regarding debt-funded outlays.",
        "opt_reasons": {
            "を抜きにして": "排除を表すため、判断の基準となる財務の健全性という視点に合いません。",
            "をもとに": "創作素材を表すため、財務健全性の見地からのリスク警告に不適です。",
            "に反して": "反逆を表すため、健全性の立場から評価する文脈に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 54–57"
    },

    # --- Chapter 11: 傾向・状態 pp. 58–61 ---
    "skm2-p1-c11-q1": {
        "trans": "This marathon race is open to anyone freely, regardless of professional versus amateur status, age, or nationality.",
        "ctx": "Open marathon entry criteria regardless of demographic attributes.",
        "opt_reasons": {
            "を問わず": "正解です。条件の差異を全く問題にしない不問の助詞句です。",
            "にかかわらず": "自然現象や行為の成否に多く使われ、名詞の対比ペア「プロ・アマ」「年齢・国籍」を包括する場合には「を問わず」が最も標準的です。",
            "抜きにして": "排除を表すため、あらゆる人々を広く受け入れる文脈に合いません。",
            "をもとに": "素材を表すため、参加資格の不問規定に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 58–61"
    },
    "skm2-p1-c11-q2": {
        "trans": "Tomorrow's charity event will be carried out as scheduled, regardless of rain or clear skies.",
        "ctx": "Event operations proceeding regardless of meteorological conditions.",
        "opt_reasons": {
            "を問わず": "天候のような自然条件の二者対立（雨天・晴天）には「にかかわらず」が最適です。",
            "抜きで": "手段の排除を表すため、天候条件の無視に不適です。",
            "に反して": "予想の裏切りを表すため、事前に天候にかかわらず催行を決めている告知に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 58–61"
    },
    "skm2-p1-c11-q3": {
        "trans": "The store handles online consultations 24 hours a day, regardless of day or night.",
        "ctx": "Uninterrupted customer support throughout day and night.",
        "opt_reasons": {
            "を問わず": "正解です。「昼夜を問わず」は固定的な慣用対比句です。",
            "抜きにして": "昼夜を排除することになり、意味が成り立ちません。",
            "をもとに": "素材を表すため、時間帯の無関係規定に合いません。",
            "に反して": "昼夜に背くことになり、意味不明な非文になります。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 58–61"
    },
    "skm2-p1-c11-q4": {
        "trans": "Regardless of whether one's individual opinion is in agreement or opposition, everyone must follow the company resolution.",
        "ctx": "Corporate compliance binding regardless of personal opinion.",
        "opt_reasons": {
            "を問わず": "「賛成か反対か」という節の二者択一には「にかかわらず」が文法的に接続します。",
            "抜きで": "手段の省略を表すため、意見の不一致の超越に合いません。",
            "に反して": "背くことを表すため、賛否両論の立場を問わない全社的拘束力に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 58–61"
    },
    "skm2-p1-c11-q5": {
        "trans": "This music transcends differences of national borders and language, moving the hearts of people worldwide.",
        "ctx": "Universal musical resonance transcending borders and language.",
        "opt_reasons": {
            "を問わず": "正解です。対立する概念「国境や言語の別」を問わず普遍的に響く文脈です。",
            "抜きにして": "国境や言語を排除することになり、不自然な表現になります。",
            "をもとに": "音楽の素材を表すことになり、音楽が国境を超越するメッセージとズレます。",
            "に反して": "国境に背くことになり、文意が通りません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 58–61"
    },
    "skm2-p1-c11-q6": {
        "trans": "Regardless of whether one participates or not, please submit the response form by Friday without fail.",
        "ctx": "Administrative RSVP deadlines binding regardless of attendance.",
        "opt_reasons": {
            "を問わず": "「参加するしない」という動詞の肯定・否定の対立には「にかかわらず」が接続します。",
            "抜きで": "省略を表すため、出欠双方に対する提出義務の課達に合いません。",
            "に反して": "予想の裏切りを表すため、出欠返信の督促に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 58–61"
    },
    "skm2-p1-c11-q7": {
        "trans": "The emergency dispatch center responds to distress reports 365 days a year, regardless of seasons.",
        "ctx": "Emergency dispatch operational readiness across all seasons.",
        "opt_reasons": {
            "を問わず": "正解です。「四季を問わず」として季節の差異を不問にする慣用句です。",
            "抜きにして": "季節を排除することになり意味が破綻します。",
            "をもとに": "素材を表すため、通年の緊急出動体制に合いません。",
            "に反して": "季節に逆らうことになり、救助体制の記述に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 58–61"
    },
    "skm2-p1-c11-q8": {
        "trans": "Regardless of whether the actual result turns out to be a success or failure, having courageously challenged oneself is significant.",
        "ctx": "Validating ambitious challenges regardless of outcome.",
        "opt_reasons": {
            "を問わず": "成否という事態の帰結対比節には「にかかわらず」が自然です。",
            "抜きで": "結果を排除して挑戦することになり、結果に対する評価の超越に合いません。",
            "に反して": "結果に逆らう意味になり、挑戦の意義を認める文意とズレます。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 58–61"
    },
    "skm2-p1-c11-q9": {
        "trans": "The company recruits talented personnel widely, regardless of gender or academic background.",
        "ctx": "Egalitarian recruitment hiring regardless of gender or degree.",
        "opt_reasons": {
            "を問わず": "正解です。「性別や学歴を問わず」は典型的な人物属性の不問表現です。",
            "抜きにして": "学歴を排除するという意味になり、公平な無条件採用の趣旨に反します。",
            "をもとに": "学歴を素材にする意味になり、不問採用と矛盾します。",
            "に反して": "学歴に逆らう意味になり、採用方針の記述になりません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 58–61"
    },
    "skm2-p1-c11-q10": {
        "trans": "Regardless of whether you like it or dislike it, taking your prescribed medicine is an obligation as a patient.",
        "ctx": "Medical prescription compliance regardless of personal preference.",
        "opt_reasons": {
            "を問わず": "「好き嫌い」という心理的対立節には「にかかわらず」が適合します。",
            "抜きで": "省略を表すため、嫌いであっても飲むべき義務の強調に合いません。",
            "に反して": "好き嫌いに背くことになり、服薬指示として不自然です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 58–61"
    },
    "skm2-p1-c11-q11": {
        "trans": "All individuals are guaranteed fundamental human rights under the law, regardless of race or religion.",
        "ctx": "Constitutional human rights guarantees regardless of race or creed.",
        "opt_reasons": {
            "を問わず": "正解です。人種や信条による差別を禁じる法的主義の不問表明です。",
            "抜きにして": "人種や宗教を排除することになり、人権保障の文脈に反します。",
            "をもとに": "人種を素材にすることになり、人権規定として不適切です。",
            "に反して": "信条に逆らうことになり、法的平等の保障に合いません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 58–61"
    },
    "skm2-p1-c11-q12": {
        "trans": "Regardless of whether one's physical condition is good or poor, skipping daily basic practice is not permitted.",
        "ctx": "Strict discipline enforcing fundamental daily training regimens.",
        "opt_reasons": {
            "を問わず": "体調の良し悪しという状態対比には「にかかわらず」が自然です。",
            "抜きで": "体調を排除することになり、日課練習の厳格さに合いません。",
            "に反して": "体調に逆らうことになり、練習方針の表現として不自然です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 58–61"
    },

    # --- Chapter 12: 原因・理由 pp. 62–65 ---
    "skm2-p1-c12-q1": {
        "trans": "Far from receiving a salary raise, suffering from poor corporate performance, even our bonuses were slashed significantly.",
        "ctx": "Economic adversity where anticipated raises inverted into bonus cuts.",
        "opt_reasons": {
            "わけがない": "論理的不可能性を表すため、「給料が上がるどころかボーナスまで減った」という極端な逆転の現実に合いません。",
            "に相違ない": "強い確信を表すため、期待と真逆の過酷な現実の対比に不適です。",
            "にすぎない": "単なる限定を表すため、昇給どころか減額された激しい落差を表せません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 62–65"
    },
    "skm2-p1-c12-q2": {
        "trans": "A person as usually earnest and deeply responsible as him would never betray comrades and leak confidential information.",
        "ctx": "Refusing betrayal allegations due to consistent personal character.",
        "opt_reasons": {
            "どころか": "反駁対比を表すため、彼の誠実な人柄から導かれる絶対的不可能性に合いません。",
            "に相違ない": "情報漏洩したという確信になってしまい、仲間を信じる文脈と正反対になります。",
            "にすぎない": "限定を表すため、情報漏洩という重大背信の完全否定に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 62–65"
    },
    "skm2-p1-c12-q3": {
        "trans": "Judging from all the objective evidence and testimony, the suspect of this incident must undoubtedly be that person.",
        "ctx": "Investigative certainty attributing guilt based on forensic evidence.",
        "opt_reasons": {
            "わけがない": "犯人である可能性を完全否定することになり、証拠が揃った結論と矛盾します。",
            "どころか": "対比を表すため、証拠に基づく断定的な犯人特定に合いません。",
            "にすぎない": "過小評価を表すため、重大な犯行動定の確信に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 62–65"
    },
    "skm2-p1-c12-q4": {
        "trans": "Far from recovering from illness, complications developed and emergency surgical hospitalization became necessary.",
        "ctx": "Illness complications escalating instead of anticipated recovery.",
        "opt_reasons": {
            "わけがない": "回復の不可能性だけを述べる形になり、合併症を併発した悪化の落差が出ません。",
            "に相違ない": "病状が回復したと確信することになり、緊急手術の現実に矛盾します。",
            "にすぎない": "限定を表すため、病状の深刻な暗転の叙述に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 62–65"
    },
    "skm2-p1-c12-q5": {
        "trans": "Even if this novel won a minor literary prize, it is merely temporary praise and one cannot become a full-fledged author with just this.",
        "ctx": "Tempering early literary praise against the long road to mastery.",
        "opt_reasons": {
            "わけがない": "賞賛の完全否定になり、新人賞受賞の事実と矛盾します。",
            "どころか": "対比を表すため、過大評価を戒める「一時的な賞賛にすぎない」という抑制に合いません。",
            "に相違ない": "確信を表すため、「これだけで一人前になれるわけではない」という冷静な限定に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 62–65"
    },
    "skm2-p1-c12-q6": {
        "trans": "After practicing and studying relentlessly for months, there is no way we will fail in the actual examination.",
        "ctx": "Unshakeable confidence rooted in months of exhaustive preparation.",
        "opt_reasons": {
            "どころか": "反駁対比を表すため、絶対合格への確信に合いません。",
            "に相違ない": "本番で失敗すると確信することになり、猛練習を重ねた文脈と正反対になります。",
            "にすぎない": "限定を表すため、不合格の可能性の論理的排除に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 62–65"
    },
    "skm2-p1-c12-q7": {
        "trans": "Far from saving money, unanticipated medical and repair expenses accumulated, resulting in a deep financial deficit.",
        "ctx": "Financial deficits mounting instead of projected savings.",
        "opt_reasons": {
            "わけがない": "貯金できた可能性の否定にとどまり、大赤字に転落した劇的悪化に合いません。",
            "に相違ない": "貯金できたと確信することになり、赤字の現実に矛盾します。",
            "にすぎない": "限定を表すため、貯金どころか赤字になった事態の強調に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 62–65"
    },
    "skm2-p1-c12-q8": {
        "trans": "From the profound joy visible on his face, he must undoubtedly have passed his first-choice university.",
        "ctx": "Deducing exam triumph from overt joyous expressions.",
        "opt_reasons": {
            "わけがない": "合格したはずがないという意味になり、満面の笑みの描写と完全に衝突します。",
            "どころか": "対比を表すため、表情から読み取る確信の推量に合いません。",
            "にすぎない": "限定を表すため、合格への強い確信の表明に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 62–65"
    },
    "skm2-p1-c12-q9": {
        "trans": "That rumor is merely an unfounded suspicion to the very end, and one must never take it seriously.",
        "ctx": "Dismissing unverified rumors as mere groundless suspicion.",
        "opt_reasons": {
            "わけがない": "憶測の可能性を完全否定することになり、「信じてはならない」理由と矛盾します。",
            "どころか": "対比を表すため、噂を「単なる憶測」と過小評価して退ける文脈に合いません。",
            "に相違ない": "確信を表すため、「単なる憶測にすぎない」という過小評価のニュアンスが出ません。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 62–65"
    },
    "skm2-p1-c12-q10": {
        "trans": "He never even reads books normally, so there is no way he would read through a dense 500-page academic philosophy book.",
        "ctx": "Deeming dense philosophical reading impossible given non-reading habits.",
        "opt_reasons": {
            "どころか": "対比を表すため、普段読書しない彼が読了する不可能性の断定に合いません。",
            "に相違ない": "読み通したと確信することになり、普段本を読まない前提と矛盾します。",
            "にすぎない": "限定を表すため、読了の不可能性の論理的否定に不適です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 62–65"
    },
    "skm2-p1-c12-q11": {
        "trans": "Far from being grateful when I kindly offered advice, he got angry saying 'stop meddling in my affairs!'",
        "ctx": "Good intentions met with ungrateful hostility.",
        "opt_reasons": {
            "わけがない": "感謝したはずがないという意味にとどまり、逆ギレされた不条理な落差に合いません。",
            "に相違ない": "感謝したと確信することになり、激怒された現実に矛盾します。",
            "にすぎない": "限定を表すため、感謝どころか怒り出した逆転の強調に不適切です。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 62–65"
    },
    "skm2-p1-c12-q12": {
        "trans": "Because that research laboratory is equipped with world-class facilities and researchers, their thesis must undoubtedly be groundbreaking.",
        "ctx": "Assuming research brilliance based on world-class faculty.",
        "opt_reasons": {
            "わけがない": "画期的であるはずがないという意味になり、世界最高峰の設備を称える前文と衝突します。",
            "どころか": "対比を表すため、確固たる背景に基づく確信の推量に合いません。",
            "にすぎない": "過小評価を表すため、世界水準の研究所の論文の優位性に反します。"
        },
        "evid": "Shin Kanzen Master N2 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 62–65"
    }
}

updated = 0
for e in exercises:
    eid = e.get("id")
    if eid in REPAIRS_1_12:
        r = REPAIRS_1_12[eid]
        e["translation"] = r["trans"]
        e["context"] = r["ctx"]
        e["provenance"] = "source-derived"
        e["sourceEvidence"] = r["evid"]
        
        # Repair options
        expl = e.get("explanation", {})
        if isinstance(expl, dict):
            for opt in expl.get("options", []):
                txt = opt.get("text", "")
                if opt.get("isCorrect"):
                    continue
                else:
                    if txt in r["opt_reasons"]:
                        opt["reason"] = f"【不正解】{r['opt_reasons'][txt]}"
                    else:
                        matched = False
                        for k, v in r["opt_reasons"].items():
                            if k in txt or txt in k:
                                opt["reason"] = f"【不正解】{v}"
                                matched = True
                                break
                        if not matched:
                            opt["reason"] = f"【不正解】文脈・文法関係（{txt}）において不適切です。"
        updated += 1

print(f"Updated {updated} exercises in SKM N2 Part 1 Chapters 1–12.")

with open(EXERCISES_PATH, "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved updated chapterExercises.json successfully.")
