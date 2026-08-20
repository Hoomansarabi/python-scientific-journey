from pathlib import Path

import cv2
import matplotlib.pyplot as plt

image_path = Path(__file__).parent / "image.png"

image_bgr = cv2.imread(str(image_path))

if image_bgr is None:
    print("تصویر پیدا نشد")
else:
    print("تصویر با موفقیت خوانده شد")

    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_bgr)
plt.title("Wrong Colors: BGR")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(image_rgb)
plt.title("Correct Colors: RGB")
plt.axis("off")

plt.tight_layout()
plt.show()

