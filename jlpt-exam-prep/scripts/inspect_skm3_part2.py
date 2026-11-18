import json
d = json.load(open('jlpt-exam-prep/src/data/chapterExercises.json', encoding='utf-8'))
p2 = [x for x in d if x.get('bookId')=='skm-n3' and 'Part 2' in x.get('chapter')]
for x in p2:
    print(x['id'], x['chapter'], x['question'], '--> ans:', x['options'][x['correctIndex']])
