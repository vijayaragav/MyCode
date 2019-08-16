import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
iris = load_iris()



df = pd.DataFrame(iris.data, columns=iris.feature_names)
dir(iris)
df['target'] = iris.target
#df.head()

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(df.drop(['target'], axis='columns'), df['target'], test_size=0.2)

model = RandomForestClassifier(n_estimators=10)
model.fit(X_train, Y_train)
model.score(X_test, Y_test)
Y_predict = model.predict(X_test)





from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_predict)

#seaborn

import matplotlib.pyplot as plt
import seaborn as sb
plt.figure(figsize=(6,5))
sb.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('True')