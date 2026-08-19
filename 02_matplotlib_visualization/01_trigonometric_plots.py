"""
01_trigonometric_plots.py
Visualizing sine and cosine waves with Matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y_sin, color="blue", label=r"$y = \sin(x)$")
plt.plot(x, y_cos, color="green", linestyle="--", label=r"$y = \cos(x)$")

plt.title("Trigonometric Functions: Sine vs Cosine")
plt.xlabel("Angle (radians)")
plt.ylabel("Amplitude")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
