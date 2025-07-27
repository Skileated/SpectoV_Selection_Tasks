# 🧠 Task 1: Clustering with K-Means and DBSCAN

## 📌 Objective

The goal of this task is to apply and compare **K-Means** and **DBSCAN** clustering algorithms on a 2D dataset. The task demonstrates the practical strengths and limitations of both algorithms in different data distributions.

---

## 📊 Problem Statement

Given a 2D synthetic dataset with clusters of varying densities and shapes, we aim to:

- Apply **K-Means clustering** and observe how it performs on non-spherical data.
- Apply **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** and evaluate its robustness to outliers and shape flexibility.
- Visualize the differences in clustering performance using scatter plots.
- Evaluate how hyperparameters affect the outcome (e.g., `eps`, `min_samples`, `n_clusters`).

---

## 🛠️ Technologies Used

- Python 3.8+
- `numpy`, `matplotlib`, `seaborn`
- `scikit-learn`

---

## 🧪 Algorithms Overview

### 🔹 K-Means
- Centroid-based algorithm.
- Assumes spherical clusters of similar size.
- Sensitive to initialization and number of clusters.

### 🔹 DBSCAN
- Density-based clustering.
- Handles noise and non-spherical shapes well.
- Requires tuning of `eps` and `min_samples`.

---

## 📁 Files Included

```text
Task1/
├── kmeans_dbscan_comparison.py   # Main script to run clustering and plots
├── Dataset.png                   # Pre-generated synthetic data 
├── DBSCAN vs KMEANS.png          # Output plot
└── README.md                     # This file
```
