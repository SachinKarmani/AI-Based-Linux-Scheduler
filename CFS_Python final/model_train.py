from sklearn.preprocessing import LabelEncoder
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
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
"""
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(Y)
y_inv = sc_y.inverse_transform(y_train)
pickle.dump(sc_X, open('final_model.sav', 'wb'))
pickle.dump(sc_y, open('final_model.sav', 'wb'))
"""

# Fitting Decision Tree Regression to the dataset
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, Y)


pickle.dump(regressor,      open('final_model.sav', 'wb'))
pickle.dump(labelencoder_X, open('final_encod.sav', 'wb'))


