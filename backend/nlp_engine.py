import re
import sudachipy

def katakana_to_hiragana(text: str) -> str:
    """Converts a Katakana string to Hiragana."""
    if not text:
        return ""
    return "".join(chr(ord(c) - 0x60) if 0x30A1 <= ord(c) <= 0x30F6 else c for c in text)

def is_kanji(ch: str) -> bool:
    return "\u4E00" <= ch <= "\u9FFF"

def extract_kanji(text: str) -> list[str]:
    return [c for c in text if is_kanji(c)]

POS_MAP = {
    "名詞": "Noun",
    "動詞": "Verb",
    "形容詞": "Adjective",
    "副詞": "Adverb",
    "連体詞": "Adnominal / Prenoun",
    "接続詞": "Conjunction",
    "感動詞": "Interjection",
    "助動詞": "Auxiliary Verb",
    "助詞": "Particle",
    "接頭辞": "Prefix",
    "接尾辞": "Suffix",
    "記号": "Symbol",
    "補助記号": "Punctuation"
}

class JapaneseNLPEngine:
    def __init__(self):
        self.dict = sudachipy.Dictionary()
        try:
            self.tokenizer = self.dict.tokenizer()
        except AttributeError:
            self.tokenizer = self.dict.create()

    def analyze_sentence(self, sentence: str) -> dict:
        """
        Segments and analyzes a Japanese sentence using Sudachi.
        Returns tokens with reading, dictionary base form, part of speech,
        conjugation form, and kanji characters.
        """
        if not sentence or not sentence.strip():
            return {"sentence": "", "tokens": [], "kanji": []}

        sentence = sentence.strip()
        tokens = []
        all_kanji = set()

        # SplitMode.C identifies compound words and natural expressions
        morphemes = self.tokenizer.tokenize(sentence, sudachipy.Tokenizer.SplitMode.C)

        for m in morphemes:
            surface = m.surface()
            base = m.dictionary_form()
            reading_kata = m.reading_form()
            reading_hira = katakana_to_hiragana(reading_kata)
            pos_tuple = m.part_of_speech()
            
            main_pos = pos_tuple[0]
            pos_label = POS_MAP.get(main_pos, main_pos)
            
            # Conjugation info
            conjugation_type = pos_tuple[4] if len(pos_tuple) > 4 and pos_tuple[4] != "*" else ""
            conjugation_form = pos_tuple[5] if len(pos_tuple) > 5 and pos_tuple[5] != "*" else ""

            word_kanji = extract_kanji(surface)
            for k in word_kanji:
                all_kanji.add(k)

            # Ignore punctuation tokens in vocabulary list
            is_punct = main_pos in ("補助記号", "記号")

            tokens.append({
                "surface": surface,
                "base_form": base,
                "reading_kata": reading_kata,
                "reading_hira": reading_hira,
                "part_of_speech": pos_label,
                "raw_pos": list(pos_tuple),
                "conjugation_type": conjugation_type,
                "conjugation_form": conjugation_form,
                "is_punctuation": is_punct,
                "kanji": word_kanji
            })

        return {
            "sentence": sentence,
            "tokens": tokens,
            "kanji": list(all_kanji)
        }
