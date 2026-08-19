"""
03_matrices_and_axes.py
2D array manipulation and reductions along axes.
"""
import numpy as np

# Sales data: 3 products across 4 seasons
sales = np.array([
    [100, 120, 130, 110],
    [80, 95, 110, 105],
    [200, 210, 190, 220]
])

# Sum along rows (each product's annual total)
total_per_product = np.sum(sales, axis=1)

# Max along columns (peak sales per season)
max_per_season = np.max(sales, axis=0)

print("Total sales per product (axis=1):", total_per_product)
print("Max sales per season (axis=0):", max_per_season)
