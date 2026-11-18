import json

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", encoding="utf-8") as f:
    matrix = json.load(f)

# Update the 5 newly implemented points in the matrix
NEW_MATRIX_DETAILS = {
    "skm2-c20-shidai-de-wa": {
        "grammarItem": "〜次第では / 〜次第だ (Contingency: Depending on Circumstances)",
        "instructionalDetails": "Noun + 次第だ / 次第で / 次第では. Expresses that an outcome, decision, or future event is contingent upon a condition or variable ('depending on N'). Contrasted with V-stem + 次第 ('as soon as').",
        "exampleCount": 3,
        "exampleIds": [
            "skm2-c20-shidai-de-wa::s-skm2-20-shidai-1",
            "skm2-c20-shidai-de-wa::s-skm2-20-shidai-2",
            "skm2-c20-shidai-de-wa::s-skm2-20-shidai-3"
        ],
        "evidence": "Substantive instruction and dedicated practice implemented. Physical scan identified: Shin Kanzen Master N2 Chapter 20 (p. 90 / PDF p. 100). Implemented as standalone card [skm2-c20-shidai-de-wa] in studyPoints.json and bookSkmN2.ts with 3 authentic example sentences and practice exercise skm2-c20-ex-shidai.",
        "missingWork": "Exercise provenance review remains separate: chapter exercises in chapterExercises.json remain unverified pending 1:1 drill matching against textbook problem sets (問題 p. 94)."
    },
    "skm2-c15-kuse-ni": {
        "grammarItem": "〜くせに (Critical Concession: Despite Being X, Blameworthy Y)",
        "instructionalDetails": "Verb/i-adj Plain form + くせに | na-adj + なくせに | Noun + のくせに. Expresses strong subjective reproach, frustration, or contempt ('despite the fact that X, they blameworthily do Y'). Same-subject restriction applies; cannot be used for the speaker themselves.",
        "exampleCount": 3,
        "exampleIds": [
            "skm2-c15-kuse-ni::s-skm2-15-kuse-1",
            "skm2-c15-kuse-ni::s-skm2-15-kuse-2",
            "skm2-c15-kuse-ni::s-skm2-15-kuse-3"
        ],
        "evidence": "Substantive instruction and dedicated practice implemented. Physical scan identified: Shin Kanzen Master N2 Chapter 15 (pp. 68-73 / PDF pp. 78-83). Implemented as standalone card [skm2-c15-kuse-ni] in studyPoints.json and bookSkmN2.ts with 3 authentic example sentences and practice exercise skm2-c15-ex-kuse.",
        "missingWork": "Exercise provenance review remains separate: chapter exercises in chapterExercises.json remain unverified pending 1:1 drill matching against textbook problem sets (問題 p. 72)."
    },
    "skm2-c17-koto-kara": {
        "grammarItem": "〜ことから (Origin & Grounds: Arising from the Fact That)",
        "instructionalDetails": "Plain form (na-adj な/である, Noun である) + ことから. Expresses empirical basis, origin, or catalyst for a name, realization, judgment, or established fact. Commonly pairs with 〜と名付けられた, 〜と呼ばれている, 〜ことが分かる.",
        "exampleCount": 3,
        "exampleIds": [
            "skm2-c17-koto-kara::s-skm2-17-koto-1",
            "skm2-c17-koto-kara::s-skm2-17-koto-2",
            "skm2-c17-koto-kara::s-skm2-17-koto-3"
        ],
        "evidence": "Substantive instruction and dedicated practice implemented. Physical scan identified: Shin Kanzen Master N2 Chapter 17 (pp. 78-81 / PDF pp. 88-91). Implemented as standalone card [skm2-c17-koto-kara] in studyPoints.json and bookSkmN2.ts with 3 authentic example sentences and practice exercise skm2-c17-ex-koto.",
        "missingWork": "Exercise provenance review remains separate: chapter exercises in chapterExercises.json remain unverified pending 1:1 drill matching against textbook problem sets (問題 p. 81)."
    },
    "skm2-c17-wake-de-wa-nai": {
        "grammarItem": "〜わけではない / 〜というわけではない (Partial Negation: Not Necessarily So)",
        "instructionalDetails": "Plain form (na-adj な/である, Noun な/である) + わけではない / というわけではない. Softens or partially negates an assumption, expectation, or overgeneralization ('it does not necessarily mean that X'). Contrasted with わけがない (absolute impossibility).",
        "exampleCount": 3,
        "exampleIds": [
            "skm2-c17-wake-de-wa-nai::s-skm2-17-wake-1",
            "skm2-c17-wake-de-wa-nai::s-skm2-17-wake-2",
            "skm2-c17-wake-de-wa-nai::s-skm2-17-wake-3"
        ],
        "evidence": "Substantive instruction and dedicated practice implemented. Physical scan identified: Shin Kanzen Master N2 Chapter 17 (pp. 78-81 / PDF pp. 88-91). Implemented as standalone card [skm2-c17-wake-de-wa-nai] in studyPoints.json and bookSkmN2.ts with 3 authentic example sentences and practice exercise skm2-c17-ex-wake.",
        "missingWork": "Exercise provenance review remains separate: chapter exercises in chapterExercises.json remain unverified pending 1:1 drill matching against textbook problem sets (問題 p. 81)."
    },
    "skm2-c14-hanmen": {
        "grammarItem": "〜反面 (On the Flip Side: Coexisting Duality in the Same Entity)",
        "instructionalDetails": "Plain form (na-adj な/である, Noun である) + 反面. Presents two coexisting, contradictory aspects or characteristics of the same subject or entity. Contrasted with 〜一方で, which can contrast two distinct external entities.",
        "exampleCount": 3,
        "exampleIds": [
            "skm2-c14-hanmen::s-skm2-14-hanmen-1",
            "skm2-c14-hanmen::s-skm2-14-hanmen-2",
            "skm2-c14-hanmen::s-skm2-14-hanmen-3"
        ],
        "evidence": "Substantive instruction and dedicated practice implemented. Physical scan identified: Shin Kanzen Master N2 Chapter 14 (pp. 64-67 / PDF pp. 74-77). Implemented as standalone card [skm2-c14-hanmen] in studyPoints.json and bookSkmN2.ts with 3 authentic example sentences and practice exercise skm2-c14-ex-hanmen.",
        "missingWork": "Exercise provenance review remains separate: chapter exercises in chapterExercises.json remain unverified pending 1:1 drill matching against textbook problem sets (問題 p. 66)."
    }
}

for r in matrix:
    cid = r.get("cardId")
    if cid in NEW_MATRIX_DETAILS:
        d = NEW_MATRIX_DETAILS[cid]
        r["grammarItem"] = d["grammarItem"]
        r["instructionalDetails"] = d["instructionalDetails"]
        r["exampleCount"] = d["exampleCount"]
        r["exampleIds"] = d["exampleIds"]
        r["evidence"] = d["evidence"]
        r["missingWork"] = d["missingWork"]

with open("jlpt-exam-prep/audit/source-coverage-matrix.json", "w", encoding="utf-8") as f:
    json.dump(matrix, f, ensure_ascii=False, indent=2)

print("Updated source-coverage-matrix.json for the 5 newly implemented standalone points!")

# Update card-review.json as well
with open("jlpt-exam-prep/audit/card-review.json", encoding="utf-8") as f:
    card_reviews = json.load(f)

existing_cr_ids = {c["id"] for c in card_reviews}
for cid, d in NEW_MATRIX_DETAILS.items():
    if cid not in existing_cr_ids:
        card_reviews.append({
            "id": cid,
            "title": d["grammarItem"],
            "level": "N2",
            "book": "Shin Kanzen Master N2",
            "chapter": cid.split("-")[1].upper(),
            "sourceReference": f"Shin Kanzen Master N2 {cid}",
            "reviewStatus": "reopened",
            "distinctUses": ["Core construction", "Syntactic restrictions and nuances"],
            "exampleCount": 3,
            "exampleIds": d["exampleIds"],
            "quizCount": 1,
            "missingUses": [],
            "dimensions": {
                "meaning": True,
                "attachment": True,
                "nuance": True,
                "practice": True
            },
            "evidenceNotes": d["evidence"]
        })

with open("jlpt-exam-prep/audit/card-review.json", "w", encoding="utf-8") as f:
    json.dump(card_reviews, f, ensure_ascii=False, indent=2)

print("Updated card-review.json with new substantive cards!")
