Here is the full content for your `README.md` file, ready to be copied and saved. You can manually create a file named `README.md` in your project root and paste the code block below directly into it to complete your submission.

```markdown
# Bird Counting and Weight Estimation from Poultry CCTV Video

## Overview
This project implements a prototype system that processes a fixed-camera poultry CCTV video to:
1. Count birds over time using object detection and stable tracking IDs.
2. Estimate bird weight using a relative weight proxy derived from video.

The solution is exposed via a minimal FastAPI service as required.

---

## Setup Instructions

### 1. Python Environment
- Python version: **3.10**

Create and activate a virtual environment (recommended):

```bash
py -3.10 -m venv venv
venv\Scripts\activate

```

Install dependencies:

```bash
pip install -r requirements.txt

```

### 2. Model

Place the trained YOLO model at:

```
models/best.pt

```

### 3. (Optional) Create Test Video

If a CCTV video is not provided, generate a test video from dataset images:

```bash
py -3.10 scripts/images_to_video.py

```

This will generate: `sample_chicken_video.mp4`

---

## Running the API

Start the FastAPI service from the project root:

```bash
py -3.10 -m uvicorn api.main:app --reload

```

The API will be available at: `http://127.0.0.1:8000`

Swagger UI (for testing): `http://127.0.0.1:8000/docs`

---

## API Endpoints

### GET /health

Health check endpoint.
Response:

```json
{ "status": "ok" }

```

### POST /analyze_video

Upload a poultry CCTV video to perform bird counting and weight estimation.

**curl Example**

```bash
curl -X POST "[http://127.0.0.1:8000/analyze_video](http://127.0.0.1:8000/analyze_video)" \
     -F "file=@sample_chicken_video.mp4"

```

**Response (Example)**

```json
{
  "counts": {
    "0": 12,
    "1": 12,
    "2": 13
  },
  "weight_unit": "relative_weight_index",
  "artifacts": {
    "annotated_video": "outputs/videos/annotated_output.mp4"
  }
}

```

## Output Artifacts

Annotated video with bounding boxes, tracking IDs, bird count, and weight proxy:
`outputs/videos/annotated_output.mp4`

```

