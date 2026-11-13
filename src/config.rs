use serde::{Deserialize, Serialize};
use std::fs;
use std::path::Path;

const CONFIG_PATH: &str = "config.json";

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CaptureRegion {
    pub x: i32,
    pub y: i32,
    pub width: i32,
    pub height: i32,
}

impl Default for CaptureRegion {
    fn default() -> Self {
        Self {
            x: 200,
            y: 720,
            width: 1520,
            height: 280,
        }
    }
}

fn default_endpoint() -> String {
    "https://api.deepseek.com/chat/completions".to_string()
}

fn default_model() -> String {
    "deepseek-chat".to_string()
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AppConfig {
    pub region: CaptureRegion,
    pub opacity: f32,
    pub compact: bool,
    pub always_on_top: bool,
    pub active_profile: String,
    #[serde(default)]
    pub deepseek_api_key: String,
    #[serde(default = "default_endpoint")]
    pub deepseek_endpoint: String,
    #[serde(default = "default_model")]
    pub deepseek_model: String,
}

impl Default for AppConfig {
    fn default() -> Self {
        Self {
            region: CaptureRegion::default(),
            opacity: 0.94,
            compact: true,
            always_on_top: true,
            active_profile: "Bottom Subtitles".to_string(),
            deepseek_api_key: String::new(),
            deepseek_endpoint: default_endpoint(),
            deepseek_model: default_model(),
        }
    }
}

impl AppConfig {
    pub fn load() -> Self {
        if Path::new(CONFIG_PATH).exists() {
            if let Ok(data) = fs::read_to_string(CONFIG_PATH) {
                if let Ok(cfg) = serde_json::from_str(&data) {
                    return cfg;
                }
            }
        }
        let cfg = Self::default();
        cfg.save();
        cfg
    }

    pub fn save(&self) {
        if let Ok(json) = serde_json::to_string_pretty(self) {
            let _ = fs::write(CONFIG_PATH, json);
        }
    }
}

