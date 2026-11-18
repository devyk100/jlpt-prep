import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

repairs_35 = {
    ('skm3-c1-ex-6', '間に'): "Incorrect. 〜間に marks a brief, momentary event occurring inside a time frame. It directly clashes with the continuous durational predicate ずっと実家に滞在していた, which requires 間.",
    ('skm3-c2-ex-1', 'ままに'): "Incorrect. 〜まま denotes leaving an unchanged passive condition or submitting to emotion (足の向くままに). Assembling furniture following an instructional guide step-by-step requires とおりに.",
    ('skm3-c2-ex-2', 'にとって'): "Incorrect. 〜にとって indicates an evaluation from the personal perspective of an entity ('for / in the eyes of'). It cannot express variation across categories ('differ depending on the country').",
    ('skm3-c3-ex-4', 'にすぎない'): "Incorrect. 〜にすぎない expresses limitation ('is nothing more than / merely'). Recommending a warm sleep as the optimal remedy for a cold requires に限る (寝るに限る).",
    ('skm3-c4-ex-2', '反面に'): "Incorrect. 〜反面 expresses dual contradictory traits within the same entity. It does not take に, nor does it express reciprocal compensation or trade-offs between two favors.",
    ('skm3-c1-ex-10', 'とおり'): "Incorrect. 〜とおり denotes conformity with instructions or expectation ('just as'). Being caught in the ongoing act of eating cake requires the physical phase marker ところを.",
    ('skm3-c1-ex-12', '始まりそう'): "Incorrect. 〜そう expresses conjectural appearance. Compounding 始まりそう with ところだ is ungrammatical and semantically redundant; imminent action requires the dictionary form 始まるところだ.",
    ('skm3-c2-ex-12', '簡単だと'): "Incorrect. The natural consequence conditional と does not pair with ほど to form the proportional correlative construction ('the simpler, the easier'); な-adjectives take なら (簡単なら簡単なほど).",
    ('skm3-c3-ex-5', 'と'): "Incorrect. The sequence 夢と思うほど expresses plain quotation ('so much that I thought it was a dream'), but the rhetorical hyperbolic expression of wondering whether it is real requires the wonder particle か (夢かと思うほど).",
    ('skm3-c3-ex-7', 'とおりなら'): "Incorrect. 〜とおり denotes conformity with a model ('in accordance with'). Comparative preference rejecting a bad alternative in favor of not starting requires くらいなら.",
    ('skm3-c3-ex-7', 'うちに'): "Incorrect. 〜うちに indicates taking advantage of a temporary time window. It cannot express preferring one difficult option over another.",
    ('skm3-c3-ex-8', 'よる'): "Incorrect. 〜による indicates dependency, means, or cause ('depends on / caused by'). Concluding that cold barley tea is the absolute best drink on a hot day requires に限る.",
    ('skm3-c3-ex-9', 'とおり'): "Incorrect. 〜とおり denotes conformity to a plan. Describing an exam room so silent that one could hardly breathe expresses extreme metaphorical degree, requiring ほど.",
    ('skm3-c3-ex-9', 'ついでに'): "Incorrect. 〜ついでに denotes taking advantage of a primary task to perform a secondary errand. It cannot express intensity of degree.",
    ('skm3-c3-ex-10', 'する'): "Incorrect. Affirmative するに限る would recommend going outside during an approaching typhoon, which contradicts safety logic. Recommending avoiding an action requires negative plain form しないに限る.",
    ('skm3-c3-ex-11', 'うちに'): "Incorrect. 〜うちに denotes seizing a time window before circumstances change. Rejecting an undesirable marriage in favor of staying single requires the preference pattern くらいなら.",
    ('skm3-c3-ex-11', 'たびに'): "Incorrect. 〜たびに denotes repeated recurrence on each occasion. It does not express preferential choice between two lifestyle options.",
    ('skm3-c3-ex-11', 'とおりに'): "Incorrect. 〜とおりに denotes conformity with advice or plans. It cannot express preferring a single life over marrying someone without respect.",
    ('skm3-c3-ex-12', 'だけに'): "Incorrect. 〜だけに indicates that a natural consequence follows especially because of a reason. Superlative negative comparison ('nothing is as blissful as family time') requires ほど…はない.",
    ('skm3-c3-ex-12', 'にとって'): "Incorrect. 〜にとって marks a subjective evaluator ('for / to'). The subjective superlative pattern expressing that nothing surpasses a standard requires ほど (時間ほど幸せなものはない).",
    ('skm3-c4-ex-8', 'とおりに'): "Incorrect. 〜のとおりに denotes doing something in faithful accordance with instructions. Acting as a proxy to attend a meeting in place of a sick manager requires the substitution pattern かわりに (部長のかわりに).",
    ('skm3-c4-ex-8', '反面に'): "Incorrect. 〜反面 denotes dual contrasting aspects. It does not take に, nor does it express official proxy substitution in place of an absent person.",
    ('skm3-c4-ex-9', 'にとって'): "Incorrect. 〜にとって marks an evaluator's perspective ('in the eyes of'). Contrasting urban youth migration against rural depopulation requires the direct contrast marker に対して.",
    ('skm3-c4-ex-10', 'において'): "Incorrect. 〜において indicates a physical or abstract domain ('in / at'). Evaluating a weight difference relative to an older phone model requires the comparative standard に比べて.",
    ('skm3-c4-ex-10', 'にとって'): "Incorrect. 〜にとって marks a person evaluating a situation ('for / to'). Comparing physical weight specifications between two smartphone models requires に比べて.",
    ('skm3-c4-ex-12', 'うちに'): "Incorrect. 〜うちに indicates taking advantage of a temporary time window. Expressing a trade-off compensation (distant station compensated by spacious low rent) requires かわりに.",
    ('skm3-c4-ex-12', 'とおりに'): "Incorrect. 〜とおりに denotes conformity with instructions or plans. It cannot express balancing a drawback against an advantage.",
    ('skm3-c4-ex-12', 'たびに'): "Incorrect. 〜たびに indicates repeated recurrence each time an event happens. It cannot express a trade-off balance between rent price and location distance.",
    ('skm3-c5-ex-5', 'にとって'): "Incorrect. 〜にとって indicates an evaluation from someone's perspective ('for / in the eyes of'). Attributing accidents to the direct physical cause of inattentive driving requires による (不注意による事故).",
    ('skm3-c5-ex-5', 'に反して'): "Incorrect. 〜に反して expresses opposition to expectations, predictions, or wishes ('contrary to'). It cannot specify the causal agent of an accident.",
    ('skm3-c5-ex-9', 'について'): "Incorrect. 〜について marks a topic of inquiry ('regarding / about'). Specifying an earthquake as the direct physical cause of building collapses requires によって (地震によって倒壊した).",
    ('skm3-c5-ex-9', 'に対して'): "Incorrect. 〜に対して indicates a target or contrast between two parties. Specifying the physical external cause of house collapses requires によって.",
    ('skm3-c5-ex-9', 'にとって'): "Incorrect. 〜にとって marks an evaluator's standpoint ('for / to'). Specifying an earthquake as the causative destructive force requires によって.",
    ('skm3-c5-ex-12', '複雑に'): "Incorrect. 複雑に is the adverbial form modifying verbs. Modifying the causal noun ために requires the adjectival noun connector な (複雑なために = because it is complex).",
    ('skm3-c5-ex-12', '複雑'): "Incorrect. A bare な-adjective stem cannot attach directly to ために (*複雑ために). It strictly requires the connector な (複雑なために)."
}

count = 0
for ex in exercises:
    for opt in ex.get('explanation', {}).get('options', []):
        key = (ex.get('id'), opt.get('text'))
        if key in repairs_35:
            opt['reason'] = repairs_35[key]
            count += 1

print(f"Applied {count} expanded repairs.")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Saved chapterExercises.json successfully!")
