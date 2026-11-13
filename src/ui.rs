use crate::ai::{AiExplanation, FallbackAiClient};
use crate::capture::{capture_screen_region, get_screen_dimensions};
use crate::config::AppConfig;
use crate::dictionary::{GrammarNote, LocalDictionary};
use crate::history::{HistoryEntry, HistoryManager};
use crate::hotkeys::{HotKeyEvent, HotkeyManager};
use crate::ocr::NativeOcrEngine;
use crate::tokenizer::{tokenize_japanese, JapaneseToken};
use eframe::egui::{
    self, Align, Color32, CornerRadius, Layout, RichText, Sense, Stroke, Vec2, ViewportCommand,
};
use std::sync::{Arc, Mutex};
use std::thread;

#[derive(Clone)]
pub struct CaptureResult {
    pub text: String,
    #[allow(dead_code)]
    pub lines: Vec<String>,
    pub tokens: Vec<JapaneseToken>,
    pub grammar: Vec<GrammarNote>,
    #[allow(dead_code)]
    pub capture_ms: f64,
    #[allow(dead_code)]
    pub ocr_ms: f64,
    pub total_ms: f64,
}

pub struct YomiFlowApp {
    pub config: AppConfig,
    pub hotkeys: HotkeyManager,
    pub ocr: Arc<NativeOcrEngine>,
    pub dict: Arc<LocalDictionary>,
    pub history: Arc<HistoryManager>,
    pub latest_result: Arc<Mutex<Option<CaptureResult>>>,
    pub ai_explanation: Arc<Mutex<Option<Result<AiExplanation, String>>>>,
    pub is_capturing: Arc<Mutex<bool>>,
    pub is_requesting_ai: Arc<Mutex<bool>>,

    // UI state
    pub is_expanded: bool,
    pub show_region_settings: bool,
    #[allow(dead_code)]
    pub show_ai_settings: bool,
    pub status_message: String,
}

impl YomiFlowApp {
    pub fn new(cc: &eframe::CreationContext<'_>) -> Self {
        let fonts = egui::FontDefinitions::default();
        cc.egui_ctx.set_fonts(fonts);

        let config = AppConfig::load();
        let hotkeys = HotkeyManager::new();
        let ocr = Arc::new(NativeOcrEngine::new());
        let dict = Arc::new(LocalDictionary::new());
        let history = Arc::new(HistoryManager::new());
        let latest_result = Arc::new(Mutex::new(None));
        let ai_explanation = Arc::new(Mutex::new(None));
        let is_capturing = Arc::new(Mutex::new(false));
        let is_requesting_ai = Arc::new(Mutex::new(false));

        Self {
            config,
            hotkeys,
            ocr,
            dict,
            history,
            latest_result,
            ai_explanation,
            is_capturing,
            is_requesting_ai,
            is_expanded: false,
            show_region_settings: false,
            show_ai_settings: false,
            status_message: "Press F8 to capture dialogue".to_string(),
        }
    }

    pub fn trigger_capture(&self, ctx: egui::Context) {
        let is_cap = self.is_capturing.clone();
        {
            let mut busy = is_cap.lock().unwrap();
            if *busy {
                return;
            }
            *busy = true;
        }

        // Reset AI explanation for new sentence
        *self.ai_explanation.lock().unwrap() = None;

        let region = self.config.region.clone();
        let ocr = self.ocr.clone();
        let dict = self.dict.clone();
        let history = self.history.clone();
        let result_store = self.latest_result.clone();

        thread::spawn(move || {
            match capture_screen_region(&region) {
                Ok((img, cap_ms)) => {
                    let (text, lines, ocr_ms) = ocr.recognize(&img);
                    let tokens = tokenize_japanese(&text);
                    let grammar = dict.detect_grammar(&text);
                    let total_ms = cap_ms + ocr_ms;

                    // Automatically record to persistent history
                    if !text.trim().is_empty() {
                        let token_surfaces: Vec<String> = tokens
                            .iter()
                            .filter(|t| !t.is_punct)
                            .map(|t| t.surface.clone())
                            .collect();

                        let entry = HistoryEntry {
                            timestamp: chrono_now_string(),
                            original: text.clone(),
                            translation: String::new(),
                            tokens: token_surfaces,
                        };
                        history.append(&entry);
                    }

                    let res = CaptureResult {
                        text,
                        lines,
                        tokens,
                        grammar,
                        capture_ms: cap_ms,
                        ocr_ms,
                        total_ms,
                    };

                    *result_store.lock().unwrap() = Some(res);
                }
                Err(err) => {
                    eprintln!("[Capture Error] {}", err);
                }
            }

            *is_cap.lock().unwrap() = false;
            ctx.request_repaint();
        });
    }

    pub fn trigger_ai_explanation(&self, ctx: egui::Context, text: String) {
        let is_req = self.is_requesting_ai.clone();
        {
            let mut busy = is_req.lock().unwrap();
            if *busy {
                return;
            }
            *busy = true;
        }

        let ai_store = self.ai_explanation.clone();
        let mut client = FallbackAiClient::new(self.config.deepseek_api_key.clone());
        client.endpoint = self.config.deepseek_endpoint.clone();
        client.model = self.config.deepseek_model.clone();

        thread::spawn(move || {
            let res = client.explain(&text);
            *ai_store.lock().unwrap() = Some(res);
            *is_req.lock().unwrap() = false;
            ctx.request_repaint();
        });
    }
}

fn chrono_now_string() -> String {
    // Lightweight timestamp without heavy external date crates
    format!("captured_{}", std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).map(|d| d.as_secs()).unwrap_or(0))
}

impl eframe::App for YomiFlowApp {
    fn clear_color(&self, _visuals: &egui::Visuals) -> [f32; 4] {
        [0.0, 0.0, 0.0, 0.0]
    }

    fn ui(&mut self, ui: &mut egui::Ui, _frame: &mut eframe::Frame) {
        let ctx = ui.ctx().clone();

        // Continuous Always-On-Top enforcement in egui and OS DWM
        crate::capture::force_window_topmost("YomiFlow");
        ctx.send_viewport_cmd(ViewportCommand::WindowLevel(egui::WindowLevel::AlwaysOnTop));

        // 1. Process Hotkey Events
        while let Ok(evt) = self.hotkeys.receiver.try_recv() {
            match evt {
                HotKeyEvent::Capture => {
                    self.trigger_capture(ctx.clone());
                }
                HotKeyEvent::ToggleVisibility => {
                    ctx.send_viewport_cmd(ViewportCommand::Visible(true));
                    ctx.send_viewport_cmd(ViewportCommand::WindowLevel(egui::WindowLevel::AlwaysOnTop));
                    crate::capture::force_window_topmost("YomiFlow");
                }
                HotKeyEvent::ToggleMode => {
                    self.is_expanded = !self.is_expanded;
                    let target_h = if self.is_expanded { 520.0 } else { 180.0 };
                    ctx.send_viewport_cmd(ViewportCommand::InnerSize(Vec2::new(640.0, target_h)));
                }
                HotKeyEvent::Dismiss => {
                    ctx.send_viewport_cmd(ViewportCommand::Minimized(true));
                }
            }
        }

        // Handle Escape to minimize when overlay is focused
        if ui.input(|i| i.key_pressed(egui::Key::Escape)) {
            ctx.send_viewport_cmd(ViewportCommand::Minimized(true));
        }

        let is_capturing_now = *self.is_capturing.lock().unwrap();
        let is_ai_running = *self.is_requesting_ai.lock().unwrap();
        let current_res = self.latest_result.lock().unwrap().clone();
        let current_ai = self.ai_explanation.lock().unwrap().clone();

        // 2. Translucent Glassmorphism Frame
        let alpha = (self.config.opacity.clamp(0.4, 1.0) * 255.0) as u8;
        let bg_color = Color32::from_rgba_premultiplied(16, 16, 24, alpha);
        let border_stroke = Stroke::new(1.0, Color32::from_rgba_premultiplied(255, 255, 255, 38));

        let panel_frame = egui::Frame::new()
            .fill(bg_color)
            .stroke(border_stroke)
            .corner_radius(CornerRadius::same(12))
            .inner_margin(egui::Margin::same(10));

        panel_frame.show(ui, |ui| {
            // === HEADER BAR (Draggable) ===
            ui.horizontal(|ui| {
                // 1. Dedicated Drag Handle Button
                let drag_btn = ui.add(
                    egui::Button::new(
                        RichText::new("⠿ Move")
                            .size(11.0)
                            .strong()
                            .color(Color32::from_rgb(230, 230, 245)),
                    )
                    .fill(Color32::from_rgba_premultiplied(255, 255, 255, 30))
                    .stroke(Stroke::new(1.0, Color32::from_rgba_premultiplied(255, 255, 255, 60)))
                    .sense(Sense::click_and_drag()),
                );
                if drag_btn.is_pointer_button_down_on() || drag_btn.drag_started() || drag_btn.dragged() {
                    ctx.send_viewport_cmd(ViewportCommand::StartDrag);
                }

                // 2. Interactive Title Labels (also draggable)
                let title_lbl = ui.add(
                    egui::Label::new(
                        RichText::new("⚡ YomiFlow").strong().color(Color32::from_rgb(244, 63, 94))
                    )
                    .sense(Sense::click_and_drag())
                );
                if title_lbl.is_pointer_button_down_on() || title_lbl.drag_started() || title_lbl.dragged() {
                    ctx.send_viewport_cmd(ViewportCommand::StartDrag);
                }

                let sub_lbl = ui.add(
                    egui::Label::new(
                        RichText::new("読みフロー").size(11.0).color(Color32::from_rgb(150, 150, 160))
                    )
                    .sense(Sense::click_and_drag())
                );
                if sub_lbl.is_pointer_button_down_on() || sub_lbl.drag_started() || sub_lbl.dragged() {
                    ctx.send_viewport_cmd(ViewportCommand::StartDrag);
                }

                // Performance Latency Badge
                if let Some(ref res) = current_res {
                    let badge_text = format!("{:.1}ms", res.total_ms);
                    ui.label(
                        RichText::new(badge_text)
                            .size(10.5)
                            .color(Color32::from_rgb(110, 231, 183)),
                    );
                } else if is_capturing_now {
                    ui.label(
                        RichText::new("Scanning...")
                            .size(11.0)
                            .color(Color32::from_rgb(252, 211, 77)),
                    );
                }

                // 3. Middle empty space as drag area
                let remaining_w = (ui.available_width() - 250.0).max(10.0);
                let (_, empty_drag) = ui.allocate_exact_size(Vec2::new(remaining_w, 22.0), Sense::click_and_drag());
                if empty_drag.is_pointer_button_down_on() || empty_drag.drag_started() || empty_drag.dragged() {
                    ctx.send_viewport_cmd(ViewportCommand::StartDrag);
                }

                ui.with_layout(Layout::right_to_left(Align::Center), |ui| {
                    // Minimize button
                    if ui.button(RichText::new("🗕").size(12.0)).on_hover_text("Minimize Overlay (Esc)").clicked() {
                        ctx.send_viewport_cmd(ViewportCommand::Minimized(true));
                    }

                    // Mode Toggle (F10)
                    let mode_lbl = if self.is_expanded { "▲ Compact" } else { "▼ Expand" };
                    if ui.button(RichText::new(mode_lbl).size(11.0)).on_hover_text("Toggle Breakdown (F10)").clicked() {
                        self.is_expanded = !self.is_expanded;
                        let target_h = if self.is_expanded { 520.0 } else { 180.0 };
                        ctx.send_viewport_cmd(ViewportCommand::InnerSize(Vec2::new(640.0, target_h)));
                    }

                    // Settings buttons
                    let reg_lbl = if self.show_region_settings { "Close Region" } else { "⚙ Region" };
                    if ui.button(RichText::new(reg_lbl).size(11.0)).clicked() {
                        self.show_region_settings = !self.show_region_settings;
                        if self.show_region_settings && !self.is_expanded {
                            self.is_expanded = true;
                            ctx.send_viewport_cmd(ViewportCommand::InnerSize(Vec2::new(640.0, 520.0)));
                        }
                    }

                    // Capture button (F8)
                    let btn_cap = ui.button(
                        RichText::new("📷 Capture (F8)")
                            .color(Color32::WHITE)
                            .strong()
                            .size(11.0),
                    );
                    if btn_cap.clicked() {
                        self.trigger_capture(ctx.clone());
                    }
                });
            });

            ui.add_space(6.0);
            ui.separator();
            ui.add_space(4.0);

            // === MAIN CONTENT ===
            if let Some(ref res) = current_res {
                if res.text.trim().is_empty() {
                    ui.vertical_centered(|ui| {
                        ui.label(RichText::new("No Japanese dialogue text found in capture region.").color(Color32::GRAY));
                        ui.label(RichText::new("Adjust capture region if needed with the ⚙ Region button.").size(11.0).color(Color32::DARK_GRAY));
                    });
                } else {
                    // Display Recognized Japanese Sentence with interactive tokens
                    ui.horizontal_wrapped(|ui| {
                        for token in &res.tokens {
                            if token.is_punct {
                                ui.label(RichText::new(&token.surface).size(16.0).color(Color32::from_rgb(180, 180, 190)));
                            } else if token.has_kanji {
                                let kanji_chip = ui.add(
                                    egui::Label::new(
                                        RichText::new(&token.surface)
                                            .size(16.0)
                                            .strong()
                                            .color(Color32::from_rgb(255, 230, 235)),
                                    )
                                    .sense(Sense::click()),
                                );
                                if kanji_chip.hovered() {
                                    // Quick tooltip showing kanji breakdown
                                    let mut tip = format!("Word: {}", token.surface);
                                    if let Some(w) = self.dict.lookup_word(&token.surface) {
                                        tip.push_str(&format!(" [{}]: {}", w.reading, w.meaning));
                                    }
                                    kanji_chip.on_hover_text(tip);
                                }
                            } else {
                                ui.label(RichText::new(&token.surface).size(16.0).color(Color32::WHITE));
                            }
                        }
                    });

                    // Quick action bar
                    ui.add_space(4.0);
                    ui.horizontal(|ui| {
                        if ui.button(RichText::new("📋 Copy").size(10.5)).clicked() {
                            ui.ctx().copy_text(res.text.clone());
                            self.status_message = "Copied to clipboard!".to_string();
                        }

                        if ui.button(RichText::new("⭐ Export Anki").size(10.5)).clicked() {
                            match self.history.export_anki_tsv("yomiflow_anki_export.txt") {
                                Ok(n) => self.status_message = format!("Exported {} cards to yomiflow_anki_export.txt", n),
                                Err(e) => self.status_message = format!("Export error: {}", e),
                            }
                        }

                        // Fallback AI button
                        let ai_lbl = if is_ai_running { "🤖 Analyzing..." } else { "🤖 AI Nuance" };
                        let btn_ai = ui.button(RichText::new(ai_lbl).size(10.5).color(Color32::from_rgb(147, 197, 253)));
                        if btn_ai.clicked() && !is_ai_running {
                            if !self.is_expanded {
                                self.is_expanded = true;
                                ctx.send_viewport_cmd(ViewportCommand::InnerSize(Vec2::new(620.0, 520.0)));
                            }
                            self.trigger_ai_explanation(ctx.clone(), res.text.clone());
                        }

                        let non_punct_count = res.tokens.iter().filter(|t| !t.is_punct).count();
                        ui.label(
                            RichText::new(format!("{} words", non_punct_count))
                                .size(10.5)
                                .color(Color32::GRAY),
                        );

                        if !self.status_message.is_empty() {
                            ui.label(RichText::new(&self.status_message).size(10.5).color(Color32::from_rgb(252, 211, 77)));
                        }
                    });
                }
            } else {
                ui.vertical_centered(|ui| {
                    ui.add_space(15.0);
                    ui.label(RichText::new("🎮 Ready to capture Japanese text.").strong().color(Color32::from_rgb(220, 220, 230)));
                    ui.label(RichText::new("Press F8 anywhere in your game to recognize dialogue instantly.").size(12.0).color(Color32::GRAY));
                    ui.add_space(10.0);
                });
            }

            // === EXPANDED VIEW / REGION CONFIG ===
            if self.is_expanded {
                ui.add_space(8.0);
                ui.separator();
                ui.add_space(6.0);

                if self.show_region_settings {
                    ui.label(RichText::new("Capture Region & Settings").strong().color(Color32::from_rgb(244, 63, 94)));
                    ui.add_space(4.0);

                    ui.horizontal(|ui| {
                        ui.label("Preset:");
                        if ui.button("Bottom Subtitles (1080p)").clicked() {
                            self.config.region = crate::config::CaptureRegion { x: 200, y: 720, width: 1520, height: 280 };
                            self.config.save();
                        }
                        if ui.button("Persona 5 Royal").clicked() {
                            self.config.region = crate::config::CaptureRegion { x: 350, y: 700, width: 1220, height: 260 };
                            self.config.save();
                        }
                        if ui.button("Fullscreen").clicked() {
                            let (sw, sh) = get_screen_dimensions();
                            self.config.region = crate::config::CaptureRegion { x: 0, y: 0, width: sw, height: sh };
                            self.config.save();
                        }
                    });

                    ui.add_space(4.0);
                    ui.horizontal(|ui| {
                        ui.label("X:");
                        ui.add(egui::DragValue::new(&mut self.config.region.x).speed(5));
                        ui.label("Y:");
                        ui.add(egui::DragValue::new(&mut self.config.region.y).speed(5));
                        ui.label("Width:");
                        ui.add(egui::DragValue::new(&mut self.config.region.width).speed(5).range(100..=3840));
                        ui.label("Height:");
                        ui.add(egui::DragValue::new(&mut self.config.region.height).speed(5).range(50..=2160));
                    });

                    ui.add_space(4.0);
                    ui.horizontal(|ui| {
                        ui.label("Overlay Opacity:");
                        if ui.add(egui::Slider::new(&mut self.config.opacity, 0.4..=1.0)).changed() {
                            self.config.save();
                        }
                    });

                    ui.add_space(4.0);
                    ui.horizontal(|ui| {
                        ui.label("Snap Window:");
                        if ui.button("📍 Top Left").clicked() {
                            ctx.send_viewport_cmd(ViewportCommand::OuterPosition(egui::Pos2::new(100.0, 80.0)));
                            self.config.window_x = Some(100.0);
                            self.config.window_y = Some(80.0);
                            self.config.save();
                        }
                        if ui.button("📍 Top Center").clicked() {
                            ctx.send_viewport_cmd(ViewportCommand::OuterPosition(egui::Pos2::new(450.0, 80.0)));
                            self.config.window_x = Some(450.0);
                            self.config.window_y = Some(80.0);
                            self.config.save();
                        }
                        if ui.button("📍 Center").clicked() {
                            ctx.send_viewport_cmd(ViewportCommand::OuterPosition(egui::Pos2::new(450.0, 260.0)));
                            self.config.window_x = Some(450.0);
                            self.config.window_y = Some(260.0);
                            self.config.save();
                        }
                        if ui.button("📍 Bottom Subtitles").clicked() {
                            ctx.send_viewport_cmd(ViewportCommand::OuterPosition(egui::Pos2::new(350.0, 520.0)));
                            self.config.window_x = Some(350.0);
                            self.config.window_y = Some(520.0);
                            self.config.save();
                        }
                    });

                    ui.add_space(6.0);
                    ui.separator();
                    ui.add_space(4.0);

                    ui.label(RichText::new("DeepSeek / OpenAI API Key (Optional Fallback):").strong().size(11.0));
                    ui.horizontal(|ui| {
                        ui.add(egui::TextEdit::singleline(&mut self.config.deepseek_api_key).password(true).hint_text("sk-...")).on_hover_text("Stored locally in config.json");
                        if ui.button("💾 Save Settings").clicked() {
                            self.config.save();
                            self.show_region_settings = false;
                        }
                    });
                } else if let Some(ref res) = current_res {
                    egui::ScrollArea::vertical().max_height(280.0).show(ui, |ui| {
                        // 1. AI Explanation (if available or requested)
                        if let Some(ref ai_res) = current_ai {
                            match ai_res {
                                Ok(expl) => {
                                    ui.group(|ui| {
                                        ui.horizontal(|ui| {
                                            ui.label(RichText::new("🤖 AI Linguistic Breakdown").strong().color(Color32::from_rgb(147, 197, 253)));
                                        });
                                        ui.add_space(2.0);
                                        ui.label(RichText::new(format!("Translation: \"{}\"", expl.translation)).strong().size(13.0).color(Color32::WHITE));
                                        if !expl.nuance.is_empty() {
                                            ui.label(RichText::new(format!("Nuance: {}", expl.nuance)).size(11.5).color(Color32::from_rgb(253, 224, 71)));
                                        }
                                        if !expl.grammar.is_empty() {
                                            ui.label(RichText::new(format!("Grammar: {}", expl.grammar)).size(11.5).color(Color32::from_rgb(167, 243, 208)));
                                        }
                                    });
                                    ui.add_space(6.0);
                                }
                                Err(err) => {
                                    ui.label(RichText::new(format!("AI Error: {}", err)).color(Color32::from_rgb(248, 113, 113)).size(11.5));
                                    ui.add_space(4.0);
                                }
                            }
                        }

                        // 2. Grammar Patterns
                        if !res.grammar.is_empty() {
                            ui.label(RichText::new("Detected Grammar & Sentence Patterns").strong().color(Color32::from_rgb(167, 139, 250)));
                            ui.add_space(2.0);
                            for g in &res.grammar {
                                ui.horizontal(|ui| {
                                    ui.label(RichText::new(g.pattern).strong().color(Color32::from_rgb(216, 180, 254)));
                                    ui.label(RichText::new(format!("— {}", g.meaning)).color(Color32::WHITE).size(12.0));
                                });
                                ui.label(RichText::new(g.explanation).size(11.0).color(Color32::GRAY));
                                ui.add_space(2.0);
                            }
                            ui.add_space(4.0);
                            ui.separator();
                            ui.add_space(4.0);
                        }

                        // 3. Vocabulary & Kanji Decomposition
                        ui.label(RichText::new("Local Vocabulary & Kanji Breakdown").strong().color(Color32::from_rgb(244, 63, 94)));
                        ui.add_space(4.0);

                        for token in &res.tokens {
                            if token.is_punct {
                                continue;
                            }
                            ui.horizontal(|ui| {
                                ui.label(RichText::new(&token.surface).strong().size(13.5).color(Color32::WHITE));

                                // Look up in local word dictionary
                                if let Some(w) = self.dict.lookup_word(&token.surface) {
                                    ui.label(RichText::new(format!("[{}]", w.reading)).size(12.0).color(Color32::from_rgb(252, 211, 77)));
                                    ui.label(RichText::new(w.meaning).size(12.0).color(Color32::from_rgb(229, 231, 235)));
                                }

                                // Kanji component decomposition
                                if token.has_kanji {
                                    for &k_char in &token.kanji {
                                        if let Some(k_info) = self.dict.lookup_kanji(k_char) {
                                            ui.label(
                                                RichText::new(format!("{} ({}): {}", k_info.character, k_info.onyomi, k_info.meaning))
                                                    .size(11.0)
                                                    .color(Color32::from_rgb(251, 146, 60)),
                                            );
                                        }
                                    }
                                }
                            });
                            ui.separator();
                        }
                    });
                }
            }
        });
    }
}
