# 🔬 Scientific Python & Digital Image Processing Journey

Welcome to this hands-on roadmap. This repository is a curated collection of step-by-step implementations, focusing on **Scientific Computing**, **Data Visualization**, and **Digital Image Processing (DIP)** from the ground up.

The core philosophy of this journey is to master the "Matrix Mindset": treating everything (especially images) as numerical arrays and leveraging vectorization to build efficient, research-grade algorithms.

---

## 🎯 Learning Objectives
- **Vectorization over Loops:** Mastering `NumPy` to eliminate slow Python for-loops in mathematical operations.
- **Visual Analytics:** Crafting publication-ready plots and scientific figures using `Matplotlib`.
- **DIP from Scratch:** Understanding digital images as matrices and implementing spatial transformations without relying solely on high-level black-box libraries.
- **Reproducible Research:** Providing clean, well-commented code that follows academic and engineering best practices.

---

## 📂 Repository Roadmap

### 1. NumPy Foundations (`/01_numpy_basics`)
*The engine of scientific computing.*
- **Vectorized Arithmetic:** Element-wise operations and scalar broadcasting.
- **Boolean Masking:** Conditional indexing and intensity thresholding.
- **Multidimensional Analysis:** Understanding `axes` (0 vs 1), slicing, and matrix reshaping.
- **Key Files:** `01_arithmetic.py`, `02_masking.py`, `03_matrices_and_axes.py`.

### 2. Scientific Visualization (`/02_matplotlib_visualization`)
*Communicating data through logic and aesthetics.*
- **Function Sampling:** Generating continuous domains with `np.linspace`.
- **Trigonometric Modeling:** Visualizing $\sin(x)$ and $\cos(x)$ with customized styles, LaTeX labels, and legends.
- **Key Files:** `01_trigonometric_plots.py`.

### 3. Image Processing Fundamentals (`/03_image_processing_fundamentals`)
*Bridging the gap between Linear Algebra and Computer Vision.*
- **Synthetic Image Generation:** Creating grayscale gradients and geometric primitives using NumPy.
- **Point Operations:** Implementing the **Negative Transformation** ($I_{neg} = 255 - I$) and intensity scaling.
- **Spatial Slicing:** Manually constructing masks and shapes within 2D/3D arrays.
- **Key Files:** `01_shapes_and_negative.py`.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Hoomansarabi/python-scientific-journey.git
cd python-scientific-journey
