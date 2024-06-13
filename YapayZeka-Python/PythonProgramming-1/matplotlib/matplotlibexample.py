# Matplotlib library is used for data visualization
# Line plot, scatter plot, bar plot, subplots, histogram

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# Get the directory where the file is located
current_directory = os.path.dirname(__file__)

print(current_directory)

# File name and path
file_path = os.path.join(current_directory, 'iris.csv')

# Read the CSV file
df = pd.read_csv(file_path)

# Check the data
print(df.head())


# Display basic information about the dataset
print(df.columns)
print(df.Species.unique())
print(df.info())
print(df.describe())

# Separate data for each species
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

# Line plot
plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label="setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm,
         color="green", label="versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm,
         color="blue", label="virginica")
plt.legend()
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.show()

# Line plot using DataFrame
df.drop(["Id"], axis=1).plot(grid=True, alpha=0.9)
plt.show()

# Scatter plot
plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm,
            color="red", label="setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm,
            color="green", label="versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm,
            color="blue", label="virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")
plt.show()

# Histogram
plt.hist(setosa.PetalLengthCm, bins=50)
plt.xlabel("PetalLengthCm values")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

# Bar plot
x = np.array([1, 2, 3, 4, 5, 6, 7])
a = ["turkey", "usa", "a", "b", "v", "d", "s"]
y = x * 2 + 5
plt.bar(a, y)
plt.title("Bar Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Subplots
df.drop(["Id"], axis=1).plot(grid=True, alpha=0.9, subplots=True)
plt.show()

# Multiple subplots
plt.subplot(2, 1, 1)
plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label="setosa")
plt.ylabel("setosa - PetalLengthCm")
plt.subplot(2, 1, 2)
plt.plot(versicolor.Id, versicolor.PetalLengthCm,
         color="green", label="versicolor")
plt.ylabel("versicolor - PetalLengthCm")
plt.show()
