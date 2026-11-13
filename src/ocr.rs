use image::RgbaImage;
use serde::Deserialize;
use std::io::Cursor;
use std::time::Instant;
use windows::core::{HSTRING, Result as WinResult};
use windows::Globalization::Language;
use windows::Graphics::Imaging::BitmapDecoder;
use windows::Media::Ocr::OcrEngine;
use windows::Storage::Streams::{DataWriter, InMemoryRandomAccessStream};

#[derive(Deserialize)]
struct NeuralOcrResponse {
    text: String,
    lines: Vec<NeuralLine>,
    #[allow(dead_code)]
    total_ms: Option<f64>,
}

#[derive(Deserialize)]
struct NeuralLine {
    text: String,
    #[allow(dead_code)]
    box_coords: Option<Vec<i32>>,
    #[allow(dead_code)]
    confidence: Option<f64>,
}

pub struct NativeOcrEngine {
    windows_engine: Option<OcrEngine>,
    neural_endpoint: String,
}

unsafe impl Send for NativeOcrEngine {}
unsafe impl Sync for NativeOcrEngine {}

impl NativeOcrEngine {
    pub fn new() -> Self {
        let neural_endpoint = "http://127.0.0.1:8766".to_string();

        // 1. Check if MeikiOCR neural daemon is alive, or start it
        Self::ensure_neural_daemon_running(&neural_endpoint);

        // 2. Initialize fallback Windows Media OCR
        let windows_engine = match Self::init_windows_engine() {
            Ok(e) => {
                println!("[OCR] Windows Media OCR fallback initialized successfully!");
                Some(e)
            }
            Err(err) => {
                eprintln!("[OCR] Windows Media OCR fallback unavailable: {:?}", err);
                None
            }
        };

        Self {
            windows_engine,
            neural_endpoint,
        }
    }

    fn ensure_neural_daemon_running(endpoint: &str) {
        let health_url = format!("{}/health", endpoint);
        let is_running = ureq::get(&health_url)
            .call()
            .map(|resp| resp.status() == 200)
            .unwrap_or(false);

        if !is_running {
            println!("[OCR] Spawning MeikiOCR neural server in background...");
            let _ = std::process::Command::new("python")
                .arg("yomiflow_ocr_server.py")
                .spawn();
        } else {
            println!("[OCR] MeikiOCR neural server is active and ready on {}!", endpoint);
        }
    }

    fn init_windows_engine() -> WinResult<OcrEngine> {
        let lang = Language::CreateLanguage(&HSTRING::from("ja"))?;
        let engine = OcrEngine::TryCreateFromLanguage(&lang)?;
        Ok(engine)
    }

    pub fn recognize(&self, img: &RgbaImage) -> (String, Vec<String>, f64) {
        let t0 = Instant::now();

        let mut png_bytes = Vec::new();
        if let Err(e) = img.write_to(&mut Cursor::new(&mut png_bytes), image::ImageFormat::Png) {
            eprintln!("[OCR] PNG encode error: {}", e);
        } else {
            // Attempt 1: High-Speed Game-Tuned Neural OCR (MeikiOCR Engine)
            if let Some((neural_text, lines, server_ms)) = self.try_neural_ocr(&png_bytes) {
                if !neural_text.trim().is_empty() {
                    let total_ms = t0.elapsed().as_secs_f64() * 1000.0;
                    println!(
                        "[OCR] Neural MeikiOCR Transcribed: {:?} (server: {:.1}ms, roundtrip: {:.1}ms)",
                        neural_text, server_ms, total_ms
                    );
                    return (neural_text, lines, total_ms);
                }
            }
        }

        // Attempt 2: Fallback to Windows Media OCR with subtitle binarization
        if let Some(ref engine) = self.windows_engine {
            let preprocessed = Self::preprocess_for_subtitles(img);
            let mut png_bytes = Vec::new();
            if let Ok(()) = preprocessed.write_to(&mut Cursor::new(&mut png_bytes), image::ImageFormat::Png) {
                if let Ok((text, lines)) = self.recognize_bytes(engine, &png_bytes) {
                    if !text.trim().is_empty() {
                        let ms = t0.elapsed().as_secs_f64() * 1000.0;
                        return (text, lines, ms);
                    }
                }
            }

            // Attempt 3: Windows Media OCR on raw image
            let mut raw_png = Vec::new();
            if let Ok(()) = img.write_to(&mut Cursor::new(&mut raw_png), image::ImageFormat::Png) {
                if let Ok((text, lines)) = self.recognize_bytes(engine, &raw_png) {
                    let ms = t0.elapsed().as_secs_f64() * 1000.0;
                    return (text, lines, ms);
                }
            }
        }

        ("".to_string(), vec![], t0.elapsed().as_secs_f64() * 1000.0)
    }

    fn try_neural_ocr(&self, img_bytes: &[u8]) -> Option<(String, Vec<String>, f64)> {
        let ocr_url = format!("{}/ocr", self.neural_endpoint);
        let resp = ureq::post(&ocr_url)
            .header("Content-Type", "image/png")
            .send(img_bytes)
            .ok()?;

        let result: NeuralOcrResponse = resp.into_body().read_json().ok()?;
        if result.text.trim().is_empty() {
            return None;
        }

        let lines: Vec<String> = result
            .lines
            .into_iter()
            .map(|l| l.text)
            .filter(|t| !t.trim().is_empty())
            .collect();

        Some((result.text, lines, result.total_ms.unwrap_or(0.0)))
    }

    /// Subtitle Preprocessing for Anime & Games with dynamic backgrounds
    pub fn preprocess_for_subtitles(img: &RgbaImage) -> RgbaImage {
        let (w, h) = (img.width(), img.height());
        // Scale 2x for optimal Japanese character radical resolution
        let scaled = image::imageops::resize(img, w * 2, h * 2, image::imageops::FilterType::Triangle);

        let mut binarized = scaled.clone();
        for p in binarized.pixels_mut() {
            let lum = 0.299 * p[0] as f32 + 0.587 * p[1] as f32 + 0.114 * p[2] as f32;
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
        let has_kanji_or_hira = text.chars().any(|c| {
            matches!(c, '\u{3040}'..='\u{309F}' | '\u{4E00}'..='\u{9FFF}')
        });
        if has_kanji_or_hira {
            return true;
        }

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
                    continue;
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
    fn test_user_jojo_image_neural() {
        let path = "C:/Users/devyk/.gemini/antigravity/brain/9bfedc6b-8c95-415b-a025-4b7628d5be10/.user_uploaded/media_1794547671450_cdc282d5.jpg";
        let img = image::open(path).expect("Failed to open image");
        let rgba = img.to_rgba8();
        let engine = NativeOcrEngine::new();
        let (text, lines, ms) = engine.recognize(&rgba);
        println!("Neural Recognized in {:.1}ms:\n{}", ms, text);
        println!("Lines: {:?}", lines);
        assert!(text.contains("家族より俺との友情を") || text.contains("家族"));
    }
}
