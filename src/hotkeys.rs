use std::ptr::null_mut;
use std::sync::mpsc::{channel, Receiver};
use std::thread;
use windows_sys::Win32::UI::Input::KeyboardAndMouse::{
    RegisterHotKey, UnregisterHotKey, MOD_NOREPEAT, VK_F10, VK_F8, VK_F9,
};
use windows_sys::Win32::UI::WindowsAndMessaging::{
    DispatchMessageW, GetMessageW, TranslateMessage, MSG, WM_HOTKEY,
};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum HotKeyEvent {
    Capture,
    ToggleVisibility,
    ToggleMode,
    #[allow(dead_code)]
    Dismiss,
}

pub struct HotkeyManager {
    pub receiver: Receiver<HotKeyEvent>,
}

impl HotkeyManager {
    pub fn new() -> Self {
        let (tx, rx) = channel::<HotKeyEvent>();

        thread::spawn(move || {
            unsafe {
                // RegisterHotKey does NOT intercept or hook normal keystrokes.
                // Windows dispatches WM_HOTKEY messages ONLY when the specific hotkey is pressed.
                const ID_F8: i32 = 1;
                const ID_F9: i32 = 2;
                const ID_F10: i32 = 3;

                let ok_f8 = RegisterHotKey(null_mut(), ID_F8, MOD_NOREPEAT, VK_F8 as u32);
                let ok_f9 = RegisterHotKey(null_mut(), ID_F9, MOD_NOREPEAT, VK_F9 as u32);
                let ok_f10 = RegisterHotKey(null_mut(), ID_F10, MOD_NOREPEAT, VK_F10 as u32);

                println!(
                    "[Hotkeys] Native Win32 RegisterHotKey: F8={}, F9={}, F10={}",
                    ok_f8 != 0,
                    ok_f9 != 0,
                    ok_f10 != 0
                );

                let mut msg: MSG = std::mem::zeroed();
                while GetMessageW(&mut msg, null_mut(), 0, 0) > 0 {
                    if msg.message == WM_HOTKEY {
                        let id = msg.wParam as i32;
                        let evt = match id {
                            ID_F8 => Some(HotKeyEvent::Capture),
                            ID_F9 => Some(HotKeyEvent::ToggleVisibility),
                            ID_F10 => Some(HotKeyEvent::ToggleMode),
                            _ => None,
                        };

                        if let Some(e) = evt {
                            let _ = tx.send(e);
                        }
                    }
                    TranslateMessage(&msg);
                    DispatchMessageW(&msg);
                }

                UnregisterHotKey(null_mut(), ID_F8);
                UnregisterHotKey(null_mut(), ID_F9);
                UnregisterHotKey(null_mut(), ID_F10);
            }
        });

        Self { receiver: rx }
    }
}
