import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons
from sklearn.cluster import KMeans, DBSCAN

# === Generate datasets ===
X_blobs, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)
X_moons, _ = make_moons(n_samples=300, noise=0.05, random_state=42)

# === Apply KMeans ===
kmeans_blobs = KMeans(n_clusters=3, random_state=42)
labels_kmeans_blobs = kmeans_blobs.fit_predict(X_blobs)

kmeans_moons = KMeans(n_clusters=2, random_state=42)
labels_kmeans_moons = kmeans_moons.fit_predict(X_moons)

# === Apply DBSCAN ===
dbscan_blobs = DBSCAN(eps=1.2, min_samples=5)
labels_dbscan_blobs = dbscan_blobs.fit_predict(X_blobs)

dbscan_moons = DBSCAN(eps=0.2, min_samples=5)
labels_dbscan_moons = dbscan_moons.fit_predict(X_moons)

# === Define reusable plotting function ===
def plot_clusters(X, labels, title, ax):
    ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=40, edgecolors='k')
    ax.set_title(title)
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")
    ax.grid(True)

# === Plot all results ===
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

plot_clusters(X_blobs, labels_kmeans_blobs, "KMeans on Blobs", axs[0, 0])
plot_clusters(X_blobs, labels_dbscan_blobs, "DBSCAN on Blobs", axs[0, 1])
plot_clusters(X_moons, labels_kmeans_moons, "KMeans on Moons", axs[1, 0])
plot_clusters(X_moons, labels_dbscan_moons, "DBSCAN on Moons", axs[1, 1])

plt.tight_layout()
plt.show()
