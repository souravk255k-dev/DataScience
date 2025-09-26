import pandas as pd 
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_csv("your_dataset.csv")   # Change file name
print("Dataset Head:\n", df.head(), "\n")
print("Missing Values:\n", df.isnull().sum(), "\n")

# -----------------------------
# 2. Handle categorical data (if any)
# -----------------------------
for col in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# -----------------------------
# 3. Select features for clustering
# -----------------------------
# Example: using last two columns for 2D plotting
X = df.iloc[:, [-2, -1]].values    
print("Selected Features:\n", X[:5], "\n")

# -----------------------------
# 4. Elbow Method to find optimal k
# -----------------------------
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS (Inertia)')
plt.show()

# -----------------------------
# 5. Apply KMeans with chosen k
# -----------------------------
k = 3   # <-- change based on Elbow Method
kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
Y = kmeans.fit_predict(X)

# -----------------------------
# 6. Visualize clusters
# -----------------------------
plt.figure(figsize=(8, 6))
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'orange', 'purple', 'brown', 'pink', 'gray']

for cluster in range(k):
    plt.scatter(X[Y == cluster, 0], X[Y == cluster, 1], 
                s=50, c=colors[cluster], label=f'Cluster {cluster+1}')

# Plot centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            s=300, c='yellow', marker='*', label='Centroids')

plt.title("KMeans Clustering Visualization")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
