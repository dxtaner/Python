from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

iris = load_iris()
X = iris.data
y = iris.target

X = (X - np.min(X)) / (np.max(X) - np.min(X))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
accuracies = cross_val_score(estimator=knn, X=X_train, y=y_train, cv=10)
print("Ortalama doğruluk: ", np.mean(accuracies))
print("Ortalama standart sapma: ", np.std(accuracies))

knn.fit(X_train, y_train)
print("Test doğruluğu: ", knn.score(X_test, y_test))

grid = {"n_neighbors": np.arange(1, 50)}
knn_cv = GridSearchCV(KNeighborsClassifier(), grid, cv=10)
knn_cv.fit(X, y)

print("En iyi hiperparametre K: ", knn_cv.best_params_)
print("En iyi doğruluk (best score): ", knn_cv.best_score_)

X_logreg = X[:100, :]
y_logreg = y[:100]

grid = {"C": np.logspace(-3, 3, 7), "penalty": ["l1", "l2"]}
logreg = LogisticRegression(solver='liblinear')
logreg_cv = GridSearchCV(logreg, grid, cv=10)
logreg_cv.fit(X_logreg, y_logreg)

print("En iyi hiperparametreler: ", logreg_cv.best_params_)
print("Doğruluk: ", logreg_cv.best_score_)
