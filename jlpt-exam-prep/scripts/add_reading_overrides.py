import json

with open("jlpt-exam-prep/content/reading-overrides.json", "r", encoding="utf-8") as f:
    overrides = json.load(f)

new_entries = {
  "出せる": ["だせる", "can put out; can produce"],
  "立て直せる": ["たてなおせる", "can turn around (business); can rebuild"],
  "先週末": ["せんしゅうまつ", "last weekend"],
  "危険区域": ["きけんくいき", "danger zone; hazardous area"],
  "弾ける": ["ひける", "can play (a stringed/keyboard instrument)"],
  "弾けます": ["ひけます", "can play (polite)"],
  "新社屋": ["しんしゃおく", "new company building / headquarters"],
  "最終面接": ["さいしゅうめんせつ", "final job interview"],
  "欠かせない": ["かかせない", "indispensable; essential"],
  "何本": ["なんぼん", "how many (long cylindrical objects)"],
  "促": ["そく", "phonological gemination / double consonant (促音)"],
  "イ音便": ["いおんびん", "i-euphony (historical sound shift in verb conjugation)"],
  "待てる": ["まてる", "can wait (potential form of 待つ)"]
}

for k, v in new_entries.items():
    overrides[k] = v

with open("jlpt-exam-prep/content/reading-overrides.json", "w", encoding="utf-8") as f:
    json.dump(overrides, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_entries)} terms to reading-overrides.json!")
