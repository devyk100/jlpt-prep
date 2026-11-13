import ctypes
from ctypes import wintypes
import time
import io
import base64
from PIL import Image

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Set Process DPI Awareness to Per-Monitor V2 where possible, fallback to System DPI
try:
    # DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 = -4
    ctypes.windll.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))
except Exception:
    try:
        user32.SetProcessDPIAware()
    except Exception:
        pass


class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ('biSize', wintypes.DWORD),
        ('biWidth', wintypes.LONG),
        ('biHeight', wintypes.LONG),
        ('biPlanes', wintypes.WORD),
        ('biBitCount', wintypes.WORD),
        ('biCompression', wintypes.DWORD),
        ('biSizeImage', wintypes.DWORD),
        ('biXPelsPerMeter', wintypes.LONG),
        ('biYPelsPerMeter', wintypes.LONG),
        ('biClrUsed', wintypes.DWORD),
        ('biClrImportant', wintypes.DWORD)
    ]


def get_screen_dimensions():
    """Returns (width, height) of the primary desktop display."""
    w = user32.GetSystemMetrics(0)  # SM_CXSCREEN
    h = user32.GetSystemMetrics(1)  # SM_CYSCREEN
    return w, h


def capture_screen_region(x: int, y: int, width: int, height: int) -> tuple[Image.Image, float]:
    """
    Captures a rectangular region of the desktop using high-performance Win32 GDI.
    Returns (PIL.Image.Image, elapsed_ms).
    Average latency: ~2-3 ms on Windows 11.
    """
    t0 = time.perf_counter()

    screen_w, screen_h = get_screen_dimensions()

    # Clamp coordinates to screen boundaries
    x = max(0, min(x, screen_w - 1))
    y = max(0, min(y, screen_h - 1))
    width = max(1, min(width, screen_w - x))
    height = max(1, min(height, screen_h - y))

    hdc_screen = user32.GetDC(0)
    hdc_mem = gdi32.CreateCompatibleDC(hdc_screen)
    hbm = gdi32.CreateCompatibleBitmap(hdc_screen, width, height)
    old_hbm = gdi32.SelectObject(hdc_mem, hbm)

    # SRCCOPY (0x00CC0020) | CAPTUREBLT (0x40000000)
    # CAPTUREBLT ensures translucent windows, layered windows, and games are accurately captured
    rop = 0x00CC0020 | 0x40000000
    gdi32.BitBlt(hdc_mem, 0, 0, width, height, hdc_screen, x, y, rop)

    bmi = BITMAPINFOHEADER()
    bmi.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    bmi.biWidth = width
    bmi.biHeight = -height  # Negative height specifies top-down DIB
    bmi.biPlanes = 1
    bmi.biBitCount = 32
    bmi.biCompression = 0  # BI_RGB

    buffer_size = width * height * 4
    buf = (ctypes.c_ubyte * buffer_size)()
    gdi32.GetDIBits(hdc_mem, hbm, 0, height, ctypes.byref(buf), ctypes.byref(bmi), 0)

    # Clean up Win32 GDI handles
    gdi32.SelectObject(hdc_mem, old_hbm)
    gdi32.DeleteObject(hbm)
    gdi32.DeleteDC(hdc_mem)
    user32.ReleaseDC(0, hdc_screen)

    # Convert raw BGRA buffer to RGB Image
    img = Image.frombuffer('RGBA', (width, height), bytes(buf), 'raw', 'BGRA', 0, 1).convert('RGB')
    elapsed_ms = (time.perf_counter() - t0) * 1000.0

    return img, elapsed_ms


def image_to_base64_data_uri(img: Image.Image, format="JPEG", quality=85) -> str:
    """Encodes PIL Image to base64 Data URI for rapid frontend preview."""
    buf = io.BytesIO()
    img.save(buf, format=format, quality=quality)
    encoded = base64.b64encode(buf.getvalue()).decode('ascii')
    return f"data:image/{format.lower()};base64,{encoded}"
