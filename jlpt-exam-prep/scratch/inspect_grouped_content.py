import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sps = json.load(f)

sp_dict = {p['id']: p for p in sps}

groups_to_check = [
    {
        "name": "Genki I: 〜んです (Explanation / Contextual Justification)",
        "ids": ["added-g1-12-18", "g1-l12-node-objective-reason"],
        "table": None
    },
    {
        "name": "Genki I & II: Advice/Suggestion (〜ほうがいい vs 〜たらどうですか)",
        "ids": ["added-g1-12-19", "g2-l14-tara-dou-desu-ka"],
        "table": None
    },
    {
        "name": "Genki II: Appearance vs Hearsay (〜そうです)",
        "ids": ["added-g2-13-20", "g2-l17-hearsay-sou-desu"],
        "table": None
    },
    {
        "name": "Genki II: Giving & Receiving (あげる・くれる・もらう & てあげる・てくれる・てもらう)",
        "ids": ["added-g2-14-22", "added-g2-16-25"],
        "table": "givingReceivingMatrix"
    },
    {
        "name": "Genki II: Conditionals (と, ば, たら, なら)",
        "ids": ["g2-l13-nara-conditional", "g2-l17-tara-conditional", "g2-l22-ba-conditional"],
        "table": "conditionalsMatrix"
    },
    {
        "name": "Genki II: Keigo (尊敬語 vs 謙譲語・丁重語)",
        "ids": ["g2-l19-sonkeigo-verbs", "added-g2-20-34"],
        "table": "keigoMatrix"
    },
    {
        "name": "Genki II: Voice (受身 vs 使役 vs 使役受身)",
        "ids": ["added-g2-21-38", "added-g2-22-40", "added-g2-23-43"],
        "table": "voiceMatrix"
    },
    {
        "name": "Genki II: Personal Decision vs Institutional Emergence (〜ことにする vs 〜ことになる)",
        "ids": ["g2-l23-koto-ni-suru-naru"],
        "table": None
    },
    {
        "name": "SKM N3: Temporal Progression (〜うちに vs 〜間・〜間に)",
        "ids": ["skm3-u1-uchini-while", "skm3-u1-uchini-change", "skm3-u1-aida-vs-aidani"],
        "table": "timeSequenceSpectrum"
    },
    {
        "name": "SKM N3: Contrast & Opposing Aspects (〜反面 vs 〜に対して)",
        "ids": ["skm3-u4-hanmen-flipside", "skm3-u4-ni-taishite"],
        "table": None
    },
    {
        "name": "SKM N3: Wake Quadruplets (〜わけだ vs 〜わけがない vs 〜わけではない vs 〜わけにはいかない)",
        "ids": ["skm3-u8-wake-ga-nai", "skm3-u8-wake-dewa-nai", "skm3-u8-wake-niwa-ikanai"],
        "table": "skmN3WakeQuadrupletsMatrix"
    },
    {
        "name": "SKM N2: Contingency vs Immediacy (〜次第では vs 〜次第)",
        "ids": ["skm2-c20-shidai-de-wa"],
        "table": None
    },
    {
        "name": "SKM N2: Critical Concession (〜くせに vs 〜のに)",
        "ids": ["skm2-c15-kuse-ni"],
        "table": None
    },
    {
        "name": "SKM N2: Coexisting Duality (〜反面)",
        "ids": ["skm2-c14-hanmen"],
        "table": None
    },
    {
        "name": "SKM N2: Origin & Grounds (〜ことから vs 〜ところから)",
        "ids": ["skm2-c17-koto-kara", "added-n2-e-121"],
        "table": None
    },
    {
        "name": "SKM N2: Inability Nuances (〜かねる vs 〜恐れがある vs 〜かねない)",
        "ids": ["skm2-c22-kaneru", "skm2-c22-osore-ga-aru", "skm2-c22-kane-nai"],
        "table": None
    },
    {
        "name": "SKM N2: Prolonged Outcomes (〜末に vs 〜あげく)",
        "ids": ["skm2-c20-sue-ni-deliberation", "skm2-c20-ageku-ni"],
        "table": None
    },
    {
        "name": "SKM N2: Normative & Advisory Endings (〜ものだ vs 〜というものだ vs 〜べきだ vs 〜ことだ)",
        "ids": ["skm2-c23-mono-da-essence", "added-n2-23-108", "added-n2-23-109", "skm2-c24-koto-da"],
        "table": "skmN2SentenceFinalConstraintsMatrix"
    },
    {
        "name": "SKM N2: Partial Negation vs Impossibility (〜わけではない vs 〜わけがない)",
        "ids": ["skm2-c17-wake-de-wa-nai"],
        "table": None
    }
]

print("=== CHECKING GROUPED CONSTRUCTIONS CONTENT & INTEGRITY ===")
for grp in groups_to_check:
    print(f"\n### GROUP: {grp['name']}")
    for cid in grp['ids']:
        card = sp_dict.get(cid)
        if not card:
            print(f"  [ERROR] Missing card: {cid}")
            continue
        print(f"  - Card: [{cid}] {card['title']}")
        print(f"    * Meaning: {card.get('meaning', '')[:100]}")
        print(f"    * Nuance: {card.get('nuance', '')[:120]}...")
        print(f"    * Key Takeaway: {card.get('keyTakeaway', '')[:120]}...")
        sentences = card.get('sentences', [])
        print(f"    * Examples: {len(sentences)} sentence(s)")
        for s in sentences[:2]:
            print(f"      ja: {s.get('ja')} | en: {s.get('en')}")
    if grp['table']:
        print(f"  * Associated Master Table: {grp['table']}")
