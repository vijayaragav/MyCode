import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_csv('C:\\Users\HP\\Downloads\\Dataset\\headbrain.csv')
X = df['Head Size(cm^3)'].values
Y = df['Brain Weight(grams)'].values
m = len(X)
X = X.reshape((m, 1))

reg = LinearRegression()
reg = reg.fit(X, Y)
Y_pred = reg.predict(X)

r2_score = reg.score(X, Y)
print(r2_score)