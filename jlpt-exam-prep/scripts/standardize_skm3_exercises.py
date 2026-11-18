import json
import re
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"
BASE_PATH = ROOT / "content/base-reviewed.json"

base_cards = {c["id"]: c for c in json.load(open(BASE_PATH, encoding="utf-8"))}
exercises = json.load(open(EXERCISES_PATH, encoding="utf-8"))

CHAPTER_MAP = {
    "skm3-c6": "Part 1 · Chapter 6",
    "skm3-c7": "Part 1 · Chapter 7",
    "skm3-c8": "Part 1 · Chapter 8",
    "skm3-c9": "Part 1 · Chapter 9",
    "skm3-c10": "Part 1 · Chapter 10",
    "skm3-c11": "Part 1 · Chapter 11",
    "skm3-c12": "Part 1 · Chapter 12",
    "skm3-fa": "Part 1 · Form review A",
    "skm3-fb": "Part 1 · Form review B",
    "skm3-fc": "Part 1 · Form review C",
    "skm3-fd": "Part 1 · Form review D",
}

# IDs of old placeholders in skm3 c6-c12 to drop in favor of authentic 12 questions
DROP_IDS = {
    "skm3-c6-ex-1", "skm3-c6-ex-2", "skm3-c6-ex-3",
    "skm3-c7-ex-1", "skm3-c7-ex-2",
    "skm3-c8-ex-1", "skm3-c8-ex-2", "skm3-c8-ex-3", "skm3-c8-ex-4",
    "skm3-c9-ex-1", "skm3-c9-ex-2",
    "skm3-c10-ex-1", "skm3-c10-ex-2",
    "skm3-c11-ex-1", "skm3-c11-ex-2",
    "skm3-c12-ex-1", "skm3-c12-ex-2",
}

def parse_explanation(raw_exp, options, correct_idx):
    if isinstance(raw_exp, dict):
        return raw_exp
    
    parts = raw_exp.split("【選択肢解説】")
    overall = parts[0].strip()
    opt_lines = [l.strip() for l in parts[1].split("\n") if l.strip()] if len(parts) > 1 else []
    
    opt_reasons = {}
    for line in opt_lines:
        m = re.match(r"^(\d+)\.\s*(.+?)\s*\((正解|不正解)\):\s*(.+)$", line)
        if m:
            idx = int(m.group(1)) - 1
            opt_reasons[idx] = m.group(4).strip()
    
    opt_list = []
    for idx, opt in enumerate(options):
        is_correct = (idx == correct_idx)
        reason = opt_reasons.get(idx, "正解です。" if is_correct else "文脈・語用論的に不適切です。")
        trap = "formation" if any(w in reason for w in ["文法", "接続", "活用", "形"]) else ("context" if "文脈" in reason else "meaning")
        if is_correct:
            trap = ""
        opt_list.append({
            "text": opt,
            "isCorrect": is_correct,
            "reason": f"【{'正解' if is_correct else '不正解'}】{reason}",
            "trapCategory": trap
        })
    
    return {
        "overall": overall,
        "options": opt_list
    }

# Find representative card for chapter
CHAPTER_CARDS = {
    "Part 1 · Chapter 6": ("skm3-u6-sae-ba", "〜さえ〜ば (If Only / Provided That Sole Prerequisite Is Met)"),
    "Part 1 · Chapter 7": ("added-n3-7-49", "〜ということだ・〜とのことだ (Formal Transmission of Reported Information)"),
    "Part 1 · Chapter 8": ("skm3-u8-wake-ga-nai", "〜わけがない (Conviction of Absolute Impossibility)"),
    "Part 1 · Chapter 9": ("skm3-u9-garu", "〜がる (Third-Person Manifestation of Emotion/Desire)"),
    "Part 1 · Chapter 10": ("skm3-u9-beki-da", "〜べきだ / 〜べきではない (Moral Obligation & Due Conscience)"),
    "Part 1 · Chapter 11": ("skm3-u11-koto-ni-shite-iru", "〜ことにしている (Conscious Personal Rule & Regular Habit)"),
    "Part 1 · Chapter 12": ("skm3-u12-keigo-respect", "尊敬語 (Honorific Verbs & Formulas: Elevating Superior's Actions)"),
    "Part 1 · Form review A": ("added-n3-a-59", "助詞の整理 A: こそ・さえ・でも・くらい・まで・など"),
    "Part 1 · Form review B": ("added-n3-b-60", "助詞の整理 B: について・に対して・によって・にとって・として"),
    "Part 1 · Form review C": ("skm3-fc-tokoro-datta", "〜ところだった (Crisis Averted at the Last Moment)"),
    "Part 1 · Form review D": ("skm3-u7-you-ni-purpose", "〜ように (Purpose Clause: Non-Volitional Objective)"),
}

new_exercises = []
for ex in exercises:
    if ex["id"] in DROP_IDS:
        continue
    
    prefix = "-".join(ex["id"].split("-")[:2])
    if prefix in CHAPTER_MAP:
        chapter_name = CHAPTER_MAP[prefix]
        default_card_id, default_card_title = CHAPTER_CARDS.get(chapter_name, ("", ""))
        
        ex["bookId"] = "skm-n3"
        ex["chapter"] = chapter_name
        ex["type"] = "multiple-choice"
        if not ex.get("grammarPointId"):
            ex["grammarPointId"] = default_card_id
        if not ex.get("grammarPointTitle"):
            ex["grammarPointTitle"] = default_card_title
        if not ex.get("context"):
            ex["context"] = f"{chapter_name} authentic situational exercise."
        if not ex.get("translation"):
            ex["translation"] = ex["question"]
        if not ex.get("hint"):
            ex["hint"] = f"Review the grammatical constraints and nuance distinctions of {chapter_name}."
        
        ex["explanation"] = parse_explanation(ex["explanation"], ex["options"], ex["correctIndex"])
    
    new_exercises.append(ex)

EXERCISES_PATH.write_text(json.dumps(new_exercises, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Standardized exercises! Total: {len(new_exercises)}")
