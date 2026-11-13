use crate::config::CaptureRegion;
use image::{Rgba, RgbaImage};
use std::ptr::null_mut;
use std::time::Instant;
use windows_sys::Win32::Graphics::Gdi::{
    BitBlt, CreateCompatibleBitmap, CreateCompatibleDC, DeleteDC, DeleteObject, GetDC, GetDIBits,
    ReleaseDC, SelectObject, BITMAPINFO, BITMAPINFOHEADER, BI_RGB, CAPTUREBLT, DIB_RGB_COLORS,
    SRCCOPY,
};
use windows_sys::Win32::UI::WindowsAndMessaging::{
    FindWindowW, GetSystemMetrics, SetProcessDPIAware, SetWindowPos, HWND_TOPMOST,
    SM_CXSCREEN, SM_CYSCREEN, SWP_NOACTIVATE, SWP_NOMOVE, SWP_NOSIZE,
};

pub fn init_dpi() {
    unsafe {
        SetProcessDPIAware();
    }
}

pub fn force_window_topmost(title: &str) {
    unsafe {
        let wide: Vec<u16> = title.encode_utf16().chain(std::iter::once(0)).collect();
        let hwnd = FindWindowW(std::ptr::null(), wide.as_ptr());
        if !hwnd.is_null() {
            SetWindowPos(
                hwnd,
                HWND_TOPMOST,
                0,
                0,
                0,
                0,
                SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE,
            );
        }
    }
}

pub fn get_screen_dimensions() -> (i32, i32) {
    unsafe {
        let w = GetSystemMetrics(SM_CXSCREEN);
        let h = GetSystemMetrics(SM_CYSCREEN);
        (w, h)
    }
}

pub fn capture_screen_region(region: &CaptureRegion) -> Result<(RgbaImage, f64), String> {
    let t0 = Instant::now();

    let (screen_w, screen_h) = get_screen_dimensions();
    let x = region.x.clamp(0, (screen_w - 1).max(0));
    let y = region.y.clamp(0, (screen_h - 1).max(0));
    let width = region.width.clamp(1, screen_w - x);
    let height = region.height.clamp(1, screen_h - y);

    unsafe {
        let hdc_screen = GetDC(null_mut());
        if hdc_screen.is_null() {
            return Err("Failed to get screen DC".into());
        }

        let hdc_mem = CreateCompatibleDC(hdc_screen);
        if hdc_mem.is_null() {
            ReleaseDC(null_mut(), hdc_screen);
            return Err("Failed to create compatible DC".into());
        }

        let hbm = CreateCompatibleBitmap(hdc_screen, width, height);
        if hbm.is_null() {
            DeleteDC(hdc_mem);
            ReleaseDC(null_mut(), hdc_screen);
            return Err("Failed to create compatible bitmap".into());
        }

        let old_hbm = SelectObject(hdc_mem, hbm);

        // SRCCOPY | CAPTUREBLT (0x40000000) captures translucent & layered game windows
        let rop = SRCCOPY | CAPTUREBLT;
        BitBlt(hdc_mem, 0, 0, width, height, hdc_screen, x, y, rop);

        let mut bmi: BITMAPINFO = std::mem::zeroed();
        bmi.bmiHeader.biSize = std::mem::size_of::<BITMAPINFOHEADER>() as u32;
        bmi.bmiHeader.biWidth = width;
        bmi.bmiHeader.biHeight = -height; // Top-down DIB
        bmi.bmiHeader.biPlanes = 1;
        bmi.bmiHeader.biBitCount = 32;
        bmi.bmiHeader.biCompression = BI_RGB;

        let mut raw_bytes: Vec<u8> = vec![0u8; (width * height * 4) as usize];

        let lines_copied = GetDIBits(
            hdc_mem,
            hbm,
            0,
            height as u32,
            raw_bytes.as_mut_ptr() as *mut _,
            &mut bmi,
            DIB_RGB_COLORS,
        );

        // Clean up GDI handles
        SelectObject(hdc_mem, old_hbm);
        DeleteObject(hbm);
        DeleteDC(hdc_mem);
        ReleaseDC(null_mut(), hdc_screen);

        if lines_copied == 0 {
            return Err("GetDIBits failed to copy bitmap".into());
        }

        // Convert BGRA bytes to RGBA image
        let mut img = RgbaImage::new(width as u32, height as u32);
        for y_idx in 0..height as u32 {
            for x_idx in 0..width as u32 {
                let offset = ((y_idx * width as u32 + x_idx) * 4) as usize;
                let b = raw_bytes[offset];
                let g = raw_bytes[offset + 1];
                let r = raw_bytes[offset + 2];
                let a = 255u8;
                img.put_pixel(x_idx, y_idx, Rgba([r, g, b, a]));
            }
        }

        let elapsed = t0.elapsed().as_secs_f64() * 1000.0;
        Ok((img, elapsed))
    }
}
