# src/weight/calibration.py

class CameraCalibration:
    """
    Placeholder for camera calibration.
    In real systems, this converts pixel area to real-world units.
    """

    def __init__(self, scale_factor: float = 1.0):
        self.scale_factor = scale_factor

    def apply(self, area: float) -> float:
        """
        Apply calibration scale (if available)
        """
        return area * self.scale_factor
