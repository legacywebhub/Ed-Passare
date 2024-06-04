# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:14:08 2024

@author: Paulson
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:55:48 2024

@author: Paulson
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('icecream_dataset.csv') #.read_excel()
x = dataset.iloc[:, 1].values.reshape(-1, 1)
y = dataset.iloc[:, -1].values.reshape(-1, 1)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Training the Multiple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(x_test)

# Predicting for a single value
new_value = np.array([[70]])  # The value should be in a 2D array
new_pred = regressor.predict(new_value)

# Determining the accuracy of the model
regressor.score(x, y)

# Plotting the Training set results
plt.figure(figsize=(10, 6))
plt.scatter(x_train, y_train, color='red', label='Training data')
plt.plot(x_train, regressor.predict(x_train), color='blue', label='Regression line')
plt.title('Temperature vs Ice Cream Sales (Training set)')
plt.xlabel('Temperature')
plt.ylabel('Ice Cream Sales')
plt.legend()
plt.show()

# Plotting the Test set results
plt.figure(figsize=(10, 6))
plt.scatter(x_test, y_test, color='green', label='Test data')
plt.plot(x_train, regressor.predict(x_train), color='blue', label='Regression line')
plt.scatter(x_test, y_pred, color='orange', label='Predicted data')
plt.title('Temperature vs Ice Cream Sales (Test set)')
plt.xlabel('Temperature')
plt.ylabel('Ice Cream Sales')
plt.legend()
plt.show()