"""
01_shapes_and_negative.py
Digital image representation as a 2D NumPy array, spatial slicing, and negative transform.
"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Create a 200x200 black canvas (zeros)
img = np.zeros((200, 200), dtype=np.uint8)

# 2. Draw two white squares using spatial slicing
img[20:70, 20:70] = 255      # Top-left square
img[120:170, 120:170] = 255  # Bottom-right square

# 3. Compute negative transformation: I_neg = 255 - I
img_negative = 255 - img

# 4. Plot both side by side
fig, axes = plt.subplots(1, 2, figsize=(8, 4))

axes[0].imshow(img, cmap="gray")
axes[0].set_title("Original Image (Two Squares)")
axes[0].axis("off")

axes[1].imshow(img_negative, cmap="gray")
axes[1].set_title("Negative Transformation")
axes[1].axis("off")

plt.tight_layout()
plt.show()
