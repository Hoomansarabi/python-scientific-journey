"""
01_vectorization_and_operations.py
NumPy array operations and broadcasting with scalars.
"""
import numpy as np

# 1. Array creation and scalar addition (Broadcasting)
scores = np.array([14, 16.5, 18])
updated_scores = scores + 1.5

print("Original Scores:", scores)
print("Updated Scores (+1.5):", updated_scores)
