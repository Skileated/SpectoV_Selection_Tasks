import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# === Load and preprocess image ===
img = cv2.imread('IMG2.jpg')
if img is None:
    raise FileNotFoundError("Image not found. Please check the filename and path.")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
original_shape = img.shape  # ✅ Add this line

# === Reshape the image to a 2D array of pixels ===
pixels = img.reshape((-1, 3))  # Each row is [R, G, B]

# === Apply KMeans clustering ===
k = 1000  # Number of color clusters
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(pixels)

# === Replace each pixel with its cluster center ===
segmented_pixels = kmeans.cluster_centers_[kmeans.labels_].astype('uint8')
segmented_img = segmented_pixels.reshape(original_shape)

# === Plot original and segmented images ===
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(segmented_img)
plt.title(f"KMeans Segmented (k={k})")
plt.axis("off")

plt.tight_layout()
plt.show()
