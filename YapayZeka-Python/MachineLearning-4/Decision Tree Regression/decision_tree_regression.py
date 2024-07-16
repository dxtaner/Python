from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("decision-tree-regression-dataset.csv", sep=";", header=None)

# Prepare the data
x = df.iloc[:, 0].values.reshape(-1, 1)  # Features
y = df.iloc[:, 1].values.reshape(-1, 1)  # Target

# Create and fit the decision tree regressor
tree_reg = DecisionTreeRegressor(random_state=0)
tree_reg.fit(x, y)

# Make a prediction for a specific value
value = 5.5
predicted_value = tree_reg.predict([[value]])

# Ensure predicted_value is treated as a 1D array
if isinstance(predicted_value, np.ndarray):
    predicted_value = predicted_value.flatten()

formatted_predicted_value = f"{predicted_value[0]:.2f}"
print(
    f"Tahmin Edilen Değer (tribun level = {value}): {formatted_predicted_value}")

# Create a range of values for plotting
x_range = np.arange(min(x), max(x), 0.01).reshape(-1, 1)
y_pred = tree_reg.predict(x_range)

# Visualize the results
plt.scatter(x, y, color="red", label="Veri")
plt.plot(x_range, y_pred, color="green", label="Decision Tree Regression")
plt.xlabel("Tribun Level")
plt.ylabel("Ucret")
plt.title("Decision Tree Regression")
plt.legend()
plt.savefig("decision_tree_regression_plot.png")
plt.show()

# Save results to a text file
with open("decision_tree_regression_results.txt", "w") as f:
    f.write(
        f"Tahmin Edilen Değer (tribun level = {value}): {formatted_predicted_value}\n")

print("\nSonuçlar 'decision_tree_regression_results.txt' dosyasına kaydedildi.")
