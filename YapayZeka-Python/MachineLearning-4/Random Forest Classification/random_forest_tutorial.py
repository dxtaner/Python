import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

#%% Load Data
data = pd.read_csv("data.csv")
data.drop(["id", "Unnamed: 32"], axis=1, inplace=True)

#%% Encode Diagnosis Column
data['diagnosis'] = data['diagnosis'].apply(lambda x: 1 if x == "M" else 0)
y = data['diagnosis'].values
x_data = data.drop(["diagnosis"], axis=1)

#%% Normalize Data
x = (x_data - x_data.min()) / (x_data.max() - x_data.min())

#%% Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=42)

#%% Decision Tree Classifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(x_train, y_train)
dt_score = dt.score(x_test, y_test)
print("Decision Tree Accuracy: {:.2f}%".format(dt_score * 100))

#%% Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(x_train, y_train)
rf_score = rf.score(x_test, y_test)
print("Random Forest Accuracy: {:.2f}%".format(rf_score * 100))
