import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# === Load sensor features ===
features = pd.read_csv("UCI HAR Dataset/train/X_train.txt", delim_whitespace=True, header=None)
print("Loaded data shape:", features.shape)

# Optional: reduce size for fast testing
# features = features.sample(1000, random_state=42)

# === Normalize ===
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# === Apply Clustering ===
kmeans = KMeans(n_clusters=6, random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)

dbscan = DBSCAN(eps=2.0, min_samples=10)
dbscan_labels = dbscan.fit_predict(X_scaled)

# === Dimensionality Reduction for Visualization ===
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# === Plot Clusters ===
def plot_clusters(X_red, labels, title):
    plt.figure(figsize=(8, 6))
    plt.scatter(X_red[:, 0], X_red[:, 1], c=labels, cmap='tab10', s=10)
    plt.title(title)
    plt.xlabel("PC 1")
    plt.ylabel("PC 2")
    plt.grid(True)
    plt.show()

plot_clusters(X_pca, kmeans_labels, "KMeans Clustering (PCA Projection)")
plot_clusters(X_pca, dbscan_labels, "DBSCAN Clustering (PCA Projection)")
