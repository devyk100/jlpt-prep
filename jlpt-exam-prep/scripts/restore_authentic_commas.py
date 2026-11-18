import json, re

with open("jlpt-exam-prep/src/data/chapterExercises.json", encoding="utf-8") as f:
    exercises = json.load(f)

# Mapping of exercise ID to the exact option that carries the comma at the clause boundary
COMMA_PATCHES = {
    "skm3-p2-c1-q6": {"opt": "かどうか", "with_comma": "かどうか、"},
    "skm3-p2-c1-q10": {"opt": "思って", "with_comma": "思って、"},
    "skm3-p2-c2-q7": {"opt": "相次いで", "with_comma": "相次いで、"},
    "skm3-p2-c2-q8": {"opt": "名作小説は", "with_comma": "名作小説は、"},
    "skm3-p2-c2-q9": {"opt": "歌声で", "with_comma": "歌声で、"},
    "skm3-p2-c2-q12": {"opt": "果たすために", "with_comma": "果たすために、"},
    "skm3-p2-c3-q7": {"opt": "家電製品は", "with_comma": "家電製品は、"},
    "skm2-p2-c1-q2": {"opt": "甲斐があって", "with_comma": "甲斐があって、"},
    "skm2-p2-c1-q4": {"opt": "救命治療の甲斐もなく", "with_comma": "救命治療の甲斐もなく、"},
    "skm2-p2-c1-q6": {"opt": "牽引できる人物は", "with_comma": "牽引できる人物は、"},
    "skm2-p2-c1-q7": {"opt": "研究を続けた甲斐があって", "with_comma": "研究を続けた甲斐があって、"},
    "skm2-p2-c1-q8": {"opt": "コンタクトレンズなど", "with_comma": "コンタクトレンズなど、"},
    "skm2-p2-c1-q9": {"opt": "プレゼン資料だったが", "with_comma": "プレゼン資料だったが、"},
    "skm2-p2-c1-q10": {"opt": "主役となる人材は", "with_comma": "主役となる人材は、"},
    "skm2-p2-c1-q12": {"opt": "徹底した甲斐があって", "with_comma": "徹底した甲斐があって、"},
    "skm2-p2-c2-q1": {"opt": "漏洩させる行為は", "with_comma": "漏洩させる行為は、"},
    "skm2-p2-c2-q2": {"opt": "維持する上で", "with_comma": "維持する上で、"},
    "skm2-p2-c2-q4": {"opt": "取引に利用するなど", "with_comma": "取引に利用するなど、"},
    "skm2-p2-c2-q6": {"opt": "国民の安全を守る責務は", "with_comma": "国民の安全を守る責務は、"},
    "skm2-p2-c2-q7": {"opt": "屈服させる行為は", "with_comma": "屈服させる行為は、"},
    "skm2-p2-c2-q8": {"opt": "べからずとの警告が", "with_comma": "べからずとの警告が、"},
    "skm2-p2-c2-q9": {"opt": "夜間急病診療所の新設が", "with_comma": "夜間急病診療所の新設が、"},
    "skm2-p2-c2-q10": {"opt": "受け取るなどは", "with_comma": "受け取るなどは、"},
    "skm2-p2-c2-q11": {"opt": "ものづくりを貫く姿勢こそが", "with_comma": "ものづくりを貫く姿勢こそが、"},
    "skm2-p2-c2-q12": {"opt": "悲劇を繰り返さない誓いは", "with_comma": "悲劇を繰り返さない誓いは、"},
    "skm2-p2-c3-q1": {"opt": "不可欠である以上", "with_comma": "不可欠である以上、"},
    "skm2-p2-c3-q2": {"opt": "祝う会である以上", "with_comma": "祝う会である以上、"},
    "skm2-p2-c3-q3": {"opt": "心がけていても", "with_comma": "心がけていても、"},
    "skm2-p2-c3-q4": {"opt": "目の当たりにして", "with_comma": "目の当たりにして、"},
    "skm2-p2-c3-q6": {"opt": "損害を与えてしまった以上", "with_comma": "損害を与えてしまった以上、"},
    "skm2-p2-c3-q7": {"opt": "格下の相手であっても", "with_comma": "格下の相手であっても、"},
    "skm2-p2-c3-q8": {"opt": "助けを求めている以上", "with_comma": "助けを求めている以上、"},
    "skm2-p2-c3-q9": {"opt": "崇高な美しさに触れて", "with_comma": "崇高な美しさに触れて、"}
}

updated = 0
for ex in exercises:
    eid = ex.get("id")
    if eid in COMMA_PATCHES:
        p = COMMA_PATCHES[eid]
        old_opt = p["opt"]
        new_opt = p["with_comma"]
        
        # 1. Update in options list
        options = ex.get("options", [])
        if old_opt in options:
            idx = options.index(old_opt)
            options[idx] = new_opt
        
        # 2. Update in explanation.options
        expl_opts = ex.get("explanation", {}).get("options", [])
        for eo in expl_opts:
            if eo.get("text") == old_opt:
                eo["text"] = new_opt
                
        # 3. Update reconstructedSentence to exact concatenation with the authentic comma
        q = ex["question"]
        order = ex.get("scrambleOrder", [])
        m = re.search(r"＿＿\s*＿＿\s*★\s*＿＿", q)
        if m:
            prefix = q[:m.start()].strip()
            suffix = q[m.end():].strip()
            ex["reconstructedSentence"] = prefix + "".join(options[pos - 1] for pos in order) + suffix
            
        updated += 1

with open("jlpt-exam-prep/src/data/chapterExercises.json", "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print(f"Successfully restored authentic commas on options and reconstructed sentences for {updated} exercises.")
