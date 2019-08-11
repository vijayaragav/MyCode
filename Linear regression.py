import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
df = pd.read_csv('C:\\Users\HP\\Downloads\\Dataset\\headbrain.csv')
X = df['Head Size(cm^3)'].values
Y = df['Brain Weight(grams)'].values
m = len(X)
X = X.reshape((m, 1))

reg = LinearRegression()
rega = reg.fit(X, Y)
Y_pred = rega.predict(X)
Z = rega.predict([[4502]])
print(Z)
import matplotlib.pyplot as plt
plt.plot(X, Y_pred, color='red')
plt.scatter(4502, Z, color='yellow')
plt.scatter(X, Y, color='Blue')
plt.title('Headbrain')
plt.xlabel('Head size')
plt.ylabel('Brainweight')
plt.show()

r2_score = reg.score(X, Y)
print(r2_score)