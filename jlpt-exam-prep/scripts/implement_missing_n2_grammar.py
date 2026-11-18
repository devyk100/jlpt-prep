import json, re

# Define the 5 substantive grammar points to add
NEW_POINTS = [
    {
        "id": "skm2-c20-shidai-de-wa",
        "title": "〜次第では / 〜次第だ (Contingency: Depending on Circumstances)",
        "meaning": "Expresses that an outcome, decision, or future event is contingent upon or determined by a condition or variable: 'Depending on N / Contingent upon N'.",
        "level": "N2",
        "book": "Shin Kanzen Master N2",
        "chapter": "Chapter 20: 時間・経過・結果",
        "streamId": "stream-condition",
        "streamName": "Conditionals & Hypotheses",
        "connection": "Noun + 次第だ / 次第で / 次第では",
        "nuance": "CONTINGENCY vs IMMEDIATE SEQUENCE: Noun + 次第では means 'depending on N' (e.g., 成績次第では 'depending on grades'). Contrast with V-ます stem + 次第 which means 'as soon as' (e.g., 決まり次第 'as soon as it is decided'). The particle は in 次第では highlights one possible critical outcome among various possibilities (e.g., 'Depending on the weather, the event may even be cancelled').",
        "keyTakeaway": "MUG-UP: Noun + 次第では = Depending on! Noun determines the outcome. (V-ます + 次第 = As soon as).",
        "sentences": [
            {
                "id": "s-skm2-20-shidai-1",
                "japanese": "検査の結果次第では、すぐに精密な手術を受ける必要があります。",
                "english": "Depending on the test results, it may be necessary to undergo surgery immediately.",
                "literal": "Examination-of result depending-on, immediately precise surgery receive necessity exists.",
                "tokens": [
                    {"word": "検査の結果次第では", "meaning": "depending on test results", "reading": "けんさのけっかしだいでは", "romaji": "kensa no kekka shidai dewa", "pos": "Grammar"},
                    {"word": "すぐに", "meaning": "immediately", "reading": "すぐに", "romaji": "sugu ni", "pos": "Adverb"},
                    {"word": "手術を", "meaning": "surgery (obj)", "reading": "しゅじゅつを", "romaji": "shujutsu wo", "pos": "Noun"},
                    {"word": "受ける", "meaning": "to receive / undergo", "reading": "うける", "romaji": "ukeru", "pos": "Verb"},
                    {"word": "必要があります", "meaning": "there is a need to", "reading": "ひつようがあります", "romaji": "hitsuyou ga arimasu", "pos": "Expression"}
                ]
            },
            {
                "id": "s-skm2-20-shidai-2",
                "japanese": "今回のプロジェクトの成否は、チーム全員の協力次第です。",
                "english": "The success or failure of this project depends on the cooperation of the entire team.",
                "literal": "This-time project success-or-failure-topic, team all-members cooperation depending-is.",
                "tokens": [
                    {"word": "成否は", "meaning": "success or failure (topic)", "reading": "せいひは", "romaji": "seihi wa", "pos": "Noun"},
                    {"word": "全員の", "meaning": "all members'", "reading": "ぜんいんの", "romaji": "zen'in no", "pos": "Noun"},
                    {"word": "協力次第です", "meaning": "depends on cooperation", "reading": "きょうりょくしだいです", "romaji": "kyouryoku shidai desu", "pos": "Grammar"}
                ]
            },
            {
                "id": "s-skm2-20-shidai-3",
                "japanese": "明日の天候次第では、登山ツアーを中止せざるを得ないかもしれません。",
                "english": "Depending on tomorrow's weather, we might have no choice but to cancel the climbing tour.",
                "literal": "Tomorrow-of weather depending-on, mountain-climbing tour cancel do-cannot-avoid may.",
                "tokens": [
                    {"word": "天候次第では", "meaning": "depending on weather", "reading": "てんこうしだいでは", "romaji": "tenkou shidai dewa", "pos": "Grammar"},
                    {"word": "登山ツアーを", "meaning": "climbing tour (obj)", "reading": "とざんつあーを", "romaji": "tozan tsuaa wo", "pos": "Noun"},
                    {"word": "中止せざるを得ない", "meaning": "cannot avoid cancelling", "reading": "ちゅうしせざるをえない", "romaji": "chuushi sezaru wo enai", "pos": "Grammar"}
                ]
            }
        ]
    },
    {
        "id": "skm2-c15-kuse-ni",
        "title": "〜くせに (Critical Concession: Despite Being X, Blameworthy Y)",
        "meaning": "Expresses strong subjective reproach, frustration, or contempt: 'Despite the fact that X / Even though X, they do Y (which is blameworthy or contradictory)'.",
        "level": "N2",
        "book": "Shin Kanzen Master N2",
        "chapter": "Chapter 15: 逆接・不満・仮定条件",
        "streamId": "stream-concession",
        "streamName": "Concession & Contrast",
        "connection": "Verb/i-adj Plain form + くせに | na-adj + なくせに | Noun + のくせに",
        "nuance": "SPEAKER'S BLAME & SAME-SUBJECT RESTRICTION: Clauses A and B must share the same subject, and the subject cannot be the speaker itself (*私は知っているくせに... is ungrammatical). Always conveys negative emotional coloring: criticism, irritation, or contempt toward the subject who fails to act appropriately given their status or knowledge. Contrast with 〜のに (neutral frustration) and 〜にもかかわらず (formal objective concession).",
        "keyTakeaway": "MUG-UP: Plain + くせに (Nの / naな)! Same subject, speaker looks down/blames. Never for yourself!",
        "sentences": [
            {
                "id": "s-skm2-15-kuse-1",
                "japanese": "彼は何も知らないくせに、いつも偉そうに専門家のような意見を言う。",
                "english": "Despite knowing nothing, he always arrogantly gives opinions like an expert.",
                "literal": "He nothing know-not despite, always arrogantly expert like opinion say.",
                "tokens": [
                    {"word": "知らないくせに", "meaning": "despite not knowing", "reading": "しらないくせに", "romaji": "shiranai kuse ni", "pos": "Grammar"},
                    {"word": "いつも", "meaning": "always", "reading": "いつも", "romaji": "itsumo", "pos": "Adverb"},
                    {"word": "偉そうに", "meaning": "arrogantly", "reading": "えらそうに", "romaji": "erasou ni", "pos": "Adverb"},
                    {"word": "意見を言う", "meaning": "give an opinion", "reading": "いけんをいう", "romaji": "iken wo iu", "pos": "Expression"}
                ]
            },
            {
                "id": "s-skm2-15-kuse-2",
                "japanese": "自分では何一つ片付けないくせに、他人の部屋の散らかり方ばかり文句を言う。",
                "english": "Even though he doesn't clean up a single thing himself, he only complains about how messy other people's rooms are.",
                "literal": "Self-by nothing tidy-not despite, others'-of room messiness only complaint say.",
                "tokens": [
                    {"word": "片付けないくせに", "meaning": "despite not tidying up", "reading": "かたづけないくせに", "romaji": "katadukenai kuse ni", "pos": "Grammar"},
                    {"word": "文句を言う", "meaning": "complain", "reading": "もんくをいう", "romaji": "monku wo iu", "pos": "Expression"}
                ]
            },
            {
                "id": "s-skm2-15-kuse-3",
                "japanese": "子どものくせに、大人の深刻な相談に口を挟むのはやめなさい。",
                "english": "Stop interrupting adults' serious consultations when you are just a child!",
                "literal": "Child despite, adults'-of serious consultation-in mouth insert stop.",
                "tokens": [
                    {"word": "子どものくせに", "meaning": "despite being a child", "reading": "こどものくせに", "romaji": "kodomo no kuse ni", "pos": "Grammar"},
                    {"word": "口を挟むのは", "meaning": "interrupting (topic)", "reading": "くちをはさむのは", "romaji": "kuchi wo hasamu no wa", "pos": "Expression"},
                    {"word": "やめなさい", "meaning": "stop (imperative)", "reading": "やめなさい", "romaji": "yamenasai", "pos": "Verb"}
                ]
            }
        ]
    },
    {
        "id": "skm2-c17-koto-kara",
        "title": "〜ことから (Origin & Grounds: Arising from the Fact That)",
        "meaning": "Expresses the empirical basis, origin, or catalyst for a name, realization, judgment, or established fact: 'From the fact that X / Because of the clue X'.",
        "level": "N2",
        "book": "Shin Kanzen Master N2",
        "chapter": "Chapter 17: 根拠・由来・部分否定",
        "streamId": "stream-cause",
        "streamName": "Causality & Reasons",
        "connection": "Verb/i-adj Plain form + ことから | na-adj + な/である + ことから | Noun + である + ことから",
        "nuance": "BASIS FOR NAMING OR JUDGMENT: Unlike everyday から (personal reason), ことから explains objective etymology, diagnostic clues, or catalysts. Clause B characteristically contains verbs of naming (〜と名付けられた), discovery/realization (〜ことが判明した), or public reputation (〜と呼ばれている). Cannot take direct commands or volitional requests in Clause B.",
        "keyTakeaway": "MUG-UP: Plain + ことから = From the fact that! Explains origins, reasons for names, and forensic clues.",
        "sentences": [
            {
                "id": "s-skm2-17-koto-1",
                "japanese": "富士山に形が似ていることから、この山は「近江富士」と呼ばれている。",
                "english": "Because its shape resembles Mt. Fuji, this mountain is called 'Omi Fuji'.",
                "literal": "Mt.-Fuji-to shape resemble from-fact-that, this mountain Omi-Fuji called-is.",
                "tokens": [
                    {"word": "似ていることから", "meaning": "from the fact that it resembles", "reading": "にていることから", "romaji": "nite iru koto kara", "pos": "Grammar"},
                    {"word": "呼ばれている", "meaning": "is called", "reading": "よばれている", "romaji": "yobarete iru", "pos": "Verb"}
                ]
            },
            {
                "id": "s-skm2-17-koto-2",
                "japanese": "現場に犯人の指紋が残っていたことから、警察はすぐに身元を特定することができた。",
                "english": "From the fact that the culprit's fingerprints remained at the scene, the police were able to identify them quickly.",
                "literal": "Scene-at culprit-of fingerprints remained from-fact-that, police immediately identity specify could.",
                "tokens": [
                    {"word": "残っていたことから", "meaning": "from the fact that it remained", "reading": "のこっていたことから", "romaji": "nokotte ita koto kara", "pos": "Grammar"},
                    {"word": "身元を特定する", "meaning": "identify identity", "reading": "みもとをとくていする", "romaji": "mimoto wo tokutei suru", "pos": "Expression"}
                ]
            },
            {
                "id": "s-skm2-17-koto-3",
                "japanese": "道が激しくぬれていることから、昨夜この地域に激しい雨が降ったことが分かる。",
                "english": "From the fact that the roads are heavily wet, we can tell that heavy rain fell in this area last night.",
                "literal": "Roads heavily wet-being from-fact-that, last-night this region-in heavy rain fell fact understand.",
                "tokens": [
                    {"word": "ぬれていることから", "meaning": "from the fact that it is wet", "reading": "ぬれていることから", "romaji": "nurete iru koto kara", "pos": "Grammar"},
                    {"word": "分かる", "meaning": "can be understood", "reading": "わかる", "romaji": "wakaru", "pos": "Verb"}
                ]
            }
        ]
    },
    {
        "id": "skm2-c17-wake-de-wa-nai",
        "title": "〜わけではない / 〜というわけではない (Partial Negation: Not Necessarily So)",
        "meaning": "Softens or partially negates an assumption, expectation, or overgeneralization: 'It doesn't mean that X / It's not that X (there are exceptions or nuanced reasons)'.",
        "level": "N2",
        "book": "Shin Kanzen Master N2",
        "chapter": "Chapter 17: 根拠・由来・部分否定",
        "streamId": "stream-negation",
        "streamName": "Negation & Refutation",
        "connection": "Verb/i-adj Plain form + わけではない | na-adj + な/である + わけではない | Noun + な/である + わけではない",
        "nuance": "PARTIAL NEGATION vs TOTAL NEGATION: Contrasts sharply with わけがない (absolute impossibility: 'there is no way'). わけではない admits that something might appear true on the surface, but refutes the absolute conclusion (e.g., 'I don't dislike it, but I don't want to eat it now'). Frequently paired with 全く (not entirely), いつも (not always), or 必ずしも (not necessarily).",
        "keyTakeaway": "MUG-UP: Plain + わけではない = It doesn't mean that! Partial negation, softens blanket assumptions.",
        "sentences": [
            {
                "id": "s-skm2-17-wake-1",
                "japanese": "甘いものが嫌いなわけではないが、今はダイエット中なので控えている。",
                "english": "It's not that I dislike sweets, but I'm currently on a diet, so I'm refraining.",
                "literal": "Sweet-things dislike mean-not but, now diet-midst-being-because refraining-am.",
                "tokens": [
                    {"word": "嫌いなわけではないが", "meaning": "it's not that I dislike, but", "reading": "きらいなわけではないが", "romaji": "kirai na wake dewa nai ga", "pos": "Grammar"},
                    {"word": "控えている", "meaning": "am refraining", "reading": "ひかえている", "romaji": "hikaete iru", "pos": "Verb"}
                ]
            },
            {
                "id": "s-skm2-17-wake-2",
                "japanese": "高級な道具を使えば必ず素晴らしい作品が作れるというわけではない。",
                "english": "Using expensive tools does not necessarily mean that one can create a wonderful work of art.",
                "literal": "High-class tools use-if without-fail wonderful work create-can mean-not.",
                "tokens": [
                    {"word": "作れるというわけではない", "meaning": "does not mean one can create", "reading": "つくれるというわけではない", "romaji": "tsukureru to iu wake dewa nai", "pos": "Grammar"}
                ]
            },
            {
                "id": "s-skm2-17-wake-3",
                "japanese": "彼と親しく話さないのは、怒っているわけではなく単に人見知りだからだ。",
                "english": "The reason I don't speak intimately with him isn't that I'm angry, but simply that I am shy around people.",
                "literal": "Him-with intimately speak-not-fact-topic, angry mean-not simply shy-because.",
                "tokens": [
                    {"word": "怒っているわけではなく", "meaning": "it's not that I am angry, but", "reading": "おこっているわけではなく", "romaji": "okotte iru wake dewa naku", "pos": "Grammar"},
                    {"word": "人見知りだからだ", "meaning": "because of being shy", "reading": "ひとみしりだからだ", "romaji": "hitomishiri dakara da", "pos": "Expression"}
                ]
            }
        ]
    },
    {
        "id": "skm2-c14-hanmen",
        "title": "〜反面 (On the Flip Side: Coexisting Duality in the Same Entity)",
        "meaning": "Presents two coexisting, contradictory aspects or characteristics of the same subject or entity: 'On one hand X, but on the other hand / on the flip side Y'.",
        "level": "N2",
        "book": "Shin Kanzen Master N2",
        "chapter": "Chapter 14: 対比・両面性・相違",
        "streamId": "stream-concession",
        "streamName": "Concession & Contrast",
        "connection": "Verb/i-adj Plain form + 反面 | na-adj + な/である + 反面 | Noun + である + 反面",
        "nuance": "COEXISTING TRAITS IN SAME ENTITY: Contrasts with 〜一方で. While 〜一方で can contrast two distinct external entities (e.g., 'Company A grew while Company B fell'), 〜反面 requires that both opposing qualities belong to the *same* entity, phenomenon, or person (e.g., 'This medicine is very effective, but on the flip side has strong side effects').",
        "keyTakeaway": "MUG-UP: Plain + 反面 = On the flip side! Opposing traits of the EXACT SAME entity coexisting.",
        "sentences": [
            {
                "id": "s-skm2-14-hanmen-1",
                "japanese": "インターネットは大変便利な反面、誤った情報が瞬時に拡散する危険性も潜んでいる。",
                "english": "While the internet is extremely convenient, on the flip side, the danger of false information spreading instantly also lurks.",
                "literal": "Internet-topic very convenient flip-side, erroneous information instantly spread danger also lurks.",
                "tokens": [
                    {"word": "便利な反面", "meaning": "convenient, but on the flip side", "reading": "べんりなはんめん", "romaji": "benri na hanmen", "pos": "Grammar"},
                    {"word": "危険性も", "meaning": "danger also", "reading": "きけんせいも", "romaji": "kikensei mo", "pos": "Noun"},
                    {"word": "潜んでいる", "meaning": "lurks", "reading": "ひそんでいる", "romaji": "hisonde iru", "pos": "Verb"}
                ]
            },
            {
                "id": "s-skm2-14-hanmen-2",
                "japanese": "この新薬は高い治療効果が期待できる反面、強い副作用が出るリスクも無視できない。",
                "english": "While this new drug promises high therapeutic efficacy, on the flip side, the risk of severe side effects cannot be ignored.",
                "literal": "This new-drug high therapeutic-effect expect-can flip-side, strong side-effect appear risk cannot-ignore.",
                "tokens": [
                    {"word": "期待できる反面", "meaning": "can be expected, but on the flip side", "reading": "きたいできるはんめん", "romaji": "kitai dekiru hanmen", "pos": "Grammar"},
                    {"word": "副作用が", "meaning": "side effects (subj)", "reading": "ふくさようが", "romaji": "fukusayou ga", "pos": "Noun"}
                ]
            },
            {
                "id": "s-skm2-14-hanmen-3",
                "japanese": "都会での生活は刺激が多くて楽しい反面、家賃や物価が高くて生活費の負担が大きい。",
                "english": "While living in the city is exciting and fun, on the flip side, rent and prices are high, making living expenses burdensome.",
                "literal": "City-in life stimulation much fun flip-side, rent prices high living-costs burden big.",
                "tokens": [
                    {"word": "楽しい反面", "meaning": "fun, but on the flip side", "reading": "たのしいはんめん", "romaji": "tanoshii hanmen", "pos": "Grammar"},
                    {"word": "負担が大きい", "meaning": "burden is heavy", "reading": "ふたんがおおきい", "romaji": "futan ga ookii", "pos": "Expression"}
                ]
            }
        ]
    }
]

# 1. Update studyPoints.json
with open("jlpt-exam-prep/src/data/studyPoints.json", encoding="utf-8") as f:
    sp = json.load(f)

existing_ids = {p["id"] for p in sp}
added_to_sp = 0
for np in NEW_POINTS:
    if np["id"] not in existing_ids:
        sp.append(np)
        added_to_sp += 1
    else:
        # Update existing
        for i, p in enumerate(sp):
            if p["id"] == np["id"]:
                sp[i] = np

with open("jlpt-exam-prep/src/data/studyPoints.json", "w", encoding="utf-8") as f:
    json.dump(sp, f, ensure_ascii=False, indent=2)

print(f"Added/updated {len(NEW_POINTS)} substantive points in studyPoints.json (newly inserted: {added_to_sp})")

# 2. Update bookSkmN2.ts
with open("jlpt-exam-prep/src/data/bookSkmN2.ts", encoding="utf-8") as f:
    ts_content = f.read()

# Check which IDs are not yet in bookSkmN2.ts
for np in NEW_POINTS:
    if f'"{np["id"]}"' not in ts_content:
        # Insert before the closing bracket of export const BOOK_SKM_N2_POINTS
        insert_text = "  " + json.dumps(np, ensure_ascii=False, indent=2).replace("\n", "\n  ") + ",\n"
        last_bracket_idx = ts_content.rfind("];")
        if last_bracket_idx != -1:
            ts_content = ts_content[:last_bracket_idx] + insert_text + ts_content[last_bracket_idx:]
            print(f"Inserted {np['id']} into bookSkmN2.ts")

with open("jlpt-exam-prep/src/data/bookSkmN2.ts", "w", encoding="utf-8") as f:
    f.write(ts_content)

# 3. Update bookSources.json sections so that each card is placed in its proper section
with open("jlpt-exam-prep/src/data/bookSources.json", encoding="utf-8") as f:
    bs = json.load(f)

for book in bs:
    if book.get("id") == "skm-n2":
        for sec in book.get("sections", []):
            name = sec.get("name", "")
            gids = sec.get("grammarIds", [])
            if "Chapter 14" in name and "skm2-c14-hanmen" not in gids:
                gids.append("skm2-c14-hanmen")
            elif "Chapter 15" in name and "skm2-c15-kuse-ni" not in gids:
                gids.append("skm2-c15-kuse-ni")
            elif "Chapter 17" in name:
                if "skm2-c17-koto-kara" not in gids:
                    gids.append("skm2-c17-koto-kara")
                if "skm2-c17-wake-de-wa-nai" not in gids:
                    gids.append("skm2-c17-wake-de-wa-nai")
            elif "Chapter 20" in name and "skm2-c20-shidai-de-wa" not in gids:
                gids.append("skm2-c20-shidai-de-wa")

with open("jlpt-exam-prep/src/data/bookSources.json", "w", encoding="utf-8") as f:
    json.dump(bs, f, ensure_ascii=False, indent=2)

print("Updated bookSources.json with new card links!")
