# 1) Pandas is fast and efficient for dataframes.
# 2) It can open and examine CSV and text files and easily save results to these file types.
# 3) Pandas helps us handle missing data efficiently.
# 4) Reshape data for more effective use.
# 5) Easy slicing and indexing.
# 6) Very helpful for time series data analysis.
# 7) Most importantly, it's optimized for speed.

import numpy as np
import pandas as pd

dictionary = {"NAME": ["ramiz", "taner", "semih", "arda", "rs2", "mavi"],
              "AGE": [15, 16, 17, 33, 45, 66],
              "SALARY": [100, 150, 240, 350, 110, 220]}

dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head()
tail = dataFrame1.tail()

# Pandas basic methods

print("Columns:", dataFrame1.columns)

print("\nInfo:")
print(dataFrame1.info())

print("\nData Types:")
print(dataFrame1.dtypes)

print("\nDescription:")
print(dataFrame1.describe())  # Numeric features = columns (age, SALARY)

# Indexing and slicing

print("\nAge column:")
print(dataFrame1["AGE"])
print("\nAge column alternative:")
print(dataFrame1.AGE)

print("\nLocation-based indexing:")
print(dataFrame1.loc[:, "AGE"])
print("\nLocation-based slicing:")
print(dataFrame1.loc[:3, "AGE":"NAME"])
print("\nLocation-based selection:")
print(dataFrame1.loc[:3, ["AGE", "NAME"]])

print("\nReverse order:")
print(dataFrame1.loc[::-1, :])

print("\nColumn range:")
print(dataFrame1.loc[:, :"NAME"])

print("\nSingle column:")
print(dataFrame1.loc[:, "NAME"])

print("\nIndex-based selection:")
print(dataFrame1.iloc[:, 2])

# Filtering

filter1 = dataFrame1.SALARY > 200
filtered_data = dataFrame1[filter1]

filter2 = dataFrame1.AGE < 20
print(dataFrame1[filter1 & filter2])

# List comprehension

average_salary = dataFrame1.SALARY.mean()

dataFrame1["salary_level"] = ["low" if average_salary >
                              each else "high" for each in dataFrame1.SALARY]

# For loop equivalent:
for each in dataFrame1.SALARY:
    if average_salary > each:
        print("low")
    else:
        print("high")

# Column operations

dataFrame1.columns

dataFrame1.columns = [each.lower() for each in dataFrame1.columns]

dataFrame1.columns = [each.split()[0] + "_" + each.split()[1] if (len(each.split()) > 1) else each for each in
                      dataFrame1.columns]

# Drop and concatenation
# dataFrame1.drop(["new_feature"], axis=1, inplace=True)
# dataFrame1 = dataFrame1.drop(["new_feature"], axis=1)

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

# Vertical concatenation
data_concat = pd.concat([data1, data2], axis=0)

# Horizontal concatenation
salary = dataFrame1.salary
age = dataFrame1.age
data_h_concat = pd.concat([salary, age], axis=1)

# Transforming data
dataFrame1["list_comp"] = [each * 2 for each in dataFrame1.age]

# Apply method


def multiply(age):
    return age * 2


dataFrame1["apply_method"] = dataFrame1.age.apply(multiply)
