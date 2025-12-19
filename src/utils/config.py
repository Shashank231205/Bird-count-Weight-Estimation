# src/utils/config.py
import os

# Absolute path to project root
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

# Absolute path to YOLO model
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "best.pt")

# Detection parameters
CONF_THRESHOLD = 0.25
IOU_THRESHOLD = 0.4
