# api/main.py

from fastapi import FastAPI, UploadFile, File
import shutil
import os

from src.pipeline import process_video

app = FastAPI(
    title="Bird Counting & Weight Estimation API",
    version="1.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze_video")
async def analyze_video(file: UploadFile = File(...)):
    """
    Upload poultry CCTV video → get bird count over time & weight proxy
    """

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    frame_results, counts = process_video(temp_path)

    os.remove(temp_path)

    return {
        "total_frames": len(frame_results),
        "counts_over_time": counts,
        "sample_frames": dict(list(frame_results.items())[:5]),
        "weight_unit": "relative_area_index"
    }
