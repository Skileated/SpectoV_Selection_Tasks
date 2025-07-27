# 🖼️ Task 5: Image Segmentation

## 📌 Objective

The goal of this task is to apply basic **image segmentation** techniques on a given input image to identify and separate distinct regions based on color, intensity, or texture.

---

## 📊 Problem Statement

Given an input image (`IMG2.jpg`), the task is to segment the image into meaningful regions using clustering-based segmentation techniques. The output should highlight how the algorithm groups pixels into clusters representing different segments.

---

## 🛠️ Technologies Used

- Python 3.8+
- `numpy`
- `opencv-python`
- `matplotlib`
- `sklearn` (for clustering)

---

## ⚙️ Methods Overview

### 🔹 Image Preprocessing
- Load and resize image
- Convert color spaces if required (e.g., RGB → Lab or HSV)

### 🔹 Segmentation Technique
- Flatten image to 2D (pixels × channels)
- Apply **K-Means clustering** to segment based on pixel similarity
- Reshape segmented output to original image shape

---

## 📁 Files Included

```text
Task5/
├── Task5.py              # Main script
├── IMG2.jpg              # Input image
├── Segmented Image.png   # Output after segmentation
└── README.md             # This file
```
## 🖼️ Sample Output

| Original Image | Segmented Output |
|----------------|------------------|
| <img src="https://github.com/Skileated/SpectoV_Selection_Tasks/blob/b33db69c9768f8be6fa4dc0586636cffdd904e95/Task5/IMG2.jpg" width="300"/> | <img src="https://github.com/Skileated/SpectoV_Selection_Tasks/blob/b33db69c9768f8be6fa4dc0586636cffdd904e95/Task5/Segmented%20Image.png" width="300"/> |

---

## 📚 Key Learnings

- **Image segmentation** simplifies the representation of an image to make it more meaningful and easier to analyze.
- **K-Means clustering** is a fast and effective way to segment images based on pixel color similarity.
- **Preprocessing steps** like resizing and color space conversion significantly impact results.

---

## ▶️ How to Run

### Install dependencies:

```bash
pip install numpy opencv-python matplotlib scikit-learn
```
Run the script:

```bash
python Task5.py
```
---
