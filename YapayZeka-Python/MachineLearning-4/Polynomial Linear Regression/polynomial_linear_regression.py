import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("polynomial-regression.csv", sep=";")

x = df['araba_fiyat'].values.reshape(-1, 1)
y = df['araba_max_hiz'].values.reshape(-1, 1)

plt.scatter(x, y)
plt.xlabel("Araba Fiyat")
plt.ylabel("Araba Max Hız")
plt.title("Araba Fiyat vs Max Hız")
plt.savefig("scatter_plot.png")
plt.show()

lr = LinearRegression()
lr.fit(x, y)

y_pred_linear = lr.predict(x)
plt.scatter(x, y, color='blue', label='Data')
plt.plot(x, y_pred_linear, color='red', label='Linear Regression')
plt.xlabel("Araba Fiyat")
plt.ylabel("Araba Max Hız")
plt.title("Linear Regression")
plt.legend()
plt.savefig("linear_regression_plot.png")
plt.show()

price = 10000000
predicted_speed = lr.predict([[price]])
formatted_predicted_speed = f"{predicted_speed[0][0]:.2f}"

with open("regression_results.txt", "w") as f:
    f.write(
        f"10 milyon TL'lik araba hız tahmini: {formatted_predicted_speed}\n")

poly_features = PolynomialFeatures(degree=2)
x_poly = poly_features.fit_transform(x)

poly_reg = LinearRegression()
poly_reg.fit(x_poly, y)

y_pred_poly = poly_reg.predict(x_poly)
plt.scatter(x, y, color='blue', label='Data')
plt.plot(x, y_pred_poly, color='green',
         label='Polynomial Regression (degree=2)')
plt.xlabel("Araba Fiyat")
plt.ylabel("Araba Max Hız")
plt.title("Polynomial Regression")
plt.legend()
plt.savefig("polynomial_regression_plot.png")
plt.show()

intercept = f"{poly_reg.intercept_[0]:.2f}"
coefficients = ", ".join([f"{coef:.2f}" for coef in poly_reg.coef_[0]])

with open("polynomial_regression_coefficients.txt", "w") as f:
    f.write("Polynomial Regression Coefficients:\n")
    f.write(f"Intercept (b0): {intercept}\n")
    f.write(f"Coefficients (b1, b2): {coefficients}\n")
