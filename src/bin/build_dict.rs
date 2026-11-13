use std::fs::File;
use std::io::{BufRead, BufReader, BufWriter, Write};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("Parsing JMdict_e into compact TSV dictionary...");
    let file = File::open("JMdict_e")?;
    let reader = BufReader::new(file);

    let out_file = File::create("yomiflow_dict.tsv")?;
    let mut writer = BufWriter::new(out_file);

    let mut in_entry = false;
    let mut kanji_list = Vec::new();
    let mut reading_list = Vec::new();
    let mut gloss_list = Vec::new();

    let mut entry_count = 0usize;

    for line_res in reader.lines() {
        let line = line_res?;
        let trimmed = line.trim();

        if trimmed == "<entry>" {
            in_entry = true;
            kanji_list.clear();
            reading_list.clear();
            gloss_list.clear();
            continue;
        }

        if trimmed == "</entry>" {
            in_entry = false;
            let primary_reading = reading_list.first().cloned().unwrap_or_default();
            let gloss = gloss_list.join("; ");

            if !gloss.is_empty() {
                // If kanji forms exist, map each kanji form
                if !kanji_list.is_empty() {
                    for k in &kanji_list {
                        writeln!(writer, "{}\t{}\t{}", k, primary_reading, gloss)?;
                        entry_count += 1;
                    }
                }
                // Also map reading form if kanji doesn't match reading
                for r in &reading_list {
                    if !kanji_list.contains(r) {
                        writeln!(writer, "{}\t{}\t{}", r, r, gloss)?;
                        entry_count += 1;
                    }
                }
            }
            continue;
        }

        if !in_entry {
            continue;
        }

        if let Some(keb) = extract_tag(trimmed, "keb") {
            kanji_list.push(keb.to_string());
        } else if let Some(reb) = extract_tag(trimmed, "reb") {
            reading_list.push(reb.to_string());
        } else if let Some(gloss) = extract_tag(trimmed, "gloss") {
            gloss_list.push(gloss.to_string());
        }
    }

    writer.flush()?;
    println!("Successfully built yomiflow_dict.tsv with {} entries!", entry_count);
    Ok(())
}

fn extract_tag<'a>(line: &'a str, tag: &str) -> Option<&'a str> {
    let open_tag = format!("<{}>", tag);
    let close_tag = format!("</{}>", tag);
    if let Some(start) = line.find(&open_tag) {
        let content_start = start + open_tag.len();
        if let Some(end) = line.find(&close_tag) {
            if end >= content_start {
                return Some(&line[content_start..end]);
            }
        }
    }
    None
}

