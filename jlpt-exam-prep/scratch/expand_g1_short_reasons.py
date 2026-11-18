import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

ex_map = {e['id']: e for e in exercises}

additional_g1_repairs = {
    ('g1-l1-ex-6', 3): "Incorrect. 9 o'clock is read with the irregular reading くじ (kuji). The numeral reading きゅう is not used for 9 o'clock, nor does any geminated form *きゅっじ exist.",
    ('g1-l3-ex-5', 3): "Incorrect. Particle へ marks the directional destination of movement (e.g., 図書館へ行く). For an action that takes place at a location (本を読む), the locative particle で is required (図書館で本を読みます).",
    ('g1-l4-ex-3', 2): "Incorrect. The location of existence for あります/います is marked by particle に (あそこにあります). Particle を marks direct objects of transitive verbs and cannot mark an existence location.",
    ('g1-l4-ex-5', 1): "Incorrect. The sentence lists two reference points joined by と ('デパートと銀行の...'). Specifying the spatial interval between two objects requires 間 (あいだ, between); 前 (in front of) cannot relate two separate landmarks coordinate-linked with と.",
    ('g1-l10-ex-6', 1): "Incorrect. い-adjectives conjugate adverbially before なる by changing final -い to -く (暖かくなる). Particle に is used exclusively with nouns and な-adjectives (静かになる), never with い-adjectives (*暖かいに).",
    ('g1-l11-ex-1', 2): "Incorrect. The desiderative suffix 〜たい attaches directly to the pre-masu stem (行き -> 行きたい). Te-form forms cannot attach たい (*行きてたい).",
    ('g1-l11-ex-1', 3): "Incorrect. The suffix 〜たい requires the pre-masu stem (行き); it cannot attach to the dictionary/plain citation form (*行くたい).",
    ('g1-l12-ex-1', 2): "Incorrect. The advice formula 〜ほうがいいです requires plain past form (行ったほうがいいです) or plain negative (行かないほうがいいです). Polite -masu forms cannot precede ほうがいい.",
    ('g1-l12-ex-1', 3): "Incorrect. Te-forms cannot precede ほうがいい (*行ってほうがいい). The standard affirmative advice construction requires plain past ta-form: 行ったほうがいいです.",
    ('g1-l12-ex-3', 1): "Incorrect. Explanatory んです / のです attaches strictly to plain (short) forms (あるんです). Polite forms like あります cannot precede んです (*ありますんです).",
    ('g1-l12-ex-3', 3): "Incorrect. A bare pre-masu verb stem cannot attach directly to explanatory んです (*ありんです); the plain dictionary form ある is required.",
    ('g1-l12-ex-4', 2): "Incorrect. When a な-adjective precedes explanatory んです in non-past affirmative, it requires the connector な (暇なんです). A bare stem (*暇んです) is ungrammatical.",
    ('g1-l12-ex-4', 3): "Incorrect. な-adjectives take な before んです (暇なんです). Connector の is used with nouns (休みなんです / 休みの日), not with な-adjectives (*暇のんです).",
    ('g1-l12-ex-6', 1): "Incorrect. The excessive auxiliary verb 〜すぎる attaches to the pre-masu stem of verbs (食べ -> 食べすぎて). It cannot attach to the dictionary form (*食べるすぎて).",
    ('g1-l12-ex-6', 2): "Incorrect. The past ta-form cannot attach 〜すぎる (*食べたすぎて). Furthermore, 食べたすぎて would be the te-form of 食べたい (wanting to eat too much), not excessive action itself.",
    ('g1-l12-ex-7', 1): "Incorrect. For い-adjectives, the suffix 〜すぎる attaches directly to the root stem by dropping final -い (高 -> 高すぎる). Retaining the final い (*高いすぎ) is ungrammatical.",
    ('g1-l12-ex-7', 2): "Incorrect. Te-form cannot attach the suffix 〜すぎる (*高くてすぎ). The adjective root stem (高すぎます) is required.",
    ('g1-l12-ex-7', 3): "Incorrect. Past ta-form cannot attach 〜すぎる (*高かったすぎ). Tense is marked on すぎる itself (高すぎました).",
    ('g1-l12-ex-12', 1): "Incorrect. The prediction applies to this afternoon (午後), describing a future possibility ('it may rain'). The past copula でした contradicts future conjecture.",
    ('g1-l12-ex-12', 3): "Incorrect. The conjecture auxiliary かもしれません attaches directly to plain short forms (降るかもしれません). It cannot take a bare suffix ます (*降るます)."
}

for (eid, opt_idx), new_reason in additional_g1_repairs.items():
    ex = ex_map[eid]
    ex['explanation']['options'][opt_idx]['reason'] = new_reason

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Successfully applied additional Genki I enhancements!")
