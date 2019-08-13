import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import load_iris
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

df['target'] = iris.target
#df['flower_names'] = df.target.apply(lambda x: iris.target_names[x])
#df.head()
df0 = df[df.target == 0]
df1 = df[df.target == 1]
df2 = df[df.target == 2]

#visualization of sepal length vs sepal Width
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'],color="red", marker='+')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'],color="blue", marker='.')
#plt.show()

#visualization of Petal length vs Pepal Width
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.scatter(df0['petal length (cm)'], df0['petal width (cm)'],color="red", marker='+')
plt.scatter(df1['petal length (cm)'], df1['petal width (cm)'],color="blue", marker='.')
#plt.show()

X = df.drop(['target'], axis='columns')
Y = df.target


#train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.2)

#SVM
model = SVC(C=3)
model.fit(X_train, Y_train)
model.score(X_test, Y_test)

#predict
model.predict([[4.5,3.1,1.3,0.5]])
