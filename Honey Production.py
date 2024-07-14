# Honey Production

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

honey = pd.read_csv('honeyproduction.csv')

#NOTE: Inspect the honeyproduction.csv file.
#print(honey.head())
#print(honey.info())
#print(honey.isnull())
#print(honey.nunique())

#NOTE: Calculate the mean of the totalprod  column per year.
prod_per_year = honey.groupby("year").totalprod.mean().reset_index()
#print("This is the mean calculation for the total production of honeybees per year:")
#print(prod_per_year)

#NOTE: Create two variables from the prod_per_year DataFrame. 
x = prod_per_year["year"]
x = x.values.reshape(-1, 1)

y = prod_per_year["totalprod"]
y = y.values.reshape(-1, 1)

#print(x)
#print(y)

#NOTE: Plot the x and y variables to see the relation ship between year and totalprod. 

plt.scatter(x, y)
#plt.show()
plt.clf()
plt.close()

#NOTE: Create a linear regression model and fit the model.

regr = linear_model.LinearRegression()
regr.fit(x, y)

#print("These are the slope from the linear model:")
#print(regr.coef_[0])
#print(regr.intercept_[0])

#NOTE: Make a list to get the predictions from the regr.

y_predict = regr.predict(x)
#print(y_predict)

#NOTE: We need to create a new plot to see our prediction working.

plt.plot(x, y_predict)
#plt.show()
plt.clf()
plt.close()

#NOTE: 

x_future = np.array(range(2013, 2050))
x_future = x_future.reshape(-1, 1)
print(x_future)

future_predict = regr.predict(x_future)

plt.plot(x_future, future_predict)
plt.show()
plt.clf()
plt.close()