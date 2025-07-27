# 🧠 Task 4: Clustering on UCI HAR Dataset using PCA + K-Means & DBSCAN

## 📌 Objective

This task focuses on applying unsupervised learning algorithms — **K-Means** and **DBSCAN** — to the **UCI Human Activity Recognition (HAR)** dataset after reducing its dimensionality using **Principal Component Analysis (PCA)**.

---

## 📊 Problem Statement

Given the high-dimensional sensor readings from the UCI HAR dataset:

- Perform **dimensionality reduction** using PCA to enable visualization and efficient clustering.
- Apply **K-Means** and **DBSCAN** to uncover hidden structures or clusters.
- Compare the clustering outcomes visually in 2D.
- Analyze the effectiveness of each method in separating activity types.

---

## 🛠️ Technologies Used

- Python 3.8+
- `numpy`, `matplotlib`, `seaborn`
- `scikit-learn`
- `pandas`

---

## ⚙️ Methods Overview

### 🔹 PCA (Principal Component Analysis)
- Reduces dimensionality while preserving variance.
- Used here to project high-dimensional data to 2D.

### 🔹 K-Means Clustering
- Groups data into `k` clusters using distance from centroids.
- Assumes roughly spherical clusters.

### 🔹 DBSCAN (Density-Based Spatial Clustering)
- Groups points based on density of data.
- Effective for noise handling and arbitrary-shaped clusters.

---

## 📁 Files Included
```text
Task4/
├── Task4.py # Main script
├── UCI_HAR_Dataset/ # Extracted dataset files
├── UCI_HAR_Dataset.zip # Dataset archive
├── KMeans Clustering (PCA Projection).png # KMeans output plot
├── DBSCAN Clustering (PCA Projection).png # DBSCAN output plot
└── README.md # This file
```

---

## 🖼️ Sample Output

| K-Means (PCA Projection) | DBSCAN (PCA Projection) |
|--------------------------|--------------------------|
| <img src="https://github.com/Skileated/SpectoV_Selection_Tasks/blob/2cf2ce14c72d4c30e5da0ec69844bcc8539707ae/Task4/KMeans%20Clustering%20(PCA%20Projection).png" width="300"/> | <img src="https://github.com/Skileated/SpectoV_Selection_Tasks/blob/2cf2ce14c72d4c30e5da0ec69844bcc8539707ae/Task4/DBSCAN%20Clustering%20(PCA%20Projection).png" width="300"/> |

---

## 📚 Key Learnings

- **PCA** enables visualization of complex high-dimensional data.
- **K-Means** is efficient but may fail on non-spherical or overlapping data.
- **DBSCAN** handles noise well and detects clusters of various shapes.
- Cluster separability varies with algorithm choice and dataset properties.

---

## ▶️ How to Run

Install dependencies:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```
Extract the dataset and run the script:

```bash
unzip UCI_HAR_Dataset.zip
python Task4.py
```
---
