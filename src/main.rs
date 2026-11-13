mod ai;
mod capture;
mod config;
mod dictionary;
mod history;
mod hotkeys;
mod ocr;
mod tokenizer;
mod ui;

use capture::init_dpi;
use eframe::egui::{Pos2, Vec2, ViewportBuilder};
use ui::YomiFlowApp;

fn main() -> eframe::Result<()> {
    // 1. Initialize High-DPI awareness on Windows
    init_dpi();

    println!("========================================================");
    println!("   YomiFlow — Universal Japanese Immersion Assistant   ");
    println!("   100% Native Rust • Zero Stutter • Direct Win32 GDI  ");
    println!("========================================================");

    let config = config::AppConfig::load();
    let initial_w = 640.0;
    let initial_h = 180.0;
    let initial_x = config.window_x.unwrap_or(100.0);
    let initial_y = config.window_y.unwrap_or(100.0);

    let native_options = eframe::NativeOptions {
        viewport: ViewportBuilder::default()
            .with_title("YomiFlow")
            .with_inner_size(Vec2::new(initial_w, initial_h))
            .with_position(Pos2::new(initial_x, initial_y))
            .with_decorations(false)
            .with_transparent(true)
            .with_always_on_top()
            .with_resizable(true),
        ..Default::default()
    };

    eframe::run_native(
        "YomiFlow",
        native_options,
        Box::new(|cc| Ok(Box::new(YomiFlowApp::new(cc)))),
    )
}
