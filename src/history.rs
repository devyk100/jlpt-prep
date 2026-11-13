use serde::{Deserialize, Serialize};
use std::fs::{create_dir_all, OpenOptions};
use std::io::Write;
use std::path::Path;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HistoryEntry {
    pub timestamp: String,
    pub original: String,
    pub translation: String,
    pub tokens: Vec<String>,
}

pub struct HistoryManager {
    log_path: String,
}

impl HistoryManager {
    pub fn new() -> Self {
        Self {
            log_path: "history.jsonl".to_string(),
        }
    }

    pub fn append(&self, entry: &HistoryEntry) {
        if let Ok(json_line) = serde_json::to_string(entry) {
            if let Ok(mut file) = OpenOptions::new()
                .create(true)
                .append(true)
                .open(&self.log_path)
            {
                let _ = writeln!(file, "{}", json_line);
            }
        }
    }

    pub fn export_anki_tsv(&self, output_path: &str) -> std::io::Result<usize> {
        if let Some(parent) = Path::new(output_path).parent() {
            let _ = create_dir_all(parent);
        }

        let content = std::fs::read_to_string(&self.log_path).unwrap_or_default();
        let mut count = 0;
        let mut tsv_out = String::new();

        // Anki TSV format: Front (Japanese) \t Back (Translation & Vocab) \t Tags
        for line in content.lines() {
            if let Ok(entry) = serde_json::from_str::<HistoryEntry>(line) {
                let front = entry.original.replace('\t', " ").replace('\n', " ");
                let back = if entry.translation.is_empty() {
                    format!("Tokens: {}", entry.tokens.join(" | "))
                } else {
                    format!("{}<br><br>Tokens: {}", entry.translation, entry.tokens.join(" | "))
                };
                let tags = "YomiFlow Immersion";
                tsv_out.push_str(&format!("{}\t{}\t{}\n", front, back, tags));
                count += 1;
            }
        }

        let mut file = OpenOptions::new()
            .create(true)
            .write(true)
            .truncate(true)
            .open(output_path)?;
        file.write_all(tsv_out.as_bytes())?;

        Ok(count)
    }
}

