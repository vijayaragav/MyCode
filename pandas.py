import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
df = pd.read_csv("C:\\Users\\HP\\Downloads\\Dataset\winequality-red.csv", index_col=0)
ds = df.head(5)
dsu = ds.reindex(columns=["volatile acidity", 'citric acid'])
dsu.plot(kind='bar')
plt.show()

