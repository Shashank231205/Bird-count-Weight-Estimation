# src/weight/weight_proxy.py

from .calibration import CameraCalibration

_calibrator = CameraCalibration(scale_factor=1.0)

def estimate_weight_proxy(box):
    """
    Estimate relative bird weight using bounding box area.
    Returns a WEIGHT INDEX (not grams).
    """
    x1, y1, x2, y2 = box
    area = (x2 - x1) * (y2 - y1)

    calibrated_area = _calibrator.apply(area)
    weight_index = calibrated_area / 1000.0

    return round(weight_index, 2)
