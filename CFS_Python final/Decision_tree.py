# Decision Tree Regression

# Importing the libraries
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_excel('alldata_1.xlsx')
X = dataset.iloc[:, 1:].values
Y = dataset.iloc[:, 0].values


if "name" in list(dataset.columns):
    labelencoder_X = LabelEncoder()
    X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

# Splitting the dataset into the Training set and Test set

Y = Y.reshape(-1,1)
from sklearn.preprocessing import StandardScaler

#sc_X = StandardScaler()
#X_train = sc_X.fit_transform(X)
#sc_y = StandardScaler()
#y_train = sc_y.fit_transform(Y)


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# Feature Scaling

# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, Y)


# Predicting a new result
y_pred = regressor.predict(X_test)
y_test = y_test.reshape(14, )

print(abs(y_pred-y_test) * 100 / y_test)

