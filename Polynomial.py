import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
ds = pd.read_csv('C:\\Users\\HP\\Downloads\\Dataset\\position_Salaries.csv')
#print(ds)

x = ds.iloc[:,1:2].values
y = ds.iloc[:,2].values

reg=PolynomialFeatures(degree=5)
x_poly = reg.fit_transform(x)
#print(x_poly)
from sklearn.linear_model import LinearRegression
reg2=LinearRegression()
reg2=reg2.fit(x_poly,y)
y_predict = reg2.predict(x_poly)
z = reg2.predict(reg.fit_transform([[7.5]]))
print(z)
plt.scatter(x,y,color='red')
plt.scatter(7.5, z, color='green')
plt.plot(x, y_predict, color='blue')
plt.title('Polynomial Regression')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()