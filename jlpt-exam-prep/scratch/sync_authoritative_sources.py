import json

# Update base-reviewed.json
with open('jlpt-exam-prep/content/base-reviewed.json', 'r', encoding='utf-8') as f:
    br_list = json.load(f)

for card in br_list:
    cid = card.get('id')
    if cid == 'skm2-c15-kuse-ni':
        card['nuance'] = (
            "SPEAKER'S BLAME & USAGE TENDENCY: Expresses critical concession loaded with reproach, dissatisfaction, "
            "or contempt toward the target's demeanor: 'despite being X, blameworthy Y'. In typical standard usage, "
            "the subject of both clauses is the same person who is being criticized. Because it conveys negative "
            "emotional evaluation and reproach, speakers generally avoid using it to describe themselves in straightforward "
            "declarative assertions (except in self-reproachful or rhetorical contexts). Contrast with 〜のに (general neutral "
            "or frustrated concession) and 〜にもかかわらず (formal objective concession)."
        )
        card['keyTakeaway'] = (
            "MUG-UP: Plain + くせに (Nの / naな). Conveys speaker's reproach or dissatisfaction. "
            "Typically same subject; generally avoided for oneself in plain assertion."
        )
    elif cid == 'g2-l14-tara-dou-desu-ka':
        card['nuance'] = (
            "〜たらどうですか conveys advice or a recommendation: \"Why don't you...? / How about doing...?\"."
            " Formation: Attaches to the past tense affirmative short form of a verb: V-た + らどうですか (薬を飲んだらどうですか, もっと勉強したらどうですか)."
            " Casual variants: shortened to 〜たらどう？ or simply 〜たら？ in casual speech."
            " PRAGMATIC USE & INVITATION CONVENTION: 〜たらどうですか focuses on advising the other person what they should do."
            " Consequently, standard Japanese etiquette avoids using it to invite someone to do an activity together with the speaker"
            " (for invitations to join the speaker, use 〜ませんか or 〜ましょうか instead of 〜たらどうですか)."
            " It can also carry a critical or pushy tone if unsolicited, so it is best used when advice is sought."
        )
        card['keyTakeaway'] = (
            "V-た + らどうですか (Why don't you...?; advice). Can carry critical tone if unsolicited."
            " Avoid for mutual invitations (use 〜ませんか / 〜ましょうか instead)."
        )

with open('jlpt-exam-prep/content/base-reviewed.json', 'w', encoding='utf-8') as f:
    json.dump(br_list, f, ensure_ascii=False, indent=2)

print("Updated content/base-reviewed.json successfully.")

# Also update studyPoints.json to have identical nuance for skm2-c15-kuse-ni
with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp_list = json.load(f)

for card in sp_list:
    cid = card.get('id')
    if cid == 'skm2-c15-kuse-ni':
        card['nuance'] = (
            "SPEAKER'S BLAME & USAGE TENDENCY: Expresses critical concession loaded with reproach, dissatisfaction, "
            "or contempt toward the target's demeanor: 'despite being X, blameworthy Y'. In typical standard usage, "
            "the subject of both clauses is the same person who is being criticized. Because it conveys negative "
            "emotional evaluation and reproach, speakers generally avoid using it to describe themselves in straightforward "
            "declarative assertions (except in self-reproachful or rhetorical contexts). Contrast with 〜のに (general neutral "
            "or frustrated concession) and 〜にもかかわらず (formal objective concession)."
        )
        card['keyTakeaway'] = (
            "MUG-UP: Plain + くせに (Nの / naな). Conveys speaker's reproach or dissatisfaction. "
            "Typically same subject; generally avoided for oneself in plain assertion."
        )

with open('jlpt-exam-prep/src/data/studyPoints.json', 'w', encoding='utf-8') as f:
    json.dump(sp_list, f, ensure_ascii=False, indent=2)

print("Updated src/data/studyPoints.json successfully.")
