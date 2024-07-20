import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# %% Create dataset

# Class 1
x1 = np.random.normal(25, 5, 1000)
y1 = np.random.normal(25, 5, 1000)

# Class 2
x2 = np.random.normal(55, 5, 1000)
y2 = np.random.normal(60, 5, 1000)

# Class 3
x3 = np.random.normal(55, 5, 1000)
y3 = np.random.normal(15, 5, 1000)

x = np.concatenate((x1, x2, x3), axis=0)
y = np.concatenate((y1, y2, y3), axis=0)

data = pd.DataFrame({"x": x, "y": y})

# %% Plot the data
plt.scatter(x1, y1, color="black", label="Class 1")
plt.scatter(x2, y2, color="black", label="Class 2")
plt.scatter(x3, y3, color="black", label="Class 3")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot of Classes")
plt.legend()
plt.show()

# %% KMeans Algorithm

# Determine the optimal number of clusters using the elbow method
wcss = []

for k in range(1, 15):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)

# Plot the elbow graph
plt.plot(range(1, 15), wcss)
plt.xlabel("Number of Clusters (k)")
plt.ylabel("WCSS")
plt.title("Elbow Method for Optimal k")
plt.show()

# %% KMeans with k=3

# Fit the model with k=3
kmeans2 = KMeans(n_clusters=3)
clusters = kmeans2.fit_predict(data)

# Add cluster labels to data
data["label"] = clusters

# Plot the clustered data
plt.scatter(data.x[data.label == 0], data.y[data.label == 0], color="red", label="Cluster 1")
plt.scatter(data.x[data.label == 1], data.y[data.label == 1], color="green", label="Cluster 2")
plt.scatter(data.x[data.label == 2], data.y[data.label == 2], color="blue", label="Cluster 3")
plt.scatter(kmeans2.cluster_centers_[:, 0], kmeans2.cluster_centers_[:, 1], color="yellow", marker="*", s=200, label="Centroids")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("KMeans Clustering with k=3")
plt.legend()
plt.show()

# Round the data to 2 decimal places and save
data = data.round(2)
data.to_csv("kmeans_clustered_data.csv", index=False)
