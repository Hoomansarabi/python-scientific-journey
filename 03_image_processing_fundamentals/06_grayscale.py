from pathlib import Path

import cv2
import matplotlib.pyplot as plt

image_path = Path(__file__).parent / "image.png"

image_bgr = cv2.imread(str(image_path))

if image_bgr is None:
    print("تصویر پیدا نشد")
else:
    print("تصویر با موفقیت خوانده شد")

    image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    print("Shape تصویر رنگی:", image_bgr.shape)
    print("Shape تصویر خاکستری:", image_gray.shape)

    # یک پیکسل نمونه
    pixel_gray = image_gray[100, 200]
    pixel_bgr = image_bgr[100, 200]

    print("مقدار پیکسل خاکستری:", pixel_gray)
    print("نوع دادهٔ پیکسل:", pixel_gray.dtype)
    print("مقدار پیکسل رنگی به صورت BGR:", pixel_bgr)

    # یک ناحیه (ROI)
    roi_bgr = image_bgr[50:150, 100:250]
    roi_gray = image_gray[50:150, 100:250]

    print("Shape ناحیه رنگی:", roi_bgr.shape)
    print("Shape ناحیه خاکستری:", roi_gray.shape)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB))
    plt.title("Color Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(image_gray, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(roi_bgr, cv2.COLOR_BGR2RGB))
    plt.title("ROI")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
