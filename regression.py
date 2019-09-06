"""
This Document was created by Ahmad ASMANDAR ON 04.09.2019
and is being used to learn data-science with Python
"""
# Addieren von Regression Möglichkeit

# Here is the USED libs pandas, matplotlib...
import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt

# add the linear Regression Model to the Program
# install the new sklearn lib Scikit-Learn
from sklearn.linear_model import LinearRegression
# I assigned the LinearRegerssion cLASS TO lg Object so i can use it simply
lg= LinearRegression()
# read csv file using pandas

data = pd.read_csv("data.csv")
# use datframes from pandas to extract data from tables

X = df(data, columns=['production_budget_usd'])
y = df(data, columns=['worldwide_gross_usd'])

#### Slope Coefficient
#  h(x)=theta0 +theta1 * X
lg.fit(X,y)
print(lg.coef_ ) # theta 1
inter=lg.intercept_ #theta 0
print(inter)

######### use matplot lib to visualise our data

# set the figure size
plt.figure(figsize=(10, 6))

# the data to plot, using the scatter plot function
# and using the alpha parameter to determine the destiny of the Data in a point
plt.scatter(X, y, alpha=0.4)
plt.plot(X, lg.predict(X), color="r",linewidth=4)
# the labels to title,x and y labels
plt.title("first data-science panda example")
plt.xlabel('production_budget_usd')
plt.ylabel('world_wide_gross')


plt.xlim(0, )
plt.ylim(0, )
plt.show()
################