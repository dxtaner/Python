import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# %% Import data
df = pd.read_csv("random-forest-regression-dataset.csv", sep=";", header=None)

# %% Split data into features (x) and target (y)
x = df.iloc[:, 0].values.reshape(-1, 1)
y = df.iloc[:, 1].values.reshape(-1, 1)

# %% Train the Random Forest Regressor model
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(x, y.ravel())  # Flatten y to 1D array

# %% Predict using the trained model
y_head = rf.predict(x)

# %% Evaluate the model
print("R^2 score:", r2_score(y, y_head))

# %% Visualize the results
plt.scatter(x, y, color="red", label="Data Points")
plt.plot(x, y_head, color="green", label="Random Forest Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Random Forest Regression")
plt.legend()
plt.show()
