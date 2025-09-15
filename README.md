# NumPy Learning Repository

This repository contains Python scripts (`main.py` and `main2.py`) that demonstrate fundamental and advanced concepts of **NumPy** — a powerful library for numerical computing in Python.  

---

## 📂 Files in This Repository

### 1. **main.py**
Covers the **basics of NumPy**:
- Creating arrays
- Dimensions (`ndim`) and shapes (`shape`)
- Chain indexing vs multidimensional indexing
- String and numeric arrays
- Slicing (rows, columns, and both combined)
- Arithmetic operations (scalar, element-wise, and vectorized math functions)
- Comparison operators and conditional assignment
- Exercises like forming words from array slices and calculating circle areas with radii

---

### 2. **main2.py**
Focuses on **intermediate to advanced NumPy features**:
- **Broadcasting**: Performing operations on arrays of different shapes
- **Aggregate functions**: 
  - `sum`, `mean`, `std`, `var`, `min`, `max`
  - `argmin`, `argmax`
  - Axis-wise operations
- **Filtering**:
  - Using boolean masks (`ages[ages < 18]`)
  - Combining conditions with `&` (AND), `|` (OR)
  - Preserving dimensions with `np.where`
- **Random number generation**:
  - `integers`, `uniform`
  - Using seeds for reproducibility
  - Shuffling arrays
  - Random choices from a list (with emojis 🍎🍊🍌🥥🍍)

---

## ⚙️ Requirements
- Python 3.x
- [NumPy](https://numpy.org/)  
Install with:
```bash
pip install numpy
