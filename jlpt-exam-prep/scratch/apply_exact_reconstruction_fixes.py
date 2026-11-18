import json

# 1. Update chapterExercises.json
with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

for ex in exercises:
    eid = ex.get('id')
    
    # Fix skm2-p1-c24-q11
    if eid == 'skm2-p1-c24-q11':
        ex['question'] = '専門家が手厚くサポートしてくれるのだから、一人で余計な心配を（　）。'
        ex['options'] = [
            'することはない',
            'することだ',
            'しようではないか',
            'するまい'
        ]
        ex['correctIndex'] = 0
        ex['explanation'] = {
            'overall': '専門家がサポートしてくれるのだから「余計な心配をすることはない（する必要はない）」と相手の不安を解消して安心させます。',
            'options': [
                {
                    'text': 'することはない',
                    'isCorrect': True,
                    'reason': '【正解】「専門家が手厚くサポートしてくれるのだから、一人で余計な心配をすることはない」となり、「〜する必要はない」と相手の不安を解消して安心させる文脈に合致します。',
                    'trapCategory': ''
                },
                {
                    'text': 'することだ',
                    'isCorrect': False,
                    'reason': '【不正解】「一人で余計な心配をすることだ」とすると、「余計な心配をしなさい」という強い助言になり、手厚いサポートがある安心の文脈と矛盾します。',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'しようではないか',
                    'isCorrect': False,
                    'reason': '【不正解】「一人で余計な心配をしようではないか」という勧誘になり、心配することを呼びかける不自然な文になります。',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'するまい',
                    'isCorrect': False,
                    'reason': '【不正解】「一人で余計な心配をするまい」では話者自身の否定の意志表明になり、相手へのアドバイス・慰めの文脈には適合しません。',
                    'trapCategory': 'modality'
                }
            ]
        }

    # Fix skm2-p1-c24-q12
    elif eid == 'skm2-p1-c24-q12':
        ex['question'] = '志望校合格の夢を果たすまで、いかなることがあろうとも受験勉強を（　）。'
        ex['options'] = [
            '投げ出すまい',
            '投げ出すことだ',
            '投げ出そうではないか',
            '投げ出すことはない'
        ]
        ex['correctIndex'] = 0
        ex['explanation'] = {
            'overall': '合格の夢を果たすまで絶対に受験勉強を投げ出さないという話者自身の固い否定の決意を表す「〜まい」を用います。',
            'options': [
                {
                    'text': '投げ出すまい',
                    'isCorrect': True,
                    'reason': '【正解】動詞五段「投げ出す」に接続し、「受験勉強を投げ出すまい（絶対に投げ出さないぞ）」と話者自身の不退転の強い否定決意を表します。',
                    'trapCategory': ''
                },
                {
                    'text': '投げ出すことだ',
                    'isCorrect': False,
                    'reason': '【不正解】「受験勉強を投げ出すことだ」では「投げ出しなさい」という助言になり、合格を目指す決意の文脈と正反対になります。',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '投げ出そうではないか',
                    'isCorrect': False,
                    'reason': '【不正解】「受験勉強を投げ出そうではないか」という勧誘になり、勉強を諦めることを周囲に呼びかける不自然な文になります。',
                    'trapCategory': 'meaning'
                },
                {
                    'text': '投げ出すことはない',
                    'isCorrect': False,
                    'reason': '【不正解】「投げ出すことはない」は「投げ出す必要はない」という客観的な不要の表現であり、自分自身を鼓舞する強い主観的決意表明には「〜まい」を用います。',
                    'trapCategory': 'nuance'
                }
            ]
        }

    # Fix skm3-c2-ex-7
    elif eid == 'skm3-c2-ex-7':
        ex['question'] = '当日の天気（　　）、花火大会が中止になることもあります。'
        ex['options'] = [
            'によっては',
            'については',
            'に対しては',
            'にとっては'
        ]
        ex['correctIndex'] = 0
        ex['explanation'] = {
            'overall': '〜によっては pinpoints one specific possibility or extreme outcome from a spectrum of potential cases: "in some cases, depending on X" (天気によっては: depending on the weather, in some weather cases).',
            'options': [
                {
                    'text': 'によっては',
                    'isCorrect': True,
                    'reason': 'Correct. Noun + によっては singles out a possible extreme outcome depending on conditions: 「当日の天気によっては、花火大会が中止になることもあります」 (Depending on the weather on that day, the fireworks festival may be canceled).',
                    'trapCategory': 'formation'
                },
                {
                    'text': 'については',
                    'isCorrect': False,
                    'reason': 'Incorrect. 「当日の天気については」 means "concerning / regarding the weather on that day", which does not express conditional variation.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'に対しては',
                    'isCorrect': False,
                    'reason': 'Incorrect. 「当日の天気に対しては」 expresses opposition or targeting toward the weather, not contingent variation.',
                    'trapCategory': 'meaning'
                },
                {
                    'text': 'にとっては',
                    'isCorrect': False,
                    'reason': 'Incorrect. 「当日の天気にとっては」 means "from the standpoint of the weather", which is nonsensical in this context.',
                    'trapCategory': 'meaning'
                }
            ]
        }

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("chapterExercises.json updated successfully.")

# 2. Update studyPoints.json
with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sps = json.load(f)

for sp in sps:
    sid = sp.get('id')
    
    # Refine skm2-c15-kuse-ni
    if sid == 'skm2-c15-kuse-ni':
        sp['nuance'] = (
            "SPEAKER'S BLAME & TYPICAL SUBJECT CONSTRAINTS: Expresses critical concession loaded with reproach, "
            "dissatisfaction, or contempt toward the target's demeanor. As noted in SKM N2, the subjects of clauses A and B "
            "are typically the same person (前と後ろの主語は同じ人であることが多い). Because it conveys reproach and criticism, "
            "speakers usually avoid using it to describe themselves in straightforward declarative statements "
            "(話者自身の行為には通常使わない, except in self-reproach or rhetorical contexts). "
            "Contrast with 〜のに (general neutral/frustrated concession) and 〜にもかかわらず (formal objective concession)."
        )
        sp['keyTakeaway'] = (
            "MUG-UP: Plain + くせに (Nの / naな). Typically same subject; conveys speaker's reproach/dissatisfaction. "
            "Generally avoided for oneself in plain assertion."
        )
        
    # Refine g2-l14-tara-dou-desu-ka
    elif sid == 'g2-l14-tara-dou-desu-ka':
        sp['nuance'] = (
            "〜たらどうですか conveys advice or a recommendation: \"Why don't you...? / How about doing...?\". "
            "Formation: Attaches to the past tense affirmative short form of a verb: V-た + らどうですか (薬を飲んだらどうですか, もっと勉強したらどうですか). "
            "Casual variants: shortened to 〜たらどう？ or simply 〜たら？ in casual speech. "
            "PRAGMATIC USE & INVITATION CONVENTION: 〜たらどうですか focuses on advising the other person what they should do. "
            "Consequently, standard Japanese etiquette avoids using it to invite someone to do an activity together with the speaker "
            "(for invitations to join the speaker, use 〜ませんか or 〜ましょうか instead of 〜たらどうですか). "
            "It can also carry a critical or pushy tone if unsolicited, so it is best used when advice is sought."
        )
        sp['keyTakeaway'] = (
            "V-た + らどうですか (Why don't you...?; advice). Can carry critical tone if unsolicited. "
            "Avoid for mutual invitations (use 〜ませんか / 〜ましょうか instead)."
        )

with open('jlpt-exam-prep/src/data/studyPoints.json', 'w', encoding='utf-8') as f:
    json.dump(sps, f, ensure_ascii=False, indent=2)

print("studyPoints.json updated successfully.")
