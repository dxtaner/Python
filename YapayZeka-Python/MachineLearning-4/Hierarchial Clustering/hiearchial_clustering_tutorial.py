import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering

# %% Create dataset

# Class 1
x1 = np.random.normal(25, 5, 100)
y1 = np.random.normal(25, 5, 100)

# Class 2
x2 = np.random.normal(55, 5, 100)
y2 = np.random.normal(60, 5, 100)

# Class 3
x3 = np.random.normal(55, 5, 100)
y3 = np.random.normal(15, 5, 100)

x = np.concatenate((x1, x2, x3), axis=0)
y = np.concatenate((y1, y2, y3), axis=0)

data = pd.DataFrame({"x": x, "y": y})

# Plot the data
plt.scatter(x1, y1, color="black", label="Class 1")
plt.scatter(x2, y2, color="black", label="Class 2")
plt.scatter(x3, y3, color="black", label="Class 3")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot of Classes")
plt.legend()
plt.show()

# %% Dendrogram

# Perform hierarchical clustering
merg = linkage(data, method="ward")

# Plot dendrogram
dendrogram(merg, leaf_rotation=90)
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.title("Dendrogram")
plt.show()

# %% Hierarchical Clustering (HC)

# Fit the model
hiyerartical_cluster = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage="ward")
cluster = hiyerartical_cluster.fit_predict(data)

# Add cluster labels to data
data["label"] = cluster

# Plot the clustered data
plt.scatter(data.x[data.label == 0], data.y[data.label == 0], color="red", label="Cluster 1")
plt.scatter(data.x[data.label == 1], data.y[data.label == 1], color="green", label="Cluster 2")
plt.scatter(data.x[data.label == 2], data.y[data.label == 2], color="blue", label="Cluster 3")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Clusters")
plt.legend()
plt.show()

# Round the data to 2 decimal places and save
data = data.round(2)
data.to_csv("clustered_data.csv", index=False)
