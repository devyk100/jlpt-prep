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

        let preprocessed = Self::preprocess_for_subtitles(img);
        // Try preprocessed subtitle image first
        let mut png_bytes = Vec::new();
        if let Ok(()) = preprocessed.write_to(&mut Cursor::new(&mut png_bytes), image::ImageFormat::Png) {
            if let Ok((text, lines)) = self.recognize_bytes(engine, &png_bytes) {
                if !text.trim().is_empty() {
                    let ms = t0.elapsed().as_secs_f64() * 1000.0;
                    return (text, lines, ms);
                }
            }
        }

        // Fallback to original image (for browser text, manga, dark on light)
        png_bytes.clear();
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

    /// Subtitle Preprocessing for Anime & Games with dynamic backgrounds
    pub fn preprocess_for_subtitles(img: &RgbaImage) -> RgbaImage {
        let (w, h) = (img.width(), img.height());
        // Scale 2x for optimal Japanese character radical resolution
        let scaled = image::imageops::resize(img, w * 2, h * 2, image::imageops::FilterType::Triangle);

        let mut binarized = scaled.clone();
        for p in binarized.pixels_mut() {
            let lum = 0.299 * p[0] as f32 + 0.587 * p[1] as f32 + 0.114 * p[2] as f32;
            // Subtitle text in anime and games is bright white/yellow
            if lum > 165.0 {
                *p = image::Rgba([0, 0, 0, 255]); // Crisp black text
            } else {
                *p = image::Rgba([255, 255, 255, 255]); // Pure white background
            }
        }
        binarized
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
            // Discard lines that do not contain genuine Japanese dialogue (e.g. English UI, website headers)
            if !Self::is_genuine_japanese_line(&line_text) {
                continue;
            }

            let cleaned = Self::clean_cjk_spaces(&line_text);
            if !cleaned.trim().is_empty() {
                lines.push(cleaned);
            }
        }

        let full_text = lines.join("\n");
        Ok((full_text, lines))
    }

    fn is_genuine_japanese_line(text: &str) -> bool {
        // Genuine Japanese lines contain Kanji or Hiragana
        let has_kanji_or_hira = text.chars().any(|c| {
            matches!(c, '\u{3040}'..='\u{309F}' | '\u{4E00}'..='\u{9FFF}')
        });
        if has_kanji_or_hira {
            return true;
        }

        // If only katakana, require at least 2 actual Katakana glyphs (excluding single stray dash/choonpu)
        let katakana_count = text
            .chars()
            .filter(|&c| matches!(c, '\u{30A1}'..='\u{30FA}'))
            .count();

        katakana_count >= 2
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_user_jojo_image() {
        let path = "C:/Users/devyk/.gemini/antigravity/brain/9bfedc6b-8c95-415b-a025-4b7628d5be10/.user_uploaded/media_1794547671450_cdc282d5.jpg";
        let img = image::open(path).expect("Failed to open image");
        let rgba = img.to_rgba8();
        let engine = NativeOcrEngine::new();
        let (text, lines, ms) = engine.recognize(&rgba);
        eprintln!("Recognized in {}ms:\n{}", ms, text);
        eprintln!("Lines: {:?}", lines);
        assert!(!lines.is_empty());
    }
}
