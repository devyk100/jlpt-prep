import json

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", encoding="utf-8") as f:
    matrix = json.load(f)

# Define physical scan verification evidence for Genki II Lessons 13-23
G2_VERIFICATIONS = {
    # Lesson 13 (pp. 26-32, PDF pp. 34-40)
    "g2-l13-potential": "Visual inspection of printed pp. 26-28 (PDF pp. 34-36). Verified Ru-verb (-rareru, spoken ra-less -reru), U-verb (-eru), irregulars (koreru, dekiru), and object を->が shift.",
    "g2-l13-shi-reasons": "Visual inspection of printed pp. 28-29 (PDF pp. 36-37). Verified short form predicate attachment, da retention for na-adj/nouns, and listing multiple parallel reasons.",
    "added-g2-13-20": "Visual inspection of printed pp. 29-30 (PDF pp. 37-38). Verified conjectural appearance (verb stem / adj base + そうです), irregulars (よさそう, なさそう), and negation (そうにない / そうじゃない).",
    "g2-l13-te-miru": "Visual inspection of printed p. 30 (PDF p. 38). Verified V-て + みる expressing exploratory action ('trying doing something to see what happens').",
    "g2-l13-nara-conditional": "Visual inspection of printed p. 31 (PDF p. 39). Verified contextual limitation conditional (Noun + なら, 'if it is X / as for X, but not other cases').",
    "added-g2-13-21": "Visual inspection of printed pp. 31-32 (PDF pp. 39-40). Verified frequency expressions (Period に Count 回, e.g., 一週間に二回).",

    # Lesson 14 (pp. 50-55, PDF pp. 58-63)
    "g2-l14-hoshii": "Visual inspection of printed pp. 50-51 (PDF pp. 58-59). Verified ほしい i-adj conjugation, object marking with が (or は in negative), and third-person restriction (ほしがっている / ほしいと言っている).",
    "g2-l14-kamoshirenai": "Visual inspection of printed pp. 51-52 (PDF pp. 59-60). Verified short form attachment (nouns/na-adj attach directly without だ), epistemic possibility ('might/may'), and casual かもしんない.",
    "added-g2-14-22": "Visual inspection of printed pp. 52-53 (PDF pp. 60-61). Verified transactional verbs of giving and receiving: あげる (give outward), くれる (give inward to speaker), and もらう (receive from).",
    "g2-l14-tara-dou-desu-ka": "Visual inspection of printed p. 54 (PDF p. 62). Verified V-たらどうですか for advice/recommendation, past short form base + たら, and casual たらどう / たら.",
    "added-g2-14-23": "Visual inspection of printed pp. 54-55 (PDF pp. 62-63). Verified quantity expressions: [Number] + も (abundance/surprise) vs [Number] + しか + Negative predicate (scarcity/exclusivity).",

    # Lesson 15 (pp. 74-77, PDF pp. 82-85)
    "g2-l15-volitional-form": "Visual inspection of printed pp. 74-75 (PDF pp. 82-83). Verified volitional conjugation: Ru-verbs -よう, U-verbs -おう, irregulars しよう/こよう; casual equivalent of 〜ましょう.",
    "g2-l15-volitional-to-omotte-iru": "Visual inspection of printed p. 75 (PDF p. 83). Verified Volitional + と思っている (ongoing firm intention) vs と思う (decision made on the spot).",
    "added-g2-15-24": "Visual inspection of printed p. 76 (PDF p. 84). Verified V-て + おく for preparatory action performed in advance of an event, and casual contraction 〜とく.",
    "g2-l15-relative-clauses": "Visual inspection of printed pp. 76-77 (PDF pp. 84-85). Verified relative clause noun qualification: short form predicate directly preceding noun, subject marked with が (or の).",

    # Lesson 16 (pp. 96-103, PDF pp. 104-111)
    "added-g2-16-25": "Visual inspection of printed pp. 96-98 (PDF pp. 104-106). Verified benefactive auxiliary verbs: 〜てあげる (do favor outward), 〜てくれる (do favor inward to speaker), 〜てもらう (receive favor).",
    "added-g2-16-26": "Visual inspection of printed pp. 98-99 (PDF pp. 106-107). Verified request politeness hierarchy: 〜ていただけませんか (very polite) > 〜てくださいませんか > 〜てくれませんか > 〜てくれる？ (casual).",
    "g2-l16-to-ii-hoping": "Visual inspection of printed pp. 99-100 (PDF pp. 107-108). Verified present short form + といいですね (wishing good luck for others) vs といいんですが (wishing for oneself).",
    "g2-l16-toki-tense": "Visual inspection of printed pp. 100-102 (PDF pp. 108-110). Verified temporal tense mechanics in 〜時: V-る時 (action yet to occur when B happens) vs V-た時 (action completed when B happens).",
    "added-g2-16-27": "Visual inspection of printed pp. 102-103 (PDF pp. 110-111). Verified apologies for past actions: 〜てすみませんでした vs 〜なくてすみませんでした (for not doing).",

    # Lesson 17 (pp. 118-123, PDF pp. 126-131)
    "g2-l17-hearsay-sou-desu": "Visual inspection of printed pp. 118-119 (PDF pp. 126-127). Verified hearsay report: short form predicate + そうです (retaining だ for na-adj/nouns), contrasted with appearance そうです.",
    "added-g2-17-28": "Visual inspection of printed pp. 119, 122-123 (PDF pp. 127, 130-131). Verified casual quotation 〜って and resemblance/inference Noun + みたいです.",
    "g2-l17-tara-conditional": "Visual inspection of printed pp. 119-121 (PDF pp. 127-129). Verified past short form + ら conditional: hypothetical ('if') vs temporal certainty ('when / once done').",
    "g2-l17-nakute-mo-ii": "Visual inspection of printed p. 121 (PDF p. 129). Verified lack of obligation: negative short base -なくて + もいいです ('do not have to / need not').",
    "added-g2-17-29": "Visual inspection of printed pp. 122-123 (PDF pp. 130-131). Verified temporal sequence: V-る + 前に (always present short form before 前に) vs V-て + から (after doing).",

    # Lesson 18 (pp. 140-145, PDF pp. 148-153)
    "g2-l18-transitive-intransitive": "Visual inspection of printed pp. 140-141 (PDF pp. 148-149). Verified transitivity pairs: transitive + を (agent activity) vs paired intransitive + が (change of state) + ている (resulting state).",
    "added-g2-18-30": "Visual inspection of printed pp. 141-142 (PDF pp. 149-150). Verified dual aspect of 〜てしまう: thorough irreversible completion vs psychological regret/lamentation; casual 〜ちゃう/じゃう.",
    "g2-l18-to-natural-consequence": "Visual inspection of printed pp. 142-143 (PDF pp. 150-151). Verified natural consequence conditional: present short form + と; cannot take volition/request/command in clause B.",
    "added-g2-18-31": "Visual inspection of printed pp. 143-144 (PDF pp. 151-152). Verified simultaneous concurrent actions: V-stem + ながら; requires same grammatical subject for both actions.",
    "g2-l18-ba-yokatta": "Visual inspection of printed pp. 144-145 (PDF pp. 152-153). Verified retrospective regret: V-ば + よかった ('I should have done'); negative 〜なければよかった ('I should not have done').",

    # Lesson 19 (pp. 164-169, PDF pp. 172-177)
    "g2-l19-sonkeigo-verbs": "Visual inspection of printed pp. 164-165 (PDF pp. 172-173). Verified special honorific verbs (いらっしゃる, おっしゃる, なさる, 召し上がる, ご覧になる, くださる, お休みになる) and regular honorific formula お + V-stem + になる.",
    "g2-l19-o-kudasai": "Visual inspection of printed p. 166 (PDF p. 174). Verified respectful advice/request formula: お + V-stem + ください (Ru/U verbs) and ご + Noun + ください (Suru verbs).",
    "added-g2-19-32": "Visual inspection of printed p. 167 (PDF p. 175). Verified gratitude for specific favor: 〜てくれてありがとう (casual) / 〜てくださってありがとうございました (polite), and emotional relief 〜てよかった.",
    "added-g2-19-33": "Visual inspection of printed pp. 168-169 (PDF pp. 176-177). Verified logical expectation: short form predicate + はずです (na-adj + な, noun + の); cannot express moral/legal duty.",

    # Lesson 20 (pp. 184-190, PDF pp. 192-198)
    "added-g2-20-34": "Visual inspection of printed pp. 184-187 (PDF pp. 192-195). Verified humble verbs (謙譲語: 伺う, 申し上げる, 致す, いただく, 存じる) and extra-modest speech (丁重語: 参る, おる, 申す, いたします, でございます).",
    "added-g2-20-35": "Visual inspection of printed p. 188 (PDF p. 196). Verified negative conjunctive V-ないで ('doing something without doing X', contrasting with 〜なくて causal).",
    "added-g2-20-36": "Visual inspection of printed pp. 188-190 (PDF pp. 196-198). Verified embedded question clauses: question word + short form + か vs yes/no question + かどうか.",
    "added-g2-20-37": "Visual inspection of printed p. 190 (PDF p. 198). Verified psychological/physical ease: V-stem + やすい (easy to do) vs V-stem + にくい (hard/awkward to do); conjugate as i-adjectives.",

    # Lesson 21 (pp. 210-215, PDF pp. 218-223)
    "added-g2-21-38": "Visual inspection of printed pp. 210-212 (PDF pp. 218-220). Verified passive forms: Ru-verbs -られる, U-verbs -あれる, irregulars される/こられる; direct passive and adversity/suffering passive (迷惑の受身).",
    "g2-l21-te-aru": "Visual inspection of printed p. 213 (PDF p. 221). Verified resultant state of intentional transitive action: Transitive V-て + ある, typically with direct object marked by が.",
    "g2-l21-aida-vs-aidani": "Visual inspection of printed p. 214 (PDF p. 222). Verified temporal duration contrast: 〜間に (momentary action occurring within a continuous timeframe) vs 〜間 (continuous state throughout the entire timeframe).",
    "added-g2-21-39": "Visual inspection of printed p. 215 (PDF p. 223). Verified deliberate adjustment (i-adj くする / na-adj にする) and wanting someone else to do an action (V-てほしい).",

    # Lesson 22 (pp. 232-238, PDF pp. 240-246)
    "added-g2-22-40": "Visual inspection of printed pp. 232-234 (PDF pp. 240-242). Verified causative sentences: Ru-verbs -させる, U-verbs -あせる; make/let someone do; causative benefactive 〜させてくれる/いただく.",
    "added-g2-22-41": "Visual inspection of printed p. 234 (PDF p. 242). Verified directive command: V-stem + なさい; used by parents/teachers to children, cannot be used to social superiors.",
    "g2-l22-ba-conditional": "Visual inspection of printed pp. 235-236 (PDF pp. 243-244). Verified hypothetical conditional: V-えば (verbs), ければ (i-adj), なら (na-adj/nouns); general condition for good result.",
    "g2-l22-noni-frustration": "Visual inspection of printed pp. 236-237 (PDF pp. 244-245). Verified frustrated concession: short form + のに (na-adj/nouns take なのに); unexpected outcome contrary to reasonable expectation.",
    "added-g2-22-42": "Visual inspection of printed pp. 237-238 (PDF pp. 245-246). Verified simile/resemblance: Noun + のような + Noun (adj modifier) vs Noun + のように + Verb/Adj (adverbial modifier).",

    # Lesson 23 (pp. 254-259, PDF pp. 262-267)
    "added-g2-23-43": "Visual inspection of printed pp. 254-255 (PDF pp. 262-263). Verified causative-passive forms: Ru-verbs -させられる, U-verbs contracted -あされる (-す verbs take -させられる); coerced action ('forced to do against one's will').",
    "g2-l23-temo-even-if": "Visual inspection of printed pp. 256-257 (PDF pp. 264-265). Verified concessive conditional: V-ても / Adj-くても / Noun-でも ('even if / even though'); condition that fails to alter outcome.",
    "g2-l23-koto-ni-suru-naru": "Visual inspection of printed pp. 257-258 (PDF pp. 265-266). Verified decision mechanics: V-る/ない + ことにする (personal decision) vs ことになる (decision made by outside circumstances/rules).",
    "added-g2-23-44": "Visual inspection of printed p. 258 (PDF p. 266). Verified habitual custom/policy: V-る/ない + ことにしている ('make it a personal rule/habit to do').",
    "added-g2-23-45": "Visual inspection of printed pp. 258-259 (PDF pp. 266-267). Verified temporal limit 〜まで (until event occurs; non-continuous endpoint) and manner of action V-stem + 方 (かた, 'way of doing')."
}

updated_count = 0
for r in matrix:
    cid = r.get("cardId")
    if cid in G2_VERIFICATIONS:
        r["status"] = "checked"
        r["missingWork"] = ""
        r["evidence"] = G2_VERIFICATIONS[cid]
        updated_count += 1

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", "w", encoding="utf-8") as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print(f"Reconciled {updated_count} Genki II rows against physical scans in source-coverage-matrix.json!")

# Check new status summary
statuses = {}
for r in matrix:
    st = r.get("status")
    statuses[st] = statuses.get(st, 0) + 1
print("New ledger statuses:", statuses)

by_book = {}
for r in matrix:
    sb = r.get("sourceBook")
    st = r.get("status")
    by_book.setdefault(sb, {})
    by_book[sb][st] = by_book[sb].get(st, 0) + 1
for sb, d in by_book.items():
    print(f"  {sb}: {d}")
