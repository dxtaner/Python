import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# %% Load data
data = pd.read_csv("data.csv")

# %% Preprocess data
data.drop(["id", "Unnamed: 32"], axis=1, inplace=True)

# Encode diagnosis column
data.diagnosis = data.diagnosis.map({'M': 1, 'B': 0})

# Separate features and labels
y = data.diagnosis.values
x_data = data.drop(["diagnosis"], axis=1)

# Normalize features
x = (x_data - x_data.min()) / (x_data.max() - x_data.min())

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

# %% Visualize data
M = data[data.diagnosis == 1]
B = data[data.diagnosis == 0]
plt.scatter(M.radius_mean, M.texture_mean, color="red", label="Malignant", alpha=0.3)
plt.scatter(B.radius_mean, B.texture_mean, color="green", label="Benign", alpha=0.3)
plt.xlabel("Radius Mean")
plt.ylabel("Texture Mean")
plt.legend()
plt.show()

# %% Train SVM classifier
svm = SVC(random_state=1)
svm.fit(x_train, y_train)

# %% Test and evaluate the model
y_pred = svm.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of SVM classifier: {accuracy:.2f}")

# Detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# %% Optional: Visualize the decision boundary (if possible)
# Note: Visualization of decision boundaries is often done in 2D for simplicity.
# Here, we will use only the first two features for visualization.

def plot_decision_boundary(clf, X, y):
    # Define bounds of the domain
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    # Predict class using data and classifier
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Create a contour plot
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k')
    plt.show()

# Use only the first two features for decision boundary visualization
svm_2d = SVC(random_state=1)
svm_2d.fit(x_train.iloc[:, :2], y_train)

plt.title("SVM Decision Boundary")
plot_decision_boundary(svm_2d, x_test.iloc[:, :2].values, y_test)
plt.xlabel("Radius Mean")
plt.ylabel("Texture Mean")

