use image::RgbaImage;
use serde::{Deserialize, Serialize};
use std::fs::{create_dir_all, OpenOptions};
use std::io::{Cursor, Write};
use std::path::Path;
use std::time::SystemTime;

#[derive(Serialize)]
struct AnkiRequest<T> {
    action: &'static str,
    version: u32,
    params: T,
}

#[derive(Serialize)]
struct CanAddNotesParams {
    notes: Vec<CanAddNoteItem>,
}

#[derive(Serialize)]
struct CanAddNoteItem {
    #[serde(rename = "deckName")]
    deck_name: String,
    #[serde(rename = "modelName")]
    model_name: String,
    fields: std::collections::HashMap<String, String>,
}

#[derive(Serialize)]
struct StoreMediaFileParams {
    filename: String,
    data: String, // base64
}

#[derive(Serialize)]
struct AddNoteParams {
    note: AddNoteItem,
}

#[derive(Serialize)]
struct AddNoteItem {
    #[serde(rename = "deckName")]
    deck_name: String,
    #[serde(rename = "modelName")]
    model_name: String,
    fields: std::collections::HashMap<String, String>,
    options: AddNoteOptions,
    tags: Vec<String>,
}

#[derive(Serialize)]
struct AddNoteOptions {
    #[serde(rename = "allowDuplicate")]
    allow_duplicate: bool,
}

#[derive(Deserialize)]
struct AnkiResponse<T> {
    result: Option<T>,
    error: Option<String>,
}

pub struct AnkiClient {
    pub endpoint: String,
    pub deck_name: String,
    pub model_name: String,
}

impl AnkiClient {
    pub fn new() -> Self {
        Self {
            endpoint: "http://127.0.0.1:8765".to_string(),
            deck_name: "Japanese".to_string(),
            model_name: "Basic".to_string(),
        }
    }

    /// 1-Click Sentence Mining to Anki with automatic media storage and fallback
    pub fn export_card(
        &self,
        sentence: &str,
        word: &str,
        reading: &str,
        definition: &str,
        translation: &str,
        source: &str,
        screenshot: Option<&RgbaImage>,
    ) -> Result<String, String> {
        let ts = SystemTime::now()
            .duration_since(SystemTime::UNIX_EPOCH)
            .map(|d| d.as_secs())
            .unwrap_or(0);
        let filename = format!("yomiflow_{}.png", ts);

        // Encode image to PNG bytes if present
        let mut png_bytes = Vec::new();
        if let Some(img) = screenshot {
            let _ = img.write_to(&mut Cursor::new(&mut png_bytes), image::ImageFormat::Png);
        }

        let vocab_field = if !reading.is_empty() {
            format!("{} 【{}】<br>{}", word, reading, definition)
        } else {
            format!("{}<br>{}", word, definition)
        };

        let sanitized_source = source.replace(' ', "_");
        let img_tag = if !png_bytes.is_empty() {
            format!("<img src=\"{}\">", filename)
        } else {
            String::new()
        };

        // Try AnkiConnect HTTP v6 first
        match self.try_ankiconnect_sync(
            sentence,
            &vocab_field,
            translation,
            &img_tag,
            &filename,
            &png_bytes,
            &sanitized_source,
        ) {
            Ok(note_id) => Ok(format!("Synced note to Anki [ID: {}]", note_id)),
            Err(ankiconnect_err) => {
                // AnkiConnect offline or failed -> Divert seamlessly to TSV fallback
                self.export_to_tsv_fallback(
                    sentence,
                    &vocab_field,
                    translation,
                    &img_tag,
                    &filename,
                    &png_bytes,
                    &sanitized_source,
                )?;
                Ok(format!(
                    "AnkiConnect offline ({}); Saved locally to yomiflow_anki_export.txt",
                    ankiconnect_err
                ))
            }
        }
    }

    fn try_ankiconnect_sync(
        &self,
        sentence: &str,
        vocab: &str,
        translation: &str,
        img_tag: &str,
        filename: &str,
        png_bytes: &[u8],
        source: &str,
    ) -> Result<u64, String> {
        use base64::Engine;

        // Step 1: Pre-flight check via canAddNotes
        let mut check_fields = std::collections::HashMap::new();
        check_fields.insert("Front".to_string(), sentence.to_string());
        check_fields.insert("Back".to_string(), vocab.to_string());

        let check_req = AnkiRequest {
            action: "canAddNotes",
            version: 6,
            params: CanAddNotesParams {
                notes: vec![CanAddNoteItem {
                    deck_name: self.deck_name.clone(),
                    model_name: self.model_name.clone(),
                    fields: check_fields,
                }],
            },
        };

        let resp = ureq::post(&self.endpoint)
            .send_json(&check_req)
            .map_err(|e| format!("HTTP request error: {}", e))?;

        let check_res: AnkiResponse<Vec<bool>> = resp
            .into_body()
            .read_json()
            .map_err(|e| format!("JSON parse error: {}", e))?;

        if let Some(err) = check_res.error {
            return Err(format!("AnkiConnect error: {}", err));
        }

        // Step 2: Upload media screenshot via storeMediaFile
        if !png_bytes.is_empty() {
            let b64_img = base64::engine::general_purpose::STANDARD.encode(png_bytes);
            let media_req = AnkiRequest {
                action: "storeMediaFile",
                version: 6,
                params: StoreMediaFileParams {
                    filename: filename.to_string(),
                    data: b64_img,
                },
            };

            let _ = ureq::post(&self.endpoint).send_json(&media_req);
        }

        // Step 3: Add Note via addNote
        let mut fields = std::collections::HashMap::new();
        fields.insert("Front".to_string(), sentence.to_string());
        fields.insert(
            "Back".to_string(),
            format!("{}<br><br><i>{}</i><br><br>{}", vocab, translation, img_tag),
        );
        // Also support 5-field immersion models if present
        fields.insert("Sentence".to_string(), sentence.to_string());
        fields.insert("Vocabulary".to_string(), vocab.to_string());
        fields.insert("Translation".to_string(), translation.to_string());
        fields.insert("Screenshot".to_string(), img_tag.to_string());
        fields.insert("Source".to_string(), source.to_string());

        let add_req = AnkiRequest {
            action: "addNote",
            version: 6,
            params: AddNoteParams {
                note: AddNoteItem {
                    deck_name: self.deck_name.clone(),
                    model_name: self.model_name.clone(),
                    fields,
                    options: AddNoteOptions {
                        allow_duplicate: true,
                    },
                    tags: vec!["YomiFlow".to_string(), source.to_string()],
                },
            },
        };

        let add_resp = ureq::post(&self.endpoint)
            .send_json(&add_req)
            .map_err(|e| format!("addNote failed: {}", e))?;

        let add_res: AnkiResponse<u64> = add_resp
            .into_body()
            .read_json()
            .map_err(|e| format!("addNote response error: {}", e))?;

        if let Some(err) = add_res.error {
            return Err(format!("addNote rejected: {}", err));
        }

        Ok(add_res.result.unwrap_or(0))
    }

    fn export_to_tsv_fallback(
        &self,
        sentence: &str,
        vocab: &str,
        translation: &str,
        img_tag: &str,
        filename: &str,
        png_bytes: &[u8],
        source: &str,
    ) -> Result<(), String> {
        // Save image to ./exports/media/
        let export_dir = Path::new("exports/media");
        create_dir_all(export_dir).map_err(|e| e.to_string())?;

        if !png_bytes.is_empty() {
            let img_path = export_dir.join(filename);
            let mut f = std::fs::File::create(&img_path).map_err(|e| e.to_string())?;
            f.write_all(png_bytes).map_err(|e| e.to_string())?;
        }

        // Append line to yomiflow_anki_export.txt
        let mut file = OpenOptions::new()
            .create(true)
            .append(true)
            .open("yomiflow_anki_export.txt")
            .map_err(|e| e.to_string())?;

        let clean_sentence = sentence.replace('\t', " ").replace('\n', " ");
        let clean_vocab = vocab.replace('\t', " ").replace('\n', " ");
        let clean_trans = translation.replace('\t', " ").replace('\n', " ");

        writeln!(
            file,
            "{}\t{}\t{}\t{}\t{}",
            clean_sentence, clean_vocab, clean_trans, img_tag, source
        )
        .map_err(|e| e.to_string())?;

        Ok(())
    }
}

