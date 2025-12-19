# Implementation Details

## Bird Counting Method (Detection + Tracking)

Birds are detected in each video frame using a pretrained YOLO object detection model, which outputs bounding boxes and confidence scores for each detected bird.

To avoid double-counting and ensure temporal consistency, a simple IoU-based tracking mechanism is applied:
- Detected bounding boxes in the current frame are matched with boxes from the previous frame using Intersection-over-Union (IoU).
- If the IoU between two boxes exceeds a threshold, the same tracking ID is retained.
- New IDs are assigned only when no suitable match is found.

This approach ensures:
- Stable tracking IDs across frames
- Accurate bird counts over time (timestamp → count)
- Reduced double-counting when birds move across frames

**Occlusions and ID switches**
- Short occlusions are handled by retaining track IDs when overlap resumes.
- ID switches are minimized by IoU matching and conservative ID assignment.
- The system is designed for fixed-camera poultry environments where bird motion is limited.

---

## Weight Estimation Approach

True bird weight ground truth is not available in the provided videos. Therefore, a **relative weight proxy (index)** is implemented.

### Weight Proxy
- For each tracked bird, the area of its bounding box is computed.
- This area is normalized to produce a relative weight index:


- Larger bounding boxes correspond to heavier birds in the same camera setup.

### Assumptions
- The camera is fixed.
- Birds are approximately at the same depth from the camera.
- Relative size changes correlate with relative weight differences.

### Conversion to Grams (Not Available)
To convert the relative weight index into absolute weight (grams), the following additional data would be required:
- Camera calibration parameters (pixel-to-centimeter mapping)
- Camera height and viewing angle
- Bird-to-camera distance estimation
- Labeled training data mapping visual size to actual bird weight

Until such calibration data is available, the system outputs a normalized weight index, which is clearly stated in the API response.

---

## Output Artifacts
- Annotated output video with bounding boxes, tracking IDs, bird count overlay, and weight index per bird
- JSON response containing bird counts over time and sample weight estimates
