# 🔬 Scientific Python & Image Processing Learning Journey

Welcome to my hands-on roadmap for mastering **Scientific Computing**, **Data Analysis**, and **Digital Image Processing** in Python from scratch.

This repository documents step-by-step practical implementations, theoretical concepts, and reproducible code exercises designed for researchers and engineers transitioning from basic Python to advanced scientific stacks.

---

## 🎯 Objectives
- Master vectorization and matrix manipulation using **NumPy** (without slow Python loops).
- Build publication-ready scientific visualizations with **Matplotlib**.
- Understand digital images as numerical matrices and implement spatial image processing algorithms from the ground up.
- Provide a clean, well-commented template for anyone who wants to follow along and practice.

---

## 📂 Repository Structure

### 1. NumPy Foundations (`/01_numpy_basics`)
- **Vectorized Arithmetic:** Element-wise addition, scalar scaling, and performance optimizations.
- **Boolean Masking & Filtering:** Conditional indexing and thresholding.
- **2D Matrices & Axes:** Multi-dimensional arrays, slicing (`matrix[row, col]`), and aggregations along dimensions (`axis=0` vs `axis=1`).

### 2. Scientific Visualization (`/02_matplotlib_visualization`)
- **Continuous Functions:** Sampling domains with `np.linspace` and rendering $y = x^2$.
- **Trigonometric Comparisons:** Multi-line plotting for $\sin(x)$ and $\cos(x)$ with customized styles, legends, and LaTeX labels.

### 3. Digital Image Processing Fundamentals (`/03_image_processing_fundamentals`)
- **Synthetic Gradients:** Constructing grayscale intensity gradients from scratch.
- **Spatial Matrix Slicing:** Generating geometric primitives (rectangles/masks) in 2D arrays.
- **Point Operations:** Inverting image intensity (Negative Transformation: $I_{neg} = 255 - I$).

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Hoomansarabi/python-scientific-journey.git
cd python-scientific-journey
