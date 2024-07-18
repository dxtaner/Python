import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# %% Import data
data = pd.read_csv("data.csv")
data.drop(["id", "Unnamed: 32"], axis=1, inplace=True)

# %% Encode diagnosis column (M -> 1, B -> 0)
data.diagnosis = data.diagnosis.apply(lambda x: 1 if x == "M" else 0)

# Split the data into features (x) and target (y)
y = data.diagnosis.values
x_data = data.drop(["diagnosis"], axis=1)

# %% Normalize the feature data
x = (x_data - x_data.min()) / (x_data.max() - x_data.min())

# %% Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=42)

# %% Train the Random Forest model
rf = RandomForestClassifier(n_estimators=100, random_state=1)
rf.fit(x_train, y_train)
print("Random Forest algorithm result:", rf.score(x_test, y_test))

# Make predictions
y_pred = rf.predict(x_test)
y_true = y_test

# %% Confusion matrix
cm = confusion_matrix(y_true, y_pred)
print(cm)

# %% Confusion matrix visualization
f, ax = plt.subplots(figsize=(5, 5))
sns.heatmap(cm, annot=True, linewidths=0.5, linecolor="red", fmt=".0f", ax=ax)
plt.xlabel("y_pred")
plt.ylabel("y_true")
plt.show()

# %% Round the data to 2 decimal places and save
processed_data = pd.concat([x, pd.Series(y, name='diagnosis')], axis=1)
processed_data = processed_data.round(2)
processed_data.to_csv("processed_data.csv", index=False)
