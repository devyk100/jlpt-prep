use image::RgbaImage;
use std::io::Cursor;
use std::time::Instant;
use windows::core::{HSTRING, Result as WinResult};
use windows::Globalization::Language;
use windows::Graphics::Imaging::BitmapDecoder;
use windows::Media::Ocr::OcrEngine;
use windows::Storage::Streams::{DataWriter, InMemoryRandomAccessStream};

pub struct NativeOcrEngine {
    engine: Option<OcrEngine>,
}

unsafe impl Send for NativeOcrEngine {}
unsafe impl Sync for NativeOcrEngine {}

impl NativeOcrEngine {
    pub fn new() -> Self {
        let engine = match Self::init_engine() {
            Ok(e) => {
                println!("[OCR] Windows Native Japanese OCR engine initialized successfully!");
                Some(e)
            }
            Err(err) => {
                eprintln!("[OCR] Failed to initialize Windows Media OCR: {:?}", err);
                None
            }
        };

        Self { engine }
    }

    fn init_engine() -> WinResult<OcrEngine> {
        let lang = Language::CreateLanguage(&HSTRING::from("ja"))?;
        let engine = OcrEngine::TryCreateFromLanguage(&lang)?;
        Ok(engine)
    }

    pub fn recognize(&self, img: &RgbaImage) -> (String, Vec<String>, f64) {
        let t0 = Instant::now();
        let engine = match &self.engine {
            Some(e) => e,
            None => return ("OCR engine unavailable".to_string(), vec![], 0.0),
        };

        // Encode image as PNG bytes in-memory
        let mut png_bytes = Vec::new();
        if let Err(e) = img.write_to(&mut Cursor::new(&mut png_bytes), image::ImageFormat::Png) {
            return (format!("Image encode error: {}", e), vec![], 0.0);
        }

        match self.recognize_bytes(engine, &png_bytes) {
            Ok((text, lines)) => {
                let ms = t0.elapsed().as_secs_f64() * 1000.0;
                (text, lines, ms)
            }
            Err(e) => {
                eprintln!("[OCR] Recognition error: {:?}", e);
                (format!("OCR error: {:?}", e), vec![], 0.0)
            }
        }
    }

    fn recognize_bytes(&self, engine: &OcrEngine, bytes: &[u8]) -> WinResult<(String, Vec<String>)> {
        let stream = InMemoryRandomAccessStream::new()?;
        let writer = DataWriter::CreateDataWriter(&stream)?;
        writer.WriteBytes(bytes)?;
        writer.StoreAsync()?.join()?;
        writer.DetachStream()?;
        stream.Seek(0)?;

        let decoder = BitmapDecoder::CreateAsync(&stream)?.join()?;
        let bitmap = decoder.GetSoftwareBitmapAsync()?.join()?;
        let result = engine.RecognizeAsync(&bitmap)?.join()?;

        let mut lines = Vec::new();
        let ocr_lines = result.Lines()?;
        for line in ocr_lines {
            let line_text = line.Text()?.to_string();
            let cleaned = Self::filter_japanese_only(&line_text);
            if !cleaned.trim().is_empty() {
                lines.push(cleaned);
            }
        }

        let full_text = lines.join("\n");
        Ok((full_text, lines))
    }

    /// Strictly filters out English/Latin text, preserving only Japanese dialogue
    fn filter_japanese_only(text: &str) -> String {
        // 1. If line has zero Japanese characters, discard immediately
        if !text.chars().any(Self::is_japanese) {
            return String::new();
        }

        // 2. Strip English/ASCII words (e.g. "Meaning", "Level", "Showmore", "Easy")
        let mut out = String::with_capacity(text.len());
        let chars: Vec<char> = text.chars().collect();
        let len = chars.len();
        let mut i = 0;

        while i < len {
            let c = chars[i];

            if c.is_ascii_alphabetic() {
                // Skip the entire English word
                while i < len && (chars[i].is_ascii_alphabetic() || chars[i].is_ascii_digit()) {
                    i += 1;
                }
                continue;
            }

            // Skip extraneous ASCII noise like URL colons or slashes
            if c == ':' || c == '/' || c == '>' || c == '<' || c == '|' {
                i += 1;
                continue;
            }

            out.push(c);
            i += 1;
        }

        let trimmed = out.trim();
        if !trimmed.chars().any(Self::is_japanese) {
            return String::new();
        }

        Self::clean_cjk_spaces(trimmed)
    }

    fn is_japanese(c: char) -> bool {
        matches!(c,
            '\u{3040}'..='\u{309F}' | // Hiragana
            '\u{30A0}'..='\u{30FF}' | // Katakana (includes choonpu 'ー' at \u{30FC})
            '\u{4E00}'..='\u{9FFF}'   // Kanji
        )
    }

    fn clean_cjk_spaces(text: &str) -> String {
        let mut out = String::with_capacity(text.len());
        let chars: Vec<char> = text.chars().collect();
        for i in 0..chars.len() {
            if chars[i] == ' ' {
                let prev_cjk = i > 0 && Self::is_cjk(chars[i - 1]);
                let next_cjk = i + 1 < chars.len() && Self::is_cjk(chars[i + 1]);
                if prev_cjk && next_cjk {
                    continue; // Skip space between two CJK glyphs
                }
            }
            out.push(chars[i]);
        }
        out
    }

    fn is_cjk(c: char) -> bool {
        matches!(c,
            '\u{3040}'..='\u{309F}' | // Hiragana
            '\u{30A0}'..='\u{30FF}' | // Katakana
            '\u{4E00}'..='\u{9FFF}' | // Kanji
            '\u{3000}'..='\u{303F}'   // CJK punctuation
        )
    }
}
