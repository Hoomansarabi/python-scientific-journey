"""
02_boolean_masking.py
Conditional filtering using Boolean Masks.
"""
import numpy as np

temperatures = np.array([25, 32, 18, 40, 29, 38])

# Filter temperatures greater than 30
high_temps = temperatures[temperatures > 30]

print("All Temperatures:", temperatures)
print("Temperatures > 30°C:", high_temps)
