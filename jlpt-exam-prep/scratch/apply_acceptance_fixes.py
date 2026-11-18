import json

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

# 1. Update Chapter 20 questions 3-12 contexts and translations
c20_updates = {
    "skm2-p1-c20-q3": {
        "context": "Customer service desk declining inquiries regarding personal privacy.",
        "translation": "At this inquiry desk, we are unable to answer questions involving our customers' personal privacy."
    },
    "skm2-p1-c20-q4": {
        "context": "Warning of tragic death from overwork if harsh prolonged overtime continues unchecked.",
        "translation": "If harsh prolonged overtime is left unchecked, it could lead to the catastrophic outcome of employees dying from overwork."
    },
    "skm2-p1-c20-q5": {
        "context": "Preparing legal countermeasures depending on the opposing party's maneuvers.",
        "translation": "Depending on how the other party acts, we are making preparations with a stance of not shrinking from legal countermeasures."
    },
    "skm2-p1-c20-q6": {
        "context": "Urgent meteorological warning that rivers risk flooding due to an approaching typhoon.",
        "translation": "A very strong, large typhoon is approaching, and rivers risk overflowing from late tonight into the early hours of tomorrow."
    },
    "skm2-p1-c20-q7": {
        "context": "Politely refusing to make a definitive commitment at the current stage in business.",
        "translation": "We truly regret it, but as we are unable to make a firm commitment at the current stage, we kindly ask for your understanding."
    },
    "skm2-p1-c20-q8": {
        "context": "Warning that a careless remark could trigger an irreparable brawl.",
        "translation": "A careless remark could deeply hurt the other person's self-esteem and develop into an irreparable fierce quarrel."
    },
    "skm2-p1-c20-q9": {
        "context": "Planning to relocate an outdoor music festival indoors depending on weather forecast trends.",
        "translation": "Depending on the progression of the weather forecast, we plan to move tomorrow's outdoor music festival to an indoor hall."
    },
    "skm2-p1-c20-q10": {
        "context": "Warning that the medical care system risks complete collapse in the event of an explosive virus outbreak.",
        "translation": "If an explosive outbreak of the novel virus occurs, the medical healthcare provision system risks completely collapsing."
    },
    "skm2-p1-c20-q11": {
        "context": "Politely deferring an immediate answer to consult with superiors back at the office.",
        "translation": "As I am unable to answer immediately on my own discretion, please allow me to take this back to the company and consult with my supervisor."
    },
    "skm2-p1-c20-q12": {
        "context": "Warning that even slight negligence in inspection could cause a major aviation incident.",
        "translation": "If inspection work is neglected even slightly, it could cause a major safety incident involving aircraft operation."
    }
}

# 2. Update Chapter 24 q11 and q12 questions
c24_updates = {
    "skm2-p1-c24-q11": {
        "question": "専門家が手厚くサポートしてくれるのだから、一人で余計な心配をす（　）。"
    },
    "skm2-p1-c24-q12": {
        "question": "志望校合格の夢を果たすまで、いかなることがあろうとも受験勉強を投げ出（　）。"
    }
}

# 3. Update Chapter 25 q1 and q2 questions
c25_updates = {
    "skm2-p1-c25-q1": {
        "question": "大勢の聴衆の前で発表する直前、過度の緊張で心臓がどきどきして（　）。"
    },
    "skm2-p1-c25-q2": {
        "question": "初めて一人暮らしを始めて誰もいない部屋に帰ってきた時、寂しくて（　）。"
    }
}

count_updated = 0
for ex in exercises:
    eid = ex.get('id')
    if eid in c20_updates:
        ex['context'] = c20_updates[eid]['context']
        ex['translation'] = c20_updates[eid]['translation']
        count_updated += 1
    elif eid in c24_updates:
        ex['question'] = c24_updates[eid]['question']
        count_updated += 1
    elif eid in c25_updates:
        ex['question'] = c25_updates[eid]['question']
        count_updated += 1

print(f"Applied repairs to {count_updated} exercises.")

with open('jlpt-exam-prep/src/data/chapterExercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)
