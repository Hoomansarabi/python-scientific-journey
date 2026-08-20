from pathlib import Path
import cv2

image_path = Path(__file__).parent / "image.png"

print("مسیر تصویر:")
print(image_path.resolve())

image = cv2.imread(str(image_path))

if image is None:
    print("تصویر پیدا نشد")
else:
    print("تصویر با موفقیت خوانده شد")
    print("اندازه تصویر:", image.shape)

    cv2.imshow("My Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
