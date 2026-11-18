import json
import re

with open("jlpt-exam-prep/src/data/chapterExercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

n3_exercises = [e for e in exercises if e.get("bookId") == "skm-n3"]

def enrich_reason(exercise, opt_idx, opt_text, is_correct, current_reason):
    r = current_reason
    q = exercise.get("question", "")
    overall = exercise.get("explanation", {}).get("overall", "")
    
    # If already long and detailed and doesn't have telegraphic markers, keep it
    if len(r) >= 30 and not any(tag in r for tag in ["【不正解】非文です。", "【不正解】禁止。", "【不正解】論文調。", "【不正解】比較。", "番目の要素です。"]):
        # clean up prefix tag if present
        return r

    # Build sentence with option inserted
    filled = q.replace("（　）", f"「{opt_text}」").replace("（　　）", f"「{opt_text}」").replace("＿＿ ＿＿ ★ ＿＿", f"[... {opt_text} ...]")

    # Check common telegraphic patterns and expand them with full sentence context
    if "非文" in r:
        return f"【不正解】接続形式の誤りです。本問の文脈で「{opt_text}」を挿入すると文法的な接続規則に合致せず、不自然な文（非文）となります。"
    
    if "過去形不適合" in r or "過去形不可" in r:
        return f"【不正解】時制の誤りです。この構文の従属節内には過去形（〜た）を接続できず、動作の未完了や継続を表す形が要求されます。"
    
    if "接続不適合" in r or "助詞接続誤り" in r or "活用不一致" in r or "助詞不適合" in r or "て形不適合" in r or "条件形不適合" in r or "構文不適合" in r or "文法的に誤り" in r:
        return f"【不正解】前後の接続形式の誤りです。「{opt_text}」の活用や助詞の組み合わせが、前後の述語・名詞との接続規則に適合しません。"

    if "意向形不適合" in r or "意向形不可" in r:
        return f"【不正解】後続節のモダリティ制約違反です。この文型では後続節に話者の意志・意向・勧誘（〜よう／〜たい）を置くことができません。"

    if "具体的物体" in r:
        return f"【不正解】意味的制約の誤りです。「{opt_text}」は具体的な物理的物体を指す場合に用いられ、本問のような抽象的事態・性質の記述には適しません。"

    if "尊敬語を自分の動作に使えない" in r:
        return f"【不正解】敬語の方向性の誤りです。「{opt_text}」は相手や上位者の動作を高める尊敬語であり、話し手自身（または身内）の動作に用いるとマナー違反になります（謙譲語を用いるべき文脈です）。"

    if "否定呼応" in r:
        return f"【不正解】呼応表現の誤りです。「{opt_text}」は文末に否定形（〜ない）を要求する呼応表現であり、本問のような肯定の文末には呼応しません。"

    if "話題" in r:
        return f"【不正解】「{opt_text}」は主題や話題を取り立てる表現（〜について等）ですが、本問の文脈で求められている構文的関係（理由・対比・条件等）と一致しません。"

    if "理由" in r:
        return f"【不正解】「{opt_text}」は直接的な理由・原因を表す表現ですが、本問の文脈（対比・逆接・時間の前後関係など）の論理的結束性を満たしません。"

    if "比較" in r:
        return f"【不正解】「{opt_text}」は二者間の程度や優劣を比較する基準を表す表現であり、本問で求められている文脈的意味に合いません。"

    if "禁止" in r:
        return f"【不正解】「{opt_text}」は強い直接的禁止を表す表現であり、本問のような客観的説明や指示の文脈には文体・語用論的に不適切です。"

    if "論文調" in r or "硬い書き言葉" in r or "くだけた口語" in r:
        return f"【不正解】位相・文体の不適合です。「{opt_text}」は文体（硬い書き言葉／くだけた会話体）が本問の文脈（場面・トーン）に合致しません。"

    if "役割" in r or "資格・役割" in r:
        return f"【不正解】「{opt_text}」は立場や資格・役割を表す用法ですが、本問で求められている論理関係とは異なります。"

    if "評価の視点" in r or "評価の基準" in r:
        return f"【不正解】「{opt_text}」は話者や主体の評価基準・判断の視点を表す表現であり、本問の事態描写・条件提示には適合しません。"

    if "極端事例" in r:
        return f"【不正解】「{opt_text}」は極端な例を挙げて全体を類推させる表現ですが、本問の文脈は一般的な条件・必然関係を述べており合いません。"

    if "限定" in r or "排他強調" in r:
        return f"【不正解】「{opt_text}」は特定の対象に限定・排他する強調表現ですが、本問の文脈的意図と論理的に矛盾します。"

    if "番目の要素です" in r:
        m = re.search(r"(\d+)番目の要素", r)
        pos = m.group(1) if m else "他"
        return f"【不正解】語順の誤りです。「{opt_text}」は{pos}番目に配置されるべき統語要素であり、★（3番目）の指定位置には入りません。"

    if "文末結び" in r:
        return f"【不正解】文末要素の誤りです。「{opt_text}」は文全体を締めくくる終止要素であり、★（3番目）の統語スロットには入りません。"

    # If it starts with 【不正解】 and is relatively short, expand it
    if r.startswith("【不正解】"):
        clean_tag = r.replace("【不正解】", "").rstrip("。")
        return f"【不正解】{clean_tag}のため不適切です。本問の文脈に挿入すると、文意や文法的呼応が成立しません。"

    if is_correct and len(r) < 25:
        return f"【正解】「{opt_text}」が文脈および前後の統語的接続規則に完全に合致します。"

    return r

# Test sample outputs
sample_tests = [
    ("skm3-c10-q1", 0, "べきではない", False, "【不正解】否定の当為になり意味が矛盾。"),
    ("skm3-c10-q1", 1, "によると", False, "【不正解】情報源の提示。"),
    ("skm3-c10-q4", 1, "するな", False, "【不正解】禁止。"),
    ("skm3-c10-q10", 2, "であること", False, "【不正解】論文調。"),
    ("skm3-p3-c1-q5", 1, "わけなら", False, "【不正解】非文です。"),
    ("skm3-p3-c1-q11", 1, "留学を決意したのは", False, "【不正解】1番目の要素です。"),
]

for sid, oidx, otext, ic, r in sample_tests:
    res = enrich_reason({"question": "テスト（　）文です。"}, oidx, otext, ic, r)
    print(f"[{sid}] '{otext}' -> {res}")
