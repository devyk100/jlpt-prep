import json

# Define the 4 missing SKM N2 cards with full sentences, nuance, and quiz
NEW_SKM2_CARDS = [
  {
    "id": "skm2-p2-majiki",
    "book": "Shin Kanzen Master N2",
    "chapter": "Part 2 · Chapter 2",
    "title": "〜まじき (Utterly Impermissible / Unpardonable for One in Such a Role)",
    "meaning": "Utterly unforgivable, impermissible, or unbecoming for someone in that professional or moral position.",
    "connection": "動詞辞書形 + まじき + 名詞 (する irregular: すまじき or するまじき)",
    "nuance": "Strict ethical prohibition based on professional duty, social status, or moral obligation ('あるまじき行為', '許すまじき暴言'). Modifies an abstract noun. Reserved for serious moral/professional transgressions; never used for trivial personal errors.",
    "sentences": [
      {
        "id": "skm2-p2-majiki::s1",
        "japanese": "公金を私的に流用するなど、政治家としてあるまじき不正行為である。",
        "english": "Embezzling public funds for personal use is an unpardonable fraudulent act, completely unbecoming of a politician.",
        "tokens": [],
        "useLabel": "Professional / Public Ethical Transgression",
        "nuanceNote": "Modifies 不正行為; highlights violation of public trust."
      },
      {
        "id": "skm2-p2-majiki::s2",
        "japanese": "患者の個人情報を第三者に漏洩することは、医師として許すまじき重大な背信行為だ。",
        "english": "Leaking a patient's personal records to a third party is an unforgivable grave breach of trust for a physician.",
        "tokens": [],
        "useLabel": "Medical / Professional Oath Violation",
        "nuanceNote": "許すまじき modifies 背信行為; emphasizes categorical moral violation."
      },
      {
        "id": "skm2-p2-majiki::s3",
        "japanese": "弱い立場の者を脅迫して金品を巻き上げるなど、人間としてあるまじき卑劣なやり方だ。",
        "english": "Intimidating vulnerable people to extort valuables is a contemptible method that should never be permitted of any human being.",
        "tokens": [],
        "useLabel": "Fundamental Humanitarian Transgression",
        "nuanceNote": "人間としてあるまじき applies universally to unacceptable human conduct."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-p2-majiki-1",
        "question": "公金を私的に流用するなど、政治家としてある（　　）不正行為である。",
        "translation": "Embezzling public funds for personal use is an unpardonable fraudulent act, completely unbecoming of a politician.",
        "options": ["まじき", "べき", "はずの", "限りの"],
        "correctIndex": 0,
        "grammarFocus": "〜まじき (Unpardonable for One in Such a Role)",
        "ruleHint": "動詞辞書形 + まじき + Noun; denotes moral impermissibility based on status.",
        "explanations": [
          {"text": "まじき", "isCorrect": True, "reason": "Correct! あるまじき modifies 不正行為 to express an unpardonable violation of status."},
          {"text": "べき", "isCorrect": False, "reason": "Incorrect. べき expresses moral duty ('should do'), creating an contradictory meaning here."},
          {"text": "はずの", "isCorrect": False, "reason": "Incorrect. はず expresses objective expectation ('supposed to be')."},
          {"text": "限りの", "isCorrect": False, "reason": "Incorrect. 限りの expresses limitation ('to the extent of')."}
        ]
      }
    ]
  },
  {
    "id": "skm2-p2-bekarazu",
    "book": "Shin Kanzen Master N2",
    "chapter": "Part 2 · Chapter 2",
    "title": "〜べからず / 〜べからざる (Must Not / Strictly Prohibited on Signs & Decrees)",
    "meaning": "Must not do / strictly forbidden on public notices, signs, slogans, and formal decrees.",
    "connection": "動詞辞書形 + べからず (sentence end) | 動詞辞書形 + べからざる + 名詞 (する: すべからず / すべからざる)",
    "nuance": "Stiff archaic prohibitive command used almost exclusively on posted signs ('立ち入るべからず' = Keep Out), warning placards, and traditional maxims ('初心忘るべからず'). In attributive form, modifies nouns like べからざる行為 / べからざる発言.",
    "sentences": [
      {
        "id": "skm2-p2-bekarazu::s1",
        "japanese": "壁に「ここにゴミを捨てるべからず」という警告の看板が立てられている。",
        "english": "A warning placard stating 'Do Not Dump Trash Here' has been erected on the wall.",
        "tokens": [],
        "useLabel": "Public Prohibition Sign",
        "nuanceNote": "Classic written imperative on authoritative public warning signs."
      },
      {
        "id": "skm2-p2-bekarazu::s2",
        "japanese": "危険区域につき、関係者以外立ち入るべからず。",
        "english": "Danger zone: unauthorized personnel must not enter under any circumstances.",
        "tokens": [],
        "useLabel": "Restricted Area Command",
        "nuanceNote": "Formal terse prohibition used at construction sites and facilities."
      },
      {
        "id": "skm2-p2-bekarazu::s3",
        "japanese": "国家機密を外国の諜報機関に売り渡すなど、国民として許すべからざる大罪だ。",
        "english": "Selling state secrets to foreign intelligence agencies is an impermissible capital crime for any citizen.",
        "tokens": [],
        "useLabel": "Attributive Decree (〜べからざるN)",
        "nuanceNote": "許すべからざる modifies 大罪 to emphasize an inexcusable legal/moral crime."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-p2-bekarazu-1",
        "question": "壁に「ここにゴミを捨てる（　　）」という看板が立てられている。",
        "translation": "A warning placard stating 'Do Not Dump Trash Here' has been erected on the wall.",
        "options": ["べからず", "まい", "ざるを得ない", "かねない"],
        "correctIndex": 0,
        "grammarFocus": "〜べからず (Public Prohibition Command)",
        "ruleHint": "動詞辞書形 + べからず; authoritative written prohibition on signage.",
        "explanations": [
          {"text": "べからず", "isCorrect": True, "reason": "Correct! 捨てるべからず is the canonical written prohibition on public warning signs."},
          {"text": "まい", "isCorrect": False, "reason": "Incorrect. まい expresses speaker's personal negative intention or negative conjecture."},
          {"text": "ざるを得ない", "isCorrect": False, "reason": "Incorrect. ざるを得ない expresses reluctant compulsion ('cannot help but')."},
          {"text": "かねない", "isCorrect": False, "reason": "Incorrect. かねない expresses a dangerous potential risk ('might end up')."}
        ]
      }
    ]
  },
  {
    "id": "skm2-p2-kai-ga-aru",
    "book": "Shin Kanzen Master N2",
    "chapter": "Part 2 · Chapter 1",
    "title": "〜甲斐があって / 〜甲斐もなく (Worth the Effort vs All in Vain)",
    "meaning": "The great effort, struggle, or patient waiting was rewarded with success (甲斐があって) / ended in complete heartbreak despite effort (甲斐もなく).",
    "connection": "動詞た形 / 名詞 + の + 甲斐があって (かいがあって) | 動詞た形 / 名詞 + の + 甲斐もなく (かいもなく)",
    "nuance": "Directly evaluates whether significant effort, perseverance, or sacrifice yielded a worthwhile fruition or ended in vain. 〜甲斐があって expresses triumphant relief; 〜甲斐もなく expresses deep disappointment and grief.",
    "sentences": [
      {
        "id": "skm2-p2-kai-ga-aru::s1",
        "japanese": "一年間毎日必死に猛勉強した甲斐があって、第一志望の難関大学に見事合格した。",
        "english": "Thanks to the effort of studying intensely every single day for a year, I successfully passed the entrance exam of my top-choice university.",
        "tokens": [],
        "useLabel": "Rewarded Perseverance (Fruition)",
        "nuanceNote": "Effort directly rewarded with joyous success."
      },
      {
        "id": "skm2-p2-kai-ga-aru::s2",
        "japanese": "医師団による懸命な救命活動の甲斐もなく、搬送された患者は息を引き取った。",
        "english": "Despite all the medical team's desperate life-saving efforts, all was in vain and the transported patient passed away.",
        "tokens": [],
        "useLabel": "Tragic Futility (In Vain)",
        "nuanceNote": "懸命な救命活動の甲斐もなく highlights heartbreaking failure despite supreme exertion."
      },
      {
        "id": "skm2-p2-kai-ga-aru::s3",
        "japanese": "週末返上で粘り強く開発を続けた甲斐があり、ついに新型バッテリーが完成した。",
        "english": "Giving up weekends and persistently continuing development proved worthwhile; the new battery prototype was finally perfected.",
        "tokens": [],
        "useLabel": "Technical Breakthrough Fruition",
        "nuanceNote": "Formal written style with 甲斐があり connecting into final positive achievement."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-p2-kai-ga-aru-1",
        "question": "医師団による懸命な救命活動の甲斐も（　　）、患者は息を引き取った。",
        "translation": "Despite all the medical team's desperate life-saving efforts, all was in vain and the patient passed away.",
        "options": ["なく", "あって", "あり", "なしに"],
        "correctIndex": 0,
        "grammarFocus": "〜甲斐もなく (All in Vain Despite Effort)",
        "ruleHint": "名詞 + の + 甲斐もなく; expresses heartbreaking failure despite intense struggle.",
        "explanations": [
          {"text": "なく", "isCorrect": True, "reason": "Correct! 甲斐もなく pairs with the tragic result of the patient passing away."},
          {"text": "あって", "isCorrect": False, "reason": "Incorrect. 甲斐があって requires a positive outcome rewarding the effort."},
          {"text": "あり", "isCorrect": False, "reason": "Incorrect. 甲斐があり also requires a triumphant successful result."},
          {"text": "なしに", "isCorrect": False, "reason": "Incorrect. なしに means 'without' and does not form this construction."}
        ]
      }
    ]
  },
  {
    "id": "skm2-p2-wo-oite",
    "book": "Shin Kanzen Master N2",
    "chapter": "Part 2 · Chapter 1",
    "title": "〜をおいて（ほかにない） (None Other Than / Unequivocally Unrivaled)",
    "meaning": "Other than X, there is nobody and nothing else capable of fulfilling this paramount role.",
    "connection": "名詞 + をおいて + [ほかにいない / ほかにない]",
    "nuance": "Expresses the absolute highest subjective praise of singular unrivaled capability. The main predicate must end in a negative statement of absence (ほかにいない, ほかにはない, 考えられない). Never used with positive predicates.",
    "sentences": [
      {
        "id": "skm2-p2-wo-oite::s1",
        "japanese": "次期リーダーとして困難なチームをまとめられるのは、人望の厚い鈴木さんをおいて他にいない。",
        "english": "The person capable of unifying this difficult team as the next leader is none other than the highly respected Suzuki-san; there is nobody else.",
        "tokens": [],
        "useLabel": "Unrivaled Human Capability",
        "nuanceNote": "鈴木さんをおいて他にいない emphasizes singular leadership capability."
      },
      {
        "id": "skm2-p2-wo-oite::s2",
        "japanese": "この危機的な経営状況を立て直せる人物は、創業者の山田会長をおいて他にない。",
        "english": "The person who can turn around this critical business crisis is none other than the founder, Chairman Yamada; there is no other.",
        "tokens": [],
        "useLabel": "Executive Crisis Resolution",
        "nuanceNote": "Culminates in 他にない; absolute unrivaled authority."
      },
      {
        "id": "skm2-p2-wo-oite::s3",
        "japanese": "伝統工芸の真髄を後世に正確に継承できる工芸家は、彼をおいて他に見当たらない。",
        "english": "The artisan capable of passing down the true essence of traditional craft to future generations can be found in nobody other than him.",
        "tokens": [],
        "useLabel": "Master Craftsmanship Supremacy",
        "nuanceNote": "他に見当たらない = cannot be found anywhere else."
      }
    ],
    "quiz": [
      {
        "id": "q-skm2-p2-wo-oite-1",
        "question": "次期リーダーとしてチームをまとめられるのは、人望の厚い鈴木さん（　　）おいて他にいない。",
        "translation": "The person capable of unifying the team as next leader is none other than Suzuki-san; there is nobody else.",
        "options": ["を", "に", "で", "へ"],
        "correctIndex": 0,
        "grammarFocus": "〜をおいて（ほかにない） (None Other Than)",
        "ruleHint": "名詞 + をおいて + ほかにない / ほかにいない.",
        "explanations": [
          {"text": "を", "isCorrect": True, "reason": "Correct! 〜をおいてほかにいない marks the irreplaceable candidate with particle を."},
          {"text": "に", "isCorrect": False, "reason": "Incorrect. において means 'in/at' (formal locus)."},
          {"text": "で", "isCorrect": False, "reason": "Incorrect. でおいて is ungrammatical."},
          {"text": "へ", "isCorrect": False, "reason": "Incorrect. へおいて is ungrammatical."}
        ]
      }
    ]
  }
]

with open("jlpt-exam-prep/src/data/studyPoints.json", "r", encoding="utf-8") as f:
    points = json.load(f)

existing_ids = {p['id'] for p in points}
added_count = 0
for card in NEW_SKM2_CARDS:
    if card['id'] not in existing_ids:
        points.append(card)
        added_count += 1

with open("jlpt-exam-prep/src/data/studyPoints.json", "w", encoding="utf-8") as f:
    json.dump(points, f, ensure_ascii=False, indent=2)

print(f"Added {added_count} new SKM N2 cards to studyPoints.json. Total cards now: {len(points)}")

# Update bookSources.json
with open("jlpt-exam-prep/src/data/bookSources.json", "r", encoding="utf-8") as f:
    books = json.load(f)

for b in books:
    if b['id'] == 'skm-n2':
        for s in b['sections']:
            if s['name'].startswith('Part 2 · Chapter 1'):
                for cid in ['skm2-p2-kai-ga-aru', 'skm2-p2-wo-oite']:
                    if cid not in s['grammarIds']:
                        s['grammarIds'].append(cid)
            elif s['name'].startswith('Part 2 · Chapter 2'):
                for cid in ['skm2-p2-majiki', 'skm2-p2-bekarazu']:
                    if cid not in s['grammarIds']:
                        s['grammarIds'].append(cid)

with open("jlpt-exam-prep/src/data/bookSources.json", "w", encoding="utf-8") as f:
    json.dump(books, f, ensure_ascii=False, indent=2)

print("Updated bookSources.json with new cards mapped into Part 2 Chapters 1 & 2.")
