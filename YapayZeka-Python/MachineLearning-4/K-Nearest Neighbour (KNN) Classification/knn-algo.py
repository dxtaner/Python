# KNN Algoritması Tutorial

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load the dataset
data = pd.read_csv("data.csv")

# Drop unnecessary columns
data.drop(["id", "Unnamed: 32"], axis=1, inplace=True)

# Display the last few rows of the dataset
print(data.tail())

# Mapping the diagnosis column: malignant (M) = 1, benign (B) = 0
data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"], axis=1)

# Normalize the features
x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data))

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=1)

# KNN Model
knn = KNeighborsClassifier(n_neighbors=3)  # k = 3
knn.fit(x_train, y_train)
prediction = knn.predict(x_test)

# Print the accuracy of the KNN model with k=3
print("3-nn score: {:.2f}".format(knn.score(x_test, y_test)))

# Find the optimal k value
score_list = []
for k in range(1, 15):
    knn2 = KNeighborsClassifier(n_neighbors=k)
    knn2.fit(x_train, y_train)
    score_list.append(knn2.score(x_test, y_test))

# Plot accuracy for different k values
plt.figure(figsize=(10, 6))
plt.plot(range(1, 15), score_list, marker='o')
plt.xlabel("K values")
plt.ylabel("Accuracy")
plt.title("K-Nearest Neighbors Accuracy vs K Value")
plt.grid(True)
plt.savefig("knn_accuracy_vs_k.png")
plt.show()

# Save the accuracy scores to a text file
with open("knn_accuracy_scores.txt", "w") as f:
    for k, score in zip(range(1, 15), score_list):
        f.write(f"k={k}: Accuracy={score:.2f}\n")

print("\nSonuçlar 'knn_accuracy_scores.txt' dosyasına kaydedildi.")
