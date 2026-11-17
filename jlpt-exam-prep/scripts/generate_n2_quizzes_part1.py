# -*- coding: utf-8 -*-
import json

N2_QUIZZES_PART1 = {
  "added-n2-1-69": {
    "id": "q-added-n2-1-69-1",
    "question": "こちらの整理券は、商品を受け取る（　　）に必要となります。",
    "translation": "This numbered ticket will be necessary on the occasion of receiving your merchandise.",
    "options": ["際（さい）", "最中（さいちゅう）", "あげく", "末（すえ）"],
    "correctIndex": 0,
    "grammarFocus": "〜際（に） (On the Occasion Of / Formal When)",
    "ruleHint": "動詞辞書形 / た形 / 名詞+の + 際に; formal equivalent of とき used in public notifications.",
    "explanations": [
      {"text": "際（さい）", "isCorrect": True, "reason": "Correct! 〜際に is the formal business/public equivalent of とき: 受け取る際に."},
      {"text": "最中（さいちゅう）", "isCorrect": False, "reason": "Incorrect. 最中に denotes being in the middle of a continuous unfolding event."},
      {"text": "あげく", "isCorrect": False, "reason": "Incorrect. あげく denotes an unfortunate eventual outcome after trouble."},
      {"text": "末（すえ）", "isCorrect": False, "reason": "Incorrect. 末に requires extensive prior deliberation or struggle."}
    ]
  },
  "added-n2-2-70": {
    "id": "q-added-n2-2-70-1",
    "question": "アイスクリームが（　　）うちに、早く食べてしまいましょう。",
    "translation": "Let's eat the ice cream quickly before it melts.",
    "options": ["溶けない（とけない）", "溶けた", "溶ける", "溶けて"],
    "correctIndex": 0,
    "grammarFocus": "〜ないうちに (Before State Changes)",
    "ruleHint": "Verb ない-form + うちに expresses acting before a negative change occurs ('before it melts').",
    "explanations": [
      {"text": "溶けない（とけない）", "isCorrect": True, "reason": "Correct! 溶けないうちに means 'before it melts / while it is still frozen'."},
      {"text": "溶けた", "isCorrect": False, "reason": "Incorrect. 溶けた would mean after it already melted."},
      {"text": "溶ける", "isCorrect": False, "reason": "Incorrect. 溶けるうちに is contradictory for ice cream."},
      {"text": "溶けて", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach to うちに."}
    ]
  },
  "added-n2-2-71": {
    "id": "q-added-n2-2-71-1",
    "question": "体に悪いと知り（　　）、夜遅くにラーメンを食べてしまう。",
    "translation": "Even while knowing it is bad for my health, I end up eating ramen late at night.",
    "options": ["つつも", "つつ", "ながらも", "ものの"],
    "correctIndex": 0,
    "grammarFocus": "Concession: Verb stem + つつも (Even While)",
    "ruleHint": "Verb ます-stem + つつも acknowledges a contradictory mental state or awareness while doing the opposite.",
    "explanations": [
      {"text": "つつも", "isCorrect": True, "reason": "Correct! 知りつつも expresses moral/cognitive conflict ('even while fully conscious of it')."},
      {"text": "つつ", "isCorrect": False, "reason": "Incorrect. Bare つつ typically marks simultaneous formal action, whereas contradiction takes つつも."},
      {"text": "ながらも", "isCorrect": False, "reason": "Incorrect. ながらも usually attaches to adjectives or nouns, while verb cognitive conflict canonically takes つつも."},
      {"text": "ものの", "isCorrect": False, "reason": "Incorrect. ものの requires plain form (知っているものの)."}
    ]
  },
  "added-n2-3-72": {
    "id": "q-added-n2-3-72-1",
    "question": "詳しい日程が決まり（　　）、メールにてご連絡申し上げます。",
    "translation": "As soon as the detailed schedule is decided, we will contact you by email.",
    "options": ["次第（しだい）", "次第で", "次第だ", "次第に"],
    "correctIndex": 0,
    "grammarFocus": "Immediate Future Succession: Verb stem + 次第 (As soon as)",
    "ruleHint": "Verb ます-stem + 次第 indicates immediate subsequent action once an event happens.",
    "explanations": [
      {"text": "次第（しだい）", "isCorrect": True, "reason": "Correct! 決まり次第 denotes immediate subsequent contact in formal correspondence."},
      {"text": "次第で", "isCorrect": False, "reason": "Incorrect. 次第で means 'depending on' after a noun."},
      {"text": "次第だ", "isCorrect": False, "reason": "Incorrect. 次第だ appears at the end of a sentence to explain background reasons."},
      {"text": "次第に", "isCorrect": False, "reason": "Incorrect. 次第に is an adverb meaning 'gradually'."}
    ]
  },
  "added-n2-3-73": {
    "id": "q-added-n2-3-73-1",
    "question": "大学を卒業し（　　）以来、彼とは一度も会っていません。",
    "translation": "Ever since graduating from university, I have not met him even once.",
    "options": ["て", "た", "る", "ない"],
    "correctIndex": 0,
    "grammarFocus": "Continuous State Since: Verb て-form + 以来",
    "ruleHint": "Verb て-form + 以来 indicates an unbroken condition that has persisted continuously since an initial starting point.",
    "explanations": [
      {"text": "て", "isCorrect": True, "reason": "Correct! 卒業して以来 expresses an unbroken state persisting since graduation."},
      {"text": "た", "isCorrect": False, "reason": "Incorrect. Past form cannot precede 以来."},
      {"text": "る", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot precede 以来."},
      {"text": "ない", "isCorrect": False, "reason": "Incorrect. Negative form cannot precede 以来."}
    ]
  },
  "added-n2-3-74": {
    "id": "q-added-n2-3-74-1",
    "question": "上司の許可をもらっ（　　）からでないと、この契約を進めることはできません。",
    "translation": "Unless we first obtain the supervisor's approval, we cannot proceed with this contract.",
    "options": ["て", "た", "る", "ない"],
    "correctIndex": 0,
    "grammarFocus": "Prerequisite Condition: Verb て-form + からでないと",
    "ruleHint": "〜てからでないと is strictly paired with a negative predicate to express an indispensable prerequisite.",
    "explanations": [
      {"text": "て", "isCorrect": True, "reason": "Correct! もらってからでないと expresses that approval is an indispensable prerequisite."},
      {"text": "た", "isCorrect": False, "reason": "Incorrect. Ta-form cannot attach to からでないと."},
      {"text": "る", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach to からでないと."},
      {"text": "ない", "isCorrect": False, "reason": "Incorrect. Negative form cannot attach to からでないと."}
    ]
  },
  "added-n2-4-75": {
    "id": "q-added-n2-4-75-1",
    "question": "一年（　　）通して、この島は温暖で過ごしやすい気候です。",
    "translation": "Throughout the entire year, this island has a mild and pleasant climate.",
    "options": ["を", "に", "で", "へ"],
    "correctIndex": 0,
    "grammarFocus": "Spanning Entire Period: 〜を通して (とおして)",
    "ruleHint": "Noun (Period) + を通して marks continuous duration across an entire time span.",
    "explanations": [
      {"text": "を", "isCorrect": True, "reason": "Correct! 一年を通して marks the entire span of the year."},
      {"text": "に", "isCorrect": False, "reason": "Incorrect. に通して is ungrammatical."},
      {"text": "で", "isCorrect": False, "reason": "Incorrect. で通して is ungrammatical."},
      {"text": "へ", "isCorrect": False, "reason": "Incorrect. へ通して is ungrammatical."}
    ]
  },
  "added-n2-4-76": {
    "id": "q-added-n2-4-76-1",
    "question": "声の（　　）限りに叫んだが、波の音にかき消されてしまった。",
    "translation": "I screamed at the top of my voice, but it was drowned out by the sound of the waves.",
    "options": ["出せる", "出そう", "出した", "出す"],
    "correctIndex": 0,
    "grammarFocus": "Maximal Limit: 〜限りに (To the Limit of Ability)",
    "ruleHint": "Potential verb plain form (出せる) + 限りに denotes exerting oneself to the utmost limit.",
    "explanations": [
      {"text": "出せる", "isCorrect": True, "reason": "Correct! 声の出せる限りに is the fixed idiom for shouting to the utmost limit of one's vocal capacity."},
      {"text": "出そう", "isCorrect": False, "reason": "Incorrect. Volitional form cannot attach to 限りに."},
      {"text": "出した", "isCorrect": False, "reason": "Incorrect. Past form does not denote maximal capability."},
      {"text": "出す", "isCorrect": False, "reason": "Incorrect. Standard capability limit requires potential 出せる."}
    ]
  },
  "added-n2-5-77": {
    "id": "q-added-n2-5-77-1",
    "question": "本日の公演に（　　）、特別割引価格でご入場いただけます。",
    "translation": "Only for today's performance, admission is available at a special discounted price.",
    "options": ["限り", "限って", "限れば", "限ると"],
    "correctIndex": 0,
    "grammarFocus": "Exclusive Privilege: 〜に限り (Strictly Limited To)",
    "ruleHint": "Noun + に限り announces special exclusive provisions, discounts, or exceptions.",
    "explanations": [
      {"text": "限り", "isCorrect": True, "reason": "Correct! 本日の公演に限り specifies exclusive limitation in official announcements."},
      {"text": "限って", "isCorrect": False, "reason": "Incorrect. に限って expresses unfortunate coincidence or subjective bias ('of all days!')."},
      {"text": "限れば", "isCorrect": False, "reason": "Incorrect. に限れば is a provisional conditional."},
      {"text": "限ると", "isCorrect": False, "reason": "Incorrect. に限ると does not form this announcement formula."}
    ]
  },
  "added-n2-5-78": {
    "id": "q-added-n2-5-78-1",
    "question": "私が知っている（　　）では、彼はそのような不正に関与していません。",
    "translation": "As far as I know, he is not involved in any such wrongdoing.",
    "options": ["限り", "だけ", "ほど", "ばかり"],
    "correctIndex": 0,
    "grammarFocus": "Scope of Information: 〜限りでは (Insofar As)",
    "ruleHint": "Verb plain form (知っている, 聞いた) + 限りでは limits one's assertion to current personal knowledge.",
    "explanations": [
      {"text": "限り", "isCorrect": True, "reason": "Correct! 知っている限りでは limits the truth of the statement to the speaker's informational scope."},
      {"text": "だけ", "isCorrect": False, "reason": "Incorrect. だけでは means 'merely with X', expressing insufficient grounds."},
      {"text": "ほど", "isCorrect": False, "reason": "Incorrect. ほどでは indicates degree, not informational boundaries."},
      {"text": "ばかり", "isCorrect": False, "reason": "Incorrect. ばかりでは does not form this scope formula."}
    ]
  },
  "added-n2-6-79": {
    "id": "q-added-n2-6-79-1",
    "question": "この商品は国内（　　）ならず、海外でも高く評価されている。",
    "translation": "This merchandise is highly evaluated not only domestically, but overseas as well.",
    "options": ["のみ", "ばかり", "だけ", "ほど"],
    "correctIndex": 0,
    "grammarFocus": "Formal Scope Addition: 〜のみならず (Not only X, but Y)",
    "ruleHint": "Noun + のみならず is the formal written equivalent of だけでなく.",
    "explanations": [
      {"text": "のみ", "isCorrect": True, "reason": "Correct! 〜のみならず is the canonical formal addition pattern: 国内のみならず."},
      {"text": "ばかり", "isCorrect": False, "reason": "Incorrect. ばかりならず is ungrammatical (takes ばかりか instead)."},
      {"text": "だけ", "isCorrect": False, "reason": "Incorrect. だけならず is ungrammatical (takes だけでなく instead)."},
      {"text": "ほど", "isCorrect": False, "reason": "Incorrect. ほどならず is ungrammatical."}
    ]
  },
  "added-n2-7-80": {
    "id": "q-added-n2-7-80-1",
    "question": "兄が社交的で活発な（　　）、弟は物静かで読書を好む。",
    "translation": "In sharp contrast to the older brother being outgoing and active, the younger brother is quiet and prefers reading.",
    "options": ["のに対して", "反面", "について", "にとって"],
    "correctIndex": 0,
    "grammarFocus": "Contrast Between Two Entities: 〜のに対して",
    "ruleHint": "に対して contrasts two DIFFERENT subjects (兄 vs 弟); 反面 contrasts two aspects of the SAME subject.",
    "explanations": [
      {"text": "のに対して", "isCorrect": True, "reason": "Correct! 〜のに対して directly contrasts two distinct individuals (兄 vs 弟)."},
      {"text": "反面", "isCorrect": False, "reason": "Incorrect. 反面 contrasts two sides of the same subject (e.g. 兄 is clever on one hand, but careless on the other)."},
      {"text": "について", "isCorrect": False, "reason": "Incorrect. について indicates topic of inquiry."},
      {"text": "にとって", "isCorrect": False, "reason": "Incorrect. にとって indicates evaluative stance."}
    ]
  },
  "added-n2-8-81": {
    "id": "q-added-n2-8-81-1",
    "question": "優れた指導者の（　　）で、選手たちはめざましい成長を遂げた。",
    "translation": "Under the guidance of an outstanding mentor, the athletes achieved remarkable growth.",
    "options": ["もと", "うえ", "あいだ", "なか"],
    "correctIndex": 0,
    "grammarFocus": "Under the Influence / Auspices: 〜のもとで",
    "ruleHint": "Noun + のもとで expresses living, developing, or working under someone's authority, guidance, or influence.",
    "explanations": [
      {"text": "もと", "isCorrect": True, "reason": "Correct! 指導者のもとで means 'under the guidance and influence of a mentor'."},
      {"text": "うえ", "isCorrect": False, "reason": "Incorrect. のうえで means 'after doing' or 'on the basis of'."},
      {"text": "あいだ", "isCorrect": False, "reason": "Incorrect. のあいだで means 'between / among people'."},
      {"text": "なか", "isCorrect": False, "reason": "Incorrect. のなかで means 'in the middle of / within a group'."}
    ]
  },
  "added-n2-8-82": {
    "id": "q-added-n2-8-82-1",
    "question": "この絵本は、小さな子供（　　）にわかりやすい言葉で書かれている。",
    "translation": "This picture book is written in easy-to-understand language targeted at young children.",
    "options": ["向け", "向き", "当て", "対し"],
    "correctIndex": 0,
    "grammarFocus": "Targeted Design: Noun + 向け (むけ)",
    "ruleHint": "〜向け means specifically designed or created for that target audience; 〜向き means naturally suited for.",
    "explanations": [
      {"text": "向け", "isCorrect": True, "reason": "Correct! 子供向け indicates intentional design and customization for children."},
      {"text": "向き", "isCorrect": False, "reason": "Incorrect. 向き denotes inherent suitability, not purposeful targeting."},
      {"text": "当て", "isCorrect": False, "reason": "Incorrect. 当て (あて) denotes mail destination / addressee."},
      {"text": "対し", "isCorrect": False, "reason": "Incorrect. に対し requires particle に."}
    ]
  },
  "added-n2-9-83": {
    "id": "q-added-n2-9-83-1",
    "question": "経済の発展に（　　）、国民の生活様式も大きく変化してきた。",
    "translation": "Concomitant with the development of the economy, the lifestyle of citizens has also changed significantly.",
    "options": ["伴って（ともなって）", "対して", "際して", "通して"],
    "correctIndex": 0,
    "grammarFocus": "Concomitant Change: 〜に伴って (ともなって)",
    "ruleHint": "Noun / Verb 辞書形 + に伴って expresses large-scale simultaneous social or natural change.",
    "explanations": [
      {"text": "伴って（ともなって）", "isCorrect": True, "reason": "Correct! 発展に伴って expresses macro-level parallel socio-economic transformation."},
      {"text": "対して", "isCorrect": False, "reason": "Incorrect. に対して marks target or contrast."},
      {"text": "際して", "isCorrect": False, "reason": "Incorrect. に際して marks milestone occasions."},
      {"text": "通して", "isCorrect": False, "reason": "Incorrect. を通して marks duration or medium."}
    ]
  },
  "added-n2-9-84": {
    "id": "q-added-n2-9-84-1",
    "question": "成功するかどうかは、君自身の今後の努力（　　）だ。",
    "translation": "Whether you succeed or not is dependent on your own future efforts.",
    "options": ["次第（しだい）", "きり", "あげく", "末（すえ）"],
    "correctIndex": 0,
    "grammarFocus": "Contingency: Noun + 次第だ (Depends on)",
    "ruleHint": "Noun + 次第だ indicates that an outcome is entirely contingent upon that determining factor.",
    "explanations": [
      {"text": "次第（しだい）", "isCorrect": True, "reason": "Correct! 努力次第だ expresses that the outcome depends entirely upon one's effort."},
      {"text": "きり", "isCorrect": False, "reason": "Incorrect. きり indicates sole continuous occurrence ('ever since')."},
      {"text": "あげく", "isCorrect": False, "reason": "Incorrect. あげく requires past tense and indicates tragic results."},
      {"text": "末（すえ）", "isCorrect": False, "reason": "Incorrect. 末だ is ungrammatical in this structure."}
    ]
  },
  "added-n2-10-85": {
    "id": "q-added-n2-10-85-1",
    "question": "仕事が山積みで、書類の整理（　　）会議の準備（　　）で目が回る忙しさだ。",
    "translation": "Work is piling up; what with organizing documents and preparing for meetings, I am dizzy with busyness.",
    "options": ["やら／やら", "だの／だの", "なり／なり", "につけ／につけ"],
    "correctIndex": 0,
    "grammarFocus": "Disorganized Listing: 〜やら〜やら",
    "ruleHint": "Noun + やら + Noun + やら lists chaotic, overwhelming things happening simultaneously.",
    "explanations": [
      {"text": "やら／やら", "isCorrect": True, "reason": "Correct! 〜やら〜やら conveys a frantic sense of multiple chaotic tasks."},
      {"text": "だの／だの", "isCorrect": False, "reason": "Incorrect. だの/だの expresses annoyance or complaining tone."},
      {"text": "なり／なり", "isCorrect": False, "reason": "Incorrect. なり/なり suggests alternative choices ('either A or B')."},
      {"text": "につけ／につけ", "isCorrect": False, "reason": "Incorrect. につけ/につけ expresses emotional reaction every time ('whenever A or B')."}
    ]
  },
  "added-n2-10-86": {
    "id": "q-added-n2-10-86-1",
    "question": "賛成するに（　　）反対するに（　　）、きちんとした論理的な根拠を示すべきだ。",
    "translation": "Whether you agree or disagree, you should demonstrate a proper logical rationale.",
    "options": ["しても／しても", "せよ／せよ", "しては／しては", "したら／したら"],
    "correctIndex": 0,
    "grammarFocus": "Whether A or B: 〜にしても〜にしても",
    "ruleHint": "〜にしても〜にしても lists opposite scenarios to state that the same principle applies regardless.",
    "explanations": [
      {"text": "しても／しても", "isCorrect": True, "reason": "Correct! 〜にしても〜にしても states that the requirement applies equally to both cases."},
      {"text": "せよ／せよ", "isCorrect": False, "reason": "Incorrect. にせよ/にせよ is archaic literary, whereas standard style takes にしても."},
      {"text": "しては／しては", "isCorrect": False, "reason": "Incorrect. にしては indicates unexpectedness relative to standard."},
      {"text": "したら／したら", "isCorrect": False, "reason": "Incorrect. にしたら indicates judging from someone's perspective."}
    ]
  },
  "added-n2-11-87": {
    "id": "q-added-n2-11-87-1",
    "question": "このマラソン大会は、年齢や性別（　　）誰でも自由に参加できる。",
    "translation": "This marathon allows anyone to participate freely, regardless of age or gender.",
    "options": ["を問わず（をとわず）", "にもかかわらず", "を抜きにして", "はさておき"],
    "correctIndex": 0,
    "grammarFocus": "Regardless Of: Noun + を問わず (をとわず)",
    "ruleHint": "Noun (with inherent pairs/ranges: 年齢, 性別, 昼夜, 国籍) + を問わず = without being questioned or restricted by.",
    "explanations": [
      {"text": "を問わず（をとわず）", "isCorrect": True, "reason": "Correct! 年齢や性別を問わず is the fixed public formula for universal eligibility."},
      {"text": "にもかかわらず", "isCorrect": False, "reason": "Incorrect. にもかかわらず indicates contrary expectation ('in spite of')."},
      {"text": "を抜きにして", "isCorrect": False, "reason": "Incorrect. を抜きにして means 'dispensing with X'."},
      {"text": "はさておき", "isCorrect": False, "reason": "Incorrect. はさておき means 'setting aside for now'."}
    ]
  },
  "added-n2-12-88": {
    "id": "q-added-n2-12-88-1",
    "question": "あんな悪質な嘘をつく人を、もう二度と信用する（　　）か！",
    "translation": "There is no way in hell I will ever trust someone who tells such malicious lies again!",
    "options": ["もの", "こと", "わけ", "ところ"],
    "correctIndex": 0,
    "grammarFocus": "Vehement Categorical Negation: 〜ものか / 〜もんか",
    "ruleHint": "Verb 辞書形 + ものか expresses intense emotional rejection ('as if I ever would! / no way!').",
    "explanations": [
      {"text": "もの", "isCorrect": True, "reason": "Correct! 〜ものか expresses vehement rejection of the premise."},
      {"text": "こと", "isCorrect": False, "reason": "Incorrect. ことか expresses intense exclamation of emotional degree ('how very...!')."},
      {"text": "わけ", "isCorrect": False, "reason": "Incorrect. わけか does not form this emphatic negation."},
      {"text": "ところ", "isCorrect": False, "reason": "Incorrect. ところか does not form emotional rejection."}
    ]
  },
  "added-n2-13-89": {
    "id": "q-added-n2-13-89-1",
    "question": "「人工知能（AI）」と（　　）、近年急速に進化している計算技術のことだ。",
    "translation": "'Artificial Intelligence (AI)' refers to computational technology that has advanced rapidly in recent years.",
    "options": ["は", "いえば", "いうと", "したら"],
    "correctIndex": 0,
    "grammarFocus": "Formal Term Definition: Noun + とは",
    "ruleHint": "Noun + とは is the standard grammatical formula for defining a term or concept.",
    "explanations": [
      {"text": "は", "isCorrect": True, "reason": "Correct! Noun + とは defines a word, concept, or terminology: 人工知能とは."},
      {"text": "いえば", "isCorrect": False, "reason": "Incorrect. といえば prompts a spontaneous topic association ('speaking of...')."},
      {"text": "いうと", "isCorrect": False, "reason": "Incorrect. というと prompts an inquiry or clarification."},
      {"text": "したら", "isCorrect": False, "reason": "Incorrect. としたら introduces a hypothetical condition ('if we assume')."}
    ]
  },
  "added-n2-13-90": {
    "id": "q-added-n2-13-90-1",
    "question": "山頂から見下ろした満天の星空の美しさ（　　）、息をのむほどだった。",
    "translation": "The sheer beauty of the starlit sky looking down from the summit—it was breathtaking beyond words.",
    "options": ["といったら", "といえば", "というと", "といっても"],
    "correctIndex": 0,
    "grammarFocus": "Inexpressible Emotional Exclamation: Noun + といったら",
    "ruleHint": "Noun + といったら highlights an intense emotional impression that cannot be adequately put into words.",
    "explanations": [
      {"text": "といったら", "isCorrect": True, "reason": "Correct! 美しさといったら introduces an overwhelming impression of extraordinary degree."},
      {"text": "といえば", "isCorrect": False, "reason": "Incorrect. といえば prompts topic association, not overwhelming emotional exclamation."},
      {"text": "というと", "isCorrect": False, "reason": "Incorrect. というと asks for clarification."},
      {"text": "といっても", "isCorrect": False, "reason": "Incorrect. といっても introduces qualification ('although it is called X')."}
    ]
  },
  "added-n2-14-91": {
    "id": "q-added-n2-14-91-1",
    "question": "激しい風雨（　　）かかわらず、多くの観客が競技場に詰めかけた。",
    "translation": "Despite the violent wind and rain, a large crowd packed into the stadium.",
    "options": ["にも", "をも", "でも", "とも"],
    "correctIndex": 0,
    "grammarFocus": "Contrary to Fact: 〜にもかかわらず",
    "ruleHint": "Noun / Plain form + にもかかわらず indicates an outcome contrary to what one would expect from that fact.",
    "explanations": [
      {"text": "にも", "isCorrect": True, "reason": "Correct! 〜にもかかわらず is the fixed formula for adversative concession ('in spite of')."},
      {"text": "をも", "isCorrect": False, "reason": "Incorrect. をもかかわらず is ungrammatical (takes もかまわず instead for personal indifference)."},
      {"text": "でも", "isCorrect": False, "reason": "Incorrect. でもかかわらず is ungrammatical."},
      {"text": "とも", "isCorrect": False, "reason": "Incorrect. ともかかわらず is ungrammatical."}
    ]
  },
  "added-n2-14-92": {
    "id": "q-added-n2-14-92-1",
    "question": "いくら給料が良い（　　）いって、過酷な重労働に耐えられるわけではない。",
    "translation": "Just because the salary is good, it doesn't mean one can endure brutal heavy labor.",
    "options": ["からと", "だからと", "のでと", "ためと"],
    "correctIndex": 0,
    "grammarFocus": "Partial Concession: 〜からといって (Just because X, doesn't mean Y)",
    "ruleHint": "Plain form + からといって followed by negative denies that reason X automatically justifies consequence Y.",
    "explanations": [
      {"text": "からと", "isCorrect": True, "reason": "Correct! 〜からといって introduces a rejected justification paired with 〜わけではない."},
      {"text": "だからと", "isCorrect": False, "reason": "Incorrect. い-adjective (良い) attaches directly to からといって without だ."},
      {"text": "のでと", "isCorrect": False, "reason": "Incorrect. のでといって is ungrammatical."},
      {"text": "ためと", "isCorrect": False, "reason": "Incorrect. ためといって is ungrammatical."}
    ]
  },
  "added-n2-15-93": {
    "id": "q-added-n2-15-93-1",
    "question": "仮にその証言が真実だ（　　）としても、裁判の結果を覆すことは難しい。",
    "translation": "Even assuming that testimony were true, it would be difficult to overturn the court's verdict.",
    "options": ["と", "に", "で", "を"],
    "correctIndex": 0,
    "grammarFocus": "Hypothetical Concession: 〜としたら / 〜としても",
    "ruleHint": "仮に + Plain form + としても concedes a hypothetical premise while denying its impact on the outcome.",
    "explanations": [
      {"text": "と", "isCorrect": True, "reason": "Correct! 〜としても establishes a hypothetical concession ('even granting that...')."},
      {"text": "に", "isCorrect": False, "reason": "Incorrect. にしても takes noun directly without だ (真実だにしても is ungrammatical)."},
      {"text": "で", "isCorrect": False, "reason": "Incorrect. でしても is ungrammatical."},
      {"text": "を", "isCorrect": False, "reason": "Incorrect. をしても is ungrammatical."}
    ]
  },
  "added-n2-15-94": {
    "id": "q-added-n2-15-94-1",
    "question": "彼にこの秘密を話（　　）ものなら、町中に広まって大変なことになる。",
    "translation": "If by some awful mistake you were to tell him this secret, it would spread throughout the entire town with disastrous results.",
    "options": ["そう", "す", "した", "して"],
    "correctIndex": 0,
    "grammarFocus": "Dreaded Catastrophic Condition: Verb 意向形 + ものなら",
    "ruleHint": "Verb volitional form (話そう) + ものなら introduces a dreaded hypothetical action that triggers catastrophe.",
    "explanations": [
      {"text": "そう", "isCorrect": True, "reason": "Correct! Volitional form (話そう) + ものなら denotes a dreaded action sparking catastrophe."},
      {"text": "す", "isCorrect": False, "reason": "Incorrect. Dictionary form cannot attach to this dreaded conditional."},
      {"text": "した", "isCorrect": False, "reason": "Incorrect. Past form cannot precede this volitional conditional."},
      {"text": "して", "isCorrect": False, "reason": "Incorrect. Te-form cannot attach to ものなら."}
    ]
  },
  "added-n2-16-95": {
    "id": "q-added-n2-16-95-1",
    "question": "本日、施設点検の（　　）、午後五時にて全館閉館とさせていただきます。",
    "translation": "Due to facility inspection today, the entire building will be closed at 5:00 PM.",
    "options": ["につき", "につれ", "にしたがい", "にそって"],
    "correctIndex": 0,
    "grammarFocus": "Official Written Notice Cause: Noun + につき",
    "ruleHint": "Noun + につき is standard formal phrasing on official notices and signs stating a public justification.",
    "explanations": [
      {"text": "につき", "isCorrect": True, "reason": "Correct! 〜につき is formal written shorthand for 'due to' on public placards."},
      {"text": "につれ", "isCorrect": False, "reason": "Incorrect. につれ indicates proportional change over time."},
      {"text": "にしたがい", "isCorrect": False, "reason": "Incorrect. に従い indicates following rules or gradual progression."},
      {"text": "にそって", "isCorrect": False, "reason": "Incorrect. に沿って means 'in alignment with'."}
    ]
  },
  "added-n2-16-96": {
    "id": "q-added-n2-16-96-1",
    "question": "合格の知らせを聞いて、嬉しさの（　　）思わず涙がこぼれた。",
    "translation": "Hearing the news that I passed, I was so overcome with joy that tears spilled over spontaneously.",
    "options": ["あまり", "おかげ", "せい", "わけ"],
    "correctIndex": 0,
    "grammarFocus": "Overcome by Emotion: Noun + のあまり",
    "ruleHint": "Emotional Noun + のあまり indicates experiencing such excessive emotion that an involuntary reaction occurs.",
    "explanations": [
      {"text": "あまり", "isCorrect": True, "reason": "Correct! 嬉しさのあまり expresses being completely overcome by extreme joy."},
      {"text": "おかげ", "isCorrect": False, "reason": "Incorrect. おかげ denotes cognitive gratitude, not physical overwhelm."},
      {"text": "せい", "isCorrect": False, "reason": "Incorrect. せい indicates fault/blame for a negative event."},
      {"text": "わけ", "isCorrect": False, "reason": "Incorrect. わけ indicates logical reason."}
    ]
  },
  "added-n2-17-97": {
    "id": "q-added-n2-17-97-1",
    "question": "試験も終わった（　　）、今夜はみんなでパーッと飲みに行こう。",
    "translation": "Since exams are finished and all, let's all go out for a big celebration tonight.",
    "options": ["ことだし", "ものだし", "わけだし", "ところだし"],
    "correctIndex": 0,
    "grammarFocus": "Casual Justification: 〜ことだし",
    "ruleHint": "Plain form + ことだし presents one agreeable reason among others to suggest or encourage an action.",
    "explanations": [
      {"text": "ことだし", "isCorrect": True, "reason": "Correct! 〜ことだし presents a favorable circumstance motivating an invitation."},
      {"text": "ものだし", "isCorrect": False, "reason": "Incorrect. ものだし is nonstandard in this usage."},
      {"text": "わけだし", "isCorrect": False, "reason": "Incorrect. わけだし states an obvious logical conclusion rather than a casual impetus."},
      {"text": "ところだし", "isCorrect": False, "reason": "Incorrect. ところだし specifies temporal timing, not justification."}
    ]
  },
  "added-n2-17-98": {
    "id": "q-added-n2-17-98-1",
    "question": "一度チームの代表を引き受けた（　　）は、最後まで全力を尽くす責任がある。",
    "translation": "Now that I have accepted the position of team representative, I have a duty to do my utmost to the end.",
    "options": ["からに", "うえに", "だけに", "あまりに"],
    "correctIndex": 0,
    "grammarFocus": "Moral Commitment: 〜からには (Now that / Insofar as)",
    "ruleHint": "Verb た-form + からには expresses resolute duty, determination, or moral obligation in the main clause.",
    "explanations": [
      {"text": "からに", "isCorrect": True, "reason": "Correct! 〜からには denotes absolute resolve based on an undertaken commitment."},
      {"text": "うえに", "isCorrect": False, "reason": "Incorrect. 上に indicates addition ('moreover'), not moral resolve."},
      {"text": "だけに", "isCorrect": False, "reason": "Incorrect. だけに indicates proportional natural result."},
      {"text": "あまりに", "isCorrect": False, "reason": "Incorrect. あまりに expresses extreme excess of emotion."}
    ]
  },
  "added-n2-18-99": {
    "id": "q-added-n2-18-99-1",
    "question": "長年連れ添った愛犬を失った彼の悲しみは、傍から見ても察し（　　）ものがある。",
    "translation": "His grief over losing his beloved dog of many years is deeply palpable, even watching from the outside.",
    "options": ["がたい", "かねる", "づらい", "にくい"],
    "correctIndex": 0,
    "grammarFocus": "Psychological Impossibility: Verb stem + がたい",
    "ruleHint": "Verb ます-stem + がたい expresses psychological, emotional, or moral impossibility (察しがたい, 信じがたい).",
    "explanations": [
      {"text": "がたい", "isCorrect": True, "reason": "Correct! 察しがたい expresses profound psychological depth of feeling."},
      {"text": "かねる", "isCorrect": False, "reason": "Incorrect. かねる expresses polite professional refusal based on principle."},
      {"text": "づらい", "isCorrect": False, "reason": "Incorrect. づらい denotes physical or practical discomfort."},
      {"text": "にくい", "isCorrect": False, "reason": "Incorrect. にくい denotes standard objective difficulty."}
    ]
  },
  "added-n2-18-100": {
    "id": "q-added-n2-18-100-1",
    "question": "明日は大事な最終面接があるから、今夜は飲み会に行く（　　）ではない。",
    "translation": "Because I have an important final interview tomorrow, tonight is absolutely no time to be going to a drinking party.",
    "options": ["どころ", "わけ", "はず", "もの"],
    "correctIndex": 0,
    "grammarFocus": "Circumstantial Infeasibility: 〜どころではない",
    "ruleHint": "〜どころではない indicates that circumstances are far too critical to permit entertaining such an action.",
    "explanations": [
      {"text": "どころ", "isCorrect": True, "reason": "Correct! 飲み会に行くどころではない emphasizes total circumstantial impossibility due to a grave priority."},
      {"text": "わけ", "isCorrect": False, "reason": "Incorrect. わけではない is weak partial negation ('it's not that I can't go')."},
      {"text": "はず", "isCorrect": False, "reason": "Incorrect. はずではない is ungrammatical (takes はずがない)."},
      {"text": "もの", "isCorrect": False, "reason": "Incorrect. ものではない is a moral admonition ('you should not')."}
    ]
  }
}

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

updated = 0
for p in points:
    if p['id'] in N2_QUIZZES_PART1 and len(p.get('quiz', [])) == 0:
        p['quiz'] = [N2_QUIZZES_PART1[p['id']]]
        updated += 1

with open("jlpt-exam-prep/src/data/studyPoints.json", "w", encoding="utf-8") as f:
    json.dump(points, f, ensure_ascii=False, indent=2)

print(f"Added quizzes to {updated} Shin Kanzen Master N2 Part 1 cards!")
