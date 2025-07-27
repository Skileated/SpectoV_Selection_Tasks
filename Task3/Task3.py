import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

# === Load dataset ===
digits = load_digits()
X = digits.data     # 64 features (8x8 image pixels)
y = digits.target   # Labels (0–9)

# === Normalize the data ===
X_scaled = StandardScaler().fit_transform(X)

# === PCA ===
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# === t-SNE ===
tsne = TSNE(n_components=2, perplexity=90, learning_rate=500, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)

# === Plotting Function ===
def plot_2D(X_red, labels, title):
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X_red[:, 0], X_red[:, 1], c=labels, cmap='tab10', s=15)
    plt.legend(*scatter.legend_elements(), title="Classes", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title(title)
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# === Visualize Results ===
plot_2D(X_pca, y, "PCA (2D Projection of Digits)")
plot_2D(X_tsne, y, "t-SNE (2D Projection of Digits)")
