# src/utils/draw.py
import cv2

def draw_boxes(frame, tracks, weights, count):
    """
    Draw bounding boxes, IDs, weight proxy, and count on frame

    tracks: dict {id: box}
    weights: dict {id: weight_index}
    """
    for tid, box in tracks.items():
        x1, y1, x2, y2 = map(int, box)
        weight = weights.get(tid, 0)

        # Bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # ID + Weight text
        label = f"ID {tid} | W {weight}"
        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

    # Total count
    cv2.putText(
        frame,
        f"Count: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (0, 0, 255),
        2
    )

    return frame
