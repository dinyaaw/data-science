# -*- coding: utf-8 -*-
"""Linear Regression from scratch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XhdyWxOMxbsttklu1AW6mqvZz7HFinjW
"""

# Libraries
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Use only one feature
diabetes_X = diabetes_X[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[-30:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes_y[:-30]
diabetes_y_test = diabetes_y[-30:]

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regression.predict(diabetes_X_test)

# Commented out IPython magic to ensure Python compatibility.
# The coefficients
print('Coefficients: ', regression.coef_)
print('Intercept: ', regression.intercept_)

# calculate these metrics by hand!
from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(diabetes_y_test, diabetes_y_pred))
print('MSE:', metrics.mean_squared_error(diabetes_y_test, diabetes_y_pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(diabetes_y_test, diabetes_y_pred)))

# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
#       % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.show()