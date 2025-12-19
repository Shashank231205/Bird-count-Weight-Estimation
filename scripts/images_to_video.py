import cv2
import os

IMG_DIR = r"data\chicken_detection\test\images"
OUT_VIDEO = "sample_chicken_video.mp4"
FPS = 2

images = sorted([
    img for img in os.listdir(IMG_DIR)
    if img.lower().endswith((".jpg", ".png", ".jpeg"))
])

assert len(images) > 0, f"No images found in {IMG_DIR}"

# Read first image to set video size
first_img = cv2.imread(os.path.join(IMG_DIR, images[0]))
height, width, _ = first_img.shape

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(OUT_VIDEO, fourcc, FPS, (width, height))

written = 0

for img_name in images[:300]:
    img_path = os.path.join(IMG_DIR, img_name)
    frame = cv2.imread(img_path)

    if frame is None:
        continue

    # 🔥 CRITICAL FIX: resize every frame
    frame = cv2.resize(frame, (width, height))

    writer.write(frame)
    written += 1

writer.release()
print(f"✅ Video created: {OUT_VIDEO} ({written} frames)")
