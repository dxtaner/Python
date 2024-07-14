import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import csv

df = pd.read_csv("linear-regression-dataset.csv", sep=";")

plt.scatter(df['deneyim'], df['maas'])
plt.xlabel("Deneyim")
plt.ylabel("Maaş")
plt.title("Deneyim vs. Maaş")
plt.show()

linear_reg = LinearRegression()

X = df['deneyim'].values.reshape(-1, 1)
y = df['maas'].values.reshape(-1, 1)

linear_reg.fit(X, y)

b0 = linear_reg.predict([[0]])[0][0]
print("b0: ", b0)

b0_ = linear_reg.intercept_[0]
print("b0_ (Intercept): ", b0_)

b1 = linear_reg.coef_[0][0]
print("b1 (Slope): ", b1)

new_experience = 11
maas_yeni = b0_ + b1 * new_experience
print(f"{new_experience} yıl deneyim için tahmin edilen maaş: {maas_yeni}")

model_prediction = linear_reg.predict([[11]])[0][0]
print("11 yıl deneyim için model tahmini: ", model_prediction)

array = np.arange(0, 16).reshape(-1, 1)

plt.scatter(X, y, label="Veri")
plt.plot(array, linear_reg.predict(array),
         color="red", label="Regresyon Çizgisi")
plt.xlabel("Deneyim")
plt.ylabel("Maaş")
plt.title("Deneyim vs. Maaş ve Regresyon Çizgisi")
plt.legend()
plt.show()

high_experience_prediction = linear_reg.predict([[100]])[0][0]
print("100 yıl deneyim için tahmin: ", high_experience_prediction)

with open('regression_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Experience (Years)', 'Predicted Salary'])
    writer.writerow([0, b0])
    writer.writerow([new_experience, maas_yeni])
    writer.writerow([100, high_experience_prediction])
    writer.writerow(['Intercept', b0_])
    writer.writerow(['Slope', b1])
    writer.writerow(['Model prediction for 11 years', model_prediction])
