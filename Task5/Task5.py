import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# === Load image ===
img = cv2.imread('IMG2.jpg')
original = img.copy()

# === Resize for faster processing ===
img = cv2.resize(img, (256, 256))
original = cv2.resize(original, (256, 256))

# === Reshape and normalize ===
Z = img.reshape((-1, 3))
Z = np.float32(Z)

# === KMeans clustering ===
k = 5
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
labels = kmeans.fit_predict(Z)
centers = np.uint8(kmeans.cluster_centers_)
segmented_data = centers[labels.flatten()]
segmented_img = segmented_data.reshape((img.shape))

# === Convert to grayscale for contour detection ===
gray = cv2.cvtColor(segmented_img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# === Find contours ===
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# === Draw bounding boxes on original image ===
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w > 10 and h > 10:  # Skip tiny regions
        cv2.rectangle(original, (x, y), (x + w, y + h), (0, 255, 0), 2)

# === Display using matplotlib ===
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original with Cluster Boxes")
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Segmented Image")
plt.imshow(cv2.cvtColor(segmented_img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()
