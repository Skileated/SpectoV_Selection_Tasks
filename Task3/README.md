# 📉 Task 3: Dimensionality Reduction using PCA and t-SNE

## 📌 Objective

This task explores dimensionality reduction techniques — **Principal Component Analysis (PCA)** and **t-distributed Stochastic Neighbor Embedding (t-SNE)** — to visualize high-dimensional datasets in 2D.

---

## 📊 Problem Statement

Given a high-dimensional dataset, the goals are to:

- Apply **PCA** to reduce dimensions while preserving variance.
- Apply **t-SNE** to cluster and visualize data structure.
- Compare the visualization effectiveness of PCA and t-SNE.
- Interpret how well clusters are separated in low dimensions.

---

## 🛠️ Technologies Used

- Python 3.8+
- `numpy`, `matplotlib`, `seaborn`
- `scikit-learn`

---

## 🔬 Techniques Overview

### 🔹 PCA (Principal Component Analysis)

- Linear dimensionality reduction technique.
- Projects data to a lower dimension by maximizing variance.
- Fast and effective for global structure preservation.

### 🔹 t-SNE (t-distributed Stochastic Neighbor Embedding)

- Nonlinear technique for visualization.
- Preserves local structure of data.
- Computationally heavier but effective for revealing clusters.

---

## 📁 Files Included
```text
Task3/
├── Task3.py      # Script to run PCA and t-SNE
├── PCA.png       # 2D scatter plot using PCA
├── t-SNE.png     # t-SNE output with default params
├── t-SNE_200.png # t-SNE with increased iterations
└── README.md     # This file
```

---

## 🖼️ Sample Output

| PCA | t-SNE | t-SNE (iter=200) |
|-----|-------|------------------|
| <img src="https://github.com/Skileated/SpectoV_Selection_Tasks/blob/0311789c6630d725170685c0447bd4282902c19e/Task3/PCA.png" width="250"/> | <img src="https://github.com/Skileated/SpectoV_Selection_Tasks/blob/0311789c6630d725170685c0447bd4282902c19e/Task3/t-SNE.png" width="250"/> | <img src="https://github.com/Skileated/SpectoV_Selection_Tasks/blob/0311789c6630d725170685c0447bd4282902c19e/Task3/t-SNE_200.png" width="250"/> |

> 💡 t-SNE provides more detailed local clustering than PCA, though it requires careful tuning.

---

## 📚 Key Learnings

- PCA is efficient and captures overall variance but may miss nonlinear relationships.
- t-SNE reveals complex local patterns and clusters but is sensitive to parameters.
- Both are valuable tools for visualizing and interpreting high-dimensional data.

---

## ▶️ How to Run

Install required libraries:

```bash
pip install numpy matplotlib seaborn scikit-learn
```
Run the script:

```bash
python Task3/dimensionality_reduction.py
```
Adjust the number of iterations or perplexity in t-SNE for different visualizations.
---
