import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

ex_map = {e['id']: e for e in exercises}

# 1. Specific repairs for Genki I items
repairs = {
    ('g1-l1-ex-1', 2): "Incorrect. The particle の marks possession or noun modification (私のかばん = my bag). Placing の after 私 creates '私のキム・ソラです' (It is my Sora Kim), which erroneously treats Kim Sora as a possessed object rather than identifying oneself. Self-introduction requires the topic marker は.",
    ('g1-l1-ex-5', 1): "Incorrect. Four o'clock has an irregular phonetic reading: 四 drops the nasal /n/ before 時 (じ) to become よじ (yoji). The standard counting numeral よん is phonologically invalid with the hour counter (*よんじ).",
    ('g1-l2-ex-5', 2): "Incorrect. だれ is an interrogative pronoun for people ('who'). The question asks for the location of the post office (郵便局), and speaker B replies with a spatial demonstrative 'あそこです' (over there). Asking for a physical location requires the place interrogative どこ.",
    ('g1-l2-ex-9', 3): "Incorrect. The polite negative copula is formed by adding ありません to では/じゃ (じゃありません) or by using the conversational form じゃないです. *じゃあります is an incomplete non-existent hybrid combining negative じゃ with affirmative あります.",
    ('g1-l2-ex-12', 1): "Incorrect. これ is an independent demonstrative pronoun that stands alone as a noun; it cannot modify another noun directly (*これ本). Direct modification of the noun 本 (book) requires the demonstrative adjective この (この本).",
    ('g1-l4-ex-2', 2): "Incorrect. します is the polite non-past form of the action verb する ('to do'). Stating the existence or presence of a living being (猫, a cat) in a location requires the existence verb います (教室に猫がいます).",
    ('g1-l4-ex-4', 2): "Incorrect. 中 (なか) means 'inside' an enclosed volume or container (like a box or drawer). A table (テーブル) is a flat surface, so placing an object on top of it takes 上 (うえ, on top of), not 中.",
    ('g1-l4-ex-4', 3): "Incorrect. 後ろ (うしろ) means 'behind' or 'in back of'. Resting a phone on the flat upper surface of a table takes the positional noun 上 (うえ, on/above), not 後ろ.",
    ('g1-l4-ex-7', 3): "Incorrect. 勉強しません is polite present/future negative ('I do not / will not study'). The time adverbial きのう (yesterday) establishes a past event, requiring the polite past affirmative 勉強しました.",
    ('g1-l4-ex-10', 3): "Incorrect. 休み is a noun ('day off / holiday'). Noun predicates conjugate past negative using じゃなかったです (or じゃありませんでした). The suffix -くない belongs strictly to い-adjectives; attaching *くないでした to a noun is morphologically invalid.",
    ('g1-l5-ex-1', 2): "Incorrect. い-adjectives conjugate past tense on the adjective stem itself: affirmative past is 高かったです, and negative past replaces final い with くなかったです (高くなかったです). Attaching でした directly to the present negative form (*高くないでした) is an ungrammatical learner error.",
    ('g1-l5-ex-3', 2): "Incorrect. 面白い is an い-adjective. Its polite past negative is formed by changing final -い to -くなかったです (面白くなかったです). Combining the present negative -くない with past copula でした (*面白くないでした) is ungrammatical.",
    ('g1-l5-ex-4', 3): "Incorrect. The irregular い-adjective いい (good) must change its base stem to よ- for all inflections: negative よくない, past よかった, past negative よかった/よくなかったです. Conjugating from base *い- (*いくなかったです) is strictly invalid.",
    ('g1-l6-ex-5', 2): "Incorrect. 行く (to go) is an irregular Godan verb whose te-form undergoes gemination to 行って (いって). It does not follow regular Godan く -> いて inflection, nor does it insert an i-stem suffix (*行きりて).",
    ('g1-l6-ex-5', 3): "Incorrect. The te-form ending -んで applies only to Godan verbs ending in む, ぶ, or ぬ (such as 飲む -> 飲んで, 遊ぶ -> 遊んで). The verb 行く ends in く and forms the irregular te-form 行って.",
    ('g1-l6-ex-9', 2): "Incorrect. 〜てください is a polite request ('please do X'). In the context of a library sign or rule prohibiting eating and drinking (飲食), the prohibitive form 〜てはいけません is required, not a polite request inviting visitors to eat.",
    ('g1-l6-ex-10', 3): "Incorrect. In Japanese, multiple sequential actions in a chronological series must be connected using the te-form (〜て、〜て、〜ました). Simply concatenating bare past ta-forms without conjunctions (*起きた、食べた、行きました) is syntactically invalid.",
    ('g1-l7-ex-1', 2): "Incorrect. 読んだ is the casual past form ('read'). The sentence opens with the progressive temporal adverb 今 (right now), describing an action currently taking place; this ongoing activity requires the polite progressive form 読んでいます, not past tense.",
    ('g1-l7-ex-3', 1): "Incorrect. While 知っている expresses the continuous state of possessing information, its negative state is expressed exclusively by the simple non-past negative verb 知りません ('I do not know'). The form *知っていません is a recognized learner overgeneralization that is ungrammatical in standard Japanese.",
    ('g1-l7-ex-3', 2): "Incorrect. 知る is a verb, not an adjective. Its polite past negative is 知りませんでした. Combining the plain negative verb stem 知らない with past copula でした (*知らないでした) is a morphologically invalid hybrid.",
    ('g1-l7-ex-4', 3): "Incorrect. 住む is a verb indicating residence. A continuous state of living somewhere is expressed with the te-iru form (住んでいます). Attaching the past copula でした directly to a bare verb stem (*住みでした) is grammatically invalid.",
    ('g1-l7-ex-11', 2): "Incorrect. 太った is the plain past form of the change-of-state verb 太る. Describing the present resulting state of being overweight requires the te-iru form 太っています (or 太っている in plain speech). Attaching copula でした directly to a plain past verb (*太ったでした) is ungrammatical.",
    ('g1-l8-ex-3', 3): "Incorrect. Plain negative forms of Godan verbs shift the final -u vowel to -a before adding -ない (話す -> 話さない). Appending ない directly to the dictionary form (*話すない) is morphologically invalid.",
    ('g1-l8-ex-4', 2): "Incorrect. ありませんでした is a polite past form (丁寧語). However, the sentence context specifies a casual conversation with a peer ('今日、お金が全然（ ）') requiring plain/short form, and 今日 (today) establishes non-past time. The casual short negative form is ない.",
    ('g1-l8-ex-10', 2): "Incorrect. 何が is an interrogative pronoun marked by the subject particle が ('what'). Expressing total negative exclusion ('did not eat anything at all') after an upset stomach requires the negative polarity item 何も (nothing) paired with negative verb 食べませんでした.",
    ('g1-l8-ex-12', 3): "Incorrect. Interrogative question words like だれ cannot take the topic marker は (*だれは). Expressing absolute negative absence ('nobody was in the classroom') requires the interrogative quantifier だれも paired with the negative verb いませんでした.",
    ('g1-l9-ex-1', 2): "Incorrect. 読む is a Godan verb ending in -mu. Its plain past (ta-form) undergoes nasal assimilation, changing -mu to -んだ (読んだ). Omitting the nasal syllabic n (*読だ) is phonologically and orthographically incorrect.",
    ('g1-l9-ex-2', 1): "Incorrect. Plain past negative of verbs is formed by conjugating -ない like an い-adjective to -なかった (行かなかった). Attaching polite past copula でした to the plain negative (*行かないでした) is an ungrammatical hybrid, and the casual sentence clause requires casual short form 行かなかった.",
    ('g1-l9-ex-2', 3): "Incorrect. 行く is an irregular verb whose te-form is 行って, not *行きて. Furthermore, the sentence simply states that the speaker did not go to school due to fever, requiring the simple past negative 行かなかった rather than a past progressive.",
    ('g1-l9-ex-3', 2): "Incorrect. また means 'again' or 'once more' (また宿題をしました = I did my homework again). In the question asking whether the homework is already completed, the aspectual adverb もう ('already') is required, which speaker B confirms with 'はい、もうしました'.",
    ('g1-l9-ex-3', 3): "Incorrect. もっと is a comparative degree adverb meaning 'more' (もっと勉強する = study more). It cannot function as a temporal/aspectual marker asking if an event has already transpired.",
    ('g1-l9-ex-9', 3): "Incorrect. The adjective いい (good) conjugates to past tense by changing its stem to よ- and adding -かった (よかった). The phrasing *よくあった misanalyzes the adjective as if it were adverb よく followed by verb あった, which is ungrammatical for 'was good'.",
    ('g1-l9-ex-10', 1): "Incorrect. The plain past negative of the copula for nouns is じゃなかった (or ではなかった). The sequence *じゃないだった incorrectly appends the past copula だった to the non-past negative じゃない, which is ungrammatical.",
    ('g1-l9-ex-10', 3): "Incorrect. The inflection -くない belongs to い-adjectives, not nouns like 休み. Furthermore, combining -くない with だった (*くないだった) is doubly ungrammatical; noun predicates take じゃなかった.",
    ('g1-l10-ex-1', 3): "Incorrect. The comparative construction 'A is more [adj] than B' requires the formula [A] のほうが [B] より [adj] です. The combination が・で does not establish a comparative comparison between two items.",
    ('g1-l10-ex-4', 3): "Incorrect. The intention pattern 〜つもりだ requires the dictionary form (行くつもりです) or negative plain form. Te-forms cannot precede つもり, and 行く has the irregular te-form 行って, making *行きて doubly invalid.",
    ('g1-l10-ex-5', 1): "Incorrect. The noun つもり can only be modified by plain (short) forms of verbs. *買いますない is an ungrammatical hybrid attempting to attach negative ない to polite -masu stem; the plain negative form is 買わない.",
    ('g1-l10-ex-5', 3): "Incorrect. 買う is a Godan verb ending in -う; its te-form is 買って, not *買いて. Furthermore, expressing intention not to buy requires the plain non-past negative 買わない, not a te-form.",
    ('g1-l10-ex-9', 3): "Incorrect. The means/manner particle で attaches to nouns (車で, 電車で). Verbs indicating manner of movement must connect via te-form (歩いて行く, to go on foot). Attaching で to the dictionary verb *歩くで is ungrammatical.",
    ('g1-l11-ex-2', 2): "Incorrect. The desiderative suffix -たい inflects exactly like an い-adjective. Its polite non-past negative is 食べたくないです. The form *食べたくないでした incorrectly attempts to attach past copula でした to present negative -くない, which is ungrammatical.",
    ('g1-l11-ex-2', 3): "Incorrect. The desiderative auxiliary -たい attaches directly to the pre-masu verb stem (食べたい). Negation is applied to -たい itself (食べたくないです). Attaching -たい to a negative verb form (*食べないたいです) is morphologically invalid.",
    ('g1-l11-ex-5', 2): "Incorrect. In Japanese grammar, -たい expresses first-person (or second-person in questions) internal desires. For a third person (メアリーさん), observable desire must be expressed with 〜たがっています. Additionally, the past form of -たい is -たかったです, making *たいでした an invalid formation.",
    ('g1-l11-ex-5', 3): "Incorrect. たがる is a Godan verb describing ongoing third-person outward symptoms of desire. In polite style, it conjugates into the continuous aspect 〜たがっています. Appending copula でした to the bare plain stem (*たがるでした) is ungrammatical.",
    ('g1-l11-ex-9', 3): "Incorrect. The representative listing pattern 〜たり〜たり closes with a conjugated form of する. For past polite style, する conjugates to しました. Attaching past copula でした to the plain dictionary verb (*するでした) is ungrammatical.",
    ('g1-l12-ex-2', 2): "Incorrect. The irregular verb する has the plain negative form しない. Attaching ない directly to the dictionary form (*するない) is ungrammatical. The negative advice pattern 'had better not do' requires plain negative + ほうがいい (しないほうがいいです).",
    ('g1-l12-ex-6', 3): "Incorrect. 食べる is an Ichidan (Ru-verb). The excessive suffix 〜すぎる attaches directly to the pre-masu stem by dropping る (食べすぎる -> 食べすぎて). Conjugating 食べる as if it were a Godan verb with an -i stem (*食べりすぎて) is morphologically invalid.",
    ('g1-l12-ex-11', 2): "Incorrect. When the explanatory conjunction ので follows a noun or な-adjective, it requires the copular connective particle な (日曜日なので). Using の (*日曜日のので) creates a stuttering duplicate particle that is strictly ungrammatical."
}

# Apply dictionary repairs
for (eid, opt_idx), new_reason in repairs.items():
    ex = ex_map[eid]
    ex['explanation']['options'][opt_idx]['reason'] = new_reason

# 2. Fix sync for g1-l3-ex-2
ex_l3 = ex_map['g1-l3-ex-2']
ex_l3['options'] = ["飲みます", "飲ます", "飲めません", "飲んだ"]
ex_l3['correctIndex'] = 0
ex_l3['explanation']['options'] = [
    {
        "text": "飲みます",
        "isCorrect": True,
        "reason": "Correct. 飲む is a Godan/U-verb ending in -mu; its polite non-past stem shifts the final -u to -i (飲み) plus ます -> 飲みます. This matches the habitual daily action marked by 毎日.",
        "trapCategory": "formation"
    },
    {
        "text": "飲ます",
        "isCorrect": False,
        "reason": "Incorrect. 飲ます is the causative base (short form of 飲ませる, 'to make someone drink'). It is not the polite non-past form of 飲む.",
        "trapCategory": "formation"
    },
    {
        "text": "飲めません",
        "isCorrect": False,
        "reason": "Incorrect. 飲めません is the polite negative potential form ('cannot drink'). The sentence states a habitual daily activity ('every day I drink...'), which requires affirmative 飲みます.",
        "trapCategory": "formation"
    },
    {
        "text": "飲んだ",
        "isCorrect": False,
        "reason": "Incorrect. 飲んだ is the informal plain past tense ('drank'). The adverb 毎日 (every day) describes an ongoing habitual routine, not a completed past event, and standard polite textbook style requires 飲みます.",
        "trapCategory": "formation"
    }
]

# 3. Fix sync for g1-l5-ex-5
ex_l5 = ex_map['g1-l5-ex-5']
# Make sure options order matches explanation.options
ex_l5['options'] = ["静かじゃないです", "静かいくないです", "静かじゃない", "静かでした"]
ex_l5['correctIndex'] = 0
ex_l5['explanation']['options'] = [
    {
        "text": "静かじゃないです",
        "isCorrect": True,
        "reason": "Correct. 静か is a な-adjective; its polite present negative is formed with じゃないです (or じゃありません).",
        "trapCategory": "formation"
    },
    {
        "text": "静かいくないです",
        "isCorrect": False,
        "reason": "Incorrect. 静か is a な-adjective, not an い-adjective. Appending the い-adjective negative suffix -くない directly to a な-adjective stem (*静かいくないです) is ungrammatical.",
        "trapCategory": "formation"
    },
    {
        "text": "静かじゃない",
        "isCorrect": False,
        "reason": "Incorrect. 静かじゃない is the informal/plain negative form. The sentence predicate requires polite style (です/ます level).",
        "trapCategory": "register"
    },
    {
        "text": "静かでした",
        "isCorrect": False,
        "reason": "Incorrect. 静かでした is the polite past affirmative ('was quiet'). The sentence context describes the current state of the apartment's neighborhood in the negative.",
        "trapCategory": "tense"
    }
]

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Successfully updated Genki I exercises in chapterExercises.json!")
