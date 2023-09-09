# -*- coding: utf-8 -*-
"""outgoing time prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A0rBLW7MWyq0kldt1-h8xjjICgyay8lp
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

dataset = pd.read_excel('DAIICT Hackathon Data.xlsx', sheet_name='Past In and Out Container Data')
dataset = dataset.dropna()

x = dataset.iloc[:, [1, 4, 5]].values
y = dataset.iloc[:,[-1,-3]].values
# print(type(y[0][0]))

timestt = x[:,0]
dates = [ts.timestamp() for ts in timestt]
print(dates)

# Replace the first column with the extracted dates
x[:, 0] = dates

print(x)



timestt2 = y[:,0]
dates2 = []
# dates2 = [float(datetime.strptime(str(ts), "%Y-%m-%d %H:%M:%S.%f").timestamp()) for ts in timestt2]
for ts in timestt2:
  try:
    dates2.append(float(datetime.strptime(str(ts), "%Y-%m-%d %H:%M:%S.%f").timestamp()))
  except ValueError:
    dates2.append(float(datetime.strptime(str(ts), "%Y-%m-%d %H:%M:%S").timestamp()))
y[:, 0] = dates2

print(y)

x20 = np.empty_like(x)
x40 = np.empty_like(x)
y20 = np.empty_like(y)
y40 = np.empty_like(y)

x20 = x[x[:, 1] == 20.0]
x40 = x[x[:, 1] == 40.0]


y20 = y[y[:, 1] == 20.0]
y40 = y[y[:, 1] == 40.0]

# Create a dictionary to map labels to numerical values
label_map = {'E': 0, 'L': 1}

# Apply the mapping to the labels column
x20[:, -1] = [label_map[label] for label in x20[:, -1]]
x40[:, -1] = [label_map[label] for label in x40[:, -1]]

print(x20)

y20 = np.delete(y20, 1, axis=1)
print(y20)



# print(len(x20))
# print(len(y20))
# print(len(x))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x20, y20, test_size = 1/2, random_state = 0)

print(X_train)

print()

print(X_test)

print(y_train)

print(y_test)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

print(len(X_train))

print(len(y_train))

from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()

scx20 = sc_X.fit_transform(x20)
scy20 = sc_y.fit_transform(y20)
regressor = SVR(kernel = 'rbf')
regressor.fit(scx20, scy20)