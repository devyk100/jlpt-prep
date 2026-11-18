import json

path = 'jlpt-exam-prep/src/data/chapterExercises.json'
with open(path, 'r', encoding='utf-8') as f:
    exs = json.load(f)

for ex in exs:
    if ex['id'] == 'g1-l1-ex-2':
        ex['question'] = 'メアリーさんの専攻（　　）日本語です。'
        ex['context'] = "Stating Mary's major (Japanese language):"
        ex['translation'] = "Mary's major is Japanese."
        ex['options'] = ['は', 'の', 'か', 'と']
        ex['correctIndex'] = 0
        ex['explanation'] = {
            'overall': 'In X は Y です, the topic is メアリーさんの専攻 (Mary\'s major), marked by は, followed by the noun predicate 日本語です.',
            'options': [
                {'text': 'は', 'isCorrect': True, 'reason': 'Correct! は marks メアリーさんの専攻 as the topic of the sentence.'},
                {'text': 'の', 'isCorrect': False, 'reason': 'Incorrect. の would link two nouns into a possessive or modifying phrase, leaving the sentence without a topic.'},
                {'text': 'か', 'isCorrect': False, 'reason': 'Incorrect. か marks questions at the end of a sentence, not topics.'},
                {'text': 'と', 'isCorrect': False, 'reason': 'Incorrect. と connects nouns ("and") or marks quotations.'}
            ]
        }
    elif ex['id'] == 'g1-l1-ex-3':
        ex['context'] = 'You want to ask whether Mr. Smith is an international student. Choose the polite question ending:'
        ex['explanation']['options'] = [
            {'text': 'ですか', 'isCorrect': True, 'reason': 'Correct! ですか forms a standard polite question.'},
            {'text': 'ですね', 'isCorrect': False, 'reason': 'Incorrect. ですね is a tag-like agreement marker ("isn\'t he?"), not an open inquiry.'},
            {'text': 'ですよ', 'isCorrect': False, 'reason': 'Incorrect. ですよ is an informative assertion ("you know"), not a question.'},
            {'text': 'でした', 'isCorrect': False, 'reason': 'Incorrect. でした is past tense ("was"), making a statement rather than asking a question.'}
        ]
    elif ex['id'] == 'g1-l1-ex-4':
        ex['context'] = 'Replying in the negative that Mary is not a teacher, but a student:'
    elif ex['id'] == 'g1-l1-ex-5':
        ex['context'] = 'The clock displays 4:00 AM (4時). Choose the irregular reading for 4 o\'clock:'
        ex['explanation']['options'] = [
            {'text': 'よ', 'isCorrect': True, 'reason': 'Correct! 4 o\'clock is read irregularly as よじ (よ時).'},
            {'text': 'よん', 'isCorrect': False, 'reason': 'Incorrect. よんじ is ungrammatical for 4:00.'},
            {'text': 'し', 'isCorrect': False, 'reason': 'Incorrect. しじ is not used for 4 o\'clock in modern Japanese.'},
            {'text': 'よっ', 'isCorrect': False, 'reason': 'Incorrect. よっ is only used in counting days (よっか) or objects (よっつ).'}
        ]
    elif ex['id'] == 'g1-l1-ex-6':
        ex['context'] = 'The library schedule states closing time is 9:00 PM (9時). Choose the irregular reading for 9 o\'clock:'
        ex['explanation']['options'] = [
            {'text': 'く', 'isCorrect': True, 'reason': 'Correct! 9 o\'clock is read irregularly as くじ (く時).'},
            {'text': 'きゅう', 'isCorrect': False, 'reason': 'Incorrect. きゅうじ is not used for 9:00.'},
            {'text': 'ここの', 'isCorrect': False, 'reason': 'Incorrect. ここのつ is the native counter for 9 objects, not hours.'},
            {'text': 'きゅっ', 'isCorrect': False, 'reason': 'Incorrect. Not a valid reading for 9 o\'clock.'}
        ]
    elif ex['id'] == 'g1-l1-ex-7':
        ex['context'] = 'The meeting schedule indicates 2:30 PM (2時30分). Choose the natural suffix meaning "half past":'
    elif ex['id'] == 'g1-l1-ex-8':
        ex['context'] = 'The announcement states the train arrives in 10 minutes (10分). Choose the correct counter reading for 10 minutes:'
    elif ex['id'] == 'g1-l1-ex-9':
        ex['context'] = 'Takeshi celebrates his 20th birthday milestone (20歳). Choose the special traditional reading for 20 years of age:'
    elif ex['id'] == 'g1-l1-ex-10':
        ex['context'] = 'Indicating Mr. Smith\'s university affiliation (a student of Sakura University):'
    elif ex['id'] == 'g1-l1-ex-11':
        ex['context'] = 'Indicating possession (Mary\'s telephone number):'
    elif ex['id'] == 'g1-l1-ex-12':
        ex['context'] = 'Describing the teaching subject (a Japanese language teacher):'

with open(path, 'w', encoding='utf-8') as f:
    json.dump(exs, f, ensure_ascii=False, indent=2)

print('Updated Genki 1 Lesson 1 exercises in chapterExercises.json')
