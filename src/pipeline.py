# src/pipeline.py

import os
import cv2

from src.detection.detector import BirdDetector
from src.detection.tracker import SimpleTracker
from src.weight.weight_proxy import estimate_weight_proxy
from src.utils.video_io import open_video, create_writer
from src.utils.draw import draw_boxes
from src.utils.config import MODEL_PATH


def process_video(video_path: str):
    """
    Full pipeline:
    Video → Detection → Tracking → Counting → Weight Estimation
    """

    detector = BirdDetector(MODEL_PATH)
    tracker = SimpleTracker()

    cap = open_video(video_path)

    # Output video setup
    output_dir = os.path.join("outputs", "videos")
    os.makedirs(output_dir, exist_ok=True)
    output_video_path = os.path.join(output_dir, "annotated_output.mp4")
    writer = create_writer(cap, output_video_path)

    frame_idx = 0
    counts_over_time = {}
    frame_results = {}

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 1. Detect birds
        boxes, _ = detector.detect(frame)

        # 2. Track birds (stable IDs)
        tracks = tracker.update(list(boxes))

        # 3. Count birds
        counts_over_time[frame_idx] = len(tracks)

        # 4. Weight estimation (proxy)
        weights = {}      # 🔥 MUST be defined BEFORE use
        birds = []

        for tid, box in tracks.items():
            w = estimate_weight_proxy(box)
            weights[tid] = w
            birds.append({
                "id": tid,
                "weight_index": w
            })

        frame_results[frame_idx] = {
            "count": len(tracks),
            "birds": birds
        }

        # 5. Draw annotations (ID + WEIGHT + COUNT)
        annotated_frame = draw_boxes(
            frame,
            tracks,
            weights,
            len(tracks)
        )

        writer.write(annotated_frame)
        frame_idx += 1

    cap.release()
    writer.release()

    return frame_results, counts_over_time
