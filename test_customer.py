import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
customer_data = pd.read_csv("Mall_Customers.csv", encoding='latin1')
print(customer_data.head())
print(customer_data.isnull().sum())

# Encode categorical data if needed (Gender is categorical, but we don't use it here)
le = LabelEncoder()

# Select features: Annual Income and Spending Score
X = customer_data.iloc[:, [3, 4]].values
print(X)

# ---- Elbow Method to find optimal clusters ----
wcss = []  
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)                 
    wcss.append(kmeans.inertia_)  

plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS (Inertia)')
plt.show()

# ---- Apply KMeans with optimal number of clusters (k=5 from Elbow) ----
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
Y = kmeans.fit_predict(X)

# ---- Visualize the clusters ----
plt.figure(figsize=(8, 8))

# Cluster 1
plt.scatter(X[Y == 0, 0], X[Y == 0, 1], s=50, c='blue', label='Cluster 1')

# Cluster 2
plt.scatter(X[Y == 1, 0], X[Y == 1, 1], s=50, c='green', label='Cluster 2')

# Cluster 3
plt.scatter(X[Y == 2, 0], X[Y == 2, 1], s=50, c='red', label='Cluster 3')

# Cluster 4
plt.scatter(X[Y == 3, 0], X[Y == 3, 1], s=50, c='cyan', label='Cluster 4')

# Cluster 5
plt.scatter(X[Y == 4, 0], X[Y == 4, 1], s=50, c='magenta', label='Cluster 5')

# Plot Centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            s=300, c='yellow', marker='*', label='Centroids')

plt.title("Customer Segments (KMeans Clustering)")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()
