#[derive(Debug, Clone, PartialEq, Eq)]
pub struct JapaneseToken {
    pub surface: String,
    pub has_kanji: bool,
    pub kanji: Vec<char>,
    pub is_punct: bool,
}

pub fn is_kanji(c: char) -> bool {
    matches!(c, '\u{4E00}'..='\u{9FFF}')
}

pub fn is_hiragana(c: char) -> bool {
    matches!(c, '\u{3040}'..='\u{309F}')
}

pub fn is_katakana(c: char) -> bool {
    matches!(c, '\u{30A0}'..='\u{30FF}')
}

pub fn is_cjk_punct(c: char) -> bool {
    matches!(c, '。' | '、' | '！' | '？' | '「' | '」' | '『' | '』' | '（' | '）' | '…' | '―')
}

#[allow(dead_code)]
pub fn katakana_to_hiragana(s: &str) -> String {
    s.chars()
        .map(|c| {
            if ('\u{30A1}'..='\u{30F6}').contains(&c) {
                char::from_u32(c as u32 - 0x60).unwrap_or(c)
            } else {
                c
            }
        })
        .collect()
}

/// Tokenizes a Japanese sentence into natural semantic blocks (Kanji head + okurigana/particles, or katakana loanwords)
pub fn tokenize_japanese(text: &str) -> Vec<JapaneseToken> {
    let mut tokens = Vec::new();
    let chars: Vec<char> = text.chars().collect();
    let len = chars.len();
    let mut i = 0;

    while i < len {
        let c = chars[i];

        // 1. Punctuation or whitespace
        if is_cjk_punct(c) || c.is_whitespace() || c.is_ascii_punctuation() {
            tokens.push(JapaneseToken {
                surface: c.to_string(),
                has_kanji: false,
                kanji: vec![],
                is_punct: true,
            });
            i += 1;
            continue;
        }

        // 2. Kanji chunk + connected okurigana
        if is_kanji(c) {
            let mut word = String::new();
            let mut kanji_list = Vec::new();

            // Collect consecutive kanji
            while i < len && is_kanji(chars[i]) {
                word.push(chars[i]);
                kanji_list.push(chars[i]);
                i += 1;
            }

            // Collect attached okurigana (hiragana following the kanji, up to 3 chars)
            let mut okurigana_count = 0;
            while i < len && is_hiragana(chars[i]) && okurigana_count < 3 {
                // If it's a standalone particle like は/が/を/に at the end of word boundary, break
                if okurigana_count > 0 && matches!(chars[i], 'は' | 'が' | 'を' | 'に' | 'へ' | 'で' | 'と') {
                    break;
                }
                word.push(chars[i]);
                okurigana_count += 1;
                i += 1;
            }

            tokens.push(JapaneseToken {
                surface: word,
                has_kanji: true,
                kanji: kanji_list,
                is_punct: false,
            });
            continue;
        }

        // 3. Katakana compound (e.g. ペルソナ, ゲーム)
        if is_katakana(c) || c == 'ー' {
            let mut kata = String::new();
            while i < len && (is_katakana(chars[i]) || chars[i] == 'ー') {
                kata.push(chars[i]);
                i += 1;
            }
            tokens.push(JapaneseToken {
                surface: kata,
                has_kanji: false,
                kanji: vec![],
                is_punct: false,
            });
            continue;
        }

        // 4. Hiragana particle or word
        if is_hiragana(c) {
            let mut hira = String::new();
            while i < len && is_hiragana(chars[i]) && !is_kanji(chars[i]) {
                hira.push(chars[i]);
                i += 1;
                // If common particle or grammar pattern, split naturally
                if matches!(chars[i - 1], 'は' | 'が' | 'を' | 'に' | 'へ' | 'で' | 'と' | 'も' | 'ね' | 'よ') {
                    break;
                }
            }
            tokens.push(JapaneseToken {
                surface: hira,
                has_kanji: false,
                kanji: vec![],
                is_punct: false,
            });
            continue;
        }

        // 5. Alphanumeric / other characters
        let mut other = String::new();
        while i < len && !is_kanji(chars[i]) && !is_hiragana(chars[i]) && !is_katakana(chars[i]) && !is_cjk_punct(chars[i]) {
            other.push(chars[i]);
            i += 1;
        }
        tokens.push(JapaneseToken {
            surface: other,
            has_kanji: false,
            kanji: vec![],
            is_punct: false,
        });
    }

    tokens
}
