import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Load the dataset
df = pd.read_csv("random-forest-regression-dataset.csv", sep=";", header=None)

# Prepare the data
x = df.iloc[:, 0].values.reshape(-1, 1)  # Features
y = df.iloc[:, 1].values  # Target (reshape to 1D array)

# Create and fit the Random Forest Regressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(x, y)

# Predict the price for a specific level (7.8)
value = 7.8
predicted_price = rf.predict([[value]])
formatted_predicted_price = f"{predicted_price[0]:.2f}"
print(f"7.8 seviyesinde fiyatın ne kadar olduğu: {formatted_predicted_price}")

# Create a range of values for plotting
x_range = np.arange(min(x), max(x), 0.01).reshape(-1, 1)
y_pred = rf.predict(x_range)

# Visualize the results
plt.scatter(x, y, color="red", label="Veri")
plt.plot(x_range, y_pred, color="green", label="Random Forest Regression")
plt.xlabel("Tribun Level")
plt.ylabel("Ucret")
plt.title("Random Forest Regression")
plt.legend()
plt.savefig("random_forest_regression_plot.png")
plt.show()

# Save results to a text file
with open("random_forest_regression_results.txt", "w") as f:
    f.write(f"7.8 seviyesinde fiyatın tahmini: {formatted_predicted_price}\n")

print("\nSonuçlar 'random_forest_regression_results.txt' dosyasına kaydedildi.")
