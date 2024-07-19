# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# %% Import data
df = pd.read_csv("linear-regression-dataset.csv", sep=";")

# %% Plot data
plt.scatter(df.deneyim, df.maas, color="blue", label="Data Points")
plt.xlabel("Deneyim (Yıl)")
plt.ylabel("Maaş (TL)")
plt.title("Deneyim ve Maaş İlişkisi")
plt.legend()
plt.show()

# %% Linear Regression
# Create linear regression model
linear_reg = LinearRegression()

# Split the data into features (x) and target (y)
x = df.deneyim.values.reshape(-1, 1)
y = df.maas.values.reshape(-1, 1)

# Train the model
linear_reg.fit(x, y)

# Make predictions
y_head = linear_reg.predict(x)

# Plot the linear regression line
plt.scatter(df.deneyim, df.maas, color="blue", label="Data Points")
plt.plot(x, y_head, color="red", label="Linear Regression Line")
plt.xlabel("Deneyim (Yıl)")
plt.ylabel("Maaş (TL)")
plt.title("Deneyim ve Maaş İlişkisi")
plt.legend()
plt.show()

# %% Evaluate the model
r2 = r2_score(y, y_head)
print("R^2 score:", r2)
