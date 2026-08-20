import numpy as np
import matplotlib.pyplot as plt


image = np.array([
    [20, 40, 60, 80],
    [90, 110, 130, 150],
    [160, 180, 200, 220],
    [30, 70, 170, 250]
])

threshold = np.mean(image)

binary_image = np.where(image >= threshold, 255, 0)

print("میانگین تصویر:", threshold)
print("تصویر دودویی:")
print(binary_image)
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(binary_image, cmap="gray")
plt.title(f"Binary Image - T = {threshold:.2f}")
plt.axis("off")

plt.show()

