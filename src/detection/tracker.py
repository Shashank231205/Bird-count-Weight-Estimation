import numpy as np

def iou(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    inter = max(0, xB - xA) * max(0, yB - yA)
    areaA = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    areaB = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    union = areaA + areaB - inter + 1e-6

    return inter / union


class SimpleTracker:
    def __init__(self, iou_threshold=0.4):
        self.tracks = {}
        self.next_id = 0
        self.iou_threshold = iou_threshold

    def update(self, detections):
        updated = {}
        used = set()

        for tid, prev_box in self.tracks.items():
            best_iou, best_idx = 0, -1
            for i, box in enumerate(detections):
                if i in used:
                    continue
                score = iou(prev_box, box)
                if score > best_iou:
                    best_iou, best_idx = score, i

            if best_iou > self.iou_threshold:
                updated[tid] = detections[best_idx]
                used.add(best_idx)

        for i, box in enumerate(detections):
            if i not in used:
                updated[self.next_id] = box
                self.next_id += 1

        self.tracks = updated
        return self.tracks
