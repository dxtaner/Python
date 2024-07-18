# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load and preprocess data
data = pd.read_csv("data.csv")
data.drop(["Unnamed: 32", "id"], axis=1, inplace=True)
data.diagnosis = data.diagnosis.map({'M': 1, 'B': 0})

# Extract features and labels
y = data.diagnosis.values
x_data = data.drop(["diagnosis"], axis=1)

# Normalize features
x = (x_data - x_data.min()) / (x_data.max() - x_data.min())

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

x_train = x_train.T
x_test = x_test.T
y_train = y_train.T
y_test = y_test.T

print(f"x_train: {x_train.shape}")
print(f"x_test: {x_test.shape}")
print(f"y_train: {y_train.shape}")
print(f"y_test: {y_test.shape}")

# Initialize weights and bias
def initialize_weights_and_bias(dimension):
    w = np.full((dimension, 1), 0.01)
    b = 0.0
    return w, b

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Forward and backward propagation
def forward_backward_propagation(w, b, x_train, y_train):
    # Forward propagation
    z = np.dot(w.T, x_train) + b
    y_head = sigmoid(z)
    loss = -y_train * np.log(y_head) - (1 - y_train) * np.log(y_head)
    cost = np.sum(loss) / x_train.shape[1]
    
    # Backward propagation
    derivative_weight = np.dot(x_train, (y_head - y_train).T) / x_train.shape[1]
    derivative_bias = np.sum(y_head - y_train) / x_train.shape[1]
    gradients = {"derivative_weight": derivative_weight, "derivative_bias": derivative_bias}
    
    return cost, gradients

# Update weights and bias
def update(w, b, x_train, y_train, learning_rate, num_iterations):
    cost_list = []
    cost_list2 = []
    index = []
    
    for i in range(num_iterations):
        cost, gradients = forward_backward_propagation(w, b, x_train, y_train)
        cost_list.append(cost)
        
        w -= learning_rate * gradients["derivative_weight"]
        b -= learning_rate * gradients["derivative_bias"]
        
        if i % 10 == 0:
            cost_list2.append(cost)
            index.append(i)
            print(f"Cost after iteration {i}: {cost:.6f}")
            
    parameters = {"weight": w, "bias": b}
    
    plt.plot(index, cost_list2)
    plt.xticks(index, rotation='vertical')
    plt.xlabel("Number of Iterations")
    plt.ylabel("Cost")
    plt.show()
    
    return parameters, gradients, cost_list

# Predict function
def predict(w, b, x_test):
    z = sigmoid(np.dot(w.T, x_test) + b)
    Y_prediction = np.zeros((1, x_test.shape[1]))
    
    for i in range(z.shape[1]):
        Y_prediction[0, i] = 1 if z[0, i] > 0.5 else 0
    
    return Y_prediction

# Logistic regression model
def logistic_regression(x_train, y_train, x_test, y_test, learning_rate, num_iterations):
    dimension = x_train.shape[0]
    w, b = initialize_weights_and_bias(dimension)
    
    parameters, gradients, cost_list = update(w, b, x_train, y_train, learning_rate, num_iterations)
    
    y_prediction_test = predict(parameters["weight"], parameters["bias"], x_test)
    
    print(f"Test accuracy: {100 - np.mean(np.abs(y_prediction_test - y_test)) * 100:.2f} %")
    
# Train and evaluate the logistic regression model
logistic_regression(x_train, y_train, x_test, y_test, learning_rate=1, num_iterations=300)

# Logistic regression with sklearn
lr = LogisticRegression()
lr.fit(x_train.T, y_train.T)
print(f"Sklearn test accuracy: {lr.score(x_test.T, y_test.T):.2f}")
