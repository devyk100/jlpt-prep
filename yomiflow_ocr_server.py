"""
YomiFlow Local Neural Scene OCR Server (MeikiOCR Engine)
Provides ultra-low latency, zero-copy Japanese subtitle & game dialogue recognition.
"""
import os
import sys
import time
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import cv2
import numpy as np
import onnxruntime as ort

DET_PATH_960 = "models/meiki.text.detect.v0.1.960x544.onnx"
DET_PATH_320 = "models/meiki.text.detect.v0.1.320x192.onnx"
REC_PATH = "models/meiki.text.rec.v0.960x32.onnx"

PORT = 8766

print("==========================================================")
print("  YomiFlow Neural OCR Server (MeikiOCR Game Engine)      ")
print("==========================================================")

# Configure session options for high throughput
so = ort.SessionOptions()
so.intra_op_num_threads = min(8, os.cpu_count() or 4)
so.inter_op_num_threads = 1
so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL

# Try DML first, fallback to CPU
providers = ['CPUExecutionProvider']

det_path = DET_PATH_960 if os.path.exists(DET_PATH_960) else DET_PATH_320
print(f"[OCR Server] Loading detector: {det_path}...")
det_session = ort.InferenceSession(det_path, so, providers=providers)

print(f"[OCR Server] Loading recognizer: {REC_PATH}...")
rec_session = ort.InferenceSession(REC_PATH, so, providers=providers)

# Warmup both models
dummy_det = np.zeros((1, 3, 544, 960), dtype=np.float32)
dummy_sizes = np.array([[960, 544]], dtype=np.int64)
det_session.run(None, {'images': dummy_det, 'orig_target_sizes': dummy_sizes})

dummy_rec = np.zeros((1, 3, 32, 960), dtype=np.float32)
dummy_rec_sizes = np.array([[960, 32]], dtype=np.int64)
rec_session.run(None, {'images': dummy_rec, 'orig_target_sizes': dummy_rec_sizes})

print("[OCR Server] Engine warmed up and resident in memory!")

def run_ocr(image_bytes: bytes):
    t_start = time.perf_counter()
    
    # Decode image from memory
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        return {"error": "Failed to decode image bytes", "text": "", "lines": []}
    
    h_orig, w_orig = img.shape[:2]
    if h_orig < 8 or w_orig < 8:
        return {"text": "", "lines": [], "latency_ms": 0.0}
    
    # --- 1. Detection ---
    t0_det = time.perf_counter()
    resized_det = cv2.resize(img, (960, 544), interpolation=cv2.INTER_LINEAR)
    img_norm = resized_det.astype(np.float32) / 255.0
    img_trans = np.transpose(img_norm, (2, 0, 1))
    img_tensor = np.expand_dims(img_trans, axis=0)
    sizes_tensor = np.array([[960, 544]], dtype=np.int64)
    
    labels, boxes, scores = det_session.run(None, {
        'images': img_tensor,
        'orig_target_sizes': sizes_tensor
    })
    det_ms = (time.perf_counter() - t0_det) * 1000.0
    
    ratio_w = 960.0 / w_orig
    ratio_h = 544.0 / h_orig
    
    line_boxes = []
    for box, score in zip(boxes[0], scores[0]):
        if score > 0.35:
            x_min, y_min, x_max, y_max = box
            fx1 = max(0, int(x_min / ratio_w) - 4)
            fy1 = max(0, int(y_min / ratio_h) - 4)
            fx2 = min(w_orig, int(x_max / ratio_w) + 4)
            fy2 = min(h_orig, int(y_max / ratio_h) + 4)
            line_boxes.append((fx1, fy1, fx2, fy2, float(score)))
    
    # Sort detected lines vertically (reading order)
    line_boxes.sort(key=lambda b: b[1])
    
    if not line_boxes:
        # Fallback: whole image if no distinct boxes were found but image is subtitle-sized
        if h_orig <= 120 and w_orig >= 200:
            line_boxes.append((0, 0, w_orig, h_orig, 0.5))
        else:
            return {
                "text": "",
                "lines": [],
                "det_ms": round(det_ms, 2),
                "rec_ms": 0.0,
                "total_ms": round((time.perf_counter() - t_start) * 1000.0, 2)
            }
    
    # --- 2. Batched Line Recognition ---
    t0_rec = time.perf_counter()
    batch_tensors = []
    crops_info = []
    
    for fx1, fy1, fx2, fy2, score in line_boxes:
        crop = img[fy1:fy2, fx1:fx2]
        ch, cw = crop.shape[:2]
        if ch < 4 or cw < 4:
            continue
        
        new_w = min(960, max(1, int(round(cw * (32.0 / ch)))))
        resized_line = cv2.resize(crop, (new_w, 32), interpolation=cv2.INTER_LINEAR)
        pad_w = 960 - new_w
        padded = np.pad(resized_line, ((0, 0), (0, pad_w), (0, 0)), constant_values=0)
        line_t = (np.transpose(padded, (2, 0, 1)).astype(np.float32)) / 255.0
        
        batch_tensors.append(line_t)
        crops_info.append((fx1, fy1, fx2, fy2, score))
    
    if not batch_tensors:
        return {"text": "", "lines": [], "total_ms": round((time.perf_counter() - t_start) * 1000.0, 2)}
    
    batch_np = np.stack(batch_tensors, axis=0) # [N, 3, 32, 960]
    batch_sizes = np.array([[960, 32]] * len(batch_tensors), dtype=np.int64)
    
    r_labels, r_boxes, r_scores = rec_session.run(None, {
        'images': batch_np,
        'orig_target_sizes': batch_sizes
    })
    rec_ms = (time.perf_counter() - t0_rec) * 1000.0
    
    parsed_lines = []
    for idx, (fx1, fy1, fx2, fy2, line_score) in enumerate(crops_info):
        labels_i = r_labels[idx]
        boxes_i = r_boxes[idx]
        scores_i = r_scores[idx]
        
        candidates = []
        for lbl, box, scr in zip(labels_i, boxes_i, scores_i):
            if scr < 0.15:
                continue
            candidates.append({
                'char': chr(lbl),
                'x1': box[0],
                'x2': box[2],
                'conf': float(scr)
            })
        
        # Deduplicate overlapping characters
        candidates.sort(key=lambda c: c['conf'], reverse=True)
        accepted = []
        for cand in candidates:
            keep = True
            for acc in accepted:
                overlap = max(0, min(cand['x2'], acc['x2']) - max(cand['x1'], acc['x1']))
                w = cand['x2'] - cand['x1'] + 1e-6
                if overlap / w > 0.3:
                    keep = False
                    break
            if keep:
                accepted.append(cand)
        
        # Sort left-to-right
        accepted.sort(key=lambda c: c['x1'])
        line_text = "".join(c['char'] for c in accepted).strip()
        
        if line_text:
            parsed_lines.append({
                "text": line_text,
                "box": [fx1, fy1, fx2, fy2],
                "confidence": round(line_score, 3)
            })
    
    full_text = "\n".join(l["text"] for l in parsed_lines)
    total_ms = (time.perf_counter() - t_start) * 1000.0
    
    return {
        "text": full_text,
        "lines": parsed_lines,
        "det_ms": round(det_ms, 2),
        "rec_ms": round(rec_ms, 2),
        "total_ms": round(total_ms, 2)
    }

class OCRHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"ready","engine":"MeikiOCR"}')
        else:
            self.send_response(404)
            self.end_headers()
            
    def do_POST(self):
        if self.path == "/ocr":
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            
            result = run_ocr(body)
            resp_bytes = json.dumps(result, ensure_ascii=False).encode('utf-8')
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(resp_bytes)))
            self.end_headers()
            self.wfile.write(resp_bytes)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Silence per-request terminal logs for maximum speed
        pass

def run_server():
    server = HTTPServer(('127.0.0.1', PORT), OCRHandler)
    print(f"[OCR Server] Listening on http://127.0.0.1:{PORT}/ocr")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("[OCR Server] Stopping...")
        server.server_close()

if __name__ == "__main__":
    run_server()

