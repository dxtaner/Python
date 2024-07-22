import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("multiple-linear-regression-dataset.csv", sep=";")

X = df.iloc[:, [0, 2]].values
y = df['maas'].values.reshape(-1, 1)

multiple_linear_regression = LinearRegression()
multiple_linear_regression.fit(X, y)

intercept = f"{multiple_linear_regression.intercept_[0]:.2f}"
coefficients = ", ".join(
    [f"{coef[0]:.2f}" for coef in multiple_linear_regression.coef_])

print("Kesişim Noktası (Intercept):", intercept)
print("Koefisiyentler (b1, b2):", coefficients)

example_data = np.array([[10, 35], [5, 35]])
predictions = multiple_linear_regression.predict(example_data)

print("\nTahminler:")
for i, (input_data, prediction) in enumerate(zip(example_data, predictions), start=1):
    print(
        f"Örnek {i} - Girdi: {input_data}, Tahmin Edilen Maaş: {prediction[0]:.2f}")

with open("multiple_linear_regression_results.txt", "w") as f:
    f.write(f"Kesişim Noktası (Intercept): {intercept}\n")
    f.write(f"Koefisiyentler (b1, b2): {coefficients}\n\n")
    f.write("Tahminler:\n")
    for i, (input_data, prediction) in enumerate(zip(example_data, predictions), start=1):
        f.write(
            f"Örnek {i} - Girdi: {input_data}, Tahmin Edilen Maaş: {prediction[0]:.2f}\n")

print("\nSonuçlar 'multiple_linear_regression_results.txt' dosyasına kaydedildi.")
